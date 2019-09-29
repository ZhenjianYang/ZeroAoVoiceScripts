from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1010.bin",                # FileName
        "c1010",                    # MapName
        "c1010",                    # Location
        0x0013,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 19, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1010",                  # 0
        "接待员米歇尔",           # 1
        "亚里欧斯",               # 2
        "亚里欧斯",               # 3
        "艾丝蒂尔",               # 4
        "艾丝蒂尔",               # 5
        "约修亚",                 # 6
        "约修亚",                 # 7
        "游击士斯克特",           # 8
        "游击士斯克特",           # 9
        "游击士温蔡尔",           # 10
        "游击士林",               # 11
        "游击士艾欧莉娅",         # 12
        "滴",                     # 13
    ))

    AddCharChip((
        "chr/ch09100.itc",                   # 00
        "chr/ch02400.itc",                   # 01
        "chr/ch00600.itc",                   # 02
        "chr/ch00700.itc",                   # 03
        "chr/ch27200.itc",                   # 04
        "chr/ch27300.itc",                   # 05
        "chr/ch32100.itc",                   # 06
        "chr/ch02402.itc",                   # 07
        "chr/ch00602.itc",                   # 08
        "chr/ch00702.itc",                   # 09
        "chr/ch27202.itc",                   # 0A
        "chr/ch32002.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch27302.itc",                   # 0D
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

    DeclNpc(1000,    0,       12819,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(970,     0,       10300,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-5900,   150,     49279,   180,  469,  0x0, 0,   7,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(1559,    0,       10220,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5900,   150,     49279,   180,  469,  0x0, 0,   8,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(180,     0,       9859,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-8430,   150,     49189,   180,  469,  0x0, 0,   9,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-4780,   0,       52229,   315,  389,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-8329,   119,     47119,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-6320,   0,       52229,   45,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-6000,   100,     47130,   0,    469,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-5099,   0,       51909,   270,  405,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(5500,    0,       6000,    1200,    5500,    1500,    6000,    0x007C, 0,  16, 0x0000)
    DeclActor(8000,    0,       6000,    1200,    8000,    1500,    6000,    0x007C, 0,  37, 0x0000)
    DeclActor(5500,    0,       2500,    1200,    5500,    1500,    2500,    0x007C, 0,  37, 0x0000)
    DeclActor(8000,    0,       2500,    1200,    8000,    1500,    2500,    0x007C, 0,  37, 0x0000)
    DeclActor(680,     0,       11370,   1700,    1000,    1500,    12820,   0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_3C4",          # 00, 0
        "Function_1_47C",          # 01, 1
        "Function_2_72E",          # 02, 2
        "Function_3_792",          # 03, 3
        "Function_4_796",          # 04, 4
        "Function_5_2729",         # 05, 5
        "Function_6_2C40",         # 06, 6
        "Function_7_3587",         # 07, 7
        "Function_8_35FD",         # 08, 8
        "Function_9_395A",         # 09, 9
        "Function_10_3A66",        # 0A, 10
        "Function_11_3E6F",        # 0B, 11
        "Function_12_406D",        # 0C, 12
        "Function_13_44A6",        # 0D, 13
        "Function_14_49AA",        # 0E, 14
        "Function_15_5024",        # 0F, 15
        "Function_16_53DC",        # 10, 16
        "Function_17_62A4",        # 11, 17
        "Function_18_6664",        # 12, 18
        "Function_19_6945",        # 13, 19
        "Function_20_6EB9",        # 14, 20
        "Function_21_74A1",        # 15, 21
        "Function_22_7EDA",        # 16, 22
        "Function_23_8682",        # 17, 23
        "Function_24_883A",        # 18, 24
        "Function_25_8912",        # 19, 25
        "Function_26_D3B7",        # 1A, 26
        "Function_27_DB87",        # 1B, 27
        "Function_28_E98E",        # 1C, 28
        "Function_29_E9D9",        # 1D, 29
        "Function_30_EA34",        # 1E, 30
        "Function_31_EA8F",        # 1F, 31
        "Function_32_1167D",       # 20, 32
        "Function_33_116A3",       # 21, 33
        "Function_34_1351D",       # 22, 34
        "Function_35_13572",       # 23, 35
        "Function_36_135E8",       # 24, 36
        "Function_37_13640",       # 25, 37
    ))


    def Function_0_3C4(): pass

    label("Function_0_3C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_404"),
        (1, "loc_410"),
        (2, "loc_41C"),
        (3, "loc_428"),
        (4, "loc_434"),
        (5, "loc_440"),
        (6, "loc_44C"),
        (SWITCH_DEFAULT, "loc_458"),
    )


    label("loc_404")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_410")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_41C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_428")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_434")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_440")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_44C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_458")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_464")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_47B")

    Return()

    # Function_0_3C4 end

    def Function_1_47C(): pass

    label("Function_1_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_48A")
    Jump("loc_6DE")

    label("loc_48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_498")
    Jump("loc_6DE")

    label("loc_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4AB")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6DE")

    label("loc_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_501")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, -6640, 0, 51900, 90)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC")
    SetChrFlags(0x8, 0x10)

    label("loc_4FC")

    Jump("loc_6DE")

    label("loc_501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_50F")
    Jump("loc_6DE")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_549")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -8400, 150, 49200, 180)
    SetChrPos(0xE, -10700, 150, 49200, 180)
    Jump("loc_6DE")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_583")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, 2220, 0, 4610, 90)
    SetChrPos(0x11, 3840, 0, 4540, 270)
    Jump("loc_6DE")

    label("loc_583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D8")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xD)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -5880, 50, 47090, 0)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -5960, 150, 49360, 180)
    Jump("loc_6DE")

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_601")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 600, 0, 39580, 90)
    SetChrFlags(0x9, 0x10)
    Jump("loc_6DE")

    label("loc_601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_614")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6DE")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_63A")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_END)), "loc_635")
    SetChrFlags(0x8, 0x10)

    label("loc_635")

    Jump("loc_6DE")

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_679")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5930, 150, 43070, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x13, -4610, 0, 43390, 225)
    Jump("loc_6DE")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_68C")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6DE")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6CB")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5930, 150, 43070, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x13, -4610, 0, 43390, 225)
    Jump("loc_6DE")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6DE")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F4")
    SetMapFlags(0x10000000)
    Event(0, 31)

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_708")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 27)
    Jump("loc_717")

    label("loc_708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_717")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 33)

    label("loc_717")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    Event(0, 21)

    label("loc_72D")

    Return()

    # Function_1_47C end

    def Function_2_72E(): pass

    label("Function_2_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_745")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_761")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_778")

    label("loc_761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_778")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_778")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_791")
    SetMapObjFrame(0xFF, "red_", 0x2, "on")

    label("loc_791")

    Return()

    # Function_2_72E end

    def Function_3_792(): pass

    label("Function_3_792")

    Call(0, 4)
    Return()

    # Function_3_792 end

    def Function_4_796(): pass

    label("Function_4_796")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_878")

    #C0001
    ChrTalk(
        0x8,
        (
            "我们的成员分工协作，\x01",
            "负责各地的搜索工作。\x01",
            "市外地区交给我们就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "你们就专心处理\x01",
            "药物调查那边的事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "还有，小滴就\x01",
            "拜托你们照顾了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        "#0100F嗯，请放心。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000F我们会负责\x01",
            "照顾好她的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_886")
    Jump("loc_2725")

    label("loc_886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C39")

    #C0006
    ChrTalk(
        0x8,
        (
            "哎呀，是你们啊，\x01",
            "你们看上去好像很赶时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "难道黑手党斗争事件\x01",
            "有了什么进展吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#0003F不是，我们是在调查别的事件……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "啊，那应该……\x01",
            "就是在调查失踪事件吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0010
    ChrTalk(
        0x101,
        (
            "#0005F游击士协会\x01",
            "也知道这件事了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "嗯，亚里欧斯\x01",
            "也正在调查这件事哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "不过，既然你们开始\x01",
            "插手这件事了……\x01",
            "那就说明问题已经很严重了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "失踪的人应该\x01",
            "不只一两个吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#0301F确实如此……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        (
            "#0200F如果可以的话，\x01",
            "希望能和你们交换情报……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "啊，我们当然是\x01",
            "非常欢迎啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "不过，这件事……\x01",
            "支援科能单独决定吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F（这情报是从一科那边得来的，\x01",
            "  确实不方便对外泄露……）\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0108F（要是被达德利警官知道了，\x01",
            "  他应该会勃然大怒的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "没关系，等你们\x01",
            "协商好了再来吧，\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "等亚里欧斯回来了，\x01",
            "我就把这边的情报整理好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 3)
    Jump("loc_CCB")

    label("loc_C39")


    #C0022
    ChrTalk(
        0x8,
        (
            "啊，对了，小滴现在\x01",
            "也刚好来市里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "亚里欧斯出去调查了，\x01",
            "所以艾丝蒂尔他们就替他\x01",
            "带小滴出去玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "嗯～亚里欧斯可真是\x01",
            "对不住小滴啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCB")

    Jump("loc_2725")

    label("loc_CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_D7F")

    #C0025
    ChrTalk(
        0x8,
        (
            "虽然我们终于掌握了情况，\x01",
            "但他们看起来不像是\x01",
            "要马上挑起斗争的样子哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        "不过现在还无法定论呢。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "为了保证协会随时都有人手出动，\x01",
            "必须先安排好轮值表呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2725")

    label("loc_D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9A")
    Call(0, 5)
    Jump("loc_E31")

    label("loc_D9A")


    #C0028
    ChrTalk(
        0x8,
        (
            "袭击『黑月』，\x01",
            "这毫无疑问就是鲁巴彻的所作所为……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "问题是，为什么他们要在这种局势下\x01",
            "突然发起袭击呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "嗯……总之必须先把\x01",
            "事情调查清楚啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E31")

    Jump("loc_2725")

    label("loc_E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_127A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1016")

    #C0031
    ChrTalk(
        0x8,
        (
            "啊，是支援科的小朋友们啊，\x01",
            "有两个星期没见了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "……关于小琪雅身世的消息，\x01",
            "我很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#0200F以协会的情报网\x01",
            "也还没发现什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "嗯，就只查到了\x01",
            "一点小传闻而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#0003F没事，没关系。\x01",
            "琪雅也完全习惯了\x01",
            "在支援科的生活。\x02\x03",

            "#0000F在查明她的身世以及\x01",
            "找回记忆之前，我觉得先照顾好\x01",
            "她现在的生活比较重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "嗯……\x01",
            "这也对。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "不过我们这边也会\x01",
            "继续调查的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "你们那里要是发现了什么，\x01",
            "再跟我们联系吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#0100F嗯，那就万事拜托了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 1)
    Jump("loc_1275")

    label("loc_1016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E3")

    #C0040
    ChrTalk(
        0x8,
        (
            "亚里欧斯上星期\x01",
            "就去了帝国那边。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "虽然是件很麻烦的工作，\x01",
            "但他也应该快要回来了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0305F咦，那边发生\x01",
            "了什么重大事件吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "其实也不算什么重大事件，\x01",
            "就是那边的协会分部\x01",
            "和军方起了冲突。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "而能够胜任调解工作的，\x01",
            "现在就只有亚里欧斯一人哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "虽然之前在利贝尔\x01",
            "也有一个人能够胜任，\x01",
            "但他已经辞去了游击士的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0106F那、那亚里欧斯先生可真是辛苦呢。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "对啊，是很辛苦哦。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "越是高等级的游击士，\x01",
            "这种麻烦工作就越多哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1275")

    label("loc_11E3")


    #C0049
    ChrTalk(
        0x8,
        (
            "而且游击士协会\x01",
            "和帝国政府\x01",
            "的关系并不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "不过在这一点上，协会在\x01",
            "克洛斯贝尔的情况倒是很乐观。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "市民都很支持我们，\x01",
            "政府也很信赖我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1275")

    Jump("loc_2725")

    label("loc_127A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1439")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CE")

    #C0052
    ChrTalk(
        0x8,
        (
            "我们会动用全大陆\x01",
            "游击士协会的情报网\x01",
            "来调查小琪雅的身世。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "简单报告只需一周就能传来，\x01",
            "详细点的也只需要一个月而已哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1341")

    #C0054
    ChrTalk(
        0x102,
        "#0105F一如既往地有效率呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_13AA")

    label("loc_1341")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1378")

    #C0055
    ChrTalk(
        0x103,
        "#0200F一如既往地有效率呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_13AA")

    label("loc_1378")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13AA")

    #C0056
    ChrTalk(
        0x104,
        "#0306F一如既往地有效率啊……\x02",
    )

    CloseMessageWindow()

    label("loc_13AA")


    #C0057
    ChrTalk(
        0x101,
        "#0000F那就万事拜托了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1434")

    label("loc_13CE")


    #C0058
    ChrTalk(
        0x8,
        (
            "游击士协会在整个大陆上\x01",
            "都有独立的情报网哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "虽然我不敢完全保证，\x01",
            "但大概的身世应该查得出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1434")

    Jump("loc_2725")

    label("loc_1439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_161C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157A")

    #C0060
    ChrTalk(
        0x8,
        (
            "啊……这不是支援科的吗。\x01",
            "你们要去哪里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#0000F嗯，我们要去一趟\x01",
            "位于乌尔斯拉间道的遗迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "是『星见之塔』吗……\x01",
            "那边应该已经被警备队封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "那附近有很厉害\x01",
            "的魔兽出没哦，\x01",
            "你们可要做好万全的准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        "#0100F是，我们会小心的。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#0203F（……还是一如既往\x01",
            "  的细心周到呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1617")

    label("loc_157A")


    #C0066
    ChrTalk(
        0x8,
        (
            "呵呵……一看到你们来访，\x01",
            "我就不自觉地想要照顾照顾呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "总之，要去『星见之塔』的话，\x01",
            "必须得提前做好充分准备哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "那附近出没的魔兽\x01",
            "可是很厉害的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1617")

    Jump("loc_2725")

    label("loc_161C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_18C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1838")

    #C0069
    ChrTalk(
        0x8,
        (
            "话说起来，彩虹的\x01",
            "新剧公演已经临近了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "我也已经买了\x01",
            "下个月的门票了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        "#0300F哎，真亏你能买到门票啊。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        (
            "#0100F米歇尔先生果然也是\x01",
            "伊莉娅小姐的崇拜者吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "不，与其说是崇拜者，\x01",
            "不如说在她身上找到了志同道合的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "如你们所见，我也拥有一副\x01",
            "如妖精般摄人心魄的美丽容颜吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "她与我同为美的追求者，\x01",
            "所以我才对伊莉娅·普拉提耶\x01",
            "产生了共鸣哦⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    #C0076
    ChrTalk(
        0x8,
        (
            "喂，\x01",
            "你们好歹也说点什么啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18BE")

    label("loc_1838")


    #C0077
    ChrTalk(
        0x8,
        (
            "伊莉娅就不用说了，\x01",
            "那个丰满的新人\x01",
            "也很值得期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "不过，就我个人而言，还是最期待\x01",
            "缇奥多尔＆尤金这对美型组合\x01",
            "的格斗场景呢⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BE")

    Jump("loc_2725")

    label("loc_18C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1AEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A75")

    #C0079
    ChrTalk(
        0x8,
        (
            "鲁巴彻是一个在克洛斯贝尔\x01",
            "深深扎根的黑手党……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "犯罪和违法行为对他们来说\x01",
            "就如同家常便饭一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "不过，他们背后有议员或政府高官这样\x01",
            "的大人物支持。\x01",
            "所以我们也很难插手干涉。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "但要是有人敢对平民出手，\x01",
            "我们一定会立刻出面收拾他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0003F你们的工作效率\x01",
            "确实不是警察能比的啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#0306F警察总是在游击士处理完紧急情况\x01",
            "之后才出现……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "对哦，你们的行动\x01",
            "要是机敏点，\x01",
            "我们就不用那么辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AE9")

    label("loc_1A75")


    #C0086
    ChrTalk(
        0x8,
        (
            "我们受到规定的限制，\x01",
            "所以很难介入与政治有关的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "但要是有人敢对平民出手，\x01",
            "我们一定会立刻出面收拾他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE9")

    Jump("loc_2725")

    label("loc_1AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1C8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC4")

    #C0088
    ChrTalk(
        0x8,
        (
            "最近鲁巴彻那帮家伙\x01",
            "活动很频繁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "我们接到的委托中，\x01",
            "也增加了很多与他们相关的内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "人们应该都是觉得警察不可靠，\x01",
            "所以才来向我们求助的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#0003F（真是无法反驳啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C85")

    label("loc_1BC4")


    #C0092
    ChrTalk(
        0x8,
        (
            "顺便说一句，艾丝蒂尔他们\x01",
            "现在应该在自己家里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "……不过，那两人虽然\x01",
            "没有亚里欧斯那么拼命，\x01",
            "但也非常卖力啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "昨天他们也是\x01",
            "工作到很晚才结束……\x01",
            "呵呵，这两人的未来真是让人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C85")

    Jump("loc_2725")

    label("loc_1C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA5")
    Call(0, 17)
    Jump("loc_1DDC")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5F")
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0095
    ChrTalk(
        0x8,
        (
            "今天就给你们\x01",
            "几个比较难的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "虽然是代替去出差的亚里欧斯，\x01",
            "但你们应该也完全应付得来。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        "就拜托你们了哦。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        "#2P好的！\x02",
    )


    #C0099
    ChrTalk(
        0xD,
        "#3P好的！\x02",
    )

    OP_57(0x1)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DDC")

    label("loc_1D5F")


    #C0100
    ChrTalk(
        0x8,
        (
            "那我把相关的资料\x01",
            "拿给你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "首先是这次\x01",
            "工作的一览表——\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0003F（他们好像很忙的样子……\x01",
            "  我们就别去打扰了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDC")

    Jump("loc_2725")

    label("loc_1DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1ED6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7F")

    #C0103
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔的警备队\x01",
            "好像有很多动作。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "那边的司令就不提了，\x01",
            "不过听说副司令很优秀啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "我们也暂时先\x01",
            "观察观察情况再说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ED1")

    label("loc_1E7F")


    #C0106
    ChrTalk(
        0x8,
        (
            "亚里欧斯去\x01",
            "共和国出差了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "真是一个工作狂啊，\x01",
            "看来得考虑让他休息一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED1")

    Jump("loc_2725")

    label("loc_1ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F9")

    #C0108
    ChrTalk(
        0x8,
        "啊，是小朋友们啊。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "特意到竞争对手这里来，\x01",
            "你们是太闲了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "要不，人家也分一点\x01",
            "任务给你们做吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#0005F不、不了。\x01",
            "我们也是在执行任务。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2010")

    #C0112
    ChrTalk(
        0x101,
        (
            "#0001F（游击士协会·克洛斯贝尔分部的\x01",
            "  接待员米歇尔先生吗……）\x02\x03",

            "#0006F（虽然之前就认识了，\x01",
            "  但我们好像被他当成小菜鸟了啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2010")


    #C0113
    ChrTalk(
        0x8,
        "这样啊，那可真是遗憾。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "……你们也差不多\x01",
            "该着急了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0115
    ChrTalk(
        0x101,
        "#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        "#0305F这话怎么说啊？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "呵呵……\x01",
            "没什么，是人家在自言自语哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_215D")

    label("loc_20F9")


    #C0118
    ChrTalk(
        0x8,
        (
            "你们不是正在执行任务吗？\x01",
            "还不快点去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "要是在这里磨磨蹭蹭，\x01",
            "任务就会被我们捷足先登了哦？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215D")

    Jump("loc_2725")

    label("loc_2162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_22EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21DE")

    #C0120
    ChrTalk(
        0x8,
        (
            "总之，你们从今往后\x01",
            "要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "成长到不会\x01",
            "扯我们后腿的\x01",
            "程度就算帮大忙了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CD")

    label("loc_21DE")


    #C0122
    ChrTalk(
        0x8,
        "呵呵，测试辛苦了啊。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "现在大概知道你们\x01",
            "处于什么水平了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        "#0205F……就依据那种程度的测试吗？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        "对，正是依据那种程度的测试才能知道。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "总之，你们从今往后\x01",
            "要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "成长到不会\x01",
            "扯我们后腿的\x01",
            "程度就算帮大忙了哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_22CD")

    Jump("loc_22E9")

    label("loc_22D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_22E6")
    Call(0, 23)
    Jump("loc_22E9")

    label("loc_22E6")

    Call(0, 22)

    label("loc_22E9")

    Jump("loc_2725")

    label("loc_22EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2692")

    #C0128
    ChrTalk(
        0x8,
        "不过，『特别任务支援科』吗……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "人家听说那是在警察局内部的\x01",
            "斗争纠纷中诞生的部门，\x01",
            "那是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#0006F唔……\x01",
            "您、您知道得还真清楚啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "你们可不要\x01",
            "小看游击士协会的情报网哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "我们掌握着周边各国\x01",
            "的各种传闻和情报哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "只要我们愿意，\x01",
            "连埃雷波尼亚的帝都里有多少好男人\x01",
            "都可以调查得清清楚楚。\x02",
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
    Sleep(1200)

    #C0134
    ChrTalk(
        0x104,
        (
            "#0300F（游击士协会的\x01",
            "  情报网确实很有名，\x01",
            "  不过这比喻也有点太那个了吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0135
    ChrTalk(
        0x8,
        (
            "不过，也是。\x01",
            "今后也还有许多事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        (
            "你们几个，\x01",
            "方便的话，稍后再过来一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "作为相识的纪念，人家会为你们\x01",
            "准备一个很有趣的方案哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        "#0005F咦……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x102,
        "#0105F那个，很有趣的方案是指……\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "只是想测试一下你们现在的实力\x01",
            "处于什么水平而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "呵呵，放心吧，\x01",
            "人家不会把你们吃了的。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#0303F（明显很可疑啊……）\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#0200F（话说回来，为什么要\x01",
            "  使用女性的说话方式呢……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 6)
    Jump("loc_2725")

    label("loc_2692")


    #C0144
    ChrTalk(
        0x8,
        (
            "你们几个，\x01",
            "方便的话，稍后再过来一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "作为相识的纪念，人家会为你们\x01",
            "准备一个很有趣的方案哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "呵呵，放心吧，\x01",
            "人家不会把你们吃了的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2725")

    TalkEnd(0x8)
    Return()

    # Function_4_796 end

    def Function_5_2729(): pass

    label("Function_5_2729")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_29F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2962")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0147
    ChrTalk(
        0x8,
        "啊，是支援科的小朋友们呢。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "#1401F你们……\x01",
            "好像也听说了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#0001F嗯，看样子，\x01",
            "游击士协会也知道了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x8,
        "当然啦。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "人家刚才已经联系了所有成员，\x01",
            "现在他们都在二楼待命哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "为了随时应对黑手党间的\x01",
            "全面斗争所带来的危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        "#0105F真、真不愧是游击士协会啊……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#0306F哎呀呀，警察这边\x01",
            "完全迟了一步啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "#1403F算了，那只是因为两者的\x01",
            "职责和做法不尽相同而已。\x02\x03",

            "#1400F我们会用我们自己的做法\x01",
            "来应付突发情况的……\x02\x03",

            "而你们用你们的做法\x01",
            "去处理就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#0001F嗯……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0xCF, 2)
    Jump("loc_29EF")

    label("loc_2962")


    #C0157
    ChrTalk(
        0x9,
        (
            "#1403F『黑月』的曹是\x01",
            "一个相当聪明的男人。\x02\x03",

            "恐怕是不会采取\x01",
            "简单武断的报复行为的吧……\x02\x03",

            "#1401F……算了，\x01",
            "现在也只能做好充分的应急准备了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29EF")

    Jump("loc_2C3C")

    label("loc_29F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2C3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BCF")
    SetChrName("")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "亚里欧斯正用旧式的\x01",
            "国际通讯器进行通话。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0159
    ChrTalk(
        0x9,
        (
            "#1404F#5P……大公阁下，\x01",
            "久疏问候。\x02\x03",

            "嗯、嗯……\x02\x03",

            "…………………………………\x02\x03",

            "#1405F……原来如此，\x01",
            "这稍微有些棘手啊。\x02\x03",

            "#1404F──我了解了。\x01",
            "等我处理完手头的紧急工作之后，\x01",
            "再前去拜访您。\x02",
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
    Sleep(1200)

    #C0160
    ChrTalk(
        0x101,
        (
            "#0012F（好、好像正在和\x01",
            "  什么大人物通话呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0105F（大公……\x01",
            "  莫非是雷米菲利亚公国的……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C3C")

    label("loc_2BCF")


    #C0162
    ChrTalk(
        0x9,
        (
            "#1402F#5P嗯，我想傍晚时\x01",
            "就可以前去拜访您了。\x02\x03",

            "#1404F……您言重了。\x01",
            "您能特别抽时间与我商量，是我的荣幸。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C3C")

    TalkEnd(0xFE)
    Return()

    # Function_5_2729 end

    def Function_6_2C40(): pass

    label("Function_6_2C40")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CD4")
    Jump("loc_2D1E")

    label("loc_2CD4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CF4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1E")

    label("loc_2CF4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D14")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1E")

    label("loc_2D14")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D1E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309E")

    #C0163
    ChrTalk(
        0xFE,
        (
            "#1403F是你们啊。\x02\x03",

            "#1400F你们应该去见过\x01",
            "『黑月』的曹了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    #C0164
    ChrTalk(
        0x101,
        "#0011F咦！？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        "#0105F您怎么会知道……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "#1404F呵……那种消息\x01",
            "很快就会传到我们这边。\x02\x03",

            "#1400F看起来『黑月』那边\x01",
            "好像没有打算立刻\x01",
            "进行报复吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#0001F是、是的……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x104,
        (
            "#0301F不过，情况仍然处于\x01",
            "一触即发的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#0206F而且他们的总部势力\x01",
            "也有可能会介入……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "#1403F『黑月』总部，应该是\x01",
            "支配着卡尔瓦德共和国黑道势力\x01",
            "的一个巨大犯罪组织。\x02\x03",

            "#1400F不过那个组织里\x01",
            "也有好几个派系，并不团结。\x02\x03",

            "如果是那个曹的话，\x01",
            "应该会阻止那些人介入吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#0005F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#0100F话说回来……\x01",
            "您知道得可真详细啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "#1404F因为工作关系，\x01",
            "我经常去共和国那边出差。\x02\x03",

            "那个『银』虽然\x01",
            "很危险，但他好像\x01",
            "也不喜欢无意义的杀戮。\x02\x03",

            "#1401F……真正需要提防的，\x01",
            "或许还是鲁巴彻吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 4)
    Jump("loc_3154")

    label("loc_309E")


    #C0174
    ChrTalk(
        0xFE,
        (
            "#1403F鲁巴彻是一个狡猾的组织。\x01",
            "像这次这种毫无计划的武断袭击，\x01",
            "实在是太少见了。\x02\x03",

            "看来那个副头目加尔西亚\x01",
            "的统治在逐渐减弱啊……\x02\x03",

            "#1401F……唔，好像有某种情况\x01",
            "在暗地里不断发生啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3154")

    Jump("loc_357F")

    label("loc_3159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_33A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32CD")

    #C0175
    ChrTalk(
        0xFE,
        (
            "#1400F是你们啊……\x02\x03",

            "#1404F呵……有一个月没见了吧，\x01",
            "你们好像稍微成长了一点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#0002F哈哈，亚里欧斯先生，\x01",
            "很久不见。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        (
            "#0300F和『风之剑圣』比起来，\x01",
            "我们这点成长实在是微不足道。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "#1404F没什么可羞愧的，\x01",
            "你们好好走你们自己的\x01",
            "路就行了。\x02\x03",

            "#1402F认真观察\x01",
            "克洛斯贝尔现在的情况吧。\x01",
            "……总有一天你们会从中受益的。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        "#0011F好、好的……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 4)
    Jump("loc_339E")

    label("loc_32CD")


    #C0180
    ChrTalk(
        0xFE,
        (
            "#1404F你们好像正在执行任务吧。\x01",
            "……好好努力。\x02\x03",

            "#1402F你们能成长\x01",
            "到何种程度……\x01",
            "我也很期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339B")

    #C0181
    ChrTalk(
        0x101,
        "#0012F（亚里欧斯先生……是在开玩笑吧？）\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#0106F（竟然说期待，\x01",
            "  也太高看我们了吧……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_339B")

    SetScenarioFlags(0x0, 1)

    label("loc_339E")

    Jump("loc_357F")

    label("loc_33A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_357F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3506")

    #C0183
    ChrTalk(
        0xFE,
        "#1405F哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#0011F亚里欧斯先生……\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#0103F那个，久疏问候。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "#1404F呵……\x01",
            "不用这么紧张。\x02\x03",

            "#1402F旧城区那件事\x01",
            "辛苦你们了。\x02\x03",

            "在我们介入之前你们就解决了，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        "#0012F没、没什么……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x104,
        (
            "#0306F（不过，只要这个大叔出面，\x01",
            "  应该一下就能解决吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        "#0211F（总觉得一切都在他的掌握之中。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 3)
    Jump("loc_357F")

    label("loc_3506")


    #C0190
    ChrTalk(
        0xFE,
        (
            "#1404F那么……\x01",
            "我也差不多该走了。\x02\x03",

            "#1402F呵呵，因为他们的加入，\x01",
            "我才有了点空闲……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#0005F……？\x01",
            "（他们是指？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_357F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_2C40 end

    def Function_7_3587(): pass

    label("Function_7_3587")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_35F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A5")
    Call(0, 17)
    Jump("loc_35F9")

    label("loc_35A5")


    #C0192
    ChrTalk(
        0xB,
        (
            "#0800F罗伊德，\x01",
            "你们是要去工作吧？\x02\x03",

            "#0809F呵呵……下次见面时，\x01",
            "还请多多关照哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F9")

    TalkEnd(0xFE)
    Return()

    # Function_7_3587 end

    def Function_8_35FD(): pass

    label("Function_8_35FD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3691")
    Jump("loc_36DB")

    label("loc_3691")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36B1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36DB")

    label("loc_36B1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36D1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36DB")

    label("loc_36D1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36DB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_37B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371B")
    Call(0, 18)
    Jump("loc_37B4")

    label("loc_371B")


    #C0193
    ChrTalk(
        0xC,
        (
            "#0806F虽然我们也想\x01",
            "直接去质问那些黑手党们……\x02\x03",

            "但在这种时候，好像还是应该\x01",
            "让警察优先采取行动啊～\x02\x03",

            "#0800F所以呢，罗伊德，\x01",
            "你们要代替我们加油调查哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B4")

    Jump("loc_3952")

    label("loc_37B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3952")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38CC")

    #C0194
    ChrTalk(
        0x153,
        (
            "#1106F艾丝蒂尔，刚才抱歉啊。\x02\x03",

            "#1108F琪雅并不是\x01",
            "讨厌艾丝蒂尔哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "#0809F啊哈哈，没关系哦，\x01",
            "我完全没放在心上。\x02\x03",

            "#0802F不过你要是有什么烦恼，\x01",
            "希望你能来找姐姐商量哦，\x02\x03",

            "姐姐一定能\x01",
            "帮上忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x153,
        "#1109F嗯！\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#0002F好的，到时候就拜托了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3952")

    label("loc_38CC")


    #C0198
    ChrTalk(
        0xC,
        (
            "#0806F……呼～这段时间\x01",
            "真是不断被抛弃啊。\x02\x03",

            "#0808F最后也没能见到\x01",
            "纪念庆典期间过来的雾香小姐……\x02\x03",

            "#0805F不过……她是来做什么的呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3952")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_35FD end

    def Function_9_395A(): pass

    label("Function_9_395A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3978")
    Call(0, 17)
    Jump("loc_3A62")

    label("loc_3978")


    #C0199
    ChrTalk(
        0xD,
        (
            "#0900F我们准备在今天\x01",
            "执行任务的时候，顺便去\x01",
            "阿尔摩利卡那边看看。\x02\x03",

            "#0904F我和艾丝蒂尔\x01",
            "对克洛斯贝尔市的周边情况\x01",
            "都还不熟悉。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5F")

    #C0200
    ChrTalk(
        0x101,
        (
            "#0003F这样啊……\x02\x03",

            "#0000F我想你们肯定没问题的，\x01",
            "不过要小心魔兽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xD,
        "#0902F嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    label("loc_3A5F")

    SetScenarioFlags(0x0, 3)

    label("loc_3A62")

    TalkEnd(0xFE)
    Return()

    # Function_9_395A end

    def Function_10_3A66(): pass

    label("Function_10_3A66")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AFA")
    Jump("loc_3B44")

    label("loc_3AFA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B1A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B44")

    label("loc_3B1A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B3A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B44")

    label("loc_3B3A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B44")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B84")
    Call(0, 18)
    Jump("loc_3C29")

    label("loc_3B84")


    #C0202
    ChrTalk(
        0xE,
        (
            "#0901F虽然已经把克洛斯贝尔\x01",
            "的情况大体掌握了……\x02\x03",

            "但在发生这种事件的时候，\x01",
            "确实能感到面前有一道巨大的『壁障』呢。\x02\x03",

            "#0903F目前至少要想办法把握到\x01",
            "准确的状况啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C29")

    Jump("loc_3E67")

    label("loc_3C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3DD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D66")

    #C0203
    ChrTalk(
        0xE,
        (
            "#0905F咦……大圣堂那边\x01",
            "也没办法吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        "#0006F嗯，其实……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "讲述了大圣堂的修女\x01",
            "为琪雅诊断时的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0206
    ChrTalk(
        0xE,
        (
            "#0903F这样啊……\x02\x03",

            "#0900F确实，像这种情况，\x01",
            "只能寄希望于\x01",
            "乌尔斯拉医院了。\x02\x03",

            "听说那里的『神经科』\x01",
            "拥有最先进的医疗技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#0002F是啊。\x01",
            "我们接下来正要去那里看看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DD4")

    label("loc_3D66")


    #C0208
    ChrTalk(
        0xE,
        (
            "#0903F以现在的情况来看，\x01",
            "只能寄希望于乌尔斯拉医院了。\x02\x03",

            "#0900F听说那里的『神经科』\x01",
            "拥有最先进的医疗技术。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD4")

    Jump("loc_3E67")

    label("loc_3DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3E67")

    #C0209
    ChrTalk(
        0xE,
        (
            "#0904F七耀教会自古以来就流传着\x01",
            "可以治愈身心的秘术。\x02\x03",

            "#0900F说不定会\x01",
            "有办法使小琪雅\x01",
            "恢复记忆吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#0000F嗯，那我们去试试看。\x02",
    )

    CloseMessageWindow()

    label("loc_3E67")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_3A66 end

    def Function_11_3E6F(): pass

    label("Function_11_3E6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3FEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F8E")

    #C0211
    ChrTalk(
        0xFE,
        (
            "帕尔现在也在\x01",
            "百货店努力做着\x01",
            "前台接待的工作吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x102,
        "#0102F是您的女朋友吗？\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "嗯，其实我们都已经订婚了呢。\x01",
            "只是两个人都太忙了，\x01",
            "所以很少有时间见面……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "……啊，看我都说了些什么。\x01",
            "公私不分是外行才会做的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "我必须要振作精神，努力工作啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3FE7")

    label("loc_3F8E")


    #C0216
    ChrTalk(
        0xFE,
        (
            "不将公私严格分清的话，\x01",
            "到头来只会两边都顾不上。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "我必须要振作精神，努力工作啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3FE7")

    Jump("loc_4069")

    label("loc_3FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3FFA")
    Jump("loc_4069")

    label("loc_3FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4069")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4015")
    Call(0, 19)
    Jump("loc_4069")

    label("loc_4015")


    #C0218
    ChrTalk(
        0xFE,
        (
            "今天早上，阿尔摩利卡村那边\x01",
            "发来了两三件委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "那么……\x01",
            "今天应该会很忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4069")

    TalkEnd(0xFE)
    Return()

    # Function_11_3E6F end

    def Function_12_406D(): pass

    label("Function_12_406D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4101")
    Jump("loc_414B")

    label("loc_4101")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4121")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_414B")

    label("loc_4121")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4141")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_414B")

    label("loc_4141")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_414B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_41FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418B")
    Call(0, 18)
    Jump("loc_41FA")

    label("loc_418B")


    #C0220
    ChrTalk(
        0xFE,
        (
            "总之，先调查调查\x01",
            "黑手党那边的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "购入重型武器的\x01",
            "违法渠道多得可怕……\x01",
            "危险事件可能会频繁发生啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41FA")

    Jump("loc_449E")

    label("loc_41FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_449E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43FC")
    SetChrSubChip(0x11, 0x0)

    #C0222
    ChrTalk(
        0x10,
        (
            "你们知道大约在两年前发生的，\x01",
            "帝国游击士协会相继被袭的事件吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        (
            "当时在帝国的温蔡尔是\x01",
            "解决那个事件的大功臣。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        (
            "#0108F那个事件……\x01",
            "当时引起了很大的骚动吧。\x02\x03",

            "#0103F听说猎兵团的连续恐怖袭击\x01",
            "让帝国的游击士协会陷入了半瘫痪状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#0000F竟然解决了\x01",
            "那样的大事件……果然很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x11,
        "……没有啦，我也没有做什么大不了的事。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x11,
        (
            "我们之所以能解决那个事件，\x01",
            "主要还是多亏了前来相助的高级游击士\x01",
            "提供的完美策略。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x11,
        (
            "我只是作为一名作战执行人员，刚好处于\x01",
            "比较显眼的位置而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_449E")

    label("loc_43FC")

    SetChrSubChip(0x10, 0x0)

    #C0229
    ChrTalk(
        0x11,
        (
            "别说我了，斯克特……\x01",
            "你最近跟未婚妻见过面吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        (
            "……完全没有，\x01",
            "这么忙，哪有时间见面啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x10,
        (
            "结婚的事也得推迟了……\x01",
            "等我有时间了，\x01",
            "必须好好补偿她啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_449E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_406D end

    def Function_13_44A6(): pass

    label("Function_13_44A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4608")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A2")
    OP_4B(0x11, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0232
    ChrTalk(
        0x11,
        (
            "艾欧莉娅，万一发生了什么事，\x01",
            "你的首要任务是\x01",
            "保护伤员。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x13,
        (
            "嗯，我知道\x01",
            "自己该怎么做。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x13,
        (
            "……不过，最好能\x01",
            "找到更稳妥的\x01",
            "解决办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x11,
        "当然了。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x11,
        (
            "所以……\x01",
            "从今以后，收集情报十分重要啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x13, 0xFF)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x0, 5)
    Jump("loc_4603")

    label("loc_45A2")


    #C0237
    ChrTalk(
        0xFE,
        (
            "可不能因为黑手党间\x01",
            "无聊的斗争，\x01",
            "让市民受到伤害。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "所以……\x01",
            "必须要多收集一些相关情报啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4603")

    Jump("loc_49A6")

    label("loc_4608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_475A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4700")

    #C0239
    ChrTalk(
        0xFE,
        (
            "今天早上，搜查一科的那些家伙们\x01",
            "好像在四处转悠。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "……那些家伙真是让人没法喜欢啊。\x01",
            "让我想起了帝国军的ＭＰ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#0005F（ＭＰ……是指宪兵吗。）\x02\x03",

            "#0003F（帝国军采取的好像也是保密主义吧……\x01",
            "  性质上确实有点像啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4755")

    label("loc_4700")


    #C0242
    ChrTalk(
        0xFE,
        (
            "帝国军让我有过\x01",
            "不好的回忆……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "同样，\x01",
            "偷偷摸摸的搜查一科\x01",
            "也让人没法喜欢啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4755")

    Jump("loc_49A6")

    label("loc_475A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4921")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4775")
    Call(0, 12)
    Jump("loc_491C")

    label("loc_4775")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4809")
    Jump("loc_4853")

    label("loc_4809")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4829")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4853")

    label("loc_4829")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4849")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4853")

    label("loc_4849")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4853")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0244
    ChrTalk(
        0x11,
        (
            "……那个事件以来，\x01",
            "帝国游击士协会就因为政府的压力\x01",
            "而开始衰弱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x11,
        (
            "我运气好，被调到了\x01",
            "克洛斯贝尔分部……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x11,
        (
            "……不，还是算了，\x01",
            "跟你们说了些无聊话呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    label("loc_491C")

    Jump("loc_49A6")

    label("loc_4921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_49A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493C")
    Call(0, 19)
    Jump("loc_49A6")

    label("loc_493C")


    #C0247
    ChrTalk(
        0xFE,
        (
            "这次，克洛斯贝尔的分部\x01",
            "会调来两个前途无量的新人。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "你们可要时刻提醒自己，\x01",
            "还有这两个强敌存在啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A6")

    TalkEnd(0xFE)
    Return()

    # Function_13_44A6 end

    def Function_14_49AA(): pass

    label("Function_14_49AA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A3E")
    Jump("loc_4A88")

    label("loc_4A3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A88")

    label("loc_4A5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A88")

    label("loc_4A7E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A88")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4C88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC8")
    Call(0, 18)
    Jump("loc_4C83")

    label("loc_4AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BFD")

    #C0249
    ChrTalk(
        0xFE,
        (
            "『风之剑圣』亚里欧斯先生，\x01",
            "利贝尔的英雄艾丝蒂尔和约修亚，\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "使用来复枪的高手斯克特和\x01",
            "帝国游击士协会的勇者温蔡尔，\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "医术高超的艾欧莉娅，\x01",
            "还有善用『泰斗流』武术的我。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "即使有这么多厉害的游击士，\x01",
            "在应对克洛斯贝尔内的事件时，\x01",
            "也必须十分慎重。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "你们那边也是，请务必谨慎行动。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4C83")

    label("loc_4BFD")


    #C0254
    ChrTalk(
        0xFE,
        (
            "这里以『风之剑圣』亚里欧斯先生为首，\x01",
            "聚集了很多厉害的游击士，\x01",
            "但在应对事件时也必须十分慎重。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        "你们那边也是，请务必谨慎行动。\x02",
    )

    CloseMessageWindow()

    label("loc_4C83")

    Jump("loc_501C")

    label("loc_4C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDE")

    #C0256
    ChrTalk(
        0xFE,
        (
            "哦，是警察局的新手们啊。\x01",
            "最近怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D06")

    #C0257
    ChrTalk(
        0x101,
        (
            "#0000F（这个人……\x01",
            "  就是游击士林小姐吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D20")

    label("loc_4D06")


    #C0258
    ChrTalk(
        0x101,
        "#0000F哈哈，您好……\x02",
    )

    CloseMessageWindow()

    label("loc_4D20")


    #C0259
    ChrTalk(
        0x102,
        (
            "#0100F难得见您一面啊，\x01",
            "今天没去出差吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "你说对了，\x01",
            "我昨天才刚回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "已经拜托米歇尔\x01",
            "不要再让我出差了，\x01",
            "所以暂时应该没有出差任务哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x104,
        "#0300F哈哈，游击士也很辛苦啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4F98")

    label("loc_4DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4F38")

    #C0263
    ChrTalk(
        0xFE,
        (
            "抱歉啊，小缇欧，\x01",
            "艾欧莉娅又纠缠你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x103,
        (
            "#0206F啊，我倒是无所谓……\x01",
            "就是不知道艾欧莉娅小姐\x01",
            "这么做的原因……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "我也不知道艾欧莉娅\x01",
            "在想什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "我说，你还是乖乖放弃，\x01",
            "当她的布偶吧。\x02",
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
    Sleep(1200)

    #C0267
    ChrTalk(
        0x101,
        "#0003F（林小姐，也太直爽了吧……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F98")

    label("loc_4F38")


    #C0268
    ChrTalk(
        0xFE,
        (
            "艾欧莉娅有着身为医生的特殊技能。\x01",
            "到处都需要她，\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "所以一直得出差，\x01",
            "和她组队真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F98")

    Jump("loc_501C")

    label("loc_4F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_501C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB8")
    Call(0, 20)
    Jump("loc_501C")

    label("loc_4FB8")


    #C0270
    ChrTalk(
        0xFE,
        (
            "算了，我可能说得太夸张了……\x01",
            "你们也不是在玩吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "所以别垂头丧气的，\x01",
            "要努力挽回局面才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_501C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_49AA end

    def Function_15_5024(): pass

    label("Function_15_5024")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_50BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5042")
    Call(0, 13)
    Jump("loc_50B9")

    label("loc_5042")


    #C0272
    ChrTalk(
        0xFE,
        (
            "虽然我有着医生资格，\x01",
            "必要时可以派上用场……\x01",
            "但我并不希望有这种出场机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "必须摸索出尽量避免\x01",
            "伤员出现的办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50B9")

    Jump("loc_53D8")

    label("loc_50BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5340")
    TurnDirection(0x13, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52AC")

    #C0274
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "这不是小缇欧嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "嗯，还是一样\x01",
            "好可爱好可爱啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "求求你，让姐姐\x01",
            "抱抱吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x103,
        "#0211F那个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51B8")

    #C0278
    ChrTalk(
        0x101,
        (
            "#0000F（跟艾欧莉娅小姐\x01",
            "  也说过好几次话了……\x01",
            "  但每次她一见到缇欧就变得很不正常呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51F9")

    label("loc_51B8")


    #C0279
    ChrTalk(
        0x101,
        (
            "#0000F（艾欧莉娅小姐……\x01",
            "  每次一见到缇欧就变得很不正常。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F9")


    #C0280
    ChrTalk(
        0x104,
        (
            "#0303F（超美丽的异国姐姐……\x01",
            "  完全是我喜欢的类型啊……）\x02\x03",

            "#0301F（但既然她喜欢上阿缇了，\x01",
            "  也就没办法啦。\x01",
            "  把她让给阿缇好了……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        "#0206F（到底该怎么办……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_533B")

    label("loc_52AC")


    #C0282
    ChrTalk(
        0xFE,
        (
            "小缇欧，来吧～！\x01",
            "让姐姐抱抱～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    #C0283
    ChrTalk(
        0x101,
        (
            "#0000F（她对缇欧的呼唤\x01",
            "  充满了喜爱之情啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x103,
        "#0206F（怎么办……）\x02",
    )

    CloseMessageWindow()

    label("loc_533B")

    Jump("loc_53D8")

    label("loc_5340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_53D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535B")
    Call(0, 20)
    Jump("loc_53D8")

    label("loc_535B")


    #C0285
    ChrTalk(
        0xFE,
        (
            "呵呵，今天出差刚回来，\x01",
            "就先到这里吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)

    #C0286
    ChrTalk(
        0xFE,
        (
            "小缇欧，\x01",
            "下次可一定要让我抱抱哦⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        "#0211F（……认定为危险人物。）\x02",
    )

    CloseMessageWindow()

    label("loc_53D8")

    TalkEnd(0xFE)
    Return()

    # Function_15_5024 end

    def Function_16_53DC(): pass

    label("Function_16_53DC")

    TalkBegin(0xFF)
    SetChrName("")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贴有游击士们的工作表。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5543")
    SetChrName("")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：  玛因兹区域\x01",
            " 　 斯克特 　： 贝尔加德门区域\x01",
            " 　 温蔡尔 　： 贝尔加德门区域\x01",
            " 　　 林 　　： 唐古拉姆门区域\x01",
            " 　艾欧莉娅　： 唐古拉姆门区域\x01",
            " 　艾丝蒂尔　： 阿尔摩利卡区域\x01",
            " 　 约修亚 　： 阿尔摩利卡区域\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_5543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_5662")
    SetChrName("")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：   市内巡逻\x01",
            " 　 斯克特 　：  贝尔加德门\x01",
            " 　 温蔡尔 　：  贝尔加德门\x01",
            " 　　 林 　　：    旧城区\x01",
            " 　艾欧莉娅　：    旧城区\x01",
            " 　艾丝蒂尔　：  ※私事（东街）\x01",
            " 　 约修亚 　：  ※私事（东街）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_5662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5785")
    SetChrName("")

    #A0291
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：   市内巡逻\x01",
            " 　 斯克特 　：  贝尔加德门\x01",
            " 　 温蔡尔 　：  贝尔加德门\x01",
            " 　　 林 　　：    旧城区\x01",
            " 　艾欧莉娅　：    旧城区\x01",
            " 　艾丝蒂尔　：  ※私事（欢乐街）\x01",
            " 　 约修亚 　：  ※私事（欢乐街）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_5785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_58A9")
    SetChrName("")

    #A0292
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：  『待命中』\x01",
            " 　 斯克特 　：     后巷\x01",
            " 　 温蔡尔 　：     后巷\x01",
            " 　　 林 　　： 克洛斯贝尔车站\x01",
            " 　艾欧莉娅　： 克洛斯贝尔车站\x01",
            " 　艾丝蒂尔　：  ※休息（自宅）\x01",
            " 　 约修亚 　：  ※休息（自宅）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_58A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_59C5")
    SetChrName("")

    #A0293
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：  『待命中』\x01",
            " 　 斯克特 　：  『待命中』\x01",
            " 　 温蔡尔 　：  『待命中』\x01",
            " 　　 林 　　：  『待命中』\x01",
            " 　艾欧莉娅　：  『待命中』\x01",
            " 　艾丝蒂尔　：  『待命中』\x01",
            " 　 约修亚 　：  『待命中』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_59C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5AE8")
    SetChrName("")

    #A0294
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　： 埃雷波尼亚帝国\x01",
            " 　 斯克特 　：    旧城区\x01",
            " 　 温蔡尔 　：    旧城区\x01",
            " 　　 林 　　：  乌尔斯拉医院\x01",
            " 　艾欧莉娅　：  乌尔斯拉医院\x01",
            " 　艾丝蒂尔　：  阿尔摩利卡村\x01",
            " 　 约修亚 　：  阿尔摩利卡村\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_5AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5C06")
    SetChrName("")

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：   市外巡逻\x01",
            " 　 斯克特 　：    ※休假\x01",
            " 　 温蔡尔 　：   市外巡逻\x01",
            " 　　 林 　　： 雷米菲利亚公国\x01",
            " 　艾欧莉娅　： 雷米菲利亚公国\x01",
            " 　艾丝蒂尔　：  『待命中』\x01",
            " 　 约修亚 　：  『待命中』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_5C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D28")
    SetChrName("")

    #A0296
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：  雷米菲利亚公国\x01",
            " 　 斯克特 　：   『待命中』\x01",
            " 　 温蔡尔 　：   『待命中』\x01",
            " 　　 林 　　：   唐古拉姆门\x01",
            " 　艾欧莉娅　：   唐古拉姆门\x01",
            " 　艾丝蒂尔　：     玛因兹\x01",
            " 　 约修亚 　：     玛因兹\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_5D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5E4B")
    SetChrName("")

    #A0297
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：   『待命中』\x01",
            " 　 斯克特 　：     玛因兹\x01",
            " 　 温蔡尔 　：     玛因兹\x01",
            " 　　 林 　　：  乌尔斯拉医院\x01",
            " 　艾欧莉娅　：  乌尔斯拉医院\x01",
            " 　艾丝蒂尔　：    贝尔加德门\x01",
            " 　 约修亚 　：    贝尔加德门\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_5E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F74")
    SetChrName("")

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：   『待命中』\x01",
            " 　 斯克特 　：     玛因兹\x01",
            " 　 温蔡尔 　：     玛因兹\x01",
            " 　　 林 　　：  乌尔斯拉医院\x01",
            " 　艾欧莉娅　：  乌尔斯拉医院\x01",
            " 　艾丝蒂尔　：   ※休息（自宅）\x01",
            " 　 约修亚 　：   ※休息（自宅）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_5F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_609B")
    SetChrName("")

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　： 卡尔瓦德共和国\x01",
            " 　 斯克特 　： 埃雷波尼亚帝国\x01",
            " 　 温蔡尔 　： 埃雷波尼亚帝国\x01",
            " 　　 林 　　：    市外巡逻\x01",
            " 　艾欧莉娅　：    市外巡逻\x01",
            " 　艾丝蒂尔　：   『待命中』\x01",
            " 　 约修亚 　：   『待命中』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_609B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_60D1")
    SetChrName("")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "正在重新排班……\x01",
            "稍等一下哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_60D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_61B6")
    SetChrName("")

    #A0301
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　： 埃雷波尼亚帝国\x01",
            " 　 斯克特 　：   市外巡逻\x01",
            " 　 温蔡尔 　：   市外巡逻\x01",
            " 　　 林 　　：  『待命中』\x01",
            " 　艾欧莉娅　：  『待命中』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_628D")

    label("loc_61B6")

    SetChrName("")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  去向　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　： 埃雷波尼亚帝国\x01",
            " 　 斯克特 　：  『待命中』\x01",
            " 　 温蔡尔 　：  『待命中』\x01",
            " 　　 林 　　：   市外巡逻\x01",
            " 　艾欧莉娅　：   市外巡逻\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_628D")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_16_53DC end

    def Function_17_62A4(): pass

    label("Function_17_62A4")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(810, 1300, 9650, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18820, 0)
    SetChrPos(0x101, 1520, 0, 8250, 0)
    SetChrPos(0x102, 340, 0, 8029, 0)
    SetChrPos(0x103, 1520, 0, 6890, 0)
    SetChrPos(0x104, 340, 0, 6640, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0xD, 0x0, 0x0)
    OP_0D()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_636B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_636B)
    Sleep(50)

    def lambda_637B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_637B)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)

    #C0303
    ChrTalk(
        0xB,
        (
            "#0805F啊，你们是昨天的……\x02\x03",

            "#0809F你们好啊！\x01",
            "特别任务支援科的各位～！\x02",
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
    Sleep(1200)

    #C0304
    ChrTalk(
        0x101,
        (
            "#0012F你、你们好，\x01",
            "艾丝蒂尔、约修亚。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        "#0204F昨天谢谢你们了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0306
    ChrTalk(
        0x8,
        (
            "哈……\x01",
            "我说，艾丝蒂尔啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_64D4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_64D4)
    Sleep(100)

    def lambda_64E4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_64E4)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)

    #C0307
    ChrTalk(
        0xB,
        "#0805F嗯，什么事啊，米歇尔先生？\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "算了，没什么。\x01",
            "我们继续商谈吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        "#0800F？？？\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)

    #C0311
    ChrTalk(
        0xD,
        (
            "#0906F如你们所见，\x01",
            "艾丝蒂尔就是这样……\x02\x03",

            "#0900F如果我们能抛开那些复杂的成见，\x01",
            "成为正常来往的朋友就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        "#0002F……嗯，我们也是这么想的。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        "#0104F还请多多指教哦。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1000, 0, 8250, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0xD, 0x0, 0x0)
    SetChrFlags(0x8, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x6D, 2)
    EventEnd(0x5)
    Return()

    # Function_17_62A4 end

    def Function_18_6664(): pass

    label("Function_18_6664")

    EventBegin(0x0)
    Fade(500)
    OP_68(-5920, 1300, 48320, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -3550, 0, 48770, 270)
    SetChrPos(0x102, -3440, 0, 47510, 270)
    SetChrPos(0x103, -2420, 0, 48770, 270)
    SetChrPos(0x104, -2320, 0, 47490, 270)
    SetChrSubChip(0xC, 0x1)
    SetChrSubChip(0xE, 0x1)
    SetChrSubChip(0x10, 0x2)
    SetChrSubChip(0x12, 0x2)
    OP_0D()

    #C0314
    ChrTalk(
        0xC,
        (
            "#0801F#1P啊，罗伊德！\x01",
            "你们听说『黑月』的事了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#0001F#11P嗯，我们现在\x01",
            "刚好在收集相关情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x102,
        (
            "#0105F#11P不过……\x01",
            "游击士竟然齐聚一堂了。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x103,
        (
            "#0202F#11P而且连『风之剑圣』也在，\x01",
            "真是壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xE,
        (
            "#0904F#1P哈哈……因为一早\x01",
            "就接到了导力通讯。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x10,
        (
            "#6P所以我们\x01",
            "都急忙赶过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        (
            "#0306F#11P哎呀，你们的\x01",
            "行动速度也太敏捷了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x12,
        (
            "#6P嗯，应该说是\x01",
            "你们太悠哉了哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    Sleep(200)

    #C0322
    ChrTalk(
        0x12,
        (
            "#12P鲁巴彻的那帮家伙……\x01",
            "竟然做出了如此过分的事情！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    #C0323
    ChrTalk(
        0xC,
        (
            "#0803F#5P嗯嗯！\x01",
            "虽然是夜晚行人较少的场所，\x01",
            "但说不定刚好会有市民经过啊！\x02\x03",

            "#0801F那帮黑手党们，真是不可原谅！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3420, 0, 48200, 270)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetScenarioFlags(0xCF, 7)
    EventEnd(0x5)
    Return()

    # Function_18_6664 end

    def Function_19_6945(): pass

    label("Function_19_6945")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_68(-4610, 1000, 51100, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, -3630, 0, 50910, 315)
    SetChrPos(0x102, -4250, 0, 49980, 315)
    SetChrPos(0x103, -2650, 0, 50000, 315)
    SetChrPos(0x104, -3250, 0, 48910, 315)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x11, 0x0)
    OP_93(0xF, 0x13B, 0x0)
    OP_93(0x11, 0x2D, 0x0)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    OP_0D()

    #C0324
    ChrTalk(
        0xF,
        (
            "#11P亚里欧斯先生去出差了吗……\x01",
            "还是一如既往地忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xF,
        (
            "#11P不过，我们也没资格说他，\x01",
            "我们接下来也要出动了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x11,
        (
            "#5P林和艾欧莉娅应该\x01",
            "快要回来了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x11,
        "#5P真不愧是米歇尔，工作表安排得果然很合理。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xF,
        "#11P哈哈，不过就是用人用得狠了些。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#11P#0005F那个……\x01",
            "请问两位是游击士吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6B4F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6B4F)

    def lambda_6B5C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B5C)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x11, 1)

    #C0330
    ChrTalk(
        0xF,
        "#5P你们……\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xF,
        (
            "#5P啊，难道你们就是\x01",
            "传说中的『特别任务支援科』？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#11P#0200F嗯，正是……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        "#12P#0304F果然一眼就能看出来啊。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x11,
        "#5P……因为你们散发出一股菜鸟的味道啊。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x11,
        (
            "#5P看起来就很不成熟……\x01",
            "你们真的能在克洛斯贝尔混下去吗？\x02",
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
    Sleep(1200)

    #C0336
    ChrTalk(
        0x102,
        (
            "#12P#0106F（嗯，虽然不甘心……\x01",
            "  但也无法否认。）\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#11P#0001F总之……\x01",
            "我们会\x01",
            "尽我们所能的。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x11,
        "#5P……太天真了。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x11,
        (
            "#5P如果不去挑战极限的话，\x01",
            "你们是永远都无法成长的。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#11P#0003F唔……\x01",
            "（好严厉……）\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xF,
        (
            "#5P哈哈，总之加油啊。\x01",
            "我个人还是支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xF,
        (
            "#5P你们这些警察要是争气点，\x01",
            "我们或许就不用这么忙了……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xF,
        (
            "#5P因为警察们搞砸的案件，\x01",
            "最后全部都会被推来我们这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        "#11P#0006F我、我们会努力的……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -3630, 0, 50910, 315)
    SetMapObjFrame(0xFF, "on_off", 0x1, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x1, 0x1)
    OP_93(0xF, 0x0, 0x0)
    OP_93(0x11, 0x2D, 0x0)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x4F, 7)
    EventEnd(0x5)
    Return()

    # Function_19_6945 end

    def Function_20_6EB9(): pass

    label("Function_20_6EB9")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x13, 0xFF)
    OP_68(-4460, 1300, 41900, 0)
    MoveCamera(17, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20100, 0)
    SetChrPos(0x101, -3430, 0, 42620, 270)
    SetChrPos(0x103, -3440, 0, 41360, 270)
    SetChrPos(0x102, -2320, 0, 42620, 270)
    SetChrPos(0x104, -2320, 0, 41360, 270)
    TurnDirection(0x13, 0x103, 0)
    SetChrSubChip(0x12, 0x1)
    OP_0D()

    #C0345
    ChrTalk(
        0x12,
        "#5P啊，你们是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0346
    ChrTalk(
        0x13,
        "#5P哇……好可爱……！\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x103,
        (
            "#11P#0205F哎……\x01",
            "是、是在说我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x13,
        "#5P当然了！\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x13,
        (
            "#5P态度明明像大人一样成熟而冷静，\x01",
            "却有着孩子气的大眼睛和可爱的小嘴唇……\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x13,
        "#5P真、真让人受不了啊～！！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    #C0351
    ChrTalk(
        0x13,
        (
            "#11P怎么样，林！\x01",
            "我可以把她带回去吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        "#11P#0211F……………………\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x12,
        (
            "#5P……艾欧莉娅，你的坏习惯又来了。\x01",
            "才第一次见面，你这样会吓到对方的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x12,
        (
            "#5P我们才刚出完差回来，\x01",
            "你给我适可而止啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x104,
        (
            "#11P#0302F这位姐姐，我可以\x01",
            "让你带回去哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)

    #C0356
    ChrTalk(
        0x13,
        "#5P你啊，你就算了吧⊥\x02",
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
    Sleep(1200)

    #C0357
    ChrTalk(
        0x104,
        "#11P#0306F……竟然回答得这么干脆。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x102,
        (
            "#11P#0106F怎、怎么说呢……\x01",
            "虽然看起来很端庄典雅，\x01",
            "但行为却有点让人难以理解呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#11P#0000F你们两位，莫非\x01",
            "是这里的游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x13,
        (
            "#5P这样说来，你们应该\x01",
            "就是『特别任务支援科』的成员吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0361
    ChrTalk(
        0x101,
        "#11P#0005F您也知道吗？\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x12,
        "#5P是米歇尔先生告诉我的。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x12,
        (
            "#5P第一次任务竟然就需要亚里欧斯先生的\x01",
            "帮助才能完成，真是没出息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x13,
        (
            "#5P警察还无法让人信任啊。\x01",
            "你们可得争气点哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x12,
        (
            "#5P反正笨鸟只要按照\x01",
            "自己的步调来努力就好了。\x02",
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
    Sleep(1200)

    #C0366
    ChrTalk(
        0x102,
        "#11P#0106F（这话说得真过分……）\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        "#11P#0000F铭、铭记于心。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3430, 0, 42620, 270)
    OP_93(0x13, 0x10E, 0x0)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x50, 0)
    EventEnd(0x5)
    Return()

    # Function_20_6EB9 end

    def Function_21_74A1(): pass

    label("Function_21_74A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(7120, 1300, 4730, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -1750, 0, 2150, 0)
    SetChrPos(0x102, -2750, 0, 1900, 0)
    SetChrPos(0x103, -1750, 0, 650, 0)
    SetChrPos(0x104, -2750, 0, 400, 0)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(950, 1300, 11510, 5000)
    OP_6F(0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-2160, 1300, 4030, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0368
    ChrTalk(
        0x101,
        (
            "#11P#0000F这里就是……\x01",
            "游击士协会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x103,
        (
            "#11P#0203F游击士协会……\x01",
            "是一个负责保护、支援一般平民的\x01",
            "国际性非政府组织吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        (
            "#11P#0300F就是所谓的正义伙伴，\x01",
            "也是我们的竞争对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#11P#0100F不过，表面上跟我们\x01",
            "应该是有互助关系的吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)

    #C0372
    ChrTalk(
        0x8,
        "#6P哎呀，欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        (
            "#6P莫非，你们就是\x01",
            "『特别任务支援科』的小朋友们？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0374
    ChrTalk(
        0x101,
        "#11P#0005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        "#11P#0105F您怎么会知道我们……\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1300, 10500, 5000)
    MoveCamera(45, 26, 0, 5000)
    SetCameraDistance(21750, 5000)

    def lambda_77F2():
        OP_96(0xFE, 0x5DC, 0x0, 0x27A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77F2)
    Sleep(50)

    def lambda_780F():
        OP_96(0xFE, 0x1F4, 0x0, 0x26AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_780F)
    Sleep(50)

    def lambda_782C():
        OP_96(0xFE, 0x5DC, 0x0, 0x21CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_782C)
    Sleep(50)

    def lambda_7849():
        OP_96(0xFE, 0x1F4, 0x0, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7849)
    Sleep(500)
    OP_93(0x8, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    def lambda_7871():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7871)
    WaitChrThread(0x102, 1)

    def lambda_7882():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7882)
    WaitChrThread(0x103, 1)

    def lambda_7893():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7893)
    WaitChrThread(0x104, 1)

    def lambda_78A4():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_78A4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0376
    ChrTalk(
        0x101,
        (
            "#12P#0000F──初次见面。\x01",
            "我是克洛斯贝尔警察局·特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02\x03",

            "#0005F那个，您是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        "#5P人家的名字叫米歇尔。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x8,
        (
            "#5P是游击士协会·克洛斯贝尔分部的\x01",
            "接待员哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#5P我从亚里欧斯那里\x01",
            "听说了你们的事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        "#12P#0000F哦，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x102,
        (
            "#12P#0100F不过，没想到您\x01",
            "竟然能认出我们就是支援科的成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#5P呵呵，只要看一下你们胸口的徽章\x01",
            "和你们的脸就知道了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x8,
        (
            "#5P你们的活动内容好像\x01",
            "跟我们游击士协会差不多吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        "#12P#0000F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x103,
        "#11P#0203F嗯，确实无法否认。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        (
            "#12P#0300F游击士协会\x01",
            "果然不会喜欢我们这种部门吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        (
            "#5P哎呀，并没有那回事哦。\x01",
            "我们很欢迎你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        (
            "#5P因为委托实在太多了，\x01",
            "光靠我们的现有成员，\x01",
            "都不太能应付得过来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x8,
        (
            "#5P你们要是能替我们分担一点，\x01",
            "可就帮大忙了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        (
            "#12P#0004F这、这样啊。\x01",
            "听到您这么说，总算稍微安心了一点……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "#5P──不过，\x01",
            "那也要等到你们能派上用场的时候哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0392
    ChrTalk(
        0x101,
        "#12P#0001F唔……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        (
            "#5P虽然这话可能有点过分，\x01",
            "但我们这里的游击士都非常优秀哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x8,
        (
            "#5P亚里欧斯就不用说了，\x01",
            "其他成员……\x01",
            "也全都有着一流的实力哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x8,
        (
            "#5P支援科是警察为了争取民心\x01",
            "而成立的部门，而且成员还全都是新人……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x8,
        (
            "#5P这种部门到底有没有实力\x01",
            "帮我们分担工作，还是个未知数哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        "#12P#0005F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x102,
        "#12P#0108F（……无法反驳啊。）\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x104,
        "#12P#0303F（不过，我们现在可能确实做不到。）\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x8,
        (
            "#5P呵呵，算了，\x01",
            "就不再欺负你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x8,
        (
            "#5P你们呢，就尽你们的所能，\x01",
            "努力加油就行了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x8,
        (
            "#5P就算把事情搞砸了，\x01",
            "也还有我们来解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        "#12P#0001F……我们会努力磨练自己的。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1000, 0, 10150, 0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x47, 2)
    EventEnd(0x5)
    Return()

    # Function_21_74A1 end

    def Function_22_7EDA(): pass

    label("Function_22_7EDA")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(1000, 1300, 10500, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21630, 0)
    SetChrPos(0x101, 1500, 0, 10150, 360)
    SetChrPos(0x102, 500, 0, 9900, 360)
    SetChrPos(0x103, 1500, 0, 8650, 360)
    SetChrPos(0x104, 500, 0, 8400, 360)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 6)), scpexpr(EXPR_END)), "loc_8105")

    #C0404
    ChrTalk(
        0x101,
        (
            "#11P#0005F米歇尔先生，\x01",
            "那个……\x02\x03",

            "#0000F我们按您的\x01",
            "要求来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x8,
        "#5P呵呵……等你们很久了哦。\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x8,
        (
            "#5P我一叫就来，\x01",
            "你们还是很可爱的嘛。\x02",
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

    #C0407
    ChrTalk(
        0x101,
        (
            "#11P#0003F……咳咳，\x01",
            "那个……\x02\x03",

            "#0000F您之前不是说，为了确认\x01",
            "我们的实力，准备了一个什么方案吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x8,
        "#5P记得很清楚嘛。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x8,
        (
            "#5P……你们几个，\x01",
            "愿意做个\x01",
            "测试吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B1")

    label("loc_8105")


    #C0410
    ChrTalk(
        0x8,
        "#5P不过，『特别任务支援科』吗……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "#5P我听说那是在警察局内部的\x01",
            "斗争纠纷中诞生的部门。\x01",
            "那是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x101,
        (
            "#11P#0006F唔……\x01",
            "您、您知道得还真清楚啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x8,
        (
            "#5P你们可不要\x01",
            "小看游击士协会的情报网哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x8,
        (
            "#5P我们掌握着周边各国\x01",
            "的各种传闻和情报哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x8,
        (
            "#5P只要我们愿意，\x01",
            "连埃雷波尼亚的帝都里有多少好男人，\x01",
            "都可以调查得清清楚楚。\x02",
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

    #C0416
    ChrTalk(
        0x104,
        (
            "#12P#0303F（游击士协会的\x01",
            "  情报网确实很有名，\x01",
            "  不过这个比喻也有点太那个了吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x103,
        (
            "#12P#0200F（还有，为什么\x01",
            "  要使用女性的说话方式……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0418
    ChrTalk(
        0x8,
        (
            "#5P不过，也是。\x01",
            "今后也还有许多事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x8,
        (
            "#5P……你们几个，\x01",
            "愿意做个\x01",
            "测试吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83B1")

    SetScenarioFlags(0x4F, 6)

    #C0420
    ChrTalk(
        0x101,
        "#11P#0005F咦……\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        "#12P#0105F测、测试……吗？\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x8,
        (
            "#5P我会从用于培训游击士的\x01",
            "基础知识的笔试问题中，\x01",
            "选择十道问题哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "#5P如果全部回答正确，\x01",
            "就可以判定你们\x01",
            "拥有准游击士程度的知识。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        "#5P反·之·呢～也就是说……\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x103,
        (
            "#12P#0203F如果回答不出那些问题，\x01",
            "在优秀游击士云集的克洛斯贝尔，\x01",
            "我们是发展不下去的……\x02\x03",

            "#0200F对吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        "#11P#0006F突、突然觉得很有压力啊……\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x104,
        (
            "#12P#0306F话说，我们要是答错了，\x01",
            "从今以后可能会一直被当成傻瓜来耍吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x8,
        (
            "#5P呵呵……\x01",
            "我可没有那种恶劣的兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#5P测试的内容，在行政区的图书馆里\x01",
            "差不多都能查得到哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x8,
        (
            "#5P说到底，这只是为了\x01",
            "确认你们是否对克洛斯贝尔\x01",
            "有所助益而已哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x8,
        (
            "#5P……怎么样？\x01",
            "现在就试试看吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x4, 0x4, 0x2)
    OP_29(0x4, 0x1, 0x0)
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_866A")
    Call(0, 25)
    Call(0, 26)

    label("loc_866A")

    SetChrPos(0x0, 1000, 0, 10150, 360)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_22_7EDA end

    def Function_23_8682(): pass

    label("Function_23_8682")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(1000, 1300, 10500, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21630, 0)
    SetChrPos(0x101, 1500, 0, 10150, 360)
    SetChrPos(0x102, 500, 0, 9900, 360)
    SetChrPos(0x103, 1500, 0, 8650, 360)
    SetChrPos(0x104, 500, 0, 8400, 360)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    #C0432
    ChrTalk(
        0x8,
        (
            "#5P我会从用于培训游击士的\x01",
            "基础知识的笔试问题中，\x01",
            "选择１０道问题哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x8,
        (
            "#5P如果全部回答正确，\x01",
            "就可以判定你们拥有准游击士程度的知识。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        (
            "#5P话虽如此，其实全都是一些简单的问题，\x01",
            "在行政区的图书馆差不多都能查得到。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x8,
        (
            "#5P……那么，怎么样？\x01",
            "要试试看吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8822")
    Call(0, 25)
    Call(0, 26)

    label("loc_8822")

    SetChrPos(0x0, 1000, 0, 10150, 360)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_8682 end

    def Function_24_883A(): pass

    label("Function_24_883A")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8911")

    #C0436
    ChrTalk(
        0x101,
        (
            "#11P#0012F唔……\x01",
            "我们还没做好心理准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x8,
        (
            "#5P哎呀，害怕了吗？\x01",
            "没想到你们原来是胆小鬼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x8,
        (
            "#5P算了算了。\x01",
            "如果想做测试了，\x01",
            "再来跟我说哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8911")

    Return()

    # Function_24_883A end

    def Function_25_8912(): pass

    label("Function_25_8912")


    #C0439
    ChrTalk(
        0x101,
        "#11P#0001F……那我们就试试看吧。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x8,
        "#5P嗯，这就对了¤\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0441
    ChrTalk(
        0x104,
        "#12P#0305F喂喂，没问题吧，罗伊德。\x02",
    )

    CloseMessageWindow()

    def lambda_8983():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8983)
    Sleep(50)

    def lambda_8993():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8993)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0442
    ChrTalk(
        0x101,
        (
            "#11P#0003F嗯，基础知识的笔试，\x01",
            "我在警察学校也接受过了。\x02\x03",

            "#0001F最重要的是……\x01",
            "如果在这里退却了，\x01",
            "总感觉好像输了什么一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x102,
        "#6P#0100F……嗯，也是。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        "#12P#0203F同意。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x104,
        (
            "#12P#0300F嗯，听你这么一说，\x01",
            "也有道理啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A89():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A89)

    def lambda_8A96():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A96)

    def lambda_8AA3():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8AA3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0446
    ChrTalk(
        0x8,
        (
            "#5P呵呵……我并不讨厌\x01",
            "这种斗志论哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x8,
        (
            "#5P也是，你看起来就是\x01",
            "他们的队长……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x8,
        (
            "#5P就由你来\x01",
            "回答测试的问题吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        "#11P#0001F……我知道了。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x8,
        (
            "#5P呵呵，眼神不错哦。\x01",
            "让人脊背发寒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x8,
        (
            "#5P那么……\x01",
            "我们就快点开始吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0452
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【米歇尔的挑战书】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    OP_68(1000, 1950, 9200, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20390, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0453
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "游击士协会分部·接待员米歇尔的挑战\x01",
            "　　～游击士·基础知识测试～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0454
    ChrTalk(
        0x8,
        (
            "#5P──第１题！！\x01",
            "先来个简单的问题试试看哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x8,
        (
            "#5P给这片大陆带来导力器的技术革命\x01",
            "被称为『导力革命』……\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x8,
        "#5P那是多少年前发生的呢？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0457
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "『导力革命』发生的时期是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①大约十年前】\x01",        # 0
            "【②大约三十年前】\x01",      # 1
            "【③大约五十年前】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8DD2"),
        (1, "loc_8F28"),
        (2, "loc_907C"),
        (SWITCH_DEFAULT, "loc_91C8"),
    )


    label("loc_8DD2")


    #C0458
    ChrTalk(
        0x101,
        "#12P#0000F……大约十年前吧。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0460
    ChrTalk(
        0x8,
        (
            "#5P错！！回答错误！\x01",
            "不可能离现在这么近吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        "#5P正确答案是：大约五十年前。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "#5P短短半个世纪之内，\x01",
            "导力器就能发展到现在这种程度，\x01",
            "实在很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x8,
        (
            "#5P我小时候，\x01",
            "从来都没想过有一天\x01",
            "会出现导力车这种交通工具哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯，开头\x01",
            "  就答错了啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91C8")

    label("loc_8F28")


    #C0465
    ChrTalk(
        0x101,
        "#12P#0000F……大约三十年前吧。\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0467
    ChrTalk(
        0x8,
        (
            "#5P错！！回答错误！\x01",
            "可不能随便乱猜哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        "#5P正确答案是：大约五十年前。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x8,
        (
            "#5P短短半个世纪之内，\x01",
            "导力器就能发展到现在这种程度，\x01",
            "实在很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x8,
        (
            "#5P我小时候，\x01",
            "从来都没想过有一天\x01",
            "会出现导力车这种交通工具哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯，开头\x01",
            "  就答错了啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91C8")

    label("loc_907C")


    #C0472
    ChrTalk(
        0x101,
        "#12P#0000F……大约五十年前吧。\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0474
    ChrTalk(
        0x8,
        "#5P没错！回答正确！\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        "#5P不过，这种问题只是常识而已。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x8,
        (
            "#5P话说回来，短短半个世纪之内，\x01",
            "导力器就能发展到现在这种程度，\x01",
            "实在很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x8,
        (
            "#5P我小时候，\x01",
            "从来都没想过有一天\x01",
            "会出现导力车这种交通工具哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        "#12P#0004F（开头还算顺利。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_91C8")

    label("loc_91C8")


    #C0479
    ChrTalk(
        0x8,
        (
            "#5P接着问了哦～\x01",
            "──第２题！！\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x8,
        (
            "#5P『导力革命』发生的主要原因是\x01",
            "某个人物发明了原始型号的导力器。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x8,
        (
            "#5P发明出导力器的人物的名字……\x01",
            "你们应该知道吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0482
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "发明出导力器的人物是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①Ａ·拉塞尔博士】\x01",          # 0
            "【②Ｃ·爱普斯泰恩博士】\x01",      # 1
            "【③Ｇ·修米特博士】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_931C"),
        (1, "loc_957A"),
        (2, "loc_979A"),
        (SWITCH_DEFAULT, "loc_99E8"),
    )


    label("loc_931C")


    #C0483
    ChrTalk(
        0x101,
        "#12P#0000F……是Ａ·拉塞尔博士吧？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0485
    ChrTalk(
        0x8,
        "#5P错！！真可惜，回答错误哦。\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x8,
        "#5P正确答案是：Ｃ·爱普斯泰恩博士。\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x8,
        (
            "#5P爱普斯泰恩博士发明的导力器，\x01",
            "刚开始并不被\x01",
            "人们所接受哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x8,
        (
            "#5P不过，后来人们逐渐认识到其出色的便利性，\x01",
            "所以导力器现在便成为了\x01",
            "我们生活中必不可少之物。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x8,
        (
            "#5P顺便一提，拉塞尔博士是\x01",
            "爱普斯泰恩博士的弟子，\x01",
            "对『导力革命』也有着巨大贡献。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯……\x01",
            "  如此说来，以前好像听说过呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x103,
        (
            "#12P#0200F再补充一点……\x01",
            "爱普斯泰恩财团就是\x01",
            "我所属的团体。\x02\x03",

            "#0211F前段时间不是刚说过吗……\x01",
            "忘记了？\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x101,
        (
            "#12P#0003F唔……\x01",
            "（目光好锐利……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99E8")

    label("loc_957A")


    #C0493
    ChrTalk(
        0x101,
        "#12P#0000F……Ｃ·爱普斯泰恩博士吧。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0495
    ChrTalk(
        0x8,
        "#5P没错！！回答正确哦。\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x8,
        (
            "#5P爱普斯泰恩博士发明的导力器，\x01",
            "刚开始并不被\x01",
            "人们所接受哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x8,
        (
            "#5P不过，后来人们逐渐认识到其出色的便利性，\x01",
            "所以导力器现在便成为了\x01",
            "我们生活中必不可少之物。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x103,
        (
            "#12P#0203F财团为了导力器的研究和推广，\x01",
            "进行了很多活动，这点\x01",
            "已经是家喻户晓的了。\x02\x03",

            "#0200F我所进行的魔导杖实战测试\x01",
            "也是其中一环。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        (
            "#12P#0003F（对啊，缇欧也是\x01",
            "  爱普斯泰恩财团的成员。）\x02\x03",

            "#0000F（……好险好险，\x01",
            "  如果回答错误，真不知会被她怎样教训啊……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_99E8")

    label("loc_979A")


    #C0500
    ChrTalk(
        0x101,
        "#12P#0000F……Ｇ·修米特博士吧？\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0502
    ChrTalk(
        0x8,
        "#5P错！！回答错误。\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x8,
        "#5P正确答案是：Ｃ·爱普斯泰恩博士。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x8,
        (
            "#5P爱普斯泰恩博士发明的导力器，\x01",
            "刚开始并不被\x01",
            "人们所接受哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x8,
        (
            "#5P不过，后来人们逐渐认识到其出色的便利性，\x01",
            "所以导力器现在便成为了\x01",
            "我们生活中必不可少之物。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x8,
        (
            "#5P顺便一提，修米特博士是\x01",
            "爱普斯泰恩博士的弟子，\x01",
            "被称为机械工程学的权威哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯……\x01",
            "  如此说来，以前好像听说过呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x103,
        (
            "#12P#0203F再补充一点……\x01",
            "爱普斯泰恩财团就是\x01",
            "我所属的团体。\x02\x03",

            "#0211F前段时间不是刚说过吗……\x01",
            "忘记了？\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        (
            "#12P#0003F唔……\x01",
            "（目光好锐利……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99E8")

    label("loc_99E8")


    #C0510
    ChrTalk(
        0x8,
        "#5P接下来──第３题！！\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x8,
        (
            "#5P众所周知，\x01",
            "结晶回路是导力器的核心部分。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x8,
        (
            "#5P制作结晶回路，\x01",
            "耀晶片是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x8,
        (
            "#5P那么……耀晶片是指，\x01",
            "七耀石的何种\x01",
            "形态呢？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0514
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "耀晶片\x01",
            "是指……？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①七耀石的结晶】\x01",        # 0
            "【②七耀石的加工品】\x01",      # 1
            "【③七耀石的碎片】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9B3B"),
        (1, "loc_9CA8"),
        (2, "loc_9E17"),
        (SWITCH_DEFAULT, "loc_9F52"),
    )


    label("loc_9B3B")


    #C0515
    ChrTalk(
        0x101,
        "#12P#0000F……七耀石的结晶。\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0517
    ChrTalk(
        0x8,
        "#5P错！！回答错误！\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x8,
        "#5P正确答案是：七耀石的碎片哦。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x8,
        (
            "#5P将碎片形态的七耀石\x01",
            "加工后就能制成结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x8,
        (
            "#5P魔兽都有被七耀石吸引\x01",
            "的特性，\x01",
            "经常会吞下耀晶片。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        (
            "#5P所以要收集耀晶片的话，\x01",
            "打败魔兽\x01",
            "是最便捷的方法哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯……\x01",
            "  原来这问题已经是特别优待了吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F52")

    label("loc_9CA8")


    #C0523
    ChrTalk(
        0x101,
        "#12P#0000F……七耀石的加工品。\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0525
    ChrTalk(
        0x8,
        "#5P错！！回答错误！\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x8,
        "#5P正确答案是：七耀石的碎片哦。\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "#5P将碎片形态的七耀石\x01",
            "加工后就能制成结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x8,
        (
            "#5P魔兽都有被七耀石吸引\x01",
            "的特性，\x01",
            "经常会吞下耀晶片。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x8,
        (
            "#5P所以要收集耀晶片的话，\x01",
            "打败魔兽\x01",
            "是最便捷的方法哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯……\x01",
            "　原来这问题已经是特别优待了吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F52")

    label("loc_9E17")


    #C0531
    ChrTalk(
        0x101,
        "#12P#0000F……七耀石的碎片。\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0533
    ChrTalk(
        0x8,
        "#5P没错！！回答正确！\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x8,
        (
            "#5P将碎片形态的七耀石\x01",
            "加工后就能制成结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x8,
        (
            "#5P魔兽都有被七耀石吸引\x01",
            "的特性，\x01",
            "经常会吞下耀晶片。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x8,
        (
            "#5P所以要收集耀晶片的话，\x01",
            "打败魔兽\x01",
            "是最便捷的方法哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x101,
        "#12P#0004F（嗯，这是常识啊。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_9F52")

    label("loc_9F52")


    #C0538
    ChrTalk(
        0x8,
        "#5P接下来──第４题！！\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x8,
        (
            "#5P位于克洛斯贝尔自治州西部的\x01",
            "『埃雷波尼亚帝国』──\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x8,
        (
            "#5P对我们这些克洛斯贝尔的居民来说，\x01",
            "那是一个十分巨大的国家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x8,
        (
            "#5P作为埃雷波尼亚帝国的象征\x01",
            "被绘于国徽上的图案……\x01",
            "你们应该知道是什么吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0542
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "埃雷波尼亚帝国\x01",
            "国徽上的图案是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①支援护臂甲】\x01",      # 0
            "【②白隼】\x01",            # 1
            "【③黄金战马】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A0E1"),
        (1, "loc_A23A"),
        (2, "loc_A37C"),
        (SWITCH_DEFAULT, "loc_A4E8"),
    )


    label("loc_A0E1")


    #C0543
    ChrTalk(
        0x101,
        "#12P#0000F……支援护臂甲吧？\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0545
    ChrTalk(
        0x8,
        "#5P错！！回答错误。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x8,
        "#5P正确答案是：黄金战马。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x8,
        (
            "#5P众所周知，身为军事大国的帝国\x01",
            "最引以为傲的就是其强大的军事实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x8,
        (
            "#5P而国徽上所绘的黄金战马\x01",
            "就象征着其军事实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x8,
        (
            "#5P而支援护臂甲是\x01",
            "游击士协会的徽章哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯……\x01",
            "  问题越来越难了啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4E8")

    label("loc_A23A")


    #C0551
    ChrTalk(
        0x101,
        "#12P#0000F……白隼……吧？\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0553
    ChrTalk(
        0x8,
        "#5P错！！回答错误。\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x8,
        "#5P正确答案是：黄金战马。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x8,
        (
            "#5P众所周知，身为军事大国的帝国\x01",
            "最引以为傲的就是其强大的军事实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x8,
        (
            "#5P而国徽上所绘的黄金战马\x01",
            "就象征着其军事实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x8,
        (
            "#5P而白隼是\x01",
            "利贝尔王国的国徽哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x101,
        "#12P#0006F（哈、哈哈……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_A4E8")

    label("loc_A37C")


    #C0559
    ChrTalk(
        0x101,
        "#12P#0000F……好像是，黄金战马吧？\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0561
    ChrTalk(
        0x8,
        "#5P没错！！回答正确。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x8,
        (
            "#5P众所周知，身为军事大国的帝国\x01",
            "最引以为傲的就是其强大的军事实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x8,
        (
            "#5P而国徽上所绘的黄金战马\x01",
            "就象征着其军事实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x8,
        (
            "#5P从前，帝国活跃着一支名叫铁骑队\x01",
            "的大规模骑兵部队，\x01",
            "那就是黄金战马的原型。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        "#12P#0004F（好！总算是回答正确了。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_A4E8")

    label("loc_A4E8")


    #C0566
    ChrTalk(
        0x8,
        (
            "#5P──第５题！！\x01",
            "快要进行到一半了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x8,
        (
            "#5P帝国的相反方向……\x01",
            "也就是克洛斯贝尔自治州的东部，\x01",
            "有个叫『卡尔瓦德共和国』的国家。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x8,
        (
            "#5P毫不夸张地说，\x01",
            "克洛斯贝尔的整个历史，就是\x01",
            "帝国和共和国这两个大国长期对峙的过程。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x8,
        (
            "#5P那么，卡尔瓦德共和国\x01",
            "以导力枪和重工业闻名的\x01",
            "导力器制造商叫做什么？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0570
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "位于共和国的\x01",
            "著名导力器制造商的名称是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①乌尔努公司】\x01",          # 0
            "【②莱恩福尔特公司】\x01",      # 1
            "【③蔡斯中央工房】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A6CE"),
        (1, "loc_A821"),
        (2, "loc_AA09"),
        (SWITCH_DEFAULT, "loc_ABE3"),
    )


    label("loc_A6CE")


    #C0571
    ChrTalk(
        0x101,
        "#12P#0000F……那当然是乌尔努公司。\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0573
    ChrTalk(
        0x8,
        "#5P没错！！回答正确回答正确！\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x8,
        (
            "#5P共和国的乌尔努公司和\x01",
            "帝国的莱恩福尔特公司\x01",
            "是两大著名的导力枪制造商。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x8,
        (
            "#5P实际上这两家公司也正在开发\x01",
            "导力车和导力巴士，\x01",
            "业务范围很广泛哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        (
            "#12P#0004F（呼……\x01",
            "  虽然有点难以区分，\x01",
            "  但总算没答错。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_ABE3")

    label("loc_A821")


    #C0577
    ChrTalk(
        0x101,
        (
            "#12P#0000F……莱恩福尔特公司，\x01",
            "好像有点印象……\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0579
    ChrTalk(
        0x8,
        "#5P错！！真可惜，回答错误！\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x8,
        (
            "#5P正确答案是：乌尔努公司哦。\x01",
            "虽然比较难以区分，\x01",
            "不过莱恩福尔特公司位于帝国哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x8,
        (
            "#5P共和国的乌尔努公司和\x01",
            "帝国的莱恩福尔特公司\x01",
            "是两大著名的导力枪制造商。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x8,
        (
            "#5P实际上这两家公司也正在开发\x01",
            "导力车和导力巴士，\x01",
            "业务范围很广泛哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x102,
        (
            "#5P#0106F呼……为什么连这种问题\x01",
            "也会答错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x101,
        (
            "#12P#0003F（这种问题对使用导力枪的艾莉来说，\x01",
            "  应该再简单不过了啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABE3")

    label("loc_AA09")


    #C0585
    ChrTalk(
        0x101,
        (
            "#12P#0000F……蔡斯中央工房，\x01",
            "我记得好像是叫这个……\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0587
    ChrTalk(
        0x8,
        "#5P错！！真可惜，回答错误！\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x8,
        (
            "#5P正确答案是：乌尔努公司哦。\x01",
            "蔡斯中央工房是\x01",
            "利贝尔王国的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x8,
        (
            "#5P共和国的乌尔努公司和\x01",
            "帝国的莱恩福尔特公司\x01",
            "是两大著名的导力枪制造商。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x8,
        (
            "#5P实际上这两家公司也正在开发\x01",
            "导力车和导力巴士，\x01",
            "业务范围很广泛哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x102,
        (
            "#5P#0106F呼……为什么连这种问题\x01",
            "也会答错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#12P#0003F（这种问题对使用导力枪的艾莉来说，\x01",
            "  应该再简单不过了啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABE3")

    label("loc_ABE3")


    #C0593
    ChrTalk(
        0x8,
        (
            "#5P……那么，总算\x01",
            "进行到一半了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AD7D")

    #C0594
    ChrTalk(
        0x103,
        (
            "#12P#0200F……现在状态\x01",
            "还算不错哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AC48():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC48)
    Sleep(50)

    def lambda_AC58():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC58)

    def lambda_AC65():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC65)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0595
    ChrTalk(
        0x104,
        (
            "#6P#0309F队长，不赖嘛。\x01",
            "按这种势头的话，接下来的还不都手到擒来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x102,
        (
            "#5P#0102F嗯，说实话我也很惊讶哦。\x01",
            "很厉害嘛，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x101,
        (
            "#11P#0012F哈哈……还行吧，\x01",
            "因为只是基础知识，\x01",
            "所以我才能回答上来的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AD4A():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD4A)

    def lambda_AD57():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD57)

    def lambda_AD64():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AD64)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_AFA3")

    label("loc_AD7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE89")

    #C0598
    ChrTalk(
        0x103,
        "#12P#0200F小错不少啊。\x02",
    )

    CloseMessageWindow()

    def lambda_ADAD():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ADAD)
    Sleep(50)

    def lambda_ADBD():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADBD)

    def lambda_ADCA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ADCA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0599
    ChrTalk(
        0x104,
        "#6P#0303F只能算是马马虎虎啊。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x102,
        (
            "#5P#0106F是啊……\x01",
            "必须再加把劲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x101,
        "#11P#0006F我、我会努力扳回局面的。\x02",
    )

    CloseMessageWindow()

    def lambda_AE56():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE56)

    def lambda_AE63():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE63)

    def lambda_AE70():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AE70)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_AFA3")

    label("loc_AE89")


    #C0602
    ChrTalk(
        0x103,
        (
            "#12P#0211F……不好好学习\x01",
            "就是这种后果啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AEBD():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AEBD)
    Sleep(50)

    def lambda_AECD():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AECD)

    def lambda_AEDA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AEDA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0603
    ChrTalk(
        0x104,
        (
            "#6P#0306F确实如此啊，\x01",
            "后面的问题真是让人担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x102,
        (
            "#5P#0103F是啊……\x01",
            "必须得努力扳回局面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x101,
        "#11P#0003F惭、惭愧万分……\x02",
    )

    CloseMessageWindow()

    def lambda_AF75():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF75)

    def lambda_AF82():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF82)

    def lambda_AF8F():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF8F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    label("loc_AFA3")


    #C0606
    ChrTalk(
        0x8,
        (
            "#5P呵呵，不管是对是错，总之还剩五题哦。\x01",
            "你要好好加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x8,
        (
            "#5P接下来的问题\x01",
            "将会更难，\x01",
            "做好心理准备哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x8,
        "#5P──那么，第６题！\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x8,
        (
            "#5P很早以前，这片塞姆里亚大陆上\x01",
            "曾经发生过一场灾难，它被后人称为『大崩坏』。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x8,
        (
            "#5P因为那场灾难而丧失了文明的人们，\x01",
            "分成了各个势力，在五百年间\x01",
            "持续着无休止的战争。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x8,
        (
            "#5P之后，那个被称为『黑暗时代』的时期\x01",
            "被某个势力所终结。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x8,
        (
            "#5P起源于『黑暗时代』时期的塞姆里亚大陆，\x01",
            "并在当时创造了新秩序的势力……\x01",
            "你们应该知道指的是什么吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0613
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "终结了『黑暗时代』的势力是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①七耀教会】\x01",        # 0
            "【②游击士协会】\x01",      # 1
            "【③钓公师团】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B225"),
        (1, "loc_B3F8"),
        (2, "loc_B60F"),
        (SWITCH_DEFAULT, "loc_B82C"),
    )


    label("loc_B225")


    #C0614
    ChrTalk(
        0x101,
        "#12P#0000F……是七耀教会吧。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0616
    ChrTalk(
        0x8,
        "#5P没错！！回答正确！\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x8,
        (
            "#5P于七耀历五百年左右出现的七耀教会，\x01",
            "通过救济民众等社会活动，\x01",
            "广泛向人们传播了『空之女神』的教诲。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x8,
        (
            "#5P其影响力之强，甚至达到了连\x01",
            "当时支配着『黑暗时代』的贵族和骑士阶级\x01",
            "也无法忽视的地步，并渐渐创造了新的秩序哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x8,
        (
            "#5P迄今为止，七耀教会所推崇的『空之女神』的教诲，\x01",
            "已经广泛渗入了这片塞姆里亚大陆的每个角落。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x101,
        "#12P#0004F（ＯＫ，状态不错。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_B82C")

    label("loc_B3F8")


    #C0621
    ChrTalk(
        0x101,
        "#12P#0000F……是游击士协会吧。\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0623
    ChrTalk(
        0x8,
        "#5P错！！回·答·错·误！\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x8,
        (
            "#5P正确答案是：七耀教会哦。\x01",
            "……真是的，这可是常识中的常识啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x8,
        (
            "#5P于七耀历五百年左右出现的七耀教会，\x01",
            "通过救济民众等社会活动，\x01",
            "广泛向人们传播了『空之女神』的教诲。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x8,
        (
            "#5P其影响力之强，甚至达到了连\x01",
            "当时支配着『黑暗时代』的贵族和骑士阶级，\x01",
            "也无法忽视的地步，并渐渐创造了新的秩序哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x8,
        (
            "#5P迄今为止，七耀教会所推崇的『空之女神』的教诲，\x01",
            "已经广泛渗入了这片塞姆里亚大陆的每个角落。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x101,
        "#12P#0006F（是我想太多了呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_B82C")

    label("loc_B60F")


    #C0629
    ChrTalk(
        0x101,
        "#12P#0000F……是钓公师团吧。\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0631
    ChrTalk(
        0x8,
        "#5P错！！回·答·错·误！\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x8,
        (
            "#5P正确答案是：七耀教会哦。\x01",
            "……话说回来，钓公师团不就是我们的邻居嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x8,
        (
            "#5P于七耀历五百年左右出现的七耀教会，\x01",
            "通过救济民众等社会活动，\x01",
            "广泛向人们传播了『空之女神』的教诲。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x8,
        (
            "#5P其影响力之强，甚至达到了连\x01",
            "当时支配着『黑暗时代』的贵族和骑士阶级，\x01",
            "也无法忽视的地步，并渐渐创造了新的秩序哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x8,
        (
            "#5P迄今为止，七耀教会所推崇的『空之女神』的教诲，\x01",
            "已经广泛渗入了这片塞姆里亚大陆的每个角落。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x101,
        "#12P#0006F（是我想太多了呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_B82C")

    label("loc_B82C")


    #C0637
    ChrTalk(
        0x8,
        "#5P接下来──第７题！\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x8,
        (
            "#5P七耀教会的总部\x01",
            "位于一个名叫『亚尔特利亚法典国』的国家。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x8,
        (
            "#5P亚尔特利亚法典国的\x01",
            "国家体制由各个不同的\x01",
            "行政机关所构成。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x8,
        (
            "#5P那些行政机关中，\x01",
            "全权负责七耀教会祭祀仪式的机关\x01",
            "叫做什么……你们知道吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0641
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "全权负责七耀教会祭祀仪式的\x01",
            "行政机关的名称是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①僧兵厅】\x01",      # 0
            "【②典礼省】\x01",      # 1
            "【③封圣省】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B9C8"),
        (1, "loc_BB2E"),
        (2, "loc_BC73"),
        (SWITCH_DEFAULT, "loc_BDFC"),
    )


    label("loc_B9C8")


    #C0642
    ChrTalk(
        0x101,
        "#12P#0000F……是僧兵厅吗？\x02",
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0644
    ChrTalk(
        0x8,
        "#5P错～！！真可惜，回答错误哦。\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x8,
        (
            "#5P僧兵厅是负责守卫亚尔特利亚法典国\x01",
            "的行政机关。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x8,
        "#5P正确答案是：典礼省哦。\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x8,
        (
            "#5P各地教会和圣堂里的\x01",
            "祭司差不多都是隶属于\x01",
            "这个机关的人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x8,
        (
            "#5P克洛斯贝尔市北出口\x01",
            "也有个大圣堂，\x01",
            "我偶尔会去那里祷告哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        "#12P#0006F（嗯，好难啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_BDFC")

    label("loc_BB2E")


    #C0650
    ChrTalk(
        0x101,
        "#12P#0000F……是典礼省吗？\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0652
    ChrTalk(
        0x8,
        "#5P没错！！回答正确哦！\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x8,
        (
            "#5P各地教会和圣堂里的\x01",
            "祭司差不多都是隶属于\x01",
            "这个机关的人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x8,
        (
            "#5P克洛斯贝尔市的北出口\x01",
            "也有个大圣堂，\x01",
            "我偶尔会去那里祷告哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x8,
        (
            "#5P那里的主教阁下好像\x01",
            "也是典礼省出身的。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x101,
        "#12P#0004F（很好，状态不错。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_BDFC")

    label("loc_BC73")


    #C0657
    ChrTalk(
        0x101,
        "#12P#0000F……是封圣省吗？\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0659
    ChrTalk(
        0x8,
        "#5P错～！！真可惜，回答错误哦。\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x8,
        (
            "#5P封圣省是调查·管理女神圣物\x01",
            "相关事宜的机关。\x01",
            "不过该机关的详细情况并不对外公开。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x8,
        "#5P正确答案是：典礼省哦。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x8,
        (
            "#5P各地教会和圣堂里的\x01",
            "祭司差不多都是隶属于\x01",
            "这个机关的人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x8,
        (
            "#5P克洛斯贝尔市的北出口\x01",
            "也有个大圣堂，\x01",
            "我偶尔会去那里祷告哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x101,
        "#12P#0006F（嗯，好难啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_BDFC")

    label("loc_BDFC")


    #C0665
    ChrTalk(
        0x8,
        (
            "#5P测试快要结束了哦。\x01",
            "──第８题！\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x8,
        (
            "#5P游击士协会在大陆各地\x01",
            "都设有分部。\x01",
            "那么……\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x8,
        (
            "#5P游击士协会的总部\x01",
            "位于哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0668
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "游击士协会的总部位于？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①克洛斯贝尔自治州】\x01",      # 0
            "【②列曼自治州】\x01",            # 1
            "【③奥雷德自治州】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BF29"),
        (1, "loc_C081"),
        (2, "loc_C189"),
        (SWITCH_DEFAULT, "loc_C2A9"),
    )


    label("loc_BF29")


    #C0669
    ChrTalk(
        0x101,
        "#12P#0000F……是克洛斯贝尔自治州。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0671
    ChrTalk(
        0x8,
        "#5P错～！！回答错误哦。\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x8,
        "#5P正确答案是：列曼自治州。\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x8,
        (
            "#5P那里是游击士协会的\x01",
            "投资方爱普斯泰恩财团的\x01",
            "所在地哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x8,
        (
            "#5P发生重大事件时，\x01",
            "总部有时也会\x01",
            "下达动员命令。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#12P#0006F（是、是这样啊。\x01",
            "  说起来，在克洛斯贝尔确实\x01",
            "  从未见过协会的总部呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A9")

    label("loc_C081")


    #C0676
    ChrTalk(
        0x101,
        (
            "#12P#0000F……那当然是\x01",
            "列曼自治州吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0678
    ChrTalk(
        0x8,
        "#5P没错～！！回答正确哦。\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x8,
        (
            "#5P那里是游击士协会的\x01",
            "投资方爱普斯泰恩财团的\x01",
            "所在地哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x8,
        (
            "#5P发生重大事件时，\x01",
            "总部有时也会\x01",
            "下达动员命令。\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#12P#0004F（哦……）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_C2A9")

    label("loc_C189")


    #C0682
    ChrTalk(
        0x101,
        "#12P#0000F……是奥雷德自治州吗？\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0684
    ChrTalk(
        0x8,
        "#5P错！！回答错误哦。\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x8,
        "#5P正确答案是：列曼自治州。\x02",
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x8,
        (
            "#5P那里是游击士协会的\x01",
            "投资方爱普斯泰恩财团的\x01",
            "所在地哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x8,
        (
            "#5P发生重大事件时，\x01",
            "总部有时也会\x01",
            "下达动员命令。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x101,
        "#12P#0006F（啊，答错了吗……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_C2A9")

    label("loc_C2A9")


    #C0689
    ChrTalk(
        0x8,
        "#5P──第９题！\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x8,
        (
            "#5P埃雷波尼亚帝国\x01",
            "有一位远近驰名的\x01",
            "『怪盗』。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x8,
        (
            "#5P善用记载着语言游戏的犯罪预告卡片，\x01",
            "将盗取来的美术品套现后再分给众人的侠盗行为，\x01",
            "还有遮掩住真实容貌的神秘面具……\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x8,
        (
            "#5P听说有些人甚至\x01",
            "把他当成英雄来崇拜。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x8,
        (
            "#5P那么，这个怪盗\x01",
            "的别称……\x01",
            "你们知道吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0694
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "数年前在帝国现身的\x01",
            "『怪盗』的别称是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①怪盗Ａ】\x01",      # 0
            "【②怪盗Ｂ】\x01",      # 1
            "【③怪盗Ｃ】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C46C"),
        (1, "loc_C64B"),
        (2, "loc_C811"),
        (SWITCH_DEFAULT, "loc_C9C1"),
    )


    label("loc_C46C")


    #C0695
    ChrTalk(
        0x101,
        "#12P#0000F……好像是怪盗Ａ吧……\x02",
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0697
    ChrTalk(
        0x8,
        (
            "#5P错错错！！回答错误！\x01",
            "这种类似于少年Ａ的称呼，还真有警察的风格呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x8,
        "#5P正确答案是：怪盗Ｂ――\x02",
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x8,
        (
            "#5P怪盗Ｂ不仅在帝国，\x01",
            "在大陆各地也都很有名气，\x01",
            "是个身份不明，神出鬼没的大盗哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x8,
        (
            "#5P他行窃的目标可谓千差万别。\x01",
            "从美术馆的画到\x01",
            "战车之类的，都是他的目标。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        (
            "#5P最近，在利贝尔\x01",
            "也传闻有东西被他盗取了。\x01",
            "今后你们说不定也会跟他打交道哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯……对别国的事件\x01",
            "  不够关注啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9C1")

    label("loc_C64B")


    #C0703
    ChrTalk(
        0x101,
        "#12P#0000F……是怪盗Ｂ……吧？\x02",
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0705
    ChrTalk(
        0x8,
        (
            "#5P没错！！\x01",
            "其它国家的事情你也知道得很清楚嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x8,
        (
            "#5P怪盗Ｂ……不仅在帝国，\x01",
            "在大陆各地也都很有名气，\x01",
            "是个身份不明，神出鬼没的大盗哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x8,
        (
            "#5P他行窃的目标可谓千差万别。\x01",
            "从美术馆的画到\x01",
            "战车之类的，都是他的目标。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x8,
        (
            "#5P最近，在利贝尔\x01",
            "也传闻有东西被他盗取了。\x01",
            "今后你们说不定也会跟他打交道哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x101,
        (
            "#12P#0006F（虽然是传说中的人物……\x01",
            "  但我可不想跟他打交道啊。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_C9C1")

    label("loc_C811")


    #C0710
    ChrTalk(
        0x101,
        "#12P#0000F……是怪盗Ｃ……吧？\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0712
    ChrTalk(
        0x8,
        "#5P错错错！！回答错误！\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x8,
        "#5P正确答案是：怪盗Ｂ――\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x8,
        (
            "#5P怪盗Ｂ不仅在帝国，\x01",
            "在大陆各地也都很有名气，\x01",
            "是个身份不明，神出鬼没的大盗哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x8,
        (
            "#5P他行窃的目标可谓千差万别。\x01",
            "从美术馆的画到\x01",
            "战车之类的，都是他的目标。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x8,
        (
            "#5P最近，在利贝尔\x01",
            "也传闻有东西被他盗取了。\x01",
            "今后你们说不定也会跟他打交道哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯……对别国的事件\x01",
            "  不够关注啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9C1")

    label("loc_C9C1")


    #C0718
    ChrTalk(
        0x8,
        (
            "#5P──第１０题！\x01",
            "那么，终于到最后一题了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x8,
        (
            "#5P为了争夺克洛斯贝尔的\x01",
            "所有权，帝国与共和国\x01",
            "持续了长时间的对立关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x8,
        (
            "#5P至今为止，两国间已经为此进行过好几次战争了，\x01",
            "牵连了许多无辜的民众。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x8,
        (
            "#5P严峻的事态引起了\x01",
            "利贝尔王国的女王·艾莉茜雅Ⅱ世的重视，\x01",
            "为了解决问题，艾莉茜雅女王提出了某个条约。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x8,
        (
            "#5P就是前年\x01",
            "利贝尔、帝国、共和国三个国家\x01",
            "共同签订的条约。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x8,
        (
            "#5P那个重要条约的名称……\x01",
            "你们身为克洛斯贝尔的居民，当然是知道的吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0724
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "利贝尔、帝国、共和国三个国家\x01",
            "共同签订的条约的名称是？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①互不干涉条约】\x01",      # 0
            "【②互不侵犯条约】\x01",      # 1
            "【③互不妨碍条约】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CC47"),
        (1, "loc_CE9F"),
        (2, "loc_D0DB"),
        (SWITCH_DEFAULT, "loc_D344"),
    )


    label("loc_CC47")


    #C0725
    ChrTalk(
        0x101,
        "#12P#0000F……是《互不干涉条约》吧。\x02",
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0727
    ChrTalk(
        0x8,
        (
            "#5P错！！！！回答错误！\x01",
            "真是的，你要争气点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x8,
        "#5P正确答案是：《互不侵犯条约》哦。\x02",
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x8,
        (
            "#5P这是为了不动用武力，而是\x01",
            "通过对话来解决\x01",
            "三国间对立的条约哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x8,
        (
            "#5P在这个条约签订之前，\x01",
            "整个克洛斯贝尔自治州\x01",
            "都处于极度紧张的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x8,
        (
            "#5P详细情况我就不多说了，不过当时两大国的机甲师团\x01",
            "都在国界附近反复进行着大规模的军事演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x8,
        (
            "#5P只要一步走错，\x01",
            "就有可能酿成一场惨案……\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x8,
        (
            "#5P为了打破那个局面，\x01",
            "艾莉茜雅女王才提出了这个条约哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x8,
        "#5P呵呵，真该好好感谢利贝尔啊。\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x101,
        "#12P#0006F（糟糕，这都答错了啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_D344")

    label("loc_CE9F")


    #C0736
    ChrTalk(
        0x101,
        "#12P#0000F……是《互不侵犯条约》吧。\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0738
    ChrTalk(
        0x8,
        (
            "#5P没错！！回答得非常正确！\x01",
            "这种常识，\x01",
            "当然是要有所了解的。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x8,
        (
            "#5P这是为了不动用武力，而是\x01",
            "通过对话来解决\x01",
            "三国间对立的条约哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x8,
        (
            "#5P在这个条约签订之前，\x01",
            "整个克洛斯贝尔自治州\x01",
            "都处于极度紧张的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x8,
        (
            "#5P详细情况我就不多说了，不过当时两大国的机甲师团\x01",
            "都在国界附近反复进行着大规模的军事演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x8,
        (
            "#5P只要一步走错，\x01",
            "就有可能酿成一场惨案……\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x8,
        (
            "#5P为了打破那个局面，\x01",
            "艾莉茜雅女王才提出了这个条约哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x8,
        "#5P呵呵，真该好好感谢利贝尔啊。\x02",
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        "#12P#0004F（好，答对了。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D344")

    label("loc_D0DB")


    #C0746
    ChrTalk(
        0x101,
        "#12P#0000F……是《互不妨碍条约》吧。\x02",
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0748
    ChrTalk(
        0x8,
        (
            "#5P错！！！！回答错误！\x01",
            "真是的，你要争气点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x8,
        "#5P正确答案是：《互不侵犯条约》哦。\x02",
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x8,
        (
            "#5P这是为了不动用武力，而是\x01",
            "通过对话来解决\x01",
            "三国间对立的条约哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x8,
        (
            "#5P在这条约签订之前，\x01",
            "整个克洛斯贝尔自治州\x01",
            "都处于极度紧张的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x8,
        (
            "#5P详细情况我就不多说了，不过当时两大国的机甲师团\x01",
            "都在国界附近反复进行着大规模的军事演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x8,
        (
            "#5P只要一步走错，\x01",
            "就有可能酿成一场惨案……\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x8,
        (
            "#5P为了打破那个局面，\x01",
            "艾莉茜雅女王才提出了这个条约哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x8,
        "#5P呵呵，真该好好感谢利贝尔啊。\x02",
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯，虽然知道条约内容，\x01",
            "  但还是答错了啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D344")

    label("loc_D344")


    #C0757
    ChrTalk(
        0x8,
        "#5P──测试就到此为止了哦。\x02",
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x8,
        "#5P呵呵，辛苦你们了。\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x101,
        "#12P#0006F（啊，终于结束了……）\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_25_8912 end

    def Function_26_D3B7(): pass

    label("Function_26_D3B7")

    OP_68(1000, 1300, 10500, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21630, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0760
    ChrTalk(
        0x8,
        "#5P──那么……来看看测试的结果吧……\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        "#11P#0001F（忐忑不安……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D74B")

    #C0762
    ChrTalk(
        0x8,
        (
            "#5P回答完全正确……\x01",
            "你的知识已经充分达到了\x01",
            "准游击士的水平。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x8,
        (
            "#5P呵呵，这样看来，你还是\x01",
            "比较值得期待的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x101,
        (
            "#11P#0000F十分感谢。\x01",
            "（没想到竟然会这么坦率地表扬我……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0765
    ChrTalk(
        0x104,
        "#12P#0300F总算松了口气了啊。\x02",
    )

    CloseMessageWindow()

    def lambda_D531():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D531)
    Sleep(50)

    def lambda_D541():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D541)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0766
    ChrTalk(
        0x102,
        (
            "#12P#0100F嗯，没想到罗伊德竟然\x01",
            "连专业外的问题都能答对。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x103,
        (
            "#12P#0200F我都想让他帮忙\x01",
            "补充数据了。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        "#11P#0012F哈哈，你们过奖了。\x02",
    )

    CloseMessageWindow()

    def lambda_D5E0():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D5E0)

    def lambda_D5ED():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D5ED)

    def lambda_D5FA():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D5FA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0769
    ChrTalk(
        0x8,
        (
            "#5P那么……\x01",
            "这是对你完美表现的奖励，\x01",
            "收下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0770
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x7F, 1)

    #C0771
    ChrTalk(
        0x101,
        (
            "#11P#0005F哇……\x01",
            "可、可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x8,
        (
            "#5P嗯，说实话，\x01",
            "我都没想到你能做得这么好。\x01",
            "这也算是我轻视了你的补偿吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x8,
        "#5P不用客气，尽管收下哦。\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x101,
        (
            "#11P#0000F那么……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    OP_2C(0x4, 0x2)
    OP_29(0x4, 0x1, 0x1)
    Jump("loc_DAAB")

    label("loc_D74B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D91A")

    #C0775
    ChrTalk(
        0x8,
        (
            "#5P嗯……\x01",
            "不管怎么说，虽然\x01",
            "顺利做完测试了。\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x8,
        (
            "#5P但既然要做，我希望\x01",
            "你能全部答对呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x8,
        "#5P不过，这也勉强算合格吧。\x02",
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x101,
        (
            "#11P#0003F嗯，我的\x01",
            "知识还有所不足……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0779
    ChrTalk(
        0x104,
        "#12P#0300F算啦，你做得已经算是挺不错了。\x02",
    )

    CloseMessageWindow()

    def lambda_D83D():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D83D)
    Sleep(50)

    def lambda_D84D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D84D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0780
    ChrTalk(
        0x102,
        (
            "#6P#0104F嗯，没错。\x02\x03",

            "#0100F不足的知识接下来\x01",
            "再补上就行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x103,
        "#12P#0200F……加油。\x02",
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x101,
        "#11P#0000F哈哈……谢谢。\x02",
    )

    CloseMessageWindow()

    def lambda_D8DC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8DC)

    def lambda_D8E9():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D8E9)

    def lambda_D8F6():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D8F6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_2C(0x4, 0x1)
    OP_29(0x4, 0x1, 0x2)
    Jump("loc_DAAB")

    label("loc_D91A")


    #C0783
    ChrTalk(
        0x8,
        (
            "#5P嗯……\x01",
            "结果比较令人遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x8,
        (
            "#5P这说明你的知识\x01",
            "还远远不够啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x101,
        "#11P#0006F……实在惭愧万分啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0786
    ChrTalk(
        0x104,
        (
            "#12P#0300F没事，别介意。\x01",
            "不拘泥于这种小事\x01",
            "才像是个大人物嘛。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D9D6():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9D6)
    Sleep(50)

    def lambda_D9E6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D9E6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0787
    ChrTalk(
        0x102,
        (
            "#6P#0106F如果连这种常识都不拘泥，\x01",
            "也太过大人物了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x103,
        "#12P#0211F前途稍显堪忧啊。\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x101,
        "#11P#0006F我、我会加油的。\x02",
    )

    CloseMessageWindow()

    def lambda_DA77():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA77)

    def lambda_DA84():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DA84)

    def lambda_DA91():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DA91)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_29(0x4, 0x1, 0x3)

    label("loc_DAAB")


    #C0790
    ChrTalk(
        0x8,
        (
            "#5P那么，总之\x01",
            "我的测试就结束了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x8,
        (
            "#5P努力成长到不会\x01",
            "扯我们后腿的\x01",
            "程度就算帮大忙了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x101,
        "#11P#0000F嗯，共同努力吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0793
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【米歇尔的挑战书】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x4, 0x4, 0x10)
    Return()

    # Function_26_D3B7 end

    def Function_27_DB87(): pass

    label("Function_27_DB87")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09102.itc", 0x1E)
    OP_68(-6000, 1100, 48100, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -6000, 100, 47100, 0)
    SetChrChipByIndex(0x9, 0x7)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -6000, 100, 49200, 180)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00900.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis152.itp")
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性的声音")

    #A0794
    AnonymousTalk(
        0xFF,
        (
            "──辛苦了，\x01",
            "这个月也很不容易呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(22000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0795
    ChrTalk(
        0x9,
        (
            "#5P#1404F没什么，都习惯了。\x02\x03",

            "#1400F那么……\x01",
            "汇款的事就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x8,
        (
            "#2P知道了，\x01",
            "通过ＩＢＣ汇款可以吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x8,
        (
            "#2P不过……\x01",
            "虽然这话由我来讲\x01",
            "有点不合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x8,
        (
            "#2P但你减少点工作量\x01",
            "会比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x8,
        (
            "#2P小滴一个人\x01",
            "也会觉得孤单吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x9,
        "#5P#1403F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x8,
        (
            "#2P抱歉啊，我答应过你\x01",
            "不说这个的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0802
    ChrTalk(
        0x8,
        (
            "#2P对了……\x01",
            "列曼总部\x01",
            "又发来联络了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x8,
        (
            "#2P──问你还不打算\x01",
            "接受吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x9,
        (
            "#5P#1405F又是这个啊……\x02\x03",

            "#1403F关于此事，我不是\x01",
            "已经拒绝过很多次了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x8,
        (
            "#2P唔，总部应该是想\x01",
            "尽快找个人来代替\x01",
            "卡西乌斯·布莱特吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x8,
        "#2P你不是他的师弟嘛？\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x8,
        (
            "#2P而且在功绩上也丝毫不逊色于他，\x01",
            "就别再拒绝，乖乖接受了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x9,
        (
            "#5P#1404F可惜……\x01",
            "我和他是完全不一样的人。\x02\x03",

            "关于功绩的问题也是，\x01",
            "我并非像他那样\x01",
            "解决了国家性的问题。\x02\x03",

            "#1402F说实话，要接替他的位置，我还不够资格。\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x8,
        (
            "#2P说到国家性的问题，\x01",
            "你不也解决了雷米菲利亚的那起事件嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x8,
        (
            "#2P大公阁下还颁发了勋章给你，\x01",
            "在功绩上，我觉得你已经绰绰有余了。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x9,
        (
            "#5P#1403F……那件事并不能\x01",
            "算是真正解决了。\x02\x03",

            "#1401F虽然将公国里的邪恶萌芽扼杀了，\x01",
            "但一部分幕后策划者还是潜逃在外。\x02\x03",

            "本来我是想\x01",
            "拒绝勋章那种奖励的……\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x8,
        (
            "#2P真是的……\x01",
            "你这人就是太死脑筋了。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x8,
        (
            "#2P至少晋升后，\x01",
            "你反而可以稍微轻松点吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x8,
        (
            "#2P仅这个月你就完成了百件以上的委托……\x01",
            "这工作量也太不寻常了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x9,
        (
            "#5P#1404F我并没有勉强自己。\x02\x03",

            "#1402F因为列车和飞行船的班数都增加了，\x01",
            "所以去自治州外出差也变得轻松了许多。\x02\x03",

            "而且马上还要调来一些可靠的成员，\x01",
            "以后应该就能轻松点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x8,
        "#2P你是说那两个孩子吗……\x02",
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x8,
        (
            "#2P也是，他们确实是\x01",
            "很值得期待的超级新星。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_END)), "loc_E34C")

    #C0818
    ChrTalk(
        0x8,
        (
            "#2P至少，\x01",
            "要比支援科的那群小朋友\x01",
            "可靠得多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E37F")

    label("loc_E34C")


    #C0819
    ChrTalk(
        0x8,
        (
            "#2P至少，\x01",
            "要比支援科的那群小朋友\x01",
            "可靠得多啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E37F")

    Sleep(150)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    OP_4B(0xB, 0xFF)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    OP_4B(0xD, 0xFF)
    OP_49()
    OP_90(0xB, 0, -500, 47000, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_90(0xD, 0, -500, 47000, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Sleep(50)
    #Sound(1700, 255, 85, 0)    #voice#Estelle

    #N0820
    NpcTalk(
        0xB,
        "少女的声音",
        "#12A#1P#2S请问有人在吗～\x02",
    )
    #Auto

    Sleep(800)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    #C0821
    ChrTalk(
        0x8,
        "#6P啊，好像已经来了呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -4900, 0, 46370, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(-2150, 1100, 49550, 2500)

    def lambda_E4C1():
        OP_95(0xFE, -2000, 0, 49500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E4C1)
    WaitChrThread(0x8, 1)

    def lambda_E4DF():
        OP_95(0xFE, -2000, 0, 49500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E4DF)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x87, 0x1F4)

    #C0822
    ChrTalk(
        0x8,
        "#5P在这里哦，上来吧！\x02",
    )

    CloseMessageWindow()

    #N0823
    NpcTalk(
        0xB,
        "少女的声音",
        "#1P#2S啊，是二楼吗？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    #Sound(1774, 255, 90, 0)    #voice#Joshua

    #N0824
    NpcTalk(
        0xD,
        "青年的声音",
        "#11P#2S打扰了。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 28)
    Sleep(1000)
    OP_68(-3310, 900, 49440, 3000)
    MoveCamera(40, 19, 0, 3000)
    SetCameraDistance(21500, 3000)
    BeginChrThread(0xB, 3, 0, 29)
    Sleep(700)
    BeginChrThread(0xD, 3, 0, 30)
    Sleep(500)
    WaitChrThread(0x8, 3)
    Sleep(500)

    #N0825
    NpcTalk(
        0xB,
        "双马尾的少女",
        "#10A#0809F#5P您好～米歇尔先生──\x02",
    )
    #Auto

    WaitChrThread(0xB, 3)
    OP_6F(0x79)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0826
    NpcTalk(
        0xB,
        "双马尾的少女",
        "#0805F#11P啊，亚里欧斯先生！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 3)

    #N0827
    NpcTalk(
        0xD,
        "黑发的青年",
        (
            "#11P#0902F太好了，\x01",
            "您正好在啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x9,
        (
            "#1404F呵呵，偶然而已。\x02\x03",

            "#1402F有三个月没见了吧……\x01",
            "你们两个终于来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x8,
        (
            "#6P真没想到你们竟然\x01",
            "会被调到我们分部。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x8,
        (
            "#6P嗯嗯，这样一来，\x01",
            "克洛斯贝尔分部也就安宁了⊥\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E718():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E718)
    Sleep(100)
    OP_93(0xD, 0xE1, 0x1F4)
    Sleep(200)

    #N0831
    NpcTalk(
        0xB,
        "双马尾的少女",
        (
            "#0809F#5P啊哈哈……\x01",
            "你们太过奖了。\x02",
        )
    )

    CloseMessageWindow()

    #N0832
    NpcTalk(
        0xD,
        "黑发的青年",
        "#11P#0904F我们会努力的，一定不辜负各位的期望。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("双马尾的少女")

    #A0833
    AnonymousTalk(
        0xFF,
        (
            "──那么，\x01",
            "正游击士──艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("黑发的青年")

    #A0834
    AnonymousTalk(
        0xFF,
        "约修亚·布莱特。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(230, 100, -1, -1)
    SetMessageWindowPos(-1, 10, -1, -1)
    SetChrName("艾丝蒂尔＆约修亚")

    #A0835
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "正式向游击士协会·克洛斯贝尔分部\x01",
            "报到──！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(21250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_57(0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_E3(0xB)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_DB87 end

    def Function_28_E98E(): pass

    label("Function_28_E98E")

    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_E99A():
        OP_95(0xFE, -4900, 0, 46370, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E99A)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -6000, 100, 47100, 0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Return()

    # Function_28_E98E end

    def Function_29_E9D9(): pass

    label("Function_29_E9D9")


    def lambda_E9DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E9DE)

    def lambda_E9EF():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E9EF)
    WaitChrThread(0xB, 1)

    def lambda_EA0D():
        OP_95(0xFE, -3200, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EA0D)
    WaitChrThread(0xB, 1)

    def lambda_EA2B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EA2B)
    Return()

    # Function_29_E9D9 end

    def Function_30_EA34(): pass

    label("Function_30_EA34")


    def lambda_EA39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_EA39)

    def lambda_EA4A():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EA4A)
    WaitChrThread(0xD, 1)

    def lambda_EA68():
        OP_95(0xFE, -2400, 0, 49600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EA68)
    WaitChrThread(0xD, 1)

    def lambda_EA86():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EA86)
    Return()

    # Function_30_EA34 end

    def Function_31_EA8F(): pass

    label("Function_31_EA8F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch08202.itc", 0x22)
    LoadChrToIndex("chr/ch09102.itc", 0x23)
    OP_68(-2000, 1000, 2000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -2000, 0, -1000, 0)
    SetChrPos(0xEF, -2000, 0, -1000, 0)
    SetChrPos(0x153, -2000, 0, -1000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_EB54():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EB54)

    def lambda_EB6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EB6E)
    Sleep(250)

    def lambda_EB82():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_EB82)

    def lambda_EB9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_EB9C)
    Sleep(600)

    def lambda_EBB0():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_EBB0)

    def lambda_EBCA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_EBCA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)

    #C0836
    ChrTalk(
        0x101,
        "#0000F──打扰了。\x02",
    )

    CloseMessageWindow()

    #N0837
    NpcTalk(
        0x8,
        "男性的声音",
        "#6P啊……？\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1000, 11300, 2000)
    OP_6F(0x79)

    #C0838
    ChrTalk(
        0x8,
        (
            "#5P哎呀，我还以为是谁呢，\x01",
            "原来是支援科的小朋友们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x8,
        (
            "#5P呵呵，欢迎欢迎，\x01",
            "欢迎来到游击士协会。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 500, 0, 3000, 0)
    SetChrPos(0xEF, 0, 0, 1900, 0)
    SetChrPos(0x153, -500, 0, 3000, 0)

    def lambda_ECC9():
        OP_96(0xFE, 0x5DC, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECC9)
    Sleep(100)

    def lambda_ECE6():
        OP_96(0xFE, 0x1F4, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_ECE6)
    Sleep(150)

    def lambda_ED03():
        OP_96(0xFE, 0x3E8, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_ED03)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)

    #C0840
    ChrTalk(
        0x101,
        "#0000F米歇尔先生，您好。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_ED81")

    #C0841
    ChrTalk(
        0x102,
        (
            "#12P#0102F那个……\x01",
            "突然来访，真是不好意思。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EDD4")

    label("loc_ED81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_EDA9")

    #C0842
    ChrTalk(
        0x103,
        "#12P#0202F很久不见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EDD4")

    label("loc_EDA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_EDD4")

    #C0843
    ChrTalk(
        0x104,
        "#12P#0300F哟，好久不见了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_EDD4")


    #C0844
    ChrTalk(
        0x8,
        (
            "#5P你们可真是\x01",
            "稀客呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x8,
        "#5P──不过，你们还有空来这里吗？\x02",
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x8,
        (
            "#5P人家听说你们好像和\x01",
            "『鲁巴彻』起纠纷了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x101,
        (
            "#0006F协会果然\x01",
            "也得到消息了……\x02\x03",

            "#0001F那件事暂且\x01",
            "算是已经得到解决了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    TurnDirection(0x153, 0x101, 400)

    #C0848
    ChrTalk(
        0x153,
        (
            "#6P#1100F我说，罗伊德。\x02\x03",

            "为什么\x01",
            "这位大叔说话跟\x01",
            "女人一样呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_EF4B():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EF4B)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_EFA3")

    #C0849
    ChrTalk(
        0x102,
        "#12P#0105F小、小琪雅……\x02",
    )

    CloseMessageWindow()
    Jump("loc_EFF6")

    label("loc_EFA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_EFCF")

    #C0850
    ChrTalk(
        0x103,
        "#12P#0205F琪雅，那是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_EFF6")

    label("loc_EFCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_EFF6")

    #C0851
    ChrTalk(
        0x104,
        "#12P#0305F喂喂，阿琪……\x02",
    )

    CloseMessageWindow()

    label("loc_EFF6")

    OP_64(0xEF)
    OP_64(0x101)
    WaitChrThread(0x101, 2)
    Sleep(300)
    OP_93(0x101, 0x0, 0x190)
    Sleep(300)

    #C0852
    ChrTalk(
        0x101,
        (
            "#0006F对、对不起，\x01",
            "她还是个孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x8,
        "#5P呵呵，小猫咪，听人家说哦。\x02",
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x8,
        (
            "#5P每个人都有\x01",
            "自己独特的风格。\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x8,
        (
            "#5P对人家来说，\x01",
            "这种说话方式是最适合的。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x8,
        (
            "#5P就像你身上穿的那件衣服\x01",
            "非常适合你一样哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0x0, 0x1F4)

    #C0857
    ChrTalk(
        0x153,
        (
            "#12P#1105F喔，原来如此。\x02\x03",

            "#1109F琪雅觉得大叔的说话方式\x01",
            "很可爱哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1100)

    #C0858
    ChrTalk(
        0x8,
        "#5P哎呀，真是个好孩子。\x02",
    )

    CloseMessageWindow()

    #C0859
    ChrTalk(
        0x8,
        (
            "#5P不过……\x01",
            "能不能不叫人家大叔呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0860
    ChrTalk(
        0x8,
        "#5P就叫人家米歇尔吧。\x02",
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x153,
        "#12P#1110F嗯，米歇尔！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0862
    ChrTalk(
        0x8,
        "#5P呵呵，真是个乖孩子呢。\x02",
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x8,
        "#5P这孩子是你们的小朋友吗？\x02",
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0x101,
        (
            "#0003F嗯，其实……\x02\x03",

            "#0001F我们这次来，就是为了跟游击士协会\x01",
            "商量有关这孩子的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0865
    ChrTalk(
        0x8,
        "#5P是吗……？\x02",
    )

    CloseMessageWindow()
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 7600, 1000, 12500, 180)
    SetChrFlags(0xB, 0x40)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 7600, 1000, 12500, 180)
    SetChrFlags(0xD, 0x40)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Sleep(300)
    #Sound(1705, 255, 95, 0)    #voice#Estelle
    Sleep(1000)

    #N0866
    NpcTalk(
        0xB,
        "少女的声音",
        "咦，有客人吗？\x02",
    )

    CloseMessageWindow()
    OP_68(4000, 1000, 9500, 3000)

    def lambda_F33F():
        OP_95(0xFE, 7600, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F33F)

    def lambda_F359():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_F359)
    Sleep(400)

    def lambda_F36D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F36D)
    Sleep(50)

    def lambda_F37D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_F37D)
    Sleep(50)

    def lambda_F38D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_F38D)
    Sleep(50)

    def lambda_F39D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F39D)
    Sleep(100)

    def lambda_F3AD():
        OP_95(0xFE, 7600, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F3AD)

    def lambda_F3C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_F3C7)
    WaitChrThread(0xB, 1)

    def lambda_F3DC():
        OP_95(0xFE, 5600, 0, 9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F3DC)
    WaitChrThread(0xD, 1)

    def lambda_F3FA():
        OP_95(0xFE, 6000, 0, 10100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F3FA)
    WaitChrThread(0xB, 1)

    def lambda_F418():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_F418)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xD, 1)

    def lambda_F450():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_F450)
    Sleep(1000)
    OP_6F(0x1)

    #C0867
    ChrTalk(
        0xB,
        "#11P#0802F啊……是你们啊！？\x02",
    )

    CloseMessageWindow()

    #C0868
    ChrTalk(
        0x101,
        "#0000F#6P你们好，艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F508")

    #C0869
    ChrTalk(
        0x102,
        "#6P#0109F呵呵，上次的事真的很感谢你们。\x02",
    )

    CloseMessageWindow()

    #C0870
    ChrTalk(
        0xD,
        (
            "#11P#0902F你们很少\x01",
            "会来协会啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5AF")

    label("loc_F508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F55A")

    #C0871
    ChrTalk(
        0x103,
        "#6P#0202F有一周没见了呢。\x02",
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0xD,
        (
            "#11P#0902F你们很少\x01",
            "会来协会啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5AF")

    label("loc_F55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F5AF")

    #C0873
    ChrTalk(
        0x104,
        "#6P#0300F哟，有一个星期没见了吧。\x02",
    )

    CloseMessageWindow()

    #C0874
    ChrTalk(
        0xD,
        (
            "#11P#0902F你们很少\x01",
            "会来协会啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5AF")


    #C0875
    ChrTalk(
        0xB,
        (
            "#11P#0809F嘿嘿，难道\x01",
            "是来看我们的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0876
    ChrTalk(
        0xB,
        "#11P#0805F咦，那个孩子……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_68(620, 1000, 9840, 1500)
    MoveCamera(35, 21, 0, 1500)
    SetCameraDistance(21500, 1500)

    def lambda_F666():

        label("loc_F666")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_F666")

    QueueWorkItem2(0x101, 2, lambda_F666)

    def lambda_F678():

        label("loc_F678")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_F678")

    QueueWorkItem2(0x153, 2, lambda_F678)

    def lambda_F68A():

        label("loc_F68A")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_F68A")

    QueueWorkItem2(0x8, 2, lambda_F68A)

    def lambda_F69C():
        OP_95(0xFE, 500, 0, 9000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F69C)
    Sleep(500)

    def lambda_F6B9():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0x2260, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_F6B9)
    WaitChrThread(0xB, 1)
    TurnDirection(0xB, 0x153, 800)
    WaitChrThread(0xEF, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x153, 0x2)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    OP_64(0xB)

    #C0877
    ChrTalk(
        0xB,
        (
            "#12P#0809F哇哇……\x01",
            "好可爱的孩子！\x02\x03",

            "#0802F你怎么会来这里的？\x01",
            "是罗伊德他们的朋友吗！？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 3, 0, 32)

    #C0878
    ChrTalk(
        0x101,
        (
            "#5P#0000F是啊……\x01",
            "她叫琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x153,
        (
            "#1105F#5P大姐姐，\x01",
            "你的头发一跳一跳的呢。\x02\x03",

            "#1100F莫非你就是游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0880
    ChrTalk(
        0xB,
        (
            "#12P#0800F嗯，我叫艾丝蒂尔，\x01",
            "这个哥哥叫约修亚。\x02\x03",

            "#0809F这样啊，你叫小琪雅啊。\x01",
            "多多指教哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x153,
        "#1109F#5P嗯！\x02",
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x101,
        "#5P#0012F嗯，这么快就混熟了呢。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F8C2")

    #C0883
    ChrTalk(
        0xD,
        (
            "#12P#0909F哈哈，艾丝蒂尔\x01",
            "很受小孩子欢迎哦……\x02\x03",

            "#0900F不过，\x01",
            "这孩子本来好像就很不怕生啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F91C")

    label("loc_F8C2")


    #C0884
    ChrTalk(
        0xD,
        (
            "#12P#0909F哈哈，艾丝蒂尔\x01",
            "很受小孩子欢迎哦……\x02\x03",

            "#0900F不过，\x01",
            "这孩子好像也很不怕生啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F949")

    #C0885
    ChrTalk(
        0x102,
        "#6P#0102F呵呵，确实如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F99C")

    label("loc_F949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F976")

    #C0886
    ChrTalk(
        0x103,
        "#6P#0204F是啊，确实如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F99C")

    label("loc_F976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F99C")

    #C0887
    ChrTalk(
        0x104,
        "#6P#0302F啊，确实如此。\x02",
    )

    CloseMessageWindow()

    label("loc_F99C")


    #C0888
    ChrTalk(
        0x8,
        (
            "#5P那么，关于这孩子，\x01",
            "你们不是有事要跟我们商量吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0x8,
        (
            "#5P要不这样吧，\x01",
            "我们去二楼慢慢谈怎么样？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA09():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FA09)
    Sleep(100)

    def lambda_FA19():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_FA19)
    Sleep(50)
    OP_93(0xEF, 0x0, 0x1F4)

    #C0890
    ChrTalk(
        0x101,
        (
            "#2P#0001F啊……\x01",
            "好的，如果不会给各位添麻烦的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0891
    ChrTalk(
        0xB,
        "#12P#0805F啊，原来是关于这孩子的事啊？\x02",
    )

    CloseMessageWindow()

    #C0892
    ChrTalk(
        0xD,
        "#12P#0901F背后好像有什么隐情呢。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(-8200, 900, 48300, 0)
    MoveCamera(47, 19, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(20000, 0)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xD, 0x9)
    SetChrSubChip(0xD, 0x1)
    SetChrPos(0xD, -10700, 150, 49200, 180)
    SetChrChipByIndex(0xB, 0x8)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -8400, 150, 49200, 180)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -6000, 100, 49200, 180)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xEF, 0x4)
    SetChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x153, 0x22)
    SetChrSubChip(0x153, 0x2)
    OP_52(0x153, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_FBAC")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    Jump("loc_FBD3")

    label("loc_FBAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_FBC2")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    Jump("loc_FBD3")

    label("loc_FBC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_FBD3")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)

    label("loc_FBD3")

    SetChrPos(0x153, -10900, 200, 47100, 0)
    SetChrPos(0x101, -8400, 100, 47000, 0)
    SetChrPos(0xEF, -6000, 100, 47000, 0)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    Sleep(500)
    SetCameraDistance(19500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0893
    ChrTalk(
        0xB,
        "#5P#0801F居、居然有那种事……\x02",
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0xD,
        (
            "#0901F#5P最近这一周，我确实感觉到\x01",
            "后巷的气氛变得有些紧张……\x02",
        )
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0x8,
        (
            "#11P哎呀呀……\x01",
            "没想到事件的经过竟然是这样的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_FD50")

    #C0896
    ChrTalk(
        0x102,
        (
            "#0103F#12P……警察这边决定\x01",
            "暂时接受鲁巴彻方面\x01",
            "的解释。\x02\x03",

            "#0101F如果协会\x01",
            "也能配合，\x01",
            "我们将不胜感激……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDC9")

    label("loc_FD50")


    #C0897
    ChrTalk(
        0x101,
        (
            "#12P#0003F……警察这边决定\x01",
            "暂时接受鲁巴彻方面\x01",
            "的解释。\x02\x03",

            "#0000F如果可以的话，我希望能以\x01",
            "这个决定为前提来进行对话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDC9")


    #C0898
    ChrTalk(
        0xB,
        "#5P#0801F唔唔……\x02",
    )

    CloseMessageWindow()

    #C0899
    ChrTalk(
        0x8,
        (
            "#11P呼，没办法，也只能如此啦，\x01",
            "毕竟我们只是局外人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x8,
        (
            "#11P话说回来，真是没想到你们竟然\x01",
            "敢潜入『黑之竞拍会』进行调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0901
    ChrTalk(
        0x8,
        "#11P很厉害嘛，对你们刮目相看了哦。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0xEF, 0x0)
    Sleep(300)

    #C0902
    ChrTalk(
        0x101,
        "#6P#0002F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0903
    ChrTalk(
        0xB,
        (
            "#5P#0806F我们之前\x01",
            "也想设法调查那个拍卖会的……\x02\x03",

            "而且，邀请卡竟然是\x01",
            "玲给你们的……\x02\x03",

            "#0801F她也真是的……\x01",
            "要是给我们就好了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x1)

    #C0904
    ChrTalk(
        0xD,
        (
            "#0904F算啦，那也是没办法的事啊。\x02\x03",

            "#0900F她应该还有些苦衷，\x01",
            "所以没法与我们见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0905
    ChrTalk(
        0xB,
        "#5P#0806F话、话虽如此……\x02",
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0x101,
        (
            "#12P#0008F结果还是从旁夺走了\x01",
            "从你们那里得知的案子啊……\x02\x03",

            "#0003F抱歉啊，如果当时联系你们就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0907
    ChrTalk(
        0xB,
        (
            "#5P#0805F啊，没什么，\x01",
            "不用介意那些。\x02\x03",

            "#0802F你们也已经很努力了，\x01",
            "我们只是很在意那个孩子而已。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    #C0908
    ChrTalk(
        0xB,
        (
            "#11P#0801F……不过……\x01",
            "现在的问题确实是小琪雅啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1010F")

    #C0909
    ChrTalk(
        0x102,
        "#0108F#12P嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10158")

    label("loc_1010F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_10135")

    #C0910
    ChrTalk(
        0x103,
        "#0203F#12P是的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10158")

    label("loc_10135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_10158")

    #C0911
    ChrTalk(
        0x104,
        "#0303F#12P算是吧……\x02",
    )

    CloseMessageWindow()

    label("loc_10158")


    #C0912
    ChrTalk(
        0x153,
        "#6P#1110F嗯？\x02",
    )

    CloseMessageWindow()

    #C0913
    ChrTalk(
        0x8,
        (
            "#11P也就是说，你们是想让我们\x01",
            "帮忙调查这孩子的身世吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0914
    ChrTalk(
        0x8,
        "#11P──通过游击士协会的情报网。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0xEF, 0x0)
    Sleep(300)

    #C0915
    ChrTalk(
        0x101,
        (
            "#6P#0003F是的……\x01",
            "我们就是为此特意来拜托你们的。\x02\x03",

            "#0000F那个，我们也可以\x01",
            "支付一些委托金的。\x02",
        )
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x8,
        "#11P啊，那个就不用了哦。\x02",
    )

    CloseMessageWindow()

    #C0917
    ChrTalk(
        0x8,
        (
            "#11P像这种委托，\x01",
            "我们这里一直都是免费受理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0x8,
        (
            "#11P那我马上去问问各地的分部，\x01",
            "看看有没有什么相关情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0919
    ChrTalk(
        0x101,
        "#6P#0002F谢、谢谢您！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_10331")

    #C0920
    ChrTalk(
        0x102,
        (
            "#0105F#12P没、没想到协会这么轻易\x01",
            "就接受了我们的委托啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_103B2")

    label("loc_10331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_10376")

    #C0921
    ChrTalk(
        0x103,
        (
            "#0205F#12P……协会这么轻易\x01",
            "就接受了我们的委托吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_103B2")

    label("loc_10376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_103B2")

    #C0922
    ChrTalk(
        0x104,
        (
            "#0305F#12P哈，这么轻易\x01",
            "就接受了我们的委托啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103B2")

    SetChrSubChip(0xB, 0x0)
    Sleep(150)

    #C0923
    ChrTalk(
        0xB,
        (
            "#5P#0800F嗯，对于这方面的委托，\x01",
            "我们的宗旨是当机立断哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0924
    ChrTalk(
        0xD,
        (
            "#0904F而且，这种案件的费用\x01",
            "也都是用各种基金或捐款来支付的。\x02\x03",

            "#0900F所以你们就不用客气了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x1)
    Sleep(300)

    #C0925
    ChrTalk(
        0x101,
        "#12P#0002F原、原来如此……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_104CD")

    #C0926
    ChrTalk(
        0x102,
        (
            "#0102F#12P这正是游击士协会中\x01",
            "救助平民制度的体现吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1055E")

    label("loc_104CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_10516")

    #C0927
    ChrTalk(
        0x103,
        (
            "#0202F#12P这也正是游击士协会\x01",
            "救助平民的职能体现吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1055E")

    label("loc_10516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1055E")

    #C0928
    ChrTalk(
        0x104,
        (
            "#0300F#12P这就表明了游击士协会里\x01",
            "有着救助平民的机制吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1055E")


    #C0929
    ChrTalk(
        0x8,
        (
            "#11P虽然在结果出来之前，\x01",
            "还需要一点时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0930
    ChrTalk(
        0x8,
        (
            "#11P但我想一周左右\x01",
            "应该就能给你们回复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0931
    ChrTalk(
        0x101,
        (
            "#12P#0004F……这已经足够了，\x01",
            "那么就万事拜托了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0932
    ChrTalk(
        0xB,
        (
            "#5P#0805F对了，如果方便的话，\x01",
            "暂时把小琪雅交给我们看护如何？\x02\x03",

            "#0800F毕竟基金中也包含了\x01",
            "提供给保护对象的生活费。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0933
    ChrTalk(
        0x101,
        "#12P#0005F咦……！？\x02",
    )

    CloseMessageWindow()

    #C0934
    ChrTalk(
        0xD,
        (
            "#0903F嗯……\x02\x03",

            "#0901F从安全角度来看，\x01",
            "这项提议也很值得考虑呢。\x02\x03",

            "而且，就算有什么突发情况，我们也能\x01",
            "为她安排克洛斯贝尔之外的安全避难所。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_10783")

    #C0935
    ChrTalk(
        0x102,
        "#0108F#12P不、不过……\x02",
    )

    CloseMessageWindow()
    Jump("loc_107D2")

    label("loc_10783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_107AD")

    #C0936
    ChrTalk(
        0x103,
        "#0208F#12P……那个……\x02",
    )

    CloseMessageWindow()
    Jump("loc_107D2")

    label("loc_107AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_107D2")

    #C0937
    ChrTalk(
        0x104,
        "#0306F#12P这个有点……\x02",
    )

    CloseMessageWindow()

    label("loc_107D2")


    #C0938
    ChrTalk(
        0x101,
        "#12P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0939
    ChrTalk(
        0x153,
        (
            "#6P#1105F嗯？\x01",
            "你怎么了，罗伊德？\x02\x03",

            "#1101F肚子痛吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0940
    ChrTalk(
        0x101,
        (
            "#11P#0005F啊，不是……\x02\x03",

            "#0006F……也是。\x01",
            "这孩子也极有可能出身于\x01",
            "克洛斯贝尔之外的地区……\x02\x03",

            "#0008F……而且确实应该以她的安全为重，如此考虑的话……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_108F9")

    #C0941
    ChrTalk(
        0x102,
        "#0108F#11P罗伊德……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1095A")

    label("loc_108F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_10929")

    #C0942
    ChrTalk(
        0x103,
        "#0208F#11P……罗伊德前辈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1095A")

    label("loc_10929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1095A")

    #C0943
    ChrTalk(
        0x104,
        "#0308F#11P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1095A")


    #C0944
    ChrTalk(
        0x153,
        "#6P#1100F？？？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    #C0945
    ChrTalk(
        0xB,
        (
            "#11P#0800F#11P那个，小琪雅。\x02\x03",

            "你要不要暂时跟我们\x01",
            "生活一段时间呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0946
    ChrTalk(
        0x153,
        (
            "#6P#1105F和艾丝蒂尔吗？\x02\x03",

            "#1110F那……艾丝蒂尔也要\x01",
            "搬到那幢大楼里住吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0947
    ChrTalk(
        0xB,
        (
            "#11P#0805F啊，不是……\x02\x03",

            "#0800F是小琪雅要\x01",
            "搬到这里来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0948
    ChrTalk(
        0x153,
        "#6P#1105F罗伊德他们也一起吗？\x02",
    )

    CloseMessageWindow()

    #C0949
    ChrTalk(
        0xB,
        (
            "#11P#0806F那个，他们要搬过来\x01",
            "就有些不方便了……\x02\x03",

            "#0800F不过，两个地方离得也不算太远，\x01",
            "要是想见面的话，马上就能见到哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(300)
    Sound(2030, 255, 90, 0)    #voice#KeA
    Sleep(1700)
    OP_64(0x153)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0950
    ChrTalk(
        0x153,
        "#6P#5S#1109F#N绝对不要。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    #Sound(1706, 255, 100, 0)    #voice#Estelle

    #C0951
    ChrTalk(
        0xB,
        "#11P#0807F#4S（大受打击！）\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    #C0952
    ChrTalk(
        0x101,
        "#11P#0011F琪雅……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_10C4F")

    #C0953
    ChrTalk(
        0x153,
        (
            "#6P#1108F因为琪雅不要和\x01",
            "罗伊德分开。\x02\x03",

            "#1103F还有艾莉、缇欧、\x01",
            "兰迪、蔡特\x01",
            "和科长。\x02\x03",

            "#1101F琪雅，绝对不搬过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0954
    ChrTalk(
        0x102,
        "#0102F#11P小、小琪雅……（感动）\x02",
    )

    CloseMessageWindow()
    Jump("loc_10D90")

    label("loc_10C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_10CF5")

    #C0955
    ChrTalk(
        0x153,
        (
            "#6P#1103F因为琪雅不要和\x01",
            "罗伊德分开。\x02\x03",

            "还有缇欧、艾莉、\x01",
            "兰迪、蔡特\x01",
            "和科长。\x02\x03",

            "#1101F琪雅，绝对不搬过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0956
    ChrTalk(
        0x103,
        "#0204F#11P…………………………（感动）\x02",
    )

    CloseMessageWindow()
    Jump("loc_10D90")

    label("loc_10CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_10D90")

    #C0957
    ChrTalk(
        0x153,
        (
            "#6P#1103F因为琪雅不要和\x01",
            "罗伊德分开。\x02\x03",

            "还有兰迪、艾莉、\x01",
            "缇欧、蔡特\x01",
            "和科长。\x02\x03",

            "#1101F琪雅，绝对不搬过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0958
    ChrTalk(
        0x104,
        "#0304F#11P哈哈……这就没办法了。\x02",
    )

    CloseMessageWindow()

    label("loc_10D90")


    #C0959
    ChrTalk(
        0xB,
        "#11P#0809F这、这样啊……\x02",
    )

    CloseMessageWindow()

    #C0960
    ChrTalk(
        0xD,
        "#0904F#5P哈哈，被拒绝了呢。\x02",
    )

    CloseMessageWindow()

    #C0961
    ChrTalk(
        0x8,
        (
            "#11P哎呀呀，艾丝蒂尔竟然\x01",
            "会被小孩子拒绝，\x01",
            "这可真是少见～\x02",
        )
    )

    CloseMessageWindow()

    #C0962
    ChrTalk(
        0x8,
        "#11P你受到沉重打击了吧？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0xB, 0x1)
    Sleep(300)

    #C0963
    ChrTalk(
        0xB,
        (
            "#5P#0801F才、才没有！\x02\x03",

            "#0806F呼……\x01",
            "不过好像确实有点打击。\x02",
        )
    )

    CloseMessageWindow()

    #C0964
    ChrTalk(
        0x153,
        (
            "#6P#1106F琪雅并不是\x01",
            "讨厌艾丝蒂尔哦……\x02\x03",

            "#1112F不过，不愿意就是不愿意嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(50)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    #C0965
    ChrTalk(
        0xB,
        (
            "#11P#0809F啊哈哈，抱歉抱歉，\x01",
            "是我欠考虑了。\x02\x03",

            "#0802F罗伊德，你们真幸福啊，\x01",
            "琪雅这么喜欢你们……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0966
    ChrTalk(
        0x101,
        (
            "#12P#0004F哈哈……\x01",
            "不过我们也不知道为什么。\x02\x03",

            "#0000F其实也有可能是因为\x01",
            "我们跟这孩子认识的人比较像吧……\x02\x03",

            "虽然她好像什么都\x01",
            "想不起来了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)
    Sleep(150)

    #C0967
    ChrTalk(
        0xD,
        (
            "#0903F──这样啊。\x02\x03",

            "#0900F有关琪雅身份的调查，\x01",
            "就交给米歇尔先生来处理吧……\x02\x03",

            "另外，你们不带她去看看\x01",
            "治疗失忆方面的专家吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0968
    ChrTalk(
        0x101,
        "#11P#0005F哎……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_110CF")

    #C0969
    ChrTalk(
        0x102,
        "#0105F#11P专家是指……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_11118")

    label("loc_110CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_110F5")

    #C0970
    ChrTalk(
        0x103,
        "#0205F#11P专家吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_11118")

    label("loc_110F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_11118")

    #C0971
    ChrTalk(
        0x104,
        "#0305F#11P专家……？\x02",
    )

    CloseMessageWindow()

    label("loc_11118")


    #C0972
    ChrTalk(
        0xD,
        (
            "#0908F嗯，假如小琪雅的失忆\x01",
            "是出自心灵或精神方面的问题……\x02\x03",

            "#0900F那么，可以去向七耀教会的人咨询一下，\x01",
            "他们应该算是这方面的专家。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0973
    ChrTalk(
        0x101,
        "#11P#0011F啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_11214")

    #C0974
    ChrTalk(
        0x102,
        "#0103F#11P……确实……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11265")

    label("loc_11214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_11240")

    #C0975
    ChrTalk(
        0x103,
        "#0204F#11P……原来如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11265")

    label("loc_11240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_11265")

    #C0976
    ChrTalk(
        0x104,
        "#0302F#11P这样说来……\x02",
    )

    CloseMessageWindow()

    label("loc_11265")

    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0977
    ChrTalk(
        0x153,
        "#6P#1111F七耀教会？\x02",
    )

    CloseMessageWindow()

    #C0978
    ChrTalk(
        0x8,
        (
            "#11P对哦，虽然克洛斯贝尔的\x01",
            "近代医疗技术十分发达……\x02",
        )
    )

    CloseMessageWindow()

    #C0979
    ChrTalk(
        0x8,
        (
            "#11P但如果是心灵方面的问题，\x01",
            "应该还是教会的专家\x01",
            "更加熟悉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0980
    ChrTalk(
        0xB,
        (
            "#11P#0809F嗯嗯，确实！\x02\x03",

            "#0802F我们也受到过\x01",
            "教会的很多帮助哦！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0981
    ChrTalk(
        0x101,
        "#12P#0005F咦，真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0982
    ChrTalk(
        0xD,
        (
            "#0904F嗯……主要是我\x01",
            "之前受到过教会的很多帮助。\x02\x03",

            "#0900F虽然不知道\x01",
            "克洛斯贝尔大圣堂里有没有\x01",
            "像那个人一样厉害的人物……\x02\x03",

            "不过，还是先去和他们商量看看如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0983
    ChrTalk(
        0x101,
        (
            "#12P#0004F……知道了。\x01",
            "这是个很宝贵的建议，谢谢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0984
    ChrTalk(
        0x101,
        (
            "#11P#0000F──琪雅，听我说哦。\x02\x03",

            "接下来我们要去\x01",
            "郊外的教堂，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0985
    ChrTalk(
        0x153,
        (
            "#6P#1104F嗯，好啊。\x02\x03",

            "#1100F那里是向女神\x01",
            "祷告的地方吧？\x02\x03",

            "#1109F我们马上出发吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(50)
    SetChrSubChip(0xD, 0x0)
    Sleep(150)

    #C0986
    ChrTalk(
        0xB,
        "#11P#0809F啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0987
    ChrTalk(
        0x8,
        "#11P真是个活泼的孩子啊。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    ClearChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 1000, 0, 12820, 180)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_4C(0x8, 0xFF)
    OP_68(-8400, 1300, 45000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x0, -8400, 0, 45000, 180)
    SetChrPos(0x1, -8400, 0, 45000, 180)
    SetChrPos(0x2, -8400, 0, 45000, 180)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -8400, 150, 49200, 180)
    SetChrPos(0xE, -10700, 150, 49200, 180)
    SetMapObjFrame(0xFF, "on_off", 0x1, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x1, 0x1)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA8, 0)
    OP_29(0x48, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_31_EA8F end

    def Function_32_1167D(): pass

    label("Function_32_1167D")


    def lambda_11682():
        OP_95(0xFE, 1400, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_11682)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0x13B, 0x1F4)
    Return()

    # Function_32_1167D end

    def Function_33_116A3(): pass

    label("Function_33_116A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch08700.itc", 0x22)
    LoadChrToIndex("chr/ch09102.itc", 0x23)
    LoadChrToIndex("chr/ch32000.itc", 0x24)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06000.itp")
    OP_68(-8200, 1600, 48300, 0)
    MoveCamera(47, 19, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, -10700, 100, 47100, 0)
    SetChrPos(0x101, -8400, 100, 47100, 0)
    SetChrPos(0x104, -6000, 100, 47100, 0)
    SetChrPos(0x103, -10700, 150, 49200, 180)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x7)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -8400, 150, 49200, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -6000, 100, 49200, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x12, 0x24)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0988
    AnonymousTalk(
        0x9,
        (
            "──原来如此，\x01",
            "没想到事情会变成这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-8200, 1100, 48300, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0989
    ChrTalk(
        0x8,
        (
            "#11P嗯，关于失踪者的传闻，\x01",
            "我们这边也有一定程度的掌握……\x02",
        )
    )

    CloseMessageWindow()

    #C0990
    ChrTalk(
        0x8,
        "#11P但我们这次的行动真是完全落后了呢。\x02",
    )

    CloseMessageWindow()

    #C0991
    ChrTalk(
        0x8,
        (
            "#11P而且，那个教团\x01",
            "竟然还出现了……\x02",
        )
    )

    CloseMessageWindow()

    #C0992
    ChrTalk(
        0x9,
        "#5P#1403F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0993
    ChrTalk(
        0x101,
        (
            "#12P#0006F……那个，亚里欧斯先生，\x01",
            "您也参与解决过\x01",
            "六年前的教团事件吧？\x02\x03",

            "#0013F您觉得仍有余党残存\x01",
            "的可能性有多大？\x02",
        )
    )

    CloseMessageWindow()

    #C0994
    ChrTalk(
        0x9,
        (
            "#5P#1403F……这个啊。\x02\x03",

            "#1401F虽然当时捣毁了所有据点，\x01",
            "但确实无法排除暗中仍有余党残存的可能性。\x02\x03",

            "只要有犯罪组织出手帮忙，\x01",
            "残存余党便能轻易隐藏起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0995
    ChrTalk(
        0x103,
        "#0208F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0996
    ChrTalk(
        0x104,
        (
            "#0306F#12P原来如此，例如『鲁巴彻』\x01",
            "就是个理想的避风港啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0997
    ChrTalk(
        0x102,
        (
            "#6P#0106F不过，为什么他们要\x01",
            "冒着高风险做这种事……\x02\x03",

            "#0108F这可不像精于计算的\x01",
            "马尔克尼会长的作风啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0998
    ChrTalk(
        0x8,
        (
            "#11P确实，如果知道了\x01",
            "那里藏匿着教团的残党，\x01",
            "很多势力都不会坐视不理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0999
    ChrTalk(
        0x8,
        (
            "#11P我们协会当然就不用说了……\x01",
            "教会和『结社』应该也一样吧。\x02",
        )
    )

    CloseMessageWindow()

    #C1000
    ChrTalk(
        0x101,
        (
            "#12P#0008F这样的话……\x02\x03",

            "#0001F也就是说，还有很多隐情\x01",
            "是我们尚未得知的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C1001
    ChrTalk(
        0x9,
        (
            "#5P#1403F嗯──不过\x01",
            "我们也没有时间去一一确认。\x02\x03",

            "#1401F当务之急，还是分头找寻黑手党\x01",
            "和失踪者们的行踪。\x02\x03",

            "他们的下落，恐怕与\x01",
            "教团余党有着密不可分的关联。\x02",
        )
    )

    CloseMessageWindow()

    #C1002
    ChrTalk(
        0x103,
        "#0202F#6P那个，这样的话……\x02",
    )

    CloseMessageWindow()

    #C1003
    ChrTalk(
        0x104,
        (
            "#0305F#12P你们方便和我们\x01",
            "进行合作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1004
    ChrTalk(
        0x8,
        "#11P嗯，我们这边没问题。\x02",
    )

    CloseMessageWindow()

    #C1005
    ChrTalk(
        0x8,
        (
            "#11P既然有市民失踪，\x01",
            "这件事自然就跟我们脱不开关系。\x02",
        )
    )

    CloseMessageWindow()

    #C1006
    ChrTalk(
        0x8,
        "#11P还有违禁药物的事件也是一样。\x02",
    )

    CloseMessageWindow()

    #C1007
    ChrTalk(
        0x101,
        (
            "#12P#0004F……感谢你们的帮助，\x01",
            "那就请多多指教了。\x02",
        )
    )

    CloseMessageWindow()

    #C1008
    ChrTalk(
        0x9,
        (
            "#5P#1404F嗯，彼此彼此。\x02\x03",

            "#1402F既然已经决定了，\x01",
            "那我们来分配下任务吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(300)

    #C1009
    ChrTalk(
        0x9,
        (
            "#1P#1400F艾丝蒂尔他们就不说了，\x01",
            "其他成员有时间吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1010
    ChrTalk(
        0x8,
        (
            "#11P幸好，斯克特和林他们\x01",
            "手边都没有紧急任务。\x02",
        )
    )

    CloseMessageWindow()

    #C1011
    ChrTalk(
        0x8,
        (
            "#11P再加上艾丝蒂尔他们，\x01",
            "总共有七个人。\x02",
        )
    )

    CloseMessageWindow()

    #C1012
    ChrTalk(
        0x9,
        (
            "#1P#1403F好，把大家都召集过来吧。\x02\x03",

            "#1401F最好能在今天之内\x01",
            "把几个重要地点检查完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C1013
    ChrTalk(
        0x8,
        (
            "#11P好的～\x01",
            "那我去联系他们了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -5000, 100, 49500, 90)
    Sound(820, 0, 100, 0)
    OP_0D()

    def lambda_11F3C():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11F3C)
    Sleep(300)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)
    SetChrSubChip(0x104, 0x2)
    WaitChrThread(0x8, 1)
    StopBGM(0x1F40)

    def lambda_11F74():
        OP_95(0xFE, 0, -500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11F74)
    Sleep(700)

    def lambda_11F91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11F91)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Sleep(1000)

    #C1014
    ChrTalk(
        0x102,
        (
            "#6P#0102F啊，一如既往地\x01",
            "高效率啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    #C1015
    ChrTalk(
        0x9,
        (
            "#5P#1404F这正是我们游击士\x01",
            "最大的优势。\x02\x03",

            "#1405F对了，赛尔盖先生\x01",
            "知道这件事了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(150)
    SetChrSubChip(0x104, 0x1)
    Sleep(150)

    #C1016
    ChrTalk(
        0x101,
        (
            "#12P#0004F嗯，关于与协会的合作，\x01",
            "我们已经取得他的许可了。\x02\x03",

            "#0000F他还让我们\x01",
            "代他向您问好。\x02",
        )
    )

    CloseMessageWindow()

    #C1017
    ChrTalk(
        0x9,
        (
            "#5P#1402F这样啊……\x02\x03",

            "#1403F………………………………\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(600)
    SetCameraDistance(18800, 60000)
    MoveCamera(42, 19, 0, 60000)
    PlayBGM("ed7001", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(800)

    #C1018
    ChrTalk(
        0x101,
        (
            "#12P#0006F……那个，亚里欧斯先生。\x02\x03",

            "听说您还是警察的时候，\x01",
            "曾在科长手下工作过吧？\x02\x03",

            "#0001F和我大哥一起……\x02",
        )
    )

    CloseMessageWindow()

    #C1019
    ChrTalk(
        0x9,
        (
            "#5P#1402F……是啊。\x02\x03",

            "#1404F赛尔盖先生、我还有盖伊……\x02\x03",

            "我们仅凭三人之力，\x01",
            "就取得了比搜查一科更加辉煌的成绩，\x01",
            "被誉为警察史上最强的队伍……\x02\x03",

            "#1400F不过，在我五年前因为私人原因\x01",
            "而辞去警察工作之后，队伍就解散了。\x02\x03",

            "赛尔盖先生被调去了警察学校，\x01",
            "而盖伊则进入了搜查一科……\x02\x03",

            "#1403F两年后──盖伊就因公殉职了。\x02",
        )
    )

    CloseMessageWindow()

    #C1020
    ChrTalk(
        0x101,
        "#12P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C1021
    ChrTalk(
        0x103,
        "#0208F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    #C1022
    ChrTalk(
        0x9,
        (
            "#5P#1403F假如我当时没有辞去警察工作的话——\x01",
            "事到如今，我自然也不打算再说这些了。\x02\x03",

            "因为，与警察之道彻底诀别是我根据\x01",
            "自身情况和意志所做出的决定。\x02\x03",

            "#1402F不过……直到如今，\x01",
            "我也仍然会时常想起那段光辉的岁月……\x02\x03",

            "那段与怪癖颇多的上司\x01",
            "和特立独行的搭档\x01",
            "一起度过的日子。\x02\x03",

            "#1404F呵呵──所以，说实话，\x01",
            "我很羡慕你们。\x02",
        )
    )

    CloseMessageWindow()

    #C1023
    ChrTalk(
        0x101,
        "#12P#0005F咦……\x02",
    )

    CloseMessageWindow()

    #C1024
    ChrTalk(
        0x104,
        (
            "#0302F#12P哈哈，举世闻名的『风之剑圣』\x01",
            "竟然也会说出这样的话啊……\x02",
        )
    )

    CloseMessageWindow()

    #C1025
    ChrTalk(
        0x102,
        (
            "#6P#0106F应该说，是我们\x01",
            "羡慕游击士协会这边\x01",
            "公开透明的风气才对……\x02",
        )
    )

    CloseMessageWindow()

    #C1026
    ChrTalk(
        0x9,
        (
            "#5P#1403F──警察是警察，\x01",
            "协会是协会，各自的职责不同。\x02\x03",

            "#1400F游击士协会\x01",
            "所追求的是不屈服于权利，\x01",
            "作为普遍理想的『正义』……\x02\x03",

            "而受制于权利的同时，\x01",
            "却仍然要追求『正义』，\x01",
            "这才是警察的使命。\x02\x03",

            "#1404F你们应该也感觉到了吧，\x01",
            "身边有着各种矛盾和不公的状况……\x02\x03",

            "我曾经也为此深深烦恼，\x01",
            "但我如今却认为，\x01",
            "那些也都是很有价值的经验。\x02",
        )
    )

    CloseMessageWindow()

    #C1027
    ChrTalk(
        0x103,
        (
            "#0205F#6P受制于权利的同时，\x01",
            "却仍然要追求的『正义』……\x02",
        )
    )

    CloseMessageWindow()

    #C1028
    ChrTalk(
        0x101,
        (
            "#12P#0013F……大哥所追求的\x01",
            "也是那个吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1029
    ChrTalk(
        0x9,
        (
            "#5P#1404F嗯……我相信是的。\x02\x03",

            "#1402F所以赛尔盖先生才会\x01",
            "竭尽全力成立了支援科。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C1030
    ChrTalk(
        0x9,
        (
            "#5P#1404F呵……\x01",
            "怎么变得像是在给你们说教了。\x02\x03",

            "#1402F其实你们只要\x01",
            "寻找到你们自己的答案就行了。\x02\x03",

            "我想那家伙大概\x01",
            "也是这样期望的。\x02",
        )
    )

    CloseMessageWindow()

    #C1031
    ChrTalk(
        0x101,
        "#12P#0002F……嗯。\x02",
    )

    CloseMessageWindow()

    #C1032
    ChrTalk(
        0x104,
        "#0304F#12P哈哈，好难的作业啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 0, -500, 47000, 0)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 0, -500, 47000, 0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x40)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 0, -500, 47000, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    Sleep(300)
    #Sound(1707, 255, 90, 0)    #voice#Estelle

    #N1033
    NpcTalk(
        0xB,
        "少女的声音",
        "#10A#1P#2S我们回来了～！\x02",
    )
    #Auto

    Sleep(800)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)
    Fade(500)
    OP_68(-1000, 900, 49400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    BeginChrThread(0xB, 3, 0, 34)
    BeginChrThread(0xD, 3, 0, 35)
    BeginChrThread(0x14, 3, 0, 36)
    Sleep(1500)
    OP_68(-6600, 900, 49400, 3000)
    MoveCamera(0, 21, 0, 3000)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x14, 3)
    OP_6F(0x79)

    #C1034
    ChrTalk(
        0x101,
        (
            "#6P#0002F艾丝蒂尔、约修亚，\x01",
            "还有小滴也……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12A19")

    #C1035
    ChrTalk(
        0x102,
        (
            "#6P#0102F呵呵……\x01",
            "你今天打扮得特别可爱哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A41")

    label("loc_12A19")


    #C1036
    ChrTalk(
        0x102,
        (
            "#6P#0102F哎呀……！\x01",
            "衣服好可爱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A41")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A1037
    AnonymousTalk(
        0x14,
        (
            "呵呵……\x01",
            "谢谢。\x02\x03",

            "各位，下午好。\x02",
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

    #C1038
    ChrTalk(
        0x103,
        "#0202F#5P打扰了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12B9A")

    #C1039
    ChrTalk(
        0x104,
        (
            "#6P#0309F喔喔，看样子，\x01",
            "你们今天好像玩得很痛快嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C1040
    ChrTalk(
        0x9,
        (
            "#1404F#5P我突然有急事，\x01",
            "所以他们代替我陪这孩子玩了。\x02\x03",

            "#1402F艾丝蒂尔、约修亚，\x01",
            "不好意思，给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CF0")

    label("loc_12B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_END)), "loc_12C4D")

    #C1041
    ChrTalk(
        0x104,
        (
            "#6P#0309F对哦，小滴\x01",
            "说过今天是她的外出日啊。\x02",
        )
    )

    CloseMessageWindow()

    #C1042
    ChrTalk(
        0x9,
        (
            "#1404F#5P嗯，我突然有急事，\x01",
            "所以他们代替我陪这孩子玩了。\x02\x03",

            "#1402F艾丝蒂尔、约修亚，\x01",
            "不好意思，给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CF0")

    label("loc_12C4D")


    #C1043
    ChrTalk(
        0x104,
        (
            "#6P#0300F什么，原来今天是小滴\x01",
            "的外出日啊？\x02",
        )
    )

    CloseMessageWindow()

    #C1044
    ChrTalk(
        0x9,
        (
            "#1404F#5P嗯，我突然有急事，\x01",
            "所以他们代替我陪这孩子玩了。\x02\x03",

            "#1402F艾丝蒂尔、约修亚，\x01",
            "不好意思，给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CF0")


    #C1045
    ChrTalk(
        0xB,
        (
            "#0802F#11P呵呵，没事啦。\x02\x03",

            "#0809F能和小滴一起玩，\x01",
            "我觉得很幸运哦。\x02\x03",

            "捏捏她那胖乎乎的可爱小脸蛋，\x01",
            "我这一天也过得很愉快呢！\x02",
        )
    )

    CloseMessageWindow()

    #C1046
    ChrTalk(
        0x14,
        "#11P#6010F艾、艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()

    #C1047
    ChrTalk(
        0xD,
        (
            "#12P#0906F真是的……\x01",
            "你又不是怪叔叔。\x02\x03",

            "#0901F──对了，\x01",
            "我从米歇尔先生那里听说了……\x02\x03",

            "协会和警察好像已经结成了\x01",
            "非正式的合作关系？\x02",
        )
    )

    CloseMessageWindow()

    #C1048
    ChrTalk(
        0x9,
        (
            "#1403F#5P嗯，等其他人来了，\x01",
            "我再一起说明。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    #C1049
    ChrTalk(
        0x9,
        (
            "#5P#1402F罗伊德，方便的话，\x01",
            "你们也一起来听吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C1050
    ChrTalk(
        0x101,
        "#6P#0000F好的……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    SetChrName("")

    #A1051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在和集合而来的游击士们\x01",
            "一起确认了当前情况，\x02\x03",

            "并分配好彼此的任务之后，\x01",
            "罗伊德一行决定暂时返回支援科。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_68(-2000, 1400, 3000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -2500, 0, 1800, 0)
    SetChrPos(0x102, -1500, 0, 1800, 0)
    SetChrPos(0x103, -3200, 0, 900, 0)
    SetChrPos(0x104, -800, 0, 900, 0)
    SetChrPos(0x14, -2000, 0, 800, 0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -2600, 0, 4000, 180)
    SetChrPos(0xB, 600, 0, 4200, 225)
    SetChrPos(0xD, 1200, 0, 3600, 225)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x8, -1400, 0, 4000, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, -400, 0, 5500, 180)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, -1400, 0, 5800, 180)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -2600, 0, 5500, 180)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, -3600, 0, 5200, 180)
    OP_4B(0x13, 0xFF)
    SetCameraDistance(22500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C1052
    ChrTalk(
        0x101,
        (
            "#12P#0004F──小滴就放心交给我们吧，\x01",
            "我们会负责好好照顾她的。\x02",
        )
    )

    CloseMessageWindow()

    #C1053
    ChrTalk(
        0x102,
        (
            "#12P#0100F科长也在那边，\x01",
            "而且还有一条很可靠的警犬，\x01",
            "所以请您不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C1054
    ChrTalk(
        0x9,
        (
            "#1404F#5P嗯，那就拜托了。\x02\x03",

            "#1402F──滴，\x01",
            "要乖乖等我来接你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C1055
    ChrTalk(
        0x14,
        (
            "#12P#6000F好的，爸爸。\x02\x03",

            "#6010F……那个……\x01",
            "爸爸，你们也要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C1056
    ChrTalk(
        0x9,
        "#1404F#5P嗯，不用担心。\x02",
    )

    CloseMessageWindow()

    #C1057
    ChrTalk(
        0xB,
        (
            "#11P#0806F嗯，要是能再多几个\x01",
            "人来帮忙就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C1058
    ChrTalk(
        0xD,
        (
            "#0900F#11P如果全员都出动的话，\x01",
            "这里就稍微有些守备不足了。\x02",
        )
    )

    CloseMessageWindow()

    #C1059
    ChrTalk(
        0x101,
        (
            "#12P#0006F不过，真的可以吗？\x02\x03",

            "#0001F我们是不是也应该分出点人，\x01",
            "参加搜索工作呢……\x02",
        )
    )

    CloseMessageWindow()

    #C1060
    ChrTalk(
        0xF,
        (
            "#5P哈哈，不用客气啦。\x02\x03",

            "#5P你们不是委托医院的医生检验\x01",
            "药物的成分，还要等待他的联络吗？\x02",
        )
    )

    CloseMessageWindow()

    #C1061
    ChrTalk(
        0x11,
        (
            "#5P找人的事就放心交给我们吧，\x01",
            "你们准备好应付今后的状况就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C1062
    ChrTalk(
        0x12,
        (
            "#5P嗯，不过还真没想到\x01",
            "有一天会和警察们合作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C1063
    ChrTalk(
        0x13,
        (
            "#1P呵呵，虽然这在雷米菲利亚\x01",
            "并不是什么新鲜事……\x02\x03",

            "各位，请多多指教哦。\x02",
        )
    )

    CloseMessageWindow()

    #C1064
    ChrTalk(
        0x104,
        "#12P#0309F哪里哪里～我们才是，请多指教！\x02",
    )

    CloseMessageWindow()

    #C1065
    ChrTalk(
        0x103,
        "#12P#0204F#N请多多指教。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C1066
    ChrTalk(
        0x8,
        (
            "#5P如果遇到什么情况的话，千万不用客气，\x01",
            "尽管与协会联络。\x02\x03",

            "#5P我们要是有什么发现，\x01",
            "也会马上联系支援科的。\x02",
        )
    )

    CloseMessageWindow()

    #C1067
    ChrTalk(
        0xB,
        (
            "#11P#0800F那么，\x01",
            "就一起努力吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    #C1068
    ChrTalk(
        0x101,
        "#6P#0000F嗯……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_116A3 end

    def Function_34_1351D(): pass

    label("Function_34_1351D")


    def lambda_13522():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_13522)

    def lambda_13533():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13533)
    WaitChrThread(0xB, 1)

    def lambda_13551():
        OP_95(0xFE, -4800, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13551)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xE1, 0x1F4)
    Return()

    # Function_34_1351D end

    def Function_35_13572(): pass

    label("Function_35_13572")

    Sleep(600)

    def lambda_1357A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1357A)

    def lambda_1358B():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1358B)
    WaitChrThread(0xD, 1)

    def lambda_135A9():
        OP_95(0xFE, -2700, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_135A9)
    WaitChrThread(0xD, 1)

    def lambda_135C7():
        OP_95(0xFE, -3300, 0, 49400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_135C7)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0x10E, 0x1F4)
    Return()

    # Function_35_13572 end

    def Function_36_135E8(): pass

    label("Function_36_135E8")

    Sleep(1200)

    def lambda_135F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_135F0)

    def lambda_13601():
        OP_95(0xFE, 0, 0, 50500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_13601)
    WaitChrThread(0x14, 1)

    def lambda_1361F():
        OP_95(0xFE, -3900, 0, 50500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1361F)
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0xE1, 0x1F4)
    Return()

    # Function_36_135E8 end

    def Function_37_13640(): pass

    label("Function_37_13640")

    TalkBegin(0xFF)
    SetChrName("")

    #A1069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贴有许多对游击士协会\x01",
            "的任务委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136D5")

    #C1070
    ChrTalk(
        0x104,
        (
            "#0305F好像也有\x01",
            "重大事件的委托啊。\x02",
        )
    )

    CloseMessageWindow()

    #C1071
    ChrTalk(
        0x101,
        "#0003F真不愧是游击士协会……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_136D5")

    TalkEnd(0xFF)
    Return()

    # Function_37_13640 end

    SaveToFile()

Try(main)
