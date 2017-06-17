from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r4090.bin",                # FileName
        "r4090",                    # MapName
        "r4090",                    # Location
        0x00A6,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x26,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 166, 0, 0, 0, 1],
    )

    BuildStringList((
        "r4090",                  # 0
        "警备队员",               # 1
        "警备队员",               # 2
        "警备队员",               # 3
        "警备队员",               # 4
        "警备队员",               # 5
        "警备队员",               # 6
        "魔人瓦鲁多",             # 7
        "米蕾优三尉",             # 8
        "国防军士兵",             # 9
        "国防军士兵",             # 10
        "国防军士兵",             # 11
        "国防军士兵",             # 12
        "国防军士兵",             # 13
        "国防军士兵",             # 14
        "国防军士兵",             # 15
        "国防军队长",             # 16
        "蔡特",                   # 17
        "倒下的树木",             # 18
        "倒下的树木",             # 19
        "倒下的树木",             # 20
        "通用模型",               # 21
        "SE控制",                 # 22
        "br4020",                 # 23
        "br4020",                 # 24
    ))

    ATBonus("ATBonus_32C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3EC", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 5, 5, 45)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_450", 0x11C2, 0, 6, 0, 0, 255, 0, 0, "br4020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_3CC", "ed7455", "ed7453", "ATBonus_32C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_40C", 0x00E2, 0, 6, 0, 0, 255, 0, 0, "br4020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_3CC", "ed7455", "ed7453", "ATBonus_32C"),
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1464, 0)                                       # 0

    ScpFunction((
        "Function_0_5B8",          # 00, 0
        "Function_1_5F3",          # 01, 1
        "Function_2_62C",          # 02, 2
        "Function_3_1CC4",         # 03, 3
        "Function_4_1CEC",         # 04, 4
        "Function_5_1D14",         # 05, 5
        "Function_6_1D3C",         # 06, 6
        "Function_7_1D64",         # 07, 7
        "Function_8_1D8C",         # 08, 8
        "Function_9_1DB4",         # 09, 9
        "Function_10_1DC5",        # 0A, 10
        "Function_11_1DE5",        # 0B, 11
        "Function_12_1E09",        # 0C, 12
        "Function_13_1E29",        # 0D, 13
        "Function_14_1E6F",        # 0E, 14
        "Function_15_3A9D",        # 0F, 15
        "Function_16_3AC7",        # 10, 16
        "Function_17_3AF1",        # 11, 17
        "Function_18_3BA7",        # 12, 18
        "Function_19_3C69",        # 13, 19
        "Function_20_3D15",        # 14, 20
        "Function_21_3DBB",        # 15, 21
        "Function_22_3E5B",        # 16, 22
        "Function_23_3F07",        # 17, 23
        "Function_24_3FBD",        # 18, 24
        "Function_25_40F0",        # 19, 25
        "Function_26_4110",        # 1A, 26
        "Function_27_4130",        # 1B, 27
        "Function_28_4150",        # 1C, 28
        "Function_29_4170",        # 1D, 29
        "Function_30_4190",        # 1E, 30
        "Function_31_41B0",        # 1F, 31
        "Function_32_41DA",        # 20, 32
        "Function_33_41FE",        # 21, 33
        "Function_34_4222",        # 22, 34
        "Function_35_4246",        # 23, 35
        "Function_36_426A",        # 24, 36
        "Function_37_428E",        # 25, 37
        "Function_38_42BD",        # 26, 38
        "Function_39_42E6",        # 27, 39
        "Function_40_430F",        # 28, 40
        "Function_41_4338",        # 29, 41
        "Function_42_4361",        # 2A, 42
        "Function_43_438A",        # 2B, 43
        "Function_44_43B3",        # 2C, 44
        "Function_45_43D6",        # 2D, 45
        "Function_46_6035",        # 2E, 46
        "Function_47_6077",        # 2F, 47
        "Function_48_60B9",        # 30, 48
        "Function_49_60FB",        # 31, 49
        "Function_50_613D",        # 32, 50
        "Function_51_617F",        # 33, 51
        "Function_52_61D5",        # 34, 52
        "Function_53_6217",        # 35, 53
        "Function_54_6259",        # 36, 54
        "Function_55_6267",        # 37, 55
        "Function_56_627D",        # 38, 56
        "Function_57_62B3",        # 39, 57
        "Function_58_6308",        # 3A, 58
        "Function_59_6408",        # 3B, 59
        "Function_60_6516",        # 3C, 60
        "Function_61_6535",        # 3D, 61
        "Function_62_657A",        # 3E, 62
        "Function_63_65B8",        # 3F, 63
        "Function_64_65DD",        # 40, 64
        "Function_65_6628",        # 41, 65
        "Function_66_66FB",        # 42, 66
        "Function_67_6791",        # 43, 67
        "Function_68_67B0",        # 44, 68
        "Function_69_689A",        # 45, 69
        "Function_70_694D",        # 46, 70
        "Function_71_6A00",        # 47, 71
        "Function_72_6A1D",        # 48, 72
    ))


    def Function_0_5B8(): pass

    label("Function_0_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C9")
    Event(0, 2)

    label("loc_5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5E0")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 14)
    Jump("loc_5F2")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_5F2")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 45)

    label("loc_5F2")

    Return()

    # Function_0_5B8 end

    def Function_1_5F3(): pass

    label("Function_1_5F3")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF3C4169), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_616")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x246), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_62B")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_62B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_62B")

    Return()

    # Function_1_5F3 end

    def Function_2_62C(): pass

    label("Function_2_62C")

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
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    LoadChrToIndex("chr/ch00056.itc", 0x2A)
    LoadChrToIndex("chr/ch00156.itc", 0x2B)
    LoadChrToIndex("chr/ch00256.itc", 0x2C)
    LoadChrToIndex("chr/ch00356.itc", 0x2D)
    LoadChrToIndex("chr/ch0295F.itc", 0x2E)
    LoadChrToIndex("chr/ch03056.itc", 0x2F)
    LoadEffect(0x0, "event/ev10008.eff")
    LoadEffect(0x1, "event\\ev15010.eff")
    LoadEffect(0x2, "event/ev14006.eff")
    SoundLoad(2914)
    SoundLoad(3571)
    SoundLoad(3572)
    SoundLoad(3573)
    SoundLoad(3574)
    SoundLoad(3576)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x0, 0xE)
    OP_49()
    SetChrPos(0xE, -5000, 0, 2000, 90)
    OP_D5(0xE, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_7C2")
    SetChrPos(0x101, -2000, 0, 1550, 270)
    SetChrPos(0x102, -1600, 0, 2550, 270)
    SetChrPos(0x103, -200, 0, 1750, 270)
    SetChrPos(0x104, -350, 0, 3100, 270)
    SetChrPos(0x109, -400, 0, 750, 270)
    SetChrPos(0x105, 850, 0, 2350, 270)
    Jump("loc_828")

    label("loc_7C2")

    SetChrPos(0x101, 11000, 0, 1550, 270)
    SetChrPos(0x102, 11400, 0, 2550, 270)
    SetChrPos(0x103, 12800, 0, 1750, 270)
    SetChrPos(0x104, 12650, 0, 3100, 270)
    SetChrPos(0x109, 12600, 0, 750, 270)
    SetChrPos(0x105, 13850, 0, 2350, 270)

    label("loc_828")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_855")
    FadeToBright(0, 0)
    Jump("loc_EE9")

    label("loc_855")

    FadeToBright(1000, 0)
    OP_68(-2000, 15700, 2000, 0)
    MoveCamera(345, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(28000, 0)
    OP_68(-2000, 700, 2000, 15000)
    MoveCamera(315, 25, 0, 15000)
    SetCameraDistance(56000, 15000)
    Sleep(7000)

    def lambda_8B9():
        OP_9B(0x0, 0x101, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8B9)
    Sleep(50)

    def lambda_8D1():
        OP_9B(0x0, 0x102, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8D1)
    Sleep(50)

    def lambda_8E9():
        OP_9B(0x0, 0x103, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8E9)
    Sleep(50)

    def lambda_901():
        OP_9B(0x0, 0x104, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_901)
    Sleep(50)

    def lambda_919():
        OP_9B(0x0, 0x109, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_919)
    Sleep(50)

    def lambda_931():
        OP_9B(0x0, 0x105, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_931)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(-1000, 700, 2000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0001
    ChrTalk(
        0x105,
        "#10308F#12P……来到一处广阔的场所呢。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00001F#5P我以前训练的时候，\x01",
            "最远也只到过这附近……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(500)

    #C0003
    ChrTalk(
        0x101,
        (
            "#00005F#5P哎……？\x01",
            "这里已经是尽头了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x109,
        (
            "#10101F#6P不，前方应该还有\x01",
            "偏僻的荒道。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00303F#11P不过，倒下的树木\x01",
            "把路堵住了……\x02\x03",

            "#00301F这些树大概是一个月前倒掉的。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#00108F#12P既、既然如此，\x01",
            "那个魔兽究竟去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        (
            "#00208F#12P……我似乎感应\x01",
            "到了某种气息……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3574, 255, 100, 0)    #voice#Wald
    Sound(833, 0, 40, 0)
    StopBGM(0xFA0)
    Fade(1500)
    SetCameraDistance(19000, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x10E, 0x1F4)

    #C0008
    ChrTalk(
        0x101,
        "#00011F#5P！？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        "#00305F#11P笑声……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(30, 15, -1, -1)
    SetChrName("诡异的声音")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3571V#40W#53A哼哼……一群蠢货，\x01",
            "竟然大摇大摆地一起过来……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    SetChrName("诡异的声音")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3572V#40W#30A你们还是和以前一样头脑简单……\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    Fade(500)
    OP_68(-1000, 1000, 2000, 0)
    MoveCamera(225, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(35000, 0)
    OP_68(-1000, 1000, 2000, 10000)
    MoveCamera(270, 15, 0, 10000)
    SetCameraDistance(16650, 10000)
    OP_0D()

    #C0012
    ChrTalk(
        0x101,
        "#00013F#5P这、这……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        (
            "#10107F#5P难道是……\x01",
            "操控魔兽的犯人……？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        "#00208F#6P不、不对……更重要的是……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#00101F#5P这声音……\x01",
            "似乎曾在哪里听到过……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        "#10310F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        "#00310F#12P喂喂，难道──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-1000, 1000, 2000, 500)
    MoveCamera(270, 15, 0, 500)
    SetCameraDistance(15650, 500)
    OP_6F(0x79)
    CancelBlur(0)
    OP_0D()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0018
    ChrTalk(
        0x105,
        "#10307F#2914V#6P#4S#11A来了──快退后！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    #C0019
    ChrTalk(
        0x101,
        "#00010F#5P！！#8A\x02",
    )
    #Auto

    CloseMessageWindow()

    label("loc_EE9")

    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0xE, -22000, 17000, 15000, 135)
    OP_D5(0xE, 0x0, 0x20F58, 0x0, 0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x393, 0x3A2, 0x1, 0x8)
    Sound(3552, 255, 100, 0)    #voice#Wald
    Sound(200, 0, 50, 0)
    Sound(251, 0, 100, 0)
    OP_68(-22000, 22000, 15000, 0)
    MoveCamera(315, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(10000, 0)
    OP_68(-3000, 1300, 2000, 2300)
    MoveCamera(315, 20, 0, 2300)
    SetCameraDistance(18500, 2300)
    Sound(834, 0, 100, 0)

    def lambda_FC8():
        OP_9D(0xFE, 0xFFFFE4A8, 0xFFFFFE70, 0x1388, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_FC8)
    Sleep(1500)
    Sound(893, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3A3, 0x3A7, 0x1, 0x8)
    Sound(3544, 255, 100, 0)    #voice#Wald
    Sleep(300)
    Sound(833, 0, 100, 0)
    Sound(248, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xE, 0x5, 0, 1000, 3000, 0, 0, 0, 1500, 2500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xE, 0x5, 0, 2500, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x12C, 0x1388, 0x7D0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x102, 3, 0, 4)
    BeginChrThread(0x103, 3, 0, 5)
    BeginChrThread(0x104, 3, 0, 6)
    BeginChrThread(0x109, 3, 0, 7)
    BeginChrThread(0x105, 3, 0, 8)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_82(0x96, 0x5A, 0x1388, 0x3E8)
    SetChrPos(0xE, -6000, 0, 0, 135)
    OP_D5(0xE, 0x0, 0x20F58, 0x0, 0x0)
    BeginChrThread(0xE, 3, 0, 9)
    SetChrFlags(0xE, 0x1)
    OP_68(-6000, 2300, 300, 0)
    MoveCamera(200, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(7800, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0xA)
    OP_68(-1350, 1300, 300, 3000)
    MoveCamera(115, 18, 0, 3000)
    SetCameraDistance(12800, 3000)
    Sleep(500)
    CancelBlur(1000)
    OP_6F(0x79)
    OP_0D()

    #C0020
    ChrTalk(
        0x101,
        "#00007F#5P什么！？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        "#10107F#5P鬼、鬼……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(280, 150, -1, -1)
    SetChrName("鬼")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3573V#50W#20A……哼哼哼…………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0x3E8, 0x3E8)
    SetChrName("鬼")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3574V#40W#4S#26A………哇哈哈哈哈哈哈哈………\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    Sound(889, 0, 40, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrPos(0xE, -5000, 0, 2000, 90)
    OP_D5(0xE, 0x0, 0x15F90, 0x0, 0x0)
    EndChrThread(0xE, 0x3)
    OP_74(0x0, 0x5)
    OP_68(-5000, 2100, 2000, 0)
    MoveCamera(180, 51, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13650, 0)
    OP_68(-5000, 4000, 2000, 5000)
    MoveCamera(270, -10, 0, 5000)
    SetCameraDistance(7350, 5000)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_71(0x0, 0x3DE, 0x3F2, 0x1, 0x8)
    OP_79(0x0)
    CancelBlur(0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x41A, 0x442, 0x1, 0x8)
    Sound(892, 0, 100, 0)
    Sleep(1300)
    Sound(892, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(30, 160, -1, -1)

    #A0024
    AnonymousTalk(
        0x102,
        "#00107F………唔…………！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)

    #A0025
    AnonymousTalk(
        0x103,
        "#00201F这、这是……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 160, -1, -1)

    #A0026
    AnonymousTalk(
        0x109,
        (
            "#10110F难道和那些通过服用『真知』\x01",
            "而魔人化的人一样……！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)

    #A0027
    AnonymousTalk(
        0x104,
        "#00311F你……难道是……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(30, 160, -1, -1)

    #A0028
    AnonymousTalk(
        0x101,
        (
            "#00007F瓦鲁多——\x01",
            "是你吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    Sleep(300)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("鬼")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#51A#3S#3576V#50W哼哼哼…#1500W…\x01",
            "#40W#5S哈哈哈哈哈哈哈哈哈哈！\x07\x00\x02",
        )
    )
    #Auto

    Sleep(1600)
    Fade(300)
    Sound(196, 0, 70, 0)
    Sound(200, 0, 60, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x64, 0xC8, 0xBB8, 0x7D0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(1200)
    OP_68(-5000, 3500, 2000, 1000)
    MoveCamera(270, 40, 0, 1000)
    SetCameraDistance(16000, 1000)
    BeginChrThread(0xE, 3, 0, 10)
    WaitChrThread(0xE, 3)
    OP_82(0x1F4, 0x0, 0xBB8, 0x4B0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    EndChrThread(0xE, 0x3)
    BeginChrThread(0xE, 3, 0, 11)
    OP_68(-1740, 2600, 2210, 0)
    MoveCamera(295, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14050, 0)
    SetCameraDistance(12750, 1500)
    OP_6F(0x79)
    OP_0D()
    SetMessageWindowPos(10, 80, -1, -1)

    #A0030
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W班宁斯，还有奥兰多……\x01",
            "真是好久不见了啊。\x02\x03",

            "#30W哼哼……\x01",
            "还有你……瓦吉。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0031
    ChrTalk(
        0x105,
        (
            "#10306F#12P#N嗯……是啊。\x02\x03",

            "#10308F虽然我早就知道\x01",
            "你的品位很低级……\x02\x03",

            "#10310F但这次未免\x01",
            "也太过火了吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 80, -1, -1)

    #A0032
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#30W哼哼……废话少说。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0033
    ChrTalk(
        0x101,
        "#00010F#4P#N稍、稍等一下！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10107F#4P#N如、如此说来，\x01",
            "是你使列车脱轨的……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(10, 80, -1, -1)

    #A0035
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W哼哼……这么显而易见的事情，\x01",
            "有必要多此一举地确认吗……？\x02\x03",

            "#30W那些弱小的魔兽\x01",
            "又怎能做到那种事……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-5000, 4200, 2000, 0)
    MoveCamera(270, 0, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(7000, 0)
    Sound(892, 0, 100, 0)
    Sound(200, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xE, 0x5, 0, 500, 0, 0, 0, 0, 2000, 2500, 2000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-500, 2300, 2000, 1000)
    MoveCamera(270, 14, 0, 1000)
    SetCameraDistance(23000, 1000)
    EndChrThread(0xE, 0x3)
    BeginChrThread(0xE, 3, 0, 12)
    Sleep(500)
    CancelBlur(500)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(-1, 110, -1, -1)

    #A0036
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S只有得到了新力量的我──\x01",
            "瓦鲁多·瓦雷斯才办得到啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-2000, 2500, 2000, 0)
    MoveCamera(60, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    MoveCamera(50, 24, 0, 10000)
    OP_0D()

    #C0037
    ChrTalk(
        0x103,
        "#00210F#11P唔……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        "#00108F#11P好惊人的鬼气……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#00310F#11P事情好像麻烦了……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 150, -1, -1)

    #A0040
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W好了，既然你们特意\x01",
            "追寻到这种地方……\x02",
        )
    )

    CloseMessageWindow()

    #A0041
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W我们就赶快开始吧……？\x02",
        )
    )

    CloseMessageWindow()

    #A0042
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W如今的我到底有多么强大……\x01",
            "就让你们切身体会一番……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0043
    ChrTalk(
        0x101,
        "#00010F#11P唔……！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x105,
        "#10301F#11P……看来是认真的。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5000, 3200, 2000, 0)
    MoveCamera(270, 0, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18250, 0)
    OP_68(-5000, 4500, 2000, 2000)
    SetCameraDistance(8250, 2000)
    MoveCamera(270, 15, 0, 2000)
    StopBGM(0xFA0)
    EndChrThread(0xE, 0x3)
    Sound(889, 0, 70, 0)
    BeginChrThread(0xE, 3, 0, 13)
    Sleep(500)
    StopSound(889, 1000, 70)
    CancelBlur(500)
    Sleep(1500)
    SetMessageWindowPos(260, 160, -1, -1)

    #A0045
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W哼哼，现在收拾你们这种货色，\x01",
            "根本就不需要拿出真正实力……\x02\x03",

            "#30W我下手一定会轻些，\x01",
            "尽量不把你们打死……\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(6730, 500)
    OP_6F(0x79)
    CancelBlur(0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7455", 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)

    #A0046
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S让你们好好体会我\x01",
            "如今的真正力量！！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-5000, 5800, 2000, 0)
    MoveCamera(270, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    OP_68(-5000, 1500, 2000, 500)
    SetCameraDistance(23000, 500)
    EndChrThread(0xE, 0x3)
    Sound(893, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x3A3, 0x3A7, 0x1, 0x8)
    Sleep(300)
    Sound(833, 0, 100, 0)
    Sound(196, 0, 100, 0)
    OP_82(0x0, 0x64, 0x1388, 0x1F4)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(500)
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_1CA6")
    Battle("BattleInfo_450", 0x30200011, 0x0, 0x100, 0x13, 0xFF)
    Jump("loc_1CB6")

    label("loc_1CA6")

    Battle("BattleInfo_40C", 0x30200011, 0x0, 0x100, 0x13, 0xFF)

    label("loc_1CB6")

    FadeToDark(0, 0, -1)
    Call(0, 14)
    Return()

    # Function_2_62C end

    def Function_3_1CC4(): pass

    label("Function_3_1CC4")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x1F4, 0xDAC)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_3_1CC4 end

    def Function_4_1CEC(): pass

    label("Function_4_1CEC")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x258, 0xBB8)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_4_1CEC end

    def Function_5_1D14(): pass

    label("Function_5_1D14")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x2BC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_5_1D14 end

    def Function_6_1D3C(): pass

    label("Function_6_1D3C")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x1F4, 0xDAC)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_6_1D3C end

    def Function_7_1D64(): pass

    label("Function_7_1D64")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x258, 0xBB8)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_1D64 end

    def Function_8_1D8C(): pass

    label("Function_8_1D8C")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x2BC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_1D8C end

    def Function_9_1DB4(): pass

    label("Function_9_1DB4")

    OP_74(0x0, 0x5)
    OP_71(0x0, 0x3CA, 0x3DE, 0x1, 0x20)
    Return()

    # Function_9_1DB4 end

    def Function_10_1DC5(): pass

    label("Function_10_1DC5")

    OP_74(0x0, 0x14)
    OP_71(0x0, 0x5B, 0x78, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    Return()

    # Function_10_1DC5 end

    def Function_11_1DE5(): pass

    label("Function_11_1DE5")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x78, 0x82, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    Return()

    # Function_11_1DE5 end

    def Function_12_1E09(): pass

    label("Function_12_1E09")

    OP_74(0x0, 0xA)
    OP_71(0x0, 0x3F2, 0x3FC, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x3FC, 0x410, 0x1, 0x20)
    Return()

    # Function_12_1E09 end

    def Function_13_1E29(): pass

    label("Function_13_1E29")

    OP_74(0x0, 0x5)
    OP_71(0x0, 0x335, 0x339, 0x1, 0x8)
    OP_79(0x0)

    label("loc_1E3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E6E")
    OP_74(0x0, 0x1)
    OP_71(0x0, 0x339, 0x33B, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x33B, 0x339, 0x1, 0x8)
    OP_79(0x0)
    Jump("loc_1E3C")

    label("loc_1E6E")

    Return()

    # Function_13_1E29 end

    def Function_14_1E6F(): pass

    label("Function_14_1E6F")

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
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    LoadChrToIndex("chr/ch00056.itc", 0x2A)
    LoadChrToIndex("chr/ch00156.itc", 0x2B)
    LoadChrToIndex("chr/ch00256.itc", 0x2C)
    LoadChrToIndex("chr/ch00356.itc", 0x2D)
    LoadChrToIndex("chr/ch0295F.itc", 0x2E)
    LoadChrToIndex("chr/ch03056.itc", 0x2F)
    LoadChrToIndex("chr/ch32650.itc", 0x30)
    LoadChrToIndex("chr/ch32651.itc", 0x31)
    LoadChrToIndex("chr/ch32657.itc", 0x32)
    LoadChrToIndex("chr/ch32653.itc", 0x33)
    LoadChrToIndex("chr/ch31250.itc", 0x34)
    LoadChrToIndex("chr/ch31251.itc", 0x35)
    LoadChrToIndex("chr/ch31252.itc", 0x36)
    LoadChrToIndex("chr/ch31253.itc", 0x37)
    LoadChrToIndex("apl/ch51444.itc", 0x38)
    SoundLoad(3575)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev606_00.eff")
    LoadEffect(0x2, "battle/cr326000.eff")
    LoadEffect(0x3, "event\\ev15010.eff")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x5A, 0x96, 0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFFFFCFB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2005")
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_2078")

    label("loc_2005")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2048")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_2078")

    label("loc_2048")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)

    label("loc_2078")

    SetChrPos(0x101, 1000, 0, 1550, 270)
    SetChrPos(0x102, 1400, 0, 2550, 270)
    SetChrPos(0x103, 2800, 0, 1750, 270)
    SetChrPos(0x104, 2650, 0, 3100, 270)
    SetChrPos(0x109, 2600, 0, 750, 270)
    SetChrPos(0x105, 3850, 0, 2350, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x30)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x34)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x34)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x34)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x34)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xF, 12000, 0, 2000, 270)
    SetChrPos(0x8, 13700, 0, 3000, 270)
    SetChrPos(0x9, 14700, 0, 2500, 270)
    SetChrPos(0xA, 15300, 0, 3500, 270)
    SetChrPos(0xB, 13200, 0, 1000, 270)
    SetChrPos(0xC, 15000, 0, 1500, 270)
    SetChrPos(0xD, 15300, 0, 500, 270)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x0, 0xE)
    OP_49()
    SetChrPos(0xE, -5000, 0, 2000, 90)
    OP_D5(0xE, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    SetChrFlags(0xE, 0x1)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2288")
    FadeToBright(0, 0)
    Jump("loc_30DA")

    label("loc_2288")

    OP_68(-1740, 2600, 2210, 0)
    MoveCamera(295, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14050, 0)
    SetCameraDistance(12750, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B5")
    SetMessageWindowPos(10, 80, -1, -1)

    #A0047
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W……喂喂……\x01",
            "你们在搞笑吗？\x02",
        )
    )

    CloseMessageWindow()

    #A0048
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W再怎么说，\x01",
            "也还不至于这么无能吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_234B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_234B)

    def lambda_2364():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2364)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    WaitChrThread(0x101, 2)
    WaitChrThread(0x104, 2)

    #C0049
    ChrTalk(
        0x101,
        "#00006F#4P#N唔……呼……呼……\x02",
    )

    CloseMessageWindow()

    def lambda_23C2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_23C2)

    def lambda_23DB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_23DB)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)

    #C0050
    ChrTalk(
        0x102,
        "#00108F#12P#N完、完全无法抗衡吗……？\x02",
    )

    CloseMessageWindow()

    def lambda_2440():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2440)

    def lambda_2459():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2459)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    WaitChrThread(0x105, 2)
    WaitChrThread(0x109, 2)

    #C0051
    ChrTalk(
        0x103,
        "#00206F#12P#N太惊人了……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_26F6")

    label("loc_24B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_261A")
    OP_2C(0xA8, 0x1)
    SetMessageWindowPos(10, 80, -1, -1)

    #A0052
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W哼哼……\x01",
            "你们也就是这种水平了。\x02",
        )
    )

    CloseMessageWindow()

    #A0053
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W哎呀呀……\x01",
            "好像比以前稍微强了一些啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0054
    ChrTalk(
        0x101,
        "#00010F#4P#N唔……\x02",
    )

    CloseMessageWindow()

    def lambda_2558():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2558)

    def lambda_2571():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2571)

    def lambda_258A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_258A)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    #C0055
    ChrTalk(
        0x109,
        (
            "#10108F#4P#N都、都已经如此拼命攻击了，\x01",
            "却几乎没有起到效果……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_26F6")

    label("loc_261A")

    OP_2C(0xA8, 0x2)
    SetMessageWindowPos(10, 80, -1, -1)

    #A0056
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W哼哼……\x01",
            "比我想象的能干嘛。\x02",
        )
    )

    CloseMessageWindow()

    #A0057
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W虽说要把乐趣留到最后，\x01",
            "但现在真想直接吞掉你们啊……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0058
    ChrTalk(
        0x101,
        "#00013F#4P#N呜……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0059
    ChrTalk(
        0x104,
        (
            "#00311F#12P#N啧……\x01",
            "六人齐上，他好像也没什么事啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_26F6")


    #C0060
    ChrTalk(
        0x105,
        "#10303F#12P#N……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2000, 2500, 2000, 0)
    MoveCamera(60, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    MoveCamera(50, 24, 0, 15000)
    Sleep(500)
    SetMessageWindowPos(10, 120, -1, -1)

    #A0061
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W哼哼……怎么了，瓦吉……？\x02",
        )
    )

    CloseMessageWindow()

    #A0062
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W再像平时一样，做出一副镇定自若\x01",
            "的表情，说点装模作样的话啊……\x02",
        )
    )

    CloseMessageWindow()

    #A0063
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W不那样可就\x01",
            "没意思了吧……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0064
    ChrTalk(
        0x105,
        (
            "#10306F瓦鲁多。\x02\x03",

            "#10301F你究竟是从什么地方\x01",
            "得到『真知』的？\x02",
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0065
    ChrTalk(
        0x101,
        "#00011F#11P说、说起来……！\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#00101F#11P约亚西姆医生制造的那些『真知』，\x01",
            "除了调查用的样本之外，\x01",
            "已经全部销毁掉了……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#00307F#11P你这家伙……\x01",
            "到底是从哪里得到的！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)

    #A0068
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W哼哼……随你们去想吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0069
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W还有，你们可不要搞错。\x02",
        )
    )

    CloseMessageWindow()

    #A0070
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W我的『力量』并不是\x01",
            "完全依靠药物得到的……\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W药物只是个引子而已──\x01",
            "我的『力量』完全来源于自身，\x01",
            "毫无杂质。\x02",
        )
    )

    CloseMessageWindow()

    #A0072
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W和那个叫约亚西姆的家伙\x01",
            "所得到的虚假『力量』是不一样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0073
    ChrTalk(
        0x103,
        (
            "#00201F#11P……的确……\x01",
            "与当时的约亚西姆医生不同，\x01",
            "他并没有疯狂失控。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x105,
        (
            "#10303F#11P虽然借助药物来引发，\x01",
            "但他已经将这力量掌控自如了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-530, 2600, 2300, 0)
    MoveCamera(271, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12750, 0)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xF, 0x8)
    Sleep(300)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrPos(0x1C, 8000, 0, 1750, 270)

    #N0075
    NpcTalk(
        0x1C,
        "男人的声音",
        "#2S#5P什、什么！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x1C, 8000, 0, 2250, 270)

    #N0076
    NpcTalk(
        0x1C,
        "男人的声音",
        "#2S#11P怪、怪物……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x1C, 0x80)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(12000, 1000, 2000, 0)
    OP_68(4500, 1000, 2000, 2500)
    MoveCamera(45, 24, 0, 0)
    MoveCamera(35, 21, 0, 2500)
    OP_6E(510, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(16000, 2500)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x103, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)
    OP_93(0x105, 0x5A, 0x0)
    SetMapObjFlags(0x0, 0x4)
    BeginChrThread(0xF, 3, 0, 15)
    Sleep(10)
    BeginChrThread(0x8, 3, 0, 16)
    BeginChrThread(0x9, 3, 0, 16)
    Sleep(10)
    BeginChrThread(0xA, 3, 0, 16)
    BeginChrThread(0xB, 3, 0, 16)
    Sleep(10)
    BeginChrThread(0xC, 3, 0, 16)
    BeginChrThread(0xD, 3, 0, 16)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_6F(0x79)
    OP_0D()

    #C0077
    ChrTalk(
        0x104,
        "#00305F#6P米蕾优……！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x109,
        "#10102F#6P米蕾优三尉……！\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#00102F#6P太好了……！\x01",
            "修复工作已经完成了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xF,
        (
            "#07905F#11P嗯……告一段落之后，\x01",
            "我们就立刻赶来了……\x02\x03",

            "#07907F那、那个怪物到底是……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E55():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E55)
    Sleep(50)

    def lambda_2E65():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E65)
    Sleep(50)

    def lambda_2E75():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2E75)
    Sleep(50)

    def lambda_2E85():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E85)
    Sleep(50)

    def lambda_2E95():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E95)
    Sleep(50)

    def lambda_2EA5():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2EA5)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(500)
    OP_68(-2000, 2500, 2000, 0)
    MoveCamera(55, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12750, 0)
    ClearMapObjFlags(0x0, 0x4)
    OP_0D()
    SetMessageWindowPos(10, 120, -1, -1)

    #A0081
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W哼哼……今天的宴席就此结束吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0082
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W特别任务支援科……还有瓦吉。\x02",
        )
    )

    CloseMessageWindow()

    #A0083
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W下次见面的时候，一定要让我\x01",
            "玩得比这次更开心一些啊……\x02",
        )
    )

    CloseMessageWindow()

    #A0084
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W就像当时在旧城区\x01",
            "玩的那场追逐赛一样。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0085
    ChrTalk(
        0x101,
        "#00013F#11P唔……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#00310F#11P你……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x105,
        "#10307F#11P瓦鲁多……！\x02",
    )

    CloseMessageWindow()
    OP_68(6000, 1000, 2000, 1500)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)

    #C0088
    ChrTalk(
        0xF,
        (
            "#07901F#11P休、休想逃跑！\x02\x03",

            "#07907F全体成员！准备战斗！\x01",
            "允许使用导弹发射器！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)
    SetMessageWindowPos(280, 10, -1, -1)
    SetChrName("众警备队员")

    #A0089
    AnonymousTalk(
        0xFF,
        "#4S是！长官！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_30DA")

    Fade(500)
    OP_68(7150, 1500, 2000, 0)
    MoveCamera(270, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13800, 0)
    OP_68(-1750, 1500, 2000, 3000)
    MoveCamera(310, 9, 0, 3000)
    SetCameraDistance(19800, 3000)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    SetChrPos(0xF, 6000, 0, 2000, 270)
    SetChrPos(0x8, 7700, 0, 3000, 270)
    SetChrPos(0x9, 8700, 0, 2500, 270)
    SetChrPos(0xA, 9300, 0, 3500, 270)
    SetChrPos(0xB, 7200, 0, 1000, 270)
    SetChrPos(0xC, 9000, 0, 1500, 270)
    SetChrPos(0xD, 9300, 0, 500, 270)
    BeginChrThread(0xF, 3, 0, 17)
    BeginChrThread(0x8, 3, 0, 18)
    BeginChrThread(0x9, 3, 0, 19)
    BeginChrThread(0xA, 3, 0, 20)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0xC, 3, 0, 22)
    BeginChrThread(0xD, 3, 0, 23)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 25)
    BeginChrThread(0x102, 3, 0, 26)
    BeginChrThread(0x103, 3, 0, 27)
    BeginChrThread(0x104, 3, 0, 28)
    BeginChrThread(0x109, 3, 0, 29)
    BeginChrThread(0x105, 3, 0, 30)
    OP_6F(0x79)
    BeginChrThread(0x101, 0, 0, 24)
    MoveCamera(295, 9, 0, 9000)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_0D()
    Fade(500)
    OP_68(-5000, 3300, 2000, 0)
    MoveCamera(270, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    MoveCamera(270, 30, 0, 10000)
    SetCameraDistance(13500, 10000)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x41A, 0x442, 0x1, 0x8)
    Sound(892, 0, 100, 0)
    Sleep(1300)
    Sound(892, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 140, -1, -1)

    #A0090
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40A#3575V哈哈……\x01",
            "#4S太弱了！\x07\x00\x05\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5000, 4250, 2000, 1200)
    MoveCamera(270, 15, 0, 1200)
    OP_6E(600, 1200)
    SetCameraDistance(9000, 1200)
    Sound(892, 0, 100, 0)
    OP_74(0x0, 0x7)
    OP_71(0x0, 0x335, 0x33E, 0x1, 0x8)
    OP_79(0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    CancelBlur(500)
    Sleep(500)
    OP_6F(0x79)
    Sound(893, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x33E, 0x348, 0x1, 0x8)
    Sound(3543, 255, 100, 0)    #voice#Wald
    Sound(833, 0, 100, 0)
    Sound(862, 0, 100, 0)
    OP_82(0x1F4, 0x1F4, 0x2328, 0x5DC)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x3, 0xFF, 0xE, 0x5, 0, 2000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_68(-5000, 800, 2000, 1000)
    MoveCamera(270, 16, 0, 1000)
    SetCameraDistance(33000, 1000)
    Sleep(700)
    CancelBlur(500)
    BeginChrThread(0xF, 3, 0, 37)
    BeginChrThread(0x8, 3, 0, 38)
    BeginChrThread(0x9, 3, 0, 39)
    BeginChrThread(0xA, 3, 0, 40)
    BeginChrThread(0xB, 3, 0, 41)
    BeginChrThread(0xC, 3, 0, 42)
    BeginChrThread(0xD, 3, 0, 43)
    BeginChrThread(0x101, 3, 0, 31)
    BeginChrThread(0x102, 3, 0, 32)
    BeginChrThread(0x103, 3, 0, 33)
    BeginChrThread(0x104, 3, 0, 34)
    BeginChrThread(0x109, 3, 0, 35)
    BeginChrThread(0x105, 3, 0, 36)

    #C0091
    ChrTalk(
        0xF,
        "#07911F呀啊！？\x05\x02",
    )


    #C0092
    ChrTalk(
        0xD,
        "哇啊啊啊啊！？\x05\x02",
    )

    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0xF, 3)
    Sound(514, 0, 100, 0)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-5000, 2800, 2000, 0)
    MoveCamera(120, 42, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27000, 0)
    BeginChrThread(0xE, 3, 0, 44)
    OP_D5(0xE, 0x0, 0x5F370, 0x0, 0x0)
    OP_D5(0xE, 0x0, 0x4BAF0, 0x0, 0x2BC)
    WaitChrThread(0xE, 3)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_68(-5000, 3800, 2000, 2000)
    MoveCamera(340, -15, 0, 2000)
    SetCameraDistance(12000, 2000)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x105, 0x118, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0x5)
    OP_71(0x0, 0x119, 0x122, 0x1, 0x20)
    Sleep(500)
    OP_68(-5000, 10000, 2000, 500)
    MoveCamera(340, -40, 0, 500)
    SetCameraDistance(20000, 500)
    OP_82(0xC8, 0x1F4, 0xFA0, 0x1F4)
    Sound(833, 0, 80, 0)
    Sound(251, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(1000)

    def lambda_3600():
        OP_9C(0xFE, 0xFFFEEE90, 0x0, 0x7530, 0x88B8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3600)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xE, 0x1)
    OP_74(0x0, 0x2D)
    OP_71(0x0, 0x123, 0x12C, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x12D, 0x140, 0x1, 0x20)
    OP_0D()
    Sleep(2500)
    Fade(500)
    EndChrThread(0xE, 0x1)
    OP_F0(0x0, 0x1)
    OP_F0(0x1, 0x3E8)
    OP_68(-26540, 13300, 18780, 0)
    MoveCamera(85, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(48960, 0)
    OP_68(-26540, 8300, 18780, 4000)
    MoveCamera(112, 23, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(73320, 4000)
    SetChrPos(0xE, -18600, 15800, 15800, 0)

    def lambda_36FA():
        OP_9D(0xFE, 0xFFFF9688, 0x23F0, 0x79AE, 0x1388, 0x1388)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_36FA)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x141, 0x154, 0x1, 0x8)
    Sleep(1100)
    Sound(833, 0, 80, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_D5(0xE, 0x0, 0x41EB0, 0x0, 0x12C)
    OP_79(0x0)
    WaitChrThread(0xE, 1)
    Sound(251, 0, 100, 0)

    def lambda_3798():
        OP_9D(0xFE, 0xFFFF444E, 0x3458, 0x57E4, 0x2710, 0x1388)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3798)
    OP_74(0x0, 0x23)
    OP_71(0x0, 0x123, 0x154, 0x1, 0x8)
    Sleep(1100)
    Sound(833, 0, 80, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_D5(0xE, 0x0, 0x4CE78, 0x0, 0x12C)
    OP_79(0x0)
    WaitChrThread(0xE, 1)
    Sound(251, 0, 100, 0)

    def lambda_3836():
        OP_9C(0xFE, 0xFFFEE2D8, 0x0, 0x9C40, 0x36B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3836)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0x123, 0x154, 0x1, 0x8)
    Sleep(550)
    BlurSwitch(0x96, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(150)
    OP_82(0x5DC, 0x5DC, 0x1388, 0x3E8)
    Sleep(1000)
    CancelBlur(3000)
    OP_79(0x0)
    WaitChrThread(0xE, 1)
    OP_0D()
    StopBGM(0x2710)
    Fade(1000)
    OP_68(-14380, 14500, -2230, 0)
    MoveCamera(350, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(60750, 0)
    OP_68(-14380, 14500, -2230, 10000)
    MoveCamera(308, 0, 0, 10000)
    SetCameraDistance(60750, 10000)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(500)
    SetChrName("")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人\x01",
            "与米蕾优的部队协作，\x01",
            "在广阔的森林中搜索……\x02\x03",

            "但直到最后也没有发现\x01",
            "魔人化的瓦鲁多。\x02\x03",

            "随着夜幕渐渐降临，\x01",
            "众人只得放弃搜索……\x02\x03",

            "罗伊德等人临近深夜才回到支援科，\x01",
            "虽然琪雅准备了火锅，但众人已经连吃饭的力气\x01",
            "都没有了，进门之后便瘫软如泥地直接入睡。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM(-1, -1)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x22, 2)
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1E6F end

    def Function_15_3A9D(): pass

    label("Function_15_3A9D")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3AAA():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AAA)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_3A9D end

    def Function_16_3AC7(): pass

    label("Function_16_3AC7")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3AD4():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AD4)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_3AC7 end

    def Function_17_3AF1(): pass

    label("Function_17_3AF1")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3AFE():
        OP_95(0xFE, 1950, 0, 5200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AFE)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x30)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x32)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_3B33")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BA6")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_3B33")

    label("loc_3BA6")

    Return()

    # Function_17_3AF1 end

    def Function_18_3BA7(): pass

    label("Function_18_3BA7")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3BB4():
        OP_95(0xFE, -2100, 0, 9400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BB4)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 80, 0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_3BF5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C68")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_3BF5")

    label("loc_3C68")

    Return()

    # Function_18_3BA7 end

    def Function_19_3C69(): pass

    label("Function_19_3C69")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3C76():
        OP_95(0xFE, 1700, 0, 7650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C76)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_3CAF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D14")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(987, 0, 50, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_3CAF")

    label("loc_3D14")

    Return()

    # Function_19_3C69 end

    def Function_20_3D15(): pass

    label("Function_20_3D15")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3D22():
        OP_95(0xFE, 1100, 0, 10100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D22)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_3D55")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DBA")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(567, 0, 50, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_3D55")

    label("loc_3DBA")

    Return()

    # Function_20_3D15 end

    def Function_21_3DBB(): pass

    label("Function_21_3DBB")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3DC8():
        OP_95(0xFE, -550, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DC8)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_3DFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E5A")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_3DFB")

    label("loc_3E5A")

    Return()

    # Function_21_3DBB end

    def Function_22_3E5B(): pass

    label("Function_22_3E5B")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3E68():
        OP_95(0xFE, 1950, 0, -1300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E68)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_3EA1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F06")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(530, 0, 40, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_3EA1")

    label("loc_3F06")

    Return()

    # Function_22_3E5B end

    def Function_23_3F07(): pass

    label("Function_23_3F07")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3F14():
        OP_95(0xFE, 2300, 0, -3900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F14)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_3F49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FBC")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_3F49")

    label("loc_3FBC")

    Return()

    # Function_23_3F07 end

    def Function_24_3FBD(): pass

    label("Function_24_3FBD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40EF")
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -6050, 0, 6310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -4270, 0, -2050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1110, 0, 2390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(450)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2860, 0, 530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1580, 0, -1780, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_24_3FBD")

    label("loc_40EF")

    Return()

    # Function_24_3FBD end

    def Function_25_40F0(): pass

    label("Function_25_40F0")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_40F0 end

    def Function_26_4110(): pass

    label("Function_26_4110")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_4110 end

    def Function_27_4130(): pass

    label("Function_27_4130")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_4130 end

    def Function_28_4150(): pass

    label("Function_28_4150")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_4150 end

    def Function_29_4170(): pass

    label("Function_29_4170")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_4170 end

    def Function_30_4190(): pass

    label("Function_30_4190")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_4190 end

    def Function_31_41B0(): pass

    label("Function_31_41B0")

    Sound(250, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_41B0 end

    def Function_32_41DA(): pass

    label("Function_32_41DA")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_41DA end

    def Function_33_41FE(): pass

    label("Function_33_41FE")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_41FE end

    def Function_34_4222(): pass

    label("Function_34_4222")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_4222 end

    def Function_35_4246(): pass

    label("Function_35_4246")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4246 end

    def Function_36_426A(): pass

    label("Function_36_426A")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_426A end

    def Function_37_428E(): pass

    label("Function_37_428E")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    OP_9D(0xFE, 0x154A, 0x0, 0x18EC, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_37_428E end

    def Function_38_42BD(): pass

    label("Function_38_42BD")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x50, 0x0, 0x2CD8, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_38_42BD end

    def Function_39_42E6(): pass

    label("Function_39_42E6")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x1068, 0x0, 0x2314, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_39_42E6 end

    def Function_40_430F(): pass

    label("Function_40_430F")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xC1C, 0x0, 0x2CBA, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_40_430F end

    def Function_41_4338(): pass

    label("Function_41_4338")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x672, 0x0, 0xFFFFE502, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_41_4338 end

    def Function_42_4361(): pass

    label("Function_42_4361")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x154A, 0x0, 0xFFFFF7EA, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_42_4361 end

    def Function_43_438A(): pass

    label("Function_43_438A")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x1324, 0x0, 0xFFFFEA98, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_43_438A end

    def Function_44_43B3(): pass

    label("Function_44_43B3")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x173, 0x17A, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x17A, 0x173, 0x1, 0x8)
    OP_79(0x0)
    Return()

    # Function_44_43B3 end

    def Function_45_43D6(): pass

    label("Function_45_43D6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "eff\\cutin00.eff")
    LoadEffect(0x1, "eff\\\\step00.eff")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00056.itc", 0x20)
    LoadChrToIndex("chr/ch41450.itc", 0x21)
    LoadChrToIndex("chr/ch41451.itc", 0x22)
    LoadChrToIndex("chr/ch41452.itc", 0x23)
    LoadChrToIndex("chr/ch41453.itc", 0x24)
    LoadChrToIndex("apl/ch51613.itc", 0x25)
    SoundLoad(825)
    SoundLoad(2949)
    SoundLoad(2950)
    SoundLoad(2951)
    SoundLoad(2952)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x1, 0x18)
    OP_49()
    SetChrPos(0x18, -36800, 0, 26550, 135)
    OP_D5(0x18, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x32, 0x1, 0x20)
    SetChrFlags(0x18, 0x1)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x206C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -5000, 0, 2000, 180)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -6000, 0, -5000, 0)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -7000, 0, -3500, 0)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -8500, 0, -2500, 45)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4500, 0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3000, 0, -3000, 0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2000, 0, -4500, 0)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -500, 0, -2500, 315)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -5000, 0, -2500, 0)
    SetMapObjFrame(0xFF, "touboku00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "touboku01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "touboku02", 0x0, 0x1)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x2, 0x19)
    OP_49()
    SetChrPos(0x19, -28500, 0, 21580, 0)
    OP_D5(0x19, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x1A, 0x80)
    OP_78(0x3, 0x1A)
    OP_49()
    SetChrPos(0x1A, -27250, 0, 18000, 0)
    OP_D5(0x1A, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x1B, 0x80)
    OP_78(0x4, 0x1B)
    OP_49()
    SetChrPos(0x1B, -24500, 0, 18250, 0)
    OP_D5(0x1B, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4707")
    FadeToBright(0, 0)
    Jump("loc_4DE6")

    label("loc_4707")

    OP_68(-5000, 1000, 2000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22500, 0)
    SetMapObjFrame(0xFF, "hikari", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_68(-5000, 1000, -300, 2500)
    OP_6F(0x79)
    OP_0D()
    OP_A6(0x101, 0x0, 0x32, 0x1F4, 0xBB8)

    #C0094
    ChrTalk(
        0x101,
        "#00006F#50W#5P呼……呼……唔……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x10,
        (
            "#12P……哼，\x01",
            "真是令人佩服啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x13,
        (
            "#12P区区一名警察，\x01",
            "居然能把我们这些新生国防军\x01",
            "的战士戏耍到如此地步……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x12,
        (
            "#6P他好像是希卡少尉\x01",
            "以前的同僚吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x12,
        "#6P的确有些真本事……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x17,
        "#11P好，赶快放下武器吧。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x17,
        (
            "#11P上面的命令是活捉，\x01",
            "尽量不要让你受伤。\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7356", 0)
    OP_A6(0x101, 0x0, 0x32, 0x1F4, 0xBB8)

    #C0101
    ChrTalk(
        0x101,
        "#00015F#60W#5P………我………拒绝………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 10000)

    def lambda_48E9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48E9)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    Sound(802, 0, 100, 0)
    BeginChrThread(0x101, 0, 0, 67)
    OP_0D()
    WaitChrThread(0x101, 2)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 54)
    BeginChrThread(0x10, 3, 0, 54)
    BeginChrThread(0x11, 3, 0, 54)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 54)
    BeginChrThread(0x13, 3, 0, 54)
    Sleep(50)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x14, 3, 0, 54)
    BeginChrThread(0x15, 3, 0, 54)
    BeginChrThread(0x16, 3, 0, 54)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)

    #C0102
    ChrTalk(
        0x10,
        "#12P这家伙……！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x11,
        "#12P还能动弹吗！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x17)

    #C0104
    ChrTalk(
        0x17,
        (
            "#11P……真是难以理解啊，\x01",
            "为何要顽抗至此？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x17,
        (
            "#11P看样子，你好像对克洛斯贝尔\x01",
            "的新体制很不满……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x17,
        (
            "#11P但你以一人之力发起反抗，\x01",
            "根本不可能改变现状。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-5000, 1000, 2000, 8000)
    MoveCamera(0, 27, 0, 8000)
    SetCameraDistance(19500, 8000)

    #C0107
    ChrTalk(
        0x101,
        (
            "#00010F#5P#40W话虽如此……\x02\x03",

            "……但是，\x01",
            "如果谁都不挺身而出，\x01",
            "这种状况就永远不会改变……！\x02\x03",

            "#00015F我绝不会就此屈服……\x01",
            "……为了用自己的双眼\x01",
            "寻找到真相……\x02\x03",

            "#00007F为了把……\x01",
            "……重要的同伴找回……！\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 60, 0)
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5000, 1000, 2000, 500)
    MoveCamera(0, 27, 0, 500)
    SetCameraDistance(17500, 500)
    OP_6F(0x79)
    CancelBlur(0)
    OP_0D()
    Sleep(1200)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0108
    ChrTalk(
        0x101,
        (
            "#00007F#4S#5P我……！\x01",
            "我绝对不会放弃！\x02\x03",

            "#4S无论失败多少次也好……！\x01",
            "就算腿被打断，\x01",
            "我也会重新站起来……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-5000, 1000, -1400, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20250, 0)
    OP_0D()

    #C0109
    ChrTalk(
        0x10,
        "#6P呜……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x13,
        "#12P这家伙……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x17,
        "#5P……真遗憾啊。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x17,
        (
            "#5P一口气解决他，\x01",
            "在他反抗之前将他制服。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x11,
        "#6P明白。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x15,
        "#12P瞄准他的腿。\x02",
    )

    CloseMessageWindow()

    label("loc_4DE6")

    Fade(500)
    OP_68(-5000, 1000, -300, 0)
    MoveCamera(135, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(25500, 0)
    SetMapObjFrame(0xFF, "hikari", 0x1, 0x1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x2)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x2)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x2)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x2)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x2)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x2)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x2)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x2)
    OP_68(-5000, 1000, 2000, 2500)
    MoveCamera(0, 21, 0, 10000)
    OP_6E(550, 10000)
    SetCameraDistance(17000, 7500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(2500)
    BeginChrThread(0x17, 3, 0, 46)
    BeginChrThread(0x10, 3, 0, 47)
    BeginChrThread(0x11, 3, 0, 48)
    BeginChrThread(0x12, 3, 0, 49)
    BeginChrThread(0x13, 3, 0, 50)
    BeginChrThread(0x14, 3, 0, 51)
    BeginChrThread(0x15, 3, 0, 52)
    BeginChrThread(0x16, 3, 0, 53)
    OP_0D()
    Sleep(800)

    #C0115
    ChrTalk(
        0x101,
        (
            "#00013F#5P#40W（……直到最后……\x01",
            "  直到最后都不能放弃……）\x02\x03",

            "#00003F（琪雅……\x01",
            "  ……艾莉……缇欧……）\x02\x03",

            "（兰迪……瓦吉……\x01",
            "  ……还有赛尔盖科长……）\x02\x03",

            "#00010F（请你们……\x01",
            "  ……把力量借给我吧……！）\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    OP_6F(0x79)
    Sleep(200)
    Sound(912, 0, 100, 0)
    Fade(500)
    OP_68(-5000, 1000, 2000, 0)
    MoveCamera(90, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(12500, 0)
    SetCameraDistance(22500, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(30, 30, -1, -1)
    SetChrName("声音")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2949V#40W#4S哎呀呀。\x02",
        )
    )

    CloseMessageWindow()

    #A0117
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2950V#40W#4S你似乎忘记了另一个\x01",
            "可靠的帮手啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB86)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    EndChrThread(0x101, 0x0)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0118
    ChrTalk(
        0x101,
        "#00005F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x17,
        "#11P……！？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x16,
        "#5P刚、刚才那是……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x13,
        "#11P声音直接在大脑中响起……\x02",
    )

    CloseMessageWindow()
    Sound(913, 0, 100, 0)
    OP_82(0xC8, 0x12C, 0x1770, 0x7D0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    CancelBlur(1000)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x101, 0x0)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A6(0x10, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(500)
    OP_64(0x10)

    #C0122
    ChrTalk(
        0x10,
        "#12P哇……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A6(0x15, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(500)
    OP_64(0x15)

    #C0123
    ChrTalk(
        0x15,
        "#5P什、什么……！？\x02",
    )

    CloseMessageWindow()
    Sound(914, 0, 100, 0)
    OP_82(0x5A, 0x96, 0x1388, 0x1F4)
    Sleep(500)
    Sleep(200)

    def lambda_5375():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5375)
    BeginChrThread(0x17, 3, 0, 55)
    BeginChrThread(0x10, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 55)
    BeginChrThread(0x12, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 55)
    BeginChrThread(0x14, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x15, 3, 0, 55)
    BeginChrThread(0x16, 3, 0, 55)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x101, 2)
    Fade(1000)
    SetChrPos(0x17, -5500, 0, -2150, 315)
    SetChrPos(0x12, -4750, 0, 4450, 300)
    OP_68(-36800, 4000, 26550, 0)
    MoveCamera(3, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(43000, 0)
    OP_68(-16120, 4000, 9190, 8500)
    MoveCamera(288, 3, 0, 8500)
    OP_6E(550, 8500)
    SetCameraDistance(23000, 8500)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x18, 3, 0, 65)
    WaitChrThread(0x18, 3)
    OP_6F(0x79)
    OP_0D()
    Sleep(800)
    OP_68(-9220, 3300, 3410, 2000)
    MoveCamera(284, 8, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(28200, 2000)
    OP_6F(0x79)

    #C0124
    ChrTalk(
        0x10,
        "#5P#40W#2S………哎…………？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x16,
        "#11P#40W#2S…………这………………\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#00005F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-9550, 3300, 4600, 0)
    MoveCamera(102, 26, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22200, 0)
    SetCameraDistance(20700, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("白色巨狼")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2951V#40W#4S退去吧，\x01",
            "守卫虚假圣地的士兵们。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 155, -1, -1)
    SetChrName("白色巨狼")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2952V#40W#4S这个人就由我带走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB88)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_82(0x96, 0x0, 0xBB8, 0x1F4)
    BeginChrThread(0x17, 3, 0, 56)
    BeginChrThread(0x10, 3, 0, 57)

    #C0129
    ChrTalk(
        0x10,
        "#11P哇、哇哇哇哇……！\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x11, 3, 0, 57)
    BeginChrThread(0x12, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 57)
    BeginChrThread(0x14, 3, 0, 57)

    #C0130
    ChrTalk(
        0x15,
        "#11P哇啊啊啊啊……！\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x15, 3, 0, 57)
    BeginChrThread(0x16, 3, 0, 57)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_68(-9550, 1700, 4600, 1500)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    OP_9B(0x0, 0x17, 0x9, 0x1770, 0x1388, 0x0)
    SetChrChipByIndex(0x17, 0x23)
    OP_A1(0x17, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 100, 0)
    OP_6F(0x79)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0131
    ChrTalk(
        0x17,
        "#11P#4S开、开什么玩笑……！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x17,
        (
            "#11P#4S新生的克洛斯贝尔国防军\x01",
            "怎么会屈服于区区幻兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-15640, 9800, 8050, 0)
    MoveCamera(315, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    Sound(913, 0, 100, 0)
    OP_82(0xC8, 0x12C, 0x1770, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-10700, 1000, 4500, 1500)
    MoveCamera(279, 26, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(18500, 1500)
    SetChrPos(0x18, -15350, 0, 8550, 225)
    SetChrPos(0x17, -10700, 0, 4500, 315)
    SetChrFlags(0x12, 0x8)
    OP_93(0x11, 0x0, 0x0)
    OP_93(0x14, 0xE1, 0x0)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0xB5, 0xDC, 0x0, 0x8)
    Sleep(300)
    CancelBlur(0)
    Sleep(850)
    StopSound(913, 700, 100)
    Sound(915, 0, 100, 0)
    SetChrFlags(0x17, 0x8)
    BeginChrThread(0x17, 3, 0, 58)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_79(0x1)
    OP_71(0x1, 0x3D, 0x64, 0x0, 0x20)
    Sound(912, 0, 50, 0)

    #C0133
    ChrTalk(
        0x11,
        "#5P#50W………哎……………\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x14,
        "#11P#50W…………呜………………\x02",
    )

    CloseMessageWindow()
    StopSound(912, 500, 40)
    Fade(500)
    OP_68(-8350, 5600, 2950, 0)
    MoveCamera(106, 31, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26750, 0)
    OP_68(-8350, 2100, 2950, 1500)
    MoveCamera(92, 36, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(23000, 1500)

    def lambda_59C6():

        label("loc_59C6")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_59C6")

    QueueWorkItem2(0x101, 2, lambda_59C6)

    def lambda_59D8():

        label("loc_59D8")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_59D8")

    QueueWorkItem2(0x10, 2, lambda_59D8)

    def lambda_59EA():

        label("loc_59EA")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_59EA")

    QueueWorkItem2(0x11, 2, lambda_59EA)

    def lambda_59FC():

        label("loc_59FC")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_59FC")

    QueueWorkItem2(0x12, 2, lambda_59FC)

    def lambda_5A0E():

        label("loc_5A0E")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5A0E")

    QueueWorkItem2(0x13, 2, lambda_5A0E)

    def lambda_5A20():

        label("loc_5A20")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5A20")

    QueueWorkItem2(0x14, 2, lambda_5A20)

    def lambda_5A32():

        label("loc_5A32")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5A32")

    QueueWorkItem2(0x15, 2, lambda_5A32)

    def lambda_5A44():

        label("loc_5A44")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5A44")

    QueueWorkItem2(0x16, 2, lambda_5A44)
    ClearChrFlags(0x12, 0x8)
    OP_64(0x17)
    SetChrFlags(0x17, 0x8)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0xB5, 0xB7, 0x1F4, 0x8)
    Sleep(500)
    ClearChrFlags(0x17, 0x8)
    BeginChrThread(0x17, 3, 0, 59)
    OP_79(0x1)
    OP_74(0x1, 0x3)
    OP_71(0x1, 0xB7, 0xB5, 0x0, 0x8)
    OP_79(0x1)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x3D, 0x64, 0x12C, 0x20)
    WaitChrThread(0x17, 3)
    OP_6F(0x79)
    OP_0D()
    EndChrThread(0x10, 0x2)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0x13, 0x2)
    EndChrThread(0x14, 0x2)
    EndChrThread(0x15, 0x2)
    EndChrThread(0x16, 0x2)
    Sleep(500)

    #C0135
    ChrTalk(
        0x17,
        "#60W#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("白色巨狼")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30W好了，\x01",
            "还用我重复一遍吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrSubChip(0x17, 0x3)
    OP_A6(0x17, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(300)

    #C0137
    ChrTalk(
        0x17,
        "#60W#12P#60W………不必了…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-7900, 1000, 2580, 0)
    MoveCamera(354, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    SetChrSubChip(0x17, 0x1)
    SetCameraDistance(14000, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(200)
    Fade(250)
    SetChrFlags(0x17, 0x20)
    ClearChrFlags(0x17, 0x2)
    SetChrSubChip(0x17, 0x1)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x17, 0x87, 0x1F4)
    Sleep(500)
    SetCameraDistance(25000, 750)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    #C0138
    ChrTalk(
        0x17,
        "#5S#5P撤退──！！！\x05\x02",
    )

    Sleep(1000)
    CancelBlur(500)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-4700, 2550, -400, 0)
    MoveCamera(310, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    OP_68(-4700, 1550, -400, 5000)
    SetCameraDistance(25000, 5000)
    BeginChrThread(0x18, 0, 0, 63)
    Sound(871, 0, 60, 0)
    Sound(825, 2, 40, 0)
    BeginChrThread(0x17, 3, 0, 61)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 62)

    #C0139
    ChrTalk(
        0x11,
        "#5P哇啊啊啊啊啊啊啊！！\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x12, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x14, 3, 0, 62)
    Sound(916, 0, 100, 0)

    #C0140
    ChrTalk(
        0x14,
        "#11P女、女神啊啊啊啊啊！！\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x15, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x16, 3, 0, 62)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    CloseMessageWindow()
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x18, 0x0)
    OP_82(0x0, 0x46, 0xBB8, 0x5DC)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(825, 1000, 40)
    OP_68(-5000, 1200, 2000, 0)
    MoveCamera(354, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_64(0x101)
    Sleep(1000)

    #C0141
    ChrTalk(
        0x101,
        "#00011F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(-7330, 3200, 1550, 2000)
    MoveCamera(348, 19, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(20760, 2000)
    BeginChrThread(0x18, 0, 0, 66)
    BeginChrThread(0x1D, 1, 0, 72)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x172, 0x19A, 0x1, 0x20)
    OP_93(0x18, 0x87, 0x0)
    OP_9B(0x0, 0x18, 0x0, 0x1B58, 0xBB8, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x1D, 0x1)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x3D, 0x64, 0x2BC, 0x20)
    OP_6F(0x79)
    Sleep(800)
    SetMessageWindowPos(20, 120, -1, -1)
    SetChrName("白色巨狼")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30W嗯，看来是受了\x01",
            "不小的惊吓啊。\x02",
        )
    )

    CloseMessageWindow()

    #A0143
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30W好久没有恢复这种形态了，\x01",
            "稍微有点控制不住轻重。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0144
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W……我想说的话\x01",
            "实在太多了……\x02\x03",

            "但还是先说\x01",
            "这句好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x1A4, 0x1AE, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x1AE, 0x1D6, 0x0, 0x20)
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("白色巨狼")

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30W嗯？什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-7330, 3200, 1550, 1200)
    MoveCamera(332, -2, 0, 1200)
    OP_6E(550, 1200)
    SetCameraDistance(20760, 1200)
    TurnDirection(0x101, 0x18, 500)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    #C0146
    ChrTalk(
        0x101,
        (
            "#00007F#12P#4S#N蔡特！\x01",
            "你来得未免也太巧了吧！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_24(0x339)
    SetScenarioFlags(0x22, 0)
    NewScene("e4200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_43D6 end

    def Function_46_6035(): pass

    label("Function_46_6035")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFEC78, 0x0, 0xFFFFF254, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_46_6035 end

    def Function_47_6077(): pass

    label("Function_47_6077")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -9000, 0, -3000, 4000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_47_6077 end

    def Function_48_60B9(): pass

    label("Function_48_60B9")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -10500, 0, 1000, 4000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_48_60B9 end

    def Function_49_60FB(): pass

    label("Function_49_60FB")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -10700, 0, 4500, 4200, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_49_60FB end

    def Function_50_613D(): pass

    label("Function_50_613D")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -1000, 0, -2000, 4000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_50_613D end

    def Function_51_617F(): pass

    label("Function_51_617F")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -2000, 0, 6500, 6000, 0x1)
    OP_95(0xFE, -6000, 0, 7500, 6000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_51_617F end

    def Function_52_61D5(): pass

    label("Function_52_61D5")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 1000, 0, 2000, 5000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_52_61D5 end

    def Function_53_6217(): pass

    label("Function_53_6217")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -2000, 0, 6500, 4200, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_6217 end

    def Function_54_6259(): pass

    label("Function_54_6259")

    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_54_6259 end

    def Function_55_6267(): pass

    label("Function_55_6267")

    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x18, 500)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_55_6267 end

    def Function_56_627D(): pass

    label("Function_56_627D")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_6294():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6294)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_64(0xFE)
    Return()

    # Function_56_627D end

    def Function_57_62B3(): pass

    label("Function_57_62B3")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_62CA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_62CA)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_64(0xFE)
    Return()

    # Function_57_62B3 end

    def Function_58_6308(): pass

    label("Function_58_6308")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -10700, 500, 4500, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x7)
    ClearChrFlags(0xFE, 0x100)
    SetChrFlags(0xFE, 0x800)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    OP_D3(0x17, 0x1, "Null_kuti(41)")
    OP_52(0xFE, 0x23, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0x0, 0x0)
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0xFFFF8AD0, 0x64)
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0xEA60, 0x190)
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0x61A8, 0x190)
    OP_63(0xFE, 0x0, 300, 0x28, 0x2B, 0x64, 0x0)

    label("loc_63E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6407")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(1000)
    Jump("loc_63E1")

    label("loc_6407")

    Return()

    # Function_58_6308 end

    def Function_59_6408(): pass

    label("Function_59_6408")

    Sound(915, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x5, 0x96)
    SetChrFlags(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x64, 0x0, 0x1388, 0x12C)
    OP_D3(0x17, 0xFF, "")
    OP_52(0xFE, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    SetChrFlags(0xFE, 0x100)
    ClearChrFlags(0xFE, 0x800)
    OP_D5(0xFE, 0x4E20, 0x0, 0x0, 0x0)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFE124, 0x0, 0xA14, 0x1F4, 0x9C4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0xFE, 0x13B, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -7900, 150, 2580, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_64EF():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64EF)
    Sound(811, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x2)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_59_6408 end

    def Function_60_6516(): pass

    label("Function_60_6516")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6534")
    OP_A1(0xFE, 0x9C4, 0x8, 0x10, 0x11, 0x12, 0x11, 0x10, 0x13, 0x14, 0x13)
    Jump("Function_60_6516")

    label("loc_6534")

    Return()

    # Function_60_6516 end

    def Function_61_6535(): pass

    label("Function_61_6535")

    SetChrFlags(0xFE, 0x2)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 64)
    BeginChrThread(0xFE, 1, 0, 60)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x1)
    OP_64(0xFE)
    Return()

    # Function_61_6535 end

    def Function_62_657A(): pass

    label("Function_62_657A")

    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 64)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_64(0xFE)
    Return()

    # Function_62_657A end

    def Function_63_65B8(): pass

    label("Function_63_65B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65DC")
    OP_82(0x3C, 0x64, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_63_65B8")

    label("loc_65DC")

    Return()

    # Function_63_65B8 end

    def Function_64_65DD(): pass

    label("Function_64_65DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6627")
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 200, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_64_65DD")

    label("loc_6627")

    Return()

    # Function_64_65DD end

    def Function_65_6628(): pass

    label("Function_65_6628")

    BeginChrThread(0xFE, 0, 0, 66)
    BeginChrThread(0x1D, 1, 0, 71)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x172, 0x19A, 0x1, 0x20)

    def lambda_6649():
        OP_9B(0x0, 0xFE, 0x163, 0x61A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6649)
    Sleep(1800)
    OP_82(0x64, 0x1F4, 0xFA0, 0x1F4)
    BeginChrThread(0x19, 3, 0, 68)
    Sleep(1000)
    OP_82(0x64, 0x1F4, 0xFA0, 0x1F4)
    BeginChrThread(0x1A, 3, 0, 69)
    Sleep(1000)
    OP_82(0x64, 0x1F4, 0xFA0, 0x1F4)
    BeginChrThread(0x1B, 3, 0, 70)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x1D, 0x1)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -15430, 500, 8570, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x3D, 0x64, 0x2BC, 0x20)
    Return()

    # Function_65_6628 end

    def Function_66_66FB(): pass

    label("Function_66_66FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6790")
    OP_82(0x5A, 0x96, 0x1388, 0x1F4)
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 500, -2500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 500, 2500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_66_66FB")

    label("loc_6790")

    Return()

    # Function_66_66FB end

    def Function_67_6791(): pass

    label("Function_67_6791")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67AF")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_67_6791")

    label("loc_67AF")

    Return()

    # Function_67_6791 end

    def Function_68_67B0(): pass

    label("Function_68_67B0")

    Sound(917, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -28500, 500, 21580, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -30500, 1500, 20080, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6829():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6829)
    OP_D5(0xFE, 0x0, 0x0, 0x7530, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -28500, 500, 21580, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x2, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_67B0 end

    def Function_69_689A(): pass

    label("Function_69_689A")

    Sound(917, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -27250, 500, 18000, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_68DC():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_68DC)
    OP_D5(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -27250, 500, 18000, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x3, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_689A end

    def Function_70_694D(): pass

    label("Function_70_694D")

    Sound(917, 0, 60, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -24500, 500, 18250, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_698F():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_698F)
    OP_D5(0xFE, 0x0, 0x0, 0x7530, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -24500, 500, 18250, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x4, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_694D end

    def Function_71_6A00(): pass

    label("Function_71_6A00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A1C")
    Sleep(100)
    Sound(914, 0, 100, 0)
    Sleep(800)
    Jump("Function_71_6A00")

    label("loc_6A1C")

    Return()

    # Function_71_6A00 end

    def Function_72_6A1D(): pass

    label("Function_72_6A1D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A39")
    Sleep(250)
    Sound(914, 0, 100, 0)
    Sleep(650)
    Jump("Function_72_6A1D")

    label("loc_6A39")

    Return()

    # Function_72_6A1D end

    SaveToFile()

Try(main)
