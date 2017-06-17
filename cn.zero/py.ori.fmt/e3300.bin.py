from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "e3300.bin",                # FileName
        "e3300",                    # MapName
        "e3300",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3300",                  # 0
        "阿奈斯特",               # 1
        "翼龙",                   # 2
        "歼灭天使玲",             # 3
        "帕蒂尔·玛蒂尔",         # 4
        "SE控制",                 # 5
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_150",          # 00, 0
        "Function_1_174",          # 01, 1
        "Function_2_175",          # 02, 2
        "Function_3_5B8",          # 03, 3
        "Function_4_5D9",          # 04, 4
        "Function_5_611",          # 05, 5
        "Function_6_62E",          # 06, 6
        "Function_7_638",          # 07, 7
        "Function_8_648",          # 08, 8
        "Function_9_668",          # 09, 9
        "Function_10_D95",         # 0A, 10
        "Function_11_DBA",         # 0B, 11
    ))


    def Function_0_150(): pass

    label("Function_0_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_164")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_173")

    label("loc_164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_173")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 9)

    label("loc_173")

    Return()

    # Function_0_150 end

    def Function_1_174(): pass

    label("Function_1_174")

    Return()

    # Function_1_174 end

    def Function_2_175(): pass

    label("Function_2_175")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02351.itc", 0x1E)
    LoadChrToIndex("apl/ch50503.itc", 0x1F)
    LoadChrToIndex("apl/ch50504.itc", 0x23)
    LoadEffect(0x0, "event\\eva03_00.eff")
    SoundLoad(132)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x7)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(132, 2, 70, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_263")
    Fade(1000)
    OP_68(39210, 19800, 2730, 0)
    MoveCamera(295, 328, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(52280, 0)
    SetCameraDistance(56280, 3000)
    OP_6F(0x10)
    OP_0D()

    label("loc_263")

    PlayEffect(0x0, 0x0, 0xFF, 0x0, 50000, 25000, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, 50000, 25000, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, 50000, 25000, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DB")
    OP_C7(0x0, 0x20000)
    SetChrChip(0x0, 0x8, 0xA, 0xC8)
    Fade(500)
    OP_68(52460, 18800, -90, 0)
    MoveCamera(270, 312, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12690, 0)
    MoveCamera(270, 396, 0, 2000)
    SetCameraDistance(4690, 2000)
    OP_68(52460, 18800, -90, 0)
    OP_68(52460, 20800, -90, 1000)
    SetChrPos(0x8, 47920, 26000, -110, 90)

    def lambda_3A0():
        OP_9D(0xFE, 0xD386, 0x1B58, 0xFFFFFF60, 0x0, 0x640)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A0)
    BeginChrThread(0xC, 1, 0, 6)
    WaitChrThread(0x8, 1)
    OP_6F(0x51)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    OP_C7(0x1, 0x20000)
    StopBGM(0x2710)
    EndChrThread(0xC, 0x1)

    label("loc_3DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D9")
    Fade(500)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_D3(0x9, 0x15F90, 0x0, 0x0, 0x0)
    ClearChrFlags(0x9, 0x100)
    OP_68(50640, 22900, 40, 0)
    MoveCamera(343, 427, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13760, 0)
    OP_68(50640, 17900, 40, 3000)
    SetCameraDistance(10760, 1500)
    SetChrPos(0x8, 49010, 30000, 110, 90)

    def lambda_473():
        OP_9D(0xFE, 0xCAF8, 0x1B58, 0x96, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_473)
    Sleep(400)
    Sound(950, 0, 100, 0)
    Sleep(500)
    Sound(952, 0, 100, 0)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    OP_93(0x8, 0x2D, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 3, 0, 4)
    WaitChrThread(0x9, 3)
    OP_0D()

    label("loc_4D9")

    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_578")
    Fade(500)
    OP_68(49660, 20600, 2230, 0)
    MoveCamera(3, 357, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20360, 0)
    SetCameraDistance(25360, 4000)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 5)
    BeginChrThread(0xC, 1, 0, 7)
    OP_D3(0x9, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x9, 0x100)
    SetChrPos(0x9, 44350, 20500, -13930, 45)
    OP_9B(0x1, 0x9, 0x0, 0xC350, 0x2710, 0x0)
    OP_6F(0x10)
    OP_0D()

    label("loc_578")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0xC, 0, 0, 8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    EndChrThread(0xC, 0x1)
    WaitChrThread(0xC, 0)
    OP_24(0x84)
    SetScenarioFlags(0x5C, 1)
    NewScene("t165B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_175 end

    def Function_3_5B8(): pass

    label("Function_3_5B8")

    SetChrPos(0xFE, 51450, 20000, -7260, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x2710, 0x2710, 0x0)
    Return()

    # Function_3_5B8 end

    def Function_4_5D9(): pass

    label("Function_4_5D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_610")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_4_5D9")

    label("loc_610")

    Return()

    # Function_4_5D9 end

    def Function_5_611(): pass

    label("Function_5_611")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62D")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_5_611")

    label("loc_62D")

    Return()

    # Function_5_611 end

    def Function_6_62E(): pass

    label("Function_6_62E")

    Sleep(400)
    Sound(812, 0, 100, 0)
    Return()

    # Function_6_62E end

    def Function_7_638(): pass

    label("Function_7_638")

    Sleep(500)
    Sound(951, 0, 100, 0)
    Sound(948, 0, 100, 0)
    Return()

    # Function_7_638 end

    def Function_8_648(): pass

    label("Function_8_648")

    OP_25(0x84, 0x28)
    Sleep(200)
    OP_25(0x84, 0x1E)
    Sleep(200)
    OP_25(0x84, 0x14)
    Sleep(200)
    OP_25(0x84, 0xA)
    Sleep(200)
    OP_24(0x84)
    Return()

    # Function_8_648 end

    def Function_9_668(): pass

    label("Function_9_668")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    SoundLoad(953)
    OP_78(0xB, 0xB)
    OP_49()
    OP_74(0xB, 0xF)
    OP_71(0xB, 0xF1, 0x104, 0x0, 0x20)
    SetChrPos(0xB, 52360, 25000, 0, 0)
    OP_D3(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    LoadEffect(0x0, "event\\ev600_01.eff")
    LoadEffect(0x1, "event\\ev601_01.eff")
    LoadEffect(0x2, "event\\eva03_01.eff")
    OP_87(0x1, 0xFF, 0xB, "Null_S_jet_r0(63)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0xFF, 0xB, "Null_S_jet_r2(64)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0xFF, 0xB, "Null_S_jet_l0(66)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0xFF, 0xB, "Null_S_jet_l2(65)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0xB, "Null_S_jet_r1(61)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0xB, "Null_S_jet_l1(62)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0xB, "Null_kata_jet_r(53)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0xB, "Null_kata_jet_l(54)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_93(0xA, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    OP_D1(0xA, 0xB, "Null_ren(52)")
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_93(0xB, 0x10E, 0x0)
    SetChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    BeginChrThread(0xB, 3, 0, 10)
    Sound(953, 2, 100, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D8")
    Fade(1000)
    OP_68(51150, 29400, -3260, 0)
    MoveCamera(288, 317, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(27650, 0)
    SetChrPos(0xB, 52360, 22000, 0, 270)

    def lambda_9B7():
        OP_98(0xFE, 0x0, 0x7D0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9B7)
    SetCameraDistance(22750, 3000)
    OP_6F(0x10)
    OP_0D()

    label("loc_9D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A74")
    Fade(1000)
    OP_68(52300, 28000, -3760, 0)
    MoveCamera(166, 357, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(21230, 0)
    OP_68(53900, 28000, -3360, 3000)
    Sleep(1000)

    def lambda_A2F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A2F)
    Sleep(400)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_A59():
        OP_93(0xFE, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_A59)
    Sleep(500)
    CancelBlur(2500)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    OP_6F(0x1)
    OP_0D()

    label("loc_A74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D85")
    Fade(1000)
    OP_11(0x2C, 0x30, 0x49, 0x19, 0xFA, 0x0)
    OP_68(58530, 28000, 1470, 0)
    MoveCamera(142, 354, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11530, 0)
    SetCameraDistance(8530, 2500)
    MoveCamera(147, 354, 0, 2500)
    OP_6F(0x10)
    Sleep(500)
    Fade(500)
    SetCameraDistance(19460, 1500)
    OP_6F(0x10)
    OP_0D()
    OP_71(0xB, 0x105, 0x12C, 0x0, 0x0)
    Sound(945, 0, 100, 0)
    Sleep(1000)
    Sound(945, 0, 100, 0)
    OP_79(0xB)
    OP_71(0xB, 0x119, 0x12C, 0x0, 0x20)
    Sound(954, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(500)
    CancelBlur(1500)

    def lambda_B3B():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B3B)
    Sleep(1000)
    Fade(500)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54860, 22000, 0, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54860, 22000, 0, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54860, 22000, 0, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54860, 22000, 0, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54860, 22000, 0, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54860, 22000, 0, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54860, 22000, 0, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54860, 22000, 0, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xB, 0x1)
    OP_9B(0x1, 0xB, 0x0, 0xFFFF63C0, 0x0, 0x0)
    OP_93(0xB, 0xF, 0x0)

    def lambda_D2A():
        OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D2A)
    BeginChrThread(0xC, 1, 0, 11)
    OP_68(55700, 27000, -2220, 0)
    MoveCamera(346, 347, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19140, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xC, 1)
    EndChrThread(0xB, 0x1)

    label("loc_D85")

    OP_24(0x3B9)
    SetScenarioFlags(0x5C, 2)
    NewScene("t165B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_668 end

    def Function_10_D95(): pass

    label("Function_10_D95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DB9")
    OP_82(0x0, 0x64, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_10_D95")

    label("loc_DB9")

    Return()

    # Function_10_D95 end

    def Function_11_DBA(): pass

    label("Function_11_DBA")

    OP_25(0x3B9, 0x5A)
    Sleep(300)
    OP_25(0x3B9, 0x50)
    Sleep(300)
    OP_25(0x3B9, 0x46)
    Sleep(300)
    OP_25(0x3B9, 0x3C)
    Sleep(300)
    OP_25(0x3B9, 0x32)
    Sleep(300)
    OP_25(0x3B9, 0x28)
    Sleep(300)
    OP_25(0x3B9, 0x1E)
    Sleep(300)
    OP_25(0x3B9, 0x14)
    Sleep(300)
    OP_25(0x3B9, 0xA)
    Sleep(300)
    OP_24(0x3B9)
    Return()

    # Function_11_DBA end

    SaveToFile()

Try(main)
