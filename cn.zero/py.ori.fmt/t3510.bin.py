from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t3510.bin",                # FileName
        "t3510",                    # MapName
        "t3510",                    # Location
        0x005C,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 92, 0, 4, 0, 5],
    )

    BuildStringList((
        "t3510",                  # 0
        "接待小姐玛尔卡娜",       # 1
        "接待员托马斯",           # 2
        "利卡尔德",               # 3
        "运送员雷古",             # 4
        "运送员罗西",             # 5
        "亚里欧斯",               # 6
        "乘客",                   # 7
        "乘客",                   # 8
        "男孩",                   # 9
        "乘客",                   # 10
        "乘客",                   # 11
        "男孩",                   # 12
        "多诺邦警督",             # 13
        "雷蒙德搜查官",           # 14
        "艾玛搜查官",             # 15
        "安敦",                   # 16
        "利库斯",                 # 17
        "接待员米歇尔",           # 18
        "滴",                     # 19
        "玲",                     # 20
        "亚里欧斯",               # 21
        "游击士斯克特",           # 22
        "游击士温蔡尔",           # 23
        "游击士林",               # 24
        "游击士艾欧莉娅",         # 25
        "蔡特",                   # 26
        "琪雅",                   # 27
        "卡片",                   # 28
        "玛夏",                   # 29
    ))

    AddCharChip((
        "chr/ch28200.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "chr/ch10500.itc",                   # 03
        "chr/ch22100.itc",                   # 04
        "chr/ch24200.itc",                   # 05
        "chr/ch23800.itc",                   # 06
        "chr/ch20000.itc",                   # 07
        "chr/ch23500.itc",                   # 08
        "chr/ch30300.itc",                   # 09
        "chr/ch30200.itc",                   # 0A
        "chr/ch30500.itc",                   # 0B
        "chr/ch02402.itc",                   # 0C
        "chr/ch37300.itc",                   # 0D
        "chr/ch37400.itc",                   # 0E
    ))

    DeclNpc(-10220,  150,     2849,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-8350,   150,     6730,    135,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6679,    0,       5530,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6630,    0,       -3460,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6110,    0,       -4760,   45,   389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4750,   5179,    12399,   75,   469,  0x0, 0,   12,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(6500,    0,       -10180,  345,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-10500,  5000,    7010,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-10970,  5000,    6079,    270,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1120,   5000,    13970,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-2160,   0,       -2170,   165,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(29,      0,       -8789,   135,  389,  0x0, 0,   6,   0,   0,   2,   0,   18,  255,  0)
    DeclNpc(8850,    0,       -7480,   225,  389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(7630,    0,       -8699,   45,   389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-7539,   5000,    11000,   315,  405,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(8329,    0,       -319,    45,   385,  0x0, 0,   13,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(6500,    0,       -330,    45,   385,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 37,  0.25999999046325684,   7.989999771118164,     0.0,                   36.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -0.04333333298563957,  -3.994999885559082,    -0.0,                  1.0])

    DeclActor(-8690,   0,       2530,    1000,    -10220,  1600,    2850,    0x007E, 0,  6,  0x0000)
    DeclActor(-7210,   0,       5680,    1000,    -8350,   1600,    6730,    0x007E, 0,  8,  0x0000)
    DeclActor(-7590,   0,       -2440,   1200,    -7590,   1500,    -2440,   0x007C, 0,  38, 0x0000)

    ScpFunction((
        "Function_0_564",          # 00, 0
        "Function_1_61C",          # 01, 1
        "Function_2_647",          # 02, 2
        "Function_3_672",          # 03, 3
        "Function_4_673",          # 04, 4
        "Function_5_73E",          # 05, 5
        "Function_6_7F0",          # 06, 6
        "Function_7_7F4",          # 07, 7
        "Function_8_B9A",          # 08, 8
        "Function_9_B9E",          # 09, 9
        "Function_10_ED7",         # 0A, 10
        "Function_11_1380",        # 0B, 11
        "Function_12_142C",        # 0C, 12
        "Function_13_14E0",        # 0D, 13
        "Function_14_1554",        # 0E, 14
        "Function_15_15A7",        # 0F, 15
        "Function_16_15D7",        # 10, 16
        "Function_17_1637",        # 11, 17
        "Function_18_1685",        # 12, 18
        "Function_19_16BB",        # 13, 19
        "Function_20_17D7",        # 14, 20
        "Function_21_180B",        # 15, 21
        "Function_22_1892",        # 16, 22
        "Function_23_1A2D",        # 17, 23
        "Function_24_20DA",        # 18, 24
        "Function_25_2172",        # 19, 25
        "Function_26_274A",        # 1A, 26
        "Function_27_29E2",        # 1B, 27
        "Function_28_2C48",        # 1C, 28
        "Function_29_2F62",        # 1D, 29
        "Function_30_3185",        # 1E, 30
        "Function_31_389F",        # 1F, 31
        "Function_32_38DC",        # 20, 32
        "Function_33_429E",        # 21, 33
        "Function_34_42B3",        # 22, 34
        "Function_35_42C8",        # 23, 35
        "Function_36_42F1",        # 24, 36
        "Function_37_431A",        # 25, 37
        "Function_38_4387",        # 26, 38
    ))


    def Function_0_564(): pass

    label("Function_0_564")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5A4"),
        (1, "loc_5B0"),
        (2, "loc_5BC"),
        (3, "loc_5C8"),
        (4, "loc_5D4"),
        (5, "loc_5E0"),
        (6, "loc_5EC"),
        (SWITCH_DEFAULT, "loc_5F8"),
    )


    label("loc_5A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_61B")

    Return()

    # Function_0_564 end

    def Function_1_61C(): pass

    label("Function_1_61C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_646")
    OP_94(0xFE, 0xFFFFF704, 0xFFFFF876, 0xDB6, 0xFFFFE1C4, 0x3E8)
    Sleep(300)
    Jump("Function_1_61C")

    label("loc_646")

    Return()

    # Function_1_61C end

    def Function_2_647(): pass

    label("Function_2_647")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_671")
    OP_94(0xFE, 0x406, 0xFFFFE192, 0xFFFFFBFA, 0xFFFFD9C2, 0x3E8)
    Sleep(100)
    Jump("Function_2_647")

    label("loc_671")

    Return()

    # Function_2_647 end

    def Function_3_672(): pass

    label("Function_3_672")

    Return()

    # Function_3_672 end

    def Function_4_673(): pass

    label("Function_4_673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_682")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_69F")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_707")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CB")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_707")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_707")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0xF, 0x10)
    BeginChrThread(0x13, 0, 0, 2)

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_71F")
    Jump("loc_73D")

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_735")
    SetMapFlags(0x10000000)
    Event(0, 29)
    Jump("loc_73D")

    label("loc_735")

    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_73D")

    Return()

    # Function_4_673 end

    def Function_5_73E(): pass

    label("Function_5_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_750")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_750")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_782")
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7AB")

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_79C")
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    Jump("loc_7AB")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7AB")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7C2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7C2")

    label("loc_7C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_END)), "loc_7D3")
    OP_24(0x86)
    Jump("loc_7EF")

    label("loc_7D3")

    SoundDistance(0x86, 0x16D0, 0x0, 0x259E, 0x1388, 0x30D40, 0x64, 0x0)

    label("loc_7EF")

    Return()

    # Function_5_73E end

    def Function_6_7F0(): pass

    label("Function_6_7F0")

    Call(0, 7)
    Return()

    # Function_6_7F0 end

    def Function_7_7F4(): pass

    label("Function_7_7F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_816")
    Call(0, 32)
    Return()

    label("loc_816")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_932")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CC")

    #C0001
    ChrTalk(
        0x8,
        (
            "已经拜托警察将\x01",
            "空港内的所有角落都仔细搜索过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "据那些搜查官判断，那个炸弹恐吓信息\x01",
            "应该是假的……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "……总之，\x01",
            "必须快点恢复\x01",
            "飞行船的运行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_92D")

    label("loc_8CC")


    #C0004
    ChrTalk(
        0x8,
        (
            "虽然不知道对方是出于何种目的\x01",
            "而发出虚假炸弹恐吓的……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "现在必须\x01",
            "快点恢复\x01",
            "飞行船的运行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92D")

    Jump("loc_B96")

    label("loc_932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9A0")

    #C0006
    ChrTalk(
        0x8,
        (
            "飞往利贝尔的定期航班\x01",
            "『卡拉布利亚号』即将起航。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "请各位乘客\x01",
            "尽快登上飞船。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F5")

    label("loc_9A0")


    #C0008
    ChrTalk(
        0x8,
        (
            "虽然不是很清楚……\x01",
            "但卡拉小姐好像\x01",
            "并没有光临本空港啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "期待您的\x01",
            "再次光临。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F5")

    Jump("loc_B96")

    label("loc_9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF4")

    #C0010
    ChrTalk(
        0x8,
        (
            "从这里出发的飞行船，\x01",
            "主要飞往北方的雷米菲利亚公国，\x01",
            "和南方的利贝尔王国。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "虽然也有飞往埃雷波尼亚帝国和\x01",
            "卡尔瓦德共和国的飞行船，\x01",
            "但和其它航班相比，乘客会比较少。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "看来，对于平民而言，\x01",
            "铁路还是主流的交通工具吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B96")

    label("loc_AF4")


    #C0013
    ChrTalk(
        0x8,
        (
            "从这里出发的飞行船，\x01",
            "主要飞往北方的雷米菲利亚公国，\x01",
            "和南方的利贝尔王国。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "虽然也有飞往帝国和共和国的航班，\x01",
            "但要前往这两个地方，\x01",
            "铁路还是主流的交通工具。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B96")

    TalkEnd(0x8)
    Return()

    # Function_7_7F4 end

    def Function_8_B9A(): pass

    label("Function_8_B9A")

    Call(0, 9)
    Return()

    # Function_8_B9A end

    def Function_9_B9E(): pass

    label("Function_9_B9E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_CD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6A")

    #C0015
    ChrTalk(
        0x9,
        (
            "当听说有人发出炸弹恐吓时，\x01",
            "我的后背直冒冷汗。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "虽然最严重的情况并没有出现，\x01",
            "但今日的航班\x01",
            "已经完全停止运行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "本次事件给乘客们带来了麻烦，\x01",
            "我们实在深感歉意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CCE")

    label("loc_C6A")


    #C0018
    ChrTalk(
        0x9,
        (
            "本日航班全部停止运行，\x01",
            "这使许多乘客的\x01",
            "行程安排都大幅度延迟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        "我对犯人实在是恨之入骨啊。\x02",
    )

    CloseMessageWindow()

    label("loc_CCE")

    Jump("loc_ED3")

    label("loc_CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D53")

    #C0020
    ChrTalk(
        0x9,
        (
            "这里是办理出入境手续\x01",
            "以及托运行李的窗口。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "我们会负责将行李\x01",
            "安全运至目的地，\x01",
            "所以请您放心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DA9")

    label("loc_D53")


    #C0022
    ChrTalk(
        0x9,
        (
            "托运行李的手续\x01",
            "在本窗口办理。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "随身携带大件行李的乘客，\x01",
            "请自由使用本项服务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA9")

    Jump("loc_ED3")

    label("loc_DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5B")

    #C0024
    ChrTalk(
        0x9,
        (
            "有这么多的游客，\x01",
            "办理入境手续实在很辛苦。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "好想抛开这一切，\x01",
            "去尽情享受\x01",
            "纪念庆典啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x9,
        (
            "……这当然是不可能的啦，\x01",
            "必须要对工作尽职尽责。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_ED3")

    label("loc_E5B")


    #C0027
    ChrTalk(
        0x9,
        (
            "这份工作实在太忙了，\x01",
            "所以产生想要逃避的念头\x01",
            "也是人之常情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "……不，还是不能逃避。\x01",
            "必须对工作\x01",
            "尽职尽责才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED3")

    TalkEnd(0x9)
    Return()

    # Function_9_B9E end

    def Function_10_ED7(): pass

    label("Function_10_ED7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF9")
    Call(0, 30)
    Return()

    label("loc_EF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_F79")

    #C0029
    ChrTalk(
        0xFE,
        (
            "我真是吓了一跳啊。\x01",
            "这张卡片神不知鬼不觉地就出现了……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "刚才运输公司的人\x01",
            "把行李交给我时\x01",
            "应该还没有的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137C")

    label("loc_F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_10D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1052")

    #C0031
    ChrTalk(
        0xFE,
        (
            "话说，警察也很不容易啊。\x01",
            "他们好像是暂时将重要任务搁在一边，\x01",
            "然后来这里进行调查的。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……对他们来说，\x01",
            "这次不是等于白跑一趟吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "算啦，至少确认了一切安全，\x01",
            "仅是如此就已经不错了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_10CB")

    label("loc_1052")


    #C0034
    ChrTalk(
        0xFE,
        (
            "我也和警察一起搜遍了\x01",
            "空港的每一个角落，\x01",
            "已经累得不行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……算啦，至少确认了一切安全，\x01",
            "仅是如此就已经不错了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CB")

    Jump("loc_137C")

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_11F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A9")

    #C0036
    ChrTalk(
        0xFE,
        (
            "生活富裕的乘客\x01",
            "有时还会带着宠物去旅游。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "就是把宠物放在专门的笼子里，\x01",
            "然后当成行李来托运……\x01",
            "不过那些宠物们在到达之后就开始又吼又叫。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "虽然并不是反对，\x01",
            "但我个人还是不喜欢这样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_11EF")

    label("loc_11A9")


    #C0039
    ChrTalk(
        0xFE,
        (
            "虽然宠物和主人\x01",
            "都没有过错……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "但我个人还是不喜欢\x01",
            "托运宠物。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EF")

    Jump("loc_137C")

    label("loc_11F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_137C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CF")

    #C0041
    ChrTalk(
        0xFE,
        (
            "现在来了一家\x01",
            "新开的运输公司，叫『卡普亚特急便』哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "听说这家公司以前好像是做黑道生意的，\x01",
            "在不久之前刚转业为运输公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "虽然经理一脸凶相，\x01",
            "说话也很粗鲁，\x01",
            "但公司的人都挺好相处的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_137C")

    label("loc_12CF")


    #C0044
    ChrTalk(
        0xFE,
        (
            "话说，他们所驾驶的\x01",
            "飞行船『山猫号』\x01",
            "性能好像很强大哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "听他们说，\x01",
            "那飞船的速度似乎不逊色于\x01",
            "高速巡洋船『埃尔赛尤』哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "不过，那种事再怎么说\x01",
            "我也不会相信的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137C")

    TalkEnd(0xFE)
    Return()

    # Function_10_ED7 end

    def Function_11_1380(): pass

    label("Function_11_1380")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F1")

    #C0047
    ChrTalk(
        0xFE,
        "喂，这个拜托你了！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "空港外面有家叫莱姆斯运输的\x01",
            "同城运输公司，\x01",
            "快去把这个交给他们！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1428")

    label("loc_13F1")


    #C0049
    ChrTalk(
        0xFE,
        "喂，快去！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "不快一点的话，\x01",
            "会被大小姐教训的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1428")

    TalkEnd(0xFE)
    Return()

    # Function_11_1380 end

    def Function_12_142C(): pass

    label("Function_12_142C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_147A")

    #C0051
    ChrTalk(
        0xFE,
        "是是，知道啦。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "真是，总是把麻烦的工作\x01",
            "推给我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_14DC")

    label("loc_147A")


    #C0053
    ChrTalk(
        0xFE,
        (
            "对了，那两个人好像也到\x01",
            "克洛斯贝尔来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "要是工作不忙的话，\x01",
            "大小姐应该会想见见他们吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DC")

    TalkEnd(0xFE)
    Return()

    # Function_12_142C end

    def Function_13_14E0(): pass

    label("Function_13_14E0")

    TalkBegin(0xFE)

    #C0055
    ChrTalk(
        0xFE,
        (
            "那些人，\x01",
            "似乎是运输公司的员工……\x01",
            "但看起来不大像啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "……算了，不关我的事，\x01",
            "粗犷的感觉也挺帅气的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_14E0 end

    def Function_14_1554(): pass

    label("Function_14_1554")

    TalkBegin(0xFE)

    #C0057
    ChrTalk(
        0xFE,
        (
            "哈哈，快看远处，\x01",
            "飞行船快起飞了哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x10,
        (
            "哇～好厉害好厉害！\x01",
            "好帅啊～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1554 end

    def Function_15_15A7(): pass

    label("Function_15_15A7")

    TalkBegin(0xFE)

    #C0059
    ChrTalk(
        0xFE,
        (
            "我马上就能乘坐飞行船了～\x01",
            "好期待啊～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_15A7 end

    def Function_16_15D7(): pass

    label("Function_16_15D7")

    TalkBegin(0xFE)

    #C0060
    ChrTalk(
        0xFE,
        (
            "空中旅行也\x01",
            "变得很舒适了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "天空是女神的居所，\x01",
            "在旅程中或许会\x01",
            "得到某种祝福呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_15D7 end

    def Function_17_1637(): pass

    label("Function_17_1637")

    TalkBegin(0xFE)

    #C0062
    ChrTalk(
        0xFE,
        "我说，动作快点！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "要是不赶快办好搭乘手续，\x01",
            "就会错过飞行船了！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1637 end

    def Function_18_1685(): pass

    label("Function_18_1685")

    TalkBegin(0xFE)

    #C0064
    ChrTalk(
        0xFE,
        (
            "嘁，我还想在克洛斯贝尔\x01",
            "再多玩一段时间啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1685 end

    def Function_19_16BB(): pass

    label("Function_19_16BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179B")

    #C0065
    ChrTalk(
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "总之，空港情况没有异常。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，虽然不知道是谁干的好事，\x01",
            "不过真是给人添了很大麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0000F……各位辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "噢，真的很累啊。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "真是的，到底是哪个混蛋做的啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_17D3")

    label("loc_179B")


    #C0071
    ChrTalk(
        0xFE,
        "接下来就交给一科吧。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "现在得回总部写报告书了。\x02",
    )

    CloseMessageWindow()

    label("loc_17D3")

    TalkEnd(0xFE)
    Return()

    # Function_19_16BB end

    def Function_20_17D7(): pass

    label("Function_20_17D7")

    TalkBegin(0xFE)

    #C0073
    ChrTalk(
        0xFE,
        (
            "又得写报告书了，\x01",
            "饶了我吧，真不想写啊～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_17D7 end

    def Function_21_180B(): pass

    label("Function_21_180B")

    TalkBegin(0xFE)
    OP_64(0xFE)

    #C0074
    ChrTalk(
        0xFE,
        "是、是……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "我知道了，我们会试着查明\x01",
            "炸弹恐吓信的寄出地。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "达德利长官，你们那边也请多加小心。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Return()

    # Function_21_180B end

    def Function_22_1892(): pass

    label("Function_22_1892")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1926")
    Jump("loc_1970")

    label("loc_1926")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1946")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1970")

    label("loc_1946")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1966")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1970")

    label("loc_1966")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1970")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B0")
    Call(0, 26)
    Jump("loc_1A25")

    label("loc_19B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19C6")
    Call(0, 27)
    Jump("loc_1A25")

    label("loc_19C6")


    #C0077
    ChrTalk(
        0xFE,
        (
            "#1403F……纪念庆典的最后一天\x01",
            "容易发生一些出人意料的事故。\x02\x03",

            "#1400F不到最后绝不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A25")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_1892 end

    def Function_23_1A2D(): pass

    label("Function_23_1A2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1ABE")

    #C0078
    ChrTalk(
        0xFE,
        (
            "在利贝尔被残酷地甩了，\x01",
            "在克洛斯贝尔被温柔地甩了……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "我说，利库斯，\x01",
            "我从今以后\x01",
            "到底该怎么办啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D97")

    label("loc_1ABE")


    #C0080
    ChrTalk(
        0x101,
        (
            "#0000F啊……\x01",
            "安敦先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……是你们啊。\x01",
            "昨天我等了你们一天……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        "#0200F（……完全忘记了。）\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0000F那个……\x01",
            "真是十分抱歉。\x02\x03",

            "因为昨天有一个调查任务，\x01",
            "实在是脱不开身……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "……结果，昨天我自己\x01",
            "去见芙兰小姐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "本来想试着约她\x01",
            "一起吃个饭的……\x01",
            "但还是被拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "她……已经有\x01",
            "喜欢的人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0000F这、这样啊……\x01",
            "那真是令人遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        (
            "#0300F（……小芙兰\x01",
            "  喜欢的人是谁啊？\x01",
            "  让人有点在意啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "没关系，你们不用管我，\x01",
            "我已经习惯这种事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "看到她说到喜欢的人时\x01",
            "那灿烂的笑脸……\x01",
            "我就彻底死心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "我现在就要回利贝尔，\x01",
            "找寻一个新的自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#0100F（嗯……\x01",
            "  没有完成答应人家的事，\x01",
            "  果然不太好啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0000F（对啊……）\x02\x03",

            "（不过，反正我们也帮不上什么忙了，\x01",
            "  就让他一个人静一静吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_1D97")

    Jump("loc_20D6")

    label("loc_1D9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E1F")

    #C0094
    ChrTalk(
        0xFE,
        (
            "在利贝尔被残酷地甩了，\x01",
            "在克洛斯贝尔被温柔地甩了……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "喂，利库斯，\x01",
            "我从今以后\x01",
            "到底该怎么办啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEE")

    label("loc_1E1F")


    #C0096
    ChrTalk(
        0xFE,
        (
            "……啊，是你们啊，\x01",
            "昨天真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#0000F安敦先生……\x01",
            "你这就要回国了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "嗯……反正也被\x01",
            "芙兰小姐拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x103,
        "#0200F……真是令人同情。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "没关系，你们不用管我，\x01",
            "我已经习惯这种事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "看到她说到喜欢的人时\x01",
            "那灿烂的笑脸……\x01",
            "我就彻底死心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0000F（其实芙兰『喜欢的人』是上士，\x01",
            "  要不要把这件事告诉他啊……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#0300F（算了吧。\x01",
            "  要是说出来，搞不好\x01",
            "  事情会变得很麻烦的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#0100F（也是，不说比较好吧。\x01",
            "  虽然他有点可怜……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_1FEE")

    Jump("loc_20D6")

    label("loc_1FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_206A")

    #C0105
    ChrTalk(
        0xFE,
        (
            "在利贝尔被残酷地甩了，\x01",
            "在克洛斯贝尔被温柔地甩了……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "喂，利库斯，\x01",
            "我从今以后\x01",
            "到底该怎么办啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D6")

    label("loc_206A")


    #C0107
    ChrTalk(
        0xFE,
        (
            "好不容易找到了……\x01",
            "帮我找回钱包的那个女孩，\x01",
            "结果还是被拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "她说她已经有了\x01",
            "喜欢的人了啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_20D6")

    TalkEnd(0xFE)
    Return()

    # Function_23_1A2D end

    def Function_24_20DA(): pass

    label("Function_24_20DA")

    TalkBegin(0xFE)

    #C0109
    ChrTalk(
        0xFE,
        (
            "通过这次失恋，是会获得成长，\x01",
            "还是陷入无尽的悲伤不可自拔……\x01",
            "这都取决于安敦自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "我作为朋友，今后所能做的\x01",
            "也就只有在一旁默默守护而已。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_20DA end

    def Function_25_2172(): pass

    label("Function_25_2172")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    LoadChrToIndex("chr/ch09100.itc", 0x20)
    LoadChrToIndex("chr/ch02400.itc", 0x21)
    LoadChrToIndex("chr/ch08200.itc", 0x22)
    LoadChrToIndex("chr/ch02702.itc", 0x23)
    LoadChrToIndex("chr/ch27200.itc", 0x24)
    LoadChrToIndex("chr/ch27300.itc", 0x25)
    LoadChrToIndex("chr/ch32100.itc", 0x26)
    LoadChrToIndex("chr/ch32000.itc", 0x27)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_68(0, 900, 1000, 0)
    MoveCamera(310, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 600, 0, -400, 0)
    SetChrPos(0x102, 1900, 0, -600, 0)
    SetChrPos(0x104, 200, 0, -1500, 0)
    SetChrPos(0x103, 1500, 0, -1700, 0)
    SetChrPos(0x107, -800, 0, 2700, 180)
    SetChrPos(0x108, 800, 0, 2700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 0, 0, 3000, 180)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2200, 0, -1100, 45)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrPos(0x19, -1100, 0, 300, 45)
    SetChrChipByIndex(0x1C, 0x21)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -2300, 0, 0, 45)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrPos(0x22, -200, 0, -400, 0)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, 2700, 0, 600, 315)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -300, 0, -2800, 0)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 1000, 0, -3100, 0)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -3200, 0, -2200, 45)
    SetChrChipByIndex(0x20, 0x26)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -2200, 0, -2200, 45)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W──艾丝蒂尔和约修亚\x01",
            "决定和玲一同返回利贝尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(320, 27, 0, 4000)
    SetCameraDistance(19000, 4000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    FadeToDark(300, 0, 100)
    OP_0D()

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W虽然游击士协会的人手\x01",
            "减少了，但经过政治改革之后，\x01",
            "警察系统的体制想必也会得到改善吧。\x02\x03",

            "今后，警察也许会与协会进一步合作，\x01",
            "以减轻他们的负担。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 700, 3000, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x3, 0xFF9B9B9B, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    Sleep(500)
    SetMessageWindowPos(50, -1, -1, -1)

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W──分别之际，玲再次\x01",
            "提起了那些令我们难以释怀的事情。\x02\x03",

            "五百年前的真相和\x01",
            "琪雅出现在竞拍会的原因……\x02\x03",

            "以及我的哥哥，盖伊·班宁斯\x01",
            "是被何人所杀……\x02\x03",

            "即便是似乎可以看穿一切的她，\x01",
            "也对那些真相不甚明了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W不过，解开那些谜团，\x01",
            "是我──不，是我们的职责。\x02\x03",

            "约定他日再见后，\x01",
            "我们彼此互道珍重。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    RemoveParty(0x6, 0x0)
    RemoveParty(0x7, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5E, 0)
    NewScene("e3500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_2172 end

    def Function_26_274A(): pass

    label("Function_26_274A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4490, 6400, 11460, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27290, 0)
    SetChrPos(0x101, -4250, 5000, 10550, 0)
    SetChrPos(0x102, -5000, 5000, 10200, 0)
    SetChrPos(0x103, -3100, 5000, 10300, 315)
    SetChrPos(0x104, -4500, 5000, 8900, 0)
    SetChrSubChip(0xD, 0x2)
    OP_0D()

    #C0115
    ChrTalk(
        0xD,
        (
            "#11P#1405F哦，真难得，\x01",
            "竟然会在这种地方遇见你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#6P#0105F亚里欧斯先生……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#0000F您、您好……\x01",
            "昨天承蒙您照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        "#6P#0300F又要去出差了吗？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xD,
        (
            "#11P#1403F是啊，去雷米菲利亚。\x02\x03",

            "#1405F看你们的样子，好像\x01",
            "并不是要乘坐飞行船吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#6P#0012F嗯，是的，有些特殊情况……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#12P#0206F我们正在陪一个人\x01",
            "玩恶趣味的猜谜游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xD,
        (
            "#11P#1404F呵……这样啊。\x02\x03",

            "#1402F今天就是纪念庆典的最后一天了。\x01",
            "不到最后，你们可不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#6P#0012F知、知道了。\x01",
            "（要混入竞拍会的事情\x01",
            "  果然不能说啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 5000, 10550, 0)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0xB3, 6)
    EventEnd(0x5)
    Return()

    # Function_26_274A end

    def Function_27_29E2(): pass

    label("Function_27_29E2")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4490, 6400, 11460, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27290, 0)
    SetChrPos(0x101, -4250, 5000, 10550, 0)
    SetChrPos(0x102, -5000, 5000, 10200, 0)
    SetChrPos(0x103, -3100, 5000, 10300, 315)
    SetChrPos(0x104, -4500, 5000, 8900, 0)
    SetChrSubChip(0xD, 0x2)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    Sleep(500)

    #C0124
    ChrTalk(
        0x102,
        (
            "#6P#0108F那个……亚里欧斯先生。\x02\x03",

            "#0101F您不去\x01",
            "看看小滴吗？\x02\x03",

            "在纪念庆典期间，您好像\x01",
            "也没怎么去看过她……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xD,
        (
            "#11P#1403F……说到我痛处了啊。\x02\x03",

            "#1402F虽然我一直在努力，\x01",
            "争取一星期至少能去看她一次……\x02\x03",

            "#1404F但最近反倒是\x01",
            "艾丝蒂尔他们\x01",
            "去陪那孩子的时间比较多。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#6P#0106F……真不好意思。\x01",
            "是我们多管闲事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "#11P#1402F……没那回事，该说不好意思的是我。\x01",
            "还让你们担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#6P#0001F（艾莉……\x01",
            "  是不是想起了她父母的事呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 5000, 10550, 0)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0xB4, 2)
    EventEnd(0x5)
    Return()

    # Function_27_29E2 end

    def Function_28_2C48(): pass

    label("Function_28_2C48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-21960, 1250, 24660, 0)
    MoveCamera(321, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(42870, 0)
    SetChrPos(0x101, -600, 0, -18300, 0)
    SetChrPos(0x102, 750, 0, -20000, 0)
    SetChrPos(0x103, 750, 0, -18300, 0)
    SetChrPos(0x104, -600, 0, -20000, 0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetCameraDistance(49570, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    OP_68(-5130, 1250, 17490, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(60830, 0)
    OP_68(830, 1250, -11780, 8000)
    MoveCamera(315, 27, 0, 8000)
    OP_6E(300, 8000)
    SetCameraDistance(51170, 8000)
    PlaceName2(340, 200, "c_plac32", 0x0, 1500)
    Sleep(3800)

    def lambda_2D5F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2D5F)
    Sleep(50)

    def lambda_2D77():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2D77)
    Sleep(50)

    def lambda_2D8F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2D8F)
    Sleep(50)

    def lambda_2DA7():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2DA7)
    WaitChrThread(0x3, 1)
    Sleep(300)
    Fade(500)
    OP_68(10, 650, -13380, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32259, 0)
    OP_0D()
    Sleep(500)

    #C0129
    ChrTalk(
        0x101,
        "#6P#0001F好了，到空港了。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        (
            "#6P#0203F怪盗Ｂ的谜语『白隼』\x01",
            "是利贝尔王国的国鸟……\x02\x03",

            "#0202F克洛斯贝尔空港有飞往利贝尔的国际定期航班，\x01",
            "如果说到『通向白隼的大门』，\x01",
            "指的应该就是这里了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#6P#0305F之后就是『时间搬离之地』了\x01",
            "……吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#6P#0104F总之，\x01",
            "我们只能仔细寻找线索了。\x02\x03",

            "#0100F先在这附近找找吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -110, 0, -15030, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xD2, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_2C48 end

    def Function_29_2F62(): pass

    label("Function_29_2F62")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-21960, 1250, 24660, 0)
    MoveCamera(321, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(42870, 0)
    SetChrPos(0x101, -600, 0, -18300, 0)
    SetChrPos(0x102, 750, 0, -20000, 0)
    SetChrPos(0x103, 750, 0, -18300, 0)
    SetChrPos(0x104, -600, 0, -20000, 0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetCameraDistance(59570, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    OP_68(-5130, 1250, 17490, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(60830, 0)
    OP_0D()
    OP_68(830, 1250, -11780, 8000)
    MoveCamera(315, 27, 0, 8000)
    OP_6E(300, 8000)
    SetCameraDistance(51170, 8000)
    PlaceName2(340, 200, "c_plac32", 0x0, 1500)
    Sleep(3800)

    def lambda_307A():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_307A)

    def lambda_308F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_308F)

    def lambda_30A4():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_30A4)

    def lambda_30B9():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_30B9)
    WaitChrThread(0x3, 1)
    Sleep(300)
    Fade(500)
    OP_68(10, 850, -13380, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32259, 0)
    OP_0D()

    #C0133
    ChrTalk(
        0x101,
        (
            "#5P#0003F克洛斯贝尔空港……\x01",
            "接待处是在对面吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#12P#0101F我们快点去\x01",
            "问问卡拉小姐的事情吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -110, 0, -15030, 0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xD2, 2)
    EventEnd(0x5)
    Return()

    # Function_29_2F62 end

    def Function_30_3185(): pass

    label("Function_30_3185")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50091.itc", 0x1E)
    OP_4B(0xA, 0xFF)
    OP_68(6620, 860, 4440, 0)
    MoveCamera(319, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32830, 0)
    SetChrPos(0x101, 6000, 10, 3800, 0)
    SetChrPos(0x102, 7200, 10, 2400, 0)
    SetChrPos(0x103, 7200, 10, 3800, 0)
    SetChrPos(0x104, 6000, 10, 2400, 0)
    SetChrPos(0xA, 6680, 0, 5530, 180)
    SetChrPos(0x23, 8580, 600, 8610, 0)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x1E)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    FadeToBright(500, 0)
    OP_0D()

    #C0135
    ChrTalk(
        0xA,
        (
            "#11P啊，你们是来\x01",
            "取行李的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "#11P要取行李的话，\x01",
            "就把托运证给我看下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#5P#0003F（这里是空港\x01",
            "  领取行李的地方吗……\x01",
            "  姑且也问问吧。）\x02\x03",

            "#0000F那个，不好意思。\x01",
            "请问您在这附近\x01",
            "看到过什么卡片吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "#11P卡片……？\x01",
            "指的不是行李的托运证吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "#11P抱歉，好像没看到过。\x01",
            "如果是失物的话，\x01",
            "你们可以去接待处那边问问看。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        "#6P#0300F哈哈，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x103,
        "#6P#0204F那打扰您了。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x23, 0, 0, 31)
    Sleep(2000)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    #C0142
    ChrTalk(
        0x101,
        "#5P#0011F#12A………呃，那是…………\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        "#6P#0111F#12A有点出乎意料呢……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(7130, 1260, 2560, 2000)

    def lambda_34D4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34D4)

    def lambda_34E1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_34E1)

    def lambda_34EE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_34EE)
    OP_95(0x102, 8090, 10, 440, 1200, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Sleep(300)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0144
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "得到了白色信封。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0145
    ChrTalk(
        0x104,
        (
            "#5P#0306F没想到卡片竟然会从这种地方被传送出来。\x02\x03",

            "#0301F怪盗Ｂ那家伙总是喜欢兜这么麻烦的圈子……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        "#6P#0108F我看看，信封里面是……\x02",
    )

    CloseMessageWindow()
    OP_95(0x102, 7200, 10, 2400, 1200, 0x0)

    def lambda_366C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_366C)

    def lambda_3679():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3679)
    Sleep(200)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, 90, -1, 3)
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "象征荣耀的传播者之证\x01",
            "　 １１９２·１１　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #C0148
    ChrTalk(
        0x101,
        "#11P#0006F……还有吗……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        "#5P#0306F只是转瞬即逝的喜悦而已啊……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#12P#0200F『象征荣耀的传播者之证』……\x01",
            "指的是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#6P#0103F信使……传达信息的人员……\x02\x03",

            "#0100F……去问问从事传达信息相关工作的人吧，\x01",
            "或许会得出答案。\x02\x03",

            "#0106F……虽然不知道具体是什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#11P#0000F总之……\x01",
            "先找找线索吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 6780, 10, 3210, 0)
    OP_4C(0xA, 0xFF)
    OP_D5(0x1E)
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x22, 0x1, 0x5)
    SetScenarioFlags(0x0, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_3185 end

    def Function_31_389F(): pass

    label("Function_31_389F")

    OP_96(0x23, 0x212A, 0x258, 0x866, 0x2DA, 0x0)
    OP_96(0x23, 0x2300, 0x258, 0x532, 0x2DA, 0x0)
    OP_96(0x23, 0x260C, 0x258, 0x456, 0x2DA, 0x0)
    Return()

    # Function_31_389F end

    def Function_32_38DC(): pass

    label("Function_32_38DC")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch34500.itc", 0x1E)
    OP_68(-7940, 850, 2230, 0)
    MoveCamera(314, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32180, 0)
    SetChrPos(0x101, -6570, 0, 2270, 266)
    SetChrPos(0x102, -6260, 0, 970, 266)
    SetChrPos(0x103, -4860, 0, 910, 266)
    SetChrPos(0x104, -5170, 0, 2290, 266)
    SetChrPos(0x24, -3120, 0, -6240, 0)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0153
    ChrTalk(
        0x101,
        (
            "#12P#0000F不好意思，可以耽误您一点时间吗？\x01",
            "我们有件很紧急的事想请教您……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        "#5P啊……是什么事呢？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#6P#0100F那个，关于飞往利贝尔的定期航班，\x01",
            "乘客中应该有一个叫\x01",
            "卡拉·坎贝尔的人。\x02\x03",

            "请问她的搭乘手续\x01",
            "已经办理好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "#5P卡拉·坎贝尔小姐吗？\x01",
            "请稍等……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x8)
    Sleep(300)

    #C0157
    ChrTalk(
        0x8,
        (
            "#5P实在不好意思，\x01",
            "乘客中并没有这么一个人……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0158
    ChrTalk(
        0x102,
        "#6P#0105F真、真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        (
            "#12P#0003F真奇怪啊，\x01",
            "她乘坐的应该是这班飞行船啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#12P#0305F飞往利贝尔的航班\x01",
            "就只有这一班吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x103,
        (
            "#12P#0200F嗯，应该还\x01",
            "没有起飞……\x02",
        )
    )

    CloseMessageWindow()

    #N0162
    NpcTalk(
        0x24,
        "声音",
        "#2P那、那个……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_3C62():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C62)

    def lambda_3C6F():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C6F)

    def lambda_3C7C():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C7C)

    def lambda_3C89():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C89)

    def lambda_3C96():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3C96)
    OP_68(-3470, 1250, -3500, 2000)
    Sleep(2000)

    #N0163
    NpcTalk(
        0x24,
        "女仆",
        "#6P呃……\x02",
    )

    CloseMessageWindow()

    #N0164
    NpcTalk(
        0x24,
        "女仆",
        "#6P那个，请问各位是警察吧……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-6070, 1250, -470, 0)
    MoveCamera(299, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30600, 0)
    SetChrPos(0x24, -3960, 0, -3890, 355)
    OP_96(0x24, 0xFFFFECD2, 0x0, 0xFFFFF556, 0x3E8, 0x0)
    OP_0D()

    #C0165
    ChrTalk(
        0x102,
        (
            "#11P#0105F啊，你好像是坎贝尔议员\x01",
            "家的玛夏小姐吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x103,
        (
            "#11P#0200F莫非，就是那个和\x01",
            "大小姐一起离家出走的女仆吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x24,
        "#6P是、是的……\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1700)

    #C0168
    ChrTalk(
        0x24,
        (
            "#6P……小姐……\x01",
            "并不是要去利贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x24,
        (
            "#6P她是想要骗老爷，\x01",
            "所以故意那样说的……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x24,
        (
            "#6P实际上她是准备\x01",
            "去她共和国的\x01",
            "一个朋友家里。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0171
    ChrTalk(
        0x101,
        (
            "#11P#0005F共和国……！？\x01",
            "糟了，难道是通过铁路……！\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x24,
        "#6P快点去的话应该还来得及！\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x24,
        (
            "#6P……不、不、不好意思，\x01",
            "没想到事情会变成这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x24,
        (
            "#6P不过，如果可以的话……\x01",
            "希望各位能把小姐带回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x24,
        (
            "#6P小姐其实\x01",
            "并不想离开克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#11P#0303F是有什么隐情吧。\x02\x03",

            "#0300F好，我们出发吧，\x01",
            "快点把她给带回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#11P#0203F前往共和国的列车……（咔哒咔哒）\x01",
            "即将发车了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#11P#0001F……好，抓紧时间吧！\x02",
    )

    CloseMessageWindow()

    def lambda_407A():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_407A)

    def lambda_4087():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4087)

    def lambda_4094():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4094)

    def lambda_40A1():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40A1)
    Sleep(200)

    def lambda_40B1():

        label("loc_40B1")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_40B1")

    QueueWorkItem2(0x24, 1, lambda_40B1)
    OP_68(-3070, 1250, -2850, 3000)
    MoveCamera(314, 28, 0, 3000)
    OP_6E(300, 3000)
    SetCameraDistance(30680, 3000)
    BeginChrThread(0x103, 1, 0, 36)
    BeginChrThread(0x104, 1, 0, 35)
    BeginChrThread(0x101, 1, 0, 33)
    BeginChrThread(0x102, 1, 0, 34)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_4111():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4111)

    def lambda_411E():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_411E)
    Sleep(400)
    OP_6F(0x79)

    #C0179
    ChrTalk(
        0x101,
        "#12P#0000F谢谢，你帮了大忙了。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x102,
        (
            "#6P#0100F能不能拜托玛夏小姐你\x01",
            "带个话给坎贝尔议员呢？\x02\x03",

            "就说我们一定会把\x01",
            "卡拉小姐带回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x24,
        (
            "#5P好、好的，\x01",
            "小姐就拜托各位了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41D9():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41D9)

    def lambda_41E6():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41E6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_41FB():
        OP_95(0xFE, 1190, 0, -16350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41FB)

    def lambda_4215():
        OP_95(0xFE, -670, 0, -16360, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4215)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x24, 0x1)
    SetChrPos(0x0, 30, 0, -15120, 180)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x5A, 0x0)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    OP_49()
    OP_D5(0x1E)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_29(0x2D, 0x1, 0x9)
    Sleep(1000)
    EventEnd(0x5)
    NewScene("r1500", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_32_38DC end

    def Function_33_429E(): pass

    label("Function_33_429E")

    OP_95(0xFE, -2100, 0, -2600, 4000, 0x0)
    Return()

    # Function_33_429E end

    def Function_34_42B3(): pass

    label("Function_34_42B3")

    OP_95(0xFE, -2700, 0, -3900, 4000, 0x0)
    Return()

    # Function_34_42B3 end

    def Function_35_42C8(): pass

    label("Function_35_42C8")

    OP_95(0xFE, 670, 0, -4290, 5000, 0x0)
    OP_95(0xFE, -400, 0, -16000, 5000, 0x0)
    Return()

    # Function_35_42C8 end

    def Function_36_42F1(): pass

    label("Function_36_42F1")

    OP_95(0xFE, 670, 0, -5760, 5000, 0x0)
    OP_95(0xFE, -400, 0, -12500, 5000, 0x0)
    Return()

    # Function_36_42F1 end

    def Function_37_431A(): pass

    label("Function_37_431A")

    EventBegin(0x1)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x0, 500)

    #C0182
    ChrTalk(
        0xA,
        (
            "啊……\x01",
            "那边是登船口哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        (
            "如果没有票，\x01",
            "是无法进入的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 960, 0, 5140, 180)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_37_431A end

    def Function_38_4387(): pass

    label("Function_38_4387")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "欢迎来到克洛斯贝尔自治州！\x01",
            "若需要住宿，\x01",
            "欢迎光临『千禧酒店』！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_4387 end

    SaveToFile()

Try(main)
