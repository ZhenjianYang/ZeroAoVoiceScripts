from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t2030.bin",                # FileName
        "t2030",                    # MapName
        "t2030",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 0, 0, 1],
    )

    BuildStringList((
        "t2030",                  # 0
        "诺艾尔少尉",             # 1
        "索妮亚司令",             # 2
        "人偶",                   # 3
        "模型",                   # 4
        "bt2030",                 # 5
    ))

    ATBonus("ATBonus_20C", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2FC", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_31C", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bt2030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2FC", "MonsterBattlePostion_2DC", "ed7452", "ed7452", "ATBonus_20C"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 4,   -18.0,                 -4.0,                  -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.0,                   0.800000011920929,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 8,   -37.630001068115234,   -14.710000038146973,   -3.2200000286102295,   900.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.05000000074505806,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.543334007263184,    0.7355000376701355,    0.6439999938011169,    1.0])

    DeclActor(21160,   -580,    -4620,   1200,    23230,   500,     -5230,   0x007C, 0,  7,  0x0000)
    DeclActor(16000,   0,       -29500,  1200,    16000,   1500,    -29500,  0x007C, 0,  2,  0x0000)

    ChipFrameInfo(904, 0)                                        # 0

    ScpFunction((
        "Function_0_388",          # 00, 0
        "Function_1_3AC",          # 01, 1
        "Function_2_452",          # 02, 2
        "Function_3_4F7",          # 03, 3
        "Function_4_A45",          # 04, 4
        "Function_5_1D3E",         # 05, 5
        "Function_6_234F",         # 06, 6
        "Function_7_236E",         # 07, 7
        "Function_8_2B23",         # 08, 8
        "Function_9_2BDE",         # 09, 9
    ))


    def Function_0_388(): pass

    label("Function_0_388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_39C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_3AB")

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3AB")
    ClearScenarioFlags(0x22, 1)
    Event(0, 5)

    label("loc_3AB")

    Return()

    # Function_0_388 end

    def Function_1_3AC(): pass

    label("Function_1_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DA")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_3DA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DA")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F2")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_3F2")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_425")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x1, 0x4)

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_434")
    OP_1B(0x3, 0x0, 0x9)

    label("loc_434")

    OP_65(0x1, 0x1)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_451")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x0, 0x4)

    label("loc_451")

    Return()

    # Function_1_3AC end

    def Function_2_452(): pass

    label("Function_2_452")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着《鸡尾酒调配指南》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_4F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x18)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『桃色蔷薇』\x07\x00",
            "的食谱已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4F3")

    TalkEnd(0xFF)
    Return()

    # Function_2_452 end

    def Function_3_4F7(): pass

    label("Function_3_4F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 29000, -2220, -10000, 270)
    SetChrPos(0x106, 30500, -2220, -10680, 270)
    SetChrPos(0x103, 29960, -2220, -9450, 270)
    SetChrPos(0x104, 31060, -2220, -9070, 270)
    SetChrPos(0x107, 32970, -2220, -9240, 270)
    SetChrPos(0x105, 31580, -2220, -10100, 270)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x105, 0x8)
    CreatePortrait(0, 16, 20, 528, 84, 0, 10, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis512.itp")
    OP_68(-3050, -700, -11150, 0)
    MoveCamera(318, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(34300, 0)
    FadeToBright(1000, 0)
    OP_68(10100, -700, -13000, 9000)
    MoveCamera(312, 10, 0, 9000)
    Sleep(2500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    Fade(1000)
    OP_68(23250, -700, -10100, 0)
    MoveCamera(305, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(15750, 2500)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x105, 0x8)

    def lambda_6AF():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6AF)
    Sleep(50)

    def lambda_6C7():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6C7)
    Sleep(50)

    def lambda_6DF():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6DF)
    Sleep(50)

    def lambda_6F7():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6F7)
    Sleep(50)

    def lambda_70F():
        OP_9B(0x0, 0x106, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_70F)
    Sleep(50)

    def lambda_727():
        OP_9B(0x0, 0x107, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_727)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_END)), "loc_814")

    #C0003
    ChrTalk(
        0x101,
        (
            "#00003F#11P货运站台……\x01",
            "好久没来这里了。\x02\x03",

            "#00001F真是万幸，\x01",
            "这里好像没有人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#00306F#12P嗯，毕竟铁道列车\x01",
            "已经停运了。\x02\x03",

            "#00300F国防军肯定不会\x01",
            "派太多人手看守这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_897")

    label("loc_814")


    #C0005
    ChrTalk(
        0x101,
        "#00005F#11P这里是……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00303F#12P哦，是贝尔加德门的\x01",
            "货运站台。\x02\x03",

            "#00300F由于铁道列车已经停运了，\x01",
            "所以好像没有派人来看守。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_897")


    #C0007
    ChrTalk(
        0x103,
        (
            "#00204F#12P原来如此……\x01",
            "看来正是潜入的好机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x105,
        (
            "#10408F#12P如果索妮亚司令在这里，\x01",
            "应该会待在二楼的司令室吧。\x02\x03",

            "#10401F如果能在不被任何人察觉的情况下\x01",
            "抵达那里就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x106,
        (
            "#10703F#12P万一遇到紧急情况，\x01",
            "就由我来发动佯攻，引开敌人。\x02\x03",

            "#10701F总之，先上去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00001F#11P知道了……\x01",
            "不过，你可千万别太勉强自己哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x107,
        "#01200F#3C#12P唔……上去看看吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 22000, -2220, -10000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 2)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_3_4F7 end

    def Function_4_A45(): pass

    label("Function_4_A45")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch03900.itc", 0x1E)
    LoadChrToIndex("chr/ch03950.itc", 0x1F)
    LoadChrToIndex("chr/ch03951.itc", 0x20)
    LoadChrToIndex("chr/ch03952.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00051.itc", 0x23)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10200.itp")
    SoundLoad(3526)
    SoundLoad(3527)
    SoundLoad(3528)
    SoundLoad(3529)
    SoundLoad(3530)
    SoundLoad(4116)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -17000, 0, -4000, 90)
    SetChrPos(0x106, -17810, 0, -3210, 90)
    SetChrPos(0x103, -18390, 0, -4720, 90)
    SetChrPos(0x104, -18930, 0, -3660, 90)
    SetChrPos(0x107, -19460, 0, -2370, 90)
    SetChrPos(0x105, -19650, 0, -4890, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -4800, 0, -3800, 270)
    SetChrFlags(0x8, 0x8)
    OP_32(0xFF, 0xF9, 0x0)
    OP_68(-13000, 1200, -4000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(16000, 2500)

    def lambda_BCB():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BCB)
    Sleep(30)

    def lambda_BE3():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BE3)
    Sleep(30)

    def lambda_BFB():
        OP_9B(0x0, 0x104, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BFB)
    Sleep(30)

    def lambda_C13():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C13)
    Sleep(30)

    def lambda_C2B():
        OP_9B(0x0, 0x106, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_C2B)
    Sleep(30)

    def lambda_C43():
        OP_9B(0x0, 0x107, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_C43)
    Sleep(1500)
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)

    #N0012
    NpcTalk(
        0x8,
        "女孩的声音",
        "#3526V#1P#12A#30W请留步。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-12500, 1000, -4000, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-11500, 1000, -4000, 2500)
    SetCameraDistance(15200, 2500)
    SetChrSubChip(0x107, 0x5)
    ClearChrFlags(0x8, 0x8)
    OP_9B(0x0, 0x8, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_6F(0x79)
    OP_0D()

    #C0013
    ChrTalk(
        0x101,
        "#00005F#6P诺艾尔……！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        "#00201F#6P为什么……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7575", 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0015
    AnonymousTalk(
        0x8,
        (
            "国防军一直都对\x01",
            "各位的动向\x01",
            "有大致掌握。\x02\x03",

            "你们在玛因兹地区与反抗军\x01",
            "达成合作关系之后……\x02\x03",

            "下一个目的地应该\x01",
            "就是这里了，\x01",
            "因此我一直在默默警戒。\x02",
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

    #C0016
    ChrTalk(
        0x105,
        "#10406F#6P哎呀呀……真是服了。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#00301F#6P真是厉害啊……\x01",
            "诺艾尔，你判断得很出色。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#10206F#11P其实我并不希望\x01",
            "自己的预料成真……\x02\x03",

            "#10201F你们是来找索妮亚司令\x01",
            "谈话的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00003F#6P嗯……正是。\x02\x03",

            "#00001F我们从米蕾优三尉那里得知，\x01",
            "现在有不少人都对\x01",
            "国防军抱有疑问。\x02\x03",

            "为了打破这种局面，\x01",
            "我们想知道司令的真实想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "#10208F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        (
            "#00206F#6P诺艾尔小姐……\x01",
            "芙兰小姐也在和我们\x01",
            "一起行动。\x02\x03",

            "#00201F她已经彻底痊愈了……\x01",
            "一直都很想见你。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#00306F#6P我们并不强求你叛变……\x02\x03",

            "#00300F只希望你能给我们一个\x01",
            "和司令交涉的机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        "#10203F#11P即使如此……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetCameraDistance(15000, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_A1(0x8, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x8,
        (
            "#10201F#11P即使如此，我也不能\x01",
            "让你们继续前行。\x02\x03",

            "我身为国防军的士兵……\x02\x03",

            "绝不能对潜入此处的\x01",
            "反抗势力视而不见。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x106,
        "#10708F#6P诺艾尔小姐……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#10406F#6P……哎呀呀，\x01",
            "你真是个不知变通的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#00001F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#10206F#11P请你们回去吧，各位。\x02\x03",

            "现在离开……\x01",
            "我还可以当作没看见你们。\x02\x03",

            "#10208F就算我们迟早有一天\x01",
            "要在战场上相见……\x02\x03",

            "#10213F……但……至少现在……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#00004F#6P你太天真了，诺艾尔。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0030
    ChrTalk(
        0x8,
        "#10205F#11P……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-10390, 1000, -3670, 1000)
    OP_9B(0x0, 0x101, 0x0, 0x320, 0x3E8, 0x0)
    OP_6F(0x79)

    #C0031
    ChrTalk(
        0x101,
        (
            "#00001F#6P如果你真的是国防军的军人，\x01",
            "就不应该说这种没用的话。\x02\x03",

            "直接呼叫援军把我们包围，\x01",
            "并当场将我们制服就行了。\x02\x03",

            "#00006F但你却说着这种伤感的话，\x01",
            "劝说我们离开……\x02\x03",

            "#00013F就凭你这种不坚定的觉悟，\x01",
            "还想为大义献身吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "#10210F#11P……唔………\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x106,
        "#10708F#6P罗伊德警官……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        (
            "#10404F#6P#N哈哈……\x01",
            "一反常态地严厉啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00003F#6P坦白告诉你吧——\x01",
            "诺艾尔，你变弱了。\x02\x03",

            "你已经不再像从前一样坦然面对\x01",
            "自己的内心，勇往直前地前进了。\x02\x03",

            "#00000F现在的你……\x01",
            "就连我这个军外人士都战胜不了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetCameraDistance(14750, 500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x8,
        "#10211F#11P！？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        "#00205F#6P#N罗、罗伊德前辈？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0038
    ChrTalk(
        0x104,
        "#00307F#6P喂喂，你想干什么……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00004F#6P我要和你一对一单挑，\x01",
            "随便你使用任何武器。\x02\x03",

            "如果你赢了，\x01",
            "就可以把我们所有人都逮捕。\x02\x03",

            "#00013F反之，\x01",
            "如果我赢了，你就是我的人了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(150)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0040
    ChrTalk(
        0x8,
        "#10205F#3527V#11P#10A#30W#4S哎？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1300)
    OP_64(0xFFFF)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Fade(150)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)

    def lambda_17EB():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17EB)
    SetChrFlags(0x8, 0x20)
    OP_9B(0x1, 0x8, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
    ClearChrFlags(0x8, 0x20)
    WaitChrThread(0x8, 2)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x320)

    #C0041
    ChrTalk(
        0x8,
        "#10214F#3528V#11P#29A#50W你、你你……你到底在说什么……！？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0042
    ChrTalk(
        0x101,
        (
            "#00006F#6P我实在是看不下去了。\x02\x03",

            "#00008F你一直待在不适合自己的地方，\x01",
            "已经渐渐失去自我……\x02\x03",

            "#00013F身为同伴，\x01",
            "我绝不能置之不顾。\x02\x03",

            "#00007F决一胜负吧！\x01",
            "诺艾尔·希卡少尉！\x02",
        )
    )

    CloseMessageWindow()
    Fade(150)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    #Sound(2463, 255, 100, 0)    #voice#Noel

    #C0043
    ChrTalk(
        0x8,
        "#10210F#11P#6A唔……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(809, 0, 70, 0)
    OP_68(-9600, 1000, -3670, 1000)
    OP_9C(0x8, 0x3E8, 0x0, 0x0, 0x12C, 0xFA0)
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_A1(0x8, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-12500, 1000, -4000, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x107, 0x190, 1900, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)

    #C0044
    ChrTalk(
        0x104,
        (
            "#00306F#6P（喂喂喂喂……！\x01",
            "  这样也行！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#00211F#6P（……真没想到。）\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x106,
        "#10709F#6P（……这………）\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x105,
        (
            "#10402F#6P（嗯……这似乎也算是\x01",
            "  他的特别天赋吧……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x107,
        "#01203F#3C#6P（呵呵，的确如此。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    Fade(500)
    PlayBGM("ed7452", 0)
    OP_68(-9630, 1000, -3450, 0)
    MoveCamera(325, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(-9630, 1000, -3450, 13000)
    MoveCamera(49, 18, 0, 13000)
    OP_6E(600, 13000)
    SetCameraDistance(15000, 13000)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0049
    ChrTalk(
        0x8,
        (
            "#10210F#3529V#11P#30A#30W好！我接受！\x01",
            "我绝对不会输给你的！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0050
    ChrTalk(
        0x8,
        (
            "#10207F#3530V#4S#11P#27A决一胜负吧！\x01",
            "罗伊德·班宁斯搜查官！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xDCA)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(4116, 255, 100, 0)    #voice#Lloyd

    #C0051
    ChrTalk(
        0x101,
        "#00007F#4S#6P#22A好，放马过来吧！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(5000, 1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x101, 0x1000)

    def lambda_1CB5():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CB5)

    def lambda_1CCA():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CCA)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x8, 0x1)
    ClearChrFlags(0x101, 0x1000)
    SetChrBattleFlags(0x106, 0x8)
    SetChrBattleFlags(0x103, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    SetChrBattleFlags(0x107, 0x8)
    Battle("BattleInfo_31C", 0x0, 0x0, 0x0, 0x22, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrBattleFlags(0x106, 0x8)
    ClearChrBattleFlags(0x103, 0x8)
    ClearChrBattleFlags(0x104, 0x8)
    ClearChrBattleFlags(0x105, 0x8)
    ClearChrBattleFlags(0x107, 0x8)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 5)
    Return()

    # Function_4_A45 end

    def Function_5_1D3E(): pass

    label("Function_5_1D3E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03900.itc", 0x1E)
    LoadChrToIndex("chr/ch12200.itc", 0x1F)
    LoadChrToIndex("chr/ch03953.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10600.itp")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -11000, 0, -4000, 90)
    SetChrPos(0x106, -13810, 0, -3210, 90)
    SetChrPos(0x103, -14390, 0, -4720, 90)
    SetChrPos(0x104, -14930, 0, -3660, 90)
    SetChrPos(0x107, -15460, 0, -2370, 90)
    SetChrPos(0x105, -15650, 0, -4890, 90)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    BeginChrThread(0x101, 0, 0, 6)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -8000, 0, -4000, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 5000, 180)
    SetChrFlags(0x9, 0x8)
    OP_68(-9500, 1000, -4000, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14000, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00015F#40W#6P呼……呼……\x02\x03",

            "#00000F#30W……是我……赢了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EE9():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1EE9)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0053
    ChrTalk(
        0x8,
        (
            "#10206F#40W#11P……呜………\x01",
            "…………呜呜…………\x02\x03",

            "#10208F……抱歉……\x01",
            "………索妮亚司令………\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x8)

    #N0054
    NpcTalk(
        0x9,
        "女性的声音",
        "#12P你并不需要道歉。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1000, 1500, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 2500)
    OP_9B(0x0, 0x9, 0x0, 0xDAC, 0x7D0, 0x0)
    TurnDirection(0x9, 0x8, 500)
    OP_6F(0x79)
    OP_0D()

    #C0055
    ChrTalk(
        0x101,
        "#00005F#6P#N啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0056
    ChrTalk(
        0x8,
        "#10213F#30W#6P#N司、司令……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0057
    ChrTalk(
        0x104,
        "#00307F#6P#N哇哇……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0058
    ChrTalk(
        0x107,
        "#01200F#3C#6P#N唔，原来已经被发现了啊。\x02",
    )

    CloseMessageWindow()
    OP_68(-500, 1000, 1300, 3000)

    def lambda_2123():
        OP_9B(0x0, 0xFE, 0x8, 0x2260, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2123)
    Sleep(1500)
    Fade(500)
    OP_68(-9550, 1000, -3150, 0)
    MoveCamera(48, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(13500, 3000)
    EndChrThread(0x101, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    Sleep(800)
    Fade(150)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0059
    AnonymousTalk(
        0x9,
        (
            "你们战斗的声音\x01",
            "已经传到楼上了哦。\x02\x03",

            "不过，我已经把别人都支走了。\x02",
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

    #C0060
    ChrTalk(
        0x101,
        "#00006F#6P非、非常感谢……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#00202F#6P#N……好久不见了，\x01",
            "索妮亚司令。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0062
    ChrTalk(
        0x9,
        (
            "#10602F#11P是啊，真的好久不见了。\x02\x03",

            "#10606F我大致猜到了你们\x01",
            "来拜访我的原因……\x02\x03",

            "#10600F总之，到我的办公室里\x01",
            "慢慢谈吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(13300, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t2020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1D3E end

    def Function_6_234F(): pass

    label("Function_6_234F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_236D")
    OP_A1(0xFE, 0x320, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_6_234F")

    label("loc_236D")

    Return()

    # Function_6_234F end

    def Function_7_236E(): pass

    label("Function_7_236E")

    EventBegin(0x0)
    Fade(500)
    OP_68(21050, 720, -4390, 0)
    MoveCamera(323, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15640, 0)
    SetChrPos(0x101, 20740, 0, -3990, 90)
    SetChrPos(0x102, 20620, -890, -4950, 90)
    SetChrPos(0x103, 19290, 0, -3680, 90)
    SetChrPos(0x104, 20630, -1840, -5960, 90)
    SetChrPos(0x109, 19070, -750, -4810, 90)
    SetChrPos(0x105, 19080, -1810, -5930, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0063
    ChrTalk(
        0x101,
        "#5P#00005F竟、竟然藏在这种地方……！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        (
            "#5P#10103F卡片上的提示是……\x01",
            "『从西方卫士们脚下通过的钢铁之道』……\x02\x03",

            "#10100F原来是指守卫西侧边境的贝尔加德门的\x01",
            "地下货运站台啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x105,
        (
            "#6P#10304F在这种地方不方便\x01",
            "打开箱子。\x02\x03",

            "#10302F先把它抬到那边的站台上吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#11P#00000F嗯，搬运时要小心一些。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-28050, 1300, -26470, 0)
    MoveCamera(303, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13840, 0)
    OP_78(0x1, 0xB)
    SetChrPos(0xB, -29850, 0, -26100, 0)
    OP_D5(0xB, 0x0, 0xFFFEA070, 0x0, 0x0)
    SetChrPos(0x101, -28270, 0, -26080, 270)
    SetChrPos(0x102, -28200, 0, -27310, 270)
    SetChrPos(0x103, -28200, 0, -24750, 270)
    SetChrPos(0x104, -27050, 0, -26080, 270)
    SetChrPos(0x109, -27050, 0, -27310, 270)
    SetChrPos(0x105, -27050, 0, -24750, 270)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x8)
    SetChrPos(0xA, -29850, 150, -26100, 0)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(1024, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x1)
    Sleep(1000)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在皮箱的内侧\x01",
            "贴着一张卡片。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0068
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最后的牢笼位于市内。\x01",
            "前往高耸入云的摩天大楼，\x01",
            "由十六层之顶下行二十一层，\x01",
            "寻找众多窥视异界的窗口。\x07\x00\x02",
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

    #C0069
    ChrTalk(
        0x102,
        (
            "#6P#00100F没错，这就是\x01",
            "一直被贝尔称作\x01",
            "『夏伦』的人偶。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#12P#00303F这是第四个了……\x01",
            "还剩下最后一个。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#12P#00200F卡片上所写的文字应该\x01",
            "提示了最后一个人偶的所在地。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x109,
        (
            "#6P#10103F『市内』的『高耸入云的摩天大楼』……\x01",
            "想必是相当高的建筑。\x02\x03",

            "#10101F莫非是指那个兰花塔……？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        (
            "#6P#00103F唔……但兰花塔\x01",
            "高达四十层……\x02\x03",

            "#00100F和『十六层之顶』这种\x01",
            "表述存在矛盾，\x01",
            "所以应该不是。\x02\x03",

            "#00106F另外，『由十六层之顶下行二十一层』\x01",
            "这句话本身就存在矛盾……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x105,
        (
            "#12P#10300F这个矛盾也许正是\x01",
            "揭开谜题的关键呢。\x02\x03",

            "#10304F『众多窥视异界的窗口』……\x01",
            "这句话又指什么呢？\x01",
            "也必须要仔细思考一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#12P#00003F我想应该和前几次一样，\x01",
            "是一种比喻的手法。\x02\x03",

            "#00000F我们一边思考其中含义，\x01",
            "一边在市内搜寻吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16I罗赞贝尔克人偶·Ｓ\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x338, 1)
    SetMapObjFlags(0x1, 0x4)
    SetChrFlags(0xA, 0x80)
    OP_D7(0x1E)
    SetChrPos(0x0, -27660, 0, -26170, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x157, 4)
    OP_29(0x7A, 0x1, 0x5)
    OP_65(0x0, 0x1)
    EventEnd(0x5)
    Return()

    # Function_7_236E end

    def Function_8_2B23(): pass

    label("Function_8_2B23")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6A")

    #C0077
    ChrTalk(
        0x101,
        (
            "#00000F在铁道上继续前进是很危险的，\x01",
            "还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA2")

    label("loc_2B6A")


    #C0078
    ChrTalk(
        0x101,
        (
            "#00001F……前方是卡雷利亚要塞，\x01",
            "无法再继续前行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA2")

    OP_5A()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x38A4), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BCA")
    SetChrPos(0x0, -34000, -2220, -18820, 90)
    Jump("loc_2BDB")

    label("loc_2BCA")

    SetChrPos(0x0, -34000, -2220, -10970, 90)

    label("loc_2BDB")

    EventEnd(0x4)
    Return()

    # Function_8_2B23 end

    def Function_9_2BDE(): pass

    label("Function_9_2BDE")

    EventBegin(0x1)

    #C0079
    ChrTalk(
        0x101,
        (
            "#00000F在铁道上继续前进是很危险的，\x01",
            "还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x38A4), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C3E")
    SetChrPos(0x0, 27940, -2220, -18600, 270)
    Jump("loc_2C4F")

    label("loc_2C3E")

    SetChrPos(0x0, 28100, -2220, -10060, 270)

    label("loc_2C4F")

    EventEnd(0x4)
    Return()

    # Function_9_2BDE end

    SaveToFile()

Try(main)
