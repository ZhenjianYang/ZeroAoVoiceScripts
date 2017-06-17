from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1090.bin",                # FileName
        "m1090",                    # MapName
        "m1090",                    # Location
        0x0072,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 114, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1090",                  # 0
        "アリアンロード",         # 1
        "剣の乙女ジャンヌ",       # 2
        "ランス",                 # 3
        "アリアンロード",         # 4
        "キーア",                 # 5
        "SE制御",                 # 6
        "bm1070",                 # 7
    ))

    ATBonus("ATBonus_1CC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_28C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_26C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_270", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_274", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_278", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_27C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_280", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_284", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2AC", 0x0052, 255, 6, 45, 3, 3, 30, 0, "bm1070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03500.dat", 0, 0, 0, 0, 0, "ms04200.dat", 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_26C", "ed7458", "ed7453", "ATBonus_1CC"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 5,   -14.5,                 5.5,                   -1.0,                  306.25,                [0.10101521760225296,  0.1414213925600052,    -0.0,                  0.0,                   -0.10101528465747833,  0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   2.0203046798706055,    1.2727930545806885,    0.19999998807907104,   1.0])

    ChipFrameInfo(812, 0)                                        # 0

    ScpFunction((
        "Function_0_32C",          # 00, 0
        "Function_1_356",          # 01, 1
        "Function_2_57A",          # 02, 2
        "Function_3_789",          # 03, 3
        "Function_4_7AE",          # 04, 4
        "Function_5_7D3",          # 05, 5
        "Function_6_1BF3",         # 06, 6
        "Function_7_1C12",         # 07, 7
        "Function_8_1D4C",         # 08, 8
        "Function_9_1DDE",         # 09, 9
        "Function_10_1E03",        # 0A, 10
        "Function_11_1E3C",        # 0B, 11
        "Function_12_1E56",        # 0C, 12
        "Function_13_4E36",        # 0D, 13
        "Function_14_4E5D",        # 0E, 14
    ))


    def Function_0_32C(): pass

    label("Function_0_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_343")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 2)
    Jump("loc_355")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_355")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 12)

    label("loc_355")

    Return()

    # Function_0_32C end

    def Function_1_356(): pass

    label("Function_1_356")

    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x1E)
    SetMapObjFrame(0x0, "bell_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C3")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x23, 0x96, 0x0)
    Jump("loc_4C7")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_END)), "loc_404")
    SetMapObjFrame(0xFF, "allback", 0x2, "red")
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    Jump("loc_4C7")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C7")
    LoadEffect(0x9, "map/mpbell02.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x0, 0x1D, 0x0, 0x20)
    SetMapObjFrame(0x0, "bell_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "allback", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cloud", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pano01", 0x1, 0x1)

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_END)), "loc_4DE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F5")

    label("loc_4DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_50A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_50A")

    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_53F")
    OP_24(0x84)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_561")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55B")
    OP_24(0x84)
    Sound(828, 1, 70, 0)
    Jump("loc_561")

    label("loc_55B")

    Sound(132, 1, 70, 0)

    label("loc_561")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_579")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_579")

    Return()

    # Function_1_356 end

    def Function_2_57A(): pass

    label("Function_2_57A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03500.itc", 0x1E)
    LoadChrToIndex("chr/ch43100.itc", 0x1F)
    LoadEffect(0x0, "battle/cr037100.eff")
    LoadEffect(0x1, "map/mpbell.eff")
    SoundLoad(828)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, -5740, 1190, 40, 90)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -6360, 1090, -1240, 45)
    SetChrFlags(0x9, 0x4)
    OP_70(0x0, 0x1E)
    SetMapObjFrame(0x0, "bell_add", 0x0, 0x1)
    Sound(828, 2, 100, 0)
    StopEffect(0x7, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    OP_68(-3620, 3240, 10, 0)
    MoveCamera(90, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(33000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 3450, 0, 7000)
    MoveCamera(60, 15, 0, 7000)
    SetCameraDistance(21000, 7000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    SetCameraDistance(28000, 10000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x19)
    Sleep(1)
    CancelBlur(4000)
    Sound(929, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 3)
    SetMapObjFrame(0x0, "bell_add", 0x1, 0x1)
    OP_71(0x0, 0x0, 0x1D, 0x0, 0x20)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Sound(829, 0, 100, 0)
    Sleep(4000)
    StopSound(828, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("r3080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_57A end

    def Function_3_789(): pass

    label("Function_3_789")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AD")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_3_789")

    label("loc_7AD")

    Return()

    # Function_3_789 end

    def Function_4_7AE(): pass

    label("Function_4_7AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D2")
    OP_82(0x64, 0x64, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_4_7AE")

    label("loc_7D2")

    Return()

    # Function_4_7AE end

    def Function_5_7D3(): pass

    label("Function_5_7D3")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_841")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)

    label("loc_841")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85F")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)

    label("loc_85F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87D")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch03251.itc", 0x27)

    label("loc_87D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89B")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch02951.itc", 0x29)

    label("loc_89B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B9")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch03151.itc", 0x29)

    label("loc_8B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D7")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)

    label("loc_8D7")

    LoadChrToIndex("chr/ch03500.itc", 0x2A)
    LoadChrToIndex("chr/ch03550.itc", 0x2B)
    LoadChrToIndex("chr/ch03551.itc", 0x2C)
    LoadChrToIndex("chr/ch03552.itc", 0x2D)
    LoadChrToIndex("chr/ch03553.itc", 0x2E)
    LoadChrToIndex("chr/ch03554.itc", 0x2F)
    LoadChrToIndex("chr/ch03557.itc", 0x30)
    LoadChrToIndex("apl/ch51408.itc", 0x31)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    CreatePortrait(1, 65296, 65408, 240, 128, 240, 136, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis286.itp")
    LoadEffect(0x0, "event\\ev17090.eff")
    LoadEffect(0x1, "event\\ev14015.eff")
    SoundLoad(3899)
    SoundLoad(3900)
    SoundLoad(3901)
    SoundLoad(3902)
    SoundLoad(3903)
    SoundLoad(3904)
    SoundLoad(3905)
    SoundLoad(3632)
    SoundLoad(3633)
    SoundLoad(825)
    SoundLoad(832)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -13110, 0, 5580, 90)
    SetChrPos(0x102, -13470, 0, 4350, 90)
    SetChrPos(0x103, -13880, 0, 6630, 90)
    SetChrPos(0x104, -13680, 0, 2960, 90)
    SetChrPos(0xF4, -15080, 0, 6140, 90)
    SetChrPos(0xF5, -14780, 0, 3600, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5900, 1140, 0, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16250, 0, -8350, 45)
    SetChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 17450, 0, -5600, 225)
    SetChrFlags(0xC, 0x8)
    OP_68(-5900, 5140, 0, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_68(-5900, 2140, 0, 8000)
    OP_6F(0x79)
    OP_0D()
    OP_68(-12700, 2420, 0, 5000)
    MoveCamera(90, 9, 0, 5000)
    OP_6E(550, 5000)
    SetCameraDistance(18150, 5000)

    def lambda_B17():
        OP_95(0xFE, -14680, 0, -2040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B17)
    Sleep(50)

    def lambda_B34():
        OP_95(0xFE, -15780, 0, -1400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B34)
    Sleep(50)

    def lambda_B51():
        OP_95(0xFE, -14470, 0, -650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B51)
    Sleep(50)

    def lambda_B6E():
        OP_95(0xFE, -14110, 0, 580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B6E)
    Sleep(50)

    def lambda_B8B():
        OP_95(0xFE, -16079, 0, 1140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B8B)
    Sleep(50)

    def lambda_BA8():
        OP_95(0xFE, -14880, 0, 1630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BA8)
    WaitChrThread(0x104, 1)

    def lambda_BC6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BC6)
    WaitChrThread(0xF5, 1)

    def lambda_BD7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_BD7)
    WaitChrThread(0x102, 1)

    def lambda_BE8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BE8)
    WaitChrThread(0x101, 1)

    def lambda_BF9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF9)
    WaitChrThread(0xF4, 1)

    def lambda_C0A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_C0A)
    WaitChrThread(0x103, 1)

    def lambda_C1B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C1B)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF5, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0x103, 2)
    OP_6F(0x79)
    BeginChrThread(0xD, 1, 0, 11)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7584", 0)
    OP_C9(0x0, 0x80000000)
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
            "#3899V#3C#40W#20A──来ましたか。\x02\x03",

            "#3900V#35Aどうやら覚悟と決意は\x01",
            "固まったようですね。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0002
    ChrTalk(
        0x102,
        "#00101F#6P#N《鋼#2Rはがね#の聖女》……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0003
    ChrTalk(
        0x103,
        "#00201F#6P#N《身喰らう蛇#10Rウ ロ ボ ロ ス#》の使徒ですか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00003F#6P#N──《道化師#6Rカンパネルラ#》が言うには\x01",
            "貴女たちの計画とやらは\x01",
            "既に帝国方面に移ったそうだな？\x02\x03",

            "#00001Fこれ以上、クロスベルに\x01",
            "居続ける必要はあるのか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0005
    ChrTalk(
        0x8,
        (
            "#04900F#3C#30Wいえ、厳密にはありません。\x02\x03",

            "博士は《零の至宝》の潜在能力に\x01",
            "興味を示していますが……\x02\x03",

            "既に我らの計画からは\x01",
            "外れてしまっている存在です。\x02\x03",

            "あとはクロイス家の方々と\x01",
            "貴方たちの問題でしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F5C")

    #C0006
    ChrTalk(
        0x109,
        "#10107F#6P#Nだ、だったらどうして……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_F82")

    label("loc_F5C")


    #C0007
    ChrTalk(
        0x106,
        "#10701F#6P#Nならどうして……！？\x02",
    )

    CloseMessageWindow()

    label("loc_F82")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE3")

    #C0008
    ChrTalk(
        0x105,
        (
            "#10406F#6P#N正直、関係ないんだったら\x01",
            "お引き取り願いたいんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1027")

    label("loc_FE3")


    #C0009
    ChrTalk(
        0x104,
        (
            "#00306F#12P#N……関係ないんだったら\x01",
            "正直、帰って欲しいんだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1027")

    OP_57(0x0)
    OP_5A()

    #C0010
    ChrTalk(
        0x8,
        (
            "#04900F#3C──簡単な事です。\x02\x03",

            "《至宝》の御子殿から\x01",
            "直接、頼まれたからです。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0011
    ChrTalk(
        0x101,
        "#00005F#6P#Nな……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0012
    ChrTalk(
        0x102,
        "#00107F#6P#Nキ、キーアちゃんから！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x33C, 0xA)
    OP_CB(0x1, 0x1, 0x41A, 0x41A, 0x0, 0x0)
    OP_CB(0x1, 0x1, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x1)
    Sleep(800)
    OP_68(17260, 1000, -7120, 0)
    MoveCamera(68, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #C0013
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#04924F#3901V#11P#3C#20A#40W──引き受けましょう。\x02\x03",

            "#04922F#3902V#56A御子殿の意には極力沿うよう、\x01",
            "《盟主》に申し付かっています。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #C0014
    ChrTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12304F#3632V#5P#13C#20A#40W……ありがとう。\x02\x03",

            "#12302F#3633V#46Aあなたたちのマスターにも\x01",
            "お礼を言っておいてね？\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_68(-12700, 2420, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x1, 0x1, 0x47E, 0x47E, 0x5DC, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    FadeToBright(1500, 16777215)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x33C, 0x1E)
    Sleep(500)

    #C0015
    ChrTalk(
        0x8,
        (
            "#04900F#3C#30W《戦鬼》に《剣聖》……\x01",
            "いずれも人としての域を\x01",
            "超えた者たちが集#2Rつど#っています。\x02\x03",

            "これ以上先に進めば\x01",
            "貴方たちも無事ではいられない。\x02\x03",

            "傷付く姿は見たくない……\x01",
            "そのように言っていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#00206F#30W#6P#N……キーア……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x104,
        "#00308F#30W#12P#Nキー坊、そんなことを……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0018
    ChrTalk(
        0x101,
        (
            "#00006F#6P#N#30Wありがとう──《鋼の聖女》。\x02\x03",

            "#00000F#20Wおかげで迷いを\x01",
            "完全に断ち切れた気分だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(500)
    SetCameraDistance(17000, 500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1574")
    Sound(540, 0, 50, 0)

    label("loc_1574")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    OP_6F(0x79)
    OP_0D()
    Sleep(800)

    #C0019
    ChrTalk(
        0x8,
        (
            "#04900F#3C……成程。\x01",
            "今の話を聞いてそうなりますか。\x02\x03",

            "どうやら最後の一押しを\x01",
            "してしまったようですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00013F#6P#Nああ──貴女には何としても\x01",
            "そこを退#2Rど#いてもらう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0021
    ChrTalk(
        0x102,
        (
            "#00104F#6P#N《壁》を乗り越えて\x01",
            "あの子を抱きしめるためにも……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0022
    ChrTalk(
        0x104,
        (
            "#00307F#12P#Nここで退いたら\x01",
            "男が廃#2Rすた#るってもんだぜ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0023
    ChrTalk(
        0x103,
        "#00201F#6P#N……女だって同じです。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1789")

    #C0024
    ChrTalk(
        0x105,
        (
            "#10402F#6P#Nフフ、どうやら\x01",
            "完全に火が点いたみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1789")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17D9")

    #C0025
    ChrTalk(
        0x106,
        (
            "#10706F#6P#N皆さんの気持ち……\x01",
            "……痛いほど分かります。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_17D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1827")

    #C0026
    ChrTalk(
        0x109,
        (
            "#10107F#6P#Nあたしも……\x01",
            "全力で援護させてもらいます！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1827")

    Sleep(500)

    #C0027
    ChrTalk(
        0x8,
        "#04900F#3C#30Wフフ……いいでしょう。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7458", 0)
    OP_68(-5900, 2420, 0, 3000)
    MoveCamera(90, 9, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(15500, 3000)
    OP_6F(0x79)
    BeginChrThread(0x8, 3, 0, 7)
    WaitChrThread(0x8, 3)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 8)
    WaitChrThread(0x8, 3)
    StopSound(828, 500, 30)
    OP_68(-12700, 2420, 0, 16000)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0028
    AnonymousTalk(
        0x8,
        (
            "#3903V#3C#30W#42A蛇の使徒が七柱、\x01",
            "《鋼》のアリアンロード……\x02\x03",

            "#3904V#54A《零》の御子殿の望みに従い、\x01",
            "ここに壁として立ち塞がらん。\x02\x03",

            "#3905V#30Aいざ──尋常に勝負！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    EndChrThread(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 10)
    Sound(2153, 255, 90, 0)    #voice#Elie
    Sound(2343, 255, 100, 1)    #voice#Randy
    Sound(2249, 255, 100, 2)    #voice#Tio
    Sound(2055, 255, 100, 3)    #voice#Lloyd
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A49")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A40")
    OP_FC(0x4)
    Sound(2478, 255, 100, 5)    #voice#Noel
    Jump("loc_1A49")

    label("loc_1A40")

    OP_FC(0x3)
    Sound(2478, 255, 100, 4)    #voice#Noel

    label("loc_1A49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A7C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A76")
    Sound(2417, 255, 100, 5)    #voice#Lazy
    Jump("loc_1A7C")

    label("loc_1A76")

    Sound(2417, 255, 100, 4)    #voice#Lazy

    label("loc_1A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AAF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA9")
    Sound(3174, 255, 100, 5)    #voice#Rixia
    Jump("loc_1AAF")

    label("loc_1AA9")

    Sound(3174, 255, 100, 4)    #voice#Rixia

    label("loc_1AAF")

    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ロイドたち")

    #A0029
    AnonymousTalk(
        0xFF,
        "#5S#12Aおおっ……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 0)
    Sound(829, 0, 50, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5900, 1640, 0, 1000)

    def lambda_1B14():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B14)

    def lambda_1B29():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B29)

    def lambda_1B3E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B3E)

    def lambda_1B53():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B53)

    def lambda_1B68():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1B68)

    def lambda_1B7D():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1B7D)
    Sleep(350)
    StopSound(825, 300, 100)
    StopSound(832, 300, 100)
    FadeToDark(0, -1, 0)
    FadeToDark(650, 16777215, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xF4, 0x1)
    EndChrThread(0xF5, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x8, 0x0)
    Battle("BattleInfo_2AC", 0x0, 0x0, 0x100, 0x40, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 12)
    Return()

    # Function_5_7D3 end

    def Function_6_1BF3(): pass

    label("Function_6_1BF3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C11")
    OP_A1(0xFE, 0x4B0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_6_1BF3")

    label("loc_1C11")

    Return()

    # Function_6_1BF3 end

    def Function_7_1C12(): pass

    label("Function_7_1C12")

    Fade(500)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 60, 0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x31)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    OP_0D()
    SetCameraDistance(15000, 2000)
    Sound(970, 0, 100, 0)
    Sound(920, 0, 100, 0)
    Sound(202, 0, 100, 0)
    PlayEffect(0x1, 0x0, 0xFE, 0x5, 0, 2200, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(1)
    CancelBlur(2500)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0xF)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -5900, 3300, -150, 0)

    def lambda_1CE7():
        OP_96(0xFE, 0xFFFFE8F4, 0x866, 0xFFFFFF6A, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CE7)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    Sound(288, 0, 70, 0)
    SetChrFlags(0xA, 0x80)
    OP_82(0x32, 0x0, 0x1388, 0x12C)
    OP_A1(0xFE, 0x4B0, 0x3, 0x5, 0x6, 0x7)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_1C12 end

    def Function_8_1D4C(): pass

    label("Function_8_1D4C")

    Fade(500)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x0, 0x1F4, 0x1388, 0x1F4)
    Sound(825, 2, 100, 0)
    Sound(832, 2, 100, 0)
    Sound(881, 0, 100, 0)
    Sound(833, 0, 70, 0)
    SetCameraDistance(14500, 500)
    StopEffect(0x7, 0x0)
    PlayEffect(0x0, 0x0, 0xFE, 0x5, 0, 0, -750, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 2000)
    BeginChrThread(0x8, 0, 0, 6)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(1000)
    BeginChrThread(0xFE, 2, 0, 9)
    Return()

    # Function_8_1D4C end

    def Function_9_1DDE(): pass

    label("Function_9_1DDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E02")
    OP_82(0x0, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_9_1DDE")

    label("loc_1E02")

    Return()

    # Function_9_1DDE end

    def Function_10_1E03(): pass

    label("Function_10_1E03")

    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sleep(500)

    label("loc_1E17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E3B")
    OP_82(0x0, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("loc_1E17")

    label("loc_1E3B")

    Return()

    # Function_10_1E03 end

    def Function_11_1E3C(): pass

    label("Function_11_1E3C")

    OP_25(0x33C, 0x3C)
    Sleep(400)
    OP_25(0x33C, 0x32)
    Sleep(400)
    OP_25(0x33C, 0x28)
    Sleep(400)
    OP_25(0x33C, 0x1E)
    Return()

    # Function_11_1E3C end

    def Function_12_1E56(): pass

    label("Function_12_1E56")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00056.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00156.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00256.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00356.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EB0")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch0295F.itc", 0x27)

    label("loc_1EB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ECE")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch0315F.itc", 0x27)

    label("loc_1ECE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EEC")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch0325A.itc", 0x27)

    label("loc_1EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F0A")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_1F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F28")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch0315F.itc", 0x29)

    label("loc_1F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F46")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch0325A.itc", 0x29)

    label("loc_1F46")

    LoadChrToIndex("chr/ch04250.itc", 0x2B)
    LoadChrToIndex("chr/ch04253.itc", 0x2E)
    LoadChrToIndex("chr/ch04254.itc", 0x2F)
    LoadChrToIndex("chr/ch00001.itc", 0x30)
    LoadChrToIndex("chr/ch00301.itc", 0x31)
    LoadChrToIndex("chr/ch02901.itc", 0x32)
    LoadChrToIndex("chr/ch03201.itc", 0x33)
    LoadEffect(0x0, "event/ev10006.eff")
    LoadEffect(0x1, "event/ev10007.eff")
    LoadEffect(0x2, "map/mpbell.eff")
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(132)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13700.itp")
    SoundLoad(3906)
    SoundLoad(3907)
    SoundLoad(3908)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -14110, 0, 580, 90)
    SetChrPos(0x102, -14470, 0, -650, 90)
    SetChrPos(0x103, -14880, 0, 1630, 90)
    SetChrPos(0x104, -14680, 0, -2040, 90)
    SetChrPos(0xF4, -16079, 0, 1140, 90)
    SetChrPos(0xF5, -15780, 0, -1400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AB")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x2E)
    SetChrSubChip(0x8, 0x3)
    Jump("loc_20E3")

    label("loc_20AB")

    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x27)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x29)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)

    label("loc_20E3")

    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5900, 1140, 0, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-5900, 2140, 0, 0)
    OP_68(-12700, 2420, 0, 5000)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16149, 0)
    SetCameraDistance(18150, 5000)
    BeginChrThread(0xD, 1, 0, 11)
    PlayBGM("ed7584", 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B65")
    OP_2C(0xB0, 0x5)
    OP_29(0xB0, 0x1, 0x7)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0030
    ChrTalk(
        0x8,
        "#13703F#40W………………………………\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00007F#40W#6P#Nはあはあ……\x01",
            "ど……どうだ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0032
    ChrTalk(
        0x104,
        (
            "#00307F#40W#12P#Nこ、これが俺たちの\x01",
            "全力ってヤツだぜ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0033
    ChrTalk(
        0x8,
        (
            "#13704F#30W……驚きました。\x02\x03",

            "#13702F私に膝を付かせる者たちが\x01",
            "よもや現れるとは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()

    def lambda_22D8():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_22D8)
    Sleep(250)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 40, 0)
    Sound(358, 0, 60, 0)
    OP_0D()
    WaitChrThread(0x8, 2)
    Sleep(500)
    Fade(500)
    OP_68(-12700, 2420, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
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

    #C0034
    ChrTalk(
        0x101,
        "#00010F#6P#Nくっ……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_244E")

    #C0035
    ChrTalk(
        0x105,
        "#10410F#6P#N#40Wまだ立てるのか……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2479")

    label("loc_244E")


    #C0036
    ChrTalk(
        0x106,
        "#10707F#6P#N#40Wまだ立てる……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2479")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24C6")

    #C0037
    ChrTalk(
        0x109,
        (
            "#10107F#6P#N#40Wで、でも……\x01",
            "こちらだって……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_24FA")

    label("loc_24C6")


    #C0038
    ChrTalk(
        0x106,
        (
            "#10707F#6P#N#40Wでも……\x01",
            "こちらだって……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_24FA")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0039
    AnonymousTalk(
        0x8,
        (
            "#30W──これ以上、\x01",
            "矛#2Rほこ#を交えるつもりはありません。\x02\x03",

            "今の貴方たちならば\x01",
            "《戦鬼》や《剣聖》たちにも\x01",
            "いずれ届くでしょう。\x02",
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
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 1500)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x2F)
    OP_A1(0x8, 0x3E8, 0x2, 0x2, 0x3)
    Sleep(150)
    SetChrSubChip(0x8, 0x4)
    OP_0D()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 250)
    Sound(357, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(500)
    Fade(600)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    Sound(288, 0, 30, 0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-11550, 1920, 0, 0)
    MoveCamera(50, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
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

    #C0040
    ChrTalk(
        0x101,
        "#00005F#6P#Nあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0041
    ChrTalk(
        0x104,
        "#00305F#6P#N退#2Rひ#いてくれんのか……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0042
    ChrTalk(
        0x8,
        (
            "#13704F#11P光明を示せたのであれば\x01",
            "これ以上は無用の手出しというもの。\x02\x03",

            "#13702Fこの結果をもって御子殿には\x01",
            "納得してもらうしかありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#00204F#6P#Nそうですか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A39")

    #C0044
    ChrTalk(
        0x105,
        (
            "#10403F#6P#N《鋼の聖女》……感謝する。\x02\x03",

            "#10408Fだが騎士団#6Rボ ク ら#が貴女たちと\x01",
            "馴れ合うことはあり得ない……\x02\x03",

            "#10401Fそれは分かっているよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0045
    ChrTalk(
        0x8,
        (
            "#13703F#11P無論です、《蒼の聖典》。\x02\x03",

            "帝国での動乱が決着すれば\x01",
            "『幻焔計画』も完了する……\x02\x03",

            "#13700F此度#4R こ たび#の顛末がどうなったとしても\x01",
            "雌雄を決する時は近いでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x105,
        "#10406F#6P#Nああ……そうだろうね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2A39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BAC")

    #C0047
    ChrTalk(
        0x106,
        (
            "#10706F#6P#N《鋼の聖女》……\x01",
            "一つだけ教えてください。\x02\x03",

            "#10701F貴女はかつて……私の父と？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0048
    ChrTalk(
        0x8,
        (
            "#13703F#11Pええ、１０年ほど前に。\x02\x03",

            "#13702F我が面を砕くほどの強者は\x01",
            "そう顕#2Rあらわ#れるものではありません。\x02\x03",

            "既にその高みに\x01",
            "届いているかもしれませんが……\x02\x03",

            "#13704Fそれでも別の道を進むかどうかは\x01",
            "貴女次第でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x106,
        "#10708F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2BAC")

    Fade(250)
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
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_68(-10990, 1920, -50, 800)
    OP_9B(0x0, 0x102, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CBD")

    #C0050
    ChrTalk(
        0x102,
        (
            "#00103F#6P#Nもう一つだけ……\x02\x03",

            "#00108F貴女のその髪、\x01",
            "そして《鉄機隊》という名前。\x02\x03",

            "#00101Fまさか貴女は、\x01",
            "かの《獅子戦役》の……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2D5F")

    label("loc_2CBD")


    #C0051
    ChrTalk(
        0x102,
        (
            "#00106F#6P#N《鋼の聖女》……\x01",
            "一つだけ教えてください。\x02\x03",

            "#00108F貴女のその髪、\x01",
            "そして《鉄機隊》という名前。\x02\x03",

            "#00101Fまさか貴女は、\x01",
            "かの《獅子戦役》の……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2D5F")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)

    #C0052
    ChrTalk(
        0x8,
        (
            "#13704F#11P#30Wふふ……\x02\x03",

            "#13702F──よくぞ気付いたとだけ、\x01",
            "答えておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0053
    ChrTalk(
        0x102,
        "#00105F#6P#N#4S……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0054
    ChrTalk(
        0x101,
        "#00005F#5Pエリィ……？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        "#00301F#5P何の話だ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0056
    ChrTalk(
        0x8,
        (
            "#13704F#3906V#30W#30A──それでは、さらばです。\x02\x03",

            "#3907V#30W#40A運命を前に貴方たちが\x01",
            "“答え”を出せること……\x02\x03",

            "#13702F#3908V#30W#30A遠き地より祈っていますよ。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopBGM(0x1770)
    SetCameraDistance(12500, 2000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)
    StopSound(832, 1000, 100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_2FA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2FA3)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    CancelBlur(1000)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-10700, 2420, 0, 0)
    OP_68(-12700, 2420, 0, 3000)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    #C0057
    ChrTalk(
        0x101,
        (
            "#00008F#5P……エリィ。\x01",
            "一体、何の話だったんだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30D2():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_30D2)
    Sleep(30)

    def lambda_30E2():
        TurnDirection(0x104, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_30E2)
    Sleep(30)

    def lambda_30F2():
        TurnDirection(0xF4, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_30F2)
    Sleep(30)

    def lambda_3102():
        TurnDirection(0xF5, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3102)
    Sleep(30)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0058
    ChrTalk(
        0x103,
        (
            "#00200F何だか、物凄く思わせぶりな\x01",
            "やり取りでしたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-16660, 2420, -660, 1500)
    MoveCamera(90, 17, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(14000, 1500)
    Sleep(500)
    OP_93(0x102, 0x110, 0x190)
    OP_6F(0x79)

    #C0059
    ChrTalk(
        0x102,
        (
            "#00106F#11P…………そうね。\x02\x03",

            "#00108F混乱させてしまいそうだから\x01",
            "あまり言いたくはないけど……\x02\x03",

            "#00101F私の考えが正しければ──\x01",
            "彼女は２５０年前の人間だわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0060
    ChrTalk(
        0x104,
        "#00307Fなにィ……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3304")

    #C0061
    ChrTalk(
        0x109,
        "#10111Fそ、それって……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3323")

    label("loc_3304")


    #C0062
    ChrTalk(
        0x106,
        "#10712Fそれは一体……！？\x02",
    )

    CloseMessageWindow()

    label("loc_3323")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    SetCameraDistance(13000, 30000)
    Sleep(500)

    #C0063
    ChrTalk(
        0x102,
        (
            "#00103F#11P#30W２５０年前、エレボニアで\x01",
            "帝位を巡る激しい継承者争いが\x01",
            "起きたことがあったの。\x02\x03",

            "争いは帝国全土に波及し、\x01",
            "遂には《獅子戦役》という名前で\x01",
            "呼ばれる事になったのだけど……\x02\x03",

            "#00108Fその時、中立の立場から\x01",
            "戦乱を終わらせるべく立ち上がった\x01",
            "とある女性の武人がいたの。\x02\x03",

            "#00101Fリアンヌ・サンドロット──\x02\x03",

            "麗しき黄金の髪をなびかせ、\x01",
            "《鉄騎隊》という一団を率いて\x01",
            "戦場を駆け抜けた人物よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00011Fあ……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        "#00205Fそれって……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        "#00310Fま、まんまじゃねーか！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35F2")

    #C0067
    ChrTalk(
        0x109,
        (
            "#10101Fあたしも本か何かで\x01",
            "読んだことがあります……！\x02\x03",

            "#10103F《戦#2Rいくさ#乙女》リアンヌ……\x01",
            "または《槍の聖女》リアンヌ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35ED")

    #C0068
    ChrTalk(
        0x105,
        (
            "#10403F帝国では誰でも知っている\x01",
            "歴史上の有名人だね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35ED")

    Jump("loc_367C")

    label("loc_35F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_367C")

    #C0069
    ChrTalk(
        0x105,
        (
            "#10403F帝国では誰でも知っている\x01",
            "歴史上の有名人だね……\x02\x03",

            "#10408Fしかも通り名の一つが、\x01",
            "《槍の聖女》リアンヌだったか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36BA")

    #C0070
    ChrTalk(
        0x106,
        (
            "#10701Fそんな人が\x01",
            "かつてエレボニアに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36BA")


    #C0071
    ChrTalk(
        0x101,
        (
            "#00006F《鉄騎隊》に《鉄機隊》……\x01",
            "《槍の聖女》に《鋼の聖女》か。\x02\x03",

            "#00008F外見といい、確かにあまりにも\x01",
            "符合が揃い過ぎている……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        (
            "#00106F#11P……でも２５０年前、\x01",
            "自らの働きで平和が戻った直後、\x01",
            "彼女は命を落としたはずよ。\x02\x03",

            "#00108F謀殺されたとか、病気だったとか、\x01",
            "色々と諸説があるのだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#00206F……普通に考えれば\x01",
            "その人物の真似をしただけだと\x01",
            "判断すべきかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#00306Fあの凄まじい力を見ちまうと\x01",
            "本人にしか思えなくなってくるな。\x02\x03",

            "#00301Fましてやあの、得体の知れねぇ\x01",
            "《結社》の人間だし。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3919")
    Sleep(300)

    #C0075
    ChrTalk(
        0x106,
        (
            "#10708F（まさか《銀#2Rイン#》と同じく\x01",
            "  誰かが跡を継いだ……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3919")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_396E")
    Sleep(300)

    #C0076
    ChrTalk(
        0x105,
        (
            "#10401F（……これは総長にも\x01",
            "  報告しておく必要があるな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396E")


    #C0077
    ChrTalk(
        0x102,
        (
            "#00104F#11Pふふ……\x01",
            "やっぱり混乱させちゃったわね。\x02\x03",

            "#00100F──いずれにしても彼女も\x01",
            "クロスベルから去ってしまった。\x02\x03",

            "憶測は置いておいて、\x01",
            "私たちの問題に集中しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#00006Fああ……そうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(-9700, 2920, 0, 2500)
    MoveCamera(90, 0, 0, 2500)
    OP_6E(550, 2500)
    SetCameraDistance(18150, 2500)

    def lambda_3A6D():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A6D)
    Sleep(30)

    def lambda_3A7D():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3A7D)
    Sleep(30)

    def lambda_3A8D():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3A8D)
    Sleep(30)

    def lambda_3A9D():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3A9D)
    Sleep(30)

    def lambda_3AAD():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3AAD)
    Sleep(30)

    def lambda_3ABD():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3ABD)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0079
    ChrTalk(
        0x101,
        (
            "#00004F#6P#Nよし──鐘の共鳴を止めよう。\x02\x03",

            "#00000F上手く行けばクロスベル市の\x01",
            "《結界》を解除できるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x2C, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    Jump("loc_4A8B")

    label("loc_3B65")

    OP_29(0xB0, 0x1, 0x6)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_3B7C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B7C)
    Sound(812, 0, 100, 0)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    WaitChrThread(0x101, 2)
    OP_0D()

    #C0080
    ChrTalk(
        0x101,
        "#00010F#40W#6P#Nぐっ……まだまだ……！\x02",
    )

    CloseMessageWindow()

    def lambda_3BE2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3BE2)
    Sound(812, 0, 100, 0)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(805, 0, 100, 0)
    WaitChrThread(0x104, 2)
    OP_0D()

    #C0081
    ChrTalk(
        0x104,
        (
            "#00310F#40W#12P#N……こんな所で……\x01",
            "立ち止まってられるかよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)

    def lambda_3C6C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C6C)
    Sleep(50)

    def lambda_3C88():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3C88)
    Sleep(50)

    def lambda_3CA4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3CA4)
    Sleep(50)

    def lambda_3CC0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_3CC0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CF6")
    Sound(540, 0, 50, 0)

    label("loc_3CF6")

    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xF5, 2)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0082
    AnonymousTalk(
        0x8,
        (
            "力不足の感は否めませんが……\x02\x03",

            "我が面を砕いたのであれば、\x01",
            "《戦鬼》や《剣聖》たちにも\x01",
            "届く可能性はあるでしょう。\x02",
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
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x2F)
    OP_A1(0x8, 0x3E8, 0x2, 0x2, 0x3)
    Sleep(150)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x8, 0x4)
    OP_0D()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 250)
    Sound(357, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(500)
    Fade(600)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    Sound(288, 0, 30, 0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-11550, 1920, 0, 0)
    MoveCamera(50, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
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

    #C0083
    ChrTalk(
        0x101,
        "#00005F#6P#Nアリアンロード……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0084
    ChrTalk(
        0x102,
        (
            "#00105F#6P#Nもしかして……\x01",
            "退#2Rひ#いてくれるのですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0085
    ChrTalk(
        0x8,
        (
            "#13704F#11P一筋の光明を示せたのであれば\x01",
            "これ以上は無用の手出しというもの。\x02\x03",

            "#13702Fこの結果をもって御子殿には\x01",
            "納得してもらうしかありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#00202F#6P#Nあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0087
    ChrTalk(
        0x104,
        "#00305F#6P#Nマジか……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42A7")

    #C0088
    ChrTalk(
        0x105,
        (
            "#10403F#6P#N《鋼の聖女》……感謝する。\x02\x03",

            "#10408Fだが騎士団#6Rボ ク ら#が貴女たちと\x01",
            "馴れ合うことはあり得ない……\x02\x03",

            "#10401Fそれは分かっているよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0089
    ChrTalk(
        0x8,
        (
            "#13703F#11P無論です、《蒼の聖典》。\x02\x03",

            "帝国での動乱が決着すれば\x01",
            "『幻焔計画』も完了する……\x02\x03",

            "#13700F此度#4R こ たび#の顛末がどうなったとしても\x01",
            "雌雄を決する時は近いでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x105,
        "#10406F#6P#Nああ……そうだろうね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_42A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4403")

    #C0091
    ChrTalk(
        0x106,
        (
            "#10706F#6P#N《鋼の聖女》……\x01",
            "一つだけ教えてください。\x02\x03",

            "#10701F貴女はかつて……私の父と？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0092
    ChrTalk(
        0x8,
        (
            "#13703F#11Pええ、１０年ほど前に。\x02\x03",

            "#13702F我が面を砕くほどの強者は\x01",
            "そう顕#2Rあらわ#れるものではありません。\x02\x03",

            "#13704Fその高みを目指すか……\x01",
            "それとも別の道を進むのかは\x01",
            "貴女次第でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x106,
        "#10708F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4403")

    Fade(250)
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
    Sleep(500)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0094
    ChrTalk(
        0x8,
        (
            "#13704F#3906V#30W#30A──それでは、さらばです。\x02\x03",

            "#3907V#30W#40A運命を前に貴方たちが\x01",
            "“答え”を出せること……\x02\x03",

            "#13702F#3908V#30W#30A遠き地より祈っていますよ。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopBGM(0x1770)
    SetCameraDistance(12500, 2000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)
    StopSound(832, 1000, 100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_459E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_459E)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    CancelBlur(1000)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-10700, 2420, 0, 0)
    OP_68(-12700, 2420, 0, 3000)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_82(0x14, 0x0, 0x7D0, 0x1F4)

    #C0095
    ChrTalk(
        0x101,
        "#00006F#40W#5Pはあああっ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46F2")

    #C0096
    ChrTalk(
        0x109,
        "#10106F#30Wつ、疲れました……\x02",
    )

    CloseMessageWindow()

    label("loc_46F2")


    #C0097
    ChrTalk(
        0x104,
        (
            "#00306F……ったく……\x01",
            "とんだ聖女様だぜ。\x02\x03",

            "#00301Fメチャクチャ美人で\x01",
            "タイプなお姉様だったのに\x01",
            "口説く所じゃなかったしよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#00211Fランディさん、\x01",
            "そういう問題では……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00106Fでも本当に……\x01",
            "よくあの兜面を砕くまで\x01",
            "食い下がれたというか……\x02\x03",

            "#00102F私たちもそれなりに\x01",
            "成長できているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00002F#5Pああ……そうだな。\x02\x03",

            "#00012Fまあ、キーアの話を聞いて\x01",
            "肚#2Rハラ#を括ることが出来たのが\x01",
            "大きかった気もするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        "#00104Fふふ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#00301Fああ……\x01",
            "あんな事を言われちゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        (
            "#00206F……絶対に取り戻して\x01",
            "抱きしめないと気が済みません。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4962")

    #C0104
    ChrTalk(
        0x105,
        (
            "#10402Fやれやれ。\x01",
            "ホント親バカだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4962")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49A4")

    #C0105
    ChrTalk(
        0x109,
        (
            "#10112Fあはは……\x01",
            "ロイドさんたちらしいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49E2")

    #C0106
    ChrTalk(
        0x106,
        (
            "#10709Fふふっ……\x01",
            "でも分かる気がします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E2")

    OP_68(-9700, 2920, 0, 2500)
    MoveCamera(90, 0, 0, 2500)
    OP_6E(550, 2500)
    SetCameraDistance(18150, 2500)
    OP_6F(0x79)

    #C0107
    ChrTalk(
        0x101,
        (
            "#00004F#6P#Nよし──鐘の共鳴を止めよう。\x02\x03",

            "#00000F上手く行けばクロスベル市の\x01",
            "《結界》を解除できるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_4A8B")

    OP_32(0xFF, 0xFF, 0x0)
    WaitBGM()
    SetChrChipByIndex(0x101, 0x30)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x104, 0x31)
    SetChrSubChip(0x104, 0x1)
    SetChrPos(0x101, 0, 1530, 2150, 180)
    SetChrPos(0x104, 0, 1530, -1900, 0)
    SetChrPos(0x102, -4480, 1300, -2860, 45)
    SetChrPos(0x103, -3630, 1320, -3800, 45)
    BeginChrThread(0x101, 3, 0, 13)
    BeginChrThread(0x104, 3, 0, 13)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B5E")
    SetChrChipByIndex(0x109, 0x32)
    SetChrSubChip(0x109, 0x1)
    SetChrPos(0x109, -2200, 1530, 0, 90)
    BeginChrThread(0x109, 3, 0, 13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B48")
    SetChrPos(0xF5, -2330, 1370, -4510, 0)
    Jump("loc_4B59")

    label("loc_4B48")

    SetChrPos(0xF4, -2330, 1370, -4510, 0)

    label("loc_4B59")

    Jump("loc_4BB6")

    label("loc_4B5E")

    SetChrChipByIndex(0x106, 0x33)
    SetChrSubChip(0x106, 0x1)
    SetChrPos(0x106, -2200, 1530, 0, 90)
    BeginChrThread(0x106, 3, 0, 13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BA5")
    SetChrPos(0xF5, -2330, 1370, -4510, 0)
    Jump("loc_4BB6")

    label("loc_4BA5")

    SetChrPos(0xF4, -2330, 1370, -4510, 0)

    label("loc_4BB6")

    StopEffect(0x7, 0x0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 2, 0, 4)
    BeginChrThread(0xD, 1, 0, 14)
    FadeToBright(1000, 0)
    OP_68(0, 1850, 0, 0)
    OP_68(0, 2850, 0, 6000)
    MoveCamera(105, 21, 0, 0)
    MoveCamera(70, 15, 0, 6000)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(15000, 6000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 2850, 0, 0)
    MoveCamera(90, 27, 0, 0)
    MoveCamera(90, 9, 0, 5000)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D1A")
    EndChrThread(0x109, 0x3)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_4D26")

    label("loc_4D1A")

    EndChrThread(0x106, 0x3)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    label("loc_4D26")

    OP_70(0x0, 0x1E)
    SetMapObjFrame(0x0, "bell_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "allback", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cloud", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back", 0x1, 0x1)
    SetMapObjFrame(0xFF, "allback", 0x2, "red")
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    Sleep(500)
    OP_68(0, 3550, 0, 0)
    MoveCamera(50, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(20000, 5000)
    Sound(132, 2, 70, 0)
    FadeToBright(2000, 16777215)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    StopSound(132, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1E56 end

    def Function_13_4E36(): pass

    label("Function_13_4E36")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E5C")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(500)
    Jump("Function_13_4E36")

    label("loc_4E5C")

    Return()

    # Function_13_4E36 end

    def Function_14_4E5D(): pass

    label("Function_14_4E5D")

    Sound(825, 2, 10, 0)
    Sleep(200)
    OP_25(0x339, 0x14)
    OP_25(0x33C, 0x28)
    Sleep(200)
    OP_25(0x339, 0x1E)
    OP_25(0x33C, 0x32)
    Sleep(200)
    OP_25(0x339, 0x28)
    OP_25(0x33C, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x32)
    OP_25(0x33C, 0x46)
    Sleep(2000)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x46)
    Return()

    # Function_14_4E5D end

    SaveToFile()

Try(main)
