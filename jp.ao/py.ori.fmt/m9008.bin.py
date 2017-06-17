from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "昇降機",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(3500,    0,       -32750,  1200,    3500,    1500,    -32750,  0x007C, 0,  2,  0x0000)
    DeclActor(0,       2750,    0,       1200,    0,       4750,    0,       0x007C, 0,  17, 0x0000)

    ChipFrameInfo(568, 0)                                        # 0

    ScpFunction((
        "Function_0_238",          # 00, 0
        "Function_1_2A3",          # 01, 1
        "Function_2_337",          # 02, 2
        "Function_3_433",          # 03, 3
        "Function_4_6B3",          # 04, 4
        "Function_5_806",          # 05, 5
        "Function_6_158C",         # 06, 6
        "Function_7_15E5",         # 07, 7
        "Function_8_16E6",         # 08, 8
        "Function_9_2066",         # 09, 9
        "Function_10_2389",        # 0A, 10
        "Function_11_242A",        # 0B, 11
        "Function_12_244E",        # 0C, 12
        "Function_13_2475",        # 0D, 13
        "Function_14_249C",        # 0E, 14
        "Function_15_24C3",        # 0F, 15
        "Function_16_24EA",        # 10, 16
        "Function_17_2511",        # 11, 17
        "Function_18_268A",        # 12, 18
        "Function_19_272B",        # 13, 19
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
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
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

    label("loc_424")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_337 end

    def Function_3_433(): pass

    label("Function_3_433")

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

    def lambda_543():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_543)

    def lambda_554():
        OP_95(0xFE, 100, -250, -25660, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_554)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_5AB)

    def lambda_5BC():
        OP_95(0xFE, -1490, -250, -25500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5BC)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_619():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_619)

    def lambda_62A():
        OP_95(0xFE, 1930, -250, -24970, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_62A)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_681():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_681)

    def lambda_692():
        OP_95(0xFE, -3010, -250, -24850, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_692)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_3_433 end

    def Function_4_6B3(): pass

    label("Function_4_6B3")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_70C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_70C)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_757():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_757)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_7A2)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_7ED)
    Sleep(1000)
    NewScene("m9080", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_6B3 end

    def Function_5_806(): pass

    label("Function_5_806")

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

    def lambda_911():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_911)
    Sleep(50)

    def lambda_929():
        OP_9B(0x0, 0xFE, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_929)
    Sleep(50)

    def lambda_941():
        OP_9B(0x0, 0xFE, 0x0, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_941)
    Sleep(50)

    def lambda_959():
        OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_959)
    Sleep(50)

    def lambda_971():
        OP_9B(0x0, 0xFE, 0x0, 0x1EDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_971)
    Sleep(50)

    def lambda_989():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_989)
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
        "#00105F#12Pここは……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00008F#6P……どうやらここが\x01",
            "《神域》の終点みたいだな……\x02",
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
        "#00201F#12P#N《領域》への門がありますね……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0005
    ChrTalk(
        0x104,
        "#00301F#6P#N奥には《結界》か……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B16")
    OP_FC(0x6)
    Jump("loc_B19")

    label("loc_B16")

    OP_FC(0xC)

    label("loc_B19")


    #C0006
    ChrTalk(
        0x10A,
        (
            "#00601F#13P……こんな場所に\x01",
            "《領域》があるという事は……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_B5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B86")
    OP_FC(0x6)
    Jump("loc_B89")

    label("loc_B86")

    OP_FC(0xC)

    label("loc_B89")


    #C0007
    ChrTalk(
        0x109,
        (
            "#10101F#13P……こんな場所に\x01",
            "《領域》があるって事は……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C35")

    label("loc_BCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C35")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF4")
    OP_FC(0x6)
    Jump("loc_BF7")

    label("loc_BF4")

    OP_FC(0xC)

    label("loc_BF7")


    #C0008
    ChrTalk(
        0x106,
        (
            "#10701F#13P……こんな場所に\x01",
            "《領域》があるという事は……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C35")


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
            "#40W#4059V#18A──来たか。\x07\x00\x02",
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
        "#00001F#6P#30W……アリオス、さん。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E1E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF4")
    OP_FC(0xFFFA)
    Jump("loc_DF7")

    label("loc_DF4")

    OP_FC(0xFFF4)

    label("loc_DF7")


    #C0012
    ChrTalk(
        0x109,
        "#10106F#13P……やっぱり……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_E6D")

    label("loc_E1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E48")
    OP_FC(0xFFFA)
    Jump("loc_E4B")

    label("loc_E48")

    OP_FC(0xFFF4)

    label("loc_E4B")


    #C0013
    ChrTalk(
        0x10A,
        "#00601F#13P……やはりか……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_E6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E97")
    OP_FC(0xFFFA)
    Jump("loc_E9A")

    label("loc_E97")

    OP_FC(0xFFF4)

    label("loc_E9A")


    #C0014
    ChrTalk(
        0x105,
        "#10403F#13Pま、当然そうだよね。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_EC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F17")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EEA")
    OP_FC(0xFFFA)
    Jump("loc_EED")

    label("loc_EEA")

    OP_FC(0xFFF4)

    label("loc_EED")


    #C0015
    ChrTalk(
        0x106,
        "#10701F#13P予想はしていましたが……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_F17")

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
            "#40W#4060V#52Aフ……\x01",
            "まさかあの戦鬼を破るとはな。\x02",
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
            "#40W#4061V#48Aもはや初めて会った時の\x01",
            "覚束#4Rおぼつか#なさは無さそうだ。\x07\x00\x02",
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
            "#40W#4062V#20A──言葉は無用。\x02",
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
            "#40W#4063V#31A我が《領域》の果てで待つ。\x07\x00\x02",
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
        "#00306F#6P#30W……遂に来ちまったか。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#00106F#12P#30Wええ……私たち特務支援課の\x01",
            "最大の競争相手#8Rラ イ バ ル#にして目標……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#00202F#6P#30W……思えばわたしたちが\x01",
            "知り合った時からの縁ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00004F#5P#30Wああ……ジオフロントに潜って\x01",
            "リュウたちを助ける時に\x01",
            "危ない所を助けてもらって……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12C9")
    OP_FC(0x6)
    Jump("loc_12CC")

    label("loc_12C9")

    OP_FC(0xC)

    label("loc_12CC")


    #C0024
    ChrTalk(
        0x10A,
        "#00602F#13P……なるほどな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_139F")

    label("loc_12F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_134B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_131C")
    OP_FC(0x6)
    Jump("loc_131F")

    label("loc_131C")

    OP_FC(0xC)

    label("loc_131F")


    #C0025
    ChrTalk(
        0x109,
        "#10100F#13Pそうだったんですか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_139F")

    label("loc_134B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_139F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1375")
    OP_FC(0x6)
    Jump("loc_1378")

    label("loc_1375")

    OP_FC(0xC)

    label("loc_1378")


    #C0026
    ChrTalk(
        0x106,
        "#10710F#13Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    label("loc_139F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1401")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13C9")
    OP_FC(0x6)
    Jump("loc_13CC")

    label("loc_13C9")

    OP_FC(0xC)

    label("loc_13CC")


    #C0027
    ChrTalk(
        0x105,
        (
            "#10404F#13Pフフ……\x01",
            "まさに因縁の関係だね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B2")

    label("loc_1401")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_145A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_142B")
    OP_FC(0x6)
    Jump("loc_142E")

    label("loc_142B")

    OP_FC(0xC)

    label("loc_142E")


    #C0028
    ChrTalk(
        0x106,
        "#10704F#13P因縁の関係、ですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B2")

    label("loc_145A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1484")
    OP_FC(0x6)
    Jump("loc_1487")

    label("loc_1484")

    OP_FC(0xC)

    label("loc_1487")


    #C0029
    ChrTalk(
        0x109,
        "#10106F#13Pまさに因縁の関係ですね……\x02",
    )

    CloseMessageWindow()

    label("loc_14B2")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0030
    ChrTalk(
        0x101,
        (
            "#00013F#5P──行こう。\x01",
            "アリオスさんが待っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#00107F#12Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#00301F#6P合点承知だぜ。\x02",
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

    # Function_5_806 end

    def Function_6_158C(): pass

    label("Function_6_158C")

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

    # Function_6_158C end

    def Function_7_15E5(): pass

    label("Function_7_15E5")

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

    # Function_7_15E5 end

    def Function_8_16E6(): pass

    label("Function_8_16E6")

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

    def lambda_185F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_185F)

    def lambda_1870():
        OP_9B(0x0, 0xFE, 0x0, 0x16A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1870)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_18C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_18C2)

    def lambda_18D3():
        OP_9B(0x0, 0xFE, 0x15A, 0x1450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18D3)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_192B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_192B)

    def lambda_193C():
        OP_9B(0x0, 0xFE, 0xE, 0x13EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_193C)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_198E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_198E)

    def lambda_199F():
        OP_9B(0x0, 0xFE, 0x14D, 0x1194, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_199F)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_19F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_19F7)

    def lambda_1A08():
        OP_9B(0x0, 0xFE, 0x1B, 0x1130, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1A08)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1A5A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A5A)

    def lambda_1A6B():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A6B)
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

    def lambda_1B38():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B38)
    Sleep(50)

    def lambda_1B48():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B48)
    Sleep(50)

    def lambda_1B58():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B58)
    Sleep(50)

    def lambda_1B68():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B68)
    Sleep(50)

    def lambda_1B78():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1B78)
    Sleep(50)

    def lambda_1B88():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1B88)
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
            "#00201F#11Pあれは……\x01",
            "昇降器のようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#00101F#5Pそれじゃあ……\x01",
            "あれの上にキーアちゃんが？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#00306F#5Pああ……間違いねぇだろう。\x02",
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

    def lambda_1CAF():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CAF)
    Sleep(50)

    def lambda_1CBF():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1CBF)
    Sleep(50)

    def lambda_1CCF():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1CCF)
    Sleep(50)

    def lambda_1CDF():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1CDF)
    Sleep(50)

    def lambda_1CEF():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1CEF)
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
            "#00001F#5Pアリオスさんは越えたが……\x01",
            "あの得体の知れない\x01",
            "マリアベルさんが残っている。\x02\x03",

            "#00003Fできれば一度、メルカバに戻って\x01",
            "最後の準備を整えておこう。\x02\x03",

            "#00013F絶対に──何としても\x01",
            "キーアを取り戻すためにも！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E0E")
    OP_FC(0xC)
    Jump("loc_1E11")

    label("loc_1E0E")

    OP_FC(0x6)

    label("loc_1E11")


    #C0038
    ChrTalk(
        0x109,
        "#10101F#13Pええ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EC6")

    label("loc_1E31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E7E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E5B")
    OP_FC(0xC)
    Jump("loc_1E5E")

    label("loc_1E5B")

    OP_FC(0x6)

    label("loc_1E5E")


    #C0039
    ChrTalk(
        0x105,
        "#10401F#13Pああ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EC6")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EC6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EA8")
    OP_FC(0xC)
    Jump("loc_1EAB")

    label("loc_1EA8")

    OP_FC(0x6)

    label("loc_1EAB")


    #C0040
    ChrTalk(
        0x106,
        "#10701F#13Pはい……！\x02",
    )

    CloseMessageWindow()

    label("loc_1EC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F38")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EF0")
    OP_FC(0xC)
    Jump("loc_1EF3")

    label("loc_1EF0")

    OP_FC(0x6)

    label("loc_1EF3")


    #C0041
    ChrTalk(
        0x10A,
        (
            "#00603F#13P……各地を回れるのも\x01",
            "これが最後になりそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2019")

    label("loc_1F38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FAC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F62")
    OP_FC(0xC)
    Jump("loc_1F65")

    label("loc_1F62")

    OP_FC(0x6)

    label("loc_1F65")


    #C0042
    ChrTalk(
        0x106,
        (
            "#10703F#13P……各地を回れるのも\x01",
            "これが最後になりそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2019")

    label("loc_1FAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2019")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FD6")
    OP_FC(0xC)
    Jump("loc_1FD9")

    label("loc_1FD6")

    OP_FC(0x6)

    label("loc_1FD9")


    #C0043
    ChrTalk(
        0x105,
        (
            "#10403F#13P……各地を回れるのも\x01",
            "これが最後になりそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2019")

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

    # Function_8_16E6 end

    def Function_9_2066(): pass

    label("Function_9_2066")

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
            "#00003F#5P（この先にキーアが……\x01",
            "  そして全ての真実が待っている。）\x02\x03",

            "#00013F（覚悟を決めよう……\x01",
            "  事件を完全に解決するために！）\x02",
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
            "昇降器を利用する\x01",      # 0
            "その場を離れる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2214"),
        (1, "loc_235C"),
        (SWITCH_DEFAULT, "loc_2388"),
    )


    label("loc_2214")

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

    def lambda_22CF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22CF)
    Sleep(50)

    def lambda_22DF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_22DF)
    Sleep(50)

    def lambda_22EF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_22EF)
    Sleep(50)

    def lambda_22FF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_22FF)
    Sleep(50)

    def lambda_230F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_230F)
    Sleep(50)

    def lambda_231F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_231F)
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
    Jump("loc_2388")

    label("loc_235C")

    SetChrPos(0x0, 0, 2750, -6890, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_2388")

    label("loc_2388")

    Return()

    # Function_9_2066 end

    def Function_10_2389(): pass

    label("Function_10_2389")

    OP_98(0xFE, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)
    OP_98(0xFE, 0x0, 0xBB8, 0x0, 0x7D0, 0x0)
    OP_98(0xFE, 0x0, 0x1388, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xBB8, 0x0, 0xFA0, 0x0)
    OP_98(0xFE, 0x0, 0x7D0, 0x0, 0x1388, 0x0)
    OP_98(0xFE, 0x0, 0x3E8, 0x0, 0x1770, 0x0)
    OP_98(0xFE, 0x0, 0x3E8, 0x0, 0x1B58, 0x0)
    OP_98(0xFE, 0x0, 0x2710, 0x0, 0x1F40, 0x0)
    Return()

    # Function_10_2389 end

    def Function_11_242A(): pass

    label("Function_11_242A")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_95(0xFE, -820, 2750, 1300, 2000, 0x0)
    Return()

    # Function_11_242A end

    def Function_12_244E(): pass

    label("Function_12_244E")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_95(0xFE, 820, 3050, 1300, 2000, 0x0)
    Return()

    # Function_12_244E end

    def Function_13_2475(): pass

    label("Function_13_2475")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x1)
    OP_95(0xFE, -1480, 3050, -80, 1000, 0x0)
    Return()

    # Function_13_2475 end

    def Function_14_249C(): pass

    label("Function_14_249C")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x1, 0x157C, 0x7D0, 0x1)
    OP_95(0xFE, 1480, 3050, -80, 1000, 0x0)
    Return()

    # Function_14_249C end

    def Function_15_24C3(): pass

    label("Function_15_24C3")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, -810, 3050, -1400, 1000, 0x0)
    Return()

    # Function_15_24C3 end

    def Function_16_24EA(): pass

    label("Function_16_24EA")

    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 810, 3050, -1400, 1000, 0x0)
    Return()

    # Function_16_24EA end

    def Function_17_2511(): pass

    label("Function_17_2511")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "昇降器がある。\x01",
            "移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2682")
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

    label("loc_2682")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_2511 end

    def Function_18_268A(): pass

    label("Function_18_268A")

    OP_98(0xFE, 0x0, 0xFFFFEC78, 0x0, 0x1388, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x1194, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xFA0, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF830, 0x0, 0xDAC, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFEC78, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x7D0, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x3E8, 0x0)
    Return()

    # Function_18_268A end

    def Function_19_272B(): pass

    label("Function_19_272B")

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

    # Function_19_272B end

    SaveToFile()

Try(main)
