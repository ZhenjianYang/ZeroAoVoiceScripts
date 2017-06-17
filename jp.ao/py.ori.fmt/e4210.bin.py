from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4210.bin",                # FileName
        "e4210",                    # MapName
        "e4210",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4210",                  # 0
        "アイオーン３",           # 1
        "帝国軍戦車",             # 2
        "帝国軍戦車",             # 3
        "帝国軍戦車",             # 4
        "帝国軍戦車",             # 5
        "帝国軍戦車・壊れ",       # 6
        "SE制御",                 # 7
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(492, 0)                                        # 0

    ScpFunction((
        "Function_0_1EC",          # 00, 0
        "Function_1_1FC",          # 01, 1
        "Function_2_1FD",          # 02, 2
        "Function_3_1634",         # 03, 3
        "Function_4_16AF",         # 04, 4
        "Function_5_1738",         # 05, 5
        "Function_6_17C1",         # 06, 6
        "Function_7_183C",         # 07, 7
        "Function_8_189A",         # 08, 8
        "Function_9_1906",         # 09, 9
        "Function_10_1972",        # 0A, 10
        "Function_11_19A3",        # 0B, 11
        "Function_12_1ABA",        # 0C, 12
        "Function_13_1AEE",        # 0D, 13
        "Function_14_1B30",        # 0E, 14
        "Function_15_1B80",        # 0F, 15
        "Function_16_1B96",        # 10, 16
        "Function_17_1BF2",        # 11, 17
        "Function_18_1C51",        # 12, 18
        "Function_19_1CB0",        # 13, 19
        "Function_20_1D81",        # 14, 20
        "Function_21_1D9A",        # 15, 21
        "Function_22_203B",        # 16, 22
        "Function_23_20AF",        # 17, 23
        "Function_24_20BF",        # 18, 24
        "Function_25_2179",        # 19, 25
        "Function_26_21C7",        # 1A, 26
        "Function_27_21F6",        # 1B, 27
        "Function_28_220C",        # 1C, 28
        "Function_29_224C",        # 1D, 29
        "Function_30_2302",        # 1E, 30
        "Function_31_23BB",        # 1F, 31
        "Function_32_2474",        # 20, 32
        "Function_33_2475",        # 21, 33
        "Function_34_2491",        # 22, 34
        "Function_35_24EB",        # 23, 35
        "Function_36_2507",        # 24, 36
    ))


    def Function_0_1EC(): pass

    label("Function_0_1EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1FB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_1FB")

    Return()

    # Function_0_1EC end

    def Function_1_1FC(): pass

    label("Function_1_1FC")

    Return()

    # Function_1_1FC end

    def Function_2_1FD(): pass

    label("Function_2_1FD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F3(200000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetMapObjFrame(0xFF, "ato00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "r10_shadow02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01_add", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_315")
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1F, 0x4)

    label("loc_315")

    LoadEffect(0x0, "event/ev15060.eff")
    LoadEffect(0x1, "event/ev15062.eff")
    LoadEffect(0x2, "event/ev15061.eff")
    LoadEffect(0x3, "event/ev15063.eff")
    LoadEffect(0x4, "event/ev15058.eff")
    LoadEffect(0x5, "event/ev10018.eff")
    LoadEffect(0x6, "event/ev14003.eff")
    LoadEffect(0x7, "battle/cr313000.eff")
    SoundLoad(825)
    SoundLoad(923)
    SoundLoad(979)
    SoundLoad(950)
    SoundLoad(875)
    SoundLoad(868)
    SoundLoad(931)
    SoundLoad(981)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 0, 0, 0, 0)
    OP_74(0x0, 0x1E)
    OP_78(0x0, 0x8)
    OP_93(0x8, 0xB4, 0x0)
    SetChrFlags(0x8, 0x1)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 0, 0, 0, 0)
    OP_74(0x2, 0x1E)
    OP_78(0x2, 0x9)
    OP_93(0x9, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_74(0x3, 0x1E)
    OP_78(0x3, 0xA)
    OP_93(0xA, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 0, 0, 0, 0)
    OP_74(0x4, 0x1E)
    OP_78(0x4, 0xB)
    OP_93(0xB, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 0, 0, 0, 0)
    OP_74(0x5, 0x1E)
    OP_78(0x5, 0xC)
    OP_93(0xC, 0x0, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 0, 0, 0, 0)
    OP_74(0x1, 0x1E)
    OP_78(0x1, 0xD)
    OP_93(0xD, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x5, 0x1000)
    OP_11(0xAA, 0xC3, 0xFF, 0x0, 0x15E, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFlags(0x5, 0x1000)
    SetChrPos(0x9, -60000, 2050, 55250, 0)
    SetChrPos(0xA, -66500, 2050, 57000, 0)
    SetChrPos(0xB, -71000, 2050, 60000, 0)
    SetChrPos(0xC, -71000, 2050, 60000, 0)
    OP_93(0x9, 0x57, 0x0)
    OP_93(0xA, 0x6C, 0x0)
    OP_93(0xB, 0x7F, 0x0)
    OP_93(0xC, 0x7F, 0x0)
    OP_E7()
    FadeToBright(1000, 0)
    OP_68(-43850, 3900, 41060, 0)
    MoveCamera(194, 7, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(39430, 0)
    OP_6F(0x79)
    OP_68(-56110, 2900, 48180, 14500)
    MoveCamera(239, 8, 0, 14500)
    OP_6E(510, 14500)
    SetCameraDistance(39430, 14500)
    BeginChrThread(0xE, 1, 0, 34)
    BeginChrThread(0x9, 0, 0, 3)
    BeginChrThread(0xA, 0, 0, 4)
    BeginChrThread(0xB, 0, 0, 5)
    BeginChrThread(0xC, 0, 0, 6)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrPos(0x9, -28000, 50, 47500, 0)
    SetChrPos(0xA, -39000, 50, 54750, 0)
    SetChrPos(0xB, -53500, 2050, 55500, 0)
    OP_93(0x9, 0xA1, 0x0)
    OP_93(0xA, 0x6C, 0x0)
    OP_93(0xB, 0x5C, 0x0)
    OP_68(-40810, 1400, 32880, 0)
    MoveCamera(26, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(45230, 0)
    Fade(500)
    OP_68(-33220, 1400, 28330, 9000)
    MoveCamera(23, 15, 0, 9000)
    OP_6E(510, 9000)
    SetCameraDistance(24440, 9000)
    BeginChrThread(0x9, 0, 0, 7)
    BeginChrThread(0xA, 0, 0, 8)
    BeginChrThread(0xB, 0, 0, 9)
    BeginChrThread(0xC, 0, 0, 10)
    OP_0D()
    OP_6F(0x79)
    StopSound(825, 500, 60)
    StopSound(923, 500, 60)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x5, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x32, 0x0, 0x20)
    SetChrPos(0x8, -107000, 14000, -56500, 0)
    OP_93(0x8, 0x2D, 0x0)
    SetChrFlags(0x8, 0x8000)
    OP_D5(0x8, 0x88B8, 0xAFC8, 0x0, 0x0)
    OP_FF(0x0, 0x1F4, 0x1F4, 0x1F4)
    Sound(979, 2, 100, 0)
    OP_11(0xAA, 0xC3, 0xFF, 0x0, 0x1C2, 0x0)
    OP_68(-81100, 9300, -30250, 0)
    MoveCamera(189, 0, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(75000, 0)
    Fade(500)
    OP_68(-81100, 10100, -30250, 4000)
    MoveCamera(196, 0, 0, 4000)
    OP_6E(510, 0)
    SetCameraDistance(65000, 4000)
    BeginChrThread(0x8, 0, 0, 11)
    OP_0D()
    OP_6F(0x79)
    OP_FF(0x0, 0x3E8, 0x3E8, 0x3E8)
    OP_11(0xAA, 0xC3, 0xFF, 0x0, 0x15E, 0x0)
    OP_68(-71360, 16100, -20830, 0)
    MoveCamera(196, 1, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(42490, 0)
    Fade(500)
    OP_68(-71360, 2600, -20830, 3000)
    MoveCamera(196, 8, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(32490, 3000)
    OP_0D()
    OP_6F(0x79)
    OP_68(-71500, 4700, -21000, 0)
    MoveCamera(207, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(11500, 0)
    Fade(500)
    OP_68(-71230, 2500, -20530, 5000)
    MoveCamera(242, 1, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(26500, 5000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x5, 0x1000)
    SetChrPos(0x8, -72000, -2000, -21500, 0)
    OP_93(0x8, 0x2D, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x9, -41000, 50, 17000, 0)
    SetChrPos(0xA, -29500, 50, 28000, 0)
    SetChrPos(0xB, -28000, 50, 47500, 0)
    OP_93(0x9, 0xD5, 0x0)
    OP_93(0xA, 0xDF, 0x0)
    OP_93(0xB, 0xB0, 0x0)
    OP_68(-36000, 1700, 20500, 0)
    MoveCamera(216, 10, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(49090, 0)
    Fade(500)
    OP_68(-40680, 600, 15870, 6000)
    MoveCamera(208, 6, 0, 6000)
    OP_6E(610, 6000)
    SetCameraDistance(48620, 6000)
    Sound(825, 2, 60, 0)
    Sound(923, 2, 60, 0)
    BeginChrThread(0x9, 0, 0, 12)
    BeginChrThread(0xA, 0, 0, 13)
    BeginChrThread(0xB, 0, 0, 14)
    BeginChrThread(0xC, 0, 0, 15)
    Sleep(2000)
    BeginChrThread(0x9, 3, 0, 16)
    BeginChrThread(0xA, 3, 0, 17)
    OP_6F(0x79)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x9, -44280, 50, 11900, 0)
    SetChrPos(0xA, -33830, 50, 23750, 0)
    SetChrPos(0xB, -20780, 50, 35730, 0)
    OP_93(0x9, 0xDB, 0x0)
    OP_93(0xA, 0xDD, 0x0)
    OP_93(0xB, 0xDC, 0x0)
    OP_68(-40000, 600, 16000, 0)
    MoveCamera(83, 16, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(29000, 0)
    Fade(500)
    OP_68(-42000, 600, 14000, 4500)
    MoveCamera(82, 16, 0, 4500)
    OP_6E(610, 4500)
    SetCameraDistance(29000, 4500)

    def lambda_B42():
        OP_9B(0x1, 0xFE, 0x0, 0xDAC, 0x2EE, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B42)

    def lambda_B57():
        OP_9B(0x1, 0xFE, 0x0, 0xDAC, 0x2EE, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B57)

    def lambda_B6C():
        OP_9B(0x1, 0xFE, 0x0, 0xDAC, 0x2EE, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B6C)
    BeginChrThread(0x9, 3, 0, 16)
    BeginChrThread(0xA, 3, 0, 17)
    BeginChrThread(0xB, 3, 0, 18)
    OP_0D()
    OP_6F(0x79)
    StopSound(825, 500, 50)
    StopSound(923, 500, 50)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    SetChrFlags(0x8, 0x8000)
    OP_68(-71500, 2300, -21000, 0)
    MoveCamera(193, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(50000, 0)
    Fade(500)
    OP_70(0x0, 0x1AE)
    OP_0D()
    Sound(979, 2, 70, 0)
    BeginChrThread(0x8, 0, 0, 19)
    BeginChrThread(0x8, 3, 0, 21)
    Sleep(200)
    OP_68(-59250, 3200, -8580, 6000)
    MoveCamera(185, 13, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(39250, 6000)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x3)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x5, 0x1000)
    SetChrPos(0x8, -58000, 500, -7500, 0)
    OP_93(0x8, 0x2D, 0x0)
    SetChrPos(0x9, -46280, 50, 9180, 0)
    SetChrPos(0xA, -35920, 50, 20900, 0)
    SetChrPos(0xB, -25900, 50, 33610, 0)
    SetChrPos(0xC, -28000, 50, 47500, 0)
    OP_93(0x9, 0xD7, 0x0)
    OP_93(0xA, 0xDC, 0x0)
    OP_93(0xB, 0xDB, 0x0)
    OP_93(0xC, 0x89, 0x0)
    OP_68(-46000, 600, 8750, 0)
    MoveCamera(94, 18, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(26080, 0)
    Fade(500)
    Sound(825, 2, 60, 0)
    Sound(923, 2, 60, 0)
    BeginChrThread(0x8, 0, 0, 24)
    BeginChrThread(0x9, 0, 0, 22)
    BeginChrThread(0xA, 0, 0, 23)
    ClearMapObjFlags(0x1, 0x4)
    Sleep(150)
    OP_68(-50500, 600, -500, 1500)
    MoveCamera(162, 21, 0, 1500)
    OP_6E(610, 1500)
    SetCameraDistance(26080, 1500)
    OP_0D()
    Sleep(1100)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0x5DC, 0x1770)
    OP_6F(0x79)
    Sleep(1500)
    OP_68(-49500, 600, 500, 2250)
    Sleep(2000)
    WaitChrThread(0x8, 0)
    Fade(500)
    CancelBlur(0)
    OP_68(-50580, 2990, 2990, 0)
    MoveCamera(275, 17, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(25890, 0)
    SetMapObjFlags(0x1, 0x1000)
    OP_93(0x9, 0xF5, 0x0)
    SetChrPos(0x8, -49110, 0, -70, 18)
    OP_D5(0x8, 0xFFFFEC78, 0x4650, 0x0, 0x0)
    BeginChrThread(0x8, 0, 0, 26)
    OP_68(-48370, 2790, 4700, 3000)
    MoveCamera(238, 12, 0, 3000)
    OP_6E(610, 3000)
    SetCameraDistance(21300, 3000)
    OP_0D()
    StopSound(979, 500, 50)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    StopEffect(0x1, 0x2)
    OP_24(0x36B)
    WaitChrThread(0x8, 0)
    Sound(288, 0, 100, 0)
    Sound(833, 0, 50, 0)
    OP_74(0x0, 0x1E)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -47140, 1690, 5810, 208, 32, 0, 150, 1250, 150, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x38E, 0x3A2, 0x0, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(250)
    StopSound(825, 300, 50)
    StopSound(923, 300, 50)
    EndChrThread(0x9, 0x0)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    OP_FD(0xD, 0x9)
    Sound(200, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -47200, 2190, 5680, 210, 32, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x320, 0x320, 0xBB8, 0x1F4)
    OP_79(0x0)
    Sleep(400)
    CancelBlur(500)
    OP_87(0x4, 0x0, 0x1, "kizu00", 0x7, 0x0, 0x0, 0x7D0, 0x0, 0x0, 0x0, 0x320, 0x320, 0x320, 0x0)
    Sound(1019, 0, 100, 0)
    OP_71(0x0, 0x3A2, 0x3CA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x8, 0, 0, 27)
    Sleep(400)
    Sound(200, 0, 100, 0)
    BeginChrThread(0xD, 0, 0, 28)
    Sound(868, 2, 60, 0)
    Sleep(400)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x320, 0x320, 0xBB8, 0x3E8)
    Sleep(1)
    CancelBlur(3000)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -46220, 3290, 6380, 250, 100, 0, 350, 150, 350, 0xFF, 0, 0, 0, 0)
    OP_79(0x0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0xD, 0)
    Sound(833, 0, 100, 0)
    Sound(200, 0, 100, 0)
    OP_6F(0x79)
    Sleep(300)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xD, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_70(0x3, 0x78)
    OP_70(0x4, 0x78)
    OP_70(0x5, 0x78)
    SetChrPos(0x8, -48000, 0, 2000, 0)
    OP_93(0x8, 0x23, 0x0)
    SetChrPos(0xA, -35190, 50, 22630, 0)
    SetChrPos(0xB, -26280, 50, 29570, 0)
    SetChrPos(0xC, -23970, 50, 40130, 0)
    OP_93(0x8, 0x23, 0x0)
    OP_93(0xA, 0xD7, 0x0)
    OP_93(0xB, 0xDB, 0x0)
    OP_93(0xC, 0xD6, 0x0)
    SetChrPos(0xD, -30660, 1150, 6950, 1250)
    OP_D5(0xD, 0x0, 0x46500, 0x88B8, 0x0)
    OP_68(-36500, 700, 11000, 0)
    MoveCamera(94, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(41390, 0)
    Fade(500)
    OP_68(-36260, 700, 14300, 4500)
    MoveCamera(58, 18, 0, 4500)
    OP_6E(510, 4500)
    SetCameraDistance(47800, 4500)
    OP_0D()
    Sound(950, 2, 80, 0)
    BeginChrThread(0xA, 3, 0, 29)
    BeginChrThread(0xB, 3, 0, 30)
    BeginChrThread(0xC, 3, 0, 31)
    BeginChrThread(0x8, 3, 0, 32)
    OP_6F(0x79)
    Sleep(500)
    StopSound(868, 300, 50)
    StopEffect(0x0, 0x2)
    Sleep(1000)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0x8, 0x3)
    StopSound(950, 500, 100)
    OP_68(-47250, 5600, 3000, 0)
    MoveCamera(215, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(32509, 0)
    Fade(500)
    OP_68(-47240, 4300, 3030, 5500)
    MoveCamera(200, -3, 0, 5500)
    OP_6E(510, 5500)
    SetCameraDistance(27730, 5500)
    OP_0D()
    Sound(981, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x5A, 0x82, 0x0, 0x0)
    Sleep(3000)
    BlurSwitch(0x0, 0x99FFFFFF, 0x0, 0x1, 0xA)
    OP_82(0xC8, 0xC8, 0x1388, 0x2328)
    BeginChrThread(0xE, 1, 0, 35)
    OP_87(0x3, 0x2, 0x0, "Null_b_cannon_r(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_87(0x3, 0x3, 0x0, "Null_b_cannon_l(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x546, 0x546, 0x546, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    OP_68(-28650, 5000, 28000, 0)
    MoveCamera(200, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(59470, 0)
    Fade(500)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x2328)
    OP_0D()
    Sleep(200)
    Sound(868, 2, 100, 0)
    BeginChrThread(0xE, 1, 0, 36)
    OP_87(0x6, 0x4, 0x3, "body", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Sleep(250)
    OP_87(0x6, 0x5, 0x4, "body", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Sleep(250)
    OP_87(0x6, 0x6, 0x5, "body", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Sleep(1500)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    Sleep(200)
    OP_71(0x6, 0x0, 0x14, 0x0, 0x0)
    Sleep(50)
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    Sleep(200)
    OP_71(0x7, 0x0, 0x14, 0x0, 0x0)
    Sleep(50)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    Sleep(200)
    OP_71(0x8, 0x0, 0x14, 0x0, 0x0)
    Sleep(2500)
    OP_79(0x0)
    OP_6F(0x79)
    SetMapObjFrame(0xFF, "ato00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "r10_shadow02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mae00", 0x0, 0x1)
    OP_68(-37540, 2400, 15510, 0)
    MoveCamera(59, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(34960, 0)
    Fade(500)
    CancelBlur(2500)
    OP_82(0xC8, 0xC8, 0xBB8, 0x7D0)
    OP_68(-37540, 2400, 15510, 5000)
    MoveCamera(56, 25, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(56810, 5000)
    OP_0D()
    Sleep(400)
    StopEffect(0x4, 0x2)
    Sleep(200)
    Sleep(50)
    StopEffect(0x5, 0x2)
    Sleep(200)
    Sleep(50)
    StopEffect(0x6, 0x2)
    EndChrThread(0xE, 0x1)
    Sleep(200)
    OP_79(0x0)
    Sleep(200)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopSound(931, 1000, 70)
    StopSound(825, 1000, 70)
    OP_6F(0x79)
    SetChrPos(0x8, -48000, 0, 2000, 0)
    OP_93(0x8, 0x23, 0x0)
    OP_68(-44980, 3900, 6130, 0)
    MoveCamera(205, 2, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(36500, 0)
    Fade(500)
    SetCameraDistance(31000, 3500)
    OP_0D()
    OP_25(0x364, 0x46)
    BeginChrThread(0x8, 0, 0, 33)
    OP_6F(0x79)
    StopSound(868, 4000, 60)
    OP_68(-45000, 6800, 6000, 0)
    MoveCamera(200, 7, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(65000, 0)
    Fade(500)
    OP_68(-45000, 6800, 6000, 4500)
    MoveCamera(200, 7, 0, 4500)
    OP_6E(510, 4500)
    SetCameraDistance(80000, 4500)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_E8()
    OP_24(0x339)
    OP_24(0x39B)
    OP_24(0x3D3)
    OP_24(0x3B6)
    OP_24(0x36B)
    OP_24(0x364)
    OP_24(0x3A3)
    SetScenarioFlags(0x22, 1)
    NewScene("t2100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1FD end

    def Function_3_1634(): pass

    label("Function_3_1634")

    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, -60000, 2050, 55250, 0)
    Sleep(2000)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x57, 0x0)
    OP_9F(0x1, -53500, 2050, 55500)
    OP_9F(0x1, -45000, 50, 55250)
    OP_9F(0x1, -39000, 50, 54750)
    OP_9F(0x1, -32500, 50, 52250)
    OP_9F(0x1, -28000, 50, 47500)
    OP_9F(0x2, 0xFE, 4000, 0x7)
    Return()

    # Function_3_1634 end

    def Function_4_16AF(): pass

    label("Function_4_16AF")

    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, -66500, 2050, 57000, 0)
    Sleep(4500)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x6C, 0x0)
    OP_9F(0x1, -60000, 2050, 55250)
    OP_9F(0x1, -53500, 2050, 55500)
    OP_9F(0x1, -45000, 50, 55250)
    OP_9F(0x1, -39000, 50, 54750)
    OP_9F(0x1, -32500, 50, 52250)
    OP_9F(0x1, -28000, 50, 47500)
    OP_9F(0x2, 0xFE, 4000, 0x7)
    Return()

    # Function_4_16AF end

    def Function_5_1738(): pass

    label("Function_5_1738")

    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, -71000, 2050, 60000, 0)
    Sleep(7000)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x7F, 0x0)
    OP_9F(0x1, -66500, 2050, 57000)
    OP_9F(0x1, -60000, 2050, 55250)
    OP_9F(0x1, -53500, 2050, 55500)
    OP_9F(0x1, -45000, 50, 55250)
    OP_9F(0x1, -39000, 50, 54750)
    OP_9F(0x1, -32500, 50, 52250)
    OP_9F(0x2, 0xFE, 4000, 0x7)
    Return()

    # Function_5_1738 end

    def Function_6_17C1(): pass

    label("Function_6_17C1")

    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, -71000, 2050, 60000, 0)
    Sleep(11500)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x7F, 0x0)
    OP_9F(0x1, -66500, 2050, 57000)
    OP_9F(0x1, -60000, 2050, 55250)
    OP_9F(0x1, -53500, 2050, 55500)
    OP_9F(0x1, -45000, 50, 55250)
    OP_9F(0x1, -39000, 50, 54750)
    OP_9F(0x2, 0xFE, 4000, 0x7)
    Return()

    # Function_6_17C1 end

    def Function_7_183C(): pass

    label("Function_7_183C")

    SetChrPos(0xFE, -28000, 50, 47500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0xA1, 0x0)
    OP_9F(0x1, -24000, 50, 35000)
    OP_9F(0x1, -31000, 50, 26000)
    OP_9F(0x1, -36500, 50, 22000)
    OP_9F(0x1, -41000, 50, 17000)
    OP_9F(0x2, 0xFE, 3000, 0x7)
    Return()

    # Function_7_183C end

    def Function_8_189A(): pass

    label("Function_8_189A")

    SetChrPos(0xFE, -39000, 50, 54750, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x6C, 0x0)
    OP_9F(0x1, -32500, 50, 52250)
    OP_9F(0x1, -28000, 50, 47500)
    OP_9F(0x1, -24000, 50, 40000)
    OP_9F(0x1, -24000, 50, 35000)
    OP_9F(0x1, -31000, 50, 26000)
    OP_9F(0x2, 0xFE, 3000, 0x7)
    Return()

    # Function_8_189A end

    def Function_9_1906(): pass

    label("Function_9_1906")

    SetChrPos(0xFE, -53500, 2050, 55500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5C, 0x0)
    OP_9F(0x1, -45000, 50, 55250)
    OP_9F(0x1, -39000, 50, 54750)
    OP_9F(0x1, -32500, 50, 52250)
    OP_9F(0x1, -28000, 50, 47500)
    OP_9F(0x1, -24000, 50, 40000)
    OP_9F(0x2, 0xFE, 3000, 0x7)
    Return()

    # Function_9_1906 end

    def Function_10_1972(): pass

    label("Function_10_1972")

    Sleep(7000)
    SetChrPos(0xFE, -45000, 50, 55500, 0)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9E(0xFE, 0xFFFF5038, 0x9088, 0xEA60, 0xBB8, 0x1)
    Return()

    # Function_10_1972 end

    def Function_11_19A3(): pass

    label("Function_11_19A3")

    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x32, 0x0, 0x20)
    SetChrPos(0xFE, -107000, 14000, -56500, 0)
    OP_93(0xFE, 0x2D, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x6E7C, 0x2710, 0x1)

    def lambda_19DF():
        OP_D5(0xFE, 0x0, 0xAFC8, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_19DF)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x2D, 0x0)
    OP_9F(0x1, -87000, 14000, -36500)
    OP_9F(0x1, -82000, 10000, -31500)
    OP_9F(0x1, -74000, 8000, -23500)
    OP_9F(0x1, -72000, -2000, -21500)
    OP_9F(0x2, 0xFE, 8000, 0x2)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    StopSound(979, 500, 100)
    OP_71(0x0, 0x33, 0x5A, 0x0, 0x0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(1500)
    OP_82(0x12C, 0x12C, 0x1770, 0x3E8)
    Return()

    # Function_11_19A3 end

    def Function_12_1ABA(): pass

    label("Function_12_1ABA")

    SetChrPos(0xFE, -41000, 50, 17000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0xD5, 0x0)
    OP_9F(0x1, -45500, 50, 10000)
    OP_9F(0x2, 0xFE, 1000, 0x7)
    Return()

    # Function_12_1ABA end

    def Function_13_1AEE(): pass

    label("Function_13_1AEE")

    SetChrPos(0xFE, -29500, 50, 28000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0xDF, 0x0)
    OP_9F(0x1, -35500, 50, 22000)
    OP_9F(0x1, -38000, 50, 19000)
    OP_9F(0x2, 0xFE, 1000, 0x7)
    Return()

    # Function_13_1AEE end

    def Function_14_1B30(): pass

    label("Function_14_1B30")

    SetChrPos(0xFE, -28000, 50, 47500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0xB0, 0x0)
    OP_9F(0x1, -23000, 50, 39000)
    OP_9F(0x1, -23500, 50, 33000)
    OP_9F(0x1, -29000, 50, 25000)
    OP_9F(0x2, 0xFE, 2000, 0x7)
    Return()

    # Function_14_1B30 end

    def Function_15_1B80(): pass

    label("Function_15_1B80")

    OP_9E(0xFE, 0xFFFF5038, 0x9088, 0x15F90, 0x7D0, 0x1)
    Return()

    # Function_15_1B80 end

    def Function_16_1B96(): pass

    label("Function_16_1B96")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BF1")
    OP_82(0xA0, 0xA0, 0xBB8, 0x1F4)
    Sound(925, 0, 100, 0)
    OP_87(0x0, 0xFF, 0x2, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x4E2, 0x4E2, 0x4E2, 0x0)
    Sleep(2000)
    Jump("Function_16_1B96")

    label("loc_1BF1")

    Return()

    # Function_16_1B96 end

    def Function_17_1BF2(): pass

    label("Function_17_1BF2")

    Sleep(300)

    label("loc_1BF5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C50")
    OP_82(0x82, 0x82, 0xA8C, 0x1F4)
    Sound(925, 0, 100, 0)
    OP_87(0x0, 0xFF, 0x3, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x4E2, 0x4E2, 0x4E2, 0x0)
    Sleep(2000)
    Jump("loc_1BF5")

    label("loc_1C50")

    Return()

    # Function_17_1BF2 end

    def Function_18_1C51(): pass

    label("Function_18_1C51")

    Sleep(600)

    label("loc_1C54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CAF")
    OP_82(0x64, 0x64, 0x9C4, 0x1F4)
    Sound(925, 0, 100, 0)
    OP_87(0x0, 0xFF, 0x4, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x4E2, 0x4E2, 0x4E2, 0x0)
    Sleep(2000)
    Jump("loc_1C54")

    label("loc_1CAF")

    Return()

    # Function_18_1C51 end

    def Function_19_1CB0(): pass

    label("Function_19_1CB0")

    SetChrPos(0xFE, -72000, -2000, -21500, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x1AE, 0x1D6, 0x1, 0x20)
    BeginChrThread(0xFE, 1, 0, 20)

    label("loc_1CD7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D80")
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x1AF, 0x1B6, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x1B7, 0x1BB, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x1BC, 0x1CA, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x1CB, 0x1CF, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x1D0, 0x1D6, 0x1, 0x0)
    OP_79(0x0)
    Jump("loc_1CD7")

    label("loc_1D80")

    Return()

    # Function_19_1CB0 end

    def Function_20_1D81(): pass

    label("Function_20_1D81")

    OP_96(0xFE, 0xFFFF1D70, 0x1F4, 0xFFFFE2B4, 0xFA0, 0x1)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_20_1D81 end

    def Function_21_1D9A(): pass

    label("Function_21_1D9A")

    Sleep(300)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    Sound(196, 0, 50, 0)
    Sound(202, 0, 100, 0)
    Sound(950, 2, 80, 0)
    OP_87(0x2, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x1388, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1)
    CancelBlur(500)
    Sleep(1100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    Sound(196, 0, 50, 0)
    Sound(202, 0, 100, 0)
    StopSound(950, 1000, 80)
    OP_87(0x2, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x1388, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1)
    CancelBlur(500)
    Sleep(900)
    Sleep(700)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    Sound(196, 0, 50, 0)
    Sound(202, 0, 100, 0)
    Sound(950, 2, 80, 0)
    OP_87(0x2, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x1388, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1)
    CancelBlur(500)
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    Sound(196, 0, 50, 0)
    Sound(202, 0, 100, 0)
    OP_87(0x2, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x1388, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1)
    CancelBlur(500)
    Sleep(800)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    Sound(196, 0, 50, 0)
    Sound(202, 0, 100, 0)
    OP_87(0x2, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x1388, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1)
    CancelBlur(500)
    Sleep(700)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    Sound(196, 0, 50, 0)
    Sound(202, 0, 100, 0)
    StopSound(950, 1000, 80)
    OP_87(0x2, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x1388, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1)
    CancelBlur(500)
    Sleep(700)
    Return()

    # Function_21_1D9A end

    def Function_22_203B(): pass

    label("Function_22_203B")

    OP_71(0x2, 0xB5, 0xF0, 0x0, 0x20)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFA, 0xBB8, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1D4C, 0x1388, 0x0)
    Sound(875, 2, 80, 0)
    Sound(288, 0, 100, 0)
    OP_87(0x1, 0x1, 0x2, "cover", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Return()

    # Function_22_203B end

    def Function_23_20AF(): pass

    label("Function_23_20AF")

    OP_9B(0x1, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    Return()

    # Function_23_20AF end

    def Function_24_20BF(): pass

    label("Function_24_20BF")

    SetChrPos(0xFE, -58000, 500, -7500, 0)
    TurnDirection(0xFE, 0x9, 300)
    BeginChrThread(0xFE, 1, 0, 25)

    label("loc_20DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2178")
    OP_4C(0x9, 0x1)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x1AF, 0x1B6, 0x1, 0x0)
    OP_79(0x0)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_4B(0xFE, 0x1)
    OP_4B(0x9, 0x1)
    OP_71(0x0, 0x1B7, 0x1BB, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0x9, 0x1)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x1BC, 0x1CA, 0x1, 0x0)
    OP_79(0x0)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_4B(0xFE, 0x1)
    OP_4B(0x9, 0x1)
    OP_71(0x0, 0x1CB, 0x1CF, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0x9, 0x1)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x1D0, 0x1D6, 0x1, 0x0)
    OP_79(0x0)
    Jump("loc_20DD")

    label("loc_2178")

    Return()

    # Function_24_20BF end

    def Function_25_2179(): pass

    label("Function_25_2179")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -52500, 0, -2000)
    OP_9F(0x2, 0xFE, 5000, 0x0)

    def lambda_2199():
        OP_98(0xFE, 0x1518, 0x0, 0x12C0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2199)
    OP_98(0xFE, 0x1518, 0x0, 0x12C0, 0x708, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_25_2179 end

    def Function_26_21C7(): pass

    label("Function_26_21C7")

    OP_74(0x0, 0x1E)
    ClearMapObjFlags(0x0, 0x0)
    OP_71(0x0, 0x186, 0x19A, 0x0, 0x0)
    OP_79(0x0)
    Sound(1019, 0, 100, 0)
    OP_71(0x0, 0x366, 0x38E, 0x0, 0x0)
    OP_79(0x0)
    Return()

    # Function_26_21C7 end

    def Function_27_21F6(): pass

    label("Function_27_21F6")

    Sound(905, 0, 100, 0)
    OP_71(0x0, 0x1D6, 0x1FE, 0x0, 0x0)
    OP_79(0x0)
    Return()

    # Function_27_21F6 end

    def Function_28_220C(): pass

    label("Function_28_220C")

    Sleep(400)

    def lambda_2214():
        OP_D5(0xFE, 0xFFFF63C0, 0x46500, 0x20F58, 0x384)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2214)
    Sound(880, 0, 100, 0)
    Sound(876, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF883C, 0x47E, 0x1B26, 0xCB2, 0x9C4)
    Return()

    # Function_28_220C end

    def Function_29_224C(): pass

    label("Function_29_224C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2301")
    Sound(925, 0, 100, 0)
    OP_87(0x0, 0xFF, 0x3, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(200)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_82(0xA0, 0xA0, 0xBB8, 0x1F4)
    Sound(196, 0, 50, 0)
    Sound(202, 0, 100, 0)
    OP_87(0x2, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x1388, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1)
    CancelBlur(500)
    Sleep(3800)
    Jump("Function_29_224C")

    label("loc_2301")

    Return()

    # Function_29_224C end

    def Function_30_2302(): pass

    label("Function_30_2302")

    Sleep(1000)

    label("loc_2305")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23BA")
    Sound(925, 0, 100, 0)
    OP_87(0x0, 0xFF, 0x4, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(200)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_82(0x82, 0x82, 0xA8C, 0x1F4)
    Sound(196, 0, 50, 0)
    Sound(202, 0, 100, 0)
    OP_87(0x2, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x1388, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1)
    CancelBlur(500)
    Sleep(3800)
    Jump("loc_2305")

    label("loc_23BA")

    Return()

    # Function_30_2302 end

    def Function_31_23BB(): pass

    label("Function_31_23BB")

    Sleep(2000)

    label("loc_23BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2473")
    Sound(925, 0, 100, 0)
    OP_87(0x0, 0xFF, 0x5, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(200)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_82(0x64, 0x64, 0x9C4, 0x1F4)
    Sound(196, 0, 50, 0)
    Sound(202, 0, 100, 0)
    OP_87(0x2, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x1388, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1)
    CancelBlur(500)
    Sleep(3800)
    Jump("loc_23BE")

    label("loc_2473")

    Return()

    # Function_31_23BB end

    def Function_32_2474(): pass

    label("Function_32_2474")

    Return()

    # Function_32_2474 end

    def Function_33_2475(): pass

    label("Function_33_2475")

    Sleep(1000)
    Sound(981, 0, 100, 0)
    OP_71(0x0, 0xA1, 0xBE, 0x0, 0x0)
    OP_79(0x0)
    Sleep(3000)
    Return()

    # Function_33_2475 end

    def Function_34_2491(): pass

    label("Function_34_2491")

    Sound(825, 2, 20, 0)
    Sound(923, 2, 20, 0)
    Sleep(400)
    OP_25(0x339, 0x19)
    OP_25(0x39B, 0x19)
    Sleep(400)
    OP_25(0x339, 0x1E)
    OP_25(0x39B, 0x1E)
    Sleep(400)
    OP_25(0x339, 0x23)
    OP_25(0x39B, 0x23)
    Sleep(400)
    OP_25(0x339, 0x28)
    OP_25(0x39B, 0x28)
    Sleep(400)
    OP_25(0x339, 0x2D)
    OP_25(0x39B, 0x2D)
    Sleep(400)
    OP_25(0x339, 0x32)
    OP_25(0x39B, 0x32)
    Sleep(400)
    OP_25(0x339, 0x37)
    OP_25(0x39B, 0x37)
    Return()

    # Function_34_2491 end

    def Function_35_24EB(): pass

    label("Function_35_24EB")

    Sound(983, 0, 100, 0)
    Sleep(2000)
    Sound(984, 0, 100, 0)
    Sound(931, 2, 80, 0)
    Sound(825, 2, 80, 0)
    Return()

    # Function_35_24EB end

    def Function_36_2507(): pass

    label("Function_36_2507")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2532")
    Sound(200, 0, 50, 0)
    Sleep(500)
    Sound(196, 0, 50, 0)
    Sleep(500)
    Sound(556, 0, 60, 0)
    Sleep(500)
    Jump("Function_36_2507")

    label("loc_2532")

    Return()

    # Function_36_2507 end

    SaveToFile()

Try(main)
