from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "a0004.bin",                # FileName
        "a0000",                    # MapName
        "a0004",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -62000, 8000, -38000, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0004",                  # 0
        "bm1010",                 # 1
        "bm1010",                 # 2
        "bm1010",                 # 3
    ))

    ATBonus("ATBonus_22C", 100, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    Sepith("Sepith_7E9", 1,   2,   3,   4,   5,   6,   7)
    Sepith("Sepith_7F1", 10,  20,  30,  40,  50,  60,  70)

    MonsterBattlePostion("MonsterBattlePostion_23C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_240", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_244", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_248", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_24C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_254", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_258", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 5, 5, 45)

    # monster count: 4

    BattleInfo(
        "BattleInfo_33C", 0x0000, 14, 6, 90, 0, 1, 25, 0, "bm1010", "Sepith_7E9", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, "ms60000.dat", "ms60000.dat", "MonsterBattlePostion_23C", "MonsterBattlePostion_2BC", "ed7400", "ed7403", "ATBonus_22C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_380", 0x0010, 14, 6, 90, 6, 1, 25, 0, "bm1010", "Sepith_7F1", 100, 0, 0, 0,
        (
            ("ms67000.dat", "ms67000.dat", "ms60000.dat", "ms63200.dat", 0, 0, "ms63100.dat", 0, "MonsterBattlePostion_23C", "MonsterBattlePostion_2BC", "ed7400", "ed7403", "ATBonus_22C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3C4", 0x0C00, 14, 6, 90, 6, 0, 25, 0, "bm1010", "Sepith_7F1", 100, 0, 0, 0,
        (
            ("ms67000.dat", "ms67000.dat", "ms60000.dat", "ms63200.dat", 0, 0, "ms63100.dat", 0, "MonsterBattlePostion_23C", "MonsterBattlePostion_2BC", "ed7400", "ed7403", "ATBonus_22C"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

    AddCharChip((
        "monster/ch60050.itc",               # 00
        "monster/ch60051.itc",               # 01
    ))

    DeclMonster(-30380,  -36260,  8000,    0x1010032,    "BattleInfo_33C", 0,   0,   0xFFFF, 0,  1)
    DeclMonster(-24870,  -41100,  8000,    0x1010032,    "BattleInfo_380", 0,   0,   0xFFFF, 0,  1)
    DeclMonster(-34610,  -42130,  8000,    0x1010032,    "BattleInfo_380", 0,   0,   0xFFFF, 0,  1)
    DeclMonster(-55840,  -42350,  8000,    0x18100E6,    "BattleInfo_3C4", 0,   0,   0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 3,   -54.68000030517578,    -33.95000076293945,    6.0,                   16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   13.670000076293945,    16.975000381469727,    -2.0,                  1.0])
    DeclEvent(0x0000, 0, 2,   -55.349998474121094,   -44.880001068115234,   8.0,                   16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   13.837499618530273,    22.440000534057617,    -2.6666667461395264,   1.0])

    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 0
    ChipFrameInfo(5000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_43C",          # 00, 0
        "Function_1_451",          # 01, 1
        "Function_2_4D4",          # 02, 2
        "Function_3_6F6",          # 03, 3
        "Function_4_730",          # 04, 4
        "Function_5_741",          # 05, 5
        "Function_6_745",          # 06, 6
    ))


    def Function_0_43C(): pass

    label("Function_0_43C")

    LoadEffect(0x0, "battle\\com002.eff")
    Return()

    # Function_0_43C end

    def Function_1_451(): pass

    label("Function_1_451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465")
    ClearChrFlags(0xB, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_465")

    PlayEffect(0x1D, 0xFF, 0x9, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0xFF, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_451 end

    def Function_2_4D4(): pass

    label("Function_2_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 0)), scpexpr(EXPR_END)), "loc_4DE")
    Return()

    label("loc_4DE")

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
        (1, "loc_5AA"),
        (SWITCH_DEFAULT, "loc_5C1"),
    )


    label("loc_5AA")

    Sleep(500)
    OP_90(0x0, -55350, 8000, -44880, 0)
    EventEnd(0x5)
    Return()

    label("loc_5C1")

    Battle("BattleInfo_3C4", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-55350, 9000, -44880, 0)
    OP_90(0x0, -55350, 8000, -44880, 0)
    OP_90(0x1, -55350, 8000, -44880, 0)
    OP_90(0x2, -55350, 8000, -44880, 0)
    OP_90(0x3, -55350, 8000, -44880, 0)
    OP_90(0x4, -55350, 8000, -44880, 0)
    OP_90(0x5, -55350, 8000, -44880, 0)
    OP_90(0x6, -55350, 8000, -44880, 0)
    OP_90(0x7, -55350, 8000, -44880, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_683"),
        (1, "loc_686"),
        (SWITCH_DEFAULT, "loc_689"),
    )


    label("loc_683")

    EventEnd(0x5)
    Return()

    label("loc_686")

    OP_B7(0x0)
    Return()

    label("loc_689")

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
    SetScenarioFlags(0x78, 0)
    OP_29(0x25, 0x4, 0x10)
    OP_29(0x25, 0x4, 0x2)
    OP_29(0x25, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_2_4D4 end

    def Function_3_6F6(): pass

    label("Function_3_6F6")

    Sleep(2000)
    Call(0, 4)
    EventBegin(0x0)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40019.itc", 0xC)
    OP_E0(0x1)
    Sound(1000, 255, 100, 0)    #voice#Lloyd

    #C0003
    ChrTalk(
        0x101,
        "#12P#001F这里是……\x02",
    )

    CloseMessageWindow()
    OP_E0(0x0)
    EventEnd(0x0)
    Return()

    # Function_3_6F6 end

    def Function_4_730(): pass

    label("Function_4_730")

    LoadChrToIndex("chr/ch40020.itc", 0xD)
    Sound(1001, 0, 100, 0)    #voice#Lloyd
    WaitChrThread(0x102, 3)
    Return()

    # Function_4_730 end

    def Function_5_741(): pass

    label("Function_5_741")

    Sleep(10000)
    Return()

    # Function_5_741 end

    def Function_6_745(): pass

    label("Function_6_745")

    Call(0, 5)
    OutputDebugInt(0x6F)

    def lambda_74F():
        OP_96(0xFE, 0x3E98F, 0x0, 0x107AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74F)
    Sleep(300)

    def lambda_76C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_76C)
    WaitChrThread(0x102, 1)
    Sleep(1500)

    def lambda_780():
        OP_96(0xFE, 0x3E98F, 0x0, 0x10428, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_780)
    WaitChrThread(0x102, 1)

    def lambda_79E():
        OP_93(0x102, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_79E)
    WaitChrThread(0x102, 2)

    def lambda_7AF():
        OP_93(0x102, 0xB5, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7AF)
    WaitChrThread(0x102, 2)
    Sleep(1500)
    OutputDebugInt(0xDE)
    Return()

    # Function_6_745 end

    SaveToFile()

Try(main)
