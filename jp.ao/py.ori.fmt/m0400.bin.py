from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0400.bin",                # FileName
        "m0400",                    # MapName
        "m0400",                    # Location
        0x00A9,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -5000, 0, 0, 1, 169, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0400",                  # 0
        "アリオス",               # 1
        "ダドリー捜査官",         # 2
        "SE制御",                 # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 22,  171.0,                 4.0,                   0.0,                   20.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -57.0,                 -1.3333333730697632,   -0.0,                  1.0])

    DeclActor(-50,     0,       33570,   1000,    -50,     1500,    33570,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(460, 0)                                        # 0

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_390",          # 02, 2
        "Function_3_397",          # 03, 3
        "Function_4_7D8",          # 04, 4
        "Function_5_837",          # 05, 5
        "Function_6_896",          # 06, 6
        "Function_7_8F6",          # 07, 7
        "Function_8_956",          # 08, 8
        "Function_9_9B6",          # 09, 9
        "Function_10_A16",         # 0A, 10
        "Function_11_A76",         # 0B, 11
        "Function_12_AF1",         # 0C, 12
        "Function_13_F4E",         # 0D, 13
        "Function_14_F8B",         # 0E, 14
        "Function_15_FD9",         # 0F, 15
        "Function_16_1027",        # 10, 16
        "Function_17_107C",        # 11, 17
        "Function_18_10D1",        # 12, 18
        "Function_19_111F",        # 13, 19
        "Function_20_1188",        # 14, 20
        "Function_21_11D0",        # 15, 21
        "Function_22_135D",        # 16, 22
        "Function_23_1394",        # 17, 23
    ))


    def Function_0_1CC(): pass

    label("Function_0_1CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4")
    ClearScenarioFlags(0x25, 1)
    Call(0, 2)

    label("loc_1E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1FB")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 3)
    Jump("loc_20D")

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_20D")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 21)

    label("loc_20D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_227")
    Event(0, 12)

    label("loc_227")

    Return()

    # Function_0_1CC end

    def Function_1_228(): pass

    label("Function_1_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B2")
    SetMapObjFrame(0xFF, "rai00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "05_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "under_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ugoku01", 0x0, 0x1)
    Jump("loc_329")

    label("loc_2B2")

    SetMapObjFrame(0xFF, "rai00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "under_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ugoku01", 0x1, 0x1)

    label("loc_329")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34D")
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x0, 0x10)

    label("loc_34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_361")
    OP_24(0x94)
    ClearScenarioFlags(0x0, 0)
    Jump("loc_38F")

    label("loc_361")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_389")
    OP_24(0x94)
    Jump("loc_38F")

    label("loc_389")

    Sound(148, 1, 100, 0)

    label("loc_38F")

    Return()

    # Function_1_228 end

    def Function_2_390(): pass

    label("Function_2_390")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_390 end

    def Function_3_397(): pass

    label("Function_3_397")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch02401.itc", 0x1F)
    LoadChrToIndex("chr/ch00900.itc", 0x20)
    LoadChrToIndex("chr/ch00901.itc", 0x21)
    SoundLoad(4052)
    SoundLoad(3458)
    OP_68(171500, 2700, -100, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 171500, 0, 5500, 180)
    SetChrPos(0x102, 171500, 0, 5500, 180)
    SetChrPos(0x103, 171500, 0, 5500, 180)
    SetChrPos(0x104, 171500, 0, 5500, 180)
    SetChrPos(0x109, 171500, 0, 5500, 180)
    SetChrPos(0x105, 171500, 0, 5500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 171500, 0, 5500, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 171500, 0, 5500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(160, 0, 100, 0)
    Sleep(300)
    OP_68(171500, 1200, -100, 3000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x8, 3, 0, 4)
    Sleep(500)
    BeginChrThread(0x9, 3, 0, 5)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 7)
    Sleep(700)
    WaitChrThread(0x8, 3)
    OP_C9(0x0, 0x80000000)

    #C0001
    ChrTalk(
        0x8,
        (
            "#12P#01401F#4052V#30W#18A──時間が惜しい。\x01",
            "先行するぞ。\x02",
        )
    )
    #Auto

    BeginChrThread(0x103, 3, 0, 8)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 9)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 10)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 11)
    CloseMessageWindow()
    Sleep(300)

    #C0002
    ChrTalk(
        0x9,
        "#00607F#3458V#30W#15A#11P遅れずに付いてくるがいい！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_61C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_61C)
    Sleep(100)

    def lambda_62C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_62C)
    WaitChrThread(0x8, 2)

    #C0003
    ChrTalk(
        0x101,
        "#00005F#11P#10Aあ……\x02",
    )
    #Auto

    OP_68(166500, 1100, -100, 2000)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)

    def lambda_670():
        OP_95(0xFE, 157000, 0, -1300, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_670)
    WaitChrThread(0x9, 2)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_696():
        OP_95(0xFE, 157000, 0, -1300, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_696)
    CloseMessageWindow()
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(171500, 1200, 1100, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0004
    ChrTalk(
        0x104,
        (
            "#00306F#11Pやれやれ……\x01",
            "元気な兄さんたちだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#00101F#11P私たちも急ぎましょう。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#6P#00007F#5Pああ……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_37()
    SetChrPos(0x0, 171500, 0, 1500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x142, 6)
    OP_29(0xA4, 0x1, 0x6)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x0, 0x10)
    EventEnd(0x5)
    Return()

    # Function_3_397 end

    def Function_4_7D8(): pass

    label("Function_4_7D8")


    def lambda_7DD():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7DD)

    def lambda_7F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7F7)
    WaitChrThread(0xFE, 1)

    def lambda_80C():
        OP_96(0xFE, 0x29ACC, 0x0, 0xFFFFFAEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_80C)
    WaitChrThread(0xFE, 1)

    def lambda_82A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_82A)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_4_7D8 end

    def Function_5_837(): pass

    label("Function_5_837")


    def lambda_83C():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83C)

    def lambda_856():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_856)
    WaitChrThread(0xFE, 1)

    def lambda_86B():
        OP_96(0xFE, 0x2A10C, 0x0, 0xFFFFFAEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86B)
    WaitChrThread(0xFE, 1)

    def lambda_889():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_889)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_5_837 end

    def Function_6_896(): pass

    label("Function_6_896")


    def lambda_89B():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_89B)

    def lambda_8B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B5)
    WaitChrThread(0xFE, 1)

    def lambda_8CA():
        OP_96(0xFE, 0x29B94, 0x0, 0x1F4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8CA)
    WaitChrThread(0xFE, 1)

    def lambda_8E8():

        label("loc_8E8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_8E8")

    QueueWorkItem2(0xFE, 2, lambda_8E8)
    Return()

    # Function_6_896 end

    def Function_7_8F6(): pass

    label("Function_7_8F6")


    def lambda_8FB():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FB)

    def lambda_915():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_915)
    WaitChrThread(0xFE, 1)

    def lambda_92A():
        OP_96(0xFE, 0x2A044, 0x0, 0x1F4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_92A)
    WaitChrThread(0xFE, 1)

    def lambda_948():

        label("loc_948")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_948")

    QueueWorkItem2(0xFE, 2, lambda_948)
    Return()

    # Function_7_8F6 end

    def Function_8_956(): pass

    label("Function_8_956")


    def lambda_95B():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_95B)

    def lambda_975():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_975)
    WaitChrThread(0xFE, 1)

    def lambda_98A():
        OP_95(0xFE, 169900, 0, 1300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_98A)
    WaitChrThread(0xFE, 1)

    def lambda_9A8():

        label("loc_9A8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9A8")

    QueueWorkItem2(0xFE, 2, lambda_9A8)
    Return()

    # Function_8_956 end

    def Function_9_9B6(): pass

    label("Function_9_9B6")


    def lambda_9BB():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9BB)

    def lambda_9D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9D5)
    WaitChrThread(0xFE, 1)

    def lambda_9EA():
        OP_96(0xFE, 0x2A42C, 0x0, 0x514, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EA)
    WaitChrThread(0xFE, 1)

    def lambda_A08():

        label("loc_A08")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_A08")

    QueueWorkItem2(0xFE, 2, lambda_A08)
    Return()

    # Function_9_9B6 end

    def Function_10_A16(): pass

    label("Function_10_A16")


    def lambda_A1B():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1B)

    def lambda_A35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A35)
    WaitChrThread(0xFE, 1)

    def lambda_A4A():
        OP_96(0xFE, 0x29B94, 0x0, 0x76C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4A)
    WaitChrThread(0xFE, 1)

    def lambda_A68():

        label("loc_A68")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_A68")

    QueueWorkItem2(0xFE, 2, lambda_A68)
    Return()

    # Function_10_A16 end

    def Function_11_A76(): pass

    label("Function_11_A76")


    def lambda_A7B():
        OP_96(0xFE, 0x29DEC, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A7B)

    def lambda_A95():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A95)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)

    def lambda_ABC():
        OP_96(0xFE, 0x2A044, 0x0, 0x76C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ABC)
    WaitChrThread(0xFE, 1)

    def lambda_ADA():

        label("loc_ADA")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_ADA")

    QueueWorkItem2(0xFE, 2, lambda_ADA)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Return()

    # Function_11_A76 end

    def Function_12_AF1(): pass

    label("Function_12_AF1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02401.itc", 0x1E)
    LoadChrToIndex("chr/ch00901.itc", 0x1F)
    SoundLoad(1007)
    SetChrPos(0x101, 35500, 0, 0, 270)
    SetChrPos(0x102, 35500, 0, 0, 270)
    SetChrPos(0x103, 35500, 0, 0, 270)
    SetChrPos(0x104, 35500, 0, 0, 270)
    SetChrPos(0x109, 35500, 0, 0, 270)
    SetChrPos(0x105, 35500, 0, 0, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 8000, 0, 0, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 8000, 0, 0, 180)
    OP_68(0, -40000, 0, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(35500, 0)
    OP_68(0, 0, 0, 9000)
    SetCameraDistance(40500, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    BeginChrThread(0xA, 1, 0, 20)
    BeginChrThread(0x8, 3, 0, 13)
    Sleep(500)
    OP_68(0, -3000, 0, 7000)
    MoveCamera(40, 33, 0, 7000)
    SetCameraDistance(58500, 7000)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 13)
    OP_6F(0x79)
    Sleep(1000)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    StopSound(1007, 2000, 100)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Fade(500)
    OP_68(27000, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18500, 0)
    OP_68(32000, 1000, 0, 3000)
    SetCameraDistance(15500, 3000)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 19)
    OP_6F(0x79)
    WaitChrThread(0x105, 3)

    #C0007
    ChrTalk(
        0x101,
        "#00011F#11Pこれは……凄い所に出たな。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        "#10111F#11P何だか圧倒されますね……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x105,
        (
            "#10305F#11Pへえ……\x01",
            "どういう場所なんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#11P#00203Fオルキスタワーの\x01",
            "メインシャフトになりますね。\x02\x03",

            "#00200F巨大なタワーの重量を\x01",
            "分散するための場所みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        (
            "#00106F#11P話は聞いていたけど……\x01",
            "こんなに大きな空間とは\x01",
            "知らなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    #C0012
    ChrTalk(
        0x104,
        "#00301F#5Pま、とにかく急ごうぜ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(150)

    #C0013
    ChrTalk(
        0x101,
        "#5P#00001Fああ、南の方だ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, 32000, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_24(0x3EF)
    SetScenarioFlags(0x142, 7)
    EventEnd(0x5)
    Return()

    # Function_12_AF1 end

    def Function_13_F4E(): pass

    label("Function_13_F4E")


    def lambda_F53():
        OP_95(0xFE, 0, 0, -8000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F53)
    WaitChrThread(0xFE, 1)

    def lambda_F71():
        OP_95(0xFE, 0, 0, -38000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F71)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_F4E end

    def Function_14_F8B(): pass

    label("Function_14_F8B")


    def lambda_F90():
        OP_96(0xFE, 0x82DC, 0x0, 0x12C, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F90)

    def lambda_FAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FAA)
    WaitChrThread(0xFE, 1)

    def lambda_FBF():
        OP_96(0xFE, 0x79E0, 0x0, 0x1C2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FBF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_F8B end

    def Function_15_FD9(): pass

    label("Function_15_FD9")


    def lambda_FDE():
        OP_96(0xFE, 0x82DC, 0x0, 0xFFFFFED4, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FDE)

    def lambda_FF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FF8)
    WaitChrThread(0xFE, 1)

    def lambda_100D():
        OP_96(0xFE, 0x7AA8, 0x0, 0xFFFFFE3E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_100D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_FD9 end

    def Function_16_1027(): pass

    label("Function_16_1027")


    def lambda_102C():
        OP_96(0xFE, 0x82DC, 0x0, 0xFFFFFED4, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_102C)

    def lambda_1046():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1046)
    WaitChrThread(0xFE, 1)

    def lambda_105B():
        OP_95(0xFE, 32400, 0, -1300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_105B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_16_1027 end

    def Function_17_107C(): pass

    label("Function_17_107C")


    def lambda_1081():
        OP_96(0xFE, 0x82DC, 0x0, 0x12C, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1081)

    def lambda_109B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_109B)
    WaitChrThread(0xFE, 1)

    def lambda_10B0():
        OP_95(0xFE, 32200, 0, 1300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_107C end

    def Function_18_10D1(): pass

    label("Function_18_10D1")


    def lambda_10D6():
        OP_96(0xFE, 0x82DC, 0x0, 0x12C, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D6)

    def lambda_10F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10F0)
    WaitChrThread(0xFE, 1)

    def lambda_1105():
        OP_96(0xFE, 0x7FBC, 0x0, 0x1C2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1105)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_10D1 end

    def Function_19_111F(): pass

    label("Function_19_111F")


    def lambda_1124():
        OP_96(0xFE, 0x82DC, 0x0, 0xFFFFFED4, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1124)

    def lambda_113E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_113E)
    WaitChrThread(0xFE, 1)

    def lambda_1153():
        OP_96(0xFE, 0x8084, 0x0, 0xFFFFFE3E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1153)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Return()

    # Function_19_111F end

    def Function_20_1188(): pass

    label("Function_20_1188")

    Sound(1007, 2, 20, 0)
    Sleep(200)
    OP_25(0x3EF, 0x1E)
    Sleep(200)
    OP_25(0x3EF, 0x28)
    Sleep(200)
    OP_25(0x3EF, 0x32)
    Sleep(200)
    OP_25(0x3EF, 0x3C)
    Sleep(200)
    OP_25(0x3EF, 0x46)
    Sleep(200)
    OP_25(0x3EF, 0x50)
    Sleep(200)
    OP_25(0x3EF, 0x5A)
    Sleep(200)
    OP_25(0x3EF, 0x64)
    Sleep(5200)
    StopSound(1007, 2000, 90)
    Return()

    # Function_20_1188 end

    def Function_21_11D0(): pass

    label("Function_21_11D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(931)
    SoundLoad(825)
    SetMapObjFrame(0xFF, "rai00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "05_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "under_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ugoku01", 0x0, 0x1)
    OP_68(-12000, -12000, -2500, 0)
    MoveCamera(75, 63, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(39500, 0)
    SetChrPos(0x0, 0, 0, 0, 0)
    SetChrPos(0x1, 0, 0, 0, 0)
    SetChrPos(0x2, 0, 0, 0, 0)
    SetChrPos(0x3, 0, 0, 0, 0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    OP_68(0, -3000, 0, 12000)
    MoveCamera(130, 63, 0, 12000)
    SetCameraDistance(79500, 12000)
    Sound(930, 0, 100, 0)
    Sound(929, 0, 50, 0)
    Sound(931, 2, 80, 0)
    Sound(825, 2, 100, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    Sound(929, 0, 60, 0)
    Sleep(3000)
    Sound(929, 0, 60, 0)
    Sleep(2000)
    StopSound(931, 2000, 80)
    StopSound(825, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("m0209", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_11D0 end

    def Function_22_135D(): pass

    label("Function_22_135D")

    EventBegin(0x1)

    #C0014
    ChrTalk(
        0x101,
        "#00001F俺たちも先を急ごう！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 171130, 0, 1480, 180)
    EventEnd(0x4)
    Return()

    # Function_22_135D end

    def Function_23_1394(): pass

    label("Function_23_1394")

    EventBegin(0x2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　この先、シャフト制御室　※\x01",
            "※　関係者以外立ち入り禁止　※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F5")

    #C0016
    ChrTalk(
        0x104,
        (
            "#00303Fまさか、こっちの方には\x01",
            "行ってねえよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#00200Fええ、セキュリティが\x01",
            "解除された様子もないので\x01",
            "この先は大丈夫なはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00001F――ならダドリーさんたちを\x01",
            "追うだけだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        "#00101Fええ、南に向かいましょう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C7, 5)

    label("loc_14F5")

    EventEnd(0x3)
    Return()

    # Function_23_1394 end

    SaveToFile()

Try(main)
