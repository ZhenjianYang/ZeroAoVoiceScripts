from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m1140.bin",                # FileName
        "m1140",                    # MapName
        "m1140",                    # Location
        0x006E,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, -28000, -30000, 0, 0, 1, 110, 0, 1, 0, 2],
    )

    BuildStringList((
        "m1140",                  # 0
        "钢铁完全体",             # 1
        "bm1040",                 # 2
        "bm1040",                 # 3
        "bm1040",                 # 4
    ))

    ATBonus("ATBonus_24C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_23C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_851", 6,   6,   15,  9,   0,   0,   0)
    Sepith("Sepith_859", 4,   4,   0,   0,   9,   9,   9)

    MonsterBattlePostion("MonsterBattlePostion_29C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_300", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_304", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_308", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_30C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_310", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_314", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_27C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 3, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 12, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 0, 0, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_33C", 0x0000, 21, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_851", 60, 25, 10, 5,
        (
            ("ms65000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_29C", "MonsterBattlePostion_2FC", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_27C", "MonsterBattlePostion_2FC", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_29C", "MonsterBattlePostion_2FC", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms65000.dat", "ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, "MonsterBattlePostion_27C", "MonsterBattlePostion_2FC", "ed7400", "ed7403", "ATBonus_24C"),
        )
    )

    BattleInfo(
        "BattleInfo_404", 0x0000, 21, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_859", 60, 25, 10, 5,
        (
            ("ms62700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_29C", "MonsterBattlePostion_2FC", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms62700.dat", "ms62700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_27C", "MonsterBattlePostion_2FC", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_29C", "MonsterBattlePostion_2FC", "ed7400", "ed7403", "ATBonus_24C"),
            ("ms62700.dat", "ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, "MonsterBattlePostion_27C", "MonsterBattlePostion_2FC", "ed7400", "ed7403", "ATBonus_24C"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_4CC", 0x0000, 40, 6, 0, 0, 1, 0, 0, "bm1040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72900.dat", "ms72900.dat", "ms72900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_31C", "MonsterBattlePostion_2FC", "ed7401", "ed7403", "ATBonus_23C"),
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
        "monster/ch65050.itc",               # 10
        "monster/ch65050.itc",               # 11
        "monster/ch62750.itc",               # 12
        "monster/ch62750.itc",               # 13
        "monster/ch72950.itc",               # 14
        "monster/ch72951.itc",               # 15
    ))

    DeclNpc(0,       -27500,  23000,   0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(20770,   2670,    -28000,  0x1010000,    "BattleInfo_33C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(7940,    18540,   -29190,  0x1010000,    "BattleInfo_404", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-1260,   21090,   -29200,  0x1010000,    "BattleInfo_404", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-12520,  16300,   -29190,  0x1010000,    "BattleInfo_33C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-21210,  -550,    -28000,  0x1010000,    "BattleInfo_404", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4300,    4670,    -27200,  0x1010000,    "BattleInfo_33C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-7580,   4170,    -27200,  0x1010000,    "BattleInfo_404", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(320,     -6970,   -27200,  0x1010000,    "BattleInfo_404", 0,   18,  0xFFFF, 2,  3)

    DeclActor(0,       -29000,  23000,   1200,    0,       -28000,  23000,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_550",          # 00, 0
        "Function_1_56F",          # 01, 1
        "Function_2_570",          # 02, 2
        "Function_3_588",          # 03, 3
    ))


    def Function_0_550(): pass

    label("Function_0_550")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_550")

    label("loc_56E")

    Return()

    # Function_0_550 end

    def Function_1_56F(): pass

    label("Function_1_56F")

    Return()

    # Function_1_56F end

    def Function_2_570(): pass

    label("Function_2_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_583")
    OP_70(0x0, 0x0)
    Jump("loc_587")

    label("loc_583")

    OP_70(0x0, 0x1E)

    label("loc_587")

    Return()

    # Function_2_570 end

    def Function_3_588(): pass

    label("Function_3_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_617")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从宝箱中感觉到了高级魔兽的气息。\x01",
            "【推测魔兽等级４０】\x01",
            "要打开宝箱吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_617")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_617")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D3")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_710")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_670():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_670)

    def lambda_68A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_68A)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0002
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
    Battle("BattleInfo_4CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6F1"),
        (2, "loc_700"),
        (1, "loc_70D"),
        (SWITCH_DEFAULT, "loc_710"),
    )


    label("loc_6F1")

    SetScenarioFlags(0x72, 4)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_710")

    label("loc_700")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_70D")

    OP_B7(0x0)
    Return()

    label("loc_710")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x9C, 1)"), scpexpr(EXPR_END)), "loc_767")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11B, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_7CE")

    label("loc_767")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x9C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x9C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_7CE")

    Jump("loc_805")

    label("loc_7D3")

    FadeToDark(300, 0, 100)

    #A0005
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

    label("loc_805")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_588 end

    SaveToFile()

Try(main)
