from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c110b.bin",                # FileName
        "c110b",                    # MapName
        "c110b",                    # Location
        0x0016,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 22, 0, 0, 0, 1],
    )

    BuildStringList((
        "c110b",                  # 0
        "猎兵",                   # 1
        "猎兵",                   # 2
        "猎兵",                   # 3
        "猎兵",                   # 4
        "猎兵",                   # 5
        "猎兵",                   # 6
        "猎兵",                   # 7
        "猎兵",                   # 8
        "猎兵",                   # 9
        "猎兵",                   # 10
        "猎兵",                   # 11
        "猎兵",                   # 12
        "猎兵",                   # 13
        "猎兵",                   # 14
        "猎兵",                   # 15
        "猎兵",                   # 16
        "猎兵",                   # 17
        "猎兵",                   # 18
        "猎兵",                   # 19
        "猎兵",                   # 20
        "中央广场",               # 21
        "西街",                   # 22
        "行政区",                 # 23
        "住宅街",                 # 24
        "欢乐街",                 # 25
        "东街",                   # 26
        "旧城区",                 # 27
        "港湾区",                 # 28
        "ＩＢＣ",                 # 29
        "站前街道",               # 30
        "后巷",                   # 31
        "乌尔斯拉间道",           # 32
        "东克洛斯贝尔街道",       # 33
        "西克洛斯贝尔街道",       # 34
        "玛因兹山道",             # 35
        "兰花塔",                 # 36
    ))

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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "中央广场")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "西街")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "行政区")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "住宅街")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "欢乐街")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "东街")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "旧城区")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "港湾区")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "站前街道")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "后巷")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-5.0, 0.0, 178.0, 0x0000, 0x0000, "兰花塔")
    PlaceName(-60.130001068115234, 0.0, -126.0999984741211, 0x0000, 0x0051, "")
    PlaceName(9.75, 0.0, -92.30000305175781, 0x0000, 0x0054, "")
    PlaceName(-28.280000686645508, 0.0, -136.5, 0x0000, 0x0057, "")
    PlaceName(-61.099998474121094, 0.0, -88.4000015258789, 0x0000, 0x0053, "")
    PlaceName(-34.45000076293945, 0.0, -57.20000076293945, 0x0000, 0x0053, "")
    PlaceName(-100.43000030517578, 0.0, -94.9000015258789, 0x0000, 0x0053, "")
    PlaceName(-113.0999984741211, 0.0, -67.5999984741211, 0x0000, 0x0053, "")
    PlaceName(-81.9000015258789, 0.0, -26.0, 0x0000, 0x0052, "")
    PlaceName(-75.7300033569336, 0.0, -42.900001525878906, 0x0000, 0x0053, "")
    PlaceName(-64.3499984741211, 0.0, -53.95000076293945, 0x0000, 0x0053, "")
    PlaceName(-27.299999237060547, 0.0, 38.349998474121094, 0x0000, 0x0051, "")
    PlaceName(118.30000305175781, 0.0, -137.8000030517578, 0x0000, 0x0052, "")
    PlaceName(96.19999694824219, 0.0, -255.4499969482422, 0x0000, 0x0053, "")
    PlaceName(79.30000305175781, 0.0, -231.39999389648438, 0x0000, 0x0053, "")

    ChipFrameInfo(1332, 0)                                       # 0

    ScpFunction((
        "Function_0_534",          # 00, 0
        "Function_1_544",          # 01, 1
        "Function_2_545",          # 02, 2
        "Function_3_E24",          # 03, 3
        "Function_4_E74",          # 04, 4
        "Function_5_EA8",          # 05, 5
    ))


    def Function_0_534(): pass

    label("Function_0_534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_543")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_543")

    Return()

    # Function_0_534 end

    def Function_1_544(): pass

    label("Function_1_544")

    Return()

    # Function_1_544 end

    def Function_2_545(): pass

    label("Function_2_545")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    LoadChrToIndex("chr/ch41950.itc", 0x23)
    LoadChrToIndex("chr/ch41951.itc", 0x24)
    LoadChrToIndex("chr/ch41952.itc", 0x25)
    LoadChrToIndex("chr/ch42050.itc", 0x28)
    LoadChrToIndex("chr/ch42051.itc", 0x29)
    LoadChrToIndex("chr/ch42052.itc", 0x2A)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "battle/ms00001.eff")
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(868)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(863)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x28)
    SetChrSubChip(0x13, 0x1)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x28)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x28)
    SetChrSubChip(0x17, 0x1)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x1)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x1)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x1)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x25)
    SetChrSubChip(0x1B, 0x1)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    OP_68(14650, 8800, 19240, 0)
    MoveCamera(25, 8, -5, 0)
    OP_6E(600, 0)
    SetCameraDistance(36650, 0)
    MoveCamera(62, -4, -5, 8000)
    SetCameraDistance(45750, 8000)
    SetChrPos(0x18, -10900, 2500, 27500, 270)
    SetChrPos(0x19, -9300, 2500, 24300, 225)
    SetChrPos(0x1A, -6300, 2500, 22950, 180)
    SetChrPos(0x1B, -3400, 2500, 23700, 135)
    Sound(868, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x4)
    SetChrPos(0x8, -5500, 2500, 35800, 180)
    SetChrPos(0x9, -4500, 2500, 33800, 0)
    SetChrPos(0xA, -5500, 2500, 33800, 0)
    SetChrPos(0xB, -6500, 2500, 33800, 0)
    SetChrPos(0xC, -4500, 2500, 31800, 0)
    SetChrPos(0xD, -5500, 2500, 31800, 0)
    SetChrPos(0xE, -6500, 2500, 31800, 0)
    SetChrPos(0xF, -4500, 2500, 29800, 0)
    SetChrPos(0x10, -5500, 2500, 29800, 0)
    SetChrPos(0x11, -6500, 2500, 29800, 0)
    SetChrPos(0x12, -4500, 2500, 27800, 0)
    SetChrPos(0x13, -5500, 2500, 27800, 0)
    SetChrPos(0x14, -6500, 2500, 27800, 0)
    SetChrPos(0x15, -4500, 2500, 25800, 0)
    SetChrPos(0x16, -5500, 2500, 25800, 0)
    SetChrPos(0x17, -6500, 2500, 25800, 0)
    Sound(865, 2, 70, 0)
    Sound(861, 2, 70, 0)
    Sound(863, 2, 100, 0)
    BeginChrThread(0x18, 0, 0, 3)
    BeginChrThread(0x18, 3, 0, 4)
    BeginChrThread(0x19, 0, 0, 3)
    BeginChrThread(0x19, 3, 0, 4)
    BeginChrThread(0x1A, 0, 0, 3)
    BeginChrThread(0x1A, 3, 0, 4)
    BeginChrThread(0x1B, 0, 0, 3)
    BeginChrThread(0x1B, 3, 0, 4)
    OP_68(-5500, 3500, 27000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(-6500, 3500, 25000, 4000)
    SetCameraDistance(17500, 4000)
    OP_0D()
    SetChrChipByIndex(0x8, 0x24)
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_AA3():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AA3)
    Sleep(50)
    SetChrChipByIndex(0x9, 0x24)
    SetChrChipByIndex(0xA, 0x24)
    SetChrChipByIndex(0xB, 0x24)

    def lambda_AC7():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AC7)

    def lambda_ADC():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_ADC)

    def lambda_AF1():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AF1)
    Sleep(50)
    SetChrChipByIndex(0xC, 0x24)
    SetChrChipByIndex(0xD, 0x24)
    SetChrChipByIndex(0xE, 0x24)

    def lambda_B15():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B15)

    def lambda_B2A():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B2A)

    def lambda_B3F():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B3F)
    Sleep(50)
    SetChrChipByIndex(0xF, 0x24)
    SetChrChipByIndex(0x10, 0x24)
    SetChrChipByIndex(0x11, 0x24)

    def lambda_B63():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B63)

    def lambda_B78():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B78)

    def lambda_B8D():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B8D)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x29)
    SetChrChipByIndex(0x13, 0x29)
    SetChrChipByIndex(0x14, 0x29)

    def lambda_BB1():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BB1)

    def lambda_BC6():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BC6)

    def lambda_BDB():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BDB)
    Sleep(50)
    SetChrChipByIndex(0x15, 0x29)
    SetChrChipByIndex(0x16, 0x29)
    SetChrChipByIndex(0x17, 0x29)

    def lambda_BFF():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BFF)

    def lambda_C14():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C14)

    def lambda_C29():
        OP_9B(0x1, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_C29)
    OP_6F(0x79)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    StopSound(865, 300, 60)
    StopSound(861, 300, 60)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1B, 0x3)
    Fade(500)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    BeginChrThread(0x8, 3, 0, 5)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 5)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x1)
    SetChrChipByIndex(0xB, 0x25)
    SetChrSubChip(0xB, 0x1)
    SetChrChipByIndex(0xC, 0x25)
    SetChrSubChip(0xC, 0x1)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x1)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x1)
    SetChrPos(0x8, -16750, 2500, 28750, 0)
    SetChrPos(0x9, -18250, 2500, 28750, 0)
    SetChrPos(0xA, -18000, 2500, 26000, 0)
    SetChrPos(0xB, -17250, 2500, 24000, 0)
    SetChrPos(0xC, -18750, 2500, 24000, 0)
    SetChrPos(0xD, -17250, 2500, 22000, 0)
    SetChrPos(0xE, -18750, 2500, 22000, 0)
    OP_68(-18000, 3500, 26000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(-18000, 3500, 30000, 8000)
    MoveCamera(45, 30, 0, 8000)
    OP_6E(500, 8000)
    SetCameraDistance(16500, 8000)
    Sleep(7000)
    StopSound(863, 1000, 90)
    StopSound(868, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x361)
    OP_24(0x35D)
    SetScenarioFlags(0x22, 0)
    NewScene("c115D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_545 end

    def Function_3_E24(): pass

    label("Function_3_E24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E73")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_3_E24")

    label("loc_E73")

    Return()

    # Function_3_E24 end

    def Function_4_E74(): pass

    label("Function_4_E74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EA7")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E9B")
    OP_4C(0xFE, 0x0)
    Jump("loc_E9F")

    label("loc_E9B")

    OP_4B(0xFE, 0x0)

    label("loc_E9F")

    Sleep(500)
    Jump("Function_4_E74")

    label("loc_EA7")

    Return()

    # Function_4_E74 end

    def Function_5_EA8(): pass

    label("Function_5_EA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F7D")
    SetChrChipByIndex(0xFE, 0x2A)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)
    Sleep(300)

    def lambda_EC7():
        OP_9B(0x1, 0xFE, 0x0, 0xFA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EC7)
    Sound(538, 0, 60, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(880, 0, 80, 0)
    Sound(196, 0, 50, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x5, -750, 1200, 1000, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x1388, 0x0)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F75")
    Sleep(1000)
    Jump("loc_F78")

    label("loc_F75")

    Sleep(500)

    label("loc_F78")

    Jump("Function_5_EA8")

    label("loc_F7D")

    Return()

    # Function_5_EA8 end

    SaveToFile()

Try(main)
