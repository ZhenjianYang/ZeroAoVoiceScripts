from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c130b.bin",                # FileName
        "c130b",                    # MapName
        "c130b",                    # Location
        0x001B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 0, 0, 1],
    )

    BuildStringList((
        "c130b",                  # 0
        "战鬼西格蒙德",           # 1
        "警备员珀尔",             # 2
        "接待小姐兰菲",           # 3
        "罗伯兹主任",             # 4
        "约纳",                   # 5
        "警备员比尔斯",           # 6
        "警备员汪古",             # 7
        "研究员库雷",             # 8
        "研究员达比德",           # 9
        "贸易商利泽罗",           # 10
        "ＩＢＣ顾客Ａ",           # 11
        "bc130b",                 # 12
        "中央广场",               # 13
        "西街",                   # 14
        "行政区",                 # 15
        "住宅街",                 # 16
        "欢乐街",                 # 17
        "东街",                   # 18
        "旧城区",                 # 19
        "港湾区",                 # 20
        "ＩＢＣ",                 # 21
        "站前街道",               # 22
        "后巷",                   # 23
        "乌尔斯拉间道",           # 24
        "东克洛斯贝尔街道",       # 25
        "西克洛斯贝尔街道",       # 26
        "玛因兹山道",             # 27
        "兰花塔",                 # 28
    ))

    ATBonus("ATBonus_508", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_5E8", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_604", 0, 0, 180)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_608", 0x1142, 0, 6, 0, 0, 255, 0, 0, "bc130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E8", "MonsterBattlePostion_5E8", "ed7586", "ed7453", "ATBonus_508"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch03350.itc",                   # 00
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
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
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

    DeclEvent(0x0000, 0, 5,   0.0,                   -45.0,                 -5.0,                  625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  9.0,                   1.0,                   1.0])

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "中央广场")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "西街")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "行政区")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "住宅街")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "欢乐街")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "东街")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "旧城区")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "站前街道")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "后巷")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-107.0, 0.0, 114.0, 0x0000, 0x0000, "兰花塔")
    PlaceName(-163.66000366210938, 0.0, -206.52999877929688, 0x0000, 0x0051, "")
    PlaceName(-90.51000213623047, 0.0, -171.14999389648438, 0x0000, 0x0054, "")
    PlaceName(-130.32000732421875, 0.0, -217.4199981689453, 0x0000, 0x0057, "")
    PlaceName(-164.67999267578125, 0.0, -167.05999755859375, 0x0000, 0x0053, "")
    PlaceName(-136.77999877929688, 0.0, -134.39999389648438, 0x0000, 0x0053, "")
    PlaceName(-205.85000610351562, 0.0, -173.8699951171875, 0x0000, 0x0053, "")
    PlaceName(-219.1199951171875, 0.0, -145.2899932861328, 0x0000, 0x0053, "")
    PlaceName(-186.4600067138672, 0.0, -101.7300033569336, 0x0000, 0x0052, "")
    PlaceName(-179.99000549316406, 0.0, -119.43000030517578, 0x0000, 0x0053, "")
    PlaceName(-168.0800018310547, 0.0, -131.0, 0x0000, 0x0053, "")
    PlaceName(-129.3000030517578, 0.0, -34.369998931884766, 0x0000, 0x0051, "")
    PlaceName(23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0052, "")
    PlaceName(0.0, 0.0, -341.95001220703125, 0x0000, 0x0053, "")
    PlaceName(-17.690000534057617, 0.0, -316.7699890136719, 0x0000, 0x0053, "")

    ChipFrameInfo(1648, 0)                                       # 0

    ScpFunction((
        "Function_0_670",          # 00, 0
        "Function_1_69A",          # 01, 1
        "Function_2_6F9",          # 02, 2
        "Function_3_9F2",          # 03, 3
        "Function_4_A26",          # 04, 4
        "Function_5_A5A",          # 05, 5
        "Function_6_15CE",         # 06, 6
        "Function_7_16D5",         # 07, 7
        "Function_8_21F1",         # 08, 8
    ))


    def Function_0_670(): pass

    label("Function_0_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_684")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_699")

    label("loc_684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_699")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 6)

    label("loc_699")

    Return()

    # Function_0_670 end

    def Function_1_69A(): pass

    label("Function_1_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6AF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_6AF")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D0")
    ModifyEventFlags(1, 0, 0x80)
    OP_7D(0xFF, 0xDC, 0xD2, 0x0, 0x0)

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6E4")
    OP_24(0x364)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_6F8")

    label("loc_6E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F8")
    Sound(868, 1, 40, 0)

    label("loc_6F8")

    Return()

    # Function_1_69A end

    def Function_2_6F9(): pass

    label("Function_2_6F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xDC, 0xD2, 0x0, 0x0)
    LoadChrToIndex("chr/ch27700.itc", 0x1E)
    LoadChrToIndex("chr/ch32800.itc", 0x1F)
    LoadChrToIndex("chr/ch28100.itc", 0x20)
    LoadChrToIndex("chr/ch29400.itc", 0x21)
    LoadChrToIndex("chr/ch28600.itc", 0x22)
    LoadChrToIndex("chr/ch27900.itc", 0x23)
    LoadChrToIndex("chr/ch29300.itc", 0x24)
    LoadChrToIndex("chr/ch06100.itc", 0x25)
    SetChrPos(0x0, 5000, 400, 12500, 0)
    SetChrPos(0x1, 5000, 400, 12500, 0)
    SetChrPos(0x2, 5000, 400, 12500, 0)
    SetChrPos(0x3, 5000, 400, 12500, 0)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -1000, 400, -30000, 180)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    OP_90(0xA, 1700, 400, -30000, 180)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    OP_90(0xB, 300, 400, -30000, 180)
    SetChrChipByIndex(0xC, 0x25)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    OP_90(0xC, -1000, 400, -30000, 180)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    OP_90(0xD, 2200, 400, -30000, 180)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    OP_90(0xE, 700, 400, -30000, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x4)
    OP_90(0xF, 1200, 400, -30000, 180)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    OP_90(0x10, -1600, 400, -30000, 180)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    OP_90(0x11, -2000, 400, -30000, 180)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    OP_90(0x12, 0, 400, -30000, 180)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    SetMapObjFlags(0xC, 0x1000)
    OP_68(0, -5100, -50000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21000, 0)
    OP_68(0, -9100, -72000, 13000)
    MoveCamera(35, 15, 0, 13000)
    SetCameraDistance(17000, 13000)
    FadeToBright(1000, 0)
    BeginChrThread(0x12, 3, 0, 3)
    Sleep(250)
    BeginChrThread(0xD, 3, 0, 3)
    Sleep(150)
    BeginChrThread(0x11, 3, 0, 3)
    Sleep(250)
    BeginChrThread(0xF, 3, 0, 3)
    Sleep(150)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(250)
    BeginChrThread(0xE, 3, 0, 3)
    Sleep(150)
    BeginChrThread(0x10, 3, 0, 3)
    Sleep(250)
    BeginChrThread(0xA, 3, 0, 3)
    Sleep(2500)
    BeginChrThread(0xB, 3, 0, 3)
    Sleep(150)
    BeginChrThread(0xC, 3, 0, 4)
    Sleep(7900)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 3)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_6F9 end

    def Function_3_9F2(): pass

    label("Function_3_9F2")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_A09():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF2928, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A09)
    WaitChrThread(0xFE, 1)
    OP_64(0xFE)
    Return()

    # Function_3_9F2 end

    def Function_4_A26(): pass

    label("Function_4_A26")

    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_A3D():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF2928, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3D)
    WaitChrThread(0xFE, 1)
    OP_64(0xFE)
    Return()

    # Function_4_A26 end

    def Function_5_A5A(): pass

    label("Function_5_A5A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    LoadChrToIndex("chr/ch03354.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    LoadEffect(0x0, "event\\ev17001.eff")
    SoundLoad(825)
    SoundLoad(256)
    SoundLoad(881)
    SoundLoad(3856)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, -27000, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_90(0x101, 1100, -1000, -59200, 0)
    OP_90(0x102, -1100, -1000, -59500, 0)
    OP_90(0x103, 2000, -1000, -60000, 0)
    OP_90(0x104, -100, -1000, -58500, 0)
    OP_90(0x109, -2000, -1000, -60000, 0)
    OP_90(0x105, 100, -1000, -60500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    SetMapObjFlags(0xC, 0x1000)
    OP_68(0, -4000, -50000, 0)
    MoveCamera(45, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    StopSound(868, 2000, 40)
    StopBGM(0x1388)

    def lambda_BF3():
        OP_97(0x104, 0x0, 0x0, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BF3)
    Sleep(100)

    def lambda_C10():
        OP_97(0x101, 0x0, 0x0, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C10)
    Sleep(100)

    def lambda_C2D():
        OP_97(0x102, 0x0, 0x0, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C2D)
    Sleep(100)

    def lambda_C4A():
        OP_97(0x103, 0x0, 0x0, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C4A)
    Sleep(100)

    def lambda_C67():
        OP_97(0x109, 0x0, 0x0, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C67)
    Sleep(100)

    def lambda_C84():
        OP_97(0x105, 0x0, 0x0, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C84)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(0, 900, -27000, 4000)
    MoveCamera(30, 15, 0, 4000)
    SetCameraDistance(14500, 4000)
    Sleep(3000)
    OP_4B(0x104, 0xFF)
    OP_4B(0x101, 0xFF)
    OP_4B(0x102, 0xFF)
    OP_4B(0x103, 0xFF)
    OP_4B(0x109, 0xFF)
    OP_4B(0x105, 0xFF)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    Fade(1000)
    OP_68(0, 3900, -27000, 0)
    MoveCamera(0, 3, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    OP_68(0, 1900, -27000, 4000)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0001
    AnonymousTalk(
        0x8,
        (
            "#3856V#40W呵呵，\x01",
            "你们来得\x01",
            "正是时候。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF10)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_68(0, 900, -32000, 2000)
    MoveCamera(0, 5, 0, 2000)
    SetCameraDistance(16500, 2000)
    Sleep(1000)
    OP_4C(0x104, 0xFF)
    OP_4C(0x101, 0xFF)
    OP_4C(0x102, 0xFF)
    OP_4C(0x103, 0xFF)
    OP_4C(0x109, 0xFF)
    OP_4C(0x105, 0xFF)
    OP_6F(0x79)
    WaitChrThread(0x105, 0)

    #C0002
    ChrTalk(
        0x104,
        "#6P#00311F叔叔，你……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#12P#N#00006F西格蒙德·奥兰多……\x01",
            "你到底有什么目的？\x02\x03",

            "#00010F在克洛斯贝尔市做出这种事！\x01",
            "蹂躏着无辜的市民……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0004
    ChrTalk(
        0x102,
        (
            "#6P#N#00107F难、难道说，这也是受\x01",
            "帝国政府指使的吗……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0005
    ChrTalk(
        0x8,
        (
            "#04504F#5P哼哼，我不是早就说过吗？\x01",
            "契约方面的事情无可奉告。\x02\x03",

            "#04500F话说回来，兰道夫……\x01",
            "你的『狂战士』怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#6P#00306F……好不容易才完成维护，\x01",
            "却又被你女儿弄坏了。\x02\x03",

            "#00311F不过就算没有它，\x01",
            "我也要在这里阻止你……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FE5():
        OP_98(0xFE, 0x0, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FE5)

    def lambda_FFF():

        label("loc_FFF")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_FFF")

    QueueWorkItem2(0x101, 2, lambda_FFF)

    def lambda_1011():

        label("loc_1011")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_1011")

    QueueWorkItem2(0x102, 2, lambda_1011)
    Sleep(50)

    def lambda_1026():

        label("loc_1026")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_1026")

    QueueWorkItem2(0x103, 2, lambda_1026)

    def lambda_1038():

        label("loc_1038")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_1038")

    QueueWorkItem2(0x109, 2, lambda_1038)
    WaitChrThread(0x104, 1)
    Sleep(300)

    #C0007
    ChrTalk(
        0x104,
        (
            "#6P#00303F不是以『赤色死神』\x01",
            "或『斗神之子』的身份……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetCameraDistance(15500, 500)
    Sleep(50)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    OP_0D()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0008
    ChrTalk(
        0x104,
        (
            "#00307F#6P#4S而是作为特别任务支援科的成员——\x01",
            "兰迪·奥兰多！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    #C0009
    ChrTalk(
        0x101,
        "#00000F兰迪……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        "#00202F……兰迪前辈。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#04504F#5P哼哼，最终选择抵抗吗？\x02\x03",

            "#04501F那么，就让我看看\x01",
            "配得上这句话的证据……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_11A0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11A0)

    def lambda_11AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11AD)

    def lambda_11BA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11BA)

    def lambda_11C7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11C7)
    Fade(500)
    OP_68(0, 1200, -27000, 0)
    MoveCamera(47, 25, -15, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x3)
    Sound(802, 0, 100, 0)
    MoveCamera(30, 25, 7, 4500)
    SetCameraDistance(13000, 4500)
    OP_82(0x64, 0x64, 0xBB8, 0x1194)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sound(256, 0, 80, 0)
    Sound(881, 0, 60, 0)
    Sound(825, 2, 100, 0)

    #C0012
    ChrTalk(
        0x8,
        "#04507F#5P#30A#5S试着打倒我『赤色战鬼』……\x02",
    )
    #Auto

    Sleep(4000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    SetCameraDistance(17000, 1000)
    OP_82(0x190, 0x190, 0xBB8, 0x3E8)
    SetChrSubChip(0x8, 0x4)
    Sound(802, 0, 100, 0)
    Sound(531, 0, 50, 0)
    Sound(358, 0, 80, 0)
    Sound(256, 0, 80, 0)

    #C0013
    ChrTalk(
        0x8,
        "#04512F#5S#25A西格蒙德吧！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(0, 900, -28700, 0)
    MoveCamera(33, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    CancelBlur(0)
    OP_90(0x104, 0, -1000, -33700, 0)
    BeginChrThread(0x8, 3, 0, 8)
    OP_68(0, 200, -31700, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_138A():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC7C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_138A)
    Sleep(50)

    def lambda_13A7():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC7C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13A7)
    Sleep(50)

    def lambda_13C4():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFAEC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13C4)
    Sleep(50)

    def lambda_13E1():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFAEC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13E1)
    Sleep(50)

    def lambda_13FE():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13FE)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x105, 1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)

    #C0014
    ChrTalk(
        0x104,
        "#12P#00310F啧……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        "#12P#N#10110F好、好惊人的斗气……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0016
    ChrTalk(
        0x105,
        "#12P#N#10310F……他真的是人类吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    Sleep(300)

    #C0017
    ChrTalk(
        0x8,
        (
            "#04504F#5P#N哼哼，你们要是有足够的实力，\x01",
            "我也可以就此离开……\x02\x03",

            "#04502F但我们的工作还很忙。\x02\x03",

            "就定个时间限制吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    #C0018
    ChrTalk(
        0x101,
        "#12P#00010F唔，他想做什么……！？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#12P#00307F虽然不太清楚……\x01",
            "但只能拼尽全力了！！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Battle("BattleInfo_608", 0x0, 0x0, 0x100, 0x3E, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 7)
    Return()

    # Function_5_A5A end

    def Function_6_15CE(): pass

    label("Function_6_15CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "限制时间内取得胜利\x01",        # 0
            "削减对方５０％ＨＰ\x01",        # 1
            "削减对方２５％ＨＰ\x01",        # 2
            "削减对方１０％ＨＰ\x01",        # 3
            "未满足条件，时间结束\x01",      # 4
            "战败\x01",                      # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_167D"),
        (1, "loc_168B"),
        (2, "loc_1699"),
        (3, "loc_16A7"),
        (4, "loc_16B5"),
        (5, "loc_16C3"),
        (SWITCH_DEFAULT, "loc_16D1"),
    )


    label("loc_167D")

    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16D1")

    label("loc_168B")

    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16D1")

    label("loc_1699")

    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16D1")

    label("loc_16A7")

    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16D1")

    label("loc_16B5")

    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16D1")

    label("loc_16C3")

    OP_50(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16D1")

    label("loc_16D1")

    Call(0, 7)
    Return()

    # Function_6_15CE end

    def Function_7_16D5(): pass

    label("Function_7_16D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03354.itc", 0x1E)
    LoadChrToIndex("chr/ch03353.itc", 0x25)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175C")
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x3)
    Jump("loc_193F")

    label("loc_175C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CB")
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Jump("loc_193F")

    label("loc_17CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1846")
    LoadChrToIndex("chr/ch00056.itc", 0x1F)
    LoadChrToIndex("chr/ch00156.itc", 0x20)
    LoadChrToIndex("chr/ch00256.itc", 0x21)
    LoadChrToIndex("chr/ch00356.itc", 0x22)
    LoadChrToIndex("chr/ch0295F.itc", 0x23)
    LoadChrToIndex("chr/ch0305F.itc", 0x24)
    LoadChrToIndex("chr/ch00050.itc", 0x26)
    LoadChrToIndex("chr/ch00350.itc", 0x27)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Jump("loc_193F")

    label("loc_1846")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B5")
    LoadChrToIndex("chr/ch00053.itc", 0x1F)
    LoadChrToIndex("chr/ch00153.itc", 0x20)
    LoadChrToIndex("chr/ch00253.itc", 0x21)
    LoadChrToIndex("chr/ch00353.itc", 0x22)
    LoadChrToIndex("chr/ch02953.itc", 0x23)
    LoadChrToIndex("chr/ch03053.itc", 0x24)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x3)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x3)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x3)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Jump("loc_193F")

    label("loc_18B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_193F")
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x4)
    LoadEffect(0x0, "event\\ev17001.eff")
    SoundLoad(825)

    label("loc_193F")

    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, -27000, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_90(0x101, 1100, -1000, -34000, 0)
    OP_90(0x102, -1100, -1000, -34000, 0)
    OP_90(0x103, 2000, -1000, -35000, 0)
    OP_90(0x104, 0, -1000, -32700, 0)
    OP_90(0x109, -2000, -1000, -35000, 0)
    OP_90(0x105, 0, -1000, -35500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    SetMapObjFlags(0xC, 0x1000)
    OP_68(0, 700, -30550, 0)
    MoveCamera(49, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A84")
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    BeginChrThread(0x8, 3, 0, 8)
    Sound(825, 2, 100, 0)

    label("loc_1A84")

    PlayBGM("ed7582", 0)
    SetCameraDistance(17000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C87")
    OP_2C(0xAB, 0x5)

    #C0020
    ChrTalk(
        0x8,
        (
            "#5P#04505F#30W……真让我吃惊。\x02\x03",

            "#04504F呵呵……\x01",
            "不愧是继承了\x01",
            "大哥血脉的人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        (
            "#12P#00306F哼……跟老爸没有关系。\x02\x03",

            "#00303F虽说你小看了我们，\x01",
            "过于手下留情……\x01",
            "但是胜负已分。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0022
    ChrTalk(
        0x104,
        "#12P#00307F#4S赶快给我离开这里！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#5P#04504F#30W呵……没问题。\x02\x03",

            "#04500F但得让我把生意上的事\x01",
            "办完才行……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        "#12P#00305F什么……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sound(802, 0, 100, 0)
    Sound(812, 0, 100, 0)
    Sound(531, 0, 50, 0)
    Sound(358, 0, 60, 0)
    Sleep(120)
    SetChrSubChip(0x8, 0x1)
    Sleep(60)
    Fade(120)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_68(0, 3300, -22550, 2000)
    MoveCamera(0, -3, 0, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)

    #C0025
    ChrTalk(
        0x8,
        "#04502F哈哈，时间到了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2158")

    label("loc_1C87")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D77")
    OP_2C(0xAB, 0x3)

    #C0026
    ChrTalk(
        0x8,
        (
            "#5P#04502F喔，还不错嘛。\x02\x03",

            "与同伴之间的配合\x01",
            "也还算合格。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#12P#00307F呼……\x01",
            "那当然！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#12P#00010F#N再加把劲，\x01",
            "大家一起上！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 3300, -22550, 2000)
    MoveCamera(0, -3, 0, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)

    #C0029
    ChrTalk(
        0x8,
        (
            "#04502F呵呵，可惜，\x01",
            "时间好像到了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2158")

    label("loc_1D77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED9")
    OP_2C(0xAB, 0x2)

    #C0030
    ChrTalk(
        0x8,
        (
            "#5P#04503F哼，勉强及格吧。\x02\x03",

            "#04500F虽然弱小，但这种不肯轻易罢手的毅力\x01",
            "还是值得表扬。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DE9():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DE9)
    Sleep(500)
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    #C0031
    ChrTalk(
        0x101,
        "#12P#00006F#N呼……呼……\x02",
    )

    CloseMessageWindow()

    def lambda_1E40():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1E40)
    Sleep(500)
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x27)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)

    #C0032
    ChrTalk(
        0x104,
        "#12P#00310F这个怪物……\x02",
    )

    CloseMessageWindow()
    OP_68(0, 3300, -22550, 2000)
    MoveCamera(0, -3, 0, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)

    #C0033
    ChrTalk(
        0x8,
        "#04502F好，时间到了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2158")

    label("loc_1ED9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2018")
    OP_2C(0xAB, 0x1)

    #C0034
    ChrTalk(
        0x8,
        (
            "#5P#04503F哼，不出所料……\x02\x03",

            "#04501F从谢莉的描述来估计，\x01",
            "本以为你们能多坚持一会。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F47():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F47)
    Sleep(500)

    #C0035
    ChrTalk(
        0x104,
        "#12P#00310F……可恶………\x02",
    )

    CloseMessageWindow()

    def lambda_1F82():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F82)
    Sleep(500)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00006F#12P#N……不行了……\x01",
            "以我们现在的实力……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 3300, -22550, 2000)
    MoveCamera(0, -3, 0, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)

    #C0037
    ChrTalk(
        0x8,
        "#04502F好，时间到了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2158")

    label("loc_2018")


    #C0038
    ChrTalk(
        0x8,
        (
            "#5P#04507F#30W……你们……\x01",
            "到底想不想打啊？\x02\x03",

            "像稻草人一样站在那里，\x01",
            "信不信我把你们一起砍了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#12P#00011F#N呜……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0040
    ChrTalk(
        0x104,
        "#12P#00306F好像惹他生气了……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0xFF)
    StopSound(825, 1000, 100)
    StopEffect(0x0, 0x2)
    OP_89(0x0, 0x0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)

    #C0041
    ChrTalk(
        0x8,
        "#5P#04504F哼，也罢。\x02",
    )

    CloseMessageWindow()
    OP_68(0, 3300, -22550, 2000)
    MoveCamera(0, -3, 0, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)

    #C0042
    ChrTalk(
        0x8,
        (
            "#04502F你们就呆站在那里，\x01",
            "欣赏无所作为的代价吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2158")

    StopBGM(0xDAC)
    ReplaceBGM(-1, -1)
    OP_68(0, 6300, -22550, 4000)
    MoveCamera(0, -13, 0, 4000)
    SetCameraDistance(14000, 4000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x339)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_03a.pmf", 0x227, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    SetScenarioFlags(0x22, 0)
    NewScene("e3900", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_16D5 end

    def Function_8_21F1(): pass

    label("Function_8_21F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2215")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_8_21F1")

    label("loc_2215")

    Return()

    # Function_8_21F1 end

    SaveToFile()

Try(main)
