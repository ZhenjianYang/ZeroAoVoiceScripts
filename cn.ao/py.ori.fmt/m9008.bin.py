from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9008.bin",                # FileName
        "m9008",                    # MapName
        "m9008",                    # Location
        0x00C5,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 197, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9008",                  # 0
        "升降机",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(3500,    0,       -32750,  1200,    3500,    1500,    -32750,  0x007C, 0,  2,  0x0000)
    DeclActor(0,       2750,    0,       1200,    0,       4750,    0,       0x007C, 0,  17, 0x0000)

    ChipFrameInfo(568, 0)                                        # 0

    ScpFunction((
        "Function_0_238",          # 00, 0
        "Function_1_2A3",          # 01, 1
        "Function_2_337",          # 02, 2
        "Function_3_41B",          # 03, 3
        "Function_4_69B",          # 04, 4
        "Function_5_7EE",          # 05, 5
        "Function_6_1539",         # 06, 6
        "Function_7_1592",         # 07, 7
        "Function_8_1693",         # 08, 8
        "Function_9_1FC9",         # 09, 9
        "Function_10_22D6",        # 0A, 10
        "Function_11_2377",        # 0B, 11
        "Function_12_239B",        # 0C, 12
        "Function_13_23C2",        # 0D, 13
        "Function_14_23E9",        # 0E, 14
        "Function_15_2410",        # 0F, 15
        "Function_16_2437",        # 10, 16
        "Function_17_245E",        # 11, 17
        "Function_18_25CB",        # 12, 18
        "Function_19_266C",        # 13, 19
    ))


    def Function_0_238(): pass

    label("Function_0_238")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249")
    Event(0, 3)

    label("loc_249")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 19)

    label("loc_271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_282")
    Event(0, 5)

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_293")
    Event(0, 8)

    label("loc_293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2A2")
    ClearScenarioFlags(0x22, 0)
    Event(0, 7)

    label("loc_2A2")

    Return()

    # Function_0_238 end

    def Function_1_2A3(): pass

    label("Function_1_2A3")

    OP_F0(0x1, 0x320)
    OP_1B(0x2, 0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C4")
    OP_1B(0x1, 0x0, 0x9)
    Jump("loc_2C7")

    label("loc_2C4")

    OP_10(0x1, 0x0)

    label("loc_2C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 2)), scpexpr(EXPR_END)), "loc_2DC")
    ClearMapObjFlags(0x2, 0x2)
    SetMapObjFlags(0x2, 0x4)

    label("loc_2DC")

    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_303")
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)

    label("loc_303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_324")
    SetMapObjFrame(0xFF, "magi_07d_add", 0x0, 0x1)

    label("loc_324")

    OP_71(0x1, 0x0, 0x0, 0x0, 0x1000)
    Sound(112, 1, 50, 0)
    Return()

    # Function_1_2A3 end

    def Function_2_337(): pass

    label("Function_2_337")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40C")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x0, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x0, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_40C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_337 end

    def Function_3_41B(): pass

    label("Function_3_41B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(-1120, 2000, -23660, 0)
    MoveCamera(46, 35, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x0, 0, 0, -20000, 180)
    SetChrPos(0x1, 0, 0, -20000, 180)
    SetChrPos(0x2, 0, 0, -20000, 180)
    SetChrPos(0x3, 0, 0, -20000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_52B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_52B)

    def lambda_53C():
        OP_95(0xFE, 100, -250, -25660, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_53C)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_593():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_593)

    def lambda_5A4():
        OP_95(0xFE, -1490, -250, -25500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5A4)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_601():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_601)

    def lambda_612():
        OP_95(0xFE, 1930, -250, -24970, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_612)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_669():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_669)

    def lambda_67A():
        OP_95(0xFE, -3010, -250, -24850, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_67A)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_3_41B end

    def Function_4_69B(): pass

    label("Function_4_69B")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_6F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6F4)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_73F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_73F)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_78A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_78A)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_7D5)
    Sleep(1000)
    NewScene("m9080", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_69B end

    def Function_5_7EE(): pass

    label("Function_5_7EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SoundLoad(4059)
    SoundLoad(4060)
    SoundLoad(4061)
    SoundLoad(4062)
    SoundLoad(4063)
    LoadChrToIndex("apl/ch51768.itc", 0x1E)
    OP_69(0x3, 0x0)
    SetChrPos(0x101, 0, -250, -33000, 0)
    SetChrPos(0x102, 1300, -250, -33600, 0)
    SetChrPos(0x103, -100, -250, -34300, 0)
    SetChrPos(0x104, -1300, -250, -34000, 0)
    SetChrPos(0xF4, -700, -250, -35800, 0)
    SetChrPos(0xF5, 900, -250, -35500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(0, 1750, -30000, 0)
    MoveCamera(0, 41, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    OP_68(0, 1750, -24850, 5000)
    MoveCamera(359, 29, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(20260, 5000)
    FadeToBright(1000, 0)

    def lambda_8F9():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F9)
    Sleep(50)

    def lambda_911():
        OP_9B(0x0, 0xFE, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_911)
    Sleep(50)

    def lambda_929():
        OP_9B(0x0, 0xFE, 0x0, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_929)
    Sleep(50)

    def lambda_941():
        OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_941)
    Sleep(50)

    def lambda_959():
        OP_9B(0x0, 0xFE, 0x0, 0x1EDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_959)
    Sleep(50)

    def lambda_971():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_971)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    #C0002
    ChrTalk(
        0x102,
        "#00105F#12P这里是……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00008F#6P……看来这里就是\x01",
            "『神域』的终点了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 2350, -19650, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(31000, 0)
    MoveCamera(0, 18, 0, 3500)
    SetCameraDistance(38000, 3500)
    OP_6F(0x79)

    #C0004
    ChrTalk(
        0x103,
        "#00201F#12P#N有一扇通往『领域』的门……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0005
    ChrTalk(
        0x104,
        "#00301F#6P#N里面还有『结界』……\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 1250, -25500, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B34")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF0")
    OP_FC(0x6)
    Jump("loc_AF3")

    label("loc_AF0")

    OP_FC(0xC)

    label("loc_AF3")


    #C0006
    ChrTalk(
        0x10A,
        (
            "#00601F#13P……在这种地方出现『领域』，\x01",
            "也就意味着……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0B")

    label("loc_B34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5E")
    OP_FC(0x6)
    Jump("loc_B61")

    label("loc_B5E")

    OP_FC(0xC)

    label("loc_B61")


    #C0007
    ChrTalk(
        0x109,
        (
            "#10101F#13P……在这种地方出现『领域』，\x01",
            "也就意味着……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0B")

    label("loc_BA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCC")
    OP_FC(0x6)
    Jump("loc_BCF")

    label("loc_BCC")

    OP_FC(0xC)

    label("loc_BCF")


    #C0008
    ChrTalk(
        0x106,
        (
            "#10701F#13P……在这种地方出现『领域』，\x01",
            "也就意味着……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0B")


    #C0009
    ChrTalk(
        0x101,
        "#00003F#6P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_68(0, 1250, -20700, 3000)
    MoveCamera(0, 18, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(16500, 3000)
    BeginChrThread(0x101, 0, 0, 6)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)
    Sleep(500)
    Sound(921, 0, 100, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4059V#18A你们来了啊。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
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

    #C0011
    ChrTalk(
        0x101,
        "#00001F#6P#30W……亚里欧斯先生。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC8")
    OP_FC(0xFFFA)
    Jump("loc_DCB")

    label("loc_DC8")

    OP_FC(0xFFF4)

    label("loc_DCB")


    #C0012
    ChrTalk(
        0x109,
        "#10106F#13P……果然……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_E3D")

    label("loc_DEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E3D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E18")
    OP_FC(0xFFFA)
    Jump("loc_E1B")

    label("loc_E18")

    OP_FC(0xFFF4)

    label("loc_E1B")


    #C0013
    ChrTalk(
        0x10A,
        "#00601F#13P……果然是你……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_E3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E92")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E67")
    OP_FC(0xFFFA)
    Jump("loc_E6A")

    label("loc_E67")

    OP_FC(0xFFF4)

    label("loc_E6A")


    #C0014
    ChrTalk(
        0x105,
        "#10403F#13P呼，果然轮到你登场了。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_E92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBC")
    OP_FC(0xFFFA)
    Jump("loc_EBF")

    label("loc_EBC")

    OP_FC(0xFFF4)

    label("loc_EBF")


    #C0015
    ChrTalk(
        0x106,
        "#10701F#13P事先就已预想到了……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_EE5")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4060V#52A呵……没想到你们\x01",
            "竟能击败战鬼。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4061V#48A初次相遇时，你们身上的那股\x01",
            "不成熟的气息，如今似乎已经彻底褪去了。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Fade(500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x2)
    SetMapObjFlags(0x2, 0x4)
    Sleep(500)
    SetChrSubChip(0x101, 0x4)
    Sleep(150)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0x0)
    Sleep(1500)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, 60, -1, -1)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4062V#20A多言无益。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#4063V#31A我在『领域』的尽头等着你们。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_C9(0x1, 0x800)
    OP_68(0, 1250, -24850, 3500)
    MoveCamera(0, 11, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(14500, 3500)
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

    #C0020
    ChrTalk(
        0x104,
        "#00306F#6P#30W……终于要面对他了。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#00106F#12P#30W嗯……他是我们特别任务支援科\x01",
            "最大的竞争对手，也是我们追赶的目标……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#00202F#6P#30W……回想起来，那还是在我们\x01",
            "刚刚相识时结下的缘分呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00004F#5P#30W嗯……我们进入地下空间，\x01",
            "救助隆和亨利的时候遭遇险境，\x01",
            "在千钧一发之际得他相救……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1292")
    OP_FC(0x6)
    Jump("loc_1295")

    label("loc_1292")

    OP_FC(0xC)

    label("loc_1295")


    #C0024
    ChrTalk(
        0x10A,
        "#00602F#13P……原来如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1358")

    label("loc_12B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_130A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12E3")
    OP_FC(0x6)
    Jump("loc_12E6")

    label("loc_12E3")

    OP_FC(0xC)

    label("loc_12E6")


    #C0025
    ChrTalk(
        0x109,
        "#10100F#13P原来是这样……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1358")

    label("loc_130A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1358")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1334")
    OP_FC(0x6)
    Jump("loc_1337")

    label("loc_1334")

    OP_FC(0xC)

    label("loc_1337")


    #C0026
    ChrTalk(
        0x106,
        "#10710F#13P原来是这样啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1358")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1382")
    OP_FC(0x6)
    Jump("loc_1385")

    label("loc_1382")

    OP_FC(0xC)

    label("loc_1385")


    #C0027
    ChrTalk(
        0x105,
        (
            "#10404F#13P呵呵……\x01",
            "真是命中注定的因缘呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_146D")

    label("loc_13BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1415")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13E4")
    OP_FC(0x6)
    Jump("loc_13E7")

    label("loc_13E4")

    OP_FC(0xC)

    label("loc_13E7")


    #C0028
    ChrTalk(
        0x106,
        "#10704F#13P真是命中注定的因缘呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_146D")

    label("loc_1415")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_146D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_143F")
    OP_FC(0x6)
    Jump("loc_1442")

    label("loc_143F")

    OP_FC(0xC)

    label("loc_1442")


    #C0029
    ChrTalk(
        0x109,
        "#10106F#13P简直是命中注定的因缘呢……\x02",
    )

    CloseMessageWindow()

    label("loc_146D")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0030
    ChrTalk(
        0x101,
        (
            "#00013F#5P动身吧，\x01",
            "亚里欧斯先生正在等着我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#00107F#12P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#00301F#6P明白。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, -250, -26000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetScenarioFlags(0x1A9, 2)
    OP_29(0xB2, 0x1, 0x7)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_5_7EE end

    def Function_6_1539(): pass

    label("Function_6_1539")

    OP_95(0xFE, 0, 0, -22300, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0xA)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_6_1539 end

    def Function_7_1592(): pass

    label("Function_7_1592")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x2, "event/ev17018.eff")
    OP_69(0x3, 0x0)
    OP_68(0, 4200, -17250, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 4100, -1300, 5000)
    MoveCamera(0, 16, 0, 5000)
    SetCameraDistance(27720, 5000)
    OP_0D()
    Sleep(3200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 5300, -5500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 50, 0)
    Sound(223, 0, 100, 0)
    Sleep(300)
    SetMapObjFrame(0xFF, "magi_07d_add", 0x0, 0x1)
    Sleep(1500)
    StopSound(112, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9082", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1592 end

    def Function_8_1693(): pass

    label("Function_8_1693")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(0, 1750, -22750, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17800, 0)
    SetChrPos(0x101, 0, 0, -20000, 180)
    SetChrPos(0x102, 0, 0, -20000, 180)
    SetChrPos(0x103, 0, 0, -20000, 180)
    SetChrPos(0x104, 0, 0, -20000, 180)
    SetChrPos(0xF4, 0, 0, -20000, 180)
    SetChrPos(0xF5, 0, 0, -20000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFrame(0xFF, "magi_07d_add", 0x0, 0x1)
    SetCameraDistance(18800, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_180C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_180C)

    def lambda_181D():
        OP_9B(0x0, 0xFE, 0x0, 0x16A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_181D)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_186F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_186F)

    def lambda_1880():
        OP_9B(0x0, 0xFE, 0x15A, 0x1450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1880)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_18D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_18D8)

    def lambda_18E9():
        OP_9B(0x0, 0xFE, 0xE, 0x13EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18E9)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_193B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_193B)

    def lambda_194C():
        OP_9B(0x0, 0xFE, 0x14D, 0x1194, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_194C)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_19A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_19A4)

    def lambda_19B5():
        OP_9B(0x0, 0xFE, 0x1B, 0x1130, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_19B5)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1A07():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A07)

    def lambda_1A18():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A18)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 2550, -18840, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(35510, 0)
    OP_68(0, 2550, -9250, 2500)
    OP_0D()

    def lambda_1AE5():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1AE5)
    Sleep(50)

    def lambda_1AF5():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1AF5)
    Sleep(50)

    def lambda_1B05():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B05)
    Sleep(50)

    def lambda_1B15():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B15)
    Sleep(50)

    def lambda_1B25():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1B25)
    Sleep(50)

    def lambda_1B35():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1B35)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_6F(0x79)

    #C0033
    ChrTalk(
        0x103,
        (
            "#00201F#11P那是……\x01",
            "升降机啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#00101F#5P也就是说……\x01",
            "小琪雅就在上面？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#00306F#5P嗯……应该没错。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00008F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1150, -24500, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14280, 0)
    Fade(500)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_1C3A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C3A)
    Sleep(50)

    def lambda_1C4A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C4A)
    Sleep(50)

    def lambda_1C5A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C5A)
    Sleep(50)

    def lambda_1C6A():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1C6A)
    Sleep(50)

    def lambda_1C7A():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1C7A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0037
    ChrTalk(
        0x101,
        (
            "#00001F#5P我们虽然战胜了亚里欧斯先生……\x01",
            "但接下来还要面对\x01",
            "深不可测的玛丽亚贝尔小姐。\x02\x03",

            "#00003F还是先回梅尔卡瓦一趟，\x01",
            "做好最后的准备工作吧。\x02\x03",

            "#00013F无论如何，\x01",
            "我们一定要夺回琪雅！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D7D")
    OP_FC(0xC)
    Jump("loc_1D80")

    label("loc_1D7D")

    OP_FC(0x6)

    label("loc_1D80")


    #C0038
    ChrTalk(
        0x109,
        "#10101F#13P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E31")

    label("loc_1D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DE9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DC8")
    OP_FC(0xC)
    Jump("loc_1DCB")

    label("loc_1DC8")

    OP_FC(0x6)

    label("loc_1DCB")


    #C0039
    ChrTalk(
        0x105,
        "#10401F#13P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E31")

    label("loc_1DE9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E13")
    OP_FC(0xC)
    Jump("loc_1E16")

    label("loc_1E13")

    OP_FC(0x6)

    label("loc_1E16")


    #C0040
    ChrTalk(
        0x106,
        "#10701F#13P是的……！\x02",
    )

    CloseMessageWindow()

    label("loc_1E31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EA1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E5B")
    OP_FC(0xC)
    Jump("loc_1E5E")

    label("loc_1E5B")

    OP_FC(0x6)

    label("loc_1E5E")


    #C0041
    ChrTalk(
        0x10A,
        (
            "#00603F#13P……如果还想前往各地，\x01",
            "这恐怕是最后的机会了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7C")

    label("loc_1EA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F11")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ECB")
    OP_FC(0xC)
    Jump("loc_1ECE")

    label("loc_1ECB")

    OP_FC(0x6)

    label("loc_1ECE")


    #C0042
    ChrTalk(
        0x106,
        (
            "#10703F#13P……如果还想前往各地，\x01",
            "这应该是最后的机会了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7C")

    label("loc_1F11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F7C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F3B")
    OP_FC(0xC)
    Jump("loc_1F3E")

    label("loc_1F3B")

    OP_FC(0x6)

    label("loc_1F3E")


    #C0043
    ChrTalk(
        0x105,
        (
            "#10403F#13P……如果还想前往各地，\x01",
            "这也许是最后的机会了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, -250, -26000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A9, 5)
    OP_29(0xB2, 0x1, 0x9)
    OP_1B(0x1, 0x0, 0x9)
    OP_10(0x1, 0x1)
    OP_E2(0x2)
    Sleep(300)
    EventEnd(0x5)
    Return()

    # Function_8_1693 end

    def Function_9_1FC9(): pass

    label("Function_9_1FC9")

    EventBegin(0x0)
    SoundLoad(832)
    SetChrPos(0x101, -50, 2750, -5770, 0)
    SetChrPos(0x102, 930, 2750, -6110, 0)
    SetChrPos(0x103, -1060, 2750, -6040, 0)
    SetChrPos(0x104, -130, 2750, -7330, 0)
    SetChrPos(0xF4, -1260, 2750, -7350, 0)
    SetChrPos(0xF5, 1080, 2750, -7380, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_78(0x1, 0x8)
    SetChrPos(0x8, 0, 2750, 0, 0)
    SetChrFlags(0x8, 0x4)
    OP_68(0, 4150, -4500, 0)
    MoveCamera(0, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16500, 0)
    Fade(500)
    OP_0D()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00003F#5P（琪雅……还有全部的真相，\x01",
            "  都在前方等待着我们。）\x02\x03",

            "#00013F（为了彻底解决这次事件……\x01",
            "  做好充分的觉悟吧！）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "乘坐升降机\x01",      # 0
            "离开此处\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2161"),
        (1, "loc_22A9"),
        (SWITCH_DEFAULT, "loc_22D5"),
    )


    label("loc_2161")

    OP_68(100, 2750, 0, 4500)
    MoveCamera(0, 40, 0, 4500)
    OP_6E(700, 4500)
    SetCameraDistance(29006, 4500)
    BeginChrThread(0x101, 0, 0, 11)
    Sleep(200)
    BeginChrThread(0x102, 0, 0, 12)
    Sleep(100)
    BeginChrThread(0x103, 0, 0, 13)
    Sleep(100)
    BeginChrThread(0x104, 0, 0, 14)
    Sleep(100)
    BeginChrThread(0xF4, 0, 0, 15)
    Sleep(100)
    BeginChrThread(0xF5, 0, 0, 16)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    Sound(832, 2, 100, 0)
    Sound(935, 0, 70, 0)
    OP_68(100, 20150, -4500, 8000)
    MoveCamera(0, 24, 0, 8000)
    SetCameraDistance(16500, 8000)
    BeginChrThread(0x8, 0, 0, 10)
    Sleep(1500)

    def lambda_221C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_221C)
    Sleep(50)

    def lambda_222C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_222C)
    Sleep(50)

    def lambda_223C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_223C)
    Sleep(50)

    def lambda_224C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_224C)
    Sleep(50)

    def lambda_225C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_225C)
    Sleep(50)

    def lambda_226C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_226C)
    Sleep(1250)
    Sleep(2000)
    StopSound(832, 500, 100)
    StopSound(112, 500, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9010", 0, 0, 0)
    IdleLoop()
    Jump("loc_22D5")

    label("loc_22A9")

    SetChrPos(0x0, 0, 2750, -6890, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_22D5")

    label("loc_22D5")

    Return()

    # Function_9_1FC9 end

    def Function_10_22D6(): pass

    label("Function_10_22D6")

    OP_98(0xFE, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)
    OP_98(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
    OP_98(0xFE, 0x0, 0x1388, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xBB8, 0x0, 0xFA0, 0x0)
    OP_98(0xFE, 0x0, 0x7D0, 0x0, 0x1388, 0x0)
    OP_98(0xFE, 0x0, 0x3E8, 0x0, 0x1770, 0x0)
    OP_98(0xFE, 0x0, 0x3E8, 0x0, 0x1B58, 0x0)
    OP_98(0xFE, 0x0, 0x2710, 0x0, 0x1F40, 0x0)
    Return()

    # Function_10_22D6 end

    def Function_11_2377(): pass

    label("Function_11_2377")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_95(0xFE, -820, 2750, 1300, 2000, 0x0)
    Return()

    # Function_11_2377 end

    def Function_12_239B(): pass

    label("Function_12_239B")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_95(0xFE, 820, 3050, 1300, 2000, 0x0)
    Return()

    # Function_12_239B end

    def Function_13_23C2(): pass

    label("Function_13_23C2")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_95(0xFE, -1480, 3050, -80, 1000, 0x0)
    Return()

    # Function_13_23C2 end

    def Function_14_23E9(): pass

    label("Function_14_23E9")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x1, 0x157C, 0x7D0, 0x1)
    OP_95(0xFE, 1480, 3050, -80, 1000, 0x0)
    Return()

    # Function_14_23E9 end

    def Function_15_2410(): pass

    label("Function_15_2410")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, -810, 3050, -1400, 1000, 0x0)
    Return()

    # Function_15_2410 end

    def Function_16_2437(): pass

    label("Function_16_2437")

    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 810, 3050, -1400, 1000, 0x0)
    Return()

    # Function_16_2437 end

    def Function_17_245E(): pass

    label("Function_17_245E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一台升降机。\x01",
            "要乘坐吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C3")
    Fade(500)
    SetChrPos(0x0, 0, 3050, -1500, 180)
    SetChrPos(0x1, -2000, 3050, 0, 270)
    SetChrPos(0x2, 2000, 3050, 0, 90)
    SetChrPos(0x3, 0, 3050, 1500, 0)
    OP_68(100, 2750, 0, 0)
    MoveCamera(0, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29006, 0)
    OP_78(0x1, 0x8)
    SetChrPos(0x8, 0, 2750, 0, 0)
    SetChrFlags(0x8, 0x4)
    OP_0D()
    Sleep(500)
    Sound(832, 2, 100, 0)
    Sound(935, 0, 70, 0)
    OP_68(100, 20150, -4500, 8000)
    MoveCamera(0, 24, 0, 8000)
    SetCameraDistance(16500, 8000)
    BeginChrThread(0x8, 0, 0, 10)
    Sleep(1500)
    Sleep(50)
    Sleep(50)
    Sleep(50)
    Sleep(50)
    Sleep(50)
    Sleep(1250)
    Sleep(2000)
    StopSound(832, 500, 100)
    StopSound(112, 500, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x0)
    Sleep(50)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m9011", 0, 0, 0)
    IdleLoop()

    label("loc_25C3")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_245E end

    def Function_18_25CB(): pass

    label("Function_18_25CB")

    OP_98(0xFE, 0x0, 0xFFFFEC78, 0x0, 0x1388, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x1194, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xFA0, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF830, 0x0, 0xDAC, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFEC78, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x7D0, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x3E8, 0x0)
    Return()

    # Function_18_25CB end

    def Function_19_266C(): pass

    label("Function_19_266C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    OP_68(0, 20150, -4500, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16500, 0)
    OP_78(0x1, 0x8)
    SetChrPos(0x8, 0, 23750, 0, 0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x0, 0, 24050, -1500, 180)
    SetChrPos(0x1, -2000, 24050, 0, 270)
    SetChrPos(0x2, 2000, 24050, 0, 90)
    SetChrPos(0x3, 0, 24050, 1500, 0)
    Sound(832, 2, 100, 0)
    MoveCamera(0, 35, 0, 3000)
    OP_68(100, 2000, 0, 8000)
    MoveCamera(0, 48, 0, 8000)
    SetCameraDistance(37710, 8000)
    BeginChrThread(0x8, 0, 0, 18)
    FadeToBright(500, 0)
    Sleep(2000)
    Sleep(1500)
    Sleep(1250)
    Sleep(2000)
    OP_24(0x340)
    Sound(149, 0, 60, 0)
    Sleep(1400)
    Sleep(500)
    OP_79(0xF)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_19_266C end

    SaveToFile()

Try(main)
