from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t052b.bin",                # FileName
        "t052b",                    # MapName
        "t052b",                    # Location
        0x003F,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 63, 0, 2, 0, 3],
    )

    BuildStringList((
        "t052b",                  # 0
        "诺玛",                   # 1
        "琉卡",                   # 2
        "卡洛斯",                 # 3
        "矿工玛尔罗",             # 4
        "矿工冈兹",               # 5
        "弗里吉亚",               # 6
        "莱缇娜",                 # 7
    ))

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch23602.itc",                   # 02
        "chr/ch26202.itc",                   # 03
        "chr/ch33300.itc",                   # 04
        "chr/ch34500.itc",                   # 05
        "chr/ch30702.itc",                   # 06
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

    DeclNpc(3700,    0,       4289,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4880,   -750,    -860,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-6130,   -600,    4219,    270,  469,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-9359,   -600,    -1110,   180,  469,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-8659,   -600,    -4480,   0,    469,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(204009,  0,       560,     270,  389,  0x0, 0,   4,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(199529,  0,       3160,    225,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)

    DeclActor(3700,    0,       2920,    1000,    3700,    1500,    4290,    0x007E, 0,  4,  0x0000)
    DeclActor(102600,  2000,    1500,    2000,    102600,  3200,    1500,    0x007C, 0,  12, 0x0000)

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_333",          # 02, 2
        "Function_3_41B",          # 03, 3
        "Function_4_432",          # 04, 4
        "Function_5_436",          # 05, 5
        "Function_6_68D",          # 06, 6
        "Function_7_732",          # 07, 7
        "Function_8_902",          # 08, 8
        "Function_9_A21",          # 09, 9
        "Function_10_B52",         # 0A, 10
        "Function_11_C9F",         # 0B, 11
        "Function_12_D4F",         # 0C, 12
        "Function_13_F8B",         # 0D, 13
    ))


    def Function_0_250(): pass

    label("Function_0_250")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_250 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_332")
    OP_94(0xFE, 0x31678, 0xFFFFFF1A, 0x321B8, 0x3DE, 0x3E8)
    Sleep(300)
    Jump("Function_1_308")

    label("loc_332")

    Return()

    # Function_1_308 end

    def Function_2_333(): pass

    label("Function_2_333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_341")
    Jump("loc_40B")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34F")
    Jump("loc_40B")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_40B")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_36B")
    Jump("loc_40B")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_379")
    Jump("loc_40B")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_387")
    Jump("loc_40B")

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_395")
    Jump("loc_40B")

    label("loc_395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A3")
    Jump("loc_40B")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3B1")
    Jump("loc_40B")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BF")
    Jump("loc_40B")

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3CD")
    Jump("loc_40B")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3F4")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_40B")

    label("loc_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_402")
    Jump("loc_40B")

    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_40B")

    label("loc_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_41A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_41A")

    Return()

    # Function_2_333 end

    def Function_3_41B(): pass

    label("Function_3_41B")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    OP_66(0x1, 0x1)

    label("loc_431")

    Return()

    # Function_3_41B end

    def Function_4_432(): pass

    label("Function_4_432")

    Call(0, 5)
    Return()

    # Function_4_432 end

    def Function_5_436(): pass

    label("Function_5_436")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_689")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "休息\x01",      # 2
            "放弃\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A2")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C2")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_684")

    label("loc_4C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_684")

    label("loc_4E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F6")
    Jump("loc_684")

    label("loc_4F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_684")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CB")

    #C0001
    ChrTalk(
        0x8,
        (
            "呵呵，那个房间怎么样。\x01",
            "很宽敞，很不错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "很少有像你们这样的\x01",
            "年轻人会在我们这里\x01",
            "留宿呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "……哦，要出门吗？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "最近镇上有些不太平，\x01",
            "所以最好早点回来哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_684")

    label("loc_5CB")


    #C0005
    ChrTalk(
        0x8,
        (
            "酒馆平时会来很多矿工，\x01",
            "都吵得人头疼。\x01",
            "但今天的客人比较少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "哎呀哎呀，真是被连累得好惨。\x01",
            "但马库斯刚刚受了伤，\x01",
            "也没办法……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "狼形魔兽什么的我不管，\x01",
            "只希望别再惹出麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_684")

    Jump("loc_443")

    label("loc_689")

    TalkEnd(0x8)
    Return()

    # Function_5_436 end

    def Function_6_68D(): pass

    label("Function_6_68D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_703")

    #C0008
    ChrTalk(
        0xFE,
        (
            "……哎呀哎呀，\x01",
            "每天都饮酒作乐，\x01",
            "还真是不吸取教训啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "既然工作结束了，\x01",
            "就该早点回家啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_72E")

    label("loc_703")


    #C0010
    ChrTalk(
        0xFE,
        (
            "话说回来，冈兹的\x01",
            "酒品总是那么差呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E")

    TalkEnd(0xFE)
    Return()

    # Function_6_68D end

    def Function_7_732(): pass

    label("Function_7_732")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C6")
    Jump("loc_810")

    label("loc_7C6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7E6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_810")

    label("loc_7E6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_806")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_810")

    label("loc_806")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_810")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A8")

    #C0011
    ChrTalk(
        0xFE,
        (
            "嗯～……\x01",
            "酒果然是好东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "一天的疲劳\x01",
            "仿佛都烟消云散了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "不过喝太多\x01",
            "也不是好事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8FA")

    label("loc_8A8")


    #C0014
    ChrTalk(
        0xFE,
        (
            "他们矿工平时似乎\x01",
            "也积累了不少郁愤呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "喝点美酒，\x01",
            "才能成为明天的活力嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_732 end

    def Function_8_902(): pass

    label("Function_8_902")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A6")

    #C0016
    ChrTalk(
        0xB,
        "（一饮而尽）……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "……呼～！\x01",
            "收工后喝杯酒真是格外爽啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "哦，但要注意\x01",
            "别喝太多才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "冈兹那家伙，\x01",
            "只要喝一点就会烂醉如泥了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A1D")

    label("loc_9A6")


    #C0020
    ChrTalk(
        0xB,
        (
            "冈兹那家伙，\x01",
            "只要喝一点就会烂醉如泥了。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "要是连我都喝醉的话，\x01",
            "就没人送这小子回家了……\x01",
            "哎，真是吃力不讨好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1D")

    TalkEnd(0xFE)
    Return()

    # Function_8_902 end

    def Function_9_A21(): pass

    label("Function_9_A21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADE")

    #C0022
    ChrTalk(
        0xC,
        (
            "我啊……\x01",
            "要在『巴鲁卡』大赚一笔……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        "让今后的人生变得轻松愉快……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xC,
        (
            "嗝～……\x01",
            "……喂，你在听吗，玛尔罗？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        "在听在听。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        "真是的，同样的话要说多少遍啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_B4E")

    label("loc_ADE")


    #C0027
    ChrTalk(
        0xC,
        "嗝～……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        (
            "我啊……\x01",
            "这星期一定要在『巴鲁卡』大赚一笔……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "……唉，回去之前，\x01",
            "必须让你醒醒酒才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4E")

    TalkEnd(0xFE)
    Return()

    # Function_9_A21 end

    def Function_10_B52(): pass

    label("Function_10_B52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C06")

    #C0030
    ChrTalk(
        0xFE,
        (
            "对面的房间\x01",
            "是你们在住吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "我也想住大房间，\x01",
            "但是老板娘和我说\x01",
            "两个人不能住四人间。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "那个老板娘，还真是颇有胆量哦。\x01",
            "好久都没有人敢\x01",
            "不顺着我的意了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C9B")

    label("loc_C06")


    #C0033
    ChrTalk(
        0xFE,
        (
            "算了，反正我们就两个人……\x01",
            "暂时忍耐一下，凑和住这个房间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "话说回来，明天还得\x01",
            "跟镇长交涉才行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "七耀石的结晶……\x01",
            "明天一定要弄到手！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9B")

    TalkEnd(0xFE)
    Return()

    # Function_10_B52 end

    def Function_11_C9F(): pass

    label("Function_11_C9F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D09")

    #C0036
    ChrTalk(
        0xFE,
        (
            "啊……要把餐具\x01",
            "还给店里才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "就因为小姐耍脾气，\x01",
            "要在房间里用餐……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_D4B")

    label("loc_D09")


    #C0038
    ChrTalk(
        0xFE,
        (
            "把餐点拿到房间里\x01",
            "是没问题……\x01",
            "但真担心送回去的时候会摔倒啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4B")

    TalkEnd(0xFE)
    Return()

    # Function_11_C9F end

    def Function_12_D4F(): pass

    label("Function_12_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8A")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【等待到深夜】\x01",      # 0
            "【还有其它事】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DB7"),
        (1, "loc_EE6"),
        (SWITCH_DEFAULT, "loc_F88"),
    )


    label("loc_DB7")


    #C0039
    ChrTalk(
        0x101,
        (
            "#0003F那么，就暂时留在这里，\x01",
            "一直等待到深夜吧。\x02\x03",

            "#0001F还要决定好魔兽出现时的\x01",
            "作战计划和人员配置。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        (
            "#0201F光是击退魔兽\x01",
            "还不行吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0103F嗯，还必须要制服\x01",
            "操纵魔兽的黑手党们。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0302F嘿，似乎是个\x01",
            "难度相当高的任务啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0x5C, 0)
    NewScene("t050B", 0, 0, 0)
    IdleLoop()
    Jump("loc_F88")

    label("loc_EE6")


    #C0043
    ChrTalk(
        0x104,
        (
            "#0300F那么，准备就绪之后\x01",
            "再回到这里来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果要在房间等待到深夜，\x01",
            "请在桌子上出现！标志时\x01",
            "按○键。  \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_F88")

    label("loc_F88")

    EventEnd(0x3)

    label("loc_F8A")

    Return()

    # Function_12_D4F end

    def Function_13_F8B(): pass

    label("Function_13_F8B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50111.itc", 0x22)
    OP_68(102070, 4500, 1190, 0)
    MoveCamera(58, 19, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32299, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 102700, 2200, 3100, 180)
    SetChrPos(0x102, 102500, 2200, -300, 0)
    SetChrPos(0x103, 101200, 2200, 1700, 90)
    SetChrPos(0x104, 104400, 2200, 1300, 270)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis021.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis022.itp")
    FadeToBright(1000, 0)
    OP_68(102370, 3300, 1380, 4000)
    OP_6F(0x1)
    OP_0D()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0003F#5P──好了，\x01",
            "开始整理情况吧。\x02\x03",

            "#0001F关于这次一连串的魔兽灾害……\x01",
            "在警备队最初的调查报告中，\x01",
            "存在数个不明之处。\x02\x03",

            "经过我们的调查，已经查清了\x01",
            "其中几处……\x02\x03",

            "#0003F但是，对于某个本应明了的信息，\x01",
            "我们目前却还是一无所知。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0105F#12P本应明了的信息……？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#0305F#11P那是什么？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K本应明了的信息是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【魔兽的真面目】\x01",      # 0
            "【魔兽的住处】\x01",        # 1
            "【魔兽的目的】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_128E"),
        (1, "loc_1386"),
        (2, "loc_1488"),
        (SWITCH_DEFAULT, "loc_14F7"),
    )


    label("loc_128E")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0049
    ChrTalk(
        0x101,
        (
            "#0006F#5P魔兽的真面目……\x01",
            "虽然想这么说。\x02\x03",

            "#0008F但对方如此神出鬼没，\x01",
            "也很难查明其真面目吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        (
            "#0206F#6P嗯，要是知道的话，\x01",
            "也就不用这么辛苦了……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#0003F#5P……是啊。\x01",
            "勉强要说的话……\x02\x03",

            "#0001F我想，应该是魔兽的目的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F7")

    label("loc_1386")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0052
    ChrTalk(
        0x101,
        (
            "#0006F#5P魔兽的住处……\x01",
            "虽然想这么说。\x02\x03",

            "#0008F可是警备队去搜山都没有找到，\x01",
            "我们就更不可能找到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0206F#6P嗯，凭我们的人数，\x01",
            "也无法进行大规模的搜山……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0003F#5P……是啊。\x01",
            "勉强要说的话……\x02\x03",

            "#0001F我想，应该是魔兽的目的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F7")

    label("loc_1488")

    OP_2C(0x3F, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0055
    ChrTalk(
        0x101,
        (
            "#0003F#5P没错，在一连串的调查中，\x01",
            "本应明了的信息……\x02\x03",

            "#0001F我想，应该就是魔兽的目的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F7")

    label("loc_14F7")


    #C0056
    ChrTalk(
        0x104,
        (
            "#0303F#11P如此说来……\x02\x03",

            "#0301F从医院的受灾情况看来，\x01",
            "它们似乎也不像是因为饥饿\x01",
            "才袭击各地的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0108F#12P如阿尔摩利卡村的村长所说，\x01",
            "也有可能是传说中的『神狼』\x01",
            "在警告人类……\x02\x03",

            "#0101F但是，实际上袭击各地的\x01",
            "很可能是黑色的狼群呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0203F#6P是的……我也这样想。\x02\x03",

            "#0201F这样一来，的确就\x01",
            "无法理解其目的了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0003F#5P嗯……\x02\x03",

            "#0001F然而，如果现在就判断为只是黑色狼群的\x01",
            "一时心血来潮，也还为时过早。\x02\x03",

            "从医院的事件也可以看得出来，\x01",
            "它们选择了非常巧妙的路线，\x01",
            "从病房楼的楼顶上入侵。\x02\x03",

            "#0003F而且没有对受害者进行\x01",
            "过大的伤害，就直接离去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#0103F#12P的确……\x02\x03",

            "#0101F如果只是一时的心血来潮，\x01",
            "计划得未免也太周密了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#0303F#11P本应一目了然的『目的』，\x01",
            "却让人完全摸不着头脑……\x02\x03",

            "#0300F也就是说，\x01",
            "这其中有什么含义吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000F#5P正是如此。\x02\x03",

            "#0003F这种情况下，\x01",
            "人往往会被一个『框架』\x01",
            "限制住。\x02\x03",

            "黑色狼群对各地发动了袭击……\x02\x03",

            "#0001F为了看清它们那个符合逻辑的目的，\x01",
            "我们应该思考另一个『框架』。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        "#0208F#6P另一个『框架』吗……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0064
    ChrTalk(
        0x101,
        (
            "#0000F#5P不用思考得太复杂。\x02\x03",

            "#0004F大体来说，所谓的犯罪事件\x01",
            "无非也就包括『犯人』、『目的』、\x01",
            "『手段』和『结果』这几个要素……\x02\x03",

            "#0000F不妨假设我们之前对其中几项\x01",
            "要素的推测出现了偏差，如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        "#0205F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#0101F#12P等、等一下，\x01",
            "我来简单总结一下试试。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "犯人　＝　黑色狼群\x01",
            "目的　＝　？\x01",
            "手段　＝　狼的身体能力\x01",
            "结果　＝　各地的受灾\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    #C0068
    ChrTalk(
        0x101,
        "#0000F#5P嗯，就是这样吧。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0301F#11P然后呢……\x01",
            "这有什么偏差？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0001F#5P嗯……\x01",
            "换个思路怎么样？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 5)

    label("loc_1AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E40")
    SetScenarioFlags(0x0, 5)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K相当于『犯人』的是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "黑色狼群\x01",          # 0
            "？\x01",                # 1
            "狼的身体能力\x01",      # 2
            "各地的受灾\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4F")
    ClearScenarioFlags(0x0, 5)

    label("loc_1B4F")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K相当于『目的』的是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "黑色狼群\x01",          # 0
            "？\x01",                # 1
            "狼的身体能力\x01",      # 2
            "各地的受灾\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC4")
    ClearScenarioFlags(0x0, 5)

    label("loc_1BC4")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K相当于『手段』的是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "黑色狼群\x01",          # 0
            "？\x01",                # 1
            "狼的身体能力\x01",      # 2
            "各地的受灾\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C39")
    ClearScenarioFlags(0x0, 5)

    label("loc_1C39")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K相当于『结果』的是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "黑色狼群\x01",          # 0
            "？\x01",                # 1
            "狼的身体能力\x01",      # 2
            "各地的受灾\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAE")
    ClearScenarioFlags(0x0, 5)

    label("loc_1CAE")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D5C")
    OP_63(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0075
    ChrTalk(
        0x101,
        (
            "#0006F#5P（嗯～……\x01",
            "  果然说不通。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)

    #C0076
    ChrTalk(
        0x101,
        "#0005F#5P（莫非是这样……？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1DB4")

    label("loc_1D5C")


    #C0077
    ChrTalk(
        0x101,
        (
            "#0003F#5P（不……\x01",
            "  这样说不通。）\x02\x03",

            "#0001F（再重新选择一次看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DB4")

    Jump("loc_1E3B")

    label("loc_1DB9")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1DC9"),
        (SWITCH_DEFAULT, "loc_1E01"),
    )


    label("loc_1DC9")

    OP_2C(0x3F, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0078
    ChrTalk(
        0x101,
        "#0000F#5P（不错……就是这样。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E3B")

    label("loc_1E01")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0079
    ChrTalk(
        0x101,
        "#0003F#5P（……大概就是这样吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E3B")

    label("loc_1E3B")

    Jump("loc_1AC2")

    label("loc_1E40")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "犯人　＝　？\x01",
            "目的　＝　狼的身体能力\x01",
            "手段　＝　黑色狼群\x01",
            "结果　＝　各地的受灾\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x102,
        "#0105F#12P这是……！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#0201F#6P假如情况真是如此……\x02\x03",

            "犯人另有其人，黑色狼群是手段，\x01",
            "而它们的身体能力则是目的……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0305F#11P喂喂……\x01",
            "视角完全改变了啊！\x02\x03",

            "#0301F这么说，在狼群的背后，\x01",
            "很可能有人类在操纵吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#0003F#5P如果可以操纵魔兽的话，\x01",
            "这样想反而更自然吧。\x02\x03",

            "#0008F关键问题是，带领大量狼形魔兽\x01",
            "以及控制它们的方法……\x02\x03",

            "#0000F其中，关于控制它们的方法，\x01",
            "我想可以从某个人物的证言中推测出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#0101F#12P某个人物的证言……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0086
    ChrTalk(
        0x104,
        "#0300F#11P……原来如此，是那句话吧？\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0004F#5P兰迪果然注意到了啊。\x02\x03",

            "#0000F嗯，那位证人就是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K证人的名字是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【哈罗德·海瓦斯】\x01",      # 0
            "【实习医生利顿】\x01",        # 1
            "【滴·马克莱因】\x01",        # 2
            "【诺艾尔·希卡】\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2203"),
        (1, "loc_229D"),
        (2, "loc_2337"),
        (3, "loc_2392"),
        (SWITCH_DEFAULT, "loc_242C"),
    )


    label("loc_2203")


    #C0089
    ChrTalk(
        0x104,
        (
            "#0303F#11P不对……搞错了吧？\x02\x03",

            "#0301F是那个眼睛失明，\x01",
            "叫小滴的孩子才对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0011F#5P啊……没错。\x02\x03",

            "#0006F为我们提供具体证言的\x01",
            "就是那个孩子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242C")

    label("loc_229D")


    #C0091
    ChrTalk(
        0x104,
        (
            "#0303F#11P不对……搞错了吧？\x02\x03",

            "#0301F是那个眼睛失明，\x01",
            "叫小滴的孩子才对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0011F#5P啊……没错。\x02\x03",

            "#0006F为我们提供具体证言的\x01",
            "就是那个孩子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242C")

    label("loc_2337")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0093
    ChrTalk(
        0x101,
        (
            "#0003F#5P滴·马克莱因……\x02\x03",

            "#0001F那个游击士亚里欧斯的\x01",
            "女儿的证言。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242C")

    label("loc_2392")


    #C0094
    ChrTalk(
        0x104,
        (
            "#0303F#11P不对……搞错了吧？\x02\x03",

            "#0301F是那个眼睛失明，\x01",
            "叫小滴的孩子才对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#0011F#5P啊……没错。\x02\x03",

            "#0006F为我们提供具体证言的\x01",
            "就是那个孩子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242C")

    label("loc_242C")


    #C0096
    ChrTalk(
        0x103,
        "#0205F#6P小滴的证言……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(40, 120, -1, -1)
    SetChrName("滴的证言")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "那个，我有点担心，\x01",
            "就打开了那边的窗子\x01",
            "仔细听了听……\x02\x03",

            "但是没有再听到惨叫声，\x01",
            "反而听到了『呼呼呼』\x01",
            "这样的喘气声……\x02\x03",

            "过了一会，又听到『咚咚』声，\x01",
            "好像是什么东西在蹦跳的声音……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetMessageWindowPos(190, 140, -1, -1)
    SetChrName("小滴的证言")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "还、还有……\x02\x03",

            "那个……在刚才说的\x01",
            "那些声音之间……\x02\x03",

            "好像……\x01",
            "还听到了『嘟～』的一声\x01",
            "很刺耳的声音。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis023.itp")

    #C0099
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0105F#12P难、难道说……\x01",
            "就是用那种声音来操纵魔兽的？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#0001F#5P嗯，很有可能。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#0203F#6P……狼和狗这样的动物，\x01",
            "似乎可以听到一些频率特别，\x01",
            "人耳听不到的声音。\x02\x03",

            "#0201F好像在很久以前就有\x01",
            "利用这种原理制作而成的特殊笛子……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#0304F#11P就是所谓的『犬笛』吧。\x02\x03",

            "#0300F直到现在，使用犬笛来操纵\x01",
            "军犬的技术也尚有流传。\x02\x03",

            "#0306F不过，相比正规军来说，\x01",
            "还是猎兵们用得比较多。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#0005F#5P是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#0108F#12P……原来如此，\x01",
            "事件的轮廓似乎清晰了不少呢。\x02\x03",

            "#0101F这样一来，还需要\x01",
            "携带魔兽移动的手段吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0105
    ChrTalk(
        0x102,
        "#0105F#12P莫非是……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_END)), "loc_2E1F")
    OP_2C(0x3F, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x40, 0x1, 0xB)

    #C0106
    ChrTalk(
        0x101,
        (
            "#0004F#5P嗯，大概正如艾莉所想。\x02\x03",

            "#0000F关于这一点，\x01",
            "我想是可以证明的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0107
    ChrTalk(
        0x101,
        (
            "#0000F#5P──缇欧，艾尼格玛的\x01",
            "通讯功能在这个镇上也能使用吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    #C0108
    ChrTalk(
        0x103,
        (
            "#0205F#6P嗯，只要在自治州之内，\x01",
            "应该勉强可以通话……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        "#0305F#11P怎么，你要联络哪里吗？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0110
    ChrTalk(
        0x101,
        "#0000F#5P嗯……是医科大学的接待处。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x10)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 101060, 2000, -560, 180)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x103, 0x2)
    SetChrSubChip(0x104, 0x1)
    Sleep(1000)
    OP_68(102370, 4500, 1380, 0)
    OP_68(102370, 3300, 1380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0111
    ChrTalk(
        0x102,
        (
            "#0101F#5P是……嗯……\x02\x03",

            "#0105F！！\x02\x03",

            "#0103F是这样吗……\x01",
            "嗯，非常感谢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x10)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0112
    ChrTalk(
        0x101,
        "#0001F#5P怎么样？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0113
    ChrTalk(
        0x102,
        (
            "#0106F#11P……正如你所料。\x02\x03",

            "#0101F魔兽在楼顶出现的那天夜里，\x01",
            "『鲁巴彻商会』的搬运车\x01",
            "似乎正巧停在停车场呢。\x02\x03",

            "好像是去高价兜售\x01",
            "医疗设备的。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#0306F#5P这时机未免也太巧了吧。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    #C0115
    ChrTalk(
        0x104,
        (
            "#0301F#11P可是，罗伊德……\x01",
            "你怎么知道他们的搬运车\x01",
            "停在停车场呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    #C0116
    ChrTalk(
        0x103,
        (
            "#0205F#6P也有可能是在深夜把车\x01",
            "开到医院前，直接发动袭击的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0003F#5P不，如果是那样的话，\x01",
            "小滴应该会先听到车子的声音。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)

    #A0118
    AnonymousTalk(
        0x101,
        (
            "#0000F而且，我们一开始\x01",
            "还以为魔兽们\x01",
            "是从草丛那边进去的……\x02\x03",

            "但那边的木箱上\x01",
            "并没有留下魔兽的足迹。\x02\x03",

            "#0003F反之，面向停车场的\x01",
            "栏杆上却有擦痕。\x02\x03",

            "#0001F因此，我觉得从那边\x01",
            "侵入的可能性比较高吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0119
    AnonymousTalk(
        0x102,
        (
            "#0106F原来如此……\x02\x03",

            "#0101F停车场方向的高度比较高，\x01",
            "本以为没法从那边入侵呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(500)

    #A0120
    AnonymousTalk(
        0x104,
        (
            "#0300F不过，如果让它们从搬运车的车顶上出发，\x01",
            "应该就很容易侵入了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0121
    AnonymousTalk(
        0x103,
        "#0206F……准备得还真周到啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 102500, 2200, -300, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Jump("loc_2E84")

    label("loc_2E1F")

    OP_29(0x40, 0x1, 0xC)

    #C0122
    ChrTalk(
        0x101,
        (
            "#0003F#5P嗯……\x01",
            "刚才我们看到的那辆黑色搬运车。\x02\x03",

            "#0001F虽然还不能断定，\x01",
            "但感觉完全符合吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E84")

    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x102)

    #C0123
    ChrTalk(
        0x103,
        "#0203F#6P……各种线索都联系起来了呢。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#0108F#12P嗯，黑手党的目的是\x01",
            "垄断七耀石的采购权……\x02\x03",

            "#0101F不对，那也只是次要目的而已吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0006F#5P嗯，应该没错。\x02\x03",

            "#0008F黑手党现在最倾注心力的事情，\x01",
            "是获得压倒对抗组织『黑月』的\x01",
            "战斗力。\x02\x03",

            "#0001F如果是出于这个原因而\x01",
            "打算将狼群作为战斗力的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#0303F#11P不听指挥，只会发狂的魔兽\x01",
            "是完全不能当作战斗力的……\x02\x03",

            "想确定是否能够完全操控它们，\x01",
            "就需要进行实际测试……\x02\x03",

            "#0301F这就是各地发生灾害\x01",
            "的真相吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#0003F#5P嗯……不会错的。\x02\x03",

            "#0001F再说，警备队刚一撤退，\x01",
            "黑手党的手下就马上来拜访，\x01",
            "这本身就极其不自然吧。\x02\x03",

            "下达撤退命令的警备队司令\x01",
            "似乎与某个很强势的议员存在一定联系……\x02\x03",

            "鲁巴彻多半是通过\x01",
            "那个议员进行事先周旋的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        (
            "#0106F#12P多半……就是这样吧。\x02\x03",

            "#0108F……虽然我早知道他们很腐败，\x01",
            "但真没想到已经到了如此地步……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    #C0129
    ChrTalk(
        0x102,
        (
            "#0101F#12P……那么……\x01",
            "你觉得他们还会继续吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#0006F#5P从魔兽的实战测试这层意义上来说，\x01",
            "行动已经足够了吧。\x02\x03",

            "而且，反过来看的话，既然授意\x01",
            "让警备队撤退，或许也正能说明他们\x01",
            "不打算再让骚乱继续扩大了。\x02\x03",

            "#0001F只是……\x01",
            "看样子，实施此次行动的人\x01",
            "似乎产生了多余的野心。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#0201F#6P就是垄断七耀石的采购权吧……\x02\x03",

            "这么说……\x01",
            "你觉得他们最后还会再行动一次？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0301F#11P从那些家伙的态度看来，\x01",
            "这种可能性似乎很高啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        "#0101F#12P如果真要袭击的话，会在什么时候？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#0003F#5P这个嘛……\x02\x03",

            "#0008F……等到明天，镇长可能\x01",
            "就会去找游击士协会商量了。\x02\x03",

            "#0001F如果要进行最后的威胁，\x01",
            "时间除了今晚以外，应该不作他想。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x102)

    #C0135
    ChrTalk(
        0x104,
        "#0300F#11P──好，那我们就来大干一场吧。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#0201F#6P目标是击退黑色狼群，\x01",
            "并逮捕那些黑手党，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#0103F#12P嗯……\x01",
            "绝对不能袖手旁观呢。\x02\x03",

            "#0101F不过，我们还是先和警备队\x01",
            "那边联络一下比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#0006F#5P……不。\x01",
            "警备队一旦展开行动，那些黑手党\x01",
            "恐怕会通过议员而察觉到。\x02\x03",

            "#0001F就靠我们自己来想办法解决吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x102,
        (
            "#0103F#12P……明白了。\x02\x03",

            "#0101F魔兽要是出现的话，\x01",
            "大概会在深夜之后吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#0203F#6P是的……至今为止的事件\x01",
            "也都是在深夜发生的。\x02\x03",

            "#0200F现在还有时间……\x01",
            "先去做些准备吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000F#5P是啊……\x01",
            "如果装备还有所不足，\x01",
            "就去补充一下吧。\x02\x03",

            "准备好以后，\x01",
            "就在这个房间里等待到深夜吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(32800, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果要在房间里等待到深夜，\x01",
            "请在桌子上出现！标志时\x01",
            "按下○键。  \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
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
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    SetChrPos(0x0, 101300, 2000, 3700, 180)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0x65, 5)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayBGM("ed7513", 0)
    EventEnd(0x5)
    Return()

    # Function_13_F8B end

    SaveToFile()

Try(main)
