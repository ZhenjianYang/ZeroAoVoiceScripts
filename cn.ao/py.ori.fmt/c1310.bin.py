from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1310.bin",                # FileName
        "c1310",                    # MapName
        "c1310",                    # Location
        0x001C,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 28, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1310",                  # 0
        "警备员汪古",             # 1
        "警备员珀尔",             # 2
        "接待小姐兰菲",           # 3
        "接待小姐柯琳娜",         # 4
        "贸易商利泽罗",           # 5
        "市民",                   # 6
        "罗伯兹主任",             # 7
        "约纳",                   # 8
        "迪塔市长",               # 9
        "玛丽亚贝尔",             # 10
    ))

    AddCharChip((
        "chr/ch27900.itc",                   # 00
        "chr/ch29300.itc",                   # 01
        "chr/ch28600.itc",                   # 02
        "chr/ch30500.itc",                   # 03
        "chr/ch21800.itc",                   # 04
        "chr/ch27702.itc",                   # 05
    ))

    DeclNpc(8500,    0,       13310,   270,  257,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-5730,   300,     29909,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       300,     31700,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7110,    300,     32759,   90,   257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-4840,   0,       18180,   90,   261,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(6570,    300,     29760,   0,    385,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(6500,    0,       17850,   270,  385,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 30,  9.5,                   16.0,                  -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.75,                 -5.333333492279053,    0.10000000894069672,   1.0])

    DeclActor(0,       300,     30300,   1500,    0,       1800,    31700,   0x007E, 0,  4,  0x0000)
    DeclActor(6650,    300,     31080,   1500,    7110,    1800,    32759,   0x007E, 0,  10, 0x0000)

    ChipFrameInfo(744, 0)                                        # 0

    ScpFunction((
        "Function_0_2E8",          # 00, 0
        "Function_1_3A0",          # 01, 1
        "Function_2_551",          # 02, 2
        "Function_3_558",          # 03, 3
        "Function_4_5B4",          # 04, 4
        "Function_5_5B8",          # 05, 5
        "Function_6_712",          # 06, 6
        "Function_7_1B0B",         # 07, 7
        "Function_8_2114",         # 08, 8
        "Function_9_211E",         # 09, 9
        "Function_10_2225",        # 0A, 10
        "Function_11_2229",        # 0B, 11
        "Function_12_2DD3",        # 0C, 12
        "Function_13_386E",        # 0D, 13
        "Function_14_3BF6",        # 0E, 14
        "Function_15_45F3",        # 0F, 15
        "Function_16_4EC0",        # 10, 16
        "Function_17_62B2",        # 11, 17
        "Function_18_62DB",        # 12, 18
        "Function_19_62F2",        # 13, 19
        "Function_20_6309",        # 14, 20
        "Function_21_6320",        # 15, 21
        "Function_22_6337",        # 16, 22
        "Function_23_7C50",        # 17, 23
        "Function_24_930E",        # 18, 24
        "Function_25_955A",        # 19, 25
        "Function_26_9642",        # 1A, 26
        "Function_27_97C5",        # 1B, 27
        "Function_28_9A5E",        # 1C, 28
        "Function_29_9AC0",        # 1D, 29
        "Function_30_A5CB",        # 1E, 30
    ))


    def Function_0_2E8(): pass

    label("Function_0_2E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_328"),
        (1, "loc_334"),
        (2, "loc_340"),
        (3, "loc_34C"),
        (4, "loc_358"),
        (5, "loc_364"),
        (6, "loc_370"),
        (SWITCH_DEFAULT, "loc_37C"),
    )


    label("loc_328")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_334")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_340")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_34C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_358")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_364")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_370")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_37C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_388")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_39F")

    Return()

    # Function_0_2E8 end

    def Function_1_3A0(): pass

    label("Function_1_3A0")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9")
    ClearScenarioFlags(0x25, 1)
    Event(0, 2)

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3F0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_4F4")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_417")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_4F4")

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_425")
    Jump("loc_4F4")

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_433")
    Jump("loc_4F4")

    label("loc_433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_446")
    SetChrFlags(0xB, 0x10)
    Jump("loc_4F4")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_454")
    Jump("loc_4F4")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_462")
    Jump("loc_4F4")

    label("loc_462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_470")
    Jump("loc_4F4")

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_497")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_4F4")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B4")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4F4")

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4EB")
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D1")
    SetChrFlags(0xB, 0x10)

    label("loc_4D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E6")
    ClearChrFlags(0xE, 0x80)

    label("loc_4E6")

    Jump("loc_4F4")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4F4")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_511")
    ClearScenarioFlags(0x22, 1)
    SetChrPos(0x0, 60, 300, 28550, 0)

    label("loc_511")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53A")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_550")
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_550")

    Return()

    # Function_1_3A0 end

    def Function_2_551(): pass

    label("Function_2_551")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_551 end

    def Function_3_558(): pass

    label("Function_3_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_59D")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_59D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('ＩＢＣ认证卡片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5B3")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_5B3")

    Return()

    # Function_3_558 end

    def Function_4_5B4(): pass

    label("Function_4_5B4")

    Call(0, 5)
    Return()

    # Function_4_5B4 end

    def Function_5_5B8(): pass

    label("Function_5_5B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E1")
    Call(0, 29)
    Return()

    label("loc_5E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")
    Call(0, 24)
    Jump("loc_620")

    label("loc_61D")

    Call(0, 26)

    label("loc_620")

    Return()

    label("loc_621")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A")
    Call(0, 22)
    Return()

    label("loc_64A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65F")
    Call(0, 6)
    Jump("loc_70E")

    label("loc_65F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "换钱\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D9")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_709")

    label("loc_6D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6ED")
    Jump("loc_709")

    label("loc_6ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_709")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_709")

    Jump("loc_669")

    label("loc_70E")

    TalkEnd(0xA)
    Return()

    # Function_5_5B8 end

    def Function_6_712(): pass

    label("Function_6_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_720")
    Jump("loc_1B0A")

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_72E")
    Jump("loc_1B0A")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_815")

    #C0001
    ChrTalk(
        0xA,
        (
            "玛因兹竟然被占领了……\x01",
            "而且连普通民众都被卷了进去。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "虽然很担心这会对ＩＢＣ带来多大的影响，\x01",
            "但事到如今，已经不是顾虑股票涨跌\x01",
            "问题的时候了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xA,
        (
            "总之，现在就先祈祷\x01",
            "身在玛因兹的大家都平安无事吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8B0")

    label("loc_815")


    #C0004
    ChrTalk(
        0xA,
        (
            "虽然很担心玛因兹事件会对ＩＢＣ带来多大的影响，\x01",
            "但事到如今，已经不是顾虑股票涨跌\x01",
            "问题的时候了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        (
            "总之，现在就先祈祷\x01",
            "身在玛因兹的大家都平安无事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B0")

    Jump("loc_1B0A")

    label("loc_8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99A")

    #C0006
    ChrTalk(
        0xA,
        (
            "导力网络这东西，\x01",
            "真是接触得越久，\x01",
            "越让人感到魅力无穷啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        (
            "柯琳娜说她最喜欢\x01",
            "导力游戏，\x01",
            "而我最喜欢的则是天气预报。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xA,
        (
            "虽然并未达到百分之百，\x01",
            "但准确率还是非常高的，\x01",
            "我每天都怀着敬佩的心情查阅。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A03")

    label("loc_99A")


    #C0009
    ChrTalk(
        0xA,
        (
            "导力网络上放出的\x01",
            "天气预报相当准确。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "顺便一提，今天的预报是\x01",
            "『雨转晴，\x01",
            "　预计在午后彻底放晴』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A03")

    Jump("loc_1B0A")

    label("loc_A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFB")

    #C0011
    ChrTalk(
        0xA,
        (
            "柯琳娜操作终端的技术……\x01",
            "不对，该说她玩导力游戏的技术\x01",
            "在公司里是数一数二的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "所以爱普斯泰恩财团\x01",
            "时常会委托她测试\x01",
            "各种游戏软件。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "不过，虽说是委托，但其实也\x01",
            "只是在工作之余帮些忙而已。\x01",
            "可以算是义务劳动。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B41")

    label("loc_AFB")


    #C0014
    ChrTalk(
        0xA,
        (
            "话说回来，她面对屏幕时\x01",
            "竟然能那么开心……\x01",
            "呵呵，还真有点羡慕呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B41")

    Jump("loc_1B0A")

    label("loc_B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCD")

    #C0015
    ChrTalk(
        0xA,
        (
            "只要我们能帮上忙，\x01",
            "一定会不遗余力地为各位提供协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "今后要是有什么事，\x01",
            "请不必客气，随时过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C41")

    label("loc_BCD")


    #C0017
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔总裁代理\x01",
            "昨天已经结束出差，\x01",
            "平安归来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "今天一大早，\x01",
            "她又开始对各部门进行调整，\x01",
            "忙得不可开交。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C41")

    Jump("loc_1B0A")

    label("loc_C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1452")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D5")

    #C0019
    ChrTalk(
        0xA,
        (
            "啊，各位。\x01",
            "玛丽亚贝尔总裁代理\x01",
            "正在外国出差……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 0)), scpexpr(EXPR_END)), "loc_D00")

    #C0020
    ChrTalk(
        0x101,
        (
            "#00005F玛丽亚贝尔『总裁代理』……\x02\x03",

            "#00003F哦，我想起来了，克洛斯贝尔时代周刊\x01",
            "也刊登了这条消息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D29")

    label("loc_D00")


    #C0021
    ChrTalk(
        0x101,
        "#00005F玛丽亚贝尔『总裁代理』……？\x02",
    )

    CloseMessageWindow()

    label("loc_D29")


    #C0022
    ChrTalk(
        0x102,
        (
            "#00100F嗯，迪塔叔叔把总裁的工作\x01",
            "全部交给董事会接管后，\x01",
            "她立刻就被任命为总裁代理了。\x02\x03",

            "#00104F也就是说，贝尔现在已经是\x01",
            "ＩＢＣ实质性的第一领导。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#00306F如此年轻就坐到了这个位子，\x01",
            "真是让人惊叹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        "#00200F玛丽亚贝尔小姐确实可以服众……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#10106F嗯，越是细想，\x01",
            "就越觉得她很了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#10300F但这样一来，\x01",
            "她的工作量就会比以往\x01",
            "增加很多了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        "嗯，那是必然的。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        (
            "为了减轻大小姐的负担，\x01",
            "董事会正在团结一致地\x01",
            "全力辅佐她……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "但大小姐既然身为总裁代理，\x01",
            "就不得不在各种各样的场所\x01",
            "露面……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00003F原来如此……\x01",
            "看来她确实非常忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "顺便一提，按照预定，\x01",
            "大小姐将在今晚回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "不过，她从明天开始的日程安排\x01",
            "已经被各种各样的会议及会谈\x01",
            "排满了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        (
            "非常抱歉，\x01",
            "我想各位暂时还是无法\x01",
            "与大小姐会面。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1361")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0034
    ChrTalk(
        0xA,
        (
            "对了……\x01",
            "大小姐有话要我\x01",
            "转告给各位。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『玛丽亚贝尔的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x27, 6)
    OP_E4(0x3)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00005F这、这是『波波碰！』的\x01",
            "账号……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#00200F玛丽亚贝尔小姐\x01",
            "也在玩这个吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "#18C『呵呵，作为技术部的\x01",
            "  参与者之一，有此爱好\x01",
            "  也是理所当然的。』\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "#18C『你们一定要添加我的账号哦。\x01",
            "  我会以高超的技术\x01",
            "  把你们打得落花流水。』\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        "……以上就是大小姐留下的传话。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        "#10105F刚才那些话……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00301F难道她已经预料到\x01",
            "罗伊德他们的反应了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#00106F……应该是的，\x01",
            "贝尔确实有能力预料到。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "不愧是艾莉大小姐，\x01",
            "正如您所说。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，确实了不起。\x02\x03",

            "#10302F这位姐姐，你的声音模仿能力\x01",
            "也很不错呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0046
    ChrTalk(
        0xA,
        (
            "哪、哪里……\x01",
            "我有些失态了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            "……总之，\x01",
            "留言就是以上内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "大小姐在出差的时候，\x01",
            "终端也是片刻不离手。\x01",
            "请各位赶快去向她挑战吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#00012F哈哈，这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13CD")

    label("loc_1361")


    #C0050
    ChrTalk(
        0x102,
        (
            "#00104F嗯，知道了。\x02\x03",

            "#00100F兰菲小姐，请帮我\x01",
            "转告贝尔一声，\x01",
            "让她千万别太操劳了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        "好的，我明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_13CD")

    SetScenarioFlags(0x16D, 0)
    Jump("loc_144D")

    label("loc_13D5")


    #C0052
    ChrTalk(
        0xA,
        (
            "按照预定，玛丽亚贝尔总裁代理\x01",
            "将于今晚结束出差，\x01",
            "返回这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "但非常抱歉，\x01",
            "我想各位暂时还是无法\x01",
            "与大小姐会面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144D")

    Jump("loc_1B0A")

    label("loc_1452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_152C")

    #C0054
    ChrTalk(
        0xA,
        (
            "看来今后有必要进一步强化\x01",
            "大楼内的安全措施呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "总之，感谢各位帮玛丽亚贝尔小姐\x01",
            "找回那些被偷走的人偶。\x01",
            "谢谢你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        (
            "如果以后有什么事情，\x01",
            "请随时过来。\x01",
            "我们非常欢迎各位。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_15AC")

    label("loc_152C")


    #C0057
    ChrTalk(
        0xA,
        (
            "总之，感谢各位帮玛丽亚贝尔小姐\x01",
            "找回那些被偷走的人偶。\x01",
            "谢谢你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "如果以后有什么事情，\x01",
            "请随时过来。\x01",
            "我们非常欢迎各位。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AC")

    Jump("loc_16E1")

    label("loc_15B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165D")

    #C0059
    ChrTalk(
        0xA,
        (
            "只要有这张认证卡，\x01",
            "就可以乘坐导力梯了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "可以前往的楼层与\x01",
            "上次给你们卡片时一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔大小姐就在\x01",
            "十六层的总裁室等候你们，\x01",
            "请各位移步。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_16E1")

    label("loc_165D")


    #C0062
    ChrTalk(
        0xA,
        (
            "只要有这张认证卡，\x01",
            "就可以前往与上次给你们\x01",
            "卡片时一样的楼层了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔大小姐就在\x01",
            "十六层的总裁室等候你们，\x01",
            "请各位移步。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E1")

    Jump("loc_1B0A")

    label("loc_16E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16F4")
    Jump("loc_1B0A")

    label("loc_16F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_199F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1944")

    #C0064
    ChrTalk(
        0xA,
        (
            "哦，各位。\x01",
            "欢迎来到ＩＢＣ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "如果有事要办，\x01",
            "请尽量在今天之内处理完毕。\x01",
            "因为明天是临时休息日。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00005F临时休息日？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#00100F听说共和国的洛克史密斯总统\x01",
            "明天下午\x01",
            "要来ＩＢＣ视察。\x02\x03",

            "是因为这件事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "不愧是艾莉大小姐，消息真灵通。\x01",
            "没错，正如您所说。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        (
            "不管怎么说，\x01",
            "洛克史密斯总统可是\x01",
            "贵宾中的贵宾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "视察当天，大楼内各企业的\x01",
            "工作人员将全部离开现场，\x01",
            "我们要以万全的安全体制迎接总统。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x109,
        (
            "#10103F原来如此，要采取和米修拉姆\x01",
            "同等级别的应对措施啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        "#00306F嗯，这也是理所当然的。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#00000F我们已经明白了。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#00100F多谢您的详细说明。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 7)
    Jump("loc_199A")

    label("loc_1944")


    #C0075
    ChrTalk(
        0xA,
        (
            "ＩＢＣ明天将\x01",
            "临时休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "各位如果有什么事情要办，\x01",
            "请尽量在今天之内处理完毕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_199A")

    Jump("loc_1B0A")

    label("loc_199F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A8A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A10")

    #C0077
    ChrTalk(
        0xA,
        (
            "看来你们已经顺利完成了\x01",
            "主任的委托啊。\x01",
            "呵呵，辛苦各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "我也要向各位\x01",
            "道谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A85")

    label("loc_1A10")


    #C0079
    ChrTalk(
        0xA,
        (
            "罗伯兹主任在ＩＢＣ大楼内的\x01",
            "爱普斯泰恩财团分部任职，\x01",
            "他总是非常忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "在导力网络方面，\x01",
            "我们时常承蒙他关照。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A85")

    Jump("loc_1B0A")

    label("loc_1A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA5")
    Call(0, 7)
    Jump("loc_1B0A")

    label("loc_1AA5")


    #C0081
    ChrTalk(
        0xA,
        (
            "我们会尽可能地向\x01",
            "特别任务支援科的各位\x01",
            "提供方便。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "各位今后要是有什么事情，\x01",
            "随时都可以过来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0A")

    Return()

    # Function_6_712 end

    def Function_7_1B0B(): pass

    label("Function_7_1B0B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-370, 1800, 29450, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, -770, 300, 29530, 0)
    SetChrPos(0x102, 430, 300, 29130, 0)
    SetChrPos(0x109, -1270, 300, 28130, 0)
    SetChrPos(0x105, 530, 300, 27920, 0)
    OP_4B(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()
    Sleep(100)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0083
    ChrTalk(
        0xA,
        (
            "#5P啊，罗伊德警官，艾莉小姐。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "#5P看来特别任务支援科\x01",
            "已经重新开始工作了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#12P#00000F嗯，托您的福。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#12P#00100F今后也请\x01",
            "多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        "#5P嗯，当然。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DEA")

    #C0088
    ChrTalk(
        0xA,
        (
            "#5P对了，以前我们好像拜托过\x01",
            "支援科的各位帮忙测试\x01",
            "新的兑换米拉服务系统……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            "#5P其实那时候交给大家的卡片\x01",
            "已经过了有效期限。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "#5P我们已经为大家准备了新的卡片，\x01",
            "请各位收下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0091
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ贵宾卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ贵宾卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0092
    ChrTalk(
        0xA,
        (
            "#5P请像以前一样在服务台\x01",
            "出示这张卡片。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#5P这样就能以比一般更高的汇率\x01",
            "将耀晶片换成米拉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F09")

    label("loc_1DEA")


    #C0094
    ChrTalk(
        0xA,
        (
            "#5P对了，有样东西要\x01",
            "交给各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        "#5P请收下这个吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0096
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ贵宾卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ贵宾卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0097
    ChrTalk(
        0x101,
        "#12P#00005F这个卡片是……？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "#5P这张卡可以证明\x01",
            "各位是本行的\x01",
            "特别会员。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "#5P只要向服务台出示这张卡片，\x01",
            "就能以比一般更高的汇率\x01",
            "将耀晶片换成米拉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F09")


    #C0100
    ChrTalk(
        0x109,
        (
            "#12P#10105F我、我们可以接受\x01",
            "这样的服务吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "#5P当然啦。因为各位是\x01",
            "库罗伊斯市长，还有玛丽亚贝尔\x01",
            "大小姐重要的朋友啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        "#5P为你们提供点方便是理所当然的。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，那我们就不客气地\x01",
            "收下这个了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#12P#00000F下次来时一定会使用这张卡的。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        "#5P呵呵，期待你们的下次光临。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ＩＢＣ的兑换服务已经可以使用了。\x01",
            "　可以将耀晶片以高于通常市值的\x01",
            "　汇率兑换成米拉。\x02\x03",

            "※和兰菲对话，\x01",
            "　并选择『换钱』，\x01",
            "  再选择『EXCHANGE』即可进行兑换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x134, 4)
    EventEnd(0x5)
    Return()

    # Function_7_1B0B end

    def Function_8_2114(): pass

    label("Function_8_2114")

    TalkBegin(0xFE)
    Call(0, 9)
    TalkEnd(0xFE)
    Return()

    # Function_8_2114 end

    def Function_9_211E(): pass

    label("Function_9_211E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219E")
    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0107
    ChrTalk(
        0xB,
        (
            "请稍等一下～\x01",
            "（哒哒哒，哒哒哒……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xB,
        (
            "我马上帮您\x01",
            "查询合约内容～\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xD,
        "嗯，拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2224")

    label("loc_219E")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)

    #C0110
    ChrTalk(
        0xD,
        (
            "嗯？干什么？\x01",
            "难道你想\x01",
            "插队吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "非常抱歉，\x01",
            "请在旁边的沙发上\x01",
            "稍等一下，按顺序来～\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xB, 0x5A, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_2224")

    Return()

    # Function_9_211E end

    def Function_10_2225(): pass

    label("Function_10_2225")

    Call(0, 11)
    Return()

    # Function_10_2225 end

    def Function_11_2229(): pass

    label("Function_11_2229")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_223A")
    Jump("loc_2DCF")

    label("loc_223A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2248")
    Jump("loc_2DCF")

    label("loc_2248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2352")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E0")

    #C0112
    ChrTalk(
        0xB,
        (
            "袭击玛因兹的似乎\x01",
            "是群非常危险的人呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "听说是连我们的保安部\x01",
            "都无法对付的级别……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "哎呀呀，\x01",
            "这可不是开玩笑的啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_234D")

    label("loc_22E0")


    #C0115
    ChrTalk(
        0xB,
        (
            "听说那个袭击了玛因兹的武装集团\x01",
            "是连我们的保安部\x01",
            "都无法对付的级别……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xB,
        (
            "哎呀呀，\x01",
            "这可不是开玩笑的啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234D")

    Jump("loc_2DCF")

    label("loc_2352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_23BD")

    #C0117
    ChrTalk(
        0xB,
        (
            "下雨天出门\x01",
            "好麻烦啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        (
            "等导力网络进一步普及之后，\x01",
            "我真想找一份可以\x01",
            "在家上班的工作～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_27DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F6")

    #C0119
    ChrTalk(
        0xB,
        "（哒哒哒哒哒哒，哒哒哒哒……！）\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        "（嗖嗖、嗞哒哒哒哒哒哒！）\x02",
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245C")

    #C0121
    ChrTalk(
        0x101,
        "#00005F这、这到底是什么声音……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2580")

    label("loc_245C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2492")

    #C0122
    ChrTalk(
        0x102,
        "#00105F这、这是什么声音……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2580")

    label("loc_2492")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24DB")

    #C0123
    ChrTalk(
        0x103,
        (
            "#00203F……好像是财团最近开发的\x01",
            "射击游戏的音效。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2580")

    label("loc_24DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2517")

    #C0124
    ChrTalk(
        0x104,
        "#00305F怎、怎么会发出这种声音……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2580")

    label("loc_2517")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254B")

    #C0125
    ChrTalk(
        0x109,
        "#10105F这、这是枪声吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2580")

    label("loc_254B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2580")

    #C0126
    ChrTalk(
        0x105,
        "#10302F呵呵，她看起来好像很开心。\x02",
    )

    CloseMessageWindow()

    label("loc_2580")

    Sleep(50)
    TurnDirection(0xB, 0x0, 0)

    #C0127
    ChrTalk(
        0xB,
        (
            "非常抱歉，各位客人～\x01",
            "现在是我的\x01",
            "休息时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "如果有什么问题，\x01",
            "请去正面服务台咨询吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_27DA")

    label("loc_25F6")


    #C0129
    ChrTalk(
        0xB,
        "（哒哒哒哒哒哒，哒哒哒哒……！）\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        "（嗖嗖、嗞哒哒哒哒哒哒！！）\x02",
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2684")

    #C0131
    ChrTalk(
        0x101,
        "#00012F（真、真是全神贯注啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_27DA")

    label("loc_2684")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C2")

    #C0132
    ChrTalk(
        0x102,
        "#00106F（现、现在最好不要打扰她……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_27DA")

    label("loc_26C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2720")

    #C0133
    ChrTalk(
        0x103,
        (
            "#00205F（很出色的反击……！\x01",
            "  ……看来她的技术已经\x01",
            "  在约纳之上了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DA")

    label("loc_2720")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2762")

    #C0134
    ChrTalk(
        0x104,
        "#00306F（看这样子，实在是不便打扰她啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_27DA")

    label("loc_2762")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A1")

    #C0135
    ChrTalk(
        0x109,
        (
            "#10106F（她、她真是\x01",
            "  全神贯注啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DA")

    label("loc_27A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27DA")

    #C0136
    ChrTalk(
        0x105,
        "#10302F（呵呵，完全融入游戏中了呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_27DA")

    Jump("loc_2DCF")

    label("loc_27DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2869")

    #C0137
    ChrTalk(
        0xB,
        (
            "玛丽亚贝尔大小姐最近\x01",
            "实在是太忙了，\x01",
            "连午饭都没有时间吃～\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "她时常在路上用餐，\x01",
            "据说平时一直都随身携带着\x01",
            "方便食品呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCF")

    label("loc_2869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_29DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2979")

    #C0139
    ChrTalk(
        0xB,
        (
            "自从市长发起独立提案以来，\x01",
            "大陆金融市场的\x01",
            "波动相当巨大呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xB,
        (
            "虽然没有出现极端的倾向性，\x01",
            "但股市的买进和卖出两方都\x01",
            "呈上升趋势。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "而这判断是否正确，\x01",
            "就完全取决于\x01",
            "克洛斯贝尔今后的局势了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "哎呀呀，股市的变动\x01",
            "就如同人生的起伏一般啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_29DA")

    label("loc_2979")


    #C0143
    ChrTalk(
        0xB,
        (
            "利泽罗先生大概是反省了\x01",
            "过往的失败吧，现在似乎\x01",
            "相当谨慎呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        (
            "我个人认为\x01",
            "这是正确的做法～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29DA")

    Jump("loc_2DCF")

    label("loc_29DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACB")

    #C0145
    ChrTalk(
        0xB,
        (
            "由于总统访问，\x01",
            "昨天放了一天假。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "街上戒备森严，实在没什么兴趣出门，\x01",
            "等回过神来之后，\x01",
            "发现我一整天都在床上耗过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "虽说因此恢复了不少精神，\x01",
            "但还是忍不住想到，如果我家\x01",
            "也有导力网络的终端就好了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B3E")

    label("loc_2ACB")


    #C0148
    ChrTalk(
        0xB,
        (
            "昨天待在家里时，\x01",
            "我忍不住想到，如果我家\x01",
            "也有导力网络的终端就好了～\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "那样我就可以在家\x01",
            "玩一整天导力游戏了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3E")

    Jump("loc_2DCF")

    label("loc_2B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B51")
    Jump("loc_2DCF")

    label("loc_2B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B62")
    Call(0, 9)
    Jump("loc_2DCF")

    label("loc_2B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF5")

    #C0150
    ChrTalk(
        0xB,
        "（哒哒哒哒哒、哒哒哒哒……！）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    #C0151
    ChrTalk(
        0xB,
        (
            "下雨的时候，\x01",
            "客人果然会减少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "这正是处理积压工作的\x01",
            "好机会～\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C30")

    label("loc_2BF5")


    #C0153
    ChrTalk(
        0xB,
        (
            "如果不是偶尔会有这种时候，\x01",
            "积压的工作都没机会处理呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C30")

    Jump("loc_2DCF")

    label("loc_2C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D4B")

    #C0154
    ChrTalk(
        0xB,
        (
            "由技术部负责的导力网络\x01",
            "第二次测试终于\x01",
            "结束第一阶段了。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "简单来说，就是可以更迅速、\x01",
            "更安全、更稳定地\x01",
            "接收和发送更多信息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "拜其所赐，几台内部专用终端\x01",
            "也已经可以连接\x01",
            "外部网络了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "这就是由玛丽亚贝尔小姐率领的\x01",
            "技术部工作人员的实力啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DCF")

    label("loc_2D4B")


    #C0158
    ChrTalk(
        0xB,
        (
            "第二次测试的成果\x01",
            "也给库罗伊斯市长\x01",
            "提供了不少方便～\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "他现在已经开始用\x01",
            "导力网络来传送文件了～\x01",
            "当然，仅限于那些机密性较低的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCF")

    TalkEnd(0xB)
    Return()

    # Function_11_2229 end

    def Function_12_2DD3(): pass

    label("Function_12_2DD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2DE4")
    Jump("loc_386A")

    label("loc_2DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DF2")
    Jump("loc_386A")

    label("loc_2DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E61")

    #C0160
    ChrTalk(
        0xFE,
        (
            "听说玛因兹那里\x01",
            "出了大事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "暂时还没有对\x01",
            "金融市场产生影响，\x01",
            "但那应该也只是时间问题了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_386A")

    label("loc_2E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2FEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F3F")

    #C0162
    ChrTalk(
        0xFE,
        (
            "一方获得利益，\x01",
            "就必定有另一方遭受损失……\x01",
            "这可以说是股市的真理。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "此外还有一条……\x01",
            "股票的世界里没有『绝对』。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "如果你打算开始投资，\x01",
            "那我强烈建议你在自己\x01",
            "能承担责任的范畴内运用资金。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2FE9")

    label("loc_2F3F")


    #C0165
    ChrTalk(
        0xFE,
        (
            "如果你打算开始投资，\x01",
            "那我强烈建议你在自己\x01",
            "能承担责任的范畴内运用资金。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "虽说股票的世界里没有绝对……\x01",
            "但我认为，如果尝试超出自己能力\x01",
            "范畴的举动，一定会招致不幸。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE9")

    Jump("loc_386A")

    label("loc_2FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_30DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3078")

    #C0167
    ChrTalk(
        0xFE,
        "什么……？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "今天早上涨得那么厉害的股票\x01",
            "竟然会跌到\x01",
            "这个地步……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "……所以才说\x01",
            "股市的行情变化莫测。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_30D7")

    label("loc_3078")


    #C0170
    ChrTalk(
        0xFE,
        (
            "今天早上涨得那么厉害的股票\x01",
            "竟然会跌到\x01",
            "这个地步……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "……所以才说\x01",
            "股市的行情变化莫测。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D7")

    Jump("loc_386A")

    label("loc_30DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_31C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316E")

    #C0172
    ChrTalk(
        0xFE,
        (
            "唔，今天早晨，\x01",
            "共和国的市价大涨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "我看好的那支股票\x01",
            "也涨了很多……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "不过，现在说什么\x01",
            "也不过是事后论了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_31BC")

    label("loc_316E")


    #C0175
    ChrTalk(
        0xFE,
        (
            "我看好的那支股票\x01",
            "涨了很多呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "不过，现在说什么\x01",
            "也不过是事后论了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BC")

    Jump("loc_386A")

    label("loc_31C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_32D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3272")

    #C0177
    ChrTalk(
        0xFE,
        (
            "最近的股市行情\x01",
            "相当不稳定。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "唔，这种持续动荡起伏，\x01",
            "并且令人难以预测的行情实在少见。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "现在的投资风险相当大……\x01",
            "外行人最好\x01",
            "别轻易出手哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_32CC")

    label("loc_3272")


    #C0180
    ChrTalk(
        0xFE,
        (
            "要是在以前，我肯定会不顾风险地\x01",
            "入市吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "唔，但我现在觉得，\x01",
            "还是不要出手为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32CC")

    Jump("loc_386A")

    label("loc_32D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3381")

    #C0182
    ChrTalk(
        0xFE,
        (
            "身为贸易商，我非常关心\x01",
            "通商会议的进展状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "帝国与共和国一定会\x01",
            "想方设法地坚持自己的主张。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "能让两国让步多少，\x01",
            "就要看迪塔市长的本事了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_33FA")

    label("loc_3381")


    #C0185
    ChrTalk(
        0xFE,
        (
            "在贸易方面的协定中，\x01",
            "帝国与共和国一定会\x01",
            "想方设法地坚持自己的主张。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "能让两国让步多少，\x01",
            "就要看迪塔市长的本事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FA")

    Jump("loc_386A")

    label("loc_33FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_340D")
    Jump("loc_386A")

    label("loc_340D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AE")

    #C0187
    ChrTalk(
        0xFE,
        (
            "不知道是不是受通商会议的影响，\x01",
            "在最近这几天，股票的平均价格\x01",
            "有上涨的倾向。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "我本想买入\x01",
            "几支股票……\x01",
            "但手头的资金完全不够啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_350E")

    label("loc_34AE")


    #C0189
    ChrTalk(
        0xFE,
        (
            "看着这样的市场行情，\x01",
            "真想要买些股票……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "唉，但暂时也只好老老实实地\x01",
            "靠本职工作赚钱了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_350E")

    Jump("loc_386A")

    label("loc_3513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3521")
    Jump("loc_386A")

    label("loc_3521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_386A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_380E")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0191
    ChrTalk(
        0xFE,
        "哎呀，你是特别任务支援科的……\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "你、你还记得我吗？\x01",
            "我是在教团事件中承蒙你们\x01",
            "搭救的贸易商。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#00000F嗯，当然记得。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x102,
        (
            "#00100F在那之后，\x01",
            "您的身体还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "嗯，我现在会定期去\x01",
            "乌尔斯拉医院检查，\x01",
            "身体非常健康哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "那起事件之后，我的公司虽然\x01",
            "欠了不少钱，却没有就此破产……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "当时真是多亏有各位，\x01",
            "我至今依然发自内心地感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "对了，你们可以\x01",
            "收下这个吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0199
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('圣灵药', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0200
    ChrTalk(
        0x101,
        "#00005F这是……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "这是以前从客户那里\x01",
            "得到的东西，\x01",
            "我留着也没什么用。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "而且，我想用实际一点的东西\x01",
            "来向你们报恩。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "这只是个人性质的赠品而已，希望你们\x01",
            "别说不合规矩之类的，收下它就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00000F好的……\x01",
            "既然如此，\x01",
            "那我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 5)
    Jump("loc_386A")

    label("loc_380E")


    #C0205
    ChrTalk(
        0xFE,
        (
            "能再次见到你们，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "当时真是多亏有各位，\x01",
            "我至今依然发自内心地感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_386A")

    TalkEnd(0xFE)
    Return()

    # Function_12_2DD3 end

    def Function_13_386E(): pass

    label("Function_13_386E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ACB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A74")

    #C0207
    ChrTalk(
        0xFE,
        (
            "你们先去把『波波碰！』\x01",
            "安装到支援科的终端上吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "然后用艾尼格玛\x01",
            "联络我。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00000F明白了，\x01",
            "安装完以后再联络您。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        (
            "#10302F话说回来，在警察的终端上\x01",
            "安装游戏，这样好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#00005F啊，你这么一说的话……\x01",
            "是不是应该先去获得批准？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "呵呵，我已经在警察局\x01",
            "得到许可了。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "我对他们说，这是一项\x01",
            "推进导力网络的试验，\x01",
            "所以他们很爽快地批准了。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#00005F这、这样啊……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x109,
        "#10106F（他、他做事可真圆滑呢。）\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        (
            "#00100F（呵呵，毕竟是\x01",
            "  克洛斯贝尔的导力网络\x01",
            "  负责人啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3AC6")

    label("loc_3A74")


    #C0217
    ChrTalk(
        0xFE,
        (
            "你们先去把『波波碰！』\x01",
            "安装到支援科的终端上吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "然后用艾尼格玛\x01",
            "联络我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC6")

    Jump("loc_3BF2")

    label("loc_3ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B79")

    #C0219
    ChrTalk(
        0xFE,
        (
            "感谢你们协助我\x01",
            "测试『波波碰！』。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "等它正式推广以后，\x01",
            "你们可以去搜集\x01",
            "其他玩家的账号。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "扩大玩家范围，和不同的人对战，\x01",
            "才是这款游戏的真正乐趣。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3BF2")

    label("loc_3B79")


    #C0222
    ChrTalk(
        0xFE,
        (
            "等『波波碰！』\x01",
            "正式推广以后，\x01",
            "你们可以多搜集一些账号。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "扩大玩家范围，和不同的人对战，\x01",
            "才是这款游戏的真正乐趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF2")

    TalkEnd(0xFE)
    Return()

    # Function_13_386E end

    def Function_14_3BF6(): pass

    label("Function_14_3BF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C07")
    Jump("loc_45EF")

    label("loc_3C07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C15")
    Jump("loc_45EF")

    label("loc_3C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3CA9")

    #C0224
    ChrTalk(
        0xFE,
        (
            "据说那个武装集团拥有\x01",
            "凌驾在警备队之上的\x01",
            "火力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "听说他们的真正身份是恶名昭彰的\x01",
            "猎兵团『赤色星座』……\x01",
            "那些人到底想干什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45EF")

    label("loc_3CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D02")

    #C0226
    ChrTalk(
        0xFE,
        "你们好像从一大早就很忙啊。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "工作大概有很多吧，\x01",
            "但也不要太拼命哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45EF")

    label("loc_3D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3E24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC8")

    #C0228
    ChrTalk(
        0xFE,
        "快到中午换班的时间了。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "嗯，吃点什么好呢？\x01",
            "今天的Ａ套餐似乎是以肉类为主的……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "……咳咳，不行不行。\x01",
            "还没有到\x01",
            "休息时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "真是的，这是精神松懈的证据啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3E1F")

    label("loc_3DC8")


    #C0232
    ChrTalk(
        0xFE,
        (
            "每当临近用餐时间，我的思绪\x01",
            "总是会飘到食欲那边去。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "唉，看来我的训练还不够啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3E1F")

    Jump("loc_45EF")

    label("loc_3E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3F7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF2")

    #C0234
    ChrTalk(
        0xFE,
        (
            "听说最近在自治州内\x01",
            "出现了来历不明的\x01",
            "怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "我们保安部成员不仅懂得制服罪犯，\x01",
            "在与魔兽交战等方面，\x01",
            "也具备一定程度的能力……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "唔，为了防备万一，\x01",
            "必须要做好心理准备啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3F75")

    label("loc_3EF2")


    #C0237
    ChrTalk(
        0xFE,
        (
            "我们保安部成员不仅懂得制服罪犯，\x01",
            "在与魔兽交战等方面，\x01",
            "也具备一定程度的能力……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "唔，为了防备万一，\x01",
            "必须要做好心理准备啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F75")

    Jump("loc_45EF")

    label("loc_3F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_413D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CF")

    #C0239
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ大楼内设有\x01",
            "职员专用的健身房。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "我们ＩＢＣ保安部的成员自不必说，\x01",
            "一些运动不足的职员\x01",
            "也会积极去那里健身。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "顺便一提，玛丽亚贝尔大小姐\x01",
            "也时常出现在那里哦，\x01",
            "只是最近很少能见到她了。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "她那身着健美服的姿态，\x01",
            "在平时是绝对见不到的，\x01",
            "那香汗淋漓的模样真是……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "怎么说呢……\x01",
            "实在是让人心跳不已啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4138")

    label("loc_40CF")


    #C0244
    ChrTalk(
        0xFE,
        (
            "咳、咳咳……我在最后好像\x01",
            "说了几句多余的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "总、总之，我们公司的\x01",
            "健身设施非常充足，\x01",
            "堪称完美。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4138")

    Jump("loc_45EF")

    label("loc_413D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_432E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41D2")

    #C0246
    ChrTalk(
        0xFE,
        (
            "听说有贼人闯入了\x01",
            "玛丽亚贝尔大小姐的房间……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "可恶，我明明没有看见\x01",
            "可疑人士啊……\x01",
            "完全被骗过去了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_420E")

    label("loc_41D2")


    #C0248
    ChrTalk(
        0xFE,
        (
            "可恶，我明明没有看见\x01",
            "可疑人士啊……\x01",
            "完全被骗过去了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_420E")

    Jump("loc_4329")

    label("loc_4213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42CB")

    #C0249
    ChrTalk(
        0xFE,
        (
            "你们能帮忙找回大小姐\x01",
            "珍爱的人偶，真是太好了。\x01",
            "我也要向你们道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "话说回来，我们保安部居然\x01",
            "完全没能察觉他的气息……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "那个怪盗Ｂ\x01",
            "到底是用了什么手段啊！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4329")

    label("loc_42CB")


    #C0252
    ChrTalk(
        0xFE,
        (
            "话说回来，我们保安部居然\x01",
            "完全没能察觉他的气息……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "那个怪盗Ｂ\x01",
            "到底用了什么手段啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4329")

    Jump("loc_45EF")

    label("loc_432E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_433C")
    Jump("loc_45EF")

    label("loc_433C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_445F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43EE")

    #C0254
    ChrTalk(
        0xFE,
        (
            "通商会议即将召开，\x01",
            "警察和警备队的戒备\x01",
            "更加森严了。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ保安部也会\x01",
            "全面协助他们\x01",
            "进行戒备。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "我们会一直和警察局的\x01",
            "警备对策总部保持联系。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_445A")

    label("loc_43EE")


    #C0257
    ChrTalk(
        0xFE,
        (
            "不管怎么说，在这种时候，\x01",
            "必须要互相帮助才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "如果有什么事需要帮忙，\x01",
            "我们一定会不遗余力地协助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_445A")

    Jump("loc_45EF")

    label("loc_445F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_44D6")

    #C0259
    ChrTalk(
        0xFE,
        (
            "唔，我们的库罗伊斯市长\x01",
            "实在是非常繁忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "多亏有玛丽亚贝尔\x01",
            "大小姐的协助，\x01",
            "各项工作才能顺利完成。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45EF")

    label("loc_44D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_45EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_458F")

    #C0261
    ChrTalk(
        0xFE,
        (
            "哎呀，你们是警察局的\x01",
            "特别任务支援科吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "欢迎来到ＩＢＣ。\x01",
            "大楼内部的安全保障就交给\x01",
            "我们保安部吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "这里的成员在身体能力上\x01",
            "可不会输给警备队员哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_45EF")

    label("loc_458F")


    #C0264
    ChrTalk(
        0xFE,
        (
            "大楼内部的安全保障就交给\x01",
            "我们保安部吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "这里的成员在身体能力上\x01",
            "可不会输给警备队员哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45EF")

    TalkEnd(0xFE)
    Return()

    # Function_14_3BF6 end

    def Function_15_45F3(): pass

    label("Function_15_45F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4604")
    Jump("loc_4EBC")

    label("loc_4604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4612")
    Jump("loc_4EBC")

    label("loc_4612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_468D")

    #C0266
    ChrTalk(
        0xFE,
        (
            "武装集团似乎还没有\x01",
            "提出具体要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "保安部的内部已经出现了\x01",
            "各种各样的推测……\x01",
            "实在是让人毛骨悚然啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EBC")

    label("loc_468D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_46DA")

    #C0268
    ChrTalk(
        0xFE,
        "大家工作辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "外面正在下雨，\x01",
            "请一定要注意身体啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EBC")

    label("loc_46DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4764")

    #C0270
    ChrTalk(
        0xFE,
        (
            "最近几乎没有在这个\x01",
            "ＩＢＣ大楼里见过\x01",
            "迪塔市长呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "虽然我相信市长\x01",
            "一定很精神……\x01",
            "但这么久见不到他，还是有点担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EBC")

    label("loc_4764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4842")

    #C0272
    ChrTalk(
        0xFE,
        (
            "据说那群在通商会议时\x01",
            "发动袭击的共和国恐怖分子残党\x01",
            "已经在昨天被抓捕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "他们好像是在乘坐列车返回\x01",
            "共和国的时候被人发现了，\x01",
            "当时还引起了一场骚动……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "搭乘那趟列车的乘客们\x01",
            "真是倒霉啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4894")

    label("loc_4842")


    #C0275
    ChrTalk(
        0xFE,
        (
            "听说在列车里发现了\x01",
            "恐怖分子的残党……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "搭乘那趟列车的乘客们\x01",
            "真是倒霉啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4894")

    Jump("loc_4EBC")

    label("loc_4899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_49D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4979")

    #C0277
    ChrTalk(
        0xFE,
        (
            "距离帝国和共和国的恐怖分子\x01",
            "在通商会议上发动袭击的事件\x01",
            "已经有一个月了。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "听说有几个漏网之鱼\x01",
            "至今还逍遥法外……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "不过，他们想回国也不是那么简单的。\x01",
            "说不定仍然潜伏在\x01",
            "自治州的某个地方呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_49CF")

    label("loc_4979")


    #C0280
    ChrTalk(
        0xFE,
        (
            "听说有几个漏网之鱼\x01",
            "至今还逍遥法外……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "说不定仍然潜伏在\x01",
            "自治州的某个地方呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49CF")

    Jump("loc_4EBC")

    label("loc_49D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A39")

    #C0282
    ChrTalk(
        0xFE,
        (
            "竟然有盗贼闯入ＩＢＣ……\x01",
            "他到底是如何闯过这么森严的\x01",
            "安全系统的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B6B")

    label("loc_4A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF0")

    #C0283
    ChrTalk(
        0xFE,
        (
            "非常感谢你们帮忙解决了\x01",
            "失窃事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "虽说对方是怪盗Ｂ，\x01",
            "但没能抓到犯人\x01",
            "还是有点遗憾啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "不过，从结果上来看，\x01",
            "我们并没有遭受任何损失，\x01",
            "总算可以安心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4B6B")

    label("loc_4AF0")


    #C0286
    ChrTalk(
        0xFE,
        (
            "话说回来，这起事件的犯人\x01",
            "完全是为了兴趣而犯罪的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "虽说能找回失窃品，\x01",
            "已经很难得了……\x01",
            "但总觉得谜团越来越多了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B6B")

    Jump("loc_4EBC")

    label("loc_4B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B7E")
    Jump("loc_4EBC")

    label("loc_4B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C26")

    #C0288
    ChrTalk(
        0xFE,
        (
            "共和国的总统预定于\x01",
            "明天下午\x01",
            "来ＩＢＣ大楼视察。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "为了做好警备工作，我们保安\x01",
            "部门的成员几乎都要参与任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "……现在就开始紧张了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4C8F")

    label("loc_4C26")


    #C0291
    ChrTalk(
        0xFE,
        (
            "共和国的总统预定于\x01",
            "明天下午\x01",
            "来ＩＢＣ大楼视察。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "一想到那时候的警备工作……\x01",
            "就忍不住开始紧张了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C8F")

    Jump("loc_4EBC")

    label("loc_4C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4DC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D55")

    #C0293
    ChrTalk(
        0xFE,
        (
            "迪塔市长和玛丽亚贝尔小姐\x01",
            "最近比以前还要忙得多，\x01",
            "简直忙得团团转呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "但即使如此，他们\x01",
            "依然不忘关心身边的人，\x01",
            "脸上也总是挂着微笑。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        "我觉得这真是非常难得。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4DBC")

    label("loc_4D55")


    #C0296
    ChrTalk(
        0xFE,
        (
            "我一忙起来，\x01",
            "就完全无法分心\x01",
            "去顾及周围的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "光凭这一点，\x01",
            "就能看出他们二人有多了不起了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DBC")

    Jump("loc_4EBC")

    label("loc_4DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4EBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E59")

    #C0298
    ChrTalk(
        0xFE,
        (
            "欢迎。\x01",
            "欢迎来到克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "我是这里的警备人员，\x01",
            "可以为大家做个简单介绍。\x01",
            "请问您今天来此，有什么事要办呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4EBC")

    label("loc_4E59")


    #C0300
    ChrTalk(
        0xFE,
        (
            "欢迎。\x01",
            "欢迎来到克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "如果想办理各类银行\x01",
            "手续，请前往正面\x01",
            "或右边的服务台。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EBC")

    TalkEnd(0xFE)
    Return()

    # Function_15_45F3 end

    def Function_16_4EC0(): pass

    label("Function_16_4EC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-640, 1800, 4860, 0)
    MoveCamera(57, 26, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15390, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    SetChrPos(0x101, -610, 300, 2900, 0)
    SetChrPos(0x102, 760, 300, 2650, 0)
    SetChrPos(0x109, -610, 300, 2900, 0)
    SetChrPos(0x105, 760, 300, 2650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    LoadChrToIndex("chr/ch05500.itc", 0x1F)
    LoadChrToIndex("apl/ch51116.itc", 0x20)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x10, -610, 300, 24300, 180)
    SetChrPos(0x11, 760, 300, 24800, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    OP_68(-900, 1800, 5640, 3000)

    def lambda_503E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_503E)

    def lambda_504F():
        OP_98(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_504F)
    Sleep(50)

    def lambda_506C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_506C)

    def lambda_507D():
        OP_98(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_507D)
    Sleep(700)

    def lambda_509A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_509A)

    def lambda_50AB():
        OP_98(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_50AB)
    Sleep(50)

    def lambda_50C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_50C8)

    def lambda_50D9():
        OP_98(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_50D9)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    #C0302
    ChrTalk(
        0x101,
        (
            "#6P#00000F对了，罗伯兹主任\x01",
            "给我们发来了一个委托吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#11P#00100F是啊，快去请服务台的\x01",
            "兰菲小姐帮忙联系他吧。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)

    #N0304
    NpcTalk(
        0x10,
        "男性的声音",
        "哎呀，你们是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_68(-1430, 1800, 8130, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(15440, 3000)

    def lambda_521E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_521E)
    Sleep(50)

    def lambda_523B():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_523B)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)

    #C0305
    ChrTalk(
        0x109,
        "#12P#10105F迪塔市长！\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        "#12P#00000F玛丽亚贝尔小姐也在一起。\x02",
    )

    CloseMessageWindow()
    OP_68(-330, 1700, 14870, 5000)
    MoveCamera(43, 22, 0, 5000)
    OP_6E(590, 5000)
    SetCameraDistance(13820, 5000)

    def lambda_52CD():
        OP_98(0x101, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52CD)
    Sleep(50)

    def lambda_52EA():
        OP_98(0x102, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_52EA)
    Sleep(50)

    def lambda_5307():
        OP_98(0x109, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5307)
    Sleep(50)

    def lambda_5324():
        OP_98(0x105, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5324)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0307
    ChrTalk(
        0x109,
        (
            "#12P#10100F你们今天来\x01",
            "ＩＢＣ了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x10,
        (
            "#02800F嗯，因为银行这边\x01",
            "积攒了好多工作没有处理。\x02\x03",

            "#02804F多亏有贝尔帮我，\x01",
            "刚刚已经把那些工作\x01",
            "处理完毕了。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0309
    AnonymousTalk(
        0x11,
        (
            "呵呵呵，各位……\x01",
            "我们好像已经很久没\x01",
            "见面了呢。\x02\x03",

            "艾莉，最近还好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0310
    ChrTalk(
        0x102,
        (
            "#12P#00109F呵呵，托你的福，\x01",
            "支援科前几天重新恢复运作了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x11,
        "#5P#02905F嗯，让我看看……\x02",
    )

    CloseMessageWindow()
    OP_68(-330, 1500, 14870, 2000)
    MoveCamera(44, 26, 0, 2000)
    OP_6E(590, 2000)
    SetCameraDistance(14510, 2000)

    def lambda_5525():

        label("loc_5525")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_5525")

    QueueWorkItem2(0x101, 1, lambda_5525)
    Sleep(50)

    def lambda_553A():

        label("loc_553A")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_553A")

    QueueWorkItem2(0x109, 1, lambda_553A)
    Sleep(50)

    def lambda_554F():

        label("loc_554F")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_554F")

    QueueWorkItem2(0x105, 1, lambda_554F)
    OP_99(0x11, 0x102, 0x1F4, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    Fade(500)
    Sound(898, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x11, 0x3)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x11, 0x2)
    SetChrPos(0x102, 760, 300, 14650, 180)
    SetChrPos(0x11, 760, 300, 15150, 180)

    #C0312
    ChrTalk(
        0x109,
        "#12P#10111F哇啊……\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x105,
        "#12P#10309F哟¤\x02",
    )

    CloseMessageWindow()

    def lambda_55F0():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_55F0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0314
    ChrTalk(
        0x102,
        "#12P#00112F等、等一下啊，贝尔……\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x11,
        (
            "#5P#02902F嗯嗯，看来你的\x01",
            "健康状况的确不错呢。\x02\x03",

            "#02904F这份柔软而温暖的触感，\x01",
            "还有透过衣服也可以感受到的\x01",
            "柔韧肌肉……\x02\x03",

            "#02909F啊啊～真让人爱不释手⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x102,
        (
            "#12P#00113F讨、讨厌……！\x01",
            "你别用这么奇怪的词语\x01",
            "来形容啦！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x11, 0x2)
    Sleep(500)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    TurnDirection(0x102, 0x11, 0)

    def lambda_574C():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_574C)
    Sleep(50)

    def lambda_5764():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5764)
    Sleep(1000)
    TurnDirection(0x11, 0x101, 500)
    Sleep(300)

    #C0317
    ChrTalk(
        0x11,
        (
            "#11P#02904F对了，罗伊德警官……\x02\x03",

            "#02901F你该不会没经过我的许可，\x01",
            "就擅自对艾莉\x01",
            "出手了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0318
    ChrTalk(
        0x101,
        "#6P#00012F刚、刚一见面就问这个吗？\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "#11P#02903F因为罗伊德警官是危险人物啊，\x01",
            "定期检查是必不可少的。\x02\x03",

            "#02901F如果让我发现你有什么\x01",
            "不轨之举……后果你应该明白吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#6P#00011F唔……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x105,
        "#12P#10309F哈哈哈，彻底被戒备了呢。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x102,
        "#11P#00106F贝尔你真是的……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x10,
        (
            "#5P#02806F哎呀呀，贝尔，\x01",
            "难得和大家见一次面，\x01",
            "你就自重一点吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5943():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5943)
    Sleep(50)

    def lambda_5953():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5953)
    Sleep(50)

    def lambda_5963():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5963)
    Sleep(50)

    def lambda_5973():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5973)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0324
    AnonymousTalk(
        0x10,
        (
            "再次向各位说一声好久不见。\x02\x03",

            "新加入的诺艾尔和瓦吉好像也\x01",
            "都已经习惯这个部门了，真是太好了。\x02\x03",

            "让我借此机会对特别任务支援科\x01",
            "重新恢复运作致以祝贺吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0325
    ChrTalk(
        0x105,
        (
            "#12P#10300F呵呵，感谢您把我推荐到支援科。\x02\x03",

            "#10309F我也借此机会\x01",
            "再次道个谢吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x109,
        (
            "#12P#10109F您还给我们配发了导力车，\x01",
            "真是太感谢了！\x02\x03",

            "#10104F没想到竟能驾驶那么\x01",
            "帅气的导力车，\x01",
            "简直就像在做梦一样！\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x10,
        (
            "#5P#02809F哈哈，能帮上你们的忙，\x01",
            "我也很高兴。\x02\x03",

            "#02800F这样一来，我这新市长也就\x01",
            "当得有意义了。\x02\x03",

            "#02806F不过……\x01",
            "同时兼任市长和ＩＢＣ总裁\x01",
            "还真是相当困难啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x11,
        (
            "#11P#02906F您会如此繁忙，\x01",
            "基本上属于\x01",
            "咎由自取吧。\x02\x03",

            "#02900F总是把所有事情都揽到自己身上，\x01",
            "偶尔也该考虑一下\x01",
            "帮您做事的我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x10,
        (
            "#5P#02804F哈哈，抱歉了，贝尔。\x01",
            "一想到每件事都是为了克洛斯贝尔，\x01",
            "便无法置之不理。\x02\x03",

            "#02800F在不知不觉中\x01",
            "就接下了过多的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#12P#00100F呵呵，外公也十分佩服\x01",
            "迪塔叔叔您的这种\x01",
            "活力呢。\x02\x03",

            "#00104F还很高兴地对我说\x01",
            "『现在的克洛斯贝尔就是需要\x01",
            "  像他那样的年轻政治家啊』。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x10,
        (
            "#5P#02809F哈哈，被老前辈麦克道尔议长\x01",
            "如此赞扬，真有些不好意思啊。\x02\x03",

            "#02803F话说回来，在政治领域中，\x01",
            "我只是个刚入门的新人而已。\x02\x03",

            "#02800F还有许许多多的\x01",
            "事情需要学习。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0332
    ChrTalk(
        0x11,
        (
            "#11P#02905F啊，父亲，\x01",
            "约定在新市政厅大楼\x01",
            "见面的时间就快到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x10,
        (
            "#5P#02805F啊，是吗？\x02\x03",

            "#02800F那么各位，\x01",
            "我这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#12P#00000F抱歉，我们好像\x01",
            "占用了您不少时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x10,
        (
            "#5P#02809F哪里哪里，没有的事。\x01",
            "多亏你们，我放松了不少呢。\x02\x03",

            "#02804F以后要是遇到了什么困难，\x01",
            "随时都可以来找我。\x02\x03",

            "#02800F我一定会不惜余力地\x01",
            "为各位提供协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#12P#00100F呵呵，非常感谢您。\x02\x03",

            "#00104F迪塔叔叔、贝尔，\x01",
            "你们都要注意身体哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    #C0337
    ChrTalk(
        0x11,
        (
            "#5P#02909F呵呵呵，谢谢了，艾莉。\x02\x03",

            "#02900F那么，\x01",
            "我们这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x109,
        "#12P#10109F两位辛苦了！\x02",
    )

    CloseMessageWindow()
    OP_68(-310, 1500, 13600, 3000)
    MoveCamera(44, 24, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(15430, 3000)
    BeginChrThread(0x101, 3, 0, 18)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 19)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 18)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 19)
    Sleep(500)
    BeginChrThread(0x10, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 17)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 20)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 20)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 21)
    WaitChrThread(0x11, 3)
    Sound(107, 0, 100, 0)
    Sleep(700)
    Sound(107, 0, 100, 0)
    Sleep(500)

    #C0339
    ChrTalk(
        0x101,
        "#00000F他们果然非常忙碌啊。\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        (
            "#11P#00103F毕竟已经临近月底的『通商会议』了……\x02\x03",

            "#00100F迪塔叔叔和贝尔的日程安排\x01",
            "肯定都十分紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，包括昨天导力车的事在内，\x01",
            "他们真的为我们\x01",
            "做了不少事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#00003F是啊，真希望他们不要因为\x01",
            "疲劳过度而累坏自己的身体……\x02\x03",

            "#00000F……总之，现在先去接受\x01",
            "罗伯兹主任委托的任务吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x109,
        (
            "#12P#10100F好的，去服务台\x01",
            "请工作人员联系他吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearMapFlags(0x10000000)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x132, 5)
    SetChrPos(0x0, -60, 300, 15630, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_16_4EC0 end

    def Function_17_62B2(): pass

    label("Function_17_62B2")

    OP_95(0xFE, -330, 300, 15470, 2000, 0x0)
    OP_95(0xFE, -40, 300, 6500, 2000, 0x0)
    Return()

    # Function_17_62B2 end

    def Function_18_62DB(): pass

    label("Function_18_62DB")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_18_62DB end

    def Function_19_62F2(): pass

    label("Function_19_62F2")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x190, 0x7D0, 0x0)
    Return()

    # Function_19_62F2 end

    def Function_20_6309(): pass

    label("Function_20_6309")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_6309 end

    def Function_21_6320(): pass

    label("Function_21_6320")

    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_6320 end

    def Function_22_6337(): pass

    label("Function_22_6337")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(500)
    OP_68(-20, 1300, 29740, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20420, 0)
    SetChrPos(0x101, -470, 300, 28930, 0)
    SetChrPos(0x102, 540, 300, 28690, 0)
    SetChrPos(0x109, -810, 300, 27570, 0)
    SetChrPos(0x105, 890, 300, 27520, 0)
    OP_0D()

    #C0344
    ChrTalk(
        0x102,
        "#12P#00100F早上好，兰菲小姐。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64DB")

    #C0345
    ChrTalk(
        0xA,
        (
            "#5P哎呀，原来是罗伊德警官和艾莉小姐。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xA,
        (
            "#5P看来特别任务支援科\x01",
            "已经重新恢复运作了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        "#12P#00000F是啊，托您的福。\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x102,
        (
            "#12P#00100F今后也要请您\x01",
            "多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xA,
        "#5P嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xA,
        (
            "#5P请问，各位今天\x01",
            "来这里有何贵干？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_651D")

    label("loc_64DB")


    #C0351
    ChrTalk(
        0xA,
        (
            "#5P哎呀，是艾莉小姐和支援科的各位。\x01",
            "各位今天来这里有何贵干？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_651D")


    #C0352
    ChrTalk(
        0x101,
        (
            "#12P#00000F爱普斯泰恩财团的罗伯兹主任\x01",
            "发给我们一件委托……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xA,
        (
            "#5P哦，我知道\x01",
            "这件事情。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5B")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_66F0")

    #C0354
    ChrTalk(
        0xA,
        "#5P对了，有件事情正好先和大家说一下……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xA,
        (
            "#5P以前交给各位的那张\x01",
            "换钱服务用卡片\x01",
            "已经过了有效期。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xA,
        (
            "#5P我们已经为大家准备了新的卡片，\x01",
            "请收下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0357
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ贵宾卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ贵宾卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0358
    ChrTalk(
        0xA,
        (
            "#5P请像以前一样，在服务台\x01",
            "出示这张卡片。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xA,
        (
            "#5P这样就能以高于市场的汇率\x01",
            "将耀晶片换成米拉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_681F")

    label("loc_66F0")


    #C0360
    ChrTalk(
        0xA,
        (
            "#5P对了，在此之前……\x01",
            "我有件东西要交给大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xA,
        "#5P请收下这个吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0362
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ贵宾卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ贵宾卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0363
    ChrTalk(
        0x101,
        "#12P#00005F这张卡片是……？\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xA,
        (
            "#5P这是可以证明\x01",
            "本行特别会员\x01",
            "身份的贵宾卡。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xA,
        (
            "#5P只要向服务台出示这张卡片，\x01",
            "就能以高于市场的汇率\x01",
            "将耀晶片换成米拉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_681F")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ＩＢＣ的兑换服务已经可以使用了。\x01",
            "　可以将耀晶片以高于通常市值的\x01",
            "　汇率兑换成米拉。\x02\x03",

            "※和兰菲对话，\x01",
            "　选择『换钱』之后再选择『EXCHANGE』，\x01",
            "  即可进行兑换。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x134, 4)

    #C0367
    ChrTalk(
        0x109,
        (
            "#12P#10105F我、我们可以接受\x01",
            "这样的服务吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xA,
        (
            "#5P当然，各位可是库罗伊斯市长，\x01",
            "还有玛丽亚贝尔大小姐的\x01",
            "重要友人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xA,
        "#5P为你们提供点方便是理所当然的。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，那我们就\x01",
            "不客气地收下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        "#12P#00000F下次过来时，一定会使用这张卡的。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xA,
        "#5P呵呵，期待各位下次光临。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xA,
        (
            "#5P那么，我马上就帮各位\x01",
            "联系罗伯兹主任。\x01",
            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A8F")

    label("loc_6A5B")


    #C0374
    ChrTalk(
        0xA,
        (
            "#5P我马上就帮各位联系罗伯兹主任，\x01",
            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A8F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    Sleep(1000)
    OP_68(6520, 1500, 14990, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(13860, 0)
    SetChrPos(0x101, 4820, 0, 16800, 90)
    SetChrPos(0x102, 4820, 0, 15390, 90)
    SetChrPos(0x109, 3530, 0, 16850, 90)
    SetChrPos(0x105, 3470, 0, 15130, 90)
    SetChrPos(0xE, 10590, 0, 16190, 270)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(700)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)
    OP_68(4600, 1500, 15420, 2000)

    def lambda_6B88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_6B88)

    def lambda_6B99():
        OP_95(0xFE, 6410, 0, 16170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6B99)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0xE, 1)
    OP_6F(0x1)

    #C0375
    ChrTalk(
        0xE,
        "哟，你们好！\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        "#6P#00000F您工作辛苦了，罗伯兹主任。\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xE,
        "你们是为了我的委托而来的吧？\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        (
            "哎呀～真是太好了。\x01",
            "我有项工作，\x01",
            "一定要请你们帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，任务内容\x01",
            "似乎很有趣的样子。\x02\x03",

            "#10304F好像是什么服务的\x01",
            "最终测试吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x109,
        (
            "#6P#10100F我记得……\x01",
            "是叫『波波碰！』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x102,
        (
            "#6P#00105F总觉得好像在哪里\x01",
            "听过这个名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#6P#00005F被你这么一提，的确有点印象呢……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xE,
        "呵呵，保证是个很愉快的任务～\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xE,
        (
            "那么，你们能立刻\x01",
            "接受这项工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        "#6P#00000F当然没问题。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x102,
        (
            "#6P#00100F可以为我们\x01",
            "说明一下工作内容吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xE,
        "呵呵，好的。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xE,
        (
            "其实我们准备在近期\x01",
            "公布一款名叫\x01",
            "『波波碰！』的导力游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xE,
        (
            "现在正以市内的导力网络\x01",
            "终端拥有者为受众\x01",
            "进行游戏研发。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x109,
        "#6P#10105F导力游戏……？\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x105,
        (
            "#6P#10305F与台球、扑克\x01",
            "之类的游戏\x01",
            "有什么不同吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xE,
        (
            "嗯，这个游戏同样以\x01",
            "固定的规则为基准，\x01",
            "以竞争得分、分出胜负为目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xE,
        (
            "但最大的不同点就是，\x01",
            "这个游戏需要移动\x01",
            "终端画面上的元素来玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#6P#00003F听、听起来\x01",
            "好像很高端啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x102,
        (
            "#6P#00105F也就是说，此次委托中的\x01",
            "『测试』就是指……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xE,
        (
            "嗯，自然是希望\x01",
            "你们帮忙测试\x01",
            "『波波碰！』这个游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xE,
        (
            "构架程序时会不可避免地\x01",
            "产生各种错误，\x01",
            "因此必须反复测试。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x105,
        (
            "#6P#10302F不过……\x01",
            "像这种简单的测试，\x01",
            "在财团内部就能完成了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xE,
        (
            "唔～其实从前一段时间开始，\x01",
            "我就一直在拜托缇欧帮忙\x01",
            "测试……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xE,
        (
            "但是遇到了两个问题，\x01",
            "所以必须要请财团外部的人员\x01",
            "来帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#6P#00005F有两个……问题吗？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xE,
        "嗯，第一个问题是……\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xE,
        (
            "缇欧在测试游戏时，\x01",
            "时常会使用\x01",
            "『永世系统』。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xE,
        (
            "因此我们实在没法从她那里\x01",
            "得到什么有用的资料……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x109,
        "#6P#10105F永世系统是……\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x102,
        (
            "#6P#00100F就是缇欧数次使用过的\x01",
            "那个系统吧？\x02\x03",

            "#00104F她之前还教过我\x01",
            "一些呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，好像就是她操纵\x01",
            "导力终端和魔导杖时\x01",
            "用的那个系统……\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xE,
        (
            "唔，趁着这个机会，\x01",
            "我来为各位说明一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xE,
        (
            "『永世系统』是\x01",
            "缇欧装备的护胸中\x01",
            "自带系统的名称。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xE,
        (
            "它的主要功能是\x01",
            "辅助缇欧的\x01",
            "高速处理能力……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xE,
        (
            "以及辅助魔导杖来发动\x01",
            "无需驱动时间的导力魔法。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xE,
        (
            "想要自如运用这个系统，\x01",
            "自身必须拥有一定的相性才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        (
            "#6P#00006F唔……\x01",
            "听起来真是好复杂……\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        (
            "#6P#00106F缇欧不在的时候，\x01",
            "这方面的话题果然很让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x105,
        (
            "#6P#10300F也就是说，那个系统\x01",
            "并不适合这个测试吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xE,
        "算、算是吧。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xE,
        (
            "听说她用永世系统连出了\x01",
            "常人根本办不到的超级连击，\x01",
            "因此一直在游戏中获得压倒性的胜利。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xE,
        (
            "约纳也曾和她\x01",
            "一起测试，\x01",
            "可是连一次都没有赢过。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xE,
        (
            "……啊，我的意思并不是缇欧\x01",
            "在作弊哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xE,
        (
            "你们可千万别对\x01",
            "缇欧说什么奇怪的话啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        "#6P#00006F好、好的……\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x109,
        (
            "#6P#10105F请问……\x01",
            "另一个问题\x01",
            "又是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xE,
        (
            "嗯，另一个问题……\x01",
            "就在于这个游戏是一款\x01",
            "『对战游戏』。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xE,
        (
            "刚才我也提及过这方面，\x01",
            "这个游戏能让两个相隔很远的\x01",
            "终端连接在一起游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xE,
        (
            "因此我想在市内\x01",
            "实地测试一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x102,
        (
            "#6P#00105F原来如此……\x01",
            "是这么一回事啊。\x02\x03",

            "#00100F不过，\x01",
            "竟然能让相隔很远的人\x01",
            "一起玩游戏，真厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xE,
        "呵呵，对吧？\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xE,
        (
            "这个设想在构想导力网络的\x01",
            "初期阶段就已经提出了。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xE,
        (
            "只要导力网络不断普及，\x01",
            "一定会有许多人能\x01",
            "一起开心地玩游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xE,
        (
            "就算遇到今天这样的\x01",
            "下雨天，也能在家里\x01",
            "和朋友一起享受游戏的快乐。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#6P#00000F嘿……\x01",
            "时代的发展真惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xE,
        (
            "似乎有点跑题了……\x01",
            "总之，就是这么一回事。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xE,
        (
            "……我先把这个\x01",
            "送给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0434
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '波波碰！β版'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('波波碰！β版', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0435
    ChrTalk(
        0x101,
        "#6P#00005F这是……记录结晶吗？\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xE,
        (
            "这个记录结晶里面存有\x01",
            "『波波碰！』程序的最终测试版。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xE,
        (
            "只要把这个安装到\x01",
            "支援科的终端上，\x01",
            "立刻就能开始游戏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x102,
        (
            "#6P#00100F安装……\x01",
            "就是指把程序复制到\x01",
            "终端里面吧？\x02\x03",

            "#00104F我以前看过\x01",
            "缇欧的操作，\x01",
            "我想我应该能完成。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0439
    ChrTalk(
        0x101,
        (
            "#6P#00000F这样啊，\x01",
            "那就拜托你了，艾莉。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xE,
        "嗯嗯，真是可靠啊。\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xE,
        (
            "还有这个，也一起交给你们吧。\x01",
            "这是我的艾尼格玛号码，\x01",
            "还有『波波碰！』的账号。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0442
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『罗伯兹主任的账号』\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 3)
    OP_E4(0x3)

    #C0443
    ChrTalk(
        0x101,
        "#6P#00005F账、账号……？\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x109,
        (
            "#6P#10106F请、请您等一下，\x01",
            "我们不懂这些专有名词的意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xE,
        (
            "嗯，简单来说，\x01",
            "账号就是指在网络上\x01",
            "使用的名字……\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xE,
        (
            "你们只需要明白，\x01",
            "这是游戏对战时需要的\x01",
            "东西就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xE,
        (
            "其它搞不懂的事情就先不用管了。\x01",
            "总之，你们安装β版的时候，\x01",
            "把账号也输入进去就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xE,
        (
            "之后就用艾尼格玛联系我，\x01",
            "我会告诉你们接下来该怎么做。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xE,
        (
            "……嗯，大致内容就是这样。\x01",
            "你们可以立刻开始测试吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        (
            "#6P#00000F好、好的，\x01",
            "没问题。\x02\x03",

            "#00004F那我们就先\x01",
            "回支援科吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x102,
        "#6P#00102F好，一起回去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0452
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【参加β测试】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    SetScenarioFlags(0x131, 3)
    OP_29(0x6C, 0x1, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xE, 0xFF)
    SetChrPos(0xE, 6500, 0, 17850, 270)
    SetChrPos(0x0, 4010, 0, 16140, 90)
    EventEnd(0x5)
    Return()

    # Function_22_6337 end

    def Function_23_7C50(): pass

    label("Function_23_7C50")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch29300.itc", 0x1E)
    LoadChrToIndex("chr/ch06100.itc", 0x1F)
    LoadChrToIndex("apl/ch51255.itc", 0x20)
    OP_68(0, 1400, 4600, 0)
    MoveCamera(54, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(16149, 0)
    SetChrPos(0x101, 500, 300, 2000, 0)
    SetChrPos(0x102, -1000, 300, 800, 0)
    SetChrPos(0x103, -500, 300, 2000, 0)
    SetChrPos(0x104, 1000, 300, 1200, 0)
    SetChrPos(0x109, 500, 300, 0, 0)
    SetChrPos(0x105, -500, 300, 0, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7D5D():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7D5D)
    Sleep(100)

    def lambda_7D7A():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7D7A)
    Sleep(100)

    def lambda_7D97():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7D97)
    Sleep(100)

    def lambda_7DB4():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7DB4)
    Sleep(100)

    def lambda_7DD1():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7DD1)
    Sleep(100)

    def lambda_7DEE():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7DEE)
    OP_68(-70, 1400, 7250, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)

    def lambda_7E28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E28)
    Sleep(100)

    def lambda_7E3C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7E3C)
    Sleep(500)

    def lambda_7E50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7E50)
    Sleep(100)

    def lambda_7E64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7E64)
    Sleep(500)

    def lambda_7E78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7E78)
    Sleep(100)

    def lambda_7E8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7E8C)
    WaitChrThread(0x105, 0)
    Sound(107, 0, 100, 0)
    OP_6F(0x79)

    #C0453
    ChrTalk(
        0x101,
        (
            "#11P#00000F嗯……\x01",
            "不知道罗伯兹主任在不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x103,
        (
            "#00203F#6P应该就在财团的\x01",
            "楼层闲晃呢。\x02\x03",

            "#00200F用艾尼格玛联系一下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7F23():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7F23)

    def lambda_7F30():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7F30)
    Sleep(50)

    def lambda_7F40():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7F40)
    Sleep(50)

    def lambda_7F50():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7F50)
    Sleep(50)

    def lambda_7F60():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7F60)
    Sleep(50)

    def lambda_7F70():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7F70)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    SetCameraDistance(15650, 2000)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x2)
    Sleep(500)
    Sound(804, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0x103, 0x1)
    Sound(823, 0, 100, 0)
    Sleep(2700)

    #C0455
    ChrTalk(
        0x103,
        (
            "#00200F#5P……你好，我是缇欧。\x02\x03",

            "#00205F不……\x01",
            "我不是那个意思。\x02\x03",

            "#00203F………………………………\x02\x03",

            "#00211F你好烦人，主任。\x01",
            "请适可而止。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0456
    ChrTalk(
        0x101,
        "#11P#00012F（还、还是老样子呢……）\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        (
            "#12P#00106F（缇欧也真是的，\x01",
            "  其实可以对他稍微温柔一点啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        (
            "#00302F#11P（不过，也许这种冷淡的态度\x01",
            "  反而能让那个大叔更加高兴。）\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x103,
        (
            "#00203F#5P……嗯，是关于艾尼格玛Ⅱ的\x01",
            "紧急警报功能……\x02\x03",

            "#00200F………嗯……没错………\x02\x03",

            "#00203F是的，我们已经在楼下了，\x01",
            "那就拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sleep(400)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x2)
    OP_0D()

    #C0460
    ChrTalk(
        0x101,
        "#11P#00000F他愿意帮我们吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0461
    ChrTalk(
        0x103,
        (
            "#00204F#6P嗯，他马上\x01",
            "就会下来。\x02\x03",

            "#00202F约纳好像也在一起呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x102,
        "#12P#00102F啊……\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x109,
        (
            "#10100F#11P就是以前住在已被炸毁的\x01",
            "地下空间房间里的那个小孩吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x105,
        (
            "#12P#10300F记得是爱普斯泰恩财团出身的\x01",
            "天才黑客少年？\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        (
            "#00304F#11P嗯，是个态度傲慢，\x01",
            "但同时也有胆小一面的小鬼头。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        (
            "#11P#00000F他现在应该已经回到\x01",
            "财团的事务所了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        (
            "#00206F#6P嗯……\x01",
            "虽然他好像很不情愿。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15150, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrPos(0x101, 4900, 0, 21000, 90)
    SetChrPos(0x102, 4700, 0, 22200, 135)
    SetChrPos(0x103, 4900, 0, 19900, 90)
    SetChrPos(0x104, 6900, 0, 23000, 180)
    SetChrPos(0x109, 5800, 0, 23000, 135)
    SetChrPos(0x105, 4400, 0, 18500, 45)
    OP_4B(0xE, 0xFF)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 7300, 0, 21000, 270)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 7300, 0, 19900, 270)
    OP_68(6100, 1100, 20450, 0)
    MoveCamera(43, 17, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15000, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0468
    AnonymousTalk(
        0xE,
        (
            "原来如此，\x01",
            "发生了这种事啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(16000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(128, 2, 50, 0)
    OP_6F(0x79)

    #C0469
    ChrTalk(
        0xF,
        (
            "#02306F#11P哼，反正就是导力耗尽了，\x01",
            "所以联系不上了吧？\x02\x03",

            "#02301F游击士都是些装好人的家伙，\x01",
            "就别管她们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#6P#00006F约纳，我说你啊……\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x102,
        (
            "#6P#00108F真是的……\x01",
            "怎么能这么说话呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xE,
        (
            "#11P唉，约纳最近\x01",
            "一直是这个样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xE,
        (
            "#11P亏我还特意在事务所里\x01",
            "准备了一间配有最新型\x01",
            "专用终端的房间给他呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(200)

    #C0474
    ChrTalk(
        0xF,
        (
            "#02310F#12P虽说那个终端的处理能力很强，\x01",
            "但鬼才会满足于那种\x01",
            "处处设限的系统！\x02\x03",

            "#02307F赶快把安全限制\x01",
            "给我解除掉！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)

    #C0475
    ChrTalk(
        0xE,
        "#5P啊，那可不行哦，约纳。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xE,
        (
            "#5P如果解除了限制，\x01",
            "你肯定又要为所欲为了。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xE,
        (
            "#5P但作为补偿，我已经给你做了一个\x01",
            "特训用的程序，或许能让你在『波波碰！』\x01",
            "游戏中胜过缇欧哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xF,
        "#02311F#12P多、多事！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0479
    ChrTalk(
        0x101,
        (
            "#6P#00012F（不管怎么说，\x01",
            "  看来他一直都在认真地监督约纳呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x103,
        (
            "#6P#00203F（虽说他有些方面很让人火大，\x01",
            "  但毕竟还是个很有才干的人。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)
    Sleep(150)

    #C0481
    ChrTalk(
        0xE,
        "#11P嗯，先不提这个了。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xE,
        (
            "#11P我想艾尼格玛Ⅱ的警报功能\x01",
            "恐怕派不上用场。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8928():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_8928)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0483
    ChrTalk(
        0x101,
        "#6P#00011F这、这样吗？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        (
            "#6P#00105F这个功能应该还是\x01",
            "存在的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xE,
        (
            "#11P嗯，但它发出的导力波太弱了，\x01",
            "几乎无法感知。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xE,
        (
            "#11P如果不在１０赛尔矩的范围内，\x01",
            "测定器就感知不到。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x109,
        "#10101F#5P１０赛尔矩……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x104,
        "#00306F#5P这个距离真是不远不近啊……\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x105,
        (
            "#6P#10301F如果在克洛斯贝尔市内，\x01",
            "应该就能感知到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x103,
        (
            "#6P#00203F……和我的传感器\x01",
            "组合使用如何？\x02\x03",

            "#00201F如果测定器的系统已经母盘化，\x01",
            "应该可以和永世结合在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xE,
        "#11P哦，也许行得通呢！\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xE,
        (
            "#11P……不，还是不行。\x01",
            "测定器的精确度太不稳定了，\x01",
            "无法和永世系统结合。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xE,
        (
            "#11P而且导力压也是一大问题，\x01",
            "再考虑到周围地形的反射，\x01",
            "实在是太勉强了。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x103,
        "#6P#00206F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x101,
        (
            "#6P#00006F我、我完全没听懂\x01",
            "到底为什么不行……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#6P#00108F看来是技术上\x01",
            "出了一些问题呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xF)

    #C0497
    ChrTalk(
        0xF,
        (
            "#02305F#11P既然如此……\x02\x03",

            "#02300F到兰花塔的塔顶上\x01",
            "测定不就行了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8D95():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8D95)

    #C0498
    ChrTalk(
        0x103,
        "#6P#00205F哎……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xE,
        "#5P……约纳？\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#6P#00001F那个……这是什么意思？\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xF,
        (
            "#02301F#11P警报用的导力波非常微弱，\x01",
            "只有在距离测定器较近时\x01",
            "才能感知得到。\x02\x03",

            "#02303F你们想把测定器和\x01",
            "缇欧的传感器结合起来，\x01",
            "但是功率不足，精确度也不够。\x02\x03",

            "#02302F不过，兰花塔的塔顶上没有障碍物，\x01",
            "如果去那里测定，感知的精确度就会上升，\x01",
            "而且也能保证高功率的导力输出了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x104,
        "#00305F#5P我、我还是听不懂在说什么……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x103, 500)

    #C0503
    ChrTalk(
        0x109,
        "#10100F#5P这办法怎么样？缇欧。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x103,
        "#6P#00204F……真让我吃惊。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xE,
        "#5P哎呀呀，真不愧是约纳！\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xE,
        (
            "#5P你在系统程序工程方面的才华\x01",
            "真是让人赞叹啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(100)

    #C0507
    ChrTalk(
        0xF,
        (
            "#02309F#12P哼、哼，\x01",
            "我本来就是天才嘛～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9002():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9002)

    #C0508
    ChrTalk(
        0x101,
        "#6P#00002F那么……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x105,
        "#6P#10302F现在已经有办法了吗？\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x103,
        "#6P#00202F嗯，也许行得通。\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    #C0511
    ChrTalk(
        0xE,
        (
            "#11P先去兰花塔的管理部门申请一下，\x01",
            "看看能不能得到\x01",
            "登上塔顶的权限吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)
    Sleep(150)

    #C0512
    ChrTalk(
        0xE,
        "#5P约纳呢，你也会来帮忙吧？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xF,
        (
            "#02302F#12P按理说，我没有这个义务……\x01",
            "但现在正好很闲，就帮帮忙好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)
    Sleep(100)

    #C0514
    ChrTalk(
        0xF,
        (
            "#02301F#11P不过，你们可要记住，\x01",
            "这次算是欠我一个人情哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x101,
        "#6P#00004F哈哈，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        (
            "#6P#00102F只要你别提太无理的要求，\x01",
            "我们一定会还上这份人情的。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0517
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，主任和约纳向兰花塔的管理部门\x01",
            "申请到了登上塔顶的许可，\x01",
            "于是带着器材，先行赶向兰花塔。\x02\x03",

            "他们似乎还需要一些准备时间，\x01",
            "因此罗伊德等人决定先处理其它事情，\x01",
            "稍后再前往兰花塔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrPos(0x0, 0, 300, 8000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 2)
    OP_29(0xA9, 0x1, 0x1)
    ClearMapFlags(0x10000000)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(128, 2, 50, 0)
    EventEnd(0x5)
    Return()

    # Function_23_7C50 end

    def Function_24_930E(): pass

    label("Function_24_930E")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-230, 1400, 29510, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15440, 0)
    SetChrPos(0x101, 0, 300, 28870, 0)
    SetChrPos(0x102, -1300, 300, 28870, 0)
    SetChrPos(0x104, 1300, 300, 28870, 0)
    SetChrPos(0x109, 0, 300, 27710, 0)
    SetChrPos(0x103, -1300, 300, 27710, 0)
    SetChrPos(0x105, 1300, 300, 27710, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0518
    ChrTalk(
        0xA,
        (
            "#5P各位……\x01",
            "欢迎你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xA,
        (
            "#5P你们是为了\x01",
            "玛丽亚贝尔大小姐的委托\x01",
            "而来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        "#00000F嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x102,
        (
            "#12P#00101F听说贝尔珍爱的\x01",
            "古董人偶被人\x01",
            "盗走了？\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x103,
        (
            "#12P#00205F莫非是那个\x01",
            "罗赞贝尔克工房制作的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xA,
        (
            "#5P嗯，正是。\x01",
            "玛丽亚贝尔大小姐\x01",
            "非常沮丧呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xA,
        (
            "#5P各位可以立刻接受大小姐的\x01",
            "这项委托吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_950B")
    Call(0, 27)

    label("loc_950B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9534")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_953E")

    label("loc_9534")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_953E")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_24_930E end

    def Function_25_955A(): pass

    label("Function_25_955A")

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
            "接受\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_95B4"),
        (1, "loc_95B9"),
        (SWITCH_DEFAULT, "loc_9641"),
    )


    label("loc_95B4")

    Jump("loc_9641")

    label("loc_95B9")


    #C0525
    ChrTalk(
        0x101,
        (
            "#00006F非常抱歉，\x01",
            "我们现在实在是腾不出时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xA,
        (
            "#5P这样啊……\x01",
            "那也没办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xA,
        (
            "#5P等你们有空之后，\x01",
            "再来通知我一声吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C6, 1)
    Jump("loc_9641")

    label("loc_9641")

    Return()

    # Function_25_955A end

    def Function_26_9642(): pass

    label("Function_26_9642")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-230, 1400, 29510, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15440, 0)
    SetChrPos(0x101, 0, 300, 28870, 0)
    SetChrPos(0x102, -1300, 300, 28870, 0)
    SetChrPos(0x104, 1300, 300, 28870, 0)
    SetChrPos(0x109, 0, 300, 27710, 0)
    SetChrPos(0x103, -1300, 300, 27710, 0)
    SetChrPos(0x105, 1300, 300, 27710, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0528
    ChrTalk(
        0xA,
        (
            "#5P由于古董人偶遭窃，\x01",
            "玛丽亚贝尔大小姐\x01",
            "现在十分沮丧……\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xA,
        (
            "#5P各位可以立刻接受大小姐的\x01",
            "这项任务吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9776")
    Call(0, 27)

    label("loc_9776")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_979F")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_97A9")

    label("loc_979F")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_97A9")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_26_9642 end

    def Function_27_97C5(): pass

    label("Function_27_97C5")


    #C0530
    ChrTalk(
        0x101,
        "#00000F嗯，我们接受。\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x103,
        (
            "#12P#00200F毕竟受到过\x01",
            "玛丽亚贝尔小姐的不少关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xA,
        "#5P呵呵，非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xA,
        (
            "#5P那么，就把卡片发给各位吧，\x01",
            "请收下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0534
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＩＢＣ认证卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＩＢＣ认证卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0535
    ChrTalk(
        0x105,
        "#12P#10305F唔，这是什么东西？\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x102,
        (
            "#6P#00100F这是我们以前也曾得到过的\x01",
            "ＩＢＣ认证卡。\x02\x03",

            "#00103F只要有这张卡，就能乘坐导力梯\x01",
            "前往特定的楼层。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x109,
        (
            "#12P#10105F原来如此，\x01",
            "是一种安全措施啊。\x01",
            "真不愧是天下闻名的ＩＢＣ。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xA,
        (
            "#5P顺便一提，使用这张卡片\x01",
            "可以前往的楼层，与上次给各位\x01",
            "卡片时相同。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xA,
        (
            "#5P玛丽亚贝尔大小姐就在十六层的\x01",
            "总裁室等候你们，\x01",
            "请各位移步。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#12P#00000F好的，谢谢。\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x7A, 0x1, 0x0)
    SetScenarioFlags(0x157, 0)
    Return()

    # Function_27_97C5 end

    def Function_28_9A5E(): pass

    label("Function_28_9A5E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找消失的收藏品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7A, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_28_9A5E end

    def Function_29_9AC0(): pass

    label("Function_29_9AC0")

    EventBegin(0x0)
    SoundLoad(836)
    OP_4B(0xA, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-230, 1400, 29510, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15440, 0)
    SetChrPos(0x101, -470, 300, 28930, 0)
    SetChrPos(0x102, 540, 300, 28690, 0)
    SetChrPos(0x103, -1190, 300, 27930, 0)
    SetChrPos(0x104, -70, 300, 27510, 0)
    SetChrPos(0x109, 890, 300, 27020, 0)
    SetChrPos(0x105, -810, 300, 26570, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0542
    ChrTalk(
        0xA,
        (
            "#5P哎呀，是特别任务支援科的各位……\x01",
            "今天来这里有何贵干？\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x101,
        (
            "#00000F嗯……\x01",
            "其实我们正在调查一起案件，\x01",
            "希望ＩＢＣ提供协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#00100F兰菲小姐，\x01",
            "你可以帮忙调查\x01",
            "ＩＢＣ的某个银行账户吗？\x02\x03",

            "我们想借此确认\x01",
            "那个银行账户的\x01",
            "资金流向。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xA,
        "#5P啊……银行账户吗？\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xA,
        (
            "#5P这个嘛……\x01",
            "如果牵扯到了犯罪行为，\x01",
            "倒也是允许的……\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xA,
        (
            "#5P……可以先把事情的\x01",
            "详细情况告诉我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        (
            "#00000F好的，我明白了。\x01",
            "其实是这样的……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将存在诈骗嫌疑的\x01",
            "事件做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0550
    ChrTalk(
        0xA,
        (
            "#5P原来如此……\x01",
            "是这么一回事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x103,
        (
            "#00200F这可以算是\x01",
            "调查理由吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x105,
        (
            "#10300F如果任由他人利用\x01",
            "银行账户从事犯罪行为，\x01",
            "也会影响到ＩＢＣ的信誉呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0553
    ChrTalk(
        0xA,
        (
            "#5P嗯，是啊……此事确实有\x01",
            "涉及犯罪行为的可能……\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xA,
        (
            "#5P口头告诉你们一些\x01",
            "终端内的情报，\x01",
            "我想应该是没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x101,
        (
            "#00000F嗯，这就足够了，\x01",
            "麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xA,
        "#5P我明白了，那么……\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)

    #C0557
    ChrTalk(
        0xA,
        (
            "#5P开户人是『敏涅斯』先生……\x01",
            "（敲击键盘）\x02",
        )
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xA,
        (
            "#5P『昆西公司』的子公司\x01",
            "『阿尔摩利卡·甜蜜商社』……\x01",
            "（敲击键盘）\x02",
        )
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0559
    ChrTalk(
        0xA,
        (
            "#5P找到了，\x01",
            "的确有这个账户呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xA,
        "#5P……哎……？\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x109,
        (
            "#10100F怎、怎么了？\x02\x03",

            "这个账户\x01",
            "确实有什么问题……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    #C0562
    ChrTalk(
        0xA,
        (
            "#5P唔……虽然不能\x01",
            "把具体金额\x01",
            "透露给各位……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xA,
        (
            "#5P但『阿尔摩利卡·甜蜜商社』的帐户里\x01",
            "只存入了最低限度的米拉。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x101,
        (
            "#00000F请问……\x01",
            "这是什么意思……？\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xA,
        (
            "#5P哦，是这样的。\x01",
            "如果要开设公司性质的银行账户，\x01",
            "必须存入一定资本金……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xA,
        (
            "#5P而这个帐户里只有开设账户\x01",
            "所需的最低金额……也就是说，\x01",
            "只有几万米拉而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0567
    ChrTalk(
        0x103,
        (
            "#00200F既要建设糕点工厂，\x01",
            "又要管理各处田地……\x02\x03",

            "这点钱\x01",
            "明显不够……\x01",
            "是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x102,
        (
            "#00100F他明明已向村民们征收了土地产权证，\x01",
            "还做了不少生意，\x01",
            "但账户中的资金却没有任何变动……\x02\x03",

            "……嗯，\x01",
            "确实相当可疑。\x02\x03",

            "他恐怕是为了获取迪利克先生的信赖，\x01",
            "才会专门开设这个账户，\x01",
            "用来做做样子吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x105,
        (
            "#10300F原来如此。\x01",
            "呵呵，这就出现明显的疑点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        (
            "#00000F嗯，我们得到了重要的情报。\x02\x03",

            "兰菲小姐，\x01",
            "非常感谢您的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xA,
        (
            "#5P不用谢，只要我们能帮得上忙，\x01",
            "一定会不遗余力地提供协助……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xA,
        (
            "#5P今后要是还有什么事，\x01",
            "请不必客气，随时过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x102,
        "#00100F呵呵，我们会的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A48F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0574
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆麦克道尔宅（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不变更】\x01",      # 0
            "【已调查】\x01",      # 1
            "【未调查】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A47A"),
        (1, "loc_A47F"),
        (2, "loc_A487"),
        (SWITCH_DEFAULT, "loc_A48F"),
    )


    label("loc_A47A")

    Jump("loc_A48F")

    label("loc_A47F")

    SetScenarioFlags(0x177, 5)
    Jump("loc_A48F")

    label("loc_A487")

    ClearScenarioFlags(0x177, 5)
    Jump("loc_A48F")

    label("loc_A48F")

    OP_29(0x87, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_A528")
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0575
    ChrTalk(
        0x101,
        (
            "#00000F好……我们已经收集到\x01",
            "不少可以证明敏涅斯\x01",
            "行事可疑的证据了。\x02\x03",

            "先回哈罗德\x01",
            "先生家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x109,
        "#10100F是，队长！\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_A58D")

    label("loc_A528")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0577
    ChrTalk(
        0x101,
        (
            "#00000F……接下来的工作，只剩下去\x01",
            "麦克道尔宅邸调查了，赶快行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x109,
        "#10100F好的！\x02",
    )

    CloseMessageWindow()

    label("loc_A58D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x177, 4)
    SetChrPos(0x0, 0, 300, 28600, 180)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_29_9AC0 end

    def Function_30_A5CB(): pass

    label("Function_30_A5CB")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A65B")

    #C0579
    ChrTalk(
        0x8,
        (
            "不好意思，必须要有认证卡，\x01",
            "才能乘坐导力梯。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x8,
        (
            "如果有什么事，\x01",
            "请去服务台说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x101,
        "#00000F嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 6)
    Jump("loc_A6B1")

    label("loc_A65B")


    #C0582
    ChrTalk(
        0x8,
        (
            "不好意思，必须要有认证卡，\x01",
            "才能乘坐导力梯。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x8,
        (
            "如果有什么事，\x01",
            "请去服务台说明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6B1")

    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_30_A5CB end

    SaveToFile()

Try(main)
