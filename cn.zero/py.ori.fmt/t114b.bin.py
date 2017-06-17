from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t114b.bin",                # FileName
        "t114b",                    # MapName
        "t114b",                    # Location
        0x0049,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 3, 0, 4],
    )

    BuildStringList((
        "t114b",                  # 0
        "雾香",                   # 1
        "马尔克尼会长",           # 2
        "哈尔特曼议长",           # 3
        "向导巴克雷",             # 4
        "管家克里斯托夫",         # 5
        "朱蒂",                   # 6
        "伊梅尔达夫人",           # 7
        "黑衣人",                 # 8
        "黑衣人",                 # 9
        "客人",                   # 10
        "客人",                   # 11
        "客人",                   # 12
        "客人",                   # 13
        "客人",                   # 14
        "客人",                   # 15
        "客人",                   # 16
        "客人",                   # 17
        "客人",                   # 18
        "客人",                   # 19
    ))

    AddCharChip((
        "chr/ch07302.itc",                   # 00
        "chr/ch06200.itc",                   # 01
        "chr/ch06500.itc",                   # 02
        "chr/ch25800.itc",                   # 03
        "chr/ch36200.itc",                   # 04
        "chr/ch36100.itc",                   # 05
        "chr/ch25900.itc",                   # 06
        "chr/ch25700.itc",                   # 07
        "chr/ch09002.itc",                   # 08
        "chr/ch33000.itc",                   # 09
        "chr/ch32400.itc",                   # 0A
        "chr/ch27702.itc",                   # 0B
        "chr/ch21600.itc",                   # 0C
        "chr/ch33300.itc",                   # 0D
        "chr/ch33002.itc",                   # 0E
        "chr/ch21800.itc",                   # 0F
        "chr/ch33100.itc",                   # 10
        "chr/ch27700.itc",                   # 11
        "chr/ch27900.itc",                   # 12
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

    DeclNpc(-5769,   150,     -18959,  90,   469,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-3500,   0,       2670,    90,   389,  0x0, 0,   1,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-4690,   0,       1710,    180,  389,  0x0, 0,   2,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-1350,   0,       3720,    135,  389,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(9,       0,       -24540,  0,    389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(2680,    0,       -18510,  180,  389,  0x0, 0,   7,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-5690,   0,       -12970,  90,   469,  0x0, 0,   8,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-1899,   0,       5139,    180,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1990,    0,       5139,    180,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(1200,    0,       -12069,  22,   389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4070,    0,       -10859,  265,  389,  0x0, 0,   18,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-5670,   150,     -949,    90,   469,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-5030,   0,       9,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2990,    0,       -12119,  336,  389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-910,    0,       -13859,  270,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-1970,   0,       -13859,  90,   389,  0x0, 0,   10,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(6389,    150,     -1009,   270,  469,  0x0, 0,   14,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(3880,    0,       -15199,  135,  389,  0x0, 0,   15,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4159,    0,       -22899,  135,  389,  0x0, 0,   16,  0,   0,   0,   0,   20,  255,  0)

    DeclEvent(0x0000, 0, 26,  0.0,                   -6.5,                  -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.1666667461395264,    0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 25,  -4.28000020980835,     2.509999990463257,     -1.0,                  6.25,                  [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.8560000658035278,    -0.5020000338554382,   0.20000000298023224,   1.0])

    ScpFunction((
        "Function_0_458",          # 00, 0
        "Function_1_510",          # 01, 1
        "Function_2_53B",          # 02, 2
        "Function_3_5C4",          # 03, 3
        "Function_4_71B",          # 04, 4
        "Function_5_755",          # 05, 5
        "Function_6_7AE",          # 06, 6
        "Function_7_993",          # 07, 7
        "Function_8_B41",          # 08, 8
        "Function_9_D7E",          # 09, 9
        "Function_10_1345",        # 0A, 10
        "Function_11_13B7",        # 0B, 11
        "Function_12_1426",        # 0C, 12
        "Function_13_16FC",        # 0D, 13
        "Function_14_17ED",        # 0E, 14
        "Function_15_1AEB",        # 0F, 15
        "Function_16_1D62",        # 10, 16
        "Function_17_1E6C",        # 11, 17
        "Function_18_1F71",        # 12, 18
        "Function_19_219C",        # 13, 19
        "Function_20_2383",        # 14, 20
        "Function_21_23FE",        # 15, 21
        "Function_22_2445",        # 16, 22
        "Function_23_248C",        # 17, 23
        "Function_24_2885",        # 18, 24
        "Function_25_36D5",        # 19, 25
        "Function_26_3A1F",        # 1A, 26
        "Function_27_47AD",        # 1B, 27
        "Function_28_47DD",        # 1C, 28
        "Function_29_483B",        # 1D, 29
    ))


    def Function_0_458(): pass

    label("Function_0_458")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_498"),
        (1, "loc_4A4"),
        (2, "loc_4B0"),
        (3, "loc_4BC"),
        (4, "loc_4C8"),
        (5, "loc_4D4"),
        (6, "loc_4E0"),
        (SWITCH_DEFAULT, "loc_4EC"),
    )


    label("loc_498")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4A4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4B0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4BC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4C8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4D4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_4F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4F8")

    label("loc_50F")

    Return()

    # Function_0_458 end

    def Function_1_510(): pass

    label("Function_1_510")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53A")
    OP_94(0xFE, 0xFFFFFCC2, 0xFFFFFCA4, 0x88E, 0x884, 0x3E8)
    Sleep(300)
    Jump("Function_1_510")

    label("loc_53A")

    Return()

    # Function_1_510 end

    def Function_2_53B(): pass

    label("Function_2_53B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C3")
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, -110, 0, -9870, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(1600)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, -940, 0, -14060, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, 820, 0, -5350, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Jump("Function_2_53B")

    label("loc_5C3")

    Return()

    # Function_2_53B end

    def Function_3_5C4(): pass

    label("Function_3_5C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_5D7")
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_709")

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_61D")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 820, 0, -5350, 315)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 650, 135)
    BeginChrThread(0xD, 0, 0, 1)
    Jump("loc_709")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_663")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 820, 0, -5350, 315)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 680, 0, 650, 135)
    BeginChrThread(0xD, 0, 0, 1)
    Jump("loc_709")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_6C4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    Event(0, 5)
    Jump("loc_709")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_709")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)

    label("loc_709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71A")
    Event(0, 23)

    label("loc_71A")

    Return()

    # Function_3_5C4 end

    def Function_4_71B(): pass

    label("Function_4_71B")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_738")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_754")

    label("loc_754")

    Return()

    # Function_4_71B end

    def Function_5_755(): pass

    label("Function_5_755")

    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x11, -3200, 0, 280, 315)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x15, -2040, 0, 1320, 315)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0x16, -1700, 0, 3200, 270)
    SetChrFlags(0x16, 0x10)
    OP_93(0x17, 0xB4, 0x0)
    Return()

    # Function_5_755 end

    def Function_6_7AE(): pass

    label("Function_6_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C4")
    Call(0, 24)
    Jump("loc_992")

    label("loc_7C4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_858")
    Jump("loc_8A2")

    label("loc_858")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_878")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A2")

    label("loc_878")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_898")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A2")

    label("loc_898")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8A2")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_918")

    #C0001
    ChrTalk(
        0x8,
        (
            "#3401F唔……\x01",
            "那就是哈尔特曼议长……\x02\x03",

            "看来是个很棘手的人物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98B")

    label("loc_918")


    #C0002
    ChrTalk(
        0x8,
        (
            "#3400F击溃这个黑之竞拍会\x01",
            "的契机……\x01",
            "说不定就近在咫尺。\x02\x03",

            "多观察观察，自行感受吧。\x01",
            "这样做一定会对你们有所帮助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98B")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)

    label("loc_992")

    Return()

    # Function_6_7AE end

    def Function_7_993(): pass

    label("Function_7_993")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_9A4")
    Jump("loc_B3D")

    label("loc_9A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_A11")

    #C0003
    ChrTalk(
        0xFE,
        (
            "客厅的收拾善后，\x01",
            "这样就算是告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "还要商量晚宴的相关事宜，\x01",
            "先到接待室\x01",
            "集合吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3D")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_A70")

    #C0005
    ChrTalk(
        0xFE,
        (
            "哎呀……客人，\x01",
            "您有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "老爷和其他宾客\x01",
            "都已经前往\x01",
            "竞拍会场了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3D")

    label("loc_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_AC6")

    #C0007
    ChrTalk(
        0xFE,
        (
            "哎呀，客人。\x01",
            "您是要额外点些什么菜吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "如有需要，\x01",
            "敬请吩咐……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3D")

    label("loc_AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B3D")

    #C0009
    ChrTalk(
        0xFE,
        (
            "各餐台的料理\x01",
            "都是由哈尔特曼府专职厨师\x01",
            "精心烹制的最高级菜肴。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "如果有什么需要，请不必客气，尽管吩咐。\x02",
    )

    CloseMessageWindow()

    label("loc_B3D")

    TalkEnd(0xFE)
    Return()

    # Function_7_993 end

    def Function_8_B41(): pass

    label("Function_8_B41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_B52")
    Jump("loc_D7A")

    label("loc_B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_C2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD8")

    #C0011
    ChrTalk(
        0xFE,
        (
            "这话可别说出去……\x01",
            "安排在院子里的看门狗\x01",
            "非常可怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "虽说是用于警备，\x01",
            "但毕竟是鲁巴彻商会的军犬……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C27")

    label("loc_BD8")


    #C0013
    ChrTalk(
        0xFE,
        (
            "安排在院子里的看门狗\x01",
            "非常可怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "万一不小心被咬到的话……\x01",
            "(发抖）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C27")

    Jump("loc_D7A")

    label("loc_C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_CA3")

    #C0015
    ChrTalk(
        0xFE,
        (
            "竞拍会即将开始，\x01",
            "站食餐会到此结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "竞拍会结束之后，\x01",
            "将在庭院内举办晚宴。\x01",
            "请各位务必赏光出席。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7A")

    label("loc_CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_D14")

    #C0017
    ChrTalk(
        0xFE,
        (
            "再过片刻，\x01",
            "竞拍会便将开场。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "随着竞拍会的开场，\x01",
            "站食餐会也将结束，\x01",
            "请趁现在尽情享用美食。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7A")

    label("loc_D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D7A")

    #C0019
    ChrTalk(
        0xFE,
        (
            "今晚的餐会\x01",
            "出于老爷的一番好意，\x01",
            "所有料理全部免费提供。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "请不必客气，\x01",
            "尽情享用美食。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7A")

    TalkEnd(0xFE)
    Return()

    # Function_8_B41 end

    def Function_9_D7E(): pass

    label("Function_9_D7E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E12")
    Jump("loc_E5C")

    label("loc_E12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E32")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E5C")

    label("loc_E32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E52")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E5C")

    label("loc_E52")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E5C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 1)), scpexpr(EXPR_END)), "loc_1035")

    #C0021
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀……\x01",
            "这张脸……好像曾在哪里见过呢。\x01",
            "嘻哈哈……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_EFE")

    #C0022
    ChrTalk(
        0x101,
        "#5105F伊梅尔达夫人！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F27")

    label("loc_EFE")


    #C0023
    ChrTalk(
        0x101,
        (
            "#5105F您是……\x01",
            "那家古董店的……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_F57")

    #C0024
    ChrTalk(
        0x102,
        "#5305F您怎么会在这里……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FBF")

    label("loc_F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_F85")

    #C0025
    ChrTalk(
        0x103,
        "#5405F……您为何会在这里？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FBF")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_FBF")

    #C0026
    ChrTalk(
        0x104,
        (
            "#5606F喂喂！\x01",
            "老婆婆，你怎么会在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBF")


    #C0027
    ChrTalk(
        0xFE,
        (
            "我通过某条门路得到了邀请函。\x01",
            "然后出于兴趣，就来看看了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#5106F（还是老样子，真是个可疑的老婆婆啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_11C4")

    label("loc_1035")


    #C0029
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀……\x01",
            "你们莫非\x01",
            "是警察局的人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x101,
        "#5105F您怎么会知……！？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "嘻哈哈……\x01",
            "果然是啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "我啊，\x01",
            "在克洛斯贝尔市\x01",
            "经营古董店哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔时代周刊上\x01",
            "看到过你们的报道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#5106F即、即使如此，\x01",
            "您又为何会在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "我通过某条门路得到了邀请函。\x01",
            "然后出于兴趣，就来看看了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#5106F（真是个超级可疑的老婆婆啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_11C4")


    #C0037
    ChrTalk(
        0x101,
        (
            "#5101F……那、那个，\x01",
            "关于我们的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "嘻哈哈……\x01",
            "不用担心，我不会告密的。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "在四处都是恶党的地方\x01",
            "有几个你们这样的人，\x01",
            "也挺有意思的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 2)
    Jump("loc_133D")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_12E7")

    #C0040
    ChrTalk(
        0xFE,
        (
            "马尔克尼那小子，每次见他，\x01",
            "都觉得更有坏狸猫的样子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "不光是行为举止，\x01",
            "连外表都和狸猫一模一样嘛。\x01",
            "嘻哈哈……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_12E7")


    #C0042
    ChrTalk(
        0xFE,
        (
            "因为有想要的拍卖品，\x01",
            "所以就来看看了……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "看来事情会变得很有趣呢。\x01",
            "嘻哈哈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_D7E end

    def Function_10_1345(): pass

    label("Function_10_1345")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_13B3")

    #C0044
    ChrTalk(
        0xFE,
        (
            "（老大和哈尔特曼议长\x01",
            "  似乎心情很好……）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        "（如果能这么顺利结束，就最好不过了……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B3")

    label("loc_13B3")

    TalkEnd(0xFE)
    Return()

    # Function_10_1345 end

    def Function_11_13B7(): pass

    label("Function_11_13B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1422")

    #C0046
    ChrTalk(
        0xFE,
        "（盯着看）………………\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "……失礼了。\x01",
            "为了确保万无一失，\x01",
            "我正在全力进行安保工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1422")

    label("loc_1422")

    TalkEnd(0xFE)
    Return()

    # Function_11_13B7 end

    def Function_12_1426(): pass

    label("Function_12_1426")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1589")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xFE, 0)

    #C0048
    ChrTalk(
        0xFE,
        (
            "……哎呀，那时多亏您行了个方便，\x01",
            "实在是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "托您的福，记者们\x01",
            "也都没捞到什么情报，\x01",
            "让我可以安心度日了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        (
            "#2700F哈哈……那就最好了。\x02\x03",

            "#2703F嗯，只要我还在政府中担任此职，\x01",
            "自然会助各位一臂之力。\x02\x03",

            "#2702F毕竟今后还要仰仗各位\x01",
            "在背后多多支持我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "哇哈哈，议长考虑得果然周全长远啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_4C(0xA, 0xFF)
    TurnDirection(0xA, 0x14, 0)
    Jump("loc_1612")

    label("loc_1589")


    #C0052
    ChrTalk(
        0xFE,
        (
            "这个宴会，我曾经\x01",
            "受邀参加过好几次了，\x01",
            "今年似乎准备得尤为用心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "呵呵，这也可以看出您平日的活跃，\x01",
            "希望您今后能有更大的发展啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1612")

    Jump("loc_16F8")

    label("loc_1617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169D")

    #C0054
    ChrTalk(
        0xFE,
        (
            "听说今天的\x01",
            "拍卖品里藏着\x01",
            "超级好货啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "据说是相当贵重的物品……\x01",
            "该不会是那个有名的『怪盗Ｂ』\x01",
            "偷来的物品吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16F8")

    label("loc_169D")


    #C0056
    ChrTalk(
        0xFE,
        (
            "听说今天的\x01",
            "拍卖品里藏着\x01",
            "超级好货啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "据说是相当贵重的物品……\x01",
            "你觉得会是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F8")

    TalkEnd(0xFE)
    Return()

    # Function_12_1426 end

    def Function_13_16FC(): pass

    label("Function_13_16FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_178C")

    #C0058
    ChrTalk(
        0xFE,
        (
            "嗯，话说回来，\x01",
            "今天的竞拍会真令人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "虽然不知道具体会有些\x01",
            "什么样的拍卖品……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "但一定都是些\x01",
            "很有魅力的商品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E9")

    label("loc_178C")


    #C0061
    ChrTalk(
        0xFE,
        (
            "你们似乎还\x01",
            "不太习惯\x01",
            "竞拍会这种活动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "呵呵……那种紧张感，\x01",
            "一旦陷进去就会上瘾的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E9")

    TalkEnd(0xFE)
    Return()

    # Function_13_16FC end

    def Function_14_17ED(): pass

    label("Function_14_17ED")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1881")
    Jump("loc_18CB")

    label("loc_1881")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18A1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18CB")

    label("loc_18A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18C1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18CB")

    label("loc_18C1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18CB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1A5B")
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F2")

    #C0063
    ChrTalk(
        0xFE,
        (
            "哈尔特曼议长，\x01",
            "初次见面，真是幸会啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "这次承蒙您的招待，\x01",
            "感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "#2705F哦，您是共和国议员……\x02\x03",

            "#2700F我也早就想\x01",
            "见您一面了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "呵呵……是吗。\x01",
            "那么，我可以期待\x01",
            "今后的良好关系吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        "#2702F嗯……那当然了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A52")

    label("loc_19F2")


    #C0068
    ChrTalk(
        0xFE,
        (
            "呵呵……其实我今天还给您\x01",
            "准备了一份薄礼。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "等竞拍会结束之后，\x01",
            "希望能去您的房间详谈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A52")

    OP_4C(0xA, 0xFF)
    Jump("loc_1AE3")

    label("loc_1A5B")


    #C0070
    ChrTalk(
        0xFE,
        (
            "据说这间宅邸的主人哈尔特曼议长\x01",
            "在帝国都拥有很强的影响力。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "今天要是能想办法\x01",
            "和他拉上关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "呵呵，我将来也就高枕无忧了。\x02",
    )

    CloseMessageWindow()

    label("loc_1AE3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_17ED end

    def Function_15_1AEB(): pass

    label("Function_15_1AEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1C1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB6")
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xFE, 0)

    #C0073
    ChrTalk(
        0xFE,
        "我对两位的将来也抱有很高的期望。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "可千万不要搞砸，\x01",
            "让警察局的走狗\x01",
            "抓住破绽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#3000F哈哈哈，您真严厉。\x02\x03",

            "请放心，我们一定会\x01",
            "小心行事的。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    TurnDirection(0x9, 0x16, 0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C17")

    label("loc_1BB6")


    #C0076
    ChrTalk(
        0xFE,
        (
            "哼，警察局的走狗\x01",
            "根本就无法揭发\x01",
            "这场竞拍会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "哈哈哈……\x01",
            "不过，多少还是要防备一下的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C17")

    Jump("loc_1D5E")

    label("loc_1C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D07")

    #C0078
    ChrTalk(
        0xFE,
        (
            "每次来克洛斯贝尔，我都能\x01",
            "深深体会到警察的无能啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "连这种规模盛大的\x01",
            "竞拍会，竟然都能够\x01",
            "在举办时瞒过公众的耳目啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "这也是因为哈尔特曼议长\x01",
            "拥有绝对的权威力量吗。\x01",
            "哈哈哈……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        "#5101F（……呜…………！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D5E")

    label("loc_1D07")


    #C0082
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的警察\x01",
            "真是无能啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "不过多亏如此，\x01",
            "我们才能有这些乐子。\x01",
            "哈哈哈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5E")

    TalkEnd(0xFE)
    Return()

    # Function_15_1AEB end

    def Function_16_1D62(): pass

    label("Function_16_1D62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1DF8")

    #C0084
    ChrTalk(
        0xFE,
        (
            "呵呵……今天一定要\x01",
            "顺利拍下漂亮的珠宝饰品，\x01",
            "意气风发地迎来晚宴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "真期待能出现不逊于去年拍下的\x01",
            "那枚翠耀石戒指的拍卖品啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E68")

    label("loc_1DF8")


    #C0086
    ChrTalk(
        0xFE,
        (
            "喏，你看，\x01",
            "这是我在去年的竞拍会中\x01",
            "拍下的翠耀石戒指。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "呵呵……今年我一定会\x01",
            "拍下比这更美的\x01",
            "珠宝首饰哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E68")

    TalkEnd(0xFE)
    Return()

    # Function_16_1D62 end

    def Function_17_1E6C(): pass

    label("Function_17_1E6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1EE8")

    #C0088
    ChrTalk(
        0xFE,
        (
            "不知今年会展出什么\x01",
            "带有内情的商品啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "珠宝这种东西很不可思议，\x01",
            "越是来路可疑，\x01",
            "就越是绚丽夺目呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F6D")

    label("loc_1EE8")


    #C0090
    ChrTalk(
        0xFE,
        (
            "听说哈尔特曼议长\x01",
            "还与那个『铁血宰相』\x01",
            "有所来往呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "不愧是出身于和帝国贵族有关的名门……\x01",
            "交友关系也和一般人不在一个境界啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F6D")

    TalkEnd(0xFE)
    Return()

    # Function_17_1E6C end

    def Function_18_1F71(): pass

    label("Function_18_1F71")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2005")
    Jump("loc_204F")

    label("loc_2005")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2025")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_204F")

    label("loc_2025")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2045")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_204F")

    label("loc_2045")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_204F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_20F9")

    #C0092
    ChrTalk(
        0xFE,
        (
            "哼，那个处事圆滑的马尔克尼……\x01",
            "不过就是哈尔特曼议长养的一条狗，\x01",
            "居然还得意忘形起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "好好当心\x01",
            "不要失足吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2194")

    label("loc_20F9")


    #C0094
    ChrTalk(
        0xFE,
        (
            "负责宅邸警备的黑衣人……\x01",
            "好像是鲁巴彻商会的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "马尔克尼那个男人\x01",
            "还真会讨好\x01",
            "哈尔特曼议长啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "哼，走着瞧吧，\x01",
            "我很快就会超过\x01",
            "那条跟班狗的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2194")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_1F71 end

    def Function_19_219C(): pass

    label("Function_19_219C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_21F6")

    #C0097
    ChrTalk(
        0xFE,
        (
            "哈尔特曼议长……\x01",
            "去和他混个脸熟总没坏处。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "好，我去打个招呼吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_237F")

    label("loc_21F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2323")

    #C0099
    ChrTalk(
        0xFE,
        (
            "唔，你们看起来似乎很年轻啊……\x01",
            "既然受邀来这里，\x01",
            "就一定是贵族或者富豪吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "如果不介意的话，\x01",
            "能不能将二位的身份\x01",
            "告诉我呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#5105F呃，这个……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……哈哈，果然很紧张吗？\x01",
            "这么年轻，紧张也是在所难免的。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "在这种场合揣测别人的身份，\x01",
            "本来也有点不识趣啊。\x01",
            "请原谅我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_237F")

    label("loc_2323")


    #C0104
    ChrTalk(
        0xFE,
        (
            "呵呵……这里的宾客，无论是老是少，\x01",
            "都不是等闲之辈啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "好……\x01",
            "我去逐一打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_237F")

    TalkEnd(0xFE)
    Return()

    # Function_19_219C end

    def Function_20_2383(): pass

    label("Function_20_2383")

    TalkBegin(0xFE)

    #C0106
    ChrTalk(
        0xFE,
        "军犬怎么会在宅子里面……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "喂、喂！\x01",
            "这骚动到底是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "要是我有个三长两短，\x01",
            "后果可是很严重的啊！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2383 end

    def Function_21_23FE(): pass

    label("Function_21_23FE")

    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    Return()

    # Function_21_23FE end

    def Function_22_2445(): pass

    label("Function_22_2445")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    Return()

    # Function_22_2445 end

    def Function_23_248C(): pass

    label("Function_23_248C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -600, 0, 4250, 180)
    SetChrPos(0xEF, 600, 0, 4250, 180)
    Call(0, 22)
    FadeToBright(1000, 0)
    OP_68(0, 1300, -21000, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18490, 0)
    OP_68(0, 1300, 4000, 12000)
    OP_6F(0x1)
    OP_0D()

    #C0109
    ChrTalk(
        0x101,
        (
            "#5101F#5P站食形式的宴会吗……\x02\x03",

            "似乎来了\x01",
            "很多宾客。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_262F")
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)

    #C0110
    ChrTalk(
        0x102,
        (
            "#5306F#11P看上去，菜肴和酒\x01",
            "都很豪华啊……\x02\x03",

            "#5301F一定是雇了\x01",
            "一流的厨师吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)

    #C0111
    ChrTalk(
        0x101,
        (
            "#5106F#5P如果不是在这种情况下，\x01",
            "我肯定会很开心地享受美食……\x02\x03",

            "但现在好紧张，都没食欲了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        "#5302F#11P呵呵，这也难怪嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2868")

    label("loc_262F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_272B")

    #C0113
    ChrTalk(
        0x103,
        (
            "#5405F#11P这里的菜肴好像都\x01",
            "十分豪华呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)

    #C0114
    ChrTalk(
        0x103,
        "#11P#5402F罗伊德前辈，要吃点什么吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)

    #C0115
    ChrTalk(
        0x101,
        (
            "#5106F#5P不，我太紧张了，\x01",
            "都没什么食欲呢。\x02\x03",

            "#5100F缇欧，要不\x01",
            "我去帮你拿点什么来吃吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        (
            "#5404F#11P不必了，我也不是\x01",
            "特别饿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2868")

    label("loc_272B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2868")

    #C0117
    ChrTalk(
        0x104,
        (
            "#5607F#11P啊～满眼都是\x01",
            "豪华的美酒和料理啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)

    #C0118
    ChrTalk(
        0x104,
        (
            "#11P#5602F嘿，罗伊德。\x01",
            "稍微吃一点也没关系吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)

    #C0119
    ChrTalk(
        0x101,
        (
            "#5106F#5P吃东西是可以……\x01",
            "但是绝对不准喝酒哦。\x02\x03",

            "#5101F还不知道接下来会出现什么情况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        (
            "#5606F#11P唔……那还是算了吧。\x02\x03",

            "#5601F这么豪华的料理，如果不喝酒光吃的话，\x01",
            "也许会更难忍受呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2868")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 5100, 180)
    SetScenarioFlags(0xA5, 2)
    Call(0, 21)
    EventEnd(0x5)
    Return()

    # Function_23_248C end

    def Function_24_2885(): pass

    label("Function_24_2885")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-3990, 1800, -19530, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(18500, 2500)
    SetChrPos(0x101, -4070, 0, -18880, 270)
    SetChrPos(0xEF, -3880, 0, -17470, 225)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03400.itp")
    Sleep(2000)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x8,
        "#3405F#5P哎呀……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x101,
        "#5105F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_29B9")

    #C0123
    ChrTalk(
        0x102,
        "#5305F#12P雾香小姐……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A17")

    label("loc_29B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_29E3")

    #C0124
    ChrTalk(
        0x103,
        "#5405F#12P您是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A17")

    label("loc_29E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2A17")

    #C0125
    ChrTalk(
        0x104,
        (
            "#5605F#12P噢噢！？\x01",
            "这不是雾香小姐吗！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A17")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0126
    AnonymousTalk(
        0x8,
        (
            "呵呵……真是巧遇啊。\x02\x03",

            "实在是出乎意料，\x01",
            "竟然会在这里见到你们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0127
    ChrTalk(
        0x101,
        "#5112F#12P这、这个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2B11")

    #C0128
    ChrTalk(
        0x102,
        "#5306F#12P那个，这是出于各种原因……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2B43")

    #C0129
    ChrTalk(
        0x103,
        "#5403F#12P因为有着种种内情……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2B7D")

    #C0130
    ChrTalk(
        0x104,
        (
            "#5609F#12P哎呀～其实稍微有那么\x01",
            "一点隐情……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7D")


    #C0131
    ChrTalk(
        0x8,
        (
            "#3404F#5P呵呵，也罢。\x02\x03",

            "#3402F──那么，在这个会场中，\x01",
            "要用什么名字来称呼你呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0132
    ChrTalk(
        0x101,
        "#5111F#12P哎……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2C59")

    #C0133
    ChrTalk(
        0x102,
        "#5301F#12P为、为什么会连这件事都……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CC0")

    label("loc_2C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2C8F")

    #C0134
    ChrTalk(
        0x103,
        "#5401F#12P……为什么您连这点都……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CC0")

    label("loc_2C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2CC0")

    #C0135
    ChrTalk(
        0x104,
        "#5606F#12P这、这真是突然袭击啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2CC0")


    #C0136
    ChrTalk(
        0x8,
        (
            "#3404F#5P考虑到你们的立场，\x01",
            "大概能想象到你们在做什么。\x02\x03",

            "而且，在递交邀请卡的时候，\x01",
            "也需要报上代表者的名字……\x02\x03",

            "#3402F那么，怎么称呼你比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0137
    ChrTalk(
        0x101,
        "#5106F#12P……请叫我盖伊吧。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "#3404F#5P呵呵……明白了，盖伊。\x02\x03",

            "#3400F你们直接叫我\x01",
            "雾香就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#5103F#12P好、好的。\x02\x03",

            "#5101F说起来……雾香小姐，\x01",
            "您怎么会在这里？\x02\x03",

            "是冲着拍卖品来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "#3404F#5P呵呵，我出于职业原因，\x01",
            "认识了不少好事的人。\x02\x03",

            "那些人拜托我\x01",
            "来确认一下，看看这里\x01",
            "都有些什么拍卖品。\x02\x03",

            "#3400F嗯，可以算是市场调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#5106F#12P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#3404F#5P说起来，那个叫哈尔特曼的议长，\x01",
            "还真是个毫无破绽的人物呢。\x02\x03",

            "这场竞拍会……\x01",
            "就组织形式来说十分巧妙。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#5105F#12P十分巧妙……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2FB6")

    #C0144
    ChrTalk(
        0x102,
        "#5305F#12P这话怎么说呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3009")

    label("loc_2FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2FE2")

    #C0145
    ChrTalk(
        0x103,
        "#5405F#12P……此话怎讲？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3009")

    label("loc_2FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3009")

    #C0146
    ChrTalk(
        0x104,
        "#5605F#12P这话怎么说啊？\x02",
    )

    CloseMessageWindow()

    label("loc_3009")


    #C0147
    ChrTalk(
        0x8,
        (
            "#3400F#5P这种专为上流阶级举办，\x01",
            "绝不会被揭发的地下竞拍会……\x02\x03",

            "对各国的有权人士而言，\x01",
            "实在是个方便的好地方。\x02\x03",

            "#3403F展品中除了单纯的赃物以外，还有贿赂品，\x01",
            "以及为了筹集资金而转手的倒卖品……\x02\x03",

            "这些东西，如果在本国卖出，\x01",
            "必然免不了被依法检举。\x02\x03",

            "#3402F但是，在这克洛斯贝尔，\x01",
            "却可以被人『视而不见』。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        "#5113F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "#3404F#5P正因如此，帝国和共和国\x01",
            "都默许了这个竞拍会呢。\x02\x03",

            "在这次的拍卖品之中，\x01",
            "恐怕也有几件那样的东西吧。\x02\x03",

            "#3400F从两国的政府相关人士那里\x01",
            "收购来的『特别处理品』……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#5110F#12P呜……\x02\x03",

            "也就是说，这里算是国际上\x01",
            "默许的黑市吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3273")

    #C0151
    ChrTalk(
        0x102,
        (
            "#5306F#12P听您这么一说，\x01",
            "还真是耸人听闻啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F4")

    label("loc_3273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_32B4")

    #C0152
    ChrTalk(
        0x103,
        (
            "#5406F#12P听您这么一说，\x01",
            "还真是相当卑劣呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F4")

    label("loc_32B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_32F4")

    #C0153
    ChrTalk(
        0x104,
        (
            "#5608F#12P哎呀，听您这么一说，\x01",
            "还真是骇人听闻啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F4")


    #C0154
    ChrTalk(
        0x8,
        (
            "#3404F#5P当然，这种形式也可以说是\x01",
            "克洛斯贝尔的特色产物。\x02\x03",

            "#3400F对你们来说，这种现状也许确实\x01",
            "很令人懊恼……\x02\x03",

            "但要想做出改变，实在很难呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#5108F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_33D9")

    #C0156
    ChrTalk(
        0x102,
        "#5308F#11P……罗伊德……\x02",
    )

    CloseMessageWindow()
    Jump("loc_342E")

    label("loc_33D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3405")

    #C0157
    ChrTalk(
        0x103,
        "#5408F#11P罗伊德前辈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_342E")

    label("loc_3405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_342E")

    #C0158
    ChrTalk(
        0x104,
        "#5603F#12P……哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    label("loc_342E")


    #C0159
    ChrTalk(
        0x8,
        (
            "#3400F#5P呵呵……\x02\x03",

            "#3404F──只是，就算安排得再巧妙，\x01",
            "这种形式终究也是不自然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#5105F#12P哎……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#3404F#5P万物的存在都基于气之流动\x01",
            "与调和……\x02\x03",

            "扭曲之物，如果一直扭曲下去，\x01",
            "便绝不会长久。\x02\x03",

            "只要出现合适的契机……\x01",
            "何时崩溃也都不足为奇。\x02\x03",

            "#3400F从这层意义上来说，你们的努力\x01",
            "或许并不会白费。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#5102F#12P雾香小姐……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_35BC")

    #C0163
    ChrTalk(
        0x102,
        (
            "#5304F#12P……听您这么一说，\x01",
            "让我们倍受鼓励呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362A")

    label("loc_35BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_35EE")

    #C0164
    ChrTalk(
        0x103,
        "#5404F#12P……感觉很受鼓舞呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_362A")

    label("loc_35EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_362A")

    #C0165
    ChrTalk(
        0x104,
        (
            "#5609F#12P哎呀，您这么一说，\x01",
            "犹如百人助阵啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362A")


    #C0166
    ChrTalk(
        0x8,
        (
            "#3404F#5P呵呵，我似乎\x01",
            "说得太多了呢。\x02\x03",

            "#3400F机会难得，\x01",
            "你们就到处看看吧。\x02\x03",

            "这样做一定会\x01",
            "对你们有所帮助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#5100F#12P是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -4450, 0, -18670, 90)
    OP_CA(0x1, 0xFF, 0x0)
    ModifyEventFlags(1, 0, 0x80)
    SetScenarioFlags(0xA5, 3)
    EventEnd(0x5)
    Return()

    # Function_24_2885 end

    def Function_25_36D5(): pass

    label("Function_25_36D5")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4210, 1200, 2390, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(22400, 0)
    SetChrPos(0x101, -990, 0, -870, 315)
    SetChrPos(0xEF, -150, 0, -530, 315)
    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3828")

    #C0168
    ChrTalk(
        0xA,
        (
            "#2703F#11P……各位嘉宾，\x01",
            "拍卖一旦正式开始，\x01",
            "大家就都是竞争对手了……\x02\x03",

            "#2702F请利用这短暂的时间和睦相处，\x01",
            "加深彼此的友谊吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "#3002F#5P今晚也将有众多\x01",
            "罕见的珍品参与拍卖。\x02\x03",

            "恭祝各位好运连连，\x01",
            "都能顺利拍到自己心仪的物品！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38DB")

    label("loc_3828")


    #C0170
    ChrTalk(
        0xA,
        (
            "#2702F#11P……除了竞拍以外，\x01",
            "还为大家准备了各种娱乐消遣。\x02\x03",

            "长夜漫漫，\x01",
            "希望大家过得开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "#3004F#5P嗯，正是正是！\x02\x03",

            "#3002F让大家过得开心，\x01",
            "正是举办这场竞拍会\x01",
            "的意义所在！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38DB")

    Fade(500)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_68(-150, 1500, -1390, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C5")

    #C0172
    ChrTalk(
        0x101,
        (
            "#5113F（帝国派的哈尔特曼议长\x01",
            "  和鲁巴彻的马尔克尼会长吗……)\x02\x03",

            "#5106F（虽然很想与他们谈话，趁机探探底细……\x01",
            "  不过，在目前的情况下，还是尽量远离为好吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A08")

    label("loc_39C5")


    #C0173
    ChrTalk(
        0x101,
        (
            "#5103F（说不定有人会认出我们，\x01",
            "  现在还是离远一点比较好吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A08")

    SetChrPos(0x0, -990, 0, -870, 315)
    SetScenarioFlags(0xB4, 3)
    EventEnd(0x5)
    Return()

    # Function_25_36D5 end

    def Function_26_3A1F(): pass

    label("Function_26_3A1F")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -1830, 0, -7850, 0)
    SetChrPos(0xEF, -2480, 0, -8680, 0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 110, 0, 3900, 180)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x40)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 6500, 180)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 0, 6500, 180)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Call(0, 22)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02700.itp")
    OP_68(-940, 1700, -9470, 0)
    MoveCamera(312, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16360, 0)
    SetCameraDistance(15360, 2000)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0174
    ChrTalk(
        0x101,
        "#5105F#6P那是……\x02",
    )

    CloseMessageWindow()
    OP_68(2120, 1700, 2009, 2500)
    SetCameraDistance(15000, 2500)
    OP_6F(0x79)
    Sleep(300)

    #C0175
    ChrTalk(
        0xB,
        "#11P各位来宾……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xB,
        (
            "#11P本竞拍会的主办者已经到场，\x01",
            "请他们为大家致辞。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-1340, 1700, -8920, 0)
    MoveCamera(312, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16690, 0)
    SetChrSubChip(0x8, 0x1)
    SetChrSubChip(0xE, 0x1)
    OP_93(0x11, 0x0, 0x0)
    OP_93(0x12, 0x0, 0x0)
    SetChrSubChip(0x13, 0x1)
    OP_93(0x15, 0x0, 0x0)
    OP_93(0x16, 0x0, 0x0)
    OP_93(0x17, 0x0, 0x0)
    SetChrSubChip(0x18, 0x2)
    OP_93(0x19, 0x0, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(919, 0, 100, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(1520, 1700, 2340, 0)
    MoveCamera(312, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13500, 0)
    OP_68(1520, 1700, 1340, 5000)
    BeginChrThread(0xB, 3, 0, 27)
    Sleep(1000)
    BeginChrThread(0x9, 3, 0, 28)
    Sleep(1000)
    BeginChrThread(0xA, 3, 0, 29)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x1)

    #C0177
    ChrTalk(
        0x101,
        "#5107F#N（那就是……！）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3DA5")

    #C0178
    ChrTalk(
        0x102,
        (
            "#5303F#N（嗯……）\x02\x03",

            "#5301F（是鲁巴彻的会长\x01",
            "  和哈尔特曼议长呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E52")

    label("loc_3DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3DF8")

    #C0179
    ChrTalk(
        0x103,
        (
            "#5401F#N（难不成……）\x02\x03",

            "（是黑手党的会长\x01",
            "  和帝国派的议长吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E52")

    label("loc_3DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3E52")

    #C0180
    ChrTalk(
        0x104,
        (
            "#5603F#N（原来如此……）\x02\x03",

            "#5600F（那就是黑手党的会长\x01",
            "  和帝国派的议长啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E52")

    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0181
    AnonymousTalk(
        0x9,
        (
            "──各位，晚上好！\x02\x03",

            "我是本次竞拍会的主办者，\x01",
            "鲁巴彻商会的马尔克尼。\x02\x03",

            "时光飞逝，本竞拍会\x01",
            "在今年也迎来了第八届。\x02\x03",

            "每年的到场来宾都有增无减，\x01",
            "与之相应，参展的拍卖物品\x01",
            "也越来越丰富充实。\x02\x03",

            "正是因为有了各位的理解和支持，\x01",
            "我们才会迎来如今的盛况！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sound(884, 0, 100, 0)
    Sleep(2000)

    #C0182
    ChrTalk(
        0x9,
        (
            "#3004F#11P此外，还有一位贵人……\x02\x03",

            "每年都会提供这座\x01",
            "豪华的宅邸，\x01",
            "作为我们的活动会场。\x02\x03",

            "#3002F请允许我为大家介绍──\x01",
            "克洛斯贝尔自治州的代表，\x01",
            "统领自治州议会的大政治家……\x02\x03",

            "哈尔特曼议长阁下！\x02",
        )
    )

    CloseMessageWindow()
    Sound(884, 0, 100, 0)
    OP_68(2120, 1700, 1340, 2000)

    def lambda_4095():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4095)
    WaitChrThread(0xA, 1)
    Sound(920, 0, 100, 0)
    OP_6F(0x1)
    Sleep(1500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0183
    AnonymousTalk(
        0xA,
        (
            "──我就是承蒙介绍的\x01",
            "自治州议长哈尔特曼。\x02\x03",

            "今晚能为这场华美的盛典\x01",
            "提供场地，我感到不胜荣幸。\x02\x03",

            "本次活动并不仅仅是竞拍会，\x01",
            "同时也可说是各界名流相聚、\x01",
            "联欢，以及邂逅的宴会。\x02\x03",

            "夜晚才刚刚开始……\x01",
            "在竞拍会结束之后，\x01",
            "我们还准备了一场小小的晚宴。\x02\x03",

            "请各位将本馆\x01",
            "当成自己的家，\x01",
            "尽情放松享受吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sound(884, 0, 100, 0)
    Sleep(500)
    Sound(920, 0, 100, 0)
    Sleep(2000)
    Fade(1000)
    OP_68(-1340, 1700, -8920, 0)
    MoveCamera(312, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16690, 0)
    SetChrPos(0xEF, -2430, 0, -8620, 0)
    OP_0D()
    Sleep(500)

    #C0184
    ChrTalk(
        0x101,
        (
            "#5113F#6P（那就是马尔克尼会长\x01",
            "  和哈尔特曼议长吗……）\x02\x03",

            "#5106F（那个议长的气势很威严，\x01",
            "  真不愧是个大政治家啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_43B0")

    #C0185
    ChrTalk(
        0x102,
        (
            "#5308F#6P（……因为他确信\x01",
            "  自己的权威\x01",
            "  是不可动摇的吧。）\x02\x03",

            "#5301F（鲁巴彻的会长\x01",
            "  还是第一次见到……）\x02\x03",

            "（感觉要比想象中\x01",
            "  更加狡猾精干呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44CC")

    label("loc_43B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_443B")

    #C0186
    ChrTalk(
        0x103,
        (
            "#5406F#6P（……感觉他是那种对自己的至高地位\x01",
            "  毫无置疑的类型呢。）\x02\x03",

            "#5411F（鲁巴彻的会长……\x01",
            "  看上去似乎狡猾又顽强。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44CC")

    label("loc_443B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_44CC")

    #C0187
    ChrTalk(
        0x104,
        (
            "#5606F#6P（对自己的权威\x01",
            "  没有半点怀疑……\x01",
            "  是大贵族中常有的类型吧。）\x02\x03",

            "#5601F（至于鲁巴彻的会长，\x01",
            "  是只厉害又狡猾的老狸猫吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44CC")


    #C0188
    ChrTalk(
        0x101,
        (
            "#5103F#6P（嗯……\x01",
            "  他们两个都是不可小觑的角色呢。）\x02\x03",

            "#5101F（原本还打算尽量去和他们接触一下……\x01",
            "  但现在看来，还是谨慎一点为好啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_45C2")

    #C0189
    ChrTalk(
        0x102,
        (
            "#5306F#6P（嗯，我毕竟和\x01",
            "  议长算是认识……）\x02\x03",

            "#5300F（最好还是避免\x01",
            "  与他直接接触哦。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4694")

    label("loc_45C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_462D")

    #C0190
    ChrTalk(
        0x103,
        (
            "#5403F#6P（……君子不入险地。）\x02\x03",

            "#5400F（或许还是该避免引起他们的注意，偷偷离开为好。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4694")

    label("loc_462D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4694")

    #C0191
    ChrTalk(
        0x104,
        (
            "#5604F#6P（正面接触的话，\x01",
            "  风险未免也太高了吧。）\x02\x03",

            "#5600F（还是不要张扬，偷偷离开吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4694")


    #C0192
    ChrTalk(
        0x101,
        (
            "#5100F#6P（明白了……\x01",
            "  不动声色地离开客厅吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -1770, 0, -8090, 0)
    SetChrPos(0x9, -3500, 0, 2670, 90)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x40)
    OP_4C(0x9, 0xFF)
    SetChrPos(0xA, -4690, 0, 1710, 180)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x40)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xB, -1350, 0, 3720, 135)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x40)
    OP_4C(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_93(0x11, 0x16, 0x0)
    OP_93(0x12, 0x109, 0x0)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x15, 0x150, 0x0)
    OP_93(0x16, 0x5A, 0x0)
    OP_93(0x17, 0x10E, 0x0)
    SetChrSubChip(0x18, 0x0)
    OP_93(0x19, 0x87, 0x0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 3)
    Call(0, 21)
    Call(0, 5)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetScenarioFlags(0xA5, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_26_3A1F end

    def Function_27_47AD(): pass

    label("Function_27_47AD")


    def lambda_47B2():
        OP_95(0xFE, -1310, 0, 3350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47B2)
    WaitChrThread(0xFE, 1)

    def lambda_47D0():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47D0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_47AD end

    def Function_28_47DD(): pass

    label("Function_28_47DD")


    def lambda_47E2():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47E2)

    def lambda_47F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_47F7)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_4810():
        OP_95(0xFE, 0, 0, 2810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4810)
    WaitChrThread(0xFE, 1)

    def lambda_482E():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_482E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_47DD end

    def Function_29_483B(): pass

    label("Function_29_483B")


    def lambda_4840():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4840)

    def lambda_4855():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4855)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_486E():
        OP_95(0xFE, 1200, 0, 3860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_486E)
    WaitChrThread(0xFE, 1)

    def lambda_488C():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_488C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_483B end

    SaveToFile()

Try(main)
