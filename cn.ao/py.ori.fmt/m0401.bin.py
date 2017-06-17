from ScenarioHelper import *

def main():
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
        "达德利搜查官",           # 1
        "亚里欧斯",               # 2
        "战鬼西格蒙德",           # 3
        "谢莉",                   # 4
        "猎兵加雷斯",             # 5
        "赤色星座猎兵",           # 6
        "赤色星座猎兵",           # 7
        "赤色星座猎兵",           # 8
        "赤色星座猎兵",           # 9
        "银",                     # 10
        "曹",                     # 11
        "刘",                     # 12
        "黑月成员",               # 13
        "黑月成员",               # 14
        "黑月成员",               # 15
        "黑月成员",               # 16
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

    ChipFrameInfo(2387, 112)                                     # 0

    ScpFunction((
        "Function_0_578",          # 00, 0
        "Function_1_5A3",          # 01, 1
        "Function_2_6C2",          # 02, 2
        "Function_3_6F0",          # 03, 3
        "Function_4_71E",          # 04, 4
        "Function_5_74C",          # 05, 5
        "Function_6_15CF",         # 06, 6
        "Function_7_160C",         # 07, 7
        "Function_8_277A",         # 08, 8
        "Function_9_27B7",         # 09, 9
        "Function_10_27E0",        # 0A, 10
        "Function_11_281D",        # 0B, 11
        "Function_12_285A",        # 0C, 12
        "Function_13_2883",        # 0D, 13
        "Function_14_28C0",        # 0E, 14
        "Function_15_2CAA",        # 0F, 15
        "Function_16_2D17",        # 10, 16
        "Function_17_2D56",        # 11, 17
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
            "#6P#00608F这……\x01",
            "果然如此啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        (
            "#5P#01403F嗯，由这里开始，\x01",
            "他们似乎就分头行动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1000, 900, -14600, 4000)
    SetCameraDistance(16500, 4000)

    def lambda_8E9():
        OP_97(0x101, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E9)
    Sleep(100)

    def lambda_906():
        OP_97(0x102, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_906)
    Sleep(100)

    def lambda_923():
        OP_97(0x103, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_923)
    Sleep(100)

    def lambda_940():
        OP_97(0x104, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_940)
    Sleep(100)

    def lambda_95D():
        OP_97(0x109, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_95D)
    Sleep(100)

    def lambda_97A():
        OP_97(0x105, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_97A)
    WaitChrThread(0x109, 0)

    def lambda_998():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_998)
    WaitChrThread(0x105, 0)

    def lambda_9A9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9A9)

    #C0003
    ChrTalk(
        0x101,
        "#00001F#5P达德利警官、亚里欧斯先生。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x109,
        "#10108F#5P那个……发生什么事了？\x02",
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
            "#12P#00606F……情况比较麻烦。\x02\x03",

            "#00601F恐怖分子好像\x01",
            "兵分两路了。\x02",
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
        "#5P#00101F也就是说……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#5P#00301F企图杀害宰相的那伙人\x01",
            "和企图杀害总统的那伙人\x01",
            "在这里分路而行了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "#12P#01403F嗯，不会有错。\x02",
    )

    CloseMessageWindow()
    OP_68(22500, 4900, -19000, 3000)
    MoveCamera(53, 23, 0, 3000)
    SetCameraDistance(24000, 3000)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(100)

    def lambda_BC3():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BC3)
    Sleep(50)

    def lambda_BD3():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BD3)
    Sleep(50)

    def lambda_BE3():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BE3)
    Sleep(50)

    def lambda_BF3():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BF3)
    Sleep(50)

    def lambda_C03():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C03)
    Sleep(50)

    def lambda_C13():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C13)
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
            "#01400F共和国的恐怖分子似乎\x01",
            "从那边进入地下空间Ｃ区域了。\x02",
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

    def lambda_CE1():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CE1)
    Sleep(50)

    def lambda_CF1():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CF1)
    Sleep(50)

    def lambda_D01():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D01)
    Sleep(50)

    def lambda_D11():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D11)
    Sleep(50)

    def lambda_D21():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D21)
    Sleep(50)

    def lambda_D31():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D31)
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
            "#01401F而帝国的恐怖分子好像\x01",
            "逃往那边的Ｄ区域了。\x02",
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

    def lambda_DD1():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DD1)
    Sleep(50)

    def lambda_DE1():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DE1)
    Sleep(50)

    def lambda_DF1():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DF1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    #C0011
    ChrTalk(
        0x102,
        "#5P#00105F竟、竟然连这些都能发现。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x105,
        "#5P#10302F原来如此，决定性的证据就是脚印吧？\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(300)

    #C0013
    ChrTalk(
        0x9,
        (
            "#12P#01404F嗯，在这种情况下，\x01",
            "他们肯定来不及伪造足迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00003F#5P既然如此……\x01",
            "我们也分头行动吧。\x02\x03",

            "#00001F再不快点，\x01",
            "就会让他们逃掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#12P#00603F嗯，这是最妥善的选择。\x02\x03",

            "#00600F我和马克莱因去右侧的\x01",
            "Ｃ区域追击。\x02\x03",

            "你们就去追逃往Ｄ区域的\x01",
            "帝国恐怖分子吧。\x02",
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
            "#00005F#5P哎……\x01",
            "不平均分配人手吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#00208F#5P你们只有两个人，\x01",
            "未免也太危险了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#12P#01403FＣ区域中存在一些\x01",
            "热处理设备，\x01",
            "调查难度比较高。\x02\x03",

            "#01400F而Ｄ区域的面积广阔，\x01",
            "探索起来会很麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        "#5P#00304F原来如此，看来这种分配方式很合理。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    #C0020
    ChrTalk(
        0x104,
        (
            "#5P#00301F罗伊德，已经没时间了，\x01",
            "我们这就开始行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00006F#5P……明白了。\x02\x03",

            "#00001F达德利警官，亚里欧斯先生，\x01",
            "请多加小心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11A3():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11A3)
    Sleep(100)

    #C0022
    ChrTalk(
        0x9,
        "#12P#01404F嗯，你们也一样。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#12P#00603F敌人是一群非常危险的恐怖分子，\x01",
            "可谓亡命之徒。\x02\x03",

            "#00601F一定要多加小心！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00007F#5P是……！\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        "#10101F明白了！\x02",
    )

    CloseMessageWindow()

    def lambda_1258():

        label("loc_1258")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1258")

    QueueWorkItem2(0x101, 2, lambda_1258)

    def lambda_126A():

        label("loc_126A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_126A")

    QueueWorkItem2(0x103, 2, lambda_126A)

    def lambda_127C():

        label("loc_127C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_127C")

    QueueWorkItem2(0x105, 2, lambda_127C)

    def lambda_128E():

        label("loc_128E")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_128E")

    QueueWorkItem2(0x102, 2, lambda_128E)

    def lambda_12A0():

        label("loc_12A0")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_12A0")

    QueueWorkItem2(0x104, 2, lambda_12A0)

    def lambda_12B2():

        label("loc_12B2")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_12B2")

    QueueWorkItem2(0x109, 2, lambda_12B2)

    def lambda_12C4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_12C4)
    Sleep(100)

    def lambda_12D4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_12D4)
    WaitChrThread(0x9, 2)
    OP_68(22500, 4900, -19000, 3000)
    MoveCamera(53, 23, 0, 3000)
    SetCameraDistance(24000, 3000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)

    def lambda_1317():
        OP_95(0xFE, 26000, 4000, -19000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1317)
    WaitChrThread(0x8, 2)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_1342():
        OP_95(0xFE, 25600, 4000, -18000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1342)
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

    def lambda_1391():
        OP_95(0xFE, 31000, 4000, -19000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1391)
    Sleep(200)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)

    def lambda_13B6():
        OP_95(0xFE, 30600, 4000, -18000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13B6)
    Sleep(300)

    def lambda_13D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_13D3)
    Sleep(200)

    def lambda_13E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_13E7)
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
            "#6P#00013F好，我们也出发吧！\x02\x03",

            "一定要在那些恐怖分子逃离地下空间之前，\x01",
            "将他们抓捕归案！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14DE():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_14DE)
    Sleep(50)

    def lambda_14EE():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_14EE)
    Sleep(50)

    def lambda_14FE():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_14FE)
    Sleep(50)

    def lambda_150E():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_150E)
    Sleep(50)

    def lambda_151E():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_151E)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0027
    ChrTalk(
        0x102,
        "#00101F#11P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#00307F#5P必须狠狠\x01",
            "教训他们一下！\x02",
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

    def Function_6_15CF(): pass

    label("Function_6_15CF")


    def lambda_15D4():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_15D4)
    Sleep(50)

    def lambda_15E4():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15E4)
    Sleep(50)

    def lambda_15F4():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15F4)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    Return()

    # Function_6_15CF end

    def Function_7_160C(): pass

    label("Function_7_160C")

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
            "#1KＡｆｔｅｒｗａｒｄｓ（之后）\x02",
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

    def lambda_1B21():
        OP_97(0x12, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1B21)
    Sleep(50)

    def lambda_1B3E():
        OP_97(0x13, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1B3E)
    Sleep(50)

    def lambda_1B5B():
        OP_97(0x11, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1B5B)
    Sleep(50)

    def lambda_1B78():
        OP_97(0x14, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1B78)
    Sleep(50)

    def lambda_1B95():
        OP_97(0x15, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1B95)
    Sleep(50)

    def lambda_1BB2():
        OP_97(0x16, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1BB2)
    Sleep(50)

    def lambda_1BCF():
        OP_97(0x17, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1BCF)
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
            "#12P#00700F唔……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x12,
        "#12P#03210F哦……？\x02",
    )

    CloseMessageWindow()
    OP_68(200000, 900, 17500, 3000)
    MoveCamera(30, 17, 0, 3000)

    def lambda_1C7E():
        OP_97(0xA, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1C7E)
    Sleep(100)

    def lambda_1C9B():
        OP_97(0xB, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1C9B)
    Sleep(100)

    def lambda_1CB8():
        OP_97(0xC, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1CB8)
    Sleep(100)

    def lambda_1CD5():
        OP_97(0xD, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1CD5)
    Sleep(100)

    def lambda_1CF2():
        OP_97(0xE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1CF2)
    Sleep(100)

    def lambda_1D0F():
        OP_97(0xF, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1D0F)
    Sleep(100)

    def lambda_1D2C():
        OP_97(0x10, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1D2C)
    WaitChrThread(0xA, 0)
    OP_6F(0x79)

    #C0032
    ChrTalk(
        0xA,
        "#5P#04500F哎呀呀。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xB,
        "#04612F#5P啊哈哈，真是奇遇啊～！\x02",
    )

    CloseMessageWindow()

    def lambda_1D8A():
        OP_97(0xA, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1D8A)
    Sleep(100)

    def lambda_1DA7():
        OP_97(0xB, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1DA7)
    Sleep(100)

    def lambda_1DC4():
        OP_97(0xC, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1DC4)
    Sleep(100)

    def lambda_1DE1():
        OP_97(0xD, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1DE1)
    Sleep(100)

    def lambda_1DFE():
        OP_97(0xE, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1DFE)
    Sleep(100)

    def lambda_1E1B():
        OP_97(0xF, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1E1B)
    Sleep(100)

    def lambda_1E38():
        OP_97(0x10, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1E38)
    Sleep(1000)
    Fade(500)
    OP_68(200600, 900, -400, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(17000, 2500)
    OP_11(0x12, 0x13, 0x16, 0x19, 0x55, 0x0)

    def lambda_1EA1():
        OP_97(0x12, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1EA1)
    Sleep(100)

    def lambda_1EBE():
        OP_97(0x13, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1EBE)
    Sleep(100)

    def lambda_1EDB():
        OP_97(0x11, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1EDB)
    Sleep(100)

    def lambda_1EF8():
        OP_97(0x14, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1EF8)
    Sleep(100)

    def lambda_1F15():
        OP_97(0x15, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1F15)
    Sleep(100)

    def lambda_1F32():
        OP_97(0x16, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1F32)
    Sleep(100)

    def lambda_1F4F():
        OP_97(0x17, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1F4F)
    WaitChrThread(0x17, 0)
    OP_6F(0x79)

    #C0034
    ChrTalk(
        0x13,
        "是『赤色星座』的……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x14,
        "#12P『战鬼』及其女儿……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0)

    #C0036
    ChrTalk(
        0xC,
        (
            "#5P西格蒙德副团长……\x01",
            "我们已经准备好了，随时可以开战。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xA,
        (
            "#5P#04504F哼哼，放松一些。\x02\x03",

            "#04500F我们双方都是刚刚将\x01",
            "雇主交代的工作完成。\x02\x03",

            "如果在这里展开无谓的冲突，\x01",
            "未免有些不解风情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x12,
        (
            "#12P#03209F呵呵，同感。\x02\x03",

            "#03205F对了，\x01",
            "祝贺『诺艾·布朗』\x01",
            "装修完毕，重新开张哦。\x02\x03",

            "#03204F没有过去问候一声，\x01",
            "真是失礼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "#5P#04504F哪里，是我们失礼才对。\x02\x03",

            "#04500F又不是不认识，却一直没有去\x01",
            "拜访你们，真是不好意思。\x02\x03",

            "#04502F说起来……\x01",
            "那些老不死的家伙还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x12,
        (
            "#12P#03204F哈哈，全都好得很，\x01",
            "健康得简直令人心烦。\x02\x03",

            "#03210F托你们的福，\x01",
            "有些老人直到现在\x01",
            "还会做噩梦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        (
            "#5P#04609F啊哈哈，是因为我们曾经\x01",
            "袭击长老会，还抓走了人质吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00700F……哼，我当时因为委托而不在场，\x01",
            "似乎很幸运呢。\x07\x00\x02",
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
            "#5P#04605F啊啊！\x01",
            "你莫非就是『银』吗！？\x02\x03",

            "#04602F人称东方人街最强的\x01",
            "传说中的刺客！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00702F……看来你就是\x01",
            "『血腥谢莉』啊。\x02\x03",

            "听说你年仅十六岁，\x01",
            "就担任最强猎兵团的大队长。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        (
            "#5P#04606F嗯，但我还是觉得\x01",
            "独自行动更加自在～\x02\x03",

            "#04611F话说回来……\x02\x03",

            "你的面罩虽然很帅，\x01",
            "但还是不戴那个的时候更厉害吧？\x02",
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
            "#12P#00705F#30W什么……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        (
            "#5P#04606F你的肌肉似乎不太自然。\x02\x03",

            "#04600F在正常状态下应该会更强，\x01",
            "现在这样子未免太可惜了吧～？\x02",
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
        "#11P#03205F哦……？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        (
            "#5P#04504F呵呵，我比较溺爱孩子，或许会\x01",
            "有点自夸，但她的眼光确实很准。\x02\x03",

            "#04500F如果她说的话令你感到不快，\x01",
            "我愿意代为道歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00702F……不必介意。\x02\x03",

            "#00700F曹，如果你还要继续说些\x01",
            "无聊的场面话，我就先走一步了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x12,
        "#11P#03204F哈哈，抱歉抱歉。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xA, 500)
    Sleep(300)

    #C0053
    ChrTalk(
        0x12,
        "#12P#03202F那我们这就告辞了，期待下次见面。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        "#5P#04502F嗯，期待下次见面。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        "#5P#04612F呵呵，再见啦～！\x02",
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
    SubItemNumber('ＩＢＣ认证卡片', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｃ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｒ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｍ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｓ', 1)
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

    # Function_7_160C end

    def Function_8_277A(): pass

    label("Function_8_277A")

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

    # Function_8_277A end

    def Function_9_27B7(): pass

    label("Function_9_27B7")

    OP_97(0xFE, 0x1388, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_9_27B7 end

    def Function_10_27E0(): pass

    label("Function_10_27E0")

    OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_97(0xFE, 0x1388, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_10_27E0 end

    def Function_11_281D(): pass

    label("Function_11_281D")

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

    # Function_11_281D end

    def Function_12_285A(): pass

    label("Function_12_285A")

    OP_97(0xFE, 0xFFFFF34E, 0x0, 0xFFFFF5D8, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_12_285A end

    def Function_13_2883(): pass

    label("Function_13_2883")

    OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFFF34E, 0x0, 0xFFFFF5D8, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_2883 end

    def Function_14_28C0(): pass

    label("Function_14_28C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C06")
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
            "#00005F这里好像是……\x01",
            "通往兰花塔\x01",
            "底层的大门。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#00203F也就是我们在通商会议中\x01",
            "追捕恐怖分子时经过的区域呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x105,
        (
            "#10306F嗯，但现在好像已经\x01",
            "完全封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x109,
        (
            "#10103F我们当时就是在\x01",
            "这里和亚里欧斯先生他们\x01",
            "分开行动的。\x02\x03",

            "#10108F在那之后……\x02",
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
            "#10106F对、对不起，\x01",
            "我好像提起了\x01",
            "一段不太愉快的回忆。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        "#00304F……哈哈，不必介意。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#00103F#4P总之，这边并没有\x01",
            "通往地上的升降机。\x02\x03",

            "#00100FＤ区域也被封锁了，\x01",
            "我们还是返回Ｃ区域吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00000F嗯，走吧。\x02",
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
    Jump("loc_2C67")

    label("loc_2C06")

    TalkBegin(0xFF)

    #C0064
    ChrTalk(
        0x101,
        (
            "#00000F这是通往兰花塔\x01",
            "底层的大门。\x02\x03",

            "现在已经被封锁了，\x01",
            "我们还是回Ｃ区域乘坐升降机吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2C67")

    Return()

    label("loc_2C68")

    TalkBegin(0xFF)

    #C0065
    ChrTalk(
        0x101,
        (
            "#00000F这是通往兰花塔\x01",
            "底层的大门，\x01",
            "现在已经被封锁了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_14_28C0 end

    def Function_15_2CAA(): pass

    label("Function_15_2CAA")

    EventBegin(0x1)

    #C0066
    ChrTalk(
        0x101,
        (
            "#00003F这是通往Ｄ区域的大门。\x02\x03",

            "……我们还是返回Ｃ区域，\x01",
            "乘坐通往地上的升降机吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24210, -8000, 3000, 180)
    EventEnd(0x4)
    Return()

    # Function_15_2CAA end

    def Function_16_2D17(): pass

    label("Function_16_2D17")

    EventBegin(0x1)

    #C0067
    ChrTalk(
        0x101,
        (
            "#00003F没时间回头了，\x01",
            "赶快前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -390, 0, 6230, 180)
    EventEnd(0x4)
    Return()

    # Function_16_2D17 end

    def Function_17_2D56(): pass

    label("Function_17_2D56")

    EventBegin(0x1)

    #C0068
    ChrTalk(
        0x101,
        (
            "#00001FＣ区域就交给\x01",
            "达德利警官和亚里欧斯先生吧。\x02\x03",

            "我们赶快去追捕逃向Ｄ区域的\x01",
            "帝国恐怖分子！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19030, 4000, -19240, 270)
    EventEnd(0x4)
    Return()

    # Function_17_2D56 end

    SaveToFile()

Try(main)
