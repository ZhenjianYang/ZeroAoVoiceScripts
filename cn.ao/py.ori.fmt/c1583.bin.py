from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1583.bin",                # FileName
        "c1583",                    # MapName
        "c1583",                    # Location
        0x00AC,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -116000, 0, 0, 1, 172, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1583",                  # 0
        "罗伯兹主任的声音",       # 1
        "艾尼格玛",               # 2
        "SE控制",                 # 3
    ))

    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  8,  0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  8,  0x0000)
    DeclActor(4740,    0,       -114000, 1200,    4740,    1500,    -114000, 0x007C, 0,  3,  0x0000)

    ChipFrameInfo(376, 0)                                        # 0

    ScpFunction((
        "Function_0_178",          # 00, 0
        "Function_1_1CF",          # 01, 1
        "Function_2_49D",          # 02, 2
        "Function_3_4A4",          # 03, 3
        "Function_4_588",          # 04, 4
        "Function_5_12D2",         # 05, 5
        "Function_6_12ED",         # 06, 6
        "Function_7_1312",         # 07, 7
        "Function_8_1391",         # 08, 8
    ))


    def Function_0_178(): pass

    label("Function_0_178")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A2")
    ClearScenarioFlags(0x25, 1)
    Call(0, 2)

    label("loc_1A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BC")
    Event(0, 4)

    label("loc_1BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1CE")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 7)

    label("loc_1CE")

    Return()

    # Function_0_178 end

    def Function_1_1CF(): pass

    label("Function_1_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_237")

    label("loc_1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_225")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_220")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_220")

    Jump("loc_237")

    label("loc_225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_237")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_237")

    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0xB, 0x10)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    ClearMapObjFlags(0xC, 0x2)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x9, 0x10)
    ClearMapObjFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CC")
    OP_70(0x8, 0x3C)
    ClearMapObjFlags(0x8, 0x2)
    Jump("loc_2F8")

    label("loc_2CC")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    OP_70(0x8, 0x3C)
    OP_70(0x9, 0x3C)
    OP_70(0xA, 0x3C)
    ClearMapObjFlags(0x8, 0x2)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 5)), scpexpr(EXPR_END)), "loc_363")
    OP_70(0x3, 0x1E)
    OP_70(0x4, 0x1E)
    OP_70(0x5, 0x1E)
    OP_70(0x6, 0x1E)
    OP_70(0x7, 0x1E)
    ClearMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    ClearMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x7, 0x2)
    OP_70(0xF, 0x48)
    OP_70(0x10, 0x48)
    SetMapObjFrame(0xFF, "maru2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita_add", 0x1, 0x1)
    Jump("loc_386")

    label("loc_363")

    SetMapObjFrame(0xFF, "maru2_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita_add", 0x0, 0x1)

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD")
    SetMapObjFrame(0xFF, "maru_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mae", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato", 0x1, 0x1)
    SetMapObjFrame(0xFF, "uehuta", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sitahuta", 0x1, 0x1)
    Jump("loc_421")

    label("loc_3DD")

    SetMapObjFrame(0xFF, "maru_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato", 0x0, 0x1)
    SetMapObjFrame(0xFF, "uehuta", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sitahuta", 0x0, 0x1)

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_433")
    OP_24(0x39F)
    Jump("loc_49C")

    label("loc_433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_499")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_494")
    Sound(927, 1, 70, 0)

    label("loc_494")

    Jump("loc_49C")

    label("loc_499")

    OP_24(0x39F)

    label("loc_49C")

    Return()

    # Function_1_1CF end

    def Function_2_49D(): pass

    label("Function_2_49D")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_49D end

    def Function_3_4A4(): pass

    label("Function_3_4A4")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_579")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x11, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x11, 0x0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x11)
    OP_71(0x11, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x11, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_579")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_4A4 end

    def Function_4_588(): pass

    label("Function_4_588")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00202.itc", 0x1E)
    LoadChrToIndex("apl/ch50218.itc", 0x1F)
    LoadChrToIndex("apl/ch50092.itc", 0x20)
    SoundLoad(938)
    SoundLoad(943)
    SetChrPos(0x101, 82000, 0, -120100, 90)
    SetChrPos(0x102, 82000, 0, -119000, 90)
    SetChrPos(0x103, 80800, 0, -120100, 90)
    SetChrPos(0x104, 80800, 0, -119000, 90)
    SetChrPos(0xF4, 79600, 0, -120100, 90)
    SetChrPos(0xF5, 79600, 0, -119000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_70(0xF, 0x0)
    OP_70(0x10, 0x0)
    OP_68(88000, 1100, -119500, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)

    def lambda_6A5():
        OP_97(0x101, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A5)
    Sleep(100)

    def lambda_6C2():
        OP_97(0x102, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6C2)
    Sleep(100)

    def lambda_6DF():
        OP_97(0x103, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6DF)
    Sleep(100)

    def lambda_6FC():
        OP_97(0x104, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6FC)
    Sleep(100)

    def lambda_719():
        OP_97(0xF4, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_719)
    Sleep(100)

    def lambda_736():
        OP_97(0xF5, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_736)
    FadeToBright(1000, 0)

    def lambda_759():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_759)
    Sleep(100)

    def lambda_76D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_76D)
    Sleep(700)

    def lambda_781():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_781)
    Sleep(100)

    def lambda_795():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_795)
    Sleep(700)

    def lambda_7A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_7A9)
    Sleep(100)

    def lambda_7BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_7BD)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(100000, 1500, -119500, 2500)
    MoveCamera(55, 19, 0, 2500)
    SetCameraDistance(21000, 2500)
    OP_6F(0x79)

    #C0002
    ChrTalk(
        0x101,
        "#00005F这里莫非是……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#00204F嗯，我想应该就是\x01",
            "主任所说的控制终端。\x02\x03",

            "#00202F赶快把屏蔽导力网络的\x01",
            "物理隔断解除吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        "#00306F呼，终于进入高潮部分了。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00101F嗯，要是能查到\x01",
            "小琪雅和总统等人\x01",
            "所在的位置就好了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 100250, 150, -119500, 90)
    BeginChrThread(0x103, 3, 0, 5)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x12)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 101100, 700, -120300, 0)
    SetChrPos(0x101, 99000, 0, -118800, 90)
    SetChrPos(0x102, 98300, 0, -120900, 90)
    SetChrPos(0x104, 96800, 0, -118400, 90)
    SetChrPos(0xF4, 97500, 0, -119100, 90)
    SetChrPos(0xF5, 97500, 0, -120300, 90)
    SetMapObjFrame(0xFF, "maru2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita_add", 0x1, 0x1)
    OP_68(100200, 1200, -119500, 0)
    MoveCamera(43, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    Sound(938, 2, 100, 0)
    SetCameraDistance(16500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    OP_68(103200, 2200, -119500, 2000)
    MoveCamera(53, 5, 0, 2000)
    SetCameraDistance(18500, 2000)
    OP_6F(0x79)
    BeginChrThread(0xA, 1, 0, 6)
    OP_71(0xF, 0x0, 0x48, 0x0, 0x0)
    OP_71(0x10, 0x0, 0x48, 0x0, 0x0)
    OP_79(0xF)
    OP_79(0x10)
    StopSound(938, 2000, 100)
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x103, 0x3)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -5000, 1500, -120000, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-5000, 3000, -120000, 0)
    MoveCamera(45, 40, -10, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_6B(0x8)
    FadeToBright(1000, 0)
    OP_0D()
    MoveCamera(135, 40, -10, 6500)

    def lambda_B6A():
        OP_9E(0xFE, 0xFFFFEC78, 0xFFFED144, 0x15F90, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B6A)
    Sound(113, 0, 100, 0)
    Sound(143, 0, 60, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(1400)
    Sound(113, 0, 100, 0)
    Sound(143, 0, 60, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(1500)
    Sound(113, 0, 100, 0)
    Sound(143, 0, 60, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(1600)
    Sound(113, 0, 100, 0)
    Sound(143, 0, 60, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(1700)
    Sound(113, 0, 100, 0)
    Sound(143, 0, 60, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    WaitChrThread(0x8, 1)
    OP_6B(0xFF)
    OP_6F(0x79)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(100200, 1200, -119500, 0)
    MoveCamera(43, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x8, 101100, -600, -120300, 0)
    SetCameraDistance(16500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0006
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S导力网络已经\x01",
            "连接到上层区域。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S好，如此一来，我就可以\x01",
            "为你们提供一些后援帮助了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00006F#5P呼……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(100)

    #C0009
    ChrTalk(
        0x103,
        (
            "#00201F#5P直达顶层的导力梯被锁住了，\x01",
            "能否将安全限制解除？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D3E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D3E)
    Sleep(50)

    def lambda_D4E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D4E)

    #C0010
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S这恐怕要花费一点时间，\x01",
            "我尽力而为吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S顺便一说，\x01",
            "总统、琪雅等重要人物\x01",
            "似乎都不在一层至二十层。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S这些楼层内只有兰花塔的职员\x01",
            "和国防军士兵，他们好像相当慌乱。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        "#6P#00108F是吗……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#00301F嗯，先不管那些家伙了，\x01",
            "关键还是三十一层以上的楼层。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00001F#5P可以查到那些楼层内\x01",
            "有什么人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S稍等片刻。\x01",
            "（敲击键盘……）\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S哦，似乎有很多人\x01",
            "聚集在三十六层呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S但还无法查明\x01",
            "具体都是什么人……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F8A")

    #C0019
    ChrTalk(
        0x10A,
        (
            "#6P#00605F三十六层……在通商会议时，\x01",
            "是国宾休息室所在的楼层……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1037")

    label("loc_F8A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FDE")

    #C0020
    ChrTalk(
        0x109,
        (
            "#6P#10105F三十六层……在通商会议时，\x01",
            "是各国首脑使用的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1037")

    label("loc_FDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1037")

    #C0021
    ChrTalk(
        0x105,
        (
            "#6P#10405F三十六层……在通商会议时，\x01",
            "是各国首脑休息室所在的楼层……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1037")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_107D")

    #C0022
    ChrTalk(
        0x106,
        (
            "#6P#10708F……总统和琪雅\x01",
            "或许也在那个楼层？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1102")

    label("loc_107D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10BF")

    #C0023
    ChrTalk(
        0x105,
        (
            "#6P#10408F总统和琪雅\x01",
            "大概也在那个楼层？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1102")

    label("loc_10BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1102")

    #C0024
    ChrTalk(
        0x109,
        (
            "#6P#10108F……莫非总统和琪雅\x01",
            "也在那个楼层！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1102")


    #C0025
    ChrTalk(
        0x101,
        (
            "#00013F#5P嗯……\x01",
            "有这种可能性。\x02",
        )
    )

    CloseMessageWindow()
    Sound(938, 2, 100, 0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 5)
    Sleep(1500)
    EndChrThread(0x103, 0x3)
    StopSound(938, 300, 100)
    Sleep(300)

    #C0026
    ChrTalk(
        0x103,
        (
            "#00203F已经探查过上层区域的封锁情况了。\x02\x03",

            "#00201F如果想由此处前往三十六层，\x01",
            "可以从疏散楼梯直接上去。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11B9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11B9)
    WaitChrThread(0x104, 2)
    Sleep(100)

    #C0027
    ChrTalk(
        0x104,
        "#00307F好，我们出发吧。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#6P#00104F罗伯兹主任，\x01",
            "请您继续\x01",
            "援助我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S嗯，我会在调查上层区域的同时，\x01",
            "尽力解除导力梯的\x01",
            "安全限制。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_37()
    SetChrPos(0x0, 98000, 0, -119500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A6, 5)
    OP_29(0xB1, 0x1, 0xC)
    OP_24(0x3AA)
    OP_24(0x3AF)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_4_588 end

    def Function_5_12D2(): pass

    label("Function_5_12D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12EC")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_5_12D2")

    label("loc_12EC")

    Return()

    # Function_5_12D2 end

    def Function_6_12ED(): pass

    label("Function_6_12ED")

    Sound(943, 2, 100, 0)
    Sleep(1100)
    OP_24(0x3AF)
    Sound(139, 0, 100, 0)
    Sleep(600)
    Sound(151, 0, 80, 0)
    Sleep(600)
    Sound(100, 0, 100, 0)
    Return()

    # Function_6_12ED end

    def Function_7_1312(): pass

    label("Function_7_1312")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(927)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K#30W同日１２：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sound(927, 2, 70, 0)
    Sleep(500)
    Sound(160, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x0, 75000, 0, 3000, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 0)
    EventEnd(0x5)
    Return()

    # Function_7_1312 end

    def Function_8_1391(): pass

    label("Function_8_1391")

    TalkBegin(0xFF)

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这部导力梯正停在\x01",
            "其它楼层，\x01",
            "暂时无法使用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_8_1391 end

    SaveToFile()

Try(main)
