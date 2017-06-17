from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "マリアベル",             # 1
        "アリオス長官",           # 2
        "キーア",                 # 3
        "国防軍兵士",             # 4
        "国防軍兵士",             # 5
        "国防軍兵士",             # 6
        "国防軍兵士",             # 7
        "国防軍兵士",             # 8
        "国防軍兵士",             # 9
        "国防軍兵士",             # 10
        "国防軍兵士",             # 11
        "ノエル少尉",             # 12
        "映像",                   # 13
        "映像",                   # 14
        "映像",                   # 15
        "映像",                   # 16
        "映像",                   # 17
        "SE制御",                 # 18
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
        "Function_6_2B7E",         # 06, 6
        "Function_7_2BEA",         # 07, 7
        "Function_8_2C56",         # 08, 8
        "Function_9_2CBC",         # 09, 9
        "Function_10_2D28",        # 0A, 10
        "Function_11_2D4A",        # 0B, 11
        "Function_12_2D6C",        # 0C, 12
        "Function_13_2D8E",        # 0D, 13
        "Function_14_2DB0",        # 0E, 14
        "Function_15_2DD2",        # 0F, 15
        "Function_16_2DE2",        # 10, 16
        "Function_17_2DF2",        # 11, 17
        "Function_18_2E02",        # 12, 18
        "Function_19_2E12",        # 13, 19
        "Function_20_2E22",        # 14, 20
        "Function_21_2E3D",        # 15, 21
        "Function_22_2E4F",        # 16, 22
        "Function_23_38BB",        # 17, 23
        "Function_24_393E",        # 18, 24
        "Function_25_395E",        # 19, 25
        "Function_26_3988",        # 1A, 26
        "Function_27_39B2",        # 1B, 27
        "Function_28_39DC",        # 1C, 28
        "Function_29_3A1C",        # 1D, 29
        "Function_30_3A38",        # 1E, 30
        "Function_31_4448",        # 1F, 31
        "Function_32_62D1",        # 20, 32
        "Function_33_631C",        # 21, 33
        "Function_34_633B",        # 22, 34
        "Function_35_635A",        # 23, 35
        "Function_36_64B9",        # 24, 36
        "Function_37_650B",        # 25, 37
        "Function_38_6560",        # 26, 38
        "Function_39_658C",        # 27, 39
        "Function_40_65B8",        # 28, 40
        "Function_41_66BB",        # 29, 41
        "Function_42_6714",        # 2A, 42
        "Function_43_6767",        # 2B, 43
        "Function_44_67BA",        # 2C, 44
        "Function_45_680D",        # 2D, 45
        "Function_46_6827",        # 2E, 46
        "Function_47_6841",        # 2F, 47
        "Function_48_6854",        # 30, 48
        "Function_49_687F",        # 31, 49
        "Function_50_78D1",        # 32, 50
        "Function_51_78F1",        # 33, 51
        "Function_52_7931",        # 34, 52
        "Function_53_796B",        # 35, 53
        "Function_54_79A5",        # 36, 54
        "Function_55_79E5",        # 37, 55
        "Function_56_7A1F",        # 38, 56
        "Function_57_7A5F",        # 39, 57
        "Function_58_7A99",        # 3A, 58
        "Function_59_7AD9",        # 3B, 59
        "Function_60_7B15",        # 3C, 60
        "Function_61_7B51",        # 3D, 61
        "Function_62_7B87",        # 3E, 62
        "Function_63_7BC3",        # 3F, 63
        "Function_64_7BD3",        # 40, 64
        "Function_65_7C0E",        # 41, 65
        "Function_66_7C49",        # 42, 66
        "Function_67_7C84",        # 43, 67
        "Function_68_7CBF",        # 44, 68
        "Function_69_7CFA",        # 45, 69
        "Function_70_7D35",        # 46, 70
        "Function_71_7D70",        # 47, 71
        "Function_72_7DAB",        # 48, 72
        "Function_73_7DDE",        # 49, 73
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
        "#00201F#11Pこ、これは……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        "#00310F#11P……おいおい……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        "#00106F#11Pどうして……\x02",
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

    def lambda_CF9():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CF9)
    Sleep(50)

    def lambda_D11():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D11)
    Sleep(50)

    def lambda_D29():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D29)
    Sleep(50)

    def lambda_D41():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D41)
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
            "#00007F#3321V#30W#20Aキーア！\x01",
            "アリオスさん……！\x02",
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
        "#00107F#3398V#30W#15A……ベル……！\x02",
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
        "#3625V#40W……ロイド……みんな……\x02",
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
            "#10804F#3780V#5P#30Wフフ……\x01",
            "ようやく着きましたわね。\x02",
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
        "#00106F#3399V#11P#40Wベル……どうして……\x02",
    )

    CloseMessageWindow()
    OP_24(0xD47)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0011
    ChrTalk(
        0x102,
        (
            "#00107F#3400V#11P#4S#30Wどうして貴女が\x01",
            "そんな場所にいるのっ！？\x02",
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
            "#3781V#30Wフフ──簡単な事ですわ。\x02\x03",

            "#3782V《大いなる至宝》を受け継いだ\x01",
            "クロイス家の末裔として……\x02\x03",

            "#3783V当然の責務を\x01",
            "果たしているだけのこと。\x02",
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
        "#00011F#11P《大いなる至宝》……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        (
            "#00207F#11Pまさかリベールに出現したという\x01",
            "《輝く環#6Rオーリオール#》と同種の……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#10809F#5Pフフ、話が早いですわね。\x02\x03",

            "#10804F遥か昔、女神が人間に授けた\x01",
            "《七の至宝#8Rセプト＝テリオン#》……\x02\x03",

            "#10811Fそのうちの一つを、\x01",
            "我が一族は受け継いできたのです。\x02\x03",

            "まあ、１２００年前までですが。\x02",
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
        "#00306F#11Pワケが分からねぇんだが……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#10804F#5Pフフ、不幸な出来事によって\x01",
            "女神の至宝は失われたのです。\x02\x03",

            "#10803Fその結果、クロイス家の始祖は\x01",
            "何としても至宝を取り戻すため\x01",
            "途方もなく遠大な計画を構想し……\x02\x03",

            "#10800Fこのクロスベルの地に巨大な\x01",
            "《式》を構築することにしました。\x02",
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
        "#00108F#11P巨大な《式》……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        (
            "#00201F#11Pまさか導力ネットを使った\x01",
            "不可解で巨大なシステム……？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#10803F#5Pええ、現代の導力技術と\x01",
            "クロイス家の錬金術を融合させて\x01",
            "生み出された《魔導科学》……\x02\x03",

            "#10802Fそれによってようやく実現できた\x01",
            "馬鹿馬鹿しいほど巨大な《式》ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        "#00208F#11P《魔導科学》による《式》……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00110F#11Pそ、それに錬金術って……\x02",
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
            "#00006F#11P……そうか……\x01",
            "そういう事だったのか。\x02\x03",

            "#00008Fかつて《星見の塔》を建造し、\x01",
            "《教団》に技術を提供していた\x01",
            "錬金術師たちの集団……\x02\x03",

            "#00007F──あれは貴女たち\x01",
            "クロイス家の事だったんだな！？\x02",
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
        "#00305F#11Pなっ……！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00207F#11Pで、でも……\x01",
            "そう考えると辻褄が合います！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#00107F#11Pそ、それじゃあ\x01",
            "キーアちゃんが眠っていた\x01",
            "あの《揺籃#4Rゆりかご#》というのも……\x02",
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
            "#10804F#5Pフフ、もちろんクロイス家が\x01",
            "《教団》に提供したものですわ。\x02\x03",

            "#10811F──彼らに信仰対象を与え、\x01",
            "気持ちよく働いてもらうためにね。\x02",
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
            "#00013F#11Pそれじゃあやっぱり、\x01",
            "《Ｄ∴Ｇ教団》というのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00108F#11Pクロイス家の目的を達するために\x01",
            "影から誘導された……？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#10804F#5Pええ、傀儡#4Rかいらい#というわけです。\x02\x03",

            "#10811Fクク……もっとも彼ら自身に\x01",
            "その自覚はなかったでしょうけど。\x02",
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
            "#10809F#5Pフフ、おおよその背景は\x01",
            "呑み込めていただけたかしら？\x02\x03",

            "#10805F──ああ、ちなみに\x01",
            "こちらのアリオスさんは\x01",
            "我が一族とは関係ありませんわ。\x02\x03",

            "#10804F今回、わたくしたちの計画に\x01",
            "賛同してくださった\x01",
            "頼もしい協力者というわけです。\x02",
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
        "#00013F#11Pアリオスさん……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#00310F#11P……アンタ、正気か？\x01",
            "こんな妄想じみた話に……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "#10504F#5Pフ……妄想じみた話か。\x02\x03",

            "#10502F確かにその点については\x01",
            "俺も同意見だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#10801F#6Pまあ……！\x01",
            "酷いですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "#10503F#5Pだが、彼らにその力があり、\x01",
            "この状況を変えられるならば……\x02\x03",

            "俺はいくらでも\x01",
            "その幻想に付き合うだけだ。\x02\x03",

            "#10501F──たとえ女神の意志に\x01",
            "背くことになったとしてもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00108F#11Pそんな……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#00208F#11P……一体どうして……\x02",
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
            "#00006F#11P……正直、途方もない話ばかりで\x01",
            "まだ整理できていないけど……\x02\x03",

            "#00003Fただ……これだけは言える。\x02",
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
            "#00010F#11Pその妄想にキーアを巻き込むのは\x01",
            "断じて認められない！\x02",
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
            "#00007F#11P#4Sキーア、戻ってくるんだ！\x02\x03",

            "#3S何を唆#2Rそそのか#されたのか知らないけど\x01",
            "キーアは、キーアだろう！？\x02\x03",

            "そんな辛そうな顔をして……\x01",
            "そんな椅子に座る事はないんだ！\x02",
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
        "#05812F#5P#30W………ロイド…………\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#10804F#5Pウフフ……キーアさん。\x02\x03",

            "あんな風にロイドさんは\x01",
            "言ってますけど……\x02\x03",

            "#10811Fどうする#8R㈲　㈲　㈲　㈲#つもりですの？\x02",
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
        "#00011F……キーア……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 170, -1, -1)

    #A0050
    AnonymousTalk(
        0x102,
        "#00105Fど、どうしたの……？\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 170, -1, -1)

    #A0051
    AnonymousTalk(
        0x104,
        (
            "#00307F#4Sキー坊、迷うことはねえ！\x02\x03",

            "いつもみたいに\x01",
            "ロイドの胸に飛び込んで来い！\x02\x03",

            "それが一番、お前にとって\x01",
            "安心できるんだろうが！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0052
    ChrTalk(
        0xA,
        "#05812F#5P#30Wランディ……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 170, -1, -1)

    #A0053
    AnonymousTalk(
        0x102,
        (
            "#00104F……そうね。\x01",
            "事情はあるのだろうけど……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 170, -1, -1)

    #A0054
    AnonymousTalk(
        0x103,
        (
            "#00201Fそれ以上に大切なことは\x01",
            "絶対に無いと思います。\x02",
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
            "#05808F#5P#30W……エリィ……ティオ……\x02\x03",

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
    SetChrName("少年の声")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3719V#30Wウフフ……\x01",
            "盛り上がってるじゃない？\x07\x00\x02",
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
        "#00110F#11P《身喰らう蛇#10Rウ ロ ボ ロ ス#》……！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        "#00201F#11Pやはり彼らと繋がりが……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0059
    ChrTalk(
        0x8,
        (
            "#10804F#5Pフフ、お互い協力関係を\x01",
            "結んでいるだけですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)

    #C0060
    ChrTalk(
        0x8,
        (
            "#10802F#11P──皆さん。\x01",
            "もう準備は宜しいのかしら？\x02",
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
    SetChrName("ノバルティス博士")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、もちろんだとも。\x02\x03",

            "満足して貰える性能に\x01",
            "仕上がっていると思うよ？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(280, 135, -1, -1)
    SetChrName("アリアンロード")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《鐘》の準備も出来ています。\x02\x03",

            "あとはそちらの《鍵》を回すだけ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(10, 150, -1, -1)
    SetChrName("カンパネルラ")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "彼らが納得するまで\x01",
            "待っててもいいんだけど……\x02\x03",

            "そろそろ時間切れみたいだよ？\x07\x00\x02",
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
        "#10800F#11Pあらあら。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        "#10501F#5P……来るか。\x02",
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
        "#00011F#11Pな、何を言っている……？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        "#00307F#11P何が時間切れだってんだ！？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "#10503F#5P決まっている──\x02\x03",

            "#10501F帝国軍と共和国軍の侵攻だ。\x02",
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
        "#00110F#11Pあ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(100)

    #C0071
    ChrTalk(
        0x8,
        (
            "#10809F#5Pフフ、せっかくだから\x01",
            "実況するとしましょうか？\x02",
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

    def Function_6_2B7E(): pass

    label("Function_6_2B7E")


    def lambda_2B83():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B83)

    def lambda_2B98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B98)
    Sound(341, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_2B7E end

    def Function_7_2BEA(): pass

    label("Function_7_2BEA")


    def lambda_2BEF():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BEF)

    def lambda_2C04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C04)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_2BEA end

    def Function_8_2C56(): pass

    label("Function_8_2C56")


    def lambda_2C5B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C5B)

    def lambda_2C70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C70)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_8_2C56 end

    def Function_9_2CBC(): pass

    label("Function_9_2CBC")


    def lambda_2CC1():
        OP_9B(0x0, 0xFE, 0x0, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CC1)

    def lambda_2CD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CD6)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_2CBC end

    def Function_10_2D28(): pass

    label("Function_10_2D28")

    OP_71(0x0, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_10_2D28 end

    def Function_11_2D4A(): pass

    label("Function_11_2D4A")

    OP_71(0x1, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x1)
    OP_71(0x1, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_11_2D4A end

    def Function_12_2D6C(): pass

    label("Function_12_2D6C")

    OP_71(0x2, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x2)
    OP_71(0x2, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_12_2D6C end

    def Function_13_2D8E(): pass

    label("Function_13_2D8E")

    OP_71(0x3, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x3)
    OP_71(0x3, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_13_2D8E end

    def Function_14_2DB0(): pass

    label("Function_14_2DB0")

    OP_71(0x4, 0x0, 0x64, 0x0, 0x8)
    Sound(922, 0, 100, 0)
    OP_79(0x4)
    OP_71(0x4, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_14_2DB0 end

    def Function_15_2DD2(): pass

    label("Function_15_2DD2")

    OP_71(0x0, 0xF5, 0x12C, 0x0, 0x8)
    OP_79(0x0)
    Return()

    # Function_15_2DD2 end

    def Function_16_2DE2(): pass

    label("Function_16_2DE2")

    OP_71(0x1, 0xFA, 0x12C, 0x0, 0x8)
    OP_79(0x1)
    Return()

    # Function_16_2DE2 end

    def Function_17_2DF2(): pass

    label("Function_17_2DF2")

    OP_71(0x2, 0xFF, 0x12C, 0x0, 0x8)
    OP_79(0x2)
    Return()

    # Function_17_2DF2 end

    def Function_18_2E02(): pass

    label("Function_18_2E02")

    OP_71(0x3, 0x104, 0x12C, 0x0, 0x8)
    OP_79(0x3)
    Return()

    # Function_18_2E02 end

    def Function_19_2E12(): pass

    label("Function_19_2E12")

    OP_71(0x4, 0x10E, 0x12C, 0x0, 0x8)
    OP_79(0x4)
    Return()

    # Function_19_2E12 end

    def Function_20_2E22(): pass

    label("Function_20_2E22")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E3C")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_20_2E22")

    label("loc_2E3C")

    Return()

    # Function_20_2E22 end

    def Function_21_2E3D(): pass

    label("Function_21_2E3D")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_21_2E3D end

    def Function_22_2E4F(): pass

    label("Function_22_2E4F")

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
        "#00110Fそ、そんな……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 170, -1, -1)

    #A0073
    AnonymousTalk(
        0x104,
        "#00311F来やがったか……！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(130, 170, -1, -1)

    #A0074
    AnonymousTalk(
        0x103,
        (
            "#00201Fしかし、警備隊の戦力では\x01",
            "食い止めようが……\x02",
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
    SetChrName("男性の声")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──それを覆せる《鍵》が\x01",
            "彼女というわけだ。\x07\x00\x02",
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
        "#00010F#11Pディーター大統領……！\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#00107F#11P……おじさま……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 20, -1, -1)
    SetChrName("ディーター大統領")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《結社》の諸君。\x01",
            "計画への協力、感謝する。\x02\x03",

            "ベルにアリオス君も。\x01",
            "どうやら予定通りのようだね？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0079
    ChrTalk(
        0x8,
        "#10804F#5Pええ、ここまでは。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "#10503F#5P……後は彼女に\x01",
            "委ねるしかありませんね。\x02",
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
    SetChrName("ディーター大統領")

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──聞いた通りだ、キーア君。\x02\x03",

            "もう分かっているのだろう？\x02\x03",

            "この事態を何とかできるのは\x01",
            "君しかいない#12R㈲　㈲　㈲　㈲　㈲　㈲#ということを──\x02",
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
        "#05803F#5P#30W…………………（コクン）\x02",
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
        "#10811F#5Pフフ、いい子ですわね。\x02",
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

    # Function_22_2E4F end

    def Function_23_38BB(): pass

    label("Function_23_38BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_393D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38EB")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_3935")

    label("loc_38EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3910")
    OP_82(0xA, 0x1E, 0xBB8, 0x1F4)
    Jump("loc_3935")

    label("loc_3910")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3935")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_3935")

    label("loc_3935")

    Sleep(500)
    Jump("Function_23_38BB")

    label("loc_393D")

    Return()

    # Function_23_38BB end

    def Function_24_393E(): pass

    label("Function_24_393E")

    SetMapObjFrame(0xFF, "chair", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    Return()

    # Function_24_393E end

    def Function_25_395E(): pass

    label("Function_25_395E")

    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on_ani")
    Sleep(1133)
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    Return()

    # Function_25_395E end

    def Function_26_3988(): pass

    label("Function_26_3988")

    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    Return()

    # Function_26_3988 end

    def Function_27_39B2(): pass

    label("Function_27_39B2")

    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on_ani")
    Sleep(966)
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_27_39B2 end

    def Function_28_39DC(): pass

    label("Function_28_39DC")

    SetMapObjFrame(0xFF, "chair", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_obj00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col00", 0x2, "on")
    SetMapObjFrame(0xFF, "Null_col01", 0x2, "on")
    Return()

    # Function_28_39DC end

    def Function_29_3A1C(): pass

    label("Function_29_3A1C")

    Sleep(500)
    Sound(162, 0, 100, 0)
    Sleep(400)
    Sound(162, 0, 100, 0)
    Sleep(300)
    Sound(162, 0, 100, 0)
    Return()

    # Function_29_3A1C end

    def Function_30_3A38(): pass

    label("Function_30_3A38")

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
        "#00007F#11P#4S──キーア、駄目だ！\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#00107F#11Pベルも止めてちょうだい！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#00310F#11Pなんだか知らねぇが\x01",
            "見過ごせるかよ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#00201F#11Pとりあえず……\x01",
            "止めさせてもらいます！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, -800, -8500, 1000)

    def lambda_3DE1():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DE1)
    Sleep(50)

    def lambda_3DF9():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DF9)
    Sleep(50)

    def lambda_3E11():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E11)
    Sleep(50)

    def lambda_3E29():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3E29)
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

    def lambda_3F2F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F2F)
    Sleep(50)

    def lambda_3F47():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F47)
    Sleep(50)

    def lambda_3F5F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3F5F)
    Sleep(50)

    def lambda_3F77():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F77)
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
        "#00311F#4P#N《風の剣聖》……\x02",
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
            "#4055V#40W……通りたくば\x01",
            "お前たちの全てをぶつけるがいい。\x02\x03",

            "#4056Vガイや俺、セルゲイさんが\x01",
            "超えられなかった《壁》──\x02\x03",

            "#4057V#30Wそれを乗り越えられる力が\x01",
            "お前たちにあるのかを……！\x02",
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
        "#00010F#3322V#6P#N#30W#15Aくっ……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0093
    ChrTalk(
        0x104,
        "#00307F#2766V#6P#N#30W#27Aビビんな、相手は一人だ！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0094
    ChrTalk(
        0x102,
        "#00107F#3401V#6P#N#30W#20A何とか勝機を掴めれば……！\x02",
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
            "#00207F#2684V#12P#N#30W#28Aエイオンシステム全開！\x01",
            "目標を撃破します……！\x02",
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

    def lambda_4394():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4394)

    def lambda_43A9():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43A9)

    def lambda_43BE():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43BE)

    def lambda_43D3():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43D3)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_24(0x3A3)
    OP_24(0x340)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_4426")
    Battle("BattleInfo_3E0", 0x0, 0x0, 0x100, 0x3F, 0xFF)
    Jump("loc_4436")

    label("loc_4426")

    Battle("BattleInfo_39C", 0x0, 0x0, 0x100, 0x3F, 0xFF)

    label("loc_4436")

    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Return()

    # Function_30_3A38 end

    def Function_31_4448(): pass

    label("Function_31_4448")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47CE")
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
    Jump("loc_4A37")

    label("loc_47CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A2")
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
    Jump("loc_4A37")

    label("loc_48A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4976")
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
    Jump("loc_4A37")

    label("loc_4976")

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

    label("loc_4A37")

    PlayBGM("ed7572", 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FAB")
    OP_2C(0xAD, 0x5)

    #C0096
    ChrTalk(
        0x101,
        "#00002F#6P#Nや、やった……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0097
    NpcTalk(
        0x103,
        "ランディ",
        (
            "#00302F#12P#Nハッ……\x01",
            "どんなモンだっつーの！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0098
    ChrTalk(
        0x9,
        (
            "#10504F#5P……フ……\x01",
            "驚かせてくれるものだ。\x02\x03",

            "#10502Fこれならば本当に……\x01",
            "俺たちを超えられるかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        "#00105F#6P#N……え……\x02",
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
            "#00207F#12P#Nアリオスさんから\x01",
            "気配を感じません！\x02",
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

    def lambda_4CF7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CF7)
    Sleep(50)

    def lambda_4D07():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D07)
    Sleep(50)

    def lambda_4D17():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4D17)
    Sleep(50)

    def lambda_4D27():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4D27)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    #C0102
    ChrTalk(
        0x104,
        "#00310F#5P空蝉#4Rうつせみ#……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#00007F#5P#Nしまった──\x02",
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
        "#15A#10503F#11P──二の型《疾風#4Rはやて#》。\x02",
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
        "#12A#5P#10507F#5S#9A斬#2Rザン#……！\x02",
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
    Jump("loc_5225")

    label("loc_4FAB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5096")
    OP_2C(0xAD, 0x3)

    #C0106
    ChrTalk(
        0x101,
        (
            "#00010F#11P#30Wくっ……\x01",
            "……ここまで来て……！\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#00310F#11P#30Wこのまま……\x01",
            "終われるかっつーの……！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "#10504F#5P……成長したものだ。\x02\x03",

            "#10502Fお前たちならいつか……\x01",
            "俺たちを超えられるかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5225")

    label("loc_5096")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5177")
    OP_2C(0xAD, 0x1)

    #C0109
    ChrTalk(
        0x101,
        "#00006F#11P#30Wくっ……はあはあ……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#00206F#11P#30W戦闘力が……\x01",
            "……違いすぎます……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#10503F#5P悪くはないが、\x01",
            "真っ直ぐすぎるようだな。\x02\x03",

            "#10501Fそれでは俺たちの\x01",
            "ニの舞になりかねんぞ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5225")

    label("loc_5177")


    #C0112
    ChrTalk(
        0x101,
        "#00006F#11P#40W……ぐうっ………\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        (
            "#00106F#11P#40Wこ、ここまで\x01",
            "相手にならないなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "#10503F#5P精進不足だな。\x02\x03",

            "#10500Fその体たらくで\x01",
            "大切なものは守れんぞ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5225")

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
        "#05807F#3626V#5P#4S#30W#13Aみんな……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0116
    ChrTalk(
        0x8,
        (
            "#10804F#6P#Nフフ、峰打ちでしょう。\x02\x03",

            "#10811F集中力を途切らせたら\x01",
            "上手く行きませんわよ？\x02",
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
            "#05806F#3627V#5P#40W#32A……分かった……\x02\x03",

            "#32A#05801F#3628V#30Wもう……\x01",
            "迷ったりしないから……！\x02",
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
        "#00107F#3402V#30W#18Aキ、キーアちゃん……！？\x02",
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
        "#00007F#3323V#4S#18A#30Wやめろおおおおっ……！\x02",
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
        "#00106F#11Pきゃあああっ……！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#00010F#11Pこ、この光は……！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        "#00310F#11P一体なんなんだ……！？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#00210F#11P凄まじい密度を持った\x01",
            "七属性の霊子情報……！\x02",
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
        "#00005F………ぁ…………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 170, -1, -1)

    #A0126
    AnonymousTalk(
        0x102,
        "#00105Fキーア……ちゃん……？\x02",
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
            "#10804F#3784V#40W……ウフフ…………\x01",
            "成功しましたわね……\x02\x03",

            "#10811F#3785V喪われし《幻の至宝》の再現……\x02\x03",

            "#10809F#3786V#30Wいいえ、それすら凌駕する\x01",
            "《零#2Rゼロ#の至宝》の誕生ですわ！\x02",
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
        "#00201Fぜ、《零の至宝》……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 170, -1, -1)

    #A0129
    AnonymousTalk(
        0x104,
        "#00310Fな、何だそりゃ……\x02",
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
            "#3629V#40Wロイド………みんな…………\x07\x00\x02",
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
            "#00011F#3324V#40W………っ……………\x02\x03",

            "#00013F#3325V#40W………キーア……………\x01",
            "本当に……キーアなのか……？\x02",
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
            "#12303F#40W#5Pうん……\x07\x00\x02",
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
            "#12315F#40W#11P……ベル、行こう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(100, 170, -1, -1)

    #A0134
    AnonymousTalk(
        0x101,
        "#00005F#30Wえ……\x02",
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
            "#10804F#11Pフフ、分かりましたわ。\x02\x03",

            "#10800Fアリオスさん。\x01",
            "ここはお任せします。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        "#10503F#11P……承知した。\x02",
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

    def lambda_5F8F():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5F8F)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1000)

    def lambda_5FB5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5FB5)
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
        "#00205F#2685V#11P#30W#12Aキーア……！？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0138
    ChrTalk(
        0x104,
        "#00307F#2767V#11P#30W#20Aおい、どこに……！\x02",
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
            "#12304F#3630V#5P#40W#5P#40Aゴメンね。\x01",
            "……今までありがとう。\x07\x00\x02",
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
            "#12302F#3631V#40W#5P#30A大好きだよ──みんな。\x07\x00\x02",
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

    # Function_31_4448 end

    def Function_32_62D1(): pass

    label("Function_32_62D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_631B")
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 8000, 8000, 8000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    Jump("Function_32_62D1")

    label("loc_631B")

    Return()

    # Function_32_62D1 end

    def Function_33_631C(): pass

    label("Function_33_631C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_633A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x30, 0x31, 0x32, 0x31, 0x30, 0x33, 0x34, 0x33)
    Jump("Function_33_631C")

    label("loc_633A")

    Return()

    # Function_33_631C end

    def Function_34_633B(): pass

    label("Function_34_633B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6359")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_34_633B")

    label("loc_6359")

    Return()

    # Function_34_633B end

    def Function_35_635A(): pass

    label("Function_35_635A")

    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    PlayEffect(0x5, 0x2, 0x9, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x2EE0, 0x1)
    StopEffect(0x2, 0x2)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    def lambda_63C6():
        OP_9B(0x1, 0xFE, 0x0, 0x1964, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63C6)
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

    # Function_35_635A end

    def Function_36_64B9(): pass

    label("Function_36_64B9")

    #Sound(2029, 255, 100, 1)    #voice#Lloyd

    #C0141
    ChrTalk(
        0x101,
        "#00010F#5P……うぐっ……！\x05\x02",
    )


    def lambda_64E4():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64E4)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_36_64B9 end

    def Function_37_650B(): pass

    label("Function_37_650B")

    #Sound(2129, 255, 90, 2)    #voice#Elie

    #C0142
    ChrTalk(
        0x102,
        "#00106F#12P………あうっ……！\x05\x02",
    )


    def lambda_6539():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6539)
    SetChrChipByIndex(0xFE, 0x37)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_650B end

    def Function_38_6560(): pass

    label("Function_38_6560")


    def lambda_6565():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6565)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_6560 end

    def Function_39_658C(): pass

    label("Function_39_658C")


    def lambda_6591():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6591)
    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_39_658C end

    def Function_40_65B8(): pass

    label("Function_40_65B8")

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

    # Function_40_65B8 end

    def Function_41_66BB(): pass

    label("Function_41_66BB")


    def lambda_66C0():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_66C0)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2031, 255, 100, 1)    #voice#Lloyd
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFDCD8, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Sound(514, 0, 100, 0)
    Return()

    # Function_41_66BB end

    def Function_42_6714(): pass

    label("Function_42_6714")


    def lambda_6719():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6719)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2128, 255, 90, 2)    #voice#Elie
    OP_9D(0xFE, 0xFFFFFC18, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_6714 end

    def Function_43_6767(): pass

    label("Function_43_6767")


    def lambda_676C():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_676C)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2224, 255, 100, 3)    #voice#Tio
    OP_9D(0xFE, 0x3E8, 0xFFFFF830, 0xFFFFD8F0, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_6767 end

    def Function_44_67BA(): pass

    label("Function_44_67BA")


    def lambda_67BF():
        OP_A6(0xFE, 0x96, 0x96, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_67BF)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Sound(2764, 255, 100, 4)    #voice#Randy
    OP_9D(0xFE, 0x0, 0xFFFFF830, 0xFFFFD508, 0x9C4, 0x7D0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_67BA end

    def Function_45_680D(): pass

    label("Function_45_680D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6826")
    Sound(929, 0, 40, 0)
    Sleep(2200)
    Jump("Function_45_680D")

    label("loc_6826")

    Return()

    # Function_45_680D end

    def Function_46_6827(): pass

    label("Function_46_6827")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6840")
    Sound(929, 0, 20, 0)
    Sleep(2200)
    Jump("Function_46_6827")

    label("loc_6840")

    Return()

    # Function_46_6827 end

    def Function_47_6841(): pass

    label("Function_47_6841")

    Sleep(6000)
    Sound(930, 0, 100, 0)
    Sleep(2000)
    Sound(928, 0, 100, 0)
    Return()

    # Function_47_6841 end

    def Function_48_6854(): pass

    label("Function_48_6854")

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

    # Function_48_6854 end

    def Function_49_687F(): pass

    label("Function_49_687F")

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
        "#00311F#12P#30W……あり得ないだろ……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#00106F#6P#30W………私たち…………\x01",
            "夢でも見ているの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x103,
        (
            "#00208F#11P#30W残念ながら……\x01",
            "……現実みたいです……\x02",
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
            "#10503F#4069V#5P#40W#N──その通りだ。\x02\x03",

            "#10501F#4070V《奇蹟》の後にも\x01",
            "現実は待ち受けている。\x02",
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
        "声",
        "#1Pいたぞ……！\x02",
    )

    CloseMessageWindow()

    #N0149
    NpcTalk(
        0xC,
        "声",
        (
            "#1Pアリオス長官！\x01",
            "ご無事ですか！\x02",
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
        "#00013F#6P#Nあ──！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0151
    ChrTalk(
        0x104,
        "#00307F#6P#Nチッ……！\x02",
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
        "娘の声",
        "#3523V#30W#15A──抵抗は無駄です。\x02",
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
        "#00105F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        "#00205F#5Pこの声は……！\x02",
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
            "#3524V#30W既にミシュラム一帯は\x01",
            "国防軍が制圧しています。\x02\x03",

            "#3525Vどうか……\x01",
            "大人しく投降してください。\x02",
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
        "#00301F#6Pノエル、お前……\x02",
    )

    CloseMessageWindow()

    #N0157
    NpcTalk(
        0x103,
        "ロイド",
        "#00013F#6P#N……どうして……\x02",
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
            "#10503F#5P──ご苦労、シーカー少尉。\x02\x03",

            "#10500F私はオルキスタワーに戻る。\x01",
            "彼らの拘束は任せたぞ。\x02",
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
        "#10201F#11P……了解しました……！\x02",
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
        "#00007F#11P──待って下さい！\x02",
    )

    CloseMessageWindow()
    OP_24(0xCFE)
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0162
    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W……一つだけ……\x01",
            "どうか一つだけ答えて欲しい。\x02\x03",

            "#00008Fもし貴方が、数年前から\x01",
            "彼らに協力していたのなら……\x02\x03",

            "#00013Fガイ・バニングスを──\x01",
            "兄貴を殺したのも貴方なのか？\x02",
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

    def lambda_7689():

        label("loc_7689")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7689")

    QueueWorkItem2(0x13, 2, lambda_7689)
    Sleep(300)

    #C0164
    ChrTalk(
        0x13,
        "#10205F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        "#00107F#5Pそ、それって……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x104,
        "#00310F#11Pおい、まさか……\x02",
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
        "#10503F#4058V#5P#40W#30Aああ──その通りだ。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xFDA)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetCameraDistance(20000, 5000)
    BeginChrThread(0x9, 0, 0, 73)

    def lambda_77B6():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_77B6)
    Sleep(300)

    def lambda_77CE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_77CE)
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

    # Function_49_687F end

    def Function_50_78D1(): pass

    label("Function_50_78D1")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_78D1 end

    def Function_51_78F1(): pass

    label("Function_51_78F1")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFFC568, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_51_78F1 end

    def Function_52_7931(): pass

    label("Function_52_7931")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFEA070, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_52_7931 end

    def Function_53_796B(): pass

    label("Function_53_796B")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF15A0, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_796B end

    def Function_54_79A5(): pass

    label("Function_54_79A5")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xFFFF5038, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_54_79A5 end

    def Function_55_79E5(): pass

    label("Function_55_79E5")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x3A98, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_55_79E5 end

    def Function_56_7A1F(): pass

    label("Function_56_7A1F")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0x15F90, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_56_7A1F end

    def Function_57_7A5F(): pass

    label("Function_57_7A5F")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xEA60, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_57_7A5F end

    def Function_58_7A99(): pass

    label("Function_58_7A99")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x1)
    OP_9E(0xFE, 0x0, 0xFFFFD8F0, 0xAFC8, 0xFA0, 0x2)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 70, 0)
    Return()

    # Function_58_7A99 end

    def Function_59_7AD9(): pass

    label("Function_59_7AD9")


    def lambda_7ADE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7ADE)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_59_7AD9 end

    def Function_60_7B15(): pass

    label("Function_60_7B15")


    def lambda_7B1A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B1A)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(531, 0, 100, 0)
    Return()

    # Function_60_7B15 end

    def Function_61_7B51(): pass

    label("Function_61_7B51")


    def lambda_7B56():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B56)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_61_7B51 end

    def Function_62_7B87(): pass

    label("Function_62_7B87")


    def lambda_7B8C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B8C)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(805, 0, 100, 0)
    Return()

    # Function_62_7B87 end

    def Function_63_7BC3(): pass

    label("Function_63_7BC3")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
    Return()

    # Function_63_7BC3 end

    def Function_64_7BD3(): pass

    label("Function_64_7BD3")

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

    # Function_64_7BD3 end

    def Function_65_7C0E(): pass

    label("Function_65_7C0E")

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

    # Function_65_7C0E end

    def Function_66_7C49(): pass

    label("Function_66_7C49")

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

    # Function_66_7C49 end

    def Function_67_7C84(): pass

    label("Function_67_7C84")

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

    # Function_67_7C84 end

    def Function_68_7CBF(): pass

    label("Function_68_7CBF")


    def lambda_7CC4():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7CC4)
    Sound(2029, 255, 70, 0)    #voice#Lloyd
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_68_7CBF end

    def Function_69_7CFA(): pass

    label("Function_69_7CFA")


    def lambda_7CFF():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7CFF)
    Sound(2127, 255, 70, 1)    #voice#Elie
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_69_7CFA end

    def Function_70_7D35(): pass

    label("Function_70_7D35")


    def lambda_7D3A():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7D3A)
    Sound(2223, 255, 70, 2)    #voice#Tio
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_70_7D35 end

    def Function_71_7D70(): pass

    label("Function_71_7D70")


    def lambda_7D75():
        OP_A6(0xFE, 0x0, 0x5A, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7D75)
    Sound(2317, 255, 70, 2)    #voice#Randy
    Sleep(150)
    Fade(250)
    Sound(811, 0, 70, 0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    WaitChrThread(0x104, 2)
    Return()

    # Function_71_7D70 end

    def Function_72_7DAB(): pass

    label("Function_72_7DAB")

    ClearChrFlags(0x9, 0x4)
    OP_9B(0x0, 0xFE, 0x14, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x1964, 0xBB8, 0x0)
    Return()

    # Function_72_7DAB end

    def Function_73_7DDE(): pass

    label("Function_73_7DDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DFC")
    OP_A1(0xFE, 0x5DC, 0x8, 0x1, 0x2, 0x3, 0x2, 0x1, 0x4, 0x5, 0x4)
    Jump("Function_73_7DDE")

    label("loc_7DFC")

    Return()

    # Function_73_7DDE end

    SaveToFile()

Try(main)
