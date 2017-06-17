from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "道化師カンパネルラ",     # 1
        "弓の乙女エンネア",       # 2
        "SE制御",                 # 3
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
        "Function_6_1518",         # 06, 6
        "Function_7_1577",         # 07, 7
        "Function_8_15B3",         # 08, 8
        "Function_9_2958",         # 09, 9
        "Function_10_297F",        # 0A, 10
        "Function_11_29B0",        # 0B, 11
        "Function_12_39A0",        # 0C, 12
        "Function_13_3A5B",        # 0D, 13
        "Function_14_3A84",        # 0E, 14
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
            "ウフフ、お疲れさん。\x02\x03",

            "《廃墟#4Rダンジョン#探索》に《宝探し#6Rトレジャーハント#》……\x02\x03",

            "たまにはああいう王道な趣向も\x01",
            "悪くなかっただろう？\x02",
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
        "#00006F#6Pやはりお前の仕業か……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0003
    ChrTalk(
        0x104,
        (
            "#00312F#6P#N随分、面倒なお遊びに\x01",
            "付き合わせるじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0004
    ChrTalk(
        0x8,
        (
            "#04802F#11Pフフ、少しは障害が無いと\x01",
            "君らだって愉しくないだろう？\x02\x03",

            "#04809F道化師ならではのお茶目な\x01",
            "サービスとでも思って欲しいな㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        "#00211F#6P#N全然嬉しくありません……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E03")

    #C0006
    ChrTalk(
        0x109,
        (
            "#10106F#6P#Nそれにしても君……\x02\x03",

            "#10108Fとても《結社》なんかに\x01",
            "いるような歳には\x01",
            "見えないんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E59")

    label("loc_E03")


    #C0007
    ChrTalk(
        0x106,
        (
            "#10703F#6P#Nしかし貴方……\x02\x03",

            "#10701F《結社》などにいるような\x01",
            "歳には見えませんね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E59")

    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x102,
        (
            "#00101F#6P#Nそのあたりはレンちゃんと\x01",
            "同じような感じなのかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0009
    ChrTalk(
        0x8,
        (
            "#04804F#11Pフフ、彼女と違って\x01",
            "見た目通りの歳じゃないけどね。\x02\x03",

            "#04805F──そうそう。\x01",
            "クロスベルの独立無効宣言は\x01",
            "拝聴させてもらったよ。\x02\x03",

            "#04802Fなかなか興味深かったけど\x01",
            "かなり茨#2Rイバラ#の道じゃないかなぁ？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00013F#6P……覚悟の上だ。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        (
            "#00103F#6P#Nたとえ茨の道であろうと……\x01",
            "踏み越えなくてはならない\x01",
            "“時”というものはあるわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0012
    ChrTalk(
        0x8,
        (
            "#04804F#11Pウフフ、まあいいか。\x02\x03",

            "#04802Fクロスベルがどうなろうと\x01",
            "ボクの使命からは外れている。\x02\x03",

            "その意味では、とっとと\x01",
            "撤退してもいいんだけど……\x02\x03",

            "#04809F最後にとっておきのショウを\x01",
            "披露させてもらおうかな？\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_123B")
    Sound(540, 0, 50, 0)

    label("loc_123B")

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
        "#00011F#3P#Nこ、これは……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x103,
        (
            "#00207F#3P#N幻術……いえ、\x01",
            "特殊な位相空間の展開！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_131E")

    #C0015
    ChrTalk(
        0x105,
        (
            "#10410F#6P#N魔術的な結界に\x01",
            "取り込むつもりか……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1346")

    label("loc_131E")


    #C0016
    ChrTalk(
        0x106,
        "#10707F#6P#N方術による結界……！？\x02",
    )

    CloseMessageWindow()

    label("loc_1346")

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
            "#04804F#11P#30W#64Aウフフ、ここは足場が悪いから\x01",
            "もう少し広い場所に案内するよ。\x02",
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
            "#3724V#43A#35W執行者Ｎｏ．０、\x01",
            "《道化師》カンパネルラ。\x02\x03",

            "#3725V#34A#30Wいざ尋常に勝負──なんてね♪\x02",
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

    def Function_6_1518(): pass

    label("Function_6_1518")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1576")
    OP_82(0x28, 0x41, 0x1388, 0xFA)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 500, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    StopEffect(0x0, 0x2)
    Jump("Function_6_1518")

    label("loc_1576")

    Return()

    # Function_6_1518 end

    def Function_7_1577(): pass

    label("Function_7_1577")

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

    # Function_7_1577 end

    def Function_8_15B3(): pass

    label("Function_8_15B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("apl/ch51416.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00150.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00350.itc", 0x23)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15FB")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_15FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1613")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_1613")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_162B")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_162B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1643")
    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_1643")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_165B")
    LoadChrToIndex("chr/ch03150.itc", 0x25)

    label("loc_165B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1673")
    LoadChrToIndex("chr/ch03250.itc", 0x25)

    label("loc_1673")

    LoadChrToIndex("chr/ch03653.itc", 0x26)
    LoadChrToIndex("chr/ch00001.itc", 0x27)
    LoadChrToIndex("chr/ch00301.itc", 0x28)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A0")
    LoadChrToIndex("chr/ch02901.itc", 0x29)
    Jump("loc_16A6")

    label("loc_16A0")

    LoadChrToIndex("chr/ch03201.itc", 0x29)

    label("loc_16A6")

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
            "#04806F#11P#30Wハァ、やれやれ……\x02\x03",

            "#04801Fやっぱり慣れないことは\x01",
            "あんまりするもんじゃないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00010F#6P#30Wはあはあ……どうだ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1971")

    #C0021
    ChrTalk(
        0x105,
        (
            "#10401F#6P#N#30W僕たちの勝ちってことで\x01",
            "いいのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AE")

    label("loc_1971")


    #C0022
    ChrTalk(
        0x106,
        (
            "#10701F#6P#N#30W私たちの勝ちということで\x01",
            "いいんですね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AE")

    OP_57(0x0)
    OP_5A()
    OP_68(14250, 8400, 0, 1000)
    Sleep(250)

    def lambda_19CA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_19CA)
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
            "#04804F#11P#30W……ウフフ、異存はないよ。\x02\x03",

            "#04802Fまあ、《鋼の聖女》相手に\x01",
            "勝てるとはとても思えないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00013F#6P#30Wくっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0025
    ChrTalk(
        0x104,
        (
            "#00311F#6P#N#30Wハッ……\x01",
            "余計なお世話だっつーの。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0026
    ChrTalk(
        0x8,
        (
            "#04804F#11P#30Wフフ、これにてボクは\x01",
            "クロスベルを去らせてもらうよ。\x02\x03",

            "#04800F人に創られし《至宝》の行方……\x02\x03",

            "#04802F本当はもう少し見届けたかったけど\x01",
            "帝国方面が忙しくなってきたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#00108F#6P#N#30W『幻焔#4Rげんえん#計画』……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C10")

    #C0028
    ChrTalk(
        0x109,
        (
            "#10110F#6P#N今度はエレボニアの方を\x01",
            "滅茶苦茶にするつもり……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4F")

    label("loc_1C10")


    #C0029
    ChrTalk(
        0x106,
        (
            "#10701F#6P#N今度は帝国の方を\x01",
            "滅茶苦茶にするつもりですか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4F")

    OP_57(0x0)
    OP_5A()

    #C0030
    ChrTalk(
        0x8,
        (
            "#04804F#11Pウフフ、全ては偉大なる\x01",
            "《盟主》の意志によるもの……\x02\x03",

            "#04800Fだが、答えを出すのはいつだって\x01",
            "運命の中にある人の子たちさ。\x02\x03",

            "それは君たちも同じだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#00005F#6Pなに……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0032
    ChrTalk(
        0x103,
        "#00205F#6P#N……答えを出す？\x02",
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
            "#3726V#40W#40Aウフフ……\x01",
            "運がよければまた会おう。\x02\x03",

            "#3727V#40A果たして君たちが\x01",
            "どんな答えを出したのか……\x02\x03",

            "#3728V#25A是非、聞かせておくれよ♪\x02",
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
        "#00201F#12P#N#30Wあ……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2065")
    Sound(540, 0, 50, 0)

    label("loc_2065")

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
            "#00306F#5Pチッ……\x01",
            "最後まで思わせぶりな事を。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#00108F#5P私たちが答えを出す……\x01",
            "一体、何のことかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2169")

    #C0037
    ChrTalk(
        0x105,
        (
            "#10403F#5Pふむ……\x02\x03",

            "#10400Fまあ、とりあえず\x01",
            "鐘の共鳴を止めてしまおうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C3")

    label("loc_2169")


    #C0038
    ChrTalk(
        0x106,
        (
            "#10708F#5P………………………………\x02\x03",

            "#10701F……とりあえず\x01",
            "鐘の共鳴を止めましょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C3")

    OP_93(0x101, 0x10E, 0x1F4)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00001F#11Pそうだな……\x01",
            "ランディ、手伝ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2239")

    #C0040
    ChrTalk(
        0x109,
        "#10101F#5Pあたしも手伝います。\x02",
    )

    CloseMessageWindow()
    Jump("loc_225D")

    label("loc_2239")


    #C0041
    ChrTalk(
        0x106,
        "#10703F#5P私もお手伝いします。\x02",
    )

    CloseMessageWindow()

    label("loc_225D")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2338")
    SetChrChipByIndex(0x109, 0x29)
    SetChrSubChip(0x109, 0x1)
    SetChrPos(0x109, 20010, 7750, 30, 90)
    BeginChrThread(0x109, 3, 0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2322")
    SetChrPos(0xF5, 20960, 7750, -4210, 0)
    Jump("loc_2333")

    label("loc_2322")

    SetChrPos(0xF4, 20960, 7750, -4210, 0)

    label("loc_2333")

    Jump("loc_2390")

    label("loc_2338")

    SetChrChipByIndex(0x106, 0x29)
    SetChrSubChip(0x106, 0x1)
    SetChrPos(0x106, 20010, 7750, 30, 90)
    BeginChrThread(0x106, 3, 0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_237F")
    SetChrPos(0xF5, 20960, 7750, -4210, 0)
    Jump("loc_2390")

    label("loc_237F")

    SetChrPos(0xF4, 20960, 7750, -4210, 0)

    label("loc_2390")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24F4")
    EndChrThread(0x109, 0x3)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2500")

    label("loc_24F4")

    EndChrThread(0x106, 0x3)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    label("loc_2500")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25D9")
    OP_93(0x109, 0x2D, 0x0)
    Jump("loc_25E0")

    label("loc_25D9")

    OP_93(0x106, 0x2D, 0x0)

    label("loc_25E0")

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
        "#00105F#11P止まった……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#00203F#11P……上位三属性は\x01",
            "相変わらず働いていますが……\x02\x03",

            "#00202F他の鐘との共鳴については\x01",
            "解除できたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#00302F#11Pこれで《塔》の鐘を止めれば\x01",
            "万事オーケーってわけだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00004F#5Pああ、少なくとも\x01",
            "鐘同士の共鳴は終わる筈だ。\x02\x03",

            "#00000Fマイスターの話が本当なら\x01",
            "クロスベル市を包む結界も\x01",
            "解除できるかもしれない……\x02\x03",

            "#00007F行こう──《星見の塔》へ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27D9")

    #C0046
    ChrTalk(
        0x109,
        "#10100F#11P了解です！\x02",
    )

    CloseMessageWindow()

    label("loc_27D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2804")

    #C0047
    ChrTalk(
        0x106,
        "#10702F#11Pはい……！\x02",
    )

    CloseMessageWindow()

    label("loc_2804")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2835")

    #C0048
    ChrTalk(
        0x105,
        "#10402F#11PＯＫ、リーダー。\x02",
    )

    CloseMessageWindow()

    label("loc_2835")

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
            "《星見の塔》はウルスラ間道の途中から\x01",
            "脇道に入ることで行く事ができます。\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2906")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_290E")

    label("loc_2906")

    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    label("loc_290E")

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

    # Function_8_15B3 end

    def Function_9_2958(): pass

    label("Function_9_2958")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_297E")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(500)
    Jump("Function_9_2958")

    label("loc_297E")

    Return()

    # Function_9_2958 end

    def Function_10_297F(): pass

    label("Function_10_297F")

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

    # Function_10_297F end

    def Function_11_29B0(): pass

    label("Function_11_29B0")

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
            "#12P#04400Fこれは……\x01",
            "報告にあった《鐘》ですね。\x02\x03",

            "#04403F中央広場にある鐘と\x01",
            "ほぼ同じ物ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x103,
        (
            "#6P#00200Fあの鐘を鳴らすことで発生する\x01",
            "何らかの“力場”が、\x01",
            "遺跡全体を包んでいるようです。\x02\x03",

            "#00206F幽霊のようなものが出るのも、\x01",
            "そのせいかと思われるのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#6P#00001F以前は、力ずくで鐘を抑えて\x01",
            "共鳴を止めたんだよな。\x02\x03",

            "#00003Fそうすることで\x01",
            "発生した力場を消す事が\x01",
            "できたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        (
            "#6P#10108Fこんな大きな鐘が\x01",
            "勝手に鳴るなんてこと\x01",
            "あるわけないですよね……\x02\x03",

            "#10106F本当に誰が鳴らしたんでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x18D,
        "#12P#04403Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#6P#00001F……何はともあれ、ひとまず\x01",
            "この鐘を止めるとしよう。\x02\x03",

            "#00003F落ち着いて話をするためにも、\x01",
            "とりあえず魔物の脅威は\x01",
            "取り除いたほうがよさそうだ。\x02\x03",

            "#00000F……ランディ、ワジ。\x01",
            "手伝ってくれるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、いいけど。\x01",
            "なんとも原始的な方法だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#12P#00301Fつべこべ言うなっつの。\x01",
            "さっさと押し止めるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x18D,
        (
            "#12P#04403Fいえ……\x01",
            "それだけでは不完全です。\x02\x03",

            "#04402F少し下がっていてください。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EF3():

        label("loc_2EF3")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2EF3")

    QueueWorkItem2(0x101, 1, lambda_2EF3)
    Sleep(50)

    def lambda_2F08():

        label("loc_2F08")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2F08")

    QueueWorkItem2(0x102, 1, lambda_2F08)
    Sleep(50)

    def lambda_2F1D():

        label("loc_2F1D")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2F1D")

    QueueWorkItem2(0x103, 1, lambda_2F1D)
    Sleep(50)

    def lambda_2F32():

        label("loc_2F32")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2F32")

    QueueWorkItem2(0x104, 1, lambda_2F32)
    Sleep(50)

    def lambda_2F47():

        label("loc_2F47")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2F47")

    QueueWorkItem2(0x109, 1, lambda_2F47)
    Sleep(50)

    def lambda_2F5C():

        label("loc_2F5C")

        TurnDirection(0xFE, 0x18D, 500)
        Yield()
        Jump("loc_2F5C")

    QueueWorkItem2(0x105, 1, lambda_2F5C)
    Sleep(300)

    #C0059
    ChrTalk(
        0x101,
        "#6P#00005Fえ……\x02",
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
        "#6P#04404F……こんなところですね。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#6P#00105Fリースさん、今のは……\x02",
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)
    Sleep(300)

    #C0062
    ChrTalk(
        0x18D,
        (
            "#11P#04402Fええ、教会に伝わる、\x01",
            "魔の力を封じ込める法術です。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#6P#00203Fなるほど、確かに\x01",
            "上位三属性の気配が\x01",
            "消えたようです。\x02\x03",

            "#00200Fひとまずこれで\x01",
            "魔物の脅威は去ったと\x01",
            "見てよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        (
            "#12P#10309Fフフ、何から何まで\x01",
            "いいところをとられちゃったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x18D,
        (
            "#11P#04404Fいえ……\x01",
            "皆さんの力あってのことです。\x02\x03",

            "#04402Fみなさん、どうも\x01",
            "ありがとうございました。\x02\x03",

            "これで“魔物”に関する\x01",
            "一通りの調査を\x01",
            "終える事が出来ました。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#6P#00000Fいえ、俺たちも危ないところを\x01",
            "助けてもらいましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#12P#00304Fま、そういうことだな。\x02\x03",

            "#00309Fカワイコちゃんのためなら\x01",
            "たとえ火の中水の中ってやつさ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18D, 0x104, 500)

    #C0068
    ChrTalk(
        0x18D,
        "#5P#04405Fはあ……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        "#12P#00306Fありゃりゃ、反応薄っ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        "#6P#10109Fあ、あはは……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#6P#00206Fまあ……リースさん、\x01",
            "気にしないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        (
            "#12P#00106Fと、とりあえず。\x02\x03",

            "#00100F一旦、リースさんを教会まで\x01",
            "送ってあげましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34DB")

    #C0073
    ChrTalk(
        0x109,
        (
            "#6P#10109Fいいかもしれませんね。\x01",
            "導力車も近くに停めていますし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3522")

    label("loc_34DB")


    #C0074
    ChrTalk(
        0x109,
        (
            "#6P#10100Fいいかもしれませんね。\x01",
            "山道に戻ればバス停もありますし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3522")


    #C0075
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、そうだな。\x01",
            "……どうでしょう、リースさん？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)
    Sleep(300)

    #C0076
    ChrTalk(
        0x18D,
        (
            "#11P#04404Fでは、お言葉に甘えることにします。\x02\x03",

            "#04402Fお腹も空きましたし、\x01",
            "一刻も早くシスター・ジュジュの\x01",
            "クッキーでも頂きたい気分です。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#6P#00009Fはは……\x01",
            "それじゃあ行きましょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6840, 5050, -120, 7000)
    MoveCamera(52, 32, 0, 7000)
    OP_6E(650, 7000)
    SetCameraDistance(16840, 7000)

    def lambda_365F():
        OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_365F)
    Sleep(50)

    def lambda_367C():
        OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_367C)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 13)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 13)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 14)
    Sleep(800)

    def lambda_36BD():
        OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18D, 1, lambda_36BD)
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
            "《星杯騎士》のお嬢さん……\x01",
            "それに、特務支援課か。\x02\x03",

            "昨日の『ポムっと』といい、\x01",
            "なかなかやってくれるじゃない。\x02\x03",

            "今回の『計画』……\x01",
            "やっぱり彼らがキーパーソンに\x01",
            "なったりするのかな？\x02\x03",

            "ウフフ……なんだか改めて、\x01",
            "愉しみになってきちゃったよ。\x02",
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

    # Function_11_29B0 end

    def Function_12_39A0(): pass

    label("Function_12_39A0")

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

    # Function_12_39A0 end

    def Function_13_3A5B(): pass

    label("Function_13_3A5B")

    OP_95(0xFE, 15890, 7750, 860, 2000, 0x0)
    OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_3A5B end

    def Function_14_3A84(): pass

    label("Function_14_3A84")

    OP_95(0xFE, 15890, 7750, -720, 2000, 0x0)
    OP_97(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_14_3A84 end

    SaveToFile()

Try(main)
