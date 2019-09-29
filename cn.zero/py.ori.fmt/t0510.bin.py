from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t0510.bin",                # FileName
        "t0510",                    # MapName
        "t0510",                    # Location
        0x003D,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 61, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0510",                  # 0
        "比克森镇长",             # 1
        "比克森镇长",             # 2
        "安娜夫人",               # 3
        "安娜夫人",               # 4
        "矿工玛尔罗",             # 5
        "矿工马库斯",             # 6
        "矿工马库斯",             # 7
        "卢利艾达",               # 8
        "米兰达",                 # 9
        "比鲁玛婆婆",             # 10
        "霍夫曼矿山长",           # 11
    ))

    AddCharChip((
        "chr/ch26200.itc",                   # 00
        "apl/ch50130.itc",                   # 01
        "chr/ch22700.itc",                   # 02
        "chr/ch23300.itc",                   # 03
        "chr/ch24300.itc",                   # 04
        "chr/ch23200.itc",                   # 05
        "chr/ch23202.itc",                   # 06
        "chr/ch20100.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch20102.itc",                   # 0C
        "chr/ch26302.itc",                   # 0D
        "chr/ch26202.itc",                   # 0E
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

    DeclNpc(-889,    750,     3319,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-889,    949,     2640,    90,   341,  0x0, 0,   6,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-6530,   750,     59,      270,  261,  0x0, 0,   7,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(860,     949,     5179,    180,  469,  0x0, 0,   12,  0,   255, 255, 0,   6,   255,  0)
    DeclNpc(153559,  0,       3329,    135,  389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(154710,  300,     2500,    315,  471,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(150729,  250,     100,     270,  469,  0x0, 0,   14,  0,   255, 255, 0,   8,   255,  0)
    DeclNpc(147369,  0,       4179,    333,  261,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(96099,   0,       4219,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(49209,   0,       4369,    0,    261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(97459,   150,     -1169,   0,    469,  0x0, 0,   13,  0,   255, 255, 0,   13,  255,  0)

    ScpFunction((
        "Function_0_288",          # 00, 0
        "Function_1_340",          # 01, 1
        "Function_2_5D6",          # 02, 2
        "Function_3_615",          # 03, 3
        "Function_4_719",          # 04, 4
        "Function_5_10AF",         # 05, 5
        "Function_6_18E6",         # 06, 6
        "Function_7_1CFE",         # 07, 7
        "Function_8_215A",         # 08, 8
        "Function_9_2543",         # 09, 9
        "Function_10_2E93",        # 0A, 10
        "Function_11_3950",        # 0B, 11
        "Function_12_3A86",        # 0C, 12
        "Function_13_4558",        # 0D, 13
        "Function_14_4998",        # 0E, 14
        "Function_15_5BD5",        # 0F, 15
        "Function_16_6937",        # 10, 16
        "Function_17_71E4",        # 11, 17
    ))


    def Function_0_288(): pass

    label("Function_0_288")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2C8"),
        (1, "loc_2D4"),
        (2, "loc_2E0"),
        (3, "loc_2EC"),
        (4, "loc_2F8"),
        (5, "loc_304"),
        (6, "loc_310"),
        (SWITCH_DEFAULT, "loc_31C"),
    )


    label("loc_2C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_2D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_2E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_2EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_2F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_304")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_310")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_31C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_328")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_328")

    label("loc_33F")

    Return()

    # Function_0_288 end

    def Function_1_340(): pass

    label("Function_1_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_35D")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_566")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_370")
    SetChrFlags(0x9, 0x80)
    Jump("loc_566")

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_37E")
    Jump("loc_566")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_38C")
    Jump("loc_566")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A4")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_566")

    label("loc_3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_414")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40F")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3F9")
    SetChrPos(0x8, -1010, 750, -630, 180)
    Jump("loc_40F")

    label("loc_3F9")

    SetChrPos(0x8, -1010, 750, -630, 0)
    SetChrFlags(0x8, 0x10)

    label("loc_40F")

    Jump("loc_566")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_484")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_469")
    SetChrPos(0x8, -1010, 750, -630, 180)
    Jump("loc_47F")

    label("loc_469")

    SetChrPos(0x8, -1010, 750, -630, 0)
    SetChrFlags(0x8, 0x10)

    label("loc_47F")

    Jump("loc_566")

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4F4")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_4D9")
    SetChrPos(0x8, -1010, 750, -630, 180)
    Jump("loc_4EF")

    label("loc_4D9")

    SetChrPos(0x8, -1010, 750, -630, 0)
    SetChrFlags(0x8, 0x10)

    label("loc_4EF")

    Jump("loc_566")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_50C")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_566")

    label("loc_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_51A")
    Jump("loc_566")

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_528")
    Jump("loc_566")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_536")
    Jump("loc_566")

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_549")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_566")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_561")
    ClearChrFlags(0xC, 0x80)

    label("loc_561")

    ClearChrFlags(0xD, 0x80)

    label("loc_566")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_594")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_5BD")

    label("loc_594")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_5BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D5")
    Event(0, 17)

    label("loc_5D5")

    Return()

    # Function_1_340 end

    def Function_2_5D6(): pass

    label("Function_2_5D6")

    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FD")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_614")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_614")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_614")

    Return()

    # Function_2_5D6 end

    def Function_3_615(): pass

    label("Function_3_615")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_684")

    #C0001
    ChrTalk(
        0x8,
        "你们竟然敢闯进这么危险的废坑啊。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "这次可真是多亏了你们，\x01",
            "以后还请继续关照啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_715")

    label("loc_684")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_712")

    #C0003
    ChrTalk(
        0x8,
        (
            "去废坑的话，就要找到矿山深处的门，\x01",
            "再使用这把钥匙开门就能进去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "消灭魔兽的事情就拜托你们啦，\x01",
            "一定要当心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_715")

    label("loc_712")

    Call(0, 16)

    label("loc_715")

    TalkEnd(0xFE)
    Return()

    # Function_3_615 end

    def Function_4_719(): pass

    label("Function_4_719")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7AD")
    Jump("loc_7F7")

    label("loc_7AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F7")

    label("loc_7CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F7")

    label("loc_7ED")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_82A")
    Jump("loc_10A7")

    label("loc_82A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_87B")

    #C0005
    ChrTalk(
        0xFE,
        (
            "冈兹的事情\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "如果有什么消息，请马上联络我。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A7")

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_905")
    SetChrSubChip(0x9, 0x1)

    #C0007
    ChrTalk(
        0xFE,
        "都已经过去两周了……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "但愿他没有被卷入到\x01",
            "什么纠纷事件中啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "一想到他那玩牌的嗜好，\x01",
            "就让人很担心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Jump("loc_10A7")

    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F0")

    #C0010
    ChrTalk(
        0xFE,
        (
            "昨天，帝国的商人弗里吉亚\x01",
            "又来找我交涉，让我把\x01",
            "七耀石的结晶转让给她。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "她从很久以前就一直向我提议了，\x01",
            "我最后还是抵挡不住她的诚意，卖给了她。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "哎，她实在是太锲而不舍了……\x01",
            "真不愧是大商人的女儿啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A54")

    label("loc_9F0")


    #C0013
    ChrTalk(
        0xFE,
        (
            "弗里吉亚真是个\x01",
            "非常有意思的商人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "哎，她实在是太锲而不舍了……\x01",
            "真不愧是大商人的女儿啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A54")

    Jump("loc_10A7")

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B0D")

    #C0015
    ChrTalk(
        0xFE,
        (
            "已经和弗里吉亚约好了，\x01",
            "她今天晚上就会过来，\x01",
            "和我交易七耀石。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "她看上去是一个\x01",
            "非常有热情的商人……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "看今天的谈判情况再做决定吧，\x01",
            "转让给她也没什么不好的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A7")

    label("loc_B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B79")

    #C0018
    ChrTalk(
        0xFE,
        (
            "在这镇子里，好像\x01",
            "总会有零星的游客前来观光。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "我一定得提醒他们注意，\x01",
            "不要进入矿山啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A7")

    label("loc_B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2F")

    #C0020
    ChrTalk(
        0xFE,
        (
            "为了庆祝纪念庆典的首日，\x01",
            "我们昨天举办了宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "呵呵，年轻矿工们的豪放吃相\x01",
            "可真是壮观。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "看来大家都很尽兴呢，\x01",
            "可以说，这次的活动办得很成功啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C8E")

    label("loc_C2F")


    #C0023
    ChrTalk(
        0xFE,
        (
            "年轻的矿工们\x01",
            "好像都去\x01",
            "克洛斯贝尔市玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "大家平时都很辛苦，\x01",
            "希望今天能尽情享受一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8E")

    Jump("loc_10A7")

    label("loc_C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D64")

    #C0025
    ChrTalk(
        0xFE,
        (
            "最近在镇上做交易的商人\x01",
            "……是叫弗里吉亚吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "虽然我被她的执著和诚意折服，\x01",
            "不过身为一个商人，她还差得远啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "看样子，她好像是\x01",
            "看上了七耀石的结晶……\x01",
            "嗯，到底该怎么做呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DE3")

    label("loc_D64")


    #C0028
    ChrTalk(
        0xFE,
        (
            "弗里吉亚好像要在这里\x01",
            "待上很长一段时间呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "明明是个年轻女孩，\x01",
            "但出手好像相当阔绰。\x01",
            "就这点来说，真不愧是经商之人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE3")

    Jump("loc_10A7")

    label("loc_DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_F46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC9")

    #C0030
    ChrTalk(
        0xFE,
        (
            "『特别任务支援科』的各位……\x01",
            "这次的事件，真是多亏了你们的帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "没想到，这一连串的事件\x01",
            "竟然都是有人在背后操控的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "真危险，差点就中了\x01",
            "黑手党的奸计了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "真是非常感谢\x01",
            "你们的帮忙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F41")

    label("loc_EC9")


    #C0034
    ChrTalk(
        0xFE,
        (
            "因魔兽侵害而延迟的开采计划，\x01",
            "应该很快就能赶上进度的。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "虽然有些对不住矿工们，\x01",
            "但最近这段时间只能再辛苦一点了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F41")

    Jump("loc_10A7")

    label("loc_F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_F54")
    Jump("loc_10A7")

    label("loc_F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_109E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1029")

    #C0036
    ChrTalk(
        0xFE,
        (
            "……警备队实在是不可靠，\x01",
            "可又不忍心找繁忙的\x01",
            "游击士来担任警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "而刚才的那帮家伙就更不必说了，\x01",
            "实在是不想和他们扯上关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "嗯……我就姑且相信你们所说的\x01",
            "『能解决这件事』吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1099")

    label("loc_1029")


    #C0039
    ChrTalk(
        0xFE,
        (
            "『特别任务支援科』吗……\x01",
            "虽然这名字很陌生……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "嗯……不过，我就姑且相信你们\x01",
            "所说的『能解决这件事』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1099")

    Jump("loc_10A7")

    label("loc_109E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_10A7")

    label("loc_10A7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_719 end

    def Function_5_10AF(): pass

    label("Function_5_10AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1104")

    #C0041
    ChrTalk(
        0xFE,
        (
            "多亏了你们啊，\x01",
            "实在是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "真的太感谢了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_1104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1166")

    #C0043
    ChrTalk(
        0xFE,
        (
            "由于常年进行\x01",
            "开采工作，\x01",
            "废坑通得非常深。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "请务必小心，\x01",
            "不要受伤哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1174")
    Jump("loc_18E2")

    label("loc_1174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1201")

    #C0045
    ChrTalk(
        0xFE,
        (
            "比克森为了去找冈兹，\x01",
            "到克洛斯贝尔去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "……总觉得冈兹的事情\x01",
            "有些奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "到底发生了什么事呢……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1261")

    label("loc_1201")


    #C0048
    ChrTalk(
        0xFE,
        (
            "……总之，知道冈兹没事，\x01",
            "我也就松口气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "我把情况告诉给了镇上的人，\x01",
            "大家也都安心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1261")

    Jump("loc_18E2")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_12CC")

    #C0050
    ChrTalk(
        0xFE,
        (
            "虽然不知道他遇到了什么事，\x01",
            "但请务必尽早找到他。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "其他矿工们\x01",
            "也都十分担心呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E2")

    label("loc_12CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_12DA")
    Jump("loc_18E2")

    label("loc_12DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_144E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B8")

    #C0052
    ChrTalk(
        0xFE,
        (
            "虽然我听说弗里吉亚是\x01",
            "帝国人后，就有点\x01",
            "退缩了……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "不过，她是一个比我想像中\x01",
            "要温和很多的好女孩。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "一说到帝国，总给人一种\x01",
            "军人般的威严印象……\x01",
            "但说不定，这种温和的人也意外地有很多呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1449")

    label("loc_13B8")


    #C0055
    ChrTalk(
        0xFE,
        (
            "说到帝国，给人的第一印象\x01",
            "就是那种军人般的威严感……\x01",
            "不过，说不定温和的人也不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "我以前总带着有色眼镜去看别人，\x01",
            "真是感到有些惭愧啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1449")

    Jump("loc_18E2")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_14A8")

    #C0057
    ChrTalk(
        0xFE,
        (
            "我丈夫也\x01",
            "支持着各位哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "他一定很欣赏你们这种\x01",
            "努力拼搏的年轻人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E2")

    label("loc_14A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1522")

    #C0059
    ChrTalk(
        0xFE,
        (
            "往年，来镇上观光的人\x01",
            "从来都没有这么多过……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "因为是自治州创立七十周年，\x01",
            "所以才会有很多人来参观吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E2")

    label("loc_1522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_159B")

    #C0061
    ChrTalk(
        0xFE,
        (
            "我丈夫每天都要\x01",
            "制定开采计划，\x01",
            "绝对不比矿工们轻松……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "所以至少在这个纪念庆典，\x01",
            "要好好犒劳一下他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E2")

    label("loc_159B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_174C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D9")

    #C0063
    ChrTalk(
        0xFE,
        (
            "因为土地的关系，\x01",
            "这个地区实在是难以生产什么食材。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "总要频繁乘坐导力巴士，去外面采购，\x01",
            "真的很麻烦啊……\x01",
            "不过，现在就不必那么辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "因为有个名叫哈罗德·海瓦斯的\x01",
            "克洛斯贝尔市的贸易商，\x01",
            "总会定期来贩卖一些农作物。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "特地从阿尔摩利卡村\x01",
            "送来那么美味的农作物，\x01",
            "实在是帮了大忙呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1747")

    label("loc_16D9")


    #C0067
    ChrTalk(
        0xFE,
        (
            "哈罗德先生对自治州各地的\x01",
            "商品需求了如指掌。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "作为克洛斯贝尔的商人，\x01",
            "非常值得信赖，让人对他很有好感。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1747")

    Jump("loc_18E2")

    label("loc_174C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_17DC")

    #C0069
    ChrTalk(
        0xFE,
        (
            "我的丈夫和矿山的负责人——\x01",
            "霍夫曼矿山长一起，\x01",
            "制定着每天的开采计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "因为必须注意开采量\x01",
            "一定不能超过\x01",
            "政府所规定的上限。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E2")

    label("loc_17DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_17EA")
    Jump("loc_18E2")

    label("loc_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_18D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A3")

    #C0071
    ChrTalk(
        0xFE,
        (
            "不过，话说回来，\x01",
            "刚刚那些穿黑衣服的人……\x01",
            "总觉得不能相信啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "警备队很快就搁置不管的案件，\x01",
            "竟然还特意赶来接手……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "这样的自信\x01",
            "到底是从何而来呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18D4")

    label("loc_18A3")


    #C0074
    ChrTalk(
        0xFE,
        (
            "刚刚那些穿黑衣服的人……\x01",
            "到底想要做什么啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D4")

    Jump("loc_18E2")

    label("loc_18D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_18E2")

    label("loc_18E2")

    TalkEnd(0xFE)
    Return()

    # Function_5_10AF end

    def Function_6_18E6(): pass

    label("Function_6_18E6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_197A")
    Jump("loc_19C4")

    label("loc_197A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_199A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19C4")

    label("loc_199A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19BA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19C4")

    label("loc_19BA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19C4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B46")

    #C0075
    ChrTalk(
        0xFE,
        (
            "关于冈兹的事，\x01",
            "丈夫和我联系过，我已经全部都听说了。\x01",
            "包括今早的失踪事件也……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "这种事情，如果告诉镇上的各位，\x01",
            "一定会给他们带来很大的打击……\x01",
            "我实在不知道该怎么办才好。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "总之，我们现在\x01",
            "也只能向女神祈祷，\x01",
            "保佑冈兹能够平安归来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3E")

    #C0078
    ChrTalk(
        0x10A,
        (
            "#0600F不能再这样继续下去了……\x01",
            "快点回去，\x01",
            "调查鲁巴彻的据点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B3E")

    SetScenarioFlags(0x0, 1)
    Jump("loc_1B78")

    label("loc_1B46")


    #C0079
    ChrTalk(
        0xFE,
        (
            "啊啊，女神啊……\x01",
            "请保佑冈兹\x01",
            "能够平安归来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B78")

    Jump("loc_1CF6")

    label("loc_1B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B8B")
    Jump("loc_1CF6")

    label("loc_1B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1B99")
    Jump("loc_1CF6")

    label("loc_1B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1BA7")
    Jump("loc_1CF6")

    label("loc_1BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C29")
    SetChrSubChip(0xB, 0x2)

    #C0080
    ChrTalk(
        0xFE,
        (
            "是啊……\x01",
            "还是尽早\x01",
            "采取措施为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "他很有可能已经陷入危机了，\x01",
            "所以我们一定要争分夺秒。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C78")

    label("loc_1C29")


    #C0082
    ChrTalk(
        0xFE,
        (
            "哎呀，是各位啊……\x01",
            "谢谢你们解决了狼形魔兽事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "请在这里放松休息吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1C78")

    Jump("loc_1CF6")

    label("loc_1C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C8B")
    Jump("loc_1CF6")

    label("loc_1C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C99")
    Jump("loc_1CF6")

    label("loc_1C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1CA7")
    Jump("loc_1CF6")

    label("loc_1CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CB5")
    Jump("loc_1CF6")

    label("loc_1CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CC3")
    Jump("loc_1CF6")

    label("loc_1CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1CD1")
    Jump("loc_1CF6")

    label("loc_1CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1CDF")
    Jump("loc_1CF6")

    label("loc_1CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1CED")
    Jump("loc_1CF6")

    label("loc_1CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1CF6")

    label("loc_1CF6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_18E6 end

    def Function_7_1CFE(): pass

    label("Function_7_1CFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D0F")
    Jump("loc_2156")

    label("loc_1D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1D1D")
    Jump("loc_2156")

    label("loc_1D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1D2B")
    Jump("loc_2156")

    label("loc_1D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1D39")
    Jump("loc_2156")

    label("loc_1D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D47")
    Jump("loc_2156")

    label("loc_1D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D55")
    Jump("loc_2156")

    label("loc_1D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D63")
    Jump("loc_2156")

    label("loc_1D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D71")
    Jump("loc_2156")

    label("loc_1D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D7F")
    Jump("loc_2156")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1D8D")
    Jump("loc_2156")

    label("loc_1D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D9B")
    Jump("loc_2156")

    label("loc_1D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1DA9")
    Jump("loc_2156")

    label("loc_1DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3C")

    #C0084
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "都快到了收工时间吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "……可恶。\x01",
            "要是没有魔兽\x01",
            "袭击就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "再继续这样的生活，\x01",
            "身体可就要锈掉了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E70")

    label("loc_1E3C")


    #C0087
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "再继续这种生活的话，\x01",
            "身体可就要锈掉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E70")

    Jump("loc_2156")

    label("loc_1E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_END)), "loc_1FBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E97")
    SetScenarioFlags(0x67, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F48")

    #C0088
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "竟然被后辈看到了\x01",
            "如此丢脸的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "这一切的一切……\x01",
            "都是那些来历不明\x01",
            "的野狼所致。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "要是下次再敢出现的话，\x01",
            "我就用铲子把它们狠狠砸扁。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FB7")

    label("loc_1F48")


    #C0091
    ChrTalk(
        0xFE,
        (
            "都是因为那些\x01",
            "来历不明的黑狼，\x01",
            "害得我暂时不能工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "要是下次再敢出现的话，\x01",
            "我就用铲子狠狠把它们砸扁。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB7")

    Jump("loc_2156")

    label("loc_1FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDE")
    SetScenarioFlags(0x67, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FDE")

    TurnDirection(0xC, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C8")

    #C0093
    ChrTalk(
        0xC,
        "马库斯，你感觉身体怎么样了？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xC,
        "听说你的腿被魔兽咬到了……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xD,
        (
            "嗯，这个伤本身\x01",
            "倒是没什么大碍……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xD,
        (
            "但是矿山长说，\x01",
            "让我暂时不要\x01",
            "再进矿山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xC,
        (
            "是这样啊……\x01",
            "呼，说的也对，你还是\x01",
            "不要勉强自己为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2156")

    label("loc_20C8")


    #C0098
    ChrTalk(
        0xD,
        (
            "唉，太丢脸了。\x01",
            "只是这点小伤而已，\x01",
            "明明一点都不碍事……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xC,
        (
            "算啦，还是多休息休息比较好啊。\x01",
            "要是一直劳动的话，\x01",
            "也会影响伤口的愈合速度啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2156")

    TalkEnd(0xFE)
    Return()

    # Function_7_1CFE end

    def Function_8_215A(): pass

    label("Function_8_215A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21EE")
    Jump("loc_2238")

    label("loc_21EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_220E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2238")

    label("loc_220E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_222E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2238")

    label("loc_222E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2238")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DC")

    #C0100
    ChrTalk(
        0xFE,
        "纪念庆典到今天就要结束了啊……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "把矿山长、镇长还有矿工罗基\x01",
            "都叫到『红砖亭』，\x01",
            "办个宴会吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_232F")

    label("loc_22DC")


    #C0102
    ChrTalk(
        0xFE,
        (
            "把大家都叫到\x01",
            "『红砖亭』参加\x01",
            "宴会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "镇长请我吃过饭，\x01",
            "我也得回请他才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232F")

    Jump("loc_253B")

    label("loc_2334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_23A5")

    #C0104
    ChrTalk(
        0xFE,
        (
            "拥有家庭，\x01",
            "真是件很美好的事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "我能够努力\x01",
            "完成矿工的工作，\x01",
            "全都是因为有个支持我的老婆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253B")

    label("loc_23A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_24EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2469")

    #C0106
    ChrTalk(
        0xFE,
        (
            "无论多么艰苦，\x01",
            "我都很喜欢这份矿工的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "矿山长会先制定出开采计划，剩下的就是\x01",
            "靠我们这些干体力活的来完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "对于不善于思考的我而言，\x01",
            "这份工作可是天职啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24EA")

    label("loc_2469")


    #C0109
    ChrTalk(
        0xFE,
        (
            "总之，要完成这份工作，\x01",
            "只需要有足够体力就可以了，\x01",
            "剩下的都不重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "对于不善于思考的我而言，\x01",
            "矿工这份工作可真是天职啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24EA")

    Jump("loc_253B")

    label("loc_24EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_253B")

    #C0111
    ChrTalk(
        0xFE,
        "昨天真是太尽兴了。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "我已经醉得都记不清\x01",
            "自己总共喝了几杯。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_215A end

    def Function_9_2543(): pass

    label("Function_9_2543")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_25C4")

    #C0113
    ChrTalk(
        0xFE,
        (
            "我的丈夫马库斯\x01",
            "最近工作得非常\x01",
            "卖力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "有干劲总是好事啊。\x01",
            "但还是希望他小心踏实地工作，\x01",
            "千万不要受伤。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_25C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_264A")

    #C0115
    ChrTalk(
        0xFE,
        (
            "直到昨天，还能听到\x01",
            "从遗迹那边传来的声音，\x01",
            "似乎是钟声呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "但到了今天，\x01",
            "就渐渐听不到了。\x01",
            "那到底是什么声音呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_264A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_26C6")

    #C0117
    ChrTalk(
        0xFE,
        (
            "好了，差不多该是男人们\x01",
            "从矿山回来的时候了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "要让他们彻底缓解劳动一天的疲惫，\x01",
            "明天才能继续努力工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_26C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2738")

    #C0119
    ChrTalk(
        0xFE,
        (
            "丈夫很高兴地告诉我说，\x01",
            "罗基最近工作得很勤快。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "罗基也终于具备\x01",
            "身为一名矿工应有的觉悟了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_2738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_27EA")

    #C0121
    ChrTalk(
        0xFE,
        (
            "我丈夫今天也在\x01",
            "矿山里努力工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "开采克洛斯贝尔的矿山，\x01",
            "不仅是对于玛因兹，\x01",
            "对整个克洛斯贝尔来说都是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "我一直都为做这份工作的\x01",
            "丈夫感到自豪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_27EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2863")

    #C0124
    ChrTalk(
        0xFE,
        (
            "漫长的假期结束了，\x01",
            "从明天开始，\x01",
            "我丈夫又要去矿山工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "决定了，明天的便当\x01",
            "一定要准备得很豪华。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_2863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_28DE")

    #C0126
    ChrTalk(
        0xFE,
        (
            "马库斯能在家里\x01",
            "这么悠闲地放松休息，\x01",
            "我真是很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "要不，泡上一壶茶，\x01",
            "来享受享受下午茶的时光吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_28DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_296C")

    #C0128
    ChrTalk(
        0xFE,
        (
            "我的丈夫马库斯，\x01",
            "被誉为年轻矿工里\x01",
            "最能干的一个。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "呵，虽然他有些傻傻的，\x01",
            "偶尔也会有些顽固，\x01",
            "不过这正是他的可爱之处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_296C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_29DD")

    #C0130
    ChrTalk(
        0xFE,
        (
            "难得的纪念庆典，\x01",
            "喝点酒也没关系，\x01",
            "不过要适可而止啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "对我来说，\x01",
            "马库斯的身体是最重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8F")

    label("loc_29DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAE")

    #C0132
    ChrTalk(
        0xFE,
        (
            "我每天都会很早起床，\x01",
            "为丈夫准备便当。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "因为他是干体力活的，\x01",
            "肚子一定会很容易饿，\x01",
            "所以便当盒一定要装得满满的才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "他回来的时候，我看到空空的便当盒，\x01",
            "会感到十分开心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B29")

    label("loc_2AAE")


    #C0135
    ChrTalk(
        0xFE,
        (
            "将装得满满的\x01",
            "便当盒交给他带走，\x01",
            "这是我每天早上的固定任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "他回来的时候，我看到空空的便当盒，\x01",
            "会感到十分开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B29")

    Jump("loc_2E8F")

    label("loc_2B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BBB")

    #C0137
    ChrTalk(
        0xFE,
        (
            "被魔兽袭击而受伤的丈夫，\x01",
            "经过这段时间的休养，伤势总算是痊愈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "他干劲十足，\x01",
            "想把休息时落下的工作补上。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C28")

    label("loc_2BBB")


    #C0139
    ChrTalk(
        0xFE,
        (
            "被魔兽袭击而受伤的丈夫，\x01",
            "经过这段时间的休养，伤势总算是痊愈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "今天也精神饱满地进入矿山工作了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2C28")

    Jump("loc_2E8F")

    label("loc_2C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_2C3B")
    Jump("loc_2E8F")

    label("loc_2C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC9")

    #C0141
    ChrTalk(
        0xFE,
        (
            "啊啊，真是的，烦死人了。\x01",
            "这么大个男人，还在那里啰啰嗦嗦的……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "受伤也是\x01",
            "没办法的事啊，\x01",
            "老老实实地睡觉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D44")

    label("loc_2CC9")


    #C0143
    ChrTalk(
        0xFE,
        (
            "一个大男人，还唠唠叨叨的……\x01",
            "简直就像个女人一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "只是受了这么点伤，\x01",
            "而且也因此得到了休假，\x01",
            "就不能乖乖睡会觉吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D44")

    Jump("loc_2E8F")

    label("loc_2D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2E8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6B")
    SetScenarioFlags(0x67, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E19")

    #C0145
    ChrTalk(
        0xFE,
        (
            "不久前，我的丈夫工作\x01",
            "结束后，在回家的路上\x01",
            "被魔兽袭击了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "不过，伤势也不是很严重……\x01",
            "而且还得到了休假，很幸运呢☆\x01",
            "换种心态，就当作是因祸得福吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E8F")

    label("loc_2E19")


    #C0147
    ChrTalk(
        0xFE,
        (
            "黑夜里，魔兽突然袭来……\x01",
            "这种情况，换成谁都防范不了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "能得到假期，很幸运呢☆\x01",
            "换种心态，就当作是因祸得福吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E8F")

    TalkEnd(0xFE)
    Return()

    # Function_9_2543 end

    def Function_10_2E93(): pass

    label("Function_10_2E93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2F1D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB2")
    Call(0, 11)
    Jump("loc_2F18")

    label("loc_2EB2")


    #C0149
    ChrTalk(
        0xFE,
        (
            "昨天晚上，镇长夫人\x01",
            "好像找我丈夫去谈了些事。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "看到他那严肃的表情，\x01",
            "我就知道不是什么好消息……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F18")

    Jump("loc_394C")

    label("loc_2F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2FAD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F39")
    Call(0, 11)
    Jump("loc_2FA8")

    label("loc_2F39")


    #C0151
    ChrTalk(
        0xFE,
        "真是太好了，找到了冈兹先生。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "最近不是有传闻说，\x01",
            "遗迹那边出现了幽灵吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "我还以为他神秘失踪了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2FA8")

    Jump("loc_394C")

    label("loc_2FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_302A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC9")
    Call(0, 11)
    Jump("loc_3025")

    label("loc_2FC9")


    #C0154
    ChrTalk(
        0xFE,
        (
            "在整个镇子的建设工作中，\x01",
            "矿工们担负着很重要的任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "所以比克森镇长\x01",
            "很重视矿工们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3025")

    Jump("loc_394C")

    label("loc_302A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3091")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3046")
    Call(0, 11)
    Jump("loc_308C")

    label("loc_3046")


    #C0156
    ChrTalk(
        0xFE,
        (
            "我刚刚去送饭\x01",
            "慰劳我的丈夫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "他能那么高兴，\x01",
            "我也很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308C")

    Jump("loc_394C")

    label("loc_3091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_310C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AD")
    Call(0, 11)
    Jump("loc_3107")

    label("loc_30AD")


    #C0158
    ChrTalk(
        0xFE,
        "霍夫曼今天是不是也在努力呢……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "他一定忙得来不及吃午饭，\x01",
            "稍后得给他\x01",
            "送过去才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3107")

    Jump("loc_394C")

    label("loc_310C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3203")

    #C0160
    ChrTalk(
        0xFE,
        (
            "亚雷库发现了\x01",
            "矿工们并不是一直\x01",
            "都工作得那么开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "说实话，对于我而言，\x01",
            "比起矿工这样危险的行业，\x01",
            "还是希望丈夫能从事些安全的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "在丈夫平安回来之前，\x01",
            "一直都是提心吊胆的，\x01",
            "只有丈夫一个人当矿工就足够了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_327C")

    label("loc_3203")


    #C0163
    ChrTalk(
        0xFE,
        (
            "我希望我的儿子\x01",
            "能去做些安全的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "在丈夫平安回来之前，\x01",
            "一直都是提心吊胆的，\x01",
            "只有丈夫一个人当矿工就足够了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327C")

    Jump("loc_394C")

    label("loc_3281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_32D4")

    #C0165
    ChrTalk(
        0xFE,
        (
            "亚雷库从昨天开始就\x01",
            "很没精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "是不是发生了什么事呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_394C")

    label("loc_32D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33A1")

    #C0167
    ChrTalk(
        0xFE,
        (
            "我丈夫霍夫曼作为矿山长，\x01",
            "负责指挥调度矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "看起来，亚雷库似乎是\x01",
            "受了他父亲的影响，\x01",
            "所以说『想要当矿工』。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "他这么憧憬父亲，\x01",
            "我也很开心，但这工作太危险了，\x01",
            "心情真有点复杂呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394C")

    label("loc_33A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3409")

    #C0170
    ChrTalk(
        0xFE,
        (
            "霍夫曼……\x01",
            "在昨天宴会上喝的酒，\x01",
            "已经完全醒透了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        "我丈夫的强韧度还真是惊人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_394C")

    label("loc_3409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3505")

    #C0172
    ChrTalk(
        0xFE,
        (
            "亚雷库也真是的……\x01",
            "果然不出我所料，\x01",
            "他昨天满身伤痕地回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "还好只是擦伤，\x01",
            "要是一不小心，发生了更严重的事，\x01",
            "说不定就真的无法挽回了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "男人可真是的……真希望他们能站在\x01",
            "整天为他们担心的人的立场上，好好想一想。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_358F")

    label("loc_3505")


    #C0175
    ChrTalk(
        0xFE,
        (
            "都是因为不注意脚下，\x01",
            "才会摔成那样。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "亚雷库也好，我那个矿工丈夫也罢……真希望他们\x01",
            "能站在整天为他们担心的人的立场上，好好想一想。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358F")

    Jump("loc_394C")

    label("loc_3594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_36A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3652")

    #C0177
    ChrTalk(
        0xFE,
        (
            "亚雷库也真是的，\x01",
            "今天好像也在镇上到处跑。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "镇上不但放着重型机器，\x01",
            "还有悬崖，\x01",
            "希望他能小心点……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "如果不提醒一下的话，\x01",
            "说不定哪天\x01",
            "就会受了重伤回来呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_36A2")

    label("loc_3652")


    #C0180
    ChrTalk(
        0xFE,
        (
            "还是提醒亚雷库\x01",
            "一次比较好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "如果他以后真受了重伤，\x01",
            "再说什么都晚了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A2")

    Jump("loc_394C")

    label("loc_36A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_36B5")
    Jump("loc_394C")

    label("loc_36B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3803")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A4")

    #C0182
    ChrTalk(
        0xFE,
        (
            "从很久以前，七耀石的矿山\x01",
            "就被人们认为是很危险的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "被七耀石吸引而来的魔兽，\x01",
            "在矿山里筑了巢。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "现在多亏有了导力灯，\x01",
            "已经安全了许多……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "但即使这样，丈夫去那种危险的地方，\x01",
            "也依然让我很害怕呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_37FE")

    label("loc_37A4")


    #C0186
    ChrTalk(
        0xFE,
        (
            "好了，太阳也下山了……\x01",
            "该让亚雷库回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "我可不能让他\x01",
            "遭遇到马库斯那样的危险。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FE")

    Jump("loc_394C")

    label("loc_3803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_394C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3825")
    SetScenarioFlags(0x67, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38DC")

    #C0188
    ChrTalk(
        0xFE,
        (
            "小孩子总喜欢\x01",
            "去危险的地方，\x01",
            "真让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "希望他不要随意进入矿山，\x01",
            "去给人家添麻烦啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "最近，镇上出现了魔兽，\x01",
            "所以非常混乱，\x01",
            "希望你们要更加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_394C")

    label("loc_38DC")


    #C0191
    ChrTalk(
        0xFE,
        (
            "亚雷库可真是的，\x01",
            "总是喜欢去那么危险的地方，\x01",
            "真让我很头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "男孩子为什么\x01",
            "总喜欢去那种\x01",
            "危险的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_394C")

    TalkEnd(0xFE)
    Return()

    # Function_10_2E93 end

    def Function_11_3950(): pass

    label("Function_11_3950")


    #C0193
    ChrTalk(
        0xFE,
        (
            "最近，矿山那边\x01",
            "好像又忙碌起来了。\x01",
            "希望我丈夫不要累坏身体啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "……不过，我丈夫一直都在\x01",
            "吃我用心制做的便当，\x01",
            "应该没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "你们的工作也挺忙的吧。\x01",
            "反正机会难得，\x01",
            "我来教你们做便当的方法吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xE)
    Return()

    # Function_11_3950 end

    def Function_12_3A86(): pass

    label("Function_12_3A86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3B2D")

    #C0198
    ChrTalk(
        0xFE,
        (
            "罗基虽然\x01",
            "嘴上一直在抱怨，\x01",
            "其实工作起来却一丝不苟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "他明明是长子，却总是喜欢偷懒，\x01",
            "我本来还挺担心的……\x01",
            "不过，看现在这样子，好像还有希望。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4554")

    label("loc_3B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3BA9")

    #C0200
    ChrTalk(
        0xFE,
        (
            "我担心，冈兹回来之后……\x01",
            "罗基又要开始偷懒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "难得他开始认真工作了，\x01",
            "希望能趁此机会，继续保持下去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4554")

    label("loc_3BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3C1B")

    #C0202
    ChrTalk(
        0xFE,
        (
            "好了，罗基和\x01",
            "亚米都该回来了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "特别是罗基，最近很努力地在干活啊，\x01",
            "一定要好好犒劳他一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4554")

    label("loc_3C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3C88")

    #C0204
    ChrTalk(
        0xFE,
        (
            "罗基今天很罕见地\x01",
            "在矿山里认真工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "……因为冈兹不在，\x01",
            "所以也很难\x01",
            "再继续偷懒了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4554")

    label("loc_3C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3D23")

    #C0206
    ChrTalk(
        0xFE,
        (
            "你们知道吗，在玛因兹西南边的\x01",
            "悬崖上，有个遗迹哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "那个遗迹从我小时候开始就在那里了，\x01",
            "但我只知道那是在很久以前\x01",
            "建造的修道院的遗迹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4554")

    label("loc_3D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3DBC")

    #C0208
    ChrTalk(
        0xFE,
        (
            "罗基……\x01",
            "我真是很担心他偷懒成性的恶习。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "在这种时候，就算不是挖矿的工作也好，\x01",
            "希望他至少能找到一点正事，\x01",
            "并努力地投入到里面呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4554")

    label("loc_3DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3E35")

    #C0210
    ChrTalk(
        0xFE,
        (
            "说到我孙女亚米，\x01",
            "她好像只要看到镇上的游客，\x01",
            "就会冲上去搭讪。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "那个孩子的坏习惯\x01",
            "怎么都改不掉啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4554")

    label("loc_3E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3EF1")

    #C0212
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔自治州\x01",
            "被帝国和共和国各自拉拢，\x01",
            "所以这个镇子也总是不得安宁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "多亏了《互不侵犯条约》，\x01",
            "最近终于变得安定起来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "这个镇上的人，\x01",
            "对政府相当不信任。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4554")

    label("loc_3EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3FEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F8C")

    #C0215
    ChrTalk(
        0xFE,
        (
            "我的孙子罗基\x01",
            "明明不能喝酒，\x01",
            "但昨天还参加了宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "果不其然，\x01",
            "他昨晚没有回家呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "哎呀呀，一会去酒馆\x01",
            "看看情况吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3FE9")

    label("loc_3F8C")


    #C0218
    ChrTalk(
        0xFE,
        (
            "真是的，都因为亚米说了句什么\x01",
            "『你真不合群』来挑衅他……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "真是的，一会去看看情况吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3FE9")

    Jump("loc_4554")

    label("loc_3FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_412B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40C6")

    #C0220
    ChrTalk(
        0xFE,
        (
            "最近啊，\x01",
            "积极想要成为矿工的年轻人\x01",
            "几乎都没有了。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "与此相对，想在镇上当商人，\x01",
            "过上荣华富贵的生活……\x01",
            "这样的孩子却越来越多了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "虽然有些凄凉的感觉……\x01",
            "不过这就是时代的变迁吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4126")

    label("loc_40C6")


    #C0223
    ChrTalk(
        0xFE,
        (
            "比起矿工，\x01",
            "越来越多的孩子想当商人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "虽然有些凄凉的感觉……\x01",
            "不过这也是时代的变迁吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4126")

    Jump("loc_4554")

    label("loc_412B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4291")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4213")

    #C0225
    ChrTalk(
        0xFE,
        (
            "在这座矿山里所开采到的七耀石，\x01",
            "品质又好，产量又高……\x01",
            "是非常珍贵的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "而且像这种能够开采到全部七种颜色\x01",
            "的七耀石的矿山，可是很宝贵的。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "外国的商人们\x01",
            "都会特意过来采购，\x01",
            "可以说是广受赞誉呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_428C")

    label("loc_4213")


    #C0228
    ChrTalk(
        0xFE,
        (
            "在这座矿山里所开采到的七耀石，\x01",
            "品质又好，产量又高。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "虽然最近的开采量\x01",
            "在渐渐减少……\x01",
            "不过商人们的评价依旧很高。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_428C")

    Jump("loc_4554")

    label("loc_4291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_429F")
    Jump("loc_4554")

    label("loc_429F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_43D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437C")

    #C0230
    ChrTalk(
        0xFE,
        (
            "我有个孙子和孙女……\x01",
            "但他们两个都有些小问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "哥哥罗基明明是个矿工，\x01",
            "但总是爱偷懒，\x01",
            "会跑到矿山外面去……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "妹妹亚米只对找男朋友\x01",
            "这件事情特别感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "是教育方法出了问题吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_43CF")

    label("loc_437C")


    #C0234
    ChrTalk(
        0xFE,
        "我家里这对兄妹都是问题儿童啊……\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "罗基和亚米……\x01",
            "是教育方法出了问题吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43CF")

    Jump("loc_4554")

    label("loc_43D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F6")
    SetScenarioFlags(0x67, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E4")

    #C0236
    ChrTalk(
        0xFE,
        (
            "从很久以前开始，\x01",
            "帝国和共和国就不断争抢\x01",
            "克洛斯贝尔的所有权……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "其中最大的原因，\x01",
            "就是看中了这里有着\x01",
            "盛产七耀石的矿山。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "虽然克洛斯贝尔现在以金融业为中心，\x01",
            "但即便如此，这里也还是\x01",
            "支撑着自治州发展的重要场所。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4554")

    label("loc_44E4")


    #C0239
    ChrTalk(
        0xFE,
        (
            "帝国和共和国\x01",
            "一直在争夺着\x01",
            "这个自治州的所有权……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "其中最大的原因\x01",
            "就是看中了这里有着\x01",
            "盛产七耀石的矿山。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4554")

    TalkEnd(0xFE)
    Return()

    # Function_12_3A86 end

    def Function_13_4558(): pass

    label("Function_13_4558")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45EC")
    Jump("loc_4636")

    label("loc_45EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_460C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4636")

    label("loc_460C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_462C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4636")

    label("loc_462C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4636")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_470A")

    #C0241
    ChrTalk(
        0xFE,
        (
            "矿山的废坑那里\x01",
            "好像发生了一些\x01",
            "麻烦事……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "……算了，\x01",
            "担心也没用。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "无论如何，主要是人手不够，\x01",
            "还是等那些年轻人回来之后\x01",
            "再想对策吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 1)
    Jump("loc_4990")

    label("loc_470A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4781")

    #C0244
    ChrTalk(
        0xFE,
        (
            "我一直都在让米兰达\x01",
            "为我担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "不过，矿工这份工作是镇上的荣耀。\x01",
            "就算再怎么危险，\x01",
            "也不能逃避。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4990")

    label("loc_4781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_48B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4833")

    #C0246
    ChrTalk(
        0xFE,
        (
            "杂货店的贝卡莱先生\x01",
            "是我的前辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "是他把矿工应该掌握的技术\x01",
            "毫无保留地教给了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "就算我现在已经开始领导整个矿山，\x01",
            "也依然十分尊重他的意见。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_48AC")

    label("loc_4833")


    #C0249
    ChrTalk(
        0xFE,
        (
            "杂货店的贝卡莱先生\x01",
            "是我的前辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "那个人对我有恩。\x01",
            "就算成为了一名可以独当一面的矿工，\x01",
            "我也依然十分尊重他的意见。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48AC")

    Jump("loc_4990")

    label("loc_48B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4911")

    #C0251
    ChrTalk(
        0xFE,
        (
            "我的儿子也很憧憬这份工作，\x01",
            "想成为一名矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "作为父亲，\x01",
            "我感到很自豪呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4990")

    label("loc_4911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4990")

    #C0253
    ChrTalk(
        0xFE,
        (
            "冈兹和玛尔罗在纪念庆典期间\x01",
            "好像会留在克洛斯贝尔市里。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "呵呵，我们这些上了年纪的人\x01",
            "就在镇上悠闲的度过庆典吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4990")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_4558 end

    def Function_14_4998(): pass

    label("Function_14_4998")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    OP_68(500, 2250, -9500, 0)
    MoveCamera(312, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(35500, 0)
    SetChrPos(0x101, 700, 750, -8600, 0)
    SetChrPos(0x102, -500, 750, -8600, 0)
    SetChrPos(0x103, 700, 750, -10000, 0)
    SetChrPos(0x104, -500, 750, -10000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrPos(0x8, -850, 750, 5450, 180)
    SetChrPos(0xA, -1900, 750, 5450, 180)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")
    FadeToBright(1000, 0)
    OP_68(500, 2250, -8000, 1800)

    def lambda_4AD8():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AD8)

    def lambda_4AF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4AF2)
    Sleep(100)

    def lambda_4B06():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4B06)

    def lambda_4B20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4B20)
    Sleep(50)

    def lambda_4B34():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4B34)

    def lambda_4B4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4B4E)
    Sleep(80)

    def lambda_4B62():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4B62)

    def lambda_4B7C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4B7C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_0D()
    OP_6F(0x1)

    #N0255
    NpcTalk(
        0x8,
        "男人的声音",
        "#3P——又来了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0256
    ChrTalk(
        0x101,
        "#0005F#6P哎……\x02",
    )

    CloseMessageWindow()
    OP_68(500, 2250, 2500, 3000)
    OP_6F(0x1)

    #C0257
    ChrTalk(
        0x8,
        (
            "#11P我刚刚才说过，\x01",
            "无法马上决定的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        "#11P今天还是请先回——\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0259
    ChrTalk(
        0x8,
        "#11P哦……？\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xA,
        (
            "#5P哎呀，你们好像不是\x01",
            "刚才的那几位啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500, 2250, 0, 3000)

    def lambda_4D23():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D23)
    Sleep(100)

    def lambda_4D40():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D40)
    Sleep(50)

    def lambda_4D5D():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D5D)
    Sleep(80)

    def lambda_4D7A():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4D7A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0261
    ChrTalk(
        0x8,
        "#11P哦、哦哦……真是失礼了。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        "#0000F#6P那个……打扰了。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#0100F#6P十分抱歉，\x01",
            "打扰您忙正事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x8,
        (
            "#11P啊……\x01",
            "没什么，不必在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        "#11P那个……你们是？\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0266
    AnonymousTalk(
        0x101,
        (
            "#1P——我们是克洛斯贝尔警察局·特别\x01",
            "任务支援科的成员。\x02\x03",

            "关于发生在这里的魔兽侵害事件，\x01",
            "想向您了解一些情况……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1080, 2950, 3060, 0)
    MoveCamera(322, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33750, 0)
    OP_68(1080, 1950, 3060, 4000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 2450, 950, 2780, 270)
    SetChrPos(0x102, 2450, 950, 3780, 270)
    SetChrPos(0x103, 1100, 950, 1500, 0)
    SetChrPos(0x104, 1100, 950, 5100, 180)
    SetChrPos(0x8, -800, 950, 2780, 90)
    SetChrPos(0xA, -800, 950, 3780, 90)
    SetChrChipByIndex(0x8, 0x6)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xB, 0xC)
    SetChrSubChip(0xB, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0267
    ChrTalk(
        0x8,
        (
            "#5P原来如此……\x01",
            "是市里的警察啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "#5P我还以为是游击士协会的\x01",
            "新人来造访了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#0012F#12P……那个，我们经常听到类似感想。\x02\x03",

            "#0001F言归正传吧……\x01",
            "我们已经向镇上的\x01",
            "很多居民询问过了。\x02\x03",

            "看来，这种恶性伤害\x01",
            "似乎还在不断地持续着……？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x8,
        (
            "#5P嗯……至今为止，\x01",
            "已经有三起受害事件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#5P每一次都是在晚上发生的，\x01",
            "刚开始时并没有人员伤亡……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        "#5P可在数日前，却出现了受伤者。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xA,
        (
            "#11P虽说只是轻伤，算是不幸中的万幸，\x01",
            "但现在的受害情况真是越来越严重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "#11P所以镇上的人\x01",
            "也都非常害怕……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#0003F#12P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        (
            "#0101F#2P那个，\x01",
            "警备队在镇上巡逻期间，\x01",
            "真的没有发生过任何情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x8,
        "#5P嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#5P看样子，那群狼\x01",
            "还真是相当聪明啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        "#5P可是，警备队也够无能的！\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "#5P明明什么都没有解决，\x01",
            "竟然就这样把我们扔下不管了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        "#5P你们也是这么想的吧！？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        (
            "#0006F#12P嗯……的确啊。\x01",
            "（虽然他们好像有很多苦衷……）\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x104,
        (
            "#0305F#2P话说回来，你们没有向\x01",
            "游击士协会发出委托吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "#5P其实，在警备队到来之前，\x01",
            "我们就向游击士协会发起过一次委托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#5P但是，他们好像一直\x01",
            "都很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "#5P也不能让他们每天来这里进行警备工作，\x01",
            "所以最后还是警备队出动了，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        (
            "#0203F#6P就在今天早上，\x01",
            "警备队突然撤退了……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "#5P是啊……\x01",
            "真是祸不单行呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x8,
        (
            "#5P因为实在是没办法了，\x01",
            "所以就算希望渺茫，我们本来也还是打算\x01",
            "联系游击士协会，再商量一下对策……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        "#5P就在这个时候，那帮人来了。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        "#0001F#12P他们是『鲁巴彻商会』的人吧。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x102,
        (
            "#0101F#2P那个……\x01",
            "他们到底有何目的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        "#5P他们提议……\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "#5P代替撤走的警备队，\x01",
            "给我们当保镖。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        "#5P还说，不管魔兽什么时候出现都没有问题。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0296
    ChrTalk(
        0x101,
        "#0005F#12P保、保镖……？\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x104,
        (
            "#0301F#2P不用问……\x01",
            "肯定不是免费的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x8,
        (
            "#5P不……\x01",
            "他们好像不要现金。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "#5P但作为回报，他们希望在这段时间里\x01",
            "独占七耀石的采购权。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#0105F#2P独占七耀石的采购权……\x02\x03",

            "#0101F我记得，矿山的开采权\x01",
            "是属于自治州的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        (
            "#5P嗯，为了防止过度开采，\x01",
            "必须遵守政府规定的开采量。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x8,
        (
            "#5P因为七耀石有国际通行的交易价格，\x01",
            "所以不能以过高的价格进行交易。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "#5P不过，开采出来的七耀石\x01",
            "要交给哪里收购，\x01",
            "倒是由镇上自行斟酌决定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        (
            "#0200F#6P所以，对他们而言，\x01",
            "这就成了提供护卫\x01",
            "的交换条件，而且十分划算。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xA,
        (
            "#5P话虽如此，但我们毕竟还有\x01",
            "其他一些老客户……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xA,
        (
            "#5P所以我一直在犹豫，\x01",
            "到底该怎么办才好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#0103F#2P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#0306F#2P哎呀呀，和这群奇怪的家伙扯上关系，\x01",
            "事情就变得麻烦了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0309
    ChrTalk(
        0x101,
        (
            "#0003F#12P——镇长，如果可以的话，\x01",
            "这件事情能不能交给我们处理？\x02\x03",

            "#0000F说不定……\x01",
            "我们能够解决呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x104, 0x1)

    #C0310
    ChrTalk(
        0x102,
        "#0105F#2P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        "#0205F#6P……罗伊德前辈……？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "#5P嗯……你们是叫\x01",
            "『特别任务支援科』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x8,
        (
            "#5P不拜托警备队和游击士，\x01",
            "拜托你们这些市里的警察也没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0004F#12P嗯，请交给我们吧。\x02\x03",

            "#0000F我想，如果顺利的话，\x01",
            "明天就能全部解决了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(34250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
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
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x5C, 0)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_4998 end

    def Function_15_5BD5(): pass

    label("Function_15_5BD5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch00802.itc", 0x22)
    LoadChrToIndex("chr/ch20102.itc", 0x24)
    OP_68(600, 2450, -6850, 0)
    MoveCamera(317, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23150, 0)
    SetChrPos(0x101, -120, 750, -5500, 0)
    SetChrPos(0x102, 240, 750, -6920, 0)
    SetChrPos(0x103, 590, 750, -8250, 0)
    SetChrPos(0x104, 180, 660, -9440, 0)
    SetChrPos(0x109, -880, 750, -7550, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrPos(0x8, 970, 750, -210, 0)
    SetChrPos(0xA, -6080, 750, -320, 270)
    FadeToBright(1000, 0)
    OP_68(600, 2450, -5350, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0315
    ChrTalk(
        0x101,
        (
            "#0000F#6P——打扰了，\x01",
            "我们是特别任务支援科的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    #C0316
    ChrTalk(
        0x8,
        "#11P哦哦，等你们很久了。\x02",
    )

    CloseMessageWindow()
    OP_68(600, 2450, -3350, 2500)

    def lambda_5D4A():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D4A)

    def lambda_5D5F():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D5F)

    def lambda_5D74():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D74)

    def lambda_5D89():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D89)

    def lambda_5D9E():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5D9E)

    def lambda_5DB3():
        OP_95(0xFE, -190, 750, -830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5DB3)
    TurnDirection(0xA, 0x103, 500)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)

    #C0317
    ChrTalk(
        0x8,
        "#11P特意叫你们过来，真是不好意思。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#11P其实我本来是想\x01",
            "去市里找你们的……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#0004F#6P请别在意，我们刚才正好在附近执行任务，\x01",
            "所以顺路就过来了。\x02\x03",

            "#0001F那么……\x01",
            "能不能马上进入正题呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        "#11P嗯，请坐吧。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xA,
        "#5P马上就给你们泡茶哦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(840, 2950, 3300, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19000, 0)
    OP_68(840, 1950, 3300, 3000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x101, 2450, 950, 2780, 270)
    SetChrPos(0x102, 2450, 950, 3880, 270)
    SetChrPos(0x103, 1100, 950, 1500, 0)
    SetChrPos(0x104, 1450, 950, 5100, 180)
    SetChrPos(0x109, 400, 950, 5100, 180)
    SetChrPos(0x8, -800, 950, 2780, 90)
    SetChrPos(0xA, -800, 950, 3880, 90)
    SetChrChipByIndex(0x8, 0x6)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0322
    ChrTalk(
        0x101,
        (
            "#0003F#12P——原来是这样。\x02\x03",

            "#0001F那么，那位叫冈兹的矿工，\x01",
            "自从两周前去了克洛斯贝尔市之后，\x01",
            "就再也没有回来过吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x8,
        "#5P嗯，是的……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        "#5P怎么说呢。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "#5P虽然他以前也是每到周末\x01",
            "就会去克洛斯贝尔欢乐街的\x01",
            "『巴鲁卡』里疯玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xA,
        (
            "#11P但这次他已经整整两周没有回来了，\x01",
            "而且一次都没有联系过镇里……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xA,
        (
            "#11P大家都很担心，\x01",
            "不知他是不是出了什么意外。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        "#0108F#12P的确……这真是让人担心啊。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#0208F#6P不知是被卷入了什么事件，\x01",
            "还是突然有什么要紧事，导致无法回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x109,
        (
            "#0506F#11P唔，\x01",
            "但愿他没有跑到市外，\x01",
            "然后被魔兽袭击啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0331
    ChrTalk(
        0x104,
        (
            "#0305F#11P——话说，那位矿工\x01",
            "有没有可能是在『巴鲁卡』里\x01",
            "赢了一大笔米拉呢？\x02\x03",

            "#0309F然后，他现在正在米修拉姆\x01",
            "带着女孩子们痛痛快快地玩着。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0332
    ChrTalk(
        0x101,
        (
            "#0006F#12P不会吧……\x01",
            "他又不是兰迪。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        (
            "#0202F#6P但是，\x01",
            "这种可能性还是不能否定的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        "#5P啊，那个……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x8,
        (
            "#5P很遗憾，我觉得\x01",
            "并没有这个可能……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0336
    ChrTalk(
        0x101,
        "#0005F#12P这是为什么呢？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x102,
        (
            "#0102F#12P虽然他喜欢玩牌，\x01",
            "但骨子里还是个很正派的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#5P哈哈，就算只是客套话，\x01",
            "正派这个词也都有点夸张呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        (
            "#5P总之，他的技术很差，属于那种\x01",
            "一直输却又一直坚持的类型。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x8,
        (
            "#5P而且，他既没有好运，也没有敏锐的直觉，\x01",
            "每次都会把身上的米拉全部输光，\x01",
            "然后才垂头丧气地回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#0012F#12P原、原来是这样……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#0303F#11P的确，抽奖倒是有可能抽中大奖。\x01",
            "但玩牌的话，如果没有实力，\x01",
            "是很难有很大斩获的。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x103,
        (
            "#0211F#6P那么，会不会是在市里借了债，\x01",
            "然后又还不上，所以自己躲起来玩失踪呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        (
            "#0106F#12P有、有道理……\x01",
            "的确有这种可能性呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        (
            "#5P……其实我们也\x01",
            "有过这种怀疑。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xA,
        (
            "#11P如果真是这样，\x01",
            "要怎样才能联系上他呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0347
    ChrTalk(
        0x101,
        (
            "#0004F#12P——我明白了，\x01",
            "这件事情就交给我们吧。\x02\x03",

            "#0000F总之，从『巴鲁卡』开始，\x01",
            "到冈兹先生可能会去的地方\x01",
            "打听一下他的消息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "#5P谢谢你们……\x01",
            "万事拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x8,
        (
            "#5P如果有什么消息，\x01",
            "请马上联络我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        (
            "#0000F#12P嗯，那么，\x01",
            "请把您的通讯号码告诉我吧……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
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
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x8, 0x5)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x24)
    OP_68(-500, 2250, -3500, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    SetChrPos(0x0, -500, 750, -3500, 180)
    SetChrPos(0x1, -500, 750, -3500, 180)
    SetChrPos(0x2, -500, 750, -3500, 180)
    SetChrPos(0x3, -500, 750, -3500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x8, -1200, 750, 600, 180)
    SetChrPos(0xA, -6530, 750, 60, 270)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xC1, 2)
    OP_29(0x4A, 0x1, 0x2)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_5BD5 end

    def Function_16_6937(): pass

    label("Function_16_6937")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-70, 2450, -3180, 0)
    MoveCamera(309, 28, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(29780, 0)
    SetChrPos(0x101, 0, 750, -2700, 0)
    SetChrPos(0x102, -1300, 750, -2700, 0)
    SetChrPos(0x103, 0, 0, -4000, 0)
    SetChrPos(0x104, -1300, 0, -4000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69D0")
    OP_93(0x8, 0x0, 0x0)
    Jump("loc_69D7")

    label("loc_69D0")

    OP_93(0x8, 0xB4, 0x0)

    label("loc_69D7")

    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E73")

    #C0351
    ChrTalk(
        0x8,
        "#11P嗯……真头疼啊……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x8,
        (
            "#11P再怎么说，也不能让矿山长\x01",
            "一个人前去消灭它们啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#6P#0000F您好，比克森镇长。\x02\x03",

            "特别任务支援科成员已经到达。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0354
    ChrTalk(
        0x8,
        (
            "#11P哦哦，是你们……！\x01",
            "我等你们很久啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x102,
        (
            "#6P#0100F是您发出了支援请求吧。\x02\x03",

            "听说矿山里\x01",
            "出现了魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        "#11P嗯……正是如此。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x8,
        (
            "#11P其实，在矿山的深处，\x01",
            "有个已经停止开采的废坑……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#11P每天晚上，\x01",
            "魔兽都会在里面折腾，\x01",
            "让人很头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#6P#0005F矿山里有魔兽出现吗……\x01",
            "这实在是很糟糕啊。\x02\x03",

            "这种事情难道\x01",
            "很常见吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x103,
        (
            "#6P#0203F……七耀石的开采地附近\x01",
            "会出现大量的魔兽，\x01",
            "每个国家都有很多类似的报告。\x02\x03",

            "#0200F虽然不知道原因，\x01",
            "但七耀石好像有种\x01",
            "吸引魔兽的特性。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#6P#0301F这么说来，\x01",
            "我好像也听说过很多次呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#6P#0105F我也听说过呢，\x01",
            "好像无论哪个国家\x01",
            "的矿山里都有些危险的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        "#6P#0003F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x8,
        (
            "#11P如果只是矿山里的魔兽，\x01",
            "在一般情况下，只靠矿工们\x01",
            "也能够驱赶掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x8,
        (
            "#11P但因为正赶上纪念庆典的假期，\x01",
            "年轻的矿工们都出镇了。\x01",
            "所以事态没法得到及时应对。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#11P虽然废坑的入口已经封锁起来了……\x01",
            "但是，如果再这样放着不管，\x01",
            "不知道会发生什么危险的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#11P所以我请你们来，\x01",
            "想让你们帮忙消灭魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x8,
        (
            "#11P怎么样，\x01",
            "愿意接受吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1C, 0x1, 0x0)
    Jump("loc_6F1A")

    label("loc_6E73")


    #C0369
    ChrTalk(
        0x8,
        (
            "#11P其实，在矿山的深处，\x01",
            "有个已经停止开采的废坑……\x01",
            "魔兽就在里面折腾。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        (
            "#11P我希望你们\x01",
            "在纪念庆典结束之前，\x01",
            "将里面的魔兽消灭。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x8,
        (
            "#11P怎么样。\x01",
            "可以接受吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F1A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6F58"),
        (1, "loc_70E2"),
        (SWITCH_DEFAULT, "loc_71A4"),
    )


    label("loc_6F58")

    OP_60(0x0)

    #C0372
    ChrTalk(
        0x101,
        (
            "#6P#0000F明白了，\x01",
            "我们接受\x01",
            "您的请求。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        "#11P……是吗，太感谢了。\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "#11P那么，\x01",
            "请收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0375
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x346),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x346, 1)

    #C0376
    ChrTalk(
        0x8,
        (
            "#11P去废墟的话，就要找到矿山深处的门，\x01",
            "使用这把钥匙就能进去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#11P那么，就拜托你们了，\x01",
            "请务必要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0378
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【讨伐矿山的魔兽】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x1C, 0x1, 0x1)
    SetScenarioFlags(0x1, 0)
    Jump("loc_71B3")

    label("loc_70E2")

    OP_60(0x0)

    #C0379
    ChrTalk(
        0x101,
        (
            "#6P#0006F对不起……\x01",
            "我们不能马上接受。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        "#11P嗯，这样啊……\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11P矿山暂时还是安全的，\x01",
            "但如果再放着不管，恐怕就控制不住事态了。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#11P等你们有空接受的时候，\x01",
            "再麻烦你们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71B3")

    label("loc_71A4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71B3")

    label("loc_71B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x0, -610, 750, -2790, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_6937 end

    def Function_17_71E4(): pass

    label("Function_17_71E4")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-70, 2450, -3180, 0)
    MoveCamera(309, 28, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(29780, 0)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1010, 750, -630, 180)
    SetChrPos(0x101, 0, 750, -2700, 0)
    SetChrPos(0x102, -1300, 750, -2700, 0)
    SetChrPos(0x103, 0, 0, -4000, 0)
    SetChrPos(0x104, -1300, 0, -4000, 0)
    OP_4B(0x8, 0xFF)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0383
    ChrTalk(
        0x8,
        (
            "#11P嗯，你们好像已经把\x01",
            "魔兽全部消灭了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        "#6P#0000F嗯，已经确认过了，全部歼灭。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x103,
        (
            "#6P#0200F短时间内，魔兽应该\x01",
            "不会再出现了。\x02\x03",

            "至少在纪念庆典结束，\x01",
            "矿工们回来之前的这段时间里，\x01",
            "安全性还是能够保证的。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x8,
        (
            "#11P哦哦，这样啊……\x01",
            "真不知道该如何感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        (
            "#11P……对了，\x01",
            "不介意的话，\x01",
            "请收下这些吧。\x02",
        )
    )

    CloseMessageWindow()
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)
    Sound(17, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0388
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２００\x01\x07\x02",

            "#57I水之耀晶片×２００\x01\x07\x02",

            "#58I火之耀晶片×２００\x01\x07\x02",

            "#59I风之耀晶片×２００\x01\x07\x02",

            "#62I时之耀晶片×２００\x01\x07\x02",

            "#60I空之耀晶片×２００\x01\x07\x02",

            "#61I幻之耀晶片×２００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0389
    ChrTalk(
        0x103,
        "#6P#0205F给我们这么多耀晶片……？\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x104,
        (
            "#6P#0309F哇，真的可以\x01",
            "收下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#6P#0011F当、当然不能收吧！？\x02\x03",

            "#0003F镇长，\x01",
            "我们和游击士不同，\x01",
            "不能直接收取报酬。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x102,
        (
            "#6P#0105F而且，这些耀晶片\x01",
            "都是在这里开采出来的\x01",
            "贵重商品吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        "#11P别介意，没问题的。\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x8,
        (
            "#11P耀晶片是七耀石的碎片……\x01",
            "换句话说，只是在开采时\x01",
            "顺便挖出来的副产品而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x8,
        (
            "#11P如果是政府严格规定交易量的\x01",
            "七耀石，自然不能这么随便就给你们，\x01",
            "但只是耀晶片的话，就完全没有问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x8,
        (
            "#11P而且，只能把这些多余的\x01",
            "东西送给你们，\x01",
            "我才应该说声抱歉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        "#6P#0005F哪、哪里的话……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x8,
        (
            "#11P呵呵……都已经\x01",
            "麻烦过你们好多次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x8,
        (
            "#11P就当作是我个人的谢礼，\x01",
            "请不必客气，收下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0400
    ChrTalk(
        0x101,
        (
            "#6P#0003F……我明白了。\x01",
            "这样的话……\x01",
            "我们就心怀感激地收下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x8,
        "#11P嗯。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x8,
        (
            "#11P那么，这次的事情，\x01",
            "我要再次向你们表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x8,
        "#11P如果以后又有什么事情，还要再麻烦你们啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0404
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【讨伐矿山的魔兽】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1C, 0x4, 0x10)
    SetScenarioFlags(0x1, 0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -610, 750, -2790, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_71E4 end

    SaveToFile()

Try(main)
