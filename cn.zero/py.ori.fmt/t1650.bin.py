from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1650.bin",                # FileName
        "t1650",                    # MapName
        "t1650",                    # Location
        0x0058,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 50500, 0, 50000, 90, 0, 1, 88, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1650",                  # 0
        "约亚西姆副教授",         # 1
        "圆形椅子",               # 2
        "折叠椅",                 # 3
        "折叠椅",                 # 4
        "折叠椅",                 # 5
        "折叠椅",                 # 6
        "伊斯教授",               # 7
    ))

    AddCharChip((
        "chr/ch07102.itc",                   # 00
        "chr/ch00000.itc",                   # 01
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

    DeclNpc(110690,  150,     57000,   270,  469,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(109380,  0,       57000,   1500,    110690,  1500,    57000,   0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_258",          # 00, 0
        "Function_1_310",          # 01, 1
        "Function_2_371",          # 02, 2
        "Function_3_3E9",          # 03, 3
        "Function_4_3ED",          # 04, 4
        "Function_5_91F",          # 05, 5
        "Function_6_A69",          # 06, 6
        "Function_7_AC2",          # 07, 7
        "Function_8_B1B",          # 08, 8
        "Function_9_B74",          # 09, 9
        "Function_10_BB1",         # 0A, 10
        "Function_11_C06",         # 0B, 11
        "Function_12_D61",         # 0C, 12
        "Function_13_FEB",         # 0D, 13
        "Function_14_3091",        # 0E, 14
        "Function_15_30C8",        # 0F, 15
        "Function_16_3133",        # 10, 16
        "Function_17_33B5",        # 11, 17
        "Function_18_33F0",        # 12, 18
        "Function_19_3424",        # 13, 19
        "Function_20_4FFD",        # 14, 20
        "Function_21_4FFE",        # 15, 21
        "Function_22_5039",        # 16, 22
        "Function_23_5074",        # 17, 23
        "Function_24_50AF",        # 18, 24
    ))


    def Function_0_258(): pass

    label("Function_0_258")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_298"),
        (1, "loc_2A4"),
        (2, "loc_2B0"),
        (3, "loc_2BC"),
        (4, "loc_2C8"),
        (5, "loc_2D4"),
        (6, "loc_2E0"),
        (SWITCH_DEFAULT, "loc_2EC"),
    )


    label("loc_298")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2A4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2B0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2BC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2C8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2D4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_30F")

    Return()

    # Function_0_258 end

    def Function_1_310(): pass

    label("Function_1_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_34D")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_331")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_34D")

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_33F")
    Jump("loc_34D")

    label("loc_33F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_34D")
    ClearChrFlags(0x8, 0x80)

    label("loc_34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_361")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)
    Jump("loc_370")

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_370")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 19)

    label("loc_370")

    Return()

    # Function_1_310 end

    def Function_2_371(): pass

    label("Function_2_371")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_383")
    Jump("loc_3B0")

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_395")
    OP_66(0x0, 0x1)
    Jump("loc_3B0")

    label("loc_395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A3")
    Jump("loc_3B0")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3B0")
    OP_66(0x0, 0x1)

    label("loc_3B0")

    OP_1B(0x1, 0x0, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_3E8")

    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_3E8")

    Return()

    # Function_2_371 end

    def Function_3_3E9(): pass

    label("Function_3_3E9")

    Call(0, 4)
    Return()

    # Function_3_3E9 end

    def Function_4_3ED(): pass

    label("Function_4_3ED")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_481")
    Jump("loc_4CB")

    label("loc_481")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A1")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB")

    label("loc_4A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C1")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB")

    label("loc_4C1")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CB")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FE")
    Jump("loc_917")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_6A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_609")

    #C0001
    ChrTalk(
        0x8,
        (
            "#2410F这药片就是传闻中的『真知』吗，\x01",
            "还是完全不同的药呢……\x02\x03",

            "#2400F虽然这样说可能有些不谨慎，\x01",
            "但身为药物学研究者，\x01",
            "我对此真的非常感兴趣。\x02\x03",

            "#2401F总而言之，我会尽一切努力\x01",
            "来仔细调查这蓝色药片的。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x103,
        "#0208F……………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6A0")

    label("loc_609")


    #C0003
    ChrTalk(
        0x8,
        (
            "#2403F借助恶魔之力的谜之秘药……\x01",
            "这种药究竟是不是真正的『真知』，\x01",
            "只有调查之后方可得知。\x02\x03",

            "#2401F总而言之，我会尽一切努力\x01",
            "来仔细调查这蓝色药片的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A0")

    Jump("loc_917")

    label("loc_6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6B3")
    Jump("loc_917")

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_END)), "loc_917")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A4")

    #C0004
    ChrTalk(
        0x8,
        (
            "#2400F既然琪雅不愿意，\x01",
            "住院检查就暂且作罢吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0006F实在对不起……\x01",
            "难得让您帮我们出主意。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#2404F哈哈，不必介意。\x02\x03",

            "#2405F话说回来，\x01",
            "你们还是早点去\x01",
            "追琪雅为好吧？\x02\x03",

            "这间乌尔斯拉医院占地还挺广的，\x01",
            "要是走丢的话，可不好找哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_800")

    #C0007
    ChrTalk(
        0x102,
        (
            "#0108F是呀……还是赶快去追比较好吧，\x01",
            "小琪雅好像很生气啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_882")

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_854")

    #C0008
    ChrTalk(
        0x103,
        (
            "#0203F的确……\x01",
            "在给医院的人添麻烦之前，\x01",
            "还是尽快找到她比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_882")

    label("loc_854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_882")

    #C0009
    ChrTalk(
        0x104,
        (
            "#0300F赶快找到她，\x01",
            "向她道歉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_882")


    #C0010
    ChrTalk(
        0x101,
        "#0000F嗯，那就走吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_917")

    label("loc_8A4")


    #C0011
    ChrTalk(
        0x8,
        (
            "#2400F琪雅今后说不定也会\x01",
            "改变主意，\x01",
            "还是事先做好检查的准备吧。\x02\x03",

            "有什么事的话就再来商量，\x01",
            "随时都可以与我联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_917")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_4_3ED end

    def Function_5_91F(): pass

    label("Function_5_91F")

    EventBegin(0x2)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【离开研究楼】")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_987"),
        (1, "loc_996"),
        (2, "loc_9C3"),
        (SWITCH_DEFAULT, "loc_9D2"),
    )


    label("loc_987")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D2")

    label("loc_996")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BE")

    label("loc_9B4")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9BE")

    Jump("loc_9D2")

    label("loc_9C3")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D2")

    label("loc_9D2")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_9EE"),
        (1, "loc_A35"),
        (2, "loc_A50"),
        (SWITCH_DEFAULT, "loc_A68"),
    )


    label("loc_9EE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0F")
    Call(0, 16)
    Jump("loc_A30")

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A25")
    Call(0, 20)
    Jump("loc_A30")

    label("loc_A25")

    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()

    label("loc_A30")

    Jump("loc_A68")

    label("loc_A35")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1620", 114, 0, 0)
    IdleLoop()
    Jump("loc_A68")

    label("loc_A50")

    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x5)
    Jump("loc_A68")

    label("loc_A68")

    Return()

    # Function_5_91F end

    def Function_6_A69(): pass

    label("Function_6_A69")


    def lambda_A6E():
        OP_95(0xFE, -4460, 0, 90610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A6E)

    def lambda_A88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A88)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_AA1():
        OP_95(0xFE, -7820, 0, 90540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AA1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_6_A69 end

    def Function_7_AC2(): pass

    label("Function_7_AC2")


    def lambda_AC7():
        OP_95(0xFE, -4460, 0, 90610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AC7)

    def lambda_AE1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AE1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_AFA():
        OP_95(0xFE, -5900, 0, 89580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_AC2 end

    def Function_8_B1B(): pass

    label("Function_8_B1B")


    def lambda_B20():
        OP_95(0xFE, -4460, 0, 90610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B20)

    def lambda_B3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B3A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_B53():
        OP_95(0xFE, -6530, 0, 90480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B53)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_B1B end

    def Function_9_B74(): pass

    label("Function_9_B74")


    def lambda_B79():
        OP_95(0xFE, -6720, 0, 95640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B79)
    WaitChrThread(0xFE, 1)

    def lambda_B97():
        OP_95(0xFE, -1680, 0, 99810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B97)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_B74 end

    def Function_10_BB1(): pass

    label("Function_10_BB1")


    def lambda_BB6():
        OP_95(0xFE, 57520, 0, 58790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB6)
    WaitChrThread(0xFE, 1)

    def lambda_BD4():
        OP_95(0xFE, 59520, 0, 58790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD4)
    Sleep(500)

    def lambda_BF1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BF1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_BB1 end

    def Function_11_C06(): pass

    label("Function_11_C06")

    OP_68(-5980, 1700, 90160, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -2320, 0, 90910, 270)
    SetChrPos(0xEF, -2320, 0, 90910, 270)
    SetChrPos(0x153, -2320, 0, 90910, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    OP_68(-6980, 1700, 90160, 3000)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0x153, 3, 0, 8)
    Sleep(1000)
    BeginChrThread(0xEF, 3, 0, 7)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x153, 3)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    OP_6F(0x1)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 9)
    Sleep(750)
    OP_68(-6980, 2700, 90160, 6000)
    BeginChrThread(0x153, 3, 0, 9)
    Sleep(325)
    BeginChrThread(0xEF, 3, 0, 9)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x153, 0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0xEF, 0x3)
    EndChrThread(0x153, 0x3)
    Sleep(1000)
    Return()

    # Function_11_C06 end

    def Function_12_D61(): pass

    label("Function_12_D61")

    FadeToBright(1000, 0)
    OP_68(56390, 1400, 57940, 0)
    MoveCamera(47, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21940, 0)
    SetCameraDistance(20900, 3000)
    SetChrPos(0x101, 57020, 0, 58790, 90)
    SetChrPos(0xEF, 56370, 0, 60220, 135)
    SetChrPos(0x153, 55430, 0, 58580, 90)
    OP_6F(0x10)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "药物学·神经科研究室\x01",
            "约亚西姆·琼塔副教授\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)

    #C0013
    ChrTalk(
        0x101,
        (
            "#0005F（好像是这里了啊……）\x02\x03",

            "#0003F──打扰了，\x01",
            "我是支援科的罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 59520, 0, 59900, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0014
    NpcTalk(
        0x8,
        "男性的声音",
        "#11P#2S请进吧，正等着你们呢。\x02",
    )

    CloseMessageWindow()

    #N0015
    NpcTalk(
        0x8,
        "男性的声音",
        "#11P#2S请进来吧。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0000F好的。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 110690, 150, 57000, 270)
    TurnDirection(0x101, 0x153, 500)

    #C0017
    ChrTalk(
        0x101,
        "#0000F#11P琪雅，进去吧。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x153,
        "#1110F#6P嗯！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    Sleep(100)

    def lambda_F66():
        OP_95(0xFE, 57520, 0, 58790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F66)
    WaitChrThread(0x101, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    Sleep(200)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(750)
    BeginChrThread(0x153, 3, 0, 10)
    Sleep(1000)
    BeginChrThread(0xEF, 3, 0, 10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x153, 3)
    Sleep(500)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_12_D61 end

    def Function_13_FEB(): pass

    label("Function_13_FEB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 11)
    Call(0, 12)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch08202.itc", 0x22)
    LoadChrToIndex("apl/ch50383.itc", 0x23)
    OP_68(113550, 1250, 51110, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23130, 0)
    SetChrPos(0x101, 108030, 0, 49200, 270)
    SetChrPos(0xEF, 108030, 0, 48000, 270)
    SetChrPos(0x153, 106810, 0, 48600, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02400.itp")
    FadeToBright(1000, 0)
    OP_68(108440, 1250, 57200, 7000)
    OP_6F(0x1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    #C0019
    ChrTalk(
        0x101,
        "#0000F──打扰了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    def lambda_1142():
        OP_95(0xFE, 108030, 0, 57600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1142)
    Sleep(150)

    def lambda_115F():
        OP_95(0xFE, 106810, 0, 57000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_115F)
    Sleep(50)

    def lambda_117C():
        OP_95(0xFE, 108030, 0, 56400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_117C)
    Sleep(3000)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x101, 1)

    def lambda_11A1():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A1)
    WaitChrThread(0x153, 1)

    def lambda_11B2():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_11B2)
    WaitChrThread(0xEF, 1)

    def lambda_11C3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_11C3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_12CF")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0020
    AnonymousTalk(
        0x8,
        (
            "哎呀，罗伊德，\x01",
            "还有艾莉小姐吗。\x02\x03",

            "纪念庆典时真是谢谢了。\x01",
            "多亏你们，我玩得很开心呢。\x02",
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

    #C0021
    ChrTalk(
        0x102,
        (
            "#0102F#6P呵呵……\x01",
            "医生您好像还是老样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149E")

    label("loc_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_13B9")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0022
    AnonymousTalk(
        0x8,
        (
            "哎呀，罗伊德，\x01",
            "还有缇欧吗。\x02\x03",

            "纪念庆典时真是谢谢了。\x01",
            "多亏你们，我玩得很开心呢。\x02",
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

    #C0023
    ChrTalk(
        0x103,
        "#0202F#6P……医生您还是老样子呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_149E")

    label("loc_13B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_149E")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0024
    AnonymousTalk(
        0x8,
        (
            "哎呀，罗伊德，\x01",
            "还有兰迪吗。\x02\x03",

            "纪念庆典时真是谢谢了。\x01",
            "多亏你们，我玩得很开心呢。\x02",
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

    #C0025
    ChrTalk(
        0x104,
        "#0302F#6P哈哈，医生还是老样子啊。\x02",
    )

    CloseMessageWindow()

    label("loc_149E")


    #C0026
    ChrTalk(
        0x101,
        (
            "#0003F#6P那个，对不起。\x02\x03",

            "#0000F我们没有事先预约，\x01",
            "就直接找上门来……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#2404F#11P哪里哪里，我的工作\x01",
            "刚好告一段落了。\x02\x03",

            "#2401F那么，听说你们收留了一个\x01",
            "失忆的孩子……就是这孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0001F#6P是的……\x01",
            "她叫琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x153,
        (
            "#1110F#6P那个那个，罗伊德。\x02\x03",

            "这个戴眼镜的叔叔\x01",
            "能把我的记忆找回来吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x8,
        (
            "#2405F#11P叔、叔叔！？\x02\x03",

            "#2406F……哈哈，我还以为\x01",
            "自己显得很年轻呢……\x01",
            "结果还是叔叔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#0011F#6P没、没有啦，医生您还很年轻呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x153, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_16E0")

    #C0032
    ChrTalk(
        0x102,
        (
            "#0106F#11P（……小琪雅。）\x02\x03",

            "#0100F（像这种时候，就算只是客套话，\x01",
            "  也应该叫哥哥比较好哦。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B1")

    label("loc_16E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1749")

    #C0033
    ChrTalk(
        0x103,
        (
            "#0203F#11P（……琪雅。）\x02\x03",

            "#0202F（在这种时候，就当是客套话，\x01",
            "  也应该叫哥哥比较好。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B1")

    label("loc_1749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_17B1")

    #C0034
    ChrTalk(
        0x104,
        (
            "#0306F#11P（喂～阿琪。）\x02\x03",

            "#0300F（在这种时候，就算只是客套话，\x01",
            "  也应该叫哥哥比较好哦。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B1")


    #C0035
    ChrTalk(
        0x153,
        "#1105F#6P（是这样吗～？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x8,
        (
            "#2406F#11P不用再说了，那种安慰话\x01",
            "反而会让人更加难过……\x02\x03",

            "#2400F……算啦，总而言之，\x01",
            "先到这边坐下。\x02\x03",

            "然后把事情原委详细地\x01",
            "说给我听听吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_18BE")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_18E5")

    label("loc_18BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_18D4")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_18E5")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_18E5")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_18E5")

    SetChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0x153, 0x22)
    SetChrSubChip(0x153, 0x0)
    SetChrFlags(0x153, 0x4)
    SetChrSubChip(0x8, 0x1)
    OP_68(111390, 2150, 55630, 0)
    MoveCamera(50, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20870, 0)
    SetChrPos(0x8, 111000, 150, 56700, 180)
    SetChrPos(0x153, 111000, 150, 55300, 0)
    SetChrPos(0x101, 112700, 0, 56600, 270)
    SetChrPos(0xEF, 112700, 0, 55500, 270)
    OP_78(0xA, 0xE)
    SetChrPos(0xE, 111000, 0, 57000, 0)
    OP_D3(0xE, 0x0, 0x0, 0x0, 0x0)
    OP_78(0x5, 0xA)
    SetChrPos(0xA, 111000, 0, 55000, 0)
    OP_78(0x6, 0xB)
    SetChrPos(0xB, 113000, 0, 56600, 0)
    OP_D3(0xB, 0x0, 0x15F90, 0x0, 0x0)
    OP_78(0x7, 0xC)
    SetChrPos(0xC, 113000, 0, 55500, 90)
    OP_D3(0xC, 0x0, 0x15F90, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(111390, 1150, 55630, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    #C0037
    ChrTalk(
        0x8,
        (
            "#2403F#6P……原来如此，\x01",
            "大体情况我已经了解了。\x02\x03",

            "#2401F唔，连七耀教会的法术\x01",
            "也无法恢复的记忆吗……\x02\x03",

            "这样的话，正如那位修女所说，\x01",
            "很有可能是神经系统的问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0006F#11P是吗……\x02\x03",

            "#0013F有没有什么\x01",
            "能够使其恢复的办法呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#2406F#6P老实说，脑神经和脑细胞方面\x01",
            "的研究才刚刚起步。\x02\x03",

            "会造成记忆丧失的原因\x01",
            "实在是不计其数，\x01",
            "所以并不存在对症疗法。\x02\x03",

            "#2400F只不过……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "副教授取出了医用放大镜。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetChrSubChip(0x8, 0x0)
    Sound(882, 0, 100, 0)
    Sleep(300)

    #C0041
    ChrTalk(
        0x8,
        (
            "#2401F#5P──琪雅，\x01",
            "看着我的眼睛好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x153,
        (
            "#1110F#12P好呀～\x02\x03",

            "#1101F（盯～）……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0043
    ChrTalk(
        0x8,
        (
            "#2403F#5P唔……瞳孔没有异常。\x02\x03",

            "#2401F最近几天，有没有觉得头痛，\x01",
            "或者想呕吐？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x153,
        "#1105F#12P头痛？呕吐？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0045
    ChrTalk(
        0x101,
        (
            "#0000F#5P就是感觉头很疼，\x01",
            "或者很恶心，不舒服的意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x153,
        "#1104F#12P没有，琪雅很健康哦。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0047
    ChrTalk(
        0x8,
        (
            "#2401F#5P唔……看来脑部\x01",
            "并没有受到损伤。\x02\x03",

            "#2403F这样的话……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1DE0")

    #C0048
    ChrTalk(
        0x102,
        "#0101F#11P您、您有什么头绪了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E3F")

    label("loc_1DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1E14")

    #C0049
    ChrTalk(
        0x103,
        "#0201F#11P……您有什么头绪了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E3F")

    label("loc_1E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1E3F")

    #C0050
    ChrTalk(
        0x104,
        "#0301F#11P您有什么头绪了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1E3F")

    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0051
    ChrTalk(
        0x8,
        (
            "#2403F#6P……这只是我的直觉。\x02\x03",

            "#2401F或许，很可能是受了\x01",
            "什么药物的影响。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x101,
        "#0007F#11P药物……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1F27")

    #C0053
    ChrTalk(
        0x102,
        (
            "#0105F#11P药物还有造成\x01",
            "记忆丧失的可能性吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F9A")

    label("loc_1F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1F66")

    #C0054
    ChrTalk(
        0x103,
        (
            "#0205F#11P药物有可能\x01",
            "造成记忆丧失吗……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F9A")

    label("loc_1F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1F9A")

    #C0055
    ChrTalk(
        0x104,
        (
            "#0305F#11P药物还能造成\x01",
            "记忆丧失吗！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F9A")


    #C0056
    ChrTalk(
        0x8,
        (
            "#2403F#6P嗯，虽然很少见，\x01",
            "但过去也有过一些类似的病例。\x02\x03",

            "#2401F药物中的某些成分，会带有阻碍\x01",
            "神经系统传导的副作用……\x02\x03",

            "#2406F只是，在多数情况下，\x01",
            "都会同时引起精神失常。\x02\x03",

            "但琪雅的情况\x01",
            "似乎与其并不吻合。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#0008F#11P的确……\x01",
            "琪雅和精神失常实在是不沾边呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_20DF")

    #C0058
    ChrTalk(
        0x102,
        (
            "#0108F#11P是呀，如您所见，\x01",
            "她既开朗又活泼……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_20DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2115")

    #C0059
    ChrTalk(
        0x103,
        "#0208F#11P…………是的………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_2153")

    label("loc_2115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2153")

    #C0060
    ChrTalk(
        0x104,
        (
            "#0308F#11P是啊，如您所见，\x01",
            "她这么活蹦乱跳的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2153")

    SetChrSubChip(0x153, 0x2)
    Sleep(300)

    #C0061
    ChrTalk(
        0x153,
        "#1100F#6P嗯～？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#2403F#6P只不过，药物学领域\x01",
            "也尚处于发展阶段。\x02\x03",

            "能引起未知效果的药物也许已经被\x01",
            "开发出来了，这种可能性也无法否定。\x02\x03",

            "#2401F从这层意义上来说，\x01",
            "或许应该同时从神经系统异常和\x01",
            "药物副作用这两个方面来着手检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0003F#11P原来如此……\x02\x03",

            "#0001F那个，可以拜托您来\x01",
            "进行检查吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#2405F#6P嗯，当然可以啊。\x02\x03",

            "#2406F只是，不但要花上一些时间，\x01",
            "而且也不保证可以恢复记忆。\x02\x03",

            "#2400F如果你们能接受的话就没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0006F#11P是、是这样吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_236A")

    #C0066
    ChrTalk(
        0x102,
        (
            "#0108F#11P请问，如果做检查的话，\x01",
            "大概要多长时间……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23F1")

    label("loc_236A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_23AD")

    #C0067
    ChrTalk(
        0x103,
        (
            "#0201F#11P……如果要做检查，\x01",
            "具体需要多长时间？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23F1")

    label("loc_23AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_23F1")

    #C0068
    ChrTalk(
        0x104,
        (
            "#0301F#11P那么，要是做检查的话，\x01",
            "大概要花多长时间啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F1")


    #C0069
    ChrTalk(
        0x8,
        (
            "#2403F#6P──至少也要三天。\x02\x03",

            "#2401F如果可以的话，我建议\x01",
            "住院一周左右，进行仔细检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#0003F#11P至少也要三天吗……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#2406F#6P药物方面的检查\x01",
            "是很耗时间的。\x02\x03",

            "因为还要用化学方法\x01",
            "来检验从体内排出的成分嘛。\x02\x03",

            "#2400F至于住院和检查的费用……\x01",
            "因为是稀有病例，\x01",
            "所以能给你们适当打个折扣。\x02\x03",

            "……怎么样？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        (
            "#0002F#5P──那个，琪雅，听我说。\x02\x03",

            "要不要在这间医院里\x01",
            "住大概三天左右？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #C0073
    ChrTalk(
        0x153,
        (
            "#1100F#6P嗯～？\x02\x03",

            "可以呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#0012F#5P呼……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_25F5")

    #C0075
    ChrTalk(
        0x102,
        "#0109F#11P呵呵，这就放心了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_264E")

    label("loc_25F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2623")

    #C0076
    ChrTalk(
        0x103,
        "#0204F#11P……这就放心了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_264E")

    label("loc_2623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_264E")

    #C0077
    ChrTalk(
        0x104,
        "#0309F#11P哈哈，这就放心啦。\x02",
    )

    CloseMessageWindow()

    label("loc_264E")

    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0078
    ChrTalk(
        0x8,
        (
            "#2404F#6P唔，那么，事不宜迟，\x01",
            "立刻去办理住院手续吧。\x02\x03",

            "#2400F如果要准备换洗衣物和个人物品的话，\x01",
            "你们最好先回去一趟，\x01",
            "帮她拿过来吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0079
    ChrTalk(
        0x101,
        (
            "#0000F#11P嗯，那我们稍后就回去取，\x01",
            "准备好之后再送过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x153,
        (
            "#1111F#6P那个那个，罗伊德。\x02\x03",

            "在这里住是可以，\x01",
            "不过我们还可以睡在一起吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)

    #C0081
    ChrTalk(
        0x101,
        "#0011F#5P呃……这个……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x153,
        (
            "#1106F#6P嗯～不行的话，\x01",
            "琪雅就忍耐一下吧～……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0006F#5P不、不是啦……\x01",
            "不是这个意思。\x02\x03",

            "#0002F要住在这间医院的\x01",
            "只有琪雅一个人哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0084
    ChrTalk(
        0x153,
        (
            "#1105F#6P是吗？\x02\x03",

            "#1110F那你们要住在\x01",
            "哪里～？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#0004F#5P我们和平时一样，\x01",
            "就住在支援科的旧楼啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0086
    ChrTalk(
        0x101,
        (
            "#0000F#5P#1K不过，我们每天\x01",
            "都会来看琪雅──\x02",
        )
    )

    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0087
    ChrTalk(
        0x153,
        "#1103F#6P#1K不要。\x02",
    )

    OP_57(0x1)
    OP_5A()

    #C0088
    ChrTalk(
        0x101,
        "#0005F#5P……哎？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    SetChrPos(0x153, 111510, 0, 55700, 45)
    Sound(820, 0, 100, 0)
    ClearChrFlags(0x153, 0x4)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(300)

    #C0089
    ChrTalk(
        0x153,
        (
            "#1101F#6P……罗伊德，你们想把琪雅\x01",
            "扔下不管了。\x02\x03",

            "#1107F琪雅是没人要的孩子了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0090
    ChrTalk(
        0x101,
        "#0013F#5P那、那怎么可能呢！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2A70")

    #C0091
    ChrTalk(
        0x102,
        (
            "#0106F#11P只、只是在这里\x01",
            "住很短一段时间而已……\x02\x03",

            "#0102F之后还能再像以前一样，\x01",
            "和大家住在一起哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B41")

    label("loc_2A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2AD8")

    #C0092
    ChrTalk(
        0x103,
        (
            "#0206F#11P只是在这里\x01",
            "小住几天而已。\x02\x03",

            "#0202F之后还能再和以前一样，\x01",
            "与大家住在一起的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B41")

    label("loc_2AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2B41")

    #C0093
    ChrTalk(
        0x104,
        (
            "#0306F#11P只是在这里\x01",
            "住上很短一段时间啦。\x02\x03",

            "#0300F之后还能再和以前一样，\x01",
            "跟大家住在一起哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B41")


    #C0094
    ChrTalk(
        0x153,
        (
            "#1101F#6P我才不管呢！\x02\x03",

            "不管是协会还是医院，\x01",
            "琪雅才不想住呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(110240, 1150, 54670, 1000)
    BeginChrThread(0x153, 3, 0, 14)
    Sleep(300)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0xEF, 0x1)
    Sleep(600)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x153, 3)

    #C0095
    ChrTalk(
        0x101,
        "#0011F#5P#N琪、琪雅？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0096
    ChrTalk(
        0x153,
        "#1107F#4S#6P罗伊德是大笨蛋！\x02",
    )

    CloseMessageWindow()
    OP_68(100850, 1150, 50000, 3000)
    BeginChrThread(0x153, 3, 0, 15)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_6F(0x79)

    #C0097
    ChrTalk(
        0x101,
        "#0007F#12P喂，琪雅！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(112060, 1150, 56390, 0)
    MoveCamera(50, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20870, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2CD1")

    #C0098
    ChrTalk(
        0x102,
        (
            "#0106F#11P呼……\x01",
            "惹她生气了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D36")

    label("loc_2CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2D02")

    #C0099
    ChrTalk(
        0x103,
        (
            "#0206F#11P唉……\x01",
            "惹她生气了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D36")

    label("loc_2D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2D36")

    #C0100
    ChrTalk(
        0x104,
        (
            "#0306F#11P哎呀哎呀……\x01",
            "惹她生气了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D36")


    #C0101
    ChrTalk(
        0x101,
        "#0006F#5P唉，真是的……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x0)
    Sleep(200)

    #C0102
    ChrTalk(
        0x101,
        (
            "#0001F#11P不好意思，医生。\x01",
            "难得您一番好意……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    #C0103
    ChrTalk(
        0x8,
        (
            "#2409F#6P哈哈，看她的样子，\x01",
            "强人所难也只会适得其反呢。\x02\x03",

            "#2400F反正就算住院检查，\x01",
            "也未必就能查出明确结果。\x02\x03",

            "不然还是等琪雅冷静下来之后，\x01",
            "再重新商量一下如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#0006F#11P好的……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#2404F#6P算啦，耐心等待\x01",
            "记忆恢复也是个办法。\x02\x03",

            "#2400F有什么事的话，就再来找我商量吧，\x01",
            "随时都可以和这里联络哦。\x02\x03",

            "我这边也再调查几个\x01",
            "记忆障碍类的病例吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#0002F#11P……非常感谢您。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2F4D")

    #C0107
    ChrTalk(
        0x102,
        (
            "#0104F#11P到时候\x01",
            "还请多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FAD")

    label("loc_2F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2F82")

    #C0108
    ChrTalk(
        0x103,
        (
            "#0204F#11P……到时\x01",
            "还请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FAD")

    label("loc_2F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2FAD")

    #C0109
    ChrTalk(
        0x104,
        "#0304F#11P到时还请多关照啦。\x02",
    )

    CloseMessageWindow()

    label("loc_2FAD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x52, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrPos(0xB, 0, 0, 0, 0)
    SetChrPos(0xC, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_D3(0xE, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    SetChrPos(0x0, 107040, 0, 52930, 180)
    SetChrPos(0x8, 110690, 150, 57000, 270)
    OP_4C(0x8, 0xFF)
    OP_66(0x0, 0x1)
    SetScenarioFlags(0xA8, 6)
    OP_29(0x48, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_FEB end

    def Function_14_3091(): pass

    label("Function_14_3091")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 111670, 0, 54050, 5000, 0x1)
    OP_95(0xFE, 109780, 0, 53980, 5000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_14_3091 end

    def Function_15_30C8(): pass

    label("Function_15_30C8")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_95(0xFE, 105220, 0, 50000, 5000, 0x1)
    OP_95(0xFE, 100910, 0, 50000, 5000, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)

    def lambda_3105():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3105)
    OP_95(0xFE, 98450, 0, 50000, 5000, 0x0)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    Sound(107, 0, 100, 0)
    Return()

    # Function_15_30C8 end

    def Function_16_3133(): pass

    label("Function_16_3133")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(56390, 1400, 57940, 0)
    MoveCamera(47, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21440, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 60040, 0, 59000, 270)
    SetChrPos(0xEF, 60040, 0, 59000, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(20900, 2000)
    OP_6F(0x10)
    OP_0D()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    OP_68(55390, 1400, 57940, 3000)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0xEF, 3, 0, 18)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    OP_6F(0x1)

    #C0110
    ChrTalk(
        0x101,
        (
            "#0006F#6P伤脑筋啊……\x01",
            "没想到她竟然这么抗拒。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3293")

    #C0111
    ChrTalk(
        0x102,
        (
            "#0102F#11P呵呵，但你不觉得\x01",
            "她这样也挺令人开心的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331A")

    label("loc_3293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_32D4")

    #C0112
    ChrTalk(
        0x103,
        (
            "#0202F#11P……不过，她这样\x01",
            "也挺令人开心的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331A")

    label("loc_32D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_331A")

    #C0113
    ChrTalk(
        0x104,
        (
            "#0302F#11P哈哈，不过，你不觉得\x01",
            "她这样也挺令人开心的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331A")


    #C0114
    ChrTalk(
        0x101,
        (
            "#0011F#6P这个……\x01",
            "嗯，确实不能否定。\x02\x03",

            "#0003F总之，快去追琪雅吧。\x02\x03",

            "#0008F唉，希望她没有\x01",
            "跑到什么奇怪的地方去……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19940, 2000)
    FadeToDark(1000, 0, -1)
    OP_6F(0x10)
    OP_0D()
    SetScenarioFlags(0xA8, 7)
    SetScenarioFlags(0x5C, 2)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3133 end

    def Function_17_33B5(): pass

    label("Function_17_33B5")


    def lambda_33BA():
        OP_95(0xFE, 55540, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33BA)

    def lambda_33D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33D4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x190)
    Return()

    # Function_17_33B5 end

    def Function_18_33F0(): pass

    label("Function_18_33F0")


    def lambda_33F5():
        OP_95(0xFE, 57040, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33F5)

    def lambda_340F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_340F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_33F0 end

    def Function_19_3424(): pass

    label("Function_19_3424")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis087.itp")
    OP_68(113550, 1250, 51110, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23130, 0)
    SetChrPos(0x101, 108030, 0, 49200, 270)
    SetChrPos(0x102, 108030, 0, 48000, 270)
    SetChrPos(0x103, 106810, 0, 48000, 270)
    SetChrPos(0x104, 106810, 0, 49200, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_68(108440, 1250, 57200, 8000)
    OP_6F(0x1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    #C0115
    ChrTalk(
        0x101,
        "#0000F──打扰了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    def lambda_3591():
        OP_95(0xFE, 108030, 0, 57600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3591)
    Sleep(150)

    def lambda_35AE():
        OP_95(0xFE, 106810, 0, 57600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_35AE)
    Sleep(50)

    def lambda_35CB():
        OP_95(0xFE, 108030, 0, 56400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35CB)
    Sleep(100)

    def lambda_35E8():
        OP_95(0xFE, 106810, 0, 56400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_35E8)
    Sleep(3000)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x101, 1)

    def lambda_360D():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_360D)
    WaitChrThread(0x104, 1)

    def lambda_361E():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_361E)
    WaitChrThread(0x102, 1)

    def lambda_362F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_362F)
    WaitChrThread(0x103, 1)

    def lambda_3640():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3640)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0116
    ChrTalk(
        0x8,
        (
            "#2406F#11P哈哈……欢迎，\x01",
            "你们来得可真是时候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0012F#6P那个……\x01",
            "突然来打扰您，真是很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#0106F#6P好像妨碍到\x01",
            "您的兴趣爱好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "#2406F#11P唉～下午的这个时间\x01",
            "正是垂钓锦鲤的\x01",
            "绝好时间段……\x02\x03",

            "#2401F不过，既然有客人来，那就没办法了。\x02\x03",

            "#2403F我可丝毫都没有\x01",
            "怨恨你们的意思，没有哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x103,
        (
            "#0206F#6P（好像感觉到了\x01",
            "  一股很强的怨念呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x104,
        (
            "#0306F#6P（还真是个无可救药的\x01",
            "  钓鱼痴啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#2409F#11P好啦，小小的牢骚话\x01",
            "就到此为止……\x02\x03",

            "#2400F今天到底有什么事？\x02\x03",

            "我还以为你们肯定又带着\x01",
            "琪雅来找我商量了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0000F#6P那个，虽然琪雅的记忆还是没有恢复。\x02\x03",

            "#0006F不过……\x01",
            "这次来找您，\x01",
            "是想商量另外一件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "#2410F#11P唔，是吗……\x02\x03",

            "#2400F我个人还是觉得应该让琪雅\x01",
            "住院检查一次比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#0108F#6P嗯，我们也曾委婉地\x01",
            "劝导过她，\x01",
            "但她好像还是很不愿意……\x02\x03",

            "#0106F……对不起，\x01",
            "让问题一拖再拖了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "#2404F#11P没关系，不必着急，\x01",
            "慢慢考虑好了。\x02\x03",

            "#2400F那么，你们说的另一件事是……？\x02\x03",

            "和我的专业有关吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#0003F#6P嗯，密切相关。\x02\x03",

            "#0001F──您能看看\x01",
            "这些药吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        "#2405F#11P哦……？\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)

    #A0129
    AnonymousTalk(
        0x8,
        (
            "#2405F……这是……\x02\x03",

            "#2401F怎么会呈现这种蓝色……\x01",
            "如果说是用色素染上的话，好像又有点……\x02",
        )
    )

    CloseMessageWindow()

    #A0130
    AnonymousTalk(
        0x101,
        (
            "#0006F这些药片是某个人\x01",
            "持有的物品……\x02\x03",

            "#0013F我们觉得这有可能是\x01",
            "违禁药物。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #C0131
    ChrTalk(
        0x8,
        (
            "#2403F#11P……原来如此。\x02\x03",

            "#2401F把详细情况\x01",
            "说给我听听吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 102150, 150, 55850, 0)
    SetChrPos(0x101, 103000, 150, 55880, 0)
    SetChrPos(0x102, 103850, 150, 55890, 0)
    SetChrPos(0x104, 105270, 0, 56100, 315)
    SetChrPos(0x8, 102990, 150, 58690, 180)
    SetChrSubChip(0x8, 0x0)
    OP_68(103000, 1950, 57370, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_68(103000, 950, 57370, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0132
    ChrTalk(
        0x8,
        (
            "#2403F#5P原来如此……\x01",
            "竟然发生了这种事啊。\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#0008F#12P那么，约亚西姆医生。\x02\x03",

            "#0001F关于这种蓝色药片，\x01",
            "您是否知道些什么呢？\x02\x03",

            "比如说，是某处开发的新药……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#2406F#5P……很遗憾，\x01",
            "我从未见过这种类型的药。\x02\x03",

            "#2401F出于专业原因，我和各国的\x01",
            "制药公司都有来往。\x02\x03",

            "他们开发的新药样品，\x01",
            "我也基本都见到过……\x02\x03",

            "但这种颜色的药片真是前所未见。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#0006F#12P是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        (
            "#2403F#5P而且，听你们所说，\x01",
            "它的效果似乎也非比寻常。\x02\x03",

            "体力、注意力、反射神经，\x01",
            "以及判断力和直觉……\x02\x03",

            "#2401F竟然能够提升一切能力……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#0106F#12P那个，目前还不确定\x01",
            "黑手党们有没有\x01",
            "服用过这种药……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x104,
        (
            "#0301F#11P实际上，确认服用过这种药物的人，\x01",
            "目前只有那位矿工而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x103,
        (
            "#0206F#6P……从伊安律师那里听到的消息\x01",
            "终究也只是传闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "#2410F#5P唔，不管怎么说，\x01",
            "这确实是一种来历不明的奇怪药物，\x01",
            "至少这点是可以确定的。\x02\x03",

            "#2400F──好吧，\x01",
            "那我就留下三片。\x02\x03",

            "立刻就去调查其中的成分。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0004F#12P非常感谢您。\x02\x03",

            "#0000F请问……要鉴定其成分的话，\x01",
            "大概需要多久呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#2400F#5P既然有药的实物，\x01",
            "也有症状等线索……\x02\x03",

            "我想，今日之内至少能\x01",
            "确认其主要成分……\x02\x03",

            "#2406F但反过来说，如果不能顺利查清具体成分的话，\x01",
            "可能就要花上不少时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#0006F#12P是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "#2400F#5P嗯，我明天下午左右\x01",
            "用通讯来联络你们吧。\x02\x03",

            "这样可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#0002F#12P没问题，\x01",
            "那一切就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#0109F#12P呵呵，这下就暂时放心了呢。\x02\x03",

            "#0105F说起来，这种药物有没有可能\x01",
            "附带副作用或引发中毒症状呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "#2403F#5P唔，这个嘛，不经过调查\x01",
            "也不好断言……\x02\x03",

            "#2401F不过，保险起见，你们能不能\x01",
            "给那位矿工的同伴传句话？就说，\x01",
            "如果发生什么异常情况，马上来找我商量。\x02\x03",

            "如果发现了其他服用者，\x01",
            "也请照此安排。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#0100F#12P明白了。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0306F#11P哎呀哎呀……\x01",
            "这种药到底流出去了多少啊。\x02\x03",

            "#0301F市里也在四处流传着\x01",
            "相关的小道消息。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    #C0150
    ChrTalk(
        0x103,
        (
            "#0206F#6P再怎么说，也不可能去向\x01",
            "鲁巴彻那边打听……\x02\x03",

            "#0201F不过，如果他们的成员真的服用过，\x01",
            "实在是担心会不会有什么副作用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#0006F#12P嗯～的确……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        "#2403F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x0)

    #C0153
    ChrTalk(
        0x101,
        "#0005F#12P……医生？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#0101F#12P果然还是有产生副作用的危险吗？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#2405F#5P啊，不……\x01",
            "不是的。\x02\x03",

            "#2410F我只是突然想起了之前\x01",
            "听过的传闻……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#0005F#12P之前听过的传闻……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        "#0301F#11P是怎样的传闻呢？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7526", 0)
    SetCameraDistance(25000, 50000)

    #C0158
    ChrTalk(
        0x8,
        (
            "#2409F#5P哈哈，伤脑筋啊，\x01",
            "其实也不是什么值得\x01",
            "仔细说明的事情……\x02\x03",

            "#2410F──数年前，在制药界\x01",
            "流传过一个奇怪的传闻。\x02\x03",

            "#2401F据说某个狂热的宗教团体\x01",
            "制造出了一种不可思议的药。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0159
    ChrTalk(
        0x101,
        "#0011F#12P狂、狂热的宗教团体……？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#0105F#12P七耀教会中的异端派别……\x01",
            "是类似这种吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#2403F#5P不不，那些家伙似乎\x01",
            "并没有那么简单哦。\x02\x03",

            "#2401F否定女神的存在，\x01",
            "并且崇拜恶魔……\x02\x03",

            "好像是这样的教团。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x101,
        "#0005F#12P崇、崇拜恶魔……！？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#0301F#11P听起来还真是\x01",
            "诡异邪门啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x103,
        "#0205F#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "#2400F#5P哈哈，我也觉得\x01",
            "有些荒诞啦。\x02\x03",

            "#2410F只是，那种药物的效果\x01",
            "倒是有些令人在意……\x02\x03",

            "#2401F──据说它能够借助恶魔的力量，\x01",
            "激发出人类的潜在能力，\x01",
            "甚至还能带来好运。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x102,
        "#0107F#12P这、这是……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#0013F#12P与这次的药物症状一致……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0168
    ChrTalk(
        0x103,
        (
            "#0208F#6P#40W请问……约亚西姆医生……\x02\x03",

            "#0201F#40W那种药物的名字……\x01",
            "您有没有听说过……？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "#2405F#5P嗯，叫什么来着……\x02\x03",

            "#2403F……对了对了，我想起来了。\x02\x03",

            "#2401F『真之睿智（真知）』──\x01",
            "据说是这个名字。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0170
    ChrTalk(
        0x103,
        "#0210F#6P…………唔……………\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#0005F#12P『真之睿智（真知）』……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#0101F#12P还、还真是个\x01",
            "故弄玄虚的名字呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "#2403F#5P嗯，因为内容太过荒诞无稽，\x01",
            "所以这个传闻马上就销声匿迹了。\x02\x03",

            "#2401F只是，也有传闻说，\x01",
            "在去年的利贝尔异变中，\x01",
            "有个奇异的组织在暗中活动吧。\x02\x03",

            "事到如今，还真是令人在意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#0013F#12P（是艾丝蒂尔他们说过的\x01",
            "  『结社』吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        (
            "#0108F#12P（崇拜恶魔的教团……\x01",
            "  会与其存在什么关联吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "#2410F#5P──总而言之，\x01",
            "为了查清蓝色药片的成分，\x01",
            "我打算去问问同行。\x02\x03",

            "#2400F顺便也去确认一下那个传闻\x01",
            "有没有什么后续消息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        "#0001F#12P拜、拜托您了。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        "#0301F#11P借助恶魔之力的药物啊……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        "#0206F#6P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 110690, 150, 57000, 270)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, 106850, 0, 52690, 180)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xC3, 4)
    OP_29(0x4C, 0x1, 0x3)
    OP_68(57830, 1200, 58960, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21440, 0)
    SetChrPos(0x101, 60040, 0, 59000, 270)
    SetChrPos(0x102, 60040, 0, 59000, 270)
    SetChrPos(0x103, 60040, 0, 59000, 270)
    SetChrPos(0x104, 60040, 0, 59000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(20900, 2000)
    OP_6F(0x10)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_68(55830, 1200, 58960, 3000)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    Sound(107, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    OP_6F(0x1)

    #C0180
    ChrTalk(
        0x101,
        (
            "#0006F#6P虽、虽然在最后好像\x01",
            "听到了一些奇怪的话……\x02\x03",

            "#0000F但总之，调查药物成分的事情\x01",
            "就交给医生好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x102,
        (
            "#0100F#5P嗯，也快到傍晚了，\x01",
            "我们快点回克洛斯贝尔市吧。\x02\x03",

            "一科的调查报告书\x01",
            "说不定已经送来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#0306F#11P哎呀哎呀，今晚好像又要\x01",
            "对着一大堆文件干瞪眼了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        "#0208F#12P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21400, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0xC3, 5)
    OP_29(0x4C, 0x1, 0x4)
    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_19_3424 end

    def Function_20_4FFD(): pass

    label("Function_20_4FFD")

    Return()

    # Function_20_4FFD end

    def Function_21_4FFE(): pass

    label("Function_21_4FFE")


    def lambda_5003():
        OP_95(0xFE, 54500, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5003)

    def lambda_501D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_501D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_21_4FFE end

    def Function_22_5039(): pass

    label("Function_22_5039")


    def lambda_503E():
        OP_95(0xFE, 56000, 0, 59800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_503E)

    def lambda_5058():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5058)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xE1, 0x12C)
    Return()

    # Function_22_5039 end

    def Function_23_5074(): pass

    label("Function_23_5074")


    def lambda_5079():
        OP_95(0xFE, 56000, 0, 58000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5079)

    def lambda_5093():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5093)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x13B, 0x12C)
    Return()

    # Function_23_5074 end

    def Function_24_50AF(): pass

    label("Function_24_50AF")


    def lambda_50B4():
        OP_95(0xFE, 57000, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_50B4)

    def lambda_50CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_50CE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x10E, 0x12C)
    Return()

    # Function_24_50AF end

    SaveToFile()

Try(main)
