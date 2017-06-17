from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9010.bin",                # FileName
        "m9010",                    # MapName
        "m9010",                    # Location
        0x0000,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9010",                  # 0
        "升降机",                 # 1
        "SE控制",                 # 2
    ))

    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(216, 0)                                        # 0

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_E8",           # 01, 1
        "Function_2_ED",           # 02, 2
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_E7")

    Return()

    # Function_0_D8 end

    def Function_1_E8(): pass

    label("Function_1_E8")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_E8 end

    def Function_2_ED(): pass

    label("Function_2_ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(1032)
    LoadEffect(0x0, "event/ev17066.eff")
    LoadEffect(0x1, "event/ev17065.eff")
    SetChrPos(0x101, -900, 0, 1500, 315)
    SetChrPos(0x102, 900, 0, 1500, 45)
    SetChrPos(0x103, -1600, 0, 0, 270)
    SetChrPos(0x104, 1600, 0, 0, 90)
    SetChrPos(0xF4, -900, 0, -1500, 225)
    SetChrPos(0xF5, 900, 0, -1500, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(0, 1550, 0, 0)
    MoveCamera(245, 51, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(34950, 0)
    OP_68(0, 1550, 0, 8000)
    MoveCamera(325, 21, 0, 8000)
    OP_6E(1000, 8000)
    SetCameraDistance(9870, 8000)
    OP_78(0x0, 0x8)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x4)
    Sound(1032, 2, 100, 0)
    Sound(112, 2, 30, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    MoveCamera(350, 21, 0, 30000)
    Sleep(1000)

    #C0001
    ChrTalk(
        0x102,
        "#00105F#6P#40W这、这是……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C0")
    OP_FC(0xC)
    Jump("loc_2C3")

    label("loc_2C0")

    OP_FC(0x6)

    label("loc_2C3")


    #C0002
    ChrTalk(
        0x109,
        "#10105F#13P#40W克洛斯贝尔各地区的状况……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA")

    label("loc_2F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_323")
    OP_FC(0xC)
    Jump("loc_326")

    label("loc_323")

    OP_FC(0x6)

    label("loc_326")


    #C0003
    ChrTalk(
        0x106,
        "#10712F#13P#40W克洛斯贝尔各地区的状况……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA")

    label("loc_35C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_386")
    OP_FC(0xC)
    Jump("loc_389")

    label("loc_386")

    OP_FC(0x6)

    label("loc_389")


    #C0004
    ChrTalk(
        0x10A,
        "#00605F#13P#40W克洛斯贝尔各地区的状况……？\x02",
    )

    CloseMessageWindow()

    label("loc_3BA")

    OP_57(0x0)
    OP_5A()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00306F#6P#40W不……不止如此。\x02\x03",

            "#00301F其中似乎还混杂着\x01",
            "过去发生的一些事情……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x103,
        (
            "#00208F#12P#40W现实世界的碎片……\x02\x03",

            "#00201F跨越时空，\x01",
            "相互联系的因果……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_492")
    OP_FC(0xC)
    Jump("loc_495")

    label("loc_492")

    OP_FC(0x6)

    label("loc_495")


    #C0007
    ChrTalk(
        0x105,
        (
            "#10406F#13P#40W……似乎不能断然\x01",
            "否定这种可能性。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A3")

    label("loc_4D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FA")
    OP_FC(0xC)
    Jump("loc_4FD")

    label("loc_4FA")

    OP_FC(0x6)

    label("loc_4FD")


    #C0008
    ChrTalk(
        0x10A,
        (
            "#00606F#13P#40W本想说不可能……\x01",
            "但似乎并不能如此断言。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A3")

    label("loc_53E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_568")
    OP_FC(0xC)
    Jump("loc_56B")

    label("loc_568")

    OP_FC(0x6)

    label("loc_56B")


    #C0009
    ChrTalk(
        0x106,
        (
            "#10706F#13P#40W……似乎无法断然\x01",
            "否定这种可能性……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A3")

    OP_57(0x0)
    OP_5A()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00003F#6P#40W……『碧之大树』……\x02\x03",

            "#00001F也就是『零之至宝』\x01",
            "的完全形态……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(10, 1650, 1300, 3000)
    MoveCamera(357, 13, 0, 3000)
    OP_6E(1000, 3000)
    SetCameraDistance(9000, 3000)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(921, 0, 100, 0)
    OP_6F(0x79)
    Sound(934, 0, 100, 0)
    Sound(928, 0, 50, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6EB():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6EB)
    Sleep(50)

    def lambda_6FB():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6FB)
    Sleep(50)

    def lambda_70B():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_70B)
    Sleep(50)

    def lambda_71B():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_71B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sound(829, 0, 100, 0)
    SetCameraDistance(8000, 2000)
    StopSound(1032, 2000, 90)
    StopSound(112, 2000, 20)
    VolumeBGM(0x46, 0x3E8)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(300)
    Sound(824, 0, 50, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis293.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    Sound(824, 0, 50, 0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis294.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(800)
    Sound(824, 0, 50, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis295.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(800)
    Sound(824, 0, 50, 0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis333.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(800)
    Sound(824, 0, 50, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis334.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(800)
    Sound(824, 0, 100, 0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis346.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(800)
    Sound(829, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(1032, 2, 100, 0)
    Sound(112, 2, 30, 0)
    SetCameraDistance(9000, 2000)
    FadeToBright(2000, 16777215)
    VolumeBGM(0x64, 0x3E8)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0011
    ChrTalk(
        0x101,
        "#00007F#6P#4S……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#00310F#12P什、什么！？\x02",
    )

    CloseMessageWindow()

    def lambda_B12():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B12)
    Sleep(50)

    def lambda_B22():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B22)
    Sleep(50)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0013
    ChrTalk(
        0x102,
        (
            "#00108F#12P刚才那是……我们潜入\x01",
            "『太阳堡垒』地下据点时的……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        (
            "#00201F#6P不，艾丝蒂尔他们\x01",
            "并不在一起……\x02\x03",

            "#00208F……而且………\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        "#00013F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xF4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C75")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C46")
    OP_FC(0xFFFA)
    Jump("loc_C49")

    label("loc_C46")

    OP_FC(0xFFF4)

    label("loc_C49")


    #C0016
    ChrTalk(
        0x10A,
        "#00601F#13P怎么……发生什么事了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0E")

    label("loc_C75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C9F")
    OP_FC(0xFFFA)
    Jump("loc_CA2")

    label("loc_C9F")

    OP_FC(0xFFF4)

    label("loc_CA2")


    #C0017
    ChrTalk(
        0x109,
        "#10101F#13P怎、怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0E")

    label("loc_CC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEE")
    OP_FC(0xFFFA)
    Jump("loc_CF1")

    label("loc_CEE")

    OP_FC(0xFFF4)

    label("loc_CF1")


    #C0018
    ChrTalk(
        0x106,
        "#10701F#13P怎么了……？\x02",
    )

    CloseMessageWindow()

    label("loc_D0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D82")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D38")
    OP_FC(0xFFFA)
    Jump("loc_D3B")

    label("loc_D38")

    OP_FC(0xFFF4)

    label("loc_D3B")


    #C0019
    ChrTalk(
        0x105,
        (
            "#10401F#13P……看样子，你们似乎\x01",
            "看到了一些我们看不到的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4F")

    label("loc_D82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DAC")
    OP_FC(0xFFFA)
    Jump("loc_DAF")

    label("loc_DAC")

    OP_FC(0xFFF4)

    label("loc_DAF")


    #C0020
    ChrTalk(
        0x106,
        (
            "#10701F#13P莫非看到了什么\x01",
            "我们看不到的东西……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4F")

    label("loc_DEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E4F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E14")
    OP_FC(0xFFFA)
    Jump("loc_E17")

    label("loc_E14")

    OP_FC(0xFFF4)

    label("loc_E17")


    #C0021
    ChrTalk(
        0x109,
        (
            "#10101F#13P是不是看到了什么\x01",
            "我们看不到的东西……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4F")

    OP_57(0x0)
    OP_5A()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00006F#5P……嗯，只有短短一瞬间而已。\x02\x03",

            "#00008F虽然还有些模糊不清……\x01",
            "但我似乎已经明白\x01",
            "琪雅的真正力量究竟是什么了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1550, 0, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(13000, 0)
    OP_0D()
    OP_68(0, -8750, 0, 3000)
    Sleep(1000)
    StopSound(1032, 2000, 90)
    StopSound(112, 2000, 20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, -8750, 0, 0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9011", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_ED end

    SaveToFile()

Try(main)
