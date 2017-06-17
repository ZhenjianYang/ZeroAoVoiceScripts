from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1310_1.bin",                # FileName
        "t1310",                    # MapName
        "t1310",                    # Location
        0x00BD,                     # MapIndex
        "ed7161",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [440, 441, 705, 859, 1008, 1065, 1191, 1425, 1497, 0, 1547, 0, 3336, 3487, 3544, 3701, 0, 3758, 0, 44, 15, 0, 0],
    )

    BuildStringList((
        "t1310_1",                # 0
    ))

    ChipFrameInfo(440, 0)                                        # 0

    ScpFunction((
        "Function_0_1B8",          # 00, 0
        "Function_1_1B9",          # 01, 1
        "Function_2_2C1",          # 02, 2
        "Function_3_35B",          # 03, 3
        "Function_4_3F0",          # 04, 4
        "Function_5_429",          # 05, 5
        "Function_6_4A7",          # 06, 6
        "Function_7_591",          # 07, 7
        "Function_8_5D9",          # 08, 8
        "Function_9_60B",          # 09, 9
        "Function_10_D08",         # 0A, 10
        "Function_11_D9F",         # 0B, 11
        "Function_12_DD8",         # 0C, 12
        "Function_13_E75",         # 0D, 13
        "Function_14_EAE",         # 0E, 14
        "Function_15_F2C",         # 0F, 15
        "Function_16_FC8",         # 10, 16
        "Function_17_103D",        # 11, 17
        "Function_18_108E",        # 12, 18
        "Function_19_1164",        # 13, 19
        "Function_20_11EC",        # 14, 20
        "Function_21_126B",        # 15, 21
        "Function_22_1356",        # 16, 22
        "Function_23_139E",        # 17, 23
        "Function_24_13DC",        # 18, 24
        "Function_25_1CBF",        # 19, 25
        "Function_26_1D56",        # 1A, 26
        "Function_27_1D8F",        # 1B, 27
        "Function_28_1E3A",        # 1C, 28
        "Function_29_1ED5",        # 1D, 29
        "Function_30_1F0E",        # 1E, 30
        "Function_31_1FB0",        # 1F, 31
        "Function_32_1FB1",        # 20, 32
        "Function_33_2018",        # 21, 33
        "Function_34_20AE",        # 22, 34
        "Function_35_2101",        # 23, 35
        "Function_36_216D",        # 24, 36
        "Function_37_2188",        # 25, 37
        "Function_38_21E4",        # 26, 38
        "Function_39_2216",        # 27, 39
        "Function_40_22B1",        # 28, 40
        "Function_41_2336",        # 29, 41
        "Function_42_2361",        # 2A, 42
        "Function_43_2389",        # 2B, 43
        "Function_44_2436",        # 2C, 44
        "Function_45_2493",        # 2D, 45
        "Function_46_251F",        # 2E, 46
        "Function_47_2606",        # 2F, 47
        "Function_48_264E",        # 30, 48
        "Function_49_2692",        # 31, 49
        "Function_50_30D1",        # 32, 50
        "Function_51_3169",        # 33, 51
        "Function_52_31A2",        # 34, 52
        "Function_53_3224",        # 35, 53
        "Function_54_32B8",        # 36, 54
        "Function_55_32F1",        # 37, 55
        "Function_56_3359",        # 38, 56
        "Function_57_33F4",        # 39, 57
        "Function_58_342D",        # 3A, 58
        "Function_59_34AF",        # 3B, 59
        "Function_60_354D",        # 3C, 60
        "Function_61_360A",        # 3D, 61
        "Function_62_3676",        # 3E, 62
        "Function_63_3771",        # 3F, 63
        "Function_64_37CD",        # 40, 64
        "Function_65_380B",        # 41, 65
        "Function_66_3853",        # 42, 66
        "Function_67_38EA",        # 43, 67
        "Function_68_3928",        # 44, 68
        "Function_69_39AD",        # 45, 69
        "Function_70_4258",        # 46, 70
        "Function_71_42F0",        # 47, 71
        "Function_72_4329",        # 48, 72
        "Function_73_43B7",        # 49, 73
        "Function_74_4451",        # 4A, 74
        "Function_75_4484",        # 4B, 75
        "Function_76_44D0",        # 4C, 76
        "Function_77_4538",        # 4D, 77
        "Function_78_4571",        # 4E, 78
        "Function_79_4641",        # 4F, 79
        "Function_80_46E1",        # 50, 80
        "Function_81_4736",        # 51, 81
        "Function_82_47BB",        # 52, 82
        "Function_83_48B0",        # 53, 83
        "Function_84_48E2",        # 54, 84
        "Function_85_4914",        # 55, 85
        "Function_86_4979",        # 56, 86
        "Function_87_49EB",        # 57, 87
        "Function_88_4A8E",        # 58, 88
    ))


    def Function_0_1B8(): pass

    label("Function_0_1B8")

    Return()

    # Function_0_1B8 end

    def Function_1_1B9(): pass

    label("Function_1_1B9")

    Call(1, 0)
    SetChrPos(0x11, 24500, -6000, -19000, 0)
    SetChrPos(0x12, 27500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -13000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrPos(0x14, 27500, -4000, -16000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(330, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(26000, -5000, -16000, 8000)
    MoveCamera(295, 30, 0, 8000)
    OP_6E(650, 8000)
    SetCameraDistance(17000, 8000)
    FadeToBright(1000, 0)
    BeginChrThread(0x12, 3, 1, 2)

    label("loc_2A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD")
    Sleep(1)
    Jump("loc_2A6")

    label("loc_2BD")

    OP_6F(0x79)
    OP_0D()
    Return()

    # Function_1_1B9 end

    def Function_2_2C1(): pass

    label("Function_2_2C1")


    def lambda_2C6():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEC78, 0xFFFFB6F4, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2C6)
    SetChrFlags(0xFE, 0x20)

    def lambda_2E8():

        label("loc_2E8")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_2E8")

    QueueWorkItem2(0xFE, 2, lambda_2E8)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0001
    ChrTalk(
        0x12,
        "#6P#7A──先輩！\x02",
    )
    #Auto


    def lambda_328():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFBBA4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_328)
    BeginChrThread(0x11, 3, 1, 3)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_2_2C1 end

    def Function_3_35B(): pass

    label("Function_3_35B")

    Sleep(500)
    Sound(809, 0, 100, 0)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_376():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_376)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    Sound(442, 0, 90, 0)

    #C0002
    ChrTalk(
        0x11,
        "#5P#5Aおらっ！\x02",
    )
    #Auto


    def lambda_3B3():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3B3)
    BeginChrThread(0x10, 3, 1, 4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_3_35B end

    def Function_4_3F0(): pass

    label("Function_4_3F0")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_403():
        OP_9D(0xFE, 0x6A40, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_403)
    BeginChrThread(0x13, 3, 1, 5)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_4_3F0 end

    def Function_5_429(): pass

    label("Function_5_429")

    SetChrFlags(0xFE, 0x20)

    def lambda_433():

        label("loc_433")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_433")

    QueueWorkItem2(0xFE, 2, lambda_433)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    #C0003
    ChrTalk(
        0x13,
        "#12P#6Aヨロシク！\x02",
    )
    #Auto


    def lambda_474():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFC694, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_474)
    BeginChrThread(0x10, 3, 1, 6)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_5_429 end

    def Function_6_4A7(): pass

    label("Function_6_4A7")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_4C2():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C2)
    Sleep(600)

    #C0004
    ChrTalk(
        0x10,
        "#11P#4S#5Aやぁッ！！#3S\x02",
    )
    #Auto

    SetChrSubChip(0xFE, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    BeginChrThread(0x14, 3, 1, 7)
    BeginChrThread(0x11, 3, 1, 8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x11, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_4A7 end

    def Function_7_591(): pass

    label("Function_7_591")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x5AD2, 0xFFFFE890, 0xFFFFADF8, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54F6, 0xFFFFE890, 0xFFFF8FBC, 0x3E8, 0x7D0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_7_591 end

    def Function_8_5D9(): pass

    label("Function_8_5D9")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_5D9 end

    def Function_9_60B(): pass

    label("Function_9_60B")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x11, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -10000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrPos(0x10, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 24500, -5500, -10200, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 12000)
    MoveCamera(305, 30, 0, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 3, 1, 10)

    label("loc_703")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71A")
    Sleep(1)
    Jump("loc_703")

    label("loc_71A")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "このまま直接アタックを決める\x01",      # 0
            "トスしてランディに打たせる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3B")
    MoveCamera(315, 25, 0, 1500)
    SetCameraDistance(15000, 1500)
    BeginChrThread(0x101, 3, 1, 18)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0005
    ChrTalk(
        0x10,
        "#13400F#5P#Nはい、アウト～ッ！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0006
    ChrTalk(
        0x101,
        "#12506F#6Pしまった、焦りすぎたか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x13, 0xE1, 0x1F4)

    #C0007
    ChrTalk(
        0x13,
        "#12902Fフフ、サンクス。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x12,
        "#13006F#5P#N危なかった～……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0009
    ChrTalk(
        0x101,
        "#12500F悪い、ランディ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    #C0010
    ChrTalk(
        0x11,
        (
            "#12800F#12Pドンマイドンマイ！\x01",
            "こっから巻き返してこうぜ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x11, 27500, -6000, -20000, 0)
    SetChrPos(0x13, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0011
    ChrTalk(
        0x10,
        (
            "#13400F#5P……ゲームセット！！\x02\x03",

            "#13409F７－１２で、\x01",
            "ワジ君チームの勝ち～！\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#12506F#6Pはあ、負けちゃったか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CFC")

    label("loc_A3B")

    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 20)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0013
    ChrTalk(
        0x10,
        "#13405F#5P#Nおおっ、やるわねランディ君！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)

    #C0014
    ChrTalk(
        0x12,
        "#13002F#11P#Nくっ……お見事です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0015
    ChrTalk(
        0x13,
        (
            "#12906F#11Pやれやれ、この身長差は\x01",
            "さすがにツラいものがあるね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    #C0016
    ChrTalk(
        0x11,
        (
            "#12809F#12Pナイストスだぜ、ロイド。\x01",
            "さすがの判断力っつぅか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0017
    ChrTalk(
        0x101,
        (
            "#12509F#5Pはは、先走るところだったけどね。\x02\x03",

            "#12500Fよし、このまま畳み掛けるぞ！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x11, 27500, -6000, -20000, 0)
    SetChrPos(0x13, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0018
    ChrTalk(
        0x10,
        (
            "#13400F#5P……ゲームセット！！\x02\x03",

            "#13409F１２－８で、弟君チームの勝ち～！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#12500F#6Pよし、勝ったぞ！！\x02",
    )

    CloseMessageWindow()

    label("loc_CFC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_9_60B end

    def Function_10_D08(): pass

    label("Function_10_D08")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_D18():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D18)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    #C0020
    ChrTalk(
        0x12,
        "#11P#5Aはあっ！\x02",
    )
    #Auto


    def lambda_D5E():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D5E)
    BeginChrThread(0x101, 3, 1, 11)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_D08 end

    def Function_11_D9F(): pass

    label("Function_11_D9F")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_DB2():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEE6C, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DB2)
    BeginChrThread(0x11, 3, 1, 12)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_11_D9F end

    def Function_12_DD8(): pass

    label("Function_12_DD8")

    SetChrFlags(0xFE, 0x20)

    def lambda_DE2():

        label("loc_DE2")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_DE2")

    QueueWorkItem2(0xFE, 2, lambda_DE2)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0021
    ChrTalk(
        0x11,
        "#6P#6Aよっと！\x02",
    )
    #Auto


    def lambda_E20():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E20)
    BeginChrThread(0x13, 3, 1, 13)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_DD8 end

    def Function_13_E75(): pass

    label("Function_13_E75")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_E88():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E88)
    BeginChrThread(0x12, 3, 1, 14)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_E75 end

    def Function_14_EAE(): pass

    label("Function_14_EAE")

    SetChrFlags(0xFE, 0x20)

    def lambda_EB8():

        label("loc_EB8")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_EB8")

    QueueWorkItem2(0xFE, 2, lambda_EB8)
    Sleep(350)

    #C0022
    ChrTalk(
        0x12,
        "#11P#8Aワジ君っ！\x02",
    )
    #Auto

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_EF9():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_EF9)
    BeginChrThread(0x13, 3, 1, 15)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_EAE end

    def Function_15_F2C(): pass

    label("Function_15_F2C")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)

    #C0023
    ChrTalk(
        0x13,
        "#11P#5Aふっ……！\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_F5D():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F5D)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_F85():
        OP_98(0xFE, 0x0, 0xFFFFFCE0, 0xFFFFF830, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F85)
    BeginChrThread(0x11, 3, 1, 16)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sound(442, 0, 80, 0)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_15_F2C end

    def Function_16_FC8(): pass

    label("Function_16_FC8")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_FE0():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FE0)
    WaitChrThread(0x14, 1)

    def lambda_1001():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCD38, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1001)
    BeginChrThread(0x12, 3, 1, 17)
    Sound(441, 0, 80, 0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_16_FC8 end

    def Function_17_103D(): pass

    label("Function_17_103D")

    WaitChrThread(0x14, 1)
    SetChrFlags(0xFE, 0x20)
    OP_93(0xFE, 0xB4, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1061():
        OP_9D(0xFE, 0x5FB4, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1061)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_103D end

    def Function_18_108E(): pass

    label("Function_18_108E")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_10A6():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBBA4, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10A6)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0024
    ChrTalk(
        0x101,
        "#5P#6A#4Sはあっ！！#3S\x02",
    )
    #Auto

    BeginChrThread(0x14, 3, 1, 19)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    Return()

    # Function_18_108E end

    def Function_19_1164(): pass

    label("Function_19_1164")

    SetChrFlags(0x13, 0x20)

    def lambda_116E():

        label("loc_116E")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_116E")

    QueueWorkItem2(0x13, 2, lambda_116E)
    SetChrFlags(0x12, 0x20)

    def lambda_1185():

        label("loc_1185")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1185")

    QueueWorkItem2(0x12, 2, lambda_1185)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x68F6, 0xFFFFE890, 0xFFFFDDBE, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x7A76, 0xFFFFE868, 0x1B58, 0x9C4, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    EndChrThread(0x13, 0x2)
    ClearChrFlags(0x13, 0x20)
    EndChrThread(0x12, 0x2)
    ClearChrFlags(0x12, 0x20)
    Return()

    # Function_19_1164 end

    def Function_20_11EC(): pass

    label("Function_20_11EC")

    SetChrFlags(0xFE, 0x20)

    def lambda_11F6():

        label("loc_11F6")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_11F6")

    QueueWorkItem2(0xFE, 2, lambda_11F6)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    #C0025
    ChrTalk(
        0x101,
        "#5P#5A頼むっ！\x02",
    )
    #Auto


    def lambda_1234():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBF8C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1234)
    BeginChrThread(0x11, 3, 1, 21)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x11, 3)
    Return()

    # Function_20_11EC end

    def Function_21_126B(): pass

    label("Function_21_126B")

    Sleep(600)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_1286():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1286)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0026
    ChrTalk(
        0x11,
        "#5P#10A#4Sおらああああっ！！#3S\x02",
    )
    #Auto
    Sleep(600)

    BeginChrThread(0x14, 3, 1, 22)
    BeginChrThread(0x13, 3, 1, 23)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x13, 3)
    Return()

    # Function_21_126B end

    def Function_22_1356(): pass

    label("Function_22_1356")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6F9A, 0xFFFFE890, 0xFFFFCCCA, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x7F76, 0xFFFFE7F0, 0x762, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_22_1356 end

    def Function_23_139E(): pass

    label("Function_23_139E")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_23_139E end

    def Function_24_13DC(): pass

    label("Function_24_13DC")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -10000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrPos(0x11, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 24500, -5500, -10200, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 13000)
    MoveCamera(305, 30, 0, 13000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 3, 1, 25)

    label("loc_14D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14EB")
    Sleep(1)
    Jump("loc_14D4")

    label("loc_14EB")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "強打を読んでブロックに参加する\x01",      # 0
            "裏を読んで後ろに下がる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18ED")
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x13, 3, 1, 39)
    WaitChrThread(0x13, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0027
    ChrTalk(
        0x11,
        (
            "#12809F#5P#Nイリアさんチーム、得点ッス！\x02\x03",

            "#12803Fしかし、流石はワジ……\x01",
            "狡#2Rこす#いマネをしやがるぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x13, 0x10E, 0x1F4)

    #C0028
    ChrTalk(
        0x13,
        (
            "#12902F#12Pフフ、人聞きが悪いなあ。\x01",
            "これも戦略の一つだよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x87, 0x1F4)

    #C0029
    ChrTalk(
        0x10,
        (
            "#13404F#5Pまあ、真面目クンチーム相手だと\x01",
            "この上なくいい戦略かもね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x12, 0x5A, 0x1F4)

    #C0030
    ChrTalk(
        0x12,
        (
            "#13001F#5Pロ、ロイドさん……\x01",
            "あんなこと言われてますよ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0031
    ChrTalk(
        0x101,
        (
            "#12510F#12Pくっ……ま、負けてたまるか！\x02\x03",

            "#12501Fこうなったら根性だ、ノエル！\x01",
            "何が何でもボールに食らいつくぞ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -13000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0032
    ChrTalk(
        0x11,
        (
            "#12800F#5P……ゲームセット！！\x02\x03",

            "#12809F３－１２で、\x01",
            "イリアさんチームの勝ちッス！！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#12506F#6Pくうっ……ダメだったか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CB3")

    label("loc_18ED")

    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x13, 3, 1, 43)
    WaitChrThread(0x13, 3)
    Sleep(600)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0034
    ChrTalk(
        0x11,
        (
            "#12800F#5P#Nロイドチーム、得点！\x02\x03",

            "#12809Fははっ、やるじゃねえか！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)

    #C0035
    ChrTalk(
        0x13,
        (
            "#12906F#11Pやれやれ、まさか読まれるとはね。\x02\x03",

            "#12902F真面目クンチームのくせに、\x01",
            "なかなかやってくれるじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#12502F#6Pワジの性格だと、あの場面なら\x01",
            "きっと裏をかくと思ってね。\x02\x03",

            "#12504F正攻法とは逆をとったまでさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0x5A, 0x1F4)

    #C0037
    ChrTalk(
        0x12,
        "#13000F#5Pやりましたね、ロイドさん！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x5A, 0x1F4)

    #C0038
    ChrTalk(
        0x10,
        (
            "#13400F#5Pフフ、どうやら\x01",
            "侮りすぎてたんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x13,
        "#12904Fハハ、そうかもしれないね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0040
    ChrTalk(
        0x101,
        (
            "#12500F#12Pよし、ノエル！\x01",
            "このままゲームの流れを\x01",
            "こっちのものにするぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x12,
        "#13009F#5Pええ、了解です！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 27500, -6000, -19000, 0)
    SetChrPos(0x12, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 24500, -6000, -13000, 180)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0042
    ChrTalk(
        0x11,
        (
            "#12800F#5P……ゲームセット！！\x02\x03",

            "#12809F１２－１１で、\x01",
            "ロイドチームの勝ち！！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#12512F#6Pや、やった……ギリギリ勝てたぞ！\x02",
    )

    CloseMessageWindow()

    label("loc_1CB3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_24_13DC end

    def Function_25_1CBF(): pass

    label("Function_25_1CBF")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_1CCF():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1CCF)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0044
    ChrTalk(
        0x10,
        "#11P#5Aほいっ！\x02",
    )
    #Auto


    def lambda_1D15():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D15)
    BeginChrThread(0x12, 3, 1, 26)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_1CBF end

    def Function_26_1D56(): pass

    label("Function_26_1D56")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1D69():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEDA4, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D69)
    BeginChrThread(0x101, 3, 1, 27)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_1D56 end

    def Function_27_1D8F(): pass

    label("Function_27_1D8F")

    SetChrFlags(0xFE, 0x20)

    def lambda_1D99():

        label("loc_1D99")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1D99")

    QueueWorkItem2(0xFE, 2, lambda_1D99)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    #C0045
    ChrTalk(
        0x101,
        "#6P#5Aノエルッ！\x02",
    )
    #Auto


    def lambda_1DD9():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1DD9)
    BeginChrThread(0x12, 3, 1, 28)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_1D8F end

    def Function_28_1E3A(): pass

    label("Function_28_1E3A")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_1E55():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E55)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    #C0046
    ChrTalk(
        0x12,
        "#5P#5Aはあっ！！\x02",
    )
    #Auto


    def lambda_1E98():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1E98)
    BeginChrThread(0x13, 3, 1, 29)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_28_1E3A end

    def Function_29_1ED5(): pass

    label("Function_29_1ED5")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1EE8():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xC80, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1EE8)
    BeginChrThread(0x10, 3, 1, 30)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_1ED5 end

    def Function_30_1F0E(): pass

    label("Function_30_1F0E")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    #C0047
    ChrTalk(
        0x10,
        "#11P#5Aとりゃっ！\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_1F3F():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F3F)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    def lambda_1F6D():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB30C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1F6D)
    BeginChrThread(0x12, 3, 1, 31)
    BeginChrThread(0x101, 3, 1, 32)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_30_1F0E end

    def Function_31_1FB0(): pass

    label("Function_31_1FB0")

    Return()

    # Function_31_1FB0 end

    def Function_32_1FB1(): pass

    label("Function_32_1FB1")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_1FC4():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFBD98, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1FC4)
    BeginChrThread(0x12, 3, 1, 33)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_1FB1 end

    def Function_33_2018(): pass

    label("Function_33_2018")

    SetChrFlags(0xFE, 0x20)

    def lambda_2022():

        label("loc_2022")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_2022")

    QueueWorkItem2(0xFE, 2, lambda_2022)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_204D():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_204D)
    BeginChrThread(0x13, 3, 1, 34)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1700)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_98(0xFE, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_2018 end

    def Function_34_20AE(): pass

    label("Function_34_20AE")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    #C0048
    ChrTalk(
        0x13,
        "#12P#5A行くよっ……！\x02",
    )
    #Auto


    def lambda_20DB():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_20DB)
    BeginChrThread(0x10, 3, 1, 35)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_20AE end

    def Function_35_2101(): pass

    label("Function_35_2101")

    SetChrFlags(0xFE, 0x20)

    def lambda_210B():

        label("loc_210B")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_210B")

    QueueWorkItem2(0xFE, 2, lambda_210B)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_2136():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2136)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_2101 end

    def Function_36_216D(): pass

    label("Function_36_216D")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_216D end

    def Function_37_2188(): pass

    label("Function_37_2188")

    BeginChrThread(0x10, 3, 1, 36)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_2188 end

    def Function_38_21E4(): pass

    label("Function_38_21E4")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_21E4 end

    def Function_39_2216(): pass

    label("Function_39_2216")

    BeginChrThread(0x101, 3, 1, 37)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_2234():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2234)
    Sleep(600)

    #C0049
    ChrTalk(
        0x13,
        "#12P#5A──なんてね♪\x02",
    )
    #Auto

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    BeginChrThread(0x14, 3, 1, 40)
    BeginChrThread(0x12, 3, 1, 38)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(441, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x12, 3)
    Return()

    # Function_39_2216 end

    def Function_40_22B1(): pass

    label("Function_40_22B1")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFAC04, 0x7D0, 0x3E8)
    Sound(443, 0, 40, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFA628, 0x3E8, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFA240, 0x1F4, 0x3E8)
    Sound(441, 0, 40, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFA04C, 0xC8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_40_22B1 end

    def Function_41_2336(): pass

    label("Function_41_2336")

    BeginChrThread(0x10, 3, 1, 36)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFF830, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_2336 end

    def Function_42_2361(): pass

    label("Function_42_2361")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_2361 end

    def Function_43_2389(): pass

    label("Function_43_2389")

    BeginChrThread(0x101, 3, 1, 41)
    BeginChrThread(0x12, 3, 1, 42)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_23AD():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23AD)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    #C0050
    ChrTalk(
        0x13,
        "#12P#5Aっと……！？\x02",
    )
    #Auto


    def lambda_23ED():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB118, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_23ED)
    BeginChrThread(0x101, 3, 1, 44)
    Sleep(100)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(5500)
    Return()

    # Function_43_2389 end

    def Function_44_2436(): pass

    label("Function_44_2436")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_2449():
        OP_9D(0xFE, 0x6590, 0xFFFFEC78, 0xFFFFB9B0, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2449)
    BeginChrThread(0x12, 3, 1, 45)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_2436 end

    def Function_45_2493(): pass

    label("Function_45_2493")

    SetChrFlags(0xFE, 0x20)

    def lambda_249D():

        label("loc_249D")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_249D")

    QueueWorkItem2(0xFE, 2, lambda_249D)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_24C8():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_24C8)
    BeginChrThread(0x101, 3, 1, 46)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_98(0x10, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_45_2493 end

    def Function_46_251F(): pass

    label("Function_46_251F")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    #C0051
    ChrTalk(
        0x101,
        "#5P#5A#4Sうおおおおっ！#3S\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_2559():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2559)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 1, 47)
    BeginChrThread(0x13, 3, 1, 48)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x13, 3)
    Return()

    # Function_46_251F end

    def Function_47_2606(): pass

    label("Function_47_2606")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6658, 0xFFFFE890, 0xFFFFCE5A, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x774C, 0xFFFFE890, 0xFFFFFA9C, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_47_2606 end

    def Function_48_264E(): pass

    label("Function_48_264E")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    Sound(441, 0, 80, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_48_264E end

    def Function_49_2692(): pass

    label("Function_49_2692")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x13, 27500, -6000, -22000, 0)
    SetChrPos(0x11, 24500, -6000, -13000, 180)
    SetChrPos(0x10, 27500, -6000, -13000, 180)
    SetChrPos(0x12, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 27500, -5500, -21800, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 15000)
    MoveCamera(305, 30, 0, 15000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 3, 1, 50)

    label("loc_278A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A1")
    Sleep(1)
    Jump("loc_278A")

    label("loc_27A1")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "イリアたちの間を狙って強打\x01",      # 0
            "ライン際へ山なりに落とす\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC2")
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 62)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0052
    ChrTalk(
        0x12,
        "#13002F#5P#Nイリアさんチーム、ポイントです！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x11, 0x5A, 0x1F4)

    #C0053
    ChrTalk(
        0x11,
        (
            "#12809F#5Pよっしゃあ！！\x01",
            "さすがッス、イリアさん！！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x10E, 0x1F4)

    #C0054
    ChrTalk(
        0x10,
        "#13400F#12Pあはは、こんなもんかしら。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x13,
        (
            "#12906F#12P#Nやれやれ。\x01",
            "正面から行って、あのチームの\x01",
            "身体能力に勝てると思ったのかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_296B():
        OP_93(0x11, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_296B)
    Sleep(30)

    def lambda_297B():
        OP_93(0x10, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_297B)
    Sleep(30)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x10, 0)
    OP_93(0x101, 0x87, 0x1F4)

    #C0056
    ChrTalk(
        0x101,
        (
            "#12506F#5Pいや、面目ない……\x02\x03",

            "#12505F……それにしてもワジ。\x01",
            "さっきの“ライ”っていうのは\x01",
            "どういう意味があったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x13,
        (
            "#12900F#12P#Nいや、イリアさんが\x01",
            "ブロックに来るだろうから、\x01",
            "強打しても無駄だと思ってね。\x02\x03",

            "#12904F“ライ”はライン……\x01",
            "要するに、山なりに打って\x01",
            "ライン際に落とせってことさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x101,
        (
            "#12506F#5Pあのな……いきなり言われて\x01",
            "分かるわけないだろ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x13,
        (
            "#12909F#12P#Nあはは、ゴメンゴメン。\x02\x03",

            "#12900Fま、気を取り直して\x01",
            "なんとか逆転しようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x13, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x10, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0060
    ChrTalk(
        0x12,
        (
            "#13000F#5P……ゲームセット！！\x02\x03",

            "#13009F４－１２で、\x01",
            "イリアさんチームの勝ちです！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#12506F#6Pふう、完敗だなあ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C5")

    label("loc_2CC2")

    OP_2C(0xA5, 0x1)
    BeginChrThread(0x101, 3, 1, 66)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0062
    ChrTalk(
        0x12,
        "#13002F#5P#Nロイドさんチーム、ポイントです！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)

    #C0063
    ChrTalk(
        0x101,
        "#12500F#6Pよしっ……！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x10,
        (
            "#13406F#11Pあっちゃ～……フェイントかあ。\x01",
            "てっきり強打で来るのかと思ったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x11,
        "#12806F#11Pいや～、裏をかかれたッスね。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x13,
        "#12902F#6P#Nフフ、上出来じゃない。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    #C0067
    ChrTalk(
        0x101,
        (
            "#12504F#11P……ああ、ワジが\x01",
            "“ライ”って合図をくれたからさ。\x02\x03",

            "#12502Fライン際が空いてるのに気づいて、\x01",
            "とっさに切り替えたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x13,
        (
            "#12904F#6P#Nフフ、突然だったから通じるものか\x01",
            "若干不安だったんだけど。\x02\x03",

            "#12909Fこれも愛の為せるワザってやつかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0069
    ChrTalk(
        0x101,
        (
            "#12506F#11Pバカ言ってるなって。\x02\x03",

            "#12500Fよし、この調子で搦め手を混ぜつつ、\x01",
            "イリアさんたちを翻弄していくぞ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x13, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x10, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0070
    ChrTalk(
        0x12,
        (
            "#13000F#5P……ゲームセット！！\x02\x03",

            "#13009F１２－１０で、\x01",
            "ロイドさんチームの勝ちです！！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#12509F#6Pよし、なんとか勝ったぞ！！\x02",
    )

    CloseMessageWindow()

    label("loc_30C5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_49_2692 end

    def Function_50_30D1(): pass

    label("Function_50_30D1")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_30E1():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_30E1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0072
    ChrTalk(
        0x13,
        "#6P#5Aふっ……！\x02",
    )
    #Auto


    def lambda_3128():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3128)
    BeginChrThread(0x10, 3, 1, 51)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_30D1 end

    def Function_51_3169(): pass

    label("Function_51_3169")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_317C():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEDA4, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_317C)
    BeginChrThread(0x11, 3, 1, 52)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_51_3169 end

    def Function_52_31A2(): pass

    label("Function_52_31A2")

    SetChrFlags(0xFE, 0x20)

    def lambda_31AC():

        label("loc_31AC")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_31AC")

    QueueWorkItem2(0xFE, 2, lambda_31AC)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_31D7():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31D7)
    BeginChrThread(0x10, 3, 1, 53)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_31A2 end

    def Function_53_3224(): pass

    label("Function_53_3224")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_323F():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_323F)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    Sound(442, 0, 80, 0)
    EndChrThread(0x14, 0x1)

    #C0073
    ChrTalk(
        0x10,
        "#11P#5Aはいっ！\x02",
    )
    #Auto


    def lambda_3281():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3281)
    BeginChrThread(0x101, 3, 1, 54)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_53_3224 end

    def Function_54_32B8(): pass

    label("Function_54_32B8")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_32CB():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32CB)
    BeginChrThread(0x13, 3, 1, 55)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_54_32B8 end

    def Function_55_32F1(): pass

    label("Function_55_32F1")

    SetChrFlags(0xFE, 0x20)

    def lambda_32FB():

        label("loc_32FB")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_32FB")

    QueueWorkItem2(0xFE, 2, lambda_32FB)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_3326():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3326)
    BeginChrThread(0x101, 3, 1, 56)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_55_32F1 end

    def Function_56_3359(): pass

    label("Function_56_3359")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3374():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3374)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    #C0074
    ChrTalk(
        0x101,
        "#5P#5Aお返しだっ……！\x02",
    )
    #Auto


    def lambda_33BD():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33BD)
    BeginChrThread(0x11, 3, 1, 57)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_3359 end

    def Function_57_33F4(): pass

    label("Function_57_33F4")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_3407():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3407)
    BeginChrThread(0x10, 3, 1, 58)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_57_33F4 end

    def Function_58_342D(): pass

    label("Function_58_342D")

    SetChrFlags(0xFE, 0x20)

    def lambda_3437():

        label("loc_3437")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3437")

    QueueWorkItem2(0xFE, 2, lambda_3437)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_3462():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3462)
    BeginChrThread(0x11, 3, 1, 59)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_58_342D end

    def Function_59_34AF(): pass

    label("Function_59_34AF")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_34CA():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34CA)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    #C0075
    ChrTalk(
        0x11,
        "#11P#5A食らいなっ！\x02",
    )
    #Auto


    def lambda_350A():
        OP_96(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFBF8C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_350A)
    BeginChrThread(0x101, 3, 1, 60)
    Sleep(100)
    Sound(442, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_59_34AF end

    def Function_60_354D(): pass

    label("Function_60_354D")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_3565():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3565)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)

    def lambda_358C():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_358C)
    BeginChrThread(0x13, 3, 1, 61)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)

    #C0076
    ChrTalk(
        0x13,
        "#6P#5Aライッ！\x02",
    )
    #Auto

    Sleep(500)
    SetChrFlags(0x10, 0x20)
    OP_93(0x10, 0xB4, 0x1F4)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_98(0x10, 0xFFFFFA24, 0x0, 0x0, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_60_354D end

    def Function_61_360A(): pass

    label("Function_61_360A")

    SetChrFlags(0xFE, 0x20)

    def lambda_3614():

        label("loc_3614")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3614")

    QueueWorkItem2(0xFE, 2, lambda_3614)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_363F():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBF8C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_363F)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_61_360A end

    def Function_62_3676(): pass

    label("Function_62_3676")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_368E():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_368E)
    Sleep(600)

    #C0077
    ChrTalk(
        0x101,
        "#5P#5A#4S……はあっ！#3S\x02",
    )
    #Auto

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3727():
        OP_96(0xFE, 0x6590, 0xFFFFF060, 0xFFFFC374, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3727)
    BeginChrThread(0x11, 3, 1, 64)
    Sleep(30)
    BeginChrThread(0x10, 3, 1, 63)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x10, 3)
    Return()

    # Function_62_3676 end

    def Function_63_3771(): pass

    label("Function_63_3771")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_3789():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3789)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    BeginChrThread(0x14, 3, 1, 65)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    Return()

    # Function_63_3771 end

    def Function_64_37CD(): pass

    label("Function_64_37CD")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
    Sound(809, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_64_37CD end

    def Function_65_380B(): pass

    label("Function_65_380B")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6FB8, 0xFFFFE890, 0xFFFFBA00, 0x3A98, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 100, 0)
    OP_9D(0xFE, 0x7CC4, 0xFFFFE890, 0xFFFFAB50, 0xBB8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_65_380B end

    def Function_66_3853(): pass

    label("Function_66_3853")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_386B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_386B)
    Sleep(600)

    #C0078
    ChrTalk(
        0x101,
        "#6P#5A#4S……はっ！#3S\x02",
    )
    #Auto

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(441, 0, 100, 0)
    BeginChrThread(0x14, 3, 1, 68)
    BeginChrThread(0x11, 3, 1, 64)
    Sleep(30)
    BeginChrThread(0x10, 3, 1, 67)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    Return()

    # Function_66_3853 end

    def Function_67_38EA(): pass

    label("Function_67_38EA")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    Sound(30, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_67_38EA end

    def Function_68_3928(): pass

    label("Function_68_3928")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFD508, 0x7D0, 0x3E8)
    Sound(443, 0, 50, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFDAE4, 0x3E8, 0x3E8)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFDECC, 0x1F4, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x639C, 0xFFFFE890, 0xFFFFE0C0, 0xC8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_68_3928 end

    def Function_69_39AD(): pass

    label("Function_69_39AD")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x101, 24500, -6000, -22000, 0)
    SetChrPos(0x10, 27500, -6000, -19000, 0)
    SetChrPos(0x11, 24500, -6000, -13000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrPos(0x13, 21300, -6000, -16000, 90)
    SetChrPos(0x14, 24500, -5500, -21800, 0)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    OP_68(26000, -5000, -16000, 15000)
    MoveCamera(305, 30, 0, 15000)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 3, 1, 70)

    label("loc_3AA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ABC")
    Sleep(1)
    Jump("loc_3AA5")

    label("loc_3ABC")

    OP_4B(0x14, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "全力を込めて高くトス\x01",      # 0
            "力を抑えて低くトス\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC4")
    OP_2C(0xA5, 0x1)
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 81)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0079
    ChrTalk(
        0x13,
        "#12902F#5P#Nフフ、お見事。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0080
    ChrTalk(
        0x11,
        (
            "#12806Fさ、さすがイリアさん……\x01",
            "反則級の身体能力ッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x12,
        (
            "#13006Fあんなとんでもない高さ……\x01",
            "いくらなんでもブロックできませんよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0082
    ChrTalk(
        0x10,
        "#13409F#6Pフフ、ざっとこんなもんよ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xE1, 0x1F4)

    #C0083
    ChrTalk(
        0x10,
        (
            "#13400F#12P弟君も、あんな高いトス\x01",
            "よく出してくれたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12500F#5Pはは、イリアさんの身体能力なら\x01",
            "いけると思ってましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x10,
        (
            "#13409F#12Pフフ、えらいえらい♪\x02\x03",

            "#13400Fさあ、このままゲームを\x01",
            "一気に獲るわよッ！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0086
    ChrTalk(
        0x13,
        (
            "#12900F#5P#N……ゲームセット！！\x02\x03",

            "#12904F１２－４で、\x01",
            "ロイドチームの勝ち。\x01",
            "フフ、お疲れ様。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0087
    ChrTalk(
        0x101,
        "#12509F#6Pよし、圧勝だ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_424C")

    label("loc_3EC4")

    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 86)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0088
    ChrTalk(
        0x13,
        (
            "#12902F#5P#Nフフ、残念。\x01",
            "チャンスを掴みきれなかったね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)

    #C0089
    ChrTalk(
        0x11,
        "#12806Fヒュウ、あっぶねえ……！\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x12,
        (
            "#13011Fでも、なんてジャンプ力……\x02\x03",

            "#13006Fあんな高さからアタックされてたら\x01",
            "さすがに防ぎきれませんでしたよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x10, 0xE1, 0x1F4)

    #C0091
    ChrTalk(
        0x10,
        "#13406F#12Pあちゃー……ゴメン、弟君。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#12512Fいや、こちらこそ……\x01",
            "まさかあんなに飛ぶなんて\x01",
            "思ってもみませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x11,
        (
            "#12800Fハハ、女神は\x01",
            "俺たちについてるみてえだな。\x01",
            "一気にけしかけっぞ、ノエル！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x12,
        "#13009Fはいっ！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(909, 0, 70, 0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x101, 24500, -6000, -19000, 0)
    SetChrPos(0x10, 27500, -6000, -20000, 0)
    SetChrPos(0x11, 24500, -6000, -12000, 180)
    SetChrPos(0x12, 27500, -6000, -13000, 180)
    SetChrFlags(0x14, 0x8)
    OP_68(26000, -5000, -16000, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0095
    ChrTalk(
        0x13,
        (
            "#12900F#5P……ゲームセット！！\x02\x03",

            "#12904F９－１２で、\x01",
            "ランディチームの勝ち。\x01",
            "フフ、お疲れ様。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        "#12506F#6Pくっ、負けてしまったか……\x02",
    )

    CloseMessageWindow()

    label("loc_424C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_69_39AD end

    def Function_70_4258(): pass

    label("Function_70_4258")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_4268():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4268)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0097
    ChrTalk(
        0x101,
        "#5P#5A……はっ！\x02",
    )
    #Auto


    def lambda_42AF():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC70, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_42AF)
    BeginChrThread(0x11, 3, 1, 71)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_70_4258 end

    def Function_71_42F0(): pass

    label("Function_71_42F0")

    WaitChrThread(0x14, 1)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4303():
        OP_9D(0xFE, 0x6AA4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4303)
    BeginChrThread(0x12, 3, 1, 72)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_71_42F0 end

    def Function_72_4329(): pass

    label("Function_72_4329")

    SetChrFlags(0xFE, 0x20)

    def lambda_4333():

        label("loc_4333")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4333")

    QueueWorkItem2(0xFE, 2, lambda_4333)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_435E():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_435E)
    BeginChrThread(0x11, 3, 1, 73)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0x10, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_72_4329 end

    def Function_73_43B7(): pass

    label("Function_73_43B7")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    #C0098
    ChrTalk(
        0x11,
        "#11P#5A速攻ォ！\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_43E6():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43E6)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_440E():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_440E)
    BeginChrThread(0x101, 3, 1, 74)
    Sleep(100)
    Sound(442, 0, 80, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_73_43B7 end

    def Function_74_4451(): pass

    label("Function_74_4451")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)

    def lambda_445E():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB0B4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_445E)
    BeginChrThread(0x10, 3, 1, 75)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_74_4451 end

    def Function_75_4484(): pass

    label("Function_75_4484")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    #C0099
    ChrTalk(
        0x10,
        "#6P#5Aはいっ！\x02",
    )
    #Auto


    def lambda_44AA():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_44AA)
    BeginChrThread(0x101, 3, 1, 76)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_75_4484 end

    def Function_76_44D0(): pass

    label("Function_76_44D0")

    SetChrFlags(0xFE, 0x20)

    def lambda_44DA():

        label("loc_44DA")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_44DA")

    QueueWorkItem2(0xFE, 2, lambda_44DA)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    def lambda_4505():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4505)
    BeginChrThread(0x12, 3, 1, 77)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_76_44D0 end

    def Function_77_4538(): pass

    label("Function_77_4538")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_454B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_454B)
    BeginChrThread(0x11, 3, 1, 78)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_77_4538 end

    def Function_78_4571(): pass

    label("Function_78_4571")

    SetChrFlags(0xFE, 0x20)

    def lambda_457B():

        label("loc_457B")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_457B")

    QueueWorkItem2(0xFE, 2, lambda_457B)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0100
    ChrTalk(
        0x11,
        "#11P#5A行けェ！\x02",
    )
    #Auto


    def lambda_45BA():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_45BA)
    BeginChrThread(0x12, 3, 1, 79)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    OP_9B(0x1, 0x10, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x11, 0x20)
    OP_93(0x11, 0xB4, 0x1F4)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    OP_98(0x11, 0x5DC, 0x0, 0x0, 0xFA0, 0x0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    Return()

    # Function_78_4571 end

    def Function_79_4641(): pass

    label("Function_79_4641")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_465C():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_465C)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    #C0101
    ChrTalk(
        0x12,
        "#11P#5Aこれならっ！？\x02",
    )
    #Auto

    Sound(442, 0, 80, 0)

    def lambda_46A4():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_46A4)
    BeginChrThread(0x10, 3, 1, 80)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_79_4641 end

    def Function_80_46E1(): pass

    label("Function_80_46E1")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_46F4():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_46F4)
    SetChrFlags(0x101, 0x20)
    OP_93(0x101, 0x5A, 0x1F4)
    ClearChrFlags(0x101, 0x20)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    EndChrThread(0x101, 0x2)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_80_46E1 end

    def Function_81_4736(): pass

    label("Function_81_4736")


    #C0102
    ChrTalk(
        0x101,
        "#5P#5Aイリアさん！！\x02",
    )
    #Auto

    SetChrFlags(0xFE, 0x20)

    def lambda_4759():

        label("loc_4759")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4759")

    QueueWorkItem2(0xFE, 2, lambda_4759)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_4784():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xCE4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4784)
    BeginChrThread(0x10, 3, 1, 82)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x10, 3)
    Return()

    # Function_81_4736 end

    def Function_82_47BB(): pass

    label("Function_82_47BB")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    #C0103
    ChrTalk(
        0x10,
        "#5P#5A#4Sはあああああっ！！#3S\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_47F9():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47F9)
    Sleep(700)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 1, 85)
    BeginChrThread(0x11, 3, 1, 83)
    BeginChrThread(0x12, 3, 1, 84)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    Return()

    # Function_82_47BB end

    def Function_83_48B0(): pass

    label("Function_83_48B0")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_83_48B0 end

    def Function_84_48E2(): pass

    label("Function_84_48E2")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_84_48E2 end

    def Function_85_4914(): pass

    label("Function_85_4914")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x64D2, 0xFFFFE890, 0xFFFFD29C, 0x61A8, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54A6, 0xFFFFE890, 0x46A, 0x7D0, 0x3E8)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x48DA, 0xFFFFE890, 0x26B6, 0x3E8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_85_4914 end

    def Function_86_4979(): pass

    label("Function_86_4979")


    #C0104
    ChrTalk(
        0x101,
        "#5P#5Aイリアさん！！\x02",
    )
    #Auto

    SetChrFlags(0xFE, 0x20)

    def lambda_499C():

        label("loc_499C")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_499C")

    QueueWorkItem2(0xFE, 2, lambda_499C)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)
    BeginChrThread(0x14, 3, 1, 88)
    BeginChrThread(0x10, 3, 1, 87)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x10, 3)
    Return()

    # Function_86_4979 end

    def Function_87_49EB(): pass

    label("Function_87_49EB")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    #C0105
    ChrTalk(
        0x10,
        "#5P#20A#4Sはああ……#3Sって、ありゃっ！？\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_4A33():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A33)
    Sleep(700)
    SetChrSubChip(0xFE, 0x1)
    Sound(590, 0, 100, 0)
    BeginChrThread(0x11, 3, 1, 83)
    BeginChrThread(0x12, 3, 1, 84)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    Return()

    # Function_87_49EB end

    def Function_88_4A8E(): pass

    label("Function_88_4A8E")

    Sound(443, 0, 40, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x898, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x6F54, 0xFFFFE890, 0xFFFFC091, 0x384, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x717A, 0xFFFFE890, 0xFFFFC1E4, 0x12C, 0x3E8)
    Return()

    # Function_88_4A8E end

    SaveToFile()

Try(main)
