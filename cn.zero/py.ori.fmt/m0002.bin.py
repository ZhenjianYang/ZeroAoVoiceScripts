from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m0002.bin",                # FileName
        "m0002",                    # MapName
        "m0002",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 4, 0, 5],
    )

    BuildStringList((
        "m0002",                  # 0
        "亚里欧斯",               # 1
        "随行人员１",             # 2
        "随行人员２",             # 3
        "随行人员１",             # 4
        "随行人员２",             # 5
        "随行人员２",             # 6
        "BOSS１",                 # 7
        "SE控制",                 # 8
        "bm0002",                 # 9
        "bm0002",                 # 10
        "bm0002",                 # 11
    ))

    ATBonus("ATBonus_290", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_390", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 4, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 12, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 2, 3, 90)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 14, 3, 270)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_334", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_338", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_33C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_340", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_344", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_348", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_350", 8, 9, 0)
    MonsterBattlePostion("MonsterBattlePostion_354", 5, 11, 45)
    MonsterBattlePostion("MonsterBattlePostion_358", 11, 11, 315)
    MonsterBattlePostion("MonsterBattlePostion_35C", 2, 13, 90)
    MonsterBattlePostion("MonsterBattlePostion_360", 14, 13, 270)
    MonsterBattlePostion("MonsterBattlePostion_364", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 3, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 13, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_438", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0002", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67000.dat", "ms61700.dat", "ms61700.dat", "ms61700.dat", "ms61700.dat", 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_330", "ed7401", "ed7403", "ATBonus_290"),
            (),
            (),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_3B0", 0x0002, 3, 6, 180, 0, 0, 0, 0, "bm0002", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73100.dat", "ms73100.dat", "ms73100.dat", "ms73100.dat", "ms73100.dat", 0, 0, 0, "MonsterBattlePostion_350", "MonsterBattlePostion_330", "ed7401", "ed7403", "ATBonus_290"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3F4", 0x0002, 3, 6, 180, 0, 0, 0, 0, "bm0002", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73100.dat", "ms73100.dat", "ms73100.dat", "ms73100.dat", "ms73100.dat", 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_330", "ed7401", "ed7403", "ATBonus_290"),
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
        "monster/ch67050.itc",               # 10
        "monster/ch67050.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       0,       0x18500B4,    "BattleInfo_438", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 6,   0.0,                   0.0,                   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  0.25,                  1.0])

    DeclActor(-220,    500,     13170,   1200,    -220,    2000,    13170,   0x007C, 0,  24, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(250, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_4FC",          # 00, 0
        "Function_1_51B",          # 01, 1
        "Function_2_537",          # 02, 2
        "Function_3_556",          # 03, 3
        "Function_4_573",          # 04, 4
        "Function_5_594",          # 05, 5
        "Function_6_70C",          # 06, 6
        "Function_7_BCF",          # 07, 7
        "Function_8_1609",         # 08, 8
        "Function_9_1676",         # 09, 9
        "Function_10_16BB",        # 0A, 10
        "Function_11_1700",        # 0B, 11
        "Function_12_1745",        # 0C, 12
        "Function_13_178A",        # 0D, 13
        "Function_14_17CF",        # 0E, 14
        "Function_15_1814",        # 0F, 15
        "Function_16_1867",        # 10, 16
        "Function_17_18BA",        # 11, 17
        "Function_18_1A6B",        # 12, 18
        "Function_19_1B06",        # 13, 19
        "Function_20_420F",        # 14, 20
        "Function_21_4265",        # 15, 21
        "Function_22_42BB",        # 16, 22
        "Function_23_42ED",        # 17, 23
        "Function_24_4338",        # 18, 24
        "Function_25_4363",        # 19, 25
    ))


    def Function_0_4FC(): pass

    label("Function_0_4FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_4FC")

    label("loc_51A")

    Return()

    # Function_0_4FC end

    def Function_1_51B(): pass

    label("Function_1_51B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_536")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_51B")

    label("loc_536")

    Return()

    # Function_1_51B end

    def Function_2_537(): pass

    label("Function_2_537")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_555")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_537")

    label("loc_555")

    Return()

    # Function_2_537 end

    def Function_3_556(): pass

    label("Function_3_556")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_572")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_3_556")

    label("loc_572")

    Return()

    # Function_3_556 end

    def Function_4_573(): pass

    label("Function_4_573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_584")
    Event(0, 7)

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_593")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 19)

    label("loc_593")

    Return()

    # Function_4_573 end

    def Function_5_594(): pass

    label("Function_5_594")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CE")
    SetMapObjFrame(0x0, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x0, "light00", 0x0, 0x1)
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    Jump("loc_5EB")

    label("loc_5CE")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)

    label("loc_5EB")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_606")
    OP_1B(0x1, 0x0, 0x19)

    label("loc_606")

    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F1")
    SetChrFlags(0x10, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_705")

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_705")
    ClearChrFlags(0x10, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_705")

    Sound(128, 1, 100, 0)
    Return()

    # Function_5_594 end

    def Function_6_70C(): pass

    label("Function_6_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 0)), scpexpr(EXPR_END)), "loc_716")
    Return()

    label("loc_716")

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

    #A0001
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
        (1, "loc_7E2"),
        (SWITCH_DEFAULT, "loc_7F9"),
    )


    label("loc_7E2")

    Sleep(500)
    OP_90(0x0, 40, 0, -8060, 0)
    EventEnd(0x5)
    Return()

    label("loc_7F9")

    Battle("BattleInfo_438", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(40, 1000, -8060, 0)
    OP_90(0x0, 40, 0, -8060, 0)
    OP_90(0x1, 40, 0, -8060, 0)
    OP_90(0x2, 40, 0, -8060, 0)
    OP_90(0x3, 40, 0, -8060, 0)
    OP_90(0x4, 40, 0, -8060, 0)
    OP_90(0x5, 40, 0, -8060, 0)
    OP_90(0x6, 40, 0, -8060, 0)
    OP_90(0x7, 40, 0, -8060, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_8BB"),
        (1, "loc_8BE"),
        (SWITCH_DEFAULT, "loc_8C1"),
    )


    label("loc_8BB")

    EventEnd(0x5)
    Return()

    label("loc_8BE")

    OP_B7(0x0)
    Return()

    label("loc_8C1")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1200, -1500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 0, 0, -2500, 0)
    SetChrPos(0x102, 1000, 0, -3750, 0)
    SetChrPos(0x103, -1000, 0, -3750, 0)
    SetChrPos(0x104, 0, 0, -5000, 0)
    SetChrFlags(0x10, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(0, 1200, -3750, 1500)
    FadeToBright(300, 0)

    def lambda_9A1():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A1)
    Sleep(50)

    def lambda_9B1():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B1)
    Sleep(50)

    def lambda_9C1():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)

    #C0003
    ChrTalk(
        0x101,
        "#0000F#5P好，总算是搞定了。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#0304F#12P不过，和那个叫亚里欧斯的\x01",
            "游击士打倒的那只相比，还是弱了一些啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#0102F#11P呵呵，不过，只要我们四人联手协力，\x01",
            "今后也一定可以克服任何困难呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#0204F#6P……是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0007
    ChrTalk(
        0x103,
        (
            "#0202F#6P刚才已经将深处大门\x01",
            "的门锁解除了。\x02\x03",

            "那里有返回地面的近路，\x01",
            "我们就走那边的通道吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0008
    ChrTalk(
        0x101,
        (
            "#0005F#5P啊，好的……\x01",
            "（哎，是什么时候解除的呢？）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, -2500, 0)
    OP_29(0x3D, 0x1, 0x4)
    SetScenarioFlags(0x78, 0)
    OP_29(0x35, 0x4, 0x10)
    OP_29(0x35, 0x4, 0x2)
    OP_29(0x35, 0x1, 0x0)
    SetMapObjFrame(0x0, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x0, "light00", 0x1, 0x1)
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFlags(0x0, 0x10)
    OP_1B(0x1, 0x0, 0x19)
    OP_65(0x0, 0x1)
    EventEnd(0x5)
    Return()

    # Function_6_70C end

    def Function_7_BCF(): pass

    label("Function_7_BCF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00152.itc", 0x26)
    LoadChrToIndex("monster/ch73150.itc", 0x27)
    LoadChrToIndex("monster/ch73151.itc", 0x28)
    LoadChrToIndex("monster/ch73153.itc", 0x29)
    OP_68(0, -3000, -17500, 0)
    MoveCamera(55, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    AddParty(0x97, 0xFF, 0xFF)
    SetChrPos(0x101, -700, -4000, -18200, 0)
    SetChrPos(0x102, 700, -4000, -18200, 0)
    SetChrPos(0x103, -700, -4000, -18200, 0)
    SetChrPos(0x104, 700, -4000, -18200, 0)
    SetChrPos(0x197, 0, -4000, -18200, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x197, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x198, 0, 0, -1000, 180)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0x9, 4800, 0, 1000, 270)
    SetChrPos(0xA, -4800, 0, 1000, 90)
    SetChrPos(0xB, 0, 0, -5500, 0)
    SetChrPos(0xC, 3400, 0, -3000, 315)
    SetChrPos(0xD, -3400, 0, -3000, 45)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    LoadEffect(0x0, "battle\\cr001000.eff")
    LoadEffect(0x1, "battle\\btgun00.eff")
    OP_68(0, -2000, -15500, 2000)
    SetCameraDistance(24000, 2000)
    FadeToBright(1000, 0)

    def lambda_E0F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E0F)

    def lambda_E20():
        OP_97(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E20)
    Sleep(150)

    def lambda_E3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E3D)

    def lambda_E4E():
        OP_97(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E4E)
    Sleep(500)

    def lambda_E6B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E6B)

    def lambda_E7C():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E7C)
    Sleep(150)

    def lambda_E99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E99)

    def lambda_EAA():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EAA)
    Sleep(500)

    def lambda_EC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_EC7)

    def lambda_ED8():
        OP_97(0xFE, 0x0, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_ED8)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    SetChrFlags(0x198, 0x4)
    SetChrPos(0x198, 0, 0, -1000, 180)

    #N0009
    NpcTalk(
        0x198,
        "男孩的声音",
        "别、别过来啊～！\x02",
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x198,
        "男孩的声音",
        (
            "哇哇，救命呀！\x01",
            "爱德丝女神～！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x5DC)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x198, 0x4)
    SetChrPos(0x198, 0, 0, -1000, 180)
    OP_68(0, 500, 0, 3000)
    MoveCamera(45, 22, 0, 3000)
    SetCameraDistance(22500, 3000)
    Sleep(500)
    PlayBGM("ed7511", 0)
    Sleep(500)
    BeginChrThread(0x198, 3, 0, 8)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x198, 3)
    Sleep(1000)
    OP_64(0x198)
    Fade(500)
    OP_68(0, -2000, -15500, 0)
    MoveCamera(55, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    OP_0D()

    #C0011
    ChrTalk(
        0x102,
        "#11P#0105F啊……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x197,
        "隆！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#12P#0013F（呜……！）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【直接向魔兽的背后突袭】\x01",        # 0
            "【将魔兽的注意力引向这边】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetScenarioFlags(0x41, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1130"),
        (1, "loc_12DC"),
        (SWITCH_DEFAULT, "loc_15F1"),
    )


    label("loc_1130")

    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0014
    ChrTalk(
        0x101,
        (
            "#12P#0007F──就这样直接突击！\x02\x03",

            "打魔兽一个措手不及，\x01",
            "并以保护孩子的安全为首要目标！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_0D()

    #C0015
    ChrTalk(
        0x104,
        "#11P#0307F收到！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        "#11P#0107F嗯！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 700, -4500, 1700)
    MoveCamera(50, 22, 0, 1700)
    SetCameraDistance(25000, 1700)

    def lambda_121B():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_121B)
    Sleep(50)

    def lambda_1238():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1238)
    Sleep(50)

    def lambda_1255():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1255)
    Sleep(50)

    def lambda_1272():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1272)
    Sleep(50)

    def lambda_128F():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_128F)
    Sleep(1500)
    OP_6F(0x79)
    Battle("BattleInfo_3B0", 0x30200011, 0x2, 0x0, 0x13, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x197, 0x1)
    Jump("loc_15F1")

    label("loc_12DC")

    TurnDirection(0x101, 0x102, 500)

    #C0017
    ChrTalk(
        0x101,
        (
            "#6P#0007F──艾莉！\x01",
            "吸引这些家伙的注意力！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    TurnDirection(0x102, 0x101, 500)

    #C0018
    ChrTalk(
        0x102,
        "#11P#0101F明白了……！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sleep(250)
    BeginChrThread(0x102, 3, 0, 17)
    WaitChrThread(0x102, 3)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 700, -6700, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    BeginChrThread(0x9, 3, 0, 15)
    BeginChrThread(0xA, 3, 0, 16)
    BeginChrThread(0xC, 3, 0, 14)
    BeginChrThread(0xD, 3, 0, 14)

    def lambda_13DD():
        OP_96(0xFE, 0x0, 0x0, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_13DD)

    def lambda_13F7():
        OP_97(0xFE, 0x0, 0x0, 0x189C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13F7)
    Sleep(50)

    def lambda_1414():
        OP_97(0xFE, 0x0, 0x0, 0x189C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1414)
    Sleep(50)

    def lambda_1431():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1431)
    Sleep(50)

    def lambda_144E():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_144E)
    WaitChrThread(0x197, 1)
    WaitChrThread(0x198, 1)

    #C0019
    ChrTalk(
        0x103,
        (
            "#12P#0201F……看来已经成功\x01",
            "让它们转移了注意力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#12P#0007F很好，解决它们吧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    BeginChrThread(0x9, 0, 0, 1)

    def lambda_1501():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1501)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    BeginChrThread(0xA, 0, 0, 1)

    def lambda_152E():
        OP_98(0xFE, 0xBB8, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_152E)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    BeginChrThread(0xB, 0, 0, 1)

    def lambda_155B():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_155B)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    BeginChrThread(0xC, 0, 0, 1)

    def lambda_1588():
        OP_98(0xFE, 0xFFFFFA24, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1588)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x20)
    BeginChrThread(0xD, 0, 0, 1)

    def lambda_15B5():
        OP_98(0xFE, 0x5DC, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_15B5)
    Sleep(500)
    Battle("BattleInfo_3F4", 0x30200011, 0x0, 0x0, 0x14, 0xFF)
    FadeToDark(0, 0, -1)
    CancelBlur(0)
    Jump("loc_15F1")

    label("loc_15F1")

    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    Call(0, 19)
    Return()

    # Function_7_BCF end

    def Function_8_1609(): pass

    label("Function_8_1609")

    BeginChrThread(0xB, 3, 0, 11)
    OP_63(0x198, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1626():
        OP_96(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_1626)
    WaitChrThread(0x198, 1)
    Sleep(1000)
    BeginChrThread(0x9, 3, 0, 9)
    BeginChrThread(0xC, 3, 0, 12)
    OP_93(0x198, 0x5A, 0x1F4)
    Sleep(1000)
    BeginChrThread(0xA, 3, 0, 10)
    BeginChrThread(0xD, 3, 0, 13)
    OP_93(0x198, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0x198, 0xB4, 0x1F4)
    Return()

    # Function_8_1609 end

    def Function_9_1676(): pass

    label("Function_9_1676")

    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_168E():
        OP_96(0xFE, 0xCE4, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_168E)
    WaitChrThread(0x9, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_9_1676 end

    def Function_10_16BB(): pass

    label("Function_10_16BB")

    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_16D3():
        OP_96(0xFE, 0xFFFFF31C, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16D3)
    WaitChrThread(0xA, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_10_16BB end

    def Function_11_1700(): pass

    label("Function_11_1700")

    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1718():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1718)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    Return()

    # Function_11_1700 end

    def Function_12_1745(): pass

    label("Function_12_1745")

    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_175D():
        OP_96(0xFE, 0x960, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_175D)
    WaitChrThread(0xC, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    Return()

    # Function_12_1745 end

    def Function_13_178A(): pass

    label("Function_13_178A")

    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_17A2():
        OP_96(0xFE, 0xFFFFF6A0, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_17A2)
    WaitChrThread(0xD, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    SetChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    Return()

    # Function_13_178A end

    def Function_14_17CF(): pass

    label("Function_14_17CF")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_17E7():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17E7)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_17CF end

    def Function_15_1814(): pass

    label("Function_15_1814")

    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1833():
        OP_98(0xFE, 0x514, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1833)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_15_1814 end

    def Function_16_1867(): pass

    label("Function_16_1867")

    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1886():
        OP_98(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1886)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_16_1867 end

    def Function_17_18BA(): pass

    label("Function_17_18BA")


    def lambda_18BF():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18BF)
    Sleep(500)
    Fade(250)
    OP_68(700, 700, -6000, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x9, 3300, 0, 0, 270)
    SetChrPos(0xA, -3300, 0, 0, 90)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    Sound(1104, 255, 100, 0)    #voice#Elie
    OP_A0(0x102, 1500, 0x0, 0x2)
    Sleep(200)
    Sound(530, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xB, 3, 0, 18)
    OP_A1(0x102, 0x7D0, 0x3, 0x3, 0x4, 0x0)
    Sleep(300)
    TurnDirection(0x102, 0x9, 500)
    Sound(1105, 255, 100, 0)    #voice#Elie
    OP_A0(0x102, 1500, 0x0, 0x2)
    Sleep(200)
    Sound(530, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xC, 3, 0, 18)
    OP_A1(0x102, 0x7D0, 0x3, 0x3, 0x4, 0x0)
    Sleep(300)
    TurnDirection(0x102, 0xA, 500)
    Sound(1106, 255, 100, 0)    #voice#Elie
    OP_A0(0x102, 1500, 0x0, 0x2)
    Sleep(200)
    Sound(530, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xD, 3, 0, 18)
    OP_A1(0x102, 0x7D0, 0x3, 0x3, 0x4, 0x0)
    Sleep(300)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_17_18BA end

    def Function_18_1A6B(): pass

    label("Function_18_1A6B")

    EndChrThread(0xFE, 0x0)

    def lambda_1A74():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A74)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 500, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_63(0xFE, 0x0, 1100, 0xC, 0xD, 0xFA, 0x2)
    OP_93(0xFE, 0xB4, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 0)
    Return()

    # Function_18_1A6B end

    def Function_19_1B06(): pass

    label("Function_19_1B06")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("monster/ch62350.itc", 0x26)
    LoadChrToIndex("monster/ch62352.itc", 0x27)
    LoadChrToIndex("chr/ch02400.itc", 0x28)
    LoadChrToIndex("apl/ch50007.itc", 0x29)
    LoadChrToIndex("apl/ch50540.itc", 0x2A)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(19000, 0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, 0, -2300, 180)
    SetChrPos(0x102, -2300, 0, 0, 270)
    SetChrPos(0x103, 2300, 0, 0, 90)
    SetChrPos(0x104, 0, 0, 2300, 0)
    SetChrPos(0x198, 500, 0, 0, 90)
    SetChrPos(0x197, -500, 0, 0, 270)
    LoadEffect(0x0, "event\\ev001_00.eff")
    LoadEffect(0x1, "event\\ev000_00.eff")
    LoadEffect(0x2, "event\\eva04_00.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01400.itp")
    SetCameraDistance(17000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0021
    ChrTalk(
        0x101,
        "#12P#0003F呼……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#6P#0106F总算是解决了呢……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#5P#0300F不过，还真是\x01",
            "费了一番工夫啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        "#11P#0206F……好累。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x198,
        "#5P吓、吓死我了……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    def lambda_1E1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E1C)
    Sleep(50)

    def lambda_1E2C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1E2C)
    Sleep(50)

    def lambda_1E3C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1E3C)
    Sleep(50)

    def lambda_1E4C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1E4C)
    Sleep(50)
    TurnDirection(0x197, 0x198, 500)

    #C0026
    ChrTalk(
        0x197,
        (
            "#6P隆，没事吧！？\x01",
            "没有受伤吧！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x198, 0x197, 500)

    #C0027
    ChrTalk(
        0x198,
        (
            "#11P嗯、嗯……\x01",
            "完全没事。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x198,
        (
            "#11P比起这个，你能平安无事\x01",
            "才真是万幸呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x198,
        (
            "#11P因为你的反应很迟钝啊～\x01",
            "我还在想，如果不赶快去救你，\x01",
            "你肯定就会被魔兽给吃掉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x197,
        (
            "#6P你、你还好意思这么说。\x01",
            "明明你自己也差一点\x01",
            "就要被魔兽吃掉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x197,
        (
            "#6P而且这次完全是你\x01",
            "强拉着我进来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x198,
        "#11P你、你在说什么啊！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x198,
        (
            "#11P最先说什么『地下空间』\x01",
            "的人不就是你吗～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x197,
        (
            "#6P可、可是我又没说\x01",
            "真的要进来……！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#0003F好啦好啦，\x01",
            "争吵就先到此为止吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2089():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_2089)
    Sleep(50)

    def lambda_2099():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_2099)
    WaitChrThread(0x198, 2)

    #C0036
    ChrTalk(
        0x197,
        "#1P对、对不起……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x198,
        (
            "#5P嘿～我好像是第一次见到\x01",
            "哥哥姐姐们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x198,
        (
            "#5P虽然看起来好像挺强的，\x01",
            "但还是新人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#5P#0306F真是的……\x01",
            "好一个嚣张的小鬼。\x02\x03",

            "#0301F我们可是救了你一命哦，\x01",
            "首先应该要道谢才对吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2194():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_2194)
    Sleep(500)

    #C0041
    ChrTalk(
        0x198,
        "#12P嘿嘿，算啦，谢谢你们救了我。\x02",
    )

    CloseMessageWindow()

    def lambda_21CA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_21CA)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_21F2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2219")

    label("loc_21F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_220F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2219")

    label("loc_220F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2219")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2235"),
        (1, "loc_22E3"),
        (2, "loc_237E"),
        (SWITCH_DEFAULT, "loc_2407"),
    )


    label("loc_2235")

    OP_2C(0x3C, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0042
    ChrTalk(
        0x198,
        (
            "#5P虽然情况很危险，\x01",
            "但我却毫发无伤哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x198,
        "#5P这样一看，你们也算是很厉害了吧？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#12P#0005F那还真是多谢夸奖了……\x02\x01",

            "#0012F不过，你果然挺嚣张的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2407")

    label("loc_22E3")

    OP_2C(0x3C, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x198,
        (
            "#5P虽然情况很危险，\x01",
            "但我只有一点轻微的擦伤而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x198,
        "#5P你们勉强算是表现合格了吧。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#12P#0002F哈哈……\x01",
            "我们会继续努力进步的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2407")

    label("loc_237E")


    #C0048
    ChrTalk(
        0x198,
        (
            "#5P不过，大哥哥，你们的\x01",
            "水平未免也太烂了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x198,
        "#5P我都以为自己要死掉了呢。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#12P#0006F……抱歉啊。\x01",
            "实在是让你受惊吓了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2407")

    label("loc_2407")


    #C0051
    ChrTalk(
        0x102,
        (
            "#6P#0104F呵呵，不过，没事就好啦。\x02\x03",

            "#0102F总之，我们就\x01",
            "赶快出去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    #C0052
    ChrTalk(
        0x103,
        (
            "#11P#0204F……是啊。\x01",
            "看起来，已经到了终点。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(300)

    #C0053
    ChrTalk(
        0x103,
        (
            "#11P#0202F赛尔盖科长交付的课题，\x01",
            "也应该算是完成了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#12P#0000F嗯……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        (
            "#5P#0306F不过，还真是完全没想到\x01",
            "会发生这种紧急状况啊。\x02\x03",

            "#0302F那么，先把小鬼们送回去，\x01",
            "然后再回警察局总部吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_255D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_255D)

    def lambda_256A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_256A)
    WaitChrThread(0x198, 2)
    OP_63(0x198, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x197, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x198)
    OP_64(0x197)

    #C0056
    ChrTalk(
        0x101,
        "#12P#0000F嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    def lambda_25C4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_25C4)

    def lambda_25D1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_25D1)
    WaitChrThread(0x198, 2)

    #C0057
    ChrTalk(
        0x198,
        "#5P那个……大哥哥。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x198,
        (
            "#5P你们应该\x01",
            "是新人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#12P#0005F啊……是这样的。\x02\x03",

            "#0000F不过，你是怎么知道的啊？\x01",
            "我们又没有穿着制服……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x198,
        "#5P制、制服……？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x197,
        "#1P那、那个～莫非。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x197,
        (
            "#1P大哥哥们……\x01",
            "并不是协会的人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0063
    ChrTalk(
        0x101,
        "#12P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#6P#0105F协会……\x01",
            "难道是指『游击士协会』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x198,
        (
            "#5P都说是协会了，\x01",
            "那还能有其它协会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x198,
        (
            "#5P哎，什么！？\x01",
            "你们真的不是游击士吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#12P#0012F不、不是……\x02\x03",

            "#0000F我们是克洛斯贝尔的警察，\x01",
            "虽然只是刚刚入职的新人……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0068
    ChrTalk(
        0x197,
        "#1P#4S哎……！？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x198,
        "#5P#4S警察吗！？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x198,
        (
            "#5P骗人的吧！\x01",
            "为什么警察局的警员\x01",
            "会来这种地方啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#12P#0003F啊，那个……\x01",
            "我们有点事情，所以才会来这里。\x02\x03",

            "然后在执行任务的途中\x01",
            "正好发现了你们。\x02\x03",

            "#0000F……不过，我们会在这里，\x01",
            "有那么不可思议吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x198,
        "#5P那当然啊！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x198,
        (
            "#5P因为，一说起警察，\x01",
            "那可是出了名的懦弱无能啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0074
    ChrTalk(
        0x101,
        "#12P#0011F#4S哎？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x198,
        (
            "#5P不仅态度傲慢无礼，\x01",
            "而且什么忙都帮不上，\x01",
            "爸爸就是这么说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x198,
        (
            "#5P在关键时刻，游击士\x01",
            "要比他们可靠几十倍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#12P#0005F………………………………\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x102,
        "#6P#0108F………果然…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x197, 0x198, 500)
    Sleep(300)

    #C0079
    ChrTalk(
        0x197,
        "#6P隆、隆，你太失礼啦。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x197,
        (
            "#6P虽然他们是警察，\x01",
            "但毕竟救了我们啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x198, 0x197, 500)

    #C0081
    ChrTalk(
        0x198,
        "#11P话、话是没错啦～\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x198,
        (
            "#11P本以为被游击士协会\x01",
            "的新人给救了，结果……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#5P#0305F嗯～？\x01",
            "心情好像很复杂嘛。\x02\x03",

            "#0301F……嗯………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)

    #C0084
    ChrTalk(
        0x104,
        "#5P#0307F喂，危险啊！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0xE, 0, 7000, -7000, 0)
    SetChrFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2C9E():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C9E)
    Sleep(100)

    def lambda_2CAE():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2CAE)

    def lambda_2CBB():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2CBB)

    #C0085
    ChrTalk(
        0x101,
        "#5P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#5P#0201F……！？\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        "#5P#0105F上面……！？\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1400, -7000, 1000)
    MoveCamera(43, 27, 0, 1000)
    SetCameraDistance(14000, 1000)
    Sleep(700)
    SetChrChip(0x0, 0xE, 0x1E, 0x64)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    Sound(812, 0, 100, 0)

    def lambda_2D5A():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0xA, 0x9C4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2D5A)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    SetCameraDistance(17000, 2000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x0, 0x2BC, 0xBB8, 0x7D0)
    Sound(813, 0, 100, 0)
    Sleep(2500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    Fade(500)
    CancelBlur(0)
    OP_68(100000, 1500, -7000, 0)
    MoveCamera(130, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrPos(0x101, 100000, 0, -2600, 180)
    SetChrPos(0x102, 97400, 0, 0, 180)
    SetChrPos(0x103, 102600, 0, 0, 180)
    SetChrPos(0x104, 100000, 0, 2400, 180)
    SetChrPos(0x198, 100500, 0, 0, 180)
    SetChrPos(0x197, 99500, 0, 0, 180)
    SetChrPos(0xE, 100000, 0, -7000, 0)
    ClearChrFlags(0xE, 0x1)
    SetChrChip(0x1, 0xE, 0x0, 0x0)
    OP_68(100000, 700, -4000, 2000)
    MoveCamera(140, 15, 0, 2000)
    SetCameraDistance(17500, 2000)
    OP_0D()
    Sleep(500)

    def lambda_2EAB():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EAB)
    Sleep(150)
    OP_63(0x197, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_2EDA():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_2EDA)
    Sleep(100)
    OP_63(0x198, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_2F09():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_2F09)
    OP_6F(0x79)

    #C0088
    ChrTalk(
        0x197,
        "#5P咦咦……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x198,
        "哇啊！？\x02",
    )

    CloseMessageWindow()
    OP_64(0x198)
    OP_64(0x197)

    #C0090
    ChrTalk(
        0x101,
        "#0010F#6P呜……！？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        "#0310F#6P这家伙是什么东西！？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        "#0107F#6P怎、怎么会如此巨大……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#0208F#6P……不妙。\x01",
            "背后的门上着锁。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#0013F#6P呜……这样下去的话……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    #C0095
    ChrTalk(
        0x104,
        (
            "#0307F#6P喂，你打算做什么！？\x02\x03",

            "就算想与它正面对抗，\x01",
            "凭现在的装备，也毫无胜算吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#0007F#5P我明白的！\x02\x03",

            "我来吸引这家伙的注意力，\x01",
            "大家先想办法逃出去！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3137():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3137)
    Sleep(50)

    def lambda_3147():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3147)
    WaitChrThread(0x103, 2)

    #C0097
    ChrTalk(
        0x102,
        "#12P#0101F等、等一下……！？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        "#0201F你是认真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#0007F#5P在这种情况下，\x01",
            "就只有这一个方法了！\x02\x03",

            "兰迪和艾莉\x01",
            "抱着那两个孩子，\x01",
            "努力找机会逃走！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0310F#6P可恶……\x01",
            "只能这样做了吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x197,
        "#5P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x198,
        "大、大哥哥……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 100000, 4000, -17700, 0)

    #N0103
    NpcTalk(
        0x8,
        "声音",
        "#3P──唉。\x02",
    )

    CloseMessageWindow()

    #N0104
    NpcTalk(
        0x8,
        "声音",
        (
            "#3P敢于自我牺牲的勇气值得肯定，\x01",
            "但这种决定未免太欠考虑了吧。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_336C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_336C)

    def lambda_3379():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3379)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 100000, 6000, -17700, 0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_68(100000, 6900, -17700, 2500)
    MoveCamera(152, 18, 0, 2500)
    SetCameraDistance(16000, 2500)
    OP_6F(0x79)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("男性")

    #A0105
    AnonymousTalk(
        0xFF,
        "…………………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)
    OP_68(100320, 1700, -6240, 1100)
    MoveCamera(127, 15, 0, 1100)
    OP_6E(600, 1100)
    SetCameraDistance(15000, 1100)
    PlayEffect(0x2, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_352D():
        OP_9D(0xFE, 0x186A0, 0x0, 0xFFFFEE6C, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_352D)
    BeginChrThread(0x8, 3, 0, 22)
    Sleep(900)
    Sound(815, 0, 100, 0)
    Sound(259, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xE, 0x0, 0, 1000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xE, 0x20)
    EndChrThread(0xE, 0x0)
    SetChrSubChip(0xE, 0x0)
    WaitChrThread(0x8, 1)
    PlayEffect(0x2, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x8, 3)
    Sleep(300)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    OP_6F(0x79)
    Sleep(1000)
    Sleep(300)

    #C0106
    ChrTalk(
        0x101,
        "#0005F#5P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_0D()
    Sleep(300)
    MoveCamera(130, 17, 0, 1500)
    SetCameraDistance(19500, 1500)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    SetChrFlags(0xE, 0x20)
    EndChrThread(0xE, 0x0)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)

    def lambda_3660():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3660)
    PlayEffect(0x0, 0xFF, 0xE, 0x0, 0, 1000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(816, 0, 100, 0)
    Sleep(500)

    def lambda_36B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_36B9)
    WaitChrThread(0xE, 2)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_6F(0x50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0107
    ChrTalk(
        0x101,
        "#0005F#5P#4S！！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(100000, 700, -6000, 0)
    MoveCamera(140, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_68(100000, 700, -4000, 2000)
    OP_6F(0x1)

    #C0108
    ChrTalk(
        0x104,
        "#0305F#6P真、真的假的……！？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#0105F#6P难、难以置信……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#0205F#6P……完全看不清动作。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, -3500, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 0, 0, -1300, 180)
    SetChrPos(0x102, -2100, 0, 0, 180)
    SetChrPos(0x103, 2100, 0, 0, 180)
    SetChrPos(0x104, 0, 0, 1500, 180)
    SetChrPos(0x198, 500, 0, 700, 180)
    SetChrPos(0x197, -500, 0, 700, 180)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 0, -5000, 0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0111
    ChrTalk(
        0x198,
        "#5P#4S好、好厉害啊───！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x198, 3, 0, 20)
    Sleep(50)
    BeginChrThread(0x197, 3, 0, 21)
    WaitChrThread(0x197, 3)
    OP_9C(0x198, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    OP_9C(0x198, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)

    #C0112
    ChrTalk(
        0x198,
        (
            "#11P太强了～！\x01",
            "真是太厉害了，亚里欧斯先生！\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x198,
        (
            "#11P哇哇～！\x01",
            "见识到了好惊人的场面呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x197,
        "#6P多、多谢您了，亚里欧斯先生！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x197,
        "#6P可是，您怎么会来这里呢……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    #N0116
    NpcTalk(
        0x8,
        "男性",
        (
            "#11P#1403F哦，因为我接到了有\x01",
            "小孩进入广场地下道出入口\x01",
            "的消息。\x02\x03",

            "#1401F你们也太胡闹了。\x02\x03",

            "万一发生什么意外，\x01",
            "该如何是好？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x197,
        "#6P呜呜……对不起。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x198,
        "#11P那个……是我不好。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5F, 0x190)
    Sleep(300)

    #N0119
    NpcTalk(
        0x8,
        "男性",
        (
            "#5P#1402F呼……\x01",
            "算了，你们没事就好。\x02\x03",

            "#1404F已经傍晚了。\x01",
            "赶快出去，然后回家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x198,
        "#11P嗯！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x197,
        "#6P知、知道了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    ClearChrFlags(0x8, 0x4)

    def lambda_3BF0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3BF0)
    Sleep(150)

    def lambda_3C0D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_3C0D)
    Sleep(50)

    def lambda_3C2A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_3C2A)
    WaitChrThread(0x8, 1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    def lambda_3C64():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_3C64)
    Sleep(50)

    def lambda_3C74():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_3C74)
    Sleep(300)

    #N0122
    NpcTalk(
        0x8,
        "男性",
        (
            "#12P#1400F──怎么了？\x01",
            "你们不回去吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0123
    ChrTalk(
        0x101,
        (
            "#0005F#5P啊，那个……\x02\x03",

            "#0001F……说得也是呢，\x01",
            "我们也一起回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0124
    NpcTalk(
        0x8,
        "男性",
        (
            "#12P#1403F那就不要磨磨蹭蹭的。\x02\x03",

            "#1400F刚才的事情就是个教训。\x01",
            "直到最后一刻，也都不能松懈大意。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_3D75():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_3D75)
    Sleep(50)

    def lambda_3D85():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_3D85)

    def lambda_3D92():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D92)
    Sleep(150)

    def lambda_3DAF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_3DAF)
    Sleep(50)

    def lambda_3DCC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_3DCC)
    WaitChrThread(0x8, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(0, 1000, -500, 2000)
    OP_6F(0x1)
    Sleep(500)
    OP_64(0x101)
    Sleep(500)

    #C0125
    ChrTalk(
        0x101,
        "#5P#0001F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#5P#0305F呼啊～！\x01",
            "那位大叔究竟是何方神圣啊？\x02\x03",

            "#0306F他散发出来的气息\x01",
            "实在是非同寻常……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x103,
        (
            "#5P#0206F……就实力来说，\x01",
            "也绝不是等闲之辈呢。\x02\x03",

            "#0200F究竟是什么人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        "#5P#0101F对了，那个人是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3F35():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3F35)
    Sleep(50)

    def lambda_3F45():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3F45)
    WaitChrThread(0x104, 2)

    #C0129
    ChrTalk(
        0x104,
        "#5P#0305F大小姐，你认识他吗？\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)

    #C0130
    ChrTalk(
        0x102,
        (
            "#6P#0103F也只是知道名字而已。\x02\x03",

            "#0105F……话说，为什么\x01",
            "要这样叫我啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#5P#0309F没什么，就是觉得这么叫比较顺口。\x02\x03",

            "#0301F话说回来，他到底是什么人啊，\x01",
            "那个厉害的大叔……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        "#6P#0108F嗯，多半就是──\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#5P#0003F──亚里欧斯·马克莱因。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_40B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_40B5)
    Sleep(50)

    def lambda_40C5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_40C5)
    Sleep(50)

    def lambda_40D5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_40D5)
    WaitChrThread(0x102, 2)
    Sleep(300)

    #C0134
    ChrTalk(
        0x101,
        (
            "#5P#0006F在克洛斯贝尔时代周刊上\x01",
            "曾经多次看到过关于他的报道。\x02\x03",

            "隶属于游击士协会·克洛斯贝尔\x01",
            "分部的最强Ａ级游击士──\x02\x03",

            "#0008F无论任何委托都能完美解决，\x01",
            "深受广大市民的信赖，\x01",
            "克洛斯贝尔真正的守护神……\x02\x03",

            "#0001F『风之剑圣』\x01",
            "亚里欧斯·马克莱因。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xF, 0, 0, 23)
    SetCameraDistance(17500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0xF, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1B06 end

    def Function_20_420F(): pass

    label("Function_20_420F")

    OP_63(0x198, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_4226():
        OP_95(0xFE, 1300, 0, -2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_4226)
    WaitChrThread(0x198, 1)

    def lambda_4244():
        OP_95(0xFE, 1000, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_4244)
    WaitChrThread(0x198, 1)
    TurnDirection(0x198, 0x8, 500)
    Return()

    # Function_20_420F end

    def Function_21_4265(): pass

    label("Function_21_4265")

    OP_63(0x197, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_427C():
        OP_95(0xFE, -1300, 0, -2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_427C)
    WaitChrThread(0x197, 1)

    def lambda_429A():
        OP_95(0xFE, -1000, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_429A)
    WaitChrThread(0x197, 1)
    TurnDirection(0x197, 0x8, 500)
    Return()

    # Function_21_4265 end

    def Function_22_42BB(): pass

    label("Function_22_42BB")

    Sleep(300)

    def lambda_42C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_42C3)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)

    def lambda_42DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_42DC)
    WaitChrThread(0x8, 2)
    Return()

    # Function_22_42BB end

    def Function_23_42ED(): pass

    label("Function_23_42ED")

    OP_25(0x80, 0x64)
    Sleep(200)
    OP_25(0x80, 0x5A)
    Sleep(200)
    OP_25(0x80, 0x50)
    Sleep(200)
    OP_25(0x80, 0x46)
    Sleep(200)
    OP_25(0x80, 0x3C)
    Sleep(200)
    OP_25(0x80, 0x32)
    Sleep(200)
    OP_25(0x80, 0x28)
    Sleep(200)
    OP_25(0x80, 0x1E)
    Sleep(200)
    OP_25(0x80, 0x14)
    Sleep(200)
    OP_25(0x80, 0xA)
    Sleep(200)
    OP_25(0x80, 0x0)
    Return()

    # Function_23_42ED end

    def Function_24_4338(): pass

    label("Function_24_4338")

    TalkBegin(0xFF)
    SetChrName("")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_24_4338 end

    def Function_25_4363(): pass

    label("Function_25_4363")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441B")

    #C0136
    ChrTalk(
        0x103,
        (
            "#0200F罗伊德前辈，深处大门\x01",
            "的门锁已经解除了。\x02\x03",

            "#0203F那里有返回地上的近路，\x01",
            "我们就走那边的通道吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0005F啊……说得也是呢。\x02\x03",

            "#0000F好，那我们就走那边吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_445E")

    label("loc_441B")


    #C0138
    ChrTalk(
        0x101,
        (
            "#0000F好像有返回地上的近路呢。\x01",
            "难得有捷径可走，还是走那边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_445E")

    Sleep(50)
    SetChrPos(0x0, 90, -3770, -16530, 0)
    EventEnd(0x4)
    Return()

    # Function_25_4363 end

    SaveToFile()

Try(main)
