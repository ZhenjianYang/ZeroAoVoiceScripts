from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0170.bin",                # FileName
        "c0170",                    # MapName
        "c0170",                    # Location
        0x0005,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0170",                  # 0
        "接待小姐帕尔",           # 1
        "接待小姐辛茜亚",         # 2
        "汉森",                   # 3
        "利乔",                   # 4
        "普拉达",                 # 5
        "贝卡",                   # 6
        "沙扎克",                 # 7
        "赛尔盖科长",             # 8
        "奈斯顿经理",             # 9
        "珍妮特",                 # 10
        "巴乔",                   # 11
        "德罗缇",                 # 12
        "肯",                     # 13
        "欧奈斯特老人",           # 14
        "桑桑",                   # 15
        "莉夏",                   # 16
        "普莉埃",                 # 17
    ))

    AddCharChip((
        "chr/ch27400.itc",                   # 00
        "chr/ch26600.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch20000.itc",                   # 05
        "chr/ch10400.itc",                   # 06
        "chr/ch34200.itc",                   # 07
        "chr/ch20400.itc",                   # 08
        "chr/ch21600.itc",                   # 09
        "chr/ch02500.itc",                   # 0A
        "chr/ch32500.itc",                   # 0B
        "chr/ch05200.itc",                   # 0C
        "chr/ch29000.itc",                   # 0D
        "chr/ch34600.itc",                   # 0E
        "chr/ch25900.itc",                   # 0F
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   14,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   15,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-11529,  8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-15989,  0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(8289,    0,       2460,    90,   385,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2660,   0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-6659,   8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(14930,   0,       2589,    90,   257,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   22,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-14449,  8000,    14420,   90,   257,  0x0, 0,   9,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(14220,   8000,    21190,   90,   405,  0x0, 0,   11,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(14220,   8000,    22209,   90,   405,  0x0, 0,   12,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(8750,    0,       1879,    90,   389,  0x0, 0,   13,  0,   0,   0,   0,   28,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  4,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  6,  0x0000)
    DeclActor(-480,    8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  8,  0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  10, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  12, 0x0000)
    DeclActor(-12390,  8000,    7660,    1000,    -11530,  9500,    8510,    0x007E, 0,  14, 0x0000)
    DeclActor(-16030,  0,       23800,   1000,    -15990,  1500,    25740,   0x007E, 0,  16, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  37, 0x0000)
    DeclActor(5790,    0,       9800,    1000,    6620,    1500,    10670,   0x007E, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_48C",          # 00, 0
        "Function_1_544",          # 01, 1
        "Function_2_61D",          # 02, 2
        "Function_3_839",          # 03, 3
        "Function_4_8FD",          # 04, 4
        "Function_5_901",          # 05, 5
        "Function_6_1459",         # 06, 6
        "Function_7_145D",         # 07, 7
        "Function_8_1F08",         # 08, 8
        "Function_9_1F0C",         # 09, 9
        "Function_10_2AC2",        # 0A, 10
        "Function_11_2AC6",        # 0B, 11
        "Function_12_3A17",        # 0C, 12
        "Function_13_3A1B",        # 0D, 13
        "Function_14_45E8",        # 0E, 14
        "Function_15_45EC",        # 0F, 15
        "Function_16_5592",        # 10, 16
        "Function_17_5596",        # 11, 17
        "Function_18_650D",        # 12, 18
        "Function_19_66B6",        # 13, 19
        "Function_20_7C90",        # 14, 20
        "Function_21_8818",        # 15, 21
        "Function_22_9271",        # 16, 22
        "Function_23_98E5",        # 17, 23
        "Function_24_9F41",        # 18, 24
        "Function_25_A9AA",        # 19, 25
        "Function_26_A9B4",        # 1A, 26
        "Function_27_A9BE",        # 1B, 27
        "Function_28_AC50",        # 1C, 28
        "Function_29_AC9A",        # 1D, 29
        "Function_30_B15C",        # 1E, 30
        "Function_31_B710",        # 1F, 31
        "Function_32_BCA6",        # 20, 32
        "Function_33_C225",        # 21, 33
        "Function_34_C79E",        # 22, 34
        "Function_35_C98D",        # 23, 35
        "Function_36_CAA8",        # 24, 36
        "Function_37_D22A",        # 25, 37
    ))


    def Function_0_48C(): pass

    label("Function_0_48C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4CC"),
        (1, "loc_4D8"),
        (2, "loc_4E4"),
        (3, "loc_4F0"),
        (4, "loc_4FC"),
        (5, "loc_508"),
        (6, "loc_514"),
        (SWITCH_DEFAULT, "loc_520"),
    )


    label("loc_4CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_508")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_514")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_520")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_52C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_543")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_543")

    Return()

    # Function_0_48C end

    def Function_1_544(): pass

    label("Function_1_544")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61C")
    OP_95(0xFE, 13800, 8000, 6200, 2000, 0x0)
    OP_95(0xFE, 14520, 8000, 20050, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8530, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -14240, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 23430, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 7560, 2000, 0x0)
    OP_95(0xFE, -11380, 8000, 2990, 2000, 0x0)
    OP_95(0xFE, 14040, 8000, 2490, 2000, 0x0)
    Jump("Function_1_544")

    label("loc_61C")

    Return()

    # Function_1_544 end

    def Function_2_61D(): pass

    label("Function_2_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_64D")
    SetChrPos(0x11, 14240, 0, 2440, 270)
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_838")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_688")
    Jump("loc_838")

    label("loc_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6A7")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6E3")
    SetChrPos(0x9, 6620, 0, 10670, 225)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_END)), "loc_6DE")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_6DE")

    Jump("loc_838")

    label("loc_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_70C")
    SetChrPos(0x9, 6620, 0, 10670, 225)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_838")

    label("loc_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_730")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_760")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    SetChrPos(0x11, -17370, 30, 22740, 45)
    Jump("loc_838")

    label("loc_760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_784")
    SetChrPos(0x11, 14240, 0, 2440, 270)
    SetChrFlags(0x12, 0x80)
    Jump("loc_838")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7B6")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x11, 14040, 8000, 21830, 90)
    Jump("loc_838")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7D5")
    SetChrPos(0x11, -17370, 30, 22740, 45)
    Jump("loc_838")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7F4")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_813")
    SetChrPos(0x11, -5240, 8000, 5490, 0)
    Jump("loc_838")

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_821")
    Jump("loc_838")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_82F")
    Jump("loc_838")

    label("loc_82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_838")

    label("loc_838")

    Return()

    # Function_2_61D end

    def Function_3_839(): pass

    label("Function_3_839")

    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_84B")
    Jump("loc_860")

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_860")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_66(0x8, 0x1)

    label("loc_860")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_881")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_88F")

    label("loc_881")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AB")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8C2")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8C2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8C2")

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8D0")
    Jump("loc_8FC")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8EA")
    Jump("loc_8FC")

    label("loc_8EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_8FC")
    OP_1B(0x0, 0x0, 0x23)

    label("loc_8FC")

    Return()

    # Function_3_839 end

    def Function_4_8FD(): pass

    label("Function_4_8FD")

    Call(0, 5)
    Return()

    # Function_4_8FD end

    def Function_5_901(): pass

    label("Function_5_901")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_932")
    TurnDirection(0x0, 0x8, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Call(0, 36)
    Return()

    label("loc_932")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_984")

    #C0001
    ChrTalk(
        0x8,
        "呵呵，能找到就好哦。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "『时代』百货店\x01",
            "欢迎您的下次光临。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1455")

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F1")

    #C0003
    ChrTalk(
        0x8,
        (
            "呼……斯克特的工作\x01",
            "什么时候才能变得\x01",
            "轻松一点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "……结婚还早得很啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A50")

    label("loc_9F1")


    #C0005
    ChrTalk(
        0x8,
        (
            "……啊，对不起！\x01",
            "不小心发了呆。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "如果有什么需要，\x01",
            "请尽管吩咐。\x01",
            "我们会认真为您服务的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A50")

    Jump("loc_1455")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AC2")

    #C0007
    ChrTalk(
        0x8,
        (
            "工作才刚刚开始，\x01",
            "这种时候总让人感觉\x01",
            "懒洋洋的，心情也轻松愉快。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "今天也请\x01",
            "加油工作哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1455")

    label("loc_AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B67")

    #C0009
    ChrTalk(
        0x8,
        (
            "欢迎光临\x01",
            "『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "本店为了抓住顾客的心，\x01",
            "会举办各种各样的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "『抓住顾客的心，就能让顾客展现笑容』……\x01",
            "这是我们经理的座右铭。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1455")

    label("loc_B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D1B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BEB")

    #C0012
    ChrTalk(
        0x8,
        (
            "为恋人选购礼物，\x01",
            "真是一个非常快乐的过程呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "呵呵，请您尽情享受\x01",
            "购物的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA")

    label("loc_BEB")


    #C0014
    ChrTalk(
        0x8,
        (
            "客人……您莫非是在\x01",
            "挑选送给恋人的\x01",
            "礼物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "您与恋人的感情真是好呢。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x19F,
        (
            "哎……\x01",
            "啊，不不，我和芙兰小姐\x01",
            "还不是那种……！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#0006F（猜错了这个事实本身，才是最让人难过的呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_CAA")

    Jump("loc_D16")

    label("loc_CAF")


    #C0018
    ChrTalk(
        0x8,
        (
            "欢迎光顾麦克道尔\x01",
            "市长的指定购物场所——\x01",
            "『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "……这种说法是不是\x01",
            "有点太夸张了啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D16")

    Jump("loc_1455")

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_D29")
    Jump("loc_1455")

    label("loc_D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC4")

    #C0020
    ChrTalk(
        0x8,
        (
            "辛茜亚前辈那样的美人\x01",
            "给人的一贯印象就是穿\x01",
            "着高跟鞋，气质冷艳……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "早上看到她穿着运动鞋\x01",
            "来上班的时候，真是有些\x01",
            "吃惊呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E41")

    label("loc_DC4")


    #C0022
    ChrTalk(
        0x8,
        (
            "辛茜亚前辈那样的美人\x01",
            "给人的一贯印象就是穿\x01",
            "着高跟鞋，气质冷艳……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "但她这种比较适合休闲风的\x01",
            "印象反差，更加吸引人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E41")

    Jump("loc_1455")

    label("loc_E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_EFA")

    #C0024
    ChrTalk(
        0x8,
        (
            "奈斯顿经理负责过\x01",
            "各种各样的企划活动，\x01",
            "是个很能干的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "似乎还曾经在创立纪念庆典\x01",
            "中负责过活动安排呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "嗯～虽然我也说不太清楚，\x01",
            "但总之不是寻常之辈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1455")

    label("loc_EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_F73")

    #C0027
    ChrTalk(
        0x8,
        (
            "……啊，珍妮特\x01",
            "望着食品卖场，\x01",
            "正在流口水呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "呵呵，她那种孩子气的地方\x01",
            "总能让我们感到轻松愉快呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1455")

    label("loc_F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_102C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8E")
    Call(0, 7)
    Jump("loc_1027")

    label("loc_F8E")

    TurnDirection(0x8, 0x0, 0)

    #C0029
    ChrTalk(
        0x8,
        (
            "其实我和协会中的一位\x01",
            "游击士已经定了婚呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "啊，虽然因为他很忙，很少有机会\x01",
            "见面，但他一直都很重视我，\x01",
            "为我着想，是个很好的人哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 0)

    label("loc_1027")

    Jump("loc_1455")

    label("loc_102C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DF")

    #C0031
    ChrTalk(
        0x8,
        (
            "这里也提供查询列车和巴士，\x01",
            "以及飞行船时刻表的服务哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "因为我们的客人有很多是从帝国\x01",
            "或共和国前来光顾的。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "如有需要，欢迎各位随时前来查询。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_113B")

    label("loc_10DF")


    #C0034
    ChrTalk(
        0x8,
        (
            "这里也提供查询列车和巴士，\x01",
            "以及飞行船时刻表的服务哦。\x01",
            "如有需要，欢迎各位随时前来查询。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113B")

    Jump("loc_1455")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_11F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C0")

    #C0035
    ChrTalk(
        0x8,
        (
            "……呼……斯克特现在\x01",
            "正在做什么呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x8,
        (
            "失、失礼了。\x01",
            "竟然在客人面前……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11EB")

    label("loc_11C0")


    #C0037
    ChrTalk(
        0x8,
        (
            "实在是失礼了。\x01",
            "竟然在客人面前叹气……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EB")

    Jump("loc_1455")

    label("loc_11F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1240")

    #C0038
    ChrTalk(
        0x8,
        (
            "经理好像又有\x01",
            "什么灵感了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "是在策划一些\x01",
            "新的活动吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1455")

    label("loc_1240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_128B")

    #C0040
    ChrTalk(
        0x8,
        "各位，早上好。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "希望大家都能精神饱满地\x01",
            "度过今天哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1455")

    label("loc_128B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_138E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1316")

    #C0042
    ChrTalk(
        0x8,
        (
            "辛茜亚前辈可是这个百货店\x01",
            "中的偶像级店员呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "不但漂亮，而且十分有女人味，\x01",
            "街上的很多女孩子都很憧憬她。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1389")

    label("loc_1316")


    #C0044
    ChrTalk(
        0x8,
        (
            "辛茜亚前辈可是这个百货店\x01",
            "中的偶像级店员呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "呵呵……其实我也\x01",
            "是因为憧憬辛茜亚前辈，\x01",
            "才会选择这个工作的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1389")

    Jump("loc_1455")

    label("loc_138E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1411")

    #C0046
    ChrTalk(
        0x8,
        (
            "进口食材、洋装、\x01",
            "鞋子、杂货、饰品……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "本店有各种类型的专柜呢。\x01",
            "呵呵，各位要不要亲自去看看呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1455")

    label("loc_1411")


    #C0048
    ChrTalk(
        0x8,
        (
            "本店有各种\x01",
            "类型的专柜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "呵呵，各位要不要\x01",
            "亲自去看看呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1455")

    TalkEnd(0x8)
    Return()

    # Function_5_901 end

    def Function_6_1459(): pass

    label("Function_6_1459")

    Call(0, 7)
    Return()

    # Function_6_1459 end

    def Function_7_145D(): pass

    label("Function_7_145D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148E")
    TurnDirection(0x0, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Call(0, 36)
    Return()

    label("loc_148E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_154F")

    #C0050
    ChrTalk(
        0x9,
        (
            "在本店里，\x01",
            "经常会发现遗失物。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "平时一直都要保管着十几件左右……\x01",
            "按规定，如果发现后一周内都无人认领，\x01",
            "就要将失物交给警察了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "也请各位客人多加小心，\x01",
            "不要遗失物品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_154F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_15DA")

    #C0053
    ChrTalk(
        0x9,
        (
            "夕阳西下的克洛斯贝尔市……\x01",
            "实在是很美呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "美丽的自然风景虽然也不错，\x01",
            "但在这种近代文化的景观下\x01",
            "慢跑，感觉也不坏呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_15DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_166B")

    #C0055
    ChrTalk(
        0x9,
        (
            "早上好，欢迎光临\x01",
            "『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "虽然刚刚开店，\x01",
            "但客人们已经可以随意选购了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "请您不必拘束，\x01",
            "尽情享受购物的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1726")

    #C0058
    ChrTalk(
        0x9,
        (
            "从经理的表情来看，他好像非常开心呢，\x01",
            "简直就像是一个发现了新玩具的\x01",
            "小孩子一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "每当他露出那种表情时，\x01",
            "肯定都是又想出了一些新的好企划。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        "呵呵，很令人期待啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1827")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17BF")

    #C0061
    ChrTalk(
        0x9,
        (
            "一层有杂货店、进口食品店，\x01",
            "二层有时装店、鞋店和\x01",
            "饰品店。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "柜台众多，总会有客人您\x01",
            "需要的商品。\x01",
            "请随意挑选吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_17BF")


    #C0063
    ChrTalk(
        0x9,
        (
            "经理从以前开始，\x01",
            "就在各行各业担任\x01",
            "企划人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "在财经界与政治界中\x01",
            "也都有着相当的知名度呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1822")

    Jump("loc_1F04")

    label("loc_1827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_18C2")

    #C0065
    ChrTalk(
        0x9,
        (
            "纪念庆典之后的休假\x01",
            "真是过得非常充实。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "在湛蓝的天空之下慢跑，\x01",
            "使人的心情非常爽朗愉快。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "呵呵，下次也叫上帕尔，\x01",
            "两个人一起跑吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_18C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_194A")

    #C0068
    ChrTalk(
        0x9,
        (
            "也许你会觉得意外吧，\x01",
            "慢跑正是我的爱好。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "在休息日等闲暇时间，\x01",
            "我经常在克洛斯贝尔\x01",
            "市内的各处慢跑呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19B3")

    label("loc_194A")


    #C0070
    ChrTalk(
        0x9,
        (
            "也许你会觉得意外吧，\x01",
            "慢跑正是我的爱好。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "我的运动鞋是在二层\x01",
            "的鞋店里买的，\x01",
            "我也向客人您推荐哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B3")

    Jump("loc_1F04")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1A64")

    #C0072
    ChrTalk(
        0x9,
        (
            "我以前在雷米菲利亚公国\x01",
            "的百货店工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "然后被这里的经理挖角，\x01",
            "跳槽到了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "被奈斯顿经理这种\x01",
            "富于才干的人物发现提拔，\x01",
            "我感到非常光荣呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1AC0")

    #C0075
    ChrTalk(
        0x9,
        "太阳也下山了啊。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "在临近关店的时间，\x01",
            "店内会播放\x01",
            "克洛斯贝尔的市歌呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1C0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA0")
    TurnDirection(0x9, 0x8, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0077
    ChrTalk(
        0x9,
        (
            "呵呵……帕尔\x01",
            "现在正是烦恼最多的时候呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "不管怎么说，见不到恋人，\x01",
            "果然还是很寂寞吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x8,
        (
            "是、是啊……\x01",
            "定下婚约之后都已经整整一年了，可是……！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C06")

    label("loc_1BA0")


    #C0080
    ChrTalk(
        0x9,
        (
            "啊……实在是失礼了。\x01",
            "竟然在客人面前说私事……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "请问您有什么需要吗？\x01",
            "我会诚心诚意为您服务的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C06")

    Jump("loc_1F04")

    label("loc_1C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1C70")

    #C0082
    ChrTalk(
        0x9,
        "欢迎光临『时代』百货店。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "您要挑选什么东西吗？\x01",
            "我可以为您进行各专柜的导购哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1CD2")

    #C0084
    ChrTalk(
        0x9,
        (
            "多谢您今日再度光顾\x01",
            "『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "请注意自己的随身物品，\x01",
            "不要丢失遗落。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1D58")

    #C0086
    ChrTalk(
        0x9,
        (
            "『经营百货店的诀窍，其实就是\x01",
            "  不断刺激顾客们的新鲜感。』\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "……这是经理的口头禅，\x01",
            "很期待经理策划的下个活动呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1DC4")

    #C0088
    ChrTalk(
        0x9,
        (
            "本店会尽力\x01",
            "满足客人们的一切要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "如果您对我们的服务有什么不满，\x01",
            "请随时向我们反映。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1E27")

    #C0090
    ChrTalk(
        0x9,
        (
            "感谢您今天\x01",
            "也前来光顾本店。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "如果对本店\x01",
            "有什么意见或建议，\x01",
            "请尽管告知我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F04")

    label("loc_1E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB2")

    #C0092
    ChrTalk(
        0x9,
        "欢迎光临『时代』百货店。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "这里是\x01",
            "综合服务台。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "如果您在店内有什么需要，\x01",
            "请不必客气，尽管前来咨询。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F04")

    label("loc_1EB2")


    #C0095
    ChrTalk(
        0x9,
        (
            "这里是\x01",
            "综合服务台。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "如果您在店内有什么需要，\x01",
            "请不必客气，尽管前来咨询。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F04")

    TalkEnd(0x9)
    Return()

    # Function_7_145D end

    def Function_8_1F08(): pass

    label("Function_8_1F08")

    Call(0, 9)
    Return()

    # Function_8_1F08 end

    def Function_9_1F0C(): pass

    label("Function_9_1F0C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1F1D")
    Jump("loc_1F4B")

    label("loc_1F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F4B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F37")
    Jump("loc_1F4B")

    label("loc_1F37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_1F4B")
    Call(0, 32)
    TalkEnd(0xA)
    Return()

    label("loc_1F4B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FA5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1FA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FC4")
    OP_AF(0x22)
    Jump("loc_1FC6")

    label("loc_1FC4")

    OP_AF(0x21)

    label("loc_1FC6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AB9")

    label("loc_1FD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FE9")
    Jump("loc_2AB9")

    label("loc_1FE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_20CB")

    #C0097
    ChrTalk(
        0xA,
        (
            "普拉达小姐又向我\x01",
            "提出挑战了呢。\x01",
            "哎呀呀，真是个喜欢竞争的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "不过，竞争能使人不断进步，\x01",
            "将自身提升至新境界，这也是事实……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "为了彼此督促，共同提高，\x01",
            "我准备接受\x01",
            "她的挑战哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_20CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2153")

    #C0100
    ChrTalk(
        0xA,
        (
            "如果觉得鞋子穿不惯，也只有\x01",
            "多穿多走才能慢慢适应了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "如果因为是新鞋而太过珍惜，\x01",
            "以至于不舍得穿，鞋子都会难过的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_2153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2218")

    #C0102
    ChrTalk(
        0xA,
        "本店也承接修鞋业务。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "如果要修的鞋子是旧款，便需要准备相关配件，\x01",
            "所以价格会比较昂贵……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "但有些客人比较怀旧，希望能\x01",
            "继续穿着寄托了自己感情的鞋子，\x01",
            "所以本服务颇受好评呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_2218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_22C8")

    #C0105
    ChrTalk(
        0xA,
        (
            "加装气垫的鞋子最近\x01",
            "在年轻人之中很流行。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "因为可以吸收冲击力，\x01",
            "所以最适合长时间运动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "斯托雷加公司最近几年的新\x01",
            "款式几乎也都采用了这种\x01",
            "气垫设计呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_22C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_233D")

    #C0108
    ChrTalk(
        0xA,
        (
            "哎呀，客人……\x01",
            "您之前选购的鞋子，\x01",
            "是给这位小朋友穿的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#0100F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_240F")

    label("loc_233D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_23A3")

    #C0110
    ChrTalk(
        0xA,
        (
            "哎呀，客人……\x01",
            "您之前选购的鞋子，\x01",
            "是给这位小朋友穿的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        "#0200F之前多谢您了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_240F")

    label("loc_23A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_240F")

    #C0112
    ChrTalk(
        0xA,
        (
            "哎呀，这位小朋友的鞋子，\x01",
            "就是刚才那两位女性顾客买的那款呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#0300F啊，那是我们的同伴。\x02",
    )

    CloseMessageWindow()

    label("loc_240F")


    #C0114
    ChrTalk(
        0xA,
        (
            "呵呵，走起来感觉还合脚吗？\x01",
            "毕竟选择了稍微大一点的号码。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x153,
        "#1110F嗯，很宽松很舒服的～！\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "那就好。\x01",
            "如果还有什么需要，请尽管吩咐哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2521")

    label("loc_24A5")


    #C0117
    ChrTalk(
        0xA,
        (
            "小孩子的脚长得很快。\x01",
            "所以比起刚好合适的，还是买稍大一点的尺寸为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "下次来百货店的时候，请一定\x01",
            "再来本柜台看看哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2521")

    Jump("loc_2AB9")

    label("loc_2526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_259C")

    #C0119
    ChrTalk(
        0xA,
        (
            "太小的鞋子有可能会\x01",
            "妨碍小孩的成长。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        (
            "比起鞋子大小刚好合适，我还是推荐\x01",
            "鞋头部分稍微松快一点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_259C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_25FD")

    #C0121
    ChrTalk(
        0xA,
        (
            "我们这里的鞋子，\x01",
            "尺码都非常齐全哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        "想试的话，请不用客气，尽管和我说吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_25FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_264E")

    #C0123
    ChrTalk(
        0xA,
        (
            "呀，这种时间了，竟然还在忙，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        "急着买鞋子吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_264E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_26D7")

    #C0125
    ChrTalk(
        0xA,
        (
            "最近大受欢迎的是这种\x01",
            "看起来像皮鞋的运动鞋。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "即使穿去职场也不会显得随便，\x01",
            "所以在商务人士之中\x01",
            "也悄然流行起来了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_26D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2777")

    #C0127
    ChrTalk(
        0xA,
        (
            "像客人您这种出于工作原因，需要经常奔走\x01",
            "的人，我建议还是应该选一双好点的鞋子。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xA,
        (
            "根据鞋子的不同，长途跋涉之后\x01",
            "的疲劳程度也会有很大差异哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_2777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_27F6")

    #C0129
    ChrTalk(
        0xA,
        (
            "在克洛斯贝尔自治州，\x01",
            "有个名为创立纪念庆典\x01",
            "的重大事件哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "对任何店铺而言，庆典期间\x01",
            "都是最大的销售旺季。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_27F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_285E")

    #C0131
    ChrTalk(
        0xA,
        (
            "听说最近又出现和黑手党\x01",
            "有关的传闻了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "只要别影响到游客\x01",
            "前来旅游的意愿就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_285E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_28F8")

    #C0133
    ChrTalk(
        0xA,
        (
            "鞋子的款式能很好地\x01",
            "体现出各职业人士的性格。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "即使是同种类型的鞋子，\x01",
            "外观也会有非常大的区别……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        "只要这么一想，就会觉得很兴奋。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_28F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_29B1")

    #C0136
    ChrTalk(
        0xA,
        (
            "我以前主要是销售服装的，\x01",
            "进入百货店后则开始专门经营鞋类。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "时装店的普拉达小姐是我在\x01",
            "个人经营时代的竞争对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "即使是现在，她也经常\x01",
            "会到这边来向我提出挑战呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB9")

    label("loc_29B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2AB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A51")

    #C0139
    ChrTalk(
        0xA,
        (
            "欢迎光临，\x01",
            "本店出售各种鞋子。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "运动鞋、皮鞋、长靴……\x01",
            "客人们需要的款式，\x01",
            "我们这里一应俱全。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        "请您放松心情，随意挑选吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2AB9")

    label("loc_2A51")


    #C0142
    ChrTalk(
        0xA,
        (
            "大受欢迎的运动鞋品牌——\x01",
            "斯托雷加公司的产品，\x01",
            "我们也预定陆续进货。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        "请您放松心情，随意挑选吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2AB9")

    Jump("loc_1F55")

    label("loc_2ABE")

    TalkEnd(0xA)
    Return()

    # Function_9_1F0C end

    def Function_10_2AC2(): pass

    label("Function_10_2AC2")

    Call(0, 11)
    Return()

    # Function_10_2AC2 end

    def Function_11_2AC6(): pass

    label("Function_11_2AC6")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2AD7")
    Jump("loc_2B05")

    label("loc_2AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2B05")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2AF1")
    Jump("loc_2B05")

    label("loc_2AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_2B05")
    Call(0, 30)
    TalkEnd(0xB)
    Return()

    label("loc_2B05")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A13")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B5F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2B5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B7F")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A0E")

    label("loc_2B7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B93")
    Jump("loc_3A0E")

    label("loc_2B93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2C21")

    #C0144
    ChrTalk(
        0xB,
        (
            "阿尔摩利卡村产的新鲜蔬菜\x01",
            "已经到货了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "不管怎么说，\x01",
            "还是这种刚刚采摘来的\x01",
            "新鲜食材最美味呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0E")

    label("loc_2C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C97")

    #C0146
    ChrTalk(
        0xB,
        (
            "如果店里缺少什么您需要的商品，\x01",
            "请不必客气，尽管告知。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "我不管花费多少心力，\x01",
            "也都会为您进货的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0E")

    label("loc_2C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6C")

    #C0148
    ChrTalk(
        0xB,
        (
            "最近的天气很不错呢。\x01",
            "多亏如此，我女儿的果汁店\x01",
            "生意也很红火。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "好像还有不少常客光顾，\x01",
            "她在家里也都很自豪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "呵呵……只她要开心，就比什么都好啊。\x01",
            "身为母亲，我也替她高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DD2")

    label("loc_2D6C")


    #C0151
    ChrTalk(
        0xB,
        (
            "女儿想要凭自己的力量做些生意，\x01",
            "所以开起了果汁店。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "呵呵……她的生意似乎也\x01",
            "开始走上正轨了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD2")

    Jump("loc_3A0E")

    label("loc_2DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2E2D")

    #C0153
    ChrTalk(
        0xB,
        "本店优质的食材一应俱全。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        "希望您能将它们变成一桌丰盛的大餐哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A0E")

    label("loc_2E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2F72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F17")

    #C0155
    ChrTalk(
        0xB,
        (
            "如果想做出美味的料理，\x01",
            "需要烹调者的高超技术以及品质上乘的食材……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "二者缺一不可。\x01",
            "但更重要的，我觉得还是一颗\x01",
            "为用餐者考虑的『心』。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "啊，各位要买点什么吗～？\x01",
            "如果没有食材，\x01",
            "可就做不成料理了哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F6D")

    label("loc_2F17")


    #C0158
    ChrTalk(
        0xB,
        (
            "今晚的料理，\x01",
            "就用国王马铃薯来做如何呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "我今天新进了一些\x01",
            "特别棒的食材哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F6D")

    Jump("loc_3A0E")

    label("loc_2F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_304E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300B")

    #C0160
    ChrTalk(
        0xB,
        (
            "随着纪念庆典的临近，\x01",
            "客人果然也增加了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "……呵呵，我女儿现在\x01",
            "也正在努力工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        "我这个当妈妈的也不能输啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3049")

    label("loc_300B")


    #C0163
    ChrTalk(
        0xB,
        (
            "女儿自己开了果汁店，\x01",
            "正在努力工作呢。\x01",
            "我也不能输给她啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3049")

    Jump("loc_3A0E")

    label("loc_304E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F0")

    #C0164
    ChrTalk(
        0xB,
        (
            "今天早上的铁路货运\x01",
            "由于货物检查而送晚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "因为送的都是新鲜蔬菜，\x01",
            "所以很慌张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xB,
        (
            "啊痛痛痛……闪到腰了。\x01",
            "我也上年纪了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_313B")

    label("loc_30F0")


    #C0167
    ChrTalk(
        0xB,
        (
            "今天早上的铁路货运\x01",
            "由于货物检查而送晚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        "铁路货运经常会送迟呢。\x02",
    )

    CloseMessageWindow()

    label("loc_313B")

    Jump("loc_3A0E")

    label("loc_3140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_31B5")

    #C0169
    ChrTalk(
        0xB,
        (
            "差不多也该到了\x01",
            "下班回家的客人增多的时间了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "百货店的营业\x01",
            "这才刚要开始呢，\x01",
            "还要继续加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0E")

    label("loc_31B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_32C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3263")

    #C0171
    ChrTalk(
        0xB,
        (
            "嗯～共和国产的最高级葡萄酒\x01",
            "这周需要进三十箱。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        (
            "纪念庆典之前的这段时间，宴会用的\x01",
            "高级食材的需求量也增加了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "还是早点下订单\x01",
            "为好呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32BE")

    label("loc_3263")


    #C0174
    ChrTalk(
        0xB,
        (
            "纪念庆典之前的这段时间，宴会用的\x01",
            "食材的需求量也增加了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        "高级食材也都卖得很好呢。\x02",
    )

    CloseMessageWindow()

    label("loc_32BE")

    Jump("loc_3A0E")

    label("loc_32C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_33EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3383")

    #C0176
    ChrTalk(
        0xB,
        (
            "我女儿在行政区\x01",
            "经营着一家果汁店。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "看来她已经完全习惯了经商，\x01",
            "在家里好像都有些自傲了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        (
            "呵呵，但在我看来，她还差得很远呢。\x01",
            "商人之道可是非常险峻的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33E5")

    label("loc_3383")


    #C0179
    ChrTalk(
        0xB,
        (
            "我以前也自己开过店，\x01",
            "所以对经商方面很熟悉。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "我女儿虽然好像很努力，\x01",
            "但其实还差得很远呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E5")

    Jump("loc_3A0E")

    label("loc_33EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_347D")

    #C0181
    ChrTalk(
        0xB,
        (
            "欢迎光临～！\x01",
            "欢迎光顾『利乔食品店』～！\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "今天刚到了利贝尔产的\x01",
            "苦西红柿哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xB,
        (
            "据说是很好的健康食品呢，\x01",
            "要不要来一个呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0E")

    label("loc_347D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_364F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D6")

    #C0184
    ChrTalk(
        0xB,
        (
            "最近有个经常来买\x01",
            "高级红茶的常客。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        "好像是叫赛尔盖吧……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xB,
        (
            "呵呵，真是个有趣又健谈的人。\x01",
            "今天和我闲聊了将近一个小时呢⊥\x02",
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

    #C0187
    ChrTalk(
        0x102,
        (
            "#0106F（科长……在我们\x01",
            "  辛苦工作的时候，竟然……）\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        "#0200F（……超级差劲……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_364A")

    label("loc_35D6")


    #C0189
    ChrTalk(
        0xB,
        (
            "赛尔盖先生是个经常来买高级\x01",
            "红茶的老顾客哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xB,
        (
            "呵呵，真是位有趣又健谈的人啊。\x01",
            "今天和我闲聊了将近一个小时呢⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_364A")

    Jump("loc_3A0E")

    label("loc_364F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_37BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3755")

    #C0191
    ChrTalk(
        0xB,
        (
            "最近，共和国的产粮地区\x01",
            "一直在下雨呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xB,
        (
            "嗯～大概是从上周开始，\x01",
            "共和国产的蔬菜开始涨价，\x01",
            "所以帝国产蔬菜的进货量要增加两成……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "……嗯，这种价格变动\x01",
            "可以通过调整进货量来弥补。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xB,
        (
            "可以的话，我希望\x01",
            "能尽量避免给客人带来不便。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37B5")

    label("loc_3755")


    #C0195
    ChrTalk(
        0xB,
        (
            "想订购进口食材的话，\x01",
            "也必须要关注国外的形势。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "呵呵，那也正是这份工作\x01",
            "的奥秘与乐趣呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B5")

    Jump("loc_3A0E")

    label("loc_37BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_392A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D3")

    #C0197
    ChrTalk(
        0xB,
        (
            "我们是天下闻名的『时代』百货店，\x01",
            "食材的品种之全，在克洛斯贝尔也数第一哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "从帝国产、共和国产，\x01",
            "到利贝尔产、雷米菲利亚产……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "甚至连奥雷德自治州产的香辛料，我们都有出售。\x01",
            "货源遍布世界各地呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "呵呵，顺便一说，\x01",
            "我还想继续增加进货的品种。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3925")

    label("loc_38D3")


    #C0201
    ChrTalk(
        0xB,
        (
            "其实我以前就是个\x01",
            "贸易商哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xB,
        (
            "然后就不知不觉开始热衷于\x01",
            "进口食材的经营了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3925")

    Jump("loc_3A0E")

    label("loc_392A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39B2")

    #C0203
    ChrTalk(
        0xB,
        (
            "欢迎您光顾\x01",
            "『利乔食品店』～\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xB,
        (
            "就算是进口食材，\x01",
            "我们这里也是应有尽有哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "请不必客气，\x01",
            "随意挑选～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A0E")

    label("loc_39B2")


    #C0206
    ChrTalk(
        0xB,
        (
            "我们也会使用铁路货运和飞行船运输\x01",
            "等方式来订购进口食材哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xB,
        (
            "请不必客气，\x01",
            "随意挑选～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0E")

    Jump("loc_2B0F")

    label("loc_3A13")

    TalkEnd(0xB)
    Return()

    # Function_11_2AC6 end

    def Function_12_3A17(): pass

    label("Function_12_3A17")

    Call(0, 13)
    Return()

    # Function_12_3A17 end

    def Function_13_3A1B(): pass

    label("Function_13_3A1B")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A2C")
    Jump("loc_3A5A")

    label("loc_3A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A5A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A46")
    Jump("loc_3A5A")

    label("loc_3A46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_3A5A")
    Call(0, 31)
    TalkEnd(0xC)
    Return()

    label("loc_3A5A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45E4")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AB4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3AB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AD3")
    OP_AF(0x1F)
    Jump("loc_3AD5")

    label("loc_3AD3")

    OP_AF(0x1E)

    label("loc_3AD5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45DF")

    label("loc_3AE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AF8")
    Jump("loc_45DF")

    label("loc_3AF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45DF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3B93")

    #C0208
    ChrTalk(
        0xC,
        (
            "与『时尚』接触的经历，\x01",
            "能使自己产生彻底改变……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xC,
        (
            "只有努力寻觅，了解各种服装的人，\x01",
            "才能得到这种贵重的经历。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_3B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C2E")

    #C0210
    ChrTalk(
        0xC,
        (
            "成熟气质的服装、充满童趣的服装……\x01",
            "世界上存在着很多种\x01",
            "不同的时尚风格。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xC,
        (
            "与其穿着不适合自己的成熟衣服，\x01",
            "还是符合自己风格的衣服最好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_3C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3D04")

    #C0212
    ChrTalk(
        0xC,
        "制服真是很美哦。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xC,
        (
            "那种以便于工作为目的而设计，\x01",
            "最适合在工作场所中穿着的服装，\x01",
            "其实拥有着光凭眼睛无法捕捉的美感呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "像警察官和警备队的制服，\x01",
            "我也都视为有价值的时尚服装，\x01",
            "高价买来收藏呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_3D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3D98")

    #C0215
    ChrTalk(
        0xC,
        (
            "有时候，装饰的突出点稍有不同，\x01",
            "就能让装扮的整体感觉\x01",
            "都发生改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        (
            "你们买了新衣服之后，\x01",
            "也可以到贝卡先生那里去\x01",
            "配一些饰品哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_3D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3FBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3E0D")

    #C0217
    ChrTalk(
        0xC,
        "啊，客人您不就是刚才的……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#0100F刚刚麻烦您帮我们\x01",
            "挑选衣服，\x01",
            "真是多谢了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED7")

    label("loc_3E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3E6F")

    #C0219
    ChrTalk(
        0xC,
        "啊，客人您不就是刚才的……\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#0200F之前麻烦您帮我们\x01",
            "挑选服装了，\x01",
            "十分感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED7")

    label("loc_3E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3ED7")

    #C0221
    ChrTalk(
        0xC,
        "啊，那个小朋友的衣服不就是刚才……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x104,
        (
            "#0300F对了，大小姐和阿缇\x01",
            "来这里给阿琪买过衣服啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED7")


    #C0223
    ChrTalk(
        0xC,
        (
            "原来如此，当时是给\x01",
            "这位小朋友买的洋装啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x153,
        "#1109F嘿嘿嘿，适合我吗？\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "呵呵，非常适合你，\x01",
            "也不枉我帮忙挑选呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3FB7")

    label("loc_3F59")


    #C0226
    ChrTalk(
        0xC,
        (
            "能让小朋友这么开心，\x01",
            "不枉我帮忙挑选呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "我们这里童装款式也有很多，\x01",
            "欢迎多来光顾啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB7")

    Jump("loc_45DF")

    label("loc_3FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4092")

    #C0228
    ChrTalk(
        0xC,
        (
            "米修拉姆疗养地那边\x01",
            "好像也开了一家高级\x01",
            "时装店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xC,
        (
            "不过，如果要比服装款式的齐全，我们一定不会输。\x01",
            "至于地段优势，那就更不用说啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xC,
        (
            "我想以一种更加贴近顾客的方式，\x01",
            "为市民提供各种时尚服装。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_4092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_40F8")

    #C0231
    ChrTalk(
        0xC,
        (
            "本店经常会承接\x01",
            "礼服方面的业务。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "在出席冠婚葬祭等活动时，\x01",
            "请一定来光顾本店哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_40F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4190")

    #C0233
    ChrTalk(
        0xC,
        "呼……终于要到关店休息的时间了。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xC,
        (
            "我在独立经营的时候，\x01",
            "经常无视时间，\x01",
            "一直干到深夜呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xC,
        "但现在不行了，或许我也上年纪了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_4190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4213")

    #C0236
    ChrTalk(
        0xC,
        (
            "我和汉森先生以前\x01",
            "是生意场上的竞争对手……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xC,
        (
            "自从他转行经营鞋店之后，\x01",
            "我们之间的那种竞争关系\x01",
            "好像就消失掉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_4213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_42BC")

    #C0238
    ChrTalk(
        0xC,
        (
            "有些人比较注重舒适性和耐久性，\x01",
            "而有些人则更加注重风格式样……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xC,
        (
            "对不同的客人而言，选择\x01",
            "与需求真是千差万别呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xC,
        (
            "请您慢慢考虑，\x01",
            "随意选购服装吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_42BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4332")

    #C0241
    ChrTalk(
        0xC,
        (
            "欢迎光临。\x01",
            "欢迎您光顾『卢卡』时装店。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xC,
        (
            "呵呵，本店今天的销售业绩也十分可观哦。\x01",
            "请您尽情选购吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_4332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_43EA")

    #C0243
    ChrTalk(
        0xC,
        (
            "我刚刚开店的时候，\x01",
            "为了收购各品牌的产品，\x01",
            "经常在国外奔波呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xC,
        (
            "现在已经有了稳定的进货渠道，\x01",
            "所以只要下个订单就万事解决了。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        (
            "偶尔也会怀念起\x01",
            "那个时候的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_43EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_449B")

    #C0246
    ChrTalk(
        0xC,
        (
            "在克洛斯贝尔，像本店\x01",
            "这种时装店是有很多的。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "但本店连一些不太\x01",
            "有名的小品牌也都会网罗。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "其它店里有的，我们绝对不会没有，\x01",
            "请各位尽情享受购物的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_449B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_44FD")

    #C0249
    ChrTalk(
        0xC,
        (
            "在克洛斯贝尔，汇集了\x01",
            "全世界的各类名牌服装。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xC,
        (
            "请各位尽情享受\x01",
            "购物的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DF")

    label("loc_44FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_45DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4583")

    #C0251
    ChrTalk(
        0xC,
        "欢迎光临『卢卡』时装店。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        (
            "从童装到男装，\x01",
            "各种名牌服装一应俱全哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        "若有什么需要，请尽管吩咐。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45DF")

    label("loc_4583")


    #C0254
    ChrTalk(
        0xC,
        (
            "从童装到男装，\x01",
            "各种名牌服装一应俱全哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        (
            "请您在『卢卡』时装店\x01",
            "尽情享受购物的快乐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45DF")

    Jump("loc_3A64")

    label("loc_45E4")

    TalkEnd(0xC)
    Return()

    # Function_13_3A1B end

    def Function_14_45E8(): pass

    label("Function_14_45E8")

    Call(0, 15)
    Return()

    # Function_14_45E8 end

    def Function_15_45EC(): pass

    label("Function_15_45EC")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_45FD")
    Jump("loc_462B")

    label("loc_45FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_462B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4617")
    Jump("loc_462B")

    label("loc_4617")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_462B")
    Call(0, 33)
    TalkEnd(0xD)
    Return()

    label("loc_462B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4635")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_558E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4685")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4685")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_46A4")
    OP_AF(0x25)
    Jump("loc_46A6")

    label("loc_46A4")

    OP_AF(0x24)

    label("loc_46A6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5589")

    label("loc_46B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46C9")
    Jump("loc_5589")

    label("loc_46C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5589")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4787")

    #C0256
    ChrTalk(
        0xD,
        (
            "说起来……\x01",
            "刚才接到了联络，据说委托加工\x01",
            "的七耀石已经加工完毕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xD,
        (
            "接下来，只要等着他们\x01",
            "从帝国给送来就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xD,
        "呵呵，不过真是有些等不及呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5589")

    label("loc_4787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4867")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_481B")

    #C0259
    ChrTalk(
        0xD,
        (
            "……冈兹？\x01",
            "啊，就是那个很有派头的矿工吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xD,
        (
            "最近他可是这里的常客呢，\x01",
            "不过这两天却一直都没露面，\x01",
            "我还有点担心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4862")

    label("loc_481B")


    #C0261
    ChrTalk(
        0xD,
        (
            "冈兹先生吗？就是那个\x01",
            "很有派头的矿工吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xD,
        "他发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_4862")

    Jump("loc_5589")

    label("loc_4867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4910")

    #C0263
    ChrTalk(
        0xD,
        (
            "从昨天开始，那个叫冈兹的矿工\x01",
            "就再也没来过了。\x01",
            "他最近一直是这里的常客呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xD,
        (
            "哈，不过他的米拉好像都是在『巴鲁卡』赚来的，\x01",
            "大概是好运已经到头了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5589")

    label("loc_4910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_49E0")

    #C0265
    ChrTalk(
        0xD,
        (
            "从前一段时间开始，有个派头十足\x01",
            "的客人经常来这里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xD,
        (
            "每次身边都带着女伴，\x01",
            "饰品总是一次就买五六件，\x01",
            "然后当礼物送出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xD,
        (
            "据说他是在『巴鲁卡』赚到了米拉……\x01",
            "老实说，还真是让人羡慕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5589")

    label("loc_49E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CFF")

    #C0268
    ChrTalk(
        0xD,
        (
            "有位名叫托马的旅行者，\x01",
            "在纪念庆典期间去了米修拉姆……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xD,
        (
            "他打算在纪念庆典时求婚，\x01",
            "所以在我这里购买了结婚戒指。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B83")

    #C0270
    ChrTalk(
        0xD,
        (
            "托马先生在回国之前\x01",
            "还专程来这里找过我呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xD,
        (
            "凭借在本店购买的订婚戒指，\x01",
            "他顺利求婚成功了，十分开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xD,
        (
            "哎呀，真是可喜可贺呢。\x01",
            "我当时花了整整一晚上的时间，在戒指上刻名字，\x01",
            "总算是没有白费力气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#0004F（求婚成功了吗……\x01",
            "  我们的努力也有了价值呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CF7")

    label("loc_4B83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4CC4")

    #C0274
    ChrTalk(
        0xD,
        (
            "托马先生在回国之前\x01",
            "还专程来这里找过我呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xD,
        (
            "他虽然不小心将\x01",
            "在本店购买的订婚戒指弄丢了，\x01",
            "但总算求婚成功了，十分开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "……哎呀，虽然该说是可喜可贺吧……\x01",
            "但我当时花了整整一晚上的时间，在戒指上刻名字，\x01",
            "结果却变成了白费力气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        (
            "#0004F（求婚成功了吗……\x01",
            "  要是当时能帮他找到戒指就好了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CF7")

    label("loc_4CC4")


    #C0278
    ChrTalk(
        0xD,
        (
            "话说，他那个生死攸关的\x01",
            "大挑战结果如何了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CF7")

    SetScenarioFlags(0x0, 5)
    Jump("loc_4D5E")

    label("loc_4CFF")


    #C0279
    ChrTalk(
        0xD,
        (
            "不过，所谓求婚，无论是以\x01",
            "何种形式进行，终究是值得祝福的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xD,
        "让我回想起了年轻时代呢。\x02",
    )

    CloseMessageWindow()

    label("loc_4D5E")

    Jump("loc_5589")

    label("loc_4D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE9")

    #C0281
    ChrTalk(
        0xD,
        (
            "面向纪念庆典时期的新商品\x01",
            "总算是已经进完货了。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xD,
        (
            "……希望那些令人\x01",
            "讨厌的假货商人\x01",
            "今年可别再来了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4E49")

    label("loc_4DE9")


    #C0283
    ChrTalk(
        0xD,
        (
            "一到纪念庆典期间，\x01",
            "卖假货的黑心商人\x01",
            "就会出现在克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xD,
        "请各位客人也要多加小心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4E49")

    Jump("loc_5589")

    label("loc_4E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4EE4")

    #C0285
    ChrTalk(
        0xD,
        (
            "差不多也该开始订购\x01",
            "面向纪念庆典期间的\x01",
            "新商品了。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "不过，装饰品、宝石这类东西\x01",
            "都是比较常见的走私货品，\x01",
            "所以进口的手续很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5589")

    label("loc_4EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4F57")

    #C0287
    ChrTalk(
        0xD,
        (
            "说起来的话，\x01",
            "我好像还没看新一期的\x01",
            "克洛斯贝尔时代周刊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xD,
        (
            "稍后去沙扎克那里，\x01",
            "顺便买一本吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5589")

    label("loc_4F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4FFB")

    #C0289
    ChrTalk(
        0xD,
        (
            "……噢，失礼了。\x01",
            "克洛斯贝尔通讯社\x01",
            "的经济杂志我已经看过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xD,
        (
            "上面也刊登了七耀石在\x01",
            "今日的最新交易价格呢。\x01",
            "哈，不自觉地关注这些也算是职业病吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5589")

    label("loc_4FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50C3")

    #C0291
    ChrTalk(
        0xD,
        (
            "刚才有位商人到这里来，\x01",
            "想要我收购一些美术品。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xD,
        (
            "……不过我看那些并不是什么上乘货，\x01",
            "于是就婉言谢绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "唔，总觉得那些一心以盈利为目标的\x01",
            "商人都很缺乏鉴赏眼光呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_513E")

    label("loc_50C3")


    #C0294
    ChrTalk(
        0xD,
        (
            "最近的商人，只懂追求眼前的利益，\x01",
            "却疏于锻炼那双鉴别商品质量\x01",
            "的慧眼。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xD,
        (
            "希望他们都能好好\x01",
            "磨练一下自己的鉴赏眼光啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_513E")

    Jump("loc_5589")

    label("loc_5143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_51C6")

    #C0296
    ChrTalk(
        0xD,
        (
            "在矿山镇玛因兹开采到的\x01",
            "七耀石是很美丽的宝石。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xD,
        (
            "特别是那些具有相当价值\x01",
            "的稀有结晶，最近能卖到\x01",
            "很高的价钱呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5589")

    label("loc_51C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5309")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52AE")

    #C0298
    ChrTalk(
        0xD,
        (
            "最近这段时间，黑市方面\x01",
            "的问题实在是让人痛心。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xD,
        (
            "在某些收藏美术品的资产家事业失败后，\x01",
            "那些珍贵艺术宝藏就这么\x01",
            "流向了那种地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xD,
        (
            "有多少美丽的艺术品就这样\x01",
            "变得无法见光了啊……\x01",
            "真是令人扼腕叹息呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5304")

    label("loc_52AE")


    #C0301
    ChrTalk(
        0xD,
        (
            "黑市方面的问题\x01",
            "实在是让人痛心。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "克洛斯贝尔的警察\x01",
            "要是能采取什么措施就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5304")

    Jump("loc_5589")

    label("loc_5309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5439")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53CC")

    #C0303
    ChrTalk(
        0xD,
        (
            "只要一听到有关美术品的传闻，\x01",
            "我就会心痒难耐，\x01",
            "坐卧不安呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xD,
        (
            "前一阵子，我还去列曼自治州\x01",
            "去参观了青瓷壶呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xD,
        (
            "如果有机会的话，真希望\x01",
            "能让客人们也欣赏一下啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5434")

    label("loc_53CC")


    #C0306
    ChrTalk(
        0xD,
        (
            "我在列曼自治州见到的\x01",
            "青瓷壶可真是个好东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xD,
        (
            "如果有机会的话，真希望\x01",
            "能让客人们也欣赏一下啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5434")

    Jump("loc_5589")

    label("loc_5439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5522")

    #C0308
    ChrTalk(
        0xD,
        (
            "我原来在帝国从事\x01",
            "美术商人的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xD,
        (
            "但是，由于不满美术品全都被一小部分\x01",
            "富豪占有囤积的现状，\x01",
            "于是就改行开了间装饰品店。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xD,
        (
            "凭借装饰品这种大众形式，\x01",
            "可以让美术品得到更加广泛的传播。\x01",
            "我觉得这是十分有意义的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5589")

    label("loc_5522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5589")

    #C0311
    ChrTalk(
        0xD,
        (
            "本店主要经营各种饰品和\x01",
            "其它小物件。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xD,
        (
            "虽然价格稍微有些高，\x01",
            "但每一件都是优质的上乘品。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5589")

    Jump("loc_4635")

    label("loc_558E")

    TalkEnd(0xD)
    Return()

    # Function_15_45EC end

    def Function_16_5592(): pass

    label("Function_16_5592")

    Call(0, 17)
    Return()

    # Function_16_5592 end

    def Function_17_5596(): pass

    label("Function_17_5596")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_55A7")
    Jump("loc_55D5")

    label("loc_55A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_55D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_55C1")
    Jump("loc_55D5")

    label("loc_55C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_55D5")
    Call(0, 29)
    TalkEnd(0xE)
    Return()

    label("loc_55D5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6509")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_562F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_562F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_564E")
    OP_AF(0x1B)
    Jump("loc_56B0")

    label("loc_564E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_565E")
    OP_AF(0x1A)
    Jump("loc_56B0")

    label("loc_565E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_566E")
    OP_AF(0x19)
    Jump("loc_56B0")

    label("loc_566E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_567E")
    OP_AF(0x18)
    Jump("loc_56B0")

    label("loc_567E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_568E")
    OP_AF(0x17)
    Jump("loc_56B0")

    label("loc_568E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_569E")
    OP_AF(0x16)
    Jump("loc_56B0")

    label("loc_569E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_56AE")
    OP_AF(0x15)
    Jump("loc_56B0")

    label("loc_56AE")

    OP_AF(0x14)

    label("loc_56B0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6504")

    label("loc_56BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56D3")
    Jump("loc_6504")

    label("loc_56D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6504")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5780")

    #C0313
    ChrTalk(
        0xE,
        (
            "终于迎来了久违的休假啊，\x01",
            "我预定回共和国的老家看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xE,
        (
            "如果知道了我在克洛斯贝尔的生意蒸蒸日上，\x01",
            "原来的商业伙伴一定会不甘心吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6504")

    label("loc_5780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_57D3")

    #C0315
    ChrTalk(
        0xE,
        "哎？有人失踪吗？\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xE,
        (
            "嗯～真让人担心啊。\x01",
            "到底发生了什么事情呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6504")

    label("loc_57D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5874")

    #C0317
    ChrTalk(
        0xE,
        (
            "商品的陈列也是门艺术，\x01",
            "并不是随便放置就可以的。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xE,
        (
            "必须要经过周密的思考，尽量展现出\x01",
            "商品吸引人的一面，让顾客一看就想买。\x01",
            "否则就没有意义了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6504")

    label("loc_5874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_58EB")

    #C0319
    ChrTalk(
        0xE,
        "我们的产品种类也渐渐齐全了啊。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xE,
        (
            "要是能为客人们提供各种商品，\x01",
            "以方便他们的生活，那就最好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6504")

    label("loc_58EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_594A")

    #C0321
    ChrTalk(
        0xE,
        "纪念庆典期间的销售额大幅度增加了哦。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xE,
        (
            "呵呵……\x01",
            "真期待今年的分红奖金呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6504")

    label("loc_594A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_59EF")

    #C0323
    ChrTalk(
        0xE,
        (
            "为了应对纪念庆典，\x01",
            "我们也增加了进货量呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xE,
        (
            "面向游客的旅行指南，\x01",
            "每年都一定会热卖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xE,
        (
            "平时一向都很不起眼的杂货柜台，\x01",
            "也会变得十分忙碌哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6504")

    label("loc_59EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AB0")

    #C0326
    ChrTalk(
        0xE,
        (
            "珍妮特今天早上好像遇到了\x01",
            "一位体格相当健壮的\x01",
            "游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xE,
        "然后从早上开始就陷入那种状态了。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x11, 500)
    Sleep(300)

    #C0328
    ChrTalk(
        0xE,
        "那个，珍妮特，工作……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x0, 0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_5AFE")

    label("loc_5AB0")


    #C0329
    ChrTalk(
        0xE,
        (
            "哈，游击士\x01",
            "确实是可靠呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xE,
        (
            "……不过在上班时间过来闲聊，\x01",
            "可就有点……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AFE")

    Jump("loc_6504")

    label("loc_5B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5B51")

    #C0331
    ChrTalk(
        0xE,
        (
            "欢迎光临。\x01",
            "想看点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xE,
        (
            "这个月的新刊\x01",
            "已经到货了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6504")

    label("loc_5B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5BD2")

    #C0333
    ChrTalk(
        0xE,
        (
            "珍妮特她……不管是什么事情，\x01",
            "只要一转过头，马上就能忘得一干二净。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xE,
        "从某种意义上来说，这也算是一种才能啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6504")

    label("loc_5BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5CFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C89")

    #C0335
    ChrTalk(
        0xE,
        (
            "彩虹剧团的新剧\x01",
            "已经公布了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xE,
        "剧目是『金之太阳、银之月』……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xE,
        (
            "我们这里本来也卖门票，\x01",
            "但没想到当天就被抢购一空。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xE,
        "彩虹剧团确实很受欢迎啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5CF7")

    label("loc_5C89")


    #C0339
    ChrTalk(
        0xE,
        (
            "虽然有些对不起珍妮特，但也只能\x01",
            "让她忍耐一下，优先供应给客人啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xE,
        (
            "说实话，其实连我自己也\x01",
            "都很想要呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF7")

    Jump("loc_6504")

    label("loc_5CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E4C")

    #C0341
    ChrTalk(
        0xE,
        (
            "最近那些大企业里\x01",
            "好像开始设置一种\x01",
            "叫导力网络的东西了。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xE,
        (
            "经常会有客人来这里\x01",
            "问我有没有介绍相关知识的书籍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x103,
        (
            "#0200F导力网络是个还在\x01",
            "研究阶段的新技术，\x01",
            "目前存在的介绍也只有论文而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xE,
        "果、果然是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xE,
        (
            "呼，虽然对不起那些为此而烦恼的客人，\x01",
            "但再怎么说，我也没办法订购到\x01",
            "还没有出版的书啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5F31")

    label("loc_5E4C")


    #C0346
    ChrTalk(
        0xE,
        (
            "来这里找我商谈的人有\x01",
            "衣装得体的商务人士，也有\x01",
            "市政厅那里的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xE,
        (
            "他们都这么形容那东西呢——\x01",
            "『看似很方便，但完全不懂怎么用！』\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……即使是在我们支援科，\x01",
            "会使用它的也只有\x01",
            "缇欧一人而已呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x104,
        "#0300F是呀。\x02",
    )

    CloseMessageWindow()

    label("loc_5F31")

    Jump("loc_6504")

    label("loc_5F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6062")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_600C")

    #C0350
    ChrTalk(
        0xE,
        (
            "嗯～目前卖得最好的\x01",
            "果然还是书籍类商品啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xE,
        (
            "我这里虽说是个杂货柜台，\x01",
            "但比起药品和日用品，\x01",
            "来买书的人倒比较多。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xE,
        (
            "而且新刊的订单也不少……\x01",
            "看来要多增加一些\x01",
            "摆放书籍的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_605D")

    label("loc_600C")


    #C0353
    ChrTalk(
        0xE,
        (
            "这里虽说是个杂货店，\x01",
            "但却有很多人来买书。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xE,
        "有空时去和经理谈谈这件事吧。\x02",
    )

    CloseMessageWindow()

    label("loc_605D")

    Jump("loc_6504")

    label("loc_6062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_62F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62A4")
    TurnDirection(0xE, 0x104, 0)

    #C0355
    ChrTalk(
        0xE,
        (
            "哎呀，你不是最近常来买\x01",
            "写真杂志的那位客人嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xE,
        (
            "哈，你好像很喜欢这个啊。\x01",
            "每周都要来这里扫货，一次都不漏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x104,
        (
            "#0300F嘿嘿，那是当然啦。\x01",
            "那可是我的毕生追求。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x102)
    OP_64(0x103)

    #C0358
    ChrTalk(
        0x102,
        "#0111F写真杂志啊……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#0006F兰迪，在女性面前，\x01",
            "这是不是稍微有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x104,
        (
            "#0305F嗯……怎么了，罗伊德，\x01",
            "你也想看吗？\x02\x03",

            "#0300F哈哈～客气什么嘛，\x01",
            "到时肯定会借你啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0361
    ChrTalk(
        0x101,
        (
            "#0011F不不，不是那个意思啦！\x01",
            "请不要说一些容易\x01",
            "招人误解的话啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x103,
        "#0211F（瞪）……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xE,
        (
            "啊、啊哈哈……\x01",
            "我好像扯到了不太好的话题呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 6)
    Jump("loc_62EF")

    label("loc_62A4")


    #C0364
    ChrTalk(
        0xE,
        (
            "说起来，在我们店，\x01",
            "总是有人不小心丢东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xE,
        "各位也要注意一点哦。\x02",
    )

    CloseMessageWindow()

    label("loc_62EF")

    Jump("loc_6504")

    label("loc_62F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A2")

    #C0366
    ChrTalk(
        0xE,
        (
            "你们知道吗，几年前，\x01",
            "克洛斯贝尔时代周刊社的大楼就坐落在中央广场。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xE,
        (
            "这个百货店的名字——『时代』\x01",
            "就取自于中央广场那时\x01",
            "的旧称『时代广场』。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6424")

    label("loc_63A2")


    #C0368
    ChrTalk(
        0xE,
        (
            "这个百货店之所以会叫『时代』，\x01",
            "就是因为克洛斯贝尔时代周刊社的大楼\x01",
            "当时就坐落于这个中央广场。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xE,
        "哎呀～影响力确实是很大呢。\x02",
    )

    CloseMessageWindow()

    label("loc_6424")

    Jump("loc_6504")

    label("loc_6429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_649A")

    #C0370
    ChrTalk(
        0xE,
        (
            "欢迎光临，\x01",
            "这里是杂货柜台哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xE,
        (
            "本柜台也出售克洛斯贝尔时代周刊，\x01",
            "请随意选购。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6504")

    label("loc_649A")


    #C0372
    ChrTalk(
        0xE,
        (
            "要说起最畅销的商品，\x01",
            "果然还是克洛斯贝尔时代周刊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xE,
        (
            "因为克洛斯贝尔有\x01",
            "很多从事着商业活动的人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6504")

    Jump("loc_55DF")

    label("loc_6509")

    TalkEnd(0xE)
    Return()

    # Function_17_5596 end

    def Function_18_650D(): pass

    label("Function_18_650D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6627")

    #C0374
    ChrTalk(
        0x104,
        "#0300F啊，这不是科长吗。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#0000F那个，科长，关于工作……？\x02\x03",

            "就是敷衍高层和搜查一科那边\x01",
            "的事情，有什么好方法了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xF,
        (
            "#1000F嗯，不用担心，\x01",
            "我脑子里已经有了很完美的计划了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x102,
        "#0100F是、是真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x103,
        (
            "#0200F但看起来好像并没有\x01",
            "什么说服力呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_66B2")

    label("loc_6627")


    #C0379
    ChrTalk(
        0xF,
        (
            "#1003F调查工作的具体程序，由你们自行判断。\x01",
            "随自己高兴，怎样做都好。\x02\x03",

            "#1000F只是，稍后可要来报告啊，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        "#0000F是的，明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_66B2")

    TalkEnd(0xFE)
    Return()

    # Function_18_650D end

    def Function_19_66B6(): pass

    label("Function_19_66B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AF0")

    #C0381
    ChrTalk(
        0x10,
        (
            "欢迎光临。\x01",
            "欢迎光顾『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_673C")

    #C0382
    ChrTalk(
        0x10,
        (
            "哎呀……这不是\x01",
            "艾莉大小姐吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6779")

    label("loc_673C")

    TurnDirection(0x10, 0x102, 500)

    #C0383
    ChrTalk(
        0x10,
        "哎呀，那位客人不是……\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x10,
        "果然是艾莉大小姐啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6779")


    #C0385
    ChrTalk(
        0x10,
        (
            "对于您今日的光顾，\x01",
            "表示诚挚感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67C0")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_67C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67E0")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_67E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6800")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6800")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6820")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6820")

    Sleep(1000)

    #C0386
    ChrTalk(
        0x101,
        "#0005F艾、艾莉大小姐……？\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#0100F啊、啊哈哈哈哈……\x02\x03",

            "那个，我的外公和\x01",
            "经理是老朋友哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x10,
        (
            "艾莉大小姐从童年\x01",
            "时期开始，就是本店的\x01",
            "重要常客啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x103,
        (
            "#0200F在这么气派的百货店中\x01",
            "拥有ＶＩＰ身份吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x104,
        (
            "#0305F哈哈～果然是名副其实的\x01",
            "『大小姐』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x102,
        "#0112F真是的，大家怎么都……\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x10,
        "……对了，大小姐。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x10,
        (
            "您留学回来之后，就改变了想法，\x01",
            "申请去警察局就职这件事，\x01",
            "我也有所耳闻了。那个……？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x102,
        (
            "#0100F嗯，是的，我现在就是一名警官哦。\x02\x03",

            "#0108F所以……如果可以的话，\x01",
            "在店内就不要对我进行特殊照顾了。\x02\x03",

            "#0106F不好意思啊，\x01",
            "总是说一些任性的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x10,
        (
            "噢，是我考虑不周了。\x01",
            "那么就照您的意愿……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x10,
        (
            "不过，您仍然是本店重要的客人，\x01",
            "这一点是不会变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x10,
        (
            "如果以后遇到什么困难，\x01",
            "不管是什么事，都请随时来找我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 2)
    TalkEnd(0xFE)
    Return()

    label("loc_6AF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B69")

    #C0398
    ChrTalk(
        0x101,
        (
            "#0000F（百货店……\x01",
            "  这里是遗失了物品的特伦特先生\x01",
            "  途中经过的地方呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)

    label("loc_6B69")


    #C0399
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，请问您在这附近\x01",
            "捡到过什么失物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "要询问遗失物品\x01",
            "方面的事项吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "那样的话，请您去中央大厅的\x01",
            "综合服务柜台进行询问吧。\x01",
            "马上就能查询到的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_6C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_6C7B")

    #C0402
    ChrTalk(
        0xFE,
        (
            "看来遗失物品已经\x01",
            "找到了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        "真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "欢迎再度光临\x01",
            "『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_6C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6D62")

    #C0405
    ChrTalk(
        0xFE,
        (
            "最近的销售情况很稳定，\x01",
            "感觉一切都安定下来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "……不过，只要百货店还在经营，\x01",
            "我们就要一直揣摩顾客的心情，\x01",
            "不断推出更多吸引人的企划活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "现在正在研究中的活动\x01",
            "可是我非常有自信的一次策划，\x01",
            "敬请期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8C")

    label("loc_6D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6E1F")

    #C0408
    ChrTalk(
        0xFE,
        (
            "将顾客的满足与安心摆在第一位，\x01",
            "这就是『时代』百货店的经营理念。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "职员们都经过专门的培训，吸取了我的\x01",
            "经验，接受了很彻底的教育。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "总之，请您心情愉快地\x01",
            "享受购物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8C")

    label("loc_6E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6EB5")

    #C0411
    ChrTalk(
        0xFE,
        (
            "今天早上起床以后，因为一件偶然的事情，\x01",
            "让我又构想出了一个新的企划方案。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "哎呀呀，企划的灵感，\x01",
            "还真是来源于生活中每一个细节呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8C")

    label("loc_6EB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_71B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F55")

    #C0413
    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "欢迎光顾『时代』百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "如果想选购什么商品，\x01",
            "就尽管去询问店员吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "我们一定会耐心诚恳地\x01",
            "为您服务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71AE")

    label("loc_6F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70F9")

    #C0416
    ChrTalk(
        0xFE,
        (
            "前段时间，麦克道尔市长\x01",
            "还向我们发表了慰问致辞。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "作为一家长期扎根在本地的老店，\x01",
            "今后也要继续努力为身边的市民们服务。\x01",
            "市长先生是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x102,
        (
            "#0100F虽然是大企业的经营者，但毫无架子，\x01",
            "永远都站在客人的角度上考虑问题。\x01",
            "奈斯顿经理就是这样的人呢。\x02\x03",

            "我的想法也和外公一样，\x01",
            "今后也请您继续加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "您实在是过誉了，\x01",
            "艾莉大小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "我们一定会不负您的期待，\x01",
            "使这里成为一家让市民满意的百货店。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_71AE")

    label("loc_70F9")


    #C0421
    ChrTalk(
        0xFE,
        (
            "我和麦克道尔市长\x01",
            "从以前开始就是亲密的好友……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "但听到如此郑重的言语，\x01",
            "仍然是惶恐不已啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "今后一定继续努力，使这里成为一家让市民们\x01",
            "满意的百货店，绝不会辜负各位的期待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71AE")

    Jump("loc_7C8C")

    label("loc_71B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7344")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72C8")

    #C0424
    ChrTalk(
        0xFE,
        (
            "我进入这个行业\x01",
            "也有很长时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "每天都在思考新的企划活动，\x01",
            "希望能让这间百货店更加繁荣……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "年轻时的那点微末经验，\x01",
            "至今仍然都能在很多\x01",
            "计划中发挥作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "当年那个莽撞冲动，可以为了\x01",
            "目标而不顾一切的年轻时代，\x01",
            "对我来说可是珍贵的宝物呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_733F")

    label("loc_72C8")


    #C0428
    ChrTalk(
        0xFE,
        (
            "年轻时的那点微末经验，\x01",
            "至今仍然都能在很多\x01",
            "计划中发挥作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "年轻时代积累了那么多的经验，\x01",
            "我觉得真是很幸运啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_733F")

    Jump("loc_7C8C")

    label("loc_7344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74AC")

    #C0430
    ChrTalk(
        0xFE,
        (
            "米修拉姆那历史悠久的吉祥物\x01",
            "『咪西』，你们听说过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "当年，在还是疗养地的米修拉姆，\x01",
            "那只是个用来贩卖的普通玩偶形象……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "但在两年前与主题公园合并之后，\x01",
            "它就一跃而起，博得了巨大的人气。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "本店也正在考虑\x01",
            "和它进行协作，联合举办\x01",
            "一些企划活动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x103,
        "#0205F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#0000F（缇欧双眼放光了呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7512")

    label("loc_74AC")


    #C0436
    ChrTalk(
        0xFE,
        (
            "我们百货店正准备同『咪西』联手，\x01",
            "共同举办一些企划活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "如果顺利实行，\x01",
            "请一定要来捧场啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7512")

    Jump("loc_7C8C")

    label("loc_7517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_75D2")

    #C0438
    ChrTalk(
        0xFE,
        (
            "百货店的新企划活动\x01",
            "正在逐步推进。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "接下来的工作就只剩下\x01",
            "和赞助商联络，让他们批准下来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "各位顾客，今后也请继续关注本百货店\x01",
            "的动向，不要错过任何精彩活动哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8C")

    label("loc_75D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7631")

    #C0441
    ChrTalk(
        0xFE,
        "本店一直经营到晚上八点。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "请放松心情，慢慢选购，\x01",
            "尽情享受购物的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8C")

    label("loc_7631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_76E9")

    #C0443
    ChrTalk(
        0xFE,
        (
            "我们百货店里的这些加盟店铺，\x01",
            "都是我从克洛斯贝尔各地与周边诸国\x01",
            "寻找到的优良店铺。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "长久以来，每当我看到前来\x01",
            "购物的客人们那满足的笑容，\x01",
            "就会觉得自己的眼光没有错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8C")

    label("loc_76E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7774")

    #C0445
    ChrTalk(
        0xFE,
        "欢迎光临『时代』百货店。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "如果有什么需要，\x01",
            "请吩咐正门服务柜台\x01",
            "的接待人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "请您放松心情，\x01",
            "尽情享受购物的乐趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8C")

    label("loc_7774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_77BF")

    #C0448
    ChrTalk(
        0xFE,
        "……欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "请您放松心情，\x01",
            "尽情享受购物的乐趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C8C")

    label("loc_77BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_78A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_785B")

    #C0450
    ChrTalk(
        0xFE,
        (
            "嗯，新装开店展销会\x01",
            "也已经开放一段时间了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "客人们也差不多快要\x01",
            "产生厌倦情绪了……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "要是能有什么\x01",
            "新的好企划就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_78A3")

    label("loc_785B")


    #C0453
    ChrTalk(
        0xFE,
        (
            "新装开店展销会\x01",
            "也已经开放了一段时间了呢。\x01",
            "还有什么其它的好方案吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78A3")

    Jump("loc_7C8C")

    label("loc_78A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79D8")

    #C0454
    ChrTalk(
        0x102,
        (
            "#0100F奈斯顿先生，\x01",
            "早上好。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xFE,
        "各位，早上好。\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xFE,
        (
            "啊……似乎是要\x01",
            "出发去什么地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        (
            "#0100F嗯……\x01",
            "您看出来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xFE,
        "哈哈，因为常年和顾客打交道嘛。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "各位，如果到达目的地后发现没带够东西，\x01",
            "肯定会非常焦急的。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        (
            "请注意提前准备好所需要的物品，\x01",
            "不要有什么遗漏。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 7)
    Jump("loc_7A38")

    label("loc_79D8")


    #C0461
    ChrTalk(
        0xFE,
        (
            "各位，请注意提前准备好所需要的物品，\x01",
            "不要有什么遗漏。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "还有，请一路小心，\x01",
            "注意安全啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A38")

    Jump("loc_7C8C")

    label("loc_7A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AF4")

    #C0463
    ChrTalk(
        0xFE,
        (
            "我想你们应该知道，本百货店\x01",
            "在去年经过一次全面改造。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xFE,
        (
            "这几年来，街道的格局\x01",
            "也有了翻天覆地的变化，\x01",
            "所以我们也要顺应潮流。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "欢迎您今后\x01",
            "多来光顾。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7B4E")

    label("loc_7AF4")


    #C0466
    ChrTalk(
        0xFE,
        (
            "为了顺应街道格局的变化，\x01",
            "本百货店也进行了全面的改造装修。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "欢迎您今后\x01",
            "多来光顾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B4E")

    Jump("loc_7C8C")

    label("loc_7B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7C8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C0B")

    #C0468
    ChrTalk(
        0xFE,
        (
            "本百货店内\x01",
            "包括各种各样的卖场。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xFE,
        (
            "无论哪一家店铺的商品，都可谓品质优秀、\x01",
            "品种齐全，绝对能让您满意……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        (
            "各位，请放松心情，\x01",
            "尽情享受购物的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7C8C")

    label("loc_7C0B")


    #C0471
    ChrTalk(
        0xFE,
        (
            "本百货店内的卖场店铺，\x01",
            "全都是品质优秀，品种齐全\x01",
            "的一流店铺，我们也引以为荣。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xFE,
        (
            "各位，请放松心情，\x01",
            "尽情享受购物的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C8C")

    TalkEnd(0xFE)
    Return()

    # Function_19_66B6 end

    def Function_20_7C90(): pass

    label("Function_20_7C90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7D0B")

    #C0473
    ChrTalk(
        0xFE,
        (
            "最近一到傍晚，就算还没下班，\x01",
            "我也会忍不住跑到这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xFE,
        (
            "唔～好香的味道……\x01",
            "肚子又开始饿了啊～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8814")

    label("loc_7D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7DFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DAA")
    OP_93(0xFE, 0x0, 0x0)

    #C0475
    ChrTalk(
        0xFE,
        "扫除，扫除……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0476
    ChrTalk(
        0xFE,
        (
            "呼，因为昨天睡过了头，\x01",
            "所以被惩罚做大扫除。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xFE,
        (
            "接下来还要去打扫仓库呢，\x01",
            "呼，真是受不了啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7DF6")

    label("loc_7DAA")


    #C0478
    ChrTalk(
        0xFE,
        (
            "那明明只是因为\x01",
            "闹钟刚好停了而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xFE,
        (
            "呼，有没有人愿意\x01",
            "替我来干啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DF6")

    Jump("loc_8814")

    label("loc_7DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E83")

    #C0480
    ChrTalk(
        0xFE,
        (
            "哈～欠，今天\x01",
            "睡过头了啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        (
            "啊，不过，这可并不是\x01",
            "我的错哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xFE,
        (
            "因为闹钟不知道什么时候\x01",
            "就自己停了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7EA2")

    label("loc_7E83")


    #C0483
    ChrTalk(
        0xFE,
        (
            "哈～欠，\x01",
            "好像还是想睡呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EA2")

    Jump("loc_8814")

    label("loc_7EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7FCD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F12")

    #C0484
    ChrTalk(
        0xFE,
        (
            "请各位随意\x01",
            "挑选商品吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xFE,
        (
            "本店非常欢迎这种自由\x01",
            "选购的形式呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FC8")

    label("loc_7F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F9D")

    #C0486
    ChrTalk(
        0xFE,
        "好了好了……快点工作！\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xFE,
        (
            "我最近可是\x01",
            "非常努力的哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xFE,
        (
            "这也是为了追上辛茜亚前辈\x01",
            "和帕尔前辈。\x01",
            "ＦＩＧＨＴ，噢～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7FC8")

    label("loc_7F9D")


    #C0489
    ChrTalk(
        0xFE,
        (
            "ＦＩＧＨＴ，噢～！\x01",
            "我今天也很努力哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC8")

    Jump("loc_8814")

    label("loc_7FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8041")

    #C0490
    ChrTalk(
        0xFE,
        (
            "纪念庆典结束之后，\x01",
            "也就可以闲下来了吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xFE,
        (
            "我非常喜欢\x01",
            "轻松的时光哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        "悠闲度日最舒服了呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_8814")

    label("loc_8041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_80A7")

    #C0493
    ChrTalk(
        0xFE,
        (
            "随着纪念庆典的临近，\x01",
            "我也越来越兴奋了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "呵呵，真期待啊～\x01",
            "今年要玩些什么呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8814")

    label("loc_80A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8143")

    #C0495
    ChrTalk(
        0xFE,
        (
            "游击士真是\x01",
            "很帅啊～……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xFE,
        (
            "之前还有游击士来\x01",
            "百货店领走迷路的\x01",
            "小孩呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xFE,
        (
            "那个，能不能\x01",
            "把我也领走呢？\x01",
            "……开、开玩笑啦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_817D")

    label("loc_8143")


    #C0498
    ChrTalk(
        0xFE,
        (
            "游击士真是\x01",
            "很帅啊～……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        (
            "我下次也\x01",
            "装作迷路好了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_817D")

    Jump("loc_8814")

    label("loc_8182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_81C1")

    #C0500
    ChrTalk(
        0xFE,
        "呼，肚子饿了～\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xFE,
        (
            "今天想早点回家\x01",
            "吃饭呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8814")

    label("loc_81C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_823F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8211")
    OP_93(0xFE, 0x5A, 0x0)

    #C0502
    ChrTalk(
        0xFE,
        "啊，这身洋装真不错～\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        "我也很想要啊～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_823A")

    label("loc_8211")


    #C0504
    ChrTalk(
        0xFE,
        (
            "这是今年的新款式啊～\x01",
            "我也很想要呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_823A")

    Jump("loc_8814")

    label("loc_823F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_84B4")
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_842B")

    #C0505
    ChrTalk(
        0xFE,
        "呜～请听我说啊～！\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "我明明拜托过沙扎克先生，\x01",
            "让他帮我留下一张彩虹剧团\x01",
            "的门票……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xFE,
        "但他却和我说，已经全部卖光了！\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xFE,
        (
            "呜呜，本来以为，在百货店\x01",
            "工作的话，肯定能弄到手呢～……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xE,
        (
            "哈哈……不好意思，\x01",
            "卖票也是有规矩的。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xE,
        (
            "我连自己的票\x01",
            "也都没有买呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xE,
        (
            "珍妮特，打起精神来吧。\x01",
            "下次有机会的话，我会好好补偿你的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xE, 500)
    Sleep(300)

    #C0512
    ChrTalk(
        0xFE,
        (
            "……真的吗？\x01",
            "那，下次请和我约会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0513
    ChrTalk(
        0xE,
        (
            "这、这倒是没什么问题……\x01",
            "但那样就足够补偿你了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_84AB")

    label("loc_842B")

    OP_93(0xFE, 0x2D, 0x0)

    #C0514
    ChrTalk(
        0xFE,
        (
            "呜，我明明那么想要\x01",
            "门票的，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "沙扎克先生是大笨蛋～！\x01",
            "请和我约会啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xE,
        (
            "珍妮特好像已经\x01",
            "自暴自弃了啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84AB")

    OP_4C(0xE, 0xFF)
    Jump("loc_8814")

    label("loc_84B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8598")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_856A")

    #C0517
    ChrTalk(
        0xFE,
        (
            "辛茜亚前辈和帕尔前辈\x01",
            "永远都是那么默契啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xFE,
        (
            "即使互相之间什么都不说，\x01",
            "好像也可以明白对方在想什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "呼，因为她们两个人\x01",
            "都是经验丰富的老手吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8593")

    label("loc_856A")


    #C0520
    ChrTalk(
        0xFE,
        (
            "我也想尽快变得\x01",
            "和她们两个人一样呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8593")

    Jump("loc_8814")

    label("loc_8598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_864E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8618")

    #C0521
    ChrTalk(
        0xFE,
        (
            "这个柜台的负责人\x01",
            "总是在休息时间\x01",
            "擦拭盘子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "而且还一边笑一边擦。\x01",
            "……不觉得他是个怪人吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8649")

    label("loc_8618")


    #C0523
    ChrTalk(
        0xFE,
        (
            "这个柜台的负责人\x01",
            "是个稍微有些怪异的家伙呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8649")

    Jump("loc_8814")

    label("loc_864E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_86FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86DB")

    #C0524
    ChrTalk(
        0xFE,
        (
            "之前，我还接待过\x01",
            "游击士客人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "那是一对年轻的男孩和女孩，\x01",
            "看起来好像是情侣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        "呼，真羡慕啊～……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_86F5")

    label("loc_86DB")


    #C0527
    ChrTalk(
        0xFE,
        "我也想找个男朋友呢～\x02",
    )

    CloseMessageWindow()

    label("loc_86F5")

    Jump("loc_8814")

    label("loc_86FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8764")

    #C0528
    ChrTalk(
        0xFE,
        (
            "辛茜亚前辈那么漂亮，\x01",
            "帕尔前辈也是个美人……\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        (
            "呼，我也想早点变成\x01",
            "像她们一样的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8814")

    label("loc_8764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87DD")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x104, 500)

    #C0530
    ChrTalk(
        0xFE,
        "啊，好帅的人……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0531
    ChrTalk(
        0xFE,
        (
            "啊，不不，没什么。\x01",
            "请随意选购～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8814")

    label("loc_87DD")


    #C0532
    ChrTalk(
        0xFE,
        (
            "我、我在这里\x01",
            "帮忙卖东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        "请、请随意挑选～\x02",
    )

    CloseMessageWindow()

    label("loc_8814")

    TalkEnd(0xFE)
    Return()

    # Function_20_7C90 end

    def Function_21_8818(): pass

    label("Function_21_8818")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8885")

    #C0534
    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xFE,
        (
            "……噢噢～危险啊！\x01",
            "打开自己要买的书后，\x01",
            "不知不觉都快站着看完了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_926D")

    label("loc_8885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_899C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892D")

    #C0536
    ChrTalk(
        0xFE,
        "噢，找到了……\x02",
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xFE,
        (
            "虽然这本参考书很贵，\x01",
            "但我拜托父母后，他们给了我钱。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xFE,
        (
            "因为是重考生，\x01",
            "所以总觉得很自卑，\x01",
            "但父母一直都在给我打气。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8997")

    label("loc_892D")


    #C0539
    ChrTalk(
        0xFE,
        (
            "好～仔细阅读这本参考书，\x01",
            "然后，如果能成为一名优秀的医生……\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xFE,
        (
            "首先要把书钱还给\x01",
            "父母才行啊，哈哈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8997")

    Jump("loc_926D")

    label("loc_899C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8A41")

    #C0541
    ChrTalk(
        0xFE,
        (
            "今天也是遵从父母的吩咐，\x01",
            "来给家里买东西的……\x01",
            "但我还是最喜欢杂货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "昨天发现的那本参考书，\x01",
            "实在是很想要……\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xFE,
        "不然就试试去拜托父母吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_926D")

    label("loc_8A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8B68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AAD")

    #C0544
    ChrTalk(
        0xFE,
        (
            "我总是遵从父母的吩咐，\x01",
            "来这里买东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xFE,
        "身为重考生，真是自卑啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B63")

    label("loc_8AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B08")

    #C0546
    ChrTalk(
        0xFE,
        "噢，新参考书出版了啊。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xFE,
        (
            "我看看……\x01",
            "噢噢！这本参考书相当不错啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8B63")

    label("loc_8B08")


    #C0548
    ChrTalk(
        0xFE,
        "……呜～真想要这本参考书啊……\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        (
            "但是，对我这个重考生来说，\x01",
            "价钱实在是太贵了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B63")

    Jump("loc_926D")

    label("loc_8B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C4E")

    #C0550
    ChrTalk(
        0xFE,
        "那么～今天要买的是……\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x153,
        (
            "#1110F大哥哥～在帮家里买东西？\x01",
            "好了不起哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xFE,
        (
            "……因为哥哥我是个重考生啊。\x01",
            "如果连这点用处都没有，我就更加自卑了～\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        (
            "……虽然是自己说的，\x01",
            "但真是越说越觉得难受啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8C8F")

    label("loc_8C4E")


    #C0554
    ChrTalk(
        0xFE,
        (
            "因为我是个重考生，如果连这点\x01",
            "用处都没有，就会更加自卑了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C8F")

    Jump("loc_926D")

    label("loc_8C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8CCD")

    #C0555
    ChrTalk(
        0xFE,
        (
            "嗯～今天好像没有\x01",
            "发现什么新参考书啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_926D")

    label("loc_8CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8DC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D59")

    #C0556
    ChrTalk(
        0xFE,
        (
            "我希望成为一名医生，\x01",
            "曾经多次去参加乌尔斯拉\x01",
            "医科大学的考试。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xFE,
        (
            "……但题目相当难，\x01",
            "所以至今都没有被录取。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8DC0")

    label("loc_8D59")


    #C0558
    ChrTalk(
        0xFE,
        "呼，当重考生可是很痛苦的啊。\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        (
            "在家人面前都抬不起头，\x01",
            "而且还会像这样，被人随意当成跑腿的使唤。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DC0")

    Jump("loc_926D")

    label("loc_8DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E56")

    #C0560
    ChrTalk(
        0xFE,
        (
            "希伦姐姐在乌尔斯拉医院\x01",
            "当护士，\x01",
            "可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xFE,
        (
            "为什么那种冒失的家伙\x01",
            "能在那么好的医院里任职呢，\x01",
            "这至今都是个疑问。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8EBE")

    label("loc_8E56")


    #C0562
    ChrTalk(
        0xFE,
        (
            "……算啦，反正希伦姐姐一直\x01",
            "都是傻人有傻福的……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        (
            "……喔，与其想那种事，\x01",
            "还是赶快把东西买了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EBE")

    Jump("loc_926D")

    label("loc_8EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8F72")

    #C0564
    ChrTalk(
        0xFE,
        (
            "我的父母啊，\x01",
            "把买东西的事情全都丢给孩子，\x01",
            "却连一米拉的跑腿费都不给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xFE,
        (
            "每次都给我分文不差\x01",
            "的钱，连一点找零的\x01",
            "钱都不会剩下……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        (
            "还真是很会\x01",
            "计算呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_926D")

    label("loc_8F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8F9D")

    #C0567
    ChrTalk(
        0xFE,
        (
            "噢，新刊到了。\x01",
            "我看看～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_926D")

    label("loc_8F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_90A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_903A")

    #C0568
    ChrTalk(
        0xFE,
        (
            "我的姐姐在乌尔斯拉\x01",
            "医院里当护士呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "她的名字叫希伦，\x01",
            "你们见过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        (
            "在家人的命令之下，\x01",
            "我要去看望她。\x01",
            "……真是麻烦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_909D")

    label("loc_903A")


    #C0571
    ChrTalk(
        0xFE,
        (
            "我的姐姐在乌尔斯拉\x01",
            "医院工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "希伦姐姐一直\x01",
            "都是个冒失鬼……\x01",
            "总是让全家人都来为她担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_909D")

    Jump("loc_926D")

    label("loc_90A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_911C")

    #C0573
    ChrTalk(
        0xFE,
        "我又被派来买东西了啊～\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "其实我只是想来找找在报告作业\x01",
            "中要用到的资料书而已……\x01",
            "我家父母真会使唤人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_926D")

    label("loc_911C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9192")

    #C0575
    ChrTalk(
        0xFE,
        (
            "百货店里的东西应有尽有，\x01",
            "所以客人们纷纷前来光顾啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xFE,
        (
            "自从去年新装修之后，\x01",
            "来客也越来越多了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_926D")

    label("loc_9192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_926D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_922A")

    #C0577
    ChrTalk(
        0xFE,
        (
            "砂糖、小麦粉\x01",
            "和洋葱酱……\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "这家店里的东西\x01",
            "还真是品种齐全啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xFE,
        (
            "就算单看砂糖，也有产地\x01",
            "各不相同的三十六种之多啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_926D")

    label("loc_922A")


    #C0580
    ChrTalk(
        0xFE,
        (
            "不过，如果不是专业厨师……\x01",
            "恐怕会眼花缭乱，不知该买哪种了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_926D")

    TalkEnd(0xFE)
    Return()

    # Function_21_8818 end

    def Function_22_9271(): pass

    label("Function_22_9271")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_92C9")

    #C0581
    ChrTalk(
        0xFE,
        "啊呀，都已经到傍晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "还没想好晚上要吃什么，\x01",
            "该怎么办呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_92C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_931A")

    #C0583
    ChrTalk(
        0xFE,
        (
            "今天我也是从刚开店时就一直在逛了，\x01",
            "早晨来购物就是清爽愉快啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_931A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_936B")

    #C0584
    ChrTalk(
        0xFE,
        "喔呵呵，我最爱购物了～！\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "今天就尽情买些\x01",
            "喜欢的东西吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_936B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9446")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_93EA")

    #C0586
    ChrTalk(
        0xFE,
        (
            "在百货店里，就算只是随便逛逛\x01",
            "也都很开心呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        (
            "几个小时的时间\x01",
            "不知不觉就这么过去了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9441")

    label("loc_93EA")


    #C0588
    ChrTalk(
        0xFE,
        "喔呵呵，明天就是我老公的发薪日啦。\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        (
            "趁现在提前来看一看，\x01",
            "到时再尽情买个够～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9441")

    Jump("loc_98E1")

    label("loc_9446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_948A")

    #C0590
    ChrTalk(
        0xFE,
        "（四处闲逛～）\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xFE,
        "……呼，怎么逛都不会厌倦呢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_948A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_94B9")

    #C0592
    ChrTalk(
        0xFE,
        (
            "你也很享受\x01",
            "逛商店的乐趣吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_94B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_950A")

    #C0593
    ChrTalk(
        0xFE,
        (
            "今天我也是从刚开店时就一直在逛了，\x01",
            "早晨来购物就是清爽愉快啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_950A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_9566")

    #C0594
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "都已经这个时间了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xFE,
        (
            "好久都没这么痛快地\x01",
            "一直逛到关店时间了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_9566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9599")

    #C0596
    ChrTalk(
        0xFE,
        (
            "不好意思啊！\x01",
            "我正忙着买东西呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_9599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9611")

    #C0597
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔，汇集了\x01",
            "大陆各地的名牌产品。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        (
            "但这些东西的价格并不是\x01",
            "我的私房钱可以承受的啊，唉……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_9611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_974A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96EC")

    #C0599
    ChrTalk(
        0xFE,
        (
            "彩虹剧团那让人期待已久\x01",
            "的新剧目，终于开始出售\x01",
            "门票了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xFE,
        (
            "呼，我也很想要，\x01",
            "但好像有些贵呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "而且，之前发售的时候，好像\x01",
            "只用一天就全部卖光了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0xFE,
        "这次也会引发一场争夺战吧～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9745")

    label("loc_96EC")


    #C0603
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的新剧公演，\x01",
            "我一直都很期待。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xFE,
        "……如果通宵排队，或许就可以买到票了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_9745")

    Jump("loc_98E1")

    label("loc_974A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_97C5")

    #C0605
    ChrTalk(
        0xFE,
        (
            "那么，料理的食材也已经买过了，\x01",
            "也去普拉达小姐那里\x01",
            "看过有什么新商品了……\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xFE,
        (
            "那个～\x01",
            "再接下来应该是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_97C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_983F")

    #C0607
    ChrTalk(
        0xFE,
        (
            "那个那个，你看到洋装店的新款服装了吗？\x01",
            "我好想要啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xFE,
        (
            "但是就算和老公说，\x01",
            "他一定也会反对吧，唉……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_983F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9876")

    #C0609
    ChrTalk(
        0xFE,
        (
            "啊，肯真是的，在那种地方\x01",
            "做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98E1")

    label("loc_9876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_98E1")

    #C0610
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，这么多家店都到了\x01",
            "一大堆新商品啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xFE,
        (
            "百货店这种地方，\x01",
            "果然必须要经常来逛才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98E1")

    TalkEnd(0xFE)
    Return()

    # Function_22_9271 end

    def Function_23_98E5(): pass

    label("Function_23_98E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9943")

    #C0612
    ChrTalk(
        0xFE,
        "呼……妈妈还是老样子。\x02",
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xFE,
        (
            "至少也该先想好买什么东西，\x01",
            "然后再出家门嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_99A3")

    #C0614
    ChrTalk(
        0xFE,
        (
            "妈妈今天也是一样，一大早\x01",
            "就带着我来百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xFE,
        (
            "呼啊啊……\x01",
            "我还想继续睡呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_99A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_99F6")

    #C0616
    ChrTalk(
        0xFE,
        "今天是爸爸的发薪日。\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "……也就是妈妈\x01",
            "欲罢不能的疯狂购物日。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_99F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9AF3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A6B")

    #C0618
    ChrTalk(
        0xFE,
        (
            "妈妈……\x01",
            "来了百货店好几次，\x01",
            "但却没买多少东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        "真是个只逛不买的常客啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AEE")

    label("loc_9A6B")


    #C0620
    ChrTalk(
        0xFE,
        (
            "我爸爸把钱包\x01",
            "的支配权完全交给\x01",
            "妈妈来掌握。\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xFE,
        (
            "……不过，为了避免家庭财政出现赤字，\x01",
            "这也是深思熟虑之后才做出的最佳决定吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AEE")

    Jump("loc_9F3D")

    label("loc_9AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9B3A")

    #C0622
    ChrTalk(
        0xFE,
        (
            "妈妈老是在百货店逛来逛去……\x01",
            "她难道永远都逛不腻吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9BAE")

    #C0623
    ChrTalk(
        0xFE,
        (
            "妈妈是那种即使不买也可以\x01",
            "满足的稀有人种。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        (
            "陪她一起来逛百货店，总会\x01",
            "感觉浪费了相当多的时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9C19")

    #C0625
    ChrTalk(
        0xFE,
        (
            "从早上开始，我就被妈妈\x01",
            "带到这里来购物。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "……唉，\x01",
            "今天明明约好了和朋友\x01",
            "一起去玩的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_9CA3")

    #C0627
    ChrTalk(
        0xFE,
        (
            "差不多也快到爸爸下班回家的时间了，\x01",
            "但晚饭和洗澡水都没有准备好。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        (
            "……爸爸对妈妈的这种性格\x01",
            "还真是非常有包容性呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9CD2")

    #C0629
    ChrTalk(
        0xFE,
        (
            "对不起，\x01",
            "我正忙着陪妈妈呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9D23")

    #C0630
    ChrTalk(
        0xFE,
        (
            "妈妈都已经不是小孩子了，\x01",
            "真希望她不要总是关注这些所谓的名牌。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9DA8")

    #C0631
    ChrTalk(
        0xFE,
        (
            "彩虹剧团……\x01",
            "我也很想去看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        (
            "……不过以妈妈这种性格，\x01",
            "估计当天还会在百货店里购物，\x01",
            "把公演的事情彻底忘掉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9E0E")

    #C0633
    ChrTalk(
        0xFE,
        (
            "妈妈会把上午时间的\x01",
            "一半都用于购物。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xFE,
        (
            "然后，等到下午之后，\x01",
            "再继续新一轮的购物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9E6C")

    #C0635
    ChrTalk(
        0xFE,
        (
            "我今天也陪妈妈\x01",
            "一起来购物。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        (
            "相比之下，还是\x01",
            "一个人留下看家比较轻松啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9ED9")

    #C0637
    ChrTalk(
        0xFE,
        (
            "妈妈根本就没有一点要买的意思，\x01",
            "却每次都要翻遍店内的每一个角落。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xFE,
        "……总觉得很丢脸呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F3D")

    label("loc_9ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9F3D")

    #C0639
    ChrTalk(
        0xFE,
        (
            "妈妈买东西要花很多时间。\x01",
            "要让人等很久呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xFE,
        "……不过也无所谓，因为我早就习惯了。\x02",
    )

    CloseMessageWindow()

    label("loc_9F3D")

    TalkEnd(0xFE)
    Return()

    # Function_23_98E5 end

    def Function_24_9F41(): pass

    label("Function_24_9F41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FD7")

    #C0641
    ChrTalk(
        0xFE,
        (
            "绞尽脑汁想了半天，最后还是\x01",
            "买了个和老伴一模一样的胸针。\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xFE,
        (
            "回去之后大概会被老伴嘲笑吧……\x01",
            "不过，这也是情趣之一。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_9FFC")

    label("loc_9FD7")


    #C0643
    ChrTalk(
        0xFE,
        (
            "和老伴用同款胸针\x01",
            "其实也不坏吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FFC")

    Jump("loc_A9A6")

    label("loc_A001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A06E")

    #C0644
    ChrTalk(
        0xFE,
        (
            "现在好像在街上都看不到\x01",
            "鲁巴彻的成员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xFE,
        "他们不在的话，反而让人感觉到另一种诡异呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9A6")

    label("loc_A06E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A0D6")

    #C0646
    ChrTalk(
        0xFE,
        "黑手党终于闹出事了啊。\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xFE,
        (
            "即使是鲁巴彻，\x01",
            "干得那么过火，也不可能\x01",
            "将责任推脱干净吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A6")

    label("loc_A0D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A1E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A152")

    #C0648
    ChrTalk(
        0xFE,
        (
            "在以前，一枚结婚戒指的价格，\x01",
            "相当于三个月的薪水呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xFE,
        "……我又想起年轻时代了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A1E1")

    label("loc_A152")


    #C0650
    ChrTalk(
        0xFE,
        (
            "把胸针送给老伴之后，\x01",
            "自己也想要一个了。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xFE,
        (
            "频繁跑了那么多趟，\x01",
            "然后老伴就嘲笑我说，一把年纪了还像\x01",
            "小女孩一样喜欢这种东西，真是不成体统。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1E1")

    Jump("loc_A9A6")

    label("loc_A1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A299")

    #C0652
    ChrTalk(
        0xFE,
        (
            "纪念庆典的最终日，市长在闭幕式\x01",
            "上的致辞也很精彩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        "你们没有去听吗？\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xFE,
        (
            "……真是让人叹息啊。\x01",
            "肩负着克洛斯贝尔未来的年轻人，\x01",
            "怎么能对时事如此漠不关心呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A6")

    label("loc_A299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A2D8")

    #C0655
    ChrTalk(
        0xFE,
        (
            "项链吗……\x01",
            "对老伴来说，这种东西太幼稚了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A6")

    label("loc_A2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A41C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3AB")

    #C0656
    ChrTalk(
        0xFE,
        (
            "前一段时间，克洛斯贝尔时代周刊\x01",
            "曝光了有偷税漏税嫌疑的\x01",
            "自治州议员哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xFE,
        (
            "但在他因为身体不适而突然住院之后，\x01",
            "相关的话题就戛然而止了……\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0xFE,
        (
            "又想用这种肮脏的手段\x01",
            "来逃脱责任吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A417")

    label("loc_A3AB")


    #C0659
    ChrTalk(
        0xFE,
        (
            "有偷税漏税嫌疑的那个议员……\x01",
            "名字好像是……\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xFE,
        (
            "盖……盖贝尔？格巴拉……？\x01",
            "嗯、嗯，好像就是这个名字。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A417")

    Jump("loc_A9A6")

    label("loc_A41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_A472")

    #C0661
    ChrTalk(
        0xFE,
        (
            "嗯～真是好难决定啊。\x01",
            "虽然不管是什么礼物，\x01",
            "老伴都会很开心地收下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A6")

    label("loc_A472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A4A5")

    #C0662
    ChrTalk(
        0xFE,
        (
            "嗯……这个帽子\x01",
            "款式相当别致呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A6")

    label("loc_A4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A5F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A56D")

    #C0663
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔警备队\x01",
            "在贝尔加德门\x01",
            "设立了司令总部哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0xFE,
        (
            "听说那是一支配备了最新\x01",
            "装备的精锐部队……\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0xFE,
        (
            "但因为没有供其表现的机会，\x01",
            "所以一直都只能负责一些\x01",
            "无关紧要的任务。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A5EC")

    label("loc_A56D")


    #C0666
    ChrTalk(
        0xFE,
        (
            "听说克洛斯贝尔警备队\x01",
            "是配备了最新装备的精锐部队。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xFE,
        (
            "但因为没有供其表现的机会，\x01",
            "所以一直都只能负责一些\x01",
            "无关紧要的任务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5EC")

    Jump("loc_A9A6")

    label("loc_A5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A656")
    OP_93(0xFE, 0x5A, 0x0)

    #C0668
    ChrTalk(
        0xFE,
        (
            "嗯，原来在这里的戒指\x01",
            "已经卖掉了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xFE,
        (
            "本来还觉得它很适合\x01",
            "我老伴呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A6")

    label("loc_A656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A746")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6EF")

    #C0670
    ChrTalk(
        0xFE,
        (
            "听传闻说，玛因兹那里\x01",
            "好像出现了魔兽侵害的事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0xFE,
        "嗯，这种情况还真是罕见啊。\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0xFE,
        (
            "是不是驱赶魔兽的\x01",
            "导力灯坏掉了呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A741")

    label("loc_A6EF")


    #C0673
    ChrTalk(
        0xFE,
        (
            "现在和以前不同，驱赶魔兽\x01",
            "的导力灯都已经普及了。\x01",
            "遭到魔兽侵害的情况很少见呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A741")

    Jump("loc_A9A6")

    label("loc_A746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A82E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7FC")

    #C0674
    ChrTalk(
        0xFE,
        (
            "这次的自治州议会\x01",
            "就是一群废物的大汇集啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0xFE,
        (
            "只懂得派系斗争，\x01",
            "却没通过一项有用的法案……\x01",
            "哎呀呀，真令人悲哀啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x102,
        "#0108F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A829")

    label("loc_A7FC")


    #C0677
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "这世上尽是些令人悲哀的事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A829")

    Jump("loc_A9A6")

    label("loc_A82E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A87E")

    #C0678
    ChrTalk(
        0xFE,
        (
            "我想给相处多年的老伴\x01",
            "送件礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "这可是好东西呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A6")

    label("loc_A87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A9A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A92C")

    #C0680
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔，每年都会发生\x01",
            "好几起可疑事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0xFE,
        (
            "前几天，在后巷那边\x01",
            "据说还发生了枪击事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0xFE,
        (
            "这个自治州也许并没有\x01",
            "外表看上去那么光鲜。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A9A6")

    label("loc_A92C")


    #C0683
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔，每年都会发生\x01",
            "好几起可疑事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0xFE,
        (
            "……即使已经基本确定犯人的身份了，\x01",
            "大多数情况下也不会去逮捕他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9A6")

    TalkEnd(0xFE)
    Return()

    # Function_24_9F41 end

    def Function_25_A9AA(): pass

    label("Function_25_A9AA")

    TalkBegin(0xFE)
    Call(0, 27)
    TalkEnd(0xFE)
    Return()

    # Function_25_A9AA end

    def Function_26_A9B4(): pass

    label("Function_26_A9B4")

    TalkBegin(0xFE)
    Call(0, 27)
    TalkEnd(0xFE)
    Return()

    # Function_26_A9B4 end

    def Function_27_A9BE(): pass

    label("Function_27_A9BE")

    OP_4B(0x17, 0xFF)
    OP_4B(0x16, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_AAAD")

    #C0685
    ChrTalk(
        0x16,
        (
            "莉夏很丰满，所以很难塑造成\x01",
            "苗条纤细的形象。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x16,
        (
            "嗯嗯，这就需要在搭配组合上\x01",
            "多下工夫了……\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x17,
        (
            "#1806F#5P（呼……\x01",
            "  这也许还真是最大的问题吧。）\x02\x03",

            "#1808F（虽然在进行『那种装扮』的时候\x01",
            "  可以用内功来改变体型……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC47")

    label("loc_AAAD")


    #C0688
    ChrTalk(
        0x16,
        (
            "嗯～那件虽然也不错，\x01",
            "但刚才的那件也难以舍弃呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x16,
        (
            "啊，这件有碎花图案的\x01",
            "好像和莉夏正相配吧¤\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 750)

    #C0690
    ChrTalk(
        0x17,
        (
            "#1810F#5P桑桑……\x01",
            "你的好意虽然让我很高兴，\x02\x03",

            "但难得的休假日，\x01",
            "还是不要给我挑选衣服啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x17, 750)

    #C0691
    ChrTalk(
        0x16,
        (
            "不行不行！\x01",
            "莉夏那么可爱，但好像\x01",
            "却没有多少衣服。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x16,
        (
            "既然如此，桑桑\x01",
            "必须要多给你选些可爱的衣服！\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x16,
        (
            "毕竟是倍受瞩目的新人，\x01",
            "不多在时尚方面下些\x01",
            "工夫可是不行的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x17,
        "#1809F#5P嗯、嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_AC47")

    OP_4C(0x17, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_27_A9BE end

    def Function_28_AC50(): pass

    label("Function_28_AC50")

    TalkBegin(0xFE)

    #C0695
    ChrTalk(
        0x18,
        (
            "今天是来购物的，\x01",
            "买些点心好了⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x18,
        "甜食可是排练的原动力啊～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_AC50 end

    def Function_29_AC9A(): pass

    label("Function_29_AC9A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-16810, 1500, 23180, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x19F, -16000, 0, 22500, 0)
    SetChrPos(0x109, -15250, 0, 22000, 0)
    SetChrPos(0x101, -16750, 0, 21250, 0)
    OP_93(0xE, 0xB4, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 3)), scpexpr(EXPR_END)), "loc_ADDD")

    #C0697
    ChrTalk(
        0xE,
        (
            "#5P能让女性喜欢的\x01",
            "礼物嘛，\x01",
            "那当然是『咪西玩偶』啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0xE,
        (
            "#5P没有女孩子\x01",
            "会讨厌玩偶吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x109,
        (
            "#12P#0500F芙兰很喜欢可爱的东西，\x01",
            "玩偶倒也是个不错的选择。\x02\x03",

            "#0503F虽然我也不知道\x01",
            "她是否喜欢咪西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFDE")

    label("loc_ADDD")


    #C0700
    ChrTalk(
        0xE,
        (
            "#5P欢迎光临，\x01",
            "这里是杂货柜台哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0xE,
        "#5P想找点什么呢？\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#12P#0000F那个……我们想找些\x01",
            "女性可能会喜欢的礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0xE,
        (
            "#5P女性可能会喜欢的\x01",
            "礼物嘛……\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0xE,
        (
            "#5P嗯，那样的话……\x01",
            "这个『咪西玩偶』\x01",
            "怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0xE,
        (
            "#5P没有女孩子\x01",
            "会讨厌玩偶吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x19F,
        (
            "#12P噢噢，这个……\x01",
            "看起来好像还不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x109,
        (
            "#12P#0503F是啊……\x02\x03",

            "#0500F芙兰很喜欢可爱的东西，\x01",
            "玩偶倒也是个不错的选择。\x02\x03",

            "#0503F虽然我也不知道\x01",
            "她是否喜欢咪西。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x19F,
        (
            "#12P怎么办呢……\x01",
            "我不擅长\x01",
            "做这种决定呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x19F,
        (
            "#12P送给芙兰小姐的礼物，\x01",
            "就选择『咪西玩偶』，\x01",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 3)

    label("loc_AFDE")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【推荐这个礼物】\x01",      # 0
            "【再考虑一下】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0EE")

    #C0710
    ChrTalk(
        0x101,
        (
            "#12P#0000F这个礼物不是\x01",
            "很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x19F,
        (
            "#12P……听你这么一说，\x01",
            "看起来好像是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x19F,
        (
            "#12P那么，我就要这个。\x01",
            "啊，麻烦您包装得漂亮一点啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0xE,
        (
            "#5P好的，多谢您的\x01",
            "惠顾。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x4)
    Call(0, 34)
    Jump("loc_B15B")

    label("loc_B0EE")


    #C0714
    ChrTalk(
        0x101,
        (
            "#12P#0000F这个嘛……\x01",
            "还是再挑挑看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x19F,
        (
            "#12P……嗯，也是呢。\x01",
            "最好多去几个店看看。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -16000, 0, 22500, 0)
    EventEnd(0x5)

    label("loc_B15B")

    Return()

    # Function_29_AC9A end

    def Function_30_B15C(): pass

    label("Function_30_B15C")

    EventBegin(0x0)
    Fade(500)
    OP_68(15120, 1500, 7250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x19F, 16000, 0, 6500, 0)
    SetChrPos(0x109, 16750, 0, 6000, 0)
    SetChrPos(0x101, 15250, 0, 5250, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 4)), scpexpr(EXPR_END)), "loc_B2F6")

    #C0716
    ChrTalk(
        0xB,
        (
            "#5P这个雷米菲利亚产的\x01",
            "『清凉果酱』怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0xB,
        (
            "#5P这种口感冰凉清爽，让人欲罢不能的\x01",
            "果酱，最近已经悄悄流行起来了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x109,
        (
            "#12P#0500F芙兰从以前开始就经常吃面包，\x01",
            "如果收到珍奇的果酱，应该会很高兴吧。\x02\x03",

            "#0503F不过，如果要送礼物，或许还是\x01",
            "选择那些能够保存下来的东西比较好吧……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B588")

    label("loc_B2F6")


    #C0719
    ChrTalk(
        0xB,
        (
            "#5P欢迎光临\x01",
            "『利乔食品店』～\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0xB,
        (
            "#5P我们的商品非常丰富，\x01",
            "连进口食材也都有哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x101,
        (
            "#12P#0000F那个……其实我们正在\x01",
            "寻找女性可能会喜欢的礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0xB,
        (
            "#5P啊，礼物吗？\x01",
            "嗯嗯，这个嘛，那么……\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0xB,
        (
            "#5P这个雷米菲利亚产的\x01",
            "『清凉果酱』怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xB,
        (
            "#5P这种口感冰凉清爽，让人欲罢不能的\x01",
            "果酱，最近已经悄悄流行起来了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x19F,
        (
            "#11P果酱吗……\x01",
            "这种令人意想不到的礼物，\x01",
            "也许会得到她的偏爱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x109,
        (
            "#12P#0500F这个嘛……\x01",
            "芙兰从以前开始就经常吃面包，\x01",
            "如果收到珍奇的果酱，应该会很高兴吧。\x02\x03",

            "#0503F不过，如果要送礼物，或许还是\x01",
            "选择那些能够保存下来的东西比较好吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x19F,
        (
            "#11P嗯～该怎么办呢……\x01",
            "我完全迷茫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x19F,
        (
            "#11P送给芙兰小姐的礼物，\x01",
            "就选择『清凉果酱』，\x01",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 4)

    label("loc_B588")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【推荐这个礼物】\x01",      # 0
            "【再考虑一下】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B69A")

    #C0729
    ChrTalk(
        0x101,
        (
            "#12P#0000F这个礼物不是\x01",
            "很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x19F,
        (
            "#11P……听你这么一说，\x01",
            "看起来好像是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x19F,
        (
            "#11P那么，我就要这个吧。\x01",
            "啊，麻烦您包装得漂亮一点啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xB,
        (
            "#5P好的，多谢\x01",
            "您的惠顾。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x5)
    Call(0, 34)
    Jump("loc_B70F")

    label("loc_B69A")


    #C0733
    ChrTalk(
        0x101,
        (
            "#12P#0000F这个嘛……\x01",
            "还是再挑挑看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x19F,
        (
            "#11P……是、是这样吗？\x01",
            "那我们就再去其它店看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 16000, 0, 6500, 0)
    EventEnd(0x5)

    label("loc_B70F")

    Return()

    # Function_30_B15C end

    def Function_31_B710(): pass

    label("Function_31_B710")

    EventBegin(0x0)
    Fade(500)
    OP_68(16149, 9530, 11470, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x19F, 15500, 8029, 12250, 90)
    SetChrPos(0x109, 14500, 8029, 11500, 90)
    SetChrPos(0x101, 14750, 8029, 13000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 5)), scpexpr(EXPR_END)), "loc_B884")

    #C0735
    ChrTalk(
        0xC,
        (
            "#11P我们这里的新产品\x01",
            "『波波绒线帽』如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xC,
        (
            "#11P白色波波造型的可爱绒线帽，\x01",
            "这柔软的手感会让人\x01",
            "入迷哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x109,
        (
            "#12P#0500F是啊……\x01",
            "这种帽子与芙兰的便服\x01",
            "应该也会很搭呢。\x02\x03",

            "#0503F不过，以芙兰的那种发型，\x01",
            "可能有些不方便戴帽子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAED")

    label("loc_B884")


    #C0738
    ChrTalk(
        0xC,
        "#11P欢迎光临『卢卡』时装店。\x02",
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xC,
        (
            "#11P从童装到男装，\x01",
            "各种名牌服装一应俱全哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xC,
        "#11P若有什么需要，请尽管吩咐。\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x101,
        (
            "#6P#0000F那个……其实我们正在\x01",
            "寻找女性可能会喜欢的礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0xC,
        (
            "#11P是送给女性的礼物吗？\x01",
            "这个嘛……\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xC,
        (
            "#11P我们的新产品，\x01",
            "『波波绒线帽』如何呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xC,
        (
            "#11P白色波波造型的可爱绒线帽，\x01",
            "这柔软的手感会让人\x01",
            "入迷哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x19F,
        (
            "#5P绒线帽吗……\x01",
            "这么可爱，好像很适合\x01",
            "她的风格呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x109,
        (
            "#12P#0500F是啊……\x01",
            "这种帽子与芙兰的便服\x01",
            "应该也会很搭呢。\x02\x03",

            "#0503F不过，以芙兰的那种发型，\x01",
            "可能有些不方便戴帽子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x19F,
        (
            "#5P嗯、嗯……\x01",
            "这可是个相当危险的赌博呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x19F,
        (
            "#5P送给芙兰小姐的礼物，\x01",
            "就选择『波波绒线帽』，\x01",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 5)

    label("loc_BAED")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【推荐这个礼物】\x01",      # 0
            "【再考虑一下】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC09")

    #C0749
    ChrTalk(
        0x101,
        (
            "#6P#0000F这个礼物不是\x01",
            "很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x19F,
        (
            "#5P……听你这么一说，\x01",
            "看起来好像是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x19F,
        (
            "#5P那么，我就要这个吧。\x01",
            "啊，麻烦您包装得漂亮一点啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0xC,
        (
            "#11P呵呵，感谢您的惠顾。\x01",
            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x6)
    Call(0, 34)
    Jump("loc_BCA5")

    label("loc_BC09")


    #C0753
    ChrTalk(
        0x101,
        (
            "#6P#0000F虽然很难决定……\x01",
            "不过我们还有时间，再去\x01",
            "其它地方看看也不迟吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x19F,
        (
            "#5P说、说得也是啊，\x01",
            "那我们就去别处再看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 15500, 8029, 12250, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    EventEnd(0x5)

    label("loc_BCA5")

    Return()

    # Function_31_B710 end

    def Function_32_BCA6(): pass

    label("Function_32_BCA6")

    EventBegin(0x0)
    Fade(500)
    OP_68(-460, 9520, 27870, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x19F, 0, 8029, 27750, 0)
    SetChrPos(0x109, 750, 8029, 27250, 0)
    SetChrPos(0x101, -750, 8029, 26500, 0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 6)), scpexpr(EXPR_END)), "loc_BE2D")

    #C0755
    ChrTalk(
        0xA,
        (
            "#5P我们这里的\x01",
            "『斯托雷加长靴』\x01",
            "怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0xA,
        (
            "#5P斯托雷加公司的产品，质量绝对有保证。\x01",
            "而且这款靴子现在在女性群体中是\x01",
            "最受欢迎的款式。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x109,
        (
            "#12P#0500F她倒是说过，\x01",
            "最近很关注长靴呢。\x02\x03",

            "#0503F但是，她到底会不会喜欢\x01",
            "这种流行的款式，\x01",
            "就另当别论了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C07E")

    label("loc_BE2D")


    #C0758
    ChrTalk(
        0xA,
        (
            "#5P欢迎光临，\x01",
            "本店出售各种鞋子。\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0xA,
        (
            "#5P运动鞋、皮鞋、长靴……\x01",
            "客人们需要的款式，\x01",
            "我们这里一应俱全。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x101,
        (
            "#12P#0000F我们正在寻找\x01",
            "女性可能会喜欢的礼物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0xA,
        "#5P嗯，让我想想哦……\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0xA,
        (
            "#5P那么，这双\x01",
            "『斯托雷加长靴』\x01",
            "应该不错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0xA,
        (
            "#5P斯托雷加公司的产品，质量绝对有保证。\x01",
            "而且这款靴子现在在女性群体中是\x01",
            "最受欢迎的款式。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x19F,
        (
            "#11P长靴吗……\x01",
            "姐姐，芙兰小姐平时\x01",
            "会穿长靴吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x109,
        (
            "#12P#0500F她倒是说过，\x01",
            "最近很关注长靴呢。\x02\x03",

            "#0503F但是，她到底会不会喜欢\x01",
            "这种流行的款式，\x01",
            "就另当别论了……\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x19F,
        "#11P真、真是拿不定主意啊……\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x19F,
        (
            "#11P送给芙兰小姐的礼物，\x01",
            "就选择『斯托雷加长靴』，\x01",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 6)

    label("loc_C07E")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【推荐这个礼物】\x01",      # 0
            "【再考虑一下】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C18E")

    #C0768
    ChrTalk(
        0x101,
        (
            "#12P#0000F这个礼物不是\x01",
            "很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x19F,
        (
            "#11P……听你这么一说，\x01",
            "看起来好像是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x19F,
        (
            "#11P那么，我就要这个吧。\x01",
            "啊，麻烦您包装得漂亮一点啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0xA,
        (
            "#5P非常感谢您的\x01",
            "惠顾。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x7)
    Call(0, 34)
    Jump("loc_C224")

    label("loc_C18E")


    #C0772
    ChrTalk(
        0x101,
        (
            "#12P#0000F……还是去其它的店看看吧。\x01",
            "我觉得还有时间，不会迟到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x19F,
        (
            "#11P说得也是啊……\x01",
            "那就再去别处\x01",
            "稍微逛逛吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 8029, 27700, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    EventEnd(0x5)

    label("loc_C224")

    Return()

    # Function_32_BCA6 end

    def Function_33_C225(): pass

    label("Function_33_C225")

    EventBegin(0x0)
    Fade(500)
    OP_68(-12820, 9330, 7150, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x19F, -13400, 8029, 6600, 45)
    SetChrPos(0x109, -13160, 8029, 5720, 45)
    SetChrPos(0x101, -14580, 8029, 6580, 45)
    OP_93(0xD, 0xE1, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 7)), scpexpr(EXPR_END)), "loc_C3AC")

    #C0774
    ChrTalk(
        0xD,
        (
            "#11P我们的精品项链\x01",
            "『粉色月亮』\x01",
            "是否符合您的要求呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xD,
        (
            "#11P这是一条装饰着粉红色宝石\x01",
            "的可爱项链哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x109,
        (
            "#12P#0500F对了……\x01",
            "芙兰很喜欢粉色，\x01",
            "我觉得这个也许相当不错呢。\x02\x03",

            "#0503F不过，第一次赠送礼物，\x01",
            "就选择项链的话，是不是\x01",
            "稍微贵重了一点呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C612")

    label("loc_C3AC")


    #C0777
    ChrTalk(
        0xD,
        (
            "#11P本店主要经营各种饰品和\x01",
            "其它小物件。\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0xD,
        (
            "#11P虽然价格稍微有些高，\x01",
            "但每一件都是优质的上乘品。\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，我们正在挑选\x01",
            "女性会喜欢的礼物，\x01",
            "您这里有什么可以推荐的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0xD,
        "#11P这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0xD,
        (
            "#11P我们的精品项链\x01",
            "『粉色月亮』\x01",
            "是否符合您的要求呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0xD,
        (
            "#11P这是一条装饰着粉红色宝石\x01",
            "的可爱项链哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x19F,
        (
            "#6P这、这个……\x01",
            "看起来好像非常棒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x109,
        (
            "#12P#0500F是啊……\x01",
            "芙兰很喜欢粉色，\x01",
            "我觉得这个也许相当不错呢。\x02\x03",

            "#0503F不过，第一次赠送礼物，\x01",
            "就选择项链的话，是不是\x01",
            "稍微贵重了一点呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x19F,
        (
            "#6P确、确实……如果送这种东西，\x01",
            "可能会显得别有深意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x19F,
        (
            "#6P送给芙兰小姐的礼物，\x01",
            "就选择『粉色月亮』，\x01",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 7)

    label("loc_C612")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【推荐这个礼物】\x01",      # 0
            "【再考虑一下】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C735")

    #C0787
    ChrTalk(
        0x101,
        (
            "#6P#0000F这个礼物不是\x01",
            "很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x19F,
        (
            "#6P……听你这么一说，\x01",
            "看起来好像是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x19F,
        (
            "#6P那么，我就要这个吧。\x01",
            "啊，麻烦您包装得漂亮一点啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0xD,
        (
            "#11P呵呵，明白了。\x01",
            "一定会认真替您\x01",
            "包装好的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x8)
    Call(0, 34)
    Jump("loc_C79D")

    label("loc_C735")


    #C0791
    ChrTalk(
        0x101,
        "#6P#0000F嗯，还是再考虑一下好了。\x02",
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x19F,
        (
            "#6P嗯嗯……\x01",
            "选礼物真是很难啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -13400, 8029, 6600, 45)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    EventEnd(0x5)

    label("loc_C79D")

    Return()

    # Function_33_C225 end

    def Function_34_C79E(): pass

    label("Function_34_C79E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x10, 0xFF)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    OP_68(0, 1500, 3750, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19400, 0)
    SetChrPos(0x101, 0, 30, 4750, 180)
    SetChrPos(0x109, -750, 30, 3250, 45)
    SetChrPos(0x19F, 750, 30, 3250, 315)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x10, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0793
    ChrTalk(
        0x19F,
        (
            "#11P多亏你们的帮忙，总算是\x01",
            "买到了不错的礼物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x19F,
        (
            "#11P要是芙兰小姐\x01",
            "能喜欢就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x109,
        (
            "#6P#0503F嗯～这要等到将礼物\x01",
            "送给她后才能知道了……\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x101,
        (
            "#5P#0005F噢……\x01",
            "我们差不多也该\x01",
            "去西餐厅啦。\x02\x03",

            "#0000F芙兰可能已经\x01",
            "在那里等着我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x19F,
        (
            "#11P好、好的……\x01",
            "那我们这就出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x109,
        "#6P#0508F（…………………………）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_C79E end

    def Function_35_C98D(): pass

    label("Function_35_C98D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_C9F8")

    #C0799
    ChrTalk(
        0x101,
        (
            "#0000F还没帮安敦先生\x01",
            "选好礼物呢。\x02\x03",

            "而且芙兰的休息时间\x01",
            "也没有那么长，\x01",
            "还是快点决定吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA91")

    label("loc_C9F8")


    #C0800
    ChrTalk(
        0x19F,
        "你要去哪里啊？\x02",
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x19F,
        (
            "不是要帮我\x01",
            "一起挑选礼物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x109,
        (
            "#0500F不快点的话，\x01",
            "芙兰的休息时间\x01",
            "可就要结束了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x101,
        (
            "#0000F也、也是呢，\x01",
            "我们快点去选吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_CA91")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 0, 0)
    EventEnd(0x4)
    Return()

    # Function_35_C98D end

    def Function_36_CAA8(): pass

    label("Function_36_CAA8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3660, 2029, 7210, 0)
    MoveCamera(17, 21, 1, 0)
    OP_6E(500, 0)
    SetCameraDistance(16100, 0)
    SetChrPos(0x101, 3750, 30, 9040, 45)
    SetChrPos(0x102, 4920, 30, 7850, 45)
    SetChrPos(0x103, 2550, 0, 7830, 45)
    SetChrPos(0x104, 3730, 0, 6660, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBC7")

    #C0804
    ChrTalk(
        0x101,
        (
            "#6P#0003F（百货店……\x01",
            "  这里是遗失了物品的特伦特先生\x01",
            "  途中经过的地方呢。）\x02\x03",

            "#0000F不好意思，请问您在这附近\x01",
            "捡到过什么失物吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_CC01")

    label("loc_CBC7")


    #C0805
    ChrTalk(
        0x101,
        (
            "#6P#0000F不好意思，请问您在这附近\x01",
            "捡到过什么失物吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC01")


    #C0806
    ChrTalk(
        0x9,
        "#5P要询问遗失物品方面的事项啊。\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x8,
        (
            "#11P嗯，我们这个窗口\x01",
            "保管着很多件哦，\x01",
            "请问您在找什么样的失物呢？\x02",
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

    #C0808
    ChrTalk(
        0x104,
        (
            "#12P#0305F喂喂，保管着好几件吗……\x01",
            "莫非全都是……\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯……\x01",
            "仔细想想的话，在百货店中，\x01",
            "似乎经常会有人丢失物品呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x102,
        (
            "#12P#0100F特伦特先生遗失的是\x01",
            "钱包、特产，还有……\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x103,
        (
            "#6P#0200F……应该把遗失物品\x01",
            "的具体特征问得再\x01",
            "详细一些呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0812
    ChrTalk(
        0x8,
        "#11P啊，莫非是……\x02",
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x8,
        (
            "#11P背包破了个洞，钱包从里面\x01",
            "掉了出来的那位先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x101,
        "#6P#0005F嗯，就是那个人！\x02",
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x102,
        (
            "#12P#0100F太好了，看来\x01",
            "有人目击到了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x8,
        "啊，不，并不是那样的……\x02",
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x8,
        (
            "那位先生在本店的\x01",
            "客人中算是非常显眼的。\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x9,
        (
            "#5P那是一位笑容满面的先生，\x01",
            "不管遇到谁，都会热情地\x01",
            "给对方讲笑话。\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x9,
        (
            "#5P然后，在他要回去时，\x01",
            "不慎将背包钩到了\x01",
            "陈列柜上。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x9,
        (
            "#5P等到我们随后去收拾时，\x01",
            "发现了掉落在那里的钱包。\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x102,
        "#12P#0100F是、是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x103,
        "#6P#0203F（结论显而易见啊……）\x02",
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x101,
        (
            "#6P#0003F特伦特先生却没有\x01",
            "回到百货店来寻找呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x104,
        (
            "#12P#0300F大概是途中就已经精疲力尽了吧。\x02\x03",

            "哈，所以才会向我们支援科\x01",
            "提出委托嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x9,
        (
            "#5P我们马上就将失物取来，\x01",
            "请稍等片刻哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0826
    ChrTalk(
        0x9,
        "#5P就是这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0827
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x337),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "拿到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x337, 1)

    #C0828
    ChrTalk(
        0x101,
        (
            "#6P#0000F太好了，\x01",
            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x9,
        (
            "#5P呵呵，那就请您\x01",
            "转交给那位先生吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1A8")

    #C0830
    ChrTalk(
        0x104,
        (
            "#12P#0300F好的，这样一来，\x01",
            "那家伙的失物就已经全部找到了。\x01",
            "马上回去向他报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1A8")

    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2, 0x1, 0x1)
    SetScenarioFlags(0x1, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1E0")
    OP_29(0x2, 0x1, 0x1F)

    label("loc_D1E0")

    SetChrPos(0x0, 3740, 0, 7840, 45)
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_68(3740, 1800, 7840, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    EventEnd(0x5)
    Return()

    # Function_36_CAA8 end

    def Function_37_D22A(): pass

    label("Function_37_D22A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0831
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２Ｆ　『卢卡』时装店\x01",
            "２Ｆ　『汉森』鞋店\x01",
            "２Ｆ　『贝卡』饰品店\x01",
            "１Ｆ　『利乔』食品店\x01",
            "１Ｆ　『沙扎克』杂货柜台\x02",
        )
    )

    CloseMessageWindow()

    #A0832
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※若有不明之处，\x01",
            "　敬请随时咨询\x01",
            "  正门综合服务台。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_37_D22A end

    SaveToFile()

Try(main)
