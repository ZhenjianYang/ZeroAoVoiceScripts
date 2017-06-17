from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0470.bin",                # FileName
        "c0470",                    # MapName
        "c0470",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 37, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0470",                  # 0
        "多雷克老板",             # 1
        "切莉",                   # 2
        "加雷提",                 # 3
        "艾琳迪",                 # 4
        "雷特罗莎",               # 5
        "利凯爷爷",               # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "雷克特",                 # 10
        "比克森镇长",             # 11
        "冈兹",                   # 12
        "雷克特",                 # 13
    ))

    AddCharChip((
        "chr/ch20002.itc",                   # 00
        "chr/ch21200.itc",                   # 01
        "chr/ch25800.itc",                   # 02
        "chr/ch25900.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch32300.itc",                   # 06
        "chr/ch32302.itc",                   # 07
        "chr/ch33302.itc",                   # 08
        "chr/ch07402.itc",                   # 09
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(1350,    -949,    11500,   0,    341,  0x0, 0,   8,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   0,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(0,       -1000,   5349,    225,  389,  0x0, 0,   1,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(0,       -1000,   5349,    225,  389,  0x0, 0,   6,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(3299,    -949,    12590,   315,  469,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(1820,    4000,    18850,   0,    469,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  5,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  7,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  9,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  11, 0x0000)
    DeclActor(7530,    4000,    17960,   1800,    7530,    5500,    17960,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    15750,   1800,    7530,    5500,    15750,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    13410,   1800,    7530,    5500,    13410,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    10460,   1800,    7530,    5500,    10460,   0x007C, 0,  20, 0x0000)
    DeclActor(7530,    4000,    8300,    1800,    7530,    5500,    8300,    0x007C, 0,  20, 0x0000)

    ScpFunction((
        "Function_0_3E4",          # 00, 0
        "Function_1_49C",          # 01, 1
        "Function_2_4C7",          # 02, 2
        "Function_3_61B",          # 03, 3
        "Function_4_713",          # 04, 4
        "Function_5_7D0",          # 05, 5
        "Function_6_7D4",          # 06, 6
        "Function_7_221D",         # 07, 7
        "Function_8_2221",         # 08, 8
        "Function_9_3433",         # 09, 9
        "Function_10_3437",        # 0A, 10
        "Function_11_408C",        # 0B, 11
        "Function_12_4090",        # 0C, 12
        "Function_13_4CBB",        # 0D, 13
        "Function_14_5D70",        # 0E, 14
        "Function_15_6E1C",        # 0F, 15
        "Function_16_6FD2",        # 10, 16
        "Function_17_729D",        # 11, 17
        "Function_18_72D9",        # 12, 18
        "Function_19_7842",        # 13, 19
        "Function_20_7B82",        # 14, 20
        "Function_21_7C0C",        # 15, 21
        "Function_22_7E7A",        # 16, 22
        "Function_23_865D",        # 17, 23
        "Function_24_9B78",        # 18, 24
        "Function_25_9BD3",        # 19, 25
        "Function_26_9C2E",        # 1A, 26
        "Function_27_9C54",        # 1B, 27
        "Function_28_9C7A",        # 1C, 28
        "Function_29_9FCF",        # 1D, 29
    ))


    def Function_0_3E4(): pass

    label("Function_0_3E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_424"),
        (1, "loc_430"),
        (2, "loc_43C"),
        (3, "loc_448"),
        (4, "loc_454"),
        (5, "loc_460"),
        (6, "loc_46C"),
        (SWITCH_DEFAULT, "loc_478"),
    )


    label("loc_424")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_430")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_43C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_448")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_454")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_460")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_46C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_478")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_484")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_484")

    label("loc_49B")

    Return()

    # Function_0_3E4 end

    def Function_1_49C(): pass

    label("Function_1_49C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C6")
    OP_94(0xFE, 0x744, 0x1BD0, 0xFFFFF704, 0xB2C, 0x3E8)
    Sleep(300)
    Jump("Function_1_49C")

    label("loc_4C6")

    Return()

    # Function_1_49C end

    def Function_2_4C7(): pass

    label("Function_2_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E2")
    SetMapFlags(0x10000000)
    Event(0, 23)
    Jump("loc_4F4")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F4")
    Event(0, 19)

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_508")
    ClearScenarioFlags(0x5C, 0)
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_527")
    SetChrPos(0xD, 50, 4050, 18950, 0)
    Jump("loc_61A")

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_535")
    Jump("loc_61A")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_55B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_551")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_556")

    label("loc_551")

    SetChrFlags(0x8, 0x80)

    label("loc_556")

    Jump("loc_61A")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_587")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_61A")

    label("loc_587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_595")
    Jump("loc_61A")

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C1")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_61A")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D4")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_61A")

    label("loc_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5EF")
    ClearChrFlags(0x10, 0x80)
    SetChrSubChip(0x10, 0x1)
    SetChrSubChip(0xC, 0x2)
    Jump("loc_61A")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_602")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_61A")

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_615")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_61A")

    label("loc_615")

    ClearChrFlags(0xE, 0x80)

    label("loc_61A")

    Return()

    # Function_2_4C7 end

    def Function_3_61B(): pass

    label("Function_3_61B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_634")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_63A")

    label("loc_634")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_63A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -6000, -1000, 16000, 5000, 5000, 0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67B")
    OP_1B(0x0, 0x0, 0x1D)

    label("loc_67B")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_691")
    OP_66(0x5, 0x1)
    Jump("loc_712")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_712")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_6AD")
    Jump("loc_712")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_6C4")
    Jump("loc_6C8")

    label("loc_6C4")

    OP_65(0x0, 0x1)

    label("loc_6C8")

    Jump("loc_712")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_6EB")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jump("loc_712")

    label("loc_6EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6F9")
    Jump("loc_712")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_712")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)

    label("loc_712")

    Return()

    # Function_3_61B end

    def Function_4_713(): pass

    label("Function_4_713")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_724")
    Jump("loc_7CC")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_732")
    Jump("loc_7CC")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_740")
    Jump("loc_7CC")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_7CC")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_75C")
    Jump("loc_7CC")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_76A")
    Jump("loc_7CC")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_778")
    Jump("loc_7CC")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_786")
    Jump("loc_7CC")

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_794")
    Jump("loc_7CC")

    label("loc_794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7A2")
    Jump("loc_7CC")

    label("loc_7A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7B0")
    Jump("loc_7CC")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7BE")
    Jump("loc_7CC")

    label("loc_7BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7CC")
    Jump("loc_7CC")

    label("loc_7CC")

    TalkEnd(0xFE)
    Return()

    # Function_4_713 end

    def Function_5_7D0(): pass

    label("Function_5_7D0")

    Call(0, 6)
    Return()

    # Function_5_7D0 end

    def Function_6_7D4(): pass

    label("Function_6_7D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EA")
    Call(0, 22)
    Jump("loc_221C")

    label("loc_7EA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_872")

    #C0001
    ChrTalk(
        0x8,
        (
            "冈兹先生好像还是\x01",
            "没有光临本店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "嗯……本店\x01",
            "也觉得十分遗憾。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "希望您能忘记昨天的事，\x01",
            "下次再来这里享乐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2219")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8ED")

    #C0004
    ChrTalk(
        0x8,
        (
            "雷克特先生昨晚\x01",
            "发牢骚说，\x01",
            "帝国已经通知他回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "他还留话说，\x01",
            "祝愿各位旗开得胜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A68")

    label("loc_8ED")


    #C0006
    ChrTalk(
        0x8,
        (
            "说起来……\x01",
            "雷克特先生\x01",
            "今天没来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "昨天好像听他说过，\x01",
            "要回帝国什么的。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#0005F哎……\x01",
            "也就是说，他已经回国了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "是的，听说有什么\x01",
            "麻烦得要死，但非得他\x01",
            "亲自出马的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#0003F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        (
            "#0101F还以为\x01",
            "他应该知道些什么的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        (
            "#0206F算了，反正他那种人\x01",
            "就算知道些什么，\x01",
            "也不会老老实实说出来的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A62")

    #C0013
    ChrTalk(
        0x10A,
        "#0605F（……在说谁呢………？）\x02",
    )

    CloseMessageWindow()

    label("loc_A62")

    SetScenarioFlags(0xD0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_A68")

    Jump("loc_BC2")

    label("loc_A6D")


    #C0014
    ChrTalk(
        0x8,
        (
            "您找冈兹先生吗，\x01",
            "他今天没来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "因为昨天发生了那种事嘛，\x01",
            "可能是不好意思再露面了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0001F嗯，倒也并没指望在这里找到他……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x104,
        (
            "#0303F其实……稍微出现了一些意外情况。\x02\x03",

            "#0300F老板，要是看到\x01",
            "那位老兄的话，\x01",
            "就请联系我们支援科吧。\x02\x03",

            "我们有点事找他。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "好的，没问题……\x01",
            "是不是跟什么犯罪事件有关啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 6)

    label("loc_BC2")

    Jump("loc_2219")

    label("loc_BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 5)), scpexpr(EXPR_END)), "loc_C84")

    #C0019
    ChrTalk(
        0x8,
        (
            "我去跟服务员们说说，\x01",
            "让他们不要把冈兹先生发疯\x01",
            "的事情外传。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "虽然多少还会传出一些流言蜚语……\x01",
            "算了，这里终究是流言横行的欢乐街嘛。\x01",
            "这种话题很快就会被遗忘的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E22")

    label("loc_C84")


    #C0021
    ChrTalk(
        0x8,
        (
            "刚才真是谢谢你们了。\x01",
            "请容我再次表示谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#0306F运气还算不错啊。\x01",
            "要是放着不管，还不知道会发生什么事……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003F是啊，倚仗着那种怪力，\x01",
            "恐怕不是把人打伤\x01",
            "就可以了结的……\x02\x03",

            "#0001F老板，如果可以的话，\x01",
            "今天发生的事情，能否暂时不要声张出去？\x02\x03",

            "因为我们还在\x01",
            "整理整个事件的经过……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "好的，对我们来说，\x01",
            "这也不是什么好事。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "虽然多少也会流出去一些传言吧，\x01",
            "但我会尽量劝说服务员们，\x01",
            "让他们不要随便乱讲。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 5)

    label("loc_E22")

    Jump("loc_2219")

    label("loc_E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_EB6")

    #C0026
    ChrTalk(
        0x8,
        (
            "冈兹先生是我们的老顾客了，\x01",
            "不可能会认错的。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "他应该住在千禧酒店\x01",
            "最顶层的\x01",
            "豪华套房里。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "如果您有事，可以去那里找他。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2219")

    label("loc_EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1150")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F90")

    #C0029
    ChrTalk(
        0x8,
        (
            "兰迪，稍微玩两把倒是没问题，\x01",
            "但不要太得意忘形哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "这种东西，\x01",
            "不管运气有多好，总有一天\x01",
            "也都会连本带利全部还回去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0306F知道知道，这些我都清楚啊。\x01",
            "（……老板好像\x01",
            "  有点紧张啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_114B")

    label("loc_F90")


    #C0032
    ChrTalk(
        0x104,
        (
            "#0300F老板，好久不见，\x01",
            "我又来玩啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "……兰迪，怎么又是你。\x01",
            "去去去，你还是别来为好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "多亏你最近没来玩，\x01",
            "我们这里的营业额也……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        "………………………………\x02",
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

    #C0036
    ChrTalk(
        0x104,
        "#0305F怎么了吗？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "……没有啦。\x01",
            "没什么大不了的。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "算了，要玩的话，\x01",
            "也记得要适可而止啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "这种东西，\x01",
            "不管运气有多好，总有一天\x01",
            "也都会连本带利全部还回去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_114B")

    Jump("loc_2219")

    label("loc_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_158D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11AE")

    #C0040
    ChrTalk(
        0x8,
        (
            "各位，一定不要随便插手\x01",
            "鲁巴彻商会之类的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "请多加小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1588")

    label("loc_11AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_137B")
    TurnDirection(0x8, 0x104, 0)

    #C0042
    ChrTalk(
        0x8,
        (
            "兰迪，听说你跑到鲁巴彻商会\x01",
            "的地盘上去了？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "哼，竟然又去插手\x01",
            "这种危险的事情啊。\x01",
            "不是都说过，叫你不要去管他们了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0306F啊，那只是顺势去一趟而已啦。\x01",
            "不过，确实是发生了一点小麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "哼……不是警备队就是警察，\x01",
            "你就会选这种危险的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "兰迪，现在也不晚，\x01",
            "还是赶快转行，找个安稳的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#0000F（哈哈……老板\x01",
            "  好像很了解你呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0300F（……从我刚刚来到\x01",
            "  克洛斯贝尔的时候，\x01",
            "  就常来这里玩了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1585")

    label("loc_137B")


    #C0049
    ChrTalk(
        0x8,
        (
            "听说各位跟兰迪一起\x01",
            "跑到鲁巴彻商会\x01",
            "的地盘上了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "你们要小心一点啊。\x01",
            "如果跟那些家伙扯上关系，可是没有什么好下场的。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "你们也好好教训一下兰迪吧。\x01",
            "那家伙……不是警备队就是警察，\x01",
            "就会选这种危险的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#0000F哈哈，让您担心了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14AC")

    #C0053
    ChrTalk(
        0x102,
        (
            "#0100F老板，您好像和兰迪\x01",
            "很熟啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EB")

    label("loc_14AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14EB")

    #C0054
    ChrTalk(
        0x103,
        (
            "#0200F老板对兰迪前辈\x01",
            "的事情好像很熟悉呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EB")


    #C0055
    ChrTalk(
        0x8,
        "嗯，是啊……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "因为兰迪从刚来到\x01",
            "克洛斯贝尔的时候开始，\x01",
            "就常来我这里玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "虽然没有太深入的了解……\x01",
            "不过，那家伙总有些\x01",
            "让人放不下心的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1585")

    SetScenarioFlags(0x0, 0)

    label("loc_1588")

    Jump("loc_2219")

    label("loc_158D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1700")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_162A")

    #C0058
    ChrTalk(
        0x8,
        (
            "据说，在一个叫做什么导力网络的东西上，\x01",
            "有人在做着『情报商』的生意……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "呵呵，不知为何，\x01",
            "那种人的手法最近也变得新潮起来了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FB")

    label("loc_162A")


    #C0060
    ChrTalk(
        0x8,
        (
            "我听说，\x01",
            "在导力网络中，还有专门以\x01",
            "贩卖情报为职业的『情报商』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "从普通的情报收集\x01",
            "到非法信息的网罗，\x01",
            "都在他的营业范畴中。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "呵呵，以前这都是\x01",
            "黑道小弟们干的工作……\x01",
            "最近不知怎么变得新潮起来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16FB")

    Jump("loc_2219")

    label("loc_1700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_18D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17A6")

    #C0063
    ChrTalk(
        0x8,
        (
            "说到底，市长毕竟是经历过自治州刚创立时的\x01",
            "那段动荡时代的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "在这十五年来，\x01",
            "克洛斯贝尔能一直和平稳定的发展，\x01",
            "也都是拜他的手腕所赐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CF")

    label("loc_17A6")


    #C0065
    ChrTalk(
        0x8,
        (
            "说到亨利·麦克道尔，\x01",
            "那可是在这十五年间\x01",
            "始终担任着市长一职的中立派政治家啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "在这十五年中，\x01",
            "克洛斯贝尔也发生了各种各样的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "多亏了他操控着舵盘，始终把握着正确的\x01",
            "大方向，才能一次次渡过难关。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "从我这种人嘴里\x01",
            "说出这样的话可能有点奇怪，\x01",
            "不过，那位先生可真是个了不起的人物。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18CF")

    Jump("loc_2219")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1A27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_192F")

    #C0069
    ChrTalk(
        0x8,
        (
            "……兰迪，休息区\x01",
            "总是有空座的。\x01",
            "有兴趣的时候，就过来喝一杯吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A22")

    label("loc_192F")


    #C0070
    ChrTalk(
        0x8,
        (
            "怎么了，兰迪，\x01",
            "一幅无精打采的表情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，是吗？\x02\x03",

            "#0306F唉，在工作中遇到了很多事啊。\x01",
            "不过也没什么值得一提的。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        "哼，是吗……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "其实啊，\x01",
            "今天进到了好酒哦。\x01",
            "等你有心情的时候，就来喝上一杯吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        "#0300F嗯，到时见啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A22")

    Jump("loc_2219")

    label("loc_1A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AA2")

    #C0075
    ChrTalk(
        0x8,
        (
            "说到鲁巴彻，\x01",
            "那可是统率着克洛斯贝尔黑道势力的首领……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "各位，可不要干出什么\x01",
            "过火的事情哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C43")

    label("loc_1AA2")

    TurnDirection(0x8, 0x104, 0)

    #C0077
    ChrTalk(
        0x8,
        (
            "兰迪，听说你们正在\x01",
            "四处打探鲁巴彻的事情？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x104,
        "#0306F呃……你怎么知道的……！？\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "先别管这个，总之，你们赶快停手吧。\x01",
            "那可不是你们这种小警察\x01",
            "就能对付的组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "在克洛斯贝尔……特别是\x01",
            "在这条欢乐街上开店的人，\x01",
            "全都是心知肚明的。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "我们店也一样，为了不跟他们起冲突，\x01",
            "还要交纳保护费呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        "#0108F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C43")

    Jump("loc_2219")

    label("loc_1C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CCD")

    #C0083
    ChrTalk(
        0x8,
        (
            "又是纪念庆典，又是彩虹剧团的新剧，\x01",
            "市里这么热闹，也就可以理解了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "我们也热切期盼着\x01",
            "下个月的到来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D6A")

    label("loc_1CCD")


    #C0085
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎来到『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "也许因为纪念庆典临近，\x01",
            "现在客人很多，热闹极了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "前些天，彩虹剧团的新剧\x01",
            "开始正式售票了……\x01",
            "真是热闹极了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D6A")

    Jump("loc_2219")

    label("loc_1D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1E51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DCA")

    #C0088
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎来到『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "希望您今天也能\x01",
            "玩得尽兴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4C")

    label("loc_1DCA")


    #C0090
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎来到『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "如果您感到疲劳的话，\x01",
            "可以在本店的休息厅里休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "本店可以为您提供\x01",
            "美味的利口酒。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E4C")

    Jump("loc_2219")

    label("loc_1E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1FEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1EBE")

    #C0093
    ChrTalk(
        0x8,
        (
            "今晚有ＶＩＰ客户\x01",
            "预约要来本店。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "是政府的高官与陪同人员……\x01",
            "所以要招待他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE9")

    label("loc_1EBE")


    #C0095
    ChrTalk(
        0x8,
        (
            "今晚有ＶＩＰ客户\x01",
            "预约来本店消费。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "是政府的高官与陪同人员。\x01",
            "在特等席招待他们好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        (
            "#0306F唉～又来了吗。\x01",
            "公款吃喝玩乐的事情，最近好像相当多啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)
    Sleep(300)

    #C0098
    ChrTalk(
        0x8,
        (
            "客人增加了，\x01",
            "这对我们来说就足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "兰迪，你可别跑到特等席来\x01",
            "搅局啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0306F我知道啦，\x01",
            "我也不想和那些家伙作对啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1FE9")

    Jump("loc_2219")

    label("loc_1FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_END)), "loc_2077")

    #C0101
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎来到『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "本店竭诚欢迎所有顾客，\x01",
            "除了蠢兰迪。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#0306F喂喂，\x01",
            "我也是客人啊，狸猫大叔……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2219")

    label("loc_2077")

    TurnDirection(0x8, 0x101, 0)

    #C0104
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎来到『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "玩一局轮盘如何？\x01",
            "正好有空座呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#0301F喂，狸猫大叔，\x01",
            "为什么不来招呼我啊～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)
    Sleep(300)

    #C0107
    ChrTalk(
        0x8,
        (
            "……兰迪，\x01",
            "你还是不来为好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "去去去，我还得为\x01",
            "其他客人服务呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#0301F呜哇，太过分了，故意排挤我，\x01",
            "难道是怕我在这里大赢一票吗？\x02\x03",

            "#0300F哼，给我记好了。\x01",
            "今晚我绝对会再来的！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        "去去去，给我闭嘴，臭小子！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#0100F（是老顾客了吗……\x01",
            "  这还真是奇怪的关系啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 0)

    label("loc_2219")

    TalkEnd(0x8)

    label("loc_221C")

    Return()

    # Function_6_7D4 end

    def Function_7_221D(): pass

    label("Function_7_221D")

    Call(0, 8)
    Return()

    # Function_7_221D end

    def Function_8_2221(): pass

    label("Function_8_2221")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2246")
    Call(0, 28)
    Return()

    label("loc_2246")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2253")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_342F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "进行交换\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22A7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_22A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230D")
    SetScenarioFlags(0x6D, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_22C9")
    OP_AF(0x41)
    Jump("loc_22FE")

    label("loc_22C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_22D9")
    OP_AF(0x40)
    Jump("loc_22FE")

    label("loc_22D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_22E9")
    OP_AF(0x3F)
    Jump("loc_22FE")

    label("loc_22E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_22FC")
    OP_AF(0x3E)
    Jump("loc_22FE")

    label("loc_22FC")

    OP_AF(0x3D)

    label("loc_22FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_342A")

    label("loc_230D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2321")
    Jump("loc_342A")

    label("loc_2321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_342A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_23F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_236F")

    #C0112
    ChrTalk(
        0x9,
        "大家一起努力大赚一笔吧⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_23EC")

    label("loc_236F")


    #C0113
    ChrTalk(
        0x9,
        "欢迎来到『巴鲁卡』～！\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "嘿嘿嘿，通过昨天的那件事，\x01",
            "『巴鲁卡』也变得\x01",
            "很有名了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        "客人也变多了，我好开心～☆\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_23EC")

    Jump("loc_342A")

    label("loc_23F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_24E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2455")

    #C0116
    ChrTalk(
        0x9,
        (
            "雷克特先生和老板\x01",
            "似乎挺合得来呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        "感觉就像是认识已久的老顾客一样⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_24E0")

    label("loc_2455")


    #C0118
    ChrTalk(
        0x9,
        "嘿嘿，欢迎来到『巴鲁卡』～！\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "昨天老板跟雷克特先生\x01",
            "喝酒喝到很晚。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "嘿嘿，虽然雷克特先生有些奇怪，\x01",
            "不过说的话都很有趣呢～☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24E0")

    Jump("loc_342A")

    label("loc_24E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_2574")

    #C0121
    ChrTalk(
        0x9,
        (
            "那个战胜了冈兹先生的人，\x01",
            "跟老板一起喝了酒～\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "在最后的决胜局中，\x01",
            "竟然亮出了一组\x01",
            "五同点呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        "他肯定是个超级牌技师吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_342A")

    label("loc_2574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2733")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25F4")

    #C0124
    ChrTalk(
        0x9,
        (
            "冈兹先生正在和\x01",
            "其他客人玩牌呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "在加雷提先生和艾琳迪小姐\x01",
            "都实力不敌的时候，\x01",
            "有人发起了挑战呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272E")

    label("loc_25F4")


    #C0126
    ChrTalk(
        0x9,
        (
            "啊，兰迪先生～\x01",
            "你要找老板吗，\x01",
            "他到特别室里去了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "从一大早就去为\x01",
            "冈兹先生的牌局做裁判了～\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#0305F特别室……就是那个只有\x01",
            "ＶＩＰ才能使用的房间吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "是啊，好像是在和一位客人\x01",
            "进行重要比试呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "之前一直都是个\x01",
            "毫不起眼的普通客人，\x01",
            "现在居然混到ＶＩＰ级别了～\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        "#0201F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_272E")

    Jump("loc_342A")

    label("loc_2733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2813")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_278F")

    #C0132
    ChrTalk(
        0x9,
        (
            "冈兹先生\x01",
            "最近运势当头呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        "跟以前比起来，简直就是判若两人～\x02",
    )

    CloseMessageWindow()
    Jump("loc_280E")

    label("loc_278F")


    #C0134
    ChrTalk(
        0x9,
        (
            "说起来，冈兹先生\x01",
            "最近样子有些奇怪呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "态度变得特别嚣张蛮横～\x01",
            "而且不断取胜～\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        "和以前相比，简直就像是变了个人。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_280E")

    Jump("loc_342A")

    label("loc_2813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_287B")

    #C0137
    ChrTalk(
        0x9,
        "想知道关于冈兹先生的事……？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "那还是去问\x01",
            "老板比较好哦。\x01",
            "因为他们总在休息厅说话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_342A")

    label("loc_287B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28EF")

    #C0139
    ChrTalk(
        0x9,
        (
            "但是……那个人居然\x01",
            "能赢得那么盆满钵满～\x01",
            "我都有点难以相信～\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        (
            "他最近玩得十分\x01",
            "豪气哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5B")

    label("loc_28EF")


    #C0141
    ChrTalk(
        0x9,
        (
            "最近有位客人一个人\x01",
            "包下了最里面的特别室。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "那是一位非常豪气的客人～\x01",
            "玩得非常大哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x9,
        (
            "昨天是跟加雷提先生玩，\x01",
            "还打出了一个同花顺呢，\x01",
            "大家都一起鼓掌给他叫好～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#0305F什、什么！？\x01",
            "除了我以外，竟然还有\x01",
            "其他人敢如此出风头……\x02\x03",

            "#0301F不可原谅！\x01",
            "让他跟我比一场！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#0006F兰迪，别跟着凑热闹啦。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x109,
        (
            "#0506F兰迪前辈……\x01",
            "看来你是真的很擅长\x01",
            "这个呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2A5B")

    Jump("loc_342A")

    label("loc_2A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2ABC")

    #C0147
    ChrTalk(
        0x9,
        (
            "这里是交换奖品和代币的\x01",
            "柜台哟⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        "请多多交换，尽情玩乐吧～☆\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BB2")

    label("loc_2ABC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B58")

    #C0149
    ChrTalk(
        0x9,
        (
            "啊呀，是兰迪先生～\x01",
            "您很久没来啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "算啦，无所谓了～\x01",
            "今天就玩个尽兴吧～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，今天有工作在身，\x01",
            "只能稍微玩一会哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BAF")

    label("loc_2B58")


    #C0152
    ChrTalk(
        0x9,
        (
            "咦，今天没跟\x01",
            "兰迪先生一起来吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "算啦，无所谓了～\x01",
            "大家一定要\x01",
            "玩个尽兴啊～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BAF")

    SetScenarioFlags(0x0, 1)

    label("loc_2BB2")

    Jump("loc_342A")

    label("loc_2BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C01")

    #C0154
    ChrTalk(
        0x9,
        (
            "警察其实是个挺不错的职业呀～\x01",
            "我都有点羡慕呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D42")

    label("loc_2C01")


    #C0155
    ChrTalk(
        0x9,
        (
            "啊呀，兰迪先生，\x01",
            "大白天的，就来这里玩吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "这可不行啊。\x01",
            "我要去向你们的科长\x01",
            "打小报告哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#0300F科长……\x01",
            "大概不会因为这种事情生气吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#0003F嗯，因为他都采取放任自由主义啊……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        "#0200F说不定连他自己也会来这里玩呢。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#0106F虽然他确实也有\x01",
            "认真的一面，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "是吗～\x01",
            "感觉这位科长人很好呢☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2D42")

    Jump("loc_342A")

    label("loc_2D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DA9")

    #C0162
    ChrTalk(
        0x9,
        (
            "老板平时总是\x01",
            "有点威严的压迫感……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        "但得知他的过去后，我就理解了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E98")

    label("loc_2DA9")


    #C0164
    ChrTalk(
        0x9,
        (
            "听说啊，老板原来\x01",
            "在欢乐街是混黑道的～\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        (
            "不过，最后好像是被鲁巴彻\x01",
            "击溃了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "听说他的胸口上\x01",
            "现在还留有枪伤的疤痕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#0305F哎，那个狸猫大叔……\x01",
            "竟然还有这种过去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "呵呵，这可是秘密哟☆\x01",
            "他让我不要\x01",
            "到处跟别人乱说的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E98")

    Jump("loc_342A")

    label("loc_2E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2F0A")

    #C0169
    ChrTalk(
        0x9,
        "欢迎来到『巴鲁卡』～！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔的夜晚，现在才刚要开始哟⊥\x01",
            "请大家都要玩得尽兴哦～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_342A")

    label("loc_2F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F94")

    #C0171
    ChrTalk(
        0x9,
        (
            "彩虹剧团的公演\x01",
            "下个月就要开始了吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "因为本店离剧团很近，\x01",
            "到时候肯定会有很多客人顺路来玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        "呵呵，好期待啊～⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_342A")

    label("loc_2F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_310F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2FF7")

    #C0174
    ChrTalk(
        0x9,
        (
            "兰迪先生最近都不来\x01",
            "这里玩通宵了……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x9,
        (
            "切莉好无聊啊。\x01",
            "要多来玩呀～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310A")

    label("loc_2FF7")


    #C0176
    ChrTalk(
        0x9,
        "欢迎来到『巴鲁卡』☆\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "这不是兰迪先生吗，\x01",
            "最近都不来玩呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        (
            "#0300F抱歉啦，小切莉，\x01",
            "工作实在是太忙了。\x01",
            "一周也只能来三次而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x9,
        (
            "哼哼，才不管，\x01",
            "你不来，人家好无聊啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0006F我觉得一周三次\x01",
            "就已经很频繁了……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#0200F兰迪前辈这个\x01",
            "坏习惯还是没有改正啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_310A")

    Jump("loc_342A")

    label("loc_310F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_320E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3186")

    #C0182
    ChrTalk(
        0x9,
        (
            "前面的大街上\x01",
            "好像发生了什么事件呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x9,
        (
            "不过，只要待在店里别出去，\x01",
            "就不会有什么问题啦～☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3209")

    label("loc_3186")


    #C0184
    ChrTalk(
        0x9,
        "刚才有警察过来了。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "在昨晚，前面的大街上\x01",
            "好像发生了什么事件呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "不过，只要待在店里别出去，\x01",
            "就不会有什么问题啦～☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3209")

    Jump("loc_342A")

    label("loc_320E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_325C")

    #C0187
    ChrTalk(
        0x9,
        (
            "老板是不是\x01",
            "不会再赌了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        "有一点点遗憾呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3300")

    label("loc_325C")


    #C0189
    ChrTalk(
        0x9,
        (
            "加雷提先生和艾琳迪小姐\x01",
            "的技术都相当高超呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "听说，如果他们拿出全力的话，\x01",
            "就会百战百胜。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "不过，据说老板\x01",
            "比那两个人还要厉害。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        "好想见识一回啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3300")

    Jump("loc_342A")

    label("loc_3305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3356")

    #C0193
    ChrTalk(
        0x9,
        (
            "这里是交换奖品和代币\x01",
            "的柜台⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x9,
        "请多多交换，尽情玩乐吧～☆\x02",
    )

    CloseMessageWindow()
    Jump("loc_342A")

    label("loc_3356")


    #C0195
    ChrTalk(
        0x9,
        "欢迎来到『巴鲁卡』～！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        "啊，是兰迪先生～\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        (
            "嘿嘿，就像平时一样，\x01",
            "玩个尽兴再走吧～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        (
            "#0309F好呀，小切莉，\x01",
            "这当然没问题！\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#0106F（他好像总是\x01",
            "  来这里玩呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#0006F（真拿他没办法……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_342A")

    Jump("loc_2253")

    label("loc_342F")

    TalkEnd(0x9)
    Return()

    # Function_8_2221 end

    def Function_9_3433(): pass

    label("Function_9_3433")

    Call(0, 10)
    Return()

    # Function_9_3433 end

    def Function_10_3437(): pass

    label("Function_10_3437")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3444")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4088")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "玩扑克\x01",          # 1
            "玩二十一点\x01",      # 2
            "放弃\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34A1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_34A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F1")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_34F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3541")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_3541")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3555")
    Jump("loc_4083")

    label("loc_3555")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4083")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_35ED")

    #C0201
    ChrTalk(
        0xA,
        (
            "冈兹先生\x01",
            "今天没有来。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xA,
        (
            "嗯……在往日，他最晚\x01",
            "也都会在傍晚时过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xA,
        (
            "难道还在对昨天\x01",
            "那件事耿耿于怀吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4083")

    label("loc_35ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3651")

    #C0204
    ChrTalk(
        0xA,
        (
            "整个『巴鲁卡』都在\x01",
            "谈论昨天的那件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xA,
        (
            "好久都没有看过\x01",
            "那么扣人心弦的牌局了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4083")

    label("loc_3651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_3708")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3687")

    #C0206
    ChrTalk(
        0xA,
        (
            "冈兹先生的身体\x01",
            "还安好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3703")

    label("loc_3687")


    #C0207
    ChrTalk(
        0xA,
        (
            "十分担心冈兹先生\x01",
            "的身体状况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xA,
        (
            "虽然在比赛的过程中，\x01",
            "的确发生了一些口角。\x01",
            "不过都是本店的熟客，也没什么关系的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3703")

    Jump("loc_4083")

    label("loc_3708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3770")

    #C0209
    ChrTalk(
        0xA,
        (
            "……冈兹先生今天\x01",
            "似乎也能赢很多米拉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        "虽然这么说有点对不起他的对手。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3803")

    label("loc_3770")


    #C0211
    ChrTalk(
        0xA,
        (
            "……刚才我去特别室\x01",
            "打探了一下……\x01",
            "实在是让人有些担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        (
            "冈兹先生的对手\x01",
            "好像在不停输牌。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xA,
        (
            "玩上五局，大概也只能\x01",
            "勉强战平一次吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3803")

    Jump("loc_4083")

    label("loc_3808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_3915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3870")

    #C0214
    ChrTalk(
        0xA,
        (
            "原本实力平平，连三张一对的牌型都很少能\x01",
            "凑出的人，为何会突然强到如此程度……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3910")

    label("loc_3870")


    #C0215
    ChrTalk(
        0xA,
        (
            "冈兹先生每当玩起扑克类游戏的时候，\x01",
            "抽牌的手气就会变得相当好。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xA,
        (
            "他一口咬定自己\x01",
            "绝对没有耍诈……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xA,
        (
            "但是我怎么都想不明白，\x01",
            "他的运气怎么能那么好呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3910")

    Jump("loc_4083")

    label("loc_3915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_399B")

    #C0218
    ChrTalk(
        0xA,
        "……冈兹先生？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        (
            "嗯，就是那位每到周末\x01",
            "就会到这里来玩的客人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        (
            "如果想知道更加详细的情况，\x01",
            "就去问问老板吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4083")

    label("loc_399B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A03")

    #C0221
    ChrTalk(
        0xA,
        (
            "哎呀呀，难道我的技巧\x01",
            "也下降了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        "……失礼了，只是一点私事而已。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A49")

    label("loc_3A03")


    #C0223
    ChrTalk(
        0xA,
        (
            "好久都没有输得这么\x01",
            "彻底了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xA,
        (
            "大概是我的技巧\x01",
            "有所下降吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A49")

    Jump("loc_4083")

    label("loc_3A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3ACF")

    #C0225
    ChrTalk(
        0xA,
        (
            "在今年的纪念庆典期间，\x01",
            "『巴鲁卡』的营业额\x01",
            "也创造了历史新高。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xA,
        (
            "所有的客人都玩得很尽兴，\x01",
            "真是令人欣喜万分。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4083")

    label("loc_3ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B4B")

    #C0227
    ChrTalk(
        0xA,
        (
            "彩虹剧团的预演前后，\x01",
            "整个欢乐街都很热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xA,
        (
            "这也是托了大明星\x01",
            "伊莉娅·普拉提耶小姐\x01",
            "的福吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD4")

    label("loc_3B4B")


    #C0229
    ChrTalk(
        0xA,
        (
            "说起来，彩虹剧团的预演\x01",
            "好像也逐渐临近了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xA,
        (
            "听说，来观看预演的人\x01",
            "都是各国的富豪和有权之人……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        "『巴鲁卡』也热闹得很呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3BD4")

    Jump("loc_4083")

    label("loc_3BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3CB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C33")

    #C0232
    ChrTalk(
        0xA,
        "各位也来玩一局吧？\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xA,
        (
            "说不定还可以顺便测一下\x01",
            "今天的运势哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB3")

    label("loc_3C33")


    #C0234
    ChrTalk(
        0xA,
        (
            "都说世事无常，\x01",
            "命运难料……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xA,
        (
            "有时候，总会发生一些\x01",
            "意料之外的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xA,
        (
            "正是因为如此，\x01",
            "人类才会相信所谓的命运吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3CB3")

    Jump("loc_4083")

    label("loc_3CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3D06")

    #C0237
    ChrTalk(
        0xA,
        "哎呀，天色已晚……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xA,
        "『巴鲁卡』也要进入客流高峰时间啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4083")

    label("loc_3D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3E14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D7C")

    #C0239
    ChrTalk(
        0xA,
        (
            "ＶＩＰ室今天\x01",
            "也已经被预约了。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xA,
        (
            "太阳一下山，就又会有\x01",
            "很多有权有势的大人物\x01",
            "光临本店了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0F")

    label("loc_3D7C")


    #C0241
    ChrTalk(
        0xA,
        (
            "特别室今天\x01",
            "也已经被预约了。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xA,
        (
            "果然是因为快要召开\x01",
            "自治州议会了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        (
            "最近这段时间，议员、高官、\x01",
            "经理和那些公司高管们\x01",
            "天天都来这里玩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3E0F")

    Jump("loc_4083")

    label("loc_3E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3E81")

    #C0244
    ChrTalk(
        0xA,
        (
            "呵呵，作弊耍诈之类的手段\x01",
            "在我面前是行不通的。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "输了就是输了，\x01",
            "只有老实承认。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EF0")

    label("loc_3E81")


    #C0246
    ChrTalk(
        0xA,
        (
            "前些天，有位快要输掉的客人\x01",
            "想耍诈翻盘。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xA,
        "呼，这是万万不可的啊。\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "输了就是输了，\x01",
            "只有老实承认。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3EF0")

    Jump("loc_4083")

    label("loc_3EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3FEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3F4C")

    #C0249
    ChrTalk(
        0xA,
        (
            "本店有ＶＩＰ专用的\x01",
            "特别室。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "但普通客人\x01",
            "是谢绝入内的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE6")

    label("loc_3F4C")


    #C0251
    ChrTalk(
        0xA,
        (
            "本店有ＶＩＰ专用的\x01",
            "特别室。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "呵呵，说是ＶＩＰ，\x01",
            "其实就是指大贵族或议员等大人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xA,
        (
            "毫无疑问，自然要为他们准备\x01",
            "与他们的地位相称的高档房间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3FE6")

    Jump("loc_4083")

    label("loc_3FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4052")

    #C0254
    ChrTalk(
        0xA,
        (
            "雷特罗莎小姐是这里的常客，\x01",
            "每周都会特意从共和国过来玩一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        "呵呵，她很厉害呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4083")

    label("loc_4052")


    #C0256
    ChrTalk(
        0xA,
        "这里是扑克台。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xA,
        (
            "玩一局二十一点\x01",
            "如何呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4083")

    Jump("loc_3444")

    label("loc_4088")

    TalkEnd(0xA)
    Return()

    # Function_10_3437 end

    def Function_11_408C(): pass

    label("Function_11_408C")

    Call(0, 12)
    Return()

    # Function_11_408C end

    def Function_12_4090(): pass

    label("Function_12_4090")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_409D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CB7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",        # 0
            "玩轮盘\x01",      # 1
            "放弃\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40EF")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_40EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413F")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_413F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4153")
    Jump("loc_4CB2")

    label("loc_4153")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CB2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4250")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_41D1")

    #C0258
    ChrTalk(
        0xB,
        (
            "欢迎光临。\x01",
            "欢迎来到『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xB,
        (
            "希望您今天也能\x01",
            "玩得尽兴，满意而归。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_424B")

    label("loc_41D1")


    #C0260
    ChrTalk(
        0xB,
        (
            "自治州议会\x01",
            "似乎结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xB,
        (
            "到了夜晚，\x01",
            "客人可能会变得更多吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xB,
        (
            "呵呵，对『巴鲁卡』来说，\x01",
            "正是最赚钱的时候呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_424B")

    Jump("loc_4CB2")

    label("loc_4250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_433C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_42D0")

    #C0263
    ChrTalk(
        0xB,
        (
            "因为昨天那场漂亮的牌局，\x01",
            "本店似乎被大家评价为\x01",
            "很豪爽的店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xB,
        (
            "呵呵，对本店来说，\x01",
            "这可是件好事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4337")

    label("loc_42D0")


    #C0265
    ChrTalk(
        0xB,
        (
            "哎呀……今天的\x01",
            "客人还真多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "呵呵，也许是因为关于昨天那场\x01",
            "精彩牌局的传闻已经传播开了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4337")

    Jump("loc_4CB2")

    label("loc_433C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_43FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4391")

    #C0267
    ChrTalk(
        0xB,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xB,
        "得重点注意那位客人呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_4391")


    #C0269
    ChrTalk(
        0xB,
        (
            "那位客人……\x01",
            "手法实在是不可思议呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xB,
        (
            "难道说……\x01",
            "他之前一直输个不停，\x01",
            "全都是在故意演戏吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_43F9")

    Jump("loc_4CB2")

    label("loc_43FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_447E")

    #C0271
    ChrTalk(
        0xB,
        (
            "呼，以那位客人的实力来说，\x01",
            "这种做法实在是鲁莽无谋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xB,
        (
            "对他来说，适可而止，早点放弃\x01",
            "才是最明智的选择啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB2")

    label("loc_447E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_44E0")

    #C0273
    ChrTalk(
        0xB,
        (
            "冈兹先生的运气和直觉\x01",
            "都好得异常呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xB,
        (
            "我也是第一次经历\x01",
            "那种连续的惨败啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB2")

    label("loc_44E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_4612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4551")

    #C0275
    ChrTalk(
        0xB,
        (
            "冈兹先生的确是\x01",
            "本店的常客。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xB,
        (
            "……如果您想了解他的详细情况，\x01",
            "最好直接向老板询问。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_460D")

    label("loc_4551")


    #C0277
    ChrTalk(
        0xB,
        "哎呀，您是问冈兹先生吗？\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xB,
        (
            "没错，他的确\x01",
            "是本店的常客。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "以前一直都是个十玩九输，\x01",
            "只在周末才会光临的普通客人而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xB,
        (
            "……如果您想了解他的详细情况，\x01",
            "请直接向老板询问吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_460D")

    Jump("loc_4CB2")

    label("loc_4612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_46FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4678")

    #C0281
    ChrTalk(
        0xB,
        "胜负主要还是靠运气。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        (
            "即使是我们这些专业人士，\x01",
            "也都会有失手的时候呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F6")

    label("loc_4678")


    #C0283
    ChrTalk(
        0xB,
        (
            "呼，就是在跟那位客人玩的时候，\x01",
            "不慎失手的……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "……失礼了，\x01",
            "其实这也没什么大不了的。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "如何，\x01",
            "想和我玩一局吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_46F6")

    Jump("loc_4CB2")

    label("loc_46FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_47EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4768")

    #C0286
    ChrTalk(
        0xB,
        (
            "呵呵，对我们店来说，\x01",
            "可是一件令人高兴的好事。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xB,
        (
            "今后也请继续光临\x01",
            "『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EA")

    label("loc_4768")


    #C0288
    ChrTalk(
        0xB,
        (
            "呵呵，纪念庆典\x01",
            "真是热闹非凡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xB,
        (
            "有很多游客，直到现在还留在市里，\x01",
            "继续观光游玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "欢乐街恐怕还要\x01",
            "再热闹一阵子吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_47EA")

    Jump("loc_4CB2")

    label("loc_47EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4861")

    #C0291
    ChrTalk(
        0xB,
        (
            "各位也要注意，玩乐应适度，\x01",
            "请不要太过火呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xB,
        (
            "呵呵，否则有可能在不知不觉间\x01",
            "就会债台高筑哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB2")

    label("loc_4861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_48D8")

    #C0293
    ChrTalk(
        0xB,
        (
            "呵呵……\x01",
            "也许你们看不出来，\x01",
            "其实我也是个专业人士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xB,
        (
            "要是以为能轻松战胜我，\x01",
            "那可就大错特错了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB2")

    label("loc_48D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4948")

    #C0295
    ChrTalk(
        0xB,
        "哎呀，都已经这么晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xB,
        (
            "因为一直待在『巴鲁卡』，\x01",
            "所以没法听见傍晚的钟声，\x01",
            "真是头疼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB2")

    label("loc_4948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4993")

    #C0297
    ChrTalk(
        0xB,
        "哎呀，您找老板有事吗？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xB,
        (
            "请到二层的\x01",
            "柜台那边找他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB2")

    label("loc_4993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_49D7")

    #C0299
    ChrTalk(
        0xB,
        (
            "呵呵，今年的纪念庆典\x01",
            "到底会如何举办呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A40")

    label("loc_49D7")


    #C0300
    ChrTalk(
        0xB,
        "好期待下个月的纪念庆典啊。\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "这条欢乐街也会比以往\x01",
            "更加热闹吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        (
            "我们也能趁机大赚\x01",
            "一笔啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4A40")

    Jump("loc_4CB2")

    label("loc_4A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4B52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4AB8")

    #C0303
    ChrTalk(
        0xB,
        (
            "运势强盛，不停取胜的高水平客人\x01",
            "也可以进入ＶＩＰ室。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "客人，您也可以\x01",
            "努力试试看哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B4D")

    label("loc_4AB8")


    #C0305
    ChrTalk(
        0xB,
        (
            "昨晚，ＶＩＰ室\x01",
            "好像非常热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xB,
        (
            "能进入特别室的人，\x01",
            "要么是很有钱的大客户，\x01",
            "要么是技巧高超的常胜客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "客人，您也可以\x01",
            "努力试试看哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4B4D")

    Jump("loc_4CB2")

    label("loc_4B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4BEE")

    #C0308
    ChrTalk(
        0xB,
        (
            "人生就是个甜蜜的陷阱，\x01",
            "经历了种种事情之后，总算是悟出了这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xB,
        (
            "就好像是脚下有个深不见底的大洞。\x01",
            "呵呵，这位客人，您也要小心一点哟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB2")

    label("loc_4BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4C30")

    #C0310
    ChrTalk(
        0xB,
        (
            "玩一局轮盘如何？\x01",
            "今天有可能\x01",
            "会赢到很多米拉哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB2")

    label("loc_4C30")


    #C0311
    ChrTalk(
        0xB,
        (
            "欢迎光临。\x01",
            "欢迎光临『巴鲁卡』。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xB,
        (
            "呵呵，客人，\x01",
            "您的眼神可真令人欣赏。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xB,
        (
            "玩一局轮盘如何？\x01",
            "今天说不定能赢一局大的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4CB2")

    Jump("loc_409D")

    label("loc_4CB7")

    TalkEnd(0xB)
    Return()

    # Function_12_4090 end

    def Function_13_4CBB(): pass

    label("Function_13_4CBB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D4F")
    Jump("loc_4D99")

    label("loc_4D4F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D6F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D99")

    label("loc_4D6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D8F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D99")

    label("loc_4D8F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D99")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4E0F")

    #C0314
    ChrTalk(
        0xC,
        (
            "不知为什么，最近\x01",
            "提不起玩乐的劲头呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        "是不是该回国了呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D68")

    label("loc_4E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4E80")

    #C0316
    ChrTalk(
        0xC,
        (
            "我向雷克特追问了\x01",
            "关于昨天那场牌局的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        "但是被他巧妙地岔开了话题。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xC,
        "真让人不爽……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D68")

    label("loc_4E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_5017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4F01")

    #C0319
    ChrTalk(
        0xC,
        (
            "那个叫雷克特的男人，\x01",
            "实力应该没什么了不起的。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xC,
        (
            "但是那种游刃有余的态度，\x01",
            "实在是让人心里没底呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5012")

    label("loc_4F01")


    #C0321
    ChrTalk(
        0xC,
        (
            "那个叫雷克特的男人，\x01",
            "昨天也来玩了，\x01",
            "他的实力应该没什么了不起的。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xC,
        (
            "因为我让\x01",
            "他输得很惨呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#0005F哎……可是，最后那局又是怎么回事呢？\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        (
            "#0301F的确，用五同点战胜同花顺\x01",
            "这种事可不是随便\x01",
            "就能做到的……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        (
            "……难道真的只是偶然吗。\x01",
            "不知道究竟是怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5012")

    Jump("loc_5D68")

    label("loc_5017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5075")

    #C0326
    ChrTalk(
        0xC,
        (
            "不过，竟敢挑战冈兹，\x01",
            "真是个愚蠢的客人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xC,
        (
            "我都已经再三\x01",
            "忠告过他了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D68")

    label("loc_5075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_5142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_50D5")

    #C0328
    ChrTalk(
        0xC,
        "我也曾和他对阵过一次呢。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xC,
        (
            "但是他根本就不像是\x01",
            "技巧平庸的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_513D")

    label("loc_50D5")


    #C0330
    ChrTalk(
        0xC,
        (
            "听说，那个叫冈兹的男人\x01",
            "以前只是个技巧非常差\x01",
            "的家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xC,
        (
            "这是真的吗，\x01",
            "实在是让人无法想象啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_513D")

    Jump("loc_5D68")

    label("loc_5142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_523E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_51A0")

    #C0332
    ChrTalk(
        0xC,
        (
            "呵呵，我听说\x01",
            "有位客人一直连战连赢呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        "我也产生一点兴趣了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5239")

    label("loc_51A0")


    #C0334
    ChrTalk(
        0xC,
        (
            "都已经好久没来克洛斯贝尔了，\x01",
            "……情况好像变得有趣起来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        (
            "这里的发牌师似乎手气不佳啊，\x01",
            "一直都在输牌。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xC,
        "呵呵，对手究竟是何方神圣呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5239")

    Jump("loc_5D68")

    label("loc_523E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_531E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_52A0")

    #C0337
    ChrTalk(
        0xC,
        "我差不多也该收手了……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xC,
        (
            "已经玩得很尽兴了，\x01",
            "差不多也该回国一次了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5319")

    label("loc_52A0")


    #C0339
    ChrTalk(
        0xC,
        (
            "呼，为了消磨时间，\x01",
            "于是让多雷克老板\x01",
            "来当我的对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xC,
        "老板的确很强呢。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xC,
        "呵呵，已经好久没尝过失败的滋味了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5319")

    Jump("loc_5D68")

    label("loc_531E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5374")

    #C0342
    ChrTalk(
        0xC,
        "那个男人又输给我了。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xC,
        (
            "呵呵……我是不是\x01",
            "下手太狠了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5404")

    label("loc_5374")

    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xC, 0x0)

    #C0344
    ChrTalk(
        0xA,
        (
            "真不愧是雷特罗莎小姐，\x01",
            "手腕还是一如既往地高超啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xA,
        (
            "这杯酒\x01",
            "是我的一点心意。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xC,
        (
            "哎呀，真是太感谢了。\x01",
            "呵呵，真是体贴呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)

    label("loc_5404")

    Jump("loc_5D68")

    label("loc_5409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_558A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_54A1")

    #C0347
    ChrTalk(
        0xC,
        (
            "听说ＩＢＣ的资产总额\x01",
            "是世界首位呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xC,
        (
            "真不愧是天下第一的ＩＢＣ……\x01",
            "要是单以资产来衡量的话，\x01",
            "是绝不会输给帝国或共和国的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5585")

    label("loc_54A1")


    #C0349
    ChrTalk(
        0xC,
        (
            "听说ＩＢＣ的资产总额\x01",
            "居于世界首位呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xC,
        (
            "毕竟克洛斯贝尔是聚集财富的地方，\x01",
            "而它也是历史悠久的国际银行。\x01",
            "要说起来，资产庞大也是理所当然的……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xC,
        (
            "呵呵，竟然比那个莱恩福尔特公司\x01",
            "和乌尔努公司还要有钱，\x01",
            "还真是让人惊讶啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5585")

    Jump("loc_5D68")

    label("loc_558A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_55C5")
    SetChrSubChip(0xC, 0x2)

    #C0352
    ChrTalk(
        0xC,
        (
            "哎呀呀……\x01",
            "只是嘴上功夫厉害呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_55C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_56C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5638")

    #C0353
    ChrTalk(
        0xC,
        (
            "听说克洛斯贝尔警备队的司令\x01",
            "每天都是游手好闲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xC,
        (
            "呵呵，他的部下们可真是\x01",
            "太可怜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56C2")

    label("loc_5638")


    #C0355
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔警备队\x01",
            "是一支精锐部队吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xC,
        (
            "但是，听说那里的司令\x01",
            "是个游手好闲的无能家伙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xC,
        (
            "呵呵……他的部下们\x01",
            "肯定会很辛苦吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_56C2")

    Jump("loc_5D68")

    label("loc_56C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5722")

    #C0358
    ChrTalk(
        0xC,
        "父亲可真是的，办事也太利落了。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xC,
        "呼……这样反倒有点没趣啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5892")

    label("loc_5722")


    #C0360
    ChrTalk(
        0xC,
        (
            "我这个月是为了买彩虹剧团\x01",
            "的门票才特意过来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#0304F呼，这个时期，\x01",
            "是有很多这样的游客啊。\x02\x03",

            "#0300F算了，就算买不到，\x01",
            "也不要灰心啊。\x02\x03",

            "要是不介意等到下下个月的话，\x01",
            "我可以陪你一起……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xC,
        (
            "父亲托人帮忙，\x01",
            "已经轻松帮我买到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xC,
        "哼，真是没意思啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x104,
        (
            "#0306F（打击）……\x01",
            "跟预想中的不太一样啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x103,
        "#0200F兰迪前辈，不要在意。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5892")

    Jump("loc_5D68")

    label("loc_5897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_597D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_58F7")

    #C0366
    ChrTalk(
        0xC,
        (
            "待在克洛斯贝尔，\x01",
            "身心都很容易浮躁。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xC,
        "呵呵，这也不是什么坏事啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5978")

    label("loc_58F7")


    #C0368
    ChrTalk(
        0xC,
        (
            "待在克洛斯贝尔，\x01",
            "身心都很容易浮躁。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xC,
        (
            "听着这些甜蜜的喧嚣声，\x01",
            "连大脑都变得有些麻木了。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xC,
        "呵呵，这也不是什么坏事啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5978")

    Jump("loc_5D68")

    label("loc_597D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5A7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_59F8")

    #C0371
    ChrTalk(
        0xC,
        (
            "听说多雷克老板\x01",
            "是个特别有名的专业人士呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xC,
        (
            "而且好像还跟黑道有些渊源。\x01",
            "嗯，对他有些兴趣呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A76")

    label("loc_59F8")


    #C0373
    ChrTalk(
        0xC,
        (
            "正好在扑克台也\x01",
            "有点玩腻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xC,
        (
            "不然就直接向多雷克老板\x01",
            "发起挑战吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xC,
        (
            "听说那个人年轻时，\x01",
            "是个很有名的专业人士呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5A76")

    Jump("loc_5D68")

    label("loc_5A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 1)), scpexpr(EXPR_END)), "loc_5B3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5AB1")

    #C0376
    ChrTalk(
        0xC,
        (
            "呵呵……\x01",
            "我最喜欢强者了⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B37")

    label("loc_5AB1")


    #C0377
    ChrTalk(
        0xC,
        (
            "呵呵……\x01",
            "我最喜欢强者了⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        (
            "#0309F（噢噢！\x01",
            "  『巴鲁卡』的感觉就是好啊！）\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#0006F（那个，兰迪，\x01",
            "  别兴奋得过头了……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5B37")

    Jump("loc_5D68")

    label("loc_5B3C")

    SetChrSubChip(0xC, 0x0)
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x104, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5BD4")
    Jump("loc_5C1E")

    label("loc_5BD4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BF4")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C1E")

    label("loc_5BF4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C14")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C1E")

    label("loc_5C14")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C1E")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0380
    ChrTalk(
        0xC,
        "……哎呀，你就是兰迪？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xC,
        (
            "呵呵，我听说过你的传闻哦。\x01",
            "听说你手腕很高超啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        (
            "#0309F嘿！\x01",
            "你这样的美人竟然主动\x01",
            "和我搭话，真是太荣幸了。\x02\x03",

            "#0300F怎么样，来和我玩一局，\x01",
            "就以人生为赌注如何！？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x102,
        (
            "#0111F……那个，这种事情\x01",
            "就不能留到休息日再做吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#0006F至少也要在\x01",
            "今天节制一点吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 1)

    label("loc_5D68")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_4CBB end

    def Function_14_5D70(): pass

    label("Function_14_5D70")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E04")
    Jump("loc_5E4E")

    label("loc_5E04")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E24")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E4E")

    label("loc_5E24")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E44")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E4E")

    label("loc_5E44")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E4E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5ED8")

    #C0385
    ChrTalk(
        0xD,
        "转换心情是件十分重要的事情。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xD,
        "这也是能长时间在这种店开心玩乐的秘诀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F81")

    label("loc_5ED8")


    #C0387
    ChrTalk(
        0xD,
        (
            "呜呜……今天\x01",
            "输得好惨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xD,
        (
            "唉，这也是没有办法的事啊。\x01",
            "这种时候，也只能给老伴\x01",
            "买点礼物，然后乖乖回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xD,
        (
            "在这种店玩的时候，转换心情\x01",
            "是一件很重要的事情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5F81")

    Jump("loc_6E14")

    label("loc_5F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5FFE")

    #C0390
    ChrTalk(
        0xD,
        "呃，那个叫雷克特的男人……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xD,
        (
            "竟然在我边上赢了三万\x01",
            "代币啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xD,
        (
            "真是让人火大……\x01",
            "不想输给他呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E14")

    label("loc_5FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_6062")

    #C0393
    ChrTalk(
        0xD,
        (
            "下面好像挺吵的……\x01",
            "发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xD,
        (
            "最近怎么总能听到\x01",
            "这种让人不安的事情呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E14")

    label("loc_6062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_610E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_60AC")

    #C0395
    ChrTalk(
        0xD,
        (
            "冈兹最近的\x01",
            "运势很旺盛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xD,
        "跟谁玩都能赢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6109")

    label("loc_60AC")


    #C0397
    ChrTalk(
        0xD,
        (
            "冈兹好像正在特别室里\x01",
            "玩大牌局呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xD,
        (
            "那个游客去挑战冈兹了吗？\x01",
            "……实在是太乱来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6109")

    Jump("loc_6E14")

    label("loc_610E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 5)), scpexpr(EXPR_END)), "loc_6176")

    #C0399
    ChrTalk(
        0xD,
        (
            "嗯嗯，正玩得高兴呢，\x01",
            "太阳就已经下山了……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xD,
        (
            "真讨厌，不想回去啊。\x01",
            "现在手气正好呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E14")

    label("loc_6176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_628B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_61EE")

    #C0401
    ChrTalk(
        0xD,
        (
            "听说啊，那些黑手党组织之间\x01",
            "已经互相打起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xD,
        (
            "我这老头子也要小心，\x01",
            "可别被卷入\x01",
            "其中啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6286")

    label("loc_61EE")


    #C0403
    ChrTalk(
        0xD,
        (
            "听说，鲁巴彻的那帮家伙\x01",
            "最近好像在鬼鬼祟祟地搞些什么阴谋。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xD,
        (
            "我也得\x01",
            "多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xD,
        (
            "要是跟那些家伙搅在一起的话，\x01",
            "就算是警官也不能轻易脱身。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6286")

    Jump("loc_6E14")

    label("loc_628B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6425")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_62FA")

    #C0406
    ChrTalk(
        0xD,
        (
            "我家老伴总是在我耳边\x01",
            "啰啰嗦嗦……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xD,
        (
            "不过她这个岁数还能\x01",
            "这么有精神，倒是件好事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6420")

    label("loc_62FA")


    #C0408
    ChrTalk(
        0xD,
        (
            "我家老伴总是不让我\x01",
            "来『巴鲁卡』玩，真是烦死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xD,
        (
            "今天早上也是，\x01",
            "和她吵了半天以后，\x01",
            "才能跑出来玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xD,
        (
            "呼，一大早\x01",
            "就出了一身臭汗。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_641D")

    #C0411
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，老爷爷看起来\x01",
            "还是老样子啊……\x02\x03",

            "您偶尔也该讨好一下老伴吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xD,
        (
            "呵呵，正如兰迪你所说，\x01",
            "我今天准备拿个\x01",
            "奖品回去送她呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_641D")

    SetScenarioFlags(0x0, 5)

    label("loc_6420")

    Jump("loc_6E14")

    label("loc_6425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_658F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_64A4")

    #C0413
    ChrTalk(
        0xD,
        (
            "我们老两口能过上这种生活，\x01",
            "也都是托了地下空间设施的福。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xD,
        (
            "原来就听说市内的管理\x01",
            "存在着很多问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_658A")

    label("loc_64A4")


    #C0415
    ChrTalk(
        0xD,
        (
            "克洛斯贝尔的地下空间\x01",
            "是在二十年前左右开始计划建设的。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xD,
        (
            "随着都市人口的增加，\x01",
            "基础设施会越来越不够用，\x01",
            "它正是为了满足这一需求而建造的。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xD,
        (
            "直到现在，也仍在不停的扩建着。\x01",
            "好像已经几乎快要占据\x01",
            "克洛斯贝尔整个地下范围了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_658A")

    Jump("loc_6E14")

    label("loc_658F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_66E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_660F")

    #C0418
    ChrTalk(
        0xD,
        (
            "那个老太婆……\x01",
            "最近真是越来越纠缠不休了。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xD,
        (
            "但就凭这种程度，\x01",
            "是不可能让我放弃来这里玩的。\x01",
            "呵呵！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66DE")

    label("loc_660F")


    #C0420
    ChrTalk(
        0xD,
        (
            "哎呀呀，瞒过老伴的眼睛\x01",
            "偷偷溜过来，可不是那么轻松的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xD,
        (
            "今天本想从后门\x01",
            "偷偷跑出去……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xD,
        (
            "没想到，刚跑到大道上，\x01",
            "就刚好和老伴正面撞上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xD,
        (
            "呼，然后我马上慌慌张张地逃跑，\x01",
            "差点就被她抓到了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_66DE")

    Jump("loc_6E14")

    label("loc_66E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_67B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6744")

    #C0424
    ChrTalk(
        0xD,
        (
            "我年轻的时候，\x01",
            "经常在夜里出去玩，\x01",
            "但现在都这个岁数了，实在是不行了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67AF")

    label("loc_6744")


    #C0425
    ChrTalk(
        0xD,
        (
            "哎呀，要是再不赶快回去的话，\x01",
            "就又要被老太婆教训了。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xD,
        (
            "到了现在这个岁数，\x01",
            "晚上出来玩真是太累了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_67AF")

    Jump("loc_6E14")

    label("loc_67B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_68F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6846")

    #C0427
    ChrTalk(
        0xD,
        (
            "欢乐街过去就是这么喧闹，\x01",
            "一点也没有变过。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xD,
        (
            "……还有啊，跟过去一样，\x01",
            "治安也一直有些差。\x01",
            "刚到此地的人可得多注意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68F4")

    label("loc_6846")


    #C0429
    ChrTalk(
        0xD,
        (
            "无论克洛斯贝尔再怎么变化，\x01",
            "欢乐街也绝对不会消失吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xD,
        (
            "酒吧、『巴鲁卡』、众多游客、\x01",
            "成群的漂亮姑娘⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xD,
        (
            "就算是外表有所变化，\x01",
            "实质上还是跟过去一样，一点也没变呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_68F4")

    Jump("loc_6E14")

    label("loc_68F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6A06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6941")

    #C0432
    ChrTalk(
        0xD,
        (
            "昨天输得真是好惨啊。\x01",
            "必须要想办法赢回来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A01")

    label("loc_6941")


    #C0433
    ChrTalk(
        0xD,
        "噢噢，今天的状态不错啊。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xD,
        (
            "好，得努力把昨天输掉的米拉\x01",
            "都给赢回来！\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x104,
        (
            "#0300F好久没来，\x01",
            "您还是老样子啊，老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xD,
        "呵呵，这不是兰迪嘛。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xD,
        (
            "那是当然啦。\x01",
            "老虎机是我每天必玩的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6A01")

    Jump("loc_6E14")

    label("loc_6A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6A7D")

    #C0438
    ChrTalk(
        0xD,
        (
            "这可是我这个老头子\x01",
            "最大的生存意义啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xD,
        (
            "可恶可恶，谁也别想把这家店\x01",
            "从我的生活中给夺走！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B02")

    label("loc_6A7D")


    #C0440
    ChrTalk(
        0xD,
        (
            "那个可恶的老太婆，\x01",
            "今天早上躲在正门外埋伏我。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xD,
        "还竖起眉毛在那里大吼。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xD,
        (
            "差点儿就被她抓回去了呢。\x01",
            "呼，真是千钧一发啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6B02")

    Jump("loc_6E14")

    label("loc_6B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6BA7")

    #C0443
    ChrTalk(
        0xD,
        (
            "我都在欢乐街上玩了五十年了……\x01",
            "可是从这里刚刚建成开始\x01",
            "就一直来玩的超级老顾客了。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xD,
        (
            "兰迪啊，像你这种毛头小子，\x01",
            "还只是菜鸟级别呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C80")

    label("loc_6BA7")


    #C0445
    ChrTalk(
        0xD,
        (
            "我在这条欢乐街上\x01",
            "已经玩了足足五十年了。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xD,
        (
            "兰迪啊，像你这种毛头小子，\x01",
            "还只是菜鸟级别呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x104,
        (
            "#0300F嗯，的确……\x01",
            "我只不过刚在这里\x01",
            "玩了一年半左右吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x103,
        (
            "#0200F……兰迪前辈，\x01",
            "不用进行这么低水准\x01",
            "的比较吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6C80")

    Jump("loc_6E14")

    label("loc_6C85")

    SetChrSubChip(0xD, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6CD8")

    #C0449
    ChrTalk(
        0xD,
        (
            "现在手气正好呢，\x01",
            "别跟我说话！\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xD,
        "……噢噢，有了有了～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E14")

    label("loc_6CD8")


    #C0451
    ChrTalk(
        0x104,
        (
            "#0300F哟，利凯爷爷。\x01",
            "今天的手气如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xD,
        "嗯？这个声音……是兰迪吗？\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xD,
        (
            "现在手气正好呢，\x01",
            "别跟我说话！\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，您还是老样子，\x01",
            "状态似乎很好呢～\x02\x03",

            "不过，要是玩得太过头，\x01",
            "就又该被老伴\x01",
            "骂了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xD,
        (
            "嗯嗯嗯，说得也是！\x01",
            "噢噢噢噢噢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#0000F（兰迪在『巴鲁卡』的朋友，\x01",
            "  是不是都是这样的人啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6E14")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_5D70 end

    def Function_15_6E1C(): pass

    label("Function_15_6E1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6EB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6E6F")

    #C0457
    ChrTalk(
        0xE,
        (
            "可恶，坐在牌桌那里的女人……\x01",
            "简直就是个魔女啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB2")

    label("loc_6E6F")


    #C0458
    ChrTalk(
        0xE,
        (
            "那个……\x01",
            "能借我点米拉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xE,
        (
            "我连回家的车票钱\x01",
            "都输光了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6EB2")

    Jump("loc_6FCE")

    label("loc_6EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6F04")

    #C0460
    ChrTalk(
        0xE,
        "呜呜，可恶……\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xE,
        (
            "下次……下次一定要\x01",
            "让那个女人输给我！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FCE")

    label("loc_6F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6F53")

    #C0462
    ChrTalk(
        0xE,
        (
            "我最讨厌那种类型\x01",
            "的女人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xE,
        "哼，以后一定要赢哭她才行！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FCE")

    label("loc_6F53")


    #C0464
    ChrTalk(
        0xE,
        "啊啊，可恶，又输了。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xE,
        (
            "坐在柜台边上的那个女人，\x01",
            "真是个相当厉害的老手啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xE,
        (
            "哼，下次……\x01",
            "下次一定要战胜她！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6FCE")

    TalkEnd(0xFE)
    Return()

    # Function_15_6E1C end

    def Function_16_6FD2(): pass

    label("Function_16_6FD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_70A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7032")

    #C0467
    ChrTalk(
        0xF,
        "七战六败……不可能啊……\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xF,
        "啊啊，我身为牌技师的自信就这么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_70A4")

    label("loc_7032")


    #C0469
    ChrTalk(
        0xF,
        (
            "不、不好……\x01",
            "我所有的一切都输给\x01",
            "牌桌边上的那个女人了……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xF,
        (
            "我得先回一趟国，\x01",
            "重新修炼以后再回来挑战……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_70A4")

    Jump("loc_7299")

    label("loc_70A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7188")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7120")

    #C0471
    ChrTalk(
        0xF,
        (
            "我可是环游世界各国的老手，\x01",
            "说出的话绝对不会有错。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xF,
        (
            "克洛斯贝尔的牌技师\x01",
            "是相当强的……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7183")

    label("loc_7120")


    #C0473
    ChrTalk(
        0xF,
        (
            "可、可恶……这次试着玩了\x01",
            "一局轮盘，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xF,
        (
            "好强啊……！\x01",
            "这家店里的家伙们真是太强了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7183")

    Jump("loc_7299")

    label("loc_7188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7220")

    #C0475
    ChrTalk(
        0xF,
        (
            "坐在牌桌边上的那个女人\x01",
            "真是太强了……\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xF,
        (
            "但是，我也是个职业牌技师。\x01",
            "就算对手是女人，我也绝不会手下留情。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xF,
        "下次一定要全力以赴。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7299")

    label("loc_7220")


    #C0478
    ChrTalk(
        0xF,
        (
            "我环游世界各国，\x01",
            "进行牌技修行。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xF,
        (
            "哼……今年就在克洛斯贝尔\x01",
            "一决胜负吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xF,
        (
            "为了成为一名\x01",
            "更加强大的牌技师……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7299")

    TalkEnd(0xFE)
    Return()

    # Function_16_6FD2 end

    def Function_17_729D(): pass

    label("Function_17_729D")

    TalkBegin(0xFE)

    #C0481
    ChrTalk(
        0x10,
        "等、等等，那是……\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x10,
        (
            "同花顺！？\x01",
            "不可能吧！！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_729D end

    def Function_18_72D9(): pass

    label("Function_18_72D9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_736D")
    Jump("loc_73B7")

    label("loc_736D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_738D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73B7")

    label("loc_738D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73B7")

    label("loc_73AD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73B7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 3)), scpexpr(EXPR_END)), "loc_7485")

    #C0483
    ChrTalk(
        0x11,
        (
            "#3504F好了，任务已经完成啦。\x01",
            "不过就这么回去可有点无聊啊。\x02\x03",

            "#3510F……好，从现在开始，\x01",
            "就让我自由活动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        (
            "#0013F（任务……\x01",
            "  究竟是指什么……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_783A")

    label("loc_7485")


    #C0485
    ChrTalk(
        0x11,
        (
            "#3505F哟，辛苦啦～\x01",
            "那个男人怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        (
            "#0003F这个嘛……很抱歉，\x01",
            "实在是难以正面回答。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x102,
        (
            "#0106F总之，\x01",
            "现在已经让他平静下来了……\x02\x03",

            "#0100F以后有机会的话，应该可以\x01",
            "让他向你道个歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x11,
        (
            "#3509F哈哈哈，哪有那种必要。\x02\x03",

            "#3500F我又不是为了看他道歉\x01",
            "才击败他的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0489
    ChrTalk(
        0x101,
        (
            "#0011F难道说……\x01",
            "你最后的那一步是事先就计划好的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        (
            "#0303F不不，不可能的。\x01",
            "无论怎么看，也都只是个幸运的偶然啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x11,
        (
            "#3509F没错，偶然啦偶然啦。\x01",
            "一定是因为我每日行善才有那么好的运气啊～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0492
    ChrTalk(
        0x101,
        (
            "#0008F（难道说……\x01",
            "　那一步真的在他的计划之中吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x104,
        (
            "#0301F（不知道呢，\x01",
            "  连我也开始有点没自信了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x103,
        (
            "#0211F（……如果是这个人的话，\x01",
            "  也不是完全没有可能吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x11,
        (
            "#3504F总之……其实我只不过是\x01",
            "推波助澜了一下而已。\x02\x03",

            "那家伙迟早都会\x01",
            "变成那样的。\x01",
            "虽然比我预想中早了一点。\x02\x03",

            "#3502F哼哼……因此呢，\x01",
            "后面的麻烦事就全部拜托你们啦～\x01",
            "你们可要看好他哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x101,
        "#0001F嗯，那是当然的……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 3)

    label("loc_783A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_72D9 end

    def Function_19_7842(): pass

    label("Function_19_7842")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1200, 500, 10850, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 0, 0, -6250, 0)
    SetChrPos(0x102, -1000, 0, -5500, 0)
    SetChrPos(0x103, 1000, 0, -4500, 0)
    SetChrPos(0x104, 0, 0, -3900, 0)
    OP_68(-1360, 500, 6970, 3000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(500)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_68(6530, 5500, 10270, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20800, 0)
    OP_68(-1050, 5500, 21040, 5000)
    MoveCamera(41, 24, 0, 5000)
    SetCameraDistance(20800, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1500, -5000, 0)
    MoveCamera(49, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xD, 0x8000)

    #C0497
    ChrTalk(
        0x104,
        "#0309F好啦，今天也要好好玩一玩！\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x103,
        (
            "#11P#0200F兰迪前辈一有点什么事，\x01",
            "就想借机到『巴鲁卡』来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x102,
        (
            "#6P#0106F本来应该要去巡视的，\x01",
            "结果就这么理直气壮地开始玩了……\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        (
            "#12P#0003F来这里也有收集情报的因素在内，\x01",
            "并不能说他完全是在玩……\x02\x03",

            "#0000F……兰迪，要节制一点啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0501
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※如果想利用『巴鲁卡』里的设施进行游玩，\x01",
            "  就请与接待人员对话，\x01",
            "  将手中的米拉兑换成代币。\x02\x03",

            "※代币无法兑换回米拉，\x01",
            "  但收集到一定数量，就可以兑换各种精美的奖品。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToBright(300, 0)
    SetChrPos(0x0, 0, 0, -5000, 0)
    SetScenarioFlags(0x6D, 5)
    EventEnd(0x5)
    Return()

    # Function_19_7842 end

    def Function_20_7B82(): pass

    label("Function_20_7B82")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "玩老虎机\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C08")
    FadeToDark(300, 0, -1)
    OP_0D()
    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_7C08")

    TalkEnd(0xFF)
    Return()

    # Function_20_7B82 end

    def Function_21_7C0C(): pass

    label("Function_21_7C0C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, -500, 14500, 0)
    MoveCamera(30, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -100, 0, -5300, 0)
    SetChrPos(0x102, 1100, 0, -4900, 330)
    SetChrPos(0x103, -1100, 0, -4900, 30)
    SetChrPos(0x104, 0, 0, -3700, 0)
    OP_68(0, 500, 7500, 6000)
    SetCameraDistance(25000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1000, -2700, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)

    def lambda_7CE8():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF574, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7CE8)
    WaitChrThread(0x104, 1)
    OP_0D()

    #C0502
    ChrTalk(
        0x104,
        "#0302F#11P『巴鲁卡』也要进入晚场啦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0503
    ChrTalk(
        0x104,
        (
            "#0309F#5P那我就随便玩玩，\x01",
            "顺便打探一下那个矿工的事情吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x101,
        "#12P#0006F不，这样可不行。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x103,
        (
            "#12P#0211F这又不是秘密调查，\x01",
            "我认为完全没有玩的必要……\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x102,
        (
            "#0103F#12P总之，我们先去问问\x01",
            "服务员和客人们吧。\x02\x03",

            "#0100F也许能打探到一些有关\x01",
            "冈兹先生的消息呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x104,
        "#0306F#5P好啦好啦，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, -4700, 0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xC1, 5)
    OP_C7(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_21_7C0C end

    def Function_22_7E7A(): pass

    label("Function_22_7E7A")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(-900, 5000, 20000, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -1100, 4000, 17400, 0)
    SetChrPos(0x102, 200, 4000, 17800, 0)
    SetChrPos(0x103, -2000, 4000, 17800, 0)
    SetChrPos(0x104, -900, 4000, 18700, 0)
    SetChrPos(0x8, -900, 4000, 21300, 180)
    OP_0D()

    #C0508
    ChrTalk(
        0x8,
        "#5P哎呀，各位好。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x8,
        (
            "#5P是跟兰迪一起\x01",
            "来玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        "#12P#0001F不，其实……\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x104,
        (
            "#0300F#11P有些事情，\x01",
            "想向老板您打听一下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0512
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向对方询问了有关\x01",
            "失踪矿工冈兹的事情。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0513
    ChrTalk(
        0x8,
        (
            "#5P失踪？\x01",
            "哈哈，怎么可能呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x8,
        (
            "#5P他今天还跑到我们这里玩，\x01",
            "捞了好大一笔呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0515
    ChrTalk(
        0x101,
        "#12P#0005F这、这是真的吗？\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        "#0105F#12P而且还捞了好大一笔……\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x104,
        (
            "#0301F#11P喂喂，老板，\x01",
            "你该不会是认错人了吧？\x02\x03",

            "我们在找的人是\x01",
            "玛因兹的一个矿工，\x01",
            "那可是个技巧和直觉都很平庸的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x8,
        "#5P嗯，没错，就是他。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x8,
        (
            "#5P那是两周前的事情了……\x01",
            "他之前好长时间没来。\x01",
            "再次出现时，突然就比别人强了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x8,
        (
            "#5P拜他所赐，我们这里的员工不停地输，\x01",
            "大概让他赢走了五十万米拉吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0521
    ChrTalk(
        0x101,
        "#12P#0011F五、五十万米拉！？\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x103,
        "#12P#0205F好大一笔啊……\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x104,
        (
            "#0306F#11P喂喂，真的假的啊……\x02\x03",

            "#0301F该不会是做了什么手脚，\x01",
            "比如耍诈之类的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x8,
        (
            "#5P我们毕竟是职业人士，\x01",
            "如果对方作弊的话，马上就能察觉到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x8,
        (
            "#5P总之，他不仅直觉变得异常敏锐，\x01",
            "连运气都好得不可思议。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x8,
        (
            "#5P我们也非常想知道，\x01",
            "他到底是怎么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x104,
        "#0303F#11P嗯……\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x102,
        (
            "#0106F#12P跟镇长先生说的\x01",
            "好像完全不一样呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        (
            "#12P#0003F那个，老板。\x02\x03",

            "#0001F冈兹先生似乎一直\x01",
            "没有回到矿山镇……\x02\x03",

            "您知道他目前住在哪里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x8,
        "#5P嗯，我知道啊……\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x8,
        (
            "#5P他每天都住在\x01",
            "附近的一座酒店里。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x8,
        (
            "#5P而且好像还是位于最顶层的\x01",
            "豪华套间呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0533
    ChrTalk(
        0x101,
        (
            "#12P#0005F是那间高级酒店中的\x01",
            "豪华套间吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x104,
        (
            "#0306F#11P喂喂……\x01",
            "那家伙到底多有钱啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0535
    ChrTalk(
        0x103,
        (
            "#6P#0202F不过，倒是很意外，\x01",
            "竟然这么快就探听到了消息。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0536
    ChrTalk(
        0x102,
        (
            "#0100F#11P是啊……\x01",
            "我们赶快去见见他吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x8, -900, 4000, 21300, 180)
    SetChrPos(0x0, -900, 4000, 17500, 180)
    OP_4C(0x8, 0xFF)
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    SetScenarioFlags(0xC1, 6)
    OP_29(0x4A, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_22_7E7A end

    def Function_23_865D(): pass

    label("Function_23_865D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    LoadChrToIndex("chr/ch07402.itc", 0x1F)
    LoadChrToIndex("chr/ch37600.itc", 0x20)
    LoadChrToIndex("chr/ch37602.itc", 0x21)
    LoadChrToIndex("chr/ch23200.itc", 0x22)
    OP_68(0, 0, 3000, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -700, 0, -5800, 0)
    SetChrPos(0x102, 700, 0, -5800, 0)
    SetChrPos(0x103, -700, 0, -6900, 0)
    SetChrPos(0x104, 700, 0, -6900, 0)
    SetChrPos(0x13D, 0, 0, -8000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 102200, 100, 5000, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 97800, 100, 5000, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 0, -1000, 3000, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 101300, 0, 1600, 315)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearMapFlags(0x10000000)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis085.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis086.itp")
    SetCameraDistance(26500, 3000)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_8865():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8865)

    def lambda_887F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_887F)
    Sleep(50)

    def lambda_8893():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8893)

    def lambda_88AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_88AD)
    Sleep(50)

    def lambda_88C1():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_88C1)

    def lambda_88DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_88DB)
    Sleep(50)

    def lambda_88EF():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_88EF)

    def lambda_8909():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8909)
    Sleep(50)

    def lambda_891D():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_891D)

    def lambda_8937():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13D, 2, lambda_8937)
    Sleep(1300)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x12, 0xB4, 0x1F4)

    #C0537
    ChrTalk(
        0x12,
        "哦哦，你们来了吗！\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x12,
        (
            "真是太好了！\x01",
            "他们随时都有可能发生冲突……！\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        (
            "#0013F您是说冈兹先生\x01",
            "和他的对手吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x12,
        "是啊……\x02",
    )

    CloseMessageWindow()

    def lambda_89EF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_89EF)
    OP_68(-3000, 0, 20200, 2500)
    MoveCamera(33, 15, 0, 2500)
    OP_6F(0x41)

    #C0541
    ChrTalk(
        0x12,
        (
            "他们正在最里面的那间特别室里\x01",
            "一对一对决呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x12,
        (
            "从目前的气氛来看，要是再不快点，\x01",
            "冈兹恐怕马上就要使用暴力了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x101,
        "#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#0105F不是冈兹先生\x01",
            "惹怒其他客人吗……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x9C4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_68(100200, 1000, 2000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 99900, 0, -7000, 0)
    SetChrPos(0x102, 99900, 0, -7000, 0)
    SetChrPos(0x103, 99900, 0, -7000, 0)
    SetChrPos(0x104, 99900, 0, -7000, 0)
    SetChrPos(0x13D, 99900, 0, -7000, 0)
    SetChrPos(0x12, 99900, 0, -7000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(100570, 1000, 5280, 4000)
    Sleep(10)
    PlayBGM("ed7518", 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0545
    ChrTalk(
        0x13,
        "#5P好，这招如何！\x02",
    )

    CloseMessageWindow()
    Sound(90, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetChrName("")

    #A0546
    AnonymousTalk(
        0x13,
        (
            "方片的９、１０、Ｊ、Ｑ、Ｋ\x01",
            "的同花大顺！\x02\x03",

            "这下你也就无计可施了吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0547
    AnonymousTalk(
        0x14,
        (
            "#3507F哇啊，真的假的！\x02\x03",

            "#3506F真没想到，在最后的决胜局中，\x01",
            "居然能亮出这么一副好牌啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0548
    ChrTalk(
        0x13,
        (
            "#5P哈！\x01",
            "这就是本大爷的实力啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x13,
        (
            "#5P……本来我早就能赢了，但你小子死缠烂打，\x01",
            "硬是拖平了好几局。\x01",
            "不过这局总算是能分出胜负了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0550
    ChrTalk(
        0x13,
        "#5P#4S赶紧把牌翻出来，然后夹着尾巴滚吧！\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0551
    ChrTalk(
        0x14,
        (
            "#11P#3505F嗯，你在说什么啊？\x02\x03",

            "#3510F我可连一次也没说过\x01",
            "自己已经输了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0552
    ChrTalk(
        0x13,
        "#5P别、别再虚张声势了！\x02",
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x13,
        (
            "#5P要想赢过我这副牌，\x01",
            "你就只有凑出\x01",
            "皇家同花顺了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x13,
        "#5P你怎么可能做得到──\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x14,
        "#11P#3504F真遗憾──你漏算啦。\x02",
    )

    CloseMessageWindow()
    Sound(90, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    SetChrName("")

    #A0556
    AnonymousTalk(
        0x13,
        "……………………咦？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0557
    AnonymousTalk(
        0x8,
        (
            "五张同点……\x01",
            "而且还是一王四Ａ的五张同点吗！！\x02\x03",

            "哎呀呀，真没想到能在这种场面下\x01",
            "见识到这种牌型啊……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0558
    AnonymousTalk(
        0x14,
        (
            "#3504F五同点是否能赢过皇家同花顺，\x01",
            "还要看具体规则是怎么定的……\x02\x03",

            "#3500F但不管怎样，\x01",
            "都要比你那副牌强吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    #C0559
    ChrTalk(
        0x13,
        "#5P#60W别、别、别、别……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)

    def lambda_903A():
        OP_9D(0xFE, 0x18060, 0x0, 0x1388, 0x64, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_903A)
    WaitChrThread(0x8, 1)
    Sound(819, 0, 100, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)

    #C0560
    ChrTalk(
        0x13,
        "#5P#4S别开玩笑了！你出老千！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x8, 500)

    #C0561
    ChrTalk(
        0x13,
        (
            "#5P喂！老板！\x01",
            "你跟他早就串通一气了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x8,
        (
            "#11P那、那怎么可能！\x01",
            "我可以向女神发誓！\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x8,
        (
            "#11P而且就我所见……\x01",
            "雷克特先生并没有任何\x01",
            "作弊的迹象！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)

    #C0564
    ChrTalk(
        0x13,
        (
            "#5P住嘴！！\x01",
            "我才不会相信你的鬼话！！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(101140, 1000, 4800, 1000)

    def lambda_9181():

        label("loc_9181")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_9181")

    QueueWorkItem2(0x8, 2, lambda_9181)

    def lambda_9193():
        OP_95(0xFE, 98400, 0, 2100, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9193)
    WaitChrThread(0x13, 1)

    def lambda_91B1():
        OP_95(0xFE, 100800, 0, 1600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_91B1)
    Sleep(50)
    SetChrSubChip(0x14, 0x1)
    WaitChrThread(0x13, 1)
    EndChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    Sound(804, 0, 100, 0)

    def lambda_91EA():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_91EA)

    def lambda_9203():
        OP_96(0xFE, 0x18BB4, 0xC8, 0x640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9203)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    ClearChrFlags(0x8, 0x20)

    #C0565
    ChrTalk(
        0x13,
        (
            "#5P我都已经得到全世界最强的\x01",
            "运气和直觉了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x13,
        (
            "#5P怎么可能会输给\x01",
            "这种莫名其妙的混账家伙！！\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x8,
        "客、客人……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x14,
        (
            "#5P#3505F喂喂，冷静一点嘛～\x02\x03",

            "#3504F──总之，这主要还是靠运气的。\x02\x03",

            "#3501F也就是说，你的好运气\x01",
            "已经到此为止啦！（一脸严肃）\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x13,
        "#5P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    def lambda_9366():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9366)

    def lambda_937F():
        OP_9D(0xFE, 0x19960, 0x0, 0x640, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_937F)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)

    #C0570
    ChrTalk(
        0x8,
        "#1P咳咳咳……\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x13,
        (
            "#5P#40W不可能……\x01",
            "我怎么可能会输……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x13,
        (
            "#5P#40W我既然使用了那种东西，\x01",
            "就不可能会输……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(100200, 1000, -1500, 2000)
    SetCameraDistance(23500, 2000)
    Sound(103, 0, 100, 0)

    def lambda_9435():
        OP_96(0xFE, 0x18894, 0x0, 0xFFFFF63C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9435)

    def lambda_944F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_944F)
    Sleep(200)

    def lambda_9463():
        OP_96(0xFE, 0x18380, 0x0, 0xFFFFF510, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9463)

    def lambda_947D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_947D)
    Sleep(450)
    BeginChrThread(0x104, 3, 0, 25)
    Sleep(450)
    BeginChrThread(0x103, 3, 0, 24)
    Sleep(450)

    def lambda_94A3():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEFFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94A3)

    def lambda_94BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_94BD)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(200)

    def lambda_9507():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEAE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_9507)

    def lambda_9521():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13D, 2, lambda_9521)
    Sleep(800)
    OP_6F(0x11)

    #C0573
    ChrTalk(
        0x12,
        "#6P冈兹……！？\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x101,
        "#0013F#12P不好……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0x0, 0x2BC)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0575
    ChrTalk(
        0x13,
        "#11P#4S不可能会输的啊啊啊啊啊！！\x02",
    )

    CloseMessageWindow()
    OP_68(101350, 1000, 3170, 1500)
    MoveCamera(45, 19, 0, 1500)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 27)
    Sleep(300)

    def lambda_95D6():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_95D6)
    Sleep(50)

    def lambda_95F3():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_95F3)
    Sleep(50)

    def lambda_9610():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9610)
    Sleep(50)

    def lambda_962D():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_962D)

    def lambda_9647():
        OP_96(0xFE, 0x18A88, 0x0, 0xA28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9647)
    WaitChrThread(0x13, 1)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x103, 1)

    def lambda_9677():
        TurnDirection(0xFE, 0x13, 700)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9677)
    OP_6F(0x41)
    Sleep(300)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    def lambda_96A0():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_96A0)

    #C0576
    ChrTalk(
        0x13,
        (
            "#4S#11P噢噢噢噢噢！\x01",
            "放、放开我啊啊啊！！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 2)

    #C0577
    ChrTalk(
        0x101,
        (
            "#0007F请、请冷静一点！\x02\x03",

            "#0010F（怎么回事！他怎么会有这么大的力量……！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x12,
        (
            "#6P冈兹！\x01",
            "请冷静一点！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0579
    ChrTalk(
        0x14,
        (
            "#5P#3505F噢噢，是你们啊～\x02\x03",

            "#3509F怎么样，最近还好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0580
    ChrTalk(
        0x102,
        (
            "#12P#0106F唉……\x01",
            "你竟然还能这么轻松悠闲地打招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x103,
        (
            "#6P#0211F#N……还是和以前一样，\x01",
            "在许多方面都超级可疑呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0582
    ChrTalk(
        0x13D,
        (
            "#12P#2102F哦，这个人可真有趣啊。\x01",
            "是你们的熟人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x104,
        (
            "#0306F这个，不，我们跟他大概\x01",
            "算不上是熟人吧──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0584
    ChrTalk(
        0x104,
        (
            "#0305F不过，居然是同花顺\x01",
            "和五张同点！？\x02\x03",

            "#0307F喂喂喂！？\x01",
            "这两种牌型竟然会同时出现！？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x14,
        (
            "#5P#3510F哎呀，刚才真是好险。\x02\x03",

            "#3504F要是输掉这局的话，\x01",
            "我恐怕连衣服都要被扒个精光了～\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x102,
        "#12P#0111F虽、虽然不太明白……\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x103,
        (
            "#6P#0206F不过，至少是顺利化解了\x01",
            "暴力伤害事件啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    def lambda_9A32():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_9A32)

    #C0588
    ChrTalk(
        0x13,
        "#11P#5S放开，放开我啊啊！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0589
    ChrTalk(
        0x13,
        (
            "#11P#4S我……我是绝对……\x01",
            "绝对不可能会输的啊啊！！！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    #A0590
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随后，矿工冈兹使用异常强大的力量，\x01",
            "拼命挣扎了一阵后，\x01",
            "突然就昏了过去。\x02\x03",

            "罗伊德等人将昏迷的冈兹\x01",
            "带回了他暂住的酒店。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0450", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_865D end

    def Function_24_9B78(): pass

    label("Function_24_9B78")


    def lambda_9B7D():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9B7D)

    def lambda_9B97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9B97)
    WaitChrThread(0x103, 1)

    def lambda_9BAC():
        OP_95(0xFE, 98700, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9BAC)
    WaitChrThread(0x103, 1)

    def lambda_9BCA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9BCA)
    Return()

    # Function_24_9B78 end

    def Function_25_9BD3(): pass

    label("Function_25_9BD3")


    def lambda_9BD8():
        OP_96(0xFE, 0x1863C, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BD8)

    def lambda_9BF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9BF2)
    WaitChrThread(0x104, 1)

    def lambda_9C07():
        OP_95(0xFE, 101100, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9C07)
    WaitChrThread(0x104, 1)

    def lambda_9C25():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9C25)
    Return()

    # Function_25_9BD3 end

    def Function_26_9C2E(): pass

    label("Function_26_9C2E")


    def lambda_9C33():
        OP_95(0xFE, 101600, 0, 2600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C33)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x13, 700)
    Return()

    # Function_26_9C2E end

    def Function_27_9C54(): pass

    label("Function_27_9C54")


    def lambda_9C59():
        OP_95(0xFE, 100400, 0, 2600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9C59)
    WaitChrThread(0x12, 1)
    TurnDirection(0x12, 0x13, 700)
    Return()

    # Function_27_9C54 end

    def Function_28_9C7A(): pass

    label("Function_28_9C7A")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(500)
    OP_68(4030, -100, 7770, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21440, 0)
    SetChrPos(0x101, 2140, -1000, 8000, 90)
    SetChrPos(0x102, 3160, -1000, 6510, 90)
    SetChrPos(0x103, 1840, -1000, 6510, 90)
    SetChrPos(0x104, 3560, -1000, 8000, 90)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_0D()

    #C0591
    ChrTalk(
        0x9,
        "#11P欢迎光临『巴鲁卡』～！\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x9,
        (
            "#11P啊，是兰迪先生。\x01",
            "欢迎光临～！\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x104,
        (
            "#6P#0300F哟，小切莉，\x01",
            "有点事想问你。\x02\x03",

            "在这里的奖品中，\x01",
            "好像有个叫『咪西』\x01",
            "的玩偶吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x9,
        "#11P嗯嗯，那是最便宜的奖品啦☆\x02",
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x9,
        (
            "#11P但因为很受欢迎，\x01",
            "所以经常被兑换一空～\x01",
            "今天去补点货好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x9,
        (
            "#11P不过，真没想到兰迪先生\x01",
            "还会对那种东西感兴趣呢～\x01",
            "好～可～爱～哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x104,
        "#6P#0309F啊哈哈哈，是吗～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    def lambda_9E82():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9E82)

    def lambda_9E8F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9E8F)
    Sleep(500)

    #C0598
    ChrTalk(
        0x104,
        "#5P#0300F怎么样，我说的不假吧？\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x102,
        "#11P#0100F的确不假啊。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        (
            "#12P#0203F……罗伊德前辈，\x01",
            "有人正为了那个东西而苦恼呢。\x02\x03",

            "#0201F总之，我们先去\x01",
            "试试手气好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 300)
    Sleep(300)

    #C0601
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯……说得也是。\x02\x03",

            "#0003F（是我的错觉吗……\x01",
            "  缇欧的眼睛似乎在闪闪发亮呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2820, -1000, 7050, 90)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetScenarioFlags(0x70, 3)
    OP_29(0xC, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_28_9C7A end

    def Function_29_9FCF(): pass

    label("Function_29_9FCF")

    EventBegin(0x1)
    Sleep(50)

    #C0602
    ChrTalk(
        0x101,
        (
            "#0001F都已经到『巴鲁卡』了，\x01",
            "我们就来打听一下有关冈兹先生的消息吧。\x02\x03",

            "服务员或客人中，也许有人会\x01",
            "知道他的行踪呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, -5000, 0)
    EventEnd(0x4)
    Return()

    # Function_29_9FCF end

    SaveToFile()

Try(main)
