from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1130.bin",                # FileName
        "c1130",                    # MapName
        "c1130",                    # Location
        0x0019,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 25, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1130",                  # 0
        "凯赛尔",                 # 1
        "凯赛尔",                 # 2
        "诺瓦斯",                 # 3
        "夏娜",                   # 4
        "夏娜",                   # 5
        "亚比",                   # 6
        "亚比",                   # 7
        "迈尔斯",                 # 8
        "塔基库",                 # 9
        "玛丽亚贝尔",             # 10
        "雷克特",                 # 11
    ))

    AddCharChip((
        "chr/ch28200.itc",                   # 00
        "chr/ch28202.itc",                   # 01
        "chr/ch29402.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch20302.itc",                   # 04
        "chr/ch34200.itc",                   # 05
        "chr/ch34202.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch28102.itc",                   # 08
        "chr/ch05502.itc",                   # 09
        "chr/ch07400.itc",                   # 0A
    ))

    DeclNpc(29309,   4000,    -9439,   90,   261,  0x0, 0,   0,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(7699,    150,     7980,    270,  469,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(18040,   180,     -9699,   180,  341,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(3500,    0,       -6989,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(13199,   4000,    10529,   180,  341,  0x0, 0,   4,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(3500,    0,       -8789,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(12649,   4000,    10529,   180,  341,  0x0, 1,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(7699,    150,     7980,    270,  341,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(10449,   180,     -12399,  300,  469,  0x0, 0,   8,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(30620,   4000,    -15439,  270,  469,  0x0, 0,   9,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(30540,   4000,    -10399,  90,   405,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)

    DeclActor(6290,    0,       8000,    1300,    7700,    1500,    7980,    0x007E, 0,  13, 0x0000)
    DeclActor(2750,    0,       11140,   1000,    2750,    1200,    11140,   0x007C, 0,  25, 0x0000)
    DeclActor(18610,   0,       -4500,   1000,    18610,   1200,    -4500,   0x007C, 0,  27, 0x0000)
    DeclActor(23750,   0,       -9500,   1000,    23750,   1200,    -9500,   0x007C, 0,  26, 0x0000)
    DeclActor(6500,    0,       -4500,   1000,    6500,    1200,    -4500,   0x007C, 0,  28, 0x0000)
    DeclActor(9300,    0,       -4500,   1000,    9300,    1200,    -4500,   0x007C, 0,  29, 0x0000)
    DeclActor(21300,   0,       -4500,   1000,    21300,   1200,    -4500,   0x007C, 0,  30, 0x0000)
    DeclActor(23750,   0,       -6600,   1000,    23750,   1200,    -6600,   0x007C, 0,  31, 0x0000)
    DeclActor(23750,   0,       -14700,  1000,    23750,   1200,    -14700,  0x007C, 0,  32, 0x0000)
    DeclActor(23750,   0,       -17600,  1000,    23750,   1200,    -17600,  0x007C, 0,  33, 0x0000)
    DeclActor(18500,   4000,    11800,   1000,    18500,   5200,    11800,   0x007C, 0,  34, 0x0000)
    DeclActor(21500,   4000,    11800,   1000,    21450,   5200,    11800,   0x007C, 0,  35, 0x0000)
    DeclActor(26400,   4000,    11800,   1000,    26400,   5200,    11800,   0x007C, 0,  36, 0x0000)
    DeclActor(29400,   4000,    11800,   1000,    29400,   5200,    11800,   0x007C, 0,  37, 0x0000)
    DeclActor(31800,   4000,    9200,    1000,    31750,   5200,    9200,    0x007C, 0,  38, 0x0000)
    DeclActor(31800,   4000,    6450,    1000,    31800,   5200,    6450,    0x007C, 0,  39, 0x0000)
    DeclActor(31800,   4000,    1440,    1000,    31800,   5200,    1440,    0x007C, 0,  40, 0x0000)
    DeclActor(31750,   4000,    -1650,   1000,    31750,   5200,    -1650,   0x007C, 0,  41, 0x0000)
    DeclActor(31750,   4000,    -6690,   1000,    31750,   5200,    -6690,   0x007C, 0,  42, 0x0000)

    ScpFunction((
        "Function_0_57C",          # 00, 0
        "Function_1_634",          # 01, 1
        "Function_2_6BD",          # 02, 2
        "Function_3_881",          # 03, 3
        "Function_4_980",          # 04, 4
        "Function_5_1A0A",         # 05, 5
        "Function_6_1C25",         # 06, 6
        "Function_7_2FC9",         # 07, 7
        "Function_8_30D1",         # 08, 8
        "Function_9_3130",         # 09, 9
        "Function_10_3A3C",        # 0A, 10
        "Function_11_3A6E",        # 0B, 11
        "Function_12_4188",        # 0C, 12
        "Function_13_4251",        # 0D, 13
        "Function_14_4266",        # 0E, 14
        "Function_15_5BC4",        # 0F, 15
        "Function_16_5D85",        # 10, 16
        "Function_17_5EE4",        # 11, 17
        "Function_18_5FFB",        # 12, 18
        "Function_19_618D",        # 13, 19
        "Function_20_61FA",        # 14, 20
        "Function_21_6364",        # 15, 21
        "Function_22_63F6",        # 16, 22
        "Function_23_67CE",        # 17, 23
        "Function_24_75E8",        # 18, 24
        "Function_25_7A5E",        # 19, 25
        "Function_26_7DB0",        # 1A, 26
        "Function_27_7F56",        # 1B, 27
        "Function_28_8045",        # 1C, 28
        "Function_29_80C4",        # 1D, 29
        "Function_30_814B",        # 1E, 30
        "Function_31_81CA",        # 1F, 31
        "Function_32_824B",        # 20, 32
        "Function_33_8349",        # 21, 33
        "Function_34_83CC",        # 22, 34
        "Function_35_8757",        # 23, 35
        "Function_36_8F67",        # 24, 36
        "Function_37_96E9",        # 25, 37
        "Function_38_99C9",        # 26, 38
        "Function_39_A042",        # 27, 39
        "Function_40_A44D",        # 28, 40
        "Function_41_A883",        # 29, 41
        "Function_42_AC25",        # 2A, 42
        "Function_43_B3A9",        # 2B, 43
        "Function_44_B58E",        # 2C, 44
        "Function_45_B691",        # 2D, 45
        "Function_46_B744",        # 2E, 46
        "Function_47_BC6F",        # 2F, 47
        "Function_48_BFA0",        # 30, 48
        "Function_49_C3A8",        # 31, 49
        "Function_50_C52B",        # 32, 50
        "Function_51_C5D8",        # 33, 51
        "Function_52_D033",        # 34, 52
        "Function_53_D5EB",        # 35, 53
        "Function_54_D74C",        # 36, 54
    ))


    def Function_0_57C(): pass

    label("Function_0_57C")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5BC"),
        (1, "loc_5C8"),
        (2, "loc_5D4"),
        (3, "loc_5E0"),
        (4, "loc_5EC"),
        (5, "loc_5F8"),
        (6, "loc_604"),
        (SWITCH_DEFAULT, "loc_610"),
    )


    label("loc_5BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_5F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_604")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_610")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_61C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_633")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_61C")

    label("loc_633")

    Return()

    # Function_0_57C end

    def Function_1_634(): pass

    label("Function_1_634")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BC")
    OP_95(0xFE, 29310, 4000, 9100, 1000, 0x0)
    OP_95(0xFE, 17140, 4000, 9100, 1000, 0x0)
    OP_95(0xFE, 17140, 4000, 6840, 1000, 0x0)
    OP_95(0xFE, 27790, 4000, 6840, 1000, 0x0)
    OP_95(0xFE, 27790, 4000, -9440, 1000, 0x0)
    OP_95(0xFE, 29310, 4000, -9440, 1000, 0x0)
    Jump("Function_1_634")

    label("loc_6BC")

    Return()

    # Function_1_634 end

    def Function_2_6BD(): pass

    label("Function_2_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6F6")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F1")
    SetChrFlags(0xF, 0x80)

    label("loc_6F1")

    Jump("loc_86A")

    label("loc_6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_704")
    Jump("loc_86A")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_712")
    Jump("loc_86A")

    label("loc_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_720")
    Jump("loc_86A")

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_733")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_86A")

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_755")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_86A")

    label("loc_755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_777")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_86A")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_799")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_86A")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7BB")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_86A")

    label("loc_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7D8")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_86A")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7E6")
    Jump("loc_86A")

    label("loc_7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7FE")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_86A")

    label("loc_7FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_80C")
    Jump("loc_86A")

    label("loc_80C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_81A")
    Jump("loc_86A")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_828")
    Jump("loc_86A")

    label("loc_828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_836")
    Jump("loc_86A")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_844")
    Jump("loc_86A")

    label("loc_844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_852")
    Jump("loc_86A")

    label("loc_852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_86A")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_86A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_880")
    Event(0, 54)

    label("loc_880")

    Return()

    # Function_2_6BD end

    def Function_3_881(): pass

    label("Function_3_881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_893")
    OP_65(0x0, 0x1)

    label("loc_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A8")
    OP_65(0x0, 0x1)

    label("loc_8A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C1")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_8C7")

    label("loc_8C1")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8FA")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8FA")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8FA")

    label("loc_8FA")

    OP_65(0x4, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_913")
    OP_66(0x8, 0x1)

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_942")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_93E")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_66(0x6, 0x1)
    Jump("loc_942")

    label("loc_93E")

    OP_65(0x3, 0x1)

    label("loc_942")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_95B")
    OP_66(0x2, 0x1)
    OP_66(0x4, 0x1)
    OP_66(0x6, 0x1)

    label("loc_95B")

    OP_65(0x5, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_97F")
    OP_66(0x5, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x9, 0x1)

    label("loc_97F")

    Return()

    # Function_3_881 end

    def Function_4_980(): pass

    label("Function_4_980")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A77")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E7")

    #C0001
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "差不多快到闭馆的时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "必须快点锁好门窗。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A18")

    label("loc_9E7")


    #C0003
    ChrTalk(
        0xFE,
        (
            "借阅、返还的受理即将结束，\x01",
            "请各位抓紧时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A18")

    Jump("loc_A72")

    label("loc_A1D")


    #C0004
    ChrTalk(
        0xFE,
        (
            "馆长有事\x01",
            "外出了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "而且差不多也快到闭馆时间了，\x01",
            "看来今天得由我\x01",
            "来锁门窗呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A72")

    Jump("loc_1A06")

    label("loc_A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE1")

    #C0006
    ChrTalk(
        0xFE,
        (
            "诺瓦斯先生今天\x01",
            "也打算待到\x01",
            "闭馆时间再走吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "最近他好像\x01",
            "干劲十足啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B3E")

    label("loc_AE1")


    #C0008
    ChrTalk(
        0xFE,
        (
            "啊……对了，古老文献\x01",
            "是禁止借出的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "如果各位想要查阅的话，\x01",
            "请在开馆\x01",
            "时间内前来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3E")

    Jump("loc_1A06")

    label("loc_B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD6")

    #C0010
    ChrTalk(
        0xFE,
        (
            "今天天气也很好啊，\x01",
            "感觉很适合晾晒防虫呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "啊……我并不是想\x01",
            "把这里的书籍弄乱哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "只是想让它们通通风而已。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C2A")

    label("loc_BD6")


    #C0013
    ChrTalk(
        0xFE,
        (
            "今天天气也很好啊，\x01",
            "感觉很适合野餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "等工作上有闲暇了，\x01",
            "我也去哪里玩玩吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2A")

    Jump("loc_1A06")

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBA")

    #C0015
    ChrTalk(
        0xFE,
        "这是摆放新发行书籍的地方。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "这个作者所著的系列作品\x01",
            "很受欢迎……\x01",
            "能读到这些书，市民们肯定都会很开心的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D03")

    label("loc_CBA")


    #C0017
    ChrTalk(
        0xFE,
        "这个作者的作品很受欢迎。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "各位要是想阅读的话，\x01",
            "早点借比较好哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D03")

    Jump("loc_1A06")

    label("loc_D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_D91")

    #C0019
    ChrTalk(
        0xFE,
        (
            "那个……\x01",
            "各位是在找儿童书籍吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "儿童书籍的书柜\x01",
            "在进门之后的右手边哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "因为比较受欢迎，\x01",
            "所以很多都借出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A06")

    label("loc_D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0A")

    #C0022
    ChrTalk(
        0xFE,
        (
            "……今天准备\x01",
            "好好将图书馆打扫一番。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "来馆的人也比较少，\x01",
            "对于打扫卫生来说时机正好呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E63")

    label("loc_E0A")


    #C0024
    ChrTalk(
        0xFE,
        "我今天早上也很早就起床了。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "今天下午两点就会闭馆，\x01",
            "各位要是想借书的话请尽快哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E63")

    Jump("loc_1A06")

    label("loc_E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED5")

    #C0026
    ChrTalk(
        0xFE,
        (
            "这个图书馆的二楼\x01",
            "可是观看游行的特等席位哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "呵呵，果然\x01",
            "大家都不知道呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F16")

    label("loc_ED5")


    #C0028
    ChrTalk(
        0xFE,
        (
            "我估计连\x01",
            "馆长都不知道。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "呵呵，因为这是只属于我的秘密。\x02",
    )

    CloseMessageWindow()

    label("loc_F16")

    Jump("loc_1A06")

    label("loc_F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1003")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAC")

    #C0030
    ChrTalk(
        0xFE,
        "今天好像比前两天更加热闹了呢……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "即使在馆内\x01",
            "都能听到外面的鼎沸人声。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "我要不要\x01",
            "也趁午休时出去转转呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FFE")

    label("loc_FAC")


    #C0033
    ChrTalk(
        0xFE,
        (
            "都说克洛斯贝尔人\x01",
            "很喜欢庆典……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "呵呵，我果然也是\x01",
            "地道的克洛斯贝尔人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFE")

    Jump("loc_1A06")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_105F")

    #C0035
    ChrTalk(
        0xFE,
        (
            "整理返还的书\x01",
            "真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "必须趁来馆的人比较少的时候，\x01",
            "重新摆放好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A06")

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1170")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111D")

    #C0037
    ChrTalk(
        0xFE,
        (
            "您好，欢迎光临克洛斯贝尔\x01",
            "市立图书馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……纪念庆典期间，\x01",
            "来馆的人果然急剧减少啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "算了，这也是没办法的事……\x01",
            "因为现在正是纪念庆典中最热闹的时候啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_116B")

    label("loc_111D")


    #C0040
    ChrTalk(
        0xFE,
        (
            "啊……对了对了，\x01",
            "馆内禁止饮食。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "在露天店铺买的东西\x01",
            "不许带入馆内哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116B")

    Jump("loc_1A06")

    label("loc_1170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_125A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1214")

    #C0042
    ChrTalk(
        0xFE,
        (
            "馆长好像在纪念庆典\x01",
            "期间休假。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "算了，反正在庆典的时候，\x01",
            "来馆的人会少很多……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "虽然还是有点没信心，\x01",
            "但我会一个人好好努力的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1255")

    label("loc_1214")


    #C0045
    ChrTalk(
        0xFE,
        "平常工作都是馆长在忙。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "难得有这个机会，\x01",
            "我得好好加油。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1255")

    Jump("loc_1A06")

    label("loc_125A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_133D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D2")

    #C0047
    ChrTalk(
        0xFE,
        (
            "那次地下传来了\x01",
            "重物倒地的声音……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "呼，总之馆长\x01",
            "没事就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "那些书还是\x01",
            "很重的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1338")

    label("loc_12D2")


    #C0050
    ChrTalk(
        0xFE,
        "幸好馆长没受伤。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "不过当时看到他\x01",
            "被埋在书堆里，挣扎着往外爬的场面，\x01",
            "我吃惊得都说不出话来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1338")

    Jump("loc_1A06")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1428")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BE")

    #C0052
    ChrTalk(
        0xFE,
        (
            "彩虹的门票\x01",
            "都已经卖光了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "要是我没放弃，\x01",
            "一直排队就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "我总是很容易就会放弃……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1423")

    label("loc_13BE")


    #C0055
    ChrTalk(
        0xFE,
        (
            "对了……在图书馆的藏书中，\x01",
            "有彩虹过去的公演目录\x01",
            "和写真集哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "……不过一直\x01",
            "都没被还回来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1423")

    Jump("loc_1A06")

    label("loc_1428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_154B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E0")

    #C0057
    ChrTalk(
        0xFE,
        (
            "馆长在休馆日\x01",
            "也会来图书馆\x01",
            "整理书籍和制作目录。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "他不仅是因为喜欢书，\x01",
            "也是为了造福市民\x01",
            "而努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "呵呵，虽然算不上位高权重，\x01",
            "但我觉得他很了不起。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1546")

    label("loc_14E0")


    #C0060
    ChrTalk(
        0xFE,
        (
            "对了……图书馆外面的草坪\x01",
            "也是馆长亲自修整的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "虽然并非位高权重，\x01",
            "但他是位勤劳且伟大的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1546")

    Jump("loc_1A06")

    label("loc_154B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_167F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160C")

    #C0062
    ChrTalk(
        0xFE,
        (
            "我听从父母的建议，\x01",
            "当上了公务员。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "虽然人们总是认为\x01",
            "公务员的报酬与工作量不成正比……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "但这个工作地点十分安静，\x01",
            "馆长也很和善，\x01",
            "所以并非大家想象得那么差。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_167A")

    label("loc_160C")


    #C0065
    ChrTalk(
        0xFE,
        (
            "我听从父母的建议，\x01",
            "当上了公务员。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "这里工作环境很安静，并且待遇也好。\x01",
            "所以并没有大家所想的那么差哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167A")

    Jump("loc_1A06")

    label("loc_167F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_175B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FF")

    #C0067
    ChrTalk(
        0xFE,
        "有白狼出场的童话书……？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "嗯，我记得\x01",
            "一楼的儿童书籍\x01",
            "专区里好像有。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "你们可以\x01",
            "去找找看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1756")

    label("loc_16FF")


    #C0070
    ChrTalk(
        0xFE,
        (
            "有白狼出场的童话书，\x01",
            "我记得一楼的\x01",
            "儿童书籍专区里好像有。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "你们可以\x01",
            "去找找看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1756")

    Jump("loc_1A06")

    label("loc_175B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_185B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1808")

    #C0072
    ChrTalk(
        0xFE,
        "唔，这本书是……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "我虽然在这里工作五年了，\x01",
            "但是还有许多藏书我没见过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "这个图书馆的藏书量真的很丰富。\x01",
            "我到现在都还没有全部搞清楚。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1856")

    label("loc_1808")


    #C0075
    ChrTalk(
        0xFE,
        (
            "这个图书馆\x01",
            "藏书量真的很丰富。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "估计只有馆长\x01",
            "才能把握全部的藏书情况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1856")

    Jump("loc_1A06")

    label("loc_185B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1935")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D5")

    #C0077
    ChrTalk(
        0xFE,
        "馆长真的是个爱书之人哦。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "不久前还不小心\x01",
            "被埋在了倒下的书堆里。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "我当时都看呆了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1930")

    label("loc_18D5")


    #C0080
    ChrTalk(
        0xFE,
        (
            "馆长之前被\x01",
            "埋在了书堆里。\x01",
            "我都看呆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……那个，说实话，\x01",
            "其实当时觉得有点好笑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1930")

    Jump("loc_1A06")

    label("loc_1935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1A06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CA")

    #C0082
    ChrTalk(
        0xFE,
        (
            "这个市立图书馆的藏书量\x01",
            "与邻近诸国相比也是数一数二的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "不过因为人手不足……\x01",
            "所以很多书籍都没有公开供大家借阅。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A06")

    label("loc_19CA")


    #C0084
    ChrTalk(
        0xFE,
        (
            "虽然这里有很多藏书……\x01",
            "但书籍空开手续的办理\x01",
            "比较缓慢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A06")

    TalkEnd(0xFE)
    Return()

    # Function_4_980 end

    def Function_5_1A0A(): pass

    label("Function_5_1A0A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A9E")
    Jump("loc_1AE8")

    label("loc_1A9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1ABE")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AE8")

    label("loc_1ABE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ADE")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AE8")

    label("loc_1ADE")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AE8")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBA")

    #C0085
    ChrTalk(
        0x9,
        (
            "欢迎光临\x01",
            "克洛斯贝尔市立图书馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "今天图书管理员上的是晚班，\x01",
            "所以现在馆里就只有我一个人……\x01",
            "但仍然可以办理借阅手续哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        "各位可以找我办理手续。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C1D")

    label("loc_1BBA")


    #C0088
    ChrTalk(
        0x9,
        (
            "今天迈尔斯先生\x01",
            "值晚班……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "……那个，\x01",
            "如果想要借阅书籍的话，\x01",
            "请不要客气，找我办理手续哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1D")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    Return()

    # Function_5_1A0A end

    def Function_6_1C25(): pass

    label("Function_6_1C25")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CB9")
    Jump("loc_1D03")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1CD9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D03")

    label("loc_1CD9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CF9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D03")

    label("loc_1CF9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D03")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1D7F")
    SetChrSubChip(0xFE, 0x0)

    #C0090
    ChrTalk(
        0xFE,
        "唔唔，哇哦！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "把这个总结一下，\x01",
            "就可以用在下篇论文上了……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC1")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEA")

    #C0092
    ChrTalk(
        0xFE,
        (
            "好资料太多\x01",
            "也让人苦恼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "想要找寻资料的话，\x01",
            "果然还是得来市立图书馆。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E0D")

    label("loc_1DEA")


    #C0094
    ChrTalk(
        0xFE,
        (
            "好，今天也要奋斗\x01",
            "到闭馆时间！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0D")

    Jump("loc_2FC1")

    label("loc_1E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1F2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC7")

    #C0095
    ChrTalk(
        0xFE,
        (
            "今天我找到了\x01",
            "很棒的东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "这可是八十年前的\x01",
            "商人们留下的笔记哦\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "嗯嗯……通过它，可以了解到\x01",
            "克洛斯贝尔当时的许多情况，\x01",
            "真是份宝贵的资料啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F27")

    label("loc_1EC7")


    #C0098
    ChrTalk(
        0xFE,
        (
            "八十年前，\x01",
            "克洛斯贝尔自治州还没有成立……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "当时不稳定的局势，\x01",
            "好像让商人们吃了很多苦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F27")

    Jump("loc_2FC1")

    label("loc_1F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1FB5")

    #C0100
    ChrTalk(
        0xFE,
        (
            "在论文被打回之后，\x01",
            "我就下定了决心。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "今后一定要全心全意\x01",
            "投身到研究中。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "因为还有很多文献和\x01",
            "资料我都还没看过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC1")

    label("loc_1FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_20C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2070")

    #C0103
    ChrTalk(
        0xFE,
        (
            "哼……你们对肯定要留级的诺瓦斯大人我\x01",
            "有什么意见吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x153,
        "#1100F？好奇怪的人。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        "（严重打击……！！）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 1)
    Jump("loc_20C0")

    label("loc_2070")


    #C0106
    ChrTalk(
        0xFE,
        (
            "呵呵，哈哈哈……\x01",
            "结果论文还是没来得及提交。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "算了，\x01",
            "再努力一年就好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C0")

    Jump("loc_2FC1")

    label("loc_20C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_21BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214E")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0108
    ChrTalk(
        0xFE,
        "现、现在几点了……？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "糟糕……\x01",
            "必须马上赶去机场了。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        "不然会来不及交论文……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21B6")

    label("loc_214E")


    #C0111
    ChrTalk(
        0xFE,
        (
            "我在位于雷曼自治州的\x01",
            "一所大学里读书……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "如果不计算交通时间，\x01",
            "很有可能会来不及……（絮絮叨叨）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B6")

    Jump("loc_2FC1")

    label("loc_21BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_22D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2292")

    #C0113
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔，『钟』自古以来\x01",
            "就拥有特殊的含义……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "早市的开始，运货马车的发车，\x01",
            "或是通知敌袭的警报……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔大圣堂\x01",
            "用鸣钟来报时的方式，\x01",
            "据说是从中世纪流传下来的习俗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22D3")

    label("loc_2292")


    #C0116
    ChrTalk(
        0xFE,
        (
            "啊，怎么觉得\x01",
            "意识有点开始恍惚了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "是不是太拼命了呢？\x02",
    )

    CloseMessageWindow()

    label("loc_22D3")

    Jump("loc_2FC1")

    label("loc_22D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_243A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2402")

    #C0118
    ChrTalk(
        0xFE,
        (
            "外面有庆典活动吗……呵呵呵，\x01",
            "我正在拼命赶论文呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "其实游行的起源是\x01",
            "本地有权有势的人物\x01",
            "在节日期间展示自家彩车。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔自治州成立之后，\x01",
            "这就成为了纪念庆典\x01",
            "的庆祝活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "然后此传统一直延续至今，\x01",
            "游行彩车一般都是由\x01",
            "财经界人士和工商协会出资提供的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2435")

    label("loc_2402")


    #C0122
    ChrTalk(
        0xFE,
        (
            "…………………………\x01",
            "大家好像都在享受庆典呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2435")

    Jump("loc_2FC1")

    label("loc_243A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_257E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2519")

    #C0123
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔从中世纪开始，\x01",
            "就是世界首屈一指的贸易都市。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "从地理位置上来看，克洛斯贝尔位于\x01",
            "前往大陆西部的交通要道，\x01",
            "所以人力资源和资金自然就流向这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "……时至今日，\x01",
            "情况也仍未改变。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2579")

    label("loc_2519")


    #C0126
    ChrTalk(
        0xFE,
        (
            "而且现在还有了列车\x01",
            "和飞行船这些交通工具……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "可以说克洛斯贝尔比\x01",
            "以往聚集了更多资源吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2579")

    Jump("loc_2FC1")

    label("loc_257E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_265D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2629")

    #C0128
    ChrTalk(
        0xFE,
        (
            "回、回过神来，\x01",
            "才发现现在是纪念庆典……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "这么说来，\x01",
            "这个月就得提交论文了……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "现、现在可不是\x01",
            "慢慢品读文献的时候，\x01",
            "必须快点写好……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2658")

    label("loc_2629")


    #C0131
    ChrTalk(
        0xFE,
        (
            "截、截稿期限……\x01",
            "我彻底把这个忘记了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2658")

    Jump("loc_2FC1")

    label("loc_265D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_272E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D5")

    #C0132
    ChrTalk(
        0xFE,
        (
            "什么……！？\x01",
            "你们要去调查\x01",
            "『星见之塔』？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "唔唔，太狡猾了……\x01",
            "我也想去那里看看的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2729")

    label("loc_26D5")


    #C0134
    ChrTalk(
        0xFE,
        (
            "『星见之塔』建造于中世纪的\x01",
            "一个重要遗迹……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "你们千万不要\x01",
            "把它破坏了哦！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2729")

    Jump("loc_2FC1")

    label("loc_272E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B9")

    #C0136
    ChrTalk(
        0xFE,
        (
            "馆长不允许\x01",
            "我进入地下资料室……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "竟然说那里危险。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "……………………？？\x01",
            "在图书馆里会有什么危险……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2821")

    label("loc_27B9")


    #C0139
    ChrTalk(
        0xFE,
        (
            "馆长说他会帮我下去找资料的，\x01",
            "我只要等着就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "不过图书馆里竟然会有危险……\x01",
            "到底是怎么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2821")

    Jump("loc_2FC1")

    label("loc_2826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2923")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28DB")

    #C0141
    ChrTalk(
        0xFE,
        (
            "论文的截稿期限临近了，\x01",
            "不抓紧点的话，又会留级了……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "咳咳，总之\x01",
            "只能拜托馆长\x01",
            "帮我去地下资料室找资料了。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "只凭手上的资料，\x01",
            "远远不够写论文啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_291E")

    label("loc_28DB")


    #C0144
    ChrTalk(
        0xFE,
        (
            "这里的地下资料室中\x01",
            "有许多古老的文献。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "十分具有查阅价值。\x02",
    )

    CloseMessageWindow()

    label("loc_291E")

    Jump("loc_2FC1")

    label("loc_2923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A01")

    #C0146
    ChrTalk(
        0xFE,
        (
            "这个市立图书馆的\x01",
            "历史很悠久哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "它的前身是资料馆，\x01",
            "原本似乎是克洛斯贝尔的商人们\x01",
            "保管账簿的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "所以这里还留有\x01",
            "三百多年前的资料。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "对研究历史的学者来说，\x01",
            "这里就是资料的宝库。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A52")

    label("loc_2A01")


    #C0150
    ChrTalk(
        0xFE,
        (
            "当时的资料，都被很好地\x01",
            "保存在这个图书馆里。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "不过那些一般都不对外公开。\x02",
    )

    CloseMessageWindow()

    label("loc_2A52")

    Jump("loc_2FC1")

    label("loc_2A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2BCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6C")

    #C0152
    ChrTalk(
        0xFE,
        (
            "虽然不怎么为人所知，\x01",
            "在克洛斯贝尔\x01",
            "残存着多处中世纪的遗迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "比较著名的有阿尔摩利卡古道尽头的\x01",
            "古战场遗迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "二十年前左右应该\x01",
            "有个大规模的调查团\x01",
            "去调查过。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "对了对了，放置在\x01",
            "中央广场的\x01",
            "那个巨大的钟……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "好像就是\x01",
            "古战场出土的文物。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BC8")

    label("loc_2B6C")


    #C0157
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔还有其它\x01",
            "几处有名的遗迹哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "我也很想去看看……\x01",
            "不过现在得赶着写论文……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC8")

    Jump("loc_2FC1")

    label("loc_2BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2CFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CAA")

    #C0159
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔，\x01",
            "熟悉历史的人\x01",
            "已经很少了……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "五十年前的历史倒还好，\x01",
            "不过一两百年前的历史\x01",
            "大家就都不知道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "我想知道克洛斯贝尔市\x01",
            "发展壮大的具体过程。\x01",
            "不过大家好像都对这个没有兴趣。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CF9")

    label("loc_2CAA")


    #C0162
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔人，\x01",
            "大多数都不了解历史呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        "作为学者，我对此感到很寒心。\x02",
    )

    CloseMessageWindow()

    label("loc_2CF9")

    Jump("loc_2FC1")

    label("loc_2CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9E")

    #C0164
    ChrTalk(
        0xFE,
        "研究历史必须脚踏实地，勤勤恳恳……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "寻找文献、搜集传说，\x01",
            "偶尔去调查相关的遗迹……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "总之历史就是一门需要不断调查的学问。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E0A")

    label("loc_2D9E")


    #C0167
    ChrTalk(
        0xFE,
        (
            "对历史研究者来说，\x01",
            "独自进行调查是基础中的基础。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "虽然我就是历史学者，\x01",
            "但也觉得这门学问很平实无华。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E0A")

    Jump("loc_2FC1")

    label("loc_2E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2A")
    Call(0, 7)
    Jump("loc_2ED3")

    label("loc_2E2A")


    #C0169
    ChrTalk(
        0xFE,
        (
            "因为资料完全不够……\x01",
            "所以我才去央求馆长，\x01",
            "拜托他让我看这些未公开资料的。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        "嗯，这下应该够了吧……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "要是不快点把论文写好的话，\x01",
            "就拿不到博士学位，又要留级……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED3")

    Jump("loc_2FC1")

    label("loc_2ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2FC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF3")
    Call(0, 7)
    Jump("loc_2FC1")

    label("loc_2EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6F")

    #C0172
    ChrTalk(
        0xFE,
        (
            "《克洛斯贝尔的传承》……\x01",
            "《玛因兹乡土史》……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "不行，资料完全不够……\x01",
            "这样会来不及提交论文的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FC1")

    label("loc_2F6F")


    #C0174
    ChrTalk(
        0xFE,
        (
            "我正在研究\x01",
            "克洛斯贝尔的历史。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "但找不到好资料。\x01",
            "这样就没法写论文了啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1C25 end

    def Function_7_2FC9(): pass

    label("Function_7_2FC9")


    #C0176
    ChrTalk(
        0xFE,
        (
            "哈哈哈……没想到\x01",
            "写个论文竟然这么难。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "在开始写论文之前，\x01",
            "我还买了娱乐小说，\x01",
            "想在闲暇之余看看的。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "啊，各位。\x01",
            "不嫌弃的话，\x01",
            "请收下这本书吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "我实在太忙了，\x01",
            "根本没时间看。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0180
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑市医生格伦　１卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('黑市医生格伦　１卷', 1)
    SetScenarioFlags(0x9C, 0)
    Return()

    # Function_7_2FC9 end

    def Function_8_30D1(): pass

    label("Function_8_30D1")

    TalkBegin(0xFE)

    #C0181
    ChrTalk(
        0xFE,
        (
            "今天我要把馆长推荐的书\x01",
            "借回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "呵呵，因为孩子回家之后\x01",
            "还想听我给他读这本书。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_30D1 end

    def Function_9_3130(): pass

    label("Function_9_3130")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31C4")
    Jump("loc_320E")

    label("loc_31C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31E4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_320E")

    label("loc_31E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3204")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_320E")

    label("loc_3204")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_320E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3241")
    Jump("loc_3A34")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_34A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_END)), "loc_336F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32FB")

    #C0183
    ChrTalk(
        0xFE,
        (
            "《玛尔克与森林中的魔女》下卷\x01",
            "终于可以借阅了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "那本书在图书馆的童话书中\x01",
            "是最受欢迎的。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "我在念给亚比\x01",
            "听的时候，\x01",
            "也不知不觉迷上了它……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_336A")

    label("loc_32FB")


    #C0186
    ChrTalk(
        0xFE,
        (
            "《玛尔克与森林深处的魔女》\x01",
            "是图书馆里最受欢迎的\x01",
            "童话书哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "书就放在一楼的书架上，\x01",
            "各位也请读读看吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_336A")

    Jump("loc_34A4")

    label("loc_336F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3381")
    Call(0, 12)
    Jump("loc_34A4")

    label("loc_3381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3448")

    #C0188
    ChrTalk(
        0xFE,
        (
            "亚比好像很想把自己喜欢的书\x01",
            "都推荐小琪雅看。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "那个，\x01",
            "会不会给各位添了很多麻烦啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        "#0204F不会，完全没有……\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#0000F我们虽然没法经常带琪雅来，\x01",
            "但还是请你多跟她玩哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34A4")

    label("loc_3448")


    #C0192
    ChrTalk(
        0xFE,
        (
            "亚比很喜欢看书，\x01",
            "只要图书馆开门，他每天都会来。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "呵呵……亚比好像\x01",
            "很喜欢小琪雅啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A4")

    Jump("loc_3A34")

    label("loc_34A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34F9")
    SetChrSubChip(0xFE, 0x0)

    #C0194
    ChrTalk(
        0xFE,
        (
            "巡警先生\x01",
            "一直拼命追赶。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "不过小猪\x01",
            "也一直拼命逃跑……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_34F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3570")

    #C0196
    ChrTalk(
        0xFE,
        (
            "纪念庆典之后，\x01",
            "亚比就一直求我给他\x01",
            "讲巡警先生的故事。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "呵呵……他好像\x01",
            "喜欢上了巡警先生的制服呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_3570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_35C5")

    #C0198
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "这孩子比我们家亚比大一点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "呵呵，你们要好好相处哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_35C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3615")

    #C0200
    ChrTalk(
        0xFE,
        (
            "啊，糟糕了。\x01",
            "都已经是这个时间了……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "得赶紧去\x01",
            "买点东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_3615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3623")
    Jump("loc_3A34")

    label("loc_3623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3694")

    #C0202
    ChrTalk(
        0xFE,
        (
            "我们家亚比如果\x01",
            "喜欢一本书，\x01",
            "就会一直求我给他念。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "呼，真没办法。\x01",
            "今天都已经读了五遍了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_3694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_371F")
    SetChrSubChip(0xFE, 0x0)

    #C0204
    ChrTalk(
        0xFE,
        (
            "那时传来了\x01",
            "女神的声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "『道路已经开启，\x01",
            "  快点回到同伴的身边吧……』\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "小狐狸听到之后，\x01",
            "便匆忙跑了出去……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_371F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37E9")

    #C0207
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "听说克洛斯贝尔的大圣堂\x01",
            "是一座很宏伟的建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "而且其中似乎也有很多\x01",
            "优秀的祭司和修女。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "亚比明年就可以去\x01",
            "主日学校上学了，\x01",
            "所以我准备先去大圣堂祷告一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_384F")

    label("loc_37E9")


    #C0210
    ChrTalk(
        0xFE,
        (
            "自从搬来克洛斯贝尔，\x01",
            "我还没去过大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "亚比非常喜欢爱德丝女神，\x01",
            "他一定会对那里很感兴趣吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384F")

    Jump("loc_3A34")

    label("loc_3854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_38BF")

    #C0212
    ChrTalk(
        0xFE,
        (
            "图书馆里有很多\x01",
            "儿童读物，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "不过看的人\x01",
            "出人意料地少。\x01",
            "这是因为什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_38BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3921")

    #C0214
    ChrTalk(
        0xFE,
        (
            "我最近刚搬来\x01",
            "克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的街道很漂亮，\x01",
            "真是一个很棒的城市呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_3921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3970")
    SetChrSubChip(0xFE, 0x0)

    #C0216
    ChrTalk(
        0xFE,
        (
            "出现在那里的\x01",
            "竟然是头恐怖的恶魔。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "哇哇哇哇哇……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_3970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3A34")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39EB")

    #C0218
    ChrTalk(
        0xFE,
        (
            "然后空之女神\x01",
            "所降下的光芒……\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    Sleep(500)

    #C0219
    ChrTalk(
        0xFE,
        "充溢了整个世界。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        "动物们都大吃一惊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A34")

    label("loc_39EB")


    #C0221
    ChrTalk(
        0xFE,
        (
            "然后空之女神\x01",
            "所降下的光芒充溢了整个世界。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "动物们都大吃一惊……\x02",
    )

    CloseMessageWindow()

    label("loc_3A34")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_3130 end

    def Function_10_3A3C(): pass

    label("Function_10_3A3C")

    TalkBegin(0xFE)

    #C0223
    ChrTalk(
        0xFE,
        (
            "回家之后，\x01",
            "我还要让妈妈给我讲故事～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_3A3C end

    def Function_11_3A6E(): pass

    label("Function_11_3A6E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B02")
    Jump("loc_3B4C")

    label("loc_3B02")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B22")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B4C")

    label("loc_3B22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B42")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B4C")

    label("loc_3B42")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B4C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3B7F")
    Jump("loc_417C")

    label("loc_3B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_END)), "loc_3BCE")

    #C0224
    ChrTalk(
        0xFE,
        "接下来故事里会发生什么呢。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        "快点念快点念嘛～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C07")

    label("loc_3BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE0")
    Call(0, 12)
    Jump("loc_3C07")

    label("loc_3BE0")


    #C0226
    ChrTalk(
        0xFE,
        (
            "下次我要把这书\x01",
            "推荐给琪雅姐姐看～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C07")

    Jump("loc_417C")

    label("loc_3C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3C38")
    SetChrSubChip(0xFE, 0x1)

    #C0227
    ChrTalk(
        0xFE,
        "哇，巡警先生好帅啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_3C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CDB")

    #C0228
    ChrTalk(
        0xFE,
        (
            "那个那个，\x01",
            "琪雅姐姐呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#0000F哈哈，今天她没和我们一起来哦。\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#0102F她下次还会来玩的，\x01",
            "乖乖等着哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "嗯，我乖乖等着！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3CFA")

    label("loc_3CDB")


    #C0232
    ChrTalk(
        0xFE,
        (
            "替我跟琪雅姐姐\x01",
            "问声好哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFA")

    Jump("loc_417C")

    label("loc_3CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9E")

    #C0233
    ChrTalk(
        0xFE,
        (
            "哇～哦，妈妈要念\x01",
            "这本书里的故事给我听哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x153,
        "#1110F真好，琪雅也想听听看。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0235
    ChrTalk(
        0xFE,
        "姐姐也喜欢这本书吗～？\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "嘿嘿嘿，跟我一样呢～！\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x153,
        "#1109F嗯，跟你一样哦～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3E15")

    #C0238
    ChrTalk(
        0x102,
        (
            "#0102F（小孩子们\x01",
            "  果然很快就能玩到一起……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E96")

    label("loc_3E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3E58")

    #C0239
    ChrTalk(
        0x103,
        (
            "#0204F（小孩子们\x01",
            "  果然很快就能玩到一起呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E96")

    label("loc_3E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3E96")

    #C0240
    ChrTalk(
        0x104,
        (
            "#0302F（小孩子们\x01",
            "  果然很快就能玩到一起啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E96")

    SetScenarioFlags(0x0, 4)
    Jump("loc_3EDE")

    label("loc_3E9E")


    #C0241
    ChrTalk(
        0xFE,
        (
            "姐姐，\x01",
            "我们下次再一起玩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x153,
        (
            "#1110F嗯，好呀～！\x01",
            "再见！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EDE")

    Jump("loc_417C")

    label("loc_3EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3F18")
    SetChrSubChip(0xFE, 0x1)

    #C0243
    ChrTalk(
        0xFE,
        (
            "啊，妈妈！\x01",
            "再多念些给我听嘛！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_3F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3F26")
    Jump("loc_417C")

    label("loc_3F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3F73")
    SetChrSubChip(0xFE, 0x1)

    #C0244
    ChrTalk(
        0xFE,
        "那个，还是这本书比较好呢。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "因为我\x01",
            "最喜欢女神了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_3F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3FB8")

    #C0246
    ChrTalk(
        0xFE,
        "哇，好兴奋……\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "听妈妈念故事书，\x01",
            "真的很开心！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_3FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4021")

    #C0248
    ChrTalk(
        0xFE,
        "我跟你们说哦……\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "那边有一个叫做大圣堂的，\x01",
            "很大的教堂哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "我也想去那里看看！\x02",
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_4021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4056")
    SetChrSubChip(0xFE, 0x1)

    #C0251
    ChrTalk(
        0xFE,
        (
            "啊，妈妈！\x01",
            "再多念些给我听嘛！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_4056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40BF")

    #C0252
    ChrTalk(
        0xFE,
        "等我长大后，\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "一定要\x01",
            "当个神父。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "然后给小孩子\x01",
            "讲这本书里的故事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4113")

    label("loc_40BF")


    #C0255
    ChrTalk(
        0xFE,
        (
            "等我长大后，\x01",
            "一定要当个神父。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "然后像妈妈一样，\x01",
            "给小孩子讲这本书里的故事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4113")

    Jump("loc_417C")

    label("loc_4118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4145")
    SetChrSubChip(0xFE, 0x1)

    #C0257
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "会怎样呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_417C")

    label("loc_4145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_417C")
    SetChrSubChip(0xFE, 0x1)

    #C0258
    ChrTalk(
        0xFE,
        "哇～哇～！\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "再多念些给我听嘛～！\x02",
    )

    CloseMessageWindow()

    label("loc_417C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_3A6E end

    def Function_12_4188(): pass

    label("Function_12_4188")

    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xE, 0x0)

    #C0260
    ChrTalk(
        0xC,
        (
            "最后大家\x01",
            "都过上了幸福美好的日子。\x01",
            "可喜可贺，可喜可贺。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        "……亚比，故事好听吗？\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xE,
        "嗯，很好听哦！\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xE,
        (
            "下次我要把这书\x01",
            "推荐给琪雅姐姐看。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "呵呵，没错。\x01",
            "这也许是个好主意哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_12_4188 end

    def Function_13_4251(): pass

    label("Function_13_4251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4262")
    Call(0, 14)
    Jump("loc_4265")

    label("loc_4262")

    Call(0, 5)

    label("loc_4265")

    Return()

    # Function_13_4251 end

    def Function_14_4266(): pass

    label("Function_14_4266")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42FA")
    Jump("loc_4344")

    label("loc_42FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_431A")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4344")

    label("loc_431A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_433A")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4344")

    label("loc_433A")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4344")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_437A")
    Call(0, 21)
    Jump("loc_5BBC")

    label("loc_437A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_452A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4410")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_43A0")
    Call(0, 20)
    Jump("loc_440B")

    label("loc_43A0")


    #C0265
    ChrTalk(
        0xF,
        (
            "谢谢你，罗伊德。\x01",
            "要是只靠馆员的话，\x01",
            "估计没办法全部收回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xF,
        "如果有需要的话，还会找你们帮忙的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_440B")

    Jump("loc_4525")

    label("loc_4410")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4435")
    Call(0, 52)
    Jump("loc_4525")

    label("loc_4435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_44F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4453")
    Call(0, 20)
    Jump("loc_44F4")

    label("loc_4453")


    #C0267
    ChrTalk(
        0xF,
        (
            "回收超期未还的书本这个任务，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xF,
        (
            "这次的借书人都是住在\x01",
            "克洛斯贝尔郊外的，\x01",
            "所以你们可以慢慢进行回收。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xF,
        (
            "收回三本书后，\x01",
            "就拿回来交给我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_44F4")

    Jump("loc_4525")

    label("loc_44F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_450E")
    Call(0, 49)
    Jump("loc_4525")

    label("loc_450E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4522")
    Call(0, 48)
    Jump("loc_4525")

    label("loc_4522")

    Call(0, 20)

    label("loc_4525")

    Jump("loc_5BBC")

    label("loc_452A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_46DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4550")
    Call(0, 19)
    Jump("loc_45BB")

    label("loc_4550")


    #C0270
    ChrTalk(
        0xF,
        (
            "谢谢你，罗伊德。\x01",
            "要是只靠馆员的话，\x01",
            "估计没办法全部收回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xF,
        "如果有需要的话，还会找你们帮忙的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_45BB")

    Jump("loc_46D5")

    label("loc_45C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45E5")
    Call(0, 52)
    Jump("loc_46D5")

    label("loc_45E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_46A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4603")
    Call(0, 19)
    Jump("loc_46A4")

    label("loc_4603")


    #C0272
    ChrTalk(
        0xF,
        (
            "回收超期未还的书本这个任务，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xF,
        (
            "这次的借书人都是住在\x01",
            "克洛斯贝尔郊外的，\x01",
            "所以你们可以慢慢进行回收。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xF,
        (
            "收回三本书后，\x01",
            "就拿回来交给我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_46A4")

    Jump("loc_46D5")

    label("loc_46A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_46BE")
    Call(0, 49)
    Jump("loc_46D5")

    label("loc_46BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_46D2")
    Call(0, 48)
    Jump("loc_46D5")

    label("loc_46D2")

    Call(0, 19)

    label("loc_46D5")

    Jump("loc_5BBC")

    label("loc_46DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_488A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4700")
    Call(0, 18)
    Jump("loc_476B")

    label("loc_4700")


    #C0275
    ChrTalk(
        0xF,
        (
            "谢谢你，罗伊德。\x01",
            "要是只靠馆员的话，\x01",
            "估计没办法全部收回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xF,
        "如果有需要的话，还会找你们帮忙的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_476B")

    Jump("loc_4885")

    label("loc_4770")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4795")
    Call(0, 52)
    Jump("loc_4885")

    label("loc_4795")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_4859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_47B3")
    Call(0, 18)
    Jump("loc_4854")

    label("loc_47B3")


    #C0277
    ChrTalk(
        0xF,
        (
            "回收超期未还的书本这个任务，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xF,
        (
            "这次的借书人都是住在\x01",
            "克洛斯贝尔郊外的，\x01",
            "所以你们可以慢慢进行回收。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xF,
        (
            "收回三本书后，\x01",
            "就拿回来交给我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4854")

    Jump("loc_4885")

    label("loc_4859")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_486E")
    Call(0, 49)
    Jump("loc_4885")

    label("loc_486E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4882")
    Call(0, 48)
    Jump("loc_4885")

    label("loc_4882")

    Call(0, 18)

    label("loc_4885")

    Jump("loc_5BBC")

    label("loc_488A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D0D")

    #C0280
    ChrTalk(
        0x153,
        (
            "#1110F那个那个，这里有好多书啊！\x02\x03",

            "#1109F琪雅也可以在\x01",
            "这里看书吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x153, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4993")
    Jump("loc_49DD")

    label("loc_4993")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_49B3")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49DD")

    label("loc_49B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49D3")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49DD")

    label("loc_49D3")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49DD")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0281
    ChrTalk(
        0xF,
        "哦，难道……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xF,
        "你喜欢看书吗？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x153,
        (
            "#1111F嗯，大概吧！\x02\x03",

            "#1110F一看到书的封面，\x01",
            "我就觉得很兴奋！\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xF,
        (
            "嗯嗯，我明白这种感觉。\x01",
            "我也是因为太喜欢书了，\x01",
            "所以才成为图书管理员的。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x153,
        "#1105F？？？\x02",
    )

    CloseMessageWindow()
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x101, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B5B")
    Jump("loc_4BA5")

    label("loc_4B5B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B7B")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4BA5")

    label("loc_4B7B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B9B")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4BA5")

    label("loc_4B9B")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BA5")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0286
    ChrTalk(
        0xF,
        (
            "罗伊德，你们一定要多借几本书，\x01",
            "如果是这孩子要看的话，借几本都行哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#0000F谢、谢谢啊，叔叔。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4C7C")

    #C0288
    ChrTalk(
        0x102,
        (
            "#0100F（呵呵，图书管理员跟罗伊德认识，\x01",
            "  真是太好了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D05")

    label("loc_4C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4CC5")

    #C0289
    ChrTalk(
        0x103,
        (
            "#0200F（图书管理员跟罗伊德前辈认识，\x01",
            "  真是太好了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D05")

    label("loc_4CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4D05")

    #C0290
    ChrTalk(
        0x104,
        (
            "#0300F（图书管理员跟罗伊德认识，\x01",
            "  真是太好了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D05")

    SetScenarioFlags(0xB0, 7)
    Jump("loc_4D9F")

    label("loc_4D0D")


    #C0291
    ChrTalk(
        0xF,
        (
            "罗伊德，你一定要\x01",
            "借几本书给这孩子看。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xF,
        (
            "读书对小孩子有好处……\x01",
            "你们一定要继续\x01",
            "培养她读书的兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈……\x01",
            "那我们就去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D9F")

    Jump("loc_5BBC")

    label("loc_4DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4EF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8D")

    #C0294
    ChrTalk(
        0xF,
        (
            "以前我就一直\x01",
            "鼓励塞茜尔，\x01",
            "叫她做自己喜欢的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xF,
        (
            "但就连我都没想到\x01",
            "她会成为一名护士。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xF,
        (
            "现在想想，好像她\x01",
            "小时候就一直央求我带她\x01",
            "去乌尔斯拉医院看看……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xF,
        (
            "应该是从那时候起\x01",
            "就梦想成为护士了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4EF1")

    label("loc_4E8D")


    #C0298
    ChrTalk(
        0xF,
        (
            "塞茜尔成为了护士，\x01",
            "你阿姨她好像很担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xF,
        (
            "不过这是那孩子自己选择的道路，\x01",
            "我们必须支持她。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF1")

    Jump("loc_5BBC")

    label("loc_4EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_509E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_502F")

    #C0300
    ChrTalk(
        0xF,
        (
            "痛痛痛……我刚才在\x01",
            "整理地下资料室的时候……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xF,
        (
            "一堆书突然倒下来，\x01",
            "把我埋在了下面。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xF,
        (
            "如果凯赛尔没来救我的话，\x01",
            "我说不定已经窒息死亡了。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#0006F没这么夸张吧……\x02\x03",

            "#0000F对了，叔叔，\x01",
            "如果有什么需要帮忙的，\x01",
            "来找我们支援科不就行了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xF,
        (
            "哈哈，抱歉抱歉。\x01",
            "因为没时间联系你们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5099")

    label("loc_502F")


    #C0305
    ChrTalk(
        0xF,
        (
            "我的梦想是将地下资料室中的文献整理好，\x01",
            "然后向市民们公开。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xF,
        (
            "不过书太多了，\x01",
            "实在没法全部都整理完。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5099")

    Jump("loc_5BBC")

    label("loc_509E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_51D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5188")

    #C0307
    ChrTalk(
        0xF,
        (
            "今天要总结\x01",
            "新书的购买清单。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xF,
        (
            "在我们图书馆，\x01",
            "这位作者的系列作品最受欢迎。\x01",
            "必须得多购买些。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……克洛斯贝尔市\x01",
            "的人口太多了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xF,
        (
            "所以来借书的人自然也就多了。\x01",
            "呵呵，这点很值得高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_51D4")

    label("loc_5188")


    #C0311
    ChrTalk(
        0xF,
        (
            "购买藏书本来用的就是市民的钱。\x01",
            "希望大家都不要客气，\x01",
            "尽量多来借一些书。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D4")

    Jump("loc_5BBC")

    label("loc_51D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_532F")

    #C0312
    ChrTalk(
        0xF,
        (
            "罗伊德，很少见你们\x01",
            "下午过来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xF,
        (
            "难道今天你们\x01",
            "休假吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0000F叔叔……\x01",
            "……啊，并不是呢。\x02\x03",

            "支援科的休假非常少，\x01",
            "今天也是从早上就开始工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x103,
        (
            "#0200F我们也是最近才体会到的，\x01",
            "支援科的工作非常忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xF,
        (
            "哈哈，这样子啊。\x01",
            "没办法，警察都忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xF,
        (
            "图书馆都会有适当的休假哦，\x01",
            "在公务员中也算是特别轻松的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5391")

    label("loc_532F")


    #C0318
    ChrTalk(
        0xF,
        (
            "这个市立图书馆\x01",
            "每星期都会固定放假一天。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xF,
        (
            "不过我是图书管理员，\x01",
            "就算放假也有很多杂活要做。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5391")

    Jump("loc_5BBC")

    label("loc_5396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5514")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_53FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_53F7")

    #C0320
    ChrTalk(
        0xF,
        "谢谢啊，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xF,
        "如果有需要的话，还会找你们帮忙的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53FA")

    label("loc_53F7")

    Call(0, 17)

    label("loc_53FA")

    Jump("loc_550F")

    label("loc_53FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('铁道爱好者的推荐', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玛尔克与森林深处的魔女·上', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('改变大陆的美人们', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5436")
    Call(0, 47)
    Jump("loc_550F")

    label("loc_5436")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_54E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5454")
    Call(0, 15)
    Jump("loc_54DE")

    label("loc_5454")


    #C0322
    ChrTalk(
        0xF,
        (
            "回收超期未还的书本这个任务，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xF,
        (
            "收回三本书后，\x01",
            "就拿回来给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xF,
        (
            "因为情况并不紧急，\x01",
            "所以你们可以慢慢进行回收。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_54DE")

    Jump("loc_550F")

    label("loc_54E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_54F8")
    Call(0, 44)
    Jump("loc_550F")

    label("loc_54F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_550C")
    Call(0, 43)
    Jump("loc_550F")

    label("loc_550C")

    Call(0, 15)

    label("loc_550F")

    Jump("loc_5BBC")

    label("loc_5514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5692")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_557D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5575")

    #C0325
    ChrTalk(
        0xF,
        "谢谢啊，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xF,
        "如果有需要的话，还会找你们帮忙的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5578")

    label("loc_5575")

    Call(0, 17)

    label("loc_5578")

    Jump("loc_568D")

    label("loc_557D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('铁道爱好者的推荐', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玛尔克与森林深处的魔女·上', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('改变大陆的美人们', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55B4")
    Call(0, 47)
    Jump("loc_568D")

    label("loc_55B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_5661")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_55D2")
    Call(0, 16)
    Jump("loc_565C")

    label("loc_55D2")


    #C0327
    ChrTalk(
        0xF,
        (
            "回收超期未还的书本这个任务，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xF,
        (
            "收回三本书后，\x01",
            "就拿回来给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xF,
        (
            "因为事情并不紧急，\x01",
            "所以你们可以慢慢进行回收。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_565C")

    Jump("loc_568D")

    label("loc_5661")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_5676")
    Call(0, 44)
    Jump("loc_568D")

    label("loc_5676")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_568A")
    Call(0, 43)
    Jump("loc_568D")

    label("loc_568A")

    Call(0, 16)

    label("loc_568D")

    Jump("loc_5BBC")

    label("loc_5692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5810")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_56FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_56F3")

    #C0330
    ChrTalk(
        0xF,
        "谢谢啊，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xF,
        "如果有需要的话，还会找你们帮忙的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_56F6")

    label("loc_56F3")

    Call(0, 17)

    label("loc_56F6")

    Jump("loc_580B")

    label("loc_56FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('铁道爱好者的推荐', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玛尔克与森林深处的魔女·上', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('改变大陆的美人们', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5732")
    Call(0, 47)
    Jump("loc_580B")

    label("loc_5732")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_57DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5750")
    Call(0, 16)
    Jump("loc_57DA")

    label("loc_5750")


    #C0332
    ChrTalk(
        0xF,
        (
            "回收超期未还的书本这个任务，\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xF,
        (
            "收回三本书后，\x01",
            "就拿回来给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xF,
        (
            "因为事情并不紧急，\x01",
            "所以你们可以慢慢进行回收。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_57DA")

    Jump("loc_580B")

    label("loc_57DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_57F4")
    Call(0, 44)
    Jump("loc_580B")

    label("loc_57F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5808")
    Call(0, 43)
    Jump("loc_580B")

    label("loc_5808")

    Call(0, 17)

    label("loc_580B")

    Jump("loc_5BBC")

    label("loc_5810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5BB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6D")

    #C0335
    ChrTalk(
        0x101,
        (
            "#0000F叔叔，\x01",
            "好久不见。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xF,
        (
            "哦？你不是……\x01",
            "以前住在隔壁的罗伊德嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xF,
        "哈哈哈，实在是吃了一惊啊！\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xF,
        (
            "虽然听说过你快回来了，\x01",
            "……但没想到你都长这么大了，简直让人认不出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#0012F呵呵，只是身高长了，\x01",
            "但内在还是很不成熟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xF,
        (
            "没那回事。\x01",
            "你不是已经顺利\x01",
            "通过搜查官考试了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xF,
        (
            "盖伊一定\x01",
            "也会为你高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#0008F……会吗？\x02\x03",

            "……如果真是那样就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xF,
        "嗯，一定会的。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xF,
        (
            "虽然我因为图书管理员的工作，\x01",
            "所以经常不在家……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xF,
        (
            "不过你阿姨她应该都在家里。\x01",
            "如果有什么需要帮忙的，\x01",
            "就去找她哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#0000F嗯，\x01",
            "那就麻烦阿姨了。\x02\x03",

            "#0003F……承蒙您照顾了，\x01",
            "叔叔。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 7)
    Jump("loc_5BAE")

    label("loc_5A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B64")

    #C0347
    ChrTalk(
        0xF,
        (
            "唔，罗伊德，\x01",
            "你不借本书去看吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#0012F哈哈……说起来，叔叔以前\x01",
            "也经常给我推荐书啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xF,
        (
            "呵呵，因为书是好东西哦。\x01",
            "只要沉浸在书堆里，心情便能得到放松。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xF,
        (
            "有空的话，\x01",
            "你们就慢慢看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xF,
        (
            "这里的藏书量\x01",
            "可是很多的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5BAE")

    label("loc_5B64")


    #C0352
    ChrTalk(
        0xF,
        (
            "有空的话，\x01",
            "你们就慢慢看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xF,
        (
            "呵呵，这里的藏书量\x01",
            "可是很多的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BAE")

    Jump("loc_5BBC")

    label("loc_5BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5BBC")

    label("loc_5BBC")

    SetChrSubChip(0xF, 0x0)
    TalkEnd(0xF)
    Return()

    # Function_14_4266 end

    def Function_15_5BC4(): pass

    label("Function_15_5BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2C")

    #C0354
    ChrTalk(
        0xF,
        (
            "嗯，还有\x01",
            "很多书未归还啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xF,
        (
            "我们这里人手不足，\x01",
            "管理上难免存在疏漏。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xF,
        (
            "所以很多人\x01",
            "到期限了都\x01",
            "没把书还回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x101,
        (
            "#0005F这样子啊。\x01",
            "叔叔也很辛苦啊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5CD5")

    #C0358
    ChrTalk(
        0xF,
        (
            "嗯，不过\x01",
            "你们可\x01",
            "帮了我们不少忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xF,
        (
            "我身为图书管理员，\x01",
            "就想把图书馆管理好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D24")

    label("loc_5CD5")


    #C0360
    ChrTalk(
        0xF,
        (
            "嗯，其中\x01",
            "有的人借了很长时间\x01",
            "都一直没把书还回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xF,
        (
            "估计应该是\x01",
            "忘了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D24")

    SetScenarioFlags(0x0, 5)
    Jump("loc_5D84")

    label("loc_5D2C")


    #C0362
    ChrTalk(
        0xF,
        (
            "我们这里人手不足，\x01",
            "管理上难免存在疏漏。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xF,
        (
            "看来果然得考虑\x01",
            "将管理费也加入预算了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D84")

    Return()

    # Function_15_5BC4 end

    def Function_16_5D85(): pass

    label("Function_16_5D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E6B")

    #C0364
    ChrTalk(
        0xF,
        (
            "这个图书馆的地下书库里，\x01",
            "保存有大量的古代书籍\x01",
            "和未整理的资料。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xF,
        (
            "……时不时下去翻翻，\x01",
            "偶尔就会找到很稀有的书，\x01",
            "那时就会感到十分幸福。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0366
    ChrTalk(
        0x101,
        (
            "#0000F（叔叔还真是\x01",
            "  很喜欢书啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5EE3")

    label("loc_5E6B")


    #C0367
    ChrTalk(
        0xF,
        (
            "地下书库里的书籍\x01",
            "都没能来得及办理公开手续，\x01",
            "所以一直都没有对外公开……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xF,
        "对喜欢书的人来说，那里就像是乐园一样。\x02",
    )

    CloseMessageWindow()

    label("loc_5EE3")

    Return()

    # Function_16_5D85 end

    def Function_17_5EE4(): pass

    label("Function_17_5EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FA6")

    #C0369
    ChrTalk(
        0xF,
        (
            "这个图书馆只允许\x01",
            "每个人借三本书。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xF,
        (
            "因为人手不够，\x01",
            "如果大家借书过多的话，\x01",
            "我们就会来不及整理归还的图书。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xF,
        (
            "嗯，要是能允许每个人借五本书的话，\x01",
            "对大家来说就方便多了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5FFA")

    label("loc_5FA6")


    #C0372
    ChrTalk(
        0xF,
        (
            "这个图书馆的\x01",
            "人手严重不足。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xF,
        (
            "要是人手再多点的话，\x01",
            "就能更好的为大家服务了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FFA")

    Return()

    # Function_17_5EE4 end

    def Function_18_5FFB(): pass

    label("Function_18_5FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60FD")

    #C0374
    ChrTalk(
        0xF,
        "琪雅非常了不起哦。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xF,
        (
            "借回去的书\x01",
            "一下子就读完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        (
            "#0100F嗯，那孩子\x01",
            "好像真的很喜欢书。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xF,
        (
            "呵呵，看到又多了一个喜欢书的同道中人，\x01",
            "我也很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xF,
        (
            "欢迎你们再来借书哦，\x01",
            "我会准备几本精彩作品的。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x103,
        "#0200F嗯，我想她会很开心的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_618C")

    label("loc_60FD")


    #C0380
    ChrTalk(
        0xF,
        "琪雅非常了不起哦。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xF,
        (
            "将来或许能继承我的衣钵，\x01",
            "成为一名图书管理员呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#0012F啊哈哈哈哈……\x01",
            "（看来叔叔已经完全\x01",
            "  喜欢上琪雅了啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_618C")

    Return()

    # Function_18_5FFB end

    def Function_19_618D(): pass

    label("Function_19_618D")


    #C0383
    ChrTalk(
        0xF,
        (
            "听说港湾公园那边\x01",
            "发生了事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xF,
        (
            "唔，那附近明明\x01",
            "是条商业街。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xF,
        "怎么一大早就听到了这么危险的事件。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_19_618D end

    def Function_20_61FA(): pass

    label("Function_20_61FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6311")

    #C0386
    ChrTalk(
        0xF,
        (
            "以前，盖伊还是警察的时候，\x01",
            "他好像每天都很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xF,
        (
            "当他还是个新人时，\x01",
            "就在餐桌上兴奋地跟我们说过，\x01",
            "他遇到了一个很合得来的搭档。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xF,
        (
            "距离那时候\x01",
            "才刚刚过去不到十年……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xF,
        (
            "但盖伊、塞茜尔还有罗伊德……\x01",
            "完全物是人非了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        "#0008F……………是啊………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6363")

    label("loc_6311")


    #C0391
    ChrTalk(
        0xF,
        (
            "哈哈，抱歉啊，\x01",
            "不自觉就感伤起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xF,
        (
            "好像是被你阿姨\x01",
            "传染得多愁善感了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6363")

    Return()

    # Function_20_61FA end

    def Function_21_6364(): pass

    label("Function_21_6364")


    #C0393
    ChrTalk(
        0xF,
        (
            "太阳快下山了啊……\x01",
            "图书馆也快要闭馆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xF,
        (
            "罗伊德，回去的时候\x01",
            "别落下东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xF,
        "明天再见。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63F2")

    #C0396
    ChrTalk(
        0x101,
        "#0000F嗯，叔叔您也辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_63F2")

    SetScenarioFlags(0x0, 5)
    Return()

    # Function_21_6364 end

    def Function_22_63F6(): pass

    label("Function_22_63F6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_648A")
    Jump("loc_64D4")

    label("loc_648A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64AA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_64D4")

    label("loc_64AA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64CA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_64D4")

    label("loc_64CA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64D4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_65D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_658D")

    #C0397
    ChrTalk(
        0xFE,
        (
            "……我有了个新发现。\x01",
            "只要来图书馆，\x01",
            "工作就会进展得很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "安静的气氛可以令人精神集中，\x01",
            "旁边也没有唠叨的上司。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_65D3")

    label("loc_658D")


    #C0399
    ChrTalk(
        0xFE,
        (
            "没想到图书馆\x01",
            "竟然还有这种功效。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "人少的地方\x01",
            "对我来说正合适。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65D3")

    Jump("loc_67C6")

    label("loc_65D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_662F")
    SetChrSubChip(0xFE, 0x0)

    #C0401
    ChrTalk(
        0xFE,
        "既不是这样，也不是那样……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "嗯，这里果然\x01",
            "还是该这么办吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67C6")

    label("loc_662F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_66E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_668C")

    #C0403
    ChrTalk(
        0xFE,
        "（唰唰唰……）\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "我可没有\x01",
            "玩乐的闲工夫。\x01",
            "工作一大堆啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_66E2")

    label("loc_668C")


    #C0405
    ChrTalk(
        0xFE,
        (
            "（唰唰唰……）\x01",
            "必须得认真工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "要是书面材料提交晚了，\x01",
            "就会没法制作预算的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66E2")

    Jump("loc_67C6")

    label("loc_66E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_67BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_677D")

    #C0407
    ChrTalk(
        0xFE,
        (
            "市政厅那边都忙成一锅粥了。\x01",
            "在那里我没办法集中精神，\x01",
            "所以就把工作带来这里做了。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "因为一个星期后\x01",
            "就是预算会议了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_67B8")

    label("loc_677D")


    #C0409
    ChrTalk(
        0xFE,
        (
            "呵呵，我为了工作\x01",
            "还特意换了办公地点，实在是太认真了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67B8")

    Jump("loc_67C6")

    label("loc_67BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_67C6")

    label("loc_67C6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_63F6 end

    def Function_23_67CE(): pass

    label("Function_23_67CE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6862")
    Jump("loc_68AC")

    label("loc_6862")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6882")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68AC")

    label("loc_6882")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68A2")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68AC")

    label("loc_68A2")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68AC")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7171")
    EventBegin(0x0)
    Fade(500)
    OP_68(29400, 5020, -14320, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18590, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, 29930, 4030, -13780, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_694C")
    SetChrPos(0x102, 28660, 4030, -13530, 135)
    Jump("loc_6993")

    label("loc_694C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6972")
    SetChrPos(0x103, 28660, 4030, -13530, 135)
    Jump("loc_6993")

    label("loc_6972")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6993")
    SetChrPos(0x104, 28660, 4030, -13530, 135)

    label("loc_6993")

    SetChrPos(0x153, 27220, 4030, -14020, 135)
    SetChrSubChip(0x11, 0x2)
    OP_0D()

    #C0410
    ChrTalk(
        0x11,
        "#2905F#11P啊，好巧啊。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        "#0005F玛丽亚贝尔小姐……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A2C")

    #C0412
    ChrTalk(
        0x102,
        (
            "#0102F#5P贝尔……\x01",
            "难得在这种地方见到你呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_6A2C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A69")

    #C0413
    ChrTalk(
        0x103,
        (
            "#0202F#5P难得在这种地方\x01",
            "遇见您呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_6A69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AA7")

    #C0414
    ChrTalk(
        0x104,
        (
            "#0305F#5P哦哦。\x01",
            "难得在这种地方看到你啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AA7")


    #C0415
    ChrTalk(
        0x11,
        (
            "#2904F呵呵，偶尔有假期时，\x01",
            "我就会来这里坐坐。\x02\x03",

            "因为图书馆里有着\x01",
            "导力网络远远无法企及的知识……\x02\x03",

            "#2902F所以没理由不好好利用啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        "#0012F真、真是让人受益匪浅。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BB4")

    #C0417
    ChrTalk(
        0x102,
        (
            "#0104F#5P呵呵……\x01",
            "你其实是很爱学习的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x11,
        "#2904F哎呀，艾莉你不也一样吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C2A")

    label("loc_6BB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BF9")

    #C0419
    ChrTalk(
        0x103,
        (
            "#0204F#5P……原来如此。\x01",
            "确实有一定的道理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C2A")

    label("loc_6BF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C2A")

    #C0420
    ChrTalk(
        0x104,
        "#0309F#5P哈……佩服佩服啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6C2A")

    SetChrSubChip(0x11, 0x0)
    Sleep(300)

    #C0421
    ChrTalk(
        0x11,
        "#2900F……嗯，先不谈这个。\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x153,
        (
            "#1101F（盯……）\x02\x03",

            "#1110F那个那个，罗伊德。\x01",
            "这位大姐姐也是你们的朋友吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CA3():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CA3)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CCA")
    TurnDirection(0x102, 0x153, 500)
    Jump("loc_6CFD")

    label("loc_6CCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CE6")
    TurnDirection(0x103, 0x153, 500)
    Jump("loc_6CFD")

    label("loc_6CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CFD")
    TurnDirection(0x104, 0x153, 500)

    label("loc_6CFD")


    #C0423
    ChrTalk(
        0x101,
        "#0002F#11P啊……算是吧。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x11,
        (
            "#2904F#11P呵呵，事情的经过我已经知道了哦。\x02\x03",

            "#2902F这孩子就是原本计划要\x01",
            "展出拍卖的『人偶』吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6DB9():
        TurnDirection(0x101, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DB9)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DE6")

    def lambda_6DD9():
        TurnDirection(0x102, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6DD9)
    Jump("loc_6E25")

    label("loc_6DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E08")

    def lambda_6DFB():
        TurnDirection(0x103, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DFB)
    Jump("loc_6E25")

    label("loc_6E08")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E25")

    def lambda_6E1D():
        TurnDirection(0x104, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E1D)

    label("loc_6E25")

    Sleep(200)

    #C0425
    ChrTalk(
        0x101,
        "#0011F什么……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E7A")

    #C0426
    ChrTalk(
        0x102,
        "#0101F#5P贝尔，你为什么会知道……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EE1")

    label("loc_6E7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EB2")

    #C0427
    ChrTalk(
        0x103,
        "#0205F#5P……您为何会知道……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EE1")

    label("loc_6EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EE1")

    #C0428
    ChrTalk(
        0x104,
        "#0305F#5P你怎么会知道……\x02",
    )

    CloseMessageWindow()

    label("loc_6EE1")


    #C0429
    ChrTalk(
        0x11,
        (
            "#2906F唉……\x01",
            "都引起了那么大的骚乱，\x01",
            "要是不知道就奇怪了。\x02\x03",

            "#2902F当时我也远远望到了\x01",
            "你们逃出宅邸时的样子。\x02\x03",

            "#2904F再把这一周以来得到的消息综合分析一下，\x01",
            "便很容易推测出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x101,
        (
            "#0006F这、这样啊……\x02\x03",

            "#0001F……那个，玛丽亚贝尔小姐。\x01",
            "这件事还请务必──\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x11,
        (
            "#2903F我知道啦。\x02\x03",

            "#2902F话说回来，我当时正好在场，\x01",
            "或许也是因为某种缘分吧。\x02\x03",

            "如果你们有什么苦恼的事，\x01",
            "不用客气，可以尽管来找我帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x101,
        (
            "#0004F玛丽亚贝尔小姐……\x01",
            "实在非常感谢您。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70D3")

    #C0433
    ChrTalk(
        0x102,
        "#0102F#5P贝尔……真的谢谢你。\x02",
    )

    CloseMessageWindow()
    Jump("loc_713A")

    label("loc_70D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7109")

    #C0434
    ChrTalk(
        0x103,
        "#0204F#5P……感谢您的关心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_713A")

    label("loc_7109")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_713A")

    #C0435
    ChrTalk(
        0x104,
        "#0304F#5P哎，真是谢谢你啊。\x02",
    )

    CloseMessageWindow()

    label("loc_713A")


    #C0436
    ChrTalk(
        0x153,
        "#1105F？？？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 29930, 4030, -13780, 180)
    SetChrSubChip(0x11, 0x0)
    SetScenarioFlags(0xB4, 7)
    ClearChrFlags(0x8, 0x80)
    EventEnd(0x5)
    Jump("loc_75E0")

    label("loc_7171")

    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x153, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7205")
    Jump("loc_724F")

    label("loc_7205")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7225")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_724F")

    label("loc_7225")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7245")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_724F")

    label("loc_7245")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_724F")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7423")

    #C0437
    ChrTalk(
        0x153,
        (
            "#1106F嗯～还是算了吧。\x02\x03",

            "#1110F琪雅想和罗伊德他们\x01",
            "待在一起呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x11,
        "#2905F啊，这可真是遗憾啊。\x02",
    )

    CloseMessageWindow()
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x101, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7374")
    Jump("loc_73BE")

    label("loc_7374")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7394")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73BE")

    label("loc_7394")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73B4")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73BE")

    label("loc_73B4")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73BE")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Sleep(300)

    #C0439
    ChrTalk(
        0x11,
        "#2910F（瞪……）\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x101,
        "#0011F（是、是我的错吗！？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_75DC")

    label("loc_7423")


    #C0441
    ChrTalk(
        0x11,
        (
            "#2902F呵呵，不过……\x02\x03",

            "真的比罗赞贝尔克的\x01",
            "人偶可爱多了。\x02\x03",

            "#2909F你是叫做琪雅吗？\x01",
            "要不要来姐姐\x01",
            "家玩啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x153,
        "#1105F罗伊德他们也一起去吗？\x02",
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x11,
        (
            "#2901F不，至少\x01",
            "罗伊德是不会去的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0444
    ChrTalk(
        0x101,
        "#0006F（又被莫名其妙地敌视了……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_756C")

    #C0445
    ChrTalk(
        0x102,
        "#0106F#5P（灾难啊……罗伊德。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D9")

    label("loc_756C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_75A2")

    #C0446
    ChrTalk(
        0x103,
        "#0204F#5P（真是令人同情。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_75D9")

    label("loc_75A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_75D9")

    #C0447
    ChrTalk(
        0x104,
        "#0309F#5P（哇哈哈，大快人心啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_75D9")

    SetScenarioFlags(0x1, 0)

    label("loc_75DC")

    SetChrSubChip(0x11, 0x0)

    label("loc_75E0")

    SetChrSubChip(0x11, 0x0)
    TalkEnd(0x11)
    Return()

    # Function_23_67CE end

    def Function_24_75E8(): pass

    label("Function_24_75E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 1)), scpexpr(EXPR_END)), "loc_7694")

    #C0448
    ChrTalk(
        0x12,
        (
            "#3504F好了，帝国的工作\x01",
            "都已经完成了。\x02\x03",

            "#3500F要不要在克洛斯贝尔\x01",
            "多放松几天呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        (
            "#0003F（……这人真是令人琢磨不透……\x01",
            "  他到底知道些什么呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A5A")

    label("loc_7694")

    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x0, 300)

    #C0450
    ChrTalk(
        0x12,
        (
            "#3500F嗯，你们也来看书吗？\x02\x03",

            "#3509F哎呀，真是好巧啊。\x01",
            "遇到了同样喜欢读书的朋友，我也很高兴哦¤\x02",
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

    #C0451
    ChrTalk(
        0x101,
        (
            "#0006F那、那个……\x01",
            "都不知道该说什么才好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x103,
        (
            "#0203F不管怎么想，\x01",
            "他肯定都不是来读书的……\x01",
            "而且还故意装出一副轻松自然的样子……\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x104,
        (
            "#0306F（……算了吧，要是跟他认真起来的话，\x01",
            "  脑子会坏掉的。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 2)), scpexpr(EXPR_END)), "loc_7A0C")

    #C0454
    ChrTalk(
        0x102,
        (
            "#0105F不过，雷克特先生，\x01",
            "您不是有事\x01",
            "要回帝国吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x12,
        (
            "#3505F啊，是啊……\x02\x03",

            "#3500F虽然说是回帝国，\x01",
            "但也用不了多长时间。\x02\x03",

            "就在贝尔加德门附近而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0456
    ChrTalk(
        0x101,
        "#0005F（……贝尔加德门附近？）\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        "#0105F（莫非是……『卡雷利亚要塞』！？）\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        (
            "#0305F（也太诡异了吧……\x01",
            "  那可是帝国最重要的一个据点啊！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x103,
        (
            "#0211F（不像是普通平民\x01",
            "  会去的地方啊。\x01",
            "  他到底是什么人呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A50")

    label("loc_7A0C")


    #C0460
    ChrTalk(
        0x102,
        (
            "#0106F（……我觉得…………\x01",
            "  还是不要对他\x01",
            "  太认真比较好……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A50")

    OP_93(0x12, 0x5A, 0x0)
    SetScenarioFlags(0xEF, 1)

    label("loc_7A5A")

    TalkEnd(0xFE)
    Return()

    # Function_24_75E8 end

    def Function_25_7A5E(): pass

    label("Function_25_7A5E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7B27")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0461
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "     　～　本月新刊　～\x01",
            "　玛尔克与森林深处的魔女·下\x01\x01",
            "　放置于一楼书架中。\x01",
            "  有兴趣的客人请前去借阅。\x01",
            "　★该书十分抢手，\x01",
            "　　想借书的客人\x01",
            "　　请尽快行动！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_7DAC")

    label("loc_7B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7B77")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0462
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　～　本月新刊　～\x01",
            "　　　　 准备中\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_7DAC")

    label("loc_7B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7BFE")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0463
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　 ～　本月新刊　～\x01",
            "　　　圣女与白狼·下\x01\x01",
            "　放置于一楼书架中。\x01",
            "　有兴趣的客人请前去借阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_7DAC")

    label("loc_7BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7CA2")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0464
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "     　～　本月新刊　～\x01",
            "　玛尔克与森林深处的魔女·中\x01",
            "　　　　季刊·垂涎\x01\x01",
            "　放置于一楼书架中。\x01",
            "　有兴趣的客人请前去借阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_7DAC")

    label("loc_7CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7D29")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0465
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　 ～　本月新刊　～\x01",
            "　　　圣女与白狼·上\x01\x01",
            "　放置于一楼书架中。\x01",
            "　有兴趣的客人请前去借阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_7DAC")

    label("loc_7D29")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0466
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "     　～　本月新刊　～\x01",
            "　玛尔克与森林深处的魔女·上\x01\x01",
            "　放置于一楼书架中。\x01",
            "　有兴趣的客人请前去借阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_7DAC")

    TalkEnd(0xFF)
    Return()

    # Function_25_7A5E end

    def Function_26_7DB0(): pass

    label("Function_26_7DB0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0467
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上有《玛尔克与森林深处的魔女》一书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7E8B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读上卷】\x01",      # 0
            "【阅读中卷】\x01",      # 1
            "【阅读下卷】\x01",      # 2
            "【放弃】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E5E")
    UseItem(0x2D6, 0xFF)

    label("loc_7E5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E72")
    UseItem(0x2DD, 0xFF)

    label("loc_7E72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E86")
    UseItem(0x2DE, 0xFF)

    label("loc_7E86")

    Jump("loc_7F52")

    label("loc_7E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7F06")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读上卷】\x01",      # 0
            "【阅读中卷】\x01",      # 1
            "【放弃】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EED")
    UseItem(0x2D6, 0xFF)

    label("loc_7EED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F01")
    UseItem(0x2DD, 0xFF)

    label("loc_7F01")

    Jump("loc_7F52")

    label("loc_7F06")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读上卷】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F52")
    UseItem(0x2D6, 0xFF)

    label("loc_7F52")

    TalkEnd(0xFF)
    Return()

    # Function_26_7DB0 end

    def Function_27_7F56(): pass

    label("Function_27_7F56")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0468
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上有《季刊·垂涎》一书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读此书】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8041")
    UseItem(0x2DC, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8041")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0469
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '溜滑杏仁豆腐'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法写在书里。\x02",
        )
    )

    CloseMessageWindow()

    #A0470
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '溜滑杏仁豆腐'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做饭已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x12)

    label("loc_8041")

    TalkEnd(0xFF)
    Return()

    # Function_27_7F56 end

    def Function_28_8045(): pass

    label("Function_28_8045")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0471
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书柜上有《改变大陆的美人们》一书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读此书】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80C0")
    UseItem(0x2D7, 0xFF)

    label("loc_80C0")

    TalkEnd(0xFF)
    Return()

    # Function_28_8045 end

    def Function_29_80C4(): pass

    label("Function_29_80C4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0472
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书柜上有《有效利用五分钟的零散时间》一书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读此书】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8147")
    UseItem(0x2D8, 0xFF)

    label("loc_8147")

    TalkEnd(0xFF)
    Return()

    # Function_29_80C4 end

    def Function_30_814B(): pass

    label("Function_30_814B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0473
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书柜上有《铁道爱好者的推荐》一书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读此书】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C6")
    UseItem(0x2D5, 0xFF)

    label("loc_81C6")

    TalkEnd(0xFF)
    Return()

    # Function_30_814B end

    def Function_31_81CA(): pass

    label("Function_31_81CA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0474
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书柜上有《克洛斯贝尔怪谈全集》一书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读此书】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8247")
    UseItem(0x2D9, 0xFF)

    label("loc_8247")

    TalkEnd(0xFF)
    Return()

    # Function_31_81CA end

    def Function_32_824B(): pass

    label("Function_32_824B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0475
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书柜上有《圣女与白狼》一书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_82F9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读上卷】\x01",      # 0
            "【阅读下卷】\x01",      # 1
            "【放弃】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82E0")
    UseItem(0x2DF, 0xFF)

    label("loc_82E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82F4")
    UseItem(0x2E0, 0xFF)

    label("loc_82F4")

    Jump("loc_8345")

    label("loc_82F9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读上卷】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8345")
    UseItem(0x2DF, 0xFF)

    label("loc_8345")

    TalkEnd(0xFF)
    Return()

    # Function_32_824B end

    def Function_33_8349(): pass

    label("Function_33_8349")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0476
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书柜上有《彩虹·Ｆａｎｂｏｏｋ》一书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读此书】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C8")
    UseItem(0x2DA, 0xFF)

    label("loc_83C8")

    TalkEnd(0xFF)
    Return()

    # Function_33_8349 end

    def Function_34_83CC(): pass

    label("Function_34_83CC")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_83E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_874A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 壹 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【ＩＢＣ】\x01",      # 0
            "【ＺＣＦ】\x01",      # 1
            "【放弃】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85B7")
    SetChrName("")
    MenuTitle(-1, 25, 0, "ＩＢＣ（International Bank of Crossbell）")
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0477
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『克洛斯贝尔国际银行』的简称。\x01",
            "这所巨大银行管理、运用着\x01",
            "从大陆全境汇集而来的庞大资产。\x01",
            "不仅限于克洛斯贝尔，IBC也\x01",
            "常年支撑着国际金融、经济市场。\x02\x03",

            "除了投资活动和金融商品的开发，\x01",
            "其业务还涉及到主题公园运营等领域，\x01",
            "并且也积极为爱普斯泰恩财团的\x01",
            "『导力网络计划』提供运作资金。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_85B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8745")
    MenuTitle(-1, 25, 0, "ＺＣＦ（Zeiss Central Factory）")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0478
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『蔡斯中央工房』的简称。\x01",
            "ＺＣＦ位于利贝尔王国的蔡斯市，\x01",
            "由导力器的发明者——爱普斯泰恩博士的\x01",
            "直系弟子Ａ·拉塞尔博士，\x01",
            "与蔡斯钟表师工会联合创办，\x01",
            "其前身为『蔡斯技术工房』。\x02\x03",

            "ＺＣＦ成功率先开发了导力飞行船，\x01",
            "是大陆上首屈一指的导力器制造商，\x01",
            "近年，它更是成功制造了\x01",
            "利贝尔王国军的高速巡洋舰『埃尔赛尤』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8745")

    Jump("loc_83E3")

    label("loc_874A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_34_83CC end

    def Function_35_8757(): pass

    label("Function_35_8757")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_876E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F5A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 贰 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【彩虹剧团】\x01",              # 0
            "【亚尔特利亚法典国】\x01",      # 1
            "【乌尔努公司】\x01",            # 2
            "【埃雷波尼亚帝国】\x01",        # 3
            "【爱普斯泰恩财团】\x01",        # 4
            "【放弃】\x01",                  # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_891E")
    MenuTitle(-1, 25, 0, "彩虹剧团")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0479
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于克洛斯贝尔自治州，\x01",
            "是世界著名的剧团。\x02\x03",

            "其技巧高超的表演\x01",
            "与激情华丽的舞台，\x01",
            "让许多观众如痴如醉。\x02\x03",

            "特别是被誉为『炎之舞姬』的\x01",
            "现任招牌女演员伊莉娅·普拉提耶\x01",
            "受到了极大欢迎，\x01",
            "其狂热追随者遍布周边各国。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_891E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A7D")
    MenuTitle(-1, 25, 0, "亚尔特利亚法典国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0480
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "亚尔特利亚法典国是七耀教会的总部所在地。\x01",
            "这座城国位于塞姆里亚大陆的中心地区，\x01",
            "并作为全大陆的信徒与宗教相关人员\x01",
            "齐聚的圣地而声名远扬。\x02\x03",

            "其中设有全权负责祭祀仪式相关事宜的『典礼省』，\x01",
            "据传负责管理女神圣物的『封圣省』，\x01",
            "以及负责城市保卫任务的『僧兵厅』等\x01",
            "各种各样的组织。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8A7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BE2")
    MenuTitle(-1, 25, 0, "乌尔努公司")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0481
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总部位于卡尔瓦德共和国，\x01",
            "是一家巨大的综合技术制造商。\x02\x03",

            "与埃雷波尼亚帝国的莱恩福尔特公司\x01",
            "同为武器和兵器开发领域的两大老牌公司，\x01",
            "但自从导力器出现后，\x01",
            "就开始着手研究和开发一切导力产品。\x02\x03",

            "其中在导力驱动车的领域，\x01",
            "以导力巴士为首，从家用车到特殊车辆的开发，\x01",
            "乌尔努公司都有着卓越的成绩。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DF0")
    MenuTitle(-1, 25, 0, "埃雷波尼亚帝国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0482
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于克洛斯贝尔自治州西部，\x01",
            "是一个以『黄金战马』为国徽的巨大帝国。\x01",
            "现任皇帝为尤肯特·莱泽·亚诺尔。\x02\x03",

            "该国家由大贵族支配，虽然体制陈旧，\x01",
            "但在被誉为『铁血宰相』——出身军队的\x01",
            "吉利亚斯·奥斯本宰相的推动下，\x01",
            "国土全境铺设了铁路，正逐渐向近代化发展。\x02\x03",

            "整个国家除了机械化的正规军之外，\x01",
            "还设有贵族的私人军队等，军事力量十分强大，\x01",
            "因此周边诸国都对其常年保持警戒。\x02\x03",

            "另外，皇帝之子——奥利维特皇子\x01",
            "去年帮助解决了利贝尔的异变事件，\x01",
            "这在帝国内引起了很大反响。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8DF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F55")
    MenuTitle(-1, 25, 0, "爱普斯泰恩财团")
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0483
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "继承了发明导力器的天才导力学者\x01",
            "Ｃ·爱普斯泰恩博士辉煌成就的财团。\x01",
            "在研究机关与制造商的领域中也有很强实力，\x01",
            "特别擅长通讯及情报处理等领域。\x02\x03",

            "另外，此财团是能够驱动魔法的\x01",
            "『战术导力器』的唯一开发制造商，\x01",
            "近年来，还在致力于研究开发\x01",
            "通讯及情报处理技术领域的尖端工程『导力网络计划』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F55")

    Jump("loc_876E")

    label("loc_8F5A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_35_8757 end

    def Function_36_8F67(): pass

    label("Function_36_8F67")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96DC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 叁 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【怪盗Ｂ】\x01",                # 0
            "【卡尔瓦德共和国】\x01",        # 1
            "【克洛斯贝尔自治州】\x01",      # 2
            "【结晶回路】\x01",              # 3
            "【古代遗物】\x01",              # 4
            "【放弃】\x01",                  # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91CF")
    MenuTitle(-1, 25, 0, "怪盗Ｂ")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0484
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "活动领域覆盖大陆全境，神出鬼没的大盗。\x01",
            "小到宝石，大至导力战车，\x01",
            "无论所有者是国家还是个人，都可以成功盗走，\x01",
            "据说由于其手法华丽，甚至获得了\x01",
            "一部分狂热的崇拜者。\x02\x03",

            "他总是将别有寓意的信息送至各地，\x01",
            "虽然有人见到过他戴着面具，身披白色斗篷的样子，\x01",
            "但其真实面目一直是个谜。\x01",
            "近年来，他号称要进行『美的解放活动』，\x01",
            "在埃雷波尼亚帝国犯下了一系列\x01",
            "华丽并且无法侦破的罪行，再次引起了新话题。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9322")
    MenuTitle(-1, 25, 0, "卡尔瓦德共和国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0485
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于克洛斯贝尔自治州东部，\x01",
            "在百年前便推行了民主化。\x01",
            "现任国家元首是洛克史密斯总统。\x02\x03",

            "该国家幅员辽阔，\x01",
            "因有着许多东方移民，\x01",
            "所以文化背景也丰富多彩。\x02\x03",

            "虽然在《互不侵犯条约》签订之后，态度便一直保持低调，\x01",
            "但在历史上，该国家与埃雷波尼亚帝国之间\x01",
            "曾发生过数次冲突。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9322")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9476")
    MenuTitle(-1, 25, 0, "克洛斯贝尔自治州")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0486
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于塞姆里亚大陆西部。\x01",
            "处在埃雷波尼亚帝国\x01",
            "和卡尔瓦德共和国这两个大国之间，\x01",
            "曾经是激烈领土争端的对象，\x01",
            "但七十年前作为自治州成立了。\x02\x03",

            "现在，其中心克洛斯贝尔市已经发展为\x01",
            "大陆首屈一指的巨大贸易都市，\x01",
            "以及连接帝国和共和国的横断大陆铁道\x01",
            "和国际定期飞行船的中转站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9476")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9559")
    MenuTitle(-1, 25, 0, "结晶回路")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0487
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "用七耀石的碎片『耀晶片』精制加工而成，\x01",
            "拥有结晶构造的回路。\x02\x03",

            "是既能作为能量源使用，\x01",
            "又可以引发各种现象的装置，\x01",
            "但若未设置于导力器内部，\x01",
            "便发挥不出功效。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9559")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96D7")
    MenuTitle(-1, 25, 0, "古代遗物")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0488
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "与导力器同样都是利用导力运作，\x01",
            "但运转原理不尽相同，是古代文明的导力器。\x02\x03",

            "据说是『古代塞姆里亚文明』时代\x01",
            "的产物，仅凭现代技术\x01",
            "是无法对其进行解析的。\x02\x03",

            "古代遗物在大陆各地的遗迹中都\x01",
            "有过少量发现，其中有不少遗物\x01",
            "甚至拥有超越常理的强大力量。\x02\x03",

            "因此七耀教会将古代遗物\x01",
            "定义为『女神过早的馈赠』，\x01",
            "并负责将其回收管理。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96D7")

    Jump("loc_8F7E")

    label("loc_96DC")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_36_8F67 end

    def Function_37_96E9(): pass

    label("Function_37_96E9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9700")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99BC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 肆 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【七耀教会】\x01",      # 0
            "【七耀石】\x01",        # 1
            "【放弃】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9882")
    MenuTitle(-1, 25, 0, "七耀教会")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0489
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "信奉在塞姆里亚大陆上拥有最多信徒的\x01",
            "『空之女神爱德丝』的宗教组织。\x01",
            "其总部位于亚尔特利亚法典国。\x02\x03",

            "自导力革命之后，虽然影响力略有降低，\x01",
            "但目前在大陆上仍然拥有很强的影响力，\x01",
            "该组织一般通过知识、教育、医疗等领域\x01",
            "来启蒙民众。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9882")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99B7")
    MenuTitle(-1, 25, 0, "七耀石")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0490
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "散布于全大陆的七种珍贵宝石。\x01",
            "该宝石自古以来\x01",
            "就被视为某种神秘的象征而极其珍贵。\x02\x03",

            "近代出现了一种技术，\x01",
            "能够将体积过小，无法打磨成宝石的七耀石碎片\x01",
            "『耀晶片』进行精制·加工，制成结晶回路，\x01",
            "这项发明使七耀石资源的重要性\x01",
            "在大陆各国间陡然增大。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_99B7")

    Jump("loc_9700")

    label("loc_99BC")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_37_96E9 end

    def Function_38_99C9(): pass

    label("Function_38_99C9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_99E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A035")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 伍 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【大崩坏】\x01",        # 0
            "【钓公师团】\x01",      # 1
            "【导力革命】\x01",      # 2
            "【导力器】\x01",        # 3
            "【放弃】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B3C")
    MenuTitle(-1, 25, 0, "大崩坏")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0491
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "指发生于一千两百年前，古代塞姆里亚文明\x01",
            "的毁灭。有资料称它是由天地异变所引发的，\x01",
            "但具体原因仍然不明。\x02\x03",

            "『大崩坏』导致文明消失之后，\x01",
            "人们度过了漫长的『黑暗时代』。\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C98")
    MenuTitle(-1, 25, 0, "钓公师团")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0492
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旨在普及钓鱼文化，\x01",
            "是垂钓界的专业组织。\x01",
            "该组织由一位原为贵族的钓鱼爱好者\x01",
            "Ｈ·费瑟尔先生所发起，\x01",
            "其总部位于利贝尔王国的格兰赛尔市。\x02\x03",

            "主要活动为进行钓鱼点的探访、调查、开发，\x01",
            "并致力于发掘培养新一代钓师，\x01",
            "另外，钓公师团近年也开始着手开发钓具、鱼饵等，\x01",
            "其活动领域正在逐年扩大。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EBA")
    MenuTitle(-1, 25, 0, "导力革命")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0493
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大约在五十年前，\x01",
            "导力器的发明\x01",
            "引发了全大陆的技术革新。\x02\x03",

            "虽然导力器是划时代的发明，\x01",
            "但当时人们却对其持怀疑态度，\x01",
            "直到爱普斯泰恩财团的导力通讯器及\x01",
            "ＺＣＦ的导力飞行船问世后，\x01",
            "其实用性才被全大陆所承认。\x02\x03",

            "现在，从取暖设备与照明设备等日用品，\x01",
            "到列车、飞行船、战车及大炮等兵器，\x01",
            "所有设备都已经得到导力化，\x01",
            "导力器对人们来说，\x01",
            "已经变得必不可少。\x02\x03",

            "近几年，随着导力机械的小型化，\x01",
            "乌尔努公司和莱恩福尔特公司对\x01",
            "高性能导力驱动车的开发也在不断进步，\x01",
            "其产品已经开始在一般民众间普及开来。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9EBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A030")
    MenuTitle(-1, 25, 0, "导力器")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0494
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由Ｃ·爱普斯泰恩博士发明，\x01",
            "通过引出七耀石中的导力，\x01",
            "来引发种种现象的机械的总称。\x02\x03",

            "导力器利用其内在构造及齿轮运转，\x01",
            "使由七耀石加工而来的结晶回路互相干涉，\x01",
            "从而引发无数种现象。\x02\x03",

            "导力器的实用性之强，\x01",
            "不仅在于能引发各种现象，并且『随时间流逝内部的\x01",
            "导力会逐渐恢复』，从经济效率上看远远\x01",
            "高于外燃、内燃机械。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A030")

    Jump("loc_99E0")

    label("loc_A035")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_38_99C9 end

    def Function_39_A042(): pass

    label("Function_39_A042")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A059")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A440")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 陆 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【导力魔法】\x01",          # 0
            "【导力网络计划】\x01",      # 1
            "【东方人街】\x01",          # 2
            "【放弃】\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1CF")
    MenuTitle(-1, 25, 0, "导力魔法")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0495
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通过将结晶回路装入爱普斯泰恩财团\x01",
            "特别设计的『战术导力器』中，\x01",
            "从而得以发动的『魔法』。\x02\x03",

            "一般被称为『导力魔法』，\x01",
            "只要经过训练，每个人都能使用，\x01",
            "因此广泛普及于军队、警察、游击士协会等组织。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A30F")
    MenuTitle(-1, 25, 0, "导力网络计划")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0496
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "爱普斯泰恩财团正在开发研究的，\x01",
            "具有革命性意义的信息网络计划。\x01",
            "此计划以导力缆线连接各终端，\x01",
            "让交换以及处理大量信息成为可能。\x02\x03",

            "虽然原本与利贝尔的ＺＣＦ\x01",
            "共同推进此计划，但现在\x01",
            "由于接受了IBC的资金援助，所以开始正\x01",
            "式在克洛斯贝尔市进行了导入实验。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A30F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A43B")
    MenuTitle(-1, 25, 0, "东方人街")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0497
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于卡尔瓦德共和国，\x01",
            "是东方移民所筑起的大规模街道。\x01",
            "东方人街汇聚了各种文化、人种、物资，\x01",
            "被誉为『东西文化的交叉点』。\x02\x03",

            "充满异国情调的建筑物鳞次栉比，\x01",
            "是享有盛名的观光地，但遗憾的是\x01",
            "据传闻说，东方人街中也存在庞大的黑手党组织。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A43B")

    Jump("loc_A059")

    label("loc_A440")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_39_A042 end

    def Function_40_A44D(): pass

    label("Function_40_A44D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A464")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A876")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 柒 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【百日战役】\x01",          # 0
            "【互不侵犯条约】\x01",      # 1
            "【放弃】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6D5")
    MenuTitle(-1, 25, 0, "百日战役")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0498
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "百日战役是七耀历１１９２年，埃雷波尼亚帝国\x01",
            "向利贝尔王国发动的一场侵略战争。\x01",
            "因为从帝国宣战开始，到七耀教会\x01",
            "协调双方结束战争，\x01",
            "大约进行了一百天，\x01",
            "所以被称为『百日战役』。\x02\x03",

            "当时利贝尔处于绝对劣势，\x01",
            "领土大半都已被帝国军队占领，\x01",
            "但在使用当时最先进的警备飞艇\x01",
            "发起闪电般的反击战后，\x01",
            "战况瞬间便被颠覆。\x02\x03",

            "关于开战理由，\x01",
            "因为两国都对此保持沉默，\x01",
            "所以至今仍然是个迷。\x01",
            "战争结束之后，帝国政府将其称为\x01",
            "『由不幸的误会而产生的错误』，\x01",
            "并向利贝尔发表了正式的谢罪声明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A6D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A871")
    MenuTitle(-1, 25, 0, "互不侵犯条约")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0499
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "互不侵犯条约是七耀历１２０２年，利贝尔王国、\x01",
            "埃雷波尼亚帝国和卡尔瓦德共和国\x01",
            "三国间签订的一则国际条约。\x01",
            "该条约由利贝尔的艾莉茜雅女王发起，\x01",
            "在该国的艾尔贝离宫签订。\x02\x03",

            "该条约虽然不具备法律强制力，\x01",
            "但条约签订后，帝国和共和国便终止了\x01",
            "在克洛斯贝尔自治州近郊举行的\x01",
            "大规模军事演习，\x01",
            "使紧张的局势大为缓和，\x01",
            "可以说，此条约起到了立竿见影的效果。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A871")

    Jump("loc_A464")

    label("loc_A876")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_40_A44D end

    def Function_41_A883(): pass

    label("Function_41_A883")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A89A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC18")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 捌 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【米修拉姆】\x01",        # 0
            "【游击士协会】\x01",      # 1
            "【放弃】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA14")
    MenuTitle(-1, 25, 0, "米修拉姆")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0500
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "米修拉姆是位于艾尔姆湖东南边的的一处高级疗养地，\x01",
            "两年前，ＩＢＣ开始着手进行开发后，\x01",
            "此地便建成了度假酒店和主题公园等，\x01",
            "并成为大受欢迎的观光旅游地点。\x02\x03",

            "被称为『咪西』\x01",
            "的当地吉祥物，\x01",
            "也十分受市民和游客的欢迎。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC13")
    MenuTitle(-1, 25, 0, "游击士协会")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0501
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "为了保护地区和平与普通人的安全，\x01",
            "游击士们所成立的民间团体。  \x01",
            "由于协会在塞姆里亚大陆全境都设有分部，\x01",
            "所以影响力与发言力也不容小觑。\x02\x03",

            "协会的理念可以说是\x01",
            "以保护平民的安全为优先，\x01",
            "但相对的，为了不威胁到平民的安全，\x01",
            "所以协会无法行使对国家与政府权力者的\x01",
            "搜查权和逮捕权，这是其组织守则上的弱点之一。\x02\x03",

            "而且克洛斯贝尔分部所接到的国际性案件较多，\x01",
            "因此集中于此处的人才都尤其优秀，\x01",
            "其中，『风之剑圣』亚里欧斯·马克莱因\x01",
            "更是获得了市民的极大支持。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AC13")

    Jump("loc_A89A")

    label("loc_AC18")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_41_A883 end

    def Function_42_AC25(): pass

    label("Function_42_AC25")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AC3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B39C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 玖 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【莱恩福尔特公司】\x01",      # 0
            "【雷米菲利亚公国】\x01",      # 1
            "【列曼自治州】\x01",          # 2
            "【利贝尔王国】\x01",          # 3
            "【猎兵团】\x01",              # 4
            "【放弃】\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE25")
    MenuTitle(-1, 25, 0, "莱恩福尔特公司")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0502
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总部位于埃雷波尼亚帝国，\x01",
            "是一家巨大的综合技术制造商。\x01",
            "前身是专门制造使用火药的\x01",
            "大炮以及重型武器的兵器工房。\x02\x03",

            "自从导力器问世之后，\x01",
            "便转而制造导力枪与导力兵器，\x01",
            "并涉足导力列车与飞行船等领域，\x01",
            "最终发展为与卡尔瓦德共和国的『乌尔努公司』\x01",
            "齐名的，世界两大制造商之一。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AE25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFB4")
    MenuTitle(-1, 25, 0, "雷米菲利亚公国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0503
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雷米菲利亚公国位于塞姆里亚大陆北部。\x01",
            "虽然处于自然环境严酷的北方，\x01",
            "但有着茂密的森林与清澈的湖泊，\x01",
            "风光明媚、景色秀丽，\x01",
            "吸引了众多游客前来观光。\x02\x03",

            "雷米菲利亚公国同时也是著名的医疗发达国家，\x01",
            "集中了全大陆的顶尖医疗器械制造商，\x01",
            "并且培养了许多优秀的医生。\x01",
            "克洛斯贝尔自治州的圣乌尔斯拉医科大学\x01",
            "也是由雷米菲利亚公国协助设立的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AFB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0A4")
    MenuTitle(-1, 25, 0, "列曼自治州")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0504
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "列曼自治州位于塞姆里亚大陆中部。\x01",
            "不仅是爱普斯泰恩财团的总部所在地，\x01",
            "同时也是Ｃ·爱普斯泰恩博士的故乡。\x02\x03",

            "除此之外，在全大陆都设有分部的\x01",
            "游击士协会的总部也设于该国。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B0A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B292")
    MenuTitle(-1, 25, 0, "利贝尔王国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0505
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "利贝尔王国位于塞姆里亚大陆西南部。\x01",
            "自古以来就拥有丰富绚丽的自然风光，\x01",
            "现在，利贝尔王国在老女王艾莉茜雅Ⅱ世的治理下，\x01",
            "局势稳定，以和平著称。\x02\x03",

            "虽然与周边诸国相比，国力稍显逊色，\x01",
            "但凭借丰富的七耀石资源和先进的技术，\x01",
            "加上灵活的外交政策，\x01",
            "使其与各国建立了平等友好的关系。\x02\x03",

            "去年，在王国中央的瓦雷利亚湖上\x01",
            "出现了神秘的巨大物体（详情不明），\x01",
            "并使王国全境的导力全部停止运转，\x01",
            "所幸，此危机最后被军队和游击士协会\x01",
            "顺利解决了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0xBF, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B292")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B397")
    MenuTitle(-1, 25, 0, "猎兵团")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0506
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "指代大陆各国的佣兵部队中\x01",
            "最优秀的部队时所使用的称号。\x02\x03",

            "雇主可依据规模和目的与其灵活地订立合同，\x01",
            "再加上猎兵拥有着强大的战斗力，\x01",
            "因此常作为私人武装被雇佣，\x01",
            "但有的国家也明令禁止其在境内活动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B397")

    Jump("loc_AC3C")

    label("loc_B39C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_42_AC25 end

    def Function_43_B3A9(): pass

    label("Function_43_B3A9")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 800, 8440, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    OP_0D()

    #C0507
    ChrTalk(
        0x101,
        "#6P#0000F叔叔，您好。\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xF,
        (
            "#11P哦，是罗伊德啊，\x01",
            "欢迎欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xF,
        "#11P今天你们是来借书的吗？\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        (
            "#6P#0000F不，今天是因为工作而来的。\x02\x03",

            "您不是向特别任务支援科\x01",
            "提出了委托吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x102,
        (
            "#5P#0100F好像是……\x01",
            "回收超期未还的书籍。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xF,
        (
            "#11P哦，没错没错，\x01",
            "我确实提出了那样的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xF,
        (
            "#11P那我就开始说明\x01",
            "委托的内容了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x5, 0x1, 0x0)
    Call(0, 45)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B57A")
    Call(0, 46)

    label("loc_B57A")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_43_B3A9 end

    def Function_44_B58E(): pass

    label("Function_44_B58E")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 800, 8440, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    OP_0D()

    #C0514
    ChrTalk(
        0xF,
        (
            "#11P我确实提出了有关\x01",
            "回收超期未还书籍的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xF,
        (
            "#11P那我就开始说明\x01",
            "委托的内容了哦。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 45)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B67D")
    Call(0, 46)

    label("loc_B67D")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_44_B58E end

    def Function_45_B691(): pass

    label("Function_45_B691")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B743")

    #C0516
    ChrTalk(
        0x101,
        (
            "#6P#0006F那个……\x01",
            "不好意思，现在有些不太方便……\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xF,
        "#11P嗯，这样啊？\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xF,
        (
            "#11P那就等你们有空了\x01",
            "再说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B743")

    Return()

    # Function_45_B691 end

    def Function_46_B744(): pass

    label("Function_46_B744")


    #C0519
    ChrTalk(
        0x101,
        "#6P#0000F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xF,
        "#11P嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xF,
        (
            "#11P最近，有很多人过了还书期限\x01",
            "却还没有归还书籍。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xF,
        (
            "#11P所以就想拜托你们\x01",
            "去找那些借书者要回书籍。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x103,
        "#6P#0203F……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x104,
        (
            "#5P#5P#0300F这任务听上去\x01",
            "好像不是很难啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "那些人的住址\x01",
            "您都知道吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xF,
        (
            "#11P嗯，借阅人的信息\x01",
            "都记在图书卡上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xF,
        "#11P那我念给你们听了哦。\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xF,
        (
            "#11P首先是……\x01",
            "西街的出租公寓\x01",
            "『贝尔海姆』的菲伊先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xF,
        (
            "#11P接着是……\x01",
            "东街的出租公寓\x01",
            "『洋槐庄园』的克拉莉丝女士。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xF,
        (
            "#11P最后是……\x01",
            "行政区克洛斯贝尔警察局总部的\x01",
            "雷蒙德警官。\x02",
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

    #C0531
    ChrTalk(
        0x102,
        "#5P#0106F雷、雷蒙德警官……\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x101,
        (
            "#6P#0003F抱、抱歉啊，叔叔。\x01",
            "没想到我们警察局里也会有不按时还书的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xF,
        "#11P没关系，别在意。\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xF,
        (
            "#11P如果是看得太入迷所以\x01",
            "忘记归还的话，\x01",
            "我反而会感到开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        (
            "#6P#0203F……我可不认为\x01",
            "那些人不还书全都是出于这个原因……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 350)

    #C0536
    ChrTalk(
        0x103,
        "#6P#0211F懒散之人还是很多的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0537
    ChrTalk(
        0x104,
        (
            "#5P#0306F什、什么啊，\x01",
            "为什么要用那种冷冷的眼神看着我……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)

    #C0538
    ChrTalk(
        0x103,
        "#6P#0200F不，没什么。\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        (
            "#6P#0003F总之。\x02\x03",

            "#0000F委托内容我们已经明白了，\x01",
            "接下来立刻就展开行动。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x5A, 0x1F4)

    #C0540
    ChrTalk(
        0xF,
        "#11P嗯，真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xF,
        (
            "#11P收回三本书后，\x01",
            "就拿回来给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xF,
        (
            "#11P罗伊德，\x01",
            "万事拜托了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0543
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【回收超期未还的书籍】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x5, 0x1, 0x1)
    Return()

    # Function_46_B744 end

    def Function_47_BC6F(): pass

    label("Function_47_BC6F")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 800, 8440, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    OP_0D()

    #C0544
    ChrTalk(
        0xF,
        "#11P哦……\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xF,
        (
            "#11P莫非你们已经把那些\x01",
            "超期未还的书籍都收回来了？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x104,
        "#5P#0300F这是当然啦。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        "#6P#0000F是的，叔叔。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0548
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '铁道爱好者的推荐'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '玛尔克与森林深处的魔女·上'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0550
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '改变大陆的美人们'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('铁道爱好者的推荐', 1)
    SubItemNumber('玛尔克与森林深处的魔女·上', 1)
    SubItemNumber('改变大陆的美人们', 1)

    #C0551
    ChrTalk(
        0xF,
        (
            "#11P……嗯，\x01",
            "三本书确实\x01",
            "都收回了。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xF,
        (
            "#11P你们真是帮了大忙呢，\x01",
            "能得到你们的帮助，\x01",
            "实在太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x102,
        (
            "#5P#0100F呵呵……\x01",
            "您能这么说，是我们的荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x103,
        "#6P#0200F……这样就算是完成任务了吧。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xF,
        (
            "#11P嗯嗯，辛苦了。\x01",
            "如果还有什么需要的话，我会去找你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x101,
        "#6P#0000F嗯，请交给我们吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0557
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【回收超期未还的书籍】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 6)
    SetChrPos(0x0, 5000, 150, 7800, 90)
    OP_29(0x5, 0x2, 0x1F)
    OP_29(0x5, 0x1, 0x5)
    OP_29(0x5, 0x4, 0x10)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_66(0x6, 0x1)
    EventEnd(0x5)
    Return()

    # Function_47_BC6F end

    def Function_48_BFA0(): pass

    label("Function_48_BFA0")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 1000, 8220, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C04D")
    SetChrPos(0x109, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_C078")

    label("loc_C04D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C078")
    SetChrPos(0x10A, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_C078")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1C4")

    #C0558
    ChrTalk(
        0x101,
        "#6P#0000F叔叔，您好。\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xF,
        (
            "#11P哦，是罗伊德啊，\x01",
            "欢迎欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xF,
        "#11P你们今天是来借书的吗？\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x101,
        (
            "#6P#0000F不，今天是因为工作而来的。\x02\x03",

            "您不是向特别任务支援科\x01",
            "提出了委托吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x102,
        (
            "#5P#0100F好像是……\x01",
            "回收超期未还的书籍。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xF,
        (
            "#11P哦，没错没错，\x01",
            "我确实提出了那样的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xF,
        (
            "#11P那我就开始说明\x01",
            "委托的内容了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C354")

    label("loc_C1C4")


    #C0565
    ChrTalk(
        0x101,
        "#6P#0000F叔叔，您好。\x02",
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xF,
        (
            "#11P哦，是罗伊德啊，\x01",
            "欢迎欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xF,
        "#11P莫非，你们今天是为了……？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，是因为工作而来的。\x02\x03",

            "您不是向特别任务支援科\x01",
            "提出了委托吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xF,
        (
            "#11P嗯，果然……\x01",
            "是来向我确认委托内容的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xF,
        "#11P抱歉啊，还让你们跑一趟。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x102,
        (
            "#5P#0100F任务内容是\x01",
            "回收超期未还的书籍吧，\x01",
            "难道……？\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xF,
        (
            "#11P嗯，这已经是第二次\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xF,
        (
            "#11P那我就开始说明\x01",
            "委托的内容了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C354")

    OP_29(0x28, 0x1, 0x0)
    Call(0, 50)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C36F")
    Call(0, 51)

    label("loc_C36F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C394")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_C394")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_48_BFA0 end

    def Function_49_C3A8(): pass

    label("Function_49_C3A8")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 1000, 8220, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    SetChrSubChip(0xF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C455")
    SetChrPos(0x109, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_C480")

    label("loc_C455")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C480")
    SetChrPos(0x10A, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_C480")

    OP_0D()

    #C0574
    ChrTalk(
        0xF,
        (
            "#11P我确实提出了有关\x01",
            "回收超期未还书籍的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xF,
        (
            "#11P那我就\x01",
            "开始介绍委托的内容了哦。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 50)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4F2")
    Call(0, 51)

    label("loc_C4F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C517")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_C517")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_49_C3A8 end

    def Function_50_C52B(): pass

    label("Function_50_C52B")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5D7")

    #C0576
    ChrTalk(
        0x101,
        (
            "#6P#0006F抱歉，叔叔，\x01",
            "现在有些不太方便……\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xF,
        "#11P嗯，这样啊？\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xF,
        (
            "#11P那就等你们有空了\x01",
            "再说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5D7")

    Return()

    # Function_50_C52B end

    def Function_51_C5D8(): pass

    label("Function_51_C5D8")


    #C0579
    ChrTalk(
        0x101,
        "#6P#0000F嗯，没问题。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7D2")

    #C0580
    ChrTalk(
        0xF,
        "#11P嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xF,
        (
            "#11P最近，有很多人过了还书期限\x01",
            "却还没有归还书籍。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xF,
        (
            "#11P所以就想拜托你们\x01",
            "去找那些借书者要回书籍。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x103,
        "#6P#0203F……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x104,
        (
            "#5P#0300F这任务听上去\x01",
            "好像不是很难啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xF,
        (
            "#11P这个……就是因为并不简单，\x01",
            "所以才令人头痛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x101,
        "#6P#0005F……怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xF,
        (
            "#11P其实这次没有按时还书的人，\x01",
            "都不是克洛斯贝尔市的市民。\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xF,
        "#11P他们全都住在郊外。\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        "#5P#0103F啊，那可就有点麻烦了呢。\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "您知道\x01",
            "那些人的住址吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9C6")

    label("loc_C7D2")


    #C0591
    ChrTalk(
        0xF,
        "#11P嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xF,
        (
            "#11P其实最近有很多人\x01",
            "都没有按时还书。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xF,
        (
            "#11P实在不好意思，\x01",
            "但能不能再次拜托你们\x01",
            "去收回超期未还的书籍呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x103,
        (
            "#6P#0200F不按时还书的人\x01",
            "还是这么多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x104,
        (
            "#5P#0300F好，这次我们也会立刻\x01",
            "就帮您解决的。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xF,
        (
            "#11P这个……就是因为没那么简单，\x01",
            "所以才令人头痛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x101,
        "#6P#0005F……怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xF,
        (
            "#11P其实这次没有按时还书的人，\x01",
            "都不是克洛斯贝尔市的市民。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xF,
        "#11P他们全都住在郊外。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x102,
        "#5P#0103F啊，那可就有点麻烦了呢。\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "这批借书者的住址，\x01",
            "您也都知道吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9C6")


    #C0602
    ChrTalk(
        0xF,
        "#11P嗯，我们在这方面还是不会马虎的。\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xF,
        (
            "#11P首先是……\x01",
            "住在阿尔摩利卡村的\x01",
            "阿尔弗雷德。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xF,
        (
            "#11P接着是……\x01",
            "住在玛因兹的\x01",
            "矿工罗基。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xF,
        (
            "#11P最后是……\x01",
            "乌尔斯拉医院的实习医生\x01",
            "芙萝拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB0C")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_CB0C")

    Sleep(1000)

    #C0606
    ChrTalk(
        0x101,
        (
            "#6P#0003F这还真是……\x01",
            "彼此分散得很远啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x104,
        (
            "#5P#0306F看来要绕\x01",
            "自治州跑一圈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x103,
        (
            "#6P#0211F………………\x01",
            "最讨厌不记得按时还书的散漫之人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        "#5P#0100F别、别介意啦。\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xF,
        (
            "#11P……因为\x01",
            "这次的范围实在太广了，\x01",
            "所以我们的人手也不够。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xF,
        (
            "#11P怎么样……\x01",
            "你们愿意帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CCDB")

    #C0612
    ChrTalk(
        0x109,
        (
            "#12P#0500F现在可以乘坐\x01",
            "我的装甲车……\x01",
            "这样就能够免去奔波之苦了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x101,
        (
            "#6P#0003F也是……\x02\x03",

            "#0000F那就谢谢了，\x01",
            "上士。\x02\x03",

            "……那么，我们接下来\x01",
            "就立刻展开行动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF57")

    label("loc_CCDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF21")

    #C0614
    ChrTalk(
        0x101,
        "#6P#0000F嗯，那就马上行动吧……\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x10A,
        "#12P#0603F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_CDA0():
        OP_93(0x101, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CDA0)

    def lambda_CDAD():
        OP_93(0x102, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CDAD)

    def lambda_CDBA():
        OP_93(0x104, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CDBA)

    def lambda_CDC7():
        OP_93(0x103, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CDC7)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)

    #C0616
    ChrTalk(
        0x102,
        (
            "#0106F（从刚才开始，达德利搜查官的\x01",
            "　眼神就很可怕啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x104,
        (
            "#5P#0303F（而且还一言不发。\x01",
            "　但看样子也没打算阻止我们。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0618
    ChrTalk(
        0xF,
        "#11P怎么了吗？\x02",
    )

    CloseMessageWindow()

    def lambda_CE92():
        OP_93(0x101, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CE92)

    def lambda_CE9F():
        OP_93(0x102, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CE9F)

    def lambda_CEAC():
        OP_93(0x104, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CEAC)

    def lambda_CEB9():
        OP_93(0x103, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CEB9)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)

    #C0619
    ChrTalk(
        0x101,
        (
            "#6P#0000F不，没什么。\x01",
            "那我们就开始行动了。\x01",
            "（尽量快些完成任务吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF57")

    label("loc_CF21")


    #C0620
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，请交给我们吧。\x01",
            "那我们就开始行动了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF57")


    #C0621
    ChrTalk(
        0xF,
        "#11P嗯，你们真是帮了大忙啊。\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xF,
        (
            "#11P收回三本书后，\x01",
            "就拿回来给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xF,
        (
            "#11P那么，支援科的各位，\x01",
            "万事拜托了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0624
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【回收自治州内超期未还的书籍】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x28, 0x1, 0x1)
    Return()

    # Function_51_C5D8 end

    def Function_52_D033(): pass

    label("Function_52_D033")

    EventBegin(0x0)
    Fade(500)
    OP_68(5720, 1000, 8220, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18730, 0)
    SetChrPos(0x101, 5000, 150, 7300, 90)
    SetChrPos(0x102, 4750, 150, 8300, 90)
    SetChrPos(0x103, 3500, 150, 7300, 90)
    SetChrPos(0x104, 3250, 150, 8300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0DC")
    SetChrPos(0x109, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_D107")

    label("loc_D0DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D107")
    SetChrPos(0x10A, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_D107")

    SetChrSubChip(0xF, 0x0)
    OP_0D()

    #C0625
    ChrTalk(
        0xF,
        "#11P哦……\x02",
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xF,
        (
            "#11P莫非你们已经把书\x01",
            "都收回来了？\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x104,
        "#5P#0300F嗯，总算都收回来了。\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x101,
        "#6P#0000F叔叔，就是这些，给您。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0629
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '有效利用五分钟的零散时间'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0630
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '克洛斯贝尔怪谈全集'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0631
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '彩虹·FanBook'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "归还了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('有效利用五分钟的零散时间', 1)
    SubItemNumber('克洛斯贝尔怪谈全集', 1)
    SubItemNumber('彩虹·FanBook', 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D2A2")

    #C0632
    ChrTalk(
        0xF,
        (
            "#11P……嗯，\x01",
            "三本书确实\x01",
            "都收回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xF,
        (
            "#11P真是不好意思，\x01",
            "又麻烦了你们一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xF,
        (
            "#11P加上上一次，\x01",
            "实在是很感谢你们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D30A")

    label("loc_D2A2")


    #C0635
    ChrTalk(
        0xF,
        (
            "#11P……嗯，\x01",
            "三本书确实\x01",
            "都收回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xF,
        (
            "#11P你们真是帮了大忙啊。\x01",
            "能得到你们的帮助，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D30A")


    #C0637
    ChrTalk(
        0x101,
        (
            "#6P#0000F哈哈……被叔叔这样表扬，\x01",
            "真有点不好意思啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3D9")

    #C0638
    ChrTalk(
        0x109,
        (
            "#12P#0506F话说回来，\x01",
            "处理支援请求这种工作\x01",
            "好像还真是很辛苦呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x102,
        (
            "#5P#0100F呵呵，这种工作对我们来说\x01",
            "已经是家常便饭了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4C4")

    label("loc_D3D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D48E")

    #C0640
    ChrTalk(
        0x10A,
        (
            "#12P#0603F哼……这就是支援科\x01",
            "平时处理的『支援请求』工作啊，\x01",
            "真是浪费我的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x101,
        "#6P#0006F唔……不、不好意思。\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x102,
        "#5P#0103F因为这是我们的日常工作……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D4C4")

    label("loc_D48E")


    #C0643
    ChrTalk(
        0x102,
        (
            "#5P#0100F呵呵，虽然有些辛苦，\x01",
            "但还是很有意义的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4C4")


    #C0644
    ChrTalk(
        0x103,
        (
            "#6P#0203F……总之，\x01",
            "这样就算是完成任务了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xF,
        (
            "#11P嗯，辛苦了。\x01",
            "真的非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x101,
        "#6P#0000F不用客气。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0647
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【回收自治州内超期未还的书籍】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 5000, 150, 7800, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D5CB")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_D5CB")

    OP_29(0x28, 0x2, 0x1F)
    OP_29(0x28, 0x1, 0xB)
    OP_29(0x28, 0x4, 0x10)
    OP_66(0x5, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x9, 0x1)
    EventEnd(0x5)
    Return()

    # Function_52_D033 end

    def Function_53_D5EB(): pass

    label("Function_53_D5EB")

    EventBegin(0x0)
    Fade(500)
    OP_68(31560, 5020, -6480, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18590, 0)
    SetChrPos(0x101, 30740, 4000, -6140, 135)
    SetChrPos(0x102, 30340, 4000, -7790, 45)
    SetChrPos(0x103, 29540, 4030, -6520, 135)
    SetChrPos(0x104, 29440, 4030, -7890, 45)
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()

    #C0648
    ChrTalk(
        0x101,
        (
            "#6P#0003F怪盗Ｂ所说的『白隼』\x01",
            "好像是利贝尔王国的国鸟。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x102,
        (
            "#5P#0100F利贝尔王国是\x01",
            "克洛斯贝尔的近邻，\x01",
            "也是关系最好的国家。\x02\x03",

            "难怪总觉得这个词\x01",
            "在哪里听过。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 30230, 4000, -6690, 90)
    SetChrPos(0x8, 29310, 4000, 0, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 1)
    OP_29(0x22, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_53_D5EB end

    def Function_54_D74C(): pass

    label("Function_54_D74C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(29750, 5020, 5000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 1310, 30, 750, 90)
    SetChrPos(0xEF, 1310, 30, -750, 90)
    SetChrPos(0x153, 3610, 30, 0, 135)
    OP_68(29750, 5020, -5500, 5000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    Fade(500)
    OP_68(17860, 1020, -12620, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    OP_68(7380, 1030, -11050, 5000)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(2250, 1030, -150, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18500, 0)
    OP_0D()
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_93(0x153, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0x153, 0x5A, 0x1F4)
    Sleep(500)

    #C0650
    ChrTalk(
        0x153,
        (
            "#1105F#5P哇，好厉害！\x01",
            "好多书啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x101,
        (
            "#6P#0002F那个……琪雅你\x01",
            "喜欢书吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0x10E, 0x1F4)

    #C0652
    ChrTalk(
        0x153,
        (
            "#1110F#11P嗯，虽然不知道为什么，但很喜欢！\x02\x03",

            "#1109F只要看到书排成一列，\x01",
            "就觉得很兴奋！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_D997")

    #C0653
    ChrTalk(
        0x102,
        (
            "#0109F#6P那么我们下次\x01",
            "再来慢慢逛吧。\x02\x03",

            "#0102F克洛斯贝尔的市立图书馆里\x01",
            "应该有很多\x01",
            "儿童读物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA5F")

    label("loc_D997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_DA05")

    #C0654
    ChrTalk(
        0x103,
        (
            "#0204F#6P那么我们下次\x01",
            "再来慢慢逛吧。\x02\x03",

            "#0202F克洛斯贝尔的市立图书馆里\x01",
            "应该有很多\x01",
            "儿童读物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA5F")

    label("loc_DA05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_DA5F")

    #C0655
    ChrTalk(
        0x104,
        (
            "#0309F#6P那么下次再\x01",
            "带你来慢慢逛吧。\x02\x03",

            "#0300F这里看上去好像有\x01",
            "很多儿童读物。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA5F")

    OP_5A()
    SetChrPos(0x0, 2500, 0, 0, 90)
    SetScenarioFlags(0xB7, 0)
    EventEnd(0x5)
    Return()

    # Function_54_D74C end

    SaveToFile()

Try(main)
