from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m2060.bin",                # FileName
        "m2060",                    # MapName
        "m2060",                    # Location
        0x0079,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 121, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2060",                  # 0
        "小丑肯帕雷拉",           # 1
        "弓箭少女恩奈雅",         # 2
        "SE控制",                 # 3
        "bm2060",                 # 4
    ))

    ATBonus("ATBonus_118", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_1D8", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1B8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1BC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1C0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_1C4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_1C8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_1CC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_1D0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D4", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_1F8", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03600.dat", 0, 0, 0, 0, 0, "ms86300.dat", 0, "MonsterBattlePostion_1D8", "MonsterBattlePostion_1B8", "ed7458", "ed7453", "ATBonus_118"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(632, 0)                                        # 0

    ScpFunction((
        "Function_0_278",          # 00, 0
        "Function_1_2C9",          # 01, 1
        "Function_2_496",          # 02, 2
        "Function_3_68F",          # 03, 3
        "Function_4_6B4",          # 04, 4
        "Function_5_6D9",          # 05, 5
        "Function_6_1442",         # 06, 6
        "Function_7_14A1",         # 07, 7
        "Function_8_14DD",         # 08, 8
        "Function_9_277A",         # 09, 9
        "Function_10_27A1",        # 0A, 10
        "Function_11_27D2",        # 0B, 11
        "Function_12_35BE",        # 0C, 12
        "Function_13_3679",        # 0D, 13
        "Function_14_36A2",        # 0E, 14
    ))


    def Function_0_278(): pass

    label("Function_0_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2A2")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_2C8")

    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_2B9")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 8)
    Jump("loc_2C8")

    label("loc_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_2C8")
    ClearScenarioFlags(0x22, 2)
    Event(0, 11)

    label("loc_2C8")

    Return()

    # Function_0_278 end

    def Function_1_2C9(): pass

    label("Function_1_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2E3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_328")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 0)), scpexpr(EXPR_END)), "loc_2FA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_328")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_316")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_328")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_328")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_36B")
    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)
    Jump("loc_406")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C8")
    LoadEffect(0x9, "map/mpbell02.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 22000, 10500, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    Jump("loc_406")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 0)), scpexpr(EXPR_END)), "loc_406")
    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)

    label("loc_406")

    OP_11(0x7B, 0xB4, 0xD5, 0x19, 0x384, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_438")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x19, 0x12C, 0x0)

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_454")
    Sound(828, 1, 70, 0)
    OP_24(0x84)
    Jump("loc_495")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_470")
    Sound(828, 1, 100, 0)
    OP_24(0x84)
    Jump("loc_495")

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48C")
    Sound(828, 1, 70, 0)
    OP_24(0x84)
    Jump("loc_495")

    label("loc_48C")

    OP_24(0x33C)
    Sound(132, 1, 70, 0)

    label("loc_495")

    Return()

    # Function_1_2C9 end

    def Function_2_496(): pass

    label("Function_2_496")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("chr/ch43300.itc", 0x1F)
    LoadEffect(0x0, "battle/cr037100.eff")
    LoadEffect(0x1, "map/mpbell.eff")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 15760, 7750, 100, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 15370, 7750, -1000, 45)
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)
    StopEffect(0x7, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 22000, 10500, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    OP_68(22000, 9700, 0, 0)
    MoveCamera(60, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(46500, 0)
    FadeToBright(1000, 0)
    OP_68(22000, 10000, 0, 7000)
    MoveCamera(90, 5, 0, 7000)
    SetCameraDistance(17750, 7000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    SetCameraDistance(28000, 10000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x19)
    Sleep(1)
    CancelBlur(4000)
    Sound(929, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 3)
    SetMapObjFrame(0x0, "root", 0x2, "move")
    SetMapObjFrame(0x0, "model02", 0x1, 0x1)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 22000, 10500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Sound(829, 0, 100, 0)
    Sleep(4000)
    StopSound(828, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m0011", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_496 end

    def Function_3_68F(): pass

    label("Function_3_68F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_3_68F")

    label("loc_6B3")

    Return()

    # Function_3_68F end

    def Function_4_6B4(): pass

    label("Function_4_6B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D8")
    OP_82(0x64, 0x64, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_4_6B4")

    label("loc_6D8")

    Return()

    # Function_4_6B4 end

    def Function_5_6D9(): pass

    label("Function_5_6D9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("apl/ch51416.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00150.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00350.itc", 0x23)
    SoundLoad(961)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_724")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_724")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73C")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_73C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_754")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_754")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76C")
    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_76C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_784")
    LoadChrToIndex("chr/ch03150.itc", 0x25)

    label("loc_784")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79C")
    LoadChrToIndex("chr/ch03250.itc", 0x25)

    label("loc_79C")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04801.itp")
    LoadEffect(0x0, "battle\\cr036301.eff")
    SoundLoad(3724)
    SoundLoad(3725)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, -1290, 8000, -60, 90)
    OP_90(0x102, -1940, 8000, 680, 90)
    OP_90(0x103, -2200, 8000, -530, 90)
    OP_90(0x104, -2900, 8000, 140, 90)
    OP_90(0xF4, -3090, 8000, -950, 90)
    OP_90(0xF5, -3460, 8000, 1140, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 16000, 7750, 0, 270)
    SetMapObjFlags(0x0, 0x1000)
    StopBGM(0xBB8)
    OP_68(0, 1960, 0, 0)
    OP_68(5880, 4940, 0, 2500)
    MoveCamera(57, 26, 0, 0)
    MoveCamera(57, 15, 0, 2500)
    OP_6E(650, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(15000, 2500)
    FadeToBright(1000, 0)

    def lambda_917():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_917)
    Sleep(30)

    def lambda_92F():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_92F)
    Sleep(30)

    def lambda_947():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_947)
    Sleep(30)

    def lambda_95F():
        OP_9B(0x0, 0x104, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_95F)
    Sleep(30)

    def lambda_977():
        OP_9B(0x0, 0xF4, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_977)
    Sleep(30)

    def lambda_98F():
        OP_9B(0x0, 0xF5, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_98F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_0D()
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(16750, 9700, 0, 2500)
    MoveCamera(63, 0, 0, 2500)
    OP_6E(650, 2500)
    SetCameraDistance(12800, 2500)
    OP_6F(0x79)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7584", 0)
    OP_68(8050, 8400, -320, 2500)
    MoveCamera(90, 3, 0, 2500)
    OP_6E(650, 2500)
    SetCameraDistance(11030, 2500)
    Sleep(700)

    def lambda_AC4():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AC4)
    Sleep(30)

    def lambda_ADC():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ADC)
    Sleep(30)

    def lambda_AF4():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AF4)
    Sleep(30)

    def lambda_B0C():
        OP_9B(0x0, 0x104, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B0C)
    Sleep(30)

    def lambda_B24():
        OP_9B(0x0, 0xF4, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B24)
    Sleep(30)

    def lambda_B3C():
        OP_9B(0x0, 0xF5, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B3C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0001
    AnonymousTalk(
        0x8,
        (
            "呵呵，辛苦了。\x02\x03",

            "『迷宫探索』和『寻宝』……\x02\x03",

            "偶尔体验一下这种\x01",
            "经典设计也不错吧？\x02",
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

    #C0002
    ChrTalk(
        0x101,
        "#00006F#6P果然是你干的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0003
    ChrTalk(
        0x104,
        (
            "#00312F#6P#N你让我们陪你玩了个\x01",
            "相当麻烦的游戏呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0004
    ChrTalk(
        0x8,
        (
            "#04802F#11P呵呵，要是毫无挑战性，\x01",
            "你们也很难玩得开心吧？\x02\x03",

            "#04809F希望你们能把这场游戏当作\x01",
            "小丑为你们提供的趣味服务⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        "#00211F#6P#N这种游戏无聊至极……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA1")

    #C0006
    ChrTalk(
        0x109,
        (
            "#10106F#6P#N话说回来……\x02\x03",

            "#10108F从你的外表来看，\x01",
            "实在不像是可以\x01",
            "加入『结社』的年纪……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF9")

    label("loc_DA1")


    #C0007
    ChrTalk(
        0x106,
        (
            "#10703F#6P#N话说回来……\x02\x03",

            "#10701F看你的外貌，实在不像是\x01",
            "可以加入『结社』的年龄啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF9")

    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x102,
        (
            "#00101F#6P#N说起来，似乎和\x01",
            "小玲的情况差不多吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0009
    ChrTalk(
        0x8,
        (
            "#04804F#11P呵呵，我和她不同，\x01",
            "我的外表与实际年龄并不一致。\x02\x03",

            "#04805F对了对了，\x01",
            "我有幸听到了\x01",
            "克洛斯贝尔独立无效宣言。\x02\x03",

            "#04802F虽然很有趣，\x01",
            "但这条路似乎会相当坎坷啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00013F#6P……我们早有心理准备了。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        (
            "#00103F#6P#N无论前方的道路上有多少困难……\x01",
            "在有些时候，也不得不\x01",
            "鼓起勇气去跨越。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0012
    ChrTalk(
        0x8,
        (
            "#04804F#11P呵呵，也罢。\x02\x03",

            "#04802F无论克洛斯贝尔如何，\x01",
            "都和我的使命无关。\x02\x03",

            "从这层意义上来说，\x01",
            "我本可以尽早撤退……\x02\x03",

            "#04809F不过，最后还是\x01",
            "表演一下压箱底的好戏吧。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(16000, 8500, 0, 1500)
    MoveCamera(60, 10, 0, 1500)
    OP_6E(650, 1500)
    SetCameraDistance(12000, 1500)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(250)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(500)
    Fade(500)
    StopSound(828, 1000, 60)
    BeginChrThread(0xA, 1, 0, 7)
    BeginChrThread(0x8, 3, 0, 6)
    OP_68(16000, 8500, 0, 0)
    MoveCamera(40, 40, 0, 0)
    MoveCamera(90, 15, 0, 8000)
    OP_6E(650, 0)
    SetCameraDistance(19550, 0)
    SetCameraDistance(12550, 8000)
    Sleep(1500)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1173")
    Sound(540, 0, 50, 0)

    label("loc_1173")

    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x24)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x25)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_0D()

    #C0013
    ChrTalk(
        0x101,
        "#00011F#3P#N这、这是……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x103,
        (
            "#00207F#3P#N幻术……不，\x01",
            "张开了特殊的相位空间！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_124C")

    #C0015
    ChrTalk(
        0x105,
        (
            "#10410F#6P#N想把我们关进\x01",
            "魔术结界中吗……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1276")

    label("loc_124C")


    #C0016
    ChrTalk(
        0x106,
        "#10707F#6P#N用方术制造的结界……！？\x02",
    )

    CloseMessageWindow()

    label("loc_1276")

    OP_57(0x0)
    OP_5A()
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7458", 0)

    #C0017
    ChrTalk(
        0x8,
        (
            "#04804F#11P#30W#64A呵呵，这个地方太小了，\x01",
            "我带你们去更宽敞一些的地方吧。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(16000, 8600, 0, 10000)
    MoveCamera(90, 10, 0, 10000)
    OP_6E(650, 10000)
    SetCameraDistance(10000, 10000)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0018
    AnonymousTalk(
        0x8,
        (
            "#3724V#43A#35W执行者Ｎｏ．０，\x01",
            "『小丑』肯帕雷拉。\x02\x03",

            "#3725V#34A#30W就在此决一死战吧——没那么严重啦¤\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)
    SetScenarioFlags(0x0, 0)
    StopSound(825, 500, 40)
    StopSound(961, 500, 60)
    Sleep(500)
    Sound(960, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    StopEffect(0x0, 0x2)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_1F8", 0x0, 0x0, 0x100, 0x3C, 0xFF)
    FadeToDark(0, 0, -1)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 8)
    Return()

    # Function_5_6D9 end

    def Function_6_1442(): pass

    label("Function_6_1442")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14A0")
    OP_82(0x28, 0x41, 0x1388, 0xFA)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 500, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    StopEffect(0x0, 0x2)
    Jump("Function_6_1442")

    label("loc_14A0")

    Return()

    # Function_6_1442 end

    def Function_7_14A1(): pass

    label("Function_7_14A1")

    Sound(961, 2, 20, 0)
    Sound(825, 2, 20, 0)
    Sleep(100)
    OP_25(0x3C1, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(100)
    OP_25(0x3C1, 0x28)
    OP_25(0x339, 0x28)
    Sleep(100)
    OP_25(0x3C1, 0x32)
    OP_25(0x339, 0x32)
    Sleep(100)
    OP_25(0x3C1, 0x3C)
    Sleep(100)
    OP_25(0x3C1, 0x46)
    Return()

    # Function_7_14A1 end

    def Function_8_14DD(): pass

    label("Function_8_14DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("apl/ch51416.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00150.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00350.itc", 0x23)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1525")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_1525")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_153D")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_153D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1555")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_1555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_156D")
    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_156D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1585")
    LoadChrToIndex("chr/ch03150.itc", 0x25)

    label("loc_1585")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_159D")
    LoadChrToIndex("chr/ch03250.itc", 0x25)

    label("loc_159D")

    LoadChrToIndex("chr/ch03653.itc", 0x26)
    LoadChrToIndex("chr/ch00001.itc", 0x27)
    LoadChrToIndex("chr/ch00301.itc", 0x28)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15CA")
    LoadChrToIndex("chr/ch02901.itc", 0x29)
    Jump("loc_15D0")

    label("loc_15CA")

    LoadChrToIndex("chr/ch03201.itc", 0x29)

    label("loc_15D0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04801.itp")
    LoadEffect(0x0, "event\\ev10002.eff")
    LoadEffect(0x1, "battle\\cr036301.eff")
    LoadEffect(0x2, "map/mpbell.eff")
    SoundLoad(959)
    SoundLoad(825)
    SoundLoad(132)
    SoundLoad(3726)
    SoundLoad(3727)
    SoundLoad(3728)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 11710, 8000, -60, 90)
    OP_90(0x102, 11060, 8000, 680, 90)
    OP_90(0x103, 10800, 8000, -530, 90)
    OP_90(0x104, 10100, 8000, 340, 90)
    OP_90(0xF4, 9910, 8000, -780, 90)
    OP_90(0xF5, 9540, 8000, 1140, 90)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x24)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x25)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 16000, 7750, 0, 270)
    SetMapObjFlags(0x0, 0x1000)
    PlayBGM("ed7584", 0)
    OP_68(14000, 8400, 0, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13750, 0)
    SetCameraDistance(10750, 0)
    SetCameraDistance(13750, 2500)
    Sound(202, 0, 100, 0)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 0, 2000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_82(0x32, 0x64, 0xBB8, 0x3E8)
    FadeToBright(1000, 0)
    Sleep(750)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    OP_0D()

    #C0019
    ChrTalk(
        0x8,
        (
            "#04806F#11P#30W呼，哎呀呀……\x02\x03",

            "#04801F果然还是不该做这种\x01",
            "自己不习惯的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00010F#6P#30W呼……呼……如何！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_187F")

    #C0021
    ChrTalk(
        0x105,
        (
            "#10401F#6P#N#30W可以算是\x01",
            "我们胜利了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AC")

    label("loc_187F")


    #C0022
    ChrTalk(
        0x106,
        (
            "#10701F#6P#N#30W可以算是\x01",
            "我们胜利了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AC")

    OP_57(0x0)
    OP_5A()
    OP_68(14250, 8400, 0, 1000)
    Sleep(250)

    def lambda_18C8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_18C8)
    Sleep(250)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    WaitChrThread(0x8, 2)
    OP_6F(0x79)
    Sleep(300)

    #C0023
    ChrTalk(
        0x8,
        (
            "#04804F#11P#30W……呵呵，没有异议。\x02\x03",

            "#04802F不过，我想你们是不可能\x01",
            "战胜『钢之圣女』的。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00013F#6P#30W唔……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0025
    ChrTalk(
        0x104,
        (
            "#00311F#6P#N#30W哼……\x01",
            "不用你多管闲事。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0026
    ChrTalk(
        0x8,
        (
            "#04804F#11P#30W呵呵，既然如此，\x01",
            "我就要离开克洛斯贝尔了。\x02\x03",

            "#04800F人类所创造的『至宝』的未来……\x02\x03",

            "#04802F虽然还想再多观察一下，\x01",
            "但帝国那边要忙起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#00108F#6P#N#30W『幻焰计划』……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ABE")

    #C0028
    ChrTalk(
        0x109,
        (
            "#10110F#6P#N这次你们打算\x01",
            "在埃雷波尼亚引发骚乱吗……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF5")

    label("loc_1ABE")


    #C0029
    ChrTalk(
        0x106,
        (
            "#10701F#6P#N这次你们打算\x01",
            "在埃雷波尼亚引发动乱吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF5")

    OP_57(0x0)
    OP_5A()

    #C0030
    ChrTalk(
        0x8,
        (
            "#04804F#11P呵呵，一切都是\x01",
            "伟大『盟主』的意志……\x02\x03",

            "#04800F然而，给出答案的始终都是\x01",
            "身处命运之中的人类之子呢。\x02\x03",

            "当然也包括你们在内。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#00005F#6P什么……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0032
    ChrTalk(
        0x103,
        "#00205F#6P#N……给出答案？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(16000, 8500, 0, 1500)
    MoveCamera(90, 15, 0, 1500)
    OP_6E(650, 1500)
    SetCameraDistance(14000, 1500)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(250)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(13000, 300)
    Sound(959, 2, 80, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    SetCameraDistance(12000, 15000)
    CancelBlur(1000)
    Sleep(500)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0033
    AnonymousTalk(
        0x8,
        (
            "#3726V#40W#40A呵呵……\x01",
            "如果运气好，我们就下次再见吧。\x02\x03",

            "#3727V#40A你们到底会给出\x01",
            "什么样的答案呢……\x02\x03",

            "#3728V#25A到时候可一定要告诉我哟¤\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(11250, 500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    StopSound(959, 1000, 70)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_6F(0x79)
    CancelBlur(1000)
    StopEffect(0x0, 0x2)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    StopBGM(0x1770)

    #C0034
    ChrTalk(
        0x103,
        "#00201F#12P#N#30W啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(15000, 7800, 0, 0)
    OP_68(13500, 7800, 0, 2500)
    MoveCamera(50, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16450, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EE7")
    Sound(540, 0, 50, 0)

    label("loc_1EE7")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00306F#5P啧……\x01",
            "直到最后，还要说些装腔作势的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#00108F#5P让我们给出答案……\x01",
            "他指的到底是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FDF")

    #C0037
    ChrTalk(
        0x105,
        (
            "#10403F#5P唔……\x02\x03",

            "#10400F算了，\x01",
            "我们还是先让钟的共鸣停下来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2035")

    label("loc_1FDF")


    #C0038
    ChrTalk(
        0x106,
        (
            "#10708F#5P………………………………\x02\x03",

            "#10701F……总之，\x01",
            "我们先让钟的共鸣停下来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2035")

    OP_93(0x101, 0x10E, 0x1F4)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00001F#11P是啊……\x01",
            "兰迪，来帮把手吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2099")

    #C0040
    ChrTalk(
        0x109,
        "#10101F#5P我也来帮忙。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20B5")

    label("loc_2099")


    #C0041
    ChrTalk(
        0x106,
        "#10703F#5P我也来帮忙。\x02",
    )

    CloseMessageWindow()

    label("loc_20B5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrChipByIndex(0x101, 0x27)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x1)
    SetChrPos(0x101, 21840, 7750, 2140, 180)
    SetChrPos(0x104, 21920, 7750, -1930, 0)
    SetChrPos(0x102, 17770, 7750, -2330, 45)
    SetChrPos(0x103, 19210, 7750, -3260, 45)
    BeginChrThread(0x101, 3, 0, 9)
    BeginChrThread(0x104, 3, 0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2190")
    SetChrChipByIndex(0x109, 0x29)
    SetChrSubChip(0x109, 0x1)
    SetChrPos(0x109, 20010, 7750, 30, 90)
    BeginChrThread(0x109, 3, 0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_217A")
    SetChrPos(0xF5, 20960, 7750, -4210, 0)
    Jump("loc_218B")

    label("loc_217A")

    SetChrPos(0xF4, 20960, 7750, -4210, 0)

    label("loc_218B")

    Jump("loc_21E8")

    label("loc_2190")

    SetChrChipByIndex(0x106, 0x29)
    SetChrSubChip(0x106, 0x1)
    SetChrPos(0x106, 20010, 7750, 30, 90)
    BeginChrThread(0x106, 3, 0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21D7")
    SetChrPos(0xF5, 20960, 7750, -4210, 0)
    Jump("loc_21E8")

    label("loc_21D7")

    SetChrPos(0xF4, 20960, 7750, -4210, 0)

    label("loc_21E8")

    StopEffect(0x7, 0x0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 22000, 10500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 2, 0, 4)
    BeginChrThread(0xA, 1, 0, 10)
    FadeToBright(1000, 0)
    OP_68(22000, 8500, 0, 0)
    OP_68(22000, 9500, 0, 6000)
    MoveCamera(110, 21, 0, 0)
    MoveCamera(75, 15, 0, 6000)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(15000, 6000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(22000, 9500, 0, 0)
    MoveCamera(90, 27, 0, 0)
    MoveCamera(90, 6, 0, 5000)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    OP_6F(0x79)
    Sleep(50)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetCameraDistance(36000, 1000)
    Sound(829, 0, 100, 0)
    StopSound(828, 2000, 60)
    StopSound(825, 2000, 60)
    FadeToDark(1000, 16777215, -1)
    Sleep(1000)
    OP_6F(0x1)
    CancelBlur(100)
    OP_0D()
    EndChrThread(0x101, 0x2)
    StopEffect(0x0, 0x0)
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x104, 0x3)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_234C")
    EndChrThread(0x109, 0x3)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2358")

    label("loc_234C")

    EndChrThread(0x106, 0x3)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    label("loc_2358")

    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x19, 0x12C, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    Sleep(500)
    Sound(132, 2, 70, 0)
    FadeToBright(2000, 16777215)
    OP_68(22000, 12500, 0, 0)
    OP_68(22000, 9500, 0, 6000)
    MoveCamera(67, 7, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34000, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_93(0x101, 0xE1, 0x0)
    OP_93(0x104, 0x13B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2431")
    OP_93(0x109, 0x2D, 0x0)
    Jump("loc_2438")

    label("loc_2431")

    OP_93(0x106, 0x2D, 0x0)

    label("loc_2438")

    OP_68(21400, 9150, 80, 0)
    OP_68(22400, 9150, 80, 3000)
    MoveCamera(89, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16320, 0)
    OP_6F(0x1)
    OP_0D()

    #C0042
    ChrTalk(
        0x102,
        "#00105F#11P停止了……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#00203F#11P……上级三属性\x01",
            "仍然在发挥作用……\x02\x03",

            "#00202F不过，和其它几口钟\x01",
            "的共鸣好像已经消失了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#00302F#11P既然如此，只要让『塔』上的钟\x01",
            "停止鸣响，就算万事大吉了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00004F#5P是啊，至少可以使\x01",
            "几口钟之间的共鸣停止。\x02\x03",

            "#00000F如果约鲁古大师说的没错，\x01",
            "到时应该就可以解除笼罩着\x01",
            "克洛斯贝尔市的结界了……\x02\x03",

            "#00007F我们走吧！去『星见之塔』！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2619")

    #C0046
    ChrTalk(
        0x109,
        "#10100F#11P明白！\x02",
    )

    CloseMessageWindow()

    label("loc_2619")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2642")

    #C0047
    ChrTalk(
        0x106,
        "#10702F#11P是……！\x02",
    )

    CloseMessageWindow()

    label("loc_2642")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_266F")

    #C0048
    ChrTalk(
        0x105,
        "#10402F#11PＯＫ，队长。\x02",
    )

    CloseMessageWindow()

    label("loc_266F")

    StopSound(132, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可以由乌尔斯拉间道中途\x01",
            "的岔路前往『星见之塔』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearMapObjFlags(0x0, 0x1000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_37()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2728")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2730")

    label("loc_2728")

    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    label("loc_2730")

    OP_90(0x0, 17280, 7750, 240, 280)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 5)
    OP_29(0xB0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    Sound(132, 2, 70, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_8_14DD end

    def Function_9_277A(): pass

    label("Function_9_277A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27A0")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(500)
    Jump("Function_9_277A")

    label("loc_27A0")

    Return()

    # Function_9_277A end

    def Function_10_27A1(): pass

    label("Function_10_27A1")

    Sound(825, 2, 10, 0)
    Sleep(200)
    OP_25(0x339, 0x14)
    Sleep(200)
    OP_25(0x339, 0x1E)
    Sleep(200)
    OP_25(0x339, 0x28)
    Sleep(200)
    OP_25(0x339, 0x32)
    Sleep(2000)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x46)
    Return()

    # Function_10_27A1 end

    def Function_11_27D2(): pass

    label("Function_11_27D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(132)
    SoundLoad(959)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("apl/ch51416.itc", 0x1F)
    LoadChrToIndex("apl/ch51257.itc", 0x20)
    LoadEffect(0x0, "event\\ev10002.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04801.itp")
    OP_68(21720, 6850, -210, 0)
    MoveCamera(91, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22260, 0)
    SetChrPos(0x101, 15890, 7750, 860, 90)
    SetChrPos(0x102, 15890, 7750, -720, 90)
    SetChrPos(0x103, 16140, 7750, 1880, 90)
    SetChrPos(0x104, 16140, 7750, -1890, 90)
    SetChrPos(0x109, 16140, 7750, 2860, 135)
    SetChrPos(0x105, 16149, 7750, -3080, 45)
    SetChrPos(0x18D, 16650, 7750, 90, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 14510, 8000, -30, 270)
    SetMapObjFlags(0x0, 0x1000)
    OP_68(21720, 9150, -210, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0050
    ChrTalk(
        0x18D,
        (
            "#12P#04400F这就是……\x01",
            "报告里提到的『钟』吧？\x02\x03",

            "#04403F和中央广场的钟\x01",
            "几乎一样啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x103,
        (
            "#6P#00200F敲响那口钟\x01",
            "所引发的某种『力场』\x01",
            "似乎笼罩着整个遗迹。\x02\x03",

            "#00206F之所以会出现类似于幽灵的东西，\x01",
            "恐怕也是出于这个原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#6P#00001F以前我们曾用强行按住\x01",
            "的方式停止了钟的共鸣。\x02\x03",

            "#00003F只要那样做，\x01",
            "就可以使大钟\x01",
            "散发的力场消失。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        (
            "#6P#10108F这么大的钟，\x01",
            "应该不可能\x01",
            "自己响起来……\x02\x03",

            "#10106F到底是谁敲响的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x18D,
        "#12P#04403F唔……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#6P#00001F……不管怎么说，\x01",
            "先让这口钟停下来吧。\x02\x03",

            "#00003F为了能静下心来好好说话，\x01",
            "还是先将魔物的威胁\x01",
            "消除为好。\x02\x03",

            "#00000F……兰迪，瓦吉，\x01",
            "能不能帮我一把？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，没问题，\x01",
            "不过这方法还真是原始啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#12P#00301F别啰嗦啦，\x01",
            "赶快按住它吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x18D,
        (
            "#12P#04403F不……\x01",
            "光是这样还不够。\x02\x03",

            "#04402F请各位稍微退后。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C4F():

        label("loc_2C4F")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2C4F")

    QueueWorkItem2(0x101, 1, lambda_2C4F)
    Sleep(50)

    def lambda_2C64():

        label("loc_2C64")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2C64")

    QueueWorkItem2(0x102, 1, lambda_2C64)
    Sleep(50)

    def lambda_2C79():

        label("loc_2C79")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2C79")

    QueueWorkItem2(0x103, 1, lambda_2C79)
    Sleep(50)

    def lambda_2C8E():

        label("loc_2C8E")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2C8E")

    QueueWorkItem2(0x104, 1, lambda_2C8E)
    Sleep(50)

    def lambda_2CA3():

        label("loc_2CA3")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2CA3")

    QueueWorkItem2(0x109, 1, lambda_2CA3)
    Sleep(50)

    def lambda_2CB8():

        label("loc_2CB8")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2CB8")

    QueueWorkItem2(0x105, 1, lambda_2CB8)
    Sleep(300)

    #C0059
    ChrTalk(
        0x101,
        "#6P#00005F咦……\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x18D, 0x0, 0x5DC, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    BeginChrThread(0x18D, 3, 0, 12)
    WaitChrThread(0x18D, 3)
    StopSound(828, 4000, 60)
    StopBGM(0xFA0)
    Sound(829, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetCameraDistance(39080, 1000)
    FadeToDark(1000, 16777215, -1)
    Sleep(1000)
    OP_6F(0x1)
    CancelBlur(100)
    OP_0D()
    Sleep(2000)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    PlayBGM("ed7304", 0)
    Sound(132, 2, 70, 0)
    SetChrChipByIndex(0x18D, 0xFF)
    SetChrSubChip(0x18D, 0x0)
    StopEffect(0x1, 0x0)
    FadeToBright(2000, 16777215)
    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)
    OP_68(22400, 11650, 80, 0)
    MoveCamera(67, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(31880, 0)
    OP_68(22400, 9150, 80, 6000)
    OP_6F(0x1)
    OP_0D()
    EndChrThread(0xA, 0x0)
    Fade(500)
    OP_68(17930, 8450, 680, 0)
    MoveCamera(56, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16840, 0)
    OP_0D()

    #C0060
    ChrTalk(
        0x18D,
        "#6P#04404F……这样应该就可以了。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#6P#00105F莉丝小姐，刚才那是……\x02",
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)
    Sleep(300)

    #C0062
    ChrTalk(
        0x18D,
        (
            "#11P#04402F嗯，那是教会传承的\x01",
            "封印魔力的法术。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#6P#00203F原来如此，\x01",
            "上级三属性的气息\x01",
            "似乎已经消失了。\x02\x03",

            "#00200F这样一来，\x01",
            "此处应该就不会再受\x01",
            "魔物的威胁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        (
            "#12P#10309F呵呵，\x01",
            "所有的功劳都被抢走了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x18D,
        (
            "#11P#04404F不……多亏有大家帮助，\x01",
            "才能顺利解决。\x02\x03",

            "#04402F各位，\x01",
            "非常感谢你们。\x02\x03",

            "这样一来，\x01",
            "对『魔物』的调查\x01",
            "工作就可以结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#6P#00000F哪里，在危急时刻，\x01",
            "多亏你出手相助。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#12P#00304F是啊，不必客气。\x02\x03",

            "#00309F为了帮助可爱的女孩，\x01",
            "就算赴汤蹈火也在所不辞。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18D, 0x104, 500)

    #C0068
    ChrTalk(
        0x18D,
        "#5P#04405F哦……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        "#12P#00306F哎呀呀，好冷淡的反应。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        "#6P#10109F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#6P#00206F那个……莉丝小姐，\x01",
            "请不要在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        (
            "#12P#00106F总、总而言之。\x02\x03",

            "#00100F我们先把莉丝小姐\x01",
            "送回教堂吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3185")

    #C0073
    ChrTalk(
        0x109,
        (
            "#6P#10109F没问题，\x01",
            "导力车刚好停在附近。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C0")

    label("loc_3185")


    #C0074
    ChrTalk(
        0x109,
        (
            "#6P#10100F没问题，\x01",
            "返回山道，就可以去车站搭乘巴士了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C0")


    #C0075
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，说的没错。\x01",
            "你意下如何？莉丝小姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)
    Sleep(300)

    #C0076
    ChrTalk(
        0x18D,
        (
            "#11P#04404F那就恭敬不如从命了。\x02\x03",

            "#04402F肚子已经饿了，\x01",
            "好想快点回去，\x01",
            "吃久久修女做的蛋糕。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#6P#00009F哈哈……\x01",
            "那我们就出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6840, 5050, -120, 7000)
    MoveCamera(52, 32, 0, 7000)
    OP_6E(650, 7000)
    SetCameraDistance(16840, 7000)

    def lambda_32BB():
        OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32BB)
    Sleep(50)

    def lambda_32D8():
        OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32D8)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 13)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 13)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 14)
    Sleep(800)

    def lambda_3319():
        OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18D, 1, lambda_3319)
    OP_6F(0x79)
    WaitChrThread(0x18D, 1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x18D, 0x80)
    OP_0D()
    ClearChrFlags(0x8, 0x80)
    OP_68(11990, 9000, -1150, 3000)
    MoveCamera(58, 12, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(12600, 3000)
    OP_6F(0x79)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("少年")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            "『星杯骑士团』的小姐，\x01",
            "还有特别任务支援科……\x02\x03",

            "昨天玩『波波碰』的表现也不错，\x01",
            "还挺能干的嘛。\x02\x03",

            "在这次的『计划』中……\x01",
            "他们似乎会成为\x01",
            "关键人物吧。\x02\x03",

            "呵呵……已经有些\x01",
            "期待了呢。\x02",
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
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(250)
    Sound(325, 0, 80, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(12050, 300)
    Sound(959, 2, 80, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    CancelBlur(1000)
    Sleep(500)
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(11250, 500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    StopSound(959, 1000, 70)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_6F(0x79)
    CancelBlur(1000)
    StopEffect(0x0, 0x2)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    SetCameraDistance(13250, 3000)
    Sleep(1000)
    StopSound(132, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x3BF)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x158, 0)
    SetScenarioFlags(0x22, 2)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_27D2 end

    def Function_12_35BE(): pass

    label("Function_12_35BE")

    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x18D, 0x20)
    SetChrSubChip(0x18D, 0x0)
    Sleep(1000)
    Sound(357, 0, 70, 0)
    PlayEffect(0x1, 0x1, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x18D, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x18D, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x1, 0x2)
    Sound(222, 0, 80, 0)
    PlayEffect(0x2, 0x2, 0x18D, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x18D, 0x3)
    Sleep(500)
    SetChrSubChip(0x18D, 0x4)
    Return()

    # Function_12_35BE end

    def Function_13_3679(): pass

    label("Function_13_3679")

    OP_95(0xFE, 15890, 7750, 860, 2000, 0x0)
    OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_3679 end

    def Function_14_36A2(): pass

    label("Function_14_36A2")

    OP_95(0xFE, 15890, 7750, -720, 2000, 0x0)
    OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_14_36A2 end

    SaveToFile()

Try(main)
