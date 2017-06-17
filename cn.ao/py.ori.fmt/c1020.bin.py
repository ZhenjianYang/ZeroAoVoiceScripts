from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1020.bin",                # FileName
        "c1020",                    # MapName
        "c1020",                    # Location
        0x0014,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 20, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1020",                  # 0
        "雷克罗德Ⅲ世",           # 1
        "接待小姐塞拉姆",         # 2
        "『银螭』特里同",         # 3
        "『龙宫』辉夜",           # 4
        "『水狂』纳西斯",         # 5
        "『海刃』沙克曼",         # 6
        "彼德",                   # 7
        "克潘",                   # 8
        "赛尔丹分部长",           # 9
        "费瑟尔团长",             # 10
    ))

    AddCharChip((
        "chr/ch45600.itc",                   # 00
        "chr/ch22100.itc",                   # 01
        "chr/ch45700.itc",                   # 02
        "chr/ch45800.itc",                   # 03
        "chr/ch45900.itc",                   # 04
        "chr/ch46000.itc",                   # 05
        "chr/ch24200.itc",                   # 06
        "chr/ch23600.itc",                   # 07
        "chr/ch32200.itc",                   # 08
        "chr/ch46100.itc",                   # 09
    ))

    DeclNpc(-4000,   0,       48369,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(7230,    0,       9069,    180,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(50,      0,       43369,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-4769,   0,       47610,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4599,    0,       -330,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-200,    0,       7579,    315,  389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4260,    0,       6059,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-3549,   0,       51630,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(5639,    0,       6059,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4260,    0,       6059,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(6580,    0,       7980,    1500,    7230,    1500,    9070,    0x007E, 0,  4,  0x0000)

    ChipFrameInfo(592, 0)                                        # 0

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_4C5",          # 02, 2
        "Function_3_53E",          # 03, 3
        "Function_4_EA7",          # 04, 4
        "Function_5_EAB",          # 05, 5
        "Function_6_29E2",         # 06, 6
        "Function_7_2AD3",         # 07, 7
        "Function_8_2BBB",         # 08, 8
        "Function_9_2CBB",         # 09, 9
        "Function_10_2D9A",        # 0A, 10
        "Function_11_2FE6",        # 0B, 11
        "Function_12_32C2",        # 0C, 12
        "Function_13_3590",        # 0D, 13
        "Function_14_3620",        # 0E, 14
        "Function_15_4282",        # 0F, 15
        "Function_16_42BD",        # 10, 16
        "Function_17_5598",        # 11, 17
        "Function_18_5976",        # 12, 18
        "Function_19_5DAD",        # 13, 19
        "Function_20_5DC9",        # 14, 20
        "Function_21_5DE5",        # 15, 21
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_31B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_470")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_35F")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4850, 0, 6960, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 8390, 0, 6850, 0)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_470")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A1")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C")
    SetChrPos(0xE, 50, 0, 43370, 90)
    ClearChrFlags(0x11, 0x80)

    label("loc_39C")

    Jump("loc_470")

    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BD")
    SetChrFlags(0x8, 0x80)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3DF")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_3DF")

    Jump("loc_470")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3F7")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_470")

    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_405")
    Jump("loc_470")

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_413")
    Jump("loc_470")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_421")
    Jump("loc_470")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_42F")
    Jump("loc_470")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_43D")
    Jump("loc_470")

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_470")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_459")
    Jump("loc_470")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_470")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_470")

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_484")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A9")
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_4C4")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C4")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_4C4")

    Return()

    # Function_1_308 end

    def Function_2_4C5(): pass

    label("Function_2_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F6")
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51D")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_534")
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53D")

    label("loc_534")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53D")

    Return()

    # Function_2_4C5 end

    def Function_3_53E(): pass

    label("Function_3_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_565")
    Call(0, 17)
    Return()

    label("loc_565")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_576")
    Jump("loc_EA3")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_613")

    #C0001
    ChrTalk(
        0x8,
        (
            "没想到他们竟然\x01",
            "把哈巴德叫来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "……哼哼，但这正合我意。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "毕竟我就是为了战胜他，\x01",
            "才会来到克洛斯贝尔的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_644")

    label("loc_613")


    #C0004
    ChrTalk(
        0x8,
        (
            "赶快放马过来吧……\x01",
            "我会亲自送你去黄泉路的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_644")

    Jump("loc_692")

    label("loc_649")


    #C0005
    ChrTalk(
        0x8,
        "让我们自由使用租船小屋吗……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "的确，那里的环境，\x01",
            "正适合修行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_692")

    Jump("loc_EA3")

    label("loc_697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74A")

    #C0007
    ChrTalk(
        0x8,
        (
            "我们钓皇俱乐部与钓公师团\x01",
            "是有不少因缘的。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "你们大概并不了解……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0009
    ChrTalk(
        0x8,
        (
            "……哼，说了些无聊的话。\x01",
            "把我刚才说的那些忘掉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_781")

    label("loc_74A")


    #C0010
    ChrTalk(
        0x8,
        (
            "……哼，说了些无聊的话。\x01",
            "把我刚才说的那些忘掉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_781")

    Jump("loc_EA3")

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_89F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_833")

    #C0011
    ChrTalk(
        0x8,
        (
            "看样子，赛尔丹他们\x01",
            "已经准备认输了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "呵呵，竟然直到现在\x01",
            "都没人有资格和我一战。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "看来你们对钓鱼的热情\x01",
            "也不过如此啊。\x01",
            "哈哈哈哈哈哈。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_89A")

    label("loc_833")


    #C0014
    ChrTalk(
        0x8,
        (
            "呵呵，竟然直到现在\x01",
            "都没人有资格和我一战。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "看来你们对钓鱼的热情\x01",
            "也不过如此啊。\x01",
            "哈哈哈哈哈哈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89A")

    Jump("loc_EA3")

    label("loc_89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_946")

    #C0016
    ChrTalk(
        0x8,
        (
            "我的父亲雷克罗德Ⅱ世\x01",
            "是最强的伟大钓师。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "我们雷克罗德公司\x01",
            "研发的多种钓具\x01",
            "都冠有他的名字……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "那些钓具都是由我父亲\x01",
            "亲手设计的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9C3")

    label("loc_946")


    #C0019
    ChrTalk(
        0x8,
        (
            "我的父亲雷克罗德Ⅱ世\x01",
            "是最强的伟大钓师。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "他那永不满足的探究之心\x01",
            "远远超过我们的想象……\x01",
            "可以称得上是究极钓鱼爱好者。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C3")

    Jump("loc_EA3")

    label("loc_9C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA2")

    #C0021
    ChrTalk(
        0x8,
        (
            "我们钓皇俱乐部的所有成员\x01",
            "都是精英级别的专业钓师。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "而且，大家会把所有垂钓成果\x01",
            "都反馈给雷克罗德公司，\x01",
            "用于新产品的开发。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "我们和钓公师团那些\x01",
            "只是玩玩而已的业余者\x01",
            "是有本质区别的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B13")

    label("loc_AA2")


    #C0024
    ChrTalk(
        0x8,
        (
            "我们钓皇俱乐部的所有成员\x01",
            "都是精英级别的专业钓师。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "和钓公师团那些\x01",
            "只是玩玩而已的业余者\x01",
            "是有本质区别的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B13")

    Jump("loc_EA3")

    label("loc_B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BB4")

    #C0026
    ChrTalk(
        0x8,
        (
            "唔，所谓的独立提案，\x01",
            "不过就是克洛斯贝尔人\x01",
            "莫名其妙的妄言罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "此地的安宁都是由我的祖国\x01",
            "埃雷波尼亚所赋予的，\x01",
            "他们为什么就不明白呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA3")

    label("loc_BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C39")

    #C0028
    ChrTalk(
        0x8,
        (
            "唔，没想到克洛斯贝尔\x01",
            "有这么多优秀的垂钓场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "虽然没有海洋，比较遗憾，\x01",
            "但鱼种很丰富，\x01",
            "就让我好好享受一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA3")

    label("loc_C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D01")

    #C0030
    ChrTalk(
        0x8,
        "你们几个，爆钓比赛的状况还顺利吗？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "呵呵，如果难以抗衡，就不要勉强了，\x01",
            "还是老老实实地投降为好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "结果无非就是今后不能在\x01",
            "克洛斯贝尔自由垂钓而已。\x01",
            "哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D86")

    label("loc_D01")


    #C0033
    ChrTalk(
        0x8,
        (
            "呵呵，如果难以抗衡，就不要勉强了，\x01",
            "还是老老实实地投降为好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "结果无非就是今后不能在\x01",
            "克洛斯贝尔自由垂钓而已。\x01",
            "哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D86")

    Jump("loc_EA3")

    label("loc_D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E10")

    #C0035
    ChrTalk(
        0x8,
        (
            "呵呵，你们究竟能顽抗到什么地步呢，\x01",
            "就让我好好期待一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "不过，最终结果根本\x01",
            "就是显而易见的啊。\x01",
            "哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA3")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6C")

    #C0037
    ChrTalk(
        0x8,
        "唔……你怎么还在？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "我和你已经没话可说了，\x01",
            "赶快出去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E95")

    label("loc_E6C")


    #C0039
    ChrTalk(
        0x8,
        (
            "我和你已经没话可说了，\x01",
            "赶快出去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E95")

    Jump("loc_EA3")

    label("loc_E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_EA3")

    label("loc_EA3")

    TalkEnd(0xFE)
    Return()

    # Function_3_53E end

    def Function_4_EA7(): pass

    label("Function_4_EA7")

    Call(0, 5)
    Return()

    # Function_4_EA7 end

    def Function_5_EAB(): pass

    label("Function_5_EAB")

    TalkBegin(0x9)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECD")
    SetScenarioFlags(0x0, 2)

    label("loc_ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_ED9")
    SetScenarioFlags(0x0, 2)

    label("loc_ED9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F37")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                    # 0
            "听取爆钓比赛的说明\x01",      # 1
            "放弃\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_F87")

    label("loc_F37")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_F87")

    label("loc_F7D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F87")

    Jump("loc_F96")

    label("loc_F8C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB6")
    OP_AF(0x36)
    Jump("loc_FB8")

    label("loc_FB6")

    OP_AF(0x37)

    label("loc_FB8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29D9")

    label("loc_FC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1975")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "比赛规则\x01",                # 0
            "挑战资格\x01",                # 1
            "钓杰四天王的所在地\x01",      # 2
            "放弃\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")

    #C0040
    ChrTalk(
        0x9,
        (
            "如果你们能在全部爆钓比赛中取得胜利……\x01",
            "我们不仅会将事务所归还，\x01",
            "而且还可以接受你们的任意一个命令。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "比赛对手一共有五人，\x01",
            "那就是钓杰四天王\x01",
            "和雷克罗德先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "顺便一说，只要战胜了钓杰四天王，\x01",
            "由相应天王所管理的\x01",
            "垂钓场所就会开放。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "另外，如果要向四天王挑战，\x01",
            "分别需要不同的资格……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "只要取得了资格，\x01",
            "之后就可以不限次数地挑战了。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1970")

    label("loc_11A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187B")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "雷克罗德Ⅲ世\x01",        # 0
            "『银螭』特里同\x01",      # 1
            "『龙宫』辉夜\x01",        # 2
            "『水狂』纳西斯\x01",      # 3
            "『海刃』沙克曼\x01",      # 4
            "放弃\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137C")

    #C0045
    ChrTalk(
        0x9,
        (
            "想向名副其实的最强钓师，\x01",
            "君临于俱乐部的顶点的\x01",
            "雷克罗德先生挑战……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "其条件再直接不过，\x01",
            "那就是\x01",
            "『战胜钓杰四天王』。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "这可是相当\x01",
            "艰辛困难的……\x01",
            "拿出干劲与毅力来挑战吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136D")

    #C0048
    ChrTalk(
        0x9,
        (
            "真是的，你不是都已经战胜四天王了嘛。\x01",
            "呵呵，很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "接下来的对手就只剩下\x01",
            "雷克罗德先生了……祝你好运。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1876")

    label("loc_137C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1498")

    #C0050
    ChrTalk(
        0x9,
        (
            "想向被誉为四天王之首的\x01",
            "『银螭』特里同先生\x01",
            "挑战……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "其条件就是\x01",
            "『取得２９种\x01",
            "垂钓战利品』。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "我想这是一条相当艰难的道路……\x01",
            "不要放弃，努力到最后吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_END)), "loc_1489")

    #C0053
    ChrTalk(
        0x9,
        (
            "真是的，\x01",
            "你不是都已经战胜特里同先生了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "呵呵，那就不需要\x01",
            "这条情报了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1489")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1876")

    label("loc_1498")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B7")

    #C0055
    ChrTalk(
        0x9,
        (
            "想向受垂钓之神所爱怜的\x01",
            "『龙宫』辉夜小姐\x01",
            "挑战……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "其条件就是\x01",
            "『钓获１３０里矩\x01",
            "以上的战利品』。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "我认为运气恐怕比\x01",
            "技术更加重要……\x01",
            "别怕失败，继续努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_END)), "loc_15A8")

    #C0058
    ChrTalk(
        0x9,
        (
            "真是的，\x01",
            "你不是都已经战胜辉夜小姐了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "呵呵，那就不需要\x01",
            "这条情报了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1876")

    label("loc_15B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F0")

    #C0060
    ChrTalk(
        0x9,
        (
            "想向最喜爱自己以及美丽鱼类的\x01",
            "『水狂』纳西斯先生\x01",
            "挑战……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "其条件就是\x01",
            "『钓获克洛斯贝尔\x01",
            "最美丽的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "虽然标准有些模糊不清……\x01",
            "不过，尽量钓取外观美丽的鱼，\x01",
            "让纳西斯先生赞叹吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_END)), "loc_16E1")

    #C0063
    ChrTalk(
        0x9,
        (
            "真是的，\x01",
            "你不是都已经战胜纳西斯先生了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "呵呵，那就不需要\x01",
            "这条情报了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1876")

    label("loc_16F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1871")

    #C0065
    ChrTalk(
        0x9,
        (
            "想向与外表形成鲜明对比，以技巧派\x01",
            "而著称的『海刃』沙克曼先生\x01",
            "挑战……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "其条件就是\x01",
            "『钓获规定的\x01",
            "六种鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "具体来说，就是大口鲈鱼、\x01",
            "岩穴鱼、阿尔摩利卡鲫鱼……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "还有食人鱼、金龙鱼\x01",
            "和珍珠龙鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "想把这些鱼全部钓到，\x01",
            "难度自然不小……\x01",
            "请加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_1862")

    #C0070
    ChrTalk(
        0x9,
        (
            "真是的，\x01",
            "你不是都已经战胜沙克曼先生了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "呵呵，那就不需要\x01",
            "这条情报了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1862")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1876")

    label("loc_1871")

    Jump("loc_187B")

    label("loc_1876")

    Jump("loc_11B9")

    label("loc_187B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1970")

    label("loc_188A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1961")

    #C0072
    ChrTalk(
        0x9,
        (
            "沙克曼先生在\x01",
            "『乌尔斯拉间道的池边』。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "纳西斯先生在\x01",
            "『玛因兹山道的溪水边』。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "辉夜小姐在\x01",
            "『阿尔摩利卡古道的休息所』。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "而特里同先生则在\x01",
            "『西克洛斯贝尔街道\x01",
            "的池塘边』。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1970")

    label("loc_1961")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1975")

    label("loc_1975")

    Jump("loc_29D9")

    label("loc_1970")

    Jump("loc_FE0")

    label("loc_197A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_199D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1AA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A36")

    #C0076
    ChrTalk(
        0x9,
        (
            "我刚才总算和\x01",
            "身在阿尔摩利卡村的\x01",
            "家人朋友们取得了联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "虽然今后的情况\x01",
            "还是让人觉得很不安……\x01",
            "但总算是稍微松了口气。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AA3")

    label("loc_1A36")


    #C0078
    ChrTalk(
        0x9,
        (
            "话说回来……\x01",
            "大家全都是不畏任何艰辛的钓鱼傻瓜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "分部长、彼德先生\x01",
            "和克潘先生全都已经\x01",
            "出去钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA3")

    Jump("loc_29D9")

    label("loc_1AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1B04")

    #C0080
    ChrTalk(
        0x9,
        (
            "……唔～\x01",
            "现在的状况真是糟糕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "希望阿尔摩利卡村\x01",
            "的大家平安无事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_1B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_1B7F")

    #C0082
    ChrTalk(
        0x9,
        (
            "钓公师团的活动\x01",
            "刚刚回到正轨，\x01",
            "就发生了不得了的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        "不然我还是先回阿尔摩利卡村一趟吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C88")

    label("loc_1B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1A")

    #C0084
    ChrTalk(
        0x9,
        (
            "多亏雷克罗德先生，\x01",
            "我才能加入钓公师团。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "雷克罗德先生\x01",
            "真是个非常善良的好人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "他为什么不能和钓公师团\x01",
            "的各位搞好关系呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C88")

    label("loc_1C1A")


    #C0087
    ChrTalk(
        0x9,
        (
            "话说回来，钓公师团的活动\x01",
            "刚刚回到正轨，\x01",
            "就发生了不得了的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        "不然我还是先回阿尔摩利卡村一趟吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1C88")

    Jump("loc_29D9")

    label("loc_1C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_201C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2E")

    #C0089
    ChrTalk(
        0x9,
        (
            "说起钓公师团的最终兵器，\x01",
            "好像是某个人物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "究竟是个什么样的人……\x01",
            "不，究竟是个什么样的钓师呢……\x01",
            "不知为何，心里异样地紧张啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2017")

    label("loc_1D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3F")

    #C0091
    ChrTalk(
        0x9,
        (
            "我听说了，你终于要向\x01",
            "雷克罗德先生发起挑战了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "决战场所是乌尔斯拉间道的浅滩……\x01",
            "在大量垂钓场所之中，\x01",
            "雷克罗德先生最喜欢的就是那里。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "这肯定会是一场苦战，\x01",
            "请加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "另外，如果可以的话，请努力\x01",
            "让钓皇俱乐部与钓公师团握手言和。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EBE")

    label("loc_1E3F")


    #C0095
    ChrTalk(
        0x9,
        (
            "决战场所是乌尔斯拉间道的浅滩……\x01",
            "在大量垂钓场所之中，\x01",
            "雷克罗德先生最喜欢的就是那里。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "这肯定会是一场苦战，\x01",
            "请加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EBE")

    Jump("loc_2017")

    label("loc_1EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB0")

    #C0097
    ChrTalk(
        0x9,
        (
            "恭喜你，罗伊德先生，\x01",
            "你完美取得了胜利啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "另外，听说在雷克罗德先生的推荐下，\x01",
            "我已经成为钓公师团的一员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "该怎么说呢，\x01",
            "雷克罗德先生真是个\x01",
            "非常善良的好人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "怎么才能消除他和钓公师团\x01",
            "之间的芥蒂呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2017")

    label("loc_1FB0")


    #C0101
    ChrTalk(
        0x9,
        (
            "该怎么说呢，\x01",
            "雷克罗德先生真是个\x01",
            "非常善良的好人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "怎么才能消除他和钓公师团\x01",
            "之间的芥蒂呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2017")

    Jump("loc_29D9")

    label("loc_201C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_210E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B7")

    #C0103
    ChrTalk(
        0x9,
        (
            "雷克罗德先生\x01",
            "之前曾说自己\x01",
            "讨厌业余钓师……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "但这似乎是因为他和\x01",
            "钓公师团有\x01",
            "一些个人恩怨呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        "究竟发生过什么事情呢？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2109")

    label("loc_20B7")


    #C0106
    ChrTalk(
        0x9,
        (
            "雷克罗德先生\x01",
            "似乎和钓公师团\x01",
            "有过一些个人恩怨呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        "究竟发生过什么事情呢？\x02",
    )

    CloseMessageWindow()

    label("loc_2109")

    Jump("loc_29D9")

    label("loc_210E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218E")

    #C0108
    ChrTalk(
        0x9,
        (
            "据说赛尔丹先生最近总是\x01",
            "喃喃自语，说是要投入\x01",
            "最终兵器。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "那到底是什么呢？\x01",
            "唔～真让人在意啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21BD")

    label("loc_218E")


    #C0110
    ChrTalk(
        0x9,
        (
            "最终兵器究竟是什么呢？\x01",
            "唔～真让人在意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BD")

    Jump("loc_29D9")

    label("loc_21C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_222A")

    #C0111
    ChrTalk(
        0x9,
        (
            "雷克罗德先生每当\x01",
            "谈起自己的父亲时，\x01",
            "双眼中都会闪烁着光辉。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        "呵呵，真让人感动呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_222A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_22D4")

    #C0113
    ChrTalk(
        0x9,
        (
            "雷克罗德先生\x01",
            "在不久前夸奖我\x01",
            "很有想象力。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "他还说水下栖息着什么样的鱼，\x01",
            "它们的生活方式是怎样的……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "在垂钓过程中，想象这些\x01",
            "的能力也是很重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_22D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_235D")

    #C0116
    ChrTalk(
        0x9,
        (
            "不知不觉间，我已经在\x01",
            "城市里生活很久了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "虽然也会定期回村子看看……\x01",
            "但真是很怀念阿尔摩利卡村\x01",
            "那悠闲自在的氛围啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_235D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_23FF")

    #C0118
    ChrTalk(
        0x9,
        (
            "从表面上看，\x01",
            "四天王整天都在游玩，\x01",
            "但他们其实也要完成各种工作的。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "钓具的测试自不用说，\x01",
            "连水质检测与生态分布调查都要负责……\x01",
            "真让人佩服啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_23FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_259D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2513")

    #C0120
    ChrTalk(
        0x9,
        (
            "听说雷克罗德先生的家族\x01",
            "世代继承帝国的子爵爵位。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "在帝国，从政或从商的\x01",
            "贵族有很多……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "但能像雷克罗德先生这样，\x01",
            "以职业钓师为副职真是很厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "听说雷克罗德先生从童年时期开始\x01",
            "就接受了垂钓方面的英才教育。\x01",
            "……虽然不知道是怎样的教育。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2598")

    label("loc_2513")


    #C0124
    ChrTalk(
        0x9,
        (
            "雷克罗德先生说自己接受过垂钓英才教育……\x01",
            "但我真是想象不出\x01",
            "垂钓英才教育到底是怎样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "……下次不如直接问问\x01",
            "雷克罗德先生吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2598")

    Jump("loc_29D9")

    label("loc_259D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2619")

    #C0126
    ChrTalk(
        0x9,
        (
            "那个……雷克罗德先生\x01",
            "已经把详细情况告诉我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "如果对比赛方面的事项有什么\x01",
            "不明之处，可以尽管问我哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_2619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_29D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2972")
    TurnDirection(0x9, 0x101, 0)

    #C0128
    ChrTalk(
        0x9,
        (
            "那个……\x01",
            "你是钓公师团的成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "我本来是想加入\x01",
            "钓公师团的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0130
    ChrTalk(
        0x101,
        "#00005F加入……钓公师团吗？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        "嗯，我之前一直都很犹豫。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "某一天，我终于下定决心要入团，\x01",
            "于是来到这里，\x01",
            "结果遇到了雷克罗德先生……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "漫无边际地聊了一番之后，\x01",
            "就成为这里的接待员了……\x02",
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

    #C0134
    ChrTalk(
        0x102,
        "#00106F这样啊，你也经历了不少事呢。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "不过，我一直没有讲明这一点，\x01",
            "总觉得心有愧疚……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "因为雷克罗德先生\x01",
            "对我非常好。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        (
            "不但把雷克罗德公司制造的\x01",
            "最新型钓竿送给了我……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "在时间充裕时，\x01",
            "还会对我进行个人垂钓指导，\x01",
            "钓饵也任由我免费使用……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#00006F真是很优厚的待遇啊……\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        "所以我的心情很复杂……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "总之，雷克罗德先生\x01",
            "好像非常厌恶\x01",
            "钓公师团……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "而我非常希望他们能\x01",
            "握手言和。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "我要是能做些\x01",
            "什么就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 6)
    Jump("loc_29CB")

    label("loc_2972")


    #C0144
    ChrTalk(
        0x9,
        (
            "钓公师团和钓皇俱乐部……\x01",
            "真希望二者能\x01",
            "握手言和啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        (
            "我要是能做些\x01",
            "什么就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CB")

    Jump("loc_29D9")

    label("loc_29D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29D9")

    label("loc_29D9")

    Jump("loc_EE3")

    label("loc_29DE")

    TalkEnd(0x9)
    Return()

    # Function_5_EAB end

    def Function_6_29E2(): pass

    label("Function_6_29E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_29F3")
    Jump("loc_2ACF")

    label("loc_29F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A48")

    #C0146
    ChrTalk(
        0xA,
        (
            "呀～没想到\x01",
            "大家都输了～\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        "虽然比赛很愉快，但终究还是不甘心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ACF")

    label("loc_2A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A56")
    Jump("loc_2ACF")

    label("loc_2A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A64")
    Jump("loc_2ACF")

    label("loc_2A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2A72")
    Jump("loc_2ACF")

    label("loc_2A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A80")
    Jump("loc_2ACF")

    label("loc_2A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A8E")
    Jump("loc_2ACF")

    label("loc_2A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A9C")
    Jump("loc_2ACF")

    label("loc_2A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AAA")
    Jump("loc_2ACF")

    label("loc_2AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AB8")
    Jump("loc_2ACF")

    label("loc_2AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2AC6")
    Jump("loc_2ACF")

    label("loc_2AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2ACF")

    label("loc_2ACF")

    TalkEnd(0xFE)
    Return()

    # Function_6_29E2 end

    def Function_7_2AD3(): pass

    label("Function_7_2AD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2AE4")
    Jump("loc_2BB7")

    label("loc_2AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B30")

    #C0148
    ChrTalk(
        0xB,
        (
            "竟然能钓到\x01",
            "巨骨龙皇鱼……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "哼，肯定只是\x01",
            "撞大运而已！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB7")

    label("loc_2B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2B3E")
    Jump("loc_2BB7")

    label("loc_2B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2B4C")
    Jump("loc_2BB7")

    label("loc_2B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B5A")
    Jump("loc_2BB7")

    label("loc_2B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B68")
    Jump("loc_2BB7")

    label("loc_2B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B76")
    Jump("loc_2BB7")

    label("loc_2B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B84")
    Jump("loc_2BB7")

    label("loc_2B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B92")
    Jump("loc_2BB7")

    label("loc_2B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2BA0")
    Jump("loc_2BB7")

    label("loc_2BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2BAE")
    Jump("loc_2BB7")

    label("loc_2BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2BB7")

    label("loc_2BB7")

    TalkEnd(0xFE)
    Return()

    # Function_7_2AD3 end

    def Function_8_2BBB(): pass

    label("Function_8_2BBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2BCC")
    Jump("loc_2CB7")

    label("loc_2BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C05")

    #C0150
    ChrTalk(
        0xC,
        (
            "钓公师团战胜了我们……\x01",
            "嗯～干得漂亮！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB7")

    label("loc_2C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C3E")

    #C0151
    ChrTalk(
        0xC,
        (
            "神秘的武装集团……\x01",
            "嗯～太没有美感了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB7")

    label("loc_2C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C4C")
    Jump("loc_2CB7")

    label("loc_2C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2C5A")
    Jump("loc_2CB7")

    label("loc_2C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2C68")
    Jump("loc_2CB7")

    label("loc_2C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C76")
    Jump("loc_2CB7")

    label("loc_2C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C84")
    Jump("loc_2CB7")

    label("loc_2C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C92")
    Jump("loc_2CB7")

    label("loc_2C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CA0")
    Jump("loc_2CB7")

    label("loc_2CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CAE")
    Jump("loc_2CB7")

    label("loc_2CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CB7")

    label("loc_2CB7")

    TalkEnd(0xFE)
    Return()

    # Function_8_2BBB end

    def Function_9_2CBB(): pass

    label("Function_9_2CBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2CCC")
    Jump("loc_2D96")

    label("loc_2CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D0F")

    #C0152
    ChrTalk(
        0xD,
        (
            "这面丰收旗……真不错啊。\x01",
            "哈哈哈，带回帝国好了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D96")

    label("loc_2D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D1D")
    Jump("loc_2D96")

    label("loc_2D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D2B")
    Jump("loc_2D96")

    label("loc_2D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D39")
    Jump("loc_2D96")

    label("loc_2D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D47")
    Jump("loc_2D96")

    label("loc_2D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D55")
    Jump("loc_2D96")

    label("loc_2D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D63")
    Jump("loc_2D96")

    label("loc_2D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D71")
    Jump("loc_2D96")

    label("loc_2D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D7F")
    Jump("loc_2D96")

    label("loc_2D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D8D")
    Jump("loc_2D96")

    label("loc_2D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D96")

    label("loc_2D96")

    TalkEnd(0xFE)
    Return()

    # Function_9_2CBB end

    def Function_10_2D9A(): pass

    label("Function_10_2D9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DAB")
    Jump("loc_2FE2")

    label("loc_2DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2DF5")

    #C0153
    ChrTalk(
        0xE,
        (
            "唔……总之，\x01",
            "现在也只能保养一下钓具，\x01",
            "以便打发时间了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE2")

    label("loc_2DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2F4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2E7D")

    #C0154
    ChrTalk(
        0xE,
        (
            "哎呀呀，\x01",
            "迪塔总统真是很大胆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xE,
        (
            "我虽然理解他的主张……\x01",
            "但克洛斯贝尔今后的命运\x01",
            "实在是让人感到十分不安。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F48")

    label("loc_2E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ED5")

    #C0156
    ChrTalk(
        0xE,
        (
            "哎呀呀，\x01",
            "我们的费瑟尔团长\x01",
            "真是太厉害了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xE,
        "费瑟尔团长万岁～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F48")

    label("loc_2ED5")


    #C0158
    ChrTalk(
        0xE,
        (
            "话说回来，迪塔总统\x01",
            "真是很大胆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xE,
        (
            "我虽然理解他的主张……\x01",
            "但克洛斯贝尔今后的命运\x01",
            "真是让人感到十分不安啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F48")

    Jump("loc_2FE2")

    label("loc_2F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2F5B")
    Jump("loc_2FE2")

    label("loc_2F5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F69")
    Jump("loc_2FE2")

    label("loc_2F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F77")
    Jump("loc_2FE2")

    label("loc_2F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2F85")
    Jump("loc_2FE2")

    label("loc_2F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F93")
    Jump("loc_2FE2")

    label("loc_2F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FA1")
    Jump("loc_2FE2")

    label("loc_2FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FAF")
    Jump("loc_2FE2")

    label("loc_2FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2FBD")
    Jump("loc_2FE2")

    label("loc_2FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2FCB")
    Jump("loc_2FE2")

    label("loc_2FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FD9")
    Jump("loc_2FE2")

    label("loc_2FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2FE2")

    label("loc_2FE2")

    TalkEnd(0xFE)
    Return()

    # Function_10_2D9A end

    def Function_11_2FE6(): pass

    label("Function_11_2FE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FF7")
    Jump("loc_32BE")

    label("loc_2FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_305E")

    #C0160
    ChrTalk(
        0xF,
        "这个分部中的食品储备很充足的说。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xF,
        (
            "……所以我们绝对不会对\x01",
            "鱼缸中的鱼图谋不轨的～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_305E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3229")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_3178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3102")

    #C0162
    ChrTalk(
        0xF,
        (
            "啊～果然还是待在这里\x01",
            "最舒服的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xF,
        (
            "话说回来，独立问题的发展趋势\x01",
            "真是让人有点捉摸不透的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xF,
        "……今后到底会怎样呢？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3173")

    label("loc_3102")


    #C0165
    ChrTalk(
        0xF,
        (
            "总算是回到了这里，实在是可喜可贺，\x01",
            "但独立问题的发展趋势真让人有点捉摸不透的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xF,
        "……今后到底会怎样呢？\x02",
    )

    CloseMessageWindow()

    label("loc_3173")

    Jump("loc_3224")

    label("loc_3178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CB")

    #C0167
    ChrTalk(
        0xF,
        "费瑟尔团长好厉害的说！\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xF,
        (
            "呼～我也好想钓到\x01",
            "那种大鱼的说！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3224")

    label("loc_31CB")


    #C0169
    ChrTalk(
        0xF,
        (
            "话说回来，独立问题的发展趋势\x01",
            "真是让人有点捉摸不透的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xF,
        "……今后到底会怎样呢？\x02",
    )

    CloseMessageWindow()

    label("loc_3224")

    Jump("loc_32BE")

    label("loc_3229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3237")
    Jump("loc_32BE")

    label("loc_3237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3245")
    Jump("loc_32BE")

    label("loc_3245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3253")
    Jump("loc_32BE")

    label("loc_3253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3261")
    Jump("loc_32BE")

    label("loc_3261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_326F")
    Jump("loc_32BE")

    label("loc_326F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_327D")
    Jump("loc_32BE")

    label("loc_327D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_328B")
    Jump("loc_32BE")

    label("loc_328B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3299")
    Jump("loc_32BE")

    label("loc_3299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32A7")
    Jump("loc_32BE")

    label("loc_32A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32B5")
    Jump("loc_32BE")

    label("loc_32B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_32BE")

    label("loc_32BE")

    TalkEnd(0xFE)
    Return()

    # Function_11_2FE6 end

    def Function_12_32C2(): pass

    label("Function_12_32C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_32D3")
    Jump("loc_358C")

    label("loc_32D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3354")

    #C0171
    ChrTalk(
        0x10,
        (
            "虽然已经料到了无法离开市区的状况还会再持续一阵子，\x01",
            "但没想到这次连分部都不能出了……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x10,
        "呼，好想出去钓鱼啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_358C")

    label("loc_3354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_34F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_33E0")

    #C0173
    ChrTalk(
        0x10,
        "克洛斯贝尔独立吗……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x10,
        (
            "就像我们与钓皇俱乐部水火不容一样，\x01",
            "难道克洛斯贝尔与帝国无法保持友好往来也是种命运吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F2")

    label("loc_33E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3473")

    #C0175
    ChrTalk(
        0x10,
        (
            "话说回来，钓皇俱乐部\x01",
            "的那些家伙真是很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x10,
        (
            "他们对垂钓的热爱之情\x01",
            "是不容置疑的……\x01",
            "通过和他们的比赛，我也有很大收获。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_34F2")

    label("loc_3473")


    #C0177
    ChrTalk(
        0x10,
        "话说回来，克洛斯贝尔独立吗……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x10,
        (
            "就像我们与钓皇俱乐部水火不容一样，\x01",
            "难道克洛斯贝尔与帝国无法保持友好往来也是种命运吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F2")

    Jump("loc_358C")

    label("loc_34F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3505")
    Jump("loc_358C")

    label("loc_3505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3513")
    Jump("loc_358C")

    label("loc_3513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3521")
    Jump("loc_358C")

    label("loc_3521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_352F")
    Jump("loc_358C")

    label("loc_352F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_353D")
    Jump("loc_358C")

    label("loc_353D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_354B")
    Jump("loc_358C")

    label("loc_354B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3559")
    Jump("loc_358C")

    label("loc_3559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3567")
    Jump("loc_358C")

    label("loc_3567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3575")
    Jump("loc_358C")

    label("loc_3575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3583")
    Jump("loc_358C")

    label("loc_3583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_358C")

    label("loc_358C")

    TalkEnd(0xFE)
    Return()

    # Function_12_32C2 end

    def Function_13_3590(): pass

    label("Function_13_3590")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3613")

    #C0179
    ChrTalk(
        0x11,
        (
            "嗯，总之，\x01",
            "能顺利化解克洛斯贝尔分部的危机，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x11,
        (
            "这样一来，\x01",
            "我也就可以昂首挺胸地\x01",
            "返回利贝尔了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_361C")

    label("loc_3613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_361C")

    label("loc_361C")

    TalkEnd(0xFE)
    Return()

    # Function_13_3590 end

    def Function_14_3620(): pass

    label("Function_14_3620")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 7530, 0, 6780, 225)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 7230, 0, 9070, 225)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrPos(0xF, 5820, 0, 4630, 45)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrPos(0xE, 5020, 0, 5530, 45)
    OP_4B(0xE, 0xFF)
    OP_68(2300, 1400, 1800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 2300, 0, 1600, 45)
    SetChrPos(0x102, 1300, 0, 2100, 45)
    SetChrPos(0x109, 1600, 0, 300, 45)
    SetChrPos(0x105, 100, 0, 1600, 45)

    def lambda_371F():
        OP_9B(0x1, 0x101, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_371F)
    Sleep(300)

    def lambda_3737():
        OP_9B(0x1, 0x102, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3737)
    Sleep(300)

    def lambda_374F():
        OP_9B(0x1, 0x109, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_374F)
    Sleep(300)

    def lambda_3767():
        OP_9B(0x1, 0x105, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3767)
    OP_68(4590, 1400, 3920, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0181
    ChrTalk(
        0x101,
        "#12P#00000F打扰一下。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0182
    ChrTalk(
        0x9,
        "#5P啊……\x02",
    )

    CloseMessageWindow()

    #N0183
    NpcTalk(
        0x8,
        "打扮考究的男人",
        "#11P嗯？什么人？\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xE,
        "#6P有、有人来了吗……？\x02",
    )

    CloseMessageWindow()

    def lambda_3834():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3834)
    Sleep(50)

    def lambda_3844():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3844)
    WaitChrThread(0xE, 1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0185
    ChrTalk(
        0xF,
        "#11P这、这不是罗伊德团员吗！？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xE,
        (
            "#5P啊，你来得正是时候。\x01",
            "罗伊德，你来和这个人\x01",
            "讲讲道理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "#5P让他明白，我们钓公师团·克洛斯贝尔分部\x01",
            "是富有和平共处精神的垂钓爱好者们\x01",
            "休息交流的场所。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0188
    ChrTalk(
        0x101,
        "#12P#00012F这、这是什么情况？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(5070, 1400, 5070, 0)
    MoveCamera(75, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21850, 0)
    SetChrPos(0x101, 4500, 0, 3800, 45)
    SetChrPos(0x102, 3400, 0, 4300, 45)
    SetChrPos(0x109, 4200, 0, 2500, 45)
    SetChrPos(0x105, 3200, 0, 3000, 45)
    SetChrPos(0xF, 5300, 0, 3000, 45)
    SetChrPos(0xE, 6200, 0, 2250, 0)
    OP_0D()

    #N0189
    NpcTalk(
        0x8,
        "打扮考究的男人",
        (
            "#5P哼，你也是钓公师团的成员啊，\x01",
            "是来帮同伴们抗议的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#12P#00005F那个……我的确是\x01",
            "这里的团员，不过……\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    SetChrName("")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向男子出示了调查手册，\x01",
            "并将前来调查的情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0192
    NpcTalk(
        0x8,
        "打扮考究的男人",
        "#5P调查可疑住户……？\x02",
    )

    CloseMessageWindow()

    #N0193
    NpcTalk(
        0x8,
        "打扮考究的男人",
        (
            "#5P哼，我确实还没有完成法人登记。\x01",
            "既然如此，就做个正式自我介绍吧，\x01",
            "我的名字是雷克罗德Ⅲ世。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        (
            "#5P总部位于埃雷波尼亚帝国，\x01",
            "大陆中首屈一指的钓具制造公司\x01",
            "『雷克罗德公司』的继承人。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "#5P而『钓皇俱乐部』\x01",
            "则是个由我担任代表\x01",
            "的职业垂钓组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#12P#00005F雷克罗德公司……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        "#6P#00105F罗伊德，你知道吗？\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯，在垂钓爱好者群体中，\x01",
            "这个名字可以说是\x01",
            "无人不知的。\x02\x03",

            "#00000F这家公司在大陆钓具\x01",
            "市场占用率中稳稳占据着\x01",
            "Ｎｏ．１的宝座。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        "#6P#00105F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x109,
        (
            "#12P#10101F不过，这样的人为何\x01",
            "会来克洛斯贝尔呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "#5P哼，那自然是为了\x01",
            "扩大我们钓皇俱乐部的规模，\x01",
            "以便进一步发展。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "#5P所以，在这里设立新的事务所\x01",
            "正是我们迈出的第一步。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "#5P顺便一说，合同的合法性\x01",
            "正如这份文件所示。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        "#12P#00001F……请容我过目。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x1, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
    Sleep(800)

    #C0205
    ChrTalk(
        0x101,
        (
            "#12P#00005F这是……\x01",
            "这座建筑的租赁合同啊。\x02\x03",

            "#00003F确实如您所说，\x01",
            "这座建筑现在的所有者是钓皇俱乐部。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        "#5P呵呵，看来你已经明白了啊。\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0xB4, 0x7D0, 0x7D0, 0x0)
    Sleep(50)

    #C0207
    ChrTalk(
        0xF,
        (
            "#11P罗伊德团员……\x01",
            "我们绝不能接受这种蛮横行为的说。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    #C0208
    ChrTalk(
        0x101,
        "#6P#00005F蛮横……？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xE,
        (
            "#11P这个男人在没有预先通知\x01",
            "赛尔丹分部长的情况下，\x01",
            "强行夺走了租赁权。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xE,
        (
            "#11P因为他事先靠金钱\x01",
            "疏通了房产公司。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0211
    ChrTalk(
        0x8,
        (
            "#5P哼，虽然手段多少有些强硬，\x01",
            "但手续却是正式的。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#5P而且，你们这种人本来就\x01",
            "没有资格占用这个地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "#5P所谓的『钓公师团』，\x01",
            "不过就是一群把垂钓当作\x01",
            "业余爱好与交友工具的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#12P#00001F你……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        "#5P总之，话就说到这里。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "#5P如果听明白了，就赶快出去吧。\x01",
            "这些话，也替我转告给赛尔丹那家伙。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0217
    ChrTalk(
        0x8,
        "#11P塞拉姆，接下来就交给你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 300)

    #C0218
    ChrTalk(
        0x9,
        "#5P是、是的，明白了。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 15)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4189():
        OP_93(0xF, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4189)
    Sleep(50)

    def lambda_4199():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4199)
    Sleep(50)

    def lambda_41A9():
        TurnDirection(0x102, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41A9)
    Sleep(50)

    def lambda_41B9():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41B9)
    Sleep(50)

    def lambda_41C9():
        TurnDirection(0x105, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41C9)
    Sleep(50)

    def lambda_41D9():
        TurnDirection(0xE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_41D9)

    #C0219
    ChrTalk(
        0xF,
        "#12P啊，竟然逃走了，好卑鄙的说。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xE,
        (
            "#12P是啊，我们还有\x01",
            "不少话要说呢……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    #C0221
    ChrTalk(
        0x105,
        "#6P#10302F呵呵，走掉了呢。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    StopSound(128, 2000, 40)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 5)
    NewScene("c1000", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3620 end

    def Function_15_4282(): pass

    label("Function_15_4282")

    OP_95(0x8, 8680, 0, 4760, 2000, 0x0)
    OP_95(0x8, 11520, 0, 4740, 2000, 0x0)
    OP_9B(0x0, 0x8, 0x10E, 0x7D0, 0x7D0, 0x0)
    Sleep(200)
    Return()

    # Function_15_4282 end

    def Function_16_42BD(): pass

    label("Function_16_42BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 7530, 0, 6780, 225)
    SetChrPos(0x10, 5820, 0, 4630, 45)
    SetChrPos(0xE, 5020, 0, 5530, 45)
    SetChrPos(0xF, 6570, 0, 3900, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_68(2300, 1400, 1800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 2300, 0, 1600, 45)
    SetChrPos(0x102, 1300, 0, 2100, 45)
    SetChrPos(0x109, 1600, 0, 300, 45)
    SetChrPos(0x104, 100, 0, 1600, 45)
    SetChrPos(0x105, 410, 0, 410, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0222
    ChrTalk(
        0x10,
        "别、别开玩笑了！\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        (
            "你们到底要把我们愚弄到\x01",
            "什么地步才满意！？\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x104,
        "#00305F（怎么，有什么纠纷吗？）\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        "#00001F（又发生什么事了吗……？）\x02",
    )

    CloseMessageWindow()

    def lambda_4464():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4464)
    Sleep(300)

    def lambda_447C():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_447C)
    Sleep(300)

    def lambda_4494():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4494)
    Sleep(300)

    def lambda_44AC():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_44AC)
    Sleep(300)

    def lambda_44C4():
        OP_9B(0x1, 0xFE, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_44C4)
    OP_68(4190, 1400, 3520, 2500)
    OP_6F(0x1)

    #C0226
    ChrTalk(
        0x101,
        (
            "#00005F各位……\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 500)

    #C0227
    ChrTalk(
        0xE,
        (
            "啊，罗伊德……\x01",
            "你来得正好。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4547():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4547)
    Sleep(50)
    TurnDirection(0xF, 0x101, 500)

    #C0228
    ChrTalk(
        0x10,
        "罗伊德团员，听我说啊。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x10,
        (
            "不久之前，这个组织的数名成员\x01",
            "出现在了市外各地的垂钓场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        (
            "他们突然宣布\x01",
            "要独占那些垂钓场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#00005F独、独占垂钓场所……？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xF,
        (
            "嗯，他们宣称，\x01",
            "除了钓皇俱乐部的成员之外，\x01",
            "其他人禁止在那些场所垂钓……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xF,
        (
            "我无视他们的无理要求，\x01",
            "仍旧去那些地方垂钓，\x01",
            "对方便突然剪断了我的钓线的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        "#00106F那可真是过分啊。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x109,
        (
            "#10101F那个……你们为什么\x01",
            "不能友好共处呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "哼，因为钓公师团只是个\x01",
            "没有追求的业余集团而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "在我们这种顶级职业组织看来，\x01",
            "他们光是在眼前晃来晃去\x01",
            "就已经很碍眼了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0238
    ChrTalk(
        0xE,
        (
            "业、业余垂钓\x01",
            "究竟有什么不好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xE,
        (
            "我们只是想享受垂钓的乐趣而已，\x01",
            "职业和业余并无区别吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47EA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_47EA)
    Sleep(50)
    TurnDirection(0xF, 0x8, 500)

    #C0240
    ChrTalk(
        0x10,
        (
            "是啊，另外，\x01",
            "我知道你们曾在很多\x01",
            "比赛中取得过成绩……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x10,
        (
            "但我们这里也有毫不逊色的垂钓高手，\x01",
            "请不要小看我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0242
    ChrTalk(
        0x8,
        "哦……？\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xF,
        "分部长说的没错的说！\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xF,
        (
            "虽然现在已经重新评定级别了，\x01",
            "但『特级钓师』可是不容小觑的说！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x32, 0x0, 0x3E8, 0xC8)

    #C0245
    ChrTalk(
        0x8,
        "#4S呵呵呵……哈哈哈哈哈哈！#3S\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "……有意思。\x01",
            "竟能从你们的口中听到这样的话，\x01",
            "倒真是让我有些意外呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "既然已经把话说到了这个地步……\x01",
            "我便给你们一个特别机会，\x01",
            "要不要接受『爆钓比赛』呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0248
    ChrTalk(
        0x10,
        "爆、爆钓比赛……？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xF,
        "你是认真的吗？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#00005F那、那个……\x01",
            "『爆钓比赛』是……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A74():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4A74)
    Sleep(50)

    def lambda_4A84():
        TurnDirection(0xE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_4A84)
    Sleep(50)

    def lambda_4A94():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_4A94)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    #C0251
    ChrTalk(
        0xE,
        (
            "哦，正如其字面上的意思，\x01",
            "是一种通过垂钓来分出胜负的对决方式……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xE,
        (
            "对钓师而言，被冠以『爆钓』之名\x01",
            "的比赛有着绝对性的意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x10,
        (
            "嗯，爆钓比赛象征着钓师的荣耀与名誉……\x01",
            "而且可以将任何有形或无形之物作为赌注，\x01",
            "可谓真正意义上的对决。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xF,
        (
            "虽然我并没有\x01",
            "亲身参与过……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xF,
        (
            "但听说有个钓师在爆钓比赛中失败之后，\x01",
            "失去了全部财产的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xF,
        (
            "也就是说……\x01",
            "这是一场无论如何都不容失败的战斗的说。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x101,
        "#00006F是、是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x104,
        "#00306F听起来好像很惊人啊……\x02",
    )

    CloseMessageWindow()

    def lambda_4CEE():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4CEE)
    Sleep(50)

    def lambda_4CFE():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_4CFE)
    Sleep(50)

    def lambda_4D0E():
        TurnDirection(0xF, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_4D0E)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    #C0259
    ChrTalk(
        0x10,
        "那么，比赛规则呢？\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "这个嘛……来到克洛斯贝尔的成员\x01",
            "包括我与四名同伴。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "钓公师团要向我们五人发起挑战，\x01",
            "只要任意一人能将五人全部战胜，\x01",
            "就算是钓公师团获胜，意下如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "想挑战多少次都可以……\x01",
            "不过，在取胜之前，\x01",
            "你们必须要服从我们的任何规定。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "话是这么说，但规定的内容\x01",
            "肯定会限定在垂钓方面。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x10,
        (
            "………………………………\x01",
            "……如果我们赢了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "唔……虽然这是可能性不足万分之一的奇迹，\x01",
            "但你们也有做梦的权利。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "好吧，只要你们战胜任意一人，\x01",
            "相应的垂钓场所就会开放，这自不必说……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x8,
        (
            "如果能把我们五人全部击败，\x01",
            "我们就会全员撤离克洛斯贝尔……\x01",
            "这间事务所自然也会还给你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "不仅如此，\x01",
            "还会接受你们的任意一个命令。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0269
    ChrTalk(
        0x101,
        "#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xF,
        "真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，但真的可以\x01",
            "相信你们吗？\x02\x03",

            "#10300F就算我们取得胜利，\x01",
            "也无法保证你们会遵守约定呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x10,
        (
            "不，正如彼德之前所说，对钓师而言，\x01",
            "爆钓比赛的结果有着绝对性的意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x10,
        (
            "而且，虽然这些家伙对我们的态度很恶劣，\x01",
            "但他们对钓师身份的荣耀感远胜常人，\x01",
            "这是不用怀疑的。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x10,
        (
            "所以他们绝对不可能\x01",
            "违背约定。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#00006F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        "#00100F是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x8,
        (
            "呵呵，赛尔丹……\x01",
            "你倒是意外地明白事理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "好了，意下如何？\x01",
            "要向我们挑战吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x10,
        "……………………………\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x10,
        "……明白了，我接受这场对决。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        "呵呵，很好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 500)

    #C0282
    ChrTalk(
        0xE,
        "赛尔丹分部长，真的要接受吗？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xE,
        (
            "如果无法取胜，\x01",
            "就要一直服从对方制定的不合理规则啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xF,
        (
            "嘿嘿，但我们可以\x01",
            "不限次数地挑战啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xF,
        (
            "这样说也许有些没志气，但既然可以\x01",
            "反复挑战，取胜也只是时间问题吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xF,
        (
            "不管实力有多强，\x01",
            "也没人能在垂钓比赛中\x01",
            "永远保持胜利啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#00006F的确……\x01",
            "我也这样想。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "呵呵，\x01",
            "看来你们根本\x01",
            "就不懂垂钓呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)

    #C0289
    ChrTalk(
        0x8,
        (
            "算了，顺便说一下，\x01",
            "只有战胜四天王的人\x01",
            "才有资格向我挑战。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "另外，在向他们挑战的时候，\x01",
            "也必须要出示相应的资格。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "我们无暇理会连基本实力\x01",
            "都没有的挑战者。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        "关于此点，还请体谅。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x10,
        "嗯……明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 500)

    #C0294
    ChrTalk(
        0xE,
        "赛尔丹分部长……\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        (
            "好了，如果还有\x01",
            "其它不明之处，\x01",
            "就去询问接待员塞拉姆吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "我们钓皇俱乐部引以为傲的\x01",
            "『钓杰四天王』……\x01",
            "是否会接受你们的挑战呢？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("c1000", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_16_42BD end

    def Function_17_5598(): pass

    label("Function_17_5598")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4540, 1400, 48400, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -4070, 0, 49840, 180)
    SetChrPos(0x102, -2990, 0, 50250, 180)
    SetChrPos(0x103, -4110, 0, 50870, 180)
    SetChrPos(0x104, -5080, 0, 51200, 180)
    SetChrPos(0x109, -2730, 0, 51480, 180)
    SetChrPos(0x105, -1420, 0, 51120, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0297
    ChrTalk(
        0x8,
        "嗯……有何贵干？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0298
    ChrTalk(
        0x8,
        (
            "你该不会是想说……\x01",
            "已经将四天王\x01",
            "全部击败了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        "#00005F那个，正是如此……\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x8,
        (
            "唔……既然如此，\x01",
            "就给我看看奖牌吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0301
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向雷克罗德Ⅲ世\x01",
            "出示了从钓杰四天王手中\x01",
            "取得的四枚奖牌。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0302
    ChrTalk(
        0x8,
        (
            "这的确是货真价实的\x01",
            "四天王奖牌……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "……呵呵，没想到\x01",
            "竟然会出现有资格\x01",
            "挑战我『钓皇』的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#00011F钓、钓皇……？\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "不错，\x01",
            "本人正是『钓皇』雷克罗德Ⅲ世。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x8,
        (
            "冠有钓皇俱乐部的『钓皇』之名，\x01",
            "君临于顶点之人。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x8,
        (
            "总之……\x01",
            "我先行一步，去决战地点等你。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        "场所就是乌尔斯拉间道的浅滩。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)

    def lambda_588A():

        label("loc_588A")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_588A")

    QueueWorkItem2(0x101, 2, lambda_588A)

    def lambda_589C():

        label("loc_589C")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_589C")

    QueueWorkItem2(0x102, 2, lambda_589C)

    def lambda_58AE():

        label("loc_58AE")

        TurnDirection(0x109, 0x8, 500)
        Yield()
        Jump("loc_58AE")

    QueueWorkItem2(0x109, 2, lambda_58AE)

    def lambda_58C0():

        label("loc_58C0")

        TurnDirection(0x105, 0x8, 500)
        Yield()
        Jump("loc_58C0")

    QueueWorkItem2(0x105, 2, lambda_58C0)

    def lambda_58D2():

        label("loc_58D2")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_58D2")

    QueueWorkItem2(0x104, 2, lambda_58D2)

    def lambda_58E4():

        label("loc_58E4")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_58E4")

    QueueWorkItem2(0x103, 2, lambda_58E4)

    def lambda_58F6():
        OP_95(0xFE, -210, 0, 50780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_58F6)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_591B():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_591B)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)
    SetScenarioFlags(0x190, 7)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4070, 0, 49840, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_17_5598 end

    def Function_18_5976(): pass

    label("Function_18_5976")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_68(410, 1400, 410, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -1580, 0, -580, 45)
    SetChrPos(0x102, -580, 0, -1580, 45)
    SetChrPos(0x104, -1580, 0, -2580, 45)
    SetChrPos(0x103, -2580, 0, -1580, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(3850, 1400, 4450, 4000)
    SetCameraDistance(22000, 4000)

    def lambda_5A54():
        OP_95(0xFE, 3330, 0, 4330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A54)

    def lambda_5A6E():
        OP_95(0xFE, 2310, 0, 3310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A6E)
    BeginChrThread(0x102, 3, 0, 19)
    BeginChrThread(0x104, 3, 0, 20)

    def lambda_5A94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A94)

    def lambda_5AA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5AA5)

    def lambda_5AB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5AB6)

    def lambda_5AC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5AC7)
    Sleep(1000)
    BeginChrThread(0x10, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 21)
    OP_6F(0x1)

    #C0309
    ChrTalk(
        0x10,
        "#11P哦哦，这不是罗伊德团员吗！\x02",
    )

    CloseMessageWindow()

    #N0310
    NpcTalk(
        0x11,
        "费瑟尔",
        (
            "唔，你就是特别任务支援科的\x01",
            "罗伊德·班宁斯啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#6P#00005F嗯，是的……\x01",
            "请问钓皇俱乐部的那些人……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0312
    ChrTalk(
        0x101,
        (
            "#6P#00000F原来如此，看来你们\x01",
            "在爆钓比赛中获胜了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x10,
        "#11P嗯，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x10,
        (
            "#11P说到底，\x01",
            "多亏有费瑟尔团长前来相助，\x01",
            "我们才能取得胜利啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0315
    ChrTalk(
        0x101,
        "#6P#00005F您、您就是钓公师团的团长……\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x10,
        (
            "#11P哎呀呀，话说回来，\x01",
            "没想到您竟然能钓到\x01",
            "那个巨大的鱼王……！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x10,
        (
            "#11P真是好久都没有\x01",
            "这么兴奋了！\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x11,
        (
            "过奖了，能取得胜利，\x01",
            "也多亏有你们开发的\x01",
            "虹丸ＥＸ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "不管怎么说，\x01",
            "能顺利夺回事务所\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#6P#00004F原、原来如此……\x01",
            "真是感谢您的帮助。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x191, 2)
    TurnDirection(0x11, 0x10, 0)
    TurnDirection(0x10, 0x11, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_4C(0x9, 0xFF)
    ClearMapFlags(0x10000000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3330, 0, 4330, 45)
    EventEnd(0x5)
    Return()

    # Function_18_5976 end

    def Function_19_5DAD(): pass

    label("Function_19_5DAD")

    OP_95(0xFE, 4310, 0, 3130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_19_5DAD end

    def Function_20_5DC9(): pass

    label("Function_20_5DC9")

    OP_95(0xFE, 3310, 0, 2130, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_20_5DC9 end

    def Function_21_5DE5(): pass

    label("Function_21_5DE5")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)
    OP_4B(0xFE, 0xFF)
    Return()

    # Function_21_5DE5 end

    SaveToFile()

Try(main)
