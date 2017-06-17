from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e3210.bin",                # FileName
        "e3210",                    # MapName
        "e3210",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e3210",                  # 0
        "科洛蒂娅公主",           # 1
        "尤莉亚准校",             # 2
        "奥利维特皇子",           # 3
        "穆拉少校",               # 4
        "基库",                   # 5
        "亲卫队",                 # 6
        "亲卫队",                 # 7
        "亲卫队",                 # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(428, 0)                                        # 0

    ScpFunction((
        "Function_0_1AC",          # 00, 0
        "Function_1_25C",          # 01, 1
        "Function_2_26C",          # 02, 2
        "Function_3_26D",          # 03, 3
        "Function_4_2ED",          # 04, 4
        "Function_5_2FF",          # 05, 5
        "Function_6_311",          # 06, 6
        "Function_7_34E",          # 07, 7
        "Function_8_3A3",          # 08, 8
        "Function_9_419",          # 09, 9
        "Function_10_471",         # 0A, 10
        "Function_11_4C9",         # 0B, 11
        "Function_12_521",         # 0C, 12
        "Function_13_597",         # 0D, 13
    ))


    def Function_0_1AC(): pass

    label("Function_0_1AC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1E4"),
        (1, "loc_1F0"),
        (2, "loc_1FC"),
        (3, "loc_208"),
        (4, "loc_214"),
        (5, "loc_220"),
        (6, "loc_22C"),
        (SWITCH_DEFAULT, "loc_238"),
    )


    label("loc_1E4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1F0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1FC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_208")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_214")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_220")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_22C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_238")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_25B")

    Return()

    # Function_0_1AC end

    def Function_1_25C(): pass

    label("Function_1_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_26B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)

    label("loc_26B")

    Return()

    # Function_1_25C end

    def Function_2_26C(): pass

    label("Function_2_26C")

    Return()

    # Function_2_26C end

    def Function_3_26D(): pass

    label("Function_3_26D")


    def lambda_272():
        OP_95(0xFE, 0, 0, 3300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_272)

    def lambda_28C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28C)
    WaitChrThread(0xFE, 1)

    def lambda_2A1():
        OP_95(0xFE, -2000, 0, 3300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A1)
    WaitChrThread(0xFE, 1)

    def lambda_2BF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BF)
    Sleep(1000)

    def lambda_2DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_3_26D end

    def Function_4_2ED(): pass

    label("Function_4_2ED")

    Sleep(2500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    Return()

    # Function_4_2ED end

    def Function_5_2FF(): pass

    label("Function_5_2FF")

    Sleep(7000)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x29)
    SetChrSubChip(0xE, 0x0)
    Return()

    # Function_5_2FF end

    def Function_6_311(): pass

    label("Function_6_311")


    def lambda_316():
        OP_95(0xFE, -99000, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_316)
    WaitChrThread(0xFE, 1)

    def lambda_334():
        OP_95(0xFE, -99000, 0, 5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_334)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_311 end

    def Function_7_34E(): pass

    label("Function_7_34E")


    def lambda_353():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_353)

    def lambda_36D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36D)
    WaitChrThread(0xFE, 1)

    def lambda_382():
        OP_95(0xFE, -100900, 0, 44300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_382)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_7_34E end

    def Function_8_3A3(): pass

    label("Function_8_3A3")

    Sleep(700)

    def lambda_3AB():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AB)

    def lambda_3C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C5)
    WaitChrThread(0xFE, 1)

    def lambda_3DA():
        OP_95(0xFE, -101400, 0, 43000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DA)
    WaitChrThread(0xFE, 1)

    def lambda_3F8():
        OP_95(0xFE, -101600, 0, 45000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_8_3A3 end

    def Function_9_419(): pass

    label("Function_9_419")

    Sleep(1600)

    def lambda_421():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_421)

    def lambda_43B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43B)
    WaitChrThread(0xFE, 1)

    def lambda_450():
        OP_95(0xFE, -102100, 0, 43700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_450)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_9_419 end

    def Function_10_471(): pass

    label("Function_10_471")

    Sleep(2300)

    def lambda_479():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_479)

    def lambda_493():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_493)
    WaitChrThread(0xFE, 1)

    def lambda_4A8():
        OP_95(0xFE, -101400, 0, 43000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_10_471 end

    def Function_11_4C9(): pass

    label("Function_11_4C9")

    Sleep(3000)

    def lambda_4D1():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D1)

    def lambda_4EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EB)
    WaitChrThread(0xFE, 1)

    def lambda_500():
        OP_95(0xFE, -100200, 0, 43000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_500)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_11_4C9 end

    def Function_12_521(): pass

    label("Function_12_521")

    Sleep(3700)

    def lambda_529():
        OP_95(0xFE, -99000, 0, 42400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_529)

    def lambda_543():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_543)
    WaitChrThread(0xFE, 1)

    def lambda_558():
        OP_95(0xFE, -95500, 0, 44900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_558)
    WaitChrThread(0xFE, 1)

    def lambda_576():
        OP_95(0xFE, -95500, 0, 48600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_576)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_12_521 end

    def Function_13_597(): pass

    label("Function_13_597")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11000.itc", 0x1E)
    LoadChrToIndex("chr/ch11100.itc", 0x1F)
    LoadChrToIndex("chr/ch11200.itc", 0x20)
    LoadChrToIndex("chr/ch11300.itc", 0x21)
    LoadChrToIndex("chr/ch13801.itc", 0x22)
    LoadChrToIndex("chr/ch41600.itc", 0x23)
    LoadChrToIndex("apl/ch51260.itc", 0x24)
    LoadChrToIndex("chr/ch11002.itc", 0x25)
    LoadChrToIndex("chr/ch11102.itc", 0x26)
    LoadChrToIndex("chr/ch11202.itc", 0x27)
    LoadChrToIndex("chr/ch11302.itc", 0x28)
    LoadChrToIndex("apl/ch51213.itc", 0x29)
    LoadChrToIndex("apl/ch51214.itc", 0x2A)
    LoadChrToIndex("apl/ch51215.itc", 0x2B)
    LoadChrToIndex("chr/ch00002.itc", 0x2C)
    LoadChrToIndex("chr/ch00102.itc", 0x2D)
    LoadChrToIndex("chr/ch00302.itc", 0x2E)
    LoadChrToIndex("chr/ch02902.itc", 0x2F)
    LoadChrToIndex("chr/ch03002.itc", 0x30)
    LoadChrToIndex("chr/ch13802.itc", 0x31)
    SoundLoad(498)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07201.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07300.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0x9, 0, 0, -13500, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 3200, 0, -6000, 270)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -3500, 0, 3500, 90)
    SetChrPos(0x101, 0, 0, -13500, 0)
    SetChrPos(0x102, 0, 0, -13500, 0)
    SetChrPos(0x104, 0, 0, -13500, 0)
    SetChrPos(0x109, 0, 0, -13500, 0)
    SetChrPos(0x105, 0, 0, -13500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_70(0x4, 0x0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(0, 1000, -10000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(0, 1000, 1000, 7000)
    SetCameraDistance(20500, 7000)
    Sound(100, 0, 80, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0xD, 3, 0, 4)
    BeginChrThread(0xE, 3, 0, 5)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(900)
    BeginChrThread(0x101, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 3)
    Sleep(500)
    Sound(100, 0, 80, 0)
    OP_6F(0x79)
    SetCameraDistance(19000, 5000)
    WaitChrThread(0x9, 3)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -3410, 0, 96130, 270)
    BeginChrThread(0xD, 3, 0, 0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 1850, 200, 97370, 90)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3520, 200, 97470, 270)
    OP_68(-1000, 1500, 97000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(-1000, 2500, 96000, 7000)
    MoveCamera(35, 25, 0, 7000)
    SetCameraDistance(21500, 7000)
    Sound(498, 2, 30, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    StopSound(498, 2000, 30)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(-99000, 1600, 2900, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -99600, 70, 900, 0)
    SetChrPos(0x102, -98400, 70, 900, 0)
    SetChrPos(0x104, -97800, 60, -300, 0)
    SetChrPos(0x109, -99000, 70, -900, 0)
    SetChrPos(0x105, -100200, 60, -300, 0)
    SetChrPos(0x9, -99000, 70, 2500, 0)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -99000, 70, 6500, 0)
    ClearChrFlags(0x8, 0x80)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-99000, 1100, 2900, 2000)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_AF5():
        OP_96(0xFE, 0xFFFE7D48, 0x46, 0xC80, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AF5)
    WaitChrThread(0x9, 1)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0001
    ChrTalk(
        0x9,
        (
            "#11P#07104F殿下，打扰了。\x02\x03",

            "我已经把特别任务支援科的\x01",
            "诸位带来了。\x02",
        )
    )

    CloseMessageWindow()

    #N0002
    NpcTalk(
        0x8,
        "平静的声音",
        "#3C#2S#11P请他们进来吧。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(100, 0, 80, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x2)

    def lambda_BA9():
        OP_95(0xFE, -97800, 70, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BA9)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xE1, 0x1F4)

    def lambda_BCE():

        label("loc_BCE")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BCE")

    QueueWorkItem2(0x9, 2, lambda_BCE)

    #C0003
    ChrTalk(
        0x9,
        "#5P#07102F来，请进。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#12P#00001F好、好的。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#00104F那就打扰了。\x02",
    )

    CloseMessageWindow()
    OP_68(-99000, 1100, 3900, 2000)
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(300)
    EndChrThread(0x9, 0x2)
    BeginChrThread(0x104, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 6)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 6)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x8, -96900, 50, 49350, 270)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x31)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, -98400, 700, 48350, 135)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, -99000, 0, 40500, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -99000, 0, 40500, 0)
    SetChrPos(0x102, -99000, 0, 40500, 0)
    SetChrPos(0x104, -99000, 0, 40500, 0)
    SetChrPos(0x109, -99000, 0, 40500, 0)
    SetChrPos(0x105, -99000, 0, 40500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-98700, 1100, 44800, 0)
    MoveCamera(27, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    OP_68(-98700, 1100, 46800, 4000)
    MoveCamera(41, 13, 0, 4000)
    OP_6E(450, 4000)
    SetCameraDistance(19290, 4000)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 3, 0, 7)
    BeginChrThread(0x102, 3, 0, 8)
    BeginChrThread(0x104, 3, 0, 9)
    BeginChrThread(0x109, 3, 0, 10)
    BeginChrThread(0x105, 3, 0, 11)
    BeginChrThread(0x9, 3, 0, 12)
    WaitChrThread(0x105, 3)

    #C0006
    ChrTalk(
        0x101,
        "#6P#00005F啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -96900, 0, 48600, 225)
    OP_0D()
    PlayBGM("ed7519", 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0007
    AnonymousTalk(
        0x8,
        (
            "呵呵，初次见面。\x02\x03",

            "我是利贝尔王国的\x01",
            "王太女科洛蒂娅。\x02\x03",

            "以这种形式请各位过来，\x01",
            "实在是不好意思。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0008
    ChrTalk(
        0xC,
        "#5P#08009F啾。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#6P#00011F哪、哪里，您太客气了。\x02\x03",

            "#00003F初次见面，\x01",
            "我是克洛斯贝尔警察局·特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        (
            "#6P#00104F我是同属特别任务支援科的\x01",
            "艾莉·麦克道尔。\x02\x03",

            "#00102F王太女殿下，\x01",
            "贵安。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#07009F#5P呵呵，我听说过许多\x01",
            "有关艾莉小姐的事情……\x02\x03",

            "#07002F很高兴能见到你。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x102,
        "#6P#00105F我吗……？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#07004F#5P嗯，之前曾和你的外公\x01",
            "麦克道尔议长阁下\x01",
            "谈过话。\x02\x03",

            "#07000F另外，我和玛丽亚贝尔小姐\x01",
            "也见过几次面。\x02\x03",

            "听说你以前曾在\x01",
            "利贝尔留过学？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#6P#00104F是的，\x01",
            "不过只待了三个月左右……\x02\x03",

            "#00102F没能前去拜会您，真是失礼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "#07009F哪里的话，彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#6P#00309F哈哈……您好，\x01",
            "我叫兰迪·奥兰多。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x109,
        (
            "#6P#N#10100F我、我是诺艾尔·希卡！\x01",
            "请多指教！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0018
    ChrTalk(
        0x105,
        (
            "#12P#10304F瓦吉·赫米斯菲亚，\x01",
            "得见美丽的公主，是我的荣幸。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0019
    ChrTalk(
        0x8,
        (
            "#07009F#5P欢迎各位。\x02\x03",

            "#07004F其实，我原本还想在此\x01",
            "向大家介绍一个人……\x02\x03",

            "#07000F但他来得似乎有点迟呢。\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -99000, 0, 39000, 0)
    VolumeBGM(0x32, 0x12C)
    Sound(849, 0, 100, 0)
    Sleep(2000)
    VolumeBGM(0x64, 0x3E8)

    #N0020
    NpcTalk(
        0xA,
        "语气轻佻的声音",
        (
            "呵……\x01",
            "不必担心。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_1C1B")

    def lambda_130F():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_130F)

    def lambda_131C():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_131C)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_13B0():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13B0)
    Sleep(50)

    def lambda_13C0():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13C0)
    Sleep(50)

    def lambda_13D0():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_13D0)
    Sleep(50)

    def lambda_13E0():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13E0)
    Sleep(50)

    def lambda_13F0():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_13F0)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0021
    ChrTalk(
        0x101,
        "#00005F#5P这声音是……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#00108F#5P好、好像在哪里听过。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        "#00305F#5P喂喂，该不会是……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "#11P#07104F#5P呵呵……\x01",
            "看来他已经来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-94200, 900, 101100, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x8, -101300, 0, 103300, 135)
    SetChrPos(0xC, -100800, 700, 102000, 90)
    SetChrPos(0x9, -99500, 0, 104700, 135)
    SetChrPos(0x101, -97700, 0, 99100, 0)
    SetChrPos(0x102, -97900, 0, 97700, 0)
    SetChrPos(0x104, -96700, 0, 97500, 0)
    SetChrPos(0x109, -96500, 0, 98900, 0)
    SetChrPos(0x105, -95300, 0, 98700, 315)
    SetChrPos(0xA, -92000, 0, 101200, 270)
    SetChrPos(0xB, -92000, 0, 101000, 270)
    ClearChrFlags(0xB, 0x80)
    OP_68(-95880, 900, 101590, 3000)
    MoveCamera(62, 16, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15300, 3000)

    def lambda_15B6():
        OP_95(0xFE, -96300, 0, 101200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15B6)

    def lambda_15D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15D0)
    Sleep(700)

    def lambda_15E4():
        OP_95(0xFE, -95100, 0, 101000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_15E4)

    def lambda_15FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_15FE)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0025
    ChrTalk(
        0x101,
        "#6P#00011F#4S什么！？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x109,
        (
            "#12P#10111F在、在之前那件\x01",
            "支援请求中见到的……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "#07005F#6P#N啊，原来你们已经见过面了吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0028
    ChrTalk(
        0x102,
        "#12P#00109F嗯，那个……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x105,
        (
            "#10302F呵呵……\x01",
            "真是个意想不到的惊喜啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0030
    NpcTalk(
        0xB,
        "帝国军官",
        (
            "#5P#07303F各位，之前有所失礼。\x02\x03",

            "#07308F#11P科洛蒂娅公主……\x01",
            "十分抱歉，我们来晚了。\x02\x03",

            "#07301F因为这个笨蛋又像平时一样，\x01",
            "到处惹是生非。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        "#07009F#6P#N呵呵，没关系……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(850, 0, 100, 0)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x2B)
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(300)
    OP_63(0xA, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    SetChrSubChip(0xA, 0x8)
    Sleep(130)
    Sound(822, 0, 100, 0)
    SetChrSubChip(0xA, 0x9)
    Sleep(130)
    SetChrSubChip(0xA, 0xA)
    Sleep(500)
    SetChrSubChip(0xA, 0xB)
    Sleep(130)
    SetChrSubChip(0xA, 0xC)
    Sleep(130)
    SetChrSubChip(0xA, 0xD)
    Sleep(130)
    SetChrSubChip(0xA, 0xE)
    Sleep(130)
    SetChrSubChip(0xA, 0xF)
    Sleep(500)
    OP_64(0xA)
    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x20)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(300)

    def lambda_1936():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1936)

    #N0032
    NpcTalk(
        0xA,
        "金发青年",
        (
            "#5P#07204F呵，重新做个\x01",
            "自我介绍好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetMessageWindowPos(14, 280, -1, 3)
    Sleep(500)
    SetChrName("金发青年")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            "我是尤肯特皇帝的代理人，来自埃雷波尼亚帝国的\x01",
            "奥利维特·莱泽·亚诺尔。\x02\x03",

            "当然，我的真正身份\x01",
            "是稀世天才和漂泊的演奏家，\x01",
            "奥利维尔·朗海姆！\x02\x03",

            "哈哈哈，\x01",
            "还请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0034
    ChrTalk(
        0x101,
        "#6P#00011F……………………（张口结舌）\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#12P#00301F这……不可能吧？\x02",
    )

    CloseMessageWindow()

    #N0036
    NpcTalk(
        0xB,
        "帝国军官",
        (
            "#5P#07306F非常遗憾，\x01",
            "但他说的是事实。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("帝国军官")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            "我是帝国军第七机甲师团的\x01",
            "穆拉·范德尔少校。\x02\x03",

            "应科洛蒂娅殿下的邀请，\x01",
            "与皇子一起拜会诸位。\x02\x03",

            "特别任务支援科的各位，请多指教。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Jump("loc_2492")

    label("loc_1C1B")


    def lambda_1C20():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1C20)

    def lambda_1C2D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1C2D)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_1CB5():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CB5)
    Sleep(50)

    def lambda_1CC5():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CC5)
    Sleep(50)

    def lambda_1CD5():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1CD5)
    Sleep(50)

    def lambda_1CE5():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1CE5)
    Sleep(50)

    def lambda_1CF5():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1CF5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0038
    ChrTalk(
        0x101,
        "#00005F#5P咦……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#00108F#5P是鲁特琴的声音……？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "#5P#07104F呵呵……\x01",
            "看来他已经来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-94200, 900, 101100, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x8, -101300, 0, 103300, 135)
    SetChrPos(0xC, -100800, 700, 102000, 90)
    SetChrPos(0x9, -99500, 0, 104700, 135)
    SetChrPos(0x101, -97700, 0, 99100, 0)
    SetChrPos(0x102, -97900, 0, 97700, 0)
    SetChrPos(0x104, -96700, 0, 97500, 0)
    SetChrPos(0x109, -96500, 0, 98900, 0)
    SetChrPos(0x105, -95300, 0, 98700, 315)
    SetChrPos(0xA, -92000, 0, 101200, 270)
    SetChrPos(0xB, -92000, 0, 101000, 270)
    ClearChrFlags(0xB, 0x80)
    OP_68(-95880, 900, 101590, 3000)
    MoveCamera(62, 16, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15300, 3000)

    def lambda_1E8F():
        OP_95(0xFE, -96300, 0, 101200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E8F)

    def lambda_1EA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1EA9)
    Sleep(700)

    def lambda_1EBD():
        OP_95(0xFE, -95100, 0, 101000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1EBD)

    def lambda_1ED7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1ED7)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0041
    ChrTalk(
        0x101,
        "#6P#00011F啊……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#12P#10111F埃、埃雷波尼亚帝国的……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        "#12P#00105F奥利维特皇子殿下……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)
    Sleep(150)

    #N0044
    NpcTalk(
        0xB,
        "帝国军官",
        (
            "#07303F#11P科洛蒂娅公主……\x01",
            "十分抱歉，我们来晚了。\x02\x03",

            "#07301F因为这个笨蛋又像平时一样，\x01",
            "到处惹是生非。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "#07009F#6P#N呵呵，没关系……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(850, 0, 100, 0)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x2B)
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrSubChip(0xA, 0x1)
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(300)
    OP_63(0xA, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    SetChrSubChip(0xA, 0x8)
    Sleep(130)
    Sound(822, 0, 100, 0)
    SetChrSubChip(0xA, 0x9)
    Sleep(130)
    SetChrSubChip(0xA, 0xA)
    Sleep(500)
    SetChrSubChip(0xA, 0xB)
    Sleep(130)
    SetChrSubChip(0xA, 0xC)
    Sleep(130)
    SetChrSubChip(0xA, 0xD)
    Sleep(130)
    SetChrSubChip(0xA, 0xE)
    Sleep(130)
    SetChrSubChip(0xA, 0xF)
    Sleep(500)
    OP_64(0xA)
    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x20)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(300)

    def lambda_2163():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2163)

    #C0046
    ChrTalk(
        0xA,
        "#5P#07204F呼，各位，初次见面。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetMessageWindowPos(14, 280, -1, 3)
    Sleep(500)

    #A0047
    AnonymousTalk(
        0xA,
        (
            "我是尤肯特皇帝的代理人，来自埃雷波尼亚帝国的\x01",
            "奥利维特·莱泽·亚诺尔。\x02\x03",

            "但说实话，比起当什么皇子，\x01",
            "我更想做个为了寻求真爱\x01",
            "而四处旅行的漂泊演奏家。\x02\x03",

            "哈哈哈，\x01",
            "请多关照啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0048
    ChrTalk(
        0x101,
        "#6P#00011F啊，那个……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#12P#00109F请、请多关照。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#12P#00305F帝国的皇子……\x01",
            "真是意想不到的轻浮啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x105,
        "#10305F话说回来，为什么还带着一把鲁特琴啊？\x02",
    )

    CloseMessageWindow()

    #N0052
    NpcTalk(
        0xB,
        "帝国军官",
        (
            "#5P#07306F关于这个问题，\x01",
            "就请各位当作没看见吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("帝国军官")

    #A0053
    AnonymousTalk(
        0xFF,
        (
            "我是帝国军第七机甲师团的\x01",
            "穆拉·范德尔少校。\x02\x03",

            "应科洛蒂娅殿下的邀请，\x01",
            "与皇子一起拜会诸位。\x02\x03",

            "特别任务支援科的各位，请多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    label("loc_2492")

    SetCameraDistance(15800, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis313.itp")
    CreatePortrait(1, 160, 8, 416, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis314.itp")
    CreatePortrait(2, 160, 8, 416, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis315.itp")
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x2)
    SetChrPos(0x8, -96900, 50, 50900, 270)
    SetChrPos(0x9, -96900, 50, 52400, 270)
    SetChrPos(0xA, -96900, 50, 49350, 270)
    SetChrPos(0xB, -96900, 50, 47850, 270)
    SetChrPos(0xC, -98400, 700, 46000, 0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2C)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2D)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x2F)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x30)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -101100, 50, 49350, 90)
    SetChrPos(0x102, -101100, 50, 50900, 90)
    SetChrPos(0x104, -101100, 50, 52400, 90)
    SetChrPos(0x109, -101100, 50, 47850, 90)
    SetChrPos(0x105, -101100, 50, 46450, 90)
    OP_68(-99250, 1600, 50090, 0)
    MoveCamera(38, 14, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18950, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0054
    AnonymousTalk(
        0x101,
        (
            "#00004F原来如此……\x01",
            "是从艾丝蒂尔他们那里听说我们的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-99250, 1100, 50090, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0055
    ChrTalk(
        0x102,
        (
            "#6P#00102F各位竟然是与艾丝蒂尔小姐他们\x01",
            "一起冒险的同伴……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#6P#00309F哈哈，仔细想想，\x01",
            "这可真是不得了的组合。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        (
            "#07204F总之，请大家\x01",
            "尽量放松吧。\x02\x03",

            "#07202F我们和艾丝蒂尔他们是\x01",
            "共同面对利贝尔异变的同伴。\x02\x03",

            "而你们和艾丝蒂尔他们则是\x01",
            "共同面对克洛斯贝尔异变的同伴。\x02\x03",

            "#07209F也就是说，我们也算是\x01",
            "命中注定的同伴呢¤\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x101,
        (
            "#6P#00012F这、这个～\x01",
            "我觉得并不是那么简单呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#6P#00106F那个……\x01",
            "老实说，我真是诚惶诚恐。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "#11P#07004F呵呵，各位真的没有必要紧张，\x01",
            "请放轻松一点。\x02\x03",

            "#07002F虽然这次请大家前来，\x01",
            "是为了商量要事……\x02\x03",

            "但更重要的是，我很想借\x01",
            "这个机会与大家亲近一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#6P#00000F公主殿下……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#6P#00309F哦哦，好感动……！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        "#6P#10112F啊……不、不敢当！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "#07204F说起来，听说艾丝蒂尔他们\x01",
            "在克洛斯贝尔\x01",
            "过得很开心呢。\x02\x03",

            "#07209F而且这里还有主题公园，\x01",
            "我也待上一个月左右吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    #C0065
    ChrTalk(
        0xB,
        (
            "#07303F……你的行程安排表已经\x01",
            "排到半年以后了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0066
    ChrTalk(
        0xA,
        (
            "#07201F#5P穆拉欺负人！\x01",
            "就不能让人家做做美梦嘛！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1300)
    SetChrSubChip(0x9, 0x1)
    Sleep(150)

    #C0067
    ChrTalk(
        0x9,
        (
            "#5P#07104F总之，情况就是这样。\x01",
            "我们对诸位已经有了\x01",
            "一定程度的了解。\x02\x03",

            "#07100F在此基础上，有几件事情\x01",
            "想告知各位……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(50)
    SetChrSubChip(0xA, 0x0)

    #C0068
    ChrTalk(
        0x101,
        (
            "#6P#00001F好的，\x01",
            "也就是今天要谈的正题吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        (
            "#6P#00101F关于这次的通商会议，\x01",
            "你们是否掌握了什么重要的情报？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "#11P#07003F是的……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    SetChrSubChip(0x8, 0x2)
    Sleep(300)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -96900, 0, 53400, 270)
    OP_0D()
    OP_92(0x9, 0xFFFE8CE8, 0xD6D8, 0x1F4)

    def lambda_2CD2():
        OP_95(0xFE, -95000, 0, 55000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2CD2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x2D, 0x1F4)
    OP_68(-99000, 1000, 54550, 2000)
    MoveCamera(20, 17, 0, 2000)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)
    Sound(72, 0, 100, 0)
    OP_74(0x4, 0xF)
    OP_71(0x4, 0xB, 0x14, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    Sound(939, 0, 50, 0)
    OP_71(0x4, 0x15, 0x1E, 0x0, 0x0)
    OP_79(0x4)
    OP_74(0x4, 0x1E)
    OP_24(0x3AB)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0071
    AnonymousTalk(
        0x109,
        "#10105F啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0072
    AnonymousTalk(
        0x101,
        (
            "#00000F这是爱普斯泰恩财团\x01",
            "开发的系统吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0073
    AnonymousTalk(
        0x9,
        (
            "#07104F是的，这艘舰艇的信息处理系统\x01",
            "是从财团引进的。\x02\x03",

            "#07101F请看这边。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(1021, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_70(0x4, 0x28)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    Sleep(500)

    #A0074
    AnonymousTalk(
        0x102,
        (
            "#00108F……这位是埃雷波尼亚帝国的宰相，\x01",
            "吉利亚斯·奥斯本阁下吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0075
    AnonymousTalk(
        0xA,
        (
            "#07200F叫他『铁血宰相』就行了。\x02\x03",

            "由于你们并不熟悉此人，\x01",
            "所以我就不在这里对他做负面评价了。\x02\x03",

            "#07203F但作为前提，\x01",
            "我希望你们了解一件事。\x02\x03",

            "#07201F如今，埃雷波尼亚帝国\x01",
            "随时都有可能发生内战。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-99250, 1100, 50090, 0)
    MoveCamera(38, 14, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18950, 0)
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x9, 0x8, 0)
    SetChrSubChip(0x104, 0x2)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0076
    ChrTalk(
        0x101,
        "#6P#00013F什么……！\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x109,
        "#6P#10107F有、有这种事！？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "#07206F很遗憾，但这确实是事实。\x02\x03",

            "#07208F具体来说，帝国目前分为以宰相为首，\x01",
            "意图在帝国创建\x01",
            "新型中央集权体制的『革新派』……\x02\x03",

            "还有以掌权贵族为首，\x01",
            "希望维持旧有贵族制度的\x01",
            "『贵族派』……\x02\x03",

            "#07201F这两大派系相互敌对，\x01",
            "正处于一触即发的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#6P#00001F革新派与贵族派的对立……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#6P#00106F……我之前就有所耳闻，\x01",
            "看来现状相当严峻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#6P#N#10300F唔，如此看来，\x01",
            "殿下应该是中立派的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0082
    ChrTalk(
        0xA,
        (
            "#07202F呵呵，与其说是中立，\x01",
            "倒不如说我想走第三条路。\x02\x03",

            "#07206F但两大阵营却都把我视为\x01",
            "无法信任的可疑之人，\x01",
            "真是让人悲哀的处境啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        "#07303F……嗯，这倒是无法否定。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#6P#00008F话说回来……\x01",
            "两大派系的对立，使帝国陷入到\x01",
            "随时有可能爆发内战的状况……\x02\x03",

            "#00013F莫非这就是关系到通商会议的\x01",
            "『重要情报』吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x109,
        "#6P#10111F啊……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        "#6P#N#10306F……原来如此。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0087
    ChrTalk(
        0xB,
        (
            "#07306F正如你所言。\x02\x03",

            "#07301F『贵族派』的当权者\x01",
            "凯恩大公已经有所行动了。\x02\x03",

            "他计划在本次通商会议的召开期间，\x01",
            "派遣恐怖分子潜入克洛斯贝尔，\x01",
            "刺杀奥斯本宰相。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0088
    ChrTalk(
        0x101,
        "#6P#00010F……！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#6P#00101F那个……不是杀手，\x01",
            "而是恐怖分子吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "#07203F宰相树敌众多，除了贵族派之外，\x01",
            "恨他入骨的人也不在少数。\x02\x03",

            "因此，被他镇压的国内外势力\x01",
            "结成了恐怖组织。\x02\x03",

            "#07201F而贵族派则付给他们米拉，\x01",
            "从而利用他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        "#6P#00301F原来是这样……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x105,
        (
            "#6P#N#10304F既不用脏了自己的手，\x01",
            "又可以将政敌消灭。\x02\x03",

            "#10305F这样一来，\x01",
            "情况可就相当棘手了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x101, 0x2)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0093
    ChrTalk(
        0x101,
        (
            "#5P#00007F何止是棘手这么简单！\x01",
            "对克洛斯贝尔来说，这也是重大事件！\x02\x03",

            "#00010F如果帝国宰相在市长举办的\x01",
            "会议中遭到暗杀，\x01",
            "不知将会被索赔多少──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    #C0094
    ChrTalk(
        0x101,
        "#6P#00006F对、对不起，这样说有些失礼……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#07204F不，你这种担心是很正常的。\x02\x03",

            "#07201F作为未能防范暗杀的代价，\x01",
            "帝国一定会向克洛斯贝尔\x01",
            "自治州索取巨额赔偿。\x02\x03",

            "即使个中缘由是因\x01",
            "帝国内部的对立而生。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x109,
        "#6P#10106F难、难以置信……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x102,
        (
            "#6P#00108F……虽然听起来很冷酷，\x01",
            "但外交就是有这样的一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        "#6P#00306F……说的也对。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#11P#07008F另外——\x02\x03",

            "#07003F其实在共和国那边\x01",
            "也有着同样的计划。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x101,
        "#6P#00011F咦……！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        "#6P#00105F是、是这样吗！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(300)

    #C0102
    ChrTalk(
        0x8,
        "#11P#07001F尤莉亚，麻烦你了。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        "#07100F是。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x1F4)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(300)
    OP_74(0x4, 0xF)
    Sound(1021, 0, 100, 0)
    OP_71(0x4, 0x29, 0x32, 0x0, 0x0)
    OP_79(0x4)
    OP_74(0x4, 0x1E)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)

    #A0104
    AnonymousTalk(
        0x102,
        (
            "#00101F卡尔瓦德共和国政府代表——\x01",
            "萨缪尔·洛克史密斯总统……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0105
    AnonymousTalk(
        0x105,
        (
            "#10301F这位大叔\x01",
            "也遭人怨恨吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0106
    AnonymousTalk(
        0x8,
        (
            "#07003F不，与其说是对他个人的怨恨，\x01",
            "倒不如说是因为卡尔瓦德的历史。\x02\x03",

            "在地处西塞姆里亚大陆，自很久以前\x01",
            "就开始吸收多元文化的卡尔瓦德，\x01",
            "有个非常麻烦的问题。\x02\x03",

            "#07001F那就是所谓的『民族问题』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0107
    AnonymousTalk(
        0x109,
        "#10101F民族问题……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0108
    AnonymousTalk(
        0x9,
        (
            "#07103F正如诸位所知，卡尔瓦德\x01",
            "自古以来，一直都在接收来自东方的移民。\x02\x03",

            "#07108F自从改为共和制之后，\x01",
            "这样的趋势更加明显，\x01",
            "甚至诞生了规模巨大的东方人街……\x02\x03",

            "#07101F这种趋势自然会招致\x01",
            "一部分人的反对。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0109
    AnonymousTalk(
        0x102,
        (
            "#00106F……也就是反东方·反移民政策主义吧？\x02\x03",

            "#00108F我只是知道有那样的\x01",
            "运动存在，但没想到……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0110
    AnonymousTalk(
        0x101,
        (
            "#00001F难道那些民族主义者\x01",
            "企图袭击总统吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0111
    AnonymousTalk(
        0x8,
        (
            "#07003F嗯，听说有个资金充裕的\x01",
            "投资方资助了他们……\x02\x03",

            "#07001F根据我们了解到的情报，某个拥有最新型武装的\x01",
            "激进派恐怖组织正在行动。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0112
    AnonymousTalk(
        0x101,
        "#00008F…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0113
    AnonymousTalk(
        0x104,
        "#00303F……这可麻烦了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x9, 0x8, 0)
    SetChrSubChip(0x104, 0x2)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)

    def lambda_3D91():
        OP_95(0xFE, -96900, 0, 53300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D91)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x2, 0x3)
    Sound(73, 0, 100, 0)
    OP_71(0x4, 0x33, 0x3C, 0x0, 0x0)
    WaitChrThread(0x9, 1)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -96900, 50, 52400, 270)
    OP_0D()
    SetChrSubChip(0x9, 0x1)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0114
    ChrTalk(
        0x101,
        (
            "#6P#00006F我明白几位的意思了。\x02\x03",

            "#00001F但为何要把如此重要的\x01",
            "事情告诉我们……？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        (
            "#6P#N#10300F确实，直接传达给自治州政府\x01",
            "应该会更好吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    OP_64(0x9)
    OP_64(0xA)
    OP_64(0xB)

    #C0116
    ChrTalk(
        0x102,
        (
            "#6P#00106F……有些事情，即使想要传达\x01",
            "也是没有办法的。\x02\x03",

            "#00101F没错吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)

    #C0117
    ChrTalk(
        0x101,
        "#6P#00005F咦……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "#07203F正如艾莉小姐所说。\x02\x03",

            "#07208F无论是奥斯本宰相，\x01",
            "还是洛克史密斯总统……\x02\x03",

            "都已经知道企图袭击\x01",
            "自己的组织开始行动了。\x02\x03",

            "#07201F但即使如此，他们也没有\x01",
            "向克洛斯贝尔政府透露分毫情况。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0119
    ChrTalk(
        0x101,
        "#6P#00013F……！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#11P#07003F虽然尚不知晓他们\x01",
            "有何打算……\x02\x03",

            "#07008F但在这种情况之下，\x01",
            "我们也不便擅自通报\x01",
            "帝国和共和国的内部情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "#07206F我虽然是皇族，\x01",
            "但却无法干涉帝国政府的方针。\x02\x03",

            "#07200F所以公主殿下提议\x01",
            "邀请你们前来。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#6P#00003F……原来如此。\x02\x03",

            "#00000F也就是说，这只是\x01",
            "非官方性质的私下会谈吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "#11P#07009F嗯，只是几个拥有相同朋友的人\x01",
            "在茶桌上随便闲聊几句而已……\x02\x03",

            "#07002F当然，如果想把在这里听到的\x01",
            "传闻透露给他人，敬请自便。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        "#6P#00102F呵呵，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#6P#00304F哎呀呀……\x01",
            "比想象中还要大胆呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x105,
        (
            "#6P#N#10302F呵呵，身为优雅的公主，\x01",
            "您倒是颇有手段啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x109, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x109, 0x2)
    Sleep(150)

    #C0127
    ChrTalk(
        0x109,
        (
            "#5P#10111F瓦、瓦吉，\x01",
            "你太失礼了……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#11P#07004F呵呵，没关系的。\x02\x03",

            "#07008F围绕着克洛斯贝尔的状况\x01",
            "正在迷雾之中越陷越深……\x02\x03",

            "#07000F为了能略微看清前方的道路，\x01",
            "也只得尽力挣扎了。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "#07206F毕竟还有一些\x01",
            "很麻烦的人物\x01",
            "在控制情报。\x02\x03",

            "#07200F在这种状况下，我们自然要\x01",
            "好好利用一下艾丝蒂尔他们的人脉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x109, 0x0)
    OP_63(0x105, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0130
    ChrTalk(
        0x101,
        "#6P#00005F很麻烦的人物……？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "#11P#07003F……我想你们应该听说过他们。\x02\x03",

            "#07001F那就是雷克特·亚兰德尔先生\x01",
            "和雾香·楼兰女士二人。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#6P#00001F……！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        (
            "#6P#00103F……原来是这样啊。\x02\x03",

            "#00101F之前说的那些情报之所以\x01",
            "没有被克洛斯贝尔政府得知……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "#5P#07103F嗯，就是因为他们两人在操纵情报。\x02\x03",

            "#07100F雾香女士曾在利贝尔\x01",
            "担任游击士协会的接待员，\x01",
            "她拥有一双可以洞察千里的慧眼。\x02\x03",

            "操纵这点情报\x01",
            "自然是毫无难度。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#6P#00008F……原来如此，\x01",
            "我们在协会也有所耳闻……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#6P#00306F如果是友方倒还好，若是与我们为敌，\x01",
            "她肯定是最棘手的类型……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "#07303F至于雷克特·亚兰德尔──\x02\x03",

            "虽然他的经历不详，出身不明，\x01",
            "但至少有一点可以确定。\x02\x03",

            "#07301F那就是……他是『铁血之子』\x01",
            "这个组织中的一员。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x109,
        "#6P#10111F铁、铁血之子……？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x105,
        (
            "#6P#N#10306F又是个很古怪的名称啊。\x02\x03",

            "#10300F听起来似乎是个与铁血宰相\x01",
            "存在关联的组织？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0140
    ChrTalk(
        0xA,
        (
            "#07203F据说他们都是被宰相阁下选中，\x01",
            "从小就开始培养的年轻人。\x02\x03",

            "虽然有些怪癖，但能力强得可怕，\x01",
            "从事着各种活动。\x02\x03",

            "#07200F贵族派们都在\x01",
            "最大限度地戒备着他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        "#11P#07008F………………………………\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#6P#00003F……『铁血之子』。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#6P#00108F看来这个对手远不止是\x01",
            "情报军官那么简单啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "#5P#07103F……另外，如今盘踞在克洛斯贝尔的\x01",
            "『黑月』和『赤色星座』也不容忽视。\x02\x03",

            "#07100F这两个组织都与政府存在着千丝万缕的联系，\x01",
            "很难想象他们会在会议期间发动袭击……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "#07303F但据我们所知，他们也有过一些\x01",
            "令人难以理解的动向。\x02\x03",

            "#07300F关于这方面，你们也许\x01",
            "了解得更加清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#6P#00003F是的……\x02\x03",

            "#00000F算不上是什么还礼，\x01",
            "我现在就把目前了解到的\x01",
            "情况告诉各位。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人向对方说明了\x01",
            "『赤色星座』和『黑月』的近期动向。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    #C0148
    ChrTalk(
        0x9,
        "#5P#07105F……竟有这种事。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "#07301F唔，那个名叫『银』的杀手\x01",
            "倒是令人有些在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "#07204F但应该不必担心他袭击\x01",
            "宰相阁下或我吧？\x02\x03",

            "#07200F至于『赤色星座』，\x01",
            "似乎是个极其好战的猎兵团。\x02\x03",

            "像我这种基本没带护卫的人，\x01",
            "做他们的目标\x01",
            "恐怕都不够资格吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#6P#00309F哈哈……\x01",
            "或许正如你所说。\x02\x03",

            "#00300F不过，既然有那位少校先生随行，\x01",
            "有些人说不定会渴求一战呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "#07303F那种可能性并不大，\x01",
            "毕竟我只是一介单兵而已。\x02\x03",

            "#07300F不管怎么说，我们目前也只能\x01",
            "把有可能发生的各种状况都考虑周全，\x01",
            "并做好充足准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "#5P#07108F是啊……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0154
    ChrTalk(
        0x8,
        (
            "#11P#07004F各位，\x01",
            "多谢你们提供的情报。\x02\x03",

            "#07002F多亏你们，我们才能\x01",
            "对各种事态做好准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#6P#00002F哪、哪里，您太客气了！\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        (
            "#6P#00102F几位将那么重要的情报透露给我们，\x01",
            "我们才应该道谢……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        "#6P#10109F实在是太感谢了！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0158
    ChrTalk(
        0xA,
        (
            "#07209F哈哈哈，彼此彼此。\x02\x03",

            "#07202F话说回来，既然你们心存谢意，\x01",
            "不如就带我去体验一下克洛斯贝尔的\x01",
            "知名夜店如何？\x02\x03",

            "兰迪和瓦吉应该\x01",
            "很熟悉那些地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        "#6P#00305F哦，那我们这就出发吧。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x105,
        (
            "#6P#N#10309F呵呵，就带你去\x01",
            "我秘藏的那家最棒的店吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0161
    ChrTalk(
        0xA,
        (
            "#07212F哦哦，既然决定了，\x01",
            "那晚宴的安排就取消好了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    #C0162
    ChrTalk(
        0xB,
        (
            "#07306F那怎么可能，蠢货。\x02\x03",

            "#07301F我们稍后还要去观看\x01",
            "彩虹剧团的演出呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0163
    ChrTalk(
        0xA,
        (
            "#07201F#5P……这倒也是。\x02\x03",

            "#07206F唔……彩虹剧团的演出\x01",
            "也是我一直想看的。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#6P#00012F哈哈……\x01",
            "相信一定能让各位尽兴而归。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#6P#00109F嗯，保证能让大家\x01",
            "看得目不转睛。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(50)
    SetChrSubChip(0xA, 0x0)

    #C0166
    ChrTalk(
        0x8,
        (
            "#11P#07009F呵呵，那我就好好期待一下吧。\x02\x03",

            "#07002F……如果今后发生了什么状况，\x01",
            "我们还会再联络诸位的。\x02\x03",

            "下次会直接联络你们，\x01",
            "就不再麻烦基库了。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        "#11P#08009F啾。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#6P#00004F哈哈，知道了。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#6P#00302F让它来传话，\x01",
            "多少有点奇怪呢。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19450, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x1F2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_597 end

    SaveToFile()

Try(main)
