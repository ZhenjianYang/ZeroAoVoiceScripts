from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r2040.bin",                # FileName
        "r2040",                    # MapName
        "r2040",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2040", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 1, 0, 2],
    )

    BuildStringList((
        "r2040",                  # 0
        "br2000",                 # 1
        "br2000",                 # 2
        "br2000",                 # 3
        "克洛斯贝尔市·矿山镇玛因兹方向",# 4
        "人偶工房方向",           # 5
    ))

    ATBonus("ATBonus_2F4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_C95", 10,  2,   0,   4,   0,   5,   2)
    Sepith("Sepith_C7D", 4,   0,   1,   10,  5,   3,   0)

    MonsterBattlePostion("MonsterBattlePostion_354", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_334", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 0, 0, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_3F4", 0x0010, 14, 6, 90, 0, 1, 5, 0, "br2000", "Sepith_C95", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
        )
    )

    BattleInfo(
        "BattleInfo_4BC", 0x0000, 14, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_C7D", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
        )
    )

    BattleInfo(
        "BattleInfo_584", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64301.dat", "ms64301.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_3B4", "ed7401", "ed7403", "ATBonus_2F4"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

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
        "monster/ch77450.itc",               # 10
        "monster/ch77450.itc",               # 11
        "monster/ch65550.itc",               # 12
        "monster/ch65551.itc",               # 13
        "monster/ch64350.itc",               # 14
        "monster/ch64350.itc",               # 15
    ))

    DeclMonster(12080,   52050,   17990,   0x1010000,    "BattleInfo_3F4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(10960,   58330,   18000,   0x1010000,    "BattleInfo_4BC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(50640,   68970,   26000,   0x1010000,    "BattleInfo_3F4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(43200,   97050,   30000,   0x1010000,    "BattleInfo_4BC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(17560,   116590,  30000,   0x1010000,    "BattleInfo_3F4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(70050,   122300,  40000,   0x1010000,    "BattleInfo_3F4", 0,   16,  0xFFFF, 2,  3)
    DeclMonster(-1580,   77570,   23000,   0x18500B4,    "BattleInfo_584", 0,   20,  0xFFFF, 4,  5)

    DeclEvent(0x0040, 0, 7,   -1.5800000429153442,   77.56999969482422,     22.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   0.19750000536441803,   -9.696249961853027,    -5.5,                  1.0])

    DeclActor(16000,   30000,   114000,  1200,    16000,   31000,   114000,  0x007C, 0,  3,  0x0000)
    DeclActor(18000,   30000,   114000,  1200,    18000,   31000,   114000,  0x007C, 0,  4,  0x0000)
    DeclActor(16410,   18000,   53460,   1200,    16410,   18000,   53460,   0x007C, 0,  5,  0x0000)
    DeclActor(57110,   36000,   119510,  1200,    57110,   36000,   119510,  0x007C, 0,  6,  0x0000)

    PlaceName(-3.25, 0.0, -1.25, 0x0000, 0x0000, "克洛斯贝尔市·矿山镇玛因兹方向")
    PlaceName(81.0, 0.0, 161.5, 0x0000, 0x0000, "人偶工房方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 5

    ScpFunction((
        "Function_0_630",          # 00, 0
        "Function_1_64D",          # 01, 1
        "Function_2_64E",          # 02, 2
        "Function_3_797",          # 03, 3
        "Function_4_8CD",          # 04, 4
        "Function_5_A03",          # 05, 5
        "Function_6_A17",          # 06, 6
        "Function_7_A2B",          # 07, 7
    ))


    def Function_0_630(): pass

    label("Function_0_630")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64C")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_630")

    label("loc_64C")

    Return()

    # Function_0_630 end

    def Function_1_64D(): pass

    label("Function_1_64D")

    Return()

    # Function_1_64D end

    def Function_2_64E(): pass

    label("Function_2_64E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66B")
    SetChrFlags(0xE, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_67F")

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F")
    ClearChrFlags(0xE, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_67F")

    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0xE, 0x100)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AD")
    OP_70(0x0, 0x0)
    Jump("loc_6B1")

    label("loc_6AD")

    OP_70(0x0, 0x1E)

    label("loc_6B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C4")
    OP_70(0x1, 0x0)
    Jump("loc_6C8")

    label("loc_6C4")

    OP_70(0x1, 0x1E)

    label("loc_6C8")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 7)), scpexpr(EXPR_END)), "loc_72E")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 16410, 18000, 53460, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)
    Jump("loc_787")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 0)), scpexpr(EXPR_END)), "loc_787")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 57110, 36000, 119510, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_796")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_796")

    Return()

    # Function_2_64E end

    def Function_3_797(): pass

    label("Function_3_797")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_884")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅰ', 1)"), scpexpr(EXPR_END)), "loc_816")
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
    SetScenarioFlags(0x104, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_87F")

    label("loc_816")

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

    label("loc_87F")

    Jump("loc_8C1")

    label("loc_884")

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

    label("loc_8C1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_797 end

    def Function_4_8CD(): pass

    label("Function_4_8CD")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BA")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_94C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x104, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_9B5")

    label("loc_94C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_9B5")

    Jump("loc_9F7")

    label("loc_9BA")

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

    label("loc_9F7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_8CD end

    def Function_5_A03(): pass

    label("Function_5_A03")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 7)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_A03 end

    def Function_6_A17(): pass

    label("Function_6_A17")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_A17 end

    def Function_7_A2B(): pass

    label("Function_7_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 1)), scpexpr(EXPR_END)), "loc_A35")
    Return()

    label("loc_A35")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_B01"),
        (SWITCH_DEFAULT, "loc_B18"),
    )


    label("loc_B01")

    Sleep(500)
    OP_90(0x0, 0, 22000, 71920, 0)
    EventEnd(0x5)
    Return()

    label("loc_B18")

    Battle("BattleInfo_584", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(0, 23000, 71920, 0)
    OP_90(0x0, 0, 22000, 71920, 0)
    OP_90(0x1, 0, 22000, 71920, 0)
    OP_90(0x2, 0, 22000, 71920, 0)
    OP_90(0x3, 0, 22000, 71920, 0)
    OP_90(0x4, 0, 22000, 71920, 0)
    OP_90(0x5, 0, 22000, 71920, 0)
    OP_90(0x6, 0, 22000, 71920, 0)
    OP_90(0x7, 0, 22000, 71920, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_BDA"),
        (1, "loc_BDD"),
        (SWITCH_DEFAULT, "loc_BE0"),
    )


    label("loc_BDA")

    EventEnd(0x5)
    Return()

    label("loc_BDD")

    OP_B7(0x0)
    Return()

    label("loc_BE0")

    EventBegin(0x1)
    SetChrFlags(0xE, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x78, 1)
    OP_29(0xB, 0x4, 0x10)
    OP_29(0xB, 0x4, 0x2)
    OP_29(0xB, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_7_A2B end

    SaveToFile()

Try(main)
