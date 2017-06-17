from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "クローディア姫",         # 1
        "ユリア准佐",             # 2
        "オリヴァルト皇子",       # 3
        "ミュラー少佐",           # 4
        "ジーク",                 # 5
        "親衛隊",                 # 6
        "親衛隊",                 # 7
        "親衛隊",                 # 8
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
            "#11P#07104F──殿下、失礼します。\x02\x03",

            "特務支援課の諸君を\x01",
            "お連れしました。\x02",
        )
    )

    CloseMessageWindow()

    #N0002
    NpcTalk(
        0x8,
        "涼しげな声",
        "#3C#2S#11Pどうぞ、お通ししてください。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(100, 0, 80, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x2)

    def lambda_BBD():
        OP_95(0xFE, -97800, 70, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BBD)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xE1, 0x1F4)

    def lambda_BE2():

        label("loc_BE2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BE2")

    QueueWorkItem2(0x9, 2, lambda_BE2)

    #C0003
    ChrTalk(
        0x9,
        "#5P#07102Fさあ、どうぞ中へ。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#12P#00001Fは、はい。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#00104Fそれでは失礼します。\x02",
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
        "#6P#00005Fあ……\x02",
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
            "ふふっ、初めまして。\x02\x03",

            "リベール王国、王太女の\x01",
            "クローディアと申します。\x02\x03",

            "あのような形でお呼びして\x01",
            "本当に申し訳ありませんでした。\x02",
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
        "#5P#08009Fピュイ。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#6P#00011Fい、いえ、とんでもない。\x02\x03",

            "#00003F初めまして──\x01",
            "クロスベル警察、特務支援課の\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        (
            "#6P#00104F同じく特務支援課、\x01",
            "エリィ・マクダエルです。\x02\x03",

            "#00102F王太女殿下におかれましては\x01",
            "ご機嫌麗しゅう。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#07009F#5Pふふ、エリィさんのことは\x01",
            "実は色々聞いていまして……\x02\x03",

            "#07002Fお会いできて嬉しいです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x102,
        "#6P#00105Fそうなのですか……？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#07004F#5Pええ、先ほどお祖父様の\x01",
            "マクダエル議長閣下と\x01",
            "お話する機会をいただきました。\x02\x03",

            "#07000Fそれと、マリアベルさんとは\x01",
            "何度か面識がありまして。\x02\x03",

            "何でも以前、リベールにも\x01",
            "留学されていた経験がおありだとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#6P#00104Fはい。\x01",
            "３ヶ月ほどの滞在でしたが……\x02\x03",

            "#00102Fご挨拶もできずに失礼しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "#07009Fいえいえ、こちらこそ。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#6P#00309Fはは……どうも。\x01",
            "ランディ・オルランドっス。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x109,
        (
            "#6P#N#10100Fノ、ノエル・シーカーです！\x01",
            "よろしくお願いします！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0018
    ChrTalk(
        0x105,
        (
            "#12P#10304Fワジ・ヘミスフィア。\x01",
            "麗#2Rうるわ#しの姫君にお会いできて光栄だよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0019
    ChrTalk(
        0x8,
        (
            "#07009F#5Pようこそお出でくださいました。\x02\x03",

            "#07004F本当なら、この場でもう一人、\x01",
            "ご紹介したい方がいたのですが……\x02\x03",

            "#07000Fその、少し遅れてらっしゃるみたいで。\x02",
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
        "飄々とした声",
        (
            "フッ……\x01",
            "心配には及ばないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_1E13")

    def lambda_144D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_144D)

    def lambda_145A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_145A)
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

    def lambda_14EE():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14EE)
    Sleep(50)

    def lambda_14FE():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_14FE)
    Sleep(50)

    def lambda_150E():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_150E)
    Sleep(50)

    def lambda_151E():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_151E)
    Sleep(50)

    def lambda_152E():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_152E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0021
    ChrTalk(
        0x101,
        "#00005F#5Pこの音って……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#00108F#5Pど、どこかで聞いたような。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        "#00305F#5Pおいおい、まさか──\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "#11P#07104F#5Pフフ……\x01",
            "いらしたようですね。\x02",
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

    def lambda_1702():
        OP_95(0xFE, -96300, 0, 101200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1702)

    def lambda_171C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_171C)
    Sleep(700)

    def lambda_1730():
        OP_95(0xFE, -95100, 0, 101000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1730)

    def lambda_174A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_174A)
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
        "#6P#00011F#4Sええっ！？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x109,
        (
            "#12P#10111Fも、もしかして\x01",
            "さっきの支援要請の！？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "#07005F#6P#Nあら、すでにご面識が？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0028
    ChrTalk(
        0x102,
        "#12P#00109Fええ、その……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x105,
        (
            "#10302Fフフ……\x01",
            "とんだサプライズだね。\x02",
        )
    )

    CloseMessageWindow()

    #N0030
    NpcTalk(
        0xB,
        "帝国軍将校",
        (
            "#5P#07303F──諸君、先ほどは失礼した。\x02\x03",

            "#07308F#11Pクローディア殿下も……\x01",
            "遅れて申し訳ありませんでした。\x02\x03",

            "#07301Fいつものように、この戯#2Rタワ#けが\x01",
            "色々と首を突っ込んでいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        "#07009F#6P#Nふふ、まあ……\x02",
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

    def lambda_1AAA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AAA)

    #N0032
    NpcTalk(
        0xA,
        "金髪の青年",
        (
            "#5P#07204F──フッ、改めて\x01",
            "自己紹介をさせてもらおう。\x02",
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
    SetChrName("金髪の青年")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            "エレボニア帝国、皇帝ユーゲントが名代、\x01",
            "オリヴァルト・ライゼ・アルノールさ。\x02\x03",

            "もちろん、真の姿は\x01",
            "不世出の天才にして漂白の演奏家、\x01",
            "オリビエ・レンハイムではあるがね！\x02\x03",

            "ハッハッハッ。\x01",
            "よろしくお願いしてくれたまえっ。\x02",
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
        "#6P#00011F……………………（パクパク）\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#12P#00301Fいや……あり得なくねぇか？\x02",
    )

    CloseMessageWindow()

    #N0036
    NpcTalk(
        0xB,
        "帝国軍将校",
        (
            "#5P#07306Fこれが現実だ。\x01",
            "極めて遺憾なことにな。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("帝国軍将校")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            "──帝国軍、第７機甲師団所属、\x01",
            "ミュラー・ヴァンダール少佐だ。\x02\x03",

            "クローディア殿下のお招きで\x01",
            "あるじ共々、参上させてもらった。\x02\x03",

            "よろしく頼む──特務支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Jump("loc_271C")

    label("loc_1E13")


    def lambda_1E18():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1E18)

    def lambda_1E25():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E25)
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

    def lambda_1EAD():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EAD)
    Sleep(50)

    def lambda_1EBD():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1EBD)
    Sleep(50)

    def lambda_1ECD():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1ECD)
    Sleep(50)

    def lambda_1EDD():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1EDD)
    Sleep(50)

    def lambda_1EED():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1EED)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0038
    ChrTalk(
        0x101,
        "#00005F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#00108F#5Pリュートの音……？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "#5P#07104Fフフ……\x01",
            "いらしたようですね。\x02",
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

    def lambda_2089():
        OP_95(0xFE, -96300, 0, 101200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2089)

    def lambda_20A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_20A3)
    Sleep(700)

    def lambda_20B7():
        OP_95(0xFE, -95100, 0, 101000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_20B7)

    def lambda_20D1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_20D1)
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
        "#6P#00011Fあ……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#12P#10111Fエ、エレボニア帝国の……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        "#12P#00105Fオリヴァルト皇子殿下……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)
    Sleep(150)

    #N0044
    NpcTalk(
        0xB,
        "帝国軍将校",
        (
            "#07303F#11P──クローディア殿下、\x01",
            "遅れて申し訳ありませんでした。\x02\x03",

            "#07301Fいつものように、この戯#2Rタワ#けが\x01",
            "色々と首を突っ込んでいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "#07009F#6P#Nふふ、まあ……\x02",
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

    def lambda_2387():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2387)

    #C0046
    ChrTalk(
        0xA,
        "#5P#07204F──フッ、初めまして諸君。\x02",
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
            "エレボニア帝国、皇帝ユーゲントが名代、\x01",
            "オリヴァルト・ライゼ・アルノールさ。\x02\x03",

            "まあ正直、皇子なんかよりも\x01",
            "愛を求める漂白の演奏家として\x01",
            "旅に出たいのだがねぇ。\x02\x03",

            "ハッハッハッ。\x01",
            "よろしくお願いしてくれたまえっ。\x02",
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
        "#6P#00011Fあ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#12P#00109Fよ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#12P#00305Fなんか帝国の皇子とは\x01",
            "思えないほどの軽さなんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x105,
        "#10305Fていうか、なんでリュート？\x02",
    )

    CloseMessageWindow()

    #N0052
    NpcTalk(
        0xB,
        "帝国軍将校",
        (
            "#5P#07306Fまあ、コレに関しては\x01",
            "できれば流してくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("帝国軍将校")

    #A0053
    AnonymousTalk(
        0xFF,
        (
            "──帝国軍、第７機甲師団所属、\x01",
            "ミュラー・ヴァンダール少佐だ。\x02\x03",

            "クローディア殿下のお招きで\x01",
            "あるじ共々、参上させてもらった。\x02\x03",

            "よろしく頼む──特務支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    label("loc_271C")

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
            "#00004Fなるほど……\x01",
            "彼女#4Rエステル#たちから聞いたんですか。\x02",
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
            "#6P#00102F皆さんがエステルさんたちと\x01",
            "冒険を共にした仲だったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#6P#00309Fハハッ、つくづく\x01",
            "とんでもないコンビだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        (
            "#07204Fまあ、そんなワケで\x01",
            "気をラク～にしてくれたまえ。\x02\x03",

            "#07202Fボクたちとエステル君たちは\x01",
            "リベールの異変に立ち向かった仲間。\x02\x03",

            "そしてキミたちとエステル君たちも\x01",
            "クロスベルの異変に立ち向かった仲間。\x02\x03",

            "#07209Fつまりボクたちも\x01",
            "運命の仲間同士というわけさっ♪\x02",
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
            "#6P#00012Fい、いや～。\x01",
            "そう単純にはいかないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#6P#00106Fその……\x01",
            "正直、畏#2Rおそ#れ多いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "#11P#07004Fふふっ、でも本当に\x01",
            "気を楽になさってください。\x02\x03",

            "#07002F相談したい事があって\x01",
            "お呼びしたのも確かですが……\x02\x03",

            "それ以上に、皆さんとお近づきに\x01",
            "なりたいと思っていたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#6P#00000F姫殿下……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#6P#00309Fおお、感激ッス……！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        "#6P#10112Fあわわ……きょ、恐縮です！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "#07204Fしかし、エステル君たちも\x01",
            "どうやらクロスベルで楽しく\x01",
            "過ごしていたようだねぇ。\x02\x03",

            "#07209Fテーマパークなんてのもあるし、\x01",
            "ボクも１ヶ月ほど滞在して──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    #C0065
    ChrTalk(
        0xB,
        (
            "#07303F……お前のスケジュールは\x01",
            "向こう半年埋まっているがな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0066
    ChrTalk(
        0xA,
        (
            "#07201F#5Pミュラー君のイケズ！\x01",
            "夢見たっていいじゃない！\x02",
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
            "#5P#07104Fまあ、そんな訳で\x01",
            "こちらは君たちについて\x01",
            "一通り知っている状態だ。\x02\x03",

            "#07100Fそれを踏まえて幾つか君たちに\x01",
            "伝えたいことがあるんだが……\x02",
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
            "#6P#00001F──はい。\x01",
            "本題というわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        (
            "#6P#00101F何でも、通商会議に関する\x01",
            "気になる情報をお持ちだとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "#11P#07003Fはい……\x02",
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

    def lambda_302E():
        OP_95(0xFE, -95000, 0, 55000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_302E)
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
        "#10105Fあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0072
    AnonymousTalk(
        0x101,
        (
            "#00000Fエプスタイン財団製の\x01",
            "システムを使っているんですね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0073
    AnonymousTalk(
        0x9,
        (
            "#07104Fああ、この艦の情報処理システムは\x01",
            "財団のものを導入しているからね。\x02\x03",

            "#07101Fこちらを見て欲しい。\x02",
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
            "#00108F……エレボニア帝国宰相、\x01",
            "ギリアス・オズボーン閣下ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0075
    AnonymousTalk(
        0xA,
        (
            "#07200Fま、《鉄血宰相》でいいさ。\x02\x03",

            "彼の人となりを知らない君たちに\x01",
            "ここで悪口を言うつもりはない。\x02\x03",

            "#07203Fただ、一つだけ前提として\x01",
            "知っていて欲しいことがあるんだ。\x02\x03",

            "#07201F──現在、エレボニア帝国内で\x01",
            "いつ内戦が起きてもおかしくない事を。\x02",
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
        "#6P#00013Fな……！\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x109,
        "#6P#10107Fそ、そうなんですか！？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "#07206F残念ながら事実だ。\x02\x03",

            "#07208F具体的には、宰相を中心とする\x01",
            "帝国に新たな中央集権体制を\x01",
            "作り上げようとする『革新派』……\x02\x03",

            "そして有力貴族を中心とする、\x01",
            "旧い貴族制度を維持し続けようとする\x01",
            "『貴族派』……\x02\x03",

            "#07201F──この２つによる対立が\x01",
            "行き着くところまで行ってるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#6P#00001F革新派と貴族派の対立……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#6P#00106F……話は聞いていましたけど\x01",
            "相当、深刻な状況みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#6P#N#10300Fふむ、察するところ、\x01",
            "殿下は中立のお立場なのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0082
    ChrTalk(
        0xA,
        (
            "#07202Fフフ、中立というより\x01",
            "第３の道を行こうと思っている。\x02\x03",

            "#07206Fま、どちらの陣営からも\x01",
            "胡散臭いコウモリに見られてしまう\x01",
            "切ない立場なんだけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        "#07303F……まあ、否定はできんな。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#6P#00008Fし、しかし……\x01",
            "両者の対立が、内戦直前まで\x01",
            "行き着いているということは……\x02\x03",

            "#00013Fまさか通商会議に関する\x01",
            "『気になる情報』というのは！？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x109,
        "#6P#10111Fあ……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        "#6P#N#10306F……なるほどね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0087
    ChrTalk(
        0xB,
        (
            "#07306F──君の懸念どおりだ。\x02\x03",

            "#07301F『貴族派』の有力者である\x01",
            "カイエン公の方で動きがあった。\x02\x03",

            "どうやら、この通商会議中、\x01",
            "オズボーン宰相を狙うテロリストを\x01",
            "クロスベルに送り込むらしい。\x02",
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
        "#6P#00010F……っ！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#6P#00101Fその、刺客ではなく\x01",
            "テロリストというのは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "#07203F宰相殿は、貴族派以外からも\x01",
            "激しい恨みを買っていてねぇ。\x02\x03",

            "国内外で弾圧された勢力が\x01",
            "テロ組織を結成しているんだ。\x02\x03",

            "#07201Fそんな連中を、貴族派が体よく\x01",
            "ミラを与えて利用しているわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        "#6P#00301Fそういうことか……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x105,
        (
            "#6P#N#10304F自分たちの手は汚さずに\x01",
            "政敵を葬ろうってワケだね。\x02\x03",

            "#10305Fでも、そんな事になったら\x01",
            "さすがに色々マズイんじゃない？\x02",
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
            "#5P#00007Fマズイどころじゃない！\x01",
            "クロスベルにとっても大問題だ！\x02\x03",

            "#00010F市長が開催した会議中に\x01",
            "帝国の宰相が暗殺されたりしたら\x01",
            "どんな賠償を要求されるか──\x02",
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
        "#6P#00006Fす、すみません……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#07204Fいや、その心配はもっともだ。\x02\x03",

            "#07201F暗殺を防げなかった代償として\x01",
            "帝国からクロスベル自治州に\x01",
            "莫大な賠償が突きつけられるだろう。\x02\x03",

            "たとえそれが帝国内での\x01",
            "対立問題から起きたことでもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x109,
        "#6P#10106Fし、信じられない……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x102,
        (
            "#6P#00108F……非情なようだけど\x01",
            "それもまた外交の一側面だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        "#6P#00306F……だろうな。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#11P#07008F───そして。\x02\x03",

            "#07003F実は同じような構図が\x01",
            "共和国の方にもあるのです。\x02",
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
        "#6P#00011Fえ……！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        "#6P#00105Fそ、そうなのですか！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(300)

    #C0102
    ChrTalk(
        0x8,
        "#11P#07001Fユリアさん、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        "#07100Fは。\x02",
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
            "#00101Fカルバード共和国政府代表、\x01",
            "サミュエル・ロックスミス大統領……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0105
    AnonymousTalk(
        0x105,
        (
            "#10301Fこっちのオジサンも\x01",
            "恨みを抱えちゃってるとか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0106
    AnonymousTalk(
        0x8,
        (
            "#07003Fいえ、彼がどうというよりは\x01",
            "カルバードの歴史によるものです。\x02\x03",

            "西ゼムリアにあって、様々な文化を\x01",
            "昔から取り入れてきたカルバードには\x01",
            "非常に難しい問題があります。\x02\x03",

            "#07001Fいわゆる『民族問題』です。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0107
    AnonymousTalk(
        0x109,
        "#10101F民族問題……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0108
    AnonymousTalk(
        0x9,
        (
            "#07103F知っての通り、カルバードは昔から\x01",
            "東方系の移民を受け入れてきた国だ。\x02\x03",

            "#07108F共和制に移行してからその流れは\x01",
            "顕著になり、巨大な東方人街などが\x01",
            "誕生することになったのだが……\x02\x03",

            "#07101F当然、そうした流れに対する\x01",
            "反動というものがあり得るわけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0109
    AnonymousTalk(
        0x102,
        (
            "#00106F……反東方・移民政策主義ですね。\x02\x03",

            "#00108Fそのような運動が存在するのは\x01",
            "知識としては知っていましたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0110
    AnonymousTalk(
        0x101,
        (
            "#00001Fそうした民族主義者が\x01",
            "大統領を狙っているんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0111
    AnonymousTalk(
        0x8,
        (
            "#07003Fええ、やはり潤沢な資金源を持つ\x01",
            "スポンサーがいるらしく……\x02\x03",

            "#07001F最新の武装を供与された過激派#6Rテロリスト#が\x01",
            "動いているという情報が入っています。\x02",
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
        "#00303F……そいつは厄介ッスね。\x02",
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

    def lambda_430F():
        OP_95(0xFE, -96900, 0, 53300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_430F)
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
            "#6P#00006F──お話は判りました。\x02\x03",

            "#00001Fですが、どうしてこのような\x01",
            "重大な話を自分たちに……？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        (
            "#6P#N#10300F確かに、自治州政府に直接\x01",
            "伝えた方がいいんじゃないの？\x02",
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
            "#6P#00106F……伝えたくても\x01",
            "伝えられない事情がある。\x02\x03",

            "#00101Fつまり、そういう事ですね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)

    #C0117
    ChrTalk(
        0x101,
        "#6P#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "#07203Fエリィ君の言う通りさ。\x02\x03",

            "#07208Fオズボーン宰相にしても\x01",
            "ロックスミス大統領にしても……\x02\x03",

            "当然、自分たちを付け狙う勢力が\x01",
            "動いているのは知っているはずだ。\x02\x03",

            "#07201Fにも関わらず、クロスベル政府に\x01",
            "その事実は全く伝えられていない。\x02",
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
            "#11P#07003Fそこにどのような思惑があるのか\x01",
            "現時点では分かりませんが……\x02\x03",

            "#07008Fただ、そのような状況で\x01",
            "こちらが帝国と共和国の裏事情を\x01",
            "勝手に伝えるわけにもいきません。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "#07206Fそしてボクも皇族とはいえ、\x01",
            "帝国政府の方針に干渉は出来ない……\x02\x03",

            "#07200Fそこで姫殿下の提案で\x01",
            "キミたちを呼んだというわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#6P#00003F………なるほど。\x02\x03",

            "#00000Fつまり、ここでの話は\x01",
            "あくまで非公式というわけですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "#11P#07009Fええ、共通の友人を持つ者同士の\x01",
            "お茶の席でのちょっとしたお喋り……\x02\x03",

            "#07002F無論、そこで聞いた噂話を\x01",
            "どなたにお伝えしようと自由です。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        "#6P#00102Fふふっ、そういう事ですか。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#6P#00304Fいやはや……\x01",
            "思った以上に大胆っつーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x105,
        (
            "#6P#N#10302Fフフ、優雅なお姫さまの割に\x01",
            "なかなかのやり手みたいだね？\x02",
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
            "#5P#10111Fちょ、ちょっとワジ君。\x01",
            "幾らなんでも失礼なんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#11P#07004Fふふっ、いいんです。\x02\x03",

            "#07008Fクロスベルを取り巻く状況は\x01",
            "ますます混迷を深めている……\x02\x03",

            "#07000F少しでも見通しを良くするためには\x01",
            "悪あがきをするしかありませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "#07206Fただでさえ、厄介な面々に\x01",
            "情報をコントロールされている\x01",
            "みたいだしねぇ。\x02\x03",

            "#07200Fエステル君方面のコネくらいは\x01",
            "活用させてもらわないと。\x02",
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
        "#6P#00005F厄介な面々……？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "#11P#07003F……多分、ご存知だと思います。\x02\x03",

            "#07001Fレクター・アランドール氏と\x01",
            "キリカ・ロウラン女史の２人です。\x02",
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
            "#6P#00103F……なるほど。\x02\x03",

            "#00101F先ほどの情報が、クロスベル政府に\x01",
            "ほとんど伝わっていないのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "#5P#07103F多分、その２人の情報操作だろう。\x02\x03",

            "#07100Fキリカ女史は、元々リベールで\x01",
            "遊撃士協会の受付をしていた人物だが\x01",
            "千里眼というべき慧眼#4Rけいがん#の持ち主でね。\x02\x03",

            "そのくらいの情報操作ならば\x01",
            "苦もなくやってのけるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#6P#00008F……なるほど。\x01",
            "ギルドの方でも聞きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#6P#00306F味方ならともかく、敵に回したら\x01",
            "一番厄介なタイプだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "#07303Fそして──レクター・アランドール。\x02\x03",

            "経歴不詳、出身も不明だが\x01",
            "一つ明らかになっていることがある。\x02\x03",

            "#07301Fそれは『鉄血の子供達#12Rア イ ア ン ブ リー ド#』と呼ばれる\x01",
            "メンバーの一人だということだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x109,
        "#6P#10111Fて、鉄血の子供たち……？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x105,
        (
            "#6P#N#10306Fまた大層な呼び名だね。\x02\x03",

            "#10300Fどうやら鉄血宰相と関係のある\x01",
            "メンバーみたいだけど？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0140
    ChrTalk(
        0xA,
        (
            "#07203F宰相殿が拾い上げたという\x01",
            "子飼いの若者たちらしくてね。\x02\x03",

            "クセはあるが恐ろしく有能で\x01",
            "様々な工作を行っているようだ。\x02\x03",

            "#07200F貴族派からは最大限に\x01",
            "警戒されているみたいだね。\x02",
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
        "#6P#00003F……『鉄血の子供達#12Rア イ ア ン ブ リー ド#』。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#6P#00108F単なる情報将校以上に\x01",
            "大変そうな相手みたいね……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "#5P#07103F……加えて、現在クロスベルに居座る\x01",
            "『黒月』と『赤い星座』の問題もある。\x02\x03",

            "#07100Fそれぞれ政府と繋がりがあるようだから\x01",
            "よもや会議を狙うとは思えないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "#07303Fだが、不可解な動きを見せているのは\x01",
            "こちらにも伝わっている。\x02\x03",

            "#07300Fそれについては君たちの方が\x01",
            "実情には詳しいかもしれないが。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#6P#00003Fはい……\x02\x03",

            "#00000F──お返しといってはなんですが\x01",
            "現状で分かっていることについて\x01",
            "お伝えします。\x02",
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
            "ロイドたちは『赤い星座』と\x01",
            "『黒月』の動きについて説明した。\x07\x00\x02",
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
        "#5P#07105F……そんな事が。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "#07301Fふむ、その《銀#2Rイン#》という刺客は\x01",
            "いささか気になるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "#07204Fまあ、宰相殿やボクを\x01",
            "狙う心配はないんじゃないかな？\x02\x03",

            "#07200Fそれに『赤い星座』というのは\x01",
            "恐ろしく好戦的な猟兵団らしい。\x02\x03",

            "護衛もあまり連れていない\x01",
            "ボクみたいな相手は標的として\x01",
            "物足りないんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#6P#00309Fハハ……\x01",
            "そうかもしれないッスね。\x02\x03",

            "#00300Fそちらの少佐さんがいるんなら\x01",
            "戦#2Rや#りたがるヤツもいそうですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "#07303Fたかが軍人一人だ。\x01",
            "それも現実的ではなかろう。\x02\x03",

            "#07300Fいずれにしても、現時点では\x01",
            "あらゆる事態を想定して\x01",
            "備えておくしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "#5P#07108Fそうですね……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0154
    ChrTalk(
        0x8,
        (
            "#11P#07004F──皆さん。\x01",
            "教えてくださって感謝します。\x02\x03",

            "#07002Fおかげでこちらの方も\x01",
            "様々な事態に対応できそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#6P#00002Fい、いえ、とんでもない！\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        (
            "#6P#00102Fこちらの方こそわざわざ\x01",
            "重要な情報を教えて頂いて……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        "#6P#10109F本当に有難うございました！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0158
    ChrTalk(
        0xA,
        (
            "#07209Fハッハッハッ、お互い様さ。\x02\x03",

            "#07202Fしかしそういう事なら\x01",
            "お礼に夜のクロスベルの名所でも\x01",
            "案内してもらおうかな？\x02\x03",

            "ワジ君やランディ君なんかは\x01",
            "色々と詳しそうだしねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        "#6P#00305Fおっ、行っちまいますか？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x105,
        (
            "#6P#N#10309Fフフ、それなら取っておきの\x01",
            "スポットに案内できると思うけど。\x02",
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
            "#07212Fおお、そうと決まれば\x01",
            "晩餐会はキャンセルして──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    #C0162
    ChrTalk(
        0xB,
        (
            "#07306F──させるか、阿呆。\x02\x03",

            "#07301Fこれからアルカンシェルの\x01",
            "公演も観劇するのだろうが。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0163
    ChrTalk(
        0xA,
        (
            "#07201F#5Pむむ……それもあったか。\x02\x03",

            "#07206Fうーん、アルカンシェルは一度、\x01",
            "見ておきたかったんだよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#6P#00012Fはは……\x01",
            "きっと楽しめると思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#6P#00109Fええ、目を丸くされること\x01",
            "請け合いだと思います。\x02",
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
            "#11P#07009Fふふ、楽しみにしていますね。\x02\x03",

            "#07002F……また何かあったら\x01",
            "皆さんにもご連絡いたします。\x02\x03",

            "今度はジークに頼らず、\x01",
            "直接通信を差し上げますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        "#11P#08009Fピュイ。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#6P#00004Fはは、承知しました。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#6P#00302Fさすがにアレは\x01",
            "何かと思ったからなぁ。\x02",
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
