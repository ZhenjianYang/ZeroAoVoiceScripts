from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1380.bin",                # FileName
        "t1380",                    # MapName
        "t1380",                    # Location
        0x00BA,                     # MapIndex
        "ed7304",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 186, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1380",                  # 0
        "艾莉",                   # 1
        "缇欧",                   # 2
        "诺艾尔",                 # 3
        "瓦吉",                   # 4
        "芙兰",                   # 5
        "莉夏",                   # 6
        "咪西",                   # 7
        "见习生",                 # 8
        "游客",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "游客",                   # 12
        "游客",                   # 13
        "假",                     # 14
        "占卜师",                 # 15
        "蔡特",                   # 16
        "咪雪",                   # 17
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch02900.itc",                   # 02
        "chr/ch03000.itc",                   # 03
        "chr/ch08500.itc",                   # 04
        "chr/ch05200.itc",                   # 05
        "chr/ch10200.itc",                   # 06
        "chr/ch20500.itc",                   # 07
        "chr/ch22802.itc",                   # 08
        "chr/ch22102.itc",                   # 09
        "chr/ch21102.itc",                   # 0A
        "chr/ch24502.itc",                   # 0B
        "chr/ch34302.itc",                   # 0C
        "chr/ch45400.itc",                   # 0D
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

    DeclNpc(-959,    0,       -3099,   0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-1549,   0,       -2500,   45,   389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-500,    0,       -250,    90,   389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1500,    0,       -2349,   90,   389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(500,     0,       -250,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       -250,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1700,    0,       5940,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       6500,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4800,    100,     4400,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4800,    100,     3599,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4800,   100,     4000,    90,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-4800,   100,     -500,    90,   389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-4800,   100,     -1500,   90,   389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-6500,   0,       2609,    180,  389,  0x0, 0,   13,  0,   0,   0,   255, 255, 255,  0)

    DeclEvent(0x0040, 0, 38,  0.0,                   8.0,                   -1.0,                  4.0,                   [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -2.0,                  0.25,                  1.0])

    DeclActor(-5050,   0,       2700,    1000,    -6500,   1500,    2610,    0x007E, 0,  36, 0x0000)
    DeclActor(-1870,   0,       5380,    1200,    -1870,   1500,    5380,    0x007C, 0,  37, 0x0000)

    ChipFrameInfo(1068, 0)                                       # 0

    ScpFunction((
        "Function_0_42C",          # 00, 0
        "Function_1_4E4",          # 01, 1
        "Function_2_561",          # 02, 2
        "Function_3_58B",          # 03, 3
        "Function_4_6D3",          # 04, 4
        "Function_5_857",          # 05, 5
        "Function_6_8FE",          # 06, 6
        "Function_7_A5E",          # 07, 7
        "Function_8_B0E",          # 08, 8
        "Function_9_C35",          # 09, 9
        "Function_10_CFB",         # 0A, 10
        "Function_11_DC4",         # 0B, 11
        "Function_12_EB7",         # 0C, 12
        "Function_13_F6F",         # 0D, 13
        "Function_14_1080",        # 0E, 14
        "Function_15_10C6",        # 0F, 15
        "Function_16_111A",        # 10, 16
        "Function_17_119D",        # 11, 17
        "Function_18_1351",        # 12, 18
        "Function_19_1C49",        # 13, 19
        "Function_20_2A48",        # 14, 20
        "Function_21_2AFC",        # 15, 21
        "Function_22_37C5",        # 16, 22
        "Function_23_380A",        # 17, 23
        "Function_24_3854",        # 18, 24
        "Function_25_3864",        # 19, 25
        "Function_26_464C",        # 1A, 26
        "Function_27_5377",        # 1B, 27
        "Function_28_6108",        # 1C, 28
        "Function_29_6DA1",        # 1D, 29
        "Function_30_77C9",        # 1E, 30
        "Function_31_84C0",        # 1F, 31
        "Function_32_902B",        # 20, 32
        "Function_33_9C87",        # 21, 33
        "Function_34_A9DA",        # 22, 34
        "Function_35_B6D9",        # 23, 35
        "Function_36_C450",        # 24, 36
        "Function_37_CBC6",        # 25, 37
        "Function_38_CC2C",        # 26, 38
    ))


    def Function_0_42C(): pass

    label("Function_0_42C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_46C"),
        (1, "loc_478"),
        (2, "loc_484"),
        (3, "loc_490"),
        (4, "loc_49C"),
        (5, "loc_4A8"),
        (6, "loc_4B4"),
        (SWITCH_DEFAULT, "loc_4C0"),
    )


    label("loc_46C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_478")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_484")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_490")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_49C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4E3")

    Return()

    # Function_0_42C end

    def Function_1_4E4(): pass

    label("Function_1_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_4F2")
    Jump("loc_560")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_500")
    Jump("loc_560")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_50E")
    Jump("loc_560")

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_51F")
    Call(0, 17)
    Jump("loc_560")

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_52D")
    Jump("loc_560")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_53B")
    Jump("loc_560")

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_560")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_557")
    Jump("loc_560")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_560")

    label("loc_560")

    Return()

    # Function_1_4E4 end

    def Function_2_561(): pass

    label("Function_2_561")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A")
    OP_66(0x0, 0x1)

    label("loc_58A")

    Return()

    # Function_2_561 end

    def Function_3_58B(): pass

    label("Function_3_58B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A4")
    Jump("loc_6CF")

    label("loc_5A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA")
    Jump("loc_6CF")

    label("loc_5BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")
    Jump("loc_6CF")

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E6")
    Jump("loc_6CF")

    label("loc_5E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66D")

    #C0001
    ChrTalk(
        0x8,
        (
            "#00100F嗯……最后一张票该\x01",
            "用在什么地方呢？\x02\x03",

            "#00104F如果可以，我想选个\x01",
            "能留下宝贵回忆的地方……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6CF")

    label("loc_66D")


    #C0002
    ChrTalk(
        0x8,
        (
            "#00100F如果可以，我想把\x01",
            "最后一张票用在可以留下\x01",
            "宝贵回忆的地方……\x02\x03",

            "#00104F嗯……去哪里好呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CF")

    TalkEnd(0xFE)
    Return()

    # Function_3_58B end

    def Function_4_6D3(): pass

    label("Function_4_6D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EC")
    Jump("loc_853")

    label("loc_6EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_702")
    Jump("loc_853")

    label("loc_702")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C1")

    #C0003
    ChrTalk(
        0x9,
        (
            "#00200F我一直在\x01",
            "跟着咪西……\x02\x03",

            "它不光会去主要的游乐设施，\x01",
            "还会在园内四处巡游。\x02\x03",

            "#00204F为了能让更多的咪西迷看到自己，\x01",
            "它真是非常努力呢……\x01",
            "不愧是咪西。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_827")

    label("loc_7C1")


    #C0004
    ChrTalk(
        0x9,
        (
            "#00200F说起来，我到现在都没找到\x01",
            "咪西的妹妹『咪雪』。\x02\x03",

            "#00204F难道它只在特定时间\x01",
            "才会出现吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_827")

    Jump("loc_853")

    label("loc_82C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_842")
    Jump("loc_853")

    label("loc_842")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_853")

    label("loc_853")

    TalkEnd(0xFE)
    Return()

    # Function_4_6D3 end

    def Function_5_857(): pass

    label("Function_5_857")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87D")
    Call(0, 16)
    Jump("loc_8A2")

    label("loc_87D")


    #C0005
    ChrTalk(
        0xA,
        "#10106F芙、芙兰，你可真是的……\x02",
    )

    CloseMessageWindow()

    label("loc_8A2")

    Jump("loc_8FA")

    label("loc_8A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BD")
    Jump("loc_8FA")

    label("loc_8BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D3")
    Jump("loc_8FA")

    label("loc_8D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E9")
    Jump("loc_8FA")

    label("loc_8E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FA")

    label("loc_8FA")

    TalkEnd(0xFE)
    Return()

    # Function_5_857 end

    def Function_6_8FE(): pass

    label("Function_6_8FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_917")
    Jump("loc_A5A")

    label("loc_917")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D")
    Jump("loc_A5A")

    label("loc_92D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_943")
    Jump("loc_A5A")

    label("loc_943")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FE")

    #C0006
    ChrTalk(
        0xB,
        (
            "#10300F呵呵，这个沙发\x01",
            "看上去很不错啊。\x02\x03",

            "#10304F在想好下一个目的地之前，\x01",
            "我就在这里尽情休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0007
    ChrTalk(
        0x101,
        "#00006F喂喂……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A44")

    label("loc_9FE")


    #C0008
    ChrTalk(
        0xB,
        (
            "#10304F呵呵，在想好下一个目的地之前，\x01",
            "我就在这里尽情休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A44")

    Jump("loc_A5A")

    label("loc_A49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5A")

    label("loc_A5A")

    TalkEnd(0xFE)
    Return()

    # Function_6_8FE end

    def Function_7_A5E(): pass

    label("Function_7_A5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A84")
    Call(0, 16)
    Jump("loc_AB2")

    label("loc_A84")


    #C0009
    ChrTalk(
        0xC,
        (
            "#06409F姐姐，去占卜一下\x01",
            "你的恋爱运吧～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB2")

    Jump("loc_B0A")

    label("loc_AB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACD")
    Jump("loc_B0A")

    label("loc_ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE3")
    Jump("loc_B0A")

    label("loc_AE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF9")
    Jump("loc_B0A")

    label("loc_AF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0A")

    label("loc_B0A")

    TalkEnd(0xFE)
    Return()

    # Function_7_A5E end

    def Function_8_B0E(): pass

    label("Function_8_B0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B27")
    Jump("loc_C31")

    label("loc_B27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B94")

    #C0010
    ChrTalk(
        0xD,
        (
            "#01805F（东方的占卜师……）\x02\x03",

            "#01803F（突然想到了\x01",
            "  一个人……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_BEF")

    label("loc_B94")


    #C0011
    ChrTalk(
        0xD,
        (
            "#01805F啊……罗伊德警官，\x01",
            "你在这里啊。\x02\x03",

            "#01809F哈哈……\x01",
            "好长的队伍啊，\x01",
            "真是让人吃惊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEF")

    Jump("loc_C31")

    label("loc_BF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0A")
    Jump("loc_C31")

    label("loc_C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C20")
    Jump("loc_C31")

    label("loc_C20")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C31")

    label("loc_C31")

    TalkEnd(0xFE)
    Return()

    # Function_8_B0E end

    def Function_9_C35(): pass

    label("Function_9_C35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E")
    Jump("loc_CF7")

    label("loc_C4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C64")
    Jump("loc_CF7")

    label("loc_C64")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD0")

    #C0012
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "这里的占卜师姐姐\x01",
            "非常厉害哦～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，可以让她给你\x01",
            "占卜各种运势哦！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF7")

    label("loc_CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE6")
    Jump("loc_CF7")

    label("loc_CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF7")

    label("loc_CF7")

    TalkEnd(0xFE)
    Return()

    # Function_9_C35 end

    def Function_10_CFB(): pass

    label("Function_10_CFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC0")
    TalkBegin(0xFE)

    #C0014
    ChrTalk(
        0xFE,
        "欢迎来到『占卜馆』！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "在这里，可以让非常厉害的占卜师\x01",
            "给大家占卜各种运势！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00003F（我们还在和咪雪捉迷藏呢……\x01",
            "　现在还是不要\x01",
            "　进这种地方了。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_DC3")

    label("loc_DC0")

    Call(0, 18)

    label("loc_DC3")

    Return()

    # Function_10_CFB end

    def Function_11_DC4(): pass

    label("Function_11_DC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E41")

    #C0017
    ChrTalk(
        0x10,
        (
            "放眼望去，这里尽是\x01",
            "女孩子呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10,
        (
            "还好我是和女朋友一起来的，\x01",
            "如果一个人来这里，一定会很郁闷。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB3")

    label("loc_E41")


    #C0019
    ChrTalk(
        0x10,
        (
            "缘分占卜的结果还不错，\x01",
            "我女朋友很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x10,
        (
            "如果占卜出了不好的结果……\x01",
            "后果恐怕就不只是气氛尴尬那么简单了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB3")

    TalkEnd(0xFE)
    Return()

    # Function_11_DC4 end

    def Function_12_EB7(): pass

    label("Function_12_EB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F09")

    #C0021
    ChrTalk(
        0x11,
        (
            "呵呵呵，占卜什么好呢？\x01",
            "还是测测我和男朋友的缘分吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6B")

    label("loc_F09")


    #C0022
    ChrTalk(
        0x11,
        (
            "那位占卜师说，\x01",
            "我们两个被命运之线\x01",
            "联系在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x11,
        (
            "呵呵呵呵呵……\x01",
            "看来我果然\x01",
            "没有选错人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6B")

    TalkEnd(0xFE)
    Return()

    # Function_12_EB7 end

    def Function_13_F6F(): pass

    label("Function_13_F6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE4")

    #C0024
    ChrTalk(
        0x12,
        (
            "我瞒着丈夫来这里，\x01",
            "想请占卜师告诉我\x01",
            "丢失的结婚戒指在哪里。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x12,
        "怎么还不快点轮到我……\x02",
    )

    CloseMessageWindow()
    Jump("loc_107C")

    label("loc_FE4")


    #C0026
    ChrTalk(
        0x12,
        (
            "我本以为结婚戒指已经丢失了，\x01",
            "请占卜师占卜之后……\x01",
            "发现它居然就在口袋里。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x12,
        (
            "『灯下黑』这句话真是没说错啊……\x01",
            "虽说找到了戒指，\x01",
            "但总觉得好丢脸啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107C")

    TalkEnd(0xFE)
    Return()

    # Function_13_F6F end

    def Function_14_1080(): pass

    label("Function_14_1080")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C2")

    #C0028
    ChrTalk(
        0x13,
        (
            "如果能占卜出美妙邂逅的\x01",
            "暗示就好了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C2")

    label("loc_10C2")

    TalkEnd(0xFE)
    Return()

    # Function_14_1080 end

    def Function_15_10C6(): pass

    label("Function_15_10C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1116")

    #C0029
    ChrTalk(
        0x14,
        (
            "男人什么的根本无所谓，\x01",
            "我只想占卜一下自己的财运。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1116")

    label("loc_1116")

    TalkEnd(0xFE)
    Return()

    # Function_15_10C6 end

    def Function_16_111A(): pass

    label("Function_16_111A")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0030
    ChrTalk(
        0xC,
        (
            "#06400F姐姐，快点快点～\x01",
            "快来排队啊～\x02\x03",

            "#06409F我们请占卜师占卜一下\x01",
            "姐姐的恋爱运！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        "#10111F不、不要啦！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_111A end

    def Function_17_119D(): pass

    label("Function_17_119D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11E9")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_11E9")

    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x8)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_128B")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_1350")

    label("loc_128B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B5")
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B0")
    SetChrFlags(0xD, 0x10)

    label("loc_12B0")

    Jump("loc_1350")

    label("loc_12B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D5")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1350")

    label("loc_12D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1330")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1310")
    SetChrFlags(0xB, 0x80)

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132B")
    ClearChrFlags(0x18, 0x80)

    label("loc_132B")

    Jump("loc_1350")

    label("loc_1330")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1350")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_1350")

    Return()

    # Function_17_119D end

    def Function_18_1351(): pass

    label("Function_18_1351")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1000, 5750, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x101, 0, 0, 5000, 0)
    OP_0D()

    #C0032
    ChrTalk(
        0xF,
        "欢迎来到『占卜馆』！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xF,
        (
            "在这里，可以让非常厉害的占卜师\x01",
            "给大家占卜各种运势！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xF,
        (
            "每次最多接待两名客人，\x01",
            "您想邀请哪位呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#00004F#6P（……要邀请谁呢？）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K邀请谁？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "艾莉")
    MenuCmd(1, 0, "缇欧")
    MenuCmd(1, 0, "兰迪")
    MenuCmd(1, 0, "诺艾尔")
    MenuCmd(1, 0, "瓦吉")
    MenuCmd(1, 0, "琪雅")
    MenuCmd(1, 0, "芙兰")
    MenuCmd(1, 0, "塞茜尔")
    MenuCmd(1, 0, "伊莉娅")
    MenuCmd(1, 0, "莉夏")
    MenuCmd(1, 0, "修利")
    MenuCmd(1, 0, "放弃")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_14F3")
    MenuCmd(3, 0, 0x0)

    label("loc_14F3")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1505")
    MenuCmd(3, 0, 0x1)

    label("loc_1505")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1517")
    MenuCmd(3, 0, 0x2)

    label("loc_1517")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1529")
    MenuCmd(3, 0, 0x3)

    label("loc_1529")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_153B")
    MenuCmd(3, 0, 0x4)

    label("loc_153B")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_154D")
    MenuCmd(3, 0, 0x5)

    label("loc_154D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_155F")
    MenuCmd(3, 0, 0x6)

    label("loc_155F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1571")
    MenuCmd(3, 0, 0x7)

    label("loc_1571")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1583")
    MenuCmd(3, 0, 0x8)

    label("loc_1583")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1595")
    MenuCmd(3, 0, 0x9)

    label("loc_1595")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_15A7")
    MenuCmd(3, 0, 0xA)

    label("loc_15A7")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C00")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_162D"),
        (1, "loc_1665"),
        (2, "loc_169D"),
        (3, "loc_16D5"),
        (4, "loc_170F"),
        (5, "loc_1747"),
        (6, "loc_177F"),
        (7, "loc_17B7"),
        (8, "loc_17F5"),
        (9, "loc_1833"),
        (10, "loc_186B"),
        (SWITCH_DEFAULT, "loc_18A3"),
    )


    label("loc_162D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0037
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请艾莉吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_1665")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0038
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请缇欧吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_169D")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0039
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请兰迪吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_16D5")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0040
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请诺艾尔吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_170F")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0041
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请瓦吉吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_1747")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0042
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请琪雅吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_177F")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0043
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请芙兰吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_17B7")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0044
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请塞茜尔姐姐吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_17F5")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请伊莉娅小姐吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_1833")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0046
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请莉夏吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_186B")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0047
    ChrTalk(
        0x101,
        "#00000F#6P（好……那就邀请修利吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_18A3")

    FadeToDark(500, 0, -1)
    OP_0D()
    LoadEffect(0x0, "event/ev13000.eff")
    LoadChrToIndex("chr/ch14202.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00300.itc", 0x21)
    LoadChrToIndex("chr/ch08200.itc", 0x22)
    LoadChrToIndex("chr/ch07500.itc", 0x23)
    LoadChrToIndex("chr/ch05100.itc", 0x24)
    LoadChrToIndex("chr/ch10100.itc", 0x25)
    LoadChrToIndex("chr/ch02710.itc", 0x26)
    LoadChrToIndex("chr/ch02702.itc", 0x27)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 0, 50, 104800, 180)
    ClearChrFlags(0x15, 0x80)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1967"),
        (1, "loc_1976"),
        (2, "loc_1985"),
        (3, "loc_1994"),
        (4, "loc_19A3"),
        (5, "loc_19B2"),
        (6, "loc_19C1"),
        (7, "loc_19D0"),
        (8, "loc_19DF"),
        (9, "loc_19EE"),
        (10, "loc_19FD"),
        (SWITCH_DEFAULT, "loc_1A0C"),
    )


    label("loc_1967")

    LoadChrToIndex("chr/ch00102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_1A0C")

    label("loc_1976")

    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_1A0C")

    label("loc_1985")

    LoadChrToIndex("chr/ch00302.itc", 0x20)
    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_1A0C")

    label("loc_1994")

    LoadChrToIndex("chr/ch02902.itc", 0x20)
    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_1A0C")

    label("loc_19A3")

    LoadChrToIndex("chr/ch03002.itc", 0x20)
    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_1A0C")

    label("loc_19B2")

    LoadChrToIndex("chr/ch08202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_1A0C")

    label("loc_19C1")

    LoadChrToIndex("chr/ch08502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_1A0C")

    label("loc_19D0")

    LoadChrToIndex("chr/ch07502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_1A0C")

    label("loc_19DF")

    LoadChrToIndex("chr/ch05102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_1A0C")

    label("loc_19EE")

    LoadChrToIndex("chr/ch05202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_1A0C")

    label("loc_19FD")

    LoadChrToIndex("chr/ch10102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_1A0C")

    label("loc_1A0C")

    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x101, -500, 0, 5000, 0)
    SetChrPos(0x15, 500, 0, 5000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0048
    ChrTalk(
        0xF,
        "那我就收下您的票了！\x02",
    )

    CloseMessageWindow()
    SubItemNumber('米修拉姆·奇幻乐园游乐券', 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "交给工作人员一张票。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0050
    ChrTalk(
        0xF,
        "二位请进！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 19)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1B35"),
        (1, "loc_1B43"),
        (2, "loc_1B51"),
        (3, "loc_1B5F"),
        (4, "loc_1B6D"),
        (5, "loc_1B7B"),
        (6, "loc_1B89"),
        (7, "loc_1B97"),
        (8, "loc_1BA5"),
        (9, "loc_1BB3"),
        (10, "loc_1BC1"),
        (SWITCH_DEFAULT, "loc_1BCF"),
    )


    label("loc_1B35")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1B43")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1B51")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1B5F")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1B6D")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1B7B")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1B89")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1B97")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1BA5")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1BB3")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1BC1")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1BCF")

    label("loc_1BCF")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFB")
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_1BFB")

    Jump("loc_1C31")

    label("loc_1C00")


    #C0051
    ChrTalk(
        0xF,
        "哎呀，不进去了吗？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xF,
        "期待您再次光临！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1C31")

    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 0, 0, 4000, 180)
    EventEnd(0x5)
    Return()

    # Function_18_1351 end

    def Function_19_1C49(): pass

    label("Function_19_1C49")

    SoundLoad(852)
    SetChrPos(0x101, -500, 0, 93000, 0)
    SetChrPos(0x15, 500, 0, 93000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 900, 97500, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 900, 100000, 3000)
    Sleep(500)

    def lambda_1CD4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CD4)

    def lambda_1CE5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1CE5)

    def lambda_1CF6():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CF6)
    Sleep(0)

    def lambda_1D0E():
        OP_9B(0x0, 0x15, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1D0E)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x15, 2)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_258D")

    #C0053
    ChrTalk(
        0x16,
        "#5P呵呵，欢迎。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x16,
        "#5P来，请坐在椅子上吧。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00000F#6P好、好的。\x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    #C0056
    ChrTalk(
        0x101,
        (
            "#00003F#6P（正如大家所说，\x01",
            "  是个充满异国情调的神秘人物呢……）\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1E27"),
        (1, "loc_1E6D"),
        (2, "loc_1EC8"),
        (3, "loc_1F2B"),
        (4, "loc_1F88"),
        (5, "loc_202A"),
        (6, "loc_2072"),
        (7, "loc_20C0"),
        (8, "loc_210C"),
        (9, "loc_215E"),
        (10, "loc_21AC"),
        (SWITCH_DEFAULT, "loc_2201"),
    )


    label("loc_1E27")


    #N0057
    NpcTalk(
        0x15,
        "艾莉",
        (
            "#00100F#12P（嗯，虽然遮住了容貌，\x01",
            "  但应该是位美人。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_1E6D")


    #N0058
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00200F#12P（嗯，而且……\x01",
            "  虽然她遮住了自己的容貌，\x01",
            "  但应该是位大美人。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_1EC8")


    #N0059
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00300F#12P（是啊，而且……\x01",
            "  虽然她遮住了面容，但肯定\x01",
            "  是一位相当美貌的大姐姐。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_1F2B")


    #N0060
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10100F#12P（是啊，而且……\x01",
            "  虽然遮住了自己的容貌，\x01",
            "  但应该是位大美人。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_1F88")


    #N0061
    NpcTalk(
        0x15,
        "瓦吉",
        "#10305F#12P（…………哦…………？）\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#00005F#6P（……瓦吉？）\x02",
    )

    CloseMessageWindow()

    #N0063
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10304F#12P（呵呵，没想到这位占卜师会如此美貌，\x01",
            "  稍微吃了一惊而已。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_202A")


    #N0064
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01100F#12P（嗯……虽然遮住了面容，\x01",
            "  但应该非常漂亮～）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_2072")


    #N0065
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06400F#12P（是啊，虽然遮住了面容，\x01",
            "  但应该是个超级大美人～）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_20C0")


    #N0066
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05900F#12P（是啊，虽然遮住了面容，\x01",
            "  但应该是位大美人。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_210C")


    #N0067
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01700F#12P（嗯，虽然遮住了面容，\x01",
            "  但应该是个很漂亮的美女呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_215E")


    #N0068
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01802F#12P（是啊……虽然她遮住了面容，\x01",
            "  但应该很美丽呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_21AC")


    #N0069
    NpcTalk(
        0x15,
        "修利",
        (
            "#14000F#12P（嗯，而且……\x01",
            "  虽然她遮住了面容，\x01",
            "  但应该是位大美人。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2201")

    label("loc_2201")


    #C0070
    ChrTalk(
        0x16,
        (
            "#5P呵呵，怎么了？\x01",
            "为何一直盯着我的脸？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x16,
        (
            "#5P后边还有不少客人在排队，\x01",
            "我们还是马上开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00012F#6P啊，抱歉，\x01",
            "那就麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x16,
        "#5P呵呵，在占卜之前……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x16,
        (
            "#5P可以把你们的血型\x01",
            "告诉我吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_233F"),
        (1, "loc_2366"),
        (2, "loc_238D"),
        (3, "loc_23B0"),
        (4, "loc_23D5"),
        (5, "loc_23F8"),
        (6, "loc_241B"),
        (7, "loc_2440"),
        (8, "loc_2469"),
        (9, "loc_249F"),
        (10, "loc_24C6"),
        (SWITCH_DEFAULT, "loc_24EB"),
    )


    label("loc_233F")


    #N0075
    NpcTalk(
        0x15,
        "艾莉",
        "#00105F#12P血型吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_2366")


    #N0076
    NpcTalk(
        0x15,
        "缇欧",
        "#00205F#12P血型吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_238D")


    #N0077
    NpcTalk(
        0x15,
        "兰迪",
        "#00305F#12P血型吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_23B0")


    #N0078
    NpcTalk(
        0x15,
        "诺艾尔",
        "#10105F#12P血型吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_23D5")


    #N0079
    NpcTalk(
        0x15,
        "瓦吉",
        "#10305F#12P血型吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_23F8")


    #N0080
    NpcTalk(
        0x15,
        "琪雅",
        "#01105F#12P血型～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_241B")


    #N0081
    NpcTalk(
        0x15,
        "芙兰",
        "#06405F#12P血型吗～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_2440")


    #N0082
    NpcTalk(
        0x15,
        "塞茜尔",
        "#05905F#12P血型吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_2469")


    #N0083
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01705F#12P血型……\x01",
            "还要参考这个吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_249F")


    #N0084
    NpcTalk(
        0x15,
        "莉夏",
        "#01805F#12P血型吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_24C6")


    #N0085
    NpcTalk(
        0x15,
        "修利",
        "#14005F#12P血型……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EB")

    label("loc_24EB")


    #C0086
    ChrTalk(
        0x16,
        (
            "#5P是的，为了占卜出准确结果，\x01",
            "血型是必需的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x16,
        (
            "#5P当然了，如果不愿意说，\x01",
            "我也不会强求。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00000F#6P哪里，这没什么可保密的，\x01",
            "我的血型是Ｏ型。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2682")

    label("loc_258D")


    #C0089
    ChrTalk(
        0x16,
        "#5P啊，你是之前那位……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x16,
        (
            "#5P呵呵，欢迎欢迎，\x01",
            "请坐在椅子上吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#00000F#6P好的。\x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    #C0092
    ChrTalk(
        0x16,
        (
            "#5P你能再次到来，\x01",
            "我非常高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x16,
        (
            "#5P那么，\x01",
            "可以把你们的血型\x01",
            "告诉我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x16,
        (
            "#5P……如果没记错，\x01",
            "这位客人是Ｏ型吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00000F#6P嗯，是的。\x02",
    )

    CloseMessageWindow()

    label("loc_2682")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_26CD"),
        (1, "loc_26FC"),
        (2, "loc_2725"),
        (3, "loc_274C"),
        (4, "loc_2773"),
        (5, "loc_27A4"),
        (6, "loc_281B"),
        (7, "loc_286A"),
        (8, "loc_2895"),
        (9, "loc_28BE"),
        (10, "loc_290B"),
        (SWITCH_DEFAULT, "loc_2941"),
    )


    label("loc_26CD")


    #N0096
    NpcTalk(
        0x15,
        "艾莉",
        "#00100F#12P哦，我的血型是Ａ型。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_26FC")


    #N0097
    NpcTalk(
        0x15,
        "缇欧",
        "#00200F#12P我是ＡＢ型的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_2725")


    #N0098
    NpcTalk(
        0x15,
        "兰迪",
        "#00300F#12P我是Ｂ型血。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_274C")


    #N0099
    NpcTalk(
        0x15,
        "诺艾尔",
        "#10100F#12P我是Ａ型。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_2773")


    #N0100
    NpcTalk(
        0x15,
        "瓦吉",
        "#10300F#12P呵呵，我记得是ＡＢ型。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_27A4")


    #N0101
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01109F#12P嗯……我应该是\x01",
            "Ｂ型～\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00000F#6P哦，想起来了，你以前在乌尔斯拉医院\x01",
            "检查身体时测过血型。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_281B")


    #N0103
    NpcTalk(
        0x15,
        "芙兰",
        "#06409F#12P啊，我也是Ｏ型哦！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#00009F#6P哈哈，我们一样呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_286A")


    #N0105
    NpcTalk(
        0x15,
        "塞茜尔",
        "#05900F#12P哦，我是Ａ型。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_2895")


    #N0106
    NpcTalk(
        0x15,
        "伊莉娅",
        "#01700F#12P我是Ｂ型哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_28BE")


    #N0107
    NpcTalk(
        0x15,
        "莉夏",
        "#01802F#12P啊……我也是Ｏ型呢。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00009F#6P哈哈，真巧啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_290B")


    #N0109
    NpcTalk(
        0x15,
        "修利",
        (
            "#14000F#12P这个嘛……\x01",
            "我大概是Ａ型吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2941")

    label("loc_2941")


    #C0110
    ChrTalk(
        0x16,
        "#5P呵呵……好的。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x16,
        "#5P那么，二位想占卜些什么呢？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#00000F#6P这个，我想想……\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_29E6"),
        (1, "loc_29EE"),
        (2, "loc_29F6"),
        (3, "loc_29FE"),
        (4, "loc_2A06"),
        (5, "loc_2A0E"),
        (6, "loc_2A16"),
        (7, "loc_2A1E"),
        (8, "loc_2A26"),
        (9, "loc_2A2E"),
        (10, "loc_2A36"),
        (SWITCH_DEFAULT, "loc_2A3E"),
    )


    label("loc_29E6")

    Call(0, 25)
    Jump("loc_2A3E")

    label("loc_29EE")

    Call(0, 26)
    Jump("loc_2A3E")

    label("loc_29F6")

    Call(0, 27)
    Jump("loc_2A3E")

    label("loc_29FE")

    Call(0, 28)
    Jump("loc_2A3E")

    label("loc_2A06")

    Call(0, 29)
    Jump("loc_2A3E")

    label("loc_2A0E")

    Call(0, 30)
    Jump("loc_2A3E")

    label("loc_2A16")

    Call(0, 31)
    Jump("loc_2A3E")

    label("loc_2A1E")

    Call(0, 32)
    Jump("loc_2A3E")

    label("loc_2A26")

    Call(0, 33)
    Jump("loc_2A3E")

    label("loc_2A2E")

    Call(0, 34)
    Jump("loc_2A3E")

    label("loc_2A36")

    Call(0, 35)
    Jump("loc_2A3E")

    label("loc_2A3E")

    OP_24(0x354)
    Call(0, 17)
    Call(0, 21)
    Return()

    # Function_19_1C49 end

    def Function_20_2A48(): pass

    label("Function_20_2A48")

    OP_68(0, 900, 103500, 3000)
    SetCameraDistance(15000, 3000)

    def lambda_2A67():
        OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A67)

    def lambda_2A7C():
        OP_9B(0x0, 0xFE, 0xA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2A7C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x15, 1)

    def lambda_2A99():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A99)

    def lambda_2AA6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2AA6)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x15, 2)
    OP_6F(0x79)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -630, 50, 101950, 0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 630, 50, 101950, 0)
    OP_0D()
    Return()

    # Function_20_2A48 end

    def Function_21_2AFC(): pass

    label("Function_21_2AFC")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2B4F"),
        (1, "loc_2B58"),
        (2, "loc_2B61"),
        (3, "loc_2B6A"),
        (4, "loc_2B73"),
        (5, "loc_2B7C"),
        (6, "loc_2B85"),
        (7, "loc_2B8E"),
        (8, "loc_2B97"),
        (9, "loc_2BA0"),
        (10, "loc_2BA9"),
        (SWITCH_DEFAULT, "loc_2BB2"),
    )


    label("loc_2B4F")

    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_2BB2")

    label("loc_2B58")

    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_2BB2")

    label("loc_2B61")

    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_2BB2")

    label("loc_2B6A")

    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_2BB2")

    label("loc_2B73")

    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_2BB2")

    label("loc_2B7C")

    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_2BB2")

    label("loc_2B85")

    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_2BB2")

    label("loc_2B8E")

    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_2BB2")

    label("loc_2B97")

    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_2BB2")

    label("loc_2BA0")

    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_2BB2")

    label("loc_2BA9")

    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_2BB2")

    label("loc_2BB2")

    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -600, 0, 5000, 90)
    SetChrPos(0x15, 600, 0, 5000, 270)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C06")
    SetChrPos(0x17, 1700, 0, 4040, 270)

    label("loc_2C06")

    OP_68(0, 1500, 5750, 0)
    OP_68(0, 1000, 5750, 3000)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2C9C"),
        (1, "loc_2D93"),
        (2, "loc_2E91"),
        (3, "loc_2F8A"),
        (4, "loc_307C"),
        (5, "loc_3167"),
        (6, "loc_32B8"),
        (7, "loc_33CF"),
        (8, "loc_34BD"),
        (9, "loc_35BF"),
        (10, "loc_36E3"),
        (SWITCH_DEFAULT, "loc_37C4"),
    )


    label("loc_2C9C")


    #N0113
    NpcTalk(
        0x15,
        "艾莉",
        (
            "#00100F#11P呼……度过了一段\x01",
            "充满神秘感的时间呢。\x02\x03",

            "#00104F那位占卜师散发出来的气息\x01",
            "实在是让人不知所措。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#00003F#5P是啊……\x01",
            "看来不是等闲之辈。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0115
    NpcTalk(
        0x15,
        "艾莉",
        "#00100F#11P嗯，一会见吧。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_2D93")


    #N0116
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00202F在那位占卜师占卜的时候，\x01",
            "我可以感觉到一股强烈的气场。\x02\x03",

            "#00204F真不愧是传说中的占卜师，\x01",
            "看来并非等闲之辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00004F确实……\x01",
            "感觉是个很厉害的人物。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0118
    NpcTalk(
        0x15,
        "缇欧",
        "#00200F好的，一会见。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_2E91")


    #N0119
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00309F……呼，话说回来，\x01",
            "真是个很棒的大姐姐啊。\x02\x03",

            "#00304F那种神秘的气质\x01",
            "让我已经忍受不了啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……的确。\x01",
            "而且她的占卜也惊人地\x01",
            "准确呢。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0121
    NpcTalk(
        0x15,
        "兰迪",
        "#00300F嗯，待会再见吧。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_2F8A")


    #N0122
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10100F……呼……度过了一段\x01",
            "充满神秘感的时间呢。\x02\x03",

            "#10104F她的占卜结果很有说服力，\x01",
            "给人一种不可思议的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#00004F是啊……\x01",
            "真是很有意思。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0124
    NpcTalk(
        0x15,
        "诺艾尔",
        "#10100F好的，再见！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_307C")


    #N0125
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10300F呵呵，真是位很有\x01",
            "意思的大姐姐。\x02\x03",

            "#10304F其实我本想和她\x01",
            "多聊几句呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，确实。\x01",
            "经她占卜之后，\x01",
            "似乎连思维都更加宽广了。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0127
    NpcTalk(
        0x15,
        "瓦吉",
        "#10300F嗯，待会见。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_3167")


    #N0128
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01109F占卜真是很有趣啊～\x02\x03",

            "#01111F她为什么会知道那么多事情呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00009F唔……这我就不清楚了，\x01",
            "应该是在相当艰辛的修行中\x01",
            "积累而成的吧？\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0130
    NpcTalk(
        0x15,
        "琪雅",
        "#01100F嗯，待会见～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A9")

    #C0131
    ChrTalk(
        0x17,
        "#01200F……嗷。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    EndChrThread(0x17, 0x0)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xB4, 0x1F4)

    def lambda_3287():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3287)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x15, 3)
    SetChrFlags(0x17, 0x80)
    Jump("loc_32B3")

    label("loc_32A9")

    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)

    label("loc_32B3")

    Jump("loc_37C4")

    label("loc_32B8")


    #N0132
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06402F呼，总觉得那个大姐姐\x01",
            "很神秘呢～\x02\x03",

            "#06409F姐姐那种帅气的女性自然很棒，\x01",
            "但这种充满神秘感的类型\x01",
            "也很让人憧憬呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#00002F哈哈……在克洛斯贝尔，\x01",
            "这种类型的女性确实相当罕见。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0134
    NpcTalk(
        0x15,
        "芙兰",
        "#06400F好的，一会见～！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_33CF")


    #N0135
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05909F呵呵……真是个\x01",
            "不可思议的人呢。\x02\x03",

            "#05904F她似乎有着\x01",
            "很复杂的过去……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00003F嗯……不知她是因为\x01",
            "什么缘由而来到克洛斯贝尔的。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0137
    NpcTalk(
        0x15,
        "塞茜尔",
        "#05900F好的，一会见吧。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_34BD")


    #N0138
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01702F哎呀呀～这世上还真是\x01",
            "存在着各种各样的厉害人物啊。\x02\x03",

            "#01703F明明只是初次见面，但却让我\x01",
            "有种被完全看透的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x01",
            "看来她不是寻常之辈。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0140
    NpcTalk(
        0x15,
        "伊莉娅",
        "#01700F嗯，一会见啦～\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_35BF")


    #N0141
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01803F（能施展那么高级的占卜术……\x01",
            "  那位女性难道是……）\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#00005F莉夏，怎么了？\x02",
    )

    CloseMessageWindow()

    #N0143
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01805F啊，没什么。\x02\x03",

            "#01802F呵呵，能有这么不可思议的体验，\x01",
            "真是很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，我也是。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0145
    NpcTalk(
        0x15,
        "莉夏",
        "#01803F好的，待会见。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_36E3")


    #N0146
    NpcTalk(
        0x15,
        "修利",
        (
            "#14000F……那个占卜师真是好厉害啊。\x02\x03",

            "#14006F我原本并不相信什么占卜，\x01",
            "但这次却是例外。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#00004F是啊……\x01",
            "她的占卜确实很准确。\x02\x03",

            "#00000F……好，那我先留在这里\x01",
            "再看看。\x02",
        )
    )

    CloseMessageWindow()

    #N0148
    NpcTalk(
        0x15,
        "修利",
        "#14000F……嗯，再见。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_37C4")

    label("loc_37C4")

    Return()

    # Function_21_2AFC end

    def Function_22_37C5(): pass

    label("Function_22_37C5")


    def lambda_37CA():

        label("loc_37CA")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_37CA")

    QueueWorkItem2(0x101, 2, lambda_37CA)
    OP_93(0x15, 0xB4, 0x1F4)

    def lambda_37E3():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_37E3)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x15, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_22_37C5 end

    def Function_23_380A(): pass

    label("Function_23_380A")

    Fade(500)
    Sound(895, 0, 50, 0)
    Sound(852, 2, 70, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 900, 103300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Return()

    # Function_23_380A end

    def Function_24_3854(): pass

    label("Function_24_3854")

    Fade(500)
    StopSound(852, 1000, 40)
    StopEffect(0x0, 0x2)
    OP_0D()
    Return()

    # Function_24_3854 end

    def Function_25_3864(): pass

    label("Function_25_3864")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",      # 0
            "让艾莉决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4051")

    #C0150
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0152
    NpcTalk(
        0x15,
        "艾莉",
        "#00112F#12P罗、罗伊德……！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0153
    ChrTalk(
        0x101,
        (
            "#00009F#6P这种机会很少有嘛，难得两个人\x01",
            "一起来，我们就测一下吧。\x02\x03",

            "#00000F反正只是随便试试而已。\x02",
        )
    )

    CloseMessageWindow()

    #N0154
    NpcTalk(
        0x15,
        "艾莉",
        "#00106F#12P随、随便试试……？你可真是……\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        (
            "#00005F#6P哎……有什么不对的吗？\x02\x03",

            "#00003F如果你实在不愿意，那就算了吧……\x02",
        )
    )

    CloseMessageWindow()

    #N0156
    NpcTalk(
        0x15,
        "艾莉",
        (
            "#00105F#12P倒、倒也不是不愿意……\x02\x03",

            "#00113F真是的，你怎么总是这样……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0157
    NpcTalk(
        0x15,
        "艾莉",
        (
            "#00111F#12P……唉，算了。\x02\x03",

            "#00100F不好意思，那就请您占卜一下\x01",
            "我们的缘分吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0158
    ChrTalk(
        0x16,
        "#5P呵呵，好的…………\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0160
    NpcTalk(
        0x15,
        "艾莉",
        "#00101F#12P（紧张……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0161
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与勤奋且充满包容力的才女……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x16,
        (
            "#5P身为拥有相同目标的同伴，\x01",
            "一起跨越过无数困难，\x01",
            "已经建立了坚固的羁绊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3D10")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0163
    ChrTalk(
        0x16,
        (
            "#5P啊……由于以前曾陷入到\x01",
            "某场生死攸关的危机之中，\x01",
            "使二位的感情大有进展。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x16,
        (
            "#5P虽然现在尚未确定下来，\x01",
            "但只要继续培养相互之间的感情，\x01",
            "总有一天能发展为更深的关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3D9B")

    label("loc_3D10")


    #C0165
    ChrTalk(
        0x16,
        (
            "#5P虽然出身不同，\x01",
            "但却能发现对方的长处，\x01",
            "形成互补互助的关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x16,
        (
            "#5P只要继续培养彼此之间的感情，\x01",
            "总有一天能发展为\x01",
            "更深的关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3D9B")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0167
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0168
    NpcTalk(
        0x15,
        "艾莉",
        "#00112F#12P更、更深的关系指的是……！？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x16,
        (
            "#5P呵呵，这个嘛……\x01",
            "如果说得太清楚，\x01",
            "未免也太不解风情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x16,
        (
            "#5P总之，关键还在于\x01",
            "你今后的行动与选择……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#00005F#6P我、我吗？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x16,
        (
            "#5P嗯，不要忘记努力\x01",
            "洞察对方的心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x16,
        (
            "#5P因为我还看到了这样的暗示——\x01",
            "你拥有一种会在无意识中\x01",
            "魅惑身边众人的魔性。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0174
    ChrTalk(
        0x101,
        "#00012F#6P魔、魔性……？\x02",
    )

    CloseMessageWindow()

    #N0175
    NpcTalk(
        0x15,
        "艾莉",
        "#00106F#12P（说得相当正确……）\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x16,
        (
            "#5P不过，占卜终究只是占卜，\x01",
            "并非预言……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x16,
        (
            "#5P『命运』这种东西，\x01",
            "会遵循因果定律而不断变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x16,
        (
            "#5P依照你们今后的行动，\x01",
            "它也会有很大的变换……\x01",
            "请记住这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#00000F#6P好、好的，\x01",
            "我会铭记于心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4640")

    label("loc_4051")

    SetChrSubChip(0x101, 0x2)

    #C0180
    ChrTalk(
        0x101,
        (
            "#00000F#6P艾莉，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0181
    NpcTalk(
        0x15,
        "艾莉",
        (
            "#00105F#12P啊，可以由我来决定吗？\x02\x03",

            "#00103F唔……我想想……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0182
    NpcTalk(
        0x15,
        "艾莉",
        (
            "#00100F#12P那么……\x01",
            "就测测克洛斯贝尔自治州\x01",
            "未来的发展如何？\x02\x03",

            "#00103F独立提案会带来\x01",
            "怎样的影响……\x01",
            "实在是很令人在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#00003F#6P嗯，的确如此。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0184
    ChrTalk(
        0x101,
        (
            "#00000F#6P……那么，\x01",
            "可以请您占卜一下吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0185
    ChrTalk(
        0x16,
        "#5P呵呵，当然没问题。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0187
    NpcTalk(
        0x15,
        "艾莉",
        "#00101F#12P（紧张……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0188
    ChrTalk(
        0x16,
        (
            "#5P……近期内，你们会被卷入\x01",
            "一场极其巨大的事件之中……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x16,
        (
            "#5P你们将要面对前所未有的\x01",
            "巨大『壁障』……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x16,
        "#5P并体会到与之相应的强烈绝望。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0x101,
        "#00005F#6P咦……！？\x02",
    )

    CloseMessageWindow()

    #N0192
    NpcTalk(
        0x15,
        "艾莉",
        "#00105F#12P那、那究竟是……？\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x16,
        "#5P……我也不清楚。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x16,
        (
            "#5P然而，那阵脚步声\x01",
            "确实在不断接近你们……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0195
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x15)

    #N0196
    NpcTalk(
        0x15,
        "艾莉",
        "#00103F#12P……这、这究竟是……？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#00003F#6P巨大的『壁障』……\x01",
            "以及与之相应的强烈绝望……\x02\x03",

            "#00008F难道说市长发起的独立提案\x01",
            "引起了某些……？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x16,
        "#5P……我也无法得知其中详情。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x16,
        (
            "#5P因为我的占卜只是以我自己的\x01",
            "方式来解读其中的暗示罢了。\x02",
        )
    )

    CloseMessageWindow()

    #N0200
    NpcTalk(
        0x15,
        "艾莉",
        (
            "#00106F#12P唔……虽然很在意……\x01",
            "但现在也只能小心留意了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x16,
        (
            "#5P看来我让你们产生了\x01",
            "无谓的担忧啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x16,
        (
            "#5P不过，占卜终究只是占卜，\x01",
            "并非预言……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x16,
        (
            "#5P『命运』这种东西，\x01",
            "会遵循因果定律而不断变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x16,
        (
            "#5P依照你们今后的行动，\x01",
            "它也会有很大的变换……\x01",
            "请记住这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#00000F#6P好的，我会铭记于心。\x02",
    )

    CloseMessageWindow()

    label("loc_4640")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_25_3864 end

    def Function_26_464C(): pass

    label("Function_26_464C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",      # 0
            "让缇欧决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE1")

    #C0207
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0209
    ChrTalk(
        0x101,
        (
            "#00000F#6P……你觉得如何？缇欧。\x01",
            "难得来一次，就试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0210
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00203F#12P……嗯，好像很有趣。\x02\x03",

            "#00200F根据占卜出来的结果，\x01",
            "我也可以斟酌一下\x01",
            "今后的立身之法。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        "#00006F#6P……不太明白你的意思呢。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0212
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00203F#12P哦，听不懂也没关系。\x02\x03",

            "#00200F那么，请您为我们占卜吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0213
    ChrTalk(
        0x16,
        "#5P嗯，好的…………\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0215
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00205F#12P（……感知到了不可思议的气场……\x01",
            "  这究竟是……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0216
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与蕴藏着卓越能力的少女……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x16,
        (
            "#5P虽然存在着一定的年龄差，\x01",
            "但却可以对等地将对方视作同伴，\x01",
            "并相互信赖……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_4A5D")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0218
    ChrTalk(
        0x16,
        (
            "#5P啊……由于以前曾陷入到\x01",
            "某场生死攸关的危机之中，\x01",
            "使二位的感情大有进展。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x16,
        (
            "#5P虽然还存在各种阻碍，\x01",
            "但从暗示中可以看出，\x01",
            "你们很可能会发展成更深的关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4AE6")

    label("loc_4A5D")


    #C0220
    ChrTalk(
        0x16,
        (
            "#5P虽然出身不同，\x01",
            "但却能发现对方的长处，\x01",
            "形成互补互助的关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x16,
        (
            "#5P虽然还存在各种阻碍，\x01",
            "但今后完全有可能\x01",
            "发展成更深的关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4AE6")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0222
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    #N0223
    NpcTalk(
        0x15,
        "缇欧",
        "#00204F#12P嗯……很有趣的结果。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00012F#6P那个……我不大明白……\x02\x03",

            "#00000F所谓的『各种阻碍』\x01",
            "是指……？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x16,
        (
            "#5P呵呵，具体来说，\x01",
            "大概就是社会的禁忌\x01",
            "与他人的看法之类……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x16,
        (
            "#5P如果你有跨越这些障碍的决心，\x01",
            "说不定可以……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#00005F#6P哎……？\x01",
            "什么决心……？\x02\x03",

            "#00003F只不过是和缇欧加深感情而已，\x01",
            "我完全不在意\x01",
            "别人的看法啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0228
    NpcTalk(
        0x15,
        "缇欧",
        "#00211F#12P……真是爆炸性的发言啊。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#00005F#6P嗯……？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x16,
        "#5P呵呵，真是位有趣的客人。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x16,
        (
            "#5P但我不得不向女神祈愿，\x01",
            "希望这种性格以后\x01",
            "别给你带来诸多灾难。\x02",
        )
    )

    CloseMessageWindow()

    #N0232
    NpcTalk(
        0x15,
        "缇欧",
        "#00206F#12P嗯，您说的完全没错。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0233
    ChrTalk(
        0x101,
        (
            "#00006F#6P那、那个……\x01",
            "你们别把我丢在一边，\x01",
            "说些让人听不懂的话啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536B")

    label("loc_4DE1")

    SetChrSubChip(0x101, 0x2)

    #C0234
    ChrTalk(
        0x101,
        (
            "#00000F#6P缇欧，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0235
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00205F#12P可以由我来决定吗？\x02\x03",

            "#00203F……那就……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0236
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00200F#12P请您测测\x01",
            "我和咪西的缘分吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0237
    ChrTalk(
        0x101,
        "#00005F#6P和、和咪西的缘分……？\x02",
    )

    CloseMessageWindow()

    #N0238
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00202F#12P嗯，我想知道今后\x01",
            "能否一直得到咪西的陪伴……\x01",
            "请为我测测看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0239
    ChrTalk(
        0x16,
        (
            "#5P唔，真是特别的要求啊。\x01",
            "……好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0241
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00205F#12P（……感知到了不可思议的气场……\x01",
            "  这究竟是……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0242
    ChrTalk(
        0x16,
        (
            "#5P……你和咪西的缘分……\x01",
            "似乎相当不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x16,
        (
            "#5P只要你继续爱它，\x01",
            "咪西就一定会回应你的感情。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x16,
        (
            "#5P今后还会有无数的咪西周边在等着你，\x01",
            "你们在主题公园中也有很多接触的机会……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0245
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()

    #N0246
    NpcTalk(
        0x15,
        "缇欧",
        "#00202F#12P呵呵，非常感谢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x101,
        (
            "#00012F#6P嗯，真是太好了，\x01",
            "咪西会回应你的感情啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0248
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00204F#12P是啊，作为一个咪西迷，\x01",
            "没有比这更让人高兴的结果了。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x16,
        "#5P哦，还有一件事。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x16,
        (
            "#5P近期将有一个重要试炼，\x01",
            "它会考验你对咪西的\x01",
            "感情是否深厚……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x16,
        (
            "#5P在占卜中出现了这样的暗示，\x01",
            "请你一定要注意哦。\x02",
        )
    )

    CloseMessageWindow()

    #N0252
    NpcTalk(
        0x15,
        "缇欧",
        (
            "#00200F#12P……来得好。\x02\x03",

            "#00201F无论是什么样的试炼，\x01",
            "都不可能动摇\x01",
            "我对咪西的爱……\x02\x03",

            "#00204F我会用行动证明这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x16,
        "#5P呵呵，我会支持你的。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0254
    ChrTalk(
        0x101,
        (
            "#00006F#6P（不、不行了。\x01",
            "  这种对话实在太奇怪了，\x01",
            "  我完全无法理解……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_26_464C end

    def Function_27_5377(): pass

    label("Function_27_5377")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",      # 0
            "让兰迪决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B08")

    #C0256
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x1)

    #N0258
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00306F#12P我说你啊……应该找自己喜欢的\x01",
            "女孩来占卜这种事吧？\x02\x03",

            "#00301F两个大男人之间的缘分\x01",
            "有什么好测的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0259
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈，好啦，随便测测看吧。\x02\x03",

            "#00000F再说了，即使是同性朋友，\x01",
            "也存在缘分这种东西吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0260
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00306F#12P唔……我倒是无所谓。\x02\x03",

            "#00300F那就麻烦你啦，大姐姐。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0261
    ChrTalk(
        0x16,
        "#5P呵呵，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0263
    NpcTalk(
        0x15,
        "兰迪",
        "#00305F#12P（哦哦……看起来很专业啊。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0264
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与把热情隐匿于心中的青年……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x16,
        (
            "#5P极富向心力的他总是站在最前方，\x01",
            "并以其乐观的个性激励和引导队友，\x01",
            "是位十分可靠的同伴……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_5799")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0266
    ChrTalk(
        0x16,
        (
            "#5P啊……由于以前曾陷入到\x01",
            "某场生死攸关的危机之中，\x01",
            "使二位的交情大幅度加深。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x16,
        (
            "#5P接下来，只要继续加深\x01",
            "对彼此的理解，\x01",
            "就能缔结更为坚固的羁绊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5826")

    label("loc_5799")


    #C0268
    ChrTalk(
        0x16,
        (
            "#5P虽然出身不同，\x01",
            "但却能发现对方的长处，\x01",
            "形成互补互助的关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x16,
        (
            "#5P接下来，只要继续加深\x01",
            "对彼此的理解，\x01",
            "就能缔结更为坚固的羁绊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5826")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0270
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0271
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00305F#12P哦哦……这结果\x01",
            "真是相当不错啊。\x02\x03",

            "#00304F大小姐、阿缇，\x01",
            "还有诺艾尔……对不起啦。\x02\x03",

            "#00302F看来罗伊德将会\x01",
            "成为我的所有物了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0272
    ChrTalk(
        0x101,
        (
            "#00006F#6P……别说那种\x01",
            "莫名其妙的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x16,
        (
            "#5P嗯……目前还没有看到\x01",
            "你们会发展成那种关系的暗示。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0274
    ChrTalk(
        0x16,
        (
            "#5P不过，所谓的命运，\x01",
            "会因你们的强烈愿望\x01",
            "而改变……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x16,
        (
            "#5P如果你们问我，今后是不是\x01",
            "绝对不可能发展成那种关系……\x01",
            "老实说，我也无法彻底否定呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x101,
        (
            "#00012F#6P那、那个……如果可以，\x01",
            "真希望你能彻底否定啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0277
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00309F#12P哈哈，别害羞，别害羞。\x02\x03",

            "#00304F如果你真的有此希望，\x01",
            "我身为可靠的大哥，就只能……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0278
    ChrTalk(
        0x101,
        (
            "#00011F#6P我才没有害羞！！\x02\x03",

            "#00006F唉，拜托你饶了我吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60FC")

    label("loc_5B08")

    SetChrSubChip(0x101, 0x2)

    #C0279
    ChrTalk(
        0x101,
        (
            "#00000F#6P兰迪，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0280
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00305F#12P嗯？可以由我来决定吗？\x02\x03",

            "#00303F让我想想……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0281
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00309F#12P嗯，那就……\x01",
            "测测今后我的\x01",
            "搭讪运吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x101,
        "#00006F#6P就、就测这个吗……？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x16,
        (
            "#5P换句话说，就是占卜你今后向\x01",
            "素未谋面的女性搭讪时，\x01",
            "对方是否会有所回应吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0284
    NpcTalk(
        0x15,
        "兰迪",
        "#00309F#12P没错！麻烦您了！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0285
    ChrTalk(
        0x16,
        "#5P呵呵，不客气。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0287
    NpcTalk(
        0x15,
        "兰迪",
        "#00305F#12P（哦哦……看起来很专业啊。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0288
    ChrTalk(
        0x16,
        (
            "#5P……你的搭讪……\x01",
            "成功率大概是\x01",
            "百分之五十。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x16,
        (
            "#5P你那天生爽朗的性格与端正的容貌\x01",
            "可以吸引很多女性……\x01",
            "但也有不少人会因此而提高警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x16,
        (
            "#5P顺便一说，即使搭讪成功，\x01",
            "你能获得真爱的可能性\x01",
            "也近乎为零。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0291
    NpcTalk(
        0x15,
        "兰迪",
        "#00306F#12P#4S（大受打击）……！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0292
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0293
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00306F#12P罗、罗伊德……\x01",
            "我已经不行了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0294
    ChrTalk(
        0x101,
        (
            "#00012F#6P好、好啦好啦……\x01",
            "不要这么沮丧啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x16,
        (
            "#5P呵呵，是啊，\x01",
            "我可以给你一个建议……\x01",
            "不要错失近在眼前的爱情。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x16,
        (
            "#5P在你的身边，就有一位十分\x01",
            "珍惜你的异性……\x01",
            "占卜中出现了这样的暗示。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #N0297
    NpcTalk(
        0x15,
        "兰迪",
        "#00305F#12P真、真的吗！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    #C0298
    ChrTalk(
        0x101,
        (
            "#00000F#6P这难道是指……\x01",
            "警备队的米蕾──\x02",
        )
    )

    CloseMessageWindow()

    #N0299
    NpcTalk(
        0x15,
        "兰迪",
        (
            "#00303F#12P──好！既然如此……\x02\x03",

            "#00309F在找到那个十分珍惜\x01",
            "我的可爱女孩之前，\x01",
            "也只能努力去搭讪了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    #C0300
    ChrTalk(
        0x101,
        "#00006F#6P为、为什么会得出这种结论……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x16,
        (
            "#5P（……是在故意装傻吗？\x01",
            "  呵呵，反正与我无关。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60FC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_27_5377 end

    def Function_28_6108(): pass

    label("Function_28_6108")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",        # 0
            "让诺艾尔决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6833")

    #C0303
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x1)

    #N0305
    NpcTalk(
        0x15,
        "诺艾尔",
        "#10105F#12P罗、罗伊德警官！？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0306
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈，机会难得，\x01",
            "所以我想测测看。\x02\x03",

            "#00000F如果你觉得为难，那就算了……\x02",
        )
    )

    CloseMessageWindow()

    #N0307
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10111F#12P没、没有的事！！\x01",
            "我并没有觉得\x01",
            "为难，只是……\x02\x03",

            "#10116F（这就是所谓的\x01",
            "  天生迟钝吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        "#00005F#6P嗯？怎么了？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0309
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10106F#12P没、没什么。\x02\x03",

            "#10100F……那、那就麻烦您\x01",
            "占卜一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0310
    ChrTalk(
        0x16,
        "#5P呵呵，我明白了。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0312
    NpcTalk(
        0x15,
        "诺艾尔",
        "#10105F#12P（哇……这是某种法术吗……？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0313
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与拥有耿直意志的女孩……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x16,
        (
            "#5P虽然岗位不同，但为了守护某些事物\x01",
            "这一相同目标而相互协助，\x01",
            "并在此过程中建立了坚固的信赖关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x16,
        (
            "#5P只要其中一方率先踏出一步，\x01",
            "触及更深的部分，\x01",
            "彼此的关系就能变得更加亲密。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0316
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()

    #N0317
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10105F#12P踏出一步吗……？\x01",
            "这是我很不擅长的事情呢。\x02\x03",

            "#10106F我总是不自觉地和人保持着距离……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x16,
        (
            "#5P呵呵，在我看来，\x01",
            "你的性格似乎比较谨慎，\x01",
            "会这样也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x16,
        (
            "#5P但是，如果你不稍微主动一些\x01",
            "去追求的话，有些本该属于你的\x01",
            "东西也会溜走哦。\x02",
        )
    )

    CloseMessageWindow()

    #N0320
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10103F#12P我、我也明白，\x01",
            "在有些时候必须要主动……\x02\x03",

            "#10101F……嗯，好吧。\x01",
            "在关键时刻，我一定会\x01",
            "鼓起勇气试试看的……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0321
    ChrTalk(
        0x101,
        (
            "#00012F#6P那、那个，诺艾尔……\x01",
            "你未免也太认真了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0322
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10105F#12P啊……！\x02\x03",

            "#10106F……说、说的也是，\x01",
            "毕竟只是随便测测看而已……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0323
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10105F#12P……啊！不对！\x01",
            "我并没有觉得遗憾，\x01",
            "根本不是这个意思……！\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#00006F#6P我、我知道啦，\x01",
            "你稍微冷静一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x16,
        "#5P（呵呵，这两个人说不定还挺般配呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D95")

    label("loc_6833")

    SetChrSubChip(0x101, 0x2)

    #C0326
    ChrTalk(
        0x101,
        (
            "#00000F#6P诺艾尔，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0327
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10105F#12P可以由我来决定吗？\x02\x03",

            "#10103F唔……该测什么呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0328
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10100F#12P那就……\x01",
            "占卜一下警备队的\x01",
            "将来吧。\x02\x03",

            "#10104F毕竟我总有一天要回归警备队，\x01",
            "在那一天到来之前，\x01",
            "我想做好心理准备。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0329
    ChrTalk(
        0x101,
        (
            "#00002F#6P好啊，这主意不错。\x02\x03",

            "#00000F那就麻烦您\x01",
            "占卜一下这件事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x16,
        "#5P嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0332
    NpcTalk(
        0x15,
        "诺艾尔",
        "#10105F#12P（哇……这是某种法术吗……？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0333
    ChrTalk(
        0x16,
        "#5P……这是……变革的暗示呢。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x16,
        (
            "#5P在不久的将来，\x01",
            "你所在的组织将会\x01",
            "发生某种变化……\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x16,
        (
            "#5P到时候，会有一道十分严酷的\x01",
            "选择题摆在你眼前……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0336
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()

    #N0337
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10103F#12P变革……还有选择题吗？\x02\x03",

            "#10101F请问，那究竟是指什么呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x16,
        (
            "#5P很遗憾，目前还无法\x01",
            "清晰地看清那一部分。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x16,
        (
            "#5P现在能确定的就是，无论结果好坏，\x01",
            "都取决于今后的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#00003F#6P嗯……以目前的情况来说，\x01",
            "的确难以预测接下来的发展。\x02\x03",

            "#00000F根据独立提案的成败，\x01",
            "警备队的情况也一定会\x01",
            "发生相应的变化。\x02",
        )
    )

    CloseMessageWindow()

    #N0341
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10100F#12P对警备队而言，那究竟会是\x01",
            "进步还是衰退呢……\x02\x03",

            "#10103F真希望是\x01",
            "进步啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x16,
        "#5P我能说的只有一点……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x16,
        (
            "#5P那就是一定不要做出\x01",
            "会让自己后悔的决定。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x16,
        (
            "#5P占卜终究只是占卜……\x01",
            "你的一个选择，就有可能\x01",
            "使未来发生巨大的变化。\x02",
        )
    )

    CloseMessageWindow()

    #N0345
    NpcTalk(
        0x15,
        "诺艾尔",
        (
            "#10100F#12P嗯，说的也是……\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D95")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_28_6108 end

    def Function_29_6DA1(): pass

    label("Function_29_6DA1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",      # 0
            "让瓦吉决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7375")

    #C0347
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0349
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10302F#12P呵呵，这可真稀奇呢，\x01",
            "你居然会主动\x01",
            "向我示好。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0350
    ChrTalk(
        0x101,
        (
            "#00003F#6P不、不是的，\x01",
            "我不是那个意思。\x02\x03",

            "#00000F我只是觉得，难得来一次，\x01",
            "不妨随便测测看。\x02",
        )
    )

    CloseMessageWindow()

    #N0351
    NpcTalk(
        0x15,
        "瓦吉",
        "#10309F#12P呵呵，不用那么害羞啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0352
    ChrTalk(
        0x101,
        "#00006F#6P……总、总之，接下来就麻烦您了。\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x16,
        "#5P呵呵，好的。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0354
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    #C0355
    ChrTalk(
        0x16,
        "#5P（……原来如此……）\x02",
    )

    CloseMessageWindow()

    #N0356
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10309F#12P呵呵，有什么问题吗？\x01",
            "占卜师姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x16,
        "#5P……呵呵，没什么。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#00005F#6P……？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与潇洒度日的少年……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x16,
        (
            "#5P二人的性格完全相反，\x01",
            "但却能认同对方的优秀之处，\x01",
            "并以此构筑牢固的信赖关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x16,
        (
            "#5P只要进一步加深彼此之间的信赖，\x01",
            "并包容对方的过去与现在，\x01",
            "就可以缔结更为巩固的羁绊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0362
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#00005F#6P包容对方的过去与现在……\x02\x03",

            "#00003F……说起来，\x01",
            "你确实没怎么提起过\x01",
            "自己的过去呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0364
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10309F#12P呵呵，真讨厌。\x01",
            "我早就对你\x01",
            "袒露一切了啊。\x02\x03",

            "#10304F再说了，藏有些秘密，\x01",
            "反而能让对方的兴趣更加强烈吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0365
    ChrTalk(
        0x101,
        (
            "#00006F#6P说来说去，你果然还是\x01",
            "隐瞒着某些秘密啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x16,
        "#5P呵呵，总之一定要保持耐性。\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x16,
        (
            "#5P这种类型的人可不会\x01",
            "轻易说出真心话。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0368
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10304F#12P呵呵，没错。\x02\x03",

            "#10309F如果你能始终保持耐性，\x01",
            "坚持不懈地接近我，我会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0369
    ChrTalk(
        0x101,
        "#00006F#6P真是的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_77BD")

    label("loc_7375")

    SetChrSubChip(0x101, 0x2)

    #C0370
    ChrTalk(
        0x101,
        (
            "#00000F#6P瓦吉，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0371
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10305F#12P哎呀，可以由我来决定吗？\x02\x03",

            "#10304F让我想想……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0372
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10300F#12P那么……\x01",
            "就占卜一下这样的内容吧。\x02\x03",

            "#10304F我能否在这片大地上\x01",
            "得到我想要的东西……\x01",
            "就是这些。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        "#00005F#6P你想要的东西……？\x02",
    )

    CloseMessageWindow()

    #N0374
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10304F#12P呵呵，那可是个秘密。\x02\x03",

            "#10300F如何？大姐姐，\x01",
            "你可以占卜这种内容吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x16,
        (
            "#5P呵呵，真有趣，\x01",
            "那我就试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0376
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    #C0377
    ChrTalk(
        0x16,
        "#5P（……原来如此……）\x02",
    )

    CloseMessageWindow()

    #N0378
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10309F#12P呵呵，有什么问题吗？\x01",
            "占卜师大姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x16,
        "#5P……呵呵，没什么。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        "#00005F#6P……？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x16,
        "#5P你所追寻之物就在你的身边……\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x16,
        (
            "#5P但现在却绝对\x01",
            "得不到。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x16,
        (
            "#5P暂时只能等待时机……\x01",
            "我得出了这样的暗示。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0384
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()

    #N0385
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10304F#12P……原来如此，\x01",
            "这已经足够了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    #C0386
    ChrTalk(
        0x101,
        (
            "#00006F#6P我根本听不懂\x01",
            "这是怎么回事……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0387
    NpcTalk(
        0x15,
        "瓦吉",
        (
            "#10300F#12P呵呵，现在听不懂不是也挺好吗？\x02\x03",

            "#10304F再说了，藏有些秘密，\x01",
            "反而能让你对我的兴趣更加强烈吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        "#00006F#6P唉，真是的……\x02",
    )

    CloseMessageWindow()

    label("loc_77BD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_6DA1 end

    def Function_30_77C9(): pass

    label("Function_30_77C9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0389
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",      # 0
            "让琪雅决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6A")

    #C0390
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0392
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01110F#12P罗伊德，『缘分』就是指\x01",
            "我们是否性情相投吧？\x02\x03",

            "#01109F真希望能和\x01",
            "罗伊德有缘分～\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0393
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈，是啊。\x01",
            "如果能得到好结果，我也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0394
    ChrTalk(
        0x101,
        (
            "#00000F#6P……那就麻烦您\x01",
            "为我们占卜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x16,
        "#5P呵呵，我知道了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0396
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0397
    NpcTalk(
        0x15,
        "琪雅",
        "#01110F#12P（哇，好漂亮……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0398
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与用笑容带来光明的少女……\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x16,
        (
            "#5P她的存在能赐予你们勇气，\x01",
            "你们也因保护她这一强烈意志\x01",
            "而建立起深厚的羁绊……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x16,
        (
            "#5P只要你们还在保护她，\x01",
            "这份羁绊就绝不会断开。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0401
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    #N0402
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01106F#12P……稍微有点\x01",
            "失望呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0403
    ChrTalk(
        0x101,
        (
            "#00005F#6P哎，为什么？\x01",
            "这个结果不是挺好的吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0404
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01108F#12P嗯……结果是不错，\x01",
            "但和我想要的不一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0405
    ChrTalk(
        0x16,
        (
            "#5P……呵呵，小姑娘。\x01",
            "占卜结果并非一切，\x01",
            "所以你没必要为此而叹息。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0406
    ChrTalk(
        0x16,
        (
            "#5P虽然现在还是\x01",
            "亲子般的关系……\x01",
            "但雏鸟总有一天会长大。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x16,
        (
            "#5P到时候……父母就会发现，\x01",
            "自己的孩子已经成长到\x01",
            "可以展翅翱翔了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0408
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01105F#12P……是吗？\x01",
            "嗯，说的也是。\x02\x03",

            "#01109F好吧，琪雅……\x01",
            "一定要赶快长大！\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        (
            "#00004F#6P唔，虽然还不太明白……\x01",
            "但你能恢复精神就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83CF")

    label("loc_7D6A")

    SetChrSubChip(0x101, 0x2)

    #C0410
    ChrTalk(
        0x101,
        (
            "#00000F#6P琪雅，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0411
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01105F#12P可以由我来决定吗～？\x02\x03",

            "#01111F唔～让我想想……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0412
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01110F#12P啊，对了！\x01",
            "我想测测自己和\x01",
            "蔡特的缘分～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0413
    ChrTalk(
        0x16,
        "#5P蔡特……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0414
    ChrTalk(
        0x101,
        (
            "#00012F#6P那、那个……\x01",
            "蔡特是在职场中和我们\x01",
            "一起生活的动物……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0415
    ChrTalk(
        0x16,
        "#5P呵呵，原来如此……\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x16,
        (
            "#5P没问题，小姑娘，\x01",
            "那就把蔡特\x01",
            "带到这里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x16,
        (
            "#5P等它来了以后，\x01",
            "我马上就可以给你们占卜。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        "#00011F#6P哎！？\x02",
    )

    CloseMessageWindow()

    #N0419
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01110F#12P真的吗～！？\x02\x03",

            "#01109F我这就把它带来～！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 1500, 0, 101500, 270)
    OP_0D()
    OP_93(0x15, 0xB4, 0x1F4)
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_7FE9():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7FE9)
    WaitChrThread(0x15, 1)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0420
    ChrTalk(
        0x101,
        (
            "#00012F#6P真、真抱歉，\x01",
            "让您占卜这么奇怪的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x16,
        (
            "#5P呵呵，没关系，\x01",
            "反正很有趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x101,
        "#00006F#6P（这位占卜师也是个怪人啊……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 630, 50, 101950, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x27)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 0, 0, 0)
    SetChrPos(0x17, 2000, 0, 101000, 315)
    FadeToBright(1000, 0)
    OP_0D()

    #C0423
    ChrTalk(
        0x17,
        "#01200F#12P咕噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x16,
        "#5P呵呵，那我就开始了…………\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0426
    NpcTalk(
        0x15,
        "琪雅",
        "#01110F#12P（哇，好漂亮……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0427
    ChrTalk(
        0x16,
        (
            "#5P用笑容带来光明的少女与\x01",
            "默默守护着同伴们的高傲白狼……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x16,
        (
            "#5P你们可以理解对方的想法，并互相尊重，\x01",
            "从而缔结了深厚的羁绊……\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x16,
        (
            "#5P无论今后发生什么事，\x01",
            "白狼都会继续守护你的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0430
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    #N0431
    NpcTalk(
        0x15,
        "琪雅",
        (
            "#01100F#12P蔡特，看来我们\x01",
            "今后也能继续待在一起呢～！\x02\x03",

            "#01109F嘿嘿，你也很高兴吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x17,
        "#01203F#12P咕噜噜……嗷。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0433
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈……真是谢谢您了，\x01",
            "竟然满足了如此奇怪的请求……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x16,
        (
            "#5P呵呵，能占卜如此罕见的内容，\x01",
            "也让我得到了不错的经验。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83CF")

    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0435
    ChrTalk(
        0x16,
        (
            "#5P（而且……\x01",
            "  还看到了相当有趣的暗示。）\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x16,
        (
            "#5P（今后的发展，\x01",
            "  恐怕只有女神才能知道了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0437
    ChrTalk(
        0x101,
        "#00005F#6P占卜师小姐……？\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x16,
        (
            "#5P呵呵……没什么，\x01",
            "期待你们再度光临……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_30_77C9 end

    def Function_31_84C0(): pass

    label("Function_31_84C0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0439
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",      # 0
            "让芙兰决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A9C")

    #C0440
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0442
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06405F#12P哦哦，罗伊德警官！\x01",
            "你很在意我们两个的\x01",
            "缘分吗～！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0443
    ChrTalk(
        0x101,
        (
            "#00002F#6P哈哈，毕竟机会难得，\x01",
            "所以我想\x01",
            "测测看……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0444
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06409F#12P呵呵，说的也是！\x01",
            "占卜师小姐，那就麻烦您\x01",
            "给我们测一测吧～！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0445
    ChrTalk(
        0x16,
        "#5P呵呵，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0447
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06405F#12P（哇～\x01",
            "  好、好像很厉害啊～）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0448
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与在后方默默支持大家的少女……\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x16,
        (
            "#5P曾经多次联手完成工作，\x01",
            "由此建立了坚固的信赖关系，\x01",
            "并结下羁绊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0450
    ChrTalk(
        0x16,
        (
            "#5P哎呀，可是……\x01",
            "女孩已经有喜欢的人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x16,
        (
            "#5P在她的心意改变之前，\x01",
            "你们是不可能发展成\x01",
            "那种关系的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0452
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()

    #N0453
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06409F#12P哦哦～真是太准了！\x01",
            "名不虚传，果然厉害啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x16,
        "#5P呵呵，谢谢夸奖。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0455
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈，其实我已经\x01",
            "隐隐猜到会是这种结果了。\x02\x03",

            "#00000F对了，芙兰，\x01",
            "我只是好奇一问，\x01",
            "你喜欢的人是……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0456
    NpcTalk(
        0x15,
        "芙兰",
        "#06409F#12P#4S当然是姐姐啊！！\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        (
            "#00004F#6P唔……果然不出所料。\x02\x03",

            "#00000F看来那种事情\x01",
            "对芙兰来说\x01",
            "还早得很呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x16,
        "#5P呵呵，但反过来想想……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x16,
        (
            "#5P只要能成为比她姐姐更加重要的人，\x01",
            "不就很有希望了吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0460
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06409F#12P没错～\x01",
            "请你继续努力吧，罗伊德警官！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0461
    ChrTalk(
        0x101,
        (
            "#00012F#6P这……让我继续\x01",
            "努力什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_901F")

    label("loc_8A9C")

    SetChrSubChip(0x101, 0x2)

    #C0462
    ChrTalk(
        0x101,
        (
            "#00000F#6P芙兰，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0463
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06405F#12P啊，可以让我来\x01",
            "决定吗～？\x02\x03",

            "#06404F嗯～让我想想哦……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0464
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06405F#12P啊，对了……！\x02\x03",

            "#06401F占卜师小姐，您能帮我\x01",
            "找到邦邦吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x16,
        "#5P邦邦……？\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        (
            "#00000F#6P那不是芙兰很珍惜的\x01",
            "玩偶吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0467
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06400F#12P是啊，其实我这次\x01",
            "本想带它一起来米修拉姆……\x02\x03",

            "#06406F但在动身的前一天，妈妈给我打扫了房间，\x01",
            "它就不知跑到什么地方去了，\x01",
            "结果没能和它一起来呢～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    #C0468
    ChrTalk(
        0x101,
        (
            "#00006F#6P原、原来如此……\x02\x03",

            "#00000F请问，您可以占卜这个吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0469
    ChrTalk(
        0x16,
        "#5P呵呵，当然没问题。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0471
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06405F#12P（哇～\x01",
            "  好、好像很厉害啊～）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0472
    ChrTalk(
        0x16,
        (
            "#5P丢失的玩偶……\x01",
            "是只小熊吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0473
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06405F#12P是、是的！！\x01",
            "您居然能看出来～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x16,
        "#5P呵呵，特征很明显，一眼就看出来了。\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x16,
        (
            "#5P你的玩偶……\x01",
            "正躺在床底下的阴影处……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #N0476
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06403F#12P床、床底下吗？\x01",
            "真奇怪啊，我明明找过\x01",
            "那个地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x16,
        (
            "#5P那里是首先就会想到的地方，\x01",
            "所以反而容易看漏。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x16,
        "#5P再去认真找找吧，一定能找到它的。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0479
    NpcTalk(
        0x15,
        "芙兰",
        "#06409F#12P好的，真是太感谢您了！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0480
    ChrTalk(
        0x101,
        "#00000F#6P哈哈，太好了，芙兰。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0481
    NpcTalk(
        0x15,
        "芙兰",
        (
            "#06406F#12P是啊，真的太好了～！\x01",
            "没有了邦邦，\x01",
            "我真的很寂寞。\x02\x03",

            "#06409F明天回去之后，马上就要找找看～！\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x16,
        "#5P呵呵，能帮上你的忙就好。\x02",
    )

    CloseMessageWindow()

    label("loc_901F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_31_84C0 end

    def Function_32_902B(): pass

    label("Function_32_902B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0483
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",        # 0
            "让塞茜尔决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9665")

    #C0484
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0486
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05900F#12P哎，罗伊德……\x02\x03",

            "#05909F根本就不需要\x01",
            "特地占卜这种事情吧？\x01",
            "我们的缘分肯定特别好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0487
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈，毕竟机会难得，\x01",
            "所以想测测看。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0488
    ChrTalk(
        0x101,
        (
            "#00000F#6P……就是这样，\x01",
            "请您给我们测测吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x16,
        "#5P好的，我知道了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0490
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0491
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05905F#12P（哎呀……\x01",
            "  看起来真的很厉害呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0492
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与充满慈爱精神的女性……\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x16,
        (
            "#5P自幼便建立了深厚的感情，\x01",
            "有着独一无二的羁绊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0494
    ChrTalk(
        0x16,
        (
            "#5P……不过，女方的心中\x01",
            "还留有切实的思念。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x16,
        (
            "#5P那是对已故心上人的\x01",
            "强烈思念……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0496
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x15)

    #N0497
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05904F#12P……呵呵，真没想到\x01",
            "会这么准呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0498
    ChrTalk(
        0x101,
        (
            "#00006F#6P……对不起，塞茜尔姐姐，\x01",
            "我不该占卜这种事的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0499
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05900F#12P啊，不用道歉啊。\x01",
            "看来咱们的缘分很不错，\x01",
            "我真是非常高兴。\x02\x03",

            "#05904F而且……能够再次确认\x01",
            "我还没有忘记盖伊，\x01",
            "也是一件好事。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x16,
        (
            "#5P……无论发生什么事，\x01",
            "对心爱之人的思念\x01",
            "都会永远留存。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x16,
        (
            "#5P正是由于那份感情，\x01",
            "才会有如今的你们……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #N0502
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05905F#12P……占卜师小姐，\x01",
            "难道你也失去了重要的人……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0503
    ChrTalk(
        0x16,
        "#5P……我似乎说得太多了。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x16,
        (
            "#5P我只是一名占卜师而已，\x01",
            "本不该言及那些事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#00004F#6P哪里，多谢指点了，\x01",
            "我一定会把您这番话铭记于心。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x16,
        "#5P呵呵……不必客气。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C7B")

    label("loc_9665")

    SetChrSubChip(0x101, 0x2)

    #C0507
    ChrTalk(
        0x101,
        (
            "#00000F#6P塞茜尔姐姐，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0508
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05905F#12P咦，可以由我来决定吗？\x02\x03",

            "#05904F呵呵，我想想……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0509
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05909F#12P那就……\x01",
            "测测罗伊德将来能娶到\x01",
            "一位什么样的新娘吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0510
    ChrTalk(
        0x101,
        "#00011F#6P#4S什么！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0511
    ChrTalk(
        0x101,
        (
            "#00011F#6P等、等一下，塞茜尔姐姐……\x01",
            "这也太让人难为情了吧……\x02",
        )
    )

    CloseMessageWindow()

    #N0512
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05909F#12P嗯？这有什么不好的，\x01",
            "姐姐很想知道啊。\x02\x03",

            "#05900F麻烦您占卜一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x16,
        "#5P呵呵，没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0514
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0515
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05900F#12P（哎呀……\x01",
            "  看起来真的很厉害呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0516
    ChrTalk(
        0x16,
        (
            "#5P将与性情正直、勇往直前的青年\x01",
            "结为夫妇的女性是……\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x16,
        (
            "#5P………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #N0518
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05905F#12P啊……\x01",
            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x16,
        (
            "#5P实在抱歉……\x01",
            "目前什么都看不出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        "#00005F#6P咦……\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x16,
        (
            "#5P我以前占卜过很多次\x01",
            "类似的内容……\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x16,
        (
            "#5P偶尔会遇到具备可能性的女性太多，\x01",
            "因此无法测出结果的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x16,
        "#5P你的情况正是如此。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0524
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05909F#12P唔……原来是这样，\x01",
            "这倒真是没想到呢。\x02\x03",

            "#05908F罗伊德是我引以为傲的弟弟，\x01",
            "我早就知道会有不少女孩子\x01",
            "盯上他，但没想到……\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#00006F#6P（总、总觉得\x01",
            "  她们把我说得\x01",
            "  很没节操……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0526
    NpcTalk(
        0x15,
        "塞茜尔",
        (
            "#05903F#12P那个……罗伊德，\x01",
            "得出这样的结果，\x01",
            "姐姐真是有点担心了……\x02\x03",

            "#05901F你可千万不要\x01",
            "做出让女孩子伤心的\x01",
            "事情哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0527
    ChrTalk(
        0x101,
        "#00012F#6P我、我才不会呢！\x02",
    )

    CloseMessageWindow()

    label("loc_9C7B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_902B end

    def Function_33_9C87(): pass

    label("Function_33_9C87")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0528
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",        # 0
            "让伊莉娅决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A18E")

    #C0529
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0531
    ChrTalk(
        0x101,
        (
            "#00009F#6P……话说回来，\x01",
            "我擅自做出这种决定，\x01",
            "您不介意吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0532
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01709F#12P哈哈，这不是挺有趣的嘛，\x01",
            "赶快测测看吧☆\x02\x03",

            "#01704F呵呵，虽然很对不起塞茜尔，\x01",
            "但如果测出好结果，\x01",
            "警察弟弟可就要归我了～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    #C0533
    ChrTalk(
        0x101,
        (
            "#00012F#6P……总、总之，\x01",
            "先看看结果再说吧。\x02\x03",

            "#00000F接下来就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x16,
        "#5P好的，我知道了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0535
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0536
    NpcTalk(
        0x15,
        "伊莉娅",
        "#01705F#12P（哦……？像模像样的啊。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0537
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与对舞台充满热情的舞姬……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x16,
        (
            "#5P她对目标的坚定与专注\x01",
            "令人陶醉憧憬……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x16,
        (
            "#5P只要坚定地支持她的理想，\x01",
            "就很有可能与之\x01",
            "发展到更深的关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x16,
        (
            "#5P不过……\x01",
            "对她来说，最重要的终究还是舞台，\x01",
            "若想成为比那更重要的东西，恐怕很难。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0541
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#00000F#6P哈哈，对伊莉娅小姐来说，\x01",
            "果然还是舞台最重要啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0543
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01700F#12P呵呵，看来正是这样呢。\x02\x03",

            "#01709F话说回来，占卜师小姐，\x01",
            "我真没想到你的占卜\x01",
            "能准确到这种地步。\x02\x03",

            "#01700F这可不是一朝一夕就能\x01",
            "掌握的技术……\x01",
            "你是在哪里修炼这种本领的呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jump("loc_A8B5")

    label("loc_A18E")

    SetChrSubChip(0x101, 0x2)

    #C0544
    ChrTalk(
        0x101,
        (
            "#00000F#6P伊莉娅小姐，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0545
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01705F#12P啊，由我来决定吗？\x02\x03",

            "#01703F嗯，让我想想……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0546
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01709F#12P那就测测莉夏和修利\x01",
            "将来能否超越我吧！\x01",
            "……你觉得如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        "#00005F#6P她们两人吗……\x02",
    )

    CloseMessageWindow()

    #N0548
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01704F#12P老实说，\x01",
            "这种事情也许并不该\x01",
            "过多参考占卜结果……\x02\x03",

            "#01702F但我还是想确认一下，\x01",
            "看看自己到底有没有看错人。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x16,
        (
            "#5P你的两名弟子的将来……\x01",
            "占卜这个内容就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0550
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01700F#12P嗯，是的，\x01",
            "可以占卜吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0551
    ChrTalk(
        0x16,
        "#5P呵呵，当然没问题。\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0553
    NpcTalk(
        0x15,
        "伊莉娅",
        "#01705F#12P（哦……？像模像样的啊。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0554
    ChrTalk(
        0x16,
        (
            "#5P对舞台充满热情的舞姬\x01",
            "亲自发掘的两位年轻舞者……\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x16,
        (
            "#5P她们虽然拥有无限的才能，\x01",
            "但目前都怀着\x01",
            "自己的烦恼。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x16,
        (
            "#5P如何跨越这道壁障……\x01",
            "就是决定她们未来走向的关键。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0557
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    #N0558
    NpcTalk(
        0x15,
        "伊莉娅",
        "#01703F#12P莉夏和修利的烦恼吗……\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        "#00005F#6P伊莉娅小姐，您有什么头绪吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #N0560
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01703F#12P我之前就隐隐察觉到\x01",
            "那两个孩子都怀有\x01",
            "某些烦恼了……\x02\x03",

            "#01700F但我并没有详细过问\x01",
            "其中的内情。\x02\x03",

            "#01704F……话说回来，每个人都会怀有\x01",
            "或多或少的烦恼。\x02\x03",

            "能否跨越壁障，关键还要取决于\x01",
            "她们自己，这不是由我来插手的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x101,
        (
            "#00000F#6P哈哈，真是严厉啊……但从某种意义上说，\x01",
            "这种想法倒也很符合伊莉娅小姐的作风。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0562
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01700F#12P呵呵，不管怎么说，\x01",
            "我相信那两个孩子可以\x01",
            "靠自己的力量跨越壁障。\x02\x03",

            "#01703F她们跨越壁障的时刻，\x01",
            "也就是我迎来人生中最强\x01",
            "竞争对手的瞬间了。\x02\x03",

            "#01709F哇～\x01",
            "忍不住开始期待了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x16,
        (
            "#5P你那乐观积极的态度……\x01",
            "也算是一种才能。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x16,
        "#5P呵呵，让我有些羡慕呢。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0565
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01702F#12P呵呵，谢谢夸奖。\x02\x03",

            "#01709F话说回来，占卜师小姐，\x01",
            "我真没想到你的占卜\x01",
            "能准确到这种地步。\x02\x03",

            "#01700F这可不是一朝一夕就能\x01",
            "掌握的技术……\x01",
            "你是在哪里修炼这种本领的呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    label("loc_A8B5")


    #C0566
    ChrTalk(
        0x16,
        (
            "#5P……我曾在一个巡游戏团中\x01",
            "表演各种技艺。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x16,
        (
            "#5P正是由于当时的磨练与实践，\x01",
            "我才能达到如今这样的实力。\x02",
        )
    )

    CloseMessageWindow()

    #N0568
    NpcTalk(
        0x15,
        "伊莉娅",
        (
            "#01705F#12P戏团……\x01",
            "也就是所谓的杂技团吧？\x02\x03",

            "#01709F唔……真想看看\x01",
            "你在舞台上活跃\x01",
            "表演的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        "#00000F#6P哈哈，我也很想看。\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x16,
        "#5P……呵呵，多谢夸奖。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_9C87 end

    def Function_34_A9DA(): pass

    label("Function_34_A9DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0571
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",      # 0
            "让莉夏决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0EA")

    #C0572
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0574
    NpcTalk(
        0x15,
        "莉夏",
        "#01805F#12P罗、罗伊德警官……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0575
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈，我们难得一起来到\x01",
            "这种地方，不如就测测看吧。\x02\x03",

            "#00000F如果你觉得为难，那就算了……\x02",
        )
    )

    CloseMessageWindow()

    #N0576
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01804F#12P……呵呵，不会。\x02\x03",

            "#01802F说的也是，机会难得，\x01",
            "就请您给我们占卜一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x16,
        "#5P呵呵，好的……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #C0578
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0579
    NpcTalk(
        0x15,
        "莉夏",
        "#01801F#12P（……这是……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0580
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与目光中充满忧郁的女孩……\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x16,
        (
            "#5P由于过去的某件事情，\x01",
            "彼此间萌生了切实的信赖……\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x16,
        (
            "#5P只要用心培育这份感情，\x01",
            "很有可能会发展为\x01",
            "更深的关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x16,
        (
            "#5P不过……若要顺利实现，\x01",
            "就必须要除去女孩\x01",
            "心中的黑暗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0584
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        "#00005F#6P莉夏心中的黑暗……？\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x16,
        "#5P嗯……我也不大清楚。\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x16,
        (
            "#5P我只是把出现在这个水晶球\x01",
            "中的暗示解读出来而已。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0588
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01802F#12P……那个，我想……\x01",
            "指的可能是我对这次\x01",
            "新版公演的担忧吧。\x02\x03",

            "#01809F这毕竟是修利的重要演出，\x01",
            "不知我能不能把舞跳好……\x01",
            "最近总是对此有些不安。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0589
    ChrTalk(
        0x101,
        (
            "#00000F#6P哦，原来是这样啊。\x02\x03",

            "#00003F你一直都在\x01",
            "努力练习，\x01",
            "一定不会有问题的。\x02\x03",

            "#00009F而且在我看过的那场公演中，\x01",
            "你的表现非常出色，让我大为感动……\x01",
            "所以根本就不必担心啦。\x02",
        )
    )

    CloseMessageWindow()

    #N0590
    NpcTalk(
        0x15,
        "莉夏",
        "#01805F#12P…………………………\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x16,
        "#5P……呵呵，这么快就付诸行动了啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #C0592
    ChrTalk(
        0x16,
        (
            "#5P看到客人如此迅速地实践我的建议，\x01",
            "身为占卜师，真是深感欣慰。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0593
    ChrTalk(
        0x101,
        "#00005F#6P什么……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0594
    ChrTalk(
        0x101,
        (
            "#00011F#6P不、不是这样的，莉夏！\x02\x03",

            "我绝对没有什么\x01",
            "非分之想……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0595
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01809F#12P……呵呵，我知道。\x02\x03",

            "#01802F谢谢你，罗伊德警官。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6CD")

    label("loc_B0EA")

    SetChrSubChip(0x101, 0x2)

    #C0596
    ChrTalk(
        0x101,
        (
            "#00000F#6P莉夏，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0597
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01805F#12P那个……可以由我\x01",
            "来决定吗？\x02\x03",

            "#01803F那、那就……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0598
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01803F#12P不久之前寻找小猫的时候，\x01",
            "我结识了一位名叫谢莉的女孩……\x02\x03",

            "#01801F能否占卜一下我和她\x01",
            "有没有再次相见的缘分呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0599
    ChrTalk(
        0x101,
        "#00005F#6P莉夏……？\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0601
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0602
    NpcTalk(
        0x15,
        "莉夏",
        "#01801F#12P（……这是……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0603
    ChrTalk(
        0x16,
        "#5P从水晶球中的暗示来看……\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x16,
        (
            "#5P你与那位名为谢莉的女孩\x01",
            "将会在克洛斯贝尔重逢。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x16,
        (
            "#5P虽然还无法得知具体时间\x01",
            "与相逢时的状况……\x01",
            "但重逢的那一天必定会来临。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0606
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()

    #N0607
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01802F#12P……原来如此，\x01",
            "真是太感谢您了。\x02\x03",

            "#01803F（『血腥谢莉』……\x01",
            "  果然要多加提防啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0608
    ChrTalk(
        0x101,
        (
            "#00000F#6P嘿，真是有点意外。\x02\x03",

            "只是在找小猫玛丽的\x01",
            "时候见过一面而已，\x01",
            "你竟然这么在意她啊？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0609
    NpcTalk(
        0x15,
        "莉夏",
        (
            "#01802F#12P啊，不是的……\x01",
            "只是一时想不出\x01",
            "该占卜什么而已。\x02\x03",

            "#01804F而且那个孩子很可爱，\x01",
            "如果以后有机会，我还想和她聊聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        (
            "#00002F#6P唔……\x01",
            "她其实是个相当危险的孩子哦。\x02\x03",

            "#00006F考虑到艾莉当时的遭遇，\x01",
            "还有另一重意义上的危险……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #N0611
    NpcTalk(
        0x15,
        "莉夏",
        "#01805F#12P……艾莉小姐的遭遇？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0612
    ChrTalk(
        0x101,
        (
            "#00012F#6P啊……啊啊，\x01",
            "没什么。\x02\x03",

            "#00003F（不、不由自主地想象出了\x01",
            "  一副相当不得了的画面……）\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x16,
        "#5P……呵呵，这位小姐。\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x16,
        (
            "#5P如果有需要，我可以为你\x01",
            "占卜一下这位男客人\x01",
            "正在想象的事情。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    #C0615
    ChrTalk(
        0x101,
        "#00012F#6P请、请饶了我吧！\x02",
    )

    CloseMessageWindow()

    label("loc_B6CD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_A9DA end

    def Function_35_B6D9(): pass

    label("Function_35_B6D9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    #A0616
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K占卜什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "两人的缘分\x01",      # 0
            "让修利决定\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD16")

    #C0617
    ChrTalk(
        0x101,
        (
            "#00000F#6P可以占卜一下\x01",
            "我们的缘分吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x16,
        "#5P嗯，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0619
    NpcTalk(
        0x15,
        "修利",
        (
            "#14011F#12P喂、喂……！\x01",
            "你到底在想什么呢！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0620
    ChrTalk(
        0x101,
        (
            "#00005F#6P咦……\x01",
            "有、有必要这么慌张吗？\x02\x03",

            "#00009F我们单独相处的机会很少，\x01",
            "我只是想趁此机会与你增进感情，\x01",
            "所以才想占卜一下啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0621
    NpcTalk(
        0x15,
        "修利",
        (
            "#14006F#12P（……正常人会当着\x01",
            "  对方的面说这种话吗！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x16,
        (
            "#5P呵呵，你们决定好了吗？\x01",
            "我倒是无所谓。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #N0623
    NpcTalk(
        0x15,
        "修利",
        (
            "#14000F#12P……唉～真是的，那就测这个吧。\x01",
            "只要随便占卜一下就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x16,
        "#5P嗯，好的………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0625
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0626
    NpcTalk(
        0x15,
        "修利",
        "#14005F#12P（……怎、怎么回事……？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0627
    ChrTalk(
        0x16,
        (
            "#5P性情正直、勇往直前的青年\x01",
            "与蕴藏着潜能的少女……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BA9E")

    #C0628
    ChrTalk(
        0x16,
        (
            "#5P两人的邂逅非常糟糕，\x01",
            "但少女似乎已经察觉到\x01",
            "青年的温柔之处了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BACC")

    label("loc_BA9E")


    #C0629
    ChrTalk(
        0x16,
        (
            "#5P少女似乎已经察觉到\x01",
            "青年的温柔之处了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BACC")


    #C0630
    ChrTalk(
        0x16,
        (
            "#5P随着时光推移，一旦少女\x01",
            "萌生了坦率的心意……\x01",
            "二位应该就能发展成兄妹般的关系……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0631
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0632
    NpcTalk(
        0x15,
        "修利",
        (
            "#14011F#12P什、什什什什什……什么嘛！\x01",
            "这个占卜结果是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0633
    ChrTalk(
        0x101,
        (
            "#00000F#6P哈哈，确实让人觉得\x01",
            "有点不好意思呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0634
    NpcTalk(
        0x15,
        "修利",
        (
            "#14006F#12P才不是什么\x01",
            "『有点不好意思』！\x02\x03",

            "#14012F为什么我要和你发展成\x01",
            "兄妹般的关系啊……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x16,
        (
            "#5P呵呵……二位现在的关系\x01",
            "就已经很好了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0636
    NpcTalk(
        0x15,
        "修利",
        "#14011F#12P完、完全不好！\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        "#00012F#6P（哈哈，真是不坦率啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_C444")

    label("loc_BD16")

    SetChrSubChip(0x101, 0x2)

    #C0638
    ChrTalk(
        0x101,
        (
            "#00000F#6P修利，\x01",
            "你有什么想测的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    #N0639
    NpcTalk(
        0x15,
        "修利",
        (
            "#14005F#12P哎？可以由我来决定吗？\x02\x03",

            "#14003F唔……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #N0640
    NpcTalk(
        0x15,
        "修利",
        (
            "#14003F#12P我想知道……\x02\x03",

            "#14000F我今后能不能在彩虹剧团\x01",
            "一直待下去……\x01",
            "请帮我占卜一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0641
    ChrTalk(
        0x101,
        "#00005F#6P修利……？\x02",
    )

    CloseMessageWindow()

    #N0642
    NpcTalk(
        0x15,
        "修利",
        (
            "#14008F#12P……如果占卜出了\x01",
            "不错的结果……\x02\x03",

            "#14008F我就不会再回到\x01",
            "那种贫民窟了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0643
    ChrTalk(
        0x101,
        "#00005F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x16,
        "#5P……好，我来为你占卜吧。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0645
    ChrTalk(
        0x16,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0646
    NpcTalk(
        0x15,
        "修利",
        "#14005F#12P（……怎、怎么回事……？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0647
    ChrTalk(
        0x16,
        (
            "#5P……在你的未来之路上，\x01",
            "有着通往不同方向的\x01",
            "多条分支。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x16,
        (
            "#5P是继续追求梦想，不断前进，\x01",
            "还是在遭受挫折之后，\x01",
            "回到原本的地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x16,
        (
            "#5P命运尚未\x01",
            "最终决定。\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x16,
        (
            "#5P所以，我目前还无法断言\x01",
            "你能在彩虹剧团一直待下去。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    #C0651
    ChrTalk(
        0x16,
        "#5P……我能看到的，大概就是这些了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    #N0652
    NpcTalk(
        0x15,
        "修利",
        (
            "#14003F#12P……是吗……\x02\x03",

            "#14008F如果你能给我\x01",
            "绝对肯定的答复，\x01",
            "我就可以稍微安心些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x101,
        "#00008F#6P修利……\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    #C0654
    ChrTalk(
        0x16,
        (
            "#5P……其实我也有个\x01",
            "出身于贫民窟的朋友。\x02",
        )
    )

    CloseMessageWindow()

    #N0655
    NpcTalk(
        0x15,
        "修利",
        "#14005F#12P咦……？\x02",
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x16,
        (
            "#5P刚刚相识的时候，\x01",
            "那孩子无论面对什么，\x01",
            "都只会摆出一副绝望的表情……\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x16,
        (
            "#5P不过，在经历了长时间的共同生活之后，\x01",
            "她最终成长为一名乐观又坚强的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x16,
        (
            "#5P之后，她还遇到了十分出色的指导者，\x01",
            "如今已是一名活跃于各地的一流游击士了。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x16,
        (
            "#5P她之所以能有如此成长……\x01",
            "首要原因无疑就是『与人相遇』。\x02",
        )
    )

    CloseMessageWindow()

    #N0660
    NpcTalk(
        0x15,
        "修利",
        "#14005F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x16,
        (
            "#5P从刚才的暗示中可以看出，\x01",
            "你已经遇到了值得\x01",
            "你尊重的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x16,
        (
            "#5P既然如此……\x01",
            "未来的走向就要取决于你自己了。\x02",
        )
    )

    CloseMessageWindow()

    #N0663
    NpcTalk(
        0x15,
        "修利",
        (
            "#14000F#12P……取决于我自己……\x02\x03",

            "#14003F……说的对。\x01",
            "虽然我不知道自己能否变得\x01",
            "像那位游击士小姐一样强大……\x02\x03",

            "#14002F但我一定会拼命努力的。\x01",
            "……谢谢您。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x16,
        "#5P呵呵……不必客气。\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x101,
        "#00002F#6P（哈哈……邀她一起来，真是太好了。）\x02",
    )

    CloseMessageWindow()

    label("loc_C444")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_35_B6D9 end

    def Function_36_C450(): pass

    label("Function_36_C450")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-7780, -1100, 4820, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x101, -3580, 0, 2100, 270)
    SetChrPos(0xEF, -3200, 0, 3370, 270)
    OP_4B(0x18, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0666
    ChrTalk(
        0x101,
        "#00000F啊，找到了！\x02",
    )

    CloseMessageWindow()
    OP_9C(0x18, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    OP_93(0x18, 0x5A, 0x1F4)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0667
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "哎呀！被找到啦☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5450, -1100, 5050, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x18, -3530, 0, 2710, 90)
    SetChrPos(0x101, -1850, 0, 2040, 270)
    SetChrPos(0xEF, -1850, 0, 3400, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0668
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，\x01",
            "小哥哥，你真是幸运呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "竟然能连续两次发现我\x01",
            "藏身的地方，\x01",
            "运气实在是太好了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x101,
        "#00012F是、是吗……？\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，但这也只是\x01",
            "小试身手而已。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "你总不可能每次\x01",
            "都这么侥幸哟☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C679():

        label("loc_C679")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_C679")

    QueueWorkItem2(0x101, 1, lambda_C679)

    def lambda_C68B():

        label("loc_C68B")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_C68B")

    QueueWorkItem2(0xEF, 1, lambda_C68B)
    SetChrFlags(0x18, 0x1000)
    OP_95(0x18, -3310, 0, 340, 5000, 0x0)
    OP_95(0x18, -240, 0, -2920, 5000, 0x0)

    def lambda_C6CA():
        OP_95(0xFE, -80, 0, -8710, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C6CA)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(310, 1200, -870, 0)
    MoveCamera(323, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14850, 0)
    SetChrPos(0x101, -780, 0, 180, 180)
    SetChrPos(0xEF, 850, 0, 160, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_C7A2")

    #C0673
    ChrTalk(
        0x102,
        (
            "#00105F……走掉了。\x02\x03",

            "#00104F话说回来，它比想象中\x01",
            "好找很多啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_C7A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_C7F5")

    #C0674
    ChrTalk(
        0x103,
        (
            "#00205F……走掉了。\x02\x03",

            "#00204F话说回来，它比想象中\x01",
            "好找很多呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_C7F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_C846")

    #C0675
    ChrTalk(
        0x104,
        (
            "#00305F……走掉了。\x02\x03",

            "#00304F说起来，它比想象中\x01",
            "好找很多呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_C846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_C899")

    #C0676
    ChrTalk(
        0x109,
        (
            "#10105F……走掉了。\x02\x03",

            "#10104F话说回来，它比想象中\x01",
            "好找很多呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_C899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_C8EE")

    #C0677
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，走掉了。\x02\x03",

            "#10302F话说回来，它比想象中\x01",
            "好找很多呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_C8EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_C92E")

    #C0678
    ChrTalk(
        0x153,
        (
            "#01105F走掉了～\x02\x03",

            "#01102F很容易就能找到它呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_C92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_C97F")

    #C0679
    ChrTalk(
        0x156,
        (
            "#06405F……走掉了呢～\x02\x03",

            "#06404F说起来，它藏得\x01",
            "未免也太好找了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_C97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_C9CC")

    #C0680
    ChrTalk(
        0x14C,
        (
            "#05905F走掉了啊。\x02\x03",

            "#05904F说起来，它藏得\x01",
            "其实很好找啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_C9CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_CA1F")

    #C0681
    ChrTalk(
        0x134,
        (
            "#01705F走掉了呢。\x02\x03",

            "#01706F话说回来，总觉得\x01",
            "很容易就能找到它……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_CA1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_CA6C")

    #C0682
    ChrTalk(
        0x135,
        (
            "#01805F……走掉了呢。\x02\x03",

            "#01803F老实说，它藏得\x01",
            "太好找了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA1")

    label("loc_CA6C")


    #C0683
    ChrTalk(
        0x166,
        (
            "#14005F……它走了。\x02\x03",

            "#14006F藏得明明\x01",
            "很差啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_CB20")

    #C0684
    ChrTalk(
        0x101,
        (
            "#00003F嗯……\x01",
            "看来它只是喜欢捉迷藏而已，\x01",
            "但却并不太擅长……\x02\x03",

            "#00000F总之，我们保持这种势头，\x01",
            "把它找出来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB91")

    label("loc_CB20")


    #C0685
    ChrTalk(
        0x101,
        (
            "#00003F唔……\x01",
            "看来它只是喜欢捉迷藏而已，\x01",
            "但却并不太擅长……\x02\x03",

            "#00000F总之，我们保持这种势头，\x01",
            "把它找出来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB91")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xB)
    SetScenarioFlags(0x1C9, 3)
    OP_65(0x0, 0x1)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x0, 130, 0, -70, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_C450 end

    def Function_37_CBC6(): pass

    label("Function_37_CBC6")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0686
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　 ～占卜馆～ 　　\x01",
            "恋爱运、财运及其它运势……\x01",
            "可以测算你的各种命运！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_37_CBC6 end

    def Function_38_CC2C(): pass

    label("Function_38_CC2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD14")
    EventBegin(0x1)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 0)

    #C0687
    ChrTalk(
        0xF,
        "欢迎来到『占卜馆』！\x02",
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0xF,
        (
            "在这里，可以让非常厉害的占卜师\x01",
            "给大家占卜各种运势！\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x101,
        (
            "#00000F（我们还在和咪雪捉迷藏……\x01",
            "　现在还是不要\x01",
            "　进这种地方了。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -70, 0, 4080, 180)
    OP_4C(0xF, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    EventEnd(0x4)
    Jump("loc_CD17")

    label("loc_CD14")

    Call(0, 18)

    label("loc_CD17")

    Return()

    # Function_38_CC2C end

    SaveToFile()

Try(main)
