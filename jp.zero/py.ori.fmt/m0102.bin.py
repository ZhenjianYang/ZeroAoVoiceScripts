from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0102.bin",                # FileName
        "m0102",                    # MapName
        "m0102",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 3, 0, 4],
    )

    BuildStringList((
        "m0102",                  # 0
        "トルゾーＢ",             # 1
        "トルゾーＢ",             # 2
        "トルゾーＢ",             # 3
        "トルゾーＢ",             # 4
        "トルゾーＤＸ",           # 5
        "bm0102",                 # 6
        "bm0102",                 # 7
    ))

    ATBonus("ATBonus_2A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_284", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_384", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 4, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 12, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 2, 3, 90)
    MonsterBattlePostion("MonsterBattlePostion_394", 14, 3, 270)
    MonsterBattlePostion("MonsterBattlePostion_398", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_348", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_34C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_350", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_354", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_358", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_35C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_364", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 5, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 11, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 6, 0, 0)
    MonsterBattlePostion("MonsterBattlePostion_374", 10, 0, 0)
    MonsterBattlePostion("MonsterBattlePostion_378", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_3E8", 0x0C10, 255, 6, 0, 0, 0, 0, 0, "bm0102", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62300.dat", "ms60401.dat", "ms60401.dat", "ms60401.dat", "ms60401.dat", 0, "ms60401.dat", 0, "MonsterBattlePostion_384", "MonsterBattlePostion_344", "ed7401", "ed7403", "ATBonus_2A4"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_3A4", 0x0002, 5, 6, 0, 0, 1, 0, 0, "bm0102", 0x00000000, 100, 0, 0, 0,
        (
            ("ms61200.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, "MonsterBattlePostion_364", "MonsterBattlePostion_364", "ed7401", "ed7403", "ATBonus_284"),
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
        "monster/ch60550.itc",               # 10
        "monster/ch60550.itc",               # 11
        "monster/ch62350.itc",               # 12
        "monster/ch62350.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)

    DeclMonster(0,       0,       750,     0x185010E,    "BattleInfo_3E8", 0,   18,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 6,   -7.0,                  0.0,                   -1.0,                  144.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   2.3333334922790527,    -0.0,                  0.20000001788139343,   1.0])
    DeclEvent(0x0040, 0, 5,   0.0,                   0.0,                   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  0.25,                  1.0])

    DeclActor(-8000,   0,       -4500,   1200,    -10500,  -8800,   -2750,   0x007C, 0,  11, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 1

    ScpFunction((
        "Function_0_474",          # 00, 0
        "Function_1_493",          # 01, 1
        "Function_2_4B2",          # 02, 2
        "Function_3_4CF",          # 03, 3
        "Function_4_4D0",          # 04, 4
        "Function_5_5BB",          # 05, 5
        "Function_6_7F7",          # 06, 6
        "Function_7_F11",          # 07, 7
        "Function_8_F71",          # 08, 8
        "Function_9_FD1",          # 09, 9
        "Function_10_1031",        # 0A, 10
        "Function_11_1091",        # 0B, 11
    ))


    def Function_0_474(): pass

    label("Function_0_474")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_492")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_474")

    label("loc_492")

    Return()

    # Function_0_474 end

    def Function_1_493(): pass

    label("Function_1_493")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B1")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_493")

    label("loc_4B1")

    Return()

    # Function_1_493 end

    def Function_2_4B2(): pass

    label("Function_2_4B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CE")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_2_4B2")

    label("loc_4CE")

    Return()

    # Function_2_4B2 end

    def Function_3_4CF(): pass

    label("Function_3_4CF")

    Return()

    # Function_3_4CF end

    def Function_4_4D0(): pass

    label("Function_4_4D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E4")
    VolumeBGM(0x64, 0x64)

    label("loc_4E4")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FC")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_51E")
    SetChrFlags(0xD, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_532")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_532")
    ClearChrFlags(0xD, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_532")

    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0xD, 0x100)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    Sound(122, 1, 100, 0)
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -10500, -8800, -2750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_4_4D0 end

    def Function_5_5BB(): pass

    label("Function_5_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 4)), scpexpr(EXPR_END)), "loc_5C5")
    Return()

    label("loc_5C5")

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
        (1, "loc_6A7"),
        (SWITCH_DEFAULT, "loc_6BE"),
    )


    label("loc_6A7")

    Sleep(500)
    OP_90(0x0, -7900, 0, -400, 90)
    EventEnd(0x5)
    Return()

    label("loc_6BE")

    Battle("BattleInfo_3E8", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-7900, 1000, -400, 0)
    OP_90(0x0, -7900, 0, -400, 90)
    OP_90(0x1, -7900, 0, -400, 90)
    OP_90(0x2, -7900, 0, -400, 90)
    OP_90(0x3, -7900, 0, -400, 90)
    OP_90(0x4, -7900, 0, -400, 90)
    OP_90(0x5, -7900, 0, -400, 90)
    OP_90(0x6, -7900, 0, -400, 90)
    OP_90(0x7, -7900, 0, -400, 90)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_780"),
        (1, "loc_783"),
        (SWITCH_DEFAULT, "loc_786"),
    )


    label("loc_780")

    EventEnd(0x5)
    Return()

    label("loc_783")

    OP_B7(0x0)
    Return()

    label("loc_786")

    EventBegin(0x1)
    SetChrFlags(0xD, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手配魔獣を退治した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x78, 4)
    OP_29(0x1A, 0x4, 0x10)
    OP_29(0x1A, 0x4, 0x2)
    OP_29(0x1A, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_5_5BB end

    def Function_6_7F7(): pass

    label("Function_6_7F7")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("monster/ch60550.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("monster/ch61250.itc", 0x23)
    LoadChrToIndex("monster/ch61253.itc", 0x24)
    LoadEffect(0x0, "event\\eva04_00.eff")
    SoundLoad(865)
    OP_68(-4000, 800, 0, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -5800, 0, 800, 90)
    SetChrPos(0x102, -5800, 0, -800, 90)
    SetChrPos(0x103, -7400, 0, -800, 90)
    SetChrPos(0x104, -7400, 0, 800, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)

    def lambda_92C():
        OP_96(0xFE, 0x320, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92C)
    Sleep(50)

    def lambda_949():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFFCE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_949)
    Sleep(50)

    def lambda_966():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_966)
    Sleep(50)

    def lambda_983():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFFCE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_983)
    OP_68(0, 800, 0, 3500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
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
    Fade(250)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_90(0x8, 15200, 3100, 900, 270)
    OP_90(0x9, 16000, 3500, -900, 270)
    OP_90(0xA, -15200, -3100, 900, 90)
    OP_90(0xB, -15000, -3500, -900, 90)
    OP_68(9500, 1800, 0, 1000)
    SetCameraDistance(20000, 1000)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 7)
    BeginChrThread(0x9, 3, 0, 8)
    Sound(865, 2, 100, 0)
    Sleep(1000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Fade(500)
    OP_68(-9500, -200, 0, 0)
    OP_0D()
    BeginChrThread(0xA, 3, 0, 9)
    BeginChrThread(0xB, 3, 0, 10)
    Sleep(1000)
    Fade(500)
    OP_68(0, 700, 0, 0)
    MoveCamera(25, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    MoveCamera(35, 22, 0, 1000)
    SetCameraDistance(17000, 1000)
    OP_0D()

    def lambda_B82():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B82)

    def lambda_B8F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B8F)

    def lambda_B9C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B9C)

    def lambda_BA9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BA9)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_24(0x361)
    Sleep(1000)
    Fade(500)
    OP_68(10000, 4700, 0, 0)
    MoveCamera(55, -2, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16500, 0)
    OP_68(5500, 1300, 0, 1500)
    MoveCamera(50, 19, 0, 1500)
    SetCameraDistance(12500, 1500)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_90(0xC, 16200, 3600, 0, 270)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0xC, 0xFF)
    SetChrChip(0x0, 0xC, 0x1E, 0x1F4)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)

    def lambda_C74():
        OP_9D(0xFE, 0x157C, 0x0, 0x0, 0xBB8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C74)
    Sound(812, 0, 100, 0)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xC, 1)
    SetChrSubChip(0xC, 0x1)
    PlayEffect(0x0, 0xFF, 0xC, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(813, 0, 100, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x3E8)
    Sleep(1000)
    SetChrChip(0x1, 0xC, 0x0, 0x0)
    OP_4C(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_68(0, 700, 0, 1500)
    MoveCamera(35, 22, 0, 1500)
    SetCameraDistance(17000, 1500)
    OP_6F(0x79)
    Sleep(300)
    Sound(865, 2, 100, 0)
    SetCameraDistance(14000, 300)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_D6D():
        OP_9A(0xFE, 0x101, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D6D)

    def lambda_D81():
        OP_9A(0xFE, 0x102, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D81)

    def lambda_D95():
        OP_9A(0xFE, 0x103, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D95)

    def lambda_DA9():
        OP_9A(0xFE, 0x104, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DA9)
    Sleep(50)

    def lambda_DC0():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DC0)
    Sleep(250)
    OP_24(0x361)
    Battle("BattleInfo_3A4", 0x0, 0x1, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xC, 0xFF)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_37()
    OP_68(0, 0, 0, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(44000, 0)
    SetChrPos(0x0, 0, 0, 0, 90)
    SetChrPos(0x1, 0, 0, 0, 90)
    SetChrPos(0x2, 0, 0, 0, 90)
    SetChrPos(0x3, 0, 0, 0, 90)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x83, 4)
    OP_24(0x361)
    OP_E0(0x2)
    EventEnd(0x5)
    Return()

    # Function_6_7F7 end

    def Function_7_F11(): pass

    label("Function_7_F11")

    SetChrChip(0x0, 0xFE, 0x64, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 0)

    def lambda_F24():
        OP_96(0xFE, 0x1770, 0x0, 0x384, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F24)
    WaitChrThread(0x8, 1)

    def lambda_F42():
        OP_96(0xFE, 0xFA0, 0x0, 0xA8C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F42)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xE1, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_7_F11 end

    def Function_8_F71(): pass

    label("Function_8_F71")

    SetChrChip(0x0, 0xFE, 0x64, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 0)

    def lambda_F84():
        OP_96(0xFE, 0x1770, 0x0, 0xFFFFFC7C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F84)
    WaitChrThread(0x9, 1)

    def lambda_FA2():
        OP_96(0xFE, 0xFA0, 0x0, 0xFFFFF574, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FA2)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x13B, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_8_F71 end

    def Function_9_FD1(): pass

    label("Function_9_FD1")

    SetChrChip(0x0, 0xFE, 0x64, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 0)

    def lambda_FE4():
        OP_96(0xFE, 0xFFFFE890, 0x0, 0x384, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FE4)
    WaitChrThread(0xA, 1)

    def lambda_1002():
        OP_96(0xFE, 0xFFFFF060, 0x0, 0xA8C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1002)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x87, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_9_FD1 end

    def Function_10_1031(): pass

    label("Function_10_1031")

    SetChrChip(0x0, 0xFE, 0x64, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 0)

    def lambda_1044():
        OP_96(0xFE, 0xFFFFE890, 0x0, 0xFFFFFC7C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1044)
    WaitChrThread(0xB, 1)

    def lambda_1062():
        OP_96(0xFE, 0xFFFFF060, 0x0, 0xFFFFF574, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1062)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0x2D, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_10_1031 end

    def Function_11_1091(): pass

    label("Function_11_1091")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0003
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(-10250, -3100, -4000, 1500)
    MoveCamera(45, 27, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(32000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0004
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1160")
    OP_E0(0x2)
    MiniGame(0x6, 0x2, 0xFFFFE0C0, 0x0, 0xFFFFEE6C, 0x113, 0xFFFFD6FC, 0xFFFFDDA0, 0xFFFFF542)

    label("loc_1160")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_11_1091 end

    SaveToFile()

Try(main)
