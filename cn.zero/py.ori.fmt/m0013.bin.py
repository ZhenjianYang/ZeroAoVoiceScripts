from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m0013.bin",                # FileName
        "m0013",                    # MapName
        "m0013",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 3, 0, 4],
    )

    BuildStringList((
        "m0013",                  # 0
        "BOSS",                   # 1
        "约纳的声音",             # 2
        "约纳的声音",             # 3
        "bm0012",                 # 4
        "bm0012",                 # 5
    ))

    ATBonus("ATBonus_324", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_404", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 6, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 10, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 8, 14, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_468", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0012", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_3C4", "ed7401", "ed7403", "ATBonus_324"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_424", 0x0012, 22, 6, 0, 0, 1, 0, 0, "bm0012", 0x00000000, 100, 0, 0, 0,
        (
            ("ms77600.dat", 0, 0, 0, 0, 0, "ms67001.dat", 0, "MonsterBattlePostion_3E4", "MonsterBattlePostion_3C4", "ed7402", "ed7403", "ATBonus_324"),
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
        "monster/ch66150.itc",               # 10
        "monster/ch66150.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       750,     0x18500B4,    "BattleInfo_468", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 6,   0.0,                   -7.5,                  -1.0,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.5,                   0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 5,   0.0,                   0.0,                   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  0.25,                  1.0])
    DeclEvent(0x0000, 0, 15,  0.0,                   9.5,                   -1.0,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.75,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 16,  0.0,                   -10.5,                 -1.5,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.25,                  0.30000001192092896,   1.0])

    DeclActor(102770,  200,     -60,     1200,    102770,  1700,    -60,     0x007C, 0,  17, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_50C",          # 00, 0
        "Function_1_528",          # 01, 1
        "Function_2_547",          # 02, 2
        "Function_3_566",          # 03, 3
        "Function_4_590",          # 04, 4
        "Function_5_6A6",          # 05, 5
        "Function_6_8C8",          # 06, 6
        "Function_7_D8C",          # 07, 7
        "Function_8_E3B",          # 08, 8
        "Function_9_11F2",         # 09, 9
        "Function_10_5537",        # 0A, 10
        "Function_11_5564",        # 0B, 11
        "Function_12_558F",        # 0C, 12
        "Function_13_55EE",        # 0D, 13
        "Function_14_564D",        # 0E, 14
        "Function_15_56F7",        # 0F, 15
        "Function_16_57F7",        # 10, 16
        "Function_17_58ED",        # 11, 17
    ))


    def Function_0_50C(): pass

    label("Function_0_50C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_527")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_50C")

    label("loc_527")

    Return()

    # Function_0_50C end

    def Function_1_528(): pass

    label("Function_1_528")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_546")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_528")

    label("loc_546")

    Return()

    # Function_1_528 end

    def Function_2_547(): pass

    label("Function_2_547")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_565")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_547")

    label("loc_565")

    Return()

    # Function_2_547 end

    def Function_3_566(): pass

    label("Function_3_566")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_580")
    Event(0, 9)

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_58F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 8)

    label("loc_58F")

    Return()

    # Function_3_566 end

    def Function_4_590(): pass

    label("Function_4_590")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5CA")
    SetChrFlags(0xB, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_5DE")

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DE")
    ClearChrFlags(0xB, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_5DE")

    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0xB, 0x100)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66F")
    SetMapFlags(0x2000)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    Jump("loc_679")

    label("loc_66F")

    ClearMapFlags(0x2000)
    ClearMapFlags(0x8000000)

    label("loc_679")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_68D")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_6A5")

    Return()

    # Function_4_590 end

    def Function_5_6A6(): pass

    label("Function_5_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 0)), scpexpr(EXPR_END)), "loc_6B0")
    Return()

    label("loc_6B0")

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
        (1, "loc_77C"),
        (SWITCH_DEFAULT, "loc_793"),
    )


    label("loc_77C")

    Sleep(500)
    OP_90(0x0, 200, 0, -8530, 0)
    EventEnd(0x5)
    Return()

    label("loc_793")

    Battle("BattleInfo_468", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(200, 1000, -8530, 0)
    OP_90(0x0, 200, 0, -8530, 0)
    OP_90(0x1, 200, 0, -8530, 0)
    OP_90(0x2, 200, 0, -8530, 0)
    OP_90(0x3, 200, 0, -8530, 0)
    OP_90(0x4, 200, 0, -8530, 0)
    OP_90(0x5, 200, 0, -8530, 0)
    OP_90(0x6, 200, 0, -8530, 0)
    OP_90(0x7, 200, 0, -8530, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_855"),
        (1, "loc_858"),
        (SWITCH_DEFAULT, "loc_85B"),
    )


    label("loc_855")

    EventEnd(0x5)
    Return()

    label("loc_858")

    OP_B7(0x0)
    Return()

    label("loc_85B")

    EventBegin(0x1)
    SetChrFlags(0xB, 0x80)
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
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x79, 0)
    OP_29(0x25, 0x4, 0x10)
    OP_29(0x25, 0x4, 0x2)
    OP_29(0x25, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_5_6A6 end

    def Function_6_8C8(): pass

    label("Function_6_8C8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("monster/ch77650.itc", 0x22)
    LoadChrToIndex("chr/ch00056.itc", 0x23)
    LoadChrToIndex("chr/ch00256.itc", 0x24)
    LoadEffect(0x0, "event\\eva04_00.eff")
    OP_68(0, 700, -1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -700, 0, -7300, 0)
    SetChrPos(0x103, 700, 0, -7000, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 6000, 0, 180)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 0xFF)

    def lambda_9ED():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9ED)
    Sleep(50)

    def lambda_A0A():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFF704, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0A)
    SetCameraDistance(20000, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)

    #C0003
    ChrTalk(
        0x101,
        "#12P#0000F这里是……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        (
            "#0204F#12P……看来已经到终点了呢。\x02\x03",

            "#0202F第３控制终端所在的房间\x01",
            "多半就在这附近──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AB4():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AB4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 80, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0005
    ChrTalk(
        0x101,
        "#12P#4S#0007F缇欧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x7D0)
    Fade(250)
    OP_68(0, 1700, -1000, 0)
    MoveCamera(50, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13500, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x1)

    def lambda_B74():
        OP_9D(0xFE, 0x12C, 0x0, 0xFFFFFDA8, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B74)
    Sound(814, 0, 100, 0)
    Sound(1011, 255, 100, 0)    #voice#Lloyd
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    BeginChrThread(0x8, 3, 0, 7)
    OP_68(0, 1500, -3000, 500)
    MoveCamera(40, 13, 0, 500)
    SetCameraDistance(14500, 500)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x2)

    def lambda_BDE():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFEE08, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDE)
    Sound(854, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x2)

    def lambda_C09():
        OP_9D(0xFE, 0x2BC, 0x0, 0xFFFFEC78, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C09)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(42, 0, 100, 0)
    Sound(31, 0, 100, 0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x8, 3)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    Sleep(500)

    #C0006
    ChrTalk(
        0x103,
        "#0207F#12P这是……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#0013F#6P可恶……\x01",
            "是下层区域魔兽的首领吗！\x02\x03",

            "#0007F缇欧，只能想办法应战了，可以吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        "#0205F#12P啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 900, 0, -5000, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0009
    ChrTalk(
        0x103,
        "#0201F#12P是……没问题！\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_D3B():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D3B)
    Sleep(50)

    def lambda_D53():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D53)
    Sleep(500)
    Battle("BattleInfo_424", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    Call(0, 8)
    Return()

    # Function_6_8C8 end

    def Function_7_D8C(): pass

    label("Function_7_D8C")

    SetChrChip(0x0, 0x8, 0x1E, 0x12C)

    def lambda_D99():
        OP_9D(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D99)
    Sound(812, 0, 100, 0)
    WaitChrThread(0x8, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_4C(0x8, 0xFF)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x1F4, 0xBB8, 0x3E8)
    Sound(813, 0, 100, 0)
    Sleep(1000)
    CancelBlur(0)
    Return()

    # Function_7_D8C end

    def Function_8_E3B(): pass

    label("Function_8_E3B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("monster/ch77650.itc", 0x22)
    LoadChrToIndex("chr/ch00056.itc", 0x23)
    LoadChrToIndex("chr/ch00256.itc", 0x24)
    OP_68(0, 1000, -4000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x101, -800, 0, -4000, 0)
    SetChrPos(0x103, 700, 0, -4200, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetCameraDistance(16000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0010
    ChrTalk(
        0x101,
        "#12P#0006F呼，总算是击退了吗。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x101, 0x103, 500)

    #C0011
    ChrTalk(
        0x101,
        (
            "#6P#0001F缇欧，没事吗？\x01",
            "刚才那场战斗真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0012
    ChrTalk(
        0x103,
        (
            "#0204F#11P嗯……没问题的。\x02\x03",

            "#0202F罗伊德前辈也没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#6P#0004F哈哈，没事，兰迪曰：\x01",
            "罗伊德最值得自豪的地方\x01",
            "也只有防御技巧高超，皮厚耐打了。\x02\x03",

            "#0001F不过，要是兰迪和艾莉也在，\x01",
            "战斗大概就能更有效率了吧。\x02\x03",

            "#0006F平日里，确实受到他们两人太多帮助了，\x01",
            "现在真是发自内心地体会到了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        "#0202F#11P……呵呵………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0015
    ChrTalk(
        0x101,
        "#6P#0011F我、我说了什么奇怪的话吗？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        (
            "#0204F#11P……没有，\x01",
            "只是我自己的问题而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(300)

    #C0017
    ChrTalk(
        0x103,
        (
            "#0202F#5P我想，『第３控制终端』\x01",
            "应该就在右面的门内。\x02\x03",

            "赶快去将其启动，\x01",
            "然后利用导力通讯与约纳联络吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#6P#0000F嗯……就这么办。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_37()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 0, 0, -4000, 0)
    SetScenarioFlags(0xA1, 2)
    OP_E0(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_E3B end

    def Function_9_11F2(): pass

    label("Function_9_11F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00202.itc", 0x1E)
    LoadChrToIndex("apl/ch50092.itc", 0x1F)
    LoadChrToIndex("apl/ch50011.itc", 0x20)
    LoadChrToIndex("apl/ch50324.itc", 0x21)
    LoadChrToIndex("apl/ch50326.itc", 0x22)
    LoadChrToIndex("apl/ch50218.itc", 0x23)
    LoadEffect(0x0, "event\\eva06_00.eff")
    SoundLoad(806)
    SoundLoad(840)
    SoundLoad(905)
    OP_68(101500, 1000, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 92000, 150, -300, 90)
    SetChrPos(0x103, 92000, 150, 300, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x13)
    SetChrFlags(0x9, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis041.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis042.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis020.itp")
    OP_68(97500, 1000, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    def lambda_1386():
        OP_96(0xFE, 0x1750C, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1386)

    def lambda_13A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13A0)
    Sleep(400)

    def lambda_13B4():
        OP_96(0xFE, 0x1750C, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13B4)

    def lambda_13CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_13CE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)

    #C0019
    ChrTalk(
        0x101,
        "#0005F#6P这个终端……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#0202F就是『第３控制终端』了呢。\x02\x03",

            "这里，再加上约纳擅自使用的\x01",
            "『第８控制终端』……我们打算从这\x01",
            "两个地方来展开黑客行动。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#0004F原来如此。\x02\x03",

            "#0000F那么，现在就和约纳取得联络吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0022
    ChrTalk(
        0x103,
        (
            "#0203F是的，拜托了。\x02\x03",

            "#0200F艾莉前辈和兰迪前辈说不定\x01",
            "也会需要与我们联络，所以\x01",
            "现在先使用我的艾尼格玛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#12P#0000F好的，知道了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德接过了缇欧的艾尼格玛。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_68(103000, 1000, 0, 3000)
    MoveCamera(55, 15, 0, 3000)
    SetCameraDistance(21000, 3000)
    OP_93(0x103, 0x5A, 0x1F4)

    def lambda_15C4():
        OP_95(0xFE, 102000, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15C4)
    Sleep(200)
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_15E8():
        OP_95(0xFE, 101200, 0, -1700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15E8)
    WaitChrThread(0x103, 1)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 102300, 250, 0, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)
    SetMapObjFrame(0x3, "m00gim02", 0x2, "open")
    Sound(72, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(902, 0, 100, 0)
    Sleep(2800)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0025
    AnonymousTalk(
        0x101,
        (
            "#0000F约纳？\x01",
            "我是罗伊德。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是你啊，\x01",
            "已经到了吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0027
    AnonymousTalk(
        0x101,
        (
            "#0000F嗯，缇欧目前\x01",
            "正在启动终端呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＯＫ，ＯＫ。\x01",
            "那么，我这边也要开始了。\x02\x03",

            "哦，对了，\x01",
            "你把艾尼格玛通讯模式中的\x01",
            "扬声器设置为ＯＮ吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0029
    AnonymousTalk(
        0x101,
        "#0005F把扬声器设置为ＯＮ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)
    SetMessageWindowPos(120, 30, -1, -1)

    #A0030
    AnonymousTalk(
        0x103,
        (
            "#0200F请按一下艾尼格玛内侧的\x01",
            "那个红色开关。\x02\x03",

            "那样的话，其他人也能听到\x01",
            "通讯对象的声音了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0031
    AnonymousTalk(
        0x101,
        "#0000F是这样吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德按照缇欧所说的进行操作，\x01",
            "然后把艾尼格玛放在了终端旁边。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x9, 102600, 700, -1500, 0)
    SetChrPos(0xA, 102600, -500, -1500, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Sound(31, 0, 100, 0)
    Sound(42, 0, 100, 0)
    Sleep(800)

    #C0033
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P──哈，\x01",
            "可以听到我的声音了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#6P#0000F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#0203F#5P因为这项功能会消耗很多ＥＰ，\x01",
            "所以一般并不推荐使用。\x01",
            "不过目前还是暂时维持这个状态吧。\x02\x03",

            "#0200F──约纳，\x01",
            "我这边已经准备完毕了。\x02\x03",

            "下一步是什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P哦，我这边已经尽可能\x01",
            "布置好足够多的诱饵了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P『小猫』一旦出现，我就会联络你们，\x01",
            "到时可要好好应对啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0200F#5P了解，\x01",
            "在那之前，我们就先行待命了。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P拜托了！\x02",
        )
    )

    CloseMessageWindow()
    Sound(825, 0, 80, 0)
    StopBGM(0x1F40)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0040
    ChrTalk(
        0x101,
        (
            "#12P#0005F──那个……\x01",
            "这样就算准备完毕了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#0204F#5P嗯，接下来就只剩下等待了。\x02\x03",

            "在开始黑客行动之后，\x01",
            "也只需我一个人就足够了……\x02\x03",

            "#0211F……现在你能明白我说要\x01",
            "一个人行动的理由了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#12P#0006F原、原来如此。\x02\x03",

            "#0000F不过，说句实话，\x01",
            "来这里的一路上相当艰难……\x02\x03",

            "就结果来说，一切顺利不是很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#0203F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#12P#0012F那个，哈哈……\x01",
            "（真糟糕啊，都没有话题可聊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)

    #C0045
    ChrTalk(
        0x101,
        (
            "#6P#0005F说起来……\x01",
            "这是『咪西』吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)

    #A0046
    AnonymousTalk(
        0x101,
        (
            "#0002F你好像很喜欢它呢，\x01",
            "还给导力器挂上了它的挂件。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0047
    AnonymousTalk(
        0x103,
        (
            "#0204F嗯……\x01",
            "或许吧。\x02\x03",

            "虽然以我一贯的性格来说，\x01",
            "对物品并不会有太多执著……\x02\x03",

            "#0202F但不可思议的是，\x01",
            "我一直都把这个带在身边呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x103, 500)

    #C0048
    ChrTalk(
        0x101,
        (
            "#12P#0005F这个不是来到这里\x01",
            "之后才买的吗？\x02\x03",

            "没记错的话，它好像是\x01",
            "克洛斯贝尔本地特有的吉祥物吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        (
            "#0204F#5P这是别人送给我的东西。\x02\x03",

            "大约是在五年前，从盖伊先生那里收到的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0050
    ChrTalk(
        0x101,
        "#12P#0011F#4S───哎？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x103,
        (
            "#0203F#5P盖伊·班宁斯……\x02\x03",

            "#0202F是罗伊德前辈的哥哥吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#12P#0008F哎、嗯，那个……\x01",
            "……当然了，不过……\x02\x03",

            "#0011F缇欧你──\x01",
            "曾经见过我的大哥吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#0204F#5P是的。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#12P#0006F我、我一直都不知道呢……\x02\x03",

            "#0002F什么啊，既然如此，\x01",
            "早点告诉我不就好了嘛！\x02\x03",

            "#0005F不过，缇欧好像是\x01",
            "从列曼自治州来的吧？\x02\x03",

            "为什么会和大哥──\x02",
        )
    )

    CloseMessageWindow()
    OP_C7(0x0, 0x800)
    FadeToDark(800, 0, -1)
    OP_C9(0x3, 0x3, 0xAAFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(300)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "说什么要出趟远门……\x01",
            "这也太突然了吧。\x02\x03",

            "你究竟要去哪里啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "雷米菲利亚公国。\x02\x03",

            "不过呢，虽说是出趟『远门』，\x01",
            "大概也只要两个月左右就能回来了吧。\x02\x03",

            "其实……\x01",
            "我要护送一位特别可爱的女孩，\x01",
            "和她一起去旅行啦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_END)), "loc_22C6")
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_C9(0x2, 0x3, 0xAAFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(300)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "缇欧……\x01",
            "你以前曾在这里住过院？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 130, -1, -1)
    SetChrName("")

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "……嗯。\x02\x03",

            "大约是在六年之前。\x02\x03",

            "关于这点，其实我并没\x01",
            "打算刻意向大家隐瞒……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Jump("loc_22E2")

    label("loc_22C6")

    FadeToBright(1000, 0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)

    label("loc_22E2")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x101,
        (
            "#12P#0005F那个女孩子难道……\x01",
            "就是缇欧吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        (
            "#0203F#5P多半是吧。\x02\x03",

            "#0202F那是在我九岁的时候……\x02\x03",

            "当时，我被盖伊先生\x01",
            "送回了位于雷米菲利亚的家中。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#12P#0002F雷米菲利亚……\x02\x03",

            "缇欧是出生在那里的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        (
            "#0202F#5P是的。\x02\x03",

            "#0204F话虽如此，对我来说，那里也\x01",
            "算不上什么有着深厚感情的故乡……\x02\x03",

            "只是一个几乎已经\x01",
            "完全舍弃的地方而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#0005F哎……\x02\x03",

            "#0001F那个，那缇欧的父母现在如何呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#0206F#5P我想，他们应该过得还好吧……\x02\x03",

            "虽然自从我三年前离开家之后，\x01",
            "就基本没有再和他们联络过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#12P#0001F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#0203F#5P──出于某些原因，\x01",
            "我从五岁左右开始，\x01",
            "就一直被认定为下落不明。\x02\x03",

            "之后得到了盖伊先生的保护……\x01",
            "身体衰弱的我，在乌尔斯拉\x01",
            "医院中住了半年左右的院。\x02\x03",

            "#0202F接着，等到身体康复以后……\x01",
            "就被送回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#12P#0003F是……这样啊……\x02\x03",

            "#0008F可是……好不容易回去了，\x01",
            "为什么要再次离家呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        "#0204F#5P呵呵……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x103, 0x20)

    def lambda_266D():
        OP_96(0xFE, 0x18ED4, 0xFA, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_266D)

    def lambda_2687():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2687)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    SetChrSubChip(0x103, 0x2)
    ClearChrFlags(0x103, 0x20)
    Sleep(500)

    #C0069
    ChrTalk(
        0x103,
        (
            "#0204F#5P──罗伊德前辈。\x02\x03",

            "#0202F相对普通人来说，我可以算是个异类。\x01",
            "你应该也明白吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x101,
        "#12P#0007F异、异类……！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#0202F#5P没关系，这是事实。\x02\x03",

            "#0203F对外界的事物与现象……\x01",
            "我拥有比普通人\x01",
            "强出数倍的感应能力。\x02\x03",

            "普通人听不见的微弱声音。\x02\x03",

            "普通人看不到的导力波流向。\x02\x03",

            "普通人无法感觉到的属性气息。\x02\x03",

            "#0208F#40W还有……连人的感情与内心波动都……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#12P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#0208F#5P即使去主日学校上课……\x01",
            "我也永远都是孤单一人。\x02\x03",

            "我眼中的万物，所感知的世界，\x01",
            "都和周围的孩子们不尽相同……\x02\x03",

            "而且，就连根本看不到的恶意与好奇心，\x01",
            "我也能清楚地感应到……\x02\x03",

            "#0206F父母虽然都很爱我，\x01",
            "……但终究也是有限度的吧。\x02\x03",

            "于是，家中的气氛日益紧张……\x01",
            "而我也终于察觉到了他们内心的真实想法……\x02\x03",

            "#0202F『啊──\x01",
            "  要是她没有回来就好了。』\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#12P#0013F！！……！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#0204F#5P等回过神来……\x01",
            "我就已经乘上了列车。\x02\x03",

            "乘上了那辆经过共和国，\x01",
            "开往克洛斯贝尔的列车。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#12P#0006F是吗……\x02\x03",

            "#0008F缇欧你……\x01",
            "是想来见我大哥的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#0208F#5P……或许吧。\x02\x03",

            "#0206F在把那个吉祥物当作\x01",
            "礼物送给我的时候，\x01",
            "盖伊先生曾经这样说过。\x02\x03",

            "#0202F『──放心吧，\x01",
            "　你一定会得到幸福的。』\x02\x03",

            "『如果没能如此，\x01",
            "　随时都可以把我叫来。』\x02\x03",

            "#0204F『我一定会将那些\x01",
            "　使你不幸的原因全部打飞的！』\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#12P#0012F哈哈，这还真是很像\x01",
            "大哥会说的话呢……\x02\x03",

            "#0008F……可是……\x01",
            "那个时候，大哥他刚刚……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#0203F#5P……………………（面色一沉）\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x103, 0x20)

    def lambda_2BCD():
        OP_96(0xFE, 0x18F9C, 0xFA, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BCD)

    def lambda_2BE7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2BE7)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x20)
    Sleep(500)

    #C0080
    ChrTalk(
        0x103,
        (
            "#0208F#5P──彻底迷失方向的我，\x01",
            "结识了爱普斯泰恩财团的人……\x02\x03",

            "我的感应能力被他们所看中，\x01",
            "在他们的招揽之下，就加入了\x01",
            "当时刚刚成立的魔导杖开发小组中。\x02\x03",

            "#0204F随后，就去了列曼自治州，\x01",
            "在财团的研究所中度过了三年时间……\x02\x03",

            "#0202F然后，就在三个月前，\x01",
            "再次回到了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        "#12P#0001F………缇欧……………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Fade(500)
    OP_68(202400, 1000, 0, 0)
    MoveCamera(310, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 202200, 0, -1700, 0)
    SetChrPos(0x103, 202400, 250, 0, 90)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x9, 203100, 750, -1300, 0)
    SetCameraDistance(19000, 1500)
    SetChrFlags(0x101, 0x4)

    def lambda_2DDA():
        OP_95(0xFE, 202200, 100, -400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DDA)
    Sleep(800)
    SetChrSubChip(0x103, 0x6)
    Sleep(150)
    SetChrSubChip(0x103, 0x7)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    Fade(250)
    SetChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0xA)
    OP_0D()
    SetChrSubChip(0x103, 0xB)
    Sleep(100)
    SetChrSubChip(0x103, 0xC)
    Sleep(100)
    SetChrSubChip(0x103, 0xD)
    Sleep(100)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x103, 0xE)
    Sleep(100)
    SetChrSubChip(0x103, 0xD)
    Sleep(100)
    SetChrSubChip(0x103, 0xC)
    Sleep(500)

    #C0082
    ChrTalk(
        0x103,
        "#0205F#5P#40W……啊………\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#6P#0006F……抱歉啊。\x01",
            "那个笨蛋大哥，竟然那么\x01",
            "突然地说走就走……\x02\x03",

            "#0008F对女孩子许诺下的约定都没能遵守，\x01",
            "真是……一点都不像大哥的作风……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#0208F#5P#40W………罗伊德前辈……………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(806, 2, 100, 0)
    Sleep(500)
    StopBGM(0x7D0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0x6)
    OP_0D()

    def lambda_2F77():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F77)
    Sleep(150)
    SetChrSubChip(0x103, 0x7)
    Sleep(300)

    #C0085
    ChrTalk(
        0x101,
        "#0005F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#0200F#5P……好像是约纳。\x02",
    )

    CloseMessageWindow()
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7524", 0)
    Sleep(300)

    #C0087
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P『小猫』出现了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P对方刚刚发现了\x01",
            "我准备的诱饵！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P现在就要进行追踪堵截了，\x01",
            "开始援助我！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        "#0203F#5P明白了。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#0003F#5P……我就只能站在一边看着了吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0092
    ChrTalk(
        0x101,
        (
            "#6P#0001F──缇欧，\x01",
            "一定不要太勉强啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        "#0202F#11P是的……不用担心。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x6)
    Sleep(100)
    SetChrSubChip(0x103, 0x5)
    Sleep(100)
    SetChrSubChip(0x103, 0x4)
    Sleep(100)
    SetChrSubChip(0x103, 0x3)
    Sleep(1000)
    SetChrSubChip(0x103, 0x4)
    Sleep(100)
    SetChrSubChip(0x103, 0x5)
    Sound(1278, 255, 100, 0)    #voice#Tio
    Sleep(1000)
    Sound(1280, 255, 100, 0)    #voice#Tio
    Sleep(1500)
    SetCameraDistance(18500, 3000)
    PlayEffect(0x0, 0x0, 0x103, 0x140, 0, 1250, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(840, 2, 100, 0)
    BeginChrThread(0x103, 3, 0, 10)
    Sound(850, 0, 100, 0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x348)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis122.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis043.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis044.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis045.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_68(302400, 1000, 0, 0)
    MoveCamera(310, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(0, 0)
    EndChrThread(0x103, 0x3)
    SetChrSubChip(0x103, 0x0)
    Sleep(500)

    #A0094
    AnonymousTalk(
        0x103,
        (
            "#0203F我这就开始在网络资源的\x01",
            "第二境界领域进行潜伏。\x02\x03",

            "#0200F等待『小猫』的到来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("约纳的声音")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "明白了，长官。\x02\x03",

            "嗯──喂喂，真的假的啊！？\x02\x03",

            "『小猫』那家伙……\x01",
            "已经把保护程序破解掉了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(905, 2, 100, 0)
    Sound(903, 0, 100, 0)
    OP_C9(0x1, 0x0, 0xFFFC0860, 0xFFFF8AD0, 0x0)
    OP_C9(0x1, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x1, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x1, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    SetChrName("约纳的声音")

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呜哇啊啊，我精心准备的\x01",
            "美味情报诱饵竟然在一瞬间就被……！\x02\x03",

            "难、难以置信……！\x01",
            "这究竟是怎么做到的啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0097
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0201F冷静一点，约纳。\x02\x03",

            "对方恐怕只是凭借压倒性的\x01",
            "处理能力来发起强行突破而已。\x02\x03",

            "#0203F不要着急，请做出领先对方两步的预测，\x01",
            "努力将其诱导到这边来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("约纳的声音")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可恶，你说得倒是轻松！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(904, 0, 100, 0)
    OP_C9(0x2, 0x0, 0xFFF97050, 0xFFFEEE90, 0x0)
    OP_C9(0x2, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x2, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("约纳的声音")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第４终端、第１７终端，\x01",
            "已经通过了市政厅的主终端……\x02",
        )
    )

    CloseMessageWindow()

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "已经将其逼至第２５终端了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(906, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis046.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis047.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis047.itp")
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("约纳的声音")

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "已经前往你那边的领域了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0102
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0202F──确认完毕。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(904, 0, 100, 0)
    OP_C9(0x0, 0x0, 0xFFFE0430, 0xFFFE2B40, 0x0)
    OP_C9(0x0, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x0, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x0, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    Sleep(500)
    SetMessageWindowPos(300, 140, -1, -1)

    #A0103
    AnonymousTalk(
        0x103,
        (
            "#0205F这就是『小猫』……\x02\x03",

            "动作确实很快……实在太快了……！\x02\x03",

            "#0201F『永世系统』解禁！\x01",
            "进入多线程并列处理……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1203, 255, 100, 0)    #voice#Tio
    Sleep(800)
    CreatePortrait(3, 0, 0, 480, 16, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x1, 0x0, 0xFFF97050, 0xFFFC5680, 0x0)
    OP_C9(0x1, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x1, 0x2, 0x0, 0x0, 0x0)
    OP_C9(0x2, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x2, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    Sound(907, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    CreatePortrait(0, 0, 256, 480, 272, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x2, 0x0, 0xFFF8FB20, 0xFFFF7748, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x1, 0x4, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x0, 0xFFFF15A0, 0xFFFD67F0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x1, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis117.itp")
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x0, 0x0)
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis048.itp")
    Sleep(500)
    SetChrName("约纳的声音")

    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这边也已经确认了──\x01",
            "哦哦！形势还不错嘛！\x02\x03",

            "照这样进展下去，仅靠你那边\x01",
            "就已经可以抓到『小猫』了吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 150, -1, -1)

    #A0105
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0206F不……和你或『小猫』不同，\x01",
            "我并不算是纯粹的黑客。\x02\x03",

            "『永世』一旦瘫痪，\x01",
            "我恐怕就无法再追上去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("约纳的声音")

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可恶，那该怎么办啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 150, -1, -1)

    #A0107
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0203F──做好系统瘫痪的准备，将处理速度提高到极限，\x01",
            "把『小猫』的一切退路彻底堵死。\x02\x03",

            "#0201F之后，『小猫』恐怕会\x01",
            "再次跳转到你那边的领域。\x02\x03",

            "请抓准时机，争取在\x01",
            "0.1秒之内将其捕获。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("约纳的声音")

    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊啊，真是的……\x01",
            "明白了，我试试总行了吧！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 90, -1, -1)

    #A0109
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0204F那么……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1281, 255, 100, 0)    #voice#Tio
    Sound(831, 0, 100, 0)
    Sound(506, 0, 100, 0)
    Sleep(2000)
    Sound(908, 0, 100, 0)
    FadeToDark(0, 16777215, -1)
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x4, 0x0, 0x0, 0x0)
    CreatePortrait(1, 0, 0, 480, 16, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sleep(1000)
    OP_C9(0x2, 0x0, 0xFFFC5680, 0xFFFF9E58, 0x0)
    OP_C9(0x2, 0x1, 0x5DC, 0x5DC, 0x0)
    OP_C9(0x3, 0x0, 0xFFFC5680, 0xFFFF9E58, 0x0)
    OP_C9(0x3, 0x1, 0x5DC, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_C9(0x2, 0x0, 0xFFFEA070, 0xFFFE5250, 0x5DC)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x3, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    Sleep(1000)
    FadeToBright(0, 16777215)
    OP_0D()
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis049.itp")
    Sound(903, 0, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    SetMessageWindowPos(200, 170, -1, -1)

    #A0110
    AnonymousTalk(
        0x103,
        "#0201F#4S──就是现在！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(907, 0, 100, 0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis118.itp")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis116.itp")
    OP_C9(0x1, 0x0, 0xFFF8AD00, 0xFFFD19D0, 0x0)
    OP_C9(0x1, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    CreatePortrait(2, 0, 0, 480, 16, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(3, 0, 256, 480, 272, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetMessageWindowPos(250, 150, -1, -1)
    SetChrName("约纳的声音")

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x18),
            "#4S#1K在那里——！！\x02",
        )
    )

    Sleep(1600)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(906, 0, 100, 0)
    Sound(813, 0, 100, 0)
    OP_24(0x389)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFD19D0, 0x0)
    OP_C9(0x0, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_C9(0x0, 0x1, 0x3E8, 0x3E8, 0x3E8)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x3E8)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFDCD8, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x2328, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFE0C0, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x1F40, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFE4A8, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x1B58, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFEC78, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x1388, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x0, 0x0)
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("约纳的声音")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好哇——！\x01",
            "抓住啦————！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(202400, 1000, 0, 0)
    MoveCamera(310, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 202200, 0, -1700, 45)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sound(840, 2, 100, 0)
    StopBGM(0x1770)

    #C0113
    ChrTalk(
        0x101,
        "#6P#0005F成、成功了吗……？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#0204F#5P#30W嗯……看起来，似乎是呢。\x02\x03",

            "#0208F#40W啊──\x02",
        )
    )

    CloseMessageWindow()
    StopEffect(0x0, 0x2)
    Sound(820, 0, 100, 0)
    OP_24(0x348)
    SetChrSubChip(0x103, 0x11)
    Sleep(150)
    SetChrSubChip(0x103, 0x12)
    Sleep(150)
    SetChrSubChip(0x103, 0x13)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_418F():
        OP_95(0xFE, 202200, 100, -400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_418F)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0x14)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0x103, 0x15)

    #C0115
    ChrTalk(
        0x101,
        "#6P#0007F没、没事吧！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1272, 255, 70, 0)    #voice#Tio
    Sleep(1000)

    #C0116
    ChrTalk(
        0x103,
        (
            "#5P#0206F#40W是、是的……\x02\x03",

            "可能是因为将处理能力提升得稍微\x01",
            "过了头，感觉有些头晕……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#0006F真是的……\x01",
            "都说过不要太勉强了嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    SetChrSubChip(0x103, 0x16)
    Sleep(130)
    SetChrSubChip(0x103, 0x17)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    SetChrSubChip(0x103, 0x19)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x103, 0x17)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    SetChrSubChip(0x103, 0x19)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    SetChrSubChip(0x103, 0x17)
    Sleep(300)
    SetChrSubChip(0x103, 0x1D)
    Sleep(100)
    SetChrSubChip(0x103, 0x1E)
    Sleep(300)

    #C0118
    ChrTalk(
        0x103,
        "#5P#0205F#30W啊……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#0003F──那个，缇欧。\x02\x03",

            "#0000F大哥和你做出的约定……\x01",
            "可不可以让我来继承呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x103,
        "#5P#0200F#30W哎──\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#6P#0008F『如果你没能得到幸福，\x01",
            "　随时都可以把我叫来……』\x02\x03",

            "『我会将那些使你不幸的原因\x01",
            "　全部打飞……』\x02\x03",

            "#0006F……虽然有些不甘心，但大哥确实很了不起。\x02\x03",

            "实力也好，行动力也好，都很惊人。\x01",
            "而我却难以望其项背。\x02\x03",

            "#0000F──可是我……一定会努力的。\x02\x03",

            "努力成为一名可靠的男子汉，\x01",
            "至少要把这条约定遵守下去。\x02\x03",

            "所以……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1E)
    Sleep(100)
    SetChrSubChip(0x103, 0x1D)
    Sleep(100)
    SetChrSubChip(0x103, 0x1C)
    Sleep(500)

    #C0122
    ChrTalk(
        0x103,
        (
            "#5P#0204F#30W……………………………………\x02\x03",

            "呵呵……真是不可思议呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#5P#0204F罗伊德前辈和盖伊先生\x01",
            "明明一点都不像……\x02\x03",

            "可是，却总感觉你们\x01",
            "的某些地方又很相似。\x02\x03",

            "该说是灵魂的本质很相似吗……\x01",
            "还是该说，你们都在注视同一个方向呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#6P#0005F我和……大哥吗……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1C)
    Sleep(100)
    SetChrSubChip(0x103, 0x1D)
    Sleep(100)
    SetChrSubChip(0x103, 0x1E)
    Sleep(300)

    #C0126
    ChrTalk(
        0x103,
        (
            "#5P#0202F是的。\x02\x03",

            "#0204F不过──你们果然还是不同的。\x02\x03",

            "罗伊德前辈就是罗伊德前辈，\x01",
            "和盖伊先生并不一样。\x02\x03",

            "#0201F关于这一点，罗伊德前辈\x01",
            "自己应该最清楚不过了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#6P#0008F……这个………\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        (
            "#5P#0204F──所以说。\x02\x03",

            "如果一定要做个约定，\x01",
            "内容也换成不同的比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0129
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_4752():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4752)
    Fade(250)
    SetChrSubChip(0x103, 0xA)
    OP_0D()
    Sleep(500)

    #C0130
    ChrTalk(
        0x103,
        (
            "#11P#0202F这个约定……\x01",
            "并不一定要马上做出。\x02\x03",

            "但前辈与我约定的内容，\x01",
            "一定要是自己想出来的……\x02\x03",

            "#0204F等你想到之后，再做约定也不迟。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#6P#0002F缇欧……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x103,
        (
            "#11P#0206F还有……\x01",
            "我已经不是小孩子了。\x02\x03",

            "我不喜欢被单方面保护，\x01",
            "也讨厌一味向别人索取。\x02\x03",

            "#0201F我……\x01",
            "也和大家一样，是支援科的一员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#6P#0002F……是啊。\x02\x03",

            "#0014F哈哈，确实如你所说。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        "#11P#0209F……呵呵………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0135
    ChrTalk(
        0x101,
        "#6P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#11P#0205F？？？\x02\x03",

            "怎么了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#6P#0011F没什么，那个……\x02\x03",

            "#0012F只是在想，好像还是第一次\x01",
            "看到你露出如此发自内心的笑容呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    #C0138
    ChrTalk(
        0x103,
        (
            "#11P#0206F我、我才没有笑……！\x02\x03",

            "#0208F这只是，那个……\x01",
            "只是因为松了一口气而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#6P#0004F哈哈，不用害羞啊。\x02\x03",

            "#0002F嗯～不过，还真是可惜呢。\x02\x03",

            "缇欧本来就非常可爱，如果平时能\x01",
            "多笑一笑，大概会很受欢迎吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#11P#0205F非、非常可爱……\x02\x03",

            "#0211F……～～～！～～～……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0141
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P那个～咳咳。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0x6)

    def lambda_4B35():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B35)
    SetChrSubChip(0x103, 0x7)
    Sleep(300)

    #C0142
    ChrTalk(
        0x101,
        "#0005F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#11P#0205F约、约纳！？\x02\x03",

            "#0201F你、你、你从什么时候\x01",
            "就开始偷听了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P那个，好像是从什么第一次露出笑脸～\x01",
            "之类的地方开始的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P哈哈，好像无意中听到了些\x01",
            "稀罕的内容呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P真没想到，你竟然\x01",
            "也会那样慌张害羞啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#11P#0211F……如果再敢继续说这些废话，\x01",
            "下次玩『波波碰』的时候就赏你四十连击。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P那根本就不可能做得到吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#6P不过话说回来，如果是你的话，\x01",
            "说不定还真能做到……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 11)
    WaitChrThread(0x101, 3)
    Fade(500)
    OP_68(103000, 1000, 0, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 101200, 0, -1700, 90)
    SetChrPos(0x103, 102300, 250, 0, 90)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x2)
    SetChrPos(0x9, 102600, 700, -1500, 0)
    OP_0D()

    #C0150
    ChrTalk(
        0x101,
        (
            "#6P#0001F那么，约纳。\x02\x03",

            "『小猫』的真实身份，\x01",
            "已经查明了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P哈，你以为\x01",
            "本少爷是谁啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P早就顺利掌握到对方的入侵地址了，\x01",
            "现在立刻就把情报发送给你们。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(824, 0, 100, 0)
    Sleep(500)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x0)

    def lambda_4E58():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E58)
    Sleep(500)

    #C0153
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#0205F#6P……？\x02\x03",

            "好像还带着奇怪\x01",
            "的附件文档呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P附件文档～？\x01",
            "──那是什么东西啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P我发过去的只是含有对方地址的进程记录而已，\x01",
            "为什么会添加了那种东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#0201F打开看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(850, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 10)
    Sleep(1200)
    EndChrThread(0x103, 0x3)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0157
    ChrTalk(
        0x103,
        "#6P#0205F哎……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#6P#0013F这是……！？\x02",
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis123.itp")
    CreatePortrait(1, 112, 64, 368, 192, 0, 0, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x1, "c_vis050.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    SetChrName("约纳的声音")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这、这、这东西是什么啊～！？\x02\x03",

            "稍、稍等一下！\x02\x03",

            "这个……莫非是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0160
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0206F我们好像遭到了入侵攻击呢，大概是\x01",
            "对方被查到地址之后，对这边做出的回敬吧。\x02\x03",

            "#0208F不……也许……\x01",
            "我们从一开始就被对方玩弄于股掌。\x02\x03",

            "#0201F那么，我们掌握到的\x01",
            "很有可能只是假情报而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("约纳的声音")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呜（晕过去）……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x103, 3, 0, 14)
    Sound(819, 0, 90, 0)
    Sound(514, 0, 70, 0)
    Sleep(1000)
    SetChrSubChip(0x103, 0x2)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)

    #C0162
    ChrTalk(
        0x101,
        "#6P#0011F喂～你没事吧？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#2S呜……\x01",
            "在那种情况下还能对地址进行伪造，\x01",
            "这种事再怎么说也不可能做到啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#2S既然如此，只要对地址进行解析，\x01",
            "总能把对方的链接点给……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#2S……不，但是……（自言自语）……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x101,
        "#6P#0012F喂～……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetMapObjFrame(0x3, "m00gim02", 0x2, "close")
    Sound(73, 0, 100, 0)
    Sleep(800)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrPos(0x103, 101800, 0, 800, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    TurnDirection(0x103, 0x101, 400)

    #C0167
    ChrTalk(
        0x103,
        (
            "#0206F#5P算了，不用管他。\x01",
            "我们先回他那里再说吧。\x02\x03",

            "#0202F还要去收取作为报酬的\x01",
            "记录结晶呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0168
    ChrTalk(
        0x101,
        (
            "#12P#0000F啊……对了，当时还说过这个呢。\x02\x03",

            "结果发生了这么多的事情，\x01",
            "我完全都忘了……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#0204F#5P呵呵……\x02\x03",

            "#0202F这附近应该有通向出口位置的\x01",
            "紧急升降机。\x02\x03",

            "将它启动，然后回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#12P#0002F嗯，就这么办。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_68(100000, 2000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 100000, 0, 0, 270)
    SetChrPos(0x1, 100000, 0, 0, 270)
    SetScenarioFlags(0xA1, 3)
    OP_29(0x45, 0x1, 0x4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7300", 0)
    OP_24(0x326)
    OP_24(0x348)
    OP_24(0x389)
    EventEnd(0x5)
    Return()

    # Function_9_11F2 end

    def Function_10_5537(): pass

    label("Function_10_5537")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5563")
    SetChrSubChip(0x103, 0x0)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    SetChrSubChip(0x103, 0x2)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    Jump("Function_10_5537")

    label("loc_5563")

    Return()

    # Function_10_5537 end

    def Function_11_5564(): pass

    label("Function_11_5564")


    def lambda_5569():
        OP_95(0xFE, 202200, 0, -1700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5569)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x190)
    ClearChrFlags(0x101, 0x4)
    Return()

    # Function_11_5564 end

    def Function_12_558F(): pass

    label("Function_12_558F")

    Sleep(1000)
    OP_C9(0x3, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_12_558F end

    def Function_13_55EE(): pass

    label("Function_13_55EE")

    Sleep(300)
    OP_C9(0x2, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_13_55EE end

    def Function_14_564D(): pass

    label("Function_14_564D")

    Sleep(300)
    OP_C9(0x0, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    OP_C9(0x1, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    OP_C9(0x1, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    OP_C9(0x1, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0x640, 0xFFFFFB50, 0x1)
    OP_C9(0x1, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_14_564D end

    def Function_15_56F7(): pass

    label("Function_15_56F7")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5782")

    #C0171
    ChrTalk(
        0x103,
        (
            "#0200F罗伊德前辈，\x01",
            "『第３控制终端』在右边的门内。\x02\x03",

            "快点将它启动，\x01",
            "然后在原地待命吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#0005F啊，说得也是呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_57E0")

    label("loc_5782")


    #C0173
    ChrTalk(
        0x103,
        (
            "#0203F……『第３控制终端』是在\x01",
            "右边的门内吧。\x02\x03",

            "#0200F必须要快点启动它，\x01",
            "然后在原地待命。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57E0")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 6540, 180)
    EventEnd(0x4)
    Return()

    # Function_15_56F7 end

    def Function_16_57F7(): pass

    label("Function_16_57F7")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5855")

    #C0174
    ChrTalk(
        0x101,
        (
            "#0005F啊……这附近应该\x01",
            "有一部紧急升降机呢。\x02\x03",

            "#0000F还是乘它离开吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A8")

    label("loc_5855")


    #C0175
    ChrTalk(
        0x103,
        (
            "#0203F……附近应该有一部\x01",
            "通向出口位置的紧急升降机。\x02\x03",

            "#0200F还是去乘坐那个吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58A8")

    Sleep(50)
    OP_68(0, 0, -8290, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    SetChrPos(0x0, 0, 0, -8290, 0)
    EventEnd(0x4)
    Return()

    # Function_16_57F7 end

    def Function_17_58ED(): pass

    label("Function_17_58ED")

    TalkBegin(0xFF)
    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "终端的导力已经停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_17_58ED end

    SaveToFile()

Try(main)
