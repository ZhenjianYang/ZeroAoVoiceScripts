from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4310.bin",                # FileName
        "e4310",                    # MapName
        "e4310",                    # Location
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
        "e4310",                  # 0
        "梅尔卡瓦五号机",         # 1
        "梅尔卡瓦九号机",         # 2
        "神机永世",               # 3
        "梅尔卡瓦光学迷彩",       # 4
        "SE控制",                 # 5
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(380, 0)                                        # 0

    ScpFunction((
        "Function_0_17C",          # 00, 0
        "Function_1_1B4",          # 01, 1
        "Function_2_1C7",          # 02, 2
        "Function_3_1626",         # 03, 3
        "Function_4_17D4",         # 04, 4
        "Function_5_197C",         # 05, 5
        "Function_6_1AB8",         # 06, 6
        "Function_7_1BF4",         # 07, 7
        "Function_8_1C56",         # 08, 8
        "Function_9_1CB8",         # 09, 9
        "Function_10_1D1A",        # 0A, 10
        "Function_11_1D59",        # 0B, 11
        "Function_12_1DC2",        # 0C, 12
        "Function_13_2090",        # 0D, 13
        "Function_14_20EB",        # 0E, 14
        "Function_15_27CE",        # 0F, 15
        "Function_16_280B",        # 10, 16
        "Function_17_284F",        # 11, 17
        "Function_18_28B0",        # 12, 18
        "Function_19_28F9",        # 13, 19
        "Function_20_2909",        # 14, 20
        "Function_21_2976",        # 15, 21
        "Function_22_2AD6",        # 16, 22
    ))


    def Function_0_17C(): pass

    label("Function_0_17C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_190")
    ClearScenarioFlags(0x22, 2)
    Event(0, 2)
    Jump("loc_1B3")

    label("loc_190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_1A4")
    ClearScenarioFlags(0x23, 2)
    Event(0, 12)
    Jump("loc_1B3")

    label("loc_1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_1B3")
    ClearScenarioFlags(0x23, 3)
    Event(0, 14)

    label("loc_1B3")

    Return()

    # Function_0_17C end

    def Function_1_1B4(): pass

    label("Function_1_1B4")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x1388)
    OP_F3(100000)
    Return()

    # Function_1_1B4 end

    def Function_2_1C7(): pass

    label("Function_2_1C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis414.itp")
    CreatePortrait(1, 16, 20, 528, 84, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis511.itp")
    LoadEffect(0x0, "event/ev17086.eff")
    LoadEffect(0x1, "event/ev17021.eff")
    LoadEffect(0x2, "event/ev17022.eff")
    LoadEffect(0x3, "event/ev17019.eff")
    LoadEffect(0x4, "event/ev17020.eff")
    LoadEffect(0x5, "event/ev17030.eff")
    LoadEffect(0x6, "event/ev10017.eff")
    LoadEffect(0x7, "event/ev17003.eff")
    LoadEffect(0x8, "event/eva03_01.eff")
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(496)
    SoundLoad(950)
    SoundLoad(1014)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x1, 0x9)
    OP_49()
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x1, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x1, 0x3CF, 0x3CF, 0x3CF)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x3, 0xB)
    OP_49()
    SetMapObjFlags(0x3, 0x1000)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x2, 0xA)
    OP_49()
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    OP_71(0x2, 0x6E, 0x96, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_F3(100000)
    SetChrPos(0x8, 7500, 0, -110000, 0)
    SetChrPos(0x9, -7500, 0, -100000, 0)
    SetChrPos(0xA, 5000000, 0, 0, 0)
    OP_68(0, 2500, -50000, 0)
    MoveCamera(200, 10, -5, 0)
    OP_6E(850, 0)
    SetCameraDistance(20000, 0)
    OP_68(0, 2500, 50000, 8000)
    MoveCamera(340, 5, 5, 8000)
    SetCameraDistance(200000, 8000)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)

    def lambda_423():
        OP_9B(0x0, 0xFE, 0x0, 0x493E0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_423)

    def lambda_438():
        OP_9B(0x0, 0xFE, 0x0, 0x493E0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_438)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    Sound(497, 2, 70, 0)
    Sound(132, 2, 100, 0)
    OP_E7()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Fade(500)
    SetChrPos(0x8, 7500, 20000, -10000, 0)
    SetChrPos(0x9, -7500, 20000, 10000, 0)
    SetChrPos(0xB, -7500, 20000, 10000, 0)
    SetChrPos(0xA, 5000000, 0, 0, 0)
    OP_68(-7500, 22500, 13500, 0)
    MoveCamera(135, 40, -10, 0)
    SetCameraDistance(30000, 0)
    OP_68(-7500, 22500, 10500, 5750)
    MoveCamera(115, 30, -10, 5750)
    SetCameraDistance(40000, 5750)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    ClearMapObjFlags(0x3, 0x4)
    OP_71(0x3, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 1000, 40)
    SetMapObjFlags(0x1, 0x4)
    OP_79(0x3)
    OP_71(0x3, 0x65, 0xA0, 0x0, 0x20)
    OP_6F(0x79)
    Fade(500)
    OP_68(7500, 21500, -10000, 0)
    MoveCamera(300, 15, -10, 0)
    OP_6E(850, 0)
    SetCameraDistance(40000, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 500, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xC, 1, 0, 10)

    def lambda_89D():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_89D)
    OP_0D()
    OP_68(7500, 21500, 5000, 3000)
    MoveCamera(325, 15, -10, 3000)
    EndChrThread(0x8, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    CancelBlur(500)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1500, 1500, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1500, 1500, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_963():
        OP_9B(0x0, 0xFE, 0x0, 0x186A0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_963)
    Sleep(500)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, -2995000, -251000, 2000, 270)
    SetChrPos(0xB, -2990000, -251000, -2000, 270)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_FF(0x0, 0xFA, 0xFA, 0xFA)
    OP_FF(0x3, 0xFA, 0xFA, 0xFA)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -1050, 450, -2550, 0, 0, 0, 250, 250, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 1050, 450, -2550, 0, 0, 0, 250, 250, 250, 0xFF, 0, 0, 0, 0)
    OP_68(-5800000, -500000, 0, 0)
    MoveCamera(270, 5, 0, 0)
    OP_6E(1200, 0)
    SetCameraDistance(2800000, 0)
    SetCameraDistance(2805000, 3000)

    def lambda_A9B():
        OP_96(0xFE, 0xFFA77FC0, 0xFFF85EE0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A9B)

    def lambda_AB5():
        OP_96(0xFE, 0xFFA77FC0, 0xFFF85EE0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AB5)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    Sound(499, 0, 70, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1000)
    CancelBlur(1000)
    StopSound(496, 3000, 40)
    StopSound(497, 3000, 60)
    Sleep(2000)
    OP_6F(0x79)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, -5800000, -350000, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 20, 0)
    Sleep(500)
    Fade(500)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    OP_68(0, 4700, 1500, 0)
    MoveCamera(215, 10, 10, 0)
    OP_6E(850, 0)
    SetCameraDistance(15000, 0)
    Sound(999, 0, 70, 0)
    Sound(980, 2, 70, 0)
    OP_68(0, 4500, 0, 8000)
    MoveCamera(215, -10, 10, 8000)
    OP_6E(850, 8000)
    SetCameraDistance(10500, 1000)
    OP_82(0x32, 0x32, 0xBB8, 0x2710)
    EndChrThread(0x8, 0x1)
    EndChrThread(0xB, 0x1)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    PlayEffect(0x8, 0x2, 0xA, 0x5, 0, 4000, 30000, 180, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(5000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    Sound(655, 0, 50, 0)
    OP_87(0x5, 0xFF, 0x2, "ch88650head:Layer1(11)", 0x7, 0xFFFFFFCE, 0x32, 0xC8, 0x0, 0x0, 0x0, 0x2EE, 0x2EE, 0x2EE, 0x0)
    Sleep(1000)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x2EE, 0x2EE, 0x2EE, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x2EE, 0x2EE, 0x2EE, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x2EE, 0x2EE, 0x2EE, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x2EE, 0x2EE, 0x2EE, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x2EE, 0x2EE, 0x2EE, 0x0)
    OP_87(0x2, 0xFF, 0x2, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x2EE, 0x2EE, 0x2EE, 0x0)
    Sound(998, 0, 70, 0)
    Sound(499, 0, 100, 0)

    def lambda_E23():
        OP_9B(0x1, 0xFE, 0x0, 0x186A0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E23)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sleep(500)
    Fade(500)
    StopEffect(0x2, 0x0)
    EndChrThread(0xA, 0x1)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    OP_68(0, 4700, 0, 0)
    MoveCamera(180, -10, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(11500, 3000)
    Sound(994, 0, 50, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)
    PlayEffect(0x6, 0x2, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(1000)
    BeginChrThread(0xA, 0, 0, 3)
    Sleep(300)
    Sound(1036, 0, 100, 0)
    Sleep(700)
    EndChrThread(0xA, 0x0)
    OP_6F(0x79)
    StopSound(980, 1000, 60)
    Sound(497, 2, 70, 0)
    StopEffect(0x2, 0x0)
    CancelBlur(0)
    Fade(500)
    OP_FF(0x0, 0x3E8, 0x3E8, 0x3E8)
    OP_FF(0x3, 0x3E8, 0x3E8, 0x3E8)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0x3, 0x4)
    SetChrPos(0xA, 5000000, 5000000, 5000000, 0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x8, 0, 0, 0, 0)
    OP_D5(0x8, 0x0, 0x0, 0x0, 0x0)
    OP_68(0, 2500, 1000, 0)
    MoveCamera(130, 25, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(50000, 0)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    OP_0D()
    OP_68(20000, 50000, 2000, 1500)
    MoveCamera(130, -15, -5, 1500)
    SetCameraDistance(150000, 800)
    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sound(499, 0, 100, 0)

    def lambda_1028():
        OP_96(0xFE, 0x4E20, 0x186A0, 0x0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1028)

    def lambda_1042():
        OP_D5(0xFE, 0x0, 0x0, 0x7530, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1042)
    BeginChrThread(0x8, 0, 0, 4)
    Sleep(300)
    Sound(1036, 0, 70, 0)
    Sleep(700)
    EndChrThread(0x8, 0x0)
    WaitChrThread(0x8, 2)
    Fade(500)
    OP_68(20000, 35000, 2000, 0)
    MoveCamera(135, -10, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(38000, 0)
    OP_68(20000, 32500, 2000, 1000)
    SetCameraDistance(35000, 3000)
    MoveCamera(135, -15, 0, 1000)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    SetChrPos(0x8, 20000, 30000, 0, 0)
    OP_D5(0x8, 0x0, 0x0, 0x1388, 0x0)
    OP_D5(0x8, 0x0, 0x0, 0x0, 0x3E8)
    OP_0D()
    Sound(905, 0, 70, 0)
    OP_71(0x0, 0x137, 0x154, 0x0, 0x8)
    OP_79(0x0)
    OP_82(0x64, 0x64, 0xBB8, 0x9C4)
    Sound(1015, 0, 100, 0)
    OP_87(0x4, 0x3, 0x0, "can00_l", 0x7, 0xFFFFF510, 0xC8, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x4, 0x4, 0x0, "can00_r", 0x7, 0xFFFFF510, 0xC8, 0x0, 0x0, 0x0, 0xB4, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)
    Sound(664, 0, 100, 0)
    Sound(321, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    OP_68(20000, 32500, 15000, 500)
    SetCameraDistance(50000, 500)
    Sleep(500)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x1F4)
    Sleep(500)
    CancelBlur(0)
    StopSound(497, 1000, 60)
    Sound(980, 2, 60, 0)
    Fade(500)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    OP_68(0, 4500, 1000, 0)
    MoveCamera(190, 20, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(13500, 0)
    MoveCamera(215, 10, -5, 3500)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    PlayEffect(0x8, 0x2, 0xA, 0x5, 0, 4000, 10000, 180, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_68(10000, 4500, 500, 1000)

    def lambda_12C3():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12C3)
    BeginChrThread(0xA, 3, 0, 5)
    Sound(664, 0, 100, 0)
    Sound(321, 0, 100, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    OP_D5(0xA, 0x0, 0x0, 0xFFFFEC78, 0x12C)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x2BC)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)
    OP_68(0, 4500, 0, 1000)

    def lambda_133D():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_133D)
    BeginChrThread(0xA, 3, 0, 6)
    Sound(664, 0, 100, 0)
    Sound(321, 0, 100, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    OP_D5(0xA, 0x0, 0x0, 0x1388, 0x12C)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x2BC)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)
    Sound(998, 0, 100, 0)
    Sound(499, 0, 100, 0)
    SetCameraDistance(20500, 500)

    def lambda_13BB():
        OP_9B(0x1, 0xFE, 0x0, 0x186A0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13BB)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sleep(500)
    Sound(497, 2, 100, 0)
    Fade(500)
    StopEffect(0x2, 0x0)
    EndChrThread(0xA, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x0, 0x1F4, 0x1F4, 0x1F4)
    SetChrPos(0x8, 20000, 0, -100000, 225)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    OP_FF(0x3, 0x1F4, 0x1F4, 0x1F4)
    SetChrPos(0xB, -20000, 0, -100000, 225)
    SetChrPos(0xA, 20000, 0, 100000, 135)
    OP_68(20000, 2500, -80000, 0)
    MoveCamera(120, 15, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(30000, 0)
    OP_68(50000, 2500, 0, 2750)
    MoveCamera(90, 1, 0, 3500)
    SetCameraDistance(60000, 6000)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -2120, 880, -5120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 2120, 880, -5120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 1, 0, 7)
    Sleep(2000)
    BeginChrThread(0xA, 1, 0, 8)
    StopSound(497, 3000, 90)
    Sleep(2000)
    StopSound(980, 3000, 50)
    Sleep(2000)
    Fade(500)
    OP_68(-50000, 2500, -20000, 0)
    MoveCamera(90, 3, 0, 0)
    SetCameraDistance(50000, 0)
    OP_68(-80000, 2500, 0, 6000)
    MoveCamera(50, 3, 0, 6000)
    SetCameraDistance(25000, 6000)
    BeginChrThread(0xC, 1, 0, 11)
    BeginChrThread(0xB, 1, 0, 9)
    Sleep(3000)
    StopSound(497, 3000, 90)
    StopSound(132, 3000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_E8()
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x84)
    OP_24(0x1F1)
    OP_24(0x1F0)
    OP_24(0x3B6)
    SetScenarioFlags(0x22, 2)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C7 end

    def Function_3_1626(): pass

    label("Function_3_1626")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17D3")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_165D"),
        (1, "loc_169A"),
        (2, "loc_16D7"),
        (3, "loc_1714"),
        (4, "loc_1751"),
        (SWITCH_DEFAULT, "loc_178E"),
    )


    label("loc_165D")

    OP_87(0x3, 0xFF, 0x2, "Null_bp_hou(16)", 0x7, 0x0, 0x0, 0x0, 0xB4, 0xFFD3, 0x0, 0xFA, 0xFA, 0xFA, 0x0)
    Jump("loc_17CB")

    label("loc_169A")

    OP_87(0x3, 0xFF, 0x2, "Null_bp_hou(16)", 0x7, 0x0, 0x0, 0x0, 0xAA, 0xFFD3, 0x0, 0xFA, 0xFA, 0xFA, 0x0)
    Jump("loc_17CB")

    label("loc_16D7")

    OP_87(0x3, 0xFF, 0x2, "Null_bp_hou(16)", 0x7, 0x0, 0x0, 0x0, 0xAF, 0xFFD3, 0x0, 0xFA, 0xFA, 0xFA, 0x0)
    Jump("loc_17CB")

    label("loc_1714")

    OP_87(0x3, 0xFF, 0x2, "Null_bp_hou(16)", 0x7, 0x0, 0x0, 0x0, 0xB9, 0xFFD3, 0x0, 0xFA, 0xFA, 0xFA, 0x0)
    Jump("loc_17CB")

    label("loc_1751")

    OP_87(0x3, 0xFF, 0x2, "Null_bp_hou(16)", 0x7, 0x0, 0x0, 0x0, 0xBE, 0xFFD3, 0x0, 0xFA, 0xFA, 0xFA, 0x0)
    Jump("loc_17CB")

    label("loc_178E")

    OP_87(0x3, 0xFF, 0x2, "Null_bp_hou(16)", 0x7, 0x0, 0x0, 0x0, 0xB4, 0xFFD3, 0x0, 0xFA, 0xFA, 0xFA, 0x0)
    Jump("loc_17CB")

    label("loc_17CB")

    Sleep(100)
    Jump("Function_3_1626")

    label("loc_17D3")

    Return()

    # Function_3_1626 end

    def Function_4_17D4(): pass

    label("Function_4_17D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_197B")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_180B"),
        (1, "loc_1847"),
        (2, "loc_1883"),
        (3, "loc_18BF"),
        (4, "loc_18FB"),
        (SWITCH_DEFAULT, "loc_1937"),
    )


    label("loc_180B")

    PlayEffect(0x3, 0xFF, 0x8, 0x4, 0, 0, -100000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1973")

    label("loc_1847")

    PlayEffect(0x3, 0xFF, 0x8, 0x4, 0, 0, -100000, 180, -5, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1973")

    label("loc_1883")

    PlayEffect(0x3, 0xFF, 0x8, 0x4, 0, 0, -100000, 180, -10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1973")

    label("loc_18BF")

    PlayEffect(0x3, 0xFF, 0x8, 0x4, 0, 0, -100000, 180, 5, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1973")

    label("loc_18FB")

    PlayEffect(0x3, 0xFF, 0x8, 0x4, 0, 0, -100000, 180, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1973")

    label("loc_1937")

    PlayEffect(0x3, 0xFF, 0x8, 0x4, 0, 0, -100000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1973")

    label("loc_1973")

    Sleep(100)
    Jump("Function_4_17D4")

    label("loc_197B")

    Return()

    # Function_4_17D4 end

    def Function_5_197C(): pass

    label("Function_5_197C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1986")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AB7")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_19B5"),
        (1, "loc_19F1"),
        (2, "loc_1A2D"),
        (SWITCH_DEFAULT, "loc_1A69"),
    )


    label("loc_19B5")

    PlayEffect(0x7, 0xFF, 0xA, 0x4, 1500, 2000, -100000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1AA5")

    label("loc_19F1")

    PlayEffect(0x7, 0xFF, 0xA, 0x4, 1500, 2000, -100000, 180, -5, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1AA5")

    label("loc_1A2D")

    PlayEffect(0x7, 0xFF, 0xA, 0x4, 1500, 2000, -100000, 180, -10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1AA5")

    label("loc_1A69")

    PlayEffect(0x7, 0xFF, 0xA, 0x4, 1500, 2000, -100000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1AA5")

    label("loc_1AA5")

    Sleep(200)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1986")

    label("loc_1AB7")

    Return()

    # Function_5_197C end

    def Function_6_1AB8(): pass

    label("Function_6_1AB8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BF3")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1AF1"),
        (1, "loc_1B2D"),
        (2, "loc_1B69"),
        (SWITCH_DEFAULT, "loc_1BA5"),
    )


    label("loc_1AF1")

    PlayEffect(0x7, 0xFF, 0xA, 0x4, 750, 2000, -100000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1BE1")

    label("loc_1B2D")

    PlayEffect(0x7, 0xFF, 0xA, 0x4, 750, 2000, -100000, 180, -5, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1BE1")

    label("loc_1B69")

    PlayEffect(0x7, 0xFF, 0xA, 0x4, 750, 2000, -100000, 180, -10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1BE1")

    label("loc_1BA5")

    PlayEffect(0x7, 0xFF, 0xA, 0x4, 750, 2000, -100000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1BE1")

    label("loc_1BE1")

    Sleep(200)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1AC2")

    label("loc_1BF3")

    Return()

    # Function_6_1AB8 end

    def Function_7_1BF4(): pass

    label("Function_7_1BF4")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 20000, 0, -100000)
    OP_9F(0x1, 30000, 0, -50000)
    OP_9F(0x1, 50000, 0, -30000)
    OP_9F(0x1, 90000, 0, -15000)
    OP_9F(0x1, 150000, 0, -7000)
    OP_9F(0x1, 250000, 0, -7000)
    OP_9F(0x2, 0xFE, 35000, 0x6)
    Return()

    # Function_7_1BF4 end

    def Function_8_1C56(): pass

    label("Function_8_1C56")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 20000, 0, 100000)
    OP_9F(0x1, 30000, 0, 50000)
    OP_9F(0x1, 50000, 0, 30000)
    OP_9F(0x1, 90000, 0, 15000)
    OP_9F(0x1, 150000, 0, 7000)
    OP_9F(0x1, 250000, 0, 7000)
    OP_9F(0x2, 0xFE, 40000, 0x6)
    Return()

    # Function_8_1C56 end

    def Function_9_1CB8(): pass

    label("Function_9_1CB8")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -20000, 0, -100000)
    OP_9F(0x1, -30000, 0, -50000)
    OP_9F(0x1, -50000, 0, -25000)
    OP_9F(0x1, -90000, 0, -5000)
    OP_9F(0x1, -150000, 0, 5000)
    OP_9F(0x1, -250000, 0, 20000)
    OP_9F(0x2, 0xFE, 32000, 0x6)
    Return()

    # Function_9_1CB8 end

    def Function_10_1D1A(): pass

    label("Function_10_1D1A")

    Sound(496, 2, 10, 0)
    Sleep(200)
    OP_25(0x1F0, 0xF)
    Sleep(200)
    OP_25(0x1F0, 0x14)
    Sleep(200)
    OP_25(0x1F0, 0x19)
    Sleep(200)
    OP_25(0x1F0, 0x1E)
    Sleep(200)
    OP_25(0x1F0, 0x23)
    Sleep(200)
    OP_25(0x1F0, 0x28)
    Sleep(200)
    OP_25(0x1F0, 0x2D)
    Sleep(200)
    OP_25(0x1F0, 0x32)
    Return()

    # Function_10_1D1A end

    def Function_11_1D59(): pass

    label("Function_11_1D59")

    Sound(497, 2, 30, 0)
    Sleep(150)
    OP_25(0x1F1, 0x23)
    Sleep(150)
    OP_25(0x1F1, 0x28)
    Sleep(150)
    OP_25(0x1F1, 0x2D)
    Sleep(150)
    OP_25(0x1F1, 0x32)
    Sleep(150)
    OP_25(0x1F1, 0x37)
    Sleep(150)
    OP_25(0x1F1, 0x3C)
    Sleep(150)
    OP_25(0x1F1, 0x41)
    Sleep(150)
    OP_25(0x1F1, 0x46)
    Sleep(150)
    OP_25(0x1F1, 0x4B)
    Sleep(150)
    OP_25(0x1F1, 0x50)
    Sleep(150)
    OP_25(0x1F1, 0x55)
    Sleep(150)
    OP_25(0x1F1, 0x5A)
    Sleep(150)
    OP_25(0x1F1, 0x5F)
    Sleep(150)
    OP_25(0x1F1, 0x64)
    Return()

    # Function_11_1D59 end

    def Function_12_1DC2(): pass

    label("Function_12_1DC2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    LoadEffect(0x9, "event/eva03_01.eff")
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(950)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    SetChrPos(0x8, 0, 0, 0, 0)
    OP_93(0x8, 0x0, 0x0)
    OP_75(0x0, 0x1, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x3, 0xB)
    OP_49()
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    OP_71(0x3, 0x65, 0xA0, 0x0, 0x20)
    SetChrPos(0x8, 0, 0, 0, 0)
    OP_93(0x8, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0x8, 0x5, 0, 0, 0, 180, 0, 0, 9000, 1000, 9000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    OP_68(0, 500, 0, 0)
    MoveCamera(185, 13, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(67740, 0)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_68(0, 500, 0, 3000)
    MoveCamera(200, 15, 0, 3000)
    OP_6E(850, 3000)
    SetCameraDistance(57740, 3000)
    OP_0D()
    Sleep(1500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_71(0x3, 0x0, 0x32, 0x0, 0x0)
    OP_75(0x0, 0x2, 0x1F4)
    Sleep(500)
    CancelBlur(1000)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_75(0x3, 0x1, 0x3E8)
    OP_68(460, 500, -15000, 3000)
    MoveCamera(180, 13, 0, 3000)
    OP_6E(850, 3000)
    SetCameraDistance(57930, 3000)
    Sleep(2000)
    BeginChrThread(0x8, 0, 0, 13)
    Sleep(500)
    OP_82(0x1F4, 0x1F4, 0x5DC, 0xBB8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(500)
    CancelBlur(3000)
    Sound(499, 0, 80, 0)
    Sleep(1000)
    StopSound(132, 1000, 90)
    StopSound(497, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x3B6)
    SetScenarioFlags(0x23, 1)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1DC2 end

    def Function_13_2090(): pass

    label("Function_13_2090")

    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x3E8, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xFA0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x1F40, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x3E80, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x5DC0, 0x0)
    Return()

    # Function_13_2090 end

    def Function_14_20EB(): pass

    label("Function_14_20EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    LoadEffect(0x1, "event/ev15056.eff")
    LoadEffect(0x3, "event/ev17019.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x9, "event/eva03_01.eff")
    OP_F3(200000)
    SoundLoad(132)
    SoundLoad(980)
    SoundLoad(497)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x0, 0x1F4, 0x1F4, 0x1F4)
    PlayEffect(0x0, 0x1, 0x8, 0x5, -2125, 875, -5125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x8, 0x5, 2125, 875, -5125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x2, 0xA)
    OP_49()
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_70(0x2, 0xDD)
    OP_87(0x7, 0xFF, 0x2, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x2, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x2, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x2, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x2, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x2, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetChrPos(0x8, 0, 0, 200000, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_93(0xA, 0x0, 0x0)
    OP_68(0, 500, 13500, 0)
    MoveCamera(0, 12, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(21000, 0)
    Sound(132, 2, 100, 0)
    Sound(980, 2, 100, 0)
    Sound(497, 2, 70, 0)
    Sound(499, 0, 80, 0)
    Sound(994, 0, 50, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0xA, 2, 0, 17)
    BeginChrThread(0x8, 0, 0, 19)
    PlayEffect(0x9, 0x7, 0x8, 0x5, 0, 0, 0, 180, 0, 0, 3000, 1000, 18000, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(30940, 2800)
    OP_82(0x12C, 0x12C, 0xBB8, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(1)
    CancelBlur(3500)
    OP_0D()
    Sleep(1600)
    BeginChrThread(0xC, 1, 0, 15)
    OP_87(0x1, 0x0, 0x2, "Null_bp_hou(16)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x113, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(200)
    OP_82(0x12C, 0x12C, 0x1388, 0x1F4)
    BlurSwitch(0x1C2, 0xBBFFFFFF, 0x0, 0x1, 0x1E)
    OP_7D(0xE1, 0xE1, 0xE1, 0x0, 0x12C)
    Sleep(500)
    CancelBlur(1500)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    OP_6F(0x50)
    Sleep(1200)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x8, 0x0)
    OP_25(0x1F1, 0x64)
    OP_FF(0x0, 0x3E8, 0x3E8, 0x3E8)
    SetChrPos(0x8, 0, 0, 50000, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0xA, 0, -1000000, -50000, 0)
    OP_93(0xA, 0x0, 0x0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x7, 0x0)
    PlayEffect(0x9, 0x7, 0x8, 0x5, 0, 0, 0, 180, 0, 0, 3000, 1000, 18000, 0xFF, 0, 0, 0, 0)
    StopSound(980, 500, 90)
    Fade(500)
    OP_68(0, 2500, 56150, 0)
    MoveCamera(180, 0, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(31010, 0)
    OP_68(0, 2500, 76150, 2000)
    MoveCamera(113, 2, 0, 2000)
    OP_6E(850, 2000)
    SetCameraDistance(31010, 2000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0xBB8, 0x7D0)
    BeginChrThread(0x8, 1, 0, 20)
    BeginChrThread(0x8, 3, 0, 21)
    OP_0D()
    Sleep(900)
    CancelBlur(2000)
    OP_68(20410, 2500, -1610, 3700)
    MoveCamera(17, 2, 0, 3700)
    OP_6E(850, 3700)
    SetCameraDistance(33010, 3700)
    OP_6F(0x79)
    SetChrPos(0xA, 0, 0, -50000, 0)
    Sound(980, 2, 70, 0)
    Sound(998, 0, 100, 0)
    OP_68(13330, 2500, -24910, 1500)
    MoveCamera(29, 6, 0, 1500)
    OP_6E(850, 1500)
    SetCameraDistance(49260, 1500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(4000)
    OP_6F(0x79)
    BeginChrThread(0xA, 2, 0, 22)
    SetCameraDistance(59260, 2000)

    def lambda_274B():
        OP_9B(0x1, 0xFE, 0x0, 0x27100, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_274B)
    Sleep(1000)
    Sound(499, 0, 100, 0)
    OP_82(0x258, 0x258, 0xBB8, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(1)
    CancelBlur(3500)

    def lambda_278E():
        OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_278E)
    Sleep(1000)
    StopSound(497, 2000, 90)
    StopSound(980, 2000, 50)
    Sleep(1000)
    BeginChrThread(0xC, 1, 0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4211", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_20EB end

    def Function_15_27CE(): pass

    label("Function_15_27CE")

    Sleep(600)
    Sound(1036, 0, 100, 0)
    Sleep(2100)
    Sound(1036, 0, 70, 0)
    Sound(1014, 0, 50, 0)
    Sleep(100)
    Sound(1014, 0, 40, 0)
    Sleep(100)
    Sound(1014, 0, 40, 0)
    Sleep(100)
    Sound(1014, 0, 40, 0)
    Sleep(100)
    Sound(1014, 0, 40, 0)
    Return()

    # Function_15_27CE end

    def Function_16_280B(): pass

    label("Function_16_280B")

    OP_25(0x84, 0x5A)
    Sleep(100)
    OP_25(0x84, 0x50)
    Sleep(100)
    OP_25(0x84, 0x46)
    Sleep(100)
    OP_25(0x84, 0x3C)
    Sleep(100)
    OP_25(0x84, 0x32)
    Sleep(100)
    OP_25(0x84, 0x28)
    Sleep(100)
    OP_25(0x84, 0x1E)
    Sleep(100)
    OP_25(0x84, 0x14)
    Sleep(100)
    OP_25(0x84, 0xA)
    Sleep(100)
    OP_25(0x84, 0x0)
    Return()

    # Function_16_280B end

    def Function_17_284F(): pass

    label("Function_17_284F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28AF")
    OP_68(-500, 2500, 10500, 1100)
    Sleep(1000)
    OP_68(0, 2500, 10350, 1100)
    Sleep(1000)
    OP_68(500, 2500, 10500, 1100)
    Sleep(1000)
    OP_68(0, 2500, 10650, 1100)
    Sleep(1000)
    Jump("Function_17_284F")

    label("loc_28AF")

    Return()

    # Function_17_284F end

    def Function_18_28B0(): pass

    label("Function_18_28B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28F8")
    MoveCamera(0, 12, 0, 900)
    Sleep(800)
    MoveCamera(0, 11, 0, 900)
    Sleep(800)
    MoveCamera(0, 10, 0, 900)
    Sleep(800)
    MoveCamera(0, 11, 0, 900)
    Sleep(800)
    Jump("Function_18_28B0")

    label("loc_28F8")

    Return()

    # Function_18_28B0 end

    def Function_19_28F9(): pass

    label("Function_19_28F9")

    OP_9B(0x1, 0xFE, 0x0, 0x186A0, 0x4E20, 0x0)
    Return()

    # Function_19_28F9 end

    def Function_20_2909(): pass

    label("Function_20_2909")

    Sleep(200)
    OP_9B(0x1, 0xFE, 0x5A, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x5A, 0x1F4, 0x1F40, 0x1)
    OP_9B(0x1, 0xFE, 0x5A, 0x1F4, 0x2EE0, 0x1)
    OP_9B(0x1, 0xFE, 0x5A, 0x5DC0, 0x4E20, 0x1)
    OP_9B(0x1, 0xFE, 0x5A, 0x1F4, 0x2EE0, 0x1)
    OP_9B(0x1, 0xFE, 0x5A, 0x1F4, 0x1F40, 0x1)
    OP_9B(0x1, 0xFE, 0x5A, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_20_2909 end

    def Function_21_2976(): pass

    label("Function_21_2976")

    Sleep(700)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 20000, 80000, 180, 27, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 20000, 80000, 180, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8000, 20000, 80000, 180, 33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 12000, 20000, 80000, 180, 36, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 16000, 20000, 80000, 180, 39, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 20000, 20000, 80000, 180, 42, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Return()

    # Function_21_2976 end

    def Function_22_2AD6(): pass

    label("Function_22_2AD6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B36")
    OP_68(12830, 2500, -24910, 1100)
    Sleep(1000)
    OP_68(13330, 2500, -24761, 1100)
    Sleep(1000)
    OP_68(13830, 2500, -24910, 1100)
    Sleep(1000)
    OP_68(13330, 2500, -25060, 1100)
    Sleep(1000)
    Jump("Function_22_2AD6")

    label("loc_2B36")

    Return()

    # Function_22_2AD6 end

    SaveToFile()

Try(main)
