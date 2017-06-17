from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0401.bin",                # FileName
        "m0401",                    # MapName
        "m0401",                    # Location
        0x00A9,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 169, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0401",                  # 0
        "ダドリー捜査官",         # 1
        "アリオス",               # 2
        "戦鬼シグムント",         # 3
        "シャーリィ",             # 4
        "猟兵ガレス",             # 5
        "赤い星座の猟兵",         # 6
        "赤い星座の猟兵",         # 7
        "赤い星座の猟兵",         # 8
        "赤い星座の猟兵",         # 9
        "銀",                     # 10
        "ツァオ",                 # 11
        "ラウ",                   # 12
        "黒月構成員",             # 13
        "黒月構成員",             # 14
        "黒月構成員",             # 15
        "黒月構成員",             # 16
    ))

    AddCharChip((
        "chr/ch00953.itc",                   # 00
        "chr/ch02400.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       -16500,  180,  453,  0x0, 3,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(1500,    0,       -16100,  225,  453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 5,   0.0,                   -8.0,                  -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.6666667461395264,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 2,   0.0,                   9.5,                   -1.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -3.1666667461395264,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 3,   -24.0,                 9.0,                   -9.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.0,                   -3.0,                  1.8000000715255737,    1.0])
    DeclEvent(0x0000, 0, 4,   28.5,                  -19.0,                 3.0,                   81.0,                  [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -9.5,                  3.1666667461395264,    -0.6000000238418579,   1.0])
    DeclEvent(0x0000, 0, 15,  -24.0,                 6.0,                   -8.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.6000001430511475,    -2.0,                  1.600000023841858,     1.0])
    DeclEvent(0x0000, 0, 17,  22.0,                  -19.0,                 3.0,                   144.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -7.333333492279053,    2.375,                 -0.6000000238418579,   1.0])

    DeclActor(0,       0,       8220,    1500,    0,       2000,    8500,    0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1400, 0)                                       # 0

    ScpFunction((
        "Function_0_578",          # 00, 0
        "Function_1_5A3",          # 01, 1
        "Function_2_6C2",          # 02, 2
        "Function_3_6F0",          # 03, 3
        "Function_4_71E",          # 04, 4
        "Function_5_74C",          # 05, 5
        "Function_6_16BD",         # 06, 6
        "Function_7_16FA",         # 07, 7
        "Function_8_293C",         # 08, 8
        "Function_9_2979",         # 09, 9
        "Function_10_29A2",        # 0A, 10
        "Function_11_29DF",        # 0B, 11
        "Function_12_2A1C",        # 0C, 12
        "Function_13_2A45",        # 0D, 13
        "Function_14_2A82",        # 0E, 14
        "Function_15_2EB6",        # 0F, 15
        "Function_16_2F31",        # 10, 16
        "Function_17_2F7C",        # 11, 17
    ))


    def Function_0_578(): pass

    label("Function_0_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_58A")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 3)
    Event(0, 7)

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A2")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)

    label("loc_5A2")

    Return()

    # Function_0_578 end

    def Function_1_5A3(): pass

    label("Function_1_5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5BD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)
    Jump("loc_5D2")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_5D2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_5D2")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EA")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5EA")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_62E")
    ModifyEventFlags(1, 1, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_62E")
    OP_70(0x0, 0x28)
    ClearMapObjFlags(0x0, 0x2)
    SetScenarioFlags(0x0, 0)

    label("loc_62E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64D")
    OP_70(0x1, 0x28)
    ClearMapObjFlags(0x1, 0x2)
    SetScenarioFlags(0x0, 1)

    label("loc_64D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66C")
    OP_70(0x2, 0x28)
    ClearMapObjFlags(0x2, 0x2)
    SetScenarioFlags(0x0, 2)

    label("loc_66C")

    ModifyEventFlags(0, 5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_693")
    OP_1B(0x0, 0x0, 0x10)
    OP_70(0x0, 0x28)
    ClearMapObjFlags(0x0, 0x2)
    ModifyEventFlags(1, 5, 0x80)

    label("loc_693")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A9")
    OP_66(0x0, 0x1)

    label("loc_6A9")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C1")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_6C1")

    Return()

    # Function_1_5A3 end

    def Function_2_6C2(): pass

    label("Function_2_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EF")
    TalkBegin(0xFF)
    Sound(147, 0, 100, 0)
    OP_71(0x0, 0x0, 0x28, 0x0, 0x8)
    ClearMapObjFlags(0x0, 0x2)
    SetScenarioFlags(0x0, 0)
    OP_79(0x0)
    EventEnd(0x3)

    label("loc_6EF")

    Return()

    # Function_2_6C2 end

    def Function_3_6F0(): pass

    label("Function_3_6F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71D")
    TalkBegin(0xFF)
    Sound(147, 0, 100, 0)
    OP_71(0x1, 0x0, 0x28, 0x0, 0x8)
    ClearMapObjFlags(0x1, 0x2)
    SetScenarioFlags(0x0, 1)
    OP_79(0x1)
    EventEnd(0x3)

    label("loc_71D")

    Return()

    # Function_3_6F0 end

    def Function_4_71E(): pass

    label("Function_4_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74B")
    TalkBegin(0xFF)
    Sound(147, 0, 100, 0)
    OP_71(0x2, 0x0, 0x28, 0x0, 0x8)
    ClearMapObjFlags(0x2, 0x2)
    SetScenarioFlags(0x0, 2)
    OP_79(0x2)
    EventEnd(0x3)

    label("loc_74B")

    Return()

    # Function_4_71E end

    def Function_5_74C(): pass

    label("Function_5_74C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch02401.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch00901.itc", 0x20)
    SoundLoad(147)
    OP_68(0, 900, -7900, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, -8200, 180)
    SetChrPos(0x102, 600, 0, -7900, 180)
    SetChrPos(0x103, -600, 0, -7000, 180)
    SetChrPos(0x104, 800, 0, -6700, 180)
    SetChrPos(0x109, -1800, 0, -7300, 180)
    SetChrPos(0x105, 1800, 0, -7300, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(0, 1100, -16500, 2000)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x8,
        (
            "#6P#00608Fこれは……\x01",
            "間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        (
            "#5P#01403Fああ、共同戦線は\x01",
            "ここまでだったようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1000, 900, -14600, 4000)
    SetCameraDistance(16500, 4000)

    def lambda_8F5():
        OP_97(0x101, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8F5)
    Sleep(100)

    def lambda_912():
        OP_97(0x102, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_912)
    Sleep(100)

    def lambda_92F():
        OP_97(0x103, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_92F)
    Sleep(100)

    def lambda_94C():
        OP_97(0x104, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_94C)
    Sleep(100)

    def lambda_969():
        OP_97(0x109, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_969)
    Sleep(100)

    def lambda_986():
        OP_97(0x105, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_986)
    WaitChrThread(0x109, 0)

    def lambda_9A4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9A4)
    WaitChrThread(0x105, 0)

    def lambda_9B5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9B5)

    #C0003
    ChrTalk(
        0x101,
        "#00001F#5Pダドリーさん、アリオスさん。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x109,
        "#10108F#5Pあの、どうかしたんですか？\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(150)

    #C0005
    ChrTalk(
        0x8,
        (
            "#12P#00606F……面倒な事になった。\x02\x03",

            "#00601Fテロリストどもは\x01",
            "ここで２手に分かれたらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0006
    ChrTalk(
        0x102,
        "#5P#00101Fそれって……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#5P#00301F宰相を狙ってた連中と\x01",
            "大統領を狙ってた連中が\x01",
            "ここで分かれたってことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "#12P#01403Fああ、間違いあるまい。\x02",
    )

    CloseMessageWindow()
    OP_68(22500, 4900, -19000, 3000)
    MoveCamera(53, 23, 0, 3000)
    SetCameraDistance(24000, 3000)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(100)

    def lambda_BFB():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BFB)
    Sleep(50)

    def lambda_C0B():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C0B)
    Sleep(50)

    def lambda_C1B():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C1B)
    Sleep(50)

    def lambda_C2B():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C2B)
    Sleep(50)

    def lambda_C3B():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C3B)
    Sleep(50)

    def lambda_C4B():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C4B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    Sleep(300)

    #C0009
    ChrTalk(
        0x9,
        (
            "#01400F共和国のテロリストは\x01",
            "そちらのジオフロントＣ区画──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1000, 900, -14600, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_68(-24000, -7100, 4500, 3500)
    MoveCamera(37, 23, 0, 3500)
    SetCameraDistance(24000, 3500)
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(100)

    def lambda_D1B():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D1B)
    Sleep(50)

    def lambda_D2B():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D2B)
    Sleep(50)

    def lambda_D3B():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D3B)
    Sleep(50)

    def lambda_D4B():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D4B)
    Sleep(50)

    def lambda_D5B():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D5B)
    Sleep(50)

    def lambda_D6B():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D6B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    Sleep(300)

    #C0010
    ChrTalk(
        0x9,
        (
            "#01401Fそして帝国のテロリストは\x01",
            "あちらのＤ区画に逃げたようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1000, 900, -14600, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    BeginChrThread(0x9, 3, 0, 6)
    Sleep(50)

    def lambda_E19():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E19)
    Sleep(50)

    def lambda_E29():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E29)
    Sleep(50)

    def lambda_E39():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E39)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    #C0011
    ChrTalk(
        0x102,
        "#5P#00105Fよ、よく分かりますね。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x105,
        "#5P#10302Fなるほど、決め手は足跡かい？\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(300)

    #C0013
    ChrTalk(
        0x9,
        (
            "#12P#01404Fああ、偽装している余裕は\x01",
            "さすがに無かったと見える。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00003F#5Pだったら……\x01",
            "ここは２手に分かれましょう。\x02\x03",

            "#00001F急がないとこのまま\x01",
            "連中に逃げられてしまいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#12P#00603Fああ、それが最善だろう。\x02\x03",

            "#00600F──右手のＣ区画は、\x01",
            "私とマクレインの２人で追う。\x02\x03",

            "お前たちはＤ区画に逃げた\x01",
            "帝国のテロリストどもを追え。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0016
    ChrTalk(
        0x101,
        (
            "#00005F#5Pえ……\x01",
            "人数を分けないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#00208F#5Pさすがに２人だけというのは\x01",
            "危険なのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#12P#01403FこちらのＣ区画は\x01",
            "熱処理プラントなどがあって\x01",
            "少々面倒な場所だったはず。\x02\x03",

            "#01400F逆に、そちらのＤ区画は\x01",
            "広くて探索が大変なはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        "#5P#00304Fいい分担かもしれねぇな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    #C0020
    ChrTalk(
        0x104,
        (
            "#5P#00301Fロイド、時間がねぇ。\x01",
            "それで行くとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00006F#5P……分かった。\x02\x03",

            "#00001Fダドリーさん、アリオスさん。\x01",
            "どうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1257():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1257)
    Sleep(100)

    #C0022
    ChrTalk(
        0x9,
        "#12P#01404Fフッ、そちらこそな。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#12P#00603F敵は自分の命すら厭#2Rいと#わない\x01",
            "危険なテロリストどもだ。\x02\x03",

            "#00601Fくれぐれも気を付けろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00007F#5Pはい……！\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        "#10101F了解しました！\x02",
    )

    CloseMessageWindow()

    def lambda_132A():

        label("loc_132A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_132A")

    QueueWorkItem2(0x101, 2, lambda_132A)

    def lambda_133C():

        label("loc_133C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_133C")

    QueueWorkItem2(0x103, 2, lambda_133C)

    def lambda_134E():

        label("loc_134E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_134E")

    QueueWorkItem2(0x105, 2, lambda_134E)

    def lambda_1360():

        label("loc_1360")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1360")

    QueueWorkItem2(0x102, 2, lambda_1360)

    def lambda_1372():

        label("loc_1372")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1372")

    QueueWorkItem2(0x104, 2, lambda_1372)

    def lambda_1384():

        label("loc_1384")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1384")

    QueueWorkItem2(0x109, 2, lambda_1384)

    def lambda_1396():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1396)
    Sleep(100)

    def lambda_13A6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_13A6)
    WaitChrThread(0x9, 2)
    OP_68(22500, 4900, -19000, 3000)
    MoveCamera(53, 23, 0, 3000)
    SetCameraDistance(24000, 3000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)

    def lambda_13E9():
        OP_95(0xFE, 26000, 4000, -19000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13E9)
    WaitChrThread(0x8, 2)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_1414():
        OP_95(0xFE, 25600, 4000, -18000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1414)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    Sound(147, 0, 100, 0)
    OP_71(0x2, 0x0, 0x28, 0x0, 0x0)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)

    def lambda_1463():
        OP_95(0xFE, 31000, 4000, -19000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1463)
    Sleep(200)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)

    def lambda_1488():
        OP_95(0xFE, 30600, 4000, -18000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1488)
    Sleep(300)

    def lambda_14A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14A5)
    Sleep(200)

    def lambda_14B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_14B9)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    Sound(147, 2, 100, 0)
    OP_71(0x2, 0x28, 0x0, 0x0, 0x0)
    Sleep(500)
    StopSound(147, 1000, 100)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Fade(500)
    OP_68(700, 900, -13100, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(150)

    #C0026
    ChrTalk(
        0x101,
        (
            "#6P#00013Fよし、俺たちも行こう！\x02\x03",

            "ジオフロントから脱出される前に\x01",
            "テロリストを捕まえるんだ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15B6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_15B6)
    Sleep(50)

    def lambda_15C6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_15C6)
    Sleep(50)

    def lambda_15D6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15D6)
    Sleep(50)

    def lambda_15E6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15E6)
    Sleep(50)

    def lambda_15F6():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_15F6)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0027
    ChrTalk(
        0x102,
        "#00101F#11Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#00307F#5Pきっちり落とし前を\x01",
            "付けさせてやらねぇとな！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_79(0x2)
    OP_70(0x2, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_37()
    SetChrPos(0x0, 0, 0, -14500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x143, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0xA4, 0x1, 0x7)
    OP_24(0x93)
    EventEnd(0x5)
    Return()

    # Function_5_74C end

    def Function_6_16BD(): pass

    label("Function_6_16BD")


    def lambda_16C2():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_16C2)
    Sleep(50)

    def lambda_16D2():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_16D2)
    Sleep(50)

    def lambda_16E2():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16E2)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    Return()

    # Function_6_16BD end

    def Function_7_16FA(): pass

    label("Function_7_16FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    LoadChrToIndex("chr/ch03400.itc", 0x1F)
    LoadChrToIndex("chr/ch41900.itc", 0x20)
    LoadChrToIndex("chr/ch00500.itc", 0x21)
    LoadChrToIndex("chr/ch06300.itc", 0x22)
    LoadChrToIndex("chr/ch31400.itc", 0x23)
    LoadChrToIndex("chr/ch31500.itc", 0x24)
    LoadChrToIndex("chr/ch12500.itc", 0x25)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis405.itp")
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, 200600, 0, 26200, 180)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xB, 199100, 0, 26500, 180)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, 200400, 0, 28300, 180)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrPos(0xD, 198400, 0, 28700, 180)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrPos(0xE, 202000, 0, 30300, 180)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x4)
    SetChrPos(0xF, 199700, 0, 29500, 180)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrPos(0x10, 198000, 0, 30100, 180)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    OP_90(0x11, 198500, 0, -21500, 0)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    OP_90(0x12, 199900, 0, -20900, 0)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    OP_90(0x13, 200400, 0, -21700, 0)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    OP_90(0x14, 198500, 0, -23300, 0)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    OP_90(0x15, 199400, 0, -24200, 0)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    OP_90(0x16, 200700, 0, -22800, 0)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    OP_90(0x17, 201600, 0, -23700, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KＡｆｔｅｒｗａｒｄｓ（その後）\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_68(200000, 0, 0, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25000, 0)
    OP_11(0x12, 0x13, 0x16, 0x19, 0x9B, 0x0)
    OP_68(200000, -1000, 0, 9000)
    MoveCamera(30, 30, 0, 9000)
    SetCameraDistance(50000, 9000)
    PlayBGM("ed7571", 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3500)
    PlaceName2(340, 200, "c_plac71", 0x0, 0)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(200000, -3000, -17000, 0)
    MoveCamera(30, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(200000, 900, -9500, 5000)
    SetCameraDistance(15000, 5000)

    def lambda_1C11():
        OP_97(0x12, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1C11)
    Sleep(50)

    def lambda_1C2E():
        OP_97(0x13, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1C2E)
    Sleep(50)

    def lambda_1C4B():
        OP_97(0x11, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1C4B)
    Sleep(50)

    def lambda_1C68():
        OP_97(0x14, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1C68)
    Sleep(50)

    def lambda_1C85():
        OP_97(0x15, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1C85)
    Sleep(50)

    def lambda_1CA2():
        OP_97(0x16, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1CA2)
    Sleep(50)

    def lambda_1CBF():
        OP_97(0x17, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1CBF)
    WaitChrThread(0x11, 0)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x79)

    #C0030
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00700Fむ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x12,
        "#12P#03210Fほう……\x02",
    )

    CloseMessageWindow()
    OP_68(200000, 900, 17500, 3000)
    MoveCamera(30, 17, 0, 3000)

    def lambda_1D6E():
        OP_97(0xA, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1D6E)
    Sleep(100)

    def lambda_1D8B():
        OP_97(0xB, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1D8B)
    Sleep(100)

    def lambda_1DA8():
        OP_97(0xC, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1DA8)
    Sleep(100)

    def lambda_1DC5():
        OP_97(0xD, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1DC5)
    Sleep(100)

    def lambda_1DE2():
        OP_97(0xE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1DE2)
    Sleep(100)

    def lambda_1DFF():
        OP_97(0xF, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1DFF)
    Sleep(100)

    def lambda_1E1C():
        OP_97(0x10, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1E1C)
    WaitChrThread(0xA, 0)
    OP_6F(0x79)

    #C0032
    ChrTalk(
        0xA,
        "#5P#04500F──これはこれは。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xB,
        "#04612F#5Pあははっ、奇遇だね～！\x02",
    )

    CloseMessageWindow()

    def lambda_1E84():
        OP_97(0xA, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1E84)
    Sleep(100)

    def lambda_1EA1():
        OP_97(0xB, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1EA1)
    Sleep(100)

    def lambda_1EBE():
        OP_97(0xC, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1EBE)
    Sleep(100)

    def lambda_1EDB():
        OP_97(0xD, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1EDB)
    Sleep(100)

    def lambda_1EF8():
        OP_97(0xE, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1EF8)
    Sleep(100)

    def lambda_1F15():
        OP_97(0xF, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1F15)
    Sleep(100)

    def lambda_1F32():
        OP_97(0x10, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1F32)
    Sleep(1000)
    Fade(500)
    OP_68(200600, 900, -400, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(17000, 2500)
    OP_11(0x12, 0x13, 0x16, 0x19, 0x55, 0x0)

    def lambda_1F9B():
        OP_97(0x12, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1F9B)
    Sleep(100)

    def lambda_1FB8():
        OP_97(0x13, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1FB8)
    Sleep(100)

    def lambda_1FD5():
        OP_97(0x11, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1FD5)
    Sleep(100)

    def lambda_1FF2():
        OP_97(0x14, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1FF2)
    Sleep(100)

    def lambda_200F():
        OP_97(0x15, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_200F)
    Sleep(100)

    def lambda_202C():
        OP_97(0x16, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_202C)
    Sleep(100)

    def lambda_2049():
        OP_97(0x17, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2049)
    WaitChrThread(0x17, 0)
    OP_6F(0x79)

    #C0034
    ChrTalk(
        0x13,
        "《赤い星座》の……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x14,
        "#12P《戦鬼》とその娘か……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0)

    #C0036
    ChrTalk(
        0xC,
        (
            "#5Pシグムント様……\x01",
            "こちらの用意はいつでも。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xA,
        (
            "#5P#04504Fクク、構えるな。\x02\x03",

            "#04500Fお互い、クライアントの\x01",
            "オーダーをクリアした後だ。\x02\x03",

            "これ以上のお楽しみは\x01",
            "さすがに無粋というものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x12,
        (
            "#12P#03209Fフフ、同感です。\x02\x03",

            "#03205Fそういえば──\x01",
            "《ノイエ＝ブラン》新装開店、\x01",
            "どうもおめでとうございます。\x02\x03",

            "#03204Fなかなか挨拶に\x01",
            "伺えずに失礼しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "#5P#04504Fなんの、こちらこそ。\x02\x03",

            "#04500F知らぬ仲でもないのに\x01",
            "挨拶にも出向かずに悪かった。\x02\x03",

            "#04502Fそういえば……\x01",
            "死に損ないどもは元気か？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x12,
        (
            "#12P#03204Fハハ、嫌になるくらい\x01",
            "元気な方々ばかりですよ。\x02\x03",

            "#03210Fまあ貴方がたのおかげで\x01",
            "いまだに夢見が悪いご老人も\x01",
            "いらっしゃるようですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        (
            "#5P#04609Fあはは、長老会を襲って\x01",
            "人質に取ったりしたからね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00700F……フン、依頼で不在で\x01",
            "正解だったようだな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0043
    ChrTalk(
        0xB,
        (
            "#5P#04605Fああっ！\x01",
            "ひょっとして《銀#2Rイン#》！？\x02\x03",

            "#04602F東方人街最強っていう\x01",
            "伝説の凶手って！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00702F……そういうお前は\x01",
            "《血染めの#8Rブ ラ ッ デ ィ#シャーリィ》か。\x02\x03",

            "わずか１６で最強の猟兵団の\x01",
            "大隊長を務めているという。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        (
            "#5P#04606Fうーん、独りの方が\x01",
            "動きやすいんだけどね～。\x02\x03",

            "#04611F──それよりも、ねえ？\x02\x03",

            "カッコいい覆面をしてるけど\x01",
            "付けない方が強いんじゃないの？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00705F#30Wなに……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        (
            "#5P#04606F筋肉の使い方も不自然だし。\x02\x03",

            "#04600F普通にしてた方が強いはずなのに\x01",
            "勿体ないんじゃないかな～？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00700F………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)

    #C0049
    ChrTalk(
        0x12,
        "#11P#03205Fほほう……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        (
            "#5P#04504Fフフ、親馬鹿かもしれんが\x01",
            "こいつの見る目は確かでな。\x02\x03",

            "#04500Fまあ、気に障ったのなら\x01",
            "俺からも謝罪させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00702F……別に。\x02\x03",

            "#00700Fツァオ、下らぬ挨拶を\x01",
            "続けるのなら先に行くぞ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x12,
        "#11P#03204Fハハ、すみません。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xA, 500)
    Sleep(300)

    #C0053
    ChrTalk(
        0x12,
        "#12P#03202F──では、またの機会に#12R㈲　㈲　㈲　㈲　㈲　㈲#。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        "#5P#04502Fああ──またの機会に#12R㈲　㈲　㈲　㈲　㈲　㈲#。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        "#5P#04612Fふふっ、まったね～！\x02",
    )

    CloseMessageWindow()
    OP_68(200600, 1000, -400, 9000)
    MoveCamera(55, 23, 0, 9000)
    SetCameraDistance(35500, 9000)
    BeginChrThread(0xA, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x12, 0, 0, 8)
    Sleep(7000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_29(0xA4, 0x1, 0xA)
    OP_29(0xA3, 0x4, 0x10)
    OP_29(0xA4, 0x4, 0x10)
    OP_E5(0xA)
    SubItemNumber(0x324, 1)
    SubItemNumber(0x335, 1)
    SubItemNumber(0x336, 1)
    SubItemNumber(0x337, 1)
    SubItemNumber(0x338, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x1E, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_16FA end

    def Function_8_293C(): pass

    label("Function_8_293C")

    BeginChrThread(0x12, 3, 0, 9)
    Sleep(800)
    BeginChrThread(0x13, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 9)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x15, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x16, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x17, 3, 0, 10)
    Return()

    # Function_8_293C end

    def Function_9_2979(): pass

    label("Function_9_2979")

    OP_97(0xFE, 0x1388, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_9_2979 end

    def Function_10_29A2(): pass

    label("Function_10_29A2")

    OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_97(0xFE, 0x1388, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_10_29A2 end

    def Function_11_29DF(): pass

    label("Function_11_29DF")

    BeginChrThread(0xA, 3, 0, 12)
    Sleep(200)
    BeginChrThread(0xB, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0xC, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0xD, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0xE, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0xF, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0x10, 3, 0, 13)
    Return()

    # Function_11_29DF end

    def Function_12_2A1C(): pass

    label("Function_12_2A1C")

    OP_97(0xFE, 0xFFFFF34E, 0x0, 0xFFFFF5D8, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_12_2A1C end

    def Function_13_2A45(): pass

    label("Function_13_2A45")

    OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFFF34E, 0x0, 0xFFFFF5D8, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_2A45 end

    def Function_14_2A82(): pass

    label("Function_14_2A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2A")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 40, 0, 4910, 0)
    SetChrPos(0x102, -1370, 0, 4110, 0)
    SetChrPos(0x103, 1370, 0, 4510, 0)
    SetChrPos(0x104, -2440, 0, 4920, 44)
    SetChrPos(0x105, 2740, 0, 5280, 315)
    SetChrPos(0x109, -3320, 0, 6000, 390)
    OP_68(1470, 0, 8070, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20900, 0)
    OP_0D()
    Sleep(1000)

    #C0056
    ChrTalk(
        0x101,
        (
            "#00005Fこっちは確か……\x01",
            "オルキスタワーの基部に\x01",
            "繋がっているゲートだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#00203F通商会議でテロリストを\x01",
            "追うときに通った区画ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x105,
        (
            "#10306Fま、今は完全に封鎖されている\x01",
            "みたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x109,
        (
            "#10103F丁度そのあたりで\x01",
            "アリオスさんたちと二手に\x01",
            "別れたんでしたよね。\x02\x03",

            "#10108Fそれから……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(50)
    OP_64(0x102)
    Sleep(50)
    OP_64(0x103)
    Sleep(50)
    OP_64(0x104)
    Sleep(50)
    OP_64(0x105)

    #C0060
    ChrTalk(
        0x109,
        (
            "#10106Fす、すみません。\x01",
            "あまりいい思い出じゃ\x01",
            "ありませんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        "#00304F……はは、気にすんな。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#00103F#4Pとにかく、こっちには\x01",
            "地上に出るリフトはないわ。\x02\x03",

            "#00100FＤ区画の方も封鎖されているし、\x01",
            "一旦Ｃ区画の方に戻りましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00000Fああ、そうしよう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 0, 0, 4910, 0)
    SetScenarioFlags(0x190, 3)
    EventEnd(0x5)
    Jump("loc_2EB5")

    label("loc_2E2A")

    TalkBegin(0xFF)

    #C0064
    ChrTalk(
        0x101,
        (
            "#00000Fこっちはオルキスタワーの基部に\x01",
            "繋がっているゲートだ。\x02\x03",

            "今は封鎖されているみたいだし、\x01",
            "Ｃ区画の方に戻ってリフトを使おう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2EB5")

    Return()

    # Function_14_2A82 end

    def Function_15_2EB6(): pass

    label("Function_15_2EB6")

    EventBegin(0x1)

    #C0065
    ChrTalk(
        0x101,
        (
            "#00003FこっちはＤ区画に繋がるゲートだな。\x02\x03",

            "……今はＣ区画に戻って、\x01",
            "地上に出るリフトを使おう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24210, -8000, 3000, 180)
    EventEnd(0x4)
    Return()

    # Function_15_2EB6 end

    def Function_16_2F31(): pass

    label("Function_16_2F31")

    EventBegin(0x1)

    #C0066
    ChrTalk(
        0x101,
        (
            "#00003F引き返している時間はない。\x01",
            "先を急ごう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -390, 0, 6230, 180)
    EventEnd(0x4)
    Return()

    # Function_16_2F31 end

    def Function_17_2F7C(): pass

    label("Function_17_2F7C")

    EventBegin(0x1)

    #C0067
    ChrTalk(
        0x101,
        (
            "#00001FＣ区画の方は、ダドリーさんと\x01",
            "アリオスさんに任せよう。\x02\x03",

            "俺たちはＤ区画に逃げた\x01",
            "帝国のテロリストを追うぞ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19030, 4000, -19240, 270)
    EventEnd(0x4)
    Return()

    # Function_17_2F7C end

    SaveToFile()

Try(main)
