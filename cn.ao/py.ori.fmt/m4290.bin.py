from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4290.bin",                # FileName
        "m4290",                    # MapName
        "m4290",                    # Location
        0x007F,                     # MapIndex
        "ed7573",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x29,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 127, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4290",                  # 0
        "诺华提斯博士",           # 1
        "小丑肯帕雷拉",           # 2
        "阿瑞安赫德",             # 3
        "银",                     # 4
        "莉夏",                   # 5
        "游击士斯克特",           # 6
        "游击士温蔡尔",           # 7
        "亚里欧斯",               # 8
        "骑士装扮的少女",         # 9
        "骑士装扮的少女",         # 10
        "骑士装扮的少女",         # 11
        "灵狮奇美拉",             # 12
        "SE控制",                 # 13
        "APL表示用",              # 14
        "bm4210",                 # 15
    ))

    ATBonus("ATBonus_24C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_30C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_304", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_32C", 0x0042, 72, 6, 45, 3, 3, 30, 0, "bm4210", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_2EC", "ed7454", "ed7453", "ATBonus_24C"),
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1052, 0)                                       # 0

    ScpFunction((
        "Function_0_41C",          # 00, 0
        "Function_1_43D",          # 01, 1
        "Function_2_480",          # 02, 2
        "Function_3_2287",         # 03, 3
        "Function_4_22C3",         # 04, 4
        "Function_5_22FF",         # 05, 5
        "Function_6_233B",         # 06, 6
        "Function_7_2377",         # 07, 7
        "Function_8_23B3",         # 08, 8
        "Function_9_23E5",         # 09, 9
        "Function_10_26EC",        # 0A, 10
        "Function_11_2773",        # 0B, 11
        "Function_12_283C",        # 0C, 12
        "Function_13_2845",        # 0D, 13
        "Function_14_284E",        # 0E, 14
        "Function_15_2857",        # 0F, 15
        "Function_16_2860",        # 10, 16
        "Function_17_2869",        # 11, 17
        "Function_18_2872",        # 12, 18
        "Function_19_6496",        # 13, 19
        "Function_20_64B8",        # 14, 20
        "Function_21_6604",        # 15, 21
        "Function_22_6617",        # 16, 22
        "Function_23_670C",        # 17, 23
        "Function_24_6776",        # 18, 24
        "Function_25_6795",        # 19, 25
        "Function_26_68A6",        # 1A, 26
        "Function_27_6912",        # 1B, 27
        "Function_28_69BE",        # 1C, 28
        "Function_29_6A5E",        # 1D, 29
        "Function_30_6AFE",        # 1E, 30
        "Function_31_6BA4",        # 1F, 31
        "Function_32_6C44",        # 20, 32
        "Function_33_6CDD",        # 21, 33
        "Function_34_6E15",        # 22, 34
        "Function_35_6F38",        # 23, 35
        "Function_36_6F4B",        # 24, 36
        "Function_37_6F80",        # 25, 37
        "Function_38_7072",        # 26, 38
        "Function_39_708D",        # 27, 39
        "Function_40_70CD",        # 28, 40
        "Function_41_710B",        # 29, 41
        "Function_42_7124",        # 2A, 42
    ))


    def Function_0_41C(): pass

    label("Function_0_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42D")
    Event(0, 2)

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_43C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)

    label("loc_43C")

    Return()

    # Function_0_41C end

    def Function_1_43D(): pass

    label("Function_1_43D")

    SoundDistance(0x7A, 0xFFFFB06E, 0xBC2, 0xFFFFD008, 0x4E20, 0x186A0, 0x64, 0x0)
    OP_E3(0x24E, 0xFFFFFD12, 0x6004)
    OP_E3(0x7DBD, 0xFFFFFD12, 0x14DC)
    Sound(123, 1, 80, 0)
    SetMapObjFlags(0x0, 0x4)
    Return()

    # Function_1_43D end

    def Function_2_480(): pass

    label("Function_2_480")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch03500.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00550.itc", 0x26)
    SoundLoad(3887)
    SoundLoad(3888)
    SoundLoad(3889)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E0")
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    Jump("loc_4E6")

    label("loc_4E0")

    LoadChrToIndex("chr/ch03050.itc", 0x25)

    label("loc_4E6")

    LoadEffect(0x7, "event/ev10008.eff")
    LoadEffect(0x0, "event/ev10017.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    SetChrPos(0x101, -800, -750, -26000, 0)
    SetChrPos(0x102, 600, -750, -26000, 0)
    SetChrPos(0x103, -1100, -750, -27400, 0)
    SetChrPos(0x104, 900, -750, -27400, 0)
    SetChrPos(0x106, -800, -750, -28800, 0)
    SetChrPos(0xF4, 600, -750, -28800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -2300, 250, 7600, 315)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrPos(0x9, -900, 250, 7400, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrPos(0xA, 600, 250, 7600, 45)
    SetChrFlags(0xA, 0x8000)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    OP_78(0x0, 0x13)
    OP_68(-290, 750, -25000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    OP_68(-720, 2250, -20050, 3000)
    MoveCamera(52, 18, 0, 3000)
    OP_6E(750, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_6DF():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6DF)
    Sleep(100)

    def lambda_6F7():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6F7)
    Sleep(50)

    def lambda_70F():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_70F)
    Sleep(50)

    def lambda_727():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_727)
    Sleep(50)

    def lambda_73F():
        OP_9B(0x0, 0xF4, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_73F)
    Sleep(50)

    def lambda_757():
        OP_9B(0x0, 0x106, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_757)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x101, 2)
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
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0001
    ChrTalk(
        0x101,
        "#00011F#6P（这、这里是……！）\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x103,
        (
            "#00205F#12P#N（好惊人……似乎汇聚着\x01",
            "  相当巨大的能量……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0003
    ChrTalk(
        0x104,
        (
            "#00311F#12P（而且……\x01",
            "  他们果然在这里啊。）\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    SetCameraDistance(12000, 4000)
    OP_68(-800, 2250, 1500, 4000)
    MoveCamera(0, 14, 0, 4000)
    OP_6E(810, 4000)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    Fade(500)
    OP_68(-800, 12550, 2650, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(5000, 0)
    OP_68(-800, 2750, 1500, 5000)
    OP_6F(0x79)
    Sleep(500)

    #C0004
    ChrTalk(
        0x9,
        (
            "#04809F#6P呵呵呵……\x01",
            "这里真是个好地方啊。\x02\x03",

            "#04800F既然已经活性化到了如此程度，\x01",
            "也就表示准备工作已经基本完成了吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "白衣男人",
        "#04704F#11P呵呵，可以这么说。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x86, 0x1F4)
    Sleep(200)

    #N0006
    NpcTalk(
        0x8,
        "白衣男人",
        (
            "#04702F#5P嗯嗯，到时候\x01",
            "一定可以大开眼界呢。\x02\x03",

            "『白面』大人要是还活着，\x01",
            "想必也会很开心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(100)

    #C0007
    ChrTalk(
        0x9,
        (
            "#04809F#11P啊哈哈，是啊。\x02\x03",

            "#04805F不过，要是博士和教授\x01",
            "一起来到克洛斯贝尔，\x01",
            "局面恐怕就无法控制了吧？\x02\x03",

            "#04802F说不定连『方舟』都会开出来，\x01",
            "正面向两大国挑衅呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x8,
        "白衣男人",
        (
            "#04709F#5P哈哈，那样不是\x01",
            "也很有趣嘛。\x02",
        )
    )

    CloseMessageWindow()

    #N0009
    NpcTalk(
        0xA,
        "穿戴甲胄的人",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P……………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B6B():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B6B)

    def lambda_B80():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B80)

    def lambda_B95():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B95)

    def lambda_BAA():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BAA)

    def lambda_BBF():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_BBF)

    def lambda_BD4():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_BD4)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x87, 0x1F4)

    #C0010
    ChrTalk(
        0x9,
        (
            "#04805F#5P哎，怎么了？\x02\x03",

            "#04800F这种程度的使命在你眼中太过简单，\x01",
            "所以提不起兴致吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0011
    NpcTalk(
        0xA,
        "穿戴甲胄的人",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P一切都要遵从那位大人的意志，\x01",
            "我不会存有任何异议。\x02\x03",

            "另外，博士、肯帕雷拉，\x01",
            "闲话就说到这里吧。\x02\x03",

            "似乎有客人来了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-800, 2250, -4500, 2500)
    MoveCamera(0, 25, 0, 2500)
    SetCameraDistance(16000, 2500)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(50)

    def lambda_D3B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D3B)
    Sleep(50)

    def lambda_D4B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D4B)
    WaitChrThread(0x101, 1)

    def lambda_D5C():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D5C)
    Sleep(50)

    def lambda_D74():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D74)
    Sleep(50)

    def lambda_D8C():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D8C)
    Sleep(50)

    def lambda_DA4():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DA4)
    Sleep(50)

    def lambda_DBC():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_DBC)
    Sleep(50)

    def lambda_DD4():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_DD4)
    OP_6F(0x79)
    Fade(500)
    OP_68(-6700, 2150, -2690, 0)
    MoveCamera(47, 8, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(10290, 0)
    SetCameraDistance(9290, 2000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    #C0012
    ChrTalk(
        0x101,
        "#00013F#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        "#00107F#12P……啊，你们是……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#12P#N……看样子，聚集着\x01",
            "比预想中更加棘手的怪物呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0015
    ChrTalk(
        0x9,
        (
            "#04805F#5P哦，原来是你们啊。\x02\x03",

            "#04804F两位游击士姐姐应该已经\x01",
            "无法动弹了，我还在奇怪……\x02\x03",

            "#04802F呵呵，你们是怎么\x01",
            "找到这个地方的？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#00203F……#12P#N这是企业秘密。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x104,
        (
            "#00301F#12P#N话说回来，你们好像\x01",
            "正在谈论一些很有趣的事情啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1015")

    #C0018
    ChrTalk(
        0x109,
        (
            "#10107F#12P#N无论你们有何企图……\x01",
            "我们都不会坐视不管！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1049")

    label("loc_1015")


    #C0019
    ChrTalk(
        0x105,
        (
            "#10302F#12P#N我们实在是没有\x01",
            "视而不见的理由呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1049")

    OP_57(0x0)
    OP_5A()

    #N0020
    NpcTalk(
        0x8,
        "白衣男人",
        (
            "#04703F#5P唔……\x02\x03",

            "#04701F看样子，你们应该是\x01",
            "克洛斯贝尔警察局的新人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003F……#12P我们是克洛斯贝尔警察局\x01",
            "『特别任务支援科』的成员。\x02\x03",

            "#00008F看来你们就是结社\x01",
            "『噬身之蛇』的成员……\x02\x03",

            "#00001F首先，能否向我们\x01",
            "证明自己的身份呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0022
    NpcTalk(
        0x8,
        "白衣男人",
        (
            "#04705F#5P证明身份……？\x01",
            "他在说些什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "#04806F#5P嗯……这好像是警察\x01",
            "在执行任务时的必要手续吧？\x02\x03",

            "#04802F呵呵，但居然让我们证明自己的身份，\x01",
            "实在是个不好笑的笑话呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0024
    NpcTalk(
        0xA,
        "穿戴甲胄的人",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P真是一位耿直的年轻人啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0025
    NpcTalk(
        0xA,
        "穿戴甲胄的人",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P如果不回应他的要求，\x01",
            "实在是于心不安……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        (
            "#00306F……#11P放弃吧，罗伊德。\x02\x03",

            "#00301F这些家伙似乎\x01",
            "不能以常理度之呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#N将他们视为与『教团』\x01",
            "成员等同的人即可。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0028
    NpcTalk(
        0x8,
        "白衣男人",
        (
            "#04703F#5P唔……被视为那种家伙的同类，\x01",
            "实在是让人很不愉快啊。\x02\x03",

            "#04702F呵呵……也罢，\x01",
            "那我就做个自我介绍好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x8, 0x0, 0x190, 0x320, 0x0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("白衣男人")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            "F·诺华提斯。\x02\x03",

            "『噬身之蛇』第六柱，\x01",
            "『十三工房』的管理者。\x02\x03",

            "呵呵，随意一些，称我为\x01",
            "『博士』就好了。\x02",
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

    #C0030
    ChrTalk(
        0x103,
        (
            "#00203F#12P#N……原来如此，\x01",
            "那些都是你开发的啊。\x02\x03",

            "#00201F在导力网络的黑客攻击中\x01",
            "所使用的那些难以理解的代码……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x8,
        (
            "#04705F#1P哦……！？\x01",
            "你能看懂那些代码吗！？\x02\x03",

            "#04709F那是『星辰代码』哦！\x01",
            "在结社的导力网络中所使用的……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        "#04801F#5P博士、博士。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#04703F#5P说起来，你就是当年被教团\x01",
            "当作实验体，之后又被爱普斯泰恩的\x01",
            "家伙所收留的那个女孩吧……\x02\x03",

            "#04702F对了！\x01",
            "要不要加入『结社』，\x01",
            "充分发挥你那出众的才能呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#00211F#12P#N我拒绝。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    #C0035
    ChrTalk(
        0x8,
        "#04705F#5P#4S（失望！）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0036
    ChrTalk(
        0x9,
        (
            "#04806F#5P真是的……\x01",
            "虽说玲逃走了，\x01",
            "但你未免也太拼命挖角了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#04701F#5P这、这和玲的事情\x01",
            "并没有关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0xA,
        "穿戴甲胄的人",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P好了，接下来轮到我。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xA, 0x0, 0x190, 0x320, 0x0)
    Fade(500)
    OP_68(-3520, 2450, 2610, 0)
    MoveCamera(53, 7, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(7100, 0)
    OP_0D()
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetChrName("穿戴甲胄的人")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3887V#40W我的名字是阿瑞安赫德。\x02\x03",

            "#3888V『噬身之蛇』第七柱，\x01",
            "被冠以『钢』之称号。\x02\x03",

            "#3889V请多加指教。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF31)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0040
    ChrTalk(
        0x101,
        "#00011F#12P#N这……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0041
    ChrTalk(
        0x102,
        "#00108F#12P#N何等清澄的声音……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00301F#12P#N这家伙身穿铠甲，\x01",
            "不过似乎是女人呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C9")

    #C0043
    ChrTalk(
        0x109,
        (
            "#10108F#12P#N这、这股威压感\x01",
            "简直让人难以置信……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FF")

    label("loc_19C9")


    #C0044
    ChrTalk(
        0x105,
        (
            "#10301F#12P#N……真是让人难以置信\x01",
            "的威压感啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FF")

    OP_57(0x0)
    OP_5A()

    #C0045
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#N……你就是『结社』\x01",
            "的最强者吗？\x02\x03",

            "你散发出来的斗气\x01",
            "的确令人不寒而栗。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2330, 1950, -5470, 2000)
    MoveCamera(14, 13, -1, 2000)
    OP_6E(630, 2000)
    SetCameraDistance(9290, 2000)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0x106, 0x26)
    SetChrSubChip(0x106, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0xF4, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 5)
    BeginChrThread(0x104, 3, 0, 6)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x102, 3, 0, 4)
    WaitChrThread(0xF4, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x106, 3)
    Sleep(150)

    #C0046
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#6P但在我『银』的面前，\x01",
            "你这轻松的态度又能维持多久呢？\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#11P#N…………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0048
    ChrTalk(
        0x101,
        "#00011F#5P喂……『银』……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#00108F#11P为何要如此……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "#04804F#5P#N呵呵，这场对战\x01",
            "真是让人兴趣十足……\x02\x03",

            "#04800F不过，在开战之前，\x01",
            "这里的主人似乎就要回来了。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    def lambda_1C8C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C8C)
    Sleep(50)

    def lambda_1C9C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C9C)
    Sleep(50)

    def lambda_1CAC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CAC)
    Sleep(50)

    def lambda_1CBC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CBC)
    Sleep(50)

    def lambda_1CCC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1CCC)
    Sleep(100)

    #C0051
    ChrTalk(
        0x101,
        "#00005F#6P什么……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D23")

    #C0052
    ChrTalk(
        0x109,
        "#10105F#12P『主人』……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D42")

    label("loc_1D23")


    #C0053
    ChrTalk(
        0x105,
        "#10305F#12P『主人』……？\x02",
    )

    CloseMessageWindow()

    label("loc_1D42")

    Sleep(100)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)

    #C0054
    ChrTalk(
        0x103,
        (
            "#00208F#6P一股强大的灵气正在接近……\x02\x03",

            "#00207F大型幻兽要来了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(11290, 5000)

    def lambda_1E37():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E37)
    Sleep(50)

    def lambda_1E47():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E47)
    Sleep(50)

    def lambda_1E57():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E57)
    Sleep(50)

    def lambda_1E67():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E67)
    Sleep(50)

    def lambda_1E77():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1E77)
    Sleep(50)

    def lambda_1E87():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1E87)
    Sleep(150)

    #C0055
    ChrTalk(
        0x104,
        "#00307F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE5")

    #C0056
    ChrTalk(
        0x109,
        "#10101F#5P从、从哪里……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F0B")

    label("loc_1EE5")


    #C0057
    ChrTalk(
        0x105,
        "#10308F#5P到底从什么地方……！？\x02",
    )

    CloseMessageWindow()

    label("loc_1F0B")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 35000, 7000, -1870, 270)
    OP_93(0x13, 0x10E, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x5A)
    SetChrFlags(0x13, 0x1)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x0, 0x4)
    OP_70(0x0, 0xE5)
    OP_68(8260, 2850, -1360, 0)
    MoveCamera(72, 16, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(11450, 0)
    Fade(500)
    BeginChrThread(0x13, 0, 0, 9)
    WaitChrThread(0x13, 0)

    def lambda_1FA2():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FA2)
    Sleep(50)

    def lambda_1FB2():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1FB2)
    Sleep(50)

    def lambda_1FC2():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1FC2)
    Sleep(50)

    def lambda_1FD2():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1FD2)
    Sleep(50)

    def lambda_1FE2():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1FE2)
    Sleep(50)

    def lambda_1FF2():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1FF2)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0xF4, 0)
    OP_6F(0x79)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x106, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0xF4, 2)
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 17)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 12)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(50)
    BeginChrThread(0xF4, 3, 0, 16)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 13)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    Sleep(500)
    SetChrPos(0x101, -1040, -750, -890, 90)
    SetChrPos(0x102, -2590, -750, 20, 90)

    #C0058
    ChrTalk(
        0x101,
        "#00007F#6P#N什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0059
    ChrTalk(
        0x102,
        "#00110F#6P#N这、这魔兽是……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0060
    ChrTalk(
        0x9,
        (
            "#04804F#6P#N幻兽『灵狮奇美拉』……\x02\x03",

            "#04802F古代幻想中的\x01",
            "神圣花园守护者吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0061
    ChrTalk(
        0x8,
        (
            "#04704F#6P#N哎呀呀，竟然连这种东西\x01",
            "都实体化了……\x02\x03",

            "#04702F呵呵，计划的精确度\x01",
            "真是值得期待啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    BeginChrThread(0x13, 0, 0, 10)
    WaitChrThread(0x13, 0)
    OP_68(-830, 2050, -5110, 2000)
    MoveCamera(52, 7, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(14680, 2000)
    OP_6F(0x79)
    Sleep(500)

    #C0062
    ChrTalk(
        0x101,
        "#00010F#6P#N唔……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0063
    ChrTalk(
        0x104,
        (
            "#00310F#6P#N啧……！\x01",
            "想咬人的话就去咬他们啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0064
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#6P#N有话稍后再说！\x01",
            "尽快制服它！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x13, 0, 0, 11)
    WaitChrThread(0x13, 0)
    Battle("BattleInfo_32C", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 18)
    Return()

    # Function_2_480 end

    def Function_3_2287(): pass

    label("Function_3_2287")


    def lambda_228C():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_228C)

    def lambda_22A1():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22A1)
    WaitChrThread(0xFE, 2)

    def lambda_22B2():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22B2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_3_2287 end

    def Function_4_22C3(): pass

    label("Function_4_22C3")


    def lambda_22C8():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22C8)

    def lambda_22DD():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22DD)
    WaitChrThread(0xFE, 2)

    def lambda_22EE():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22EE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_4_22C3 end

    def Function_5_22FF(): pass

    label("Function_5_22FF")


    def lambda_2304():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2304)

    def lambda_2319():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2319)
    WaitChrThread(0xFE, 2)

    def lambda_232A():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_232A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_5_22FF end

    def Function_6_233B(): pass

    label("Function_6_233B")


    def lambda_2340():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2340)

    def lambda_2355():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2355)
    WaitChrThread(0xFE, 2)

    def lambda_2366():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2366)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_233B end

    def Function_7_2377(): pass

    label("Function_7_2377")


    def lambda_237C():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFF6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_237C)

    def lambda_2391():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2391)
    WaitChrThread(0xFE, 2)

    def lambda_23A2():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23A2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0x13, 2)
    Return()

    # Function_7_2377 end

    def Function_8_23B3(): pass

    label("Function_8_23B3")

    OP_68(-4000, 1950, -6700, 800)
    MoveCamera(21, 12, -1, 800)
    OP_6F(0x79)
    OP_68(-4650, 1950, -8700, 800)
    OP_6F(0x79)
    Return()

    # Function_8_23B3 end

    def Function_9_23E5(): pass

    label("Function_9_23E5")

    OP_68(17070, 10650, -6540, 0)
    MoveCamera(48, 5, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(7630, 0)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(1300)
    OP_68(17070, 10650, -6540, 1650)
    MoveCamera(312, 24, 0, 1650)
    OP_6E(810, 1650)
    SetCameraDistance(7630, 1650)
    Sound(914, 0, 100, 0)
    Sound(251, 0, 100, 0)
    Sound(834, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xE5, 0xEF, 0x0, 0x0)
    CloseMessageWindow()
    OP_96(0xFE, 0x3A98, 0x1B58, 0xFFFFF8B2, 0x4268, 0x0)
    OP_74(0x0, 0x1E)
    OP_68(9820, 9950, -1820, 0)
    MoveCamera(82, 49, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(12750, 0)
    Fade(500)
    PlayEffect(0x0, 0x0, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(990, 0, 100, 0)
    OP_68(9820, 1350, -1820, 1500)
    MoveCamera(67, 7, 0, 1500)
    OP_6E(810, 1500)
    SetCameraDistance(10570, 1500)

    def lambda_2535():
        OP_9D(0xFE, 0x29F4, 0xFFFFFE0C, 0xFFFFF8B2, 0x96, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2535)
    Sleep(1100)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    WaitChrThread(0xFE, 2)
    OP_0D()
    Sound(833, 0, 100, 0)
    StopEffect(0x0, 0x2)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    OP_82(0x96, 0x12C, 0x1388, 0x320)
    OP_71(0x0, 0xF0, 0xF8, 0x0, 0x0)
    Sleep(300)
    CancelBlur(900)
    OP_79(0x0)
    Sleep(900)
    OP_68(9820, 2750, -1820, 600)
    MoveCamera(67, -3, 0, 600)
    OP_6E(810, 600)
    SetCameraDistance(10570, 600)
    OP_74(0x0, 0xF)
    Sound(251, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    OP_71(0x0, 0xF9, 0x104, 0x0, 0x0)

    def lambda_265D():
        OP_9C(0xFE, 0x32, 0x0, 0x0, 0x546, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_265D)
    WaitChrThread(0xFE, 2)
    Sound(893, 0, 50, 0)
    OP_68(8900, 2000, -1790, 700)
    MoveCamera(61, -2, 0, 700)
    OP_6E(810, 700)
    SetCameraDistance(10360, 700)
    OP_79(0x0)
    OP_71(0x0, 0x105, 0x118, 0x0, 0x0)
    Sleep(200)
    Sound(833, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    OP_6F(0x79)
    Return()

    # Function_9_23E5 end

    def Function_10_26EC(): pass

    label("Function_10_26EC")

    Fade(100)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x40, 0x4C, 0x0, 0x0)
    OP_79(0x0)
    OP_0D()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(11950, 500)
    Sound(913, 0, 100, 0)
    OP_71(0x0, 0x4D, 0x55, 0x0, 0x20)
    Sleep(300)
    OP_82(0xC8, 0xC8, 0xBB8, 0x5DC)
    Sleep(1800)
    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_6F(0x79)
    CancelBlur(0)
    OP_71(0x0, 0x56, 0x63, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    Return()

    # Function_10_26EC end

    def Function_11_2773(): pass

    label("Function_11_2773")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0xD4, 0xE4, 0x0, 0x0)
    Sleep(300)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(400)
    CancelBlur(300)
    OP_79(0x0)
    SetChrFlags(0xFE, 0x4)
    OP_71(0x0, 0xE5, 0xED, 0x0, 0x20)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_82(0x32, 0x64, 0xBB8, 0x1F4)
    Sound(251, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_68(-2700, 2550, -4100, 700)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_9C(0xFE, 0xFFFFE890, 0x1F4, 0x0, 0x226, 0x640)
    CancelBlur(0)
    Return()

    # Function_11_2773 end

    def Function_12_283C(): pass

    label("Function_12_283C")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_283C end

    def Function_13_2845(): pass

    label("Function_13_2845")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_2845 end

    def Function_14_284E(): pass

    label("Function_14_284E")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_284E end

    def Function_15_2857(): pass

    label("Function_15_2857")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_2857 end

    def Function_16_2860(): pass

    label("Function_16_2860")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_2860 end

    def Function_17_2869(): pass

    label("Function_17_2869")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_2869 end

    def Function_18_2872(): pass

    label("Function_18_2872")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch03500.itc", 0x20)
    LoadChrToIndex("chr/ch00500.itc", 0x21)
    LoadChrToIndex("chr/ch13700.itc", 0x22)
    LoadChrToIndex("chr/ch27200.itc", 0x23)
    LoadChrToIndex("chr/ch27300.itc", 0x24)
    LoadChrToIndex("chr/ch02400.itc", 0x25)
    LoadChrToIndex("chr/ch43150.itc", 0x26)
    LoadChrToIndex("chr/ch43250.itc", 0x27)
    LoadChrToIndex("chr/ch43350.itc", 0x28)
    LoadChrToIndex("apl/ch50011.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00150.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch00550.itc", 0x2E)
    LoadChrToIndex("chr/ch03550.itc", 0x30)
    LoadChrToIndex("chr/ch03552.itc", 0x31)
    LoadChrToIndex("apl/ch51408.itc", 0x32)
    LoadChrToIndex("chr/ch00053.itc", 0x33)
    LoadChrToIndex("chr/ch00153.itc", 0x34)
    LoadChrToIndex("chr/ch00253.itc", 0x35)
    LoadChrToIndex("chr/ch00353.itc", 0x36)
    LoadChrToIndex("chr/ch00056.itc", 0x39)
    LoadChrToIndex("chr/ch00156.itc", 0x3A)
    LoadChrToIndex("chr/ch00256.itc", 0x3B)
    LoadChrToIndex("chr/ch00356.itc", 0x3C)
    LoadChrToIndex("chr/ch00556.itc", 0x3D)
    LoadChrToIndex("chr/ch43100.itc", 0x3F)
    LoadChrToIndex("chr/ch43200.itc", 0x40)
    LoadChrToIndex("chr/ch43300.itc", 0x41)
    LoadChrToIndex("apl/ch51415.itc", 0x42)
    LoadChrToIndex("apl/ch51416.itc", 0x37)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00701.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    LoadEffect(0x1, "battle/bs000001.eff")
    LoadEffect(0x2, "eff/cutin35.eff")
    LoadEffect(0x3, "event/eva01_01.eff")
    LoadEffect(0x4, "event/ev14016.eff")
    LoadEffect(0x5, "event/ev10007.eff")
    LoadEffect(0x6, "event/ev10002.eff")
    LoadEffect(0x7, "battle/ms00001.eff")
    LoadEffect(0x8, "event/ev10006.eff")
    LoadEffect(0x9, "event/ev14015.eff")
    SoundLoad(3890)
    SoundLoad(3891)
    SoundLoad(3892)
    SoundLoad(4053)
    SoundLoad(4054)
    SoundLoad(4068)
    SoundLoad(3459)
    SoundLoad(3460)
    SoundLoad(2915)
    SoundLoad(3519)
    SoundLoad(3248)
    SoundLoad(3249)
    SoundLoad(4135)
    SoundLoad(959)
    SoundLoad(803)
    SoundLoad(825)
    RemoveParty(0x5, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B0E")
    LoadChrToIndex("chr/ch02950.itc", 0x2F)
    LoadChrToIndex("chr/ch02953.itc", 0x38)
    LoadChrToIndex("chr/ch0295F.itc", 0x3E)
    SetScenarioFlags(0x0, 0)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_2B27")

    label("loc_2B0E")

    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03053.itc", 0x38)
    LoadChrToIndex("chr/ch0305F.itc", 0x3E)
    ClearScenarioFlags(0x0, 0)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_2B27")

    OP_68(-1820, 1450, 3350, 0)
    MoveCamera(153, 15, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(17390, 0)
    SetChrPos(0x101, -2190, -750, -670, 270)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x102, -210, -750, -3260, 270)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x103, -1200, -750, -2190, 270)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x104, -2960, -750, -2640, 270)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0xF4, 960, -750, -1430, 270)
    SetChrChipByIndex(0xF4, 0x2F)
    SetChrSubChip(0xF4, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x5, 10000, 12000, -7000, 0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrPos(0xB, 200, -750, 0, 270)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 200, -750, -3000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -2300, 250, 7600, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrPos(0x9, -900, 250, 7400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrPos(0xA, 600, 250, 7600, 180)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x25)
    SetChrPos(0xF, 900, -750, -23000, 0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrPos(0xD, -900, -750, -25000, 0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrPos(0xE, 900, -750, -25000, 0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x26)
    SetChrPos(0x10, 0, -750, -13600, 0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x27)
    SetChrPos(0x11, 3850, -750, -7000, 250)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x28)
    SetChrPos(0x12, -4180, -750, -8370, 117)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0x13)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -9950, -750, 880, 0)
    OP_93(0x13, 0x64, 0x0)
    OP_74(0x0, 0x1E)
    SetChrFlags(0x13, 0x1)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 0x32)
    SetChrSubChip(0x15, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 600, 750, 5200, 180)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x15, 0x1000)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x1)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetScenarioFlags(0x0, 1)
    OP_68(-5390, 2150, 1420, 0)
    MoveCamera(246, 16, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(14170, 0)
    SetCameraDistance(19170, 3000)
    FadeToBright(1000, 0)
    OP_82(0x0, 0x32, 0x5DC, 0x1388)
    BeginChrThread(0x13, 3, 0, 19)
    OP_0D()
    Sleep(500)
    Sound(843, 0, 100, 0)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    PlayEffect(0x1, 0x0, 0x13, 0x1, 500, -750, 500, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_6F(0x79)
    OP_75(0x0, 0x1, 0x5DC)

    def lambda_2E9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2E9A)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    CancelBlur(2000)
    OP_6F(0x79)
    Sleep(500)
    OP_68(1240, 2150, 1060, 2000)
    MoveCamera(246, 16, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(15170, 2000)
    OP_6F(0x79)
    Sleep(300)

    #C0065
    ChrTalk(
        0x101,
        "#00006F#6P唔……呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#00108F#6P总、总算打倒了……\x02",
    )

    CloseMessageWindow()
    Sound(971, 0, 100, 0)
    Sleep(1000)
    #Sound(4124, 255, 100, 0)    #voice#Companella
    Sleep(500)

    #C0067
    ChrTalk(
        0x9,
        "#04809F#5P呵呵，干得不错嘛⊥\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(1140, 2150, 4290, 2000)
    MoveCamera(313, 15, -1, 2000)
    OP_6E(630, 2000)
    SetCameraDistance(9710, 2000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_2F9F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F9F)
    Sleep(50)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_2FB7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2FB7)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_2FCF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2FCF)
    Sleep(50)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_2FE7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2FE7)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)

    def lambda_2FFF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_2FFF)
    Sleep(50)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)

    def lambda_3017():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3017)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xB, 2)

    #C0068
    ChrTalk(
        0x8,
        (
            "#04704F#5P嗯，以普通人的标准来说，\x01",
            "做得确实挺出色呢。\x02\x03",

            "#04700F那把魔导杖似乎是财团那些\x01",
            "家伙制造的。以他们的能力来说，\x01",
            "完成度还算可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        "#00201F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0070
    ChrTalk(
        0x104,
        "#00311F#6P#N这些混蛋……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-6700, 2150, -2690, 0)
    MoveCamera(47, 8, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(9290, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    OP_9B(0x1, 0x101, 0x0, 0x190, 0x3E8, 0x0)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    #C0071
    ChrTalk(
        0x101,
        (
            "#00003F#12P『噬身之蛇』，\x01",
            "赶快回答我的问题吧！\x02\x03",

            "#00013F你们想在克洛斯贝尔\x01",
            "做什么！？\x02\x03",

            "#00007F这只是我的凭空猜测而已……\x01",
            "制造新『真知』的人\x01",
            "该不会就是你们吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0072
    ChrTalk(
        0x102,
        "#00105F#11P哎！？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        "#00208F#11P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3306")

    #C0074
    ChrTalk(
        0x109,
        "#10110F#11P难、难道……\x02",
    )

    CloseMessageWindow()

    label("loc_3306")


    #C0075
    ChrTalk(
        0x9,
        (
            "#04809F#5P哈哈，你们见到了那个\x01",
            "魔人化的不良团伙首领吗？\x02\x03",

            "我也欣赏过他的表现，\x01",
            "爆发力的确很不错呢。\x02\x03",

            "#04802F呵呵，要是能再进步些，\x01",
            "说不定可以加入『结社』呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DB")

    #C0076
    ChrTalk(
        0x105,
        "#10301F#11P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_33DB")


    #C0077
    ChrTalk(
        0x101,
        (
            "#00007F#12P不要东拉西扯！\x01",
            "回答我的问题！\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#04709F#1P哈哈，你会那样臆测，\x01",
            "倒也可以理解……\x02\x03",

            "#04702F但我们来此，只是为了\x01",
            "确认『计划』的进行度而已。\x02\x03",

            "也就是七耀脉的活性化程度……\x01",
            "以及『约定之日』的具体时机。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#00205F#12P#N『约定之日』……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00301F#12P#N啧，到底要\x01",
            "故弄玄虚到什么程度。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0081
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P……………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(8000, 1500)

    def lambda_354E():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_354E)
    WaitChrThread(0xB, 1)
    Sleep(300)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrSubChip(0xB, 0x0)
    OP_6F(0x79)
    Sleep(300)

    #C0082
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#12P已经没什么好谈的了。\x02\x03",

            "接下来，就用武力\x01",
            "撬开他们的嘴吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0083
    ChrTalk(
        0x101,
        "#00008F#6P银……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_361B")

    #C0084
    ChrTalk(
        0x109,
        (
            "#10107F#12P……看来也只有\x01",
            "这个办法了呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3647")

    label("loc_361B")


    #C0085
    ChrTalk(
        0x105,
        (
            "#10303F#12P……似乎已经\x01",
            "别无他法了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3647")

    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xF4, 0x2F)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7584", 0)
    Fade(500)
    OP_68(-970, 1050, 4590, 0)
    MoveCamera(150, 17, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(18630, 0)
    SetCameraDistance(18130, 1000)
    OP_0D()
    Sleep(300)

    #C0086
    ChrTalk(
        0x8,
        "#04704F#6P哎呀呀。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "#04804F#6P要我与你们全员对抗，\x01",
            "终究是有些勉强呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    #C0088
    ChrTalk(
        0x9,
        (
            "#04802F#12P接下来的事情\x01",
            "就交给你如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P真没办法啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3771():
        OP_9B(0x1, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3771)
    Sleep(50)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_9B(0x1, 0x9, 0x0, 0xFFFFFCE0, 0x3E8, 0x0)
    Sleep(300)
    Fade(500)
    OP_68(130, 1950, 4130, 0)
    MoveCamera(11, 10, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 1000)
    OP_6F(0x79)
    BeginChrThread(0xA, 0, 0, 22)
    Sleep(300)
    SetCameraDistance(13000, 500)
    BlurSwitch(0xA, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    CancelBlur(0)
    WaitChrThread(0xA, 0)
    OP_6F(0x79)
    OP_68(-740, 2050, -670, 1200)
    SetCameraDistance(16550, 1200)
    OP_6F(0x79)
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
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0090
    ChrTalk(
        0x101,
        "#00011F#6P#N长、长枪……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0091
    ChrTalk(
        0x102,
        (
            "#00105F#12P#N看起来，好像是\x01",
            "中世纪的骑士所使用的骑兵枪……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0092
    ChrTalk(
        0x104,
        (
            "#00306F#6P#N喂喂……\x01",
            "你拿出那种古董\x01",
            "想做什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0093
    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3890V#5P#30W多言无益。\x02\x03",

            "#3891V亮出你们的兵器，\x01",
            "全力抵挡吧。\x02\x03",

            "#3892V否则将丧命于此。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF34)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0094
    ChrTalk(
        0x101,
        "#00005F#6P#N唔……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0095
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#12P#N来了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(800)
    BeginChrThread(0xA, 3, 0, 24)
    Sleep(700)
    EndChrThread(0xA, 0x3)
    BeginChrThread(0xA, 3, 0, 25)
    BeginChrThread(0x14, 1, 0, 39)
    Fade(500)
    OP_68(-4770, 1950, -2610, 0)
    OP_68(-5000, 1850, -2610, 3000)
    MoveCamera(51, 8, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(9500, 0)
    SetCameraDistance(11000, 3000)
    Fade(500)
    CancelBlur(0)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x32, 0x5DC, 0x7D0)
    SetCameraDistance(12000, 3000)
    BeginChrThread(0xB, 3, 0, 32)
    BeginChrThread(0xB, 2, 0, 33)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x101, 2, 0, 34)
    BeginChrThread(0x102, 3, 0, 28)
    BeginChrThread(0x103, 3, 0, 29)
    BeginChrThread(0x104, 3, 0, 30)
    BeginChrThread(0xF4, 3, 0, 31)

    #C0096
    ChrTalk(
        0x102,
        "#00105F#11P#7A哎……\x02",
    )
    #Auto

    Sleep(800)

    #C0097
    ChrTalk(
        0x101,
        "#00010F#4P#N#7A什么……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0xA, 3)
    Sleep(300)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-3210, 1650, -4260, 1000)
    MoveCamera(36, 5, -1, 1000)
    OP_6E(530, 1000)
    SetCameraDistance(17220, 1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)
    Sound(369, 0, 100, 0)
    Sound(196, 0, 80, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(2031, 255, 100, 0)    #voice#Lloyd
    Sound(2129, 255, 70, 1)    #voice#Elie
    Sound(2223, 255, 100, 2)    #voice#Tio
    Sound(2318, 255, 100, 3)    #voice#Randy
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3C59")
    Sound(2464, 255, 100, 4)    #voice#Noel
    Jump("loc_3C5F")

    label("loc_3C59")

    Sound(2404, 255, 100, 4)    #voice#Lazy

    label("loc_3C5F")

    WaitChrThread(0xB, 2)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0xF4, 3)
    CancelBlur(0)
    Sleep(500)
    BeginChrThread(0xA, 3, 0, 26)
    WaitChrThread(0xA, 3)

    #C0098
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D3B")

    #C0099
    ChrTalk(
        0x109,
        "#10108F#12P#30W#N怎、怎么会……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0100
    ChrTalk(
        0x104,
        (
            "#00310F#12P#30W#N一、一瞬间发出了\x01",
            "数十击超高速的突刺吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3DAE")

    label("loc_3D3B")


    #C0101
    ChrTalk(
        0x104,
        "#00310F#12P#30W#N唔……刚才那难道是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0102
    ChrTalk(
        0x105,
        (
            "#10310F#12P#30W#N……一口气发出了\x01",
            "数十击超高速的突刺吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3DAE")


    #C0103
    ChrTalk(
        0x103,
        (
            "#00206F#12P#30W#N……不可能……\x01",
            "这不是人类能做到的……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0104
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00710F#11P#30W…………唔……………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#04702F#5P哦，居然有人可以闪过『钢\x01",
            "之圣女』的长枪呢。  \x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "#04809F#5P呵呵呵，东方人街的魔人果然不是\x01",
            "浪得虚名的呢？          \x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P很不错的反应。\x02\x03",

            "但与『上一代』相比，\x01",
            "似乎仍然心存迷茫呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    #Sound(2617, 255, 100, 0)    #voice#Yin

    #C0108
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00705F#11P#30W#10A………什么…………\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(972, 0, 100, 0)
    Sleep(800)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-90, 550, -3200, 0)
    MoveCamera(168, 27, -1, 0)
    MoveCamera(168, 23, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1000)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0x39)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 0x3A)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x3C)
    SetChrSubChip(0x104, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    ClearChrFlags(0x103, 0x20)
    SetChrChipByIndex(0x103, 0x3B)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0xF4, 0x20)
    SetChrChipByIndex(0xF4, 0x3E)
    SetChrSubChip(0xF4, 0x0)
    Sleep(300)
    OP_6F(0x79)
    OP_FD(0xC, 0xB)
    BeginChrThread(0xB, 0, 0, 40)
    WaitChrThread(0xB, 0)
    SetChrChipByIndex(0xC, 0x42)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0109
    AnonymousTalk(
        0xC,
        "#30W…………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0110
    ChrTalk(
        0x101,
        "#00011F#12P……！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#00105F#5P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        "#00307F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#00205F#11P莉夏……小姐……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_41CC")

    #C0114
    ChrTalk(
        0x109,
        "#10111F#5P哎，这……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_41FD")

    label("loc_41CC")


    #C0115
    ChrTalk(
        0x105,
        (
            "#10301F#5P好厉害……\x01",
            "可以自由改变体型吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41FD")

    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0116
    ChrTalk(
        0x9,
        (
            "#04809F#5P啊哈哈，真是太精彩了！\x02\x03",

            "『银』的真实身份\x01",
            "竟然是彩虹剧团的\x01",
            "女二号莉夏·毛！\x02\x03",

            "#04802F呵呵呵，想必可以\x01",
            "改编成很有趣的剧本呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xC,
        "#00711F#5P…………呜……………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x5, -900, -750, -23000, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_434C")

    #N0118
    NpcTalk(
        0x105,
        "少年的声音",
        (
            "#2915V#6P#29A哎呀呀，\x01",
            "场面似乎相当凶险呢。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_4380")

    label("loc_434C")


    #N0119
    NpcTalk(
        0x109,
        "女孩的声音",
        "#3519V#6P#20A各位，没事吧！？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    label("loc_4380")

    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0x5)
    OP_68(-2330, 1950, -1820, 1500)
    MoveCamera(158, 16, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(14070, 1500)
    Sleep(500)

    def lambda_4458():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_4458)
    Sleep(100)

    def lambda_4470():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4470)
    Sleep(50)

    def lambda_4488():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4488)
    Sleep(50)

    def lambda_44A0():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_44A0)

    def lambda_44B5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_44B5)
    Sleep(50)

    def lambda_44C5():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_44C5)
    Sleep(50)

    def lambda_44D5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_44D5)
    Sleep(50)

    def lambda_44E5():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_44E5)
    Sleep(50)

    def lambda_44F5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44F5)
    Sleep(150)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x5, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_456D")

    #C0120
    ChrTalk(
        0x101,
        (
            "#00008F#6P#N瓦吉……\x01",
            "连亚里欧斯先生和大家都……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A4")

    label("loc_456D")


    #C0121
    ChrTalk(
        0x101,
        (
            "#00008F#6P#N诺艾尔……\x01",
            "连亚里欧斯先生和大家都……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A4")

    OP_57(0x0)
    OP_5A()

    #C0122
    ChrTalk(
        0x102,
        "#00106F#6P你们来了啊……\x02",
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_45CD():
        OP_9B(0x0, 0xFE, 0x163, 0x1A90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_45CD)
    Sleep(100)

    def lambda_45E5():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_45E5)
    Sleep(150)

    def lambda_45FD():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_45FD)
    Sleep(50)

    def lambda_4615():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4615)
    Sleep(400)
    Fade(500)
    SetChrChipByIndex(0xC, 0x42)
    SetChrFlags(0xC, 0x1000)
    ClearChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0x1)
    OP_68(-3310, 1950, -11270, 0)
    MoveCamera(24, 9, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(13150, 0)
    WaitChrThread(0x5, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0123
    ChrTalk(
        0xE,
        "#12P那些人是……！\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        "#12P『蛇』的家伙吗……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0125
    AnonymousTalk(
        0xF,
        (
            "#4053V#11P#40W『小丑』肯帕雷拉……\x02\x03",

            "#4054V还有『十三工房』的管理者\x01",
            "和『钢之圣女』吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFD6)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    #C0126
    ChrTalk(
        0x8,
        (
            "#04705F#5P#N哦……\x01",
            "那就是『风之剑圣』吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0127
    ChrTalk(
        0x9,
        (
            "#04802F#5P#N呵呵，他的实力似乎\x01",
            "可以与莱维匹敌，可惜……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0128
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N『风之剑圣』，\x01",
            "我们还是初次见面。\x02\x03",

            "果然名不虚传，\x01",
            "看来你的确拥有很出色的实力。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0129
    ChrTalk(
        0xF,
        (
            "#01403F#11P……客套话就不必说了。\x02\x03",

            "我终究无法像你一样，\x01",
            "达至超越『人类极限』的领域。\x02\x03",

            "#01401F面对你手中的『长枪』，\x01",
            "就算是一个军队，恐怕也只能选择退却。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N呵呵，能够看出这一点，\x01",
            "就已经很了不起了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0131
    ChrTalk(
        0xD,
        "#6P亚里欧斯先生……！？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "#12P你难道……\x01",
            "打算就这么放过他们吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xF,
        (
            "#01403F#11P怎么会……\x01",
            "但现在的状况对我们很不利。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xE,
        "#12P！？\x02",
    )

    CloseMessageWindow()
    OP_68(30, 150, -9540, 1500)
    MoveCamera(24, 25, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(21930, 1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(30, 150, -9540, 0)
    MoveCamera(345, 34, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(21930, 0)
    OP_68(970, 150, -9750, 3000)
    MoveCamera(64, 29, -1, 3000)
    OP_6E(530, 3000)
    SetCameraDistance(21930, 3000)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(977, 0, 100, 0)
    BeginChrThread(0x14, 1, 0, 42)
    PlayEffect(0x5, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4B54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_4B54)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x11, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4B9F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4B9F)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4BEA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_4BEA)
    Sleep(800)
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
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4CCA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_4CCA)
    Sleep(150)

    def lambda_4CDA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4CDA)
    Sleep(150)

    def lambda_4CEA():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4CEA)
    Sleep(250)

    #C0135
    ChrTalk(
        0x10,
        "#11P…………………………\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        (
            "#5P呜……\x01",
            "是林和艾欧莉娅遭遇到的那些……！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4D8B")

    #C0137
    ChrTalk(
        0x105,
        (
            "#10301F#11P看样子，这几位小姐\x01",
            "也不是寻常之辈呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DBF")

    label("loc_4D8B")


    #C0138
    ChrTalk(
        0x109,
        (
            "#10108F#11P呜……\x01",
            "（竟然没有丝毫破绽……！？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DBF")

    OP_68(240, 1000, -7460, 1500)
    MoveCamera(25, 10, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(20910, 1500)
    OP_6F(0x79)

    #C0139
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N退下吧，\x01",
            "没必要在此地大开杀戒。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0140
    ChrTalk(
        0x11,
        "#11P是。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x12,
        "#5P呵呵，明白了。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x10,
        "#11P谨遵大人的吩咐。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    Sound(805, 0, 70, 0)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x10, 0x3F)
    SetChrChipByIndex(0x11, 0x40)
    SetChrChipByIndex(0x12, 0x41)
    OP_0D()
    Sleep(300)

    def lambda_4E93():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4E93)
    Sleep(100)

    def lambda_4EAB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4EAB)
    Sleep(100)

    def lambda_4EC3():
        OP_9B(0x1, 0xFE, 0x13B, 0xFFFFFD44, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4EC3)
    Sleep(500)

    #C0143
    ChrTalk(
        0x101,
        "#00010F#1P呜……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xC,
        "#00712F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        "#04804F#5P#N呵呵，该走了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(440, 1150, 7910, 0)
    MoveCamera(30, 11, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(19660, 0)
    SetCameraDistance(18660, 1000)
    OP_6F(0x79)

    def lambda_4F7B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4F7B)

    def lambda_4F88():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F88)

    def lambda_4F95():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4F95)

    def lambda_4FA2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4FA2)

    def lambda_4FAF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4FAF)

    def lambda_4FBC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_4FBC)

    def lambda_4FC9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_4FC9)

    def lambda_4FD6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4FD6)

    def lambda_4FE3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4FE3)

    #C0146
    ChrTalk(
        0x8,
        (
            "#04704F#5P『计划』的进行度\x01",
            "与七耀脉的状态都已确认完毕。\x02\x03",

            "#04702F呵呵，我也差不多该回去\x01",
            "进行最后的工作了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 41)
    WaitChrThread(0x9, 0)
    Sound(959, 2, 100, 0)
    PlayEffect(0x6, 0x0, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0x2, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)
    OP_93(0x101, 0x0, 0x1F4)

    #C0147
    ChrTalk(
        0x101,
        "#00007F#12P#N慢、慢着……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0148
    ChrTalk(
        0xF,
        (
            "#01407F#12P#N……无论如何也不能\x01",
            "就这么放过你们……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0149
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P给你们一个忠告吧。\x02\x03",

            "在此次『计划』中，\x01",
            "我们仅仅是配角而已。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#00005F#12P#N哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0151
    ChrTalk(
        0xF,
        "#01405F什么#12P#N……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0152
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P不久后，凶兽将会倾巢而出，\x01",
            "给此地招来混乱。\x02\x03",

            "但即使如此，你们也不应被眼前\x01",
            "发生的悲剧所束缚，请记住这一点。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "#04802F#5P呵呵呵……\x01",
            "那就告辞啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "#04709F#5P哈哈，请尽情期待\x01",
            "下一次的见面吧。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 35)
    BeginChrThread(0x102, 1, 0, 35)
    BeginChrThread(0x103, 1, 0, 35)
    BeginChrThread(0x104, 1, 0, 35)
    BeginChrThread(0xF4, 1, 0, 35)
    ClearChrFlags(0xC, 0x1000)
    ClearChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    Sound(4135, 255, 100, 0)    #voice#Companella
    OP_68(-160, 750, 1070, 8000)
    MoveCamera(31, 15, -1, 8000)
    OP_6E(530, 8000)
    SetCameraDistance(25510, 8000)
    StopEffect(0x0, 0x2)

    def lambda_535E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_535E)
    Sound(1035, 0, 100, 0)
    Sound(977, 0, 100, 0)
    Sleep(400)
    StopEffect(0x1, 0x2)

    def lambda_5381():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5381)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopEffect(0x2, 0x2)

    def lambda_539E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_539E)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopSound(959, 1000, 100)
    Sleep(600)

    def lambda_53C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_53C1)
    Sleep(400)

    def lambda_53D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_53D5)
    Sleep(400)

    def lambda_53E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_53E9)
    Sleep(400)
    StopBGM(0x1F40)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xC)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xD)
    OP_64(0xE)
    OP_64(0xF)
    OP_6F(0x79)
    Fade(500)
    OP_68(-860, 750, -6060, 0)
    MoveCamera(137, 16, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(17680, 0)
    OP_0D()
    Sleep(300)

    #C0155
    ChrTalk(
        0xE,
        "#11P啧……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xD,
        (
            "#11P『噬身之蛇』……\x01",
            "真是一群惊人的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        "#00713F#11P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 3, 0, 36)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 38)
    BeginChrThread(0x102, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 38)
    BeginChrThread(0x104, 3, 0, 38)
    BeginChrThread(0x109, 3, 0, 38)
    BeginChrThread(0x105, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 38)
    BeginChrThread(0xE, 3, 0, 38)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xE, 2)
    Sleep(100)

    #C0158
    ChrTalk(
        0x101,
        "#00011F#12P莉夏……！？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        "#00108F#11P莉夏小姐……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0160
    ChrTalk(
        0xC,
        (
            "#00714F#3248V#5P#30W……我必须要\x01",
            "赶快回去练习了。\x02\x03",

            "#00713F#3249V…………失陪……………\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCB1)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0xC, 3, 0, 37)
    Sleep(500)
    OP_68(2660, 750, -9640, 2000)
    MoveCamera(140, 15, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(23490, 2000)
    WaitChrThread(0xC, 3)
    SetChrFlags(0xC, 0x80)
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_68(-960, 750, -5650, 1500)
    MoveCamera(140, 17, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(18220, 1500)
    OP_6F(0x79)

    #C0161
    ChrTalk(
        0x101,
        "#00008F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#00108F#6P连续发生了这么多难以置信的事情，\x01",
            "一时都找不到现实感呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        "#00306F#12P………是啊………………\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x103,
        (
            "#00208F#6P感觉简直就像是\x01",
            "在做梦一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x109,
        "#10106F#6P确、确实如此……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x105,
        (
            "#10308F#12P瓦鲁多的事情也是一样……\x01",
            "不过那应该算是噩梦吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0167
    ChrTalk(
        0xF,
        "#01403F#4068V#5P#40W不过，这些全都是真切的现实。\x02",
    )

    CloseMessageWindow()
    OP_24(0xFE4)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5A64():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5A64)
    Sleep(50)

    def lambda_5A74():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A74)

    def lambda_5A81():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A81)
    Sleep(50)

    def lambda_5A91():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5A91)

    def lambda_5A9E():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A9E)

    def lambda_5AAB():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5AAB)
    Sleep(50)

    def lambda_5ABB():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5ABB)

    def lambda_5AC8():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5AC8)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)

    #C0168
    ChrTalk(
        0x101,
        "#00001F#6P亚里欧斯先生……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    #C0169
    ChrTalk(
        0xF,
        (
            "#01401F#5P『结社』的那些家伙给我们\x01",
            "留下了比预想中更多的线索。\x02\x03",

            "这个场所的意义，以及\x01",
            "『在不久后将会倾巢而出的凶兽』……\x02\x03",

            "#01403F我们现在并没有发呆的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#00013F#6P是、是的。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        "#00311F#12P（『凶兽』……难道……）\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
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

    def lambda_5C8B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C8B)

    def lambda_5C98():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C98)
    Sleep(50)

    def lambda_5CA8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5CA8)

    def lambda_5CB5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5CB5)
    Sleep(50)

    def lambda_5CC5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5CC5)

    def lambda_5CD2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5CD2)
    Sleep(50)

    def lambda_5CE2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5CE2)

    def lambda_5CEF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5CEF)
    Sleep(700)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0172
    ChrTalk(
        0x101,
        (
            "#00011F#6P啊，\x01",
            "导力波可以传到这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        "#00200F#11P嗯，这是网络覆盖范围的极限。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0174
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F您好！\x01",
            "我是特别任务支援科的班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3459V#30W……我是达德利。\x02\x03",

            "#3460V听说你们前往湖的南岸了，\x01",
            "现在正在什么地方？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD84)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0176
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F啊，这个……\x02\x03",

            "#00001F嗯……情况比较复杂，\x01",
            "亚里欧斯先生他们也在这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "正好，那就替我\x01",
            "转告他们。\x02\x03",

            "『赤色星座』的成员\x01",
            "一个不剩地从市内消失了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0178
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F#4S什么……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果方便，\x01",
            "就听听奥兰多的看法吧。\x02\x03",

            "你们最好尽快回来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0180
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010F明、明白了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 60, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0181
    ChrTalk(
        0x102,
        "#00101F#5P怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x109,
        "#10113F#5P你好像相当惊慌啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0183
    ChrTalk(
        0x101,
        "#00003F#6P嗯……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将达德利提供的情报做了简短说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0185
    ChrTalk(
        0x104,
        "#00310F#4S#11P！！\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x103,
        "#00205F#11P这……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xD,
        "#11P『赤色星座』竟然……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xE,
        (
            "#5P哼，我们也一直在关注\x01",
            "他们的动向，结果却……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xF)

    #C0189
    ChrTalk(
        0xF,
        (
            "#01403F#5P罗伊德，\x01",
            "你们赶快回市里。\x02\x03",

            "#01400F我们在这里调查完毕\x01",
            "后就会回去。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_62AA():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_62AA)
    Sleep(50)

    def lambda_62BA():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_62BA)

    def lambda_62C7():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62C7)
    Sleep(50)

    def lambda_62D7():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62D7)

    def lambda_62E4():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62E4)

    def lambda_62F1():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_62F1)
    Sleep(250)

    #C0190
    ChrTalk(
        0x101,
        (
            "#00011F#6P啊……\x02\x03",

            "#00003F……不好意思，\x01",
            "那真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        "#00306F#12P……多谢了。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xD,
        "#11P在这种时候就要互相协助。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xE,
        (
            "#5P而且林和艾欧莉娅\x01",
            "一时还无法动弹。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xF,
        (
            "#01403F#5P如果『赤色星座』已经出动，\x01",
            "『黑月』应该也会有所行动……\x02\x03",

            "#01401F我们会尽快回去的，\x01",
            "你们一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#00007F#6P是……！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x109,
        "#10107F#6P那就先告辞了！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20180, 2000)
    StopSound(122, 2000, 50)
    StopSound(123, 2000, 70)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x0, 0x10000)
    OP_24(0x323)
    SoundLoad(959)
    SoundLoad(825)
    SetScenarioFlags(0x22, 1)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2872 end

    def Function_19_6496(): pass

    label("Function_19_6496")

    OP_71(0x0, 0x157, 0x16C, 0x0, 0x0)
    OP_79(0x0)
    Sound(913, 0, 100, 0)
    OP_71(0x0, 0x16D, 0x17E, 0x0, 0x20)
    Return()

    # Function_19_6496 end

    def Function_20_64B8(): pass

    label("Function_20_64B8")

    Sound(970, 0, 100, 0)
    Sound(920, 0, 100, 0)
    Sound(202, 0, 100, 0)
    PlayEffect(0x9, 0xFF, 0xFE, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(893, 0, 70, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(156)
    SetChrSubChip(0xFE, 0x9)
    Sleep(144)
    SetChrSubChip(0xFE, 0xA)
    Sleep(132)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(108)
    SetChrSubChip(0xFE, 0xD)
    Sleep(96)
    SetChrSubChip(0xFE, 0xE)
    Sleep(84)
    SetChrSubChip(0xFE, 0xF)
    Sleep(72)

    label("loc_6552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65A4")
    Sound(893, 0, 50, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(60)
    SetChrSubChip(0xFE, 0x9)
    Sleep(60)
    SetChrSubChip(0xFE, 0xA)
    Sleep(60)
    SetChrSubChip(0xFE, 0xB)
    Sleep(60)
    SetChrSubChip(0xFE, 0xC)
    Sleep(60)
    SetChrSubChip(0xFE, 0xD)
    Sleep(60)
    SetChrSubChip(0xFE, 0xE)
    Sleep(60)
    SetChrSubChip(0xFE, 0xF)
    Sleep(60)
    Jump("loc_6552")

    label("loc_65A4")

    Sound(893, 0, 60, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(72)
    SetChrSubChip(0xFE, 0x9)
    Sleep(84)
    SetChrSubChip(0xFE, 0xA)
    Sleep(96)
    SetChrSubChip(0xFE, 0xB)
    Sleep(108)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xD)
    Sleep(132)
    SetChrSubChip(0xFE, 0xE)
    Sleep(144)
    SetChrSubChip(0xFE, 0xF)
    Sleep(156)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 50, 0)
    Sound(308, 0, 100, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(400)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_64B8 end

    def Function_21_6604(): pass

    label("Function_21_6604")

    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x1F4, 0x1)
    Return()

    # Function_21_6604 end

    def Function_22_6617(): pass

    label("Function_22_6617")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 60, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 20)
    BeginChrThread(0x15, 2, 0, 21)
    Sleep(2500)
    ClearScenarioFlags(0x0, 1)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x15, 3)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(3000)
    OP_82(0x0, 0x64, 0x1388, 0x320)
    SetCameraDistance(11000, 250)

    def lambda_66B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_66B6)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    Sound(288, 0, 70, 0)
    Sound(308, 0, 100, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(100)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Return()

    # Function_22_6617 end

    def Function_23_670C(): pass

    label("Function_23_670C")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(150)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(800)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(100)
    Return()

    # Function_23_670C end

    def Function_24_6776(): pass

    label("Function_24_6776")

    SetChrChipByIndex(0xFE, 0x31)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Return()

    # Function_24_6776 end

    def Function_25_6795(): pass

    label("Function_25_6795")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_67AD():
        OP_9D(0xFE, 0xFFFFFF06, 0xFFFFFD12, 0x726, 0x96, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_67AD)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x4, 0x0, 0xFE, 0x4, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    StopEffect(0x0, 0x2)
    Return()

    # Function_25_6795 end

    def Function_26_68A6(): pass

    label("Function_26_68A6")

    SetChrSubChip(0xFE, 0x5)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 60, 0)
    Sound(250, 0, 80, 0)

    def lambda_68C6():
        OP_9D(0xFE, 0x258, 0xFA, 0x1900, 0x60E, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_68C6)
    WaitChrThread(0xFE, 2)
    Sound(326, 0, 50, 0)
    Sleep(300)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(531, 0, 60, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    Return()

    # Function_26_68A6 end

    def Function_27_6912(): pass

    label("Function_27_6912")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)

    label("loc_691A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6941")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_691A")

    label("loc_6941")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    Sound(251, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0xFFFFFE70, 0xFFFFF34E, 0x2EE, 0x3AB6)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(150)
    Return()

    # Function_27_6912 end

    def Function_28_69BE(): pass

    label("Function_28_69BE")

    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    label("loc_69C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69ED")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_69C6")

    label("loc_69ED")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0xFA, 0x0, 0xFFFFF34E, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_28_69BE end

    def Function_29_6A5E(): pass

    label("Function_29_6A5E")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    label("loc_6A66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A8D")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_6A66")

    label("loc_6A8D")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFEF66, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_29_6A5E end

    def Function_30_6AFE(): pass

    label("Function_30_6AFE")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)

    label("loc_6B06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B2D")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_6B06")

    label("loc_6B2D")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0xFFFFFF06, 0x0, 0xFFFFF15A, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(150)
    Return()

    # Function_30_6AFE end

    def Function_31_6BA4(): pass

    label("Function_31_6BA4")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)

    label("loc_6BAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BD3")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_6BAC")

    label("loc_6BD3")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0x190, 0x0, 0xFFFFF34E, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_31_6BA4 end

    def Function_32_6C44(): pass

    label("Function_32_6C44")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xDAC, 0x0, 0xFFFFFE0C, 0x3E8, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xFFFFF060, 0x0, 0x0, 0x5DC, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0xC8, 0xBB8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)

    label("loc_6CAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC2")
    Sleep(1)
    Jump("loc_6CAB")

    label("loc_6CC2")

    Sleep(200)
    OP_9D(0xFE, 0xC8, 0xFFFFFD12, 0xFFFFF3E4, 0x2EE, 0x5DC)
    Return()

    # Function_32_6C44 end

    def Function_33_6CDD(): pass

    label("Function_33_6CDD")

    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_33_6CDD end

    def Function_34_6E15(): pass

    label("Function_34_6E15")

    Sleep(50)
    PlayEffect(0x7, 0xFF, 0x101, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x7, 0xFF, 0x102, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x7, 0xFF, 0x103, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x7, 0xFF, 0x104, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x7, 0xFF, 0xF4, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_34_6E15 end

    def Function_35_6F38(): pass

    label("Function_35_6F38")

    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_6F38 end

    def Function_36_6F4B(): pass

    label("Function_36_6F4B")

    OP_93(0xFE, 0xB3, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x514, 0x4B0, 0x0)
    OP_95(0xFE, 470, -750, -5220, 1200, 0x0)
    OP_93(0xFE, 0x87, 0x0)
    Return()

    # Function_36_6F4B end

    def Function_37_6F80(): pass

    label("Function_37_6F80")

    SetChrFlags(0xFE, 0x40)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x5, 0x3E8, 0x1B58, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x3E8, 0x1B58, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x3E8, 0x1B58, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_9B(0x0, 0xFE, 0x5, 0x9C4, 0x1B58, 0x1)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0xDAC, 0x6D6, 0xFFFFDECC, 0x7D0, 0xDAC)
    ClearChrFlags(0xFE, 0x20)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x1B58, 0x1)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0x3E8, 0xFA0, 0xFFFFF768, 0x1388, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_37_6F80 end

    def Function_38_7072(): pass

    label("Function_38_7072")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_708C")
    TurnDirection(0xFE, 0xC, 500)
    Sleep(300)
    Jump("Function_38_7072")

    label("loc_708C")

    Return()

    # Function_38_7072 end

    def Function_39_708D(): pass

    label("Function_39_708D")

    Sleep(200)
    Sound(287, 0, 100, 0)
    Sound(270, 0, 80, 0)
    Sound(225, 0, 70, 0)
    Sound(833, 0, 70, 0)
    Sound(825, 2, 100, 0)
    Sleep(1000)
    Sound(271, 0, 80, 0)
    Sound(287, 0, 60, 0)
    Sleep(1000)
    StopSound(225, 1000, 40)
    StopSound(825, 1000, 90)
    Return()

    # Function_39_708D end

    def Function_40_70CD(): pass

    label("Function_40_70CD")

    SetChrChipByIndex(0xFE, 0x42)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    Sound(1037, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(400)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)
    SetChrSubChip(0xFE, 0x2)
    Sleep(400)
    Sound(1037, 0, 70, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(400)
    SetChrSubChip(0xFE, 0x4)
    Sleep(400)
    Return()

    # Function_40_70CD end

    def Function_41_710B(): pass

    label("Function_41_710B")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    Return()

    # Function_41_710B end

    def Function_42_7124(): pass

    label("Function_42_7124")

    Sleep(1500)
    Sound(936, 0, 100, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Return()

    # Function_42_7124 end

    SaveToFile()

Try(main)
