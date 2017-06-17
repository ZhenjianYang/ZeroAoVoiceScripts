from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1490.bin",                # FileName
        "t1490",                    # MapName
        "t1490",                    # Location
        0x00BB,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 187, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1490",                  # 0
        "玛丽亚贝尔",             # 1
        "亚里欧斯长官",           # 2
        "琪雅",                   # 3
        "国防军士兵",             # 4
        "国防军士兵",             # 5
        "国防军士兵",             # 6
        "国防军士兵",             # 7
        "国防军士兵",             # 8
        "国防军士兵",             # 9
        "国防军士兵",             # 10
        "国防军士兵",             # 11
        "诺艾尔少尉",             # 12
        "映像画面",               # 13
        "映像画面",               # 14
        "映像画面",               # 15
        "映像画面",               # 16
        "映像画面",               # 17
        "SE控制",                 # 18
        "bt1430",                 # 19
        "bt1430",                 # 20
    ))

    ATBonus("ATBonus_2BC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_37C", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_3E0", 0x1142, 3, 6, 45, 3, 3, 30, 0, "bt1430", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_37C", "ed7540", "ed7453", "ATBonus_2BC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_39C", 0x1162, 3, 6, 45, 3, 3, 30, 0, "bt1430", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_37C", "ed7540", "ed7453", "ATBonus_2BC"),
            (),
            (),
            (),
        )
    )

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
    DeclNpc(-10000,  5000,    8500,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-6500,   6349,    8300,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(10000,   5000,    8500,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(6500,    6349,    8300,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-100,    10699,   9300,    0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1356, 0)                                       # 0

    ScpFunction((
        "Function_0_54C",          # 00, 0
        "Function_1_5D0",          # 01, 1
        "Function_2_650",          # 02, 2
        "Function_3_70A",          # 03, 3
        "Function_4_7C4",          # 04, 4
        "Function_5_87E",          # 05, 5
        "Function_6_2923",         # 06, 6
        "Function_7_298F",         # 07, 7
        "Function_8_29FB",         # 08, 8
        "Function_9_2A61",         # 09, 9
        "Function_10_2ACD",        # 0A, 10
        "Function_11_2AEF",        # 0B, 11
        "Function_12_2B11",        # 0C, 12
        "Function_13_2B33",        # 0D, 13
        "Function_14_2B55",        # 0E, 14
        "Function_15_2B77",        # 0F, 15
        "Function_16_2B87",        # 10, 16
        "Function_17_2B97",        # 11, 17
        "Function_18_2BA7",        # 12, 18
        "Function_19_2BB7",        # 13, 19
        "Function_20_2BC7",        # 14, 20
        "Function_21_2BE2",        # 15, 21
        "Function_22_2BF4",        # 16, 22
        "Function_23_3603",        # 17, 23
        "Function_24_3686",        # 18, 24
        "Function_25_36A6",        # 19, 25
        "Function_26_36D0",        # 1A, 26
        "Function_27_36FA",        # 1B, 27
        "Function_28_3724",        # 1C, 28
        "Function_29_3764",        # 1D, 29
        "Function_30_3780",        # 1E, 30
        "Function_31_4166",        # 1F, 31
        "Function_32_5F3D",        # 20, 32
        "Function_33_5F88",        # 21, 33
        "Function_34_5FA7",        # 22, 34
        "Function_35_5FC6",        # 23, 35
        "Function_36_6125",        # 24, 36
        "Function_37_6173",        # 25, 37
        "Function_38_61C4",        # 26, 38
        "Function_39_61F0",        # 27, 39
        "Function_40_621C",        # 28, 40
        "Function_41_631F",        # 29, 41
        "Function_42_6378",        # 2A, 42
        "Function_43_63CB",        # 2B, 43
        "Function_44_641E",        # 2C, 44
        "Function_45_6471",        # 2D, 45
        "Function_46_648B",        # 2E, 46
        "Function_47_64A5",        # 2F, 47
        "Function_48_64B8",        # 30, 48
        "Function_49_64E3",        # 31, 49
        "Function_50_74BD",        # 32, 50
        "Function_51_74DD",        # 33, 51
        "Function_52_751D",        # 34, 52
        "Function_53_7557",        # 35, 53
        "Function_54_7591",        # 36, 54
        "Function_55_75D1",        # 37, 55
        "Function_56_760B",        # 38, 56
        "Function_57_764B",        # 39, 57
        "Function_58_7685",        # 3A, 58
        "Function_59_76C5",        # 3B, 59
        "Function_60_7701",        # 3C, 60
        "Function_61_773D",        # 3D, 61
        "Function_62_7773",        # 3E, 62
        "Function_63_77AF",        # 3F, 63
        "Function_64_77BF",        # 40, 64
        "Function_65_77FA",        # 41, 65
        "Function_66_7835",        # 42, 66
        "Function_67_7870",        # 43, 67
        "Function_68_78AB",        # 44, 68
        "Function_69_78E6",        # 45, 69
        "Function_70_7921",        # 46, 70
        "Function_71_795C",        # 47, 71
        "Function_72_7997",        # 48, 72
        "Function_73_79CA",        # 49, 73
    ))


    def Function_0_54C(): pass

    label("Function_0_54C")

    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_581")
    SetScenarioFlags(0x0, 0)
    Event(0, 5)

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_595")
    ClearScenarioFlags(0x22, 0)
    Event(0, 22)
    Jump("loc_5CF")

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_5A9")
    ClearScenarioFlags(0x22, 1)
    Event(0, 30)
    Jump("loc_5CF")

    label("loc_5A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_5BD")
    ClearScenarioFlags(0x22, 2)
    Event(0, 31)
    Jump("loc_5CF")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_5CF")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 1)
    Event(0, 49)

    label("loc_5CF")

    Return()

    # Function_0_54C end

    def Function_1_5D0(): pass

    label("Function_1_5D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5E5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_5E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5FF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_617")

    label("loc_5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_617")
    SetScenarioFlags(0x0, 2)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_617")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_649")
    OP_24(0x39F)
    ClearScenarioFlags(0x0, 2)
    Jump("loc_64F")

    label("loc_649")

    Sound(927, 1, 80, 0)

    label("loc_64F")

    Return()

    # Function_1_5D0 end

    def Function_2_650(): pass

    label("Function_2_650")

    SetMapObjFrame(0xFF, "floor03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back_mi", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_back01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor_g02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "meca02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "code_b02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mirror", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_back", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mirror_", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pole02", 0x0, 0x1)
    Return()

    # Function_2_650 end

    def Function_3_70A(): pass

    label("Function_3_70A")

    SetMapObjFrame(0xFF, "floor03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back_mi", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_back01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "floor_g02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "meca02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "code_b02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mirror", 0x1, 0x1)
    SetMapObjFrame(0xFF, "Null_back", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mirror_", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pole02", 0x1, 0x1)
    Return()

    # Function_3_70A end

    def Function_4_7C4(): pass

    label("Function_4_7C4")

    SetMapObjFrame(0xFF, "floor03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back_mi", 0x1, 0x1)
    SetMapObjFrame(0xFF, "Null_back01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "floor_g02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "meca02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "code_b02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mirror", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_back", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mirror_", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pole02", 0x1, 0x1)
    Return()

    # Function_4_7C4 end

    def Function_5_87E(): pass

    label("Function_5_87E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51528.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch03754.itc", 0x21)
    LoadChrToIndex("apl/ch51529.itc", 0x22)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu10800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05800.itp")
    LoadEffect(0x0, "event\\ev15050.eff")
    SoundLoad(3719)
    SoundLoad(3398)
    SoundLoad(3399)
    SoundLoad(3400)
    SoundLoad(3321)
    SoundLoad(3780)
    SoundLoad(3781)
    SoundLoad(3782)
    SoundLoad(3783)
    SoundLoad(3625)
    SetChrPos(0x101, 0, -2000, -41500, 0)
    SetChrPos(0x102, -1000, -2000, -41500, 0)
    SetChrPos(0x103, 1000, -2000, -41500, 0)
    SetChrPos(0x104, 0, -2000, -41500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3250, 7150, 180)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1000, 2000, 3500, 180)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 2000, 2600, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x0, 0x14)
    OP_78(0x1, 0x15)
    OP_78(0x2, 0x16)
    OP_78(0x4, 0x18)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "m_face2", 0x0, 0x1)
    SetMapObjFrame(0x4, "m_face3", 0x0, 0x1)
    Call(0, 3)
    OP_68(0, 1000, -36000, 0)
    MoveCamera(145, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    FadeToBright(1000, 0)
    OP_68(0, -300, -36000, 6000)
    SetCameraDistance(16500, 6000)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(650)
    BeginChrThread(0x102, 3, 0, 7)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 8)
    Sleep(650)
    BeginChrThread(0x104, 3, 0, 9)
    WaitChrThread(0x101, 3)
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0001
    ChrTalk(
        0x101,
        "#00007F#11P#4S！！\x02",
    )

    CloseMessageWindow()
    OP_68(0, -300, -26000, 2000)
    MoveCamera(135, 16, 0, 2000)
    SetCameraDistance(15000, 2000)

    def lambda_BC4():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC4)
    Sleep(50)

    def lambda_BDC():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BDC)
    Sleep(50)

    def lambda_BF4():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BF4)
    Sleep(50)

    def lambda_C0C():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C0C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0002
    ChrTalk(
        0x103,
        "#00201F#11P这、这是……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        "#00310F#11P……喂喂……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        "#00106F#11P为什么……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7572", 0)
    Fade(1000)
    Call(0, 2)
    OP_68(0, 4000, -19000, 0)
    MoveCamera(0, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40000, 0)
    OP_68(0, 4000, 5000, 12000)
    MoveCamera(0, 15, 0, 12000)
    SetCameraDistance(35000, 12000)
    Sleep(1000)

    def lambda_CF1():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CF1)
    Sleep(50)

    def lambda_D09():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D09)
    Sleep(50)

    def lambda_D21():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D21)
    Sleep(50)

    def lambda_D39():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D39)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 1400, 5000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(0, 3300, 5000, 4000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(80, 170, -1, -1)

    #A0005
    AnonymousTalk(
        0x101,
        (
            "#00007F#3321V#30W#20A琪雅！\x01",
            "亚里欧斯先生……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(230, 170, -1, -1)

    #A0006
    AnonymousTalk(
        0x102,
        "#00107F#3398V#30W#15A……贝尔……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(1000)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(13500, 2000)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0007
    AnonymousTalk(
        0xA,
        "#3625V#40W……罗伊德……大家……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE29)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    Call(0, 3)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    SetChrPos(0x101, 0, -2000, -10500, 0)
    SetChrPos(0x102, -1000, -2000, -11500, 0)
    SetChrPos(0x103, 1000, -2000, -11500, 0)
    SetChrPos(0x104, 0, -2000, -12500, 0)
    OP_0D()

    #C0008
    ChrTalk(
        0x9,
        "#10503F#5P#30W……………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0009
    ChrTalk(
        0x8,
        (
            "#10804F#3780V#5P#30W呵呵……\x01",
            "你们总算到了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEC4)
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    #C0010
    ChrTalk(
        0x102,
        "#00106F#3399V#11P#40W贝尔……为什么……\x02",
    )

    CloseMessageWindow()
    OP_24(0xD47)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0011
    ChrTalk(
        0x102,
        (
            "#00107F#3400V#11P#4S#30W你为什么\x01",
            "会在这种地方！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD48)
    Fade(500)
    Call(0, 2)
    OP_68(-510, 3300, 2670, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16740, 0)
    SetCameraDistance(15740, 1500)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0012
    AnonymousTalk(
        0x8,
        (
            "#3781V#30W呵呵，答案很简单啊。\x02\x03",

            "#3782V身为继承了『伟大至宝』\x01",
            "的库罗伊斯家族后裔……\x02\x03",

            "#3783V我只是在履行\x01",
            "自己应尽的职责而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xEC7)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(300)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    Call(0, 3)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    OP_0D()

    #C0013
    ChrTalk(
        0x101,
        "#00011F#11P『伟大至宝』……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        (
            "#00207F#11P难道是和出现在利贝尔的\x01",
            "『辉之环』类似的……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#10809F#5P呵呵，既然你们知道这些，那就好解释了。\x02\x03",

            "#10804F在遥远的过去，女神将\x01",
            "『七至宝』赐给人类……\x02\x03",

            "#10811F而其中一件至宝就由\x01",
            "我的祖先世代继承。\x02\x03",

            "不过，只持续到一千二百年前而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#00205F#11P………？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        "#00306F#11P根本听不懂她在说什么……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#10804F#5P呵呵，由于发生了一件不幸的事故，\x01",
            "我们失去了女神所赐的至宝。\x02\x03",

            "#10803F其结果，就是让库罗伊斯家族的祖先们\x01",
            "坚定了无论如何也要寻回至宝的信念，\x01",
            "于是便展开了一项极其惊人的远大计划……\x02\x03",

            "#10800F最终，我们在克洛斯贝尔的地下\x01",
            "构筑了庞大的『式』。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00013F#11P！？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#00108F#11P庞大的『式』……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        (
            "#00201F#11P难道是利用了导力网络的\x01",
            "那个难以理解的巨大系统……？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#10803F#5P嗯，将现代导力技术与\x01",
            "库罗伊斯家族的炼金术融合之后，\x01",
            "便诞生了『魔导科学』……\x02\x03",

            "#10802F在『魔导科学』的基础上，我们终于\x01",
            "成功构筑了那个极其惊人的巨大的『式』。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        "#00208F#11P凭借『魔导科学』而构筑的『式』……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00110F#11P还、还有炼金术……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -800, -10500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00006F#11P……是吗……\x01",
            "原来是这样啊。\x02\x03",

            "#00008F建造『星见之塔』，\x01",
            "并为『教团』提供技术\x01",
            "的炼金术师集团……\x02\x03",

            "#00007F就是你们\x01",
            "库罗伊斯家族吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0026
    ChrTalk(
        0x104,
        "#00305F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00207F#11P不、不过……\x01",
            "这样一想的话，所有疑问就都能解开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#00107F#11P如、如此说来，\x01",
            "琪雅沉睡时所在的\x01",
            "那个『摇篮』也是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    OP_68(0, 3900, 5500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 1000)
    OP_0D()
    OP_6F(0x79)

    #C0029
    ChrTalk(
        0x8,
        (
            "#10804F#5P呵呵，那当然也是库罗伊斯家族\x01",
            "提供给『教团』的。\x02\x03",

            "#10811F给予他们信仰的对象，\x01",
            "从而让他们心情愉快地效力。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        "#05808F#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 3)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    OP_0D()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00013F#11P既然如此，\x01",
            "那『Ｄ∴Ｇ教团』显然……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00108F#11P是库罗伊斯家族为了达成目的\x01",
            "而暗中诱导的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#10804F#5P嗯，只不过是我们的傀儡而已。\x02\x03",

            "#10811F哼哼……但他们自己\x01",
            "却完全没有察觉到呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0034
    ChrTalk(
        0x8,
        (
            "#10809F#5P呵呵，你们已经大致理解\x01",
            "事情的背景了吧？\x02\x03",

            "#10805F哦，顺便一说，\x01",
            "亚里欧斯先生与我们家族\x01",
            "并无关系哦。\x02\x03",

            "#10804F他只是一位\x01",
            "赞同我们计划的\x01",
            "可靠协助者。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        "#10503F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00013F#11P亚里欧斯先生……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#00310F#11P……你是认真的吗？\x01",
            "你竟会赞同这种荒谬不堪的妄想……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "#10504F#5P呵……荒谬不堪的妄想吗。\x02\x03",

            "#10502F如果单论此言，\x01",
            "我也赞同你的看法。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#10801F#6P呼……！\x01",
            "真过分啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "#10503F#5P但既然他们拥有足够的力量，\x01",
            "可以将如今的状况改变……\x02\x03",

            "就算是虚无缥缈的幻想，\x01",
            "我也愿意协助到底。\x02\x03",

            "#10501F即使违背女神的意志\x01",
            "也在所不惜。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00108F#11P怎么会……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#00208F#11P……为什么……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -800, -10500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x22)
    OP_A1(0x101, 0x3E8, 0x2, 0x1, 0x2)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_6F(0x79)

    #C0043
    ChrTalk(
        0x101,
        (
            "#00006F#11P……老实说，突然听到了这么多惊人的事实，\x01",
            "我一时还无法将头绪理清……\x02\x03",

            "#00003F但是……有一句话我必须要说。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0x101, 0x514, 0x2, 0x3, 0x4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0044
    ChrTalk(
        0x101,
        (
            "#00010F#11P我绝不允许你们把琪雅\x01",
            "卷入到自己的妄想之中！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, -800, -10400, 500)
    Sound(33, 0, 100, 0)
    Sound(48, 0, 50, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_6F(0x79)
    Sleep(300)
    Fade(250)
    SetCameraDistance(16200, 300)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x22)
    OP_A1(0x101, 0x3E8, 0x2, 0x6, 0x7)
    OP_6F(0x79)
    OP_0D()
    Sleep(150)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0045
    ChrTalk(
        0x101,
        (
            "#00007F#11P#4S琪雅！快回来！\x02\x03",

            "#3S虽然我不知道他们是如何教唆你的，\x01",
            "但琪雅始终都是琪雅吧！？\x02\x03",

            "我不会让你一脸悲伤地……\x01",
            "坐在那种椅子上！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    OP_68(0, 3900, 5500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 1000)
    OP_0D()
    OP_6F(0x79)

    #C0046
    ChrTalk(
        0xA,
        "#05812F#5P#30W………罗伊德…………\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#10804F#5P呵呵……琪雅。\x02\x03",

            "罗伊德警官\x01",
            "都已经这样说了……\x02\x03",

            "#10811F你准备怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        "#05808F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(14000, 15000)
    OP_0D()
    Sleep(500)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0xE)
    Sleep(200)
    SetChrSubChip(0xA, 0x16)
    Sleep(800)
    SetMessageWindowPos(80, 170, -1, -1)

    #A0049
    AnonymousTalk(
        0x101,
        "#00011F……琪雅……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 170, -1, -1)

    #A0050
    AnonymousTalk(
        0x102,
        "#00105F你、你怎么了……？\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 170, -1, -1)

    #A0051
    AnonymousTalk(
        0x104,
        (
            "#00307F#4S阿琪！这有什么好犹豫的！？\x02\x03",

            "就像平时一样，\x01",
            "扑到罗伊德的怀里啊！\x02\x03",

            "这才是最能让你\x01",
            "安心的做法吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0052
    ChrTalk(
        0xA,
        "#05812F#5P#30W兰迪……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 170, -1, -1)

    #A0053
    AnonymousTalk(
        0x102,
        (
            "#00104F……是啊，\x01",
            "也许你有很多心事……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 170, -1, -1)

    #A0054
    AnonymousTalk(
        0x103,
        (
            "#00201F但我认为没有\x01",
            "比这更加重要的事情了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0055
    ChrTalk(
        0xA,
        (
            "#05808F#5P#30W……艾莉……缇欧……\x02\x03",

            "#05814F#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(921, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 3400, 7500, 0)
    MoveCamera(30, 50, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("少年的声音")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3719V#30W呵呵……\x01",
            "好像很热闹嘛。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE87)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(-8000, 5500, 8400, 0)
    MoveCamera(30, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(22000, 3500)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 10)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 11)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(8000, 5500, 8400, 0)
    MoveCamera(330, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(22000, 3500)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x16, 3, 0, 12)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(0, 5200, 7000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(32000, 4000)
    Sleep(500)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    Call(0, 3)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0057
    ChrTalk(
        0x102,
        "#00110F#11P『噬身之蛇』……！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        "#00201F#11P果然和他们脱不开关系……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0059
    ChrTalk(
        0x8,
        (
            "#10804F#5P呵呵，我们只不过是\x01",
            "互相协助而已……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)

    #C0060
    ChrTalk(
        0x8,
        (
            "#10802F#11P各位，\x01",
            "已经准备好了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    OP_68(0, 5200, 7000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    OP_0D()
    SetMessageWindowPos(80, 120, -1, -1)
    SetChrName("诺华提斯博士")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，那当然。\x02\x03",

            "已经全部完工，\x01",
            "性能一定让你满意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(280, 135, -1, -1)
    SetChrName("阿瑞安赫德")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『钟』也已经准备完毕。\x02\x03",

            "接下来就只需旋转你们那里的『钥匙』了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(10, 150, -1, -1)
    SetChrName("肯帕雷拉")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "为了让他们接受，\x01",
            "我们稍等一下倒也无妨……\x02\x03",

            "但时间就快到了哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-1500, 3000, 3800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    #C0064
    ChrTalk(
        0x8,
        "#10800F#11P哎呀呀。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        "#10501F#5P……要来了啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 3)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    OP_0D()

    #C0066
    ChrTalk(
        0x101,
        "#00011F#11P你、你们在说什么……？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        "#00307F#11P什么时间快到了！？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "#10503F#5P那还用问？\x02\x03",

            "#10501F自然是帝国军和共和国军的入侵。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0069
    ChrTalk(
        0x101,
        "#00007F#11P#4S！！\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        "#00110F#11P啊……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(100)

    #C0071
    ChrTalk(
        0x8,
        (
            "#10809F#5P呵呵，机会难得，\x01",
            "就来看看实况转播如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    OP_68(0, 3900, 5500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x21)
    BeginChrThread(0x8, 3, 0, 21)
    Sleep(300)
    OP_68(0, 9400, 5500, 5000)
    MoveCamera(0, -15, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(19000, 5000)
    OP_6F(0x79)
    BeginChrThread(0x18, 3, 0, 14)
    Sleep(2000)
    StopSound(927, 1000, 80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t2100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_87E end

    def Function_6_2923(): pass

    label("Function_6_2923")


    def lambda_2928():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2928)

    def lambda_293D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_293D)
    Sound(341, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_2923 end

    def Function_7_298F(): pass

    label("Function_7_298F")


    def lambda_2994():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2994)

    def lambda_29A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29A9)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_298F end

    def Function_8_29FB(): pass

    label("Function_8_29FB")


    def lambda_2A00():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A00)

    def lambda_2A15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A15)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_8_29FB end

    def Function_9_2A61(): pass

    label("Function_9_2A61")


    def lambda_2A66():
        OP_9B(0x0, 0xFE, 0x0, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A66)

    def lambda_2A7B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A7B)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_2A61 end

    def Function_10_2ACD(): pass

    label("Function_10_2ACD")

    OP_71(0x0, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_10_2ACD end

    def Function_11_2AEF(): pass

    label("Function_11_2AEF")

    OP_71(0x1, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x1)
    OP_71(0x1, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_11_2AEF end

    def Function_12_2B11(): pass

    label("Function_12_2B11")

    OP_71(0x2, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x2)
    OP_71(0x2, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_12_2B11 end

    def Function_13_2B33(): pass

    label("Function_13_2B33")

    OP_71(0x3, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x3)
    OP_71(0x3, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_13_2B33 end

    def Function_14_2B55(): pass

    label("Function_14_2B55")

    OP_71(0x4, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x4)
    OP_71(0x4, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_14_2B55 end

    def Function_15_2B77(): pass

    label("Function_15_2B77")

    OP_71(0x0, 0xF5, 0x12C, 0x0, 0x8)
    OP_79(0x0)
    Return()

    # Function_15_2B77 end

    def Function_16_2B87(): pass

    label("Function_16_2B87")

    OP_71(0x1, 0xFA, 0x12C, 0x0, 0x8)
    OP_79(0x1)
    Return()

    # Function_16_2B87 end

    def Function_17_2B97(): pass

    label("Function_17_2B97")

    OP_71(0x2, 0xFF, 0x12C, 0x0, 0x8)
    OP_79(0x2)
    Return()

    # Function_17_2B97 end

    def Function_18_2BA7(): pass

    label("Function_18_2BA7")

    OP_71(0x3, 0x104, 0x12C, 0x0, 0x8)
    OP_79(0x3)
    Return()

    # Function_18_2BA7 end

    def Function_19_2BB7(): pass

    label("Function_19_2BB7")

    OP_71(0x4, 0x10E, 0x12C, 0x0, 0x8)
    OP_79(0x4)
    Return()

    # Function_19_2BB7 end

    def Function_20_2BC7(): pass

    label("Function_20_2BC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BE1")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_20_2BC7")

    label("loc_2BE1")

    Return()

    # Function_20_2BC7 end

    def Function_21_2BE2(): pass

    label("Function_21_2BE2")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_21_2BE2 end

    def Function_22_2BF4(): pass

    label("Function_22_2BF4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51528.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch03754.itc", 0x21)
    LoadEffect(0x0, "battle/mgaria0.eff")
    LoadEffect(0x1, "event\\ev500_00.eff")
    SoundLoad(852)
    SoundLoad(825)
    SetChrPos(0x101, 0, -2000, -10500, 0)
    SetChrPos(0x102, -1000, -2000, -11500, 0)
    SetChrPos(0x103, 1000, -2000, -11500, 0)
    SetChrPos(0x104, 0, -2000, -12500, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3250, 7150, 180)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1000, 2000, 3500, 180)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 2000, 2600, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x0, 0x14)
    OP_78(0x1, 0x15)
    OP_78(0x2, 0x16)
    OP_78(0x3, 0x17)
    OP_78(0x4, 0x18)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    OP_71(0x0, 0x64, 0xC8, 0x0, 0x20)
    OP_71(0x1, 0x64, 0xC8, 0x0, 0x20)
    OP_71(0x2, 0x64, 0xC8, 0x0, 0x20)
    OP_71(0x4, 0x64, 0xC8, 0x0, 0x20)
    SetMapObjFrame(0x4, "m_face1", 0x0, 0x1)
    SetMapObjFrame(0x4, "m_face3", 0x0, 0x1)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    OP_68(0, 9400, 5500, 0)
    MoveCamera(0, -15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(19000, 4000)
    OP_6F(0x79)
    OP_0D()
    SetMessageWindowPos(230, 170, -1, -1)

    #A0072
    AnonymousTalk(
        0x102,
        "#00110F怎、怎么会……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 170, -1, -1)

    #A0073
    AnonymousTalk(
        0x104,
        "#00311F要来了吗……！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(130, 170, -1, -1)

    #A0074
    AnonymousTalk(
        0x103,
        (
            "#00201F凭警备队的战斗力，\x01",
            "无论如何也难以……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(921, 0, 80, 0)
    Sleep(500)
    Fade(500)
    OP_68(0, 3400, 7500, 0)
    MoveCamera(330, 50, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    OP_0D()
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("男性的声音")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "所以说，她正是\x01",
            "扭转这种局面的『钥匙』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(6500, 6350, 8300, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(22000, 3500)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 13)
    WaitChrThread(0x17, 3)
    Fade(500)
    Call(0, 3)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0076
    ChrTalk(
        0x101,
        "#00010F#11P迪塔总统……！\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#00107F#11P……迪塔叔叔……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 20, -1, -1)
    SetChrName("迪塔总统")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『结社』的诸位，\x01",
            "感谢你们在此次计划中提供的协助。\x02\x03",

            "贝尔和亚里欧斯也辛苦了。\x01",
            "看样子，情况始终如预期般发展吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0079
    ChrTalk(
        0x8,
        "#10804F#5P嗯，目前为止，是这样的。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "#10503F#5P……但接下来的事情\x01",
            "就只能交给她了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    OP_68(1700, 3400, 9440, 0)
    MoveCamera(326, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 1500)
    SetCameraDistance(24500, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(230, 150, -1, -1)
    SetChrName("迪塔总统")

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅，情况就是这样……\x02\x03",

            "你应该明白吧？\x02\x03",

            "只有你才能解决\x01",
            "如今这种事态。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 3000)
    OP_0D()
    OP_63(0xA, 0x0, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    OP_6F(0x79)
    Fade(500)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0xE)
    Sleep(200)
    SetChrSubChip(0xA, 0x16)
    OP_0D()
    Sleep(300)

    #C0082
    ChrTalk(
        0xA,
        "#05803F#5P#30W…………………（点头）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7585", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x249), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(14500, 5000)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(928, 0, 50, 0)
    Sound(852, 2, 100, 0)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x1)
    BeginChrThread(0xA, 3, 0, 24)
    WaitChrThread(0xA, 3)
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 2, 0, 23)
    Sound(825, 2, 50, 0)
    OP_0D()
    Fade(1000)
    OP_68(0, 3900, 10000, 0)
    OP_68(0, 7900, 10000, 3000)
    MoveCamera(0, 50, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    BeginChrThread(0x19, 1, 0, 29)
    BeginChrThread(0x14, 3, 0, 15)
    BeginChrThread(0x15, 3, 0, 16)
    BeginChrThread(0x16, 3, 0, 17)
    BeginChrThread(0x17, 3, 0, 18)
    BeginChrThread(0x18, 3, 0, 19)
    Sleep(1300)
    Sound(147, 0, 100, 0)
    Sleep(200)
    BeginChrThread(0xA, 3, 0, 25)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_25(0x339, 0x3C)
    OP_68(0, -2000, 7500, 0)
    MoveCamera(315, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(39000, 0)
    OP_68(0, 7000, 7500, 10000)
    Sleep(750)
    BeginChrThread(0xA, 3, 0, 26)
    WaitChrThread(0xA, 3)
    Sleep(2000)
    BeginChrThread(0xA, 3, 0, 27)
    WaitChrThread(0xA, 3)
    Sleep(4000)
    OP_0D()
    Fade(1000)
    OP_68(0, 3900, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(10500, 0)
    SetCameraDistance(15500, 3000)
    OP_6F(0x79)
    OP_0D()
    Sound(833, 0, 100, 0)
    OP_11(0x53, 0x59, 0x88, 0x2D, 0x78, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 3900, 7500, 1000)
    MoveCamera(0, 4, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(84250, 1000)
    Sleep(1000)
    CancelBlur(1000)
    OP_6F(0x79)
    Sleep(2000)
    Fade(1000)
    OP_68(0, 4900, 4000, 0)
    OP_68(0, 3900, 4000, 2500)
    MoveCamera(325, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_11(0x53, 0x59, 0x88, 0xF, 0x78, 0x0)
    OP_6F(0x79)
    OP_0D()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    #C0083
    ChrTalk(
        0x8,
        "#10811F#5P呵呵，真是个好孩子。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    Sound(357, 0, 100, 0)
    StopSound(852, 1000, 100)
    PlayEffect(0x0, 0xFF, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 3, 0, 20)
    Sleep(1300)
    StopSound(825, 2000, 70)
    StopSound(927, 2000, 70)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_24(0x354)
    OP_24(0x339)
    SetScenarioFlags(0x22, 0)
    NewScene("m1090", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_2BF4 end

    def Function_23_3603(): pass

    label("Function_23_3603")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3685")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3633")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_367D")

    label("loc_3633")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3658")
    OP_82(0xA, 0x1E, 0xBB8, 0x1F4)
    Jump("loc_367D")

    label("loc_3658")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_367D")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_367D")

    label("loc_367D")

    Sleep(500)
    Jump("Function_23_3603")

    label("loc_3685")

    Return()

    # Function_23_3603 end

    def Function_24_3686(): pass

    label("Function_24_3686")

    SetMapObjFrame(0xFF, "chair", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    Return()

    # Function_24_3686 end

    def Function_25_36A6(): pass

    label("Function_25_36A6")

    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on_ani")
    Sleep(1133)
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    Return()

    # Function_25_36A6 end

    def Function_26_36D0(): pass

    label("Function_26_36D0")

    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    Return()

    # Function_26_36D0 end

    def Function_27_36FA(): pass

    label("Function_27_36FA")

    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_27_36FA end

    def Function_28_3724(): pass

    label("Function_28_3724")

    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_28_3724 end

    def Function_29_3764(): pass

    label("Function_29_3764")

    Sleep(500)
    Sound(162, 0, 100, 0)
    Sleep(400)
    Sound(162, 0, 100, 0)
    Sleep(300)
    Sound(162, 0, 100, 0)
    Return()

    # Function_29_3764 end

    def Function_30_3780(): pass

    label("Function_30_3780")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10500.itp")
    LoadChrToIndex("apl/ch51528.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch03754.itc", 0x21)
    LoadChrToIndex("apl/ch51530.itc", 0x22)
    LoadChrToIndex("chr/ch00050.itc", 0x23)
    LoadChrToIndex("chr/ch00051.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00151.itc", 0x26)
    LoadChrToIndex("chr/ch00250.itc", 0x27)
    LoadChrToIndex("chr/ch00251.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("chr/ch00351.itc", 0x2A)
    LoadChrToIndex("chr/ch03850.itc", 0x2B)
    LoadEffect(0x0, "battle/mgaria0.eff")
    LoadEffect(0x1, "event\\ev500_00.eff")
    SoundLoad(931)
    SoundLoad(832)
    SoundLoad(533)
    SoundLoad(932)
    SoundLoad(4055)
    SoundLoad(4056)
    SoundLoad(4057)
    SoundLoad(3401)
    SoundLoad(3322)
    SoundLoad(2766)
    SoundLoad(2684)
    SetChrPos(0x101, 0, -2000, -10500, 0)
    SetChrPos(0x102, -1000, -2000, -11500, 0)
    SetChrPos(0x103, 1000, -2000, -11500, 0)
    SetChrPos(0x104, 0, -2000, -12500, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3250, 7150, 180)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1000, 2000, 3500, 90)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 2000, 2600, 180)
    Sound(832, 2, 70, 0)
    PlayEffect(0x0, 0xFF, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x21)
    BeginChrThread(0x8, 3, 0, 20)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Call(0, 28)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 2, 0, 23)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    OP_68(0, 3800, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    Sound(931, 2, 10, 0)
    Sound(832, 2, 40, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22500, 5500)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_25(0x340, 0x1E)
    Call(0, 3)
    OP_68(0, -800, -10500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0084
    ChrTalk(
        0x101,
        "#00007F#11P#4S琪雅！不要啊！\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#00107F#11P贝尔！你也快住手！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#00310F#11P虽然不知道是怎么回事，\x01",
            "但绝不能坐视不理……！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#00201F#11P总之……\x01",
            "先去阻止琪雅！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, -800, -8500, 1000)

    def lambda_3B15():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B15)
    Sleep(50)

    def lambda_3B2D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B2D)
    Sleep(50)

    def lambda_3B45():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3B45)
    Sleep(50)

    def lambda_3B5D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B5D)
    Sleep(450)
    StopBGM(0xFA0)
    StopSound(931, 2000, 10)
    Fade(250)
    OP_25(0x340, 0x46)
    Call(0, 2)
    OP_68(0, -800, -10500, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 2070, -250, 2000)
    MoveCamera(0, 7, 0, 2000)
    OP_6E(900, 2000)
    SetCameraDistance(9700, 2000)
    BlurSwitch(0x2BC, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -250, 180)
    SetChrFlags(0x9, 0x4)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrPos(0x101, 0, -2000, -10500, 0)
    SetChrPos(0x102, -1000, -2000, -11500, 0)
    SetChrPos(0x103, 1000, -2000, -11500, 0)
    SetChrPos(0x104, 0, -2000, -12500, 0)

    def lambda_3C63():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C63)
    Sleep(50)

    def lambda_3C7B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C7B)
    Sleep(50)

    def lambda_3C93():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C93)
    Sleep(50)

    def lambda_3CAB():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CAB)
    Sleep(950)
    CancelBlur(1250)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_0D()

    #C0088
    ChrTalk(
        0x101,
        "#00011F#6P#N……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0089
    ChrTalk(
        0x104,
        "#00311F#4P#N『风之剑圣』……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0090
    ChrTalk(
        0x9,
        "#10503F#5P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    Sound(932, 0, 100, 0)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 50, 0)
    SetCameraDistance(9200, 500)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetCameraDistance(8700, 8000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0091
    AnonymousTalk(
        0x9,
        (
            "#4055V#40W……如果想从此处通过，\x01",
            "就拿出你们的全部力量吧。\x02\x03",

            "#4056V盖伊、我，还有赛尔盖先生\x01",
            "都没能跨越那道『壁障』……\x02\x03",

            "#4057V#30W而你们是否拥有\x01",
            "跨越它的力量呢……！\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_24(0xFD9)
    OP_82(0x0, 0x15E, 0xBB8, 0x1F4)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x8)
    SetCameraDistance(8200, 250)
    Sound(533, 0, 60, 0)
    Sound(540, 0, 60, 0)
    Sound(531, 0, 60, 0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)
    Sleep(500)
    CancelBlur(500)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1270, -1750, 0)
    MoveCamera(0, 3, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(11550, 0)
    OP_0D()

    #C0092
    ChrTalk(
        0x101,
        "#00010F#3322V#6P#N#30W#15A唔……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0093
    ChrTalk(
        0x104,
        "#00307F#2766V#6P#N#30W#27A别胆怯！对手只有一个人而已！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0094
    ChrTalk(
        0x102,
        "#00107F#3401V#6P#N#30W#20A只要努力寻找制胜机会……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0095
    ChrTalk(
        0x103,
        (
            "#00207F#2684V#12P#N#30W#28A永世系统完全开启！\x01",
            "准备击破目标……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x27)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(100)
    OP_68(0, 2070, -250, 600)
    MoveCamera(0, 7, 0, 600)
    OP_6E(900, 600)
    SetCameraDistance(7700, 600)

    def lambda_40B2():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40B2)

    def lambda_40C7():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40C7)

    def lambda_40DC():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_40DC)

    def lambda_40F1():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40F1)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_24(0x3A3)
    OP_24(0x340)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_4144")
    Battle("BattleInfo_3E0", 0x0, 0x0, 0x100, 0x3F, 0xFF)
    Jump("loc_4154")

    label("loc_4144")

    Battle("BattleInfo_39C", 0x0, 0x0, 0x100, 0x3F, 0xFF)

    label("loc_4154")

    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Return()

    # Function_30_3780 end

    def Function_31_4166(): pass

    label("Function_31_4166")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51528.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch03754.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x23)
    LoadChrToIndex("chr/ch00051.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00151.itc", 0x26)
    LoadChrToIndex("chr/ch00250.itc", 0x27)
    LoadChrToIndex("chr/ch00251.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("chr/ch00351.itc", 0x2A)
    LoadChrToIndex("chr/ch00056.itc", 0x2B)
    LoadChrToIndex("chr/ch00156.itc", 0x2C)
    LoadChrToIndex("chr/ch00256.itc", 0x2D)
    LoadChrToIndex("chr/ch00356.itc", 0x2E)
    LoadChrToIndex("chr/ch03850.itc", 0x2F)
    LoadChrToIndex("chr/ch03853.itc", 0x32)
    LoadChrToIndex("apl/ch51531.itc", 0x33)
    LoadChrToIndex("chr/ch03856.itc", 0x34)
    LoadChrToIndex("chr/ch03852.itc", 0x35)
    LoadChrToIndex("chr/ch00053.itc", 0x36)
    LoadChrToIndex("chr/ch00153.itc", 0x37)
    LoadChrToIndex("chr/ch00253.itc", 0x38)
    LoadChrToIndex("chr/ch00353.itc", 0x39)
    LoadChrToIndex("apl/ch51545.itc", 0x3A)
    LoadEffect(0x0, "battle/mgaria0.eff")
    LoadEffect(0x1, "event\\ev500_00.eff")
    LoadEffect(0x2, "event\\ev400_00.eff")
    LoadEffect(0x3, "event\\ev15051.eff")
    LoadEffect(0x4, "event\\evwarp.eff")
    LoadEffect(0x5, "event\\ev609_00.eff")
    LoadEffect(0x6, "event\\ev609_01.eff")
    LoadEffect(0x7, "event\\ev001_00.eff")
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(852)
    SoundLoad(3402)
    SoundLoad(3323)
    SoundLoad(3324)
    SoundLoad(3325)
    SoundLoad(2767)
    SoundLoad(2685)
    SoundLoad(3784)
    SoundLoad(3785)
    SoundLoad(3786)
    SoundLoad(3626)
    SoundLoad(3627)
    SoundLoad(3628)
    SoundLoad(3629)
    SoundLoad(3630)
    SoundLoad(3631)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 3250, 7150, 180)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1000, 2000, 3500, 90)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 0, 0)
    Sound(832, 2, 50, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x21)
    BeginChrThread(0x8, 3, 0, 20)
    PlayEffect(0x1, 0x1, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Call(0, 28)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 2, 0, 23)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44EC")
    SetChrChipByIndex(0x9, 0x32)
    SetChrSubChip(0x9, 0x3)
    SetChrChipByIndex(0x101, 0x23)
    SetChrChipByIndex(0x102, 0x25)
    SetChrChipByIndex(0x103, 0x27)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x101, 0, 0, -3500, 0)
    OP_90(0x102, -1000, 0, -4500, 0)
    OP_90(0x103, 1000, 0, -4500, 0)
    OP_90(0x104, 0, 0, -5500, 0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -1000, 180)
    SetChrFlags(0x9, 0x4)
    OP_68(0, 1200, -1000, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 3000)
    Call(0, 2)
    Jump("loc_4755")

    label("loc_44EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C0")
    SetChrChipByIndex(0x101, 0x2B)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x103, 0x2D)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, -2000, -9000, 0)
    SetChrPos(0x102, -1000, -2000, -10000, 0)
    SetChrPos(0x103, 1000, -2000, -10000, 0)
    SetChrPos(0x104, 0, -2000, -11000, 0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -2500, 180)
    SetChrFlags(0x9, 0x4)
    OP_68(0, -300, -9000, 0)
    OP_68(0, -300, -7000, 3000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Call(0, 3)
    Jump("loc_4755")

    label("loc_45C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4694")
    SetChrChipByIndex(0x101, 0x2B)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x103, 0x2D)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, -2000, -9000, 0)
    SetChrPos(0x102, -1000, -2000, -10000, 0)
    SetChrPos(0x103, 1000, -2000, -10000, 0)
    SetChrPos(0x104, 0, -2000, -11000, 0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -2500, 180)
    SetChrFlags(0x9, 0x4)
    OP_68(0, -300, -9000, 0)
    OP_68(0, -300, -7000, 3000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Call(0, 3)
    Jump("loc_4755")

    label("loc_4694")

    SetChrChipByIndex(0x101, 0x2B)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x103, 0x2D)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, -2000, -9000, 0)
    SetChrPos(0x102, -1000, -2000, -10000, 0)
    SetChrPos(0x103, 1000, -2000, -10000, 0)
    SetChrPos(0x104, 0, -2000, -11000, 0)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -2500, 180)
    SetChrFlags(0x9, 0x4)
    OP_68(0, -300, -9000, 0)
    OP_68(0, -300, -7000, 3000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Call(0, 3)

    label("loc_4755")

    PlayBGM("ed7572", 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C81")
    OP_2C(0xAD, 0x5)

    #C0096
    ChrTalk(
        0x101,
        "#00002F#6P#N成、成功了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0097
    NpcTalk(
        0x103,
        "兰迪",
        (
            "#00302F#12P#N呼……\x01",
            "怎么样！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0098
    ChrTalk(
        0x9,
        (
            "#10504F#5P……呵……\x01",
            "真是让我吃了一惊。\x02\x03",

            "#10502F如此看来，你们说不定……\x01",
            "真的能超越我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        "#00105F#6P#N……哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0100
    ChrTalk(
        0x103,
        (
            "#00207F#12P#N感觉不到\x01",
            "亚里欧斯先生的气息了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0101
    ChrTalk(
        0x101,
        "#00011F#6P#N！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetCameraDistance(15500, 0)
    Sound(341, 0, 100, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x2BC)
    OP_0D()
    Fade(500)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, -800, -5000, 0)
    OP_68(0, -800, -6500, 1000)
    MoveCamera(30, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12000, 0)
    Sleep(250)
    Sound(341, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, -2000, -9500, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x226)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_49F1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49F1)
    Sleep(50)

    def lambda_4A01():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4A01)
    Sleep(50)

    def lambda_4A11():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4A11)
    Sleep(50)

    def lambda_4A21():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4A21)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    #C0102
    ChrTalk(
        0x104,
        "#00310F#5P空蝉……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#00007F#5P#N糟糕……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BlurSwitch(0xFA, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, -1000, -9000, 1200)
    MoveCamera(150, 30, 0, 1200)
    OP_6E(750, 1200)
    SetCameraDistance(10000, 1200)
    Sleep(500)
    CancelBlur(1000)
    OP_6F(0x79)
    Fade(400)
    SetCameraDistance(9500, 0)
    SetChrChipByIndex(0x9, 0x35)
    OP_A1(0x9, 0x3E8, 0x2, 0x4, 0x3)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 50, 0)
    OP_0D()
    OP_6F(0x79)
    #Sound(3990, 255, 100, 0)    #voice#Arios

    #C0104
    ChrTalk(
        0x9,
        "#15A#10503F#11P第二型『疾风』。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF96)
    ClearChrFlags(0x9, 0x4)
    OP_68(0, 0, -3400, 1000)
    MoveCamera(145, 36, 0, 1000)
    OP_6E(750, 1000)
    SetCameraDistance(11700, 1000)
    Sound(251, 0, 100, 0)
    BeginChrThread(0x9, 3, 0, 35)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()
    Sleep(250)
    Fade(250)
    OP_68(0, 300, -3500, 0)
    OP_68(0, 1300, -1500, 1500)
    MoveCamera(40, 12, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12000, 0)
    OP_90(0x9, 0, 0, -1500, 0)
    Sleep(300)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_6F(0x79)
    #Sound(3992, 255, 100, 0)    #voice#Arios

    #C0105
    ChrTalk(
        0x9,
        "#12A#5P#10507F#5S#9A斩……！\x02",
    )
    #Auto

    BeginChrThread(0x9, 3, 0, 40)
    WaitChrThread(0x9, 3)
    Sleep(800)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(0, -300, -9000, 0)
    OP_68(0, -300, -7000, 3000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    OP_90(0x9, 0, 3000, -2500, 180)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    SetChrFlags(0x9, 0x4)
    Jump("loc_4ECF")

    label("loc_4C81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D50")
    OP_2C(0xAD, 0x3)

    #C0106
    ChrTalk(
        0x101,
        (
            "#00010F#11P#30W呜……\x01",
            "都已经坚持到这种地步了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#00310F#11P#30W又怎能……\x01",
            "就此放弃……！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "#10504F#5P……你们确实有所成长。\x02\x03",

            "#10502F有朝一日……\x01",
            "或许可以超越我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4ECF")

    label("loc_4D50")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E23")
    OP_2C(0xAD, 0x1)

    #C0109
    ChrTalk(
        0x101,
        "#00006F#11P#30W呜……呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#00206F#11P#30W战斗力……\x01",
            "……相差太远了……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#10503F#5P你们的实力不差，\x01",
            "只是太欠缺技巧了。\x02\x03",

            "#10501F这样下去，恐怕只会\x01",
            "重蹈我们的覆辙。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4ECF")

    label("loc_4E23")


    #C0112
    ChrTalk(
        0x101,
        "#00006F#11P#40W……呜………\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        (
            "#00106F#11P#40W实、实力竟然\x01",
            "相差如此悬殊……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "#10503F#5P你们修炼得还不够啊。\x02\x03",

            "#10500F就凭这种狼狈的样子，\x01",
            "又怎能守护重要的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4ECF")

    Fade(1000)
    OP_25(0x340, 0x46)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    OP_68(0, 3800, 4000, 0)
    OP_68(0, 3800, 5500, 1200)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    OP_6F(0x79)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0115
    ChrTalk(
        0xA,
        "#05807F#3626V#5P#4S#30W#13A大家……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0116
    ChrTalk(
        0x8,
        (
            "#10804F#6P#N呵呵，别担心，已经手下留情了。\x02\x03",

            "#10811F不要分散注意力，\x01",
            "否则无法顺利完成哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Sound(825, 2, 50, 0)
    Fade(1000)
    OP_68(0, 3900, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_C9(0x0, 0x80000000)

    #C0117
    ChrTalk(
        0xA,
        (
            "#05806F#3627V#5P#40W#32A……明白了……\x02\x03",

            "#32A#05801F#3628V#30W我不会……\x01",
            "再迷茫下去了……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE2C)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0xE)
    Sleep(200)
    SetChrSubChip(0xA, 0x16)
    OP_0D()
    Sleep(300)
    OP_A1(0xA, 0x3E8, 0x2, 0xE, 0x6)
    Sleep(200)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrPos(0xA, 0, 3350, 7150, 180)
    SetChrSubChip(0xA, 0x10)
    OP_0D()
    Sleep(300)
    OP_A1(0xA, 0x514, 0x2, 0x11, 0x12)
    Sleep(300)
    OP_A1(0xA, 0x514, 0x2, 0x13, 0x14)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7552", 0)
    Fade(500)
    SetCameraDistance(16500, 0)
    BeginChrThread(0xA, 3, 0, 32)
    Sound(928, 0, 80, 0)
    Sound(929, 0, 60, 0)
    Sound(852, 2, 100, 0)
    OP_0D()
    SetCameraDistance(15500, 10000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetMessageWindowPos(50, 170, -1, -1)

    #A0118
    AnonymousTalk(
        0x102,
        "#00107F#3402V#30W#18A琪、琪雅……！？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_82(0x190, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(-1, 170, -1, -1)
    OP_C9(0x0, 0x80000000)

    #A0119
    AnonymousTalk(
        0x101,
        "#00007F#3323V#4S#18A#30W不要啊……！！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopSound(832, 1400, 70)
    StopSound(825, 1400, 50)
    Sound(829, 0, 100, 0)
    FadeToDark(1500, 16777215, -1)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(10500, 1500)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(1)
    StopSound(927, 500, 80)
    StopSound(852, 500, 100)
    OP_C9(0x0, 0x10)
    FadeToBright(1000, 16777215)
    OP_0D()
    OP_C9(0x1, 0x10)
    OP_24(0x340)
    OP_24(0x339)
    OP_24(0x354)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_05.pmf", 0x228, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    EndChrThread(0xA, 0x3)
    StopEffect(0x1, 0x0)
    StopEffect(0x0, 0x0)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x2D, 0x0)
    SoundLoad(933)
    SoundLoad(852)
    SoundLoad(825)
    SoundLoad(927)
    Sound(825, 2, 50, 0)
    Sound(927, 2, 80, 0)
    Sound(933, 2, 80, 0)
    FadeToBright(20000, 16777215)
    OP_11(0x53, 0x59, 0x88, 0x2D, 0x78, 0x3E8)
    OP_68(0, 3900, -4200, 0)
    OP_68(0, 3900, 7500, 10000)
    MoveCamera(0, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(75000, 0)
    BeginChrThread(0x19, 1, 0, 45)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    EndChrThread(0x19, 0x1)
    Sleep(1000)
    OP_6F(0x79)
    OP_11(0x53, 0x59, 0x88, 0xF, 0x78, 0x0)
    BeginChrThread(0x19, 1, 0, 46)
    FadeToDark(0, 16777215, 120)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, -800, -8500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)

    #C0120
    ChrTalk(
        0x102,
        "#00106F#11P呀呀呀呀呀……！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#00010F#11P这、这光芒……！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        "#00310F#11P到底是怎么回事……！？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#00210F#11P密度极其惊人的\x01",
            "七属性灵子情报……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, -300, -7500, 2000)
    Sleep(500)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(1000)
    EndChrThread(0x19, 0x1)
    BeginChrThread(0x19, 1, 0, 45)
    Fade(1000)
    OP_68(0, 4200, 7500, 0)
    MoveCamera(0, 30, 0, 0)
    MoveCamera(0, 15, 0, 8000)
    OP_6E(550, 0)
    SetCameraDistance(25500, 0)
    SetCameraDistance(15500, 8000)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x33)
    SetChrSubChip(0xA, 0x30)
    BeginChrThread(0xA, 3, 0, 33)
    SetChrPos(0xA, 0, 3750, 7150, 180)
    SetChrFlags(0xA, 0x8)
    BeginChrThread(0x19, 2, 0, 47)
    BeginChrThread(0x19, 3, 0, 48)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x3, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x19, 0x1)
    Sound(852, 2, 100, 0)
    StopSound(933, 1000, 80)
    StopSound(825, 1000, 50)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    SetCameraDistance(14500, 0)
    ClearChrFlags(0xA, 0x8)
    PlayEffect(0x1, 0x1, 0xA, 0x5, 0, 750, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    #A0124
    AnonymousTalk(
        0x9,
        "#10500F#11P…………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(80, 170, -1, -1)

    #A0125
    AnonymousTalk(
        0x101,
        "#00005F………啊…………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 170, -1, -1)

    #A0126
    AnonymousTalk(
        0x102,
        "#00105F琪……琪雅……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(50, 140, -1, -1)

    #A0127
    AnonymousTalk(
        0x8,
        (
            "#10804F#3784V#40W……呵呵呵…………\x01",
            "成功了呢……\x02\x03",

            "#10811F#3785V消失的『幻之至宝』终于重现……\x02\x03",

            "#10809F#3786V#30W不，应该说是凌驾在『幻之至宝』\x01",
            "之上的『零之至宝』终于诞生了！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xECA)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetMessageWindowPos(200, 170, -1, -1)

    #A0128
    AnonymousTalk(
        0x103,
        "#00201F零、零之至宝……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 170, -1, -1)

    #A0129
    AnonymousTalk(
        0x104,
        "#00310F那、那是什么……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    SetCameraDistance(14000, 1500)
    EndChrThread(0xA, 0x3)
    OP_A1(0xA, 0x3E8, 0x7, 0x34, 0x36, 0x37, 0x0, 0x1, 0x2, 0x3)
    OP_A1(0xA, 0x3E8, 0x3, 0x4, 0x5, 0x6)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 3, 0, 34)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)
    OP_C9(0x0, 0x80000000)
    SetChrName("？？？")

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3629V#40W罗伊德………大家…………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE2D)
    Sleep(150)
    SetMessageWindowPos(0, 140, -1, -1)

    #A0131
    AnonymousTalk(
        0x101,
        (
            "#00011F#3324V#40W………唔……………\x02\x03",

            "#00013F#3325V#40W………琪雅……………\x01",
            "真的是……琪雅吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xCFD)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Fade(250)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x33)
    OP_A1(0xA, 0x3E8, 0x3, 0x6, 0x7, 0x8)
    OP_0D()
    Sleep(150)

    #C0132
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12303F#40W#5P嗯……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x3E8, 0x2, 0x7, 0x6)
    Sleep(300)
    OP_A1(0xA, 0x3E8, 0x2, 0xA, 0xB)
    Sleep(300)

    #C0133
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12315F#40W#11P……贝尔，我们走吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(100, 170, -1, -1)

    #A0134
    AnonymousTalk(
        0x101,
        "#00005F#30W哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 3)
    OP_68(-1500, 2500, 0, 0)
    MoveCamera(140, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20850, 0)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 3, 0, 34)
    OP_93(0x8, 0x0, 0x0)
    OP_0D()

    #C0135
    ChrTalk(
        0x8,
        (
            "#10804F#11P呵呵，明白了。\x02\x03",

            "#10800F亚里欧斯先生，\x01",
            "这里的事情就交给你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        "#10503F#11P……知道了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 3900, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(20500, 5000)
    SetChrFlags(0xA, 0x20)

    def lambda_5BF5():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5BF5)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1000)

    def lambda_5C1B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5C1B)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xA, 1)
    ClearChrFlags(0xA, 0x20)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(0, -800, -8500, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16500, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0137
    ChrTalk(
        0x103,
        "#00205F#2685V#11P#30W#12A琪雅……！？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0138
    ChrTalk(
        0x104,
        "#00307F#2767V#11P#30W#20A喂，你要去哪里……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 5300, 7500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(15000, 1500)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x33)
    SetChrSubChip(0xA, 0x6)
    OP_6F(0x79)
    OP_0D()
    OP_A1(0xA, 0x3E8, 0x5, 0x6, 0xD, 0xE, 0xF, 0x10)
    Sleep(300)

    #C0139
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12304F#3630V#5P#40W#5P#40A对不起。\x01",
            "……谢谢大家至今为止对我的照顾。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(14500, 500)
    OP_A1(0xA, 0x3E8, 0x4, 0x10, 0x11, 0x12, 0x13)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0140
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12302F#3631V#40W#5P#30A我……最喜欢你们了。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE2F)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(28000, 1500)
    MoveCamera(0, 15, 0, 1500)
    StopSound(852, 1000, 100)
    Sleep(700)
    Sound(936, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrFlags(0xA, 0x8)
    Sleep(300)
    Sound(936, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x8, 0x0, 0, 750, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrFlags(0x8, 0x8)
    OP_6F(0x79)
    Sleep(1000)
    StopSound(927, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x228), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3A5)
    OP_24(0x354)
    OP_24(0x339)
    OP_24(0x39F)
    SetScenarioFlags(0x22, 3)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4166 end

    def Function_32_5F3D(): pass

    label("Function_32_5F3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F87")
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Jump("Function_32_5F3D")

    label("loc_5F87")

    Return()

    # Function_32_5F3D end

    def Function_33_5F88(): pass

    label("Function_33_5F88")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FA6")
    OP_A1(0xFE, 0x3E8, 0x8, 0x30, 0x31, 0x32, 0x31, 0x30, 0x33, 0x34, 0x33)
    Jump("Function_33_5F88")

    label("loc_5FA6")

    Return()

    # Function_33_5F88 end

    def Function_34_5FA7(): pass

    label("Function_34_5FA7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FC5")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_34_5FA7")

    label("loc_5FC5")

    Return()

    # Function_34_5FA7 end

    def Function_35_5FC6(): pass

    label("Function_35_5FC6")

    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    PlayEffect(0x5, 0x2, 0x9, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x2EE0, 0x1)
    StopEffect(0x2, 0x2)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6032():
        OP_9B(0x1, 0xFE, 0x0, 0x1964, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6032)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sound(569, 0, 100, 0)
    Sound(833, 0, 100, 0)
    PlayEffect(0x5, 0x2, 0x9, 0x5, 0, 1000, 0, 0, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 300, -3500, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_82(0x15E, 0x15E, 0x1388, 0x2BC)
    BeginChrThread(0x104, 3, 0, 39)
    BeginChrThread(0x102, 3, 0, 37)
    BeginChrThread(0x103, 3, 0, 38)
    BeginChrThread(0x101, 3, 0, 36)
    WaitChrThread(0xFE, 1)
    StopEffect(0x2, 0x2)
    CancelBlur(500)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    Sleep(700)
    SetChrSubChip(0xFE, 0x2)
    Sleep(75)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_5FC6 end

    def Function_36_6125(): pass

    label("Function_36_6125")

    #Sound(2029, 255, 100, 1)    #voice#Lloyd

    #C0141
    ChrTalk(
        0x101,
        "#00010F#5P……呜……！\x05\x02",
    )


    def lambda_614C():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_614C)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_36_6125 end

    def Function_37_6173(): pass

    label("Function_37_6173")

    #Sound(2129, 255, 90, 2)    #voice#Elie

    #C0142
    ChrTalk(
        0x102,
        "#00106F#12P………啊……！\x05\x02",
    )


    def lambda_619D():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_619D)
    SetChrChipByIndex(0xFE, 0x37)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_6173 end

    def Function_38_61C4(): pass

    label("Function_38_61C4")


    def lambda_61C9():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61C9)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_61C4 end

    def Function_39_61F0(): pass

    label("Function_39_61F0")


    def lambda_61F5():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61F5)
    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_39_61F0 end

    def Function_40_621C(): pass

    label("Function_40_621C")

    Fade(500)
    SetCameraDistance(10500, 500)
    Sound(533, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 100, 0)
    Sound(532, 0, 100, 0)
    Sound(833, 0, 60, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(75)
    Sound(569, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 1300, -5500, 700)
    SetCameraDistance(12500, 700)
    SetChrSubChip(0xFE, 0x2)
    Sleep(75)
    SetChrSubChip(0xFE, 0x3)
    Sound(200, 0, 100, 0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x3E8)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 1000, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x104, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 42)
    BeginChrThread(0x103, 3, 0, 43)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(500)
    CancelBlur(1500)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    Fade(250)
    SetChrSubChip(0xFE, 0x4)
    OP_0D()
    Return()

    # Function_40_621C end

    def Function_41_631F(): pass

    label("Function_41_631F")


    def lambda_6324():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6324)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2031, 255, 100, 1)    #voice#Lloyd
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFDCD8, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Sound(514, 0, 100, 0)
    Return()

    # Function_41_631F end

    def Function_42_6378(): pass

    label("Function_42_6378")


    def lambda_637D():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_637D)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2128, 255, 90, 2)    #voice#Elie
    OP_9D(0xFE, 0xFFFFFC18, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_6378 end

    def Function_43_63CB(): pass

    label("Function_43_63CB")


    def lambda_63D0():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_63D0)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2224, 255, 100, 3)    #voice#Tio
    OP_9D(0xFE, 0x3E8, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_63CB end

    def Function_44_641E(): pass

    label("Function_44_641E")


    def lambda_6423():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6423)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2764, 255, 100, 4)    #voice#Randy
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFD508, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_641E end

    def Function_45_6471(): pass

    label("Function_45_6471")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_648A")
    Sound(929, 0, 40, 0)
    Sleep(2200)
    Jump("Function_45_6471")

    label("loc_648A")

    Return()

    # Function_45_6471 end

    def Function_46_648B(): pass

    label("Function_46_648B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64A4")
    Sound(929, 0, 20, 0)
    Sleep(2200)
    Jump("Function_46_648B")

    label("loc_64A4")

    Return()

    # Function_46_648B end

    def Function_47_64A5(): pass

    label("Function_47_64A5")

    Sleep(6000)
    Sound(930, 0, 100, 0)
    Sleep(2000)
    Sound(928, 0, 100, 0)
    Return()

    # Function_47_64A5 end

    def Function_48_64B8(): pass

    label("Function_48_64B8")

    Sound(934, 0, 70, 0)
    Sleep(1500)
    Sound(934, 0, 80, 0)
    Sleep(1500)
    Sound(934, 0, 90, 0)
    Sleep(1500)
    Sound(934, 0, 100, 0)
    Sleep(1500)
    Sound(934, 0, 90, 0)
    Return()

    # Function_48_64B8 end

    def Function_49_64E3(): pass

    label("Function_49_64E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00056.itc", 0x26)
    LoadChrToIndex("chr/ch00156.itc", 0x27)
    LoadChrToIndex("chr/ch00256.itc", 0x28)
    LoadChrToIndex("chr/ch00356.itc", 0x29)
    LoadChrToIndex("chr/ch03800.itc", 0x2A)
    LoadChrToIndex("chr/ch03850.itc", 0x2B)
    LoadChrToIndex("chr/ch03900.itc", 0x2C)
    LoadChrToIndex("chr/ch41450.itc", 0x2D)
    LoadChrToIndex("chr/ch41451.itc", 0x2E)
    LoadChrToIndex("chr/ch41452.itc", 0x2F)
    LoadChrToIndex("apl/ch51533.itc", 0x30)
    LoadChrToIndex("apl/ch51534.itc", 0x31)
    SoundLoad(4069)
    SoundLoad(4070)
    SoundLoad(4058)
    SoundLoad(3326)
    SoundLoad(3523)
    SoundLoad(3524)
    SoundLoad(3525)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis411.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10200.itp")
    SetChrChipByIndex(0x101, 0x26)
    SetChrChipByIndex(0x102, 0x27)
    SetChrChipByIndex(0x103, 0x28)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, -2000, -9000, 0)
    SetChrPos(0x102, -1000, -2000, -10000, 0)
    SetChrPos(0x103, 1000, -2000, -10000, 0)
    SetChrPos(0x104, 0, -2000, -11000, 0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, 0, 3000, -2500, 180)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x2D)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x2D)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x2D)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x2D)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x13, 0, -2000, -20000, 0)
    SetChrPos(0xB, 500, -2000, -28000, 0)
    SetChrPos(0xC, 1500, -2000, -28500, 0)
    SetChrPos(0xD, 2000, -2000, -30000, 0)
    SetChrPos(0xE, 500, -2000, -29500, 0)
    SetChrPos(0xF, -500, -2000, -28000, 0)
    SetChrPos(0x10, -1500, -2000, -28500, 0)
    SetChrPos(0x11, -2000, -2000, -30000, 0)
    SetChrPos(0x12, -500, -2000, -29500, 0)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x4, 0x18)
    OP_49()
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    OP_71(0x4, 0x64, 0xC8, 0x0, 0x20)
    SetMapObjFrame(0x4, "m_face1", 0x0, 0x1)
    SetMapObjFrame(0x4, "m_face2", 0x0, 0x1)
    Call(0, 2)
    OP_68(0, 7000, 9500, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(40000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 7000, -9500, 10000)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    Call(0, 4)
    OP_68(-850, -300, -10800, 0)
    MoveCamera(32, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12770, 0)
    OP_0D()
    Sleep(300)

    #C0143
    ChrTalk(
        0x101,
        "#00010F#11P#40W………………………………\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        "#00311F#12P#30W……怎么可能……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#00106F#6P#30W………我们…………\x01",
            "难道是在做梦吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x103,
        (
            "#00208F#11P#30W很遗憾……\x01",
            "……好像是现实……\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7571", 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0147
    ChrTalk(
        0x9,
        (
            "#10503F#4069V#5P#40W#N正是如此。\x02\x03",

            "#10501F#4070V在『奇迹』发生之后，\x01",
            "等待着你们的还是现实。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFE6)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    Sound(937, 0, 50, 0)

    #N0148
    NpcTalk(
        0xB,
        "声音",
        "#1P在这里……！\x02",
    )

    CloseMessageWindow()

    #N0149
    NpcTalk(
        0xC,
        "声音",
        (
            "#1P亚里欧斯长官！\x01",
            "您没事吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -300, -7000, 0)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(0, -1000, -21000, 3000)
    MoveCamera(135, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16500, 3000)
    BeginChrThread(0xB, 3, 0, 50)
    Sleep(200)
    BeginChrThread(0xC, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0xD, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0xF, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0x10, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0x11, 3, 0, 50)
    Sleep(100)
    BeginChrThread(0x12, 3, 0, 50)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    OP_6F(0x79)

    #C0150
    ChrTalk(
        0x101,
        "#00013F#6P#N啊……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0151
    ChrTalk(
        0x104,
        "#00307F#6P#N啧……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 2)
    Fade(500)
    OP_68(0, -1000, -14000, 0)
    MoveCamera(50, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(0, -1000, -11000, 5000)
    BeginChrThread(0x101, 3, 0, 59)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 60)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 61)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 62)
    BeginChrThread(0xB, 3, 0, 51)
    Sleep(50)
    BeginChrThread(0xC, 3, 0, 52)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 53)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 54)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 56)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 58)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_0D()
    ClearChrFlags(0x13, 0x8)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #N0152
    NpcTalk(
        0x13,
        "少女的声音",
        "#3523V#30W#15A不要做无谓的抵抗。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xDC3)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0153
    ChrTalk(
        0x102,
        "#00105F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        "#00205F#5P这声音是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Call(0, 4)
    OP_68(0, -1000, -10000, 0)
    MoveCamera(180, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(0, -1000, -13000, 4000)
    BeginChrThread(0x13, 3, 0, 63)
    WaitChrThread(0x13, 3)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0155
    AnonymousTalk(
        0x13,
        (
            "#3524V#30W国防军已经完全控制了\x01",
            "米修拉姆地区。\x02\x03",

            "#3525V请你们……\x01",
            "老老实实地投降吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDC5)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0156
    ChrTalk(
        0x104,
        "#00301F#6P诺艾尔，你……\x02",
    )

    CloseMessageWindow()

    #N0157
    NpcTalk(
        0x103,
        "罗伊德",
        "#00013F#6P#N……为什么……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0158
    ChrTalk(
        0x13,
        "#10208F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -300, -7000, 0)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    Sleep(300)

    #C0159
    ChrTalk(
        0x9,
        (
            "#10503F#5P辛苦了，希卡少尉。\x02\x03",

            "#10500F我要返回兰花塔，\x01",
            "就由你来押送他们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, -1000, -14000, 2000)
    MoveCamera(150, 25, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    Fade(250)
    SetCameraDistance(16000, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x30)
    SetChrSubChip(0x13, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0160
    ChrTalk(
        0x13,
        "#10201F#11P……明白了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Call(0, 2)
    OP_68(0, -1000, -10000, 0)
    MoveCamera(0, 34, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(16000, 1000)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 64)
    Sleep(50)
    BeginChrThread(0xC, 3, 0, 65)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 66)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 67)
    CancelBlur(1500)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x10, 3)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    Call(0, 4)
    OP_68(0, -300, -7000, 0)
    OP_68(0, -1200, -10000, 6000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 3, 0, 72)
    Sleep(3000)
    OP_0D()
    Fade(500)
    OP_68(-2560, -200, -12050, 0)
    OP_68(-2560, -200, -15050, 3000)
    MoveCamera(353, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    #Sound(3326, 255, 100, 0)    #voice#Lloyd
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0161
    ChrTalk(
        0x101,
        "#00007F#11P等一下！\x02",
    )

    CloseMessageWindow()
    OP_24(0xCFE)
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0162
    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W希望你回答我一个问题，\x01",
            "一个就好……\x02\x03",

            "#00008F既然你从数年前就\x01",
            "开始与他们合作了……\x02\x03",

            "#00013F那么，杀害盖伊·班宁斯……\x01",
            "杀害我大哥的人也是你吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0163
    ChrTalk(
        0x103,
        "#00205F#11P！？\x02",
    )

    CloseMessageWindow()

    def lambda_7287():

        label("loc_7287")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7287")

    QueueWorkItem2(0x13, 2, lambda_7287)
    Sleep(300)

    #C0164
    ChrTalk(
        0x13,
        "#10205F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        "#00107F#5P这、这……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x104,
        "#00310F#11P喂，难道说……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        "#10500F#5P#40W………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 3000)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x9)
    Sleep(400)
    Fade(250)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x31)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)
    OP_C9(0x0, 0x80000000)

    #C0168
    ChrTalk(
        0x9,
        "#10503F#4058V#5P#40W#30A嗯，正是。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xFDA)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetCameraDistance(20000, 5000)
    BeginChrThread(0x9, 0, 0, 73)

    def lambda_73A2():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_73A2)
    Sleep(300)

    def lambda_73BA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_73BA)
    Sleep(700)
    StopSound(927, 1000, 80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_29(0xAD, 0x1, 0x6)
    OP_29(0xAD, 0x4, 0x10)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x21, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    ReplaceBGM(-1, -1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("t3520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_49_64E3 end

    def Function_50_74BD(): pass

    label("Function_50_74BD")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_74BD end

    def Function_51_74DD(): pass

    label("Function_51_74DD")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFFC568, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_51_74DD end

    def Function_52_751D(): pass

    label("Function_52_751D")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFEA070, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_52_751D end

    def Function_53_7557(): pass

    label("Function_53_7557")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF15A0, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_7557 end

    def Function_54_7591(): pass

    label("Function_54_7591")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF5038, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_54_7591 end

    def Function_55_75D1(): pass

    label("Function_55_75D1")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x3A98, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_55_75D1 end

    def Function_56_760B(): pass

    label("Function_56_760B")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x15F90, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_56_760B end

    def Function_57_764B(): pass

    label("Function_57_764B")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xEA60, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_57_764B end

    def Function_58_7685(): pass

    label("Function_58_7685")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xAFC8, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_58_7685 end

    def Function_59_76C5(): pass

    label("Function_59_76C5")


    def lambda_76CA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_76CA)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_59_76C5 end

    def Function_60_7701(): pass

    label("Function_60_7701")


    def lambda_7706():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7706)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(531, 0, 100, 0)
    Return()

    # Function_60_7701 end

    def Function_61_773D(): pass

    label("Function_61_773D")


    def lambda_7742():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7742)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_61_773D end

    def Function_62_7773(): pass

    label("Function_62_7773")


    def lambda_7778():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7778)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(805, 0, 100, 0)
    Return()

    # Function_62_7773 end

    def Function_63_77AF(): pass

    label("Function_63_77AF")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
    Return()

    # Function_63_77AF end

    def Function_64_77BF(): pass

    label("Function_64_77BF")

    TurnDirection(0xFE, 0x104, 500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0xA, 0x73A, 0xFA0, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 71)
    WaitChrThread(0x104, 3)
    Return()

    # Function_64_77BF end

    def Function_65_77FA(): pass

    label("Function_65_77FA")

    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0xA, 0xCB2, 0xFA0, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 68)
    WaitChrThread(0x101, 3)
    Return()

    # Function_65_77FA end

    def Function_66_7835(): pass

    label("Function_66_7835")

    TurnDirection(0xFE, 0x103, 500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x5, 0x109A, 0xFA0, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 70)
    WaitChrThread(0x103, 3)
    Return()

    # Function_66_7835 end

    def Function_67_7870(): pass

    label("Function_67_7870")

    TurnDirection(0xFE, 0x102, 500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0xFFFB, 0x9C4, 0xFA0, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 69)
    WaitChrThread(0x102, 3)
    Return()

    # Function_67_7870 end

    def Function_68_78AB(): pass

    label("Function_68_78AB")


    def lambda_78B0():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_78B0)
    Sound(2029, 255, 70, 0)    #voice#Lloyd
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_68_78AB end

    def Function_69_78E6(): pass

    label("Function_69_78E6")


    def lambda_78EB():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_78EB)
    Sound(2127, 255, 70, 1)    #voice#Elie
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_69_78E6 end

    def Function_70_7921(): pass

    label("Function_70_7921")


    def lambda_7926():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7926)
    Sound(2223, 255, 70, 2)    #voice#Tio
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_70_7921 end

    def Function_71_795C(): pass

    label("Function_71_795C")


    def lambda_7961():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7961)
    Sound(2317, 255, 70, 2)    #voice#Randy
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_71_795C end

    def Function_72_7997(): pass

    label("Function_72_7997")

    ClearChrFlags(0x9, 0x4)
    OP_9B(0x0, 0xFE, 0x14, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x1964, 0xBB8, 0x0)
    Return()

    # Function_72_7997 end

    def Function_73_79CA(): pass

    label("Function_73_79CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_79E8")
    OP_A1(0xFE, 0x5DC, 0x8, 0x1, 0x2, 0x3, 0x2, 0x1, 0x4, 0x5, 0x4)
    Jump("Function_73_79CA")

    label("loc_79E8")

    Return()

    # Function_73_79CA end

    SaveToFile()

Try(main)
