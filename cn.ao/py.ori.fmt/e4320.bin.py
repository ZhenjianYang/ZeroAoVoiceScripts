from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4320.bin",                # FileName
        "e4320",                    # MapName
        "e4320",                    # Location
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
        "e4320",                  # 0
        "猎兵加雷斯",             # 1
        "猎兵扎克斯",             # 2
        "梅尔卡瓦",               # 3
        "贝奥武夫",               # 4
        "假",                     # 5
        "SE控制",                 # 6
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(364, 0)                                        # 0

    ScpFunction((
        "Function_0_16C",          # 00, 0
        "Function_1_1B8",          # 01, 1
        "Function_2_1C6",          # 02, 2
        "Function_3_79D",          # 03, 3
        "Function_4_855",          # 04, 4
        "Function_5_90D",          # 05, 5
        "Function_6_125D",         # 06, 6
        "Function_7_1276",         # 07, 7
        "Function_8_176E",         # 08, 8
        "Function_9_17CA",         # 09, 9
        "Function_10_24A3",        # 0A, 10
        "Function_11_24C8",        # 0B, 11
    ))


    def Function_0_16C(): pass

    label("Function_0_16C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 7)), scpexpr(EXPR_END)), "loc_180")
    ClearScenarioFlags(0x23, 7)
    Event(0, 2)
    Jump("loc_1B7")

    label("loc_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 0)), scpexpr(EXPR_END)), "loc_194")
    ClearScenarioFlags(0x24, 0)
    Event(0, 5)
    Jump("loc_1B7")

    label("loc_194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 1)), scpexpr(EXPR_END)), "loc_1A8")
    ClearScenarioFlags(0x24, 1)
    Event(0, 7)
    Jump("loc_1B7")

    label("loc_1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 2)), scpexpr(EXPR_END)), "loc_1B7")
    ClearScenarioFlags(0x24, 2)
    Event(0, 9)

    label("loc_1B7")

    Return()

    # Function_0_16C end

    def Function_1_1B8(): pass

    label("Function_1_1B8")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x5208)
    Return()

    # Function_1_1B8 end

    def Function_2_1C6(): pass

    label("Function_2_1C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17021.eff")
    LoadEffect(0x1, "event/ev17086.eff")
    LoadEffect(0x2, "event/ev17087.eff")
    LoadEffect(0x3, "event/eva03_01.eff")
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(496)
    CreatePortrait(0, 16, 20, 528, 84, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis507.itp")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x0, 0xA)
    OP_49()
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x0, 0x1F4, 0x1F4, 0x1F4)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x1, 0xB)
    OP_49()
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x1, 0x64, 0x82, 0x0, 0x20)
    OP_F3(100000)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0xA, 0, 205000, -8700000, 0)
    OP_D5(0xA, 0x7D0, 0x0, 0x0, 0x0)
    OP_68(0, 201000, 400000, 0)
    MoveCamera(0, 0, 2, 0)
    OP_6E(800, 0)
    SetCameraDistance(9080000, 0)
    SetCameraDistance(9100000, 6000)
    MoveCamera(0, 0, -2, 6000)
    PlayBGM("ed7542", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x0, 0xA, 0x5, -2120, 870, -5120, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xA, 0x5, 2120, 870, -5120, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    Sound(132, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sound(499, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    def lambda_3E2():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3E2)
    Sleep(500)
    CancelBlur(1000)
    WaitChrThread(0xA, 1)
    OP_0D()
    OP_6F(0x79)
    Sound(497, 2, 60, 0)
    Sound(496, 2, 50, 0)
    Fade(500)
    Call(0, 3)
    OP_FF(0x0, 0x3E8, 0x3E8, 0x3E8)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    OP_68(0, 2000, 10000, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, 2000, 0, 6000)
    MoveCamera(135, 10, -5, 6000)
    SetCameraDistance(45000, 6000)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    OP_82(0x32, 0x32, 0xBB8, 0x1D4C)
    PlayEffect(0x1, 0x0, 0xA, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xA, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0xA, 0x5, 0, 4000, 30000, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_6F(0x79)
    PlayEffect(0x0, 0x2, 0xA, 0x0, 100000, 20000, -150000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    StopSound(496, 500, 40)
    OP_25(0x1F1, 0x64)
    Fade(500)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetChrPos(0xB, 0, 0, 0, 0)
    OP_68(0, 5500, 10000, 0)
    MoveCamera(90, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(21000, 0)
    OP_68(0, 5500, -10000, 5000)
    OP_82(0x32, 0x32, 0xBB8, 0x1388)
    CancelBlur(0)
    OP_87(0x2, 0x2, 0x1, "Null_burn_l", 0x7, 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    OP_87(0x2, 0x3, 0x1, "Null_burn_r", 0x7, 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    PlayEffect(0x3, 0x4, 0xB, 0x5, 0, 4500, 30000, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(4000)
    Fade(500)
    OP_68(0, 4500, 3000, 0)
    MoveCamera(170, 15, 5, 0)
    OP_6E(800, 0)
    SetCameraDistance(60000, 0)
    OP_68(0, 4500, 0, 7100)
    MoveCamera(160, 10, 5, 7100)
    SetCameraDistance(45000, 7100)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    OP_82(0x64, 0x64, 0xBB8, 0x1BBC)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    StopSound(497, 1000, 90)
    StopSound(132, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x1F0)
    SetScenarioFlags(0x23, 7)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C6 end

    def Function_3_79D(): pass

    label("Function_3_79D")

    SetMapObjFrame(0xFF, "ud02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ud01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bigwood", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mawaru02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mawaru01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mawaru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "nukieda", 0x0, 0x1)
    SetMapObjFrame(0xFF, "wood01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari2_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "spinkumo01", 0x0, 0x1)
    Return()

    # Function_3_79D end

    def Function_4_855(): pass

    label("Function_4_855")

    SetMapObjFrame(0xFF, "ud02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ud01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bigwood", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mawaru02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mawaru01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mawaru00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "nukieda", 0x1, 0x1)
    SetMapObjFrame(0xFF, "wood01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "spinkumo01", 0x1, 0x1)
    Return()

    # Function_4_855 end

    def Function_5_90D(): pass

    label("Function_5_90D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    LoadEffect(0x1, "event/ev17087.eff")
    LoadEffect(0x2, "event/ev10012.eff")
    LoadEffect(0x3, "event/ev17055.eff")
    LoadEffect(0x4, "event/ev17056.eff")
    LoadEffect(0x5, "event/ev17094.eff")
    LoadEffect(0x6, "event/eva03_01.eff")
    LoadEffect(0x7, "event/ev17093.eff")
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(496)
    SoundLoad(865)
    SoundLoad(861)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x0, 0xA)
    OP_49()
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x1, 0xB)
    OP_49()
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x1, 0x64, 0x82, 0x0, 0x20)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Call(0, 3)
    OP_F3(100000)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetChrPos(0xB, 0, 0, 0, 0)
    OP_D5(0xB, 0x0, 0x0, 0x0, 0x0)
    OP_68(0, 5000, 6750, 0)
    MoveCamera(135, -10, 10, 0)
    OP_6E(800, 0)
    SetCameraDistance(26000, 0)
    OP_68(0, 5000, 8750, 2000)
    SetCameraDistance(32000, 2000)
    OP_87(0x1, 0x0, 0x1, "Null_burn_l", 0x7, 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    OP_87(0x1, 0x1, 0x1, "Null_burn_r", 0x7, 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    PlayEffect(0x6, 0x4, 0xB, 0x5, 0, 5000, 30000, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 100, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x7D0)
    OP_87(0x2, 0x2, 0x1, "Null_burn_l", 0x7, 0x0, 0x0, 0x2EE0, 0xB4, 0x0, 0x0, 0x7D0, 0x7D0, 0xFA0, 0x0)
    OP_87(0x2, 0x3, 0x1, "Null_burn_r", 0x7, 0x0, 0x0, 0x2EE0, 0xB4, 0x0, 0x0, 0x7D0, 0x7D0, 0xFA0, 0x0)
    Sleep(1500)
    OP_68(0, 5000, 20000, 500)
    Sleep(250)
    Fade(500)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_D5(0xA, 0x0, 0x0, 0xFFFFD8F0, 0x0)
    SetChrPos(0xC, 10000, -3000, -30000, 0)
    OP_D5(0xC, 0x0, 0xAFC8, 0x0, 0x0)
    OP_68(0, 1000, 0, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(55000, 0)
    StopSound(865, 3500, 80)
    StopSound(861, 3500, 80)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x2710)
    PlayEffect(0x5, 0x4, 0xC, 0x5, 0, 0, 0, -40, -25, 0, 30000, 30000, 15000, 0xFF, 0, 0, 0, 0)
    Sound(499, 0, 100, 0)
    Sound(496, 2, 80, 0)

    def lambda_CFC():
        OP_96(0xFE, 0xFFFF3CB0, 0xC350, 0x4E20, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CFC)

    def lambda_D16():
        OP_D5(0xFE, 0x0, 0x0, 0xFFFFC568, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D16)
    OP_68(-50000, 50000, 20000, 2000)
    MoveCamera(345, -20, 0, 2000)
    SetCameraDistance(100000, 2000)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    Sound(994, 0, 80, 0)

    def lambda_D62():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D62)
    OP_96(0xA, 0xFFFF3CB0, 0xC350, 0x88B8, 0x4E20, 0x0)
    OP_68(-50000, 50000, 200000, 3000)
    MoveCamera(355, -10, 0, 3000)
    SetCameraDistance(350000, 3000)
    StopEffect(0x4, 0x2)

    def lambda_DB7():
        OP_96(0xFE, 0xFFFF3CB0, 0xC350, 0x3D090, 0x186A0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_DB7)
    PlayEffect(0x7, 0x2, 0xA, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x3, 0xA, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x0, 0xA, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xA, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    CancelBlur(500)
    WaitChrThread(0xA, 1)
    Fade(500)
    SetChrFlags(0xC, 0x80)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    SetChrPos(0xA, 0, 0, -100000, 0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    OP_68(0, 1000, -95000, 0)
    MoveCamera(350, 30, -5, 0)
    OP_6E(800, 0)
    SetCameraDistance(38000, 0)
    OP_68(0, 1000, 0, 3000)
    MoveCamera(10, 20, 5, 3000)
    SetCameraDistance(50000, 3000)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -20000, -8750, 10000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 20000, 9750, -10000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -10250, 6750, 20000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 10250, -3750, -10000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -15250, 4750, 1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 15250, -5750, 10000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4250, 3750, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4250, -3750, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x2, 0xA, 0x5, 0, 4000, 30000, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    PlayEffect(0x0, 0x3, 0xA, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xA, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xA, 0x0, 0x186A0, 0x9C40, 0x0)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    StopEffect(0x2, 0x2)
    OP_82(0x2EE, 0x2EE, 0xBB8, 0x9C4)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 6)
    StopSound(132, 1400, 100)
    Sleep(1500)
    StopSound(497, 1000, 90)
    StopSound(496, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_90D end

    def Function_6_125D(): pass

    label("Function_6_125D")

    Sound(289, 0, 100, 0)
    Sleep(400)
    Sound(203, 0, 100, 0)
    Sleep(900)
    Sound(203, 0, 100, 0)
    Return()

    # Function_6_125D end

    def Function_7_1276(): pass

    label("Function_7_1276")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17087.eff")
    LoadEffect(0x1, "event/ev17057.eff")
    LoadEffect(0x2, "event/eva01_01.eff")
    LoadEffect(0x3, "event/ev10017.eff")
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(496)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x0, 0xA)
    OP_49()
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x1, 0xB)
    OP_49()
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x1, 0x64, 0x82, 0x0, 0x20)
    Call(0, 3)
    OP_F3(100000)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0xB, 60000, -1000, 200000, 0)
    OP_D5(0xB, 0x0, 0x2E630, 0x0, 0x0)
    OP_68(7500, 2500, 38000, 0)
    MoveCamera(10, 5, 5, 0)
    OP_6E(800, 0)
    SetCameraDistance(70000, 0)
    MoveCamera(20, 7, 5, 2000)
    OP_68(20000, 5500, 60000, 2000)
    SetCameraDistance(32000, 2000)
    PlayEffect(0x3, 0x2, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    Sound(994, 0, 70, 0)

    def lambda_142E():
        OP_99(0xFE, 0xA, 0xC350, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_142E)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    CancelBlur(0)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    CancelBlur(0)
    EndChrThread(0xB, 0x1)
    Fade(500)
    Sound(496, 2, 80, 0)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrPos(0xB, 30000, -4000, 60000, 10)
    OP_D5(0xB, 0x0, 0x2E630, 0x0, 0x0)
    OP_68(6000, 2500, 4000, 0)
    MoveCamera(50, 25, 10, 0)
    OP_6E(800, 0)
    SetCameraDistance(33000, 0)
    MoveCamera(45, 30, 10, 750)
    SetCameraDistance(35000, 3000)
    OP_87(0x0, 0x0, 0x1, "Null_burn_l", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    OP_87(0x0, 0x1, 0x1, "Null_burn_r", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    Sound(920, 0, 100, 0)
    Sound(921, 0, 100, 0)
    Sound(922, 0, 100, 0)
    PlayEffect(0x1, 0x2, 0xA, 0x5, -5000, 0, 10000, 70, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_96(0xB, 0x4A38, 0xFFFFF060, 0x4268, 0xD6D8, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    BeginChrThread(0xB, 0, 0, 8)
    Sound(833, 0, 100, 0)
    Sound(880, 0, 100, 0)
    Sound(875, 2, 70, 0)
    Sleep(2000)
    Fade(500)
    SetChrPos(0xB, 22000, -2000, 15000, 10)
    OP_D5(0xB, 0x0, 0x2E630, 0x0, 0x0)
    OP_68(7900, 1500, 0, 0)
    MoveCamera(20, 20, 10, 0)
    OP_6E(800, 0)
    SetCameraDistance(40000, 0)
    MoveCamera(0, 10, 10, 3000)
    Sound(200, 0, 60, 0)
    Sound(833, 0, 100, 0)

    def lambda_1671():
        OP_96(0xFE, 0x55F0, 0xFFFFF830, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1671)

    def lambda_168B():
        OP_D5(0xFE, 0x0, 0x2BF20, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_168B)
    OP_0D()
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    StopEffect(0x2, 0x2)
    StopSound(875, 500, 60)
    StopSound(132, 500, 90)
    EndChrThread(0xB, 0x0)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    SetCameraDistance(50000, 500)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x7D0)
    Sound(200, 0, 60, 0)
    Sound(880, 0, 100, 0)

    def lambda_16F2():
        OP_96(0xA, 0xFFFFF830, 0x0, 0x0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16F2)

    def lambda_170C():
        OP_96(0xB, 0x61A8, 0xFFFFF830, 0xFFFF3CB0, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_170C)

    def lambda_1726():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1726)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    StopSound(497, 1000, 90)
    StopSound(496, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 1)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1276 end

    def Function_8_176E(): pass

    label("Function_8_176E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17C9")
    OP_82(0x190, 0x190, 0xBB8, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, -11000, 8000, -7000, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_8_176E")

    label("loc_17C9")

    Return()

    # Function_8_176E end

    def Function_9_17CA(): pass

    label("Function_9_17CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch42600.itc", 0x1E)
    LoadChrToIndex("chr/ch42700.itc", 0x1F)
    LoadEffect(0x0, "event/ev17058.eff")
    LoadEffect(0x1, "event/ev17086.eff")
    LoadEffect(0x2, "event/ev17087.eff")
    LoadEffect(0x3, "event/ev17055.eff")
    LoadEffect(0x4, "event/ev10009.eff")
    LoadEffect(0x5, "event/eva03_01.eff")
    LoadEffect(0x6, "event/ev17093.eff")
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(496)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x0, 0xA)
    OP_49()
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x1, 0xB)
    OP_49()
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x1, 0x64, 0x82, 0x0, 0x20)
    Call(0, 3)
    OP_F3(100000)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0xA, 0, 0, -50000, 0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    OP_68(0, 1000, -50000, 0)
    MoveCamera(115, 10, 5, 0)
    OP_6E(800, 0)
    SetCameraDistance(55000, 0)
    OP_68(0, 1000, -47000, 2000)
    MoveCamera(135, 0, 5, 9000)
    SetCameraDistance(50000, 9000)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 80, 0)
    Sound(496, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(994, 0, 100, 0)
    PlayEffect(0x6, 0x3, 0xA, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x4, 0xA, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x0, 0xA, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xA, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x5, 0xA, 0x5, 0, 4000, 30000, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_68(0, 1000, 50000, 3000)
    Sleep(300)

    def lambda_1AC6():
        OP_9B(0x1, 0xFE, 0x0, 0x186A0, 0x9470, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1AC6)
    Sleep(1000)
    Sound(983, 0, 60, 0)
    Sound(881, 0, 80, 0)
    PlayEffect(0x0, 0x2, 0xA, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Fade(500)
    EndChrThread(0xA, 0x1)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    Sound(825, 2, 100, 0)
    OP_68(0, 1000, 5000, 0)
    MoveCamera(200, -10, 5, 0)
    OP_6E(800, 0)
    SetCameraDistance(50000, 0)
    OP_68(0, 1000, 100000, 5000)
    MoveCamera(225, -15, 5, 5000)
    SetCameraDistance(55000, 5000)

    def lambda_1BAA():
        OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BAA)
    OP_82(0xC8, 0xC8, 0xBB8, 0x1388)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 10000, 8000, 10000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 20000, 10000, 20000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -10000, -5000, 30000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -12000, 15000, 40000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 10000, -10000, 50000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 10000, 20000, 60000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -8000, 6000, 70000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -9000, 10000, 80000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 12000, -10000, 90000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 15000, -20000, 100000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xD, 1, 0, 11)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, 5000, 5000, 4000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, -5000, 2000, 5000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, 2000, -3000, 3000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, 3000, 6000, 8000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, -5000, -5000, 5000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, 5000, -2000, 8000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, 2000, 5000, 2000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, 0, 4000, 10000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x2, 0x2)
    StopSound(497, 2000, 70)
    StopSound(496, 2000, 90)
    Fade(500)
    StopEffect(0x5, 0x0)
    CancelBlur(0)
    PlayEffect(0x1, 0x0, 0xA, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xA, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1500, 0xFF, 0, 0, 0, 0)
    SetChrPos(0xA, 0, 200000, 0, 0)
    Call(0, 4)
    OP_68(0, 201000, 0, 0)
    MoveCamera(0, 0, 2, 0)
    OP_6E(800, 0)
    SetCameraDistance(50000, 0)
    MoveCamera(0, 0, -2, 5000)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(499, 0, 100, 0)
    Sound(994, 0, 100, 0)

    def lambda_20CC():
        OP_9B(0x1, 0xFE, 0x0, 0x493E0, 0x124F8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_20CC)
    Sleep(500)
    CancelBlur(1000)
    Sleep(1500)
    StopSound(825, 1000, 100)
    StopSound(132, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x1)
    OP_68(10000000, 10000000, 10000000, 0)
    Sleep(500)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_07b.pmf", 0x21E, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    OP_70(0x1, 0xF)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xB, 30000, 400000, 0, 0)
    OP_D5(0xB, 0x0, 0x11170, 0x0, 0x0)
    SetChrPos(0x9, 25500, 411300, 2250, 315)
    SetChrPos(0x8, 27000, 411300, 2650, 315)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(24170, 412400, 3120, 0)
    MoveCamera(23, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(70000, 0)
    OP_68(21130, 412400, -15210, 0)
    MoveCamera(27, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(60160, 0)
    OP_68(25260, 412400, 2950, 5000)
    MoveCamera(3, 14, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(50000, 5000)
    OP_87(0x2, 0x3, 0x1, "Null_burn_l", 0x7, 0x0, 0x0, 0x0, 0xFA, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x2, 0x4, 0x1, "Null_burn_r", 0x7, 0x0, 0x0, 0x0, 0xFA, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sound(132, 2, 60, 0)
    Sound(497, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0x1770)
    Fade(1000)
    OP_68(27300, 412400, 9360, 0)
    MoveCamera(8, 8, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(28000, 0)
    MoveCamera(14, 8, 0, 50000)
    SetCameraDistance(27000, 1500)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)

    #C0001
    ChrTalk(
        0x9,
        "#5P啧……有点本事啊。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        (
            "#5P本想用锚固定住他们的飞艇，\x01",
            "接近之后展开白刃战呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#11P看来我们的空战技术\x01",
            "还不纯熟啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#11P算啦，之后的事情就交给\x01",
            "西格蒙德副团长他们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            "#5P嘿……\x01",
            "真羡慕小姐和副团长啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "#5P竟然可以在那么棒的地方\x01",
            "尽情享受战斗的乐趣。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 3000)
    StopSound(132, 2000, 50)
    StopSound(497, 2000, 30)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("m9000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_17CA end

    def Function_10_24A3(): pass

    label("Function_10_24A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24C7")
    OP_82(0x2, 0x2, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_10_24A3")

    label("loc_24C7")

    Return()

    # Function_10_24A3 end

    def Function_11_24C8(): pass

    label("Function_11_24C8")

    Sound(833, 0, 100, 0)
    Sleep(100)
    Sound(607, 0, 100, 0)
    Sound(598, 0, 80, 0)
    Sleep(500)
    Sound(598, 0, 70, 0)
    Sleep(500)
    Sound(598, 0, 70, 0)
    Sleep(500)
    Sound(598, 0, 70, 0)
    Sleep(500)
    Sound(598, 0, 70, 0)
    Sleep(500)
    Sound(598, 0, 70, 0)
    Sleep(500)
    Sound(598, 0, 70, 0)
    Sleep(500)
    Sound(598, 0, 70, 0)
    Return()

    # Function_11_24C8 end

    SaveToFile()

Try(main)
