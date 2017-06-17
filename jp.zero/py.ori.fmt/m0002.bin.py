from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "アリオス",               # 1
        "お供１",                 # 2
        "お供２",                 # 3
        "お供１",                 # 4
        "お供２",                 # 5
        "お供２",                 # 6
        "ボス１",                 # 7
        "SE制御",                 # 8
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
        "Function_7_BEF",          # 07, 7
        "Function_8_1669",         # 08, 8
        "Function_9_16D6",         # 09, 9
        "Function_10_171B",        # 0A, 10
        "Function_11_1760",        # 0B, 11
        "Function_12_17A5",        # 0C, 12
        "Function_13_17EA",        # 0D, 13
        "Function_14_182F",        # 0E, 14
        "Function_15_1874",        # 0F, 15
        "Function_16_18C7",        # 10, 16
        "Function_17_191A",        # 11, 17
        "Function_18_1ACB",        # 12, 18
        "Function_19_1B66",        # 13, 19
        "Function_20_44F2",        # 14, 20
        "Function_21_4548",        # 15, 21
        "Function_22_459E",        # 16, 22
        "Function_23_45D0",        # 17, 23
        "Function_24_461B",        # 18, 24
        "Function_25_4656",        # 19, 25
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
            "大型の魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_7F8"),
        (SWITCH_DEFAULT, "loc_80F"),
    )


    label("loc_7F8")

    Sleep(500)
    OP_90(0x0, 40, 0, -8060, 0)
    EventEnd(0x5)
    Return()

    label("loc_80F")

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
        (2, "loc_8D1"),
        (1, "loc_8D4"),
        (SWITCH_DEFAULT, "loc_8D7"),
    )


    label("loc_8D1")

    EventEnd(0x5)
    Return()

    label("loc_8D4")

    OP_B7(0x0)
    Return()

    label("loc_8D7")

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
            "手配魔獣を退治した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(0, 1200, -3750, 1500)
    FadeToBright(300, 0)

    def lambda_9BB():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BB)
    Sleep(50)

    def lambda_9CB():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9CB)
    Sleep(50)

    def lambda_9DB():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9DB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)

    #C0003
    ChrTalk(
        0x101,
        "#0000F#5Pよし、何とかなったか。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#0304F#12Pま、アリオスって遊撃士が\x01",
            "倒したのよりは格下だったけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#0102F#11Pふふ、でも４人で協力すれば\x01",
            "今後も何とかなりそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#0204F#6P……ですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0007
    ChrTalk(
        0x103,
        (
            "#0202F#6P先ほど、奥のゲートの\x01",
            "ロックを解除しておきました。\x02\x03",

            "地上に戻る近道があるので\x01",
            "そちらのルートを使いましょう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0008
    ChrTalk(
        0x101,
        (
            "#0005F#5Pあ、ああ……\x01",
            "（って、いつの間に？）\x02",
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

    def Function_7_BEF(): pass

    label("Function_7_BEF")

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

    def lambda_E2F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E2F)

    def lambda_E40():
        OP_97(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E40)
    Sleep(150)

    def lambda_E5D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E5D)

    def lambda_E6E():
        OP_97(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E6E)
    Sleep(500)

    def lambda_E8B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E8B)

    def lambda_E9C():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E9C)
    Sleep(150)

    def lambda_EB9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EB9)

    def lambda_ECA():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ECA)
    Sleep(500)

    def lambda_EE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_EE7)

    def lambda_EF8():
        OP_97(0xFE, 0x0, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_EF8)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    SetChrFlags(0x198, 0x4)
    SetChrPos(0x198, 0, 0, -1000, 180)

    #N0009
    NpcTalk(
        0x198,
        "男の子の声",
        "く、くるなよ～っ！\x02",
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x198,
        "男の子の声",
        (
            "うわあん、助けてえぇっ！\x01",
            "女神#4Rエイドス#さま～っ！\x02",
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
        "#11P#0105Fあっ……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x197,
        "リュウっ！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#12P#0013F（くっ……！）\x02",
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
            "【そのまま魔獣の背後に突っ込む】\x01",        # 0
            "【魔獣の注意をこちらに引き付ける】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetScenarioFlags(0x41, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1182"),
        (1, "loc_1334"),
        (SWITCH_DEFAULT, "loc_1651"),
    )


    label("loc_1182")

    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0014
    ChrTalk(
        0x101,
        (
            "#12P#0007F──このまま突っ込むぞ！\x02\x03",

            "魔獣の不意を突きつつ\x01",
            "子供の安全確保を最優先で！\x02",
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
        "#11P#0307Fよしきた！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        "#11P#0107Fええ！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 700, -4500, 1700)
    MoveCamera(50, 22, 0, 1700)
    SetCameraDistance(25000, 1700)

    def lambda_1273():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1273)
    Sleep(50)

    def lambda_1290():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1290)
    Sleep(50)

    def lambda_12AD():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12AD)
    Sleep(50)

    def lambda_12CA():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12CA)
    Sleep(50)

    def lambda_12E7():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_12E7)
    Sleep(1500)
    OP_6F(0x79)
    Battle("BattleInfo_3B0", 0x30200011, 0x2, 0x0, 0x13, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x197, 0x1)
    Jump("loc_1651")

    label("loc_1334")

    TurnDirection(0x101, 0x102, 500)

    #C0017
    ChrTalk(
        0x101,
        (
            "#6P#0007F──エリィ！\x01",
            "奴らの注意を引き付けてくれ！\x02",
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
        "#11P#0101F分かった……！\x02",
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

    def lambda_143F():
        OP_96(0xFE, 0x0, 0x0, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_143F)

    def lambda_1459():
        OP_97(0xFE, 0x0, 0x0, 0x189C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1459)
    Sleep(50)

    def lambda_1476():
        OP_97(0xFE, 0x0, 0x0, 0x189C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1476)
    Sleep(50)

    def lambda_1493():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1493)
    Sleep(50)

    def lambda_14B0():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_14B0)
    WaitChrThread(0x197, 1)
    WaitChrThread(0x198, 1)

    #C0019
    ChrTalk(
        0x103,
        (
            "#12P#0201F……何とか注意を\x01",
            "逸らせたみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#12P#0007Fよし、片付けるぞ！\x02",
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

    def lambda_1561():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1561)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    BeginChrThread(0xA, 0, 0, 1)

    def lambda_158E():
        OP_98(0xFE, 0xBB8, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_158E)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    BeginChrThread(0xB, 0, 0, 1)

    def lambda_15BB():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_15BB)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    BeginChrThread(0xC, 0, 0, 1)

    def lambda_15E8():
        OP_98(0xFE, 0xFFFFFA24, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_15E8)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x20)
    BeginChrThread(0xD, 0, 0, 1)

    def lambda_1615():
        OP_98(0xFE, 0x5DC, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1615)
    Sleep(500)
    Battle("BattleInfo_3F4", 0x30200011, 0x0, 0x0, 0x14, 0xFF)
    FadeToDark(0, 0, -1)
    CancelBlur(0)
    Jump("loc_1651")

    label("loc_1651")

    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    Call(0, 19)
    Return()

    # Function_7_BEF end

    def Function_8_1669(): pass

    label("Function_8_1669")

    BeginChrThread(0xB, 3, 0, 11)
    OP_63(0x198, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1686():
        OP_96(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_1686)
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

    # Function_8_1669 end

    def Function_9_16D6(): pass

    label("Function_9_16D6")

    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_16EE():
        OP_96(0xFE, 0xCE4, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16EE)
    WaitChrThread(0x9, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_9_16D6 end

    def Function_10_171B(): pass

    label("Function_10_171B")

    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1733():
        OP_96(0xFE, 0xFFFFF31C, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1733)
    WaitChrThread(0xA, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_10_171B end

    def Function_11_1760(): pass

    label("Function_11_1760")

    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1778():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1778)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    Return()

    # Function_11_1760 end

    def Function_12_17A5(): pass

    label("Function_12_17A5")

    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_17BD():
        OP_96(0xFE, 0x960, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_17BD)
    WaitChrThread(0xC, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    Return()

    # Function_12_17A5 end

    def Function_13_17EA(): pass

    label("Function_13_17EA")

    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1802():
        OP_96(0xFE, 0xFFFFF6A0, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1802)
    WaitChrThread(0xD, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    SetChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    Return()

    # Function_13_17EA end

    def Function_14_182F(): pass

    label("Function_14_182F")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1847():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1847)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_182F end

    def Function_15_1874(): pass

    label("Function_15_1874")

    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1893():
        OP_98(0xFE, 0x514, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1893)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_15_1874 end

    def Function_16_18C7(): pass

    label("Function_16_18C7")

    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_18E6():
        OP_98(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18E6)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_16_18C7 end

    def Function_17_191A(): pass

    label("Function_17_191A")


    def lambda_191F():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_191F)
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

    # Function_17_191A end

    def Function_18_1ACB(): pass

    label("Function_18_1ACB")

    EndChrThread(0xFE, 0x0)

    def lambda_1AD4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1AD4)
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

    # Function_18_1ACB end

    def Function_19_1B66(): pass

    label("Function_19_1B66")

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
        "#12P#0003Fふう……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#6P#0106F何とか片付いたわね……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#5P#0300Fさすがにちょいと\x01",
            "手こずっちまったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        "#11P#0206F……疲れました。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x198,
        "#5Pび、びっくりしたぁ……！\x02",
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

    def lambda_1E98():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E98)
    Sleep(50)

    def lambda_1EA8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1EA8)
    Sleep(50)

    def lambda_1EB8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1EB8)
    Sleep(50)

    def lambda_1EC8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1EC8)
    Sleep(50)
    TurnDirection(0x197, 0x198, 500)

    #C0026
    ChrTalk(
        0x197,
        (
            "#6Pリュウ、大丈夫！？\x01",
            "ケガとかしてない！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x198, 0x197, 500)

    #C0027
    ChrTalk(
        0x198,
        (
            "#11Pう、うん……\x01",
            "ぜんぜんヘーキだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x198,
        (
            "#11Pそれよりオマエも無事で\x01",
            "ホントーによかったぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x198,
        (
            "#11Pオマエ、どんくさいからな～。\x01",
            "オレが助けてやんないと\x01",
            "魔獣に喰われちまうと思ってさぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x197,
        (
            "#6Pよ、よく言うよ。\x01",
            "自分だって魔獣に食べられそうに\x01",
            "なってたくせに……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x197,
        (
            "#6Pだいたい今度だって\x01",
            "リュウが入ろうって強引に……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x198,
        "#11Pな、なに言ってんだよ！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x198,
        (
            "#11P最初に『じおふろんと』の話を\x01",
            "し始めたのはオマエの方だろー！？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x197,
        (
            "#6Pだ、だからって本当に\x01",
            "入るとか言い出すなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#0003Fはいはい。\x01",
            "言い争いはそこまでだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2161():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_2161)
    Sleep(50)

    def lambda_2171():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_2171)
    WaitChrThread(0x198, 2)

    #C0036
    ChrTalk(
        0x197,
        "#1Pご、ごめんなさい……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x198,
        (
            "#5Pへ～、兄ちゃんたち、\x01",
            "初めて見るカオだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x198,
        (
            "#5Pけっこう強いみたいだけど\x01",
            "新人のヒトたち？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#12P#0005Fへ……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#5P#0306Fったく……\x01",
            "調子のいいガキンチョだな。\x02\x03",

            "#0301F助けられたんだったら\x01",
            "まずはお礼を言うのが先だろ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2286():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_2286)
    Sleep(500)

    #C0041
    ChrTalk(
        0x198,
        "#12Pへへっ、まあ助かったよ。\x02",
    )

    CloseMessageWindow()

    def lambda_22B8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_22B8)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_22E0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2307")

    label("loc_22E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_22FD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2307")

    label("loc_22FD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2307")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2323"),
        (1, "loc_23D9"),
        (2, "loc_2478"),
        (SWITCH_DEFAULT, "loc_250F"),
    )


    label("loc_2323")

    OP_2C(0x3C, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0042
    ChrTalk(
        0x198,
        (
            "#5P危ない所もあったけど\x01",
            "オレもカスリ傷ひとつ無かったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x198,
        "#5Pわりと手際がいいんじゃね？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#12P#0005Fそりゃどうも……\x02\x01",

            "#0012Fって、ホント調子いいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250F")

    label("loc_23D9")

    OP_2C(0x3C, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x198,
        (
            "#5P危ない所もあったけど\x01",
            "オレもカスリ傷くらいで済んだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x198,
        "#5Pま、ギリギリ合格点かな。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#12P#0002Fはは……\x01",
            "精進させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250F")

    label("loc_2478")


    #C0048
    ChrTalk(
        0x198,
        (
            "#5Pたださあ、兄ちゃんたち\x01",
            "ちょっと手際が悪すぎない？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x198,
        "#5P死ぬかと思ったよ、オレ。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#12P#0006F……ごめんな。\x01",
            "怖い思いをさせちゃって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250F")

    label("loc_250F")


    #C0051
    ChrTalk(
        0x102,
        (
            "#6P#0104Fふふ、でも無事でよかった。\x02\x03",

            "#0102Fとにかく一度、\x01",
            "外に出るとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    #C0052
    ChrTalk(
        0x103,
        (
            "#11P#0204F……そうですね。\x01",
            "どうやら終点みたいですし。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(300)

    #C0053
    ChrTalk(
        0x103,
        (
            "#11P#0202F一応、セルゲイ課長の課題も\x01",
            "クリアしたことになりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#12P#0000Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        (
            "#5P#0306Fま、こんなハプニングがあるとは\x01",
            "思ってもなかったけどな。\x02\x03",

            "#0302Fそんじゃ、ガキどもを送ったら\x01",
            "警察本部に戻るとするか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_269F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_269F)

    def lambda_26AC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_26AC)
    WaitChrThread(0x198, 2)
    OP_63(0x198, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x197, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x198)
    OP_64(0x197)

    #C0056
    ChrTalk(
        0x101,
        "#12P#0000Fん、どうしたんだ？\x02",
    )

    CloseMessageWindow()

    def lambda_270C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_270C)

    def lambda_2719():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_2719)
    WaitChrThread(0x198, 2)

    #C0057
    ChrTalk(
        0x198,
        "#5Pあのさ……兄ちゃんたち。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x198,
        (
            "#5P兄ちゃんたちって\x01",
            "やっぱり新人なんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあ、ああ……そうだけど。\x02\x03",

            "#0000Fしかしよく分かるな？\x01",
            "制服だって着てないのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x198,
        "#5Pせ、制服……？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x197,
        "#1Pあ、あのー、ひょっとして。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x197,
        (
            "#1Pお兄さんたち……\x01",
            "ギルドの人じゃないんですか？\x02",
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
        "#12P#0011Fえっ……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#6P#0105Fギルドって……\x01",
            "《遊撃士協会#10Rブレイサーギルド#》のこと？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x198,
        (
            "#5Pギルドっていったら\x01",
            "他にあるわけがないじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x198,
        (
            "#5Pえ、なに！？\x01",
            "本当に遊撃士#6Rブレイサー#じゃないの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#12P#0012Fい、いや……\x02\x03",

            "#0000F俺たちは、クロスベル警察に\x01",
            "入ったばかりの新人だけど……\x02",
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
        "#1P#4Sええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x198,
        "#5P#4Sケーサツの人間っ！？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x198,
        (
            "#5Pうっそだぁ！\x01",
            "どうしてケーサツのお巡りが\x01",
            "こんなところにいるんだよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#12P#0003Fあ、ああ……\x01",
            "ちょっと事情があってさ。\x02\x03",

            "任務の途中で君たちを\x01",
            "見つけたって訳なんだけど。\x02\x03",

            "#0000F……でも、\x01",
            "そんなに不思議なことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x198,
        "#5Pだってさあ！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x198,
        (
            "#5Pケーサツのお巡りっていったら\x01",
            "腰抜けって有名じゃんか！\x02",
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
        "#12P#0011F#4Sえ゛。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x198,
        (
            "#5P態度もオーヘイなわりに\x01",
            "何の手助けもしてくれないって\x01",
            "父ちゃんが言ってたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x198,
        (
            "#5Pいざという時は、遊撃士の方が\x01",
            "何十倍も頼りになるって。\x02",
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
        "#6P#0108F………やっぱり…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x197, 0x198, 500)
    Sleep(300)

    #C0079
    ChrTalk(
        0x197,
        "#6Pリ、リュウ、失礼だよ。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x197,
        (
            "#6Pいくら警察のヒトだって\x01",
            "ボクたちを助けてくれたんだし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x198, 0x197, 500)

    #C0081
    ChrTalk(
        0x198,
        "#11Pそ、そうだけどさ～。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x198,
        (
            "#11Pせっかくギルドの新人に\x01",
            "助けてもらったと思ったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#5P#0305Fふーん？\x01",
            "色々とあるみたいだな。\x02\x03",

            "#0301F……って………\x02",
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
        "#5P#0307Fおい、マズイぞ！？\x02",
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

    def lambda_2ED5():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2ED5)
    Sleep(100)

    def lambda_2EE5():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2EE5)

    def lambda_2EF2():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2EF2)

    #C0085
    ChrTalk(
        0x101,
        "#5P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#5P#0201Fっ……！？\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        "#5P#0105F上……！？\x02",
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

    def lambda_2F91():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0xA, 0x9C4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2F91)
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

    def lambda_30E2():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30E2)
    Sleep(150)
    OP_63(0x197, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3111():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_3111)
    Sleep(100)
    OP_63(0x198, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3140():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_3140)
    OP_6F(0x79)

    #C0088
    ChrTalk(
        0x197,
        "#5Pひっ……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x198,
        "うわあっ！？\x02",
    )

    CloseMessageWindow()
    OP_64(0x198)
    OP_64(0x197)

    #C0090
    ChrTalk(
        0x101,
        "#0010F#6Pくっ……！？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        "#0310F#6Pなんだコイツは！？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        "#0107F#6Pな、なんて大きさ……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#0208F#6P……まずいです。\x01",
            "背後の扉はロックされています。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#0013F#6Pくっ……このままじゃ……！\x02",
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
            "#0307F#6Pおい、どうするつもりだ！？\x02\x03",

            "まともにやっても\x01",
            "今の装備じゃ勝ち目はねぇぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#0007F#5P分かってる！\x02\x03",

            "ここは俺が引き付けるから\x01",
            "みんなは何とか脱出してくれ！\x02",
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

    def lambda_3392():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3392)
    Sleep(50)

    def lambda_33A2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_33A2)
    WaitChrThread(0x103, 2)

    #C0097
    ChrTalk(
        0x102,
        "#12P#0101Fちょ、ちょっと……！？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        "#0201F正気ですか……？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#0007F#5Pこの状況じゃ\x01",
            "それしか方法はない！\x02\x03",

            "ランディとエリィで\x01",
            "その子たちを抱きかかえて\x01",
            "とにかく隙をついて逃げろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0310F#6Pちっ……\x01",
            "それしかねぇか……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x197,
        "#5Pそ、そんな……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x198,
        "に、兄ちゃん……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 100000, 4000, -17700, 0)

    #N0103
    NpcTalk(
        0x8,
        "声",
        "#3P──やれやれ。\x02",
    )

    CloseMessageWindow()

    #N0104
    NpcTalk(
        0x8,
        "声",
        (
            "#3P自己犠牲も結構だが\x01",
            "少々、短絡的すぎるな。\x02",
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

    def lambda_35D5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_35D5)

    def lambda_35E2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_35E2)
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
    SetChrName("男")

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

    def lambda_3794():
        OP_9D(0xFE, 0x186A0, 0x0, 0xFFFFEE6C, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3794)
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
        "#0005F#5Pあ……\x02",
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

    def lambda_38C7():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_38C7)
    PlayEffect(0x0, 0xFF, 0xE, 0x0, 0, 1000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(816, 0, 100, 0)
    Sleep(500)

    def lambda_3920():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3920)
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
        "#0305F#6Pマ、マジかよ……！？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#0105F#6Pし、信じられない……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#0205F#6P……見えませんでした。\x02",
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
        "#5P#4Sす、すっげ───っ！\x02",
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
            "#11Pすげーっ！\x01",
            "すごすぎるよ、アリオスさんっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x198,
        (
            "#11Pうっわ～っ！\x01",
            "いいもん見ちゃったなああ！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x197,
        "#6Pあ、ありがとう、アリオスさん！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x197,
        "#6Pでも、どうしてここに……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    #N0116
    NpcTalk(
        0x8,
        "男",
        (
            "#11P#1403Fああ、広場のマンホールに\x01",
            "子供が入っていくのを\x01",
            "見たという報せがあってな。\x02\x03",

            "#1401Fしかし無茶をする。\x02\x03",

            "もしものことがあったら\x01",
            "どうするつもりだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x197,
        "#6Pううっ……ごめんなさい。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x198,
        "#11Pその……悪かったよ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5F, 0x190)
    Sleep(300)

    #N0119
    NpcTalk(
        0x8,
        "男",
        (
            "#5P#1402Fフ……\x01",
            "まあ、無事ならそれでいい。\x02\x03",

            "#1404Fもう夕方だ。\x01",
            "とっとと出て家に帰るぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x198,
        "#11Pうんっ！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x197,
        "#6Pわ、わかりました！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    ClearChrFlags(0x8, 0x4)

    def lambda_3E9D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E9D)
    Sleep(150)

    def lambda_3EBA():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_3EBA)
    Sleep(50)

    def lambda_3ED7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_3ED7)
    WaitChrThread(0x8, 1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    def lambda_3F11():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_3F11)
    Sleep(50)

    def lambda_3F21():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_3F21)
    Sleep(300)

    #N0122
    NpcTalk(
        0x8,
        "男",
        (
            "#12P#1400F──どうした？\x01",
            "お前たちは戻らないのか？\x02",
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
            "#0005F#5Pえ、ああ……\x02\x03",

            "#0001F……そうですね。\x01",
            "一緒に戻らせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #N0124
    NpcTalk(
        0x8,
        "男",
        (
            "#12P#1403Fなら、グズグズするな。\x02\x03",

            "#1400F先程のようなこともある。\x01",
            "最後まで気を抜かないことだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_4032():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_4032)
    Sleep(50)

    def lambda_4042():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_4042)

    def lambda_404F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_404F)
    Sleep(150)

    def lambda_406C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_406C)
    Sleep(50)

    def lambda_4089():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_4089)
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
            "#5P#0305Fかあ～っ！\x01",
            "なんていうオッサンだよ？\x02\x03",

            "#0306Fまとってるオーラが\x01",
            "尋常じゃないというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x103,
        (
            "#5P#0206F……腕前の方も\x01",
            "普通ではありませんでした。\x02\x03",

            "#0200Fいったい何者なんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        "#5P#0101Fそう、あの人が……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4208():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4208)
    Sleep(50)

    def lambda_4218():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4218)
    WaitChrThread(0x104, 2)

    #C0129
    ChrTalk(
        0x104,
        "#5P#0305Fお嬢、知ってるのか？\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)

    #C0130
    ChrTalk(
        0x102,
        (
            "#6P#0103F名前くらいだけど、ね。\x02\x03",

            "#0105F……というか、何で私を\x01",
            "そんな風に呼ぶのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#5P#0309Fいや、何となくノリで。\x02\x03",

            "#0301Fそれで何者なんだよ、\x01",
            "あの凄まじいオッサンは。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        "#6P#0108Fええ、多分──\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#5P#0003F──アリオス・マクレイン。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_438E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_438E)
    Sleep(50)

    def lambda_439E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_439E)
    Sleep(50)

    def lambda_43AE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_43AE)
    WaitChrThread(0x102, 2)
    Sleep(300)

    #C0134
    ChrTalk(
        0x101,
        (
            "#5P#0006Fクロスベルタイムズで\x01",
            "何度か読んだことがある。\x02\x03",

            "遊撃士協会・クロスベル支部に\x01",
            "所属する最強のＡ級遊撃士──\x02\x03",

            "#0008Fどんな依頼も完璧にこなし、\x01",
            "市民から絶大な信頼を得ている\x01",
            "クロスベルの真の守護神……\x02\x03",

            "#0001F《風の剣聖》\x01",
            "アリオス・マクレインだ。\x02",
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

    # Function_19_1B66 end

    def Function_20_44F2(): pass

    label("Function_20_44F2")

    OP_63(0x198, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_4509():
        OP_95(0xFE, 1300, 0, -2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_4509)
    WaitChrThread(0x198, 1)

    def lambda_4527():
        OP_95(0xFE, 1000, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_4527)
    WaitChrThread(0x198, 1)
    TurnDirection(0x198, 0x8, 500)
    Return()

    # Function_20_44F2 end

    def Function_21_4548(): pass

    label("Function_21_4548")

    OP_63(0x197, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_455F():
        OP_95(0xFE, -1300, 0, -2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_455F)
    WaitChrThread(0x197, 1)

    def lambda_457D():
        OP_95(0xFE, -1000, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_457D)
    WaitChrThread(0x197, 1)
    TurnDirection(0x197, 0x8, 500)
    Return()

    # Function_21_4548 end

    def Function_22_459E(): pass

    label("Function_22_459E")

    Sleep(300)

    def lambda_45A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_45A6)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)

    def lambda_45BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_45BF)
    WaitChrThread(0x8, 2)
    Return()

    # Function_22_459E end

    def Function_23_45D0(): pass

    label("Function_23_45D0")

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

    # Function_23_45D0 end

    def Function_24_461B(): pass

    label("Function_24_461B")

    TalkBegin(0xFF)
    SetChrName("")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉はロックされており、\x01",
            "開きそうもない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_24_461B end

    def Function_25_4656(): pass

    label("Function_25_4656")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4732")

    #C0136
    ChrTalk(
        0x103,
        (
            "#0200Fロイドさん、奥のゲートの\x01",
            "ロックを解除しておきました。\x02\x03",

            "#0203F地上に戻る近道があるので\x01",
            "そちらのルートを使いましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……そうだったな。\x02\x03",

            "#0000Fよし、そっちに回ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_477D")

    label("loc_4732")


    #C0138
    ChrTalk(
        0x101,
        (
            "#0000F地上に戻る近道があるみたいだ。\x01",
            "折角だし、そっちを使ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477D")

    Sleep(50)
    SetChrPos(0x0, 90, -3770, -16530, 0)
    EventEnd(0x4)
    Return()

    # Function_25_4656 end

    SaveToFile()

Try(main)
