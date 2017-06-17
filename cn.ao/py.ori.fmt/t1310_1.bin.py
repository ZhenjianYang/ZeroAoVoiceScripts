from ScenarioHelper import *

def main():
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
        [440, 441, 705, 859, 1004, 1061, 1187, 1417, 1489, 0, 1539, 0, 3172, 3319, 3376, 3529, 0, 3586, 0, 124, 14, 0, 0],
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
        "Function_4_3EC",          # 04, 4
        "Function_5_425",          # 05, 5
        "Function_6_4A3",          # 06, 6
        "Function_7_589",          # 07, 7
        "Function_8_5D1",          # 08, 8
        "Function_9_603",          # 09, 9
        "Function_10_C64",         # 0A, 10
        "Function_11_CF7",         # 0B, 11
        "Function_12_D30",         # 0C, 12
        "Function_13_DC9",         # 0D, 13
        "Function_14_E02",         # 0E, 14
        "Function_15_E7C",         # 0F, 15
        "Function_16_F16",         # 10, 16
        "Function_17_F8B",         # 11, 17
        "Function_18_FDC",         # 12, 18
        "Function_19_10AE",        # 13, 19
        "Function_20_1136",        # 14, 20
        "Function_21_11B5",        # 15, 21
        "Function_22_129C",        # 16, 22
        "Function_23_12E4",        # 17, 23
        "Function_24_1322",        # 18, 24
        "Function_25_1B7B",        # 19, 25
        "Function_26_1C0E",        # 1A, 26
        "Function_27_1C47",        # 1B, 27
        "Function_28_1CF0",        # 1C, 28
        "Function_29_1D87",        # 1D, 29
        "Function_30_1DC0",        # 1E, 30
        "Function_31_1E5E",        # 1F, 31
        "Function_32_1E5F",        # 20, 32
        "Function_33_1EC6",        # 21, 33
        "Function_34_1F5C",        # 22, 34
        "Function_35_1FAD",        # 23, 35
        "Function_36_2019",        # 24, 36
        "Function_37_2034",        # 25, 37
        "Function_38_2090",        # 26, 38
        "Function_39_20C2",        # 27, 39
        "Function_40_2159",        # 28, 40
        "Function_41_21DE",        # 29, 41
        "Function_42_2209",        # 2A, 42
        "Function_43_2231",        # 2B, 43
        "Function_44_22DE",        # 2C, 44
        "Function_45_233B",        # 2D, 45
        "Function_46_23C7",        # 2E, 46
        "Function_47_24AC",        # 2F, 47
        "Function_48_24F4",        # 30, 48
        "Function_49_2538",        # 31, 49
        "Function_50_2E9B",        # 32, 50
        "Function_51_2F31",        # 33, 51
        "Function_52_2F6A",        # 34, 52
        "Function_53_2FEC",        # 35, 53
        "Function_54_307E",        # 36, 54
        "Function_55_30B7",        # 37, 55
        "Function_56_311F",        # 38, 56
        "Function_57_31B8",        # 39, 57
        "Function_58_31F1",        # 3A, 58
        "Function_59_3273",        # 3B, 59
        "Function_60_330B",        # 3C, 60
        "Function_61_33C6",        # 3D, 61
        "Function_62_3432",        # 3E, 62
        "Function_63_3529",        # 3F, 63
        "Function_64_3585",        # 40, 64
        "Function_65_35C3",        # 41, 65
        "Function_66_360B",        # 42, 66
        "Function_67_36A0",        # 43, 67
        "Function_68_36DE",        # 44, 68
        "Function_69_3763",        # 45, 69
        "Function_70_3F80",        # 46, 70
        "Function_71_4016",        # 47, 71
        "Function_72_404F",        # 48, 72
        "Function_73_40DD",        # 49, 73
        "Function_74_4175",        # 4A, 74
        "Function_75_41A8",        # 4B, 75
        "Function_76_41F0",        # 4C, 76
        "Function_77_4258",        # 4D, 77
        "Function_78_4291",        # 4E, 78
        "Function_79_435F",        # 4F, 79
        "Function_80_43FD",        # 50, 80
        "Function_81_4452",        # 51, 81
        "Function_82_44D7",        # 52, 82
        "Function_83_45CA",        # 53, 83
        "Function_84_45FC",        # 54, 84
        "Function_85_462E",        # 55, 85
        "Function_86_4693",        # 56, 86
        "Function_87_4705",        # 57, 87
        "Function_88_47A0",        # 58, 88
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
        "#6P#7A──前辈！\x02",
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
        "#5P#5A哦！\x02",
    )
    #Auto


    def lambda_3AF():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3AF)
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

    def Function_4_3EC(): pass

    label("Function_4_3EC")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_3FF():
        OP_9D(0xFE, 0x6A40, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3FF)
    BeginChrThread(0x13, 3, 1, 5)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_4_3EC end

    def Function_5_425(): pass

    label("Function_5_425")

    SetChrFlags(0xFE, 0x20)

    def lambda_42F():

        label("loc_42F")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_42F")

    QueueWorkItem2(0xFE, 2, lambda_42F)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    #C0003
    ChrTalk(
        0x13,
        "#12P#6A交给你了！\x02",
    )
    #Auto


    def lambda_470():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFC694, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_470)
    BeginChrThread(0x10, 3, 1, 6)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_5_425 end

    def Function_6_4A3(): pass

    label("Function_6_4A3")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_4BE():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BE)
    Sleep(600)

    #C0004
    ChrTalk(
        0x10,
        "#11P#4S#5A呀！！#3S\x02",
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

    # Function_6_4A3 end

    def Function_7_589(): pass

    label("Function_7_589")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x5AD2, 0xFFFFE890, 0xFFFFADF8, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54F6, 0xFFFFE890, 0xFFFF8FBC, 0x3E8, 0x7D0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_7_589 end

    def Function_8_5D1(): pass

    label("Function_8_5D1")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_5D1 end

    def Function_9_603(): pass

    label("Function_9_603")

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

    label("loc_6FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712")
    Sleep(1)
    Jump("loc_6FB")

    label("loc_712")

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
            "直接扣击\x01",                      # 0
            "托球回传，由兰迪发动攻击\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DD")
    MoveCamera(315, 25, 0, 1500)
    SetCameraDistance(15000, 1500)
    BeginChrThread(0x101, 3, 1, 18)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0005
    ChrTalk(
        0x10,
        "#13400F#5P#N出界～！！\x02",
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
        "#12506F#6P糟糕，太着急了吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x13, 0xE1, 0x1F4)

    #C0007
    ChrTalk(
        0x13,
        "#12902F呵呵，承让了。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x12,
        "#13006F#5P#N真危险～\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0009
    ChrTalk(
        0x101,
        "#12500F抱歉！兰迪！\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    #C0010
    ChrTalk(
        0x11,
        (
            "#12800F#12P没事没事！\x01",
            "接下来就是我们的反击了！\x02",
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
            "#13400F#5P……比赛结束！！\x02\x03",

            "#13409F７比１２，\x01",
            "瓦吉队获胜～！\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#12506F#6P呼，输了呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C58")

    label("loc_9DD")

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
        "#13405F#5P#N哦哦！厉害啊，兰迪！\x02",
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
        "#13002F#11P#N唔……干得漂亮。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0015
    ChrTalk(
        0x13,
        (
            "#12906F#11P哎呀呀，身高差距\x01",
            "实在是让人头疼呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x10E, 0x1F4)

    #C0016
    ChrTalk(
        0x11,
        (
            "#12809F#12P传得好，罗伊德，\x01",
            "你的判断力果然出色。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0017
    ChrTalk(
        0x101,
        (
            "#12509F#5P哈哈，我们只是暂时领先而已。\x02\x03",

            "#12500F好！乘胜追击吧！！\x02",
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
            "#13400F#5P……比赛结束！！\x02\x03",

            "#13409F１２比８，警察弟弟队获胜～！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#12500F#6P好！赢了！！\x02",
    )

    CloseMessageWindow()

    label("loc_C58")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_9_603 end

    def Function_10_C64(): pass

    label("Function_10_C64")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_C74():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C74)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    #C0020
    ChrTalk(
        0x12,
        "#11P#5A呼！\x02",
    )
    #Auto


    def lambda_CB6():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_CB6)
    BeginChrThread(0x101, 3, 1, 11)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_C64 end

    def Function_11_CF7(): pass

    label("Function_11_CF7")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_D0A():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEE6C, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D0A)
    BeginChrThread(0x11, 3, 1, 12)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_11_CF7 end

    def Function_12_D30(): pass

    label("Function_12_D30")

    SetChrFlags(0xFE, 0x20)

    def lambda_D3A():

        label("loc_D3A")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_D3A")

    QueueWorkItem2(0xFE, 2, lambda_D3A)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0021
    ChrTalk(
        0x11,
        "#6P#6A哦！\x02",
    )
    #Auto


    def lambda_D74():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D74)
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

    # Function_12_D30 end

    def Function_13_DC9(): pass

    label("Function_13_DC9")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_DDC():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DDC)
    BeginChrThread(0x12, 3, 1, 14)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_DC9 end

    def Function_14_E02(): pass

    label("Function_14_E02")

    SetChrFlags(0xFE, 0x20)

    def lambda_E0C():

        label("loc_E0C")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_E0C")

    QueueWorkItem2(0xFE, 2, lambda_E0C)
    Sleep(350)

    #C0022
    ChrTalk(
        0x12,
        "#11P#8A瓦吉！\x02",
    )
    #Auto

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_E49():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E49)
    BeginChrThread(0x13, 3, 1, 15)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_E02 end

    def Function_15_E7C(): pass

    label("Function_15_E7C")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)

    #C0023
    ChrTalk(
        0x13,
        "#11P#5A嗯……！\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_EAB():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EAB)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_ED3():
        OP_98(0xFE, 0x0, 0xFFFFFCE0, 0xFFFFF830, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ED3)
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

    # Function_15_E7C end

    def Function_16_F16(): pass

    label("Function_16_F16")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_F2E():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F2E)
    WaitChrThread(0x14, 1)

    def lambda_F4F():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCD38, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_F4F)
    BeginChrThread(0x12, 3, 1, 17)
    Sound(441, 0, 80, 0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Return()

    # Function_16_F16 end

    def Function_17_F8B(): pass

    label("Function_17_F8B")

    WaitChrThread(0x14, 1)
    SetChrFlags(0xFE, 0x20)
    OP_93(0xFE, 0xB4, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_FAF():
        OP_9D(0xFE, 0x5FB4, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_FAF)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_F8B end

    def Function_18_FDC(): pass

    label("Function_18_FDC")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_FF4():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBBA4, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FF4)
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
        "#5P#6A#4S嘿！！#3S\x02",
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

    # Function_18_FDC end

    def Function_19_10AE(): pass

    label("Function_19_10AE")

    SetChrFlags(0x13, 0x20)

    def lambda_10B8():

        label("loc_10B8")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_10B8")

    QueueWorkItem2(0x13, 2, lambda_10B8)
    SetChrFlags(0x12, 0x20)

    def lambda_10CF():

        label("loc_10CF")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_10CF")

    QueueWorkItem2(0x12, 2, lambda_10CF)
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

    # Function_19_10AE end

    def Function_20_1136(): pass

    label("Function_20_1136")

    SetChrFlags(0xFE, 0x20)

    def lambda_1140():

        label("loc_1140")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1140")

    QueueWorkItem2(0xFE, 2, lambda_1140)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    #C0025
    ChrTalk(
        0x101,
        "#5P#5A拜托了！\x02",
    )
    #Auto


    def lambda_117E():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBF8C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_117E)
    BeginChrThread(0x11, 3, 1, 21)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x11, 3)
    Return()

    # Function_20_1136 end

    def Function_21_11B5(): pass

    label("Function_21_11B5")

    Sleep(600)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_11D0():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11D0)
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
        "#5P#10A#4S噢噢噢噢噢！！#3S\x02",
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

    # Function_21_11B5 end

    def Function_22_129C(): pass

    label("Function_22_129C")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6F9A, 0xFFFFE890, 0xFFFFCCCA, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x7F76, 0xFFFFE7F0, 0x762, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_22_129C end

    def Function_23_12E4(): pass

    label("Function_23_12E4")

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

    # Function_23_12E4 end

    def Function_24_1322(): pass

    label("Function_24_1322")

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

    label("loc_141A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1431")
    Sleep(1)
    Jump("loc_141A")

    label("loc_1431")

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
            "预判为强力扣击，参与阻截\x01",      # 0
            "判断对方的真意，退至后场\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FF")
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
            "#12809F#5P#N伊莉娅小姐队得分！\x02\x03",

            "#12803F话说回来，不愧是瓦吉啊……\x01",
            "竟然击出如此狡诈的球。\x02",
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
            "#12902F#12P呵呵，别说得这么难听嘛，\x01",
            "这也是战术的一种。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x87, 0x1F4)

    #C0029
    ChrTalk(
        0x10,
        (
            "#13404F#5P嗯，和他们这种单纯刻板的对手比赛，\x01",
            "没有比这更好的战术了～\x02",
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
            "#13001F#5P罗、罗伊德警官……\x01",
            "他们竟敢这样说我们！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0031
    ChrTalk(
        0x101,
        (
            "#12510F#12P唔唔……绝、绝不能输！\x02\x03",

            "#12501F既然如此，诺艾尔，我们就靠意志来取胜吧！\x01",
            "无论如何也要接住他们的球！\x02",
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
            "#12800F#5P……比赛结束！！\x02\x03",

            "#12809F３比１２，\x01",
            "伊莉娅小姐队获胜！！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#12506F#6P呜……还是不行吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B6F")

    label("loc_17FF")

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
            "#12800F#5P#N罗伊德队得分！\x02\x03",

            "#12809F哈哈，干得不错嘛！\x02",
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
            "#12906F#11P哎呀呀，没想到会被你识破。\x02\x03",

            "#12902F平时那么单纯刻板，\x01",
            "竟能做出如此出色的判断～\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#12502F#6P以瓦吉的性格来说，\x01",
            "在那种情况下肯定会采用取巧手段。\x02\x03",

            "#12504F与其正面对攻，不如反其道而行。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0x5A, 0x1F4)

    #C0037
    ChrTalk(
        0x12,
        "#13000F#5P成功了！罗伊德警官！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x5A, 0x1F4)

    #C0038
    ChrTalk(
        0x10,
        (
            "#13400F#5P呵呵，似乎有些\x01",
            "小看他们了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x13,
        "#12904F哈哈，看来是这样啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0040
    ChrTalk(
        0x101,
        (
            "#12500F#12P好！诺艾尔！\x01",
            "我们就保持这种状态，\x01",
            "把握住比赛的节奏吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x12,
        "#13009F#5P嗯！明白了！！\x02",
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
            "#12800F#5P……比赛结束！！\x02\x03",

            "#12809F１２比１１，\x01",
            "罗伊德队获胜！！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#12512F#6P赢、赢了……勉强险胜啊！\x02",
    )

    CloseMessageWindow()

    label("loc_1B6F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_24_1322 end

    def Function_25_1B7B(): pass

    label("Function_25_1B7B")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_1B8B():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1B8B)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0044
    ChrTalk(
        0x10,
        "#11P#5A嘿！\x02",
    )
    #Auto


    def lambda_1BCD():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1BCD)
    BeginChrThread(0x12, 3, 1, 26)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_1B7B end

    def Function_26_1C0E(): pass

    label("Function_26_1C0E")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1C21():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEDA4, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1C21)
    BeginChrThread(0x101, 3, 1, 27)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_1C0E end

    def Function_27_1C47(): pass

    label("Function_27_1C47")

    SetChrFlags(0xFE, 0x20)

    def lambda_1C51():

        label("loc_1C51")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1C51")

    QueueWorkItem2(0xFE, 2, lambda_1C51)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    #C0045
    ChrTalk(
        0x101,
        "#6P#5A诺艾尔！\x02",
    )
    #Auto


    def lambda_1C8F():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1C8F)
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

    # Function_27_1C47 end

    def Function_28_1CF0(): pass

    label("Function_28_1CF0")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_1D0B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D0B)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    #C0046
    ChrTalk(
        0x12,
        "#5P#5A嗯！！\x02",
    )
    #Auto


    def lambda_1D4A():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D4A)
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

    # Function_28_1CF0 end

    def Function_29_1D87(): pass

    label("Function_29_1D87")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1D9A():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xC80, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D9A)
    BeginChrThread(0x10, 3, 1, 30)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_1D87 end

    def Function_30_1DC0(): pass

    label("Function_30_1DC0")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    #C0047
    ChrTalk(
        0x10,
        "#11P#5A接球！\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_1DED():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DED)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    def lambda_1E1B():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB30C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1E1B)
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

    # Function_30_1DC0 end

    def Function_31_1E5E(): pass

    label("Function_31_1E5E")

    Return()

    # Function_31_1E5E end

    def Function_32_1E5F(): pass

    label("Function_32_1E5F")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_1E72():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFBD98, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1E72)
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

    # Function_32_1E5F end

    def Function_33_1EC6(): pass

    label("Function_33_1EC6")

    SetChrFlags(0xFE, 0x20)

    def lambda_1ED0():

        label("loc_1ED0")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1ED0")

    QueueWorkItem2(0xFE, 2, lambda_1ED0)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_1EFB():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1EFB)
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

    # Function_33_1EC6 end

    def Function_34_1F5C(): pass

    label("Function_34_1F5C")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    #C0048
    ChrTalk(
        0x13,
        "#12P#5A看招吧……！\x02",
    )
    #Auto


    def lambda_1F87():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1F87)
    BeginChrThread(0x10, 3, 1, 35)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_1F5C end

    def Function_35_1FAD(): pass

    label("Function_35_1FAD")

    SetChrFlags(0xFE, 0x20)

    def lambda_1FB7():

        label("loc_1FB7")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_1FB7")

    QueueWorkItem2(0xFE, 2, lambda_1FB7)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_1FE2():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1FE2)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_1FAD end

    def Function_36_2019(): pass

    label("Function_36_2019")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_2019 end

    def Function_37_2034(): pass

    label("Function_37_2034")

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

    # Function_37_2034 end

    def Function_38_2090(): pass

    label("Function_38_2090")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_2090 end

    def Function_39_20C2(): pass

    label("Function_39_20C2")

    BeginChrThread(0x101, 3, 1, 37)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_20E0():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_20E0)
    Sleep(600)

    #C0049
    ChrTalk(
        0x13,
        "#12P#5A骗你们啦¤\x02",
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

    # Function_39_20C2 end

    def Function_40_2159(): pass

    label("Function_40_2159")

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

    # Function_40_2159 end

    def Function_41_21DE(): pass

    label("Function_41_21DE")

    BeginChrThread(0x10, 3, 1, 36)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFF830, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_21DE end

    def Function_42_2209(): pass

    label("Function_42_2209")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_2209 end

    def Function_43_2231(): pass

    label("Function_43_2231")

    BeginChrThread(0x101, 3, 1, 41)
    BeginChrThread(0x12, 3, 1, 42)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_2255():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2255)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    #C0050
    ChrTalk(
        0x13,
        "#12P#5A什么……！？\x02",
    )
    #Auto


    def lambda_2295():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB118, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2295)
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

    # Function_43_2231 end

    def Function_44_22DE(): pass

    label("Function_44_22DE")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_22F1():
        OP_9D(0xFE, 0x6590, 0xFFFFEC78, 0xFFFFB9B0, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_22F1)
    BeginChrThread(0x12, 3, 1, 45)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_98(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_22DE end

    def Function_45_233B(): pass

    label("Function_45_233B")

    SetChrFlags(0xFE, 0x20)

    def lambda_2345():

        label("loc_2345")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_2345")

    QueueWorkItem2(0xFE, 2, lambda_2345)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_2370():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2370)
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

    # Function_45_233B end

    def Function_46_23C7(): pass

    label("Function_46_23C7")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    #C0051
    ChrTalk(
        0x101,
        "#5P#5A#4S噢噢噢噢噢！#3S\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_23FF():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23FF)
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

    # Function_46_23C7 end

    def Function_47_24AC(): pass

    label("Function_47_24AC")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6658, 0xFFFFE890, 0xFFFFCE5A, 0x4E20, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x774C, 0xFFFFE890, 0xFFFFFA9C, 0x1388, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_47_24AC end

    def Function_48_24F4(): pass

    label("Function_48_24F4")

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

    # Function_48_24F4 end

    def Function_49_2538(): pass

    label("Function_49_2538")

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

    label("loc_2630")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2647")
    Sleep(1)
    Jump("loc_2630")

    label("loc_2647")

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
            "将球强攻向伊莉娅和兰迪之间\x01",      # 0
            "瞄准后场边界线，击出弧线球\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B08")
    MoveCamera(315, 25, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x101, 3, 1, 62)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0052
    ChrTalk(
        0x12,
        "#13002F#5P#N伊莉娅小姐队得分！\x02",
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
            "#12809F#5P完美！！\x01",
            "真不愧是伊莉娅小姐！！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x10E, 0x1F4)

    #C0054
    ChrTalk(
        0x10,
        "#13400F#12P啊哈哈，普普通通啦。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x13,
        (
            "#12906F#12P#N哎呀呀，\x01",
            "竟然选择正面强攻，难道你认为自己\x01",
            "可以胜过他们二人的身体能力吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_27F5():
        OP_93(0x11, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_27F5)
    Sleep(30)

    def lambda_2805():
        OP_93(0x10, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2805)
    Sleep(30)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x10, 0)
    OP_93(0x101, 0x87, 0x1F4)

    #C0056
    ChrTalk(
        0x101,
        (
            "#12506F#5P唉，真丢脸……\x02\x03",

            "#12505F……话说回来，瓦吉，\x01",
            "你刚才突然说『边界』，\x01",
            "到底是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x13,
        (
            "#12900F#12P#N哦，我当时就料到\x01",
            "伊莉娅小姐会发起拦截了，\x01",
            "所以觉得正面强攻肯定徒劳无功。\x02\x03",

            "#12904F『边界』就是边界线……\x01",
            "也就是说，让你击出弧线吊球，\x01",
            "使球落到后场边界线处。\x02",
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
            "#12506F#5P这……你突然那样说，\x01",
            "又有谁能听得懂啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x13,
        (
            "#12909F#12P#N啊哈哈，抱歉抱歉。\x02\x03",

            "#12900F好啦，尽快调整情绪，\x01",
            "想办法逆转比分吧。\x02",
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
            "#13000F#5P……比赛结束！！\x02\x03",

            "#13009F４比１２，\x01",
            "伊莉娅小姐队获胜！！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#12506F#6P呼，完败啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_2B08")

    OP_2C(0xA5, 0x1)
    BeginChrThread(0x101, 3, 1, 66)
    WaitChrThread(0x101, 3)
    Sound(909, 0, 70, 0)
    Sleep(500)

    #C0062
    ChrTalk(
        0x12,
        "#13002F#5P#N罗伊德警官队得分！\x02",
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
        "#12500F#6P好……！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x10,
        (
            "#13406F#11P哎呀呀～居然是吊球……\x01",
            "本以为他们肯定会选择正面强攻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x11,
        "#12806F#11P唉～被对手识破了呢。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x13,
        "#12902F#6P#N呵呵，干得不错嘛。\x02",
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
            "#12504F#11P……嗯，因为你对我\x01",
            "喊了暗号──『边界』。\x02\x03",

            "#12502F我察觉到对方的后场有空位，\x01",
            "所以立刻改打吊球了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x13,
        (
            "#12904F#6P#N呵呵，突然喊出那种暗号，\x01",
            "原本还有些不安，担心你无法领会呢。\x02\x03",

            "#12909F这大概就是爱的力量吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0069
    ChrTalk(
        0x101,
        (
            "#12506F#11P少说蠢话了。\x02\x03",

            "#12500F好，继续用这种战术扰乱\x01",
            "伊莉娅小姐他们的视线吧！\x02",
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
            "#13000F#5P……比赛结束！！\x02\x03",

            "#13009F１２比１０，\x01",
            "罗伊德警官队获胜！！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#12509F#6P好！总算赢了！！\x02",
    )

    CloseMessageWindow()

    label("loc_2E8F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_49_2538 end

    def Function_50_2E9B(): pass

    label("Function_50_2E9B")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_2EAB():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2EAB)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0072
    ChrTalk(
        0x13,
        "#6P#5A呼……！\x02",
    )
    #Auto


    def lambda_2EF0():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2EF0)
    BeginChrThread(0x10, 3, 1, 51)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_2E9B end

    def Function_51_2F31(): pass

    label("Function_51_2F31")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_2F44():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEDA4, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2F44)
    BeginChrThread(0x11, 3, 1, 52)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_51_2F31 end

    def Function_52_2F6A(): pass

    label("Function_52_2F6A")

    SetChrFlags(0xFE, 0x20)

    def lambda_2F74():

        label("loc_2F74")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_2F74")

    QueueWorkItem2(0xFE, 2, lambda_2F74)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_2F9F():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2F9F)
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

    # Function_52_2F6A end

    def Function_53_2FEC(): pass

    label("Function_53_2FEC")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3007():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3007)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    Sound(442, 0, 80, 0)
    EndChrThread(0x14, 0x1)

    #C0073
    ChrTalk(
        0x10,
        "#11P#5A接球！\x02",
    )
    #Auto


    def lambda_3047():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3047)
    BeginChrThread(0x101, 3, 1, 54)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_53_2FEC end

    def Function_54_307E(): pass

    label("Function_54_307E")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_3091():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3091)
    BeginChrThread(0x13, 3, 1, 55)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_54_307E end

    def Function_55_30B7(): pass

    label("Function_55_30B7")

    SetChrFlags(0xFE, 0x20)

    def lambda_30C1():

        label("loc_30C1")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_30C1")

    QueueWorkItem2(0xFE, 2, lambda_30C1)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_30EC():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBBA4, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_30EC)
    BeginChrThread(0x101, 3, 1, 56)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_55_30B7 end

    def Function_56_311F(): pass

    label("Function_56_311F")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_313A():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_313A)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 80, 0)

    #C0074
    ChrTalk(
        0x101,
        "#5P#5A回敬你们……！\x02",
    )
    #Auto


    def lambda_3181():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC0C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3181)
    BeginChrThread(0x11, 3, 1, 57)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_311F end

    def Function_57_31B8(): pass

    label("Function_57_31B8")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_31CB():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31CB)
    BeginChrThread(0x10, 3, 1, 58)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_57_31B8 end

    def Function_58_31F1(): pass

    label("Function_58_31F1")

    SetChrFlags(0xFE, 0x20)

    def lambda_31FB():

        label("loc_31FB")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_31FB")

    QueueWorkItem2(0xFE, 2, lambda_31FB)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_3226():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3226)
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

    # Function_58_31F1 end

    def Function_59_3273(): pass

    label("Function_59_3273")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_328E():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_328E)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    #C0075
    ChrTalk(
        0x11,
        "#11P#5A看招！\x02",
    )
    #Auto


    def lambda_32C8():
        OP_96(0xFE, 0x5FB4, 0xFFFFF254, 0xFFFFBF8C, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32C8)
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

    # Function_59_3273 end

    def Function_60_330B(): pass

    label("Function_60_330B")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_3323():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3323)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 60, 0)

    def lambda_334A():
        OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB5C8, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_334A)
    BeginChrThread(0x13, 3, 1, 61)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)

    #C0076
    ChrTalk(
        0x13,
        "#6P#5A边界！\x02",
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

    # Function_60_330B end

    def Function_61_33C6(): pass

    label("Function_61_33C6")

    SetChrFlags(0xFE, 0x20)

    def lambda_33D0():

        label("loc_33D0")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_33D0")

    QueueWorkItem2(0xFE, 2, lambda_33D0)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_33FB():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFBF8C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33FB)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_61_33C6 end

    def Function_62_3432(): pass

    label("Function_62_3432")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_344A():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_344A)
    Sleep(600)

    #C0077
    ChrTalk(
        0x101,
        "#5P#5A#4S……呼！#3S\x02",
    )
    #Auto

    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)
    Sound(442, 0, 100, 0)
    Sound(547, 0, 40, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_34DF():
        OP_96(0xFE, 0x6590, 0xFFFFF060, 0xFFFFC374, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_34DF)
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

    # Function_62_3432 end

    def Function_63_3529(): pass

    label("Function_63_3529")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)

    def lambda_3541():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3541)
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

    # Function_63_3529 end

    def Function_64_3585(): pass

    label("Function_64_3585")

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

    # Function_64_3585 end

    def Function_65_35C3(): pass

    label("Function_65_35C3")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x6FB8, 0xFFFFE890, 0xFFFFBA00, 0x3A98, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 100, 0)
    OP_9D(0xFE, 0x7CC4, 0xFFFFE890, 0xFFFFAB50, 0xBB8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_65_35C3 end

    def Function_66_360B(): pass

    label("Function_66_360B")

    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3623():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFBD98, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3623)
    Sleep(600)

    #C0078
    ChrTalk(
        0x101,
        "#6P#5A#4S……嘿！#3S\x02",
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

    # Function_66_360B end

    def Function_67_36A0(): pass

    label("Function_67_36A0")

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

    # Function_67_36A0 end

    def Function_68_36DE(): pass

    label("Function_68_36DE")

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

    # Function_68_36DE end

    def Function_69_3763(): pass

    label("Function_69_3763")

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

    label("loc_385B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3872")
    Sleep(1)
    Jump("loc_385B")

    label("loc_3872")

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
            "全力将球托高\x01",      # 0
            "控制力度托球\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_4C(0x14, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C56")
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
        "#12902F#5P#N呵呵，打得漂亮。\x02",
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
            "#12806F真、真不愧是伊莉娅小姐……\x01",
            "那种身体能力简直就是犯规啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x12,
        (
            "#13006F在那种惊人的高度扣球……\x01",
            "我们根本不可能挡得住呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0082
    ChrTalk(
        0x10,
        "#13409F#6P呵呵，随意一击罢了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xE1, 0x1F4)

    #C0083
    ChrTalk(
        0x10,
        (
            "#13400F#12P警察弟弟的判断很出色呢，\x01",
            "竟然把球托得那么高。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12500F#5P哈哈，因为我觉得凭伊莉娅小姐\x01",
            "的身体能力，肯定能接到那一球。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x10,
        (
            "#13409F#12P呵呵，聪明聪明¤\x02\x03",

            "#13400F好，我们就保持这种势头，\x01",
            "一鼓作气结束比赛吧！\x02",
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
            "#12900F#5P#N……比赛结束！！\x02\x03",

            "#12904F１２比４，\x01",
            "罗伊德队获胜！！\x01",
            "呵呵，辛苦啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0087
    ChrTalk(
        0x101,
        "#12509F#6P好！压倒性完胜！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F74")

    label("loc_3C56")

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
            "#12902F#5P#N呵呵，真遗憾，\x01",
            "没能把握住机会呢。\x02",
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
        "#12806F呼，好危险……！\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x12,
        (
            "#13011F不过，弹跳力好惊人啊……\x02\x03",

            "#13006F如果真能在那种高度击出扣球，\x01",
            "我们肯定接不下。\x02",
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
        "#13406F#12P哎呀呀……抱歉哦，警察弟弟。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#12512F哪里，是我的失误……\x01",
            "没想到你竟然\x01",
            "能跳那么高。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x11,
        (
            "#12800F哈哈，看来女神\x01",
            "站在我们这边呢。\x01",
            "一鼓作气取得胜利吧！诺艾尔！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x12,
        "#13009F是！\x02",
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
            "#12900F#5P……比赛结束！！\x02\x03",

            "#12904F９比１２，\x01",
            "兰迪队获胜。\x01",
            "呵呵，辛苦啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        "#12506F#6P呜，输了呢……\x02",
    )

    CloseMessageWindow()

    label("loc_3F74")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_69_3763 end

    def Function_70_3F80(): pass

    label("Function_70_3F80")

    ClearChrFlags(0x14, 0x8)
    Sound(802, 0, 60, 0)

    def lambda_3F90():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3F90)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0097
    ChrTalk(
        0x101,
        "#5P#5A……嘿！\x02",
    )
    #Auto


    def lambda_3FD5():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFCC70, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3FD5)
    BeginChrThread(0x11, 3, 1, 71)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_70_3F80 end

    def Function_71_4016(): pass

    label("Function_71_4016")

    WaitChrThread(0x14, 1)
    Sound(441, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4029():
        OP_9D(0xFE, 0x6AA4, 0xFFFFEC78, 0xFFFFCD38, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4029)
    BeginChrThread(0x12, 3, 1, 72)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_71_4016 end

    def Function_72_404F(): pass

    label("Function_72_404F")

    SetChrFlags(0xFE, 0x20)

    def lambda_4059():

        label("loc_4059")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4059")

    QueueWorkItem2(0xFE, 2, lambda_4059)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    Sound(441, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4084():
        OP_9D(0xFE, 0x5FB4, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4084)
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

    # Function_72_404F end

    def Function_73_40DD(): pass

    label("Function_73_40DD")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    #C0098
    ChrTalk(
        0x11,
        "#11P#5A速攻！\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_410A():
        OP_9D(0xFE, 0x5FB4, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_410A)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    def lambda_4132():
        OP_96(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4132)
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

    # Function_73_40DD end

    def Function_74_4175(): pass

    label("Function_74_4175")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)

    def lambda_4182():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB0B4, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4182)
    BeginChrThread(0x10, 3, 1, 75)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_74_4175 end

    def Function_75_41A8(): pass

    label("Function_75_41A8")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    #C0099
    ChrTalk(
        0x10,
        "#6P#5A嘿！\x02",
    )
    #Auto


    def lambda_41CA():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_41CA)
    BeginChrThread(0x101, 3, 1, 76)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_75_41A8 end

    def Function_76_41F0(): pass

    label("Function_76_41F0")

    SetChrFlags(0xFE, 0x20)

    def lambda_41FA():

        label("loc_41FA")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_41FA")

    QueueWorkItem2(0xFE, 2, lambda_41FA)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 60, 0)

    def lambda_4225():
        OP_9D(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFCC0C, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4225)
    BeginChrThread(0x12, 3, 1, 77)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_76_41F0 end

    def Function_77_4258(): pass

    label("Function_77_4258")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 80, 0)

    def lambda_426B():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFC568, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_426B)
    BeginChrThread(0x11, 3, 1, 78)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_77_4258 end

    def Function_78_4291(): pass

    label("Function_78_4291")

    SetChrFlags(0xFE, 0x20)

    def lambda_429B():

        label("loc_429B")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_429B")

    QueueWorkItem2(0xFE, 2, lambda_429B)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    #C0100
    ChrTalk(
        0x11,
        "#11P#5A上了！\x02",
    )
    #Auto


    def lambda_42D8():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFC75C, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_42D8)
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

    # Function_78_4291 end

    def Function_79_435F(): pass

    label("Function_79_435F")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_437A():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFC568, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_437A)
    Sleep(600)
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0x14, 0x1)

    #C0101
    ChrTalk(
        0x12,
        "#11P#5A这招如何！？\x02",
    )
    #Auto

    Sound(442, 0, 80, 0)

    def lambda_43C0():
        OP_96(0xFE, 0x6B6C, 0xFFFFEA84, 0xFFFFB6F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_43C0)
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

    # Function_79_435F end

    def Function_80_43FD(): pass

    label("Function_80_43FD")

    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_4410():
        OP_9D(0xFE, 0x5FB4, 0xFFFFEC78, 0xFFFFB5C8, 0xBB8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4410)
    SetChrFlags(0x101, 0x20)
    OP_93(0x101, 0x5A, 0x1F4)
    ClearChrFlags(0x101, 0x20)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    EndChrThread(0x101, 0x2)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_80_43FD end

    def Function_81_4452(): pass

    label("Function_81_4452")


    #C0102
    ChrTalk(
        0x101,
        "#5P#5A伊莉娅小姐！！\x02",
    )
    #Auto

    SetChrFlags(0xFE, 0x20)

    def lambda_4475():

        label("loc_4475")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_4475")

    QueueWorkItem2(0xFE, 2, lambda_4475)
    Sleep(350)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0xFE, 0x1)
    Sound(441, 0, 100, 0)

    def lambda_44A0():
        OP_9D(0xFE, 0x6B6C, 0xFFFFF448, 0xFFFFBBA4, 0xCE4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_44A0)
    BeginChrThread(0x10, 3, 1, 82)
    Sleep(500)
    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x10, 3)
    Return()

    # Function_81_4452 end

    def Function_82_44D7(): pass

    label("Function_82_44D7")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    #C0103
    ChrTalk(
        0x10,
        "#5P#5A#4S噢啊啊啊啊啊！！#3S\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_4513():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4513)
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

    # Function_82_44D7 end

    def Function_83_45CA(): pass

    label("Function_83_45CA")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_83_45CA end

    def Function_84_45FC(): pass

    label("Function_84_45FC")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x7D0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_84_45FC end

    def Function_85_462E(): pass

    label("Function_85_462E")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_96(0xFE, 0x64D2, 0xFFFFE890, 0xFFFFD29C, 0x61A8, 0x0)
    Sound(443, 0, 100, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x54A6, 0xFFFFE890, 0x46A, 0x7D0, 0x3E8)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x48DA, 0xFFFFE890, 0x26B6, 0x3E8, 0x3E8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_85_462E end

    def Function_86_4693(): pass

    label("Function_86_4693")


    #C0104
    ChrTalk(
        0x101,
        "#5P#5A伊莉娅小姐！！\x02",
    )
    #Auto

    SetChrFlags(0xFE, 0x20)

    def lambda_46B6():

        label("loc_46B6")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_46B6")

    QueueWorkItem2(0xFE, 2, lambda_46B6)
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

    # Function_86_4693 end

    def Function_87_4705(): pass

    label("Function_87_4705")

    Sleep(500)
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    #C0105
    ChrTalk(
        0x10,
        "#5P#20A#4S噢啊啊……#3S哎？哎呀！\x02",
    )
    #Auto

    Sound(809, 0, 100, 0)

    def lambda_4745():
        OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0xAF0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4745)
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

    # Function_87_4705 end

    def Function_88_47A0(): pass

    label("Function_88_47A0")

    Sound(443, 0, 40, 0)
    Sound(441, 0, 80, 0)
    OP_9D(0xFE, 0x6B6C, 0xFFFFE890, 0xFFFFBD98, 0x898, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x6F54, 0xFFFFE890, 0xFFFFC091, 0x384, 0x3E8)
    Sound(441, 0, 60, 0)
    OP_9D(0xFE, 0x717A, 0xFFFFE890, 0xFFFFC1E4, 0x12C, 0x3E8)
    Return()

    # Function_88_47A0 end

    SaveToFile()

Try(main)
