from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t160b.bin",                # FileName
        "t160b",                    # MapName
        "t160b",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 0, 0, 1],
    )

    BuildStringList((
        "t160b",                  # 0
        "实习医生利顿",           # 1
        "狗１",                   # 2
        "狗２",                   # 3
        "狗３",                   # 4
        "塞茜尔",                 # 5
        "米海尔",                 # 6
        "事件用魔兽",             # 7
        "事件用魔兽",             # 8
        "事件用魔兽",             # 9
        "事件用魔兽",             # 10
        "盖里教授",               # 11
        "阿修拉主任",             # 12
        "拉格教授",               # 13
        "bt160b",                 # 14
        "乌尔斯拉间道",           # 15
    ))

    ATBonus("ATBonus_2CC", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_38C", 4, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 9, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_370", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_374", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_378", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_37C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_380", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_384", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_3AC", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt160b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_38C", "MonsterBattlePostion_36C", "ed7402", "ed7403", "ATBonus_2CC"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 7,   5.5,                   10.5,                  6.0,                   625.0,                 [0.14142131805419922,  0.07071070373058319,   -0.0,                  0.0,                   -0.14142140746116638,  0.07071065902709961,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.7071075439453125,    -1.1313707828521729,   -1.2000000476837158,   1.0])

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ScpFunction((
        "Function_0_43C",          # 00, 0
        "Function_1_488",          # 01, 1
        "Function_2_517",          # 02, 2
        "Function_3_98C",          # 03, 3
        "Function_4_9AB",          # 04, 4
        "Function_5_9CA",          # 05, 5
        "Function_6_A18",          # 06, 6
        "Function_7_A56",          # 07, 7
        "Function_8_14D5",         # 08, 8
        "Function_9_154B",         # 09, 9
        "Function_10_1563",        # 0A, 10
        "Function_11_158D",        # 0B, 11
        "Function_12_162C",        # 0C, 12
        "Function_13_16EA",        # 0D, 13
        "Function_14_1BC0",        # 0E, 14
        "Function_15_239F",        # 0F, 15
        "Function_16_23C5",        # 10, 16
        "Function_17_2953",        # 11, 17
        "Function_18_2A1F",        # 12, 18
    ))


    def Function_0_43C(): pass

    label("Function_0_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_450")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_487")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_464")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 13)
    Jump("loc_487")

    label("loc_464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_478")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 14)
    Jump("loc_487")

    label("loc_478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_487")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 16)

    label("loc_487")

    Return()

    # Function_0_43C end

    def Function_1_488(): pass

    label("Function_1_488")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4E2")
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    Jump("loc_516")

    label("loc_4E2")

    SetMapObjFrame(0xFF, "model6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x2)

    label("loc_516")

    Return()

    # Function_1_488 end

    def Function_2_517(): pass

    label("Function_2_517")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xA0, 0xA0, 0xF0, 0x0, 0x0)
    LoadChrToIndex("chr/ch29400.itc", 0x1E)
    LoadChrToIndex("monster/ch75650.itc", 0x1F)
    LoadChrToIndex("monster/ch75652.itc", 0x20)
    LoadChrToIndex("monster/ch75651.itc", 0x21)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_68(18820, 8000, -18070, 0)
    MoveCamera(36, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, -1500, 7000, 23500, 180)
    SetChrPos(0x1, -1500, 7000, 23500, 180)
    SetChrPos(0x2, -1500, 7000, 23500, 180)
    SetChrPos(0x3, -1500, 7000, 23500, 180)
    SetChrPos(0x4, -1500, 7000, 23500, 180)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 18380, 7000, -15790, 180)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 19450, 7000, -13130, 180)
    OP_A7(0x9, 0x37, 0x37, 0x37, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 16920, 7000, -13390, 180)
    OP_A7(0xA, 0x37, 0x37, 0x37, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 19540, 7000, -10010, 180)
    OP_A7(0xB, 0x37, 0x37, 0x37, 0x0, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    Sleep(500)

    #A0001
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "这份实习报告要交给\x01",
            "拉格教授，他可是以难伺候\x01",
            "而闻名的。\x02\x03",

            "我是全神贯注地\x01",
            "熬夜写完的。\x01",
            "说实话，当时连意识都已经朦胧了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    SetCameraDistance(28000, 3000)

    def lambda_772():
        OP_95(0xFE, 18670, 7000, -18200, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_772)
    Sleep(1000)
    SetChrName("实习医生利顿")

    #A0002
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "而意识虽然已经有些朦胧，\x01",
            "但总觉得很兴奋……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)
    OP_6F(0x10)
    OP_0D()

    #A0003
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "在这种状态下去吹晚风，\x01",
            "……结果就听到了那个声音。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(836, 0, 100, 0)
    Sleep(800)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)
    OP_68(18220, 8000, -16770, 1500)
    SetCameraDistance(26500, 1500)

    def lambda_851():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_851)
    WaitChrThread(0x8, 1)
    BeginChrThread(0x9, 3, 0, 5)
    BeginChrThread(0xA, 3, 0, 5)
    BeginChrThread(0xB, 3, 0, 5)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_89E():
        OP_96(0xFE, 0x495C, 0x1B58, 0xFFFFB672, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_89E)
    WaitChrThread(0x8, 1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0x9, 3, 0, 6)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 6)
    Sleep(100)
    Sound(814, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 6)
    FadeToDark(0, -1, 0)
    FadeToDark(1000, 16777215, -1)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xC)
    SetCameraDistance(15000, 1000)
    OP_68(18820, 8000, -18070, 1000)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetScenarioFlags(0x5C, 2)
    NewScene("t1540", 0, 20, 0)
    IdleLoop()
    Return()

    # Function_2_517 end

    def Function_3_98C(): pass

    label("Function_3_98C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9AA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_3_98C")

    label("loc_9AA")

    Return()

    # Function_3_98C end

    def Function_4_9AB(): pass

    label("Function_4_9AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C9")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_4_9AB")

    label("loc_9C9")

    Return()

    # Function_4_9AB end

    def Function_5_9CA(): pass

    label("Function_5_9CA")

    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_9D5():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D5)

    def lambda_9EA():
        OP_A7(0xFE, 0x37, 0x37, 0x37, 0xFF, 0x2BC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9EA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 3)
    Return()

    # Function_5_9CA end

    def Function_6_A18(): pass

    label("Function_6_A18")

    SetChrChipByIndex(0xFE, 0x20)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0x495C, 0x1B58, 0xFFFFB672, 0xBB8, 0x1388)
    Return()

    # Function_6_A18 end

    def Function_7_A56(): pass

    label("Function_7_A56")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("chr/ch34000.itc", 0x1F)
    LoadChrToIndex("monster/ch75750.itc", 0x20)
    LoadChrToIndex("monster/ch75750.itc", 0x21)
    LoadChrToIndex("monster/ch75750.itc", 0x22)
    LoadChrToIndex("chr/ch00050.itc", 0x23)
    LoadChrToIndex("chr/ch00051.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00151.itc", 0x26)
    LoadChrToIndex("chr/ch00250.itc", 0x27)
    LoadChrToIndex("chr/ch00251.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("chr/ch00351.itc", 0x2A)
    LoadChrToIndex("chr/ch00550.itc", 0x2B)
    LoadChrToIndex("chr/ch00551.itc", 0x2C)
    LoadChrToIndex("chr/ch00052.itc", 0x2D)
    LoadEffect(0x0, "event\\ev606_00.eff")
    LoadEffect(0x1, "battle\\ms00001.eff")
    OP_68(7160, 8000, 9090, 0)
    MoveCamera(15, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26750, 0)
    SetChrPos(0x101, 6200, 7000, 10440, 135)
    SetChrPos(0x102, 5570, 7000, 12240, 135)
    SetChrPos(0x103, 4770, 7000, 10160, 135)
    SetChrPos(0x104, 3860, 7000, 12290, 135)
    SetChrPos(0x106, 4720, 7000, 13350, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 18630, 7000, -14670, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 19630, 7000, -15010, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x20)
    SetChrPos(0xE, 21060, 7000, -10800, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    TurnDirection(0xE, 0xC, 0)
    OP_9B(0x1, 0xE, 0x0, 0xFFFFFE0C, 0xEA60, 0x0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0xF, 0x20)
    SetChrPos(0xF, 16600, 7500, -12300, 135)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    TurnDirection(0xF, 0xC, 0)
    OP_9B(0x1, 0xF, 0x0, 0xFFFFFE0C, 0xEA60, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x20)
    SetChrPos(0x10, 15620, 7000, -14850, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    TurnDirection(0x10, 0xC, 0)
    OP_9B(0x1, 0x10, 0x0, 0xFFFFFE0C, 0xEA60, 0x0)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x20)
    SetChrPos(0x11, 16760, 7000, -18190, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    TurnDirection(0x11, 0xC, 0)
    OP_9B(0x1, 0x11, 0x0, 0xFFFFFE0C, 0xEA60, 0x0)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 0, 0, 9)
    Sleep(10)
    BeginChrThread(0xF, 0, 0, 9)
    Sleep(10)
    BeginChrThread(0x10, 0, 0, 9)
    Sleep(10)
    BeginChrThread(0x11, 0, 0, 9)
    FadeToBright(1000, 0)
    SetCameraDistance(25250, 1500)

    def lambda_D3A():
        OP_95(0xFE, 7150, 7000, 9240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D3A)

    def lambda_D54():
        OP_95(0xFE, 6870, 7000, 10580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D54)
    Sleep(50)

    def lambda_D71():
        OP_95(0xFE, 5710, 7000, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D71)

    def lambda_D8B():
        OP_95(0xFE, 5030, 7000, 10760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D8B)
    Sleep(50)

    def lambda_DA8():
        OP_95(0xFE, 5980, 7000, 11680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_DA8)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    #Sound(1089, 255, 100, 0)    #voice#Lloyd

    #C0004
    ChrTalk(
        0x101,
        "#0013F#5P那是……！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        "#0307F#5P喂，不妙啊……！\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_68(17880, 7900, -13870, 3000)
    MoveCamera(60, 19, 0, 3000)
    SetCameraDistance(26250, 3000)
    OP_6F(0x79)
    Sound(835, 0, 100, 0)

    def lambda_EC4():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_EC4)
    Sleep(200)

    def lambda_EDC():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_EDC)
    Sleep(100)

    def lambda_EF4():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_EF4)
    Sleep(160)

    def lambda_F0C():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F0C)
    Sleep(500)

    def lambda_F24():
        OP_96(0xFE, 0x4B14, 0x1B58, 0xFFFFC626, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F24)
    Sleep(300)

    def lambda_F41():
        OP_96(0xFE, 0x4E3E, 0x1B58, 0xFFFFC504, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F41)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)

    def lambda_F73():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F73)
    Sleep(500)

    #C0006
    ChrTalk(
        0xD,
        (
            "#11P呜……\x01",
            "塞茜尔姐姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xC,
        (
            "#1304F#5P别怕，没关系的。\x02\x03",

            "#1301F来，抓紧我。\x02\x03",

            "我们一口气逃进病房楼去。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xD,
        "#11P嗯、嗯……！\x02",
    )

    CloseMessageWindow()
    OP_68(18420, 7900, -13900, 2000)
    SetCameraDistance(23250, 10000)

    def lambda_102B():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_102B)
    Sleep(160)

    def lambda_1043():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1043)
    Sleep(100)

    def lambda_105B():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_105B)
    Sleep(200)

    def lambda_1073():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1073)
    SetCameraDistance(23250, 10000)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    Sleep(1000)

    #C0009
    ChrTalk(
        0xC,
        (
            "#1301F#11P（……要想两人一起逃脱似乎很难了。）\x02\x03",

            "（但是，顺利的话……\x01",
            "  至少能把这孩子送进建筑物里面……）\x02\x03",

            "#1303F（爸爸，妈妈，伊莉娅……）\x02\x03",

            "#1308F（罗伊德，盖伊……\x01",
            "  ………对不起………！）\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 16800, 7000, -7900, 135)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0010
    ChrTalk(
        0x101,
        "#0007F#4S#2P塞茜尔姐姐！！\x02",
    )

    CloseMessageWindow()
    OP_64(0xC)
    OP_64(0xD)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_11F6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11F6)

    def lambda_1203():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1203)
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    Fade(500)
    SetChrPos(0xF, 16920, 7000, -11530, 135)
    SetChrPos(0x11, 17850, 7000, -18160, 0)
    OP_68(19250, 8000, -14850, 0)
    MoveCamera(325, 35, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(21000, 1000)
    OP_6F(0x79)
    OP_0D()
    BeginChrThread(0xC, 3, 0, 12)
    BeginChrThread(0x11, 3, 0, 10)
    Sleep(400)
    BeginChrThread(0xE, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x10, 3, 0, 10)
    BeginChrThread(0xF, 3, 0, 10)
    WaitChrThread(0x10, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0xC, 3)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x27)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x2B)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x101, 13900, 7000, -5430, 135)
    SetChrPos(0x102, 14960, 7000, -4030, 135)
    SetChrPos(0x103, 11490, 7000, -6790, 135)
    SetChrPos(0x104, 9360, 7000, -6960, 135)
    SetChrPos(0x106, 11980, 7000, -4590, 135)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(16900, 7900, -11490, 1000)
    MoveCamera(325, 15, 0, 1000)
    BeginChrThread(0x101, 3, 0, 8)

    def lambda_135C():
        OP_95(0xFE, 17280, 7000, -8620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_135C)

    def lambda_1376():
        OP_95(0xFE, 13910, 7000, -10360, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1376)

    def lambda_1390():
        OP_95(0xFE, 12240, 7000, -12520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1390)

    def lambda_13AA():
        OP_95(0xFE, 13940, 7000, -8820, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_13AA)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    #C0011
    ChrTalk(
        0xC,
        "#1305F#6P罗、罗伊德……！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xD,
        "#12P警察局的哥哥姐姐……！？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0007F#11P有话之后再说！\x01",
            "先击退这些家伙！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0707F#5P注意不要\x01",
            "被卷进来……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    Battle("BattleInfo_3AC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    Call(0, 13)
    Return()

    # Function_7_A56 end

    def Function_8_14D5(): pass

    label("Function_8_14D5")


    def lambda_14DA():
        OP_9D(0xFE, 0x3F48, 0x1B58, 0xFFFFD6DE, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14DA)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x1F4)
    ClearChrFlags(0xFE, 0x1)
    Sound(1015, 255, 100, 0)    #voice#Lloyd
    Sleep(450)
    Sound(854, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x2, 0x3)
    BeginChrThread(0xF, 3, 0, 11)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x6)
    SetChrFlags(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xF, 3)
    Return()

    # Function_8_14D5 end

    def Function_9_154B(): pass

    label("Function_9_154B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1562")
    OP_A0(0xFE, 1250, 0x0, 0xFB)
    Jump("Function_9_154B")

    label("loc_1562")

    Return()

    # Function_9_154B end

    def Function_10_1563(): pass

    label("Function_10_1563")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1574():
        OP_A6(0xFE, 0x0, 0x50, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1574)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_1563 end

    def Function_11_158D(): pass

    label("Function_11_158D")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 17000, 8300, -12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x12C)
    Sound(816, 0, 100, 0)
    Sound(246, 0, 100, 0)

    def lambda_15E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_15E6)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)

    def lambda_15FF():
        OP_A6(0xFE, 0x0, 0x50, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15FF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 0)
    Sound(514, 0, 100, 0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_11_158D end

    def Function_12_162C(): pass

    label("Function_12_162C")

    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 18190, 7000, -16430, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 19120, 7000, -12070, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    Sleep(100)
    Sound(530, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 16560, 7000, -13120, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_12_162C end

    def Function_13_16EA(): pass

    label("Function_13_16EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("chr/ch34000.itc", 0x1F)
    OP_68(17410, 8000, -12880, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 16810, 7000, -12960, 90)
    SetChrPos(0x102, 16100, 7000, -11900, 90)
    SetChrPos(0x103, 15080, 7000, -14420, 90)
    SetChrPos(0x104, 14290, 7000, -13590, 90)
    SetChrPos(0x106, 13800, 7000, -12240, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 19310, 7000, -13460, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 19340, 7000, -14290, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(23500, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0015
    ChrTalk(
        0xC,
        (
            "#1302F#11P罗伊德……还有大家。\x02\x03",

            "#1304F谢谢……\x01",
            "真不知道该怎么谢你们才好。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#0302F#6P哪里哪里！\x01",
            "道谢什么的，也太见外啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        "#0102F#6P二位平安无事就好。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        "#0204F#6P……还好赶上了。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008F#6P你没事……真是太好了。\x02\x03",

            "#0006F塞茜尔姐姐要是出了什么事，\x01",
            "我可该如何向大哥交代啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xC,
        "#1305F#11P罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    def lambda_199E():
        OP_A6(0xFE, 0x0, 0x14, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_199E)

    #C0022
    ChrTalk(
        0xD,
        "#11P#40W咳、咳咳……\x02",
    )

    CloseMessageWindow()
    OP_64(0xD)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0023
    ChrTalk(
        0x101,
        "#0005F#6P没、没事吧……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    #C0024
    ChrTalk(
        0xC,
        (
            "#1303F#5P似乎开始发作了……\x02\x03",

            "#1300F米海尔，回房间\x01",
            "去吃药吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 400)
    Sleep(300)

    #C0025
    ChrTalk(
        0xD,
        "#11P#40W嗯、嗯……咳咳……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xD,
        "#11P#40W对不起哦，塞茜尔姐姐……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        (
            "#11P#40W……都怪我太任性……\x01",
            "才会这样……咳咳……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        "#1302F#5P没关系，没关系哦……\x02",
    )

    CloseMessageWindow()
    OP_68(18160, 8000, -12960, 1000)
    OP_9B(0x0, 0x101, 0x0, 0x28A, 0x4B0, 0x0)
    OP_6F(0x1)

    #C0029
    ChrTalk(
        0x101,
        "#0000F#6P塞茜尔姐姐，我来抱他吧。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        "#0300F#6P赶快回楼里去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t155B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_16EA end

    def Function_14_1BC0(): pass

    label("Function_14_1BC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32700.itc", 0x1E)
    LoadChrToIndex("chr/ch32900.itc", 0x1F)
    LoadChrToIndex("chr/ch29200.itc", 0x20)
    OP_68(14000, 8000, -3000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 14150, 7000, -3400, 270)
    SetChrPos(0x102, 14950, 7000, -1870, 270)
    SetChrPos(0x103, 14960, 7000, -3810, 270)
    SetChrPos(0x104, 15580, 7000, -4440, 270)
    SetChrPos(0x106, 16020, 7000, -2150, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, 11700, 7000, -2950, 90)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, 10800, 7000, -3500, 90)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x14, 11700, 7000, -4050, 90)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0031
    AnonymousTalk(
        0x101,
        (
            "#0013F──那么，您一直都没\x01",
            "见过约亚西姆医生吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()

    #C0032
    ChrTalk(
        0x14,
        (
            "#6P嗯，那些黑衣人\x01",
            "闯进研究楼的时候，\x01",
            "他就已经不见了……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x12,
        (
            "#5P我本还以为他\x01",
            "一定是又去夜钓了……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#0006F#11P是吗……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#0203F#11P很遗憾……\x01",
            "以目前情况看来，相当可疑呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#0106F#11P是啊……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#0305F#11P如此说来，研究楼中的魔兽\x01",
            "是从哪里来的？\x02\x03",

            "#0301F和那些军犬一样，\x01",
            "是黑手党特意带进来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x14,
        (
            "#6P不，感觉好像就是\x01",
            "凭空冒出来的一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x12,
        "#5P我也没看见呢……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x13,
        (
            "#6P对了，那些魔兽的话，\x01",
            "好像是一个奇怪的人带来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x13,
        (
            "#6P他没穿黑衣，\x01",
            "所以看起来\x01",
            "并不像是黑手党。\x02",
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

    #C0042
    ChrTalk(
        0x102,
        "#0105F#11P那是……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#0201F#11P是像熊一样高大的男人，\x01",
            "还是秃顶的矮胖子呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x13,
        (
            "#6P不不，\x01",
            "好像就是个普通人。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x13,
        (
            "#6P他乘坐导力梯\x01",
            "上四楼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0001F#11P四楼……是教授们的\x01",
            "研究室所在的楼层呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#0101F#11P会、会是什么人呢……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x14,
        (
            "#6P唔……要进去调查的话，\x01",
            "最好多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x12,
        (
            "#5P我们就暂时留在\x01",
            "病房楼的空房间里避难吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x13,
        (
            "#6P如果有什么困难的话，\x01",
            "请随时过来哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(14000, 8000, -1000, 4000)

    def lambda_210C():

        label("loc_210C")

        TurnDirection(0x101, 0x14, 500)
        Yield()
        Jump("loc_210C")

    QueueWorkItem2(0x101, 1, lambda_210C)

    def lambda_211E():

        label("loc_211E")

        TurnDirection(0x102, 0x14, 500)
        Yield()
        Jump("loc_211E")

    QueueWorkItem2(0x102, 1, lambda_211E)

    def lambda_2130():

        label("loc_2130")

        TurnDirection(0x103, 0x14, 500)
        Yield()
        Jump("loc_2130")

    QueueWorkItem2(0x103, 1, lambda_2130)

    def lambda_2142():

        label("loc_2142")

        TurnDirection(0x104, 0x14, 500)
        Yield()
        Jump("loc_2142")

    QueueWorkItem2(0x104, 1, lambda_2142)

    def lambda_2154():

        label("loc_2154")

        TurnDirection(0x106, 0x14, 500)
        Yield()
        Jump("loc_2154")

    QueueWorkItem2(0x106, 1, lambda_2154)
    BeginChrThread(0x12, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0x13, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0x14, 3, 0, 15)
    OP_6F(0x1)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x106, 0x1)
    Fade(1000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_68(15800, 8000, -2380, 0)
    MoveCamera(65, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x106, 0x101, 500)

    #C0051
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P率领魔兽的神秘男人吗……\x02\x03",

            "你们有什么头绪吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_223B():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_223B)
    Sleep(50)

    def lambda_224B():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_224B)
    Sleep(50)

    def lambda_225B():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_225B)
    Sleep(50)

    def lambda_226B():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_226B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0052
    ChrTalk(
        0x101,
        (
            "#0006F#6P不……\x01",
            "目前来说，实在是毫无头绪。\x02\x03",

            "#0008F听上去，好像并不是\x01",
            "约亚西姆医生……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0053
    ChrTalk(
        0x104,
        (
            "#0303F#11P虽然不知是何方神圣……\x01",
            "总之必须要把他逮捕归案啊。\x02\x03",

            "#0301F想办法上四楼看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0054
    ChrTalk(
        0x101,
        "#0013F#6P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetChrPos(0x0, 14000, 7000, -3000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE3, 2)
    OP_29(0x4D, 0x1, 0xD)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_1BC0 end

    def Function_15_239F(): pass

    label("Function_15_239F")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_23AB():
        OP_97(0xFE, 0x0, 0x0, 0x36B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23AB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_239F end

    def Function_16_23C5(): pass

    label("Function_16_23C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00501.itc", 0x1E)
    OP_68(550, 8500, 2390, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19370, 0)
    SetChrPos(0x101, 4880, 7000, 2680, 270)
    SetChrPos(0x102, 6660, 7000, 4040, 270)
    SetChrPos(0x103, 5810, 7000, 1720, 270)
    SetChrPos(0x104, 7430, 7000, 3180, 270)
    SetChrPos(0x106, 8189, 7000, 1130, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_68(4550, 8500, 2390, 4500)
    OP_6F(0x1)
    OP_0D()

    #C0055
    ChrTalk(
        0x104,
        (
            "#0302F#11P哎呀呀……\x01",
            "这样一来，就可以暂时放心了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#0106F#11P嗯……\x01",
            "但还是不能松懈大意。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#0208F#11P……是呀……\x02\x03",

            "#0201F从那个秘书的话看来，\x01",
            "似乎还有什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#0013F#11P嗯，和副司令谈过之后，\x01",
            "就赶快回克洛斯贝尔市吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#11P呵呵……\x01",
            "看来是到此为止了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(5890, 8500, 1050, 1500)
    SetCameraDistance(17440, 1500)

    def lambda_2606():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2606)

    def lambda_2613():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2613)
    Sleep(100)

    def lambda_2623():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2623)

    def lambda_2630():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2630)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0060
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F#6P『银』……你要走了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#11P呵呵，我没有义务\x01",
            "继续奉陪吧。\x02\x03",

            "毕竟，这些情报已经足够向曹交差了，\x01",
            "而且我也有我需要守护的东西。\x02\x03",

            "与你们相同。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#0005F#8P哎……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        "#0105F#5P你到底是……\x02",
    )

    CloseMessageWindow()
    OP_93(0x106, 0xB4, 0x1F4)
    Sleep(300)

    #C0064
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P……今夜恐怕不会再见面了。\x02\x03",

            "然而，夜晚依然漫长……\x01",
            "你们就多加小心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0002F#6P好的……谢谢！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        "#0300F#5P嗯，姑且谢谢你啦。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x103,
        "#0202F#6P……辛苦了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1614, 255, 100, 0)    #voice#Yin

    #C0068
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P#20A呵……后会有期。\x07\x00\x02",
        )
    )
    #Auto

    Sleep(2400)

    def lambda_2813():
        OP_95(0xFE, 9020, 7000, -5060, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2813)
    WaitChrThread(0x106, 1)
    Fade(500)
    OP_68(6470, 10000, -19480, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(13000, 3000)
    BeginChrThread(0x106, 3, 0, 17)
    Sleep(2500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人与索妮亚和诺艾尔会合，\x01",
            "简短说明了情况……\x02\x03",

            "随后便乘坐警备队的车辆，\x01",
            "返回了克洛斯贝尔市。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_32(0x0, 0x5, 0xC8)
    OP_32(0x1, 0x5, 0xC8)
    OP_32(0x2, 0x5, 0xC8)
    OP_32(0x3, 0x5, 0xC8)
    OP_BA(0x5)
    RemoveParty(0x5, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_23C5 end

    def Function_17_2953(): pass

    label("Function_17_2953")

    SetChrPos(0xFE, 8350, 8000, -4940, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)

    def lambda_2981():
        OP_95(0xFE, 8350, 8000, -13940, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2981)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x1F4)
    Sound(814, 0, 100, 0)

    def lambda_29BB():
        OP_9D(0xFE, 0x209E, 0x1F40, 0xFFFFB9EC, 0x514, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29BB)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_29E6():
        OP_9D(0xFE, 0x209E, 0x0, 0xFFFF7478, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29E6)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_17_2953 end

    def Function_18_2A1F(): pass

    label("Function_18_2A1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A36")
    OP_A0(0xFE, 3000, 0x0, 0xFB)
    Jump("Function_18_2A1F")

    label("loc_2A36")

    Return()

    # Function_18_2A1F end

    SaveToFile()

Try(main)
