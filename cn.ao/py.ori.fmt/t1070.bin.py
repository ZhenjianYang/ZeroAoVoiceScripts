from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1070.bin",                # FileName
        "t1070",                    # MapName
        "t1070",                    # Location
        0x0000,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1070",                  # 0
        "玛瑞亚",                 # 1
        "泰勒",                   # 2
        "游客",                   # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "瓦吉",                   # 7
        "兰迪",                   # 8
        "诺艾尔",                 # 9
        "芙兰",                   # 10
    ))

    AddCharChip((
        "chr/ch32400.itc",                   # 00
        "chr/ch25900.itc",                   # 01
        "chr/ch33000.itc",                   # 02
        "chr/ch22000.itc",                   # 03
        "chr/ch33300.itc",                   # 04
        "chr/ch33200.itc",                   # 05
        "chr/ch03000.itc",                   # 06
        "chr/ch00300.itc",                   # 07
        "chr/ch02900.itc",                   # 08
        "chr/ch08500.itc",                   # 09
    ))

    DeclNpc(-6500,   0,       5000,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6300,   0,       9500,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       5000,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6119,    0,       3660,    90,   389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(6119,    0,       2240,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       5000,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(6119,    0,       3660,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(5550,    0,       10000,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(500,     0,       9000,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-500,    0,       9000,    0,    389,  0x0, 0,   9,   0,   0,   0,   0,   3,   255,  0)

    DeclActor(-4700,   0,       5000,    1000,    -6500,   1500,    5000,    0x007E, 0,  8,  0x0000)

    ChipFrameInfo(636, 0)                                        # 0

    ScpFunction((
        "Function_0_27C",          # 00, 0
        "Function_1_334",          # 01, 1
        "Function_2_4FB",          # 02, 2
        "Function_3_532",          # 03, 3
        "Function_4_6EB",          # 04, 4
        "Function_5_9DC",          # 05, 5
        "Function_6_B08",          # 06, 6
        "Function_7_F17",          # 07, 7
        "Function_8_FEA",          # 08, 8
        "Function_9_FEE",          # 09, 9
        "Function_10_1483",        # 0A, 10
        "Function_11_176E",        # 0B, 11
        "Function_12_18BB",        # 0C, 12
        "Function_13_192B",        # 0D, 13
        "Function_14_1A3F",        # 0E, 14
        "Function_15_1B94",        # 0F, 15
        "Function_16_2475",        # 10, 16
        "Function_17_24CE",        # 11, 17
        "Function_18_2527",        # 12, 18
        "Function_19_2580",        # 13, 19
        "Function_20_25CB",        # 14, 20
        "Function_21_261D",        # 15, 21
        "Function_22_353E",        # 16, 22
        "Function_23_3590",        # 17, 23
        "Function_24_3614",        # 18, 24
        "Function_25_366D",        # 19, 25
        "Function_26_36BF",        # 1A, 26
        "Function_27_370A",        # 1B, 27
        "Function_28_3736",        # 1C, 28
        "Function_29_3781",        # 1D, 29
        "Function_30_450D",        # 1E, 30
        "Function_31_506E",        # 1F, 31
        "Function_32_5D6E",        # 20, 32
    ))


    def Function_0_27C(): pass

    label("Function_0_27C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2BC"),
        (1, "loc_2C8"),
        (2, "loc_2D4"),
        (3, "loc_2E0"),
        (4, "loc_2EC"),
        (5, "loc_2F8"),
        (6, "loc_304"),
        (SWITCH_DEFAULT, "loc_310"),
    )


    label("loc_2BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_304")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_310")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_31C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_333")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_333")

    Return()

    # Function_0_27C end

    def Function_1_334(): pass

    label("Function_1_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_342")
    Jump("loc_47C")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_350")
    Jump("loc_47C")

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_3B0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 100, 0, 5000, 90)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1200, 0, 5000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1")
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_3AB")

    label("loc_3A1")

    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_3AB")

    Jump("loc_47C")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_3BE")
    Jump("loc_47C")

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_421")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_3FC")
    TurnDirection(0x10, 0x11, 0)
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x11, 0x10, 0)
    ClearChrFlags(0x11, 0x10)

    label("loc_3FC")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -5340, 0, 1100, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    Jump("loc_47C")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_43E")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_47C")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_44C")
    Jump("loc_47C")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_473")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_47C")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_47C")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    Event(0, 15)
    Jump("loc_4FA")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_4BB")
    Event(0, 21)
    Jump("loc_4FA")

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_4CC")
    Event(0, 29)
    Jump("loc_4FA")

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_4DD")
    Event(0, 30)
    Jump("loc_4FA")

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_4EE")
    Event(0, 31)
    Jump("loc_4FA")

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_4FA")
    Event(0, 32)

    label("loc_4FA")

    Return()

    # Function_1_334 end

    def Function_2_4FB(): pass

    label("Function_2_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_514")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_51A")

    label("loc_514")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_531")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_531")

    Return()

    # Function_2_4FB end

    def Function_3_532(): pass

    label("Function_3_532")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_543")
    Jump("loc_6E7")

    label("loc_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_551")
    Jump("loc_6E7")

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_55F")
    Jump("loc_6E7")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_612")

    #C0001
    ChrTalk(
        0x11,
        (
            "#06406F姐姐的样子从刚才开始\x01",
            "就有点怪怪的～\x02\x03",

            "#06402F在沙滩上发生了什么事吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00012F这、这个嘛……\x01",
            "这种事情，\x01",
            "我也不便说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x11,
        "#06405F？？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_642")

    label("loc_612")


    #C0004
    ChrTalk(
        0x11,
        (
            "#06406F姐姐的样子从刚才开始\x01",
            "就有点怪怪的～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_642")

    Jump("loc_6E7")

    label("loc_647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_6C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_662")
    Call(0, 5)
    Jump("loc_6BD")

    label("loc_662")


    #C0005
    ChrTalk(
        0x11,
        (
            "#06409F罗伊德警官，你买这条项链\x01",
            "送我好不好～\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#00006F不、不行啊，我根本就买不起。\x02",
    )

    CloseMessageWindow()

    label("loc_6BD")

    Jump("loc_6E7")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_6D0")
    Jump("loc_6E7")

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_6DE")
    Jump("loc_6E7")

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_6E7")

    label("loc_6E7")

    TalkEnd(0xFE)
    Return()

    # Function_3_532 end

    def Function_4_6EB(): pass

    label("Function_4_6EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_6FC")
    Jump("loc_9D8")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_70A")
    Jump("loc_9D8")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_718")
    Jump("loc_9D8")

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_893")

    #C0007
    ChrTalk(
        0x10,
        (
            "#10106F唉……虽然一开始就知道会有危险，\x01",
            "但没想到泳装真的会被划破……\x02\x03",

            "#10101F连那种程度的攻击都不能防范，\x01",
            "看来我仍然需要锻炼。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00006F……对、对不起，\x01",
            "要是我早些察觉到，\x01",
            "也许就不会搞成这样了……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x10,
        (
            "#10114F啊……没、没有的事！\x01",
            "我又没有受伤！\x02\x03",

            "#10103F虽、虽然有些难为情……\x01",
            "但我会以此为动力，继续努力的！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00012F（是、是指哪方面的……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_920")

    label("loc_893")


    #C0011
    ChrTalk(
        0x10,
        (
            "#10106F唉……连那种低级魔兽的\x01",
            "攻击都没能防范，\x01",
            "看来我还差得远啊。\x02\x03",

            "#10101F所以才会留下那么丢脸的回忆……\x01",
            "我一定要以此为动力，继续努力！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_920")

    Jump("loc_9D8")

    label("loc_925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_9A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_940")
    Call(0, 5)
    Jump("loc_9A0")

    label("loc_940")


    #C0012
    ChrTalk(
        0x10,
        (
            "#10106F这、这么贵的项链，\x01",
            "谁能买得起啊。\x02\x03",

            "#10101F这种价格……\x01",
            "简直都可以媲美国宝了吧……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A0")

    Jump("loc_9D8")

    label("loc_9A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9B3")
    Jump("loc_9D8")

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_9C1")
    Jump("loc_9D8")

    label("loc_9C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9CF")
    Jump("loc_9D8")

    label("loc_9CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_9D8")

    label("loc_9D8")

    TalkEnd(0xFE)
    Return()

    # Function_4_6EB end

    def Function_5_9DC(): pass

    label("Function_5_9DC")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0013
    ChrTalk(
        0x10,
        "#10109F哇～好漂亮的项链……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x11,
        (
            "#06402F据说是这里的镇店之宝呢～\x02\x03",

            "#06405F我看看价格……\x01",
            "……一个零、两个零、三个零……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)
    OP_64(0x11)

    #C0015
    ChrTalk(
        0x10,
        (
            "#10106F……买、买这一条项链的钱，\x01",
            "都够买好几辆导力车了……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x11,
        "#06406F果、果然离我们很遥远啊～\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_5_9DC end

    def Function_6_B08(): pass

    label("Function_6_B08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_B19")
    Jump("loc_F13")

    label("loc_B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B27")
    Jump("loc_F13")

    label("loc_B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_B35")
    Jump("loc_F13")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_DF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D87")

    #C0017
    ChrTalk(
        0xF,
        (
            "#00300F哦，罗伊德，\x01",
            "你已经找到阿琪了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x153,
        "#01109F嘿嘿，对不起，我不该到处乱跑。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xF,
        (
            "#00303F……嗯，原谅你了！\x01",
            "怎么可能不原谅嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……\x02\x03",

            "#00005F……啊，兰迪，\x01",
            "你在这里买东西了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xF,
        (
            "#00302F嗯，我准备送米蕾优\x01",
            "一件礼物。\x02\x03",

            "#00304F那家伙快要升职了，\x01",
            "就当作贺礼送她吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00005F嘿～原来如此……\x02\x03",

            "#00012F那个……兰迪，\x01",
            "莫非你对米蕾优准尉……？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xF,
        (
            "#00304F哈哈，你在\x01",
            "说什么傻话。\x02\x03",

            "#00300F我在警备队的时候经常受她关照，\x01",
            "送个礼物只是出于礼貌而已。\x02\x03",

            "#00309F再说了，我的第一目标可是\x01",
            "塞茜尔小姐哦！！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#00006F这种话……\x01",
            "我可不能当作没听见啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 1)
    Jump("loc_DEB")

    label("loc_D87")


    #C0025
    ChrTalk(
        0xF,
        (
            "#00300F我稍后会和诺艾尔她们\x01",
            "一起去集合地点。\x02\x03",

            "#00304F在她们逛完之前，\x01",
            "我就在这里随便看看好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEB")

    Jump("loc_F13")

    label("loc_DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9B")

    #C0026
    ChrTalk(
        0xF,
        (
            "#00301F嗯～项链吗……\x02\x03",

            "#00306F以那家伙的性格来说，\x01",
            "肯定会认为这种东西\x01",
            "在演习时很碍事。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00005F（兰迪好像在很认真的\x01",
            "  挑选礼物呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_EE9")

    label("loc_E9B")


    #C0028
    ChrTalk(
        0xF,
        (
            "#00303F还是选个不会碍事的\x01",
            "小东西比较好。\x02\x03",

            "#00300F过去看看对面的\x01",
            "胸针吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE9")

    Jump("loc_F13")

    label("loc_EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_EFC")
    Jump("loc_F13")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F0A")
    Jump("loc_F13")

    label("loc_F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_F13")

    label("loc_F13")

    TalkEnd(0xFE)
    Return()

    # Function_6_B08 end

    def Function_7_F17(): pass

    label("Function_7_F17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_F28")
    Jump("loc_FE6")

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_F36")
    Jump("loc_FE6")

    label("loc_F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_F44")
    Jump("loc_FE6")

    label("loc_F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_FB3")

    #C0029
    ChrTalk(
        0xE,
        (
            "#10305F……哦，这颗宝石和之前那位\x01",
            "夫人送我的很像呢。\x02\x03",

            "#10302F呵呵，难道她就是在这里买的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_FB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_FC1")
    Jump("loc_FE6")

    label("loc_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_FCF")
    Jump("loc_FE6")

    label("loc_FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_FDD")
    Jump("loc_FE6")

    label("loc_FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_FE6")

    label("loc_FE6")

    TalkEnd(0xFE)
    Return()

    # Function_7_F17 end

    def Function_8_FEA(): pass

    label("Function_8_FEA")

    Call(0, 9)
    Return()

    # Function_8_FEA end

    def Function_9_FEE(): pass

    label("Function_9_FEE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_122B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 7)), scpexpr(EXPR_END)), "loc_10D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1087")

    #C0030
    ChrTalk(
        0x8,
        (
            "呵呵呵……\x01",
            "感谢您的光顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "珠宝饰品是\x01",
            "包含了人生百感的\x01",
            "贵重礼物……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "愿女神保佑它们\x01",
            "受到主人的珍惜。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10CE")

    label("loc_1087")


    #C0033
    ChrTalk(
        0x8,
        "珠宝饰品是贵重的人生赠礼……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "愿女神保佑它们\x01",
            "受到主人的珍惜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CE")

    Jump("loc_1226")

    label("loc_10D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118E")

    #C0035
    ChrTalk(
        0x8,
        (
            "珠宝饰品是\x01",
            "包含了人生百感的\x01",
            "贵重礼物……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "至于能否抓住将其赠送出去的机会，\x01",
            "可就全看当事人的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "呵呵呵……\x01",
            "下次再度光临时，\x01",
            "请一定要做好充足的『准备』哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1226")

    label("loc_118E")


    #C0038
    ChrTalk(
        0x8,
        (
            "珠宝饰品正是贵重的人生赠礼……\x01",
            "至于能否抓住将其赠送出去的机会，\x01",
            "可就全看当事人的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "呵呵呵……\x01",
            "下次再度光临时，\x01",
            "请一定要做好充足『准备』哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1226")

    Jump("loc_147F")

    label("loc_122B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1301")

    #C0040
    ChrTalk(
        0x8,
        (
            "本店之所以采取会员制度，\x01",
            "是为了向信赖本店的各位熟客\x01",
            "提供最完美的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "如果客人增多，\x01",
            "服务质量必然就会随之降低。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "要想做好生意，\x01",
            "不能只是一味招揽客人。\x01",
            "呵呵呵，你明白了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_138D")

    label("loc_1301")


    #C0043
    ChrTalk(
        0x8,
        (
            "本店之所以采取会员制度，\x01",
            "是为了向信赖本店的各位熟客\x01",
            "提供最完美的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "要想做好生意，\x01",
            "不能只是一味招揽客人。\x01",
            "呵呵呵，你明白了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138D")

    Jump("loc_147F")

    label("loc_1392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_147F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141D")

    #C0045
    ChrTalk(
        0x8,
        (
            "呵呵呵……\x01",
            "欢迎光临\x01",
            "『亮饰』。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "本店只销售\x01",
            "最高级的珠宝饰品。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "不知您是否有资格\x01",
            "得到这永恒的光辉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_147F")

    label("loc_141D")


    #C0048
    ChrTalk(
        0x8,
        (
            "珠宝店『亮饰』\x01",
            "只销售最高级的\x01",
            "珠宝饰品。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "呵呵呵……\x01",
            "不知您是否有资格\x01",
            "得到这永恒的光辉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147F")

    TalkEnd(0x8)
    Return()

    # Function_9_FEE end

    def Function_10_1483(): pass

    label("Function_10_1483")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_14AF")

    #C0050
    ChrTalk(
        0x9,
        (
            "……期待您\x01",
            "再度光临。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176A")

    label("loc_14AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1659")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C0")

    #C0051
    ChrTalk(
        0x9,
        (
            "在那个陈列柜中，\x01",
            "展示着一条被称为\x01",
            "『圣女之泪』的项链。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "那条项链发掘于中世纪的遗迹，\x01",
            "是当时的克洛斯贝尔领主的所有物，\x01",
            "如今特别展示在此，供大家观赏。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "为了方便管理，本店给它标示了价格，\x01",
            "但那其实是一件非卖品。\x01",
            "慎重起见，特此向您说明。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1654")

    label("loc_15C0")


    #C0054
    ChrTalk(
        0x9,
        (
            "在那个陈列柜中，\x01",
            "展示着一条被称为\x01",
            "『圣女之泪』的项链。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "为了方便管理，本店给它标示了价格，\x01",
            "但那其实是一件非卖品。\x01",
            "慎重起见，特此向您说明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1654")

    Jump("loc_176A")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_176A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FC")

    #C0056
    ChrTalk(
        0x9,
        "之前实在是太失礼了。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "我们今后会把各位当作特别会员，\x01",
            "为大家提供最好的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "如果有什么需要，请不必客气，\x01",
            "随时向我们提出。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_176A")

    label("loc_16FC")


    #C0059
    ChrTalk(
        0x9,
        (
            "我们今后会把各位当作特别会员，\x01",
            "为大家提供最好的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "如果有什么需要，请不必客气，\x01",
            "随时向我们提出。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176A")

    TalkEnd(0xFE)
    Return()

    # Function_10_1483 end

    def Function_11_176E(): pass

    label("Function_11_176E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_177F")
    Jump("loc_18B7")

    label("loc_177F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_178D")
    Jump("loc_18B7")

    label("loc_178D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_18B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1857")

    #C0061
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔拥有一座可以开采出\x01",
            "大量七耀石的玛因兹矿山……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "因此，这家店销售的珠宝饰品，\x01",
            "尤其是用七耀石加工而成的珠宝，\x01",
            "全都是顶级品质。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        "嗯，真不愧是克洛斯贝尔啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_18B7")

    label("loc_1857")


    #C0064
    ChrTalk(
        0xA,
        (
            "在这家店里，陈列着大量的\x01",
            "高品质七耀石饰品。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "真不愧是坐拥玛因兹矿山的\x01",
            "克洛斯贝尔啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B7")

    TalkEnd(0xFE)
    Return()

    # Function_11_176E end

    def Function_12_18BB(): pass

    label("Function_12_18BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_18CC")
    Jump("loc_1927")

    label("loc_18CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_18DA")
    Jump("loc_1927")

    label("loc_18DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1927")

    #C0066
    ChrTalk(
        0xB,
        "呵呵，真没办法。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xB,
        (
            "为了让你开心，\x01",
            "买一两条项链\x01",
            "当然没问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1927")

    TalkEnd(0xFE)
    Return()

    # Function_12_18BB end

    def Function_13_192B(): pass

    label("Function_13_192B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_19EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_198C")

    #C0068
    ChrTalk(
        0xC,
        "呵呵，之前实在是抱歉了，\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "毕竟我们都已经\x01",
            "有自己的爱人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E7")

    label("loc_198C")


    #C0070
    ChrTalk(
        0xC,
        (
            "嗯，我最近经常\x01",
            "去帝国……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "但在那边也很少能见到\x01",
            "陈列着这么多优质珠宝\x01",
            "饰品的商店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E7")

    Jump("loc_1A3B")

    label("loc_19EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_19FA")
    Jump("loc_1A3B")

    label("loc_19FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1A3B")

    #C0072
    ChrTalk(
        0xC,
        (
            "这条项链\x01",
            "真不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "亲爱的，\x01",
            "买来送我好不好？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3B")

    TalkEnd(0xFE)
    Return()

    # Function_13_192B end

    def Function_14_1A3F(): pass

    label("Function_14_1A3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1AFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AAA")

    #C0074
    ChrTalk(
        0xD,
        "虽说适度玩火也很具诱惑力……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xD,
        (
            "但对淑女来说，\x01",
            "贞淑终究还是很重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF8")

    label("loc_1AAA")


    #C0076
    ChrTalk(
        0xD,
        (
            "呵呵，\x01",
            "确实如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xD,
        (
            "克洛斯贝尔出产的七耀石加工品\x01",
            "完全不输给其它国家。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF8")

    Jump("loc_1B90")

    label("loc_1AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1B87")

    #C0078
    ChrTalk(
        0xD,
        (
            "很难找到与我\x01",
            "相衬的珠宝饰品啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xD,
        (
            "不过，真正适合自己的宝石是很少的，\x01",
            "或许一生才能遇到一件，我还是耐下心来慢慢找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B90")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1B90")

    label("loc_1B90")

    TalkEnd(0xFE)
    Return()

    # Function_14_1A3F end

    def Function_15_1B94(): pass

    label("Function_15_1B94")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 0, -3000, 0)
    SetChrPos(0x104, 0, 0, -3000, 0)
    SetChrPos(0x105, 0, 0, -3000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(2140, 400, 4920, 0)
    MoveCamera(312, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25520, 0)
    FadeToBright(1000, 0)
    OP_68(-380, 400, 2640, 5000)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 18)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)
    OP_0D()

    #C0080
    ChrTalk(
        0x101,
        "#00005F这里是……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#6P#10300F记得是会员制的珠宝店。\x02\x03",

            "#10304F我以前和俱乐部的客人\x01",
            "一起来过几次。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_1D6D")

    #C0082
    ChrTalk(
        0x104,
        (
            "#6P#00306F我们上次来的时候，\x01",
            "在店门口就被拦住了。\x02\x03",

            "#00301F那个店员的态度\x01",
            "真让人有点不爽。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#11P#00000F是啊，但这次倒是\x01",
            "没有阻挡我们呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE0")

    label("loc_1D6D")


    #C0084
    ChrTalk(
        0x104,
        (
            "#6P#00306F就是拒绝陌生客人入内吧……\x01",
            "真让人不舒服。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#11P#00005F啊，如此说来，\x01",
            "我们擅自入内，恐怕不妥吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE0")

    OP_68(-3330, 400, 5840, 2500)
    OP_6F(0x1)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x87, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    #N0086
    NpcTalk(
        0x9,
        "店员",
        "各位客人。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 19)
    Sleep(50)
    OP_68(-2610, 600, 2290, 3000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(2000)

    def lambda_1E86():

        label("loc_1E86")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1E86")

    QueueWorkItem2(0x101, 2, lambda_1E86)

    def lambda_1E98():

        label("loc_1E98")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1E98")

    QueueWorkItem2(0x104, 2, lambda_1E98)

    def lambda_1EAA():

        label("loc_1EAA")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1EAA")

    QueueWorkItem2(0x105, 2, lambda_1EAA)
    WaitChrThread(0x9, 3)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x105, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_1EF8")

    #C0087
    ChrTalk(
        0x105,
        "#12P#10300F呵呵，一说就到啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F11")

    label("loc_1EF8")


    #C0088
    ChrTalk(
        0x101,
        "#12P#00011F糟糕……\x02",
    )

    CloseMessageWindow()

    label("loc_1F11")


    #C0089
    ChrTalk(
        0x9,
        (
            "#5P欢迎光临\x01",
            "珠宝店『亮饰』。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "#5P……不好意思，\x01",
            "请问各位持有哪位\x01",
            "贵宾的介绍信呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#12P#00005F这、这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x105,
        "#12P#10300F不好意思，我们并没有介绍信。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        "#5P很抱歉，那就请各位移步吧。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#5P本店采取会员制度，\x01",
            "只接待特定的客人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0095
    ChrTalk(
        0x104,
        (
            "#00306F啧，真没办法……\x01",
            "我们出去吧，罗伊德。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0096
    ChrTalk(
        0x101,
        (
            "#12P#00012F说的也是，我们\x01",
            "还要去沙滩等大家……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x9,
        "#5P罗伊德先生……？\x02",
    )

    CloseMessageWindow()

    def lambda_20B6():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_20B6)
    Sleep(50)

    def lambda_20C6():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_20C6)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    #C0098
    ChrTalk(
        0x9,
        (
            "#5P……各位客人，\x01",
            "莫非你们是\x01",
            "『特别任务支援科』的成员吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0099
    ChrTalk(
        0x101,
        "#12P#00005F嗯，是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0100
    ChrTalk(
        0x9,
        "#5P#4S万、万分抱歉！#3S\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        "#6P#00305F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "#5P咳、咳咳……\x01",
            "玛丽亚贝尔小姐\x01",
            "之前联系了我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "#5P她特地叮嘱我们，\x01",
            "今日要特别接待各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "#5P请原谅我刚才的无礼之举。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#12P#00000F啊，您的意思是……\x01",
            "我们也可以在这里买东西了？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "#5P是的，本店今后会把各位视作特别会员，\x01",
            "并提供最好的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "#5P如果有什么需要，\x01",
            "请随时吩咐。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 3)
    OP_4C(0x9, 0xFF)

    def lambda_2323():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2323)

    def lambda_2330():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2330)

    def lambda_233D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_233D)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_93(0x105, 0x13B, 0x1F4)

    #C0108
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，看来那位大小姐\x01",
            "已经帮我们把一切都安排好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#5P#00306F话说回来，那个店员的态度\x01",
            "未免转变得太快了吧。\x02\x03",

            "#00300F算了，既然已经得到资格了，\x01",
            "我们就在这里好好逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#11P#00012F哈哈，但这里的东西\x01",
            "好像都很贵，我们不一定买得起呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15B, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 800, 0)
    EventEnd(0x5)
    Return()

    # Function_15_1B94 end

    def Function_16_2475(): pass

    label("Function_16_2475")


    def lambda_247A():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_247A)

    def lambda_2494():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2494)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_24AD():
        OP_95(0xFE, 0, 0, 800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24AD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_2475 end

    def Function_17_24CE(): pass

    label("Function_17_24CE")


    def lambda_24D3():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24D3)

    def lambda_24ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_24ED)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2506():
        OP_95(0xFE, -790, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2506)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_24CE end

    def Function_18_2527(): pass

    label("Function_18_2527")


    def lambda_252C():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_252C)

    def lambda_2546():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2546)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_255F():
        OP_95(0xFE, 870, 0, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_255F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_2527 end

    def Function_19_2580(): pass

    label("Function_19_2580")


    def lambda_2585():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2585)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x0)

    def lambda_25AA():
        OP_95(0xFE, -3560, 0, 2870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25AA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_19_2580 end

    def Function_20_25CB(): pass

    label("Function_20_25CB")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_25D7():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25D7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x0)

    def lambda_25FC():
        OP_95(0xFE, -6300, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25FC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_20_25CB end

    def Function_21_261D(): pass

    label("Function_21_261D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x102, -200, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x102, 3, 0, 23)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)

    #C0111
    ChrTalk(
        0x102,
        (
            "#00105F这里就是珠宝店『亮饰』……\x02\x03",

            "#00104F果然陈列着很多\x01",
            "精美的珠宝饰品啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，你们白天去了时装店，\x01",
            "没来这里吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0113
    ChrTalk(
        0x101,
        (
            "#12P#00005F哎，话说回来……\x01",
            "艾莉，你不是这里的会员吗？\x02\x03",

            "#00000F你可是玛丽亚贝尔小姐的童年玩伴，\x01",
            "本以为肯定是这里的贵宾会员呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x102,
        (
            "#00106F哦，上次和贝尔一起来的时候，\x01",
            "我们没有进珠宝店。\x02\x03",

            "#00100F我还是更喜欢在\x01",
            "时装店挑衣服。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12P#00009F哈哈，原来如此。\x02\x03",

            "#00000F难得来一次，\x01",
            "我们就一起逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#00102F嗯，好啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4810, 1400, 4230, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 4100, 0, 4500, 270)
    SetChrPos(0x102, 4000, 0, 5500, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#00000F项链、戒指、胸针……\x02\x03",

            "#00003F珠宝饰品也分很多种呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#11P#00100F呵呵，是啊。\x01",
            "不过，好像全都是贵得\x01",
            "让人望而却步的高档品呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x102,
        (
            "#11P#00102F罗伊德，你看，\x01",
            "这枚戒指很漂亮吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#6P#00005F我看看……\x02\x03",

            "#00000F嗯，确实不错……\x01",
            "好像很适合你呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        (
            "#11P#00109F呵呵，不用说\x01",
            "这种客气话啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#6P#00012F才没有，真的很适合啊。\x02\x03",

            "#00003F（这价格……差不多是\x01",
            "  我三个月的薪水啊，\x01",
            "  果然很贵。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0123
    ChrTalk(
        0x101,
        "#6P#00011F（等等，这个专柜是……！）\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    BeginChrThread(0x9, 3, 0, 24)
    WaitChrThread(0x9, 3)

    #C0124
    ChrTalk(
        0x9,
        "二位客人，你们正在挑选订婚戒指吗？\x02",
    )

    CloseMessageWindow()

    def lambda_2B22():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2B22)
    Sleep(50)

    def lambda_2B32():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B32)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    #C0125
    ChrTalk(
        0x9,
        (
            "如果需要，\x01",
            "我可以为你们介绍一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0126
    ChrTalk(
        0x102,
        "#6P#00105F#4S哎……？#3S\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#6P#00012F哈哈，不是啦……这个……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "怎么？原来二位\x01",
            "并不是未婚夫妇吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "实在抱歉，我看你们一直\x01",
            "在看婚戒专柜，所以才会……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0130
    ChrTalk(
        0x102,
        (
            "#6P#00112F啊……！\x02\x03",

            "#00112F这、这……您、您误会了！\x01",
            "我们还没有发展到那种程度……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0131
    ChrTalk(
        0x102,
        (
            "#11P#00112F对、对吧！？罗伊德！\x02\x03",

            "#00113F我并不是想给你\x01",
            "什么暗示……！\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#00012F我、我知道，\x01",
            "不必那么慌张……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "……哦，言下之意，\x01",
            "二位的关系还会\x01",
            "继续发展下去啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0134
    ChrTalk(
        0x102,
        "#6P#00112F不、不是啦……！\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#6P#00012F（哈哈，看她那么\x01",
            "  拼命地解释，\x01",
            "  总有些莫名的失落感……）\x02\x03",

            "#00004F（……但仔细想想，\x01",
            "  平时总是依靠艾莉的帮助。）\x02\x03",

            "#00000F（结婚戒指什么的暂且不说，\x01",
            "  确实应该送她一件礼物呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0136
    ChrTalk(
        0x101,
        (
            "#12P#00000F（这枚翠耀石胸针……\x01",
            "  好像很适合艾莉。）\x02\x03",

            "#00003F（价格是……一万米拉，\x01",
            "  真是不便宜……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_33D2")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "购买胸针\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3295")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    #C0137
    ChrTalk(
        0x101,
        (
            "#6P#00000F不好意思，我要这枚胸针，\x01",
            "请帮我包一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        "哦……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0139
    ChrTalk(
        0x102,
        "#11P#00112F罗、罗伊德……！？\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#6P#00009F哈哈，毕竟总是\x01",
            "受你关照嘛。\x02\x03",

            "#00000F并没有什么特别的意思，\x01",
            "可以收下这份礼物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            "#11P#00113F（可、可你这样说，\x01",
            "  就已经让人觉得\x01",
            "  很有特别含义了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#6P#00005F你、你果然还是……\x01",
            "不想收我送的礼物吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0143
    ChrTalk(
        0x102,
        (
            "#11P#00112F怎、怎么会，才不是不想收……\x02\x03",

            "#00104F……咳咳。\x01",
            "谢谢，罗伊德，我很高兴哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0144
    ChrTalk(
        0x102,
        (
            "#11P#00100F那么，作为回礼……\x01",
            "我也给你挑一件\x01",
            "适合你的饰品吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#6P#00005F哎，这样好吗？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#11P#00100F呵呵，难得来一次嘛。\x02\x03",

            "#00109F那我这就去挑选，\x01",
            "请稍等一下哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德和艾莉请店员\x01",
            "把自己买下的饰品包好，\x01",
            "并彼此交换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x398),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x398, 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_33CD")

    label("loc_3295")


    #C0149
    ChrTalk(
        0x101,
        (
            "#6P#00006F（……现在送的话，意义太复杂了，\x01",
            "  这次还是算了吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#6P#00112F……总、总之，我们还\x01",
            "不是情侣呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        "呼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0152
    ChrTalk(
        0x102,
        (
            "#11P#00113F喂，罗伊德！\x01",
            "你也来解释几句啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0153
    ChrTalk(
        0x101,
        "#6P#00012F好、好的……我知道了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德与艾莉\x01",
            "在略显尴尬的气氛下\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_33CD")

    Jump("loc_352E")

    label("loc_33D2")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0155
    ChrTalk(
        0x101,
        (
            "#12P#00006F（……唔，身上的钱根本不够，\x01",
            "  虽然很遗憾，但也只能放弃了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        (
            "#6P#00112F……总、总之，我们还\x01",
            "不是情侣呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        "呼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0158
    ChrTalk(
        0x102,
        (
            "#11P#00113F喂，罗伊德！\x01",
            "你也来解释几句啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0159
    ChrTalk(
        0x101,
        "#6P#00012F好、好的……我知道了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德与艾莉\x01",
            "在略显尴尬的气氛下\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_352E")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_261D end

    def Function_22_353E(): pass

    label("Function_22_353E")


    def lambda_3543():
        OP_95(0xFE, 800, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3543)

    def lambda_355D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_355D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3576():
        OP_95(0xFE, 800, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3576)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_353E end

    def Function_23_3590(): pass

    label("Function_23_3590")


    def lambda_3595():
        OP_95(0xFE, -200, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3595)

    def lambda_35AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35AF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)

    def lambda_35FA():
        OP_95(0xFE, -200, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35FA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_3590 end

    def Function_24_3614(): pass

    label("Function_24_3614")


    def lambda_3619():
        OP_95(0xFE, 4120, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3619)

    def lambda_3633():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3633)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_3653():
        OP_95(0xFE, 4120, 0, 7340, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3653)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_3614 end

    def Function_25_366D(): pass

    label("Function_25_366D")


    def lambda_3672():
        OP_95(0xFE, -500, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3672)

    def lambda_368C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_368C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_36A5():
        OP_95(0xFE, -500, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36A5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_366D end

    def Function_26_36BF(): pass

    label("Function_26_36BF")

    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_36CB():
        OP_95(0xFE, 650, 0, 8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36CB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_36F0():
        OP_95(0xFE, 650, 0, 6000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36F0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_36BF end

    def Function_27_370A(): pass

    label("Function_27_370A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3735")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Jump("Function_27_370A")

    label("loc_3735")

    Return()

    # Function_27_370A end

    def Function_28_3736(): pass

    label("Function_28_3736")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_3742():
        OP_95(0xFE, -3800, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3742)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_3767():
        OP_95(0xFE, -3800, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3767)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_3736 end

    def Function_29_3781(): pass

    label("Function_29_3781")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x103, -200, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x103, 3, 0, 23)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x103, 3)

    #C0161
    ChrTalk(
        0x103,
        (
            "#00205F这里就是珠宝店啊……\x02\x03",

            "#00202F罗伊德前辈，\x01",
            "我可以四处看看吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#12P#00000F好啊，\x01",
            "反正还有时间。\x02\x03",

            "#00012F话说回来……\x01",
            "你这么想来这里逛啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#00203F是、是的……\x01",
            "因为我听说这里有\x01",
            "很多漂亮的饰品。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00009F哈哈，原来如此。\x02\x03",

            "#00000F那我们就一起看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        "#00209F……好的！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(70, 1400, 8900, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 500, 0, 8900, 0)
    SetChrPos(0x103, -500, 0, 9000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0166
    ChrTalk(
        0x101,
        (
            "#12P#00005F这条项链\x01",
            "好漂亮啊。\x02\x03",

            "#00004F中世纪时代的珠宝吗……\x01",
            "能隐隐感受到历史气息呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        "#6P#00205F………………………………\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#12P#00005F……怎么了？缇欧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x103,
        (
            "#00205F……啊，没、没什么。\x02\x03",

            "#00204F这条项链实在太漂亮了，\x01",
            "让我一时不知该说些什么……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0170
    ChrTalk(
        0x101,
        "#12P#00005F………………………………\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#00205F……怎么了？\x01",
            "你的眼睛瞪得好大。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#12P#00012F没、没什么……\x01",
            "只是觉得有点意外。\x02\x03",

            "#00003F其实我刚才就在想，\x01",
            "缇欧竟然会对这种\x01",
            "世俗之物感兴趣……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        (
            "#00211F我、我当然也会喜欢\x01",
            "这种漂亮的东西啊。\x02\x03",

            "#00204F……不过，会有这种想法，\x01",
            "大概也是因为受了罗伊德前辈你们的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#12P#00005F啊……\x02\x03",

            "#00004F（仔细想想……虽说在初次相遇时\x01",
            "  就给我们留下了很成熟的印象……）\x02\x03",

            "（但缇欧毕竟还是个\x01",
            "  花季少女啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        "#00205F……罗伊德前辈？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#12P#00002F哦，没什么。\x02\x03",

            "#00004F（嗯……倒也不是为了\x01",
            "  讨她的欢心……）\x02\x03",

            "（但趁此机会送缇欧一件礼物\x01",
            "  也不错。）\x02\x03",

            "#00000F（她会喜欢什么呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x101,
        (
            "#5P#00000F（哦，这个苍耀石发饰……\x01",
            "  好像很适合缇欧啊。）\x02\x03",

            "#00003F（价格是……一万米拉，\x01",
            "  真是不便宜……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_43DD")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "购买发饰\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E7")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    #C0178
    ChrTalk(
        0x101,
        (
            "#12P#00000F缇欧，我送你那个\x01",
            "发饰当礼物吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Sleep(1000)
    OP_64(0x103)

    #C0179
    ChrTalk(
        0x103,
        "#00205F哎……？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#12P#00012F哈哈，虽然我实在是\x01",
            "买不起那条\x01",
            "贵重的项链……\x02\x03",

            "#00000F但我很希望缇欧像普通女孩一样，\x01",
            "打扮得漂漂亮亮。\x02\x03",

            "当然了，这并不包含什么\x01",
            "特殊含义……可以收下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0181
    ChrTalk(
        0x103,
        (
            "#00204F……嗯，我很高兴。\x02\x03",

            "#00200F但有件事情\x01",
            "不得不指出。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0182
    ChrTalk(
        0x103,
        (
            "#00203F『当然了，这并不包含什么特殊含义』……\x02\x03",

            "#00211F和女性说这种话，\x01",
            "是不是有些失礼呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#12P#00005F哎，是、是吗？\x02\x03",

            "#00002F我的意思只是……你把它当作\x01",
            "哥哥送给妹妹的礼物就可以了……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#00206F……唉。\x02\x03",

            "#00211F算了，这次就\x01",
            "不和你计较了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0185
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯……？\x01",
            "你好像不太愿意接受啊。\x02\x03",

            "#00012F看来还是不该选发饰，\x01",
            "也许送咪西的周边更好吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0186
    ChrTalk(
        0x103,
        (
            "#00206F（这个人实在是……）\x02\x03",

            "#00202F……哦，对了。\x01",
            "如果可以，我也想送\x01",
            "罗伊德前辈一份礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        "#12P#00005F哎，这样好吗？\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        (
            "#00202F是的，毕竟难得来一趟。\x02\x03",

            "#00204F我这就去挑个合适的礼物，\x01",
            "请稍等一会。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德和缇欧请店员\x01",
            "把自己买下的饰品包好，\x01",
            "并彼此交换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0190
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x399),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x399, 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_43D8")

    label("loc_42E7")


    #C0191
    ChrTalk(
        0x101,
        (
            "#5P#00006F（……还是算了吧，\x01",
            "  说不定会让她困惑……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0192
    ChrTalk(
        0x103,
        (
            "#00202F……罗伊德前辈，\x01",
            "再去看看那边的饰品吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0193
    ChrTalk(
        0x101,
        (
            "#12P#00012F哦，好啊，\x01",
            "我会陪你看个够的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和缇欧\x01",
            "继续逛了一阵后，\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_43D8")

    Jump("loc_44FD")

    label("loc_43DD")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0195
    ChrTalk(
        0x101,
        (
            "#5P#00006F（……唔，身上的钱根本不够，\x01",
            "  虽然很遗憾，但也只能放弃了……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0196
    ChrTalk(
        0x103,
        (
            "#00202F……罗伊德前辈，\x01",
            "再去看看那边的饰品吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0197
    ChrTalk(
        0x101,
        (
            "#12P#00012F哦，好啊，\x01",
            "我会陪你看个够的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和缇欧\x01",
            "继续逛了一阵后，\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_44FD")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3781 end

    def Function_30_450D(): pass

    label("Function_30_450D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x104, -500, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x104, 3, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)

    #C0199
    ChrTalk(
        0x101,
        "#12P#00000F我们到珠宝店了。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        (
            "#00300F好～那就马上\x01",
            "陪你挑选一份\x01",
            "礼物吧。\x02\x03",

            "#00309F对了，你的目标是谁啊？\x01",
            "赶快告诉哥哥吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#12P#00012F哪、哪有什么目标，\x01",
            "我都说过不是为了买礼物才来的了。\x02\x03",

            "#00000F总之，离集合还有些时间，\x01",
            "我们就在店内随便逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        "#00302F嗯，知道啦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(5520, 1400, 8900, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24620, 0)
    SetChrPos(0x101, 5350, 0, 9700, 270)
    SetChrPos(0x104, 4150, 0, 9700, 90)
    SetChrPos(0x9, -900, 0, 9680, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0203
    ChrTalk(
        0x101,
        (
            "#12P#00001F该怎么说呢……\x02\x03",

            "#00006F越看越觉得这种店\x01",
            "很不适合两个大男人\x01",
            "在晚上一起逛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        (
            "#00306F喂喂，你要这么说的话，\x01",
            "那我大白天一个人跑来逛\x01",
            "又算什么啊？\x02\x03",

            "#00300F不过，我也同意你的说法。\x01",
            "与其来这里，还不如到主题公园\x01",
            "找大姐姐搭讪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#12P#00011F我、我们可没有那么多时间啊。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        (
            "#00306F话说回来，我们在水上巴士上\x01",
            "不是约好要去一起搭讪的吗～\x02\x03",

            "#00301F你小子可真是的，该说是太过纯良吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0207
    ChrTalk(
        0x104,
        (
            "#00302F好吧，难得来一趟，\x01",
            "我就挑个可以让你更有\x01",
            "男人味的饰品送给你吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#12P#00005F哎……这、这样好吗？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        (
            "#00300F嗯，别客气，\x01",
            "我刚才正好在对面那个橱窗里\x01",
            "发现了一件挺适合你的东西。\x02\x03",

            "#00309F哈哈，送给你挺好玩的，\x01",
            "你就不要往心里去啦。\x02\x03",

            "#00304F当然了，我也没有什么\x01",
            "特别的意思。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0210
    ChrTalk(
        0x101,
        (
            "#12P#00006F这……\x01",
            "如果真有，那可就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x104,
        (
            "#00302F哈哈，开个玩笑啦。\x02\x03",

            "#00304F那我这就去让店员\x01",
            "给我包起来。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4210, 1400, 7590, 2000)
    OP_6F(0x79)
    TurnDirection(0x104, 0xC, 500)

    #C0212
    ChrTalk(
        0x104,
        (
            "#11P#00309F顺便和那边那两位\x01",
            "名流大姐姐定下\x01",
            "今晚的约会！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 2, 0, 27)
    BeginChrThread(0x104, 3, 0, 26)

    def lambda_4AE2():

        label("loc_4AE2")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_4AE2")

    QueueWorkItem2(0x101, 2, lambda_4AE2)
    WaitChrThread(0x104, 3)
    EndChrThread(0x104, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    def lambda_4B04():
        TurnDirection(0xC, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4B04)
    TurnDirection(0xD, 0x104, 500)
    EndChrThread(0x101, 0xFF)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0213
    ChrTalk(
        0x101,
        (
            "#12P#00012F哈哈，真是的……\x02\x03",

            "#00004F（说起来，兰迪真是很体贴，\x01",
            "  我们大家都经常受他照顾。）\x02\x03",

            "（我作为支援科的队长，\x01",
            "  也应该表达一下自己的谢意……）\x02\x03",

            "#00000F（难得来到珠宝店，\x01",
            "  我也挑件礼物送他好了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x101,
        (
            "#5P#00000F（这个镶有红耀石的手镯……\x01",
            "  好像挺适合兰迪呢。）\x02\x03",

            "#00003F（价格是……一万米拉，\x01",
            "  真是不便宜……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4F24")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "购买手镯\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1A")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    #C0215
    ChrTalk(
        0x101,
        (
            "#12P#00000F你好，打扰一下，\x01",
            "我想买这个手镯……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4B(0x9, 0xFF)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    #C0216
    ChrTalk(
        0x9,
        "#5P好的，我这就来。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德开着玩笑，不断安慰\x01",
            "因搭讪失败而垂头丧气的兰迪……\x02\x03",

            "二人请店员包好了自己买下的饰品，\x01",
            "并彼此交换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_4F1F")

    label("loc_4E1A")


    #C0218
    ChrTalk(
        0x101,
        (
            "#5P#00006F（……总觉得有点不好意思，\x01",
            "  还是算了吧。）\x02\x03",

            "#00000F（等以后有机会时，再用其它方式\x01",
            "  来表达对兰迪的感谢之情吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德开着玩笑，不断安慰\x01",
            "因搭讪失败而垂头丧气的兰迪……\x02\x03",

            "并收下兰迪送给他的珠宝饰品，\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4F1F")

    Jump("loc_5029")

    label("loc_4F24")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0220
    ChrTalk(
        0x101,
        (
            "#5P#00006F（……唔，身上的钱根本不够啊。）\x02\x03",

            "#00008F（虽然很抱歉，\x01",
            "  但也只能放弃送他礼物了……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德开着玩笑，不断安慰\x01",
            "因搭讪失败而垂头丧气的兰迪……\x02\x03",

            "并收下兰迪送给他的珠宝饰品，\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5029")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x39A, 1)
    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_450D end

    def Function_31_506E(): pass

    label("Function_31_506E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x109, -200, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x109, 3, 0, 23)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x109, 3)

    #C0223
    ChrTalk(
        0x109,
        (
            "#10108F唔，我白天就和\x01",
            "芙兰来这里逛过了……\x02\x03",

            "#10106F唉，还是觉得自己\x01",
            "很不适合来这种高档店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#12P#00012F要不是玛丽亚贝尔小姐\x01",
            "事先打过招呼，我们根本就\x01",
            "不能进这家店。\x02\x03",

            "#00000F不过，难得来一趟，\x01",
            "这次就陪我随便看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x109,
        "#10100F好的，我很乐意！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6510, 1400, 6990, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 6000, 0, 8500, 90)
    SetChrPos(0x109, 6000, 0, 7200, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0226
    ChrTalk(
        0x109,
        "#5P#10103F唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    #C0227
    ChrTalk(
        0x101,
        "#00005F怎么了？诺艾尔。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0228
    ChrTalk(
        0x109,
        (
            "#6P#10101F没什么，只是看了这么多饰品之后，\x01",
            "我突然产生了一种想法……\x02\x03",

            "#10106F珠宝饰品这种东西\x01",
            "实在是很多余吧？\x02\x03",

            "#10108F戴上这种东西之后，\x01",
            "不仅行动不便，\x01",
            "还会对工作造成妨碍……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    #C0229
    ChrTalk(
        0x109,
        (
            "#6P#10111F啊！对、对不起！\x01",
            "难得你这么有兴致，我却说些扫兴话……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#00012F哈哈……不用介意，\x01",
            "这种看法还真符合诺艾尔的作风啊。\x02\x03",

            "#00000F说起来，你的便服\x01",
            "也都很便于行动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        (
            "#6P#10109F哈哈……\x01",
            "挑选便服的时候，\x01",
            "我非常重视这一点。\x02\x03",

            "#10106F在一个人挑选衣服的时候，\x01",
            "总会配出一身很男性化的服装，\x01",
            "这让我很苦恼。\x02\x03",

            "#10100F所以我总是让芙兰\x01",
            "帮我搭配服装……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，原来如此。\x02\x03",

            "#00000F既然如此，这家店里\x01",
            "恐怕不会有你中意的东西吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x109,
        "#6P#10100F我看看……\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x109, 0x87, 0x1F4)
    Sleep(500)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0234
    ChrTalk(
        0x109,
        (
            "#5P#10102F啊，这条镶有\x01",
            "琥耀石的项链……\x02\x03",

            "#10109F白天和芙兰一起看到的时候，\x01",
            "我就觉得\x01",
            "挺不错的。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#00002F哈哈，确实很适合诺艾尔呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0236
    ChrTalk(
        0x101,
        (
            "#00000F（嗯……难得一起来这里，\x01",
            "  不如买下送她好了。）\x02\x03",

            "#00003F（价格是……一万米拉，\x01",
            "  真是不便宜……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5C15")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "购买项链\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AE8")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0237
    ChrTalk(
        0x101,
        (
            "#00000F诺艾尔，这条项链……\x01",
            "我就送你当礼物吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0238
    ChrTalk(
        0x109,
        "#6P#10105F咦…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0239
    ChrTalk(
        0x109,
        "#6P#10111F咦咦咦咦咦咦咦！？\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00005F啊，难道让你觉得为难吗？\x02\x03",

            "#00004F我只是觉得，你来支援科以后一直都\x01",
            "工作得那么努力，所以想慰劳你一下，\x01",
            "并没有什么特别的意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        (
            "#6P#10111F这、这个……该怎么说呢！！\x01",
            "要问我高不高兴，那当然是高兴的……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        "#00005F那、那还有什么问题吗？\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x109,
        (
            "#6P#10112F……没、没有啦！！\x01",
            "并没有什么问题……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    #C0244
    ChrTalk(
        0x109,
        (
            "#6P#10101F……那、那么！\x01",
            "既然你如此费心，\x01",
            "那我就却之不恭了！\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        "#00012F哈哈，你不必这么紧张啊……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x109,
        (
            "#6P#10106F这、这个……\x01",
            "但还是有些不好意思。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x109,
        (
            "#6P#10103F对了，既然如此……\x02\x03",

            "#10100F我也送罗伊德警官\x01",
            "一件礼物好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        "#00005F咦，这样好吗？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x109,
        (
            "#6P#10109F当然了，难得来一趟。\x02\x03",

            "#10100F我这就去挑个合适的礼物，\x01",
            "请稍微等我一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德和诺艾尔请店员\x01",
            "把自己买下的饰品包好，\x01",
            "并彼此交换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x39B, 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_5C10")

    label("loc_5AE8")


    #C0252
    ChrTalk(
        0x101,
        (
            "#00006F（……唔，还是算了吧，\x01",
            "  说不定会让芙兰他们产生误会……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0253
    ChrTalk(
        0x109,
        "#6P#10105F罗伊德警官，你怎么了？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00004F啊，没什么，没什么。\x02\x03",

            "#00000F我们再逛一阵，\x01",
            "看看有没有别的中意之物吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        "#6P#10102F嗯，好的！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和诺艾尔\x01",
            "继续逛了一阵后，\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5C10")

    Jump("loc_5D5E")

    label("loc_5C15")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x101,
        (
            "#00006F（……唔，身上的钱根本不够，\x01",
            "  虽然很遗憾，但也只能放弃了……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0258
    ChrTalk(
        0x109,
        "#6P#10105F罗伊德警官，你怎么了？\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#00004F啊，没什么，没什么。\x02\x03",

            "#00000F我们再逛一阵，\x01",
            "看看有没有别的中意之物吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x109,
        "#6P#10102F嗯，好的！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0261
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和诺艾尔\x01",
            "继续逛了一阵后，\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5D5E")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_506E end

    def Function_32_5D6E(): pass

    label("Function_32_5D6E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x105, -500, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x105, 3, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)

    #C0262
    ChrTalk(
        0x101,
        "#12P#00000F我们到珠宝店了。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x105,
        (
            "#10300F距离晚餐会开始还有些时间，\x01",
            "要不要一起逛逛呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#12P#00002F好啊，难得来一趟，\x01",
            "就随便看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，那我们就在\x01",
            "店里逛一圈吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6510, 1400, 6990, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 6000, 0, 8100, 90)
    SetChrPos(0x105, 6000, 0, 6900, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0266
    ChrTalk(
        0x101,
        (
            "#00003F唔，真不愧是会员制的商店，\x01",
            "卖的都是些高价货啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，机会难得，\x01",
            "买个戒指送给\x01",
            "琪雅好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0268
    ChrTalk(
        0x101,
        (
            "#00006F喂喂，那可不是\x01",
            "适合送给小孩子的东西啊。\x02\x03",

            "#00005F……对了，瓦吉，\x01",
            "你在加入支援科之前\x01",
            "就已经很有钱了吧？\x02\x03",

            "#00003F在我们初次相遇时，\x01",
            "你就拥有战术导力器这种稀有物……\x02\x03",

            "#00000F请容我冒昧一问，\x01",
            "你在男公关俱乐部\x01",
            "肯定能赚到不少钱吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0269
    ChrTalk(
        0x105,
        (
            "#6P#10300F没有啦，我毕竟是兼职，\x01",
            "只是偶尔过去帮个忙而已，\x01",
            "实际上并没有拿到多少薪水。\x02\x03",

            "#10304F相比固定薪水，在俱乐部的主要收益\x01",
            "还是客人赠礼之类的额外收入。\x02\x03",

            "#10302F偶尔还会有些\x01",
            "名流夫人送我宝石\x01",
            "当小费呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#00003F……原、原来如此。\x01",
            "虽然我不太赞同这种工作，\x01",
            "但这是你的主要资金来源吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，不不不，\x01",
            "我可不会把客人送我的礼物\x01",
            "拿去换钱哦。\x02\x03",

            "#10304F以前用的那部艾尼格玛，\x01",
            "也是我用自己的钱在\x01",
            "亚修莉女士的店里买的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0272
    ChrTalk(
        0x101,
        (
            "#00005F……那问题就回到原点了，\x01",
            "你的钱到底是从哪里来的？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x105,
        "#6P#10309F呵呵，那可是我的商业秘密。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0274
    ChrTalk(
        0x101,
        "#00006F这、这算什么回答啊……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，好啦，这种无关紧要的\x01",
            "小事就先放到一边……\x02\x03",

            "#10302F罗伊德，你可以\x01",
            "收下这个吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0276
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0277
    ChrTalk(
        0x101,
        "#00005F这是……\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x105,
        (
            "#6P#10300F这是我刚才在\x01",
            "对面的展示柜\x01",
            "看中的饰品。\x02\x03",

            "#10304F感觉很适合你，再加上机会难得，\x01",
            "就买下来送你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#00006F什、什么时候买的……\x02\x03",

            "#00005F看起来好像很贵呢，\x01",
            "我真的可以收下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，我只是一时兴起而已，\x01",
            "你不必想太多。\x02\x03",

            "#10309F而且，用这种东西就能让你欠我\x01",
            "一个人情，真是相当便宜了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x101,
        (
            "#00006F喂喂……\x02\x03",

            "#00000F不管怎么说，真是谢谢你了，\x01",
            "那我就收下啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x105,
        "#6P#10300F呵呵，不用客气。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x101,
        (
            "#00000F（……对了，总不能\x01",
            "　就只收人家的礼物……）\x02\x03",

            "#00004F（不如也回送他\x01",
            "  点什么吧。）\x02\x03",

            "#00000F（自从瓦吉加入之后，我们支援科\x01",
            "  在处理工作时的灵活性比以前更强了，\x01",
            "　也该送给他一份谢礼……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0284
    ChrTalk(
        0x101,
        (
            "#00000F（这个金耀石吊坠\x01",
            "  好像很适合瓦吉。）\x02\x03",

            "#00003F（价格是……一万米拉，\x01",
            "  真是不便宜……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6A3E")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "购买吊坠\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6931")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0285
    ChrTalk(
        0x101,
        (
            "#00000F既然如此，那我就把\x01",
            "这个吊坠当作回礼送你吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x2D, 0x1F4)

    #C0286
    ChrTalk(
        0x105,
        (
            "#6P#10305F哦？这样好吗？\x02\x03",

            "#10300F呵呵，你的品位\x01",
            "还真不错呢。\x02\x03",

            "#10302F作为一件礼物，未免有些廉价，\x01",
            "不过，也算是勉强及格了。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#00006F我说你啊……\x01",
            "如果不要，那我就不买了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x105,
        (
            "#6P#10309F啊哈哈，怎么会呢。\x02\x03",

            "#10302F这可是你用心为我挑选的礼物，\x01",
            "我会心存感激地收下的。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#00002F……哈哈，好吧，\x01",
            "那我这就去叫店员过来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随后，罗伊德请店员\x01",
            "包好了自己买下的饰品，\x01",
            "并送给了瓦吉。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_6A39")

    label("loc_6931")


    #C0291
    ChrTalk(
        0x101,
        (
            "#00006F（……这次还是算了，\x01",
            "　等以后有机会时再回礼吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x105,
        "#6P#10305F嗯？怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0293
    ChrTalk(
        0x101,
        (
            "#00004F哦，没什么。\x02\x03",

            "#00000F还有些时间，\x01",
            "我们继续在店里逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        "#6P#10302F呵呵，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和瓦吉\x01",
            "继续逛了一阵后，\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6A39")

    Jump("loc_6B6F")

    label("loc_6A3E")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0296
    ChrTalk(
        0x101,
        (
            "#00006F（……唔，身上的钱根本不够，\x01",
            "  虽然很遗憾，但也只能放弃了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        "#6P#10305F嗯？怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0298
    ChrTalk(
        0x101,
        (
            "#00004F哦，没什么。\x02\x03",

            "#00000F还有些时间，\x01",
            "我们继续在店里逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x105,
        "#6P#10302F呵呵，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和瓦吉\x01",
            "继续逛了一阵后，\x01",
            "离开了珠宝店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6B6F")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_5D6E end

    SaveToFile()

Try(main)
