from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c015c.bin",                # FileName
        "c015c",                    # MapName
        "c015c",                    # Location
        0x0007,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 7, 0, 3, 0, 4],
    )

    BuildStringList((
        "c015c",                  # 0
        "霍伊斯托夫",             # 1
        "布拉温",                 # 2
        "赛尔缇欧",               # 3
        "侬诺",                   # 4
        "罗伯兹主任",             # 5
        "伊兹丽夫人",             # 6
        "菲利克",                 # 7
        "辛迪",                   # 8
        "亨利",                   # 9
        "约库斯",                 # 10
        "玛丽埃塔",               # 11
        "青年",                   # 12
        "少女",                   # 13
        "弗罗缇",                 # 14
        "游客",                   # 15
        "游客",                   # 16
        "游客",                   # 17
        "游客",                   # 18
        "游客",                   # 19
        "游客",                   # 20
        "游客",                   # 21
        "游客",                   # 22
        "游客",                   # 23
        "基隆德",                 # 24
        "游击士温蔡尔",           # 25
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch34302.itc",                   # 04
        "chr/ch23402.itc",                   # 05
        "chr/ch21402.itc",                   # 06
        "chr/ch21202.itc",                   # 07
        "chr/ch20200.itc",                   # 08
        "chr/ch20802.itc",                   # 09
        "chr/ch21600.itc",                   # 0A
        "chr/ch21602.itc",                   # 0B
        "chr/ch24500.itc",                   # 0C
        "chr/ch24502.itc",                   # 0D
        "chr/ch21200.itc",                   # 0E
        "chr/ch21702.itc",                   # 0F
        "chr/ch22000.itc",                   # 10
        "chr/ch22100.itc",                   # 11
        "chr/ch22200.itc",                   # 12
        "chr/ch27600.itc",                   # 13
        "chr/ch21900.itc",                   # 14
        "chr/ch32300.itc",                   # 15
        "chr/ch24500.itc",                   # 16
        "chr/ch27300.itc",                   # 17
        "chr/ch29302.itc",                   # 18
        "chr/ch29300.itc",                   # 19
    ))

    DeclNpc(-509,    0,       12449,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-42889,  0,       5699,    0,    257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-45700,  0,       5530,    0,    257,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-8880,   0,       3240,    45,   257,  0x0, 0,   3,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-1750,   5000,    17659,   180,  341,  0x0, 0,   24,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-949,    200,     2299,    273,  405,  0x0, 2,   15,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-2190,   0,       -200,    0,    389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-4670,   0,       4480,    45,   405,  0x0, 0,   17,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-5730,   0,       1269,    270,  405,  0x0, 0,   18,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-759,    0,       3640,    180,  405,  0x0, 0,   19,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-3710,   0,       5789,    225,  405,  0x0, 0,   20,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(610,     5000,    9779,    180,  389,  0x0, 0,   21,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-500,    5000,    9770,    180,  389,  0x0, 0,   22,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-7449,   150,     8510,    270,  341,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6829,    150,     3569,    270,  469,  0x0, 0,   5,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(2009,    150,     3569,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(1200,    0,       -1909,   135,  385,  0x0, 0,   14,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(2019,    0,       5309,    315,  385,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   11,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(3289,    0,       6320,    315,  385,  0x0, 0,   12,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5369,    150,     -3880,   270,  469,  0x0, 0,   13,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(60580,   -1000,   -8600,   270,  257,  0x0, 0,   8,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(56479,   -1000,   -8770,   90,   389,  0x0, 0,   23,  0,   0,   0,   0,   7,   255,  0)

    DeclActor(59140,   -1000,   -8880,   1500,    60580,   500,     -8600,   0x007E, 0,  5,  0x0000)
    DeclActor(-510,    0,       10640,   1000,    -510,    1500,    12450,   0x007E, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_488",          # 00, 0
        "Function_1_540",          # 01, 1
        "Function_2_5DD",          # 02, 2
        "Function_3_667",          # 03, 3
        "Function_4_7A5",          # 04, 4
        "Function_5_7A6",          # 05, 5
        "Function_6_7AA",          # 06, 6
        "Function_7_14E2",         # 07, 7
        "Function_8_15DD",         # 08, 8
        "Function_9_15E1",         # 09, 9
        "Function_10_1C5D",        # 0A, 10
        "Function_11_204B",        # 0B, 11
        "Function_12_23BB",        # 0C, 12
        "Function_13_24E3",        # 0D, 13
        "Function_14_2943",        # 0E, 14
        "Function_15_2B14",        # 0F, 15
        "Function_16_2C5D",        # 10, 16
        "Function_17_2C9F",        # 11, 17
        "Function_18_2CDB",        # 12, 18
        "Function_19_2E45",        # 13, 19
        "Function_20_2E90",        # 14, 20
        "Function_21_2FE7",        # 15, 21
        "Function_22_3025",        # 16, 22
        "Function_23_3190",        # 17, 23
        "Function_24_32FC",        # 18, 24
        "Function_25_33EA",        # 19, 25
        "Function_26_350E",        # 1A, 26
        "Function_27_355D",        # 1B, 27
        "Function_28_3612",        # 1C, 28
        "Function_29_36C0",        # 1D, 29
        "Function_30_37A5",        # 1E, 30
        "Function_31_37FF",        # 1F, 31
        "Function_32_39BD",        # 20, 32
        "Function_33_45C5",        # 21, 33
    ))


    def Function_0_488(): pass

    label("Function_0_488")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4C8"),
        (1, "loc_4D4"),
        (2, "loc_4E0"),
        (3, "loc_4EC"),
        (4, "loc_4F8"),
        (5, "loc_504"),
        (6, "loc_510"),
        (SWITCH_DEFAULT, "loc_51C"),
    )


    label("loc_4C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_504")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_510")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_51C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_528")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_53F")

    Return()

    # Function_0_488 end

    def Function_1_540(): pass

    label("Function_1_540")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DC")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_540")

    label("loc_5DC")

    Return()

    # Function_1_540 end

    def Function_2_5DD(): pass

    label("Function_2_5DD")


    def lambda_5E2():
        OP_A6(0xFE, 0x4, 0x0, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5E2)

    label("loc_5F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_666")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_63B")
    OP_94(0xFE, 0xFFFFF16E, 0x1C0C, 0x3B6, 0x20DA, 0x3E8)
    Sleep(100)
    Jump("loc_661")

    label("loc_63B")

    OP_93(0xFE, 0xE1, 0x3E8)
    OP_93(0xFE, 0x13B, 0x3E8)
    OP_93(0xFE, 0x2D, 0x3E8)
    OP_93(0xFE, 0x87, 0x3E8)
    OP_93(0xFE, 0xE1, 0x3E8)
    Sleep(500)

    label("loc_661")

    Jump("loc_5F6")

    label("loc_666")

    Return()

    # Function_2_5DD end

    def Function_3_667(): pass

    label("Function_3_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6EF")
    SetChrPos(0xB, -6980, 0, 1280, 90)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0xC, -210, 5000, 18380, 0)
    SetChrChipByIndex(0xC, 0x19)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x10)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7A4")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_735")
    SetChrPos(0xA, -1460, 0, 7630, 180)
    BeginChrThread(0xA, 0, 0, 2)
    SetChrPos(0xB, 6810, 0, 9660, 270)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_7A4")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_752")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_7A4")

    label("loc_752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_76F")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_7A4")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_78C")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_7A4")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7A4")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_7A4")

    Return()

    # Function_3_667 end

    def Function_4_7A5(): pass

    label("Function_4_7A5")

    Return()

    # Function_4_7A5 end

    def Function_5_7A6(): pass

    label("Function_5_7A6")

    Call(0, 6)
    Return()

    # Function_5_7A6 end

    def Function_6_7AA(): pass

    label("Function_6_7AA")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94A")

    #C0001
    ChrTalk(
        0x1F,
        (
            "嘿，欢迎光临。\x01",
            "本来应该这么说……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x1F,
        (
            "不过，小子们，在克洛斯贝尔，\x01",
            "如果没有许可证的话，是不能买武器的。\x01",
            "如果只是来闲逛的话，还是请回吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0000F啊，不，我们\x01",
            "是克洛斯贝尔警察局的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x1F,
        "你们这样的小鬼会是警察……？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x1F,
        (
            "对了，你们就是\x01",
            "赛尔盖那家伙之前说的……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x1F,
        (
            "哼，知道啦。\x01",
            "你们随便看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x1F,
        (
            "想买武器的时候，\x01",
            "要给我看调查手册啊。\x01",
            "这个可以代替许可证。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 2)
    SetScenarioFlags(0xAF, 2)

    label("loc_94A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_954")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_9A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9C3")
    OP_AF(0x5)
    Jump("loc_A05")

    label("loc_9C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9D3")
    OP_AF(0x4)
    Jump("loc_A05")

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9E3")
    OP_AF(0x3)
    Jump("loc_A05")

    label("loc_9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9F3")
    OP_AF(0x2)
    Jump("loc_A05")

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A03")
    OP_AF(0x1)
    Jump("loc_A05")

    label("loc_A03")

    OP_AF(0x0)

    label("loc_A05")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14D9")

    label("loc_A14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A28")
    Jump("loc_14D9")

    label("loc_A28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABA")

    #C0008
    ChrTalk(
        0x1F,
        (
            "哎呀呀，狂欢\x01",
            "也就到今天为止了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x1F,
        (
            "哦……好吧，你们几个，\x01",
            "要玩乐的话，也就趁现在了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AF7")

    label("loc_ABA")


    #C0010
    ChrTalk(
        0x1F,
        (
            "到今天为止，都可以不拘小节。\x01",
            "要玩乐的话，也就趁现在了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF7")

    Jump("loc_14D9")

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_B65")

    #C0011
    ChrTalk(
        0x1F,
        (
            "哟，还在找那个\x01",
            "走失的孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x1F,
        (
            "这个城市很大啊……\x01",
            "不过，也只能耐心\x01",
            "去探听情报了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D9")

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE8")

    #C0013
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0015
    ChrTalk(
        0x1F,
        (
            "哦，拿着照片\x01",
            "探听情报吗……\x01",
            "今天做的事倒是很像警察的工作嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，是啊……\x02\x03",

            "#0001F那么，您有线索吗？\x01",
            "这是我一个熟人的孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x1F,
        (
            "我并没有去看游行，\x01",
            "既然他没来我的店，那我肯定没见过。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x1F,
        (
            "不过，如果他是跟着\x01",
            "游行的队伍走了，\x01",
            "应该是去了东街那边吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x1F,
        (
            "游行队伍的行进路线\x01",
            "应该是会经过那里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0008F说得也是呢……\x01",
            "（可是，根据兰迪的联络，\x01",
            "  他好像没有去过东街……）\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x160,
        (
            "#3300F……那么，大哥哥，\x01",
            "你打算怎么办呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 0)
    Call(0, 31)

    #C0022
    ChrTalk(
        0x160,
        (
            "#3304F呵呵……真是慎重啊，\x01",
            "好有趣的大哥哥。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4B")

    label("loc_DE8")


    #C0023
    ChrTalk(
        0x1F,
        (
            "游行的行进路线\x01",
            "应该是从这里往东街去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x1F,
        (
            "如果是跟着\x01",
            "游行的队伍走了，\x01",
            "应该就是去那边了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4B")

    Jump("loc_14D9")

    label("loc_E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF7")

    #C0025
    ChrTalk(
        0x1F,
        (
            "导力车吗……游行\x01",
            "也是日新月异啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x1F,
        (
            "不过，警察们还是那么忙，\x01",
            "这一点倒是一直都没变呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x1F,
        "那些新人警官如今肯定都已经精疲力尽了吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F35")

    label("loc_EF7")


    #C0028
    ChrTalk(
        0x1F,
        (
            "就算时代变迁，\x01",
            "警察们的忙碌和辛苦也是\x01",
            "从来都不会变的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F35")

    Jump("loc_14D9")

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_100A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAC")

    #C0029
    ChrTalk(
        0x1F,
        "今天有游行呢。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x1F,
        (
            "哎呀呀……\x01",
            "那些穿制服的家伙可要辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x1F,
        "我真同情他们啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1005")

    label("loc_FAC")


    #C0032
    ChrTalk(
        0x1F,
        (
            "你们要是有空的话，\x01",
            "也可以去行政区的广场看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x1F,
        "穿制服的家伙们一定都手忙脚乱了。\x02",
    )

    CloseMessageWindow()

    label("loc_1005")

    Jump("loc_14D9")

    label("loc_100A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_12BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1250")

    #C0034
    ChrTalk(
        0x1F,
        (
            "我本想和赛尔盖那家伙\x01",
            "一起去喝一杯……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x1F,
        "不过，他今天好像要开会啊。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x1F,
        (
            "唔～希望不是又把麻烦事\x01",
            "推给他了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x101,
        "#0005F此话怎讲……？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x1F,
        (
            "啊，那家伙从以前开始\x01",
            "就一直是个怪人嘛。\x01",
            "总会莫名其妙地背上一些麻烦事。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x1F,
        (
            "比如给你们『特别任务支援科』\x01",
            "收拾善后什么的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x103,
        "#0203F的确是呢……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x1F,
        (
            "不过，支援科是那家伙\x01",
            "自己建立的部门。\x01",
            "这也算是自作自受吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12B6")

    label("loc_1250")


    #C0042
    ChrTalk(
        0x1F,
        (
            "算了，今天的会议大概是\x01",
            "商讨明天游行时的警备体制吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x1F,
        (
            "支援科毕竟立过了大功，\x01",
            "也不用太担心吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B6")

    Jump("loc_14D9")

    label("loc_12BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133C")

    #C0044
    ChrTalk(
        0x1F,
        (
            "话说回来，亚里欧斯\x01",
            "那家伙好像回国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x1F,
        "今年的人多得非比寻常嘛。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x1F,
        (
            "他好像也\x01",
            "不得不回来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_137E")

    label("loc_133C")


    #C0047
    ChrTalk(
        0x1F,
        "亚里欧斯好像也回自治州了。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1F,
        "今年的人这么多，也没办法吧。\x02",
    )

    CloseMessageWindow()

    label("loc_137E")

    Jump("loc_14D9")

    label("loc_1383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_14D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1485")

    #C0049
    ChrTalk(
        0x1F,
        (
            "……欢迎，\x01",
            "这里是武器店。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x1F,
        (
            "哎，怎么，是你们啊。\x01",
            "还以为是吵闹的游客呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x1F,
        (
            "你们也真是的，在如此喜庆的日子，\x01",
            "就不要再到这么冷清的武器店来啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x1F,
        (
            "好啦，办完事就\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0000F哈哈哈……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        "#0200F真是冷若冰霜啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D9")

    label("loc_1485")


    #C0055
    ChrTalk(
        0x1F,
        (
            "我这里可是武器店，\x01",
            "在这么喜庆的日子别进来啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x1F,
        (
            "好啦，办完事就\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D9")

    Jump("loc_954")

    label("loc_14DE")

    TalkEnd(0x1F)
    Return()

    # Function_6_7AA end

    def Function_7_14E2(): pass

    label("Function_7_14E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_15D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1580")

    #C0057
    ChrTalk(
        0xFE,
        (
            "因为工作与警备任务，\x01",
            "分部的游击士全都被派出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "为了防备紧急情况，\x01",
            "我留在克洛斯贝尔市待命。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "趁现在买把新剑吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_15D9")

    label("loc_1580")


    #C0060
    ChrTalk(
        0xFE,
        (
            "我和搭档斯克特今天也要分别行动……\x01",
            "不过，那家伙的话，就算是独自一人也不需要担心吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D9")

    TalkEnd(0xFE)
    Return()

    # Function_7_14E2 end

    def Function_8_15DD(): pass

    label("Function_8_15DD")

    Call(0, 9)
    Return()

    # Function_8_15DD end

    def Function_9_15E1(): pass

    label("Function_9_15E1")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C59")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_163E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_163E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165E")
    OP_AF(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C54")

    label("loc_165E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1672")
    Jump("loc_1C54")

    label("loc_1672")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C54")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16D4")

    #C0061
    ChrTalk(
        0x8,
        "这可真是一大家子啊。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "呵呵，今天我也\x01",
            "下厨帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_16D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_175C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1726")

    #C0063
    ChrTalk(
        0x8,
        "咳咳……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "本店员工的一点才艺，\x01",
            "大家还喜欢吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1757")

    label("loc_1726")


    #C0065
    ChrTalk(
        0x8,
        (
            "赛尔缇欧……\x01",
            "你就没有再像样点的才艺了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1757")

    Jump("loc_1C54")

    label("loc_175C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1924")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186E")

    #C0066
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0068
    ChrTalk(
        0x8,
        (
            "哦，是走失的孩子吗？\x01",
            "这可真是可怜啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "不过我没有头绪呢，\x01",
            "他应该没有来过本店。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 31)
    Jump("loc_191F")

    label("loc_186E")


    #C0071
    ChrTalk(
        0x8,
        (
            "唔，从照片看来，\x01",
            "这孩子长得还真漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "感觉似乎和这位小姑娘\x01",
            "有那么几分神似呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#0005F（这么一说……\x01",
            "  好像还真是有点像啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x160,
        "#3308F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_191F")

    Jump("loc_1C54")

    label("loc_1924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_19AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1976")

    #C0075
    ChrTalk(
        0x8,
        "咳咳……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "本店员工的一点才艺，\x01",
            "大家还喜欢吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19A7")

    label("loc_1976")


    #C0077
    ChrTalk(
        0x8,
        (
            "赛尔缇欧……\x01",
            "你就没有再像样点的才艺了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A7")

    Jump("loc_1C54")

    label("loc_19AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A26")

    #C0078
    ChrTalk(
        0x8,
        (
            "本店下午\x01",
            "会有员工\x01",
            "进行才艺表演。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "计划在游行结束之后开始，\x01",
            "不嫌弃的话，请过来看看哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A6D")

    label("loc_1A26")


    #C0080
    ChrTalk(
        0x8,
        (
            "……毕竟是赛尔缇欧\x01",
            "灵机一动想到的点子。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        "不过真的能顺利吗……\x02",
    )

    CloseMessageWindow()

    label("loc_1A6D")

    Jump("loc_1C54")

    label("loc_1A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1AD9")

    #C0082
    ChrTalk(
        0x8,
        (
            "我们准备了纪念庆典时期的\x01",
            "限定料理——\x01",
            "特制午间套餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "数量有限，\x01",
            "还请尽早点餐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_1AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B85")

    #C0084
    ChrTalk(
        0x8,
        (
            "虽然满座是件好事……\x01",
            "但从早上到现在，仍有一部分\x01",
            "食材没有送到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "由于纪念庆典的影响，\x01",
            "各处的送货员都迟到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        "哎呀，真是伤脑筋啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BA4")

    label("loc_1B85")


    #C0087
    ChrTalk(
        0x8,
        (
            "必须要想点办法\x01",
            "才行呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA4")

    Jump("loc_1C54")

    label("loc_1BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C02")

    #C0088
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "客人是四位吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "请到空着的位置\x01",
            "随意就坐。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C54")

    label("loc_1C02")


    #C0090
    ChrTalk(
        0x8,
        (
            "这才刚是第二天呢……\x01",
            "今年的客人可真多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "本店也会更加用心地\x01",
            "提供服务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C54")

    Jump("loc_15EE")

    label("loc_1C59")

    TalkEnd(0x8)
    Return()

    # Function_9_15E1 end

    def Function_10_1C5D(): pass

    label("Function_10_1C5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE5")

    #C0092
    ChrTalk(
        0xFE,
        (
            "今天我们打算\x01",
            "开个慰劳会。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "准备在店里打烊以后，\x01",
            "召集店员们去喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "今年事情多，十分忙碌嘛。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D2D")

    label("loc_1CE5")


    #C0095
    ChrTalk(
        0xFE,
        (
            "今天我们打算\x01",
            "开个慰劳会。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧……\x01",
            "看来还是不要喝酒为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2D")

    Jump("loc_2047")

    label("loc_1D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1D6C")

    #C0097
    ChrTalk(
        0xFE,
        "店里好像很吵闹呢。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "出什么事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2047")

    label("loc_1D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1DAD")

    #C0099
    ChrTalk(
        0xFE,
        (
            "我小的时候\x01",
            "也很期待游行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        "游行很棒呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2047")

    label("loc_1DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1E64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E20")

    #C0101
    ChrTalk(
        0xFE,
        (
            "好，一份特制午间套餐，\x01",
            "已经做完啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "纪念庆典时，客人果然多呢。\x01",
            "实在是够忙的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E5F")

    label("loc_1E20")


    #C0103
    ChrTalk(
        0xFE,
        "今年可真是热闹非凡啊。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "听说港湾区那边\x01",
            "还有舞台表演？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5F")

    Jump("loc_2047")

    label("loc_1E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F48")

    #C0105
    ChrTalk(
        0xFE,
        (
            "食材的送货延迟了，\x01",
            "从Ａ套餐到Ｃ套餐，\x01",
            "终于全部都卖光，做不出来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "正因如此，\x01",
            "我们就把所有的午餐菜式都混在一起，\x01",
            "推出了纪念庆典的特别限定套餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "名为特制午间套餐。\x01",
            "……这创意很不错吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F81")

    label("loc_1F48")


    #C0108
    ChrTalk(
        0xFE,
        (
            "今天推出了\x01",
            "特制午间套餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "想点餐的话请尽快哦。\x02",
    )

    CloseMessageWindow()

    label("loc_1F81")

    Jump("loc_2047")

    label("loc_1F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2012")

    #C0110
    ChrTalk(
        0xFE,
        (
            "因为纪念庆典的影响，\x01",
            "食材的送货延迟了，\x01",
            "Ａ套餐今天已经卖光了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "伤脑筋啊，\x01",
            "稍后跟霍伊斯托夫商量看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2047")

    label("loc_2012")


    #C0112
    ChrTalk(
        0xFE,
        (
            "这种时候，慌张也无济于事，\x01",
            "就交给店长来决定吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2047")

    TalkEnd(0xFE)
    Return()

    # Function_10_1C5D end

    def Function_11_204B(): pass

    label("Function_11_204B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CD")

    #C0113
    ChrTalk(
        0xFE,
        (
            "好痛……\x01",
            "昨天好像喝多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "脑袋一阵阵地痛，\x01",
            "什么都不记得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "……我是不是做了什么啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_20FA")

    label("loc_20CD")


    #C0116
    ChrTalk(
        0xFE,
        (
            "呜呜，头好痛……\x01",
            "我昨天到底干了什么呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20FA")

    Jump("loc_23B7")

    label("loc_20FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2176")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2140")

    #C0117
    ChrTalk(
        0xFE,
        "嘿～……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        "四号，开始唱了～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2171")

    label("loc_2140")


    #C0119
    ChrTalk(
        0xFE,
        "呜哈哈哈……！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "来吧，今天\x01",
            "要大喝特喝～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2171")

    Jump("loc_23B7")

    label("loc_2176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_21F1")

    #C0121
    ChrTalk(
        0xFE,
        (
            "呼……其实，\x01",
            "我很会唱歌的。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "今天要让客人们\x01",
            "听听我的美妙歌声哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "希望会有\x01",
            "很多的女孩子来听啊¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B7")

    label("loc_21F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_22C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2275")

    #C0124
    ChrTalk(
        0xFE,
        (
            "他们教给我的特制午间套餐，\x01",
            "稍微试了一下，还挺容易做的，真是意外。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "嘿嘿……我的才能真是可怕啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_22C2")

    label("loc_2275")


    #C0126
    ChrTalk(
        0xFE,
        (
            "等着吧，客人。\x01",
            "这就让您尝尝我的特制午餐……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "……好烫！被油溅到了！\x02",
    )

    CloseMessageWindow()

    label("loc_22C2")

    Jump("loc_23B7")

    label("loc_22C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_235E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233B")

    #C0128
    ChrTalk(
        0xFE,
        (
            "布拉温先生\x01",
            "突然跟我说\x01",
            "要制作新菜式。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "……说得倒轻松，\x01",
            "哪能那么轻易就做出来啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2359")

    label("loc_233B")


    #C0130
    ChrTalk(
        0xFE,
        "唉唉，我也想出去玩啊～！\x02",
    )

    CloseMessageWindow()

    label("loc_2359")

    Jump("loc_23B7")

    label("loc_235E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23B7")

    #C0131
    ChrTalk(
        0xFE,
        (
            "右手切菜，\x01",
            "左手拿锅……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "呜噢噢噢，来不及啦～！\x01",
            "怎么能同时做五道菜啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B7")

    TalkEnd(0xFE)
    Return()

    # Function_11_204B end

    def Function_12_23BB(): pass

    label("Function_12_23BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2406")

    #C0133
    ChrTalk(
        0xFE,
        (
            "今天来了\x01",
            "一大家子客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "我也得\x01",
            "鼓足干劲才行呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DF")

    label("loc_2406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2437")

    #C0135
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧他莫非\x01",
            "不能喝酒吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DF")

    label("loc_2437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2488")

    #C0136
    ChrTalk(
        0xFE,
        "今天好像有游行呢。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "广场那边吵吵闹闹的，\x01",
            "就是因为这个吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DF")

    label("loc_2488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_24DF")

    #C0138
    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "Ａ套餐现在\x01",
            "已经卖完了。\x01",
            "想点套餐的话，请点Ｂ或者Ｃ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DF")

    TalkEnd(0xFE)
    Return()

    # Function_12_23BB end

    def Function_13_24E3(): pass

    label("Function_13_24E3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2577")
    Jump("loc_25C1")

    label("loc_2577")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2597")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25C1")

    label("loc_2597")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25B7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25C1")

    label("loc_25B7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25C1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_267E")

    #C0140
    ChrTalk(
        0xFE,
        "今天就是最终日了呢……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "我至少该去听听\x01",
            "市长的闭幕宣言吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "狂欢的尾声……\x01",
            "别具韵味，倒也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293B")

    label("loc_267E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_26E1")

    #C0144
    ChrTalk(
        0xFE,
        "噗……！？\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "……那个厨师，\x01",
            "别表演这种奇怪的才艺啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        "害得我都喷咖啡了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_293B")

    label("loc_26E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_278E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273F")

    #C0147
    ChrTalk(
        0xFE,
        (
            "一直在说游行、游行的，\x01",
            "大家还真烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "所以我才讨厌游客。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2789")

    label("loc_273F")


    #C0149
    ChrTalk(
        0xFE,
        (
            "难道他们就不明白，\x01",
            "也有一些客人只想静静地\x01",
            "沉浸在读书的乐趣之中吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2789")

    Jump("loc_293B")

    label("loc_278E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_280B")

    #C0150
    ChrTalk(
        0xFE,
        "今天也都是些大呼小叫的吵闹客人……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "哼，什么特制午餐嘛。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "我就和平时一样，\x01",
            "点一杯咖啡坐到底好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293B")

    label("loc_280B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28A2")

    #C0153
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "各家商店似乎都在出售\x01",
            "只有这个时期才能买到的商品。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "一直卖下去多好啊，\x01",
            "万一要是没买到，会很懊恼的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293B")

    label("loc_28A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_293B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2914")

    #C0156
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "大家都兴高采烈，吵吵嚷嚷的……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "所以我才\x01",
            "讨厌克洛斯贝尔人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_293B")

    label("loc_2914")


    #C0159
    ChrTalk(
        0xFE,
        (
            "哼，我才不会\x01",
            "受什么庆典的影响呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_24E3 end

    def Function_14_2943(): pass

    label("Function_14_2943")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29D7")
    Jump("loc_2A21")

    label("loc_29D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29F7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A21")

    label("loc_29F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A17")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A21")

    label("loc_2A17")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A21")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADF")

    #C0160
    ChrTalk(
        0xFE,
        (
            "唔，儿子似乎\x01",
            "也很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "我们出身于大陆的东方。\x01",
            "远道而来，本来还有些不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "看样子，稍微努点力，\x01",
            "过来玩一趟也是值得的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2B0C")

    label("loc_2ADF")


    #C0163
    ChrTalk(
        0xFE,
        (
            "我们是远道而来的，\x01",
            "一定要好好享受才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B0C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_2943 end

    def Function_15_2B14(): pass

    label("Function_15_2B14")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BA8")
    Jump("loc_2BF2")

    label("loc_2BA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF2")

    label("loc_2BC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BE8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF2")

    label("loc_2BE8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BF2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0164
    ChrTalk(
        0xFE,
        "喂～儿童套餐还没好吗～？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        "我想早点吃完出去玩呀～\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_2B14 end

    def Function_16_2C5D(): pass

    label("Function_16_2C5D")

    TalkBegin(0xFE)

    #C0166
    ChrTalk(
        0xFE,
        (
            "乡下的老爸\x01",
            "明天会来看我。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "要预约个好位置才行呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_2C5D end

    def Function_17_2C9F(): pass

    label("Function_17_2C9F")

    TalkBegin(0xFE)

    #C0168
    ChrTalk(
        0xFE,
        "怎么样，老爸，开心吗？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "还好事先\x01",
            "预约了啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2C9F end

    def Function_18_2CDB(): pass

    label("Function_18_2CDB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D6F")
    Jump("loc_2DB9")

    label("loc_2D6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D8F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DB9")

    label("loc_2D8F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DAF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DB9")

    label("loc_2DAF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DB9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0170
    ChrTalk(
        0xFE,
        "唔，味道很不错呢。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "就连以前当过厨师的我\x01",
            "也都觉得无可挑剔。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        "可以放心品尝了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_2CDB end

    def Function_19_2E45(): pass

    label("Function_19_2E45")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x13B, 0x0)

    #C0173
    ChrTalk(
        0xFE,
        "好、好差劲的才艺表演啊！\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "完全不知道\x01",
            "是在模仿谁啊！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2E45 end

    def Function_20_2E90(): pass

    label("Function_20_2E90")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F24")
    Jump("loc_2F6E")

    label("loc_2F24")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F44")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F6E")

    label("loc_2F44")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F64")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F6E")

    label("loc_2F64")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F6E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0175
    ChrTalk(
        0xFE,
        (
            "说起游行，\x01",
            "果然还是要在中央广场看啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "得赶快出去\x01",
            "选个好地方才行。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_2E90 end

    def Function_21_2FE7(): pass

    label("Function_21_2FE7")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x13B, 0x0)

    #C0177
    ChrTalk(
        0xFE,
        "啊哈哈，不过好搞笑啊～！\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        "再来一个～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2FE7 end

    def Function_22_3025(): pass

    label("Function_22_3025")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30B9")
    Jump("loc_3103")

    label("loc_30B9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30D9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3103")

    label("loc_30D9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30F9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3103")

    label("loc_30F9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3103")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0179
    ChrTalk(
        0xFE,
        (
            "（嚼嚼……）\x01",
            "离游行开始，还有点时间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "要不要去逛逛百货店？\x01",
            "那里好像正在打折吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_3025 end

    def Function_23_3190(): pass

    label("Function_23_3190")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3224")
    Jump("loc_326E")

    label("loc_3224")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3244")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_326E")

    label("loc_3244")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3264")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_326E")

    label("loc_3264")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_326E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xD, 0x2)
    OP_4B(0x11, 0xFF)

    #C0181
    ChrTalk(
        0xD,
        "纪念庆典是一家人尽享天伦之乐的节日。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xD,
        (
            "至少在我家，\x01",
            "这一点是毫无疑问的。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_23_3190 end

    def Function_24_32FC(): pass

    label("Function_24_32FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_337D")

    #C0183
    ChrTalk(
        0xE,
        (
            "虽然我和朋友约好了出去玩，\x01",
            "不过，今天还是和家人们共同度过吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xE,
        (
            "已经有好久都没见过\x01",
            "老爸和老妈在一起了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E6")

    label("loc_337D")


    #C0185
    ChrTalk(
        0xE,
        (
            "我们家没人\x01",
            "敢违抗奶奶。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xE,
        "嘿嘿，也没办法啦。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "今天是最后一天了，\x01",
            "全家人在一起尽情玩乐吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_33E6")

    TalkEnd(0xFE)
    Return()

    # Function_24_32FC end

    def Function_25_33EA(): pass

    label("Function_25_33EA")

    TalkBegin(0xFE)
    OP_4B(0x12, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3467")
    TurnDirection(0xF, 0x0, 0)

    #C0188
    ChrTalk(
        0xF,
        "真是好久没有见到妈妈了。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xF,
        (
            "因为太久没见了，\x01",
            "今天真是吓了一跳呢～\x01",
            "真不愧是奶奶啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x2D, 0x0)
    Jump("loc_3506")

    label("loc_3467")


    #C0190
    ChrTalk(
        0xF,
        (
            "……妈妈！？\x01",
            "你是什么时候回自治州的！？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xF,
        (
            "工作呢？\x01",
            "真的没问题吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x12,
        (
            "婆婆叫我回来的，\x01",
            "没办法嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x12,
        (
            "而且，又能见到孩子们，\x01",
            "忍不住就溜出来了⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_3506")

    OP_4C(0x12, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_25_33EA end

    def Function_26_350E(): pass

    label("Function_26_350E")

    TalkBegin(0xFE)
    OP_4B(0xB, 0xFF)

    #C0194
    ChrTalk(
        0x10,
        (
            "请问，能麻烦你\x01",
            "加把椅子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "明白了，\x01",
            "立刻给您拿过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_26_350E end

    def Function_27_355D(): pass

    label("Function_27_355D")

    TalkBegin(0xFE)

    #C0196
    ChrTalk(
        0x11,
        (
            "妈妈，我们还有工作要做呢，\x01",
            "您这样擅自叫我们回来，会令我们头疼的啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        "不过你们好像还是设法申请到了年中休假吧。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xD,
        (
            "好了，别站在那里，赶快坐下吧。\x01",
            "要开始用餐了哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_355D end

    def Function_28_3612(): pass

    label("Function_28_3612")

    TalkBegin(0xFE)
    OP_4B(0xF, 0xFF)

    #C0199
    ChrTalk(
        0xF,
        (
            "……妈妈！？\x01",
            "你是什么时候回自治州的！？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xF,
        (
            "工作呢？\x01",
            "真的没问题吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x12,
        (
            "婆婆叫我回来的，\x01",
            "没办法嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x12,
        (
            "而且，又能见到孩子们，\x01",
            "忍不住就溜出来了⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_28_3612 end

    def Function_29_36C0(): pass

    label("Function_29_36C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_371B")

    #C0203
    ChrTalk(
        0x13,
        (
            "在那家伙的家里，\x01",
            "奶奶好像比较权威呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x13,
        (
            "嘁，今天\x01",
            "没法一起去玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A1")

    label("loc_371B")


    #C0205
    ChrTalk(
        0x13,
        (
            "嘁，竟然抛下我们这些朋友，\x01",
            "去和家人吃饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x13,
        (
            "菲利克那家伙，\x01",
            "还真是有点孩子气……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x13,
        (
            "不、不过，\x01",
            "有一点羡慕呢，只有一点啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_37A1")

    TalkEnd(0xFE)
    Return()

    # Function_29_36C0 end

    def Function_30_37A5(): pass

    label("Function_30_37A5")

    TalkBegin(0xFE)

    #C0208
    ChrTalk(
        0x14,
        (
            "菲利克那家伙，\x01",
            "好像很开心呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x14,
        (
            "唉～要是我家\x01",
            "也有个那么健朗的\x01",
            "奶奶就好了～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_37A5 end

    def Function_31_37FF(): pass

    label("Function_31_37FF")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3943")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_38B0")

    #C0210
    ChrTalk(
        0x101,
        (
            "#0003F按原定计划，继续探听吧。\x01",
            "没有收集到足够的情报\x01",
            "就强行进行判断，往往是错误之源。\x02\x03",

            "#0000F在中央广场已经探听够了，\x01",
            "……接下来就去站前街道吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_392C")

    label("loc_38B0")


    #C0211
    ChrTalk(
        0x160,
        (
            "#3300F（在中央广场的探听\x01",
            "  就到此为止吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x101,
        (
            "#0003F（嗯，应该足够了。）\x02\x03",

            "#0000F（接下来去\x01",
            "  站前街道打听看看吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_392C")

    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)
    Jump("loc_39BC")

    label("loc_3943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_39BC")

    #C0213
    ChrTalk(
        0x101,
        (
            "#0003F按原定计划，继续在\x01",
            "中央广场探听情报吧。\x02\x03",

            "#0000F没有收集到足够的情报\x01",
            "就强行进行判断，往往是错误之源。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BC")

    Return()

    # Function_31_37FF end

    def Function_32_39BD(): pass

    label("Function_32_39BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3BC1")
    TalkBegin(0xFE)
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3A72")

    #C0214
    ChrTalk(
        0xFE,
        "哎呀～好期待啊～\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "哈哈哈，所以\x01",
            "不必担心啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_3BA7")

    label("loc_3A72")


    #C0216
    ChrTalk(
        0xFE,
        (
            "啊哈哈，说得是呢～\x01",
            "中央广场的人太多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "……顺带一提，等一下\x01",
            "我打算去见缇欧呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "嗯嗯，哈哈哈！\x01",
            "这个不必担心啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x103,
        "#0211F（……主任……在和谁联络……）\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#0005F（缇欧，没关系吗？\x01",
            "  不用去和主任打个招呼吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x103,
        (
            "#0206F（……嗯，那样做的话，\x01",
            "  会让精神很疲惫的，\x01",
            "  还是无视他吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_3BA7")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    TalkEnd(0xFE)
    Jump("loc_45C4")

    label("loc_3BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3D89")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C5E")
    Jump("loc_3CA8")

    label("loc_3C5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CA8")

    label("loc_3C7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C9E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CA8")

    label("loc_3C9E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CA8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0222
    ChrTalk(
        0xFE,
        (
            "好，今天去基约姆的修理店\x01",
            "转转吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "那家伙以前就是那副德性，\x01",
            "肯定不会看什么游行的……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "呵呵，得给他带点\x01",
            "礼物去呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#0000F（缇欧的上司，\x01",
            "  十分享受庆典呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_45C4")

    label("loc_3D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3F0D")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E26")
    Jump("loc_3E70")

    label("loc_3E26")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E46")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E70")

    label("loc_3E46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E66")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E70")

    label("loc_3E66")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E70")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0226
    ChrTalk(
        0xFE,
        (
            "哎呀～今年的游行\x01",
            "真是太棒了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        "那就是传说中的『咪西』啊……\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "嗯嗯，拍了张\x01",
            "构图不错的照片呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_45C4")

    label("loc_3F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4121")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FAA")
    Jump("loc_3FF4")

    label("loc_3FAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FCA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FF4")

    label("loc_3FCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FEA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FF4")

    label("loc_3FEA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FF4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_408C")

    #C0229
    ChrTalk(
        0xFE,
        (
            "调出克洛斯贝尔市的\x01",
            "市街区地图，\x01",
            "检索最合适的好去处！\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "……嗯，果然还是\x01",
            "欢乐街那边最好吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_408C")


    #C0231
    ChrTalk(
        0xFE,
        (
            "今天有游行呢。\x01",
            "那么，要在哪里看好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "这种时候，便携终端就派上用场了！\x01",
            "（快速按键）……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        "#0211F主任……好像很开心呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_4115")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_45C4")

    label("loc_4121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42A0")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41BE")
    Jump("loc_4208")

    label("loc_41BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41DE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4208")

    label("loc_41DE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41FE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4208")

    label("loc_41FE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4208")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4243")
    Call(0, 33)
    Jump("loc_4294")

    label("loc_4243")


    #C0234
    ChrTalk(
        0xFE,
        "纪念庆典的特制午餐吗……\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "嗯嗯，既然是期间限定套餐，\x01",
            "那就非吃不可了呢¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4294")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_45C4")

    label("loc_42A0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4334")
    Jump("loc_437E")

    label("loc_4334")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4354")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_437E")

    label("loc_4354")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4374")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_437E")

    label("loc_4374")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_437E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_442A")

    #C0236
    ChrTalk(
        0xFE,
        (
            "稍后带去支援科，\x01",
            "当作慰问品吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "咳咳……缇欧\x01",
            "总是承蒙你们的照顾嘛。\x01",
            "我作为监督者，可要讲究礼节，好好感谢各位～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45BD")

    label("loc_442A")


    #C0238
    ChrTalk(
        0x103,
        "#0200F啊，主任……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "缇欧～……\x01",
            "哎呀，纪念庆典真是好啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "我去年也逛过，\x01",
            "不过，感觉今年更加豪华了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "啊，缇欧，要不要一起吃呢？\x01",
            "今天我请客哦……¤\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        "#0211F好意心领了。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0243
    ChrTalk(
        0xFE,
        "是、是吗，那就没办法了……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "算啦，稍后我带到支援科\x01",
            "去慰问你们吧，哈哈哈～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0245
    ChrTalk(
        0x103,
        "#0211F（都已经忘乎所以了……）\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        "#0000F（的确是高兴得忘乎所以了……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_45BD")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_45C4")

    Return()

    # Function_32_39BD end

    def Function_33_45C5(): pass

    label("Function_33_45C5")


    #C0247
    ChrTalk(
        0xFE,
        (
            "啊，缇欧～\x01",
            "真少见啊，就你们两个……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "啊，莫非是……\x01",
            "在约会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0011F……哎！？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        (
            "#0211F……请不要突然\x01",
            "说这么无聊的话，很烦人的。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "哈哈哈……\x01",
            "缇欧还是老样子啊¤\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "好，既然如此，\x01",
            "就把这个给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0253
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了 。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0254
    ChrTalk(
        0x103,
        (
            "#0203F（……看来是沉迷于纪念庆典，\x01",
            "  兴奋过头了呢。）\x02\x03",

            "#0201F（之后必须要好好教训他一顿。）\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        "#0003F（表、表情好恐怖啊，缇欧……）\x02",
    )

    CloseMessageWindow()
    AddItemNumber('黑市医生格伦　７卷', 1)
    SetScenarioFlags(0x9C, 6)
    Return()

    # Function_33_45C5 end

    SaveToFile()

Try(main)
