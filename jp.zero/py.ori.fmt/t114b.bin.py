from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "キリカ",                 # 1
        "マルコーニ会長",         # 2
        "ハルトマン議長",         # 3
        "案内人バークレイ",       # 4
        "執事クリストフ",         # 5
        "ジュディ",               # 6
        "イメルダ夫人",           # 7
        "黒服",                   # 8
        "黒服",                   # 9
        "招待客",                 # 10
        "招待客",                 # 11
        "招待客",                 # 12
        "招待客",                 # 13
        "招待客",                 # 14
        "招待客",                 # 15
        "招待客",                 # 16
        "招待客",                 # 17
        "招待客",                 # 18
        "招待客",                 # 19
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
        "Function_7_9BD",          # 07, 7
        "Function_8_BE3",          # 08, 8
        "Function_9_ECB",          # 09, 9
        "Function_10_155A",        # 0A, 10
        "Function_11_15D8",        # 0B, 11
        "Function_12_164F",        # 0C, 12
        "Function_13_19EF",        # 0D, 13
        "Function_14_1B0E",        # 0E, 14
        "Function_15_1E96",        # 0F, 15
        "Function_16_2187",        # 10, 16
        "Function_17_22E5",        # 11, 17
        "Function_18_2412",        # 12, 18
        "Function_19_2689",        # 13, 19
        "Function_20_28A6",        # 14, 20
        "Function_21_292D",        # 15, 21
        "Function_22_2974",        # 16, 22
        "Function_23_29BB",        # 17, 23
        "Function_24_2E38",        # 18, 24
        "Function_25_3E25",        # 19, 25
        "Function_26_41C9",        # 1A, 26
        "Function_27_5135",        # 1B, 27
        "Function_28_5165",        # 1C, 28
        "Function_29_51C3",        # 1D, 29
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
    Jump("loc_9BC")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_924")

    #C0001
    ChrTalk(
        0x8,
        (
            "#3401Fふむ……\x01",
            "あれがハルトマン議長……\x02\x03",

            "なかなか手強そうな人物のようね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B5")

    label("loc_924")


    #C0002
    ChrTalk(
        0x8,
        (
            "#3400Fこの闇の競売会を\x01",
            "突き崩すきっかけ……\x01",
            "案外近くにあるかもしれない。\x02\x03",

            "色々なものを見て、感じなさい。\x01",
            "それがきっとあなた達の糧になるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B5")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)

    label("loc_9BC")

    Return()

    # Function_6_7AE end

    def Function_7_9BD(): pass

    label("Function_7_9BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_9CE")
    Jump("loc_BDF")

    label("loc_9CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_A55")

    #C0003
    ChrTalk(
        0xFE,
        (
            "サロンの後片付けは\x01",
            "これで一通り終わりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "夜会の打ち合わせもありますし\x01",
            "一旦饗応の間に\x01",
            "集合するとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDF")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_ADA")

    #C0005
    ChrTalk(
        0xFE,
        (
            "おや……お客様、\x01",
            "いかがなされましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "主人や他の招待客の皆様は\x01",
            "オークション会場の方へ\x01",
            "向かわれていますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDF")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_B4A")

    #C0007
    ChrTalk(
        0xFE,
        (
            "おや、お客様。\x01",
            "なにか追加でご注文ですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "御用がありましたら\x01",
            "何なりとお申し付けを……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDF")

    label("loc_B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_BDF")

    #C0009
    ChrTalk(
        0xFE,
        (
            "各テーブルの料理は、\x01",
            "ハルトマン邸専属のシェフが仕上げた\x01",
            "最高級のものとなっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "なにかありましたら遠慮なくお申し付け下さい。\x02",
    )

    CloseMessageWindow()

    label("loc_BDF")

    TalkEnd(0xFE)
    Return()

    # Function_7_9BD end

    def Function_8_BE3(): pass

    label("Function_8_BE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_BF4")
    Jump("loc_EC7")

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_D09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C98")

    #C0011
    ChrTalk(
        0xFE,
        (
            "ここだけの話ですが……\x01",
            "庭に放されている番犬が\x01",
            "恐ろしゅうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "いくら警備のためとはいえ\x01",
            "ルバーチェ商会の軍用犬ですし……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D04")

    label("loc_C98")


    #C0013
    ChrTalk(
        0xFE,
        (
            "庭に放されている軍用犬が\x01",
            "恐ろしゅうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "まかり間違って噛みつかれたりしたら……\x01",
            "ぞぞっ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D04")

    Jump("loc_EC7")

    label("loc_D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_DB0")

    #C0015
    ChrTalk(
        0xFE,
        (
            "オークション開始が近づきましたので\x01",
            "立食パーティは終了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "オークション後には\x01",
            "中庭のほうで夜会が催される予定です。\x01",
            "是非ご参加下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC7")

    label("loc_DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_E4B")

    #C0017
    ChrTalk(
        0xFE,
        (
            "今しばらくいたしましたら\x01",
            "競売会の方が開場されます。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "開場と共に立食パーティは\x01",
            "終了となりますので、\x01",
            "今のうちにお召し上がりください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC7")

    label("loc_E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_EC7")

    #C0019
    ChrTalk(
        0xFE,
        (
            "今宵のお食事会は、\x01",
            "ご主人様の好意で\x01",
            "無償にて提供しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "どうぞ遠慮なさらず\x01",
            "お召し上がりください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC7")

    TalkEnd(0xFE)
    Return()

    # Function_8_BE3 end

    def Function_9_ECB(): pass

    label("Function_9_ECB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F5F")
    Jump("loc_FA9")

    label("loc_F5F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F7F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FA9")

    label("loc_F7F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F9F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FA9")

    label("loc_F9F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FA9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 1)), scpexpr(EXPR_END)), "loc_1198")

    #C0021
    ChrTalk(
        0xFE,
        (
            "おやおや……\x01",
            "どこぞで見た顔だねぇ。\x01",
            "ヒヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1047")

    #C0022
    ChrTalk(
        0x101,
        "#5105Fイメルダさん！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_107A")

    label("loc_1047")


    #C0023
    ChrTalk(
        0x101,
        (
            "#5105Fあなたは……\x01",
            "アンティークショップの！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_10AE")

    #C0024
    ChrTalk(
        0x102,
        "#5305Fどうしてこんな所に……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_111C")

    label("loc_10AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_10E0")

    #C0025
    ChrTalk(
        0x103,
        "#5405F……何故このような所に？\x02",
    )

    CloseMessageWindow()
    Jump("loc_111C")

    label("loc_10E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_111C")

    #C0026
    ChrTalk(
        0x104,
        (
            "#5606Fおいおい！\x01",
            "なんで婆さんがこんな所に……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111C")


    #C0027
    ChrTalk(
        0xFE,
        (
            "ある筋から招待状を手に入れてねぇ。\x01",
            "興味本位で来てみたってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#5106F（相変わらず怪しいお婆さんだな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_138B")

    label("loc_1198")


    #C0029
    ChrTalk(
        0xFE,
        (
            "おやおや……\x01",
            "もしかしてあんたたち、\x01",
            "警察のモンじゃないかい？\x02",
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
        "#5105Fどうしてそれを……！？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "ヒヒャヒャ……\x01",
            "ほんとにそうだったかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "あたしゃ、クロスベル市で\x01",
            "アンティークショップを\x01",
            "やっていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズなんかで\x01",
            "あんたたちの噂は聞いてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#5106Fそ、それにしたって\x01",
            "こんな場所にいるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "ある筋から招待状を手に入れてねぇ。\x01",
            "興味本位で来てみたってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#5106F（とことん怪しいお婆さんだな……）\x02",
    )

    CloseMessageWindow()

    label("loc_138B")


    #C0037
    ChrTalk(
        0x101,
        (
            "#5101F……あ、あの。\x01",
            "俺たちのことは……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "ヒヒャヒャ……\x01",
            "心配せんでも告げ口したりはせんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "あくどい連中だらけの場所に\x01",
            "あんたたちみたいなのがいるのも\x01",
            "なかなか面白いしねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 2)
    Jump("loc_1552")

    label("loc_144D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_14EC")

    #C0040
    ChrTalk(
        0xFE,
        (
            "マルコーニの小僧、見かけるたびに\x01",
            "悪狸ぶりに磨きがかかっているねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "立ち振舞いだけじゃなく、\x01",
            "姿も狸そのものじゃないか。\x01",
            "ヒヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1552")

    label("loc_14EC")


    #C0042
    ChrTalk(
        0xFE,
        (
            "目当ての出品物があったんで\x01",
            "来てみたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "なかなか楽しいことになりそうだよ。\x01",
            "ヒヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1552")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_ECB end

    def Function_10_155A(): pass

    label("Function_10_155A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_15D4")

    #C0044
    ChrTalk(
        0xFE,
        (
            "（ボスとハルトマン議長、\x01",
            "  大層ご機嫌みたいだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        "（このまま何事もなく終わればいいが……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_15D4")

    label("loc_15D4")

    TalkEnd(0xFE)
    Return()

    # Function_10_155A end

    def Function_11_15D8(): pass

    label("Function_11_15D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_164B")

    #C0046
    ChrTalk(
        0xFE,
        "ジロリ………………\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "……失礼。\x01",
            "万が一のことがないように\x01",
            "全力で警戒に当たっているのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164B")

    label("loc_164B")

    TalkEnd(0xFE)
    Return()

    # Function_11_15D8 end

    def Function_12_164F(): pass

    label("Function_12_164F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_18C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1806")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0xFE, 0)

    #C0048
    ChrTalk(
        0xFE,
        (
            "……いや、あの時は便宜を図っていただき\x01",
            "本当に助かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "おかげ様で記者どもに\x01",
            "情報を掴まれることもなく、\x01",
            "悠々と過ごさせてもらっていますぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        (
            "#2700Fハハ……それはなによりだ。\x02\x03",

            "#2703Fまぁ、私が政府の片翼を担う限り\x01",
            "力をお貸しするのは当然のことです。\x02\x03",

            "#2702F皆様にはこれからも、私の背中を\x01",
            "後押しして頂かなくてはなりませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "わっはっは、さすが議長は抜け目がない……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_4C(0xA, 0xFF)
    TurnDirection(0xA, 0x14, 0)
    Jump("loc_18BD")

    label("loc_1806")


    #C0052
    ChrTalk(
        0xFE,
        (
            "何度もこのパーティに\x01",
            "招待していただいておりますが、\x01",
            "今年はことさら力が入っているようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "ふふ、日頃のご健勝ぶりが伺えるというもの。\x01",
            "今後の更なる躍進を祈っておりますぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BD")

    Jump("loc_19EB")

    label("loc_18C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196E")

    #C0054
    ChrTalk(
        0xFE,
        (
            "何でも、今日の出品物には\x01",
            "目玉となる商品が\x01",
            "隠されてるそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "大層高価な品らしいが……\x01",
            "かの有名な“怪盗Ｂ”の\x01",
            "横流し品でも出るのかねぇ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19EB")

    label("loc_196E")


    #C0056
    ChrTalk(
        0xFE,
        (
            "何でも、今日の出品物には\x01",
            "特別な目玉商品が\x01",
            "隠されてるそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "大層高価な品らしいが……\x01",
            "君はなんだと思うね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EB")

    TalkEnd(0xFE)
    Return()

    # Function_12_164F end

    def Function_13_19EF(): pass

    label("Function_13_19EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1A91")

    #C0058
    ChrTalk(
        0xFE,
        (
            "ああ、それにしても\x01",
            "今日のオークションが楽しみだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "出品物に何が出るかは\x01",
            "知らないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "それはそれは魅力的な\x01",
            "商品に違いないわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B0A")

    label("loc_1A91")


    #C0061
    ChrTalk(
        0xFE,
        (
            "あなた達はあまり\x01",
            "オークションというものには\x01",
            "慣れていなさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "ふふ……あの緊張感は\x01",
            "一度ハマると病み付きよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0A")

    TalkEnd(0xFE)
    Return()

    # Function_13_19EF end

    def Function_14_1B0E(): pass

    label("Function_14_1B0E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BA2")
    Jump("loc_1BEC")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1BC2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BEC")

    label("loc_1BC2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BE2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BEC")

    label("loc_1BE2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BEC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1DE8")
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D67")

    #C0063
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長、\x01",
            "お初にお目にかかりますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "今回はご招待いただき\x01",
            "感謝しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "#2705Fほほう、貴方は共和国議員の……\x02\x03",

            "#2700F私も以前からお会いしたいと\x01",
            "思っていたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "グフフ……そうでしたか。\x01",
            "それでは今後は良き関係を期待しても\x01",
            "よろしいですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        "#2702Fええ……もちろんですとも。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DDF")

    label("loc_1D67")


    #C0068
    ChrTalk(
        0xFE,
        (
            "グフフ……実は今日は\x01",
            "手土産を用意してきておるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "競売会の後にでも\x01",
            "お部屋にうかがわせていただければと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDF")

    OP_4C(0xA, 0xFF)
    Jump("loc_1E8E")

    label("loc_1DE8")


    #C0070
    ChrTalk(
        0xFE,
        (
            "屋敷の主であるハルトマン議長は\x01",
            "帝国にも強い影響力を持つと言う。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "今日何とかしてコネクションを\x01",
            "作ることができれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "グフフ、わしの将来は安泰じゃわい。\x02",
    )

    CloseMessageWindow()

    label("loc_1E8E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_1B0E end

    def Function_15_1E96(): pass

    label("Function_15_1E96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F79")
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xFE, 0)

    #C0073
    ChrTalk(
        0xFE,
        "今後もお二方には期待しておる。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "ヘマをやらかして\x01",
            "警察の犬なんぞに\x01",
            "尻尾を掴まれんようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#3000Fはっはっは、手厳しい。\x02\x03",

            "いや、気をつけさせて\x01",
            "いただきますかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    TurnDirection(0x9, 0x16, 0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_1FF8")

    label("loc_1F79")


    #C0076
    ChrTalk(
        0xFE,
        (
            "まぁ、警察の犬なんぞが\x01",
            "この競売会を摘発できるわけは\x01",
            "ないのだがのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "はっはっは……\x01",
            "まぁ、用心くらいはしておかれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF8")

    Jump("loc_2183")

    label("loc_1FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210C")

    #C0078
    ChrTalk(
        0xFE,
        (
            "クロスベルに来るたびに思うが\x01",
            "警察とは無能だのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "これだけ大々的に開かれている\x01",
            "この競売会を、公の下に晒すことすら\x01",
            "できないでいるのだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "これもハルトマン議長の\x01",
            "絶対的な権威の力かのう。\x01",
            "はっはっは……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        "#5101F（……くっ…………！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2183")

    label("loc_210C")


    #C0082
    ChrTalk(
        0xFE,
        (
            "クロスベルの警察とは\x01",
            "本当に無能だのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "おかげさまでこうして\x01",
            "楽しませてもらっているのだがな。\x01",
            "はっはっは……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2183")

    TalkEnd(0xFE)
    Return()

    # Function_15_1E96 end

    def Function_16_2187(): pass

    label("Function_16_2187")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_2241")

    #C0084
    ChrTalk(
        0xFE,
        (
            "うふふ……今年の夜会は\x01",
            "美しい宝飾品を見事落札して、\x01",
            "清々しい気分で迎えたいですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "去年落札した翠耀石#6Rエスメラス#の指輪に\x01",
            "劣らない出品物を期待してますわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E1")

    label("loc_2241")


    #C0086
    ChrTalk(
        0xFE,
        (
            "ほら、見てくださいな。\x01",
            "これは去年の競売会で落札した\x01",
            "翠耀石#6Rエスメラス#の指輪ですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "うふふ……今年はこれに勝る\x01",
            "美しい宝飾品を\x01",
            "落札して見せますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E1")

    TalkEnd(0xFE)
    Return()

    # Function_16_2187 end

    def Function_17_22E5(): pass

    label("Function_17_22E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_237D")

    #C0088
    ChrTalk(
        0xFE,
        (
            "今年はどんな曰く付きの\x01",
            "商品が出品されるのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "宝飾品などは、\x01",
            "怪しい由来があるものほど\x01",
            "不思議と美しく輝く物ですからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240E")

    label("loc_237D")


    #C0090
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長はあの\x01",
            "《鉄血宰相》とも\x01",
            "繋がりを持っているそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "流石は帝国貴族の名門の出……\x01",
            "交友関係も他者とは一線を画しているわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240E")

    TalkEnd(0xFE)
    Return()

    # Function_17_22E5 end

    def Function_18_2412(): pass

    label("Function_18_2412")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24A6")
    Jump("loc_24F0")

    label("loc_24A6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24C6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F0")

    label("loc_24C6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24E6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F0")

    label("loc_24E6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24F0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_25AE")

    #C0092
    ChrTalk(
        0xFE,
        (
            "フン、世渡り上手のマルコーニめ……\x01",
            "ハルトマン議長の飼い犬の分際で\x01",
            "いい気になりおって。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "せいぜい失敗せぬよう\x01",
            "気をつけることだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2681")

    label("loc_25AE")


    #C0094
    ChrTalk(
        0xFE,
        (
            "屋敷の警備に当たっている黒服は……\x01",
            "ルバーチェ商会、だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "マルコーニという男は\x01",
            "ハルトマン議長に\x01",
            "うまく取り入ったものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "フン、見ておれ。\x01",
            "あのような飼い犬風情\x01",
            "近いうちに追い越してくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2681")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_2412 end

    def Function_19_2689(): pass

    label("Function_19_2689")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_26F9")

    #C0097
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長……\x01",
            "顔を通しておくに越したことはあるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "どれ、挨拶に行くとするか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28A2")

    label("loc_26F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2844")

    #C0099
    ChrTalk(
        0xFE,
        (
            "ふむ、随分若いようだが……\x01",
            "ここに招待されている以上は\x01",
            "貴族か、富豪か……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "差し支えなければ\x01",
            "どのような身分の方か\x01",
            "教えていただけるかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#5105Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……はは、さすがに緊張しているか。\x01",
            "その若さでは無理もない。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "そもそも、この場で勘繰るのは\x01",
            "いささかヤボであったな。\x01",
            "許してくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_28A2")

    label("loc_2844")


    #C0104
    ChrTalk(
        0xFE,
        (
            "ふふ……老いも若きも\x01",
            "そうそうたる顔触れですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "どれ……\x01",
            "挨拶回りと行くとするかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A2")

    TalkEnd(0xFE)
    Return()

    # Function_19_2689 end

    def Function_20_28A6(): pass

    label("Function_20_28A6")

    TalkBegin(0xFE)

    #C0106
    ChrTalk(
        0xFE,
        "なんで軍用犬が屋敷の中に……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "お、おい君！\x01",
            "この騒ぎは一体何なのかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "この私に何かあったら\x01",
            "ただじゃ済まさんぞ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_28A6 end

    def Function_21_292D(): pass

    label("Function_21_292D")

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

    # Function_21_292D end

    def Function_22_2974(): pass

    label("Function_22_2974")

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

    # Function_22_2974 end

    def Function_23_29BB(): pass

    label("Function_23_29BB")

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
            "#5101F#5P立食形式のパーティか……\x02\x03",

            "かなりの招待客が\x01",
            "集まってるみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2B90")
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)

    #C0110
    ChrTalk(
        0x102,
        (
            "#5306F#11P料理やお酒も\x01",
            "さすがに豪華そうね……\x02\x03",

            "#5301F一流のシェフを\x01",
            "雇っているのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)

    #C0111
    ChrTalk(
        0x101,
        (
            "#5106F#5Pこんな状況じゃなければ\x01",
            "喜んでご馳走になるんだけど……\x02\x03",

            "何だか緊張して食欲が無いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        "#5302F#11Pふふ、無理もないわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E1B")

    label("loc_2B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2CBC")

    #C0113
    ChrTalk(
        0x103,
        (
            "#5405F#11P何だか豪華そうな\x01",
            "お料理ばかりですね……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)

    #C0114
    ChrTalk(
        0x103,
        "#11P#5402Fロイドさん、何か食べます？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)

    #C0115
    ChrTalk(
        0x101,
        (
            "#5106F#5Pいや、さすがに緊張して\x01",
            "あんまり食欲が無いな。\x02\x03",

            "#5100Fティオ、良かったら\x01",
            "なにか貰って来たらどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        (
            "#5404F#11Pいえ、わたしも特に\x01",
            "空腹ではありませんので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1B")

    label("loc_2CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2E1B")

    #C0117
    ChrTalk(
        0x104,
        (
            "#5607F#11Pか～っ、豪華そうな\x01",
            "酒と料理が並んでやがるな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)

    #C0118
    ChrTalk(
        0x104,
        (
            "#11P#5602Fなあロイド。\x01",
            "ちょっとくらいいいだろ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)

    #C0119
    ChrTalk(
        0x101,
        (
            "#5106F#5P別にいいけど……\x01",
            "さすがに酒は止めてくれよ？\x02\x03",

            "#5101F何があるか分からないんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        (
            "#5606F#11Pぐっ……だったら止めとくぜ。\x02\x03",

            "#5601Fこれだけの料理、酒ナシで喰ったら\x01",
            "かえってストレスが溜まりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1B")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 5100, 180)
    SetScenarioFlags(0xA5, 2)
    Call(0, 21)
    EventEnd(0x5)
    Return()

    # Function_23_29BB end

    def Function_24_2E38(): pass

    label("Function_24_2E38")

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
        "#3405F#5Pあら……\x02",
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
        "#5105F#12Pあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2F6E")

    #C0123
    ChrTalk(
        0x102,
        "#5305F#12Pキリカさん……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FDA")

    label("loc_2F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2F9C")

    #C0124
    ChrTalk(
        0x103,
        "#5405F#12Pあなたは……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FDA")

    label("loc_2F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2FDA")

    #C0125
    ChrTalk(
        0x104,
        (
            "#5605F#12Pおおっ！？\x01",
            "キリカさんじゃないッスか！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FDA")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0126
    AnonymousTalk(
        0x8,
        (
            "フフ……本当に奇遇ね。\x02\x03",

            "こんな場所であなた達と会うなんて\x01",
            "さすがに想定外だったわ。\x02",
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
        "#5112F#12Pこ、これはその……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_30E6")

    #C0128
    ChrTalk(
        0x102,
        "#5306F#12Pその、色々と訳が……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3160")

    label("loc_30E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_311E")

    #C0129
    ChrTalk(
        0x103,
        "#5403F#12P諸般の事情がありまして……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3160")

    label("loc_311E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3160")

    #C0130
    ChrTalk(
        0x104,
        (
            "#5609F#12Pいや～、ちょいとばかり\x01",
            "訳がありまして……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3160")


    #C0131
    ChrTalk(
        0x8,
        (
            "#3404F#5Pふふ、まあいいわ。\x02\x03",

            "#3402F──それで、この会場では\x01",
            "どんな名で呼べばいいのかしら？\x02",
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
        "#5111F#12Pええっ……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_324A")

    #C0133
    ChrTalk(
        0x102,
        "#5301F#12Pど、どうしてそこまで……\x02",
    )

    CloseMessageWindow()
    Jump("loc_32AF")

    label("loc_324A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_327E")

    #C0134
    ChrTalk(
        0x103,
        "#5401F#12P……どうしてそれを……\x02",
    )

    CloseMessageWindow()
    Jump("loc_32AF")

    label("loc_327E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_32AF")

    #C0135
    ChrTalk(
        0x104,
        "#5606F#12Pちょ、いきなりッスか……\x02",
    )

    CloseMessageWindow()

    label("loc_32AF")


    #C0136
    ChrTalk(
        0x8,
        (
            "#3404F#5Pあなた達の立場を考えれば\x01",
            "何をしているのか想像は付くわ。\x02\x03",

            "そして招待カードを渡す時には\x01",
            "代表者が名乗る必要がある……\x02\x03",

            "#3402Fで、何と呼べばいいのかしら？\x02",
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
        "#5106F#12P……ガイ、でお願いします。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "#3404F#5Pフフ……分かったわ、ガイ君。\x02\x03",

            "#3400F私はそのまま\x01",
            "キリカと呼んでちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#5103F#12Pわ、分かりました。\x02\x03",

            "#5101Fそれで……どうして\x01",
            "キリカさんはこの場所に？\x02\x03",

            "やはり出品物が目当てですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "#3404F#5Pフフ、職業柄、\x01",
            "好事家の知り合いが多くてね。\x02\x03",

            "そういった人たちから\x01",
            "どういう出物があるか\x01",
            "確かめて欲しいと頼まれたのよ。\x02\x03",

            "#3400Fまあ、市場調査といった所ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#5106F#12Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#3404F#5Pしかしハルトマン議長という人は\x01",
            "なかなか抜け目ない人物のようね。\x02\x03",

            "この競売会……\x01",
            "仕組みとしてよく出来ているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#5105F#12Pよく出来ている……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3619")

    #C0144
    ChrTalk(
        0x102,
        "#5305F#12Pどういう事ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3678")

    label("loc_3619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_364D")

    #C0145
    ChrTalk(
        0x103,
        "#5405F#12P……どういう事ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3678")

    label("loc_364D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3678")

    #C0146
    ChrTalk(
        0x104,
        "#5605F#12Pどういう事ッスか？\x02",
    )

    CloseMessageWindow()

    label("loc_3678")


    #C0147
    ChrTalk(
        0x8,
        (
            "#3400F#5P決して摘発されることのない、\x01",
            "上流階級御用達の裏の競売会……\x02\x03",

            "それは各国の有力者にとって\x01",
            "実に都合のいい場であるという事よ。\x02\x03",

            "#3403F単なる盗品以外にも、賄賂の品や、\x01",
            "資金調達のための横流し品……\x02\x03",

            "それらを自国で処分しようとすれば\x01",
            "法律による摘発は免れない。\x02\x03",

            "#3402Fでも、このクロスベルでは\x01",
            "“見なかったこと”にされてしまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        "#5113F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "#3404F#5Pだからこそ帝国も、共和国も\x01",
            "この競売会を黙認しているのね。\x02\x03",

            "恐らく、今回の出品物の中にも\x01",
            "幾つかあるのではないかしら。\x02\x03",

            "#3400F両国の政府筋から引き取られた\x01",
            "“曰#2Rいわ#くつきの品々”が……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#5110F#12Pくっ……\x02\x03",

            "要するに、国際的にも黙認された\x01",
            "ブラックマーケットって事ですか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3941")

    #C0151
    ChrTalk(
        0x102,
        (
            "#5306F#12P改めて聞くと\x01",
            "とんでもない話\x09",
            "ですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C4")

    label("loc_3941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3982")

    #C0152
    ChrTalk(
        0x103,
        (
            "#5406F#12Pそう聞くと\x01",
            "結構えげつないですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C4")

    label("loc_3982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_39C4")

    #C0153
    ChrTalk(
        0x104,
        (
            "#5608F#12Pいや、改めて聞くと\x01",
            "とんでもねぇ話だよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C4")


    #C0154
    ChrTalk(
        0x8,
        (
            "#3404F#5Pもちろん、そんな仕組みも\x01",
            "クロスベルならではと言えるわ。\x02\x03",

            "#3400Fあなた達にとっては\x01",
            "歯がゆい現実でしょうけど……\x02\x03",

            "まあ、逆らうのは難しいでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#5108F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3ABB")

    #C0156
    ChrTalk(
        0x102,
        "#5308F#11P……ロイド……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B10")

    label("loc_3ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3AE7")

    #C0157
    ChrTalk(
        0x103,
        "#5408F#11Pロイドさん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B10")

    label("loc_3AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3B10")

    #C0158
    ChrTalk(
        0x104,
        "#5603F#12P……やれやれ……\x02",
    )

    CloseMessageWindow()

    label("loc_3B10")


    #C0159
    ChrTalk(
        0x8,
        (
            "#3400F#5Pフフ……\x02\x03",

            "#3404F──ただ、よく出来てはいても\x01",
            "不自然な仕組みであるのも確かよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#5105F#12Pえ……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#3404F#5P万物は気の流れと\x01",
            "調和によって成り立つ……\x02\x03",

            "歪んだものは、歪んだままでは\x01",
            "決して長続きはしないわ。\x02\x03",

            "何かきっかけがあれば……\x01",
            "いつ崩れ去ってもおかしくない。\x02\x03",

            "#3400Fその意味では、あなた達の頑張りも\x01",
            "無駄にはならないかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#5102F#12Pキリカさん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3CD6")

    #C0163
    ChrTalk(
        0x102,
        (
            "#5304F#12P……そう言って頂けると\x01",
            "とても心強いです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4A")

    label("loc_3CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3D0A")

    #C0164
    ChrTalk(
        0x103,
        "#5404F#12P……何だか心強いです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D4A")

    label("loc_3D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3D4A")

    #C0165
    ChrTalk(
        0x104,
        (
            "#5609F#12Pいや、そう言って頂けると\x01",
            "百人力ッスよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D4A")


    #C0166
    ChrTalk(
        0x8,
        (
            "#3404F#5Pフフ、お喋りが\x01",
            "過ぎてしまったみたいね。\x02\x03",

            "#3400Fせっかくの機会だから\x01",
            "色々なものを見てくるといいわ。\x02\x03",

            "それがきっと\x01",
            "あなた達の糧になるはずだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#5100F#12Pはい……！\x02",
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

    # Function_24_2E38 end

    def Function_25_3E25(): pass

    label("Function_25_3E25")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9C")

    #C0168
    ChrTalk(
        0xA,
        (
            "#2703F#11P……招待客の皆々様。\x01",
            "ひとたび競売が始まれば\x01",
            "みなさんは敵同士……\x02\x03",

            "#2702Fどうかこの僅かな時に\x01",
            "親睦を深めていきましょうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "#3002F#5P今宵も滅多に見られない\x01",
            "逸品の数々を出品する予定です。\x02\x03",

            "目当ての品を落札できるよう、\x01",
            "皆様の健闘を祈っております！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_407F")

    label("loc_3F9C")


    #C0170
    ChrTalk(
        0xA,
        (
            "#2702F#11P……競売に限らず、\x01",
            "様々な趣向も用意しております。\x02\x03",

            "是非ともこの長い夜を\x01",
            "楽しんでいって頂きたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "#3004F#5Pええ、まさにまさに！\x02\x03",

            "#3002F皆様に楽しんで頂ければこそ、\x01",
            "この競売会を開く\x01",
            "意味があるというものです！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_407F")

    Fade(500)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_68(-150, 1500, -1390, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4163")

    #C0172
    ChrTalk(
        0x101,
        (
            "#5113F（帝国派のハルトマン議長と\x01",
            "  ルバーチェのマルコーニ会長か……）\x02\x03",

            "#5106F（どんな人物か話してみたいけど……\x01",
            "  この場は離れた方がよさそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41B2")

    label("loc_4163")


    #C0173
    ChrTalk(
        0x101,
        (
            "#5103F（俺たちの顔は割れているはずだ。\x01",
            "  ここは離れた方がよさそうだな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41B2")

    SetChrPos(0x0, -990, 0, -870, 315)
    SetScenarioFlags(0xB4, 3)
    EventEnd(0x5)
    Return()

    # Function_25_3E25 end

    def Function_26_41C9(): pass

    label("Function_26_41C9")

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
        "#5105F#6Pあれは……\x02",
    )

    CloseMessageWindow()
    OP_68(2120, 1700, 2009, 2500)
    SetCameraDistance(15000, 2500)
    OP_6F(0x79)
    Sleep(300)

    #C0175
    ChrTalk(
        0xB,
        "#11Pご来場の皆様……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xB,
        (
            "#11P当競売会の主催者が参りましたので\x01",
            "皆様にご挨拶させていただきます。\x02",
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
        "#5107F#N（あれが……！）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_456F")

    #C0178
    ChrTalk(
        0x102,
        (
            "#5303F#N（ええ……）\x02\x03",

            "#5301F（ルバーチェの会長と\x01",
            "  ハルトマン議長ね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4638")

    label("loc_456F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_45D4")

    #C0179
    ChrTalk(
        0x103,
        (
            "#5401F#N（ひょっとして……）\x02\x03",

            "（マフィアの会長さんと\x01",
            "  帝国派の議長さんですか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4638")

    label("loc_45D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4638")

    #C0180
    ChrTalk(
        0x104,
        (
            "#5603F#N（なるほど……）\x02\x03",

            "#5600F（あれがマフィアの会長と\x01",
            "  帝国派の議長ってヤツか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4638")

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
            "──皆様、ご機嫌よう！\x02\x03",

            "当オークションを主催しておる\x01",
            "ルバーチェ商会のマルコーニです。\x02\x03",

            "早いもので、この競売会も\x01",
            "今年で８回目を迎えました。\x02\x03",

            "年々、来場される方々も増え、\x01",
            "それに比例して出品物もますます\x01",
            "充実したものになっております。\x02\x03",

            "これもひとえに、皆様のご理解と\x01",
            "ご愛顧の賜物であると言えましょう！\x02",
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
            "#3004F#11Pそしてもう一方#4Rひとかた#……\x02\x03",

            "毎年、わたくしどもの催しに\x01",
            "この素晴らしい邸宅を会場として\x01",
            "提供して下さっている方がおります。\x02\x03",

            "#3002Fご紹介しましょう──\x01",
            "クロスベル自治州代表にして\x01",
            "自治州議会をまとめる大政治家……\x02\x03",

            "ハルトマン議長閣下です！\x02",
        )
    )

    CloseMessageWindow()
    Sound(884, 0, 100, 0)
    OP_68(2120, 1700, 1340, 2000)

    def lambda_48F1():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_48F1)
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
            "──たった今、紹介にあずかった\x01",
            "自治州議長を務めるハルトマンです。\x02\x03",

            "今宵、この素晴らしい催しの場を\x01",
            "提供させて頂くのは誠に光栄の極み。\x02\x03",

            "単なる競売会というだけでなく、\x01",
            "各界の名士の方々が集い、交歓#4Rこうかん#する\x01",
            "出会いの場であるとも言えましょう。\x02\x03",

            "まだまだ宵の口……\x01",
            "オークションが終了した後には\x01",
            "ささやかな夜会も用意しております。\x02\x03",

            "皆様におかれましては、\x01",
            "どうか当館をご自分の家と思い、\x01",
            "心より寛#2Rくつろ#いでいただきたい。\x02",
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
            "#5113F#6P（あれがマルコーニ会長に\x01",
            "  ハルトマン議長か……）\x02\x03",

            "#5106F（議長の方はさすがに\x01",
            "  大物政治家って感じだな……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4CCC")

    #C0185
    ChrTalk(
        0x102,
        (
            "#5308F#6P（……自らの権威が\x01",
            "  揺るぎないものであるのを\x01",
            "  確信しているからでしょうね。）\x02\x03",

            "#5301F（ルバーチェの会長の方は\x01",
            "  初めて見たけれど……）\x02\x03",

            "（思っていた以上に\x01",
            "  狡猾でやり手といった感じね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E24")

    label("loc_4CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4D71")

    #C0186
    ChrTalk(
        0x103,
        (
            "#5406F#6P（……自分が偉いっていう事を\x01",
            "  ぜんぜん疑ってない感じですね。）\x02\x03",

            "#5411F（ルバーチェの会長の方は……\x01",
            "  ズルくてしぶとい感じでしょうか。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E24")

    label("loc_4D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4E24")

    #C0187
    ChrTalk(
        0x104,
        (
            "#5606F#6P（てめぇの権威を\x01",
            "  毛程たりとも疑っちゃいない……\x01",
            "  大貴族にありがちなタイプかもな。）\x02\x03",

            "#5601F（ルバーチェの会長の方は\x01",
            "  したたかで狡猾な狸ってところか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E24")


    #C0188
    ChrTalk(
        0x101,
        (
            "#5103F#6P（ああ……\x01",
            "  どちらも一筋縄じゃいかなそうだ。）\x02\x03",

            "#5101F（できれば話してみたいけど……\x01",
            "  さすがに自重した方が良さそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4F3C")

    #C0189
    ChrTalk(
        0x102,
        (
            "#5306F#6P（ええ、私は一応、\x01",
            "  議長と少し面識もあるし……）\x02\x03",

            "#5300F（直接コンタクトするのは\x01",
            "  避けてもらえると助かるわ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5014")

    label("loc_4F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4FA3")

    #C0190
    ChrTalk(
        0x103,
        (
            "#5403F#6P（……君子危うきに近寄らずです。）\x02\x03",

            "#5400F（目立たないよう出るべきかと。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5014")

    label("loc_4FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5014")

    #C0191
    ChrTalk(
        0x104,
        (
            "#5604F#6P（さすがにそいつは\x01",
            "  リスクの高すぎる賭けだろう。）\x02\x03",

            "#5600F（目立たないよう消えようぜ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5014")


    #C0192
    ChrTalk(
        0x101,
        (
            "#5100F#6P（分かった……\x01",
            "  さり気なくサロンから出よう。）\x02",
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

    # Function_26_41C9 end

    def Function_27_5135(): pass

    label("Function_27_5135")


    def lambda_513A():
        OP_95(0xFE, -1310, 0, 3350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_513A)
    WaitChrThread(0xFE, 1)

    def lambda_5158():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5158)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_5135 end

    def Function_28_5165(): pass

    label("Function_28_5165")


    def lambda_516A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_516A)

    def lambda_517F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_517F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_5198():
        OP_95(0xFE, 0, 0, 2810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5198)
    WaitChrThread(0xFE, 1)

    def lambda_51B6():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51B6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_5165 end

    def Function_29_51C3(): pass

    label("Function_29_51C3")


    def lambda_51C8():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51C8)

    def lambda_51DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_51DD)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_51F6():
        OP_95(0xFE, 1200, 0, 3860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51F6)
    WaitChrThread(0xFE, 1)

    def lambda_5214():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5214)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_51C3 end

    SaveToFile()

Try(main)
