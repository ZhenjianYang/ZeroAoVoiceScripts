from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "キャサル",               # 1
        "キャサル",               # 2
        "ノバース",               # 3
        "シャーナ",               # 4
        "シャーナ",               # 5
        "アビー",                 # 6
        "アビー",                 # 7
        "マイルズ",               # 8
        "タジク",                 # 9
        "マリアベル",             # 10
        "レクター",               # 11
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
        "Function_5_1DA6",         # 05, 5
        "Function_6_1FE3",         # 06, 6
        "Function_7_3649",         # 07, 7
        "Function_8_3779",         # 08, 8
        "Function_9_37E8",         # 09, 9
        "Function_10_42D6",        # 0A, 10
        "Function_11_4310",        # 0B, 11
        "Function_12_4B70",        # 0C, 12
        "Function_13_4C69",        # 0D, 13
        "Function_14_4C7E",        # 0E, 14
        "Function_15_6840",        # 0F, 15
        "Function_16_6A99",        # 10, 16
        "Function_17_6C14",        # 11, 17
        "Function_18_6D51",        # 12, 18
        "Function_19_6F2B",        # 13, 19
        "Function_20_6FA6",        # 14, 20
        "Function_21_7138",        # 15, 21
        "Function_22_71F0",        # 16, 22
        "Function_23_7610",        # 17, 23
        "Function_24_852A",        # 18, 24
        "Function_25_8A1A",        # 19, 25
        "Function_26_8DB2",        # 1A, 26
        "Function_27_8F68",        # 1B, 27
        "Function_28_9061",        # 1C, 28
        "Function_29_90E8",        # 1D, 29
        "Function_30_9171",        # 1E, 30
        "Function_31_91F4",        # 1F, 31
        "Function_32_9277",        # 20, 32
        "Function_33_9381",        # 21, 33
        "Function_34_940E",        # 22, 34
        "Function_35_9806",        # 23, 35
        "Function_36_A0DE",        # 24, 36
        "Function_37_A982",        # 25, 37
        "Function_38_AC9E",        # 26, 38
        "Function_39_B435",        # 27, 39
        "Function_40_B8D4",        # 28, 40
        "Function_41_BD82",        # 29, 41
        "Function_42_C18C",        # 2A, 42
        "Function_43_C9A8",        # 2B, 43
        "Function_44_CBD1",        # 2C, 44
        "Function_45_CCE4",        # 2D, 45
        "Function_46_CDB1",        # 2E, 46
        "Function_47_D394",        # 2F, 47
        "Function_48_D709",        # 30, 48
        "Function_49_DB89",        # 31, 49
        "Function_50_DD1C",        # 32, 50
        "Function_51_DDEF",        # 33, 51
        "Function_52_E9B6",        # 34, 52
        "Function_53_F018",        # 35, 53
        "Function_54_F19F",        # 36, 54
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_AAD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EF")

    #C0001
    ChrTalk(
        0xFE,
        (
            "あら……\x01",
            "そろそろ閉館時間ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "戸締りの準備をしないと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A28")

    label("loc_9EF")


    #C0003
    ChrTalk(
        0xFE,
        (
            "貸出、返却はまもなく終了ですよ。\x01",
            "急いでくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A28")

    Jump("loc_AA8")

    label("loc_A2D")


    #C0004
    ChrTalk(
        0xFE,
        (
            "館長は所用で\x01",
            "出かけてしまったんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "そろそろ閉館時間ですし……\x01",
            "今日は私が戸締りをしなくちゃ\x01",
            "いけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA8")

    Jump("loc_1DA2")

    label("loc_AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B45")

    #C0006
    ChrTalk(
        0xFE,
        (
            "ノバースさん、今日も\x01",
            "閉館時間ギリギリまで\x01",
            "ねばるつもりかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "最近なんだか張り切って\x01",
            "らっしゃるみたいですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BB4")

    label("loc_B45")


    #C0008
    ChrTalk(
        0xFE,
        (
            "あ……ちなみに古い文献は\x01",
            "貸出禁止ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "お調べになるなら\x01",
            "開館している時間だけに\x01",
            "お願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB4")

    Jump("loc_1DA2")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C70")

    #C0010
    ChrTalk(
        0xFE,
        (
            "今日もいいお天気ですね。\x01",
            "虫干しするのに良さそうな感じです。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "あ……別にここの書籍を\x01",
            "散らかすわけじゃありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "少し風を通すだけですから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CDE")

    label("loc_C70")


    #C0013
    ChrTalk(
        0xFE,
        (
            "今日もいいお天気ですね。\x01",
            "ピクニックにも良さそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "仕事が休みなら\x01",
            "私もどこか出かけるんですけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDE")

    Jump("loc_1DA2")

    label("loc_CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D78")

    #C0015
    ChrTalk(
        0xFE,
        "新刊書籍を並べている所なんです。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "この作者さんのシリーズは\x01",
            "とても人気なので……\x01",
            "きっと市民の皆さんも喜びますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DE3")

    label("loc_D78")


    #C0017
    ChrTalk(
        0xFE,
        "この作者さん、とても人気なんです。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "皆さんもお読みになりたいなら\x01",
            "早めに貸出しておくといいですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE3")

    Jump("loc_1DA2")

    label("loc_DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E93")

    #C0019
    ChrTalk(
        0xFE,
        (
            "えっと……\x01",
            "子供向けの本をお探しですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "入ってすぐ右側に\x01",
            "専門のコーナーがありますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "比較的人気ですから、\x01",
            "貸し出し中のものも多いんですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA2")

    label("loc_E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F18")

    #C0022
    ChrTalk(
        0xFE,
        (
            "さっさっ……今日は\x01",
            "掃き掃除をしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "来館者も少ないですし\x01",
            "お掃除には打ってつけですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F79")

    label("loc_F18")


    #C0024
    ChrTalk(
        0xFE,
        "私も今日は早上がりなんです。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "午後の２時には閉館するので\x01",
            "貸出はお早めにお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F79")

    Jump("loc_1DA2")

    label("loc_F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_104D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF9")

    #C0026
    ChrTalk(
        0xFE,
        (
            "この図書館２階が\x01",
            "パレードを見る特等席だなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "ふふ、やっぱり\x01",
            "誰も知りませんよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1048")

    label("loc_FF9")


    #C0028
    ChrTalk(
        0xFE,
        (
            "この事は館長も\x01",
            "ご存じないと思うんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "ふふ、私だけの秘密ですから。\x02",
    )

    CloseMessageWindow()

    label("loc_1048")

    Jump("loc_1DA2")

    label("loc_104D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1151")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E6")

    #C0030
    ChrTalk(
        0xFE,
        "今日は一段と華やかですね……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "館内にいても\x01",
            "ざわめきが聞こえてきますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "私もお昼休みは\x01",
            "一回りしてみようかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_114C")

    label("loc_10E6")


    #C0033
    ChrTalk(
        0xFE,
        (
            "クロスベル人は\x01",
            "お祭り好きっていいますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "ふふ、私もやっぱり\x01",
            "クロスベル人みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114C")

    Jump("loc_1DA2")

    label("loc_1151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11C3")

    #C0035
    ChrTalk(
        0xFE,
        (
            "返却された本の整理は\x01",
            "なかなか大変なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "来館者が少ない間に\x01",
            "並べなおしておかないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA2")

    label("loc_11C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_12F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128B")

    #C0037
    ChrTalk(
        0xFE,
        (
            "こんにちは、クロスベル\x01",
            "市立図書館へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……やっぱり記念祭の間は\x01",
            "来館者がぐんと減ってしまいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "まあ無理もないですね……\x01",
            "お祭りの最中なんですもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12F1")

    label("loc_128B")


    #C0040
    ChrTalk(
        0xFE,
        (
            "あ……そうそう。\x01",
            "館内は飲食禁止ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "出店で買ったものを\x01",
            "持ち込んだりしてはダメですよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F1")

    Jump("loc_1DA2")

    label("loc_12F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1410")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BA")

    #C0042
    ChrTalk(
        0xFE,
        (
            "館長は記念祭には\x01",
            "お休みを取るそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "まあ、お祭りの間は来館者も\x01",
            "ぐっと減ってしまいますから……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "ちょっと心細いですけど、\x01",
            "私が一人で頑張っちゃいます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_140B")

    label("loc_13BA")


    #C0045
    ChrTalk(
        0xFE,
        "普段は館長に任せきりですし。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "私もこの機会に\x01",
            "頑張らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140B")

    Jump("loc_1DA2")

    label("loc_1410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C2")

    #C0047
    ChrTalk(
        0xFE,
        (
            "地下の方からズドドド……！\x01",
            "という音がしたもので……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "ふう、ともかく館長に\x01",
            "お怪我が無くてよかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "書籍って結構\x01",
            "重たいものですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_153C")

    label("loc_14C2")


    #C0050
    ChrTalk(
        0xFE,
        "館長にお怪我が無くてよかったです。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "その、本に埋もれて\x01",
            "アップアップなさってる姿には\x01",
            "呆れてしまいましたけれども。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153C")

    Jump("loc_1DA2")

    label("loc_1541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_167C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EC")

    #C0052
    ChrTalk(
        0xFE,
        (
            "アルカンシェルのチケットは\x01",
            "もう売り切れてしまったんですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "私も諦めずに\x01",
            "並べばよかったでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "私ってつい諦めがちで……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1677")

    label("loc_15EC")


    #C0055
    ChrTalk(
        0xFE,
        (
            "ちなみに……図書館の蔵書には\x01",
            "過去のアルカンシェルの公演目録や\x01",
            "写真集なんかもあるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "……ずっと貸し出し中\x01",
            "なんですけれどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1677")

    Jump("loc_1DA2")

    label("loc_167C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_17EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176E")

    #C0057
    ChrTalk(
        0xFE,
        (
            "館長は休館日にも出勤して\x01",
            "書籍の整理や目録作りを\x01",
            "なさってるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "本がお好きなだけじゃなくて、\x01",
            "市民の皆さんのために\x01",
            "努力しておられるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "ふふ、目立たない役職ですけど\x01",
            "私は立派な方だと思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17EA")

    label("loc_176E")


    #C0060
    ChrTalk(
        0xFE,
        (
            "ちなみに……図書館の表の芝生も\x01",
            "館長が手入れなさっているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "目立たない役職ですけど\x01",
            "勤勉で立派な方なんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EA")

    Jump("loc_1DA2")

    label("loc_17EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_193B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C4")

    #C0062
    ChrTalk(
        0xFE,
        (
            "私は両親の勧めで\x01",
            "公務員を目指したんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "公務員って報われない\x01",
            "イメージがありますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "この通り職場は静かですし\x01",
            "館長もお優しい人です。\x01",
            "そう捨てたものじゃありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1936")

    label("loc_18C4")


    #C0065
    ChrTalk(
        0xFE,
        (
            "私は両親の勧めで\x01",
            "公務員を目指したんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "職場は静かだし手当ては厚いし。\x01",
            "そう悪いものじゃありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1936")

    Jump("loc_1DA2")

    label("loc_193B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DD")

    #C0067
    ChrTalk(
        0xFE,
        "白い狼が出てくる童話……？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "ええ、たしか\x01",
            "１階の子供向けコーナーに\x01",
            "あったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "探してみると\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A50")

    label("loc_19DD")


    #C0070
    ChrTalk(
        0xFE,
        (
            "白い狼が出てくる童話なら\x01",
            "１階の子供向けコーナーに\x01",
            "あったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "探してみると\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A50")

    Jump("loc_1DA2")

    label("loc_1A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B10")

    #C0072
    ChrTalk(
        0xFE,
        "ええと、この本は……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "私、勤めて５年になりますけど\x01",
            "まだまだ知らない蔵書が沢山あります。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "本当に蔵書量が多いんですよね。\x01",
            "いまだに迷ってしまいます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B7C")

    label("loc_1B10")


    #C0075
    ChrTalk(
        0xFE,
        (
            "この図書館は\x01",
            "本当に蔵書量が多いんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "全て把握しているのは\x01",
            "館長くらいのものじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B7C")

    Jump("loc_1DA2")

    label("loc_1B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1CB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1F")

    #C0077
    ChrTalk(
        0xFE,
        "館長ったら本当に本好きですね。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "この前も、崩れた本の山に\x01",
            "埋もれてあたふたしていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "私、呆れてしまいましたもの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CAC")

    label("loc_1C1F")


    #C0080
    ChrTalk(
        0xFE,
        (
            "館長ったら、本の山に埋もれて\x01",
            "あたふたしていたんですよ。\x01",
            "私、呆れてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……その、本当を言うと\x01",
            "少し面白かったんですけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAC")

    Jump("loc_1DA2")

    label("loc_1CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1DA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4C")

    #C0082
    ChrTalk(
        0xFE,
        (
            "この市立図書館は近隣諸国でも\x01",
            "一、二を争う蔵書量なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "でも人手が足りなくって……\x01",
            "未公開の書籍も多いんですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DA2")

    label("loc_1D4C")


    #C0084
    ChrTalk(
        0xFE,
        (
            "本はたくさんあるんですけど……\x01",
            "市民に公開する手続きが\x01",
            "追いついていないんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA2")

    TalkEnd(0xFE)
    Return()

    # Function_4_980 end

    def Function_5_1DA6(): pass

    label("Function_5_1DA6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E3A")
    Jump("loc_1E84")

    label("loc_1E3A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E5A")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E84")

    label("loc_1E5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E7A")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E84")

    label("loc_1E7A")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E84")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F5C")

    #C0085
    ChrTalk(
        0x9,
        (
            "こんにちは、\x01",
            "クロスベル市立図書館へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "今日は司書の者が遅番なので\x01",
            "私一人ですけど……\x01",
            "貸し出しは問題なく行えますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        "ぜひご利用くださいね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FDB")

    label("loc_1F5C")


    #C0088
    ChrTalk(
        0x9,
        (
            "今日はマイルズさんが\x01",
            "遅番の日なんですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "……ええと、失礼しました。\x01",
            "貸し出しでしたら\x01",
            "遠慮なく仰ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FDB")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    Return()

    # Function_5_1DA6 end

    def Function_6_1FE3(): pass

    label("Function_6_1FE3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2077")
    Jump("loc_20C1")

    label("loc_2077")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2097")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20C1")

    label("loc_2097")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20B7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20C1")

    label("loc_20B7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20C1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2145")
    SetChrSubChip(0xFE, 0x0)

    #C0090
    ChrTalk(
        0xFE,
        "ふむふむ、わーお！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "こいつを纏めりゃ、\x01",
            "次の論文はいただきだな……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3641")

    label("loc_2145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_21FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C0")

    #C0092
    ChrTalk(
        0xFE,
        (
            "いい資料がたくさん\x01",
            "見つかって困っちゃうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "やっぱり調べ物をするなら\x01",
            "市立図書館だね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21F5")

    label("loc_21C0")


    #C0094
    ChrTalk(
        0xFE,
        (
            "よーし、今日も閉館時間\x01",
            "ギリギリまで頑張るぞー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F5")

    Jump("loc_3641")

    label("loc_21FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_233A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BD")

    #C0095
    ChrTalk(
        0xFE,
        (
            "今日は中々\x01",
            "いい物を見つけちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "これは８０年ほど前の\x01",
            "商人達の覚え書きだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "ふむふむ……当時の\x01",
            "クロスベルの事情がよく分かる\x01",
            "貴重な資料といえるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2335")

    label("loc_22BD")


    #C0098
    ChrTalk(
        0xFE,
        (
            "８０年前っていえば\x01",
            "まだクロスベル自治州が成立する前だ……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "情勢が不安定で、\x01",
            "商人たちも苦労していたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2335")

    Jump("loc_3641")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_23EB")

    #C0100
    ChrTalk(
        0xFE,
        (
            "論文がお流れになったことで\x01",
            "決心がついた。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "これからはもっと\x01",
            "腰を据えて研究する事にしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "目を通していない資料や文献は\x01",
            "まだまだたくさんあるからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3641")

    label("loc_23EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A6")

    #C0103
    ChrTalk(
        0xFE,
        (
            "フ……留年確定した\x01",
            "このノバースさんに言う事はあるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x153,
        "#1100F？　変なヒトー。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        "がぁん……！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 1)
    Jump("loc_251C")

    label("loc_24A6")


    #C0106
    ChrTalk(
        0xFE,
        (
            "フフ、ははは……\x01",
            "結局論文は間に合わなかったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "ま、いいんだけどね。\x01",
            "もう１年頑張ればいいんだからさ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251C")

    Jump("loc_3641")

    label("loc_2521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25C0")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0108
    ChrTalk(
        0xFE,
        "い、いま何時……？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "ま、まずい……\x01",
            "そろそろ空港に向かわないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        "論文の提出が間に合わないかも……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2630")

    label("loc_25C0")


    #C0111
    ChrTalk(
        0xFE,
        (
            "僕はレマン自治州の\x01",
            "大学に在籍してるんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "移動時間を計算しないと\x01",
            "間に合わない可能性が、ブツブツ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2630")

    Jump("loc_3641")

    label("loc_2635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_272A")

    #C0113
    ChrTalk(
        0xFE,
        (
            "クロスベルで“鐘”は古来から\x01",
            "特別な意味を持っていたんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "市場の朝や荷馬車の発車、\x01",
            "あるいは敵襲を知らせる警報として……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "クロスベル大聖堂が\x01",
            "鐘を鳴らして時を告げるのは\x01",
            "中世の頃からの習慣らしいんだよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_277D")

    label("loc_272A")


    #C0116
    ChrTalk(
        0xFE,
        (
            "あれ、なんか\x01",
            "意識が朦朧としてきた気がする……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "ちょっと頑張りすぎかなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_277D")

    Jump("loc_3641")

    label("loc_2782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_291C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E0")

    #C0118
    ChrTalk(
        0xFE,
        (
            "外はお祭りかぁ……とほほ。\x01",
            "僕は論文の仕上げでカンヅメだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "ちなみにパレードってのは\x01",
            "元々地元の有力者が祝いの日に\x01",
            "山車を出したのが始まりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "クロスベルが成立した後は\x01",
            "記念祭の行事として\x01",
            "行われるようになったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "今でも慣習が残っていて、\x01",
            "財界人や商工会がミラを出して\x01",
            "パレードの車を用意するんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2917")

    label("loc_28E0")


    #C0122
    ChrTalk(
        0xFE,
        (
            "…………………………\x01",
            "お祭り、みんな楽しそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2917")

    Jump("loc_3641")

    label("loc_291C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F7")

    #C0123
    ChrTalk(
        0xFE,
        (
            "クロスベルは中世の頃から\x01",
            "世界有数の交易都市だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "地形的に、大陸西部へ向かう\x01",
            "交通の要所だったからね。\x01",
            "自然と人やミラが集まったって訳だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "……それは今も\x01",
            "変わらないみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A5F")

    label("loc_29F7")


    #C0126
    ChrTalk(
        0xFE,
        (
            "今は鉄道や飛行船が\x01",
            "行き来している……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "むしろ昔以上にたくさんの物が\x01",
            "集まるのかもしれないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5F")

    Jump("loc_3641")

    label("loc_2A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2B49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B13")

    #C0128
    ChrTalk(
        0xFE,
        (
            "き、気が付いたら\x01",
            "記念祭だなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "今月で論文の\x01",
            "締め切りじゃないか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "ぶ、文献なんて\x01",
            "読んでいる場合じゃない。\x01",
            "早く纏めないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B44")

    label("loc_2B13")


    #C0131
    ChrTalk(
        0xFE,
        (
            "し、締め切りが……\x01",
            "すっかり忘れてたよ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B44")

    Jump("loc_3641")

    label("loc_2B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD5")

    #C0132
    ChrTalk(
        0xFE,
        (
            "なにっ……！？\x01",
            "君たちは『星見の塔』を\x01",
            "調べに行くのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "ううっ、ずるい……\x01",
            "僕だって行ってみたいのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C43")

    label("loc_2BD5")


    #C0134
    ChrTalk(
        0xFE,
        (
            "『星見の塔』は中世の時代に\x01",
            "建てられた貴重な遺跡なんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "くれぐれも、壊したりは\x01",
            "しないでくれよ！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C43")

    Jump("loc_3641")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFB")

    #C0136
    ChrTalk(
        0xFE,
        (
            "地下資料室への立ち入り、\x01",
            "館長に許してもらえなかったよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "なんでも、危険だからとか。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "……………………？？\x01",
            "図書館に危険なんてあるのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D65")

    label("loc_2CFB")


    #C0139
    ChrTalk(
        0xFE,
        (
            "資料なら探しておくから\x01",
            "待っていてと言われたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "でも図書館に危険なんて……\x01",
            "どういうことだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D65")

    Jump("loc_3641")

    label("loc_2D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E4D")

    #C0141
    ChrTalk(
        0xFE,
        (
            "論文の締め切りも近いし\x01",
            "そろそろ焦んないと、また留年だよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "こほん、まあともかく\x01",
            "まずは館長に頼んで\x01",
            "地下の資料室に入れてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "手持ちの資料じゃ\x01",
            "分からない事が多すぎるんだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E9E")

    label("loc_2E4D")


    #C0144
    ChrTalk(
        0xFE,
        (
            "ここの地下資料室には\x01",
            "古い文献が沢山あるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "調べがいがありそうだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_2E9E")

    Jump("loc_3641")

    label("loc_2EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3027")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB9")

    #C0146
    ChrTalk(
        0xFE,
        (
            "この市立図書館って\x01",
            "結構古い歴史があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "前身である書籍館は、\x01",
            "元々クロスベルの商人たちが\x01",
            "帳簿を保管する場所だったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "だから３００年くらい前の\x01",
            "資料も残っているってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "歴史の研究者としては\x01",
            "資料の宝庫みたいなもんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3022")

    label("loc_2FB9")


    #C0150
    ChrTalk(
        0xFE,
        (
            "当時の資料は、この図書館にも\x01",
            "ちゃんと受け継がれているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "一般公開はされてないんだけどね。\x02",
    )

    CloseMessageWindow()

    label("loc_3022")

    Jump("loc_3641")

    label("loc_3027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3188")

    #C0152
    ChrTalk(
        0xFE,
        (
            "あまり知られていないけど、\x01",
            "クロスベルには方々に\x01",
            "中世の遺跡が残っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "有名なのは、アルモリカ古道の\x01",
            "外れにある古戦場の砦跡だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "２０年くらい前には\x01",
            "大規模な調査団も\x01",
            "結成されていたはずだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "そうそう、確か\x01",
            "中央広場の広場に置かれている\x01",
            "巨大な鐘……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "あれは古戦場から\x01",
            "出土したものじゃなかったっけ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31FC")

    label("loc_3188")


    #C0157
    ChrTalk(
        0xFE,
        (
            "クロスベルには他にも\x01",
            "いくつか有名な遺跡があるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "僕も見に行きたいんだけど……\x01",
            "今は論文の締め切りがね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31FC")

    Jump("loc_3641")

    label("loc_3201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_335E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3306")

    #C0159
    ChrTalk(
        0xFE,
        (
            "クロスベルには\x01",
            "昔の事を知っている人が\x01",
            "少ないなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "５０年位なら遡れるんだけど、\x01",
            "１００年、２００年となると\x01",
            "みんな知らないと言うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "クロスベル市が大きく発展してきた\x01",
            "詳しい経緯を知りたい……\x01",
            "皆そうは考えないのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3359")

    label("loc_3306")


    #C0162
    ChrTalk(
        0xFE,
        (
            "クロスベル人って\x01",
            "たいてい歴史に疎いよねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        "研究者としてはさみしいな。\x02",
    )

    CloseMessageWindow()

    label("loc_3359")

    Jump("loc_3641")

    label("loc_335E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3457")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33FE")

    #C0164
    ChrTalk(
        0xFE,
        "歴史の研究とは地道なものだ……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "文献をあさり、伝承を集め、\x01",
            "たまにゆかりの史跡を訪れる……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "まあ調べ物の学問だね、うん。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3452")

    label("loc_33FE")


    #C0167
    ChrTalk(
        0xFE,
        (
            "歴史の研究は\x01",
            "１人で調べ物が基本だ……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "研究者ながら\x01",
            "地味な学問だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3452")

    Jump("loc_3641")

    label("loc_3457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3472")
    Call(0, 7)
    Jump("loc_3521")

    label("loc_3472")


    #C0169
    ChrTalk(
        0xFE,
        (
            "資料が全然足りなくて……\x01",
            "館長に泣きついて、古い\x01",
            "未公開資料を出してもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        "うーん、足りるかなぁ……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "でも論文を纏めないと\x01",
            "博士号が取れないまま留年だよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3521")

    Jump("loc_3641")

    label("loc_3526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3541")
    Call(0, 7)
    Jump("loc_3641")

    label("loc_3541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D1")

    #C0172
    ChrTalk(
        0xFE,
        (
            "『クロスベルの伝承』……\x01",
            "『マインツ郷土史』……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "だめだ、全然資料が足りない……\x01",
            "これじゃ締め切りに間に合わないよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3641")

    label("loc_35D1")


    #C0174
    ChrTalk(
        0xFE,
        (
            "僕はクロスベルの歴史を\x01",
            "研究しているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "いい資料が見つからない。\x01",
            "これじゃ論文が書けないよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3641")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1FE3 end

    def Function_7_3649(): pass

    label("Function_7_3649")


    #C0176
    ChrTalk(
        0xFE,
        (
            "はああ……論文を纏めるのが\x01",
            "こんなに大変だなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "始める前は\x01",
            "暇な時間に読もうと思って\x01",
            "娯楽小説まで買ったのになぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "あ、君たち。\x01",
            "良かったらこの本を\x01",
            "持っていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "忙しくて\x01",
            "読む暇が無さそうなんだよ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C6, 1)
    SetScenarioFlags(0x9C, 0)
    Return()

    # Function_7_3649 end

    def Function_8_3779(): pass

    label("Function_8_3779")

    TalkBegin(0xFE)

    #C0181
    ChrTalk(
        0xFE,
        (
            "今日は館長さんオススメの\x01",
            "本を借りて帰るんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "ふふ、家でも読んでって\x01",
            "ねだられちゃいますね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_3779 end

    def Function_9_37E8(): pass

    label("Function_9_37E8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_387C")
    Jump("loc_38C6")

    label("loc_387C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_389C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38C6")

    label("loc_389C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38C6")

    label("loc_38BC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38C6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_38F9")
    Jump("loc_42CE")

    label("loc_38F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_END)), "loc_3A67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E3")

    #C0183
    ChrTalk(
        0xFE,
        (
            "『マルクと深き森の魔女』、\x01",
            "やっと下巻が入荷されましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "あの本は図書館に置いている童話で\x01",
            "一番人気のある本なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "私もアビーに\x01",
            "読んであげているうちに\x01",
            "すっかりハマっちゃって……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A62")

    label("loc_39E3")


    #C0186
    ChrTalk(
        0xFE,
        (
            "『マルクと深き森の魔女』は\x01",
            "図書館で一番人気のある\x01",
            "童話なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "１階の本棚に入ってますし\x01",
            "読んでみてはどうですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A62")

    Jump("loc_3BDA")

    label("loc_3A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A79")
    Call(0, 12)
    Jump("loc_3BDA")

    label("loc_3A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B6E")

    #C0188
    ChrTalk(
        0xFE,
        (
            "アビーは気に入った本はなんでも\x01",
            "キーアちゃんに見せたいみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "あの、いつも\x01",
            "ご迷惑だったりしませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        "#0204Fいえ、全くそんなことは……\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#0000Fあまり連れて来れませんけど\x01",
            "またキーアと遊んでやってください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3BDA")

    label("loc_3B6E")


    #C0192
    ChrTalk(
        0xFE,
        (
            "アビーは本が好きで\x01",
            "開館日は毎日来ているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "ふふ……キーアちゃんのことが\x01",
            "大好きみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BDA")

    Jump("loc_42CE")

    label("loc_3BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3C4B")
    SetChrSubChip(0xFE, 0x0)

    #C0194
    ChrTalk(
        0xFE,
        (
            "お巡りさんは\x01",
            "走って走って追いかけました。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "でも子豚は\x01",
            "どんどん逃げていきます……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CE")

    label("loc_3C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3CEC")

    #C0196
    ChrTalk(
        0xFE,
        (
            "アビーは記念祭の後から\x01",
            "お巡りさんが出てくるお話を\x01",
            "ねだるようになったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "ふふ……お巡りさんの制服が\x01",
            "気に入ってしまったみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CE")

    label("loc_3CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3D45")

    #C0198
    ChrTalk(
        0xFE,
        (
            "あら……\x01",
            "うちのアビーより年上の子ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "ふふ、仲良くしてあげてね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_42CE")

    label("loc_3D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3DA7")

    #C0200
    ChrTalk(
        0xFE,
        (
            "あら、いけない。\x01",
            "もうこんな時間……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "そろそろお買い物して\x01",
            "帰らなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CE")

    label("loc_3DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3DB5")
    Jump("loc_42CE")

    label("loc_3DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3E38")

    #C0202
    ChrTalk(
        0xFE,
        (
            "うちの子って\x01",
            "お気に入りの本を\x01",
            "何度もねだるんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "うーん、まあいいのかしら。\x01",
            "今日５回目なんですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CE")

    label("loc_3E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3EF1")
    SetChrSubChip(0xFE, 0x0)

    #C0204
    ChrTalk(
        0xFE,
        (
            "そのとき聞こえてきたのは\x01",
            "女神様の声です。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "『さあ、道はひらかれました。\x01",
            "  なかまの元へもどりなさい……』\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "それをきいた子狐は\x01",
            "大急ぎでかけていきました……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CE")

    label("loc_3EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_405C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FDB")

    #C0207
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "クロスベルの大聖堂って\x01",
            "立派な建物だそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "優秀な司祭やシスターの方も\x01",
            "たくさんいらっしゃると聞きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "アビーも来年からは\x01",
            "日曜学校に通えますし、\x01",
            "一度お祈りにいこうかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4057")

    label("loc_3FDB")


    #C0210
    ChrTalk(
        0xFE,
        (
            "クロスベルに引っ越してから\x01",
            "まだ大聖堂には行っていませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "アビーは女神さまが大好きだから\x01",
            "喜ぶかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4057")

    Jump("loc_42CE")

    label("loc_405C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_40E7")

    #C0212
    ChrTalk(
        0xFE,
        (
            "図書館には子供向けの本も\x01",
            "たくさんあって助かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "でも利用している人は\x01",
            "意外と少ないですよね。\x01",
            "どうしてかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CE")

    label("loc_40E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4163")

    #C0214
    ChrTalk(
        0xFE,
        (
            "私、最近クロスベルに\x01",
            "引っ越してきたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "クロスベルって街並みも綺麗だし\x01",
            "とってもいい所ですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CE")

    label("loc_4163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_41BE")
    SetChrSubChip(0xFE, 0x0)

    #C0216
    ChrTalk(
        0xFE,
        (
            "そこに現れたのは\x01",
            "なんと恐ろしい悪魔です。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "ぐわはははは……っ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_42CE")

    label("loc_41BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_42CE")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4262")

    #C0218
    ChrTalk(
        0xFE,
        (
            "そして空の女神#8Rエ イ ド ス#さまの\x01",
            "放った光は……\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    Sleep(500)

    #C0219
    ChrTalk(
        0xFE,
        "せかい中に広がっていきました。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        "動物たちはそれに驚いて……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_42CE")

    label("loc_4262")


    #C0221
    ChrTalk(
        0xFE,
        (
            "空の女神#8Rエ イ ド ス#さまの放った光は\x01",
            "せかい中に広がっていきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "動物たちはそれに驚いて……\x02",
    )

    CloseMessageWindow()

    label("loc_42CE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_37E8 end

    def Function_10_42D6(): pass

    label("Function_10_42D6")

    TalkBegin(0xFE)

    #C0223
    ChrTalk(
        0xFE,
        (
            "おうちにかえったら\x01",
            "ママによんでもらうんだ～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_42D6 end

    def Function_11_4310(): pass

    label("Function_11_4310")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43A4")
    Jump("loc_43EE")

    label("loc_43A4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43C4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43EE")

    label("loc_43C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43E4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43EE")

    label("loc_43E4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43EE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4421")
    Jump("loc_4B64")

    label("loc_4421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_44CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_END)), "loc_4478")

    #C0224
    ChrTalk(
        0xFE,
        "続きはどうなったのかなぁ。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        "ねぇ、早く読んで読んで～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_44C7")

    label("loc_4478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_448A")
    Call(0, 12)
    Jump("loc_44C7")

    label("loc_448A")


    #C0226
    ChrTalk(
        0xFE,
        (
            "こんどキーアおねーちゃんに\x01",
            "おすすめしてあげるんだ～っ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44C7")

    Jump("loc_4B64")

    label("loc_44CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4504")
    SetChrSubChip(0xFE, 0x1)

    #C0227
    ChrTalk(
        0xFE,
        "わ～っ、お巡りさんかっこいい～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B64")

    label("loc_4504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_45F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C1")

    #C0228
    ChrTalk(
        0xFE,
        (
            "ねーねー、\x01",
            "キーアおねーちゃんは～？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#0000Fはは、今日は一緒じゃないんだ。\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#0102Fまた今度遊びに来るから\x01",
            "楽しみにしていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "うん、たのしみ～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45EC")

    label("loc_45C1")


    #C0232
    ChrTalk(
        0xFE,
        (
            "キーアおねーちゃんに\x01",
            "よろしくね～っ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45EC")

    Jump("loc_4B64")

    label("loc_45F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4819")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C4")

    #C0233
    ChrTalk(
        0xFE,
        (
            "わーい、ママに\x01",
            "ご本を読んでもらうんだ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x153,
        "#1110Fいいなー、キーアも聞きたいかも。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0235
    ChrTalk(
        0xFE,
        "おねーちゃんも、ご本すきなの～？\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "えへへ、ぼくとおんなじだ～！\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x153,
        "#1109Fうん、おんなじだね～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_472F")

    #C0238
    ChrTalk(
        0x102,
        (
            "#0102F（やっぱり子供同士だと\x01",
            "  馴染むのが早いわね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BC")

    label("loc_472F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4778")

    #C0239
    ChrTalk(
        0x103,
        (
            "#0204F（やはり子供同士だと\x01",
            "  馴染むのが早いですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BC")

    label("loc_4778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_47BC")

    #C0240
    ChrTalk(
        0x104,
        (
            "#0302F（やっぱ子供同士だと\x01",
            "  馴染むのが早いなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BC")

    SetScenarioFlags(0x0, 4)
    Jump("loc_4814")

    label("loc_47C4")


    #C0241
    ChrTalk(
        0xFE,
        (
            "おねーちゃん、\x01",
            "こんどあそんでね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x153,
        (
            "#1110Fうん、いいよー！\x01",
            "またねー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4814")

    Jump("loc_4B64")

    label("loc_4819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4858")
    SetChrSubChip(0xFE, 0x1)

    #C0243
    ChrTalk(
        0xFE,
        (
            "あーん、ママ～！\x01",
            "もっとご本読んでよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B64")

    label("loc_4858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4866")
    Jump("loc_4B64")

    label("loc_4866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_48C7")
    SetChrSubChip(0xFE, 0x1)

    #C0244
    ChrTalk(
        0xFE,
        "ううん、このご本がいいの。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "だってぼく、\x01",
            "めがみさま大好きなんだもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B64")

    label("loc_48C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_491E")

    #C0246
    ChrTalk(
        0xFE,
        "わーい、わくわく……\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "ママにご本読んでもらうの、\x01",
            "たのしいな～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B64")

    label("loc_491E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_49A9")

    #C0248
    ChrTalk(
        0xFE,
        "あのね、あのね……\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "あっちの方に、だいせーどーっていう\x01",
            "おっきな教会があるんだって～！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "ぼくもいってみたいな～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B64")

    label("loc_49A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_49E8")
    SetChrSubChip(0xFE, 0x1)

    #C0251
    ChrTalk(
        0xFE,
        (
            "あーん、ママ～！\x01",
            "もっとご本読んでよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B64")

    label("loc_49E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4AEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A83")

    #C0252
    ChrTalk(
        0xFE,
        "ぼくね、ぼくね……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "大きくなったら\x01",
            "しんぷさんになるんだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "それでちっちゃい子にね、\x01",
            "ご本を読んであげるんだよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4AE7")

    label("loc_4A83")


    #C0255
    ChrTalk(
        0xFE,
        (
            "ぼくね、大きくなったら\x01",
            "しんぷさんになるんだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "ママみたいにご本を\x01",
            "読んであげるんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE7")

    Jump("loc_4B64")

    label("loc_4AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4B27")
    SetChrSubChip(0xFE, 0x1)

    #C0257
    ChrTalk(
        0xFE,
        (
            "ふええぇ～……\x01",
            "どうなっちゃうの～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B64")

    label("loc_4B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4B64")
    SetChrSubChip(0xFE, 0x1)

    #C0258
    ChrTalk(
        0xFE,
        "わーい、わーい！\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "もっとご本読んで～！\x02",
    )

    CloseMessageWindow()

    label("loc_4B64")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_4310 end

    def Function_12_4B70(): pass

    label("Function_12_4B70")

    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xE, 0x0)

    #C0260
    ChrTalk(
        0xC,
        (
            "こうしてみんな\x01",
            "幸せに暮らしましたとさ。\x01",
            "めでたし、めでたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        "……アビー、面白かった？\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xE,
        "うん、すごくおもしろかった！\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xE,
        (
            "こんどキーアおねーちゃんに\x01",
            "おすすめしてあげる～っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "ふふ、そうね。\x01",
            "それがいいかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_12_4B70 end

    def Function_13_4C69(): pass

    label("Function_13_4C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4C7A")
    Call(0, 14)
    Jump("loc_4C7D")

    label("loc_4C7A")

    Call(0, 5)

    label("loc_4C7D")

    Return()

    # Function_13_4C69 end

    def Function_14_4C7E(): pass

    label("Function_14_4C7E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D12")
    Jump("loc_4D5C")

    label("loc_4D12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D32")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D5C")

    label("loc_4D32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D52")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D5C")

    label("loc_4D52")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D5C")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4D92")
    Call(0, 21)
    Jump("loc_6838")

    label("loc_4D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4F5C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4DB8")
    Call(0, 20)
    Jump("loc_4E2F")

    label("loc_4DB8")


    #C0265
    ChrTalk(
        0xF,
        (
            "ありがとうな、ロイドくん。\x01",
            "さすがに職員だけでは\x01",
            "回収し切れなかったところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xF,
        "また何かあったら相談するよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4E2F")

    Jump("loc_4F57")

    label("loc_4E34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E59")
    Call(0, 52)
    Jump("loc_4F57")

    label("loc_4E59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_4F2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4E77")
    Call(0, 20)
    Jump("loc_4F26")

    label("loc_4E77")


    #C0267
    ChrTalk(
        0xF,
        (
            "延滞本の回収、\x01",
            "よろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xF,
        (
            "今回はクロスベル郊外に\x01",
            "散ってしまっているし、\x01",
            "ノンビリ進めてくれて構わない。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xF,
        (
            "３冊の本が集まったら\x01",
            "私の所に持ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4F26")

    Jump("loc_4F57")

    label("loc_4F2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_4F40")
    Call(0, 49)
    Jump("loc_4F57")

    label("loc_4F40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4F54")
    Call(0, 48)
    Jump("loc_4F57")

    label("loc_4F54")

    Call(0, 20)

    label("loc_4F57")

    Jump("loc_6838")

    label("loc_4F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5126")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4FFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4F82")
    Call(0, 19)
    Jump("loc_4FF9")

    label("loc_4F82")


    #C0270
    ChrTalk(
        0xF,
        (
            "ありがとうな、ロイドくん。\x01",
            "さすがに職員だけでは\x01",
            "回収し切れなかったところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xF,
        "また何かあったら相談するよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4FF9")

    Jump("loc_5121")

    label("loc_4FFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5023")
    Call(0, 52)
    Jump("loc_5121")

    label("loc_5023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_50F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5041")
    Call(0, 19)
    Jump("loc_50F0")

    label("loc_5041")


    #C0272
    ChrTalk(
        0xF,
        (
            "延滞本の回収、\x01",
            "よろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xF,
        (
            "今回はクロスベル郊外に\x01",
            "散ってしまっているし、\x01",
            "ノンビリ進めてくれて構わない。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xF,
        (
            "３冊の本が集まったら\x01",
            "私の所に持ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_50F0")

    Jump("loc_5121")

    label("loc_50F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_510A")
    Call(0, 49)
    Jump("loc_5121")

    label("loc_510A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_511E")
    Call(0, 48)
    Jump("loc_5121")

    label("loc_511E")

    Call(0, 19)

    label("loc_5121")

    Jump("loc_6838")

    label("loc_5126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_52F0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_51C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_514C")
    Call(0, 18)
    Jump("loc_51C3")

    label("loc_514C")


    #C0275
    ChrTalk(
        0xF,
        (
            "ありがとうな、ロイドくん。\x01",
            "さすがに職員だけでは\x01",
            "回収し切れなかったところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xF,
        "また何かあったら相談するよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_51C3")

    Jump("loc_52EB")

    label("loc_51C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51ED")
    Call(0, 52)
    Jump("loc_52EB")

    label("loc_51ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_52BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_520B")
    Call(0, 18)
    Jump("loc_52BA")

    label("loc_520B")


    #C0277
    ChrTalk(
        0xF,
        (
            "延滞本の回収、\x01",
            "よろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xF,
        (
            "今回はクロスベル郊外に\x01",
            "散ってしまっているし、\x01",
            "ノンビリ進めてくれて構わない。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xF,
        (
            "３冊の本が集まったら\x01",
            "私の所に持ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_52BA")

    Jump("loc_52EB")

    label("loc_52BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_52D4")
    Call(0, 49)
    Jump("loc_52EB")

    label("loc_52D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_52E8")
    Call(0, 48)
    Jump("loc_52EB")

    label("loc_52E8")

    Call(0, 18)

    label("loc_52EB")

    Jump("loc_6838")

    label("loc_52F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_585A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B5")

    #C0280
    ChrTalk(
        0x153,
        (
            "#1110Fねえねえ、本がいっぱいあるね！\x02\x03",

            "#1109Fキーアもここで\x01",
            "本を読んでもいい？\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5405")
    Jump("loc_544F")

    label("loc_5405")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5425")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_544F")

    label("loc_5425")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5445")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_544F")

    label("loc_5445")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_544F")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0281
    ChrTalk(
        0xF,
        "ほう、これはこれは……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xF,
        "君は本が好きなのかな？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x153,
        (
            "#1111Fんー、たぶん！\x02\x03",

            "#1110F本のひょうしを見てると\x01",
            "ワクワクする！\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xF,
        (
            "うんうん、気持ちは分かるよ。\x01",
            "僕も本好きが高じて\x01",
            "司書になってしまった口だ。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_55E9")
    Jump("loc_5633")

    label("loc_55E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5609")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5633")

    label("loc_5609")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5629")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5633")

    label("loc_5629")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5633")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0286
    ChrTalk(
        0xF,
        (
            "ロイド君、ぜひ借りてあげなさい。\x01",
            "この子なら何冊でもＯＫだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#0000Fあ、ありがとう、おじさん。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_5712")

    #C0288
    ChrTalk(
        0x102,
        (
            "#0100F（ふふ、ロイドの知り合いが\x01",
            "  司書さんで良かったわね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57AD")

    label("loc_5712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5765")

    #C0289
    ChrTalk(
        0x103,
        (
            "#0200F（ロイドさんのお知り合いが\x01",
            "  司書さんで良かったですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57AD")

    label("loc_5765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_57AD")

    #C0290
    ChrTalk(
        0x104,
        (
            "#0300F（ロイドの知り合いが\x01",
            "  司書さんで良かったよなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57AD")

    SetScenarioFlags(0xB0, 7)
    Jump("loc_5855")

    label("loc_57B5")


    #C0291
    ChrTalk(
        0xF,
        (
            "ロイド君、この子に\x01",
            "ぜひ本を借りてあげなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xF,
        (
            "読む子は育つ……\x01",
            "ぜひぜひ、興味を\x01",
            "伸ばしてあげなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        (
            "#0000Fははは……\x01",
            "じゃあ少し見て行こうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5855")

    Jump("loc_6838")

    label("loc_585A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_59CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5955")

    #C0294
    ChrTalk(
        0xF,
        (
            "セシルには昔から\x01",
            "好きな事をやりなさいと\x01",
            "言ってきたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xF,
        (
            "まさか看護師になるとは\x01",
            "私も思わなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xF,
        (
            "そういえば小さい頃は\x01",
            "よくウルスラ病院を見たいと\x01",
            "ねだっていたな……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xF,
        (
            "あの頃から\x01",
            "憧れていたんだろうかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_59C5")

    label("loc_5955")


    #C0298
    ChrTalk(
        0xF,
        (
            "セシルが看護師になって\x01",
            "母さんは心配しているようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xF,
        (
            "あの子が選んだ道だ。\x01",
            "見守ってやらなくてはね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59C5")

    Jump("loc_6838")

    label("loc_59CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B31")

    #C0300
    ChrTalk(
        0xF,
        (
            "いてて……地下の資料室の\x01",
            "整理をしていたんだがね……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xF,
        (
            "雪崩が発生して\x01",
            "生き埋めになってしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xF,
        (
            "キャサル君が助けに来てくれなければ\x01",
            "窒息していたかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#0006Fそんな大げさな……\x02\x03",

            "#0000Fっていうかおじさん、\x01",
            "何かあれば支援課に\x01",
            "知らせてくれればいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xF,
        (
            "ハハ、すまない。\x01",
            "連絡する間もなかったのでね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5BA5")

    label("loc_5B31")


    #C0305
    ChrTalk(
        0xF,
        (
            "地下の資料室を整理して\x01",
            "一般公開するのが僕の夢なんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xF,
        (
            "書籍が多すぎて、とても\x01",
            "全ては無理なんだけれどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BA5")

    Jump("loc_6838")

    label("loc_5BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5D19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CBA")

    #C0307
    ChrTalk(
        0xF,
        (
            "今日は新書購入の\x01",
            "リストを纏めているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xF,
        (
            "この作者のシリーズは\x01",
            "ウチでも一番の人気でね。\x01",
            "複数冊購入しておかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x101,
        (
            "#0000Fはは……クロスベル市は\x01",
            "人口が多いからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xF,
        (
            "借りる人は借りてくれるという事だね。\x01",
            "うふふ、嬉しいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5D14")

    label("loc_5CBA")


    #C0311
    ChrTalk(
        0xF,
        (
            "蔵書の購入費は元々市民のものだ。\x01",
            "みんなもっと気兼ねなく\x01",
            "借りていってほしいものだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D14")

    Jump("loc_6838")

    label("loc_5D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E91")

    #C0312
    ChrTalk(
        0xF,
        (
            "ロイド君、午後から\x01",
            "顔を出すなんて珍しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xF,
        (
            "もしかして今日は\x01",
            "お休みだったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0000Fおじさん……\x01",
            "……いや、残念ながら。\x02\x03",

            "支援課は休みって少なくてさ。\x01",
            "今日も朝から仕事なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x103,
        (
            "#0200F最近分かりましたが、\x01",
            "結構忙しいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xF,
        (
            "はは、そうか。\x01",
            "まあ警察だからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xF,
        (
            "図書館はきっちり休みがあるよ。\x01",
            "公務員の中でも特に気楽だね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F07")

    label("loc_5E91")


    #C0318
    ChrTalk(
        0xF,
        (
            "この市立図書館は\x01",
            "週に１日、きっちり休みがある。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xF,
        (
            "まあ僕は司書職だから、\x01",
            "休みでも雑用をすることがあるけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F07")

    Jump("loc_6838")

    label("loc_5F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_60A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5F71")

    #C0320
    ChrTalk(
        0xF,
        "ありがとうな、ロイドくん。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xF,
        "また何かあったら相談するよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F74")

    label("loc_5F71")

    Call(0, 17)

    label("loc_5F74")

    Jump("loc_60A3")

    label("loc_5F79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D5, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D6, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FB0")
    Call(0, 47)
    Jump("loc_60A3")

    label("loc_5FB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_6077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5FCE")
    Call(0, 15)
    Jump("loc_6072")

    label("loc_5FCE")


    #C0322
    ChrTalk(
        0xF,
        (
            "延滞本の回収、\x01",
            "よろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xF,
        (
            "３冊の本が集まったら\x01",
            "私の所に持ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xF,
        (
            "ああ、そこまで急ぎじゃないから\x01",
            "ゆっくりやってくれて結構だからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6072")

    Jump("loc_60A3")

    label("loc_6077")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_608C")
    Call(0, 44)
    Jump("loc_60A3")

    label("loc_608C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_60A0")
    Call(0, 43)
    Jump("loc_60A3")

    label("loc_60A0")

    Call(0, 15)

    label("loc_60A3")

    Jump("loc_6838")

    label("loc_60A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6244")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_610D")

    #C0325
    ChrTalk(
        0xF,
        "ありがとうな、ロイドくん。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xF,
        "また何かあったら相談するよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6110")

    label("loc_610D")

    Call(0, 17)

    label("loc_6110")

    Jump("loc_623F")

    label("loc_6115")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D5, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D6, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_614C")
    Call(0, 47)
    Jump("loc_623F")

    label("loc_614C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_6213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_616A")
    Call(0, 16)
    Jump("loc_620E")

    label("loc_616A")


    #C0327
    ChrTalk(
        0xF,
        (
            "延滞本の回収、\x01",
            "よろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xF,
        (
            "３冊の本が集まったら\x01",
            "私の所に持ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xF,
        (
            "ああ、そこまで急ぎじゃないから\x01",
            "ゆっくりやってくれて結構だからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_620E")

    Jump("loc_623F")

    label("loc_6213")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_6228")
    Call(0, 44)
    Jump("loc_623F")

    label("loc_6228")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_623C")
    Call(0, 43)
    Jump("loc_623F")

    label("loc_623C")

    Call(0, 16)

    label("loc_623F")

    Jump("loc_6838")

    label("loc_6244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_63E0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_62B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_62A9")

    #C0330
    ChrTalk(
        0xF,
        "ありがとうな、ロイドくん。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xF,
        "また何かあったら相談するよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_62AC")

    label("loc_62A9")

    Call(0, 17)

    label("loc_62AC")

    Jump("loc_63DB")

    label("loc_62B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D5, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D6, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E8")
    Call(0, 47)
    Jump("loc_63DB")

    label("loc_62E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_63AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6306")
    Call(0, 16)
    Jump("loc_63AA")

    label("loc_6306")


    #C0332
    ChrTalk(
        0xF,
        (
            "延滞本の回収、\x01",
            "よろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xF,
        (
            "３冊の本が集まったら\x01",
            "私の所に持ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xF,
        (
            "ああ、そこまで急ぎじゃないから\x01",
            "ゆっくりやってくれて結構だからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_63AA")

    Jump("loc_63DB")

    label("loc_63AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_63C4")
    Call(0, 44)
    Jump("loc_63DB")

    label("loc_63C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_63D8")
    Call(0, 43)
    Jump("loc_63DB")

    label("loc_63D8")

    Call(0, 17)

    label("loc_63DB")

    Jump("loc_6838")

    label("loc_63E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_682F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66B7")

    #C0335
    ChrTalk(
        0x101,
        (
            "#0000Fおじさん、久し振り。\x01",
            "長い間ご無沙汰してました。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xF,
        (
            "おや？　もしかして……\x01",
            "隣に住んでいたロイド君じゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xF,
        "ははは、いや驚いた！\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xF,
        (
            "そろそろ戻ってくるとは聞いていたが\x01",
            "……こりゃあ見違えたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#0012Fいや、背ばかり伸びちゃって。\x01",
            "中身はまだまだだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xF,
        (
            "そんな事はない。\x01",
            "捜査官の試験にだって\x01",
            "見事に合格したのだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xF,
        (
            "きっとガイ君も\x01",
            "喜んでくれているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#0008Fそう……かな。\x02\x03",

            "……だとしたら俺も嬉しいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xF,
        "うむ、きっとそうだとも。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xF,
        (
            "僕は司書の仕事があるから\x01",
            "不在がちになってしまうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xF,
        (
            "母さんはいつも家にいるはずだ。\x01",
            "何かあったら母さんを頼りなさい、\x01",
            "……いいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#0000Fうん、そうさせて\x01",
            "もらうと思う。\x02\x03",

            "#0003F……またお世話になります、\x01",
            "おじさん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 7)
    Jump("loc_682A")

    label("loc_66B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67CA")

    #C0347
    ChrTalk(
        0xF,
        (
            "ふむ、ロイド君。\x01",
            "本を借りていかないかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#0012Fはは……そう言えばおじさんには\x01",
            "昔から本を勧められたような。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xF,
        (
            "ふふ、本はいいよ。\x01",
            "囲まれているだけで落ち着く。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xF,
        (
            "まあよかったら\x01",
            "ゆっくり見ていきたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xF,
        (
            "ここの蔵書数は\x01",
            "相当なものだからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_682A")

    label("loc_67CA")


    #C0352
    ChrTalk(
        0xF,
        (
            "君たちもよかったら\x01",
            "ゆっくり見ていきたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xF,
        (
            "ふふ、ここの蔵書数は\x01",
            "相当なものだからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_682A")

    Jump("loc_6838")

    label("loc_682F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6838")

    label("loc_6838")

    SetChrSubChip(0xF, 0x0)
    TalkEnd(0xF)
    Return()

    # Function_14_4C7E end

    def Function_15_6840(): pass

    label("Function_15_6840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A24")

    #C0354
    ChrTalk(
        0xF,
        (
            "ううむ、また\x01",
            "返却数が合わないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xF,
        (
            "うちも人手が足りていないくてね。\x01",
            "管理が行き届いていないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xF,
        (
            "期限どおりに\x01",
            "本を返却してくれない人って\x01",
            "結構いるんだよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x101,
        (
            "#0005Fそうなんだ。\x01",
            "おじさんも大変だね……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_69B3")

    #C0358
    ChrTalk(
        0xF,
        (
            "うむ、だけど\x01",
            "ロイド君たちが手伝ってくれた\x01",
            "おかげで幾分助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xF,
        (
            "司書としては\x01",
            "きちんと管理したい所だからねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1C")

    label("loc_69B3")


    #C0360
    ChrTalk(
        0xF,
        (
            "うむ、中には\x01",
            "長期間借りっ放しになっている\x01",
            "人もいてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xF,
        (
            "たぶん忘れちゃってるんじゃ\x01",
            "ないかなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A1C")

    SetScenarioFlags(0x0, 5)
    Jump("loc_6A98")

    label("loc_6A24")


    #C0362
    ChrTalk(
        0xF,
        (
            "こちらも人手が足りなくてね。\x01",
            "管理が行き届いていないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xF,
        (
            "やっぱり管理費の予算も\x01",
            "きちんと計上しようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A98")

    Return()

    # Function_15_6840 end

    def Function_16_6A99(): pass

    label("Function_16_6A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BA7")

    #C0364
    ChrTalk(
        0xF,
        (
            "この図書館の地下書庫には\x01",
            "古い書籍や未整理の資料なんかが\x01",
            "大量に保管されているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xF,
        (
            "……たまにもぐると\x01",
            "稀覯#4Rきこう#本が見つかったりしてね、\x01",
            "幸せな気分になれるよ。\x02",
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
            "#0000F（おじさんは本当に\x01",
            "  本好きだなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6C13")

    label("loc_6BA7")


    #C0367
    ChrTalk(
        0xF,
        (
            "地下書庫の書籍は\x01",
            "公開手続きが追いつかずに\x01",
            "非公開になっているんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xF,
        "本好きにとっては楽園だよ。\x02",
    )

    CloseMessageWindow()

    label("loc_6C13")

    Return()

    # Function_16_6A99 end

    def Function_17_6C14(): pass

    label("Function_17_6C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CF0")

    #C0369
    ChrTalk(
        0xF,
        (
            "この図書館は一人三冊しか\x01",
            "借りられないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xF,
        (
            "返却本の整理係が足りていなくてね、\x01",
            "これ以上冊数を増やすと\x01",
            "業務が追いつかないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xF,
        (
            "ふむ、せめて五冊借りられれば\x01",
            "使い勝手もよくなるんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D50")

    label("loc_6CF0")


    #C0372
    ChrTalk(
        0xF,
        (
            "この図書館も\x01",
            "人手が足りていなくてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xF,
        (
            "もう少し使い勝手を\x01",
            "よくできればいいんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D50")

    Return()

    # Function_17_6C14 end

    def Function_18_6D51(): pass

    label("Function_18_6D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7F")

    #C0374
    ChrTalk(
        0xF,
        "キーア君は大したものだよ。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xF,
        (
            "貸し出した本をあっという間に\x01",
            "読んでしまうなんてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        (
            "#0100Fええ、あの子は本当に\x01",
            "本好きみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xF,
        (
            "ふふ、僕も\x01",
            "本好き仲間ができて嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xF,
        (
            "またみんなで本を借りにおいで。\x01",
            "いいものを用意しておくから。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x103,
        "#0200Fはい、喜ぶと思います。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6F2A")

    label("loc_6E7F")


    #C0380
    ChrTalk(
        0xF,
        "キーア君は大したものだよ。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xF,
        (
            "将来は僕の跡をついで\x01",
            "司書さんになるかもしれないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#0012Fあはははは……\x01",
            "（おじさんもすっかり\x01",
            "  気に入っちゃったみだいだな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F2A")

    Return()

    # Function_18_6D51 end

    def Function_19_6F2B(): pass

    label("Function_19_6F2B")


    #C0383
    ChrTalk(
        0xF,
        (
            "港湾公園の方では\x01",
            "事件があったそうだねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xF,
        (
            "ふぅむ、あの辺りは\x01",
            "ビジネス街だというのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xF,
        "朝から物騒な事だよ。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_19_6F2B end

    def Function_20_6FA6(): pass

    label("Function_20_6FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70D7")

    #C0386
    ChrTalk(
        0xF,
        (
            "昔、ガイ君が警察に勤めていた時は\x01",
            "本当に楽しそうだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xF,
        (
            "まだ新人だったころ、\x01",
            "気のあう相棒が出来たって\x01",
            "食卓で話していたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xF,
        (
            "あれから１０年も\x01",
            "経っていないのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xF,
        (
            "ガイ君も、セシルも、ロイド君も……\x01",
            "みんな変わってしまったねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        "#0008F……………そうだね………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7137")

    label("loc_70D7")


    #C0391
    ChrTalk(
        0xF,
        (
            "ハハ、すまないな。\x01",
            "感傷に浸ってしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xF,
        (
            "こういう事は本当は\x01",
            "母さんの仕事なんだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7137")

    Return()

    # Function_20_6FA6 end

    def Function_21_7138(): pass

    label("Function_21_7138")


    #C0393
    ChrTalk(
        0xF,
        (
            "そろそろ日が落ちるねえ……\x01",
            "図書館も閉館時間だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xF,
        (
            "ロイド君、忘れ物を\x01",
            "しないように帰るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xF,
        "それじゃあ、また明日。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71EC")

    #C0396
    ChrTalk(
        0x101,
        "#0000Fうん、おじさんもお疲れ様。\x02",
    )

    CloseMessageWindow()

    label("loc_71EC")

    SetScenarioFlags(0x0, 5)
    Return()

    # Function_21_7138 end

    def Function_22_71F0(): pass

    label("Function_22_71F0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7284")
    Jump("loc_72CE")

    label("loc_7284")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_72A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_72CE")

    label("loc_72A4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72C4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_72CE")

    label("loc_72C4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_72CE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_73EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7383")

    #C0397
    ChrTalk(
        0xFE,
        (
            "……新発見だ。\x01",
            "図書館にくると\x01",
            "意外と仕事がはかどるんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "静かで集中できるし、\x01",
            "うるさい上司もいないしな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_73E5")

    label("loc_7383")


    #C0399
    ChrTalk(
        0xFE,
        (
            "まさか図書館に\x01",
            "こんな効能があるなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "人がほとんどいねえのが\x01",
            "オレ的にはグッドだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73E5")

    Jump("loc_7608")

    label("loc_73EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_744D")
    SetChrSubChip(0xFE, 0x0)

    #C0401
    ChrTalk(
        0xFE,
        "あーでもない、こーでもない……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "うーん、ここは\x01",
            "やっぱこうしておくか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7608")

    label("loc_744D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74B4")

    #C0403
    ChrTalk(
        0xFE,
        "せっせ……\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "こっちには\x01",
            "浮かれてる暇はねえんだよ。\x01",
            "仕事仕事っと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_751C")

    label("loc_74B4")


    #C0405
    ChrTalk(
        0xFE,
        (
            "せっせ……\x01",
            "少しはマジで仕事しねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "書類の提出が遅れたら\x01",
            "予算編成が止まっちまうんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_751C")

    Jump("loc_7608")

    label("loc_7521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_75FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75BB")

    #C0407
    ChrTalk(
        0xFE,
        (
            "市庁舎の方はバタバタしてるんだ。\x01",
            "集中できないから\x01",
            "仕事を持ってきちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "なにせ一週間後には\x01",
            "予算議会だからな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_75FA")

    label("loc_75BB")


    #C0409
    ChrTalk(
        0xFE,
        (
            "とほほ、場所を移してまで\x01",
            "仕事に励んでるオレってマジメ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75FA")

    Jump("loc_7608")

    label("loc_75FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7608")

    label("loc_7608")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_71F0 end

    def Function_23_7610(): pass

    label("Function_23_7610")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_76A4")
    Jump("loc_76EE")

    label("loc_76A4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_76C4")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_76EE")

    label("loc_76C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76E4")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_76EE")

    label("loc_76E4")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_76EE")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8051")
    EventBegin(0x0)
    Fade(500)
    OP_68(29400, 5020, -14320, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18590, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, 29930, 4030, -13780, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_778E")
    SetChrPos(0x102, 28660, 4030, -13530, 135)
    Jump("loc_77D5")

    label("loc_778E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77B4")
    SetChrPos(0x103, 28660, 4030, -13530, 135)
    Jump("loc_77D5")

    label("loc_77B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77D5")
    SetChrPos(0x104, 28660, 4030, -13530, 135)

    label("loc_77D5")

    SetChrPos(0x153, 27220, 4030, -14020, 135)
    SetChrSubChip(0x11, 0x2)
    OP_0D()

    #C0410
    ChrTalk(
        0x11,
        "#2905F#11Pあら、奇遇ですわね。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        "#0005Fマリアベルさん……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7874")

    #C0412
    ChrTalk(
        0x102,
        (
            "#0102F#5Pベル……\x01",
            "珍しい場所にいるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78F5")

    label("loc_7874")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78B5")

    #C0413
    ChrTalk(
        0x103,
        (
            "#0202F#5P珍しい場所で\x01",
            "お会いしますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78F5")

    label("loc_78B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78F5")

    #C0414
    ChrTalk(
        0x104,
        (
            "#0305F#5Pおおっ。\x01",
            "珍しい場所にいるッスね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78F5")


    #C0415
    ChrTalk(
        0x11,
        (
            "#2904Fフフ、たまの休日に\x01",
            "立ち寄ることは結構ありますわ。\x02\x03",

            "図書館には導力ネットにはない\x01",
            "莫大な知の集積がある……\x02\x03",

            "#2902F活用しない手はありませんもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        "#0012Fお、お見それしました。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A22")

    #C0417
    ChrTalk(
        0x102,
        (
            "#0104F#5Pふふっ……\x01",
            "本当に勉強家なんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x11,
        "#2904Fあら、それはエリィもでしょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AA2")

    label("loc_7A22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A6B")

    #C0419
    ChrTalk(
        0x103,
        (
            "#0204F#5P……なるほど。\x01",
            "確かに一理ありますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA2")

    label("loc_7A6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AA2")

    #C0420
    ChrTalk(
        0x104,
        "#0309F#5Pは～……頭が下がるッス。\x02",
    )

    CloseMessageWindow()

    label("loc_7AA2")

    SetChrSubChip(0x11, 0x0)
    Sleep(300)

    #C0421
    ChrTalk(
        0x11,
        "#2900F……まあ、それはそれとして。\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x153,
        (
            "#1101Fじー……\x02\x03",

            "#1110Fねーねー、ロイド。\x01",
            "このお姉ちゃんもシリアイ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B1F():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B1F)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B46")
    TurnDirection(0x102, 0x153, 500)
    Jump("loc_7B79")

    label("loc_7B46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B62")
    TurnDirection(0x103, 0x153, 500)
    Jump("loc_7B79")

    label("loc_7B62")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B79")
    TurnDirection(0x104, 0x153, 500)

    label("loc_7B79")


    #C0423
    ChrTalk(
        0x101,
        "#0002F#11Pあ、ああ……まあね。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x11,
        (
            "#2904F#11Pフフ、事情は承知していますわ。\x02\x03",

            "#2902F──その子が出品される予定だった\x01",
            "《人形》というわけですわね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_7C4B():
        TurnDirection(0x101, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C4B)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C78")

    def lambda_7C6B():
        TurnDirection(0x102, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C6B)
    Jump("loc_7CB7")

    label("loc_7C78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C9A")

    def lambda_7C8D():
        TurnDirection(0x103, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7C8D)
    Jump("loc_7CB7")

    label("loc_7C9A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7CB7")

    def lambda_7CAF():
        TurnDirection(0x104, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7CAF)

    label("loc_7CB7")

    Sleep(200)

    #C0425
    ChrTalk(
        0x101,
        "#0011Fなっ……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D0C")

    #C0426
    ChrTalk(
        0x102,
        "#0101F#5Pベル、どうしてそれを……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D71")

    label("loc_7D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D42")

    #C0427
    ChrTalk(
        0x103,
        "#0205F#5P……何故それを……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D71")

    label("loc_7D42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D71")

    #C0428
    ChrTalk(
        0x104,
        "#0305F#5Pなんでそれを……\x02",
    )

    CloseMessageWindow()

    label("loc_7D71")


    #C0429
    ChrTalk(
        0x11,
        (
            "#2906Fふう……\x01",
            "あれだけの騒ぎを起こして\x01",
            "気付かない方がおかしいですわ。\x02\x03",

            "#2902Fあなた方が脱出する所は\x01",
            "遠目でしたけど見かけましたし。\x02\x03",

            "#2904Fここ一週間で流れた情報を\x01",
            "総合してみたら当然の推測です。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x101,
        (
            "#0006Fそ、そうですか……\x02\x03",

            "#0001F……あの、マリアベルさん。\x01",
            "その事はくれぐれも──\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x11,
        (
            "#2903Fもちろん分かっていますわ。\x02\x03",

            "#2902Fですが、あの場にわたくしが\x01",
            "居合わせたのも何かの縁でしょう。\x02\x03",

            "もし困った事があったら\x01",
            "遠慮なく頼って欲しいですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x101,
        (
            "#0004Fマリアベルさん……\x01",
            "どうもありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FA9")

    #C0433
    ChrTalk(
        0x102,
        "#0102F#5Pベル……本当にありがとう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_801A")

    label("loc_7FA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FE5")

    #C0434
    ChrTalk(
        0x103,
        "#0204F#5P……ご配慮、感謝します。\x02",
    )

    CloseMessageWindow()
    Jump("loc_801A")

    label("loc_7FE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_801A")

    #C0435
    ChrTalk(
        0x104,
        "#0304F#5Pいや、本当に感謝ッス。\x02",
    )

    CloseMessageWindow()

    label("loc_801A")


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
    Jump("loc_8522")

    label("loc_8051")

    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x153, 0)
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80E5")
    Jump("loc_812F")

    label("loc_80E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8105")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_812F")

    label("loc_8105")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8125")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_812F")

    label("loc_8125")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_812F")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_831B")

    #C0437
    ChrTalk(
        0x153,
        (
            "#1106Fんー、だったらいいや。\x02\x03",

            "#1110Fキーア、ロイドとも\x01",
            "いっしょにいたいモン。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x11,
        "#2905Fあら、それは残念ですわ。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8268")
    Jump("loc_82B2")

    label("loc_8268")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8288")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_82B2")

    label("loc_8288")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82A8")
    OP_52(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_82B2")

    label("loc_82A8")

    OP_52(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_82B2")

    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Sleep(300)

    #C0439
    ChrTalk(
        0x11,
        "#2910Fジロッ……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x101,
        "#0011F（お、俺のせいなのか！？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_851E")

    label("loc_831B")


    #C0441
    ChrTalk(
        0x11,
        (
            "#2902Fふふ、それにしても……\x02\x03",

            "本当にローゼンベルクの\x01",
            "人形以上の可愛さですわね。\x02\x03",

            "#2909Fキーアさんといったかしら？\x01",
            "わたくしのお家に\x01",
            "遊びに来るつもりはない？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x153,
        "#1105Fロイドたちといっしょに？\x02",
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x11,
        (
            "#2901Fいえ、少なくとも\x01",
            "ロイドさんは除外ですわね。\x02",
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
        "#0006F（まだ微妙に敵視されてる……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84AE")

    #C0445
    ChrTalk(
        0x102,
        "#0106F#5P（災難ね……ロイド。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_851B")

    label("loc_84AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84E4")

    #C0446
    ChrTalk(
        0x103,
        "#0204F#5P（ご愁傷様です。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_851B")

    label("loc_84E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_851B")

    #C0447
    ChrTalk(
        0x104,
        "#0309F#5P（わはは、いい気味だ。）\x02",
    )

    CloseMessageWindow()

    label("loc_851B")

    SetScenarioFlags(0x1, 0)

    label("loc_851E")

    SetChrSubChip(0x11, 0x0)

    label("loc_8522")

    SetChrSubChip(0x11, 0x0)
    TalkEnd(0x11)
    Return()

    # Function_23_7610 end

    def Function_24_852A(): pass

    label("Function_24_852A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 1)), scpexpr(EXPR_END)), "loc_85F8")

    #C0448
    ChrTalk(
        0x12,
        (
            "#3504Fさてと、帝国のお仕事は\x01",
            "済ませたワケだし。\x02\x03",

            "#3500Fもうちょいクロスベルで\x01",
            "のんびりさせて貰うかなァ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        (
            "#0003F（……本当に判らない人だ……\x01",
            "  何をどこまで知ってるんだろう……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A16")

    label("loc_85F8")

    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x0, 300)

    #C0450
    ChrTalk(
        0x12,
        (
            "#3500Fん、お前らも読書か？\x02\x03",

            "#3509Fいや～、奇遇だなァ。\x01",
            "オレも読書の友ができて嬉しいぜ～♪\x02",
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
            "#0006Fいや、あの……\x01",
            "どこから突っ込んだらいいのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x103,
        (
            "#0203Fどう考えても\x01",
            "読書目的じゃないような……\x01",
            "その割に馴染んでるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x104,
        (
            "#0306F（……ダメだ、真面目に考えると\x01",
            "  頭がこんがらがってきたぜ。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 2)), scpexpr(EXPR_END)), "loc_89BA")

    #C0454
    ChrTalk(
        0x102,
        (
            "#0105Fというかレクターさん、\x01",
            "用事があって帝国に帰られたんじゃ\x01",
            "なかったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x12,
        (
            "#3505Fん、ああ……\x02\x03",

            "#3500F帝国っつっても\x01",
            "そんなに時間は掛かんねえぞ？\x02\x03",

            "ベルガード門の近くだしな。\x02",
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
        "#0005F（……ベルガード門の近く？）\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        "#0105F（まさか……《ガレリア要塞》！？）\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        (
            "#0305F（それはヤバすぎだろ……\x01",
            "  帝国の最重要拠点の一つだぞ！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x103,
        (
            "#0211F（民間人が用事のある場所じゃ\x01",
            "  ありませんよね。\x01",
            "  本当に何者なんでしょうか……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A0C")

    label("loc_89BA")


    #C0460
    ChrTalk(
        0x102,
        (
            "#0106F（……私も…………\x01",
            "  ここはまともに相手をしない方が\x01",
            "  良さそうね……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A0C")

    OP_93(0x12, 0x5A, 0x0)
    SetScenarioFlags(0xEF, 1)

    label("loc_8A16")

    TalkEnd(0xFE)
    Return()

    # Function_24_852A end

    def Function_25_8A1A(): pass

    label("Function_25_8A1A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8AF9")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0461
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　 ～　今月の新刊　～\x01",
            "　マルクと深き森の魔女・下\x01\x01",
            "１階の本棚に入っております。\x01",
            "　興味のある方は是非どうぞ。\x01",
            "　★人気の本ですので、\x01",
            "　　借りようと考えている方は\x01",
            "　　お早めに！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_8DAE")

    label("loc_8AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8B4C")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0462
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　～　今月の新刊　～\x01",
            "　　　　　準備中\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_8DAE")

    label("loc_8B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8BE1")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0463
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　 ～　今月の新刊　～\x01",
            "　　　聖女と白い狼・下\x01\x01",
            "１階の本棚に入っております。\x01",
            "　興味のある方は是非どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_8DAE")

    label("loc_8BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8C8E")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0464
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　 ～　今月の新刊　～\x01",
            "　マルクと深き森の魔女・中\x01",
            "　　　　 季刊・舌鼓\x01\x01",
            "１階の本棚に入っております。\x01",
            "　興味のある方は是非どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_8DAE")

    label("loc_8C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8D23")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0465
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　 ～　今月の新刊　～\x01",
            "　　　聖女と白い狼・上\x01\x01",
            "１階の本棚に入っております。\x01",
            "　興味のある方は是非どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_8DAE")

    label("loc_8D23")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0466
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　 ～　今月の新刊　～\x01",
            "　マルクと深き森の魔女・上\x01\x01",
            "１階の本棚に入っております。\x01",
            "　興味のある方は是非どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_8DAE")

    TalkEnd(0xFF)
    Return()

    # Function_25_8A1A end

    def Function_26_8DB2(): pass

    label("Function_26_8DB2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0467
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『マルクと深き森の魔女』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8E93")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【上巻を読む】\x01",      # 0
            "【中巻を読む】\x01",      # 1
            "【下巻を読む】\x01",      # 2
            "【やめる】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E66")
    UseItem(0x2D6, 0xFF)

    label("loc_8E66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E7A")
    UseItem(0x2DD, 0xFF)

    label("loc_8E7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E8E")
    UseItem(0x2DE, 0xFF)

    label("loc_8E8E")

    Jump("loc_8F64")

    label("loc_8E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8F14")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【上巻を読む】\x01",      # 0
            "【中巻を読む】\x01",      # 1
            "【やめる】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EFB")
    UseItem(0x2D6, 0xFF)

    label("loc_8EFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F0F")
    UseItem(0x2DD, 0xFF)

    label("loc_8F0F")

    Jump("loc_8F64")

    label("loc_8F14")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【上巻を読む】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F64")
    UseItem(0x2D6, 0xFF)

    label("loc_8F64")

    TalkEnd(0xFF)
    Return()

    # Function_26_8DB2 end

    def Function_27_8F68(): pass

    label("Function_27_8F68")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0468
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『季刊・舌鼓』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_905D")
    UseItem(0x2DC, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_905D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0469
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピが書かれていた。\x02",
        )
    )

    CloseMessageWindow()

    #A0470
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x12)

    label("loc_905D")

    TalkEnd(0xFF)
    Return()

    # Function_27_8F68 end

    def Function_28_9061(): pass

    label("Function_28_9061")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0471
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『大陸を動かした美人たち』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90E4")
    UseItem(0x2D7, 0xFF)

    label("loc_90E4")

    TalkEnd(0xFF)
    Return()

    # Function_28_9061 end

    def Function_29_90E8(): pass

    label("Function_29_90E8")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0472
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『余った五分の有効な使い方』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_916D")
    UseItem(0x2D8, 0xFF)

    label("loc_916D")

    TalkEnd(0xFF)
    Return()

    # Function_29_90E8 end

    def Function_30_9171(): pass

    label("Function_30_9171")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0473
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『鉄道マニアのススメ』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91F0")
    UseItem(0x2D5, 0xFF)

    label("loc_91F0")

    TalkEnd(0xFF)
    Return()

    # Function_30_9171 end

    def Function_31_91F4(): pass

    label("Function_31_91F4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0474
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『クロスベル怪奇全集』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9273")
    UseItem(0x2D9, 0xFF)

    label("loc_9273")

    TalkEnd(0xFF)
    Return()

    # Function_31_91F4 end

    def Function_32_9277(): pass

    label("Function_32_9277")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0475
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『聖女と白い狼』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_932D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【上巻を読む】\x01",      # 0
            "【下巻を読む】\x01",      # 1
            "【やめる】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9314")
    UseItem(0x2DF, 0xFF)

    label("loc_9314")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9328")
    UseItem(0x2E0, 0xFF)

    label("loc_9328")

    Jump("loc_937D")

    label("loc_932D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【上巻を読む】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_937D")
    UseItem(0x2DF, 0xFF)

    label("loc_937D")

    TalkEnd(0xFF)
    Return()

    # Function_32_9277 end

    def Function_33_9381(): pass

    label("Function_33_9381")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0476
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『アルカンシェル・ファンブック』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_940A")
    UseItem(0x2DA, 0xFF)

    label("loc_940A")

    TalkEnd(0xFF)
    Return()

    # Function_33_9381 end

    def Function_34_940E(): pass

    label("Function_34_940E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9425")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97F9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Ａ～Ｚ")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【ＩＢＣ】\x01",      # 0
            "【ＺＣＦ】\x01",      # 1
            "【やめる】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_962C")
    SetChrName("")
    MenuTitle(-1, 25, 0, "ＩＢＣ（International Bank of Crossbell）")
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0477
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《クロスベル国際銀行》の略称。\x01",
            "大陸全土から集まってくる莫大な資産を\x01",
            "管理・運用する巨大銀行で、\x01",
            "クロスベルのみならず、国際的な金融・\x01",
            "経済市場を長年に渡って支えてきた。\x02\x03",

            "投資活動や金融商品の開発のみならず、\x01",
            "テーマパークの運営なども手がけており、\x01",
            "エプスタイン財団の《導力ネットワーク計画》にも\x01",
            "積極的な資金提供を行っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_962C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97F4")
    MenuTitle(-1, 25, 0, "ＺＣＦ（Zeiss Central Factory）")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0478
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《ツァイス中央工房》の略称。\x01",
            "リベール王国のツァイス市に拠点を構え、\x01",
            "オーブメントの発明者、エプスタイン博士の\x01",
            "直弟子であるＡ・ラッセル博士によって、\x01",
            "ツァイス時計師組合と協同で設立された\x01",
            "「ツァイス技術工房」を前身とする。\x02\x03",

            "世界に先駆けて導力飛行船の開発に\x01",
            "成功した大陸有数の導力器メーカーで、\x01",
            "近年ではリベール王国軍所属の\x01",
            "高速巡洋艦《アルセイユ》を完成させた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97F4")

    Jump("loc_9425")

    label("loc_97F9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_34_940E end

    def Function_35_9806(): pass

    label("Function_35_9806")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_981D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0D1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "ア行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【アルカンシェル】\x01",        # 0
            "【アルテリア法国】\x01",        # 1
            "【ヴェルヌ社】\x01",            # 2
            "【エレボニア帝国】\x01",        # 3
            "【エプスタイン財団】\x01",      # 4
            "【やめる】\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A0D")
    MenuTitle(-1, 25, 0, "アルカンシェル")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0479
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州に存在する\x01",
            "国際的にも有名な劇団。\x02\x03",

            "アクロバティックなパフォーマンスと\x01",
            "華麗かつ情熱的な舞台で\x01",
            "多くの観客を魅了し続けている。\x02\x03",

            "《炎の舞姫》の異名で知られる\x01",
            "現在の看板女優イリア・プラティエは\x01",
            "特に人気が高く、周辺諸国にも\x01",
            "熱狂的なファンが多い。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B72")
    MenuTitle(-1, 25, 0, "アルテリア法国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0480
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀教会の総本山にあたる都市国家。\x01",
            "ゼムリア大陸の中心部に位置しており、\x01",
            "大陸全土から大勢の信徒や宗教関係者が\x01",
            "集まる聖地としても知られている。\x02\x03",

            "祭儀全般を監督する『典礼省』、\x01",
            "女神の秘蹟を管理するという『封聖省』、\x01",
            "都市の防衛を担当する『僧兵庁』など、\x01",
            "様々な組織が存在している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9B72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CFF")
    MenuTitle(-1, 25, 0, "ヴェルヌ社")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0481
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カルバード共和国に本拠を置く\x01",
            "巨大総合技術メーカー。\x02\x03",

            "エレボニア帝国のラインフォルト社と\x01",
            "双璧をなす武器・兵器開発の老舗として有名だが、\x01",
            "オーブメントが発明されてからは、\x01",
            "あらゆる導力製品の研究・開発を行っている。\x02\x03",

            "中でも導力駆動車の分野においては、\x01",
            "導力バスを始め、自家用車から特殊車両に至るまで\x01",
            "様々な製品を開発している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9CFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F2F")
    MenuTitle(-1, 25, 0, "エレボニア帝国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0482
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州の西に位置する、\x01",
            "《黄金の軍馬》の紋章を掲げる巨大帝国。\x01",
            "現皇帝はユーゲント・ライゼ・アルノール。\x02\x03",

            "大貴族の支配する旧い体制の国家だが、\x01",
            "《鉄血宰相》の異名で知られる軍部出身の\x01",
            "ギリアス・オズボーン宰相の指揮の下、\x01",
            "全土に鉄道が敷かれ、近代化されつつある。\x02\x03",

            "機甲化された正規軍の他、大貴族の私設軍など\x01",
            "巨大な軍事力を保持しており、\x01",
            "周辺諸国に常に緊張を強いている。\x02\x03",

            "なお、昨年リベールで起きた異変の解決に\x01",
            "皇帝の子息、オリヴァルト皇子が協力。\x01",
            "帝国内で大きな話題となった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0CC")
    MenuTitle(-1, 25, 0, "エプスタイン財団")
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0483
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを発明した天才導力学者、\x01",
            "Ｃ・エプスタイン博士の業績を受け継いだ財団。\x01",
            "研究機関、メーカーとしての側面も強く、\x01",
            "通信・情報処理などの分野に特に優れている。\x02\x03",

            "魔法#4Rアーツ#を発動できる《戦術オーブメント》を\x01",
            "開発している唯一のメーカーである他、\x01",
            "近年では通信・情報処理技術を発展させた\x01",
            "《導力ネットワーク計画》に力を入れている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A0CC")

    Jump("loc_981D")

    label("loc_A0D1")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_35_9806 end

    def Function_36_A0DE(): pass

    label("Function_36_A0DE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A0F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A975")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "カ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【怪盗Ｂ】\x01",                          # 0
            "【カルバード共和国】\x01",                # 1
            "【クロスベル自治州】\x01",                # 2
            "【結晶回路／クオーツ】\x01",              # 3
            "【古代遺物／アーティファクト】\x01",      # 4
            "【やめる】\x01",                          # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A398")
    MenuTitle(-1, 25, 0, "怪盗Ｂ")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0484
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大陸を叉に掛ける神出鬼没の大泥棒。\x01",
            "宝石から、果ては導力戦車に至るまで、\x01",
            "国・個人を問わず、数多の盗みを働き、\x01",
            "その鮮やかで華麗な手口から、一部では熱狂的な\x01",
            "ファンまで存在するほど評判となっている。\x02\x03",

            "趣向に富んだメッセージを各所に送りつけ、\x01",
            "仮面と白マントを纏って姿を晒すこともあるが、\x01",
            "その正体は謎に包まれている。\x01",
            "近年では、本人自ら「美の解放活動」を語り、\x01",
            "エレボニア帝国で実行された、不可解ながらも\x01",
            "華麗な一連の犯行が話題に新しい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A398")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4FF")
    MenuTitle(-1, 25, 0, "カルバード共和国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0485
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "百年ほど前に民主化を成し遂げた\x01",
            "クロスベル自治州の東に位置する共和国。\x01",
            "現元首はロックスミス大統領。\x02\x03",

            "広大な国土を持ち、\x01",
            "東方からの移民を受け入れてきたため\x01",
            "多様な文化背景を持つ。\x02\x03",

            "《不戦条約》締結後は沈静化を\x01",
            "見せているが、歴史上エレボニア帝国と\x01",
            "幾度となく衝突を繰り返してきた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A4FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A681")
    MenuTitle(-1, 25, 0, "クロスベル自治州")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0486
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸西部にある自治州。\x01",
            "エレボニア帝国、カルバード共和国という\x01",
            "２大国に挟まれており、\x01",
            "熾烈な領土争いの対象となってきたが、\x01",
            "７０年前に自治州として成立した。\x02\x03",

            "現在、中心のクロスベル市は大陸有数の\x01",
            "巨大貿易都市に成長を遂げており、\x01",
            "帝国～共和国を結ぶ大陸横断鉄道や\x01",
            "国際定期飛行船の中継点となっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A681")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A78E")
    MenuTitle(-1, 25, 0, "結晶回路／クオーツ")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0487
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀石の欠片《セピス》を精製・加工した\x01",
            "結晶構造を持つ回路。\x02\x03",

            "エネルギー源であると同時に、\x01",
            "様々な現象を起こすデバイスでもあるが、\x01",
            "オーブメントの内部にセットされないと\x01",
            "効果を発揮しない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A78E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A970")
    MenuTitle(-1, 25, 0, "古代遺物／アーティファクト")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0488
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントと同じ導力で稼動しながらも\x01",
            "異なる作動原理を持つ、古代文明の導力器。\x02\x03",

            "《古代ゼムリア文明》の時代に\x01",
            "生み出されたと言われ、現代の技術では\x01",
            "解析は不可能とされている。\x02\x03",

            "大陸各地の遺跡から稀に発見されることがあり、\x01",
            "今なお人智を超えた強大な力を\x01",
            "発揮するものも少なくない。\x02\x03",

            "そのため七耀教会ではアーティファクトを\x01",
            "『早すぎた女神の贈り物』と定義し、\x01",
            "その回収・管理を責務としているという。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A970")

    Jump("loc_A0F5")

    label("loc_A975")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_36_A0DE end

    def Function_37_A982(): pass

    label("Function_37_A982")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A999")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC91")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "サ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【七耀教会】\x01",                # 0
            "【七耀石／セプチウム】\x01",      # 1
            "【やめる】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB3D")
    MenuTitle(-1, 25, 0, "七耀教会")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0489
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸で最も広く信仰されている\x01",
            "《空の女神エイドス》を奉じる宗教組織。\x01",
            "アルテリア法国に総本山を持つ。\x02\x03",

            "導力革命以降、影響力は低下したものの\x01",
            "今なお大陸全土に強い影響力を持ち、\x01",
            "学問・教育・医療などの分野を通して、\x01",
            "民衆を啓蒙する立場にある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC8C")
    MenuTitle(-1, 25, 0, "七耀石／セプチウム")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0490
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大陸全般に分布する７種類の貴石群。\x01",
            "古くから宝石として、\x01",
            "神秘の象徴として珍重されてきた。\x02\x03",

            "近代になって、宝石にするには小さすぎる\x01",
            "欠片《セピス》を精製・加工して\x01",
            "クオーツを作る技術が発明された事により、\x01",
            "七耀石資源の重要性は\x01",
            "大陸諸国間で一気に高まった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AC8C")

    Jump("loc_A999")

    label("loc_AC91")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_37_A982 end

    def Function_38_AC9E(): pass

    label("Function_38_AC9E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ACB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B428")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "タ行・上")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【大崩壊】\x01",                    # 0
            "【釣公師団】\x01",                  # 1
            "【導力革命】\x01",                  # 2
            "【導力器／オーブメント】\x01",      # 3
            "【やめる】\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE3B")
    MenuTitle(-1, 25, 0, "大崩壊")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0491
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "約１２００年前に起こったとされる、\x01",
            "古代ゼムリア文明の崩壊のこと。\x01",
            "天変地異が原因とも言われているが詳細は不明。\x02\x03",

            "《大崩壊》によって文明が失われた後、\x01",
            "人々は長きに渡る《暗黒時代》を辿った。\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AE3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFC5")
    MenuTitle(-1, 25, 0, "釣公師団")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0492
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣り文化の普及を目的に活動している、\x01",
            "釣りのプロフェッショナル集団。\x01",
            "元貴族の釣り愛好家、\x01",
            "Ｈ・フィッシャー氏によって発足され、\x01",
            "リベール王国のグランセル市に本部を構える。\x02\x03",

            "釣り場の探訪・調査・開拓にはじまり、\x01",
            "新世代の釣師の発掘や教育、さらに近年では\x01",
            "釣り道具・釣りエサの開発にも携わるなど、\x01",
            "年々その活動の幅を広げている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AFC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B24F")
    MenuTitle(-1, 25, 0, "導力革命")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0493
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "およそ５０年ほど前、\x01",
            "オーブメントが発明されることで起きた\x01",
            "大陸規模での技術革新のこと。\x02\x03",

            "画期的な発明であるにも関わらず\x01",
            "当時の人々は懐疑的だったが、\x01",
            "エプスタイン財団の導力通信器や\x01",
            "ＺＣＦの導力飛行船が世に出るにつれ、\x01",
            "その有用性は大陸全土に認知されていった。\x02\x03",

            "現在では暖房や照明などの日用品から\x01",
            "鉄道や飛行船、戦車や大砲などの兵器まで\x01",
            "ありとあらゆるものが導力化され、\x01",
            "もはやオーブメントは人々にとって\x01",
            "なくてはならないものとなっている。\x02\x03",

            "なお近年、導力機関の小型化に伴い、\x01",
            "ヴェルヌ社やラインフォルト社によって\x01",
            "高性能な導力駆動車の開発が進んでおり、\x01",
            "一般層への普及も始まっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B24F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B423")
    MenuTitle(-1, 25, 0, "導力器／オーブメント")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0494
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ｃ・エプスタイン博士によって\x01",
            "発明された、七耀石から導力を引き出し、\x01",
            "様々な現象を引き起こす機械の総称。\x02\x03",

            "オーブメント内の構造・歯車の動きで、\x01",
            "七耀石を加工した結晶回路を相互干渉せることで\x01",
            "無数のバリエーションの現象を発現させる。\x02\x03",

            "オーブメントの有用性は、バリエーションの\x01",
            "豊富さに加えて、『時間が経てば内部の\x01",
            "導力が回復する』ことにあり、外燃・内燃機関と\x01",
            "較べると経済効率が遙かに高い。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B423")

    Jump("loc_ACB5")

    label("loc_B428")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_38_AC9E end

    def Function_39_B435(): pass

    label("Function_39_B435")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B44C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8C7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "タ行・下")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【導力魔法／オーバルアーツ】\x01",      # 0
            "【導力ネットワーク計画】\x01",          # 1
            "【東方人街】\x01",                      # 2
            "【やめる】\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B61D")
    MenuTitle(-1, 25, 0, "導力魔法／オーバルアーツ")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0495
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エプスタイン財団によって特別に設計された\x01",
            "《戦術オーブメント》に結晶回路#8Rク オ ー ツ#を組み込むことで\x01",
            "発動することができる“魔法”。\x02\x03",

            "一般的には“アーツ”と呼ばれ、\x01",
            "訓練次第で誰もが使える技術として\x01",
            "軍隊・警察・ギルドなどに普及している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B61D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78A")
    MenuTitle(-1, 25, 0, "導力ネットワーク計画")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0496
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エプスタイン財団が研究開発を進めている\x01",
            "革新的な情報ネットワーク計画。\x01",
            "端末同士を導力ケーブルで結び、\x01",
            "莫大な情報のやり取りと処理を可能にしている。\x02\x03",

            "元々はリベールのＺＣＦと共同で開発が\x01",
            "進められていたが、現在はＩＢＣの\x01",
            "資金提供を受け、クロスベル市への\x01",
            "本格的な試験導入が始まった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B78A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8C2")
    MenuTitle(-1, 25, 0, "東方人街")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0497
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カルバード共和国に存在する、\x01",
            "東方系移民が築き上げた大規模な街。\x01",
            "様々な文化、人々、物資が行き交い、\x01",
            "“東西文化の交差点”と呼ばれている。\x02\x03",

            "エキゾチックな建物が建ち並ぶ\x01",
            "観光地としても有名だが、東方系の\x01",
            "巨大シンジケートの存在も囁かれている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B8C2")

    Jump("loc_B44C")

    label("loc_B8C7")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_39_B435 end

    def Function_40_B8D4(): pass

    label("Function_40_B8D4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B8EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD75")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "ナ・ハ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【百日戦役】\x01",      # 0
            "【不戦条約】\x01",      # 1
            "【やめる】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBA0")
    MenuTitle(-1, 25, 0, "百日戦役")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0498
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀暦１１９２年、エレボニア帝国・\x01",
            "リベール王国間で起きた侵略戦争。\x01",
            "帝国による宣戦布告から、七耀教会の\x01",
            "仲立ちで実現した戦争終結まで、\x01",
            "およそ百日で決着をみたことから\x01",
            "こう呼ばれる。\x02\x03",

            "当初リベールは劣勢を強いられ、\x01",
            "国土の大半を帝国軍に占領されたが、\x01",
            "当時の最先端を誇る警備飛行艇を\x01",
            "用いた電撃的な反攻作戦によって\x01",
            "瞬く間にその戦況を覆した。\x02\x03",

            "そもそもの開戦理由については、\x01",
            "両国とも沈黙を保ったため\x01",
            "結局明かされることはなかったが、\x01",
            "後に「不幸な誤解から生じた過ち」\x01",
            "という表現で、帝国政府からリベールに\x01",
            "正式な謝罪声明が出された。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BBA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD70")
    MenuTitle(-1, 25, 0, "不戦条約")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0499
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀暦１２０２年、リベール王国・\x01",
            "エレボニア帝国・カルバード共和国の\x01",
            "３国間で締結された国際条約。\x01",
            "リベールのアリシア女王により提唱され、\x01",
            "同国のエルベ離宮にて調印式が執り行われた。\x02\x03",

            "本条約には法的な強制力はないが、\x01",
            "条約締結後は、クロスベル自治州近郊で\x01",
            "展開されていた帝国・共和国それぞれによる\x01",
            "大規模な軍事演習が撤収されるなど、\x01",
            "緊張状態が大幅に緩和しており、\x01",
            "確実に効果が現れていると言える。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BD70")

    Jump("loc_B8EB")

    label("loc_BD75")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_40_B8D4 end

    def Function_41_BD82(): pass

    label("Function_41_BD82")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BD99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C17F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "マ・ヤ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【ミシュラム】\x01",                        # 0
            "【遊撃士協会／ブレイサーギルド】\x01",      # 1
            "【やめる】\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF3F")
    MenuTitle(-1, 25, 0, "ミシュラム")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0500
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エルム湖南東に位置する高級保養地。\x01",
            "２年前、ＩＢＣが開発に着手してからは\x01",
            "リゾートホテルやテーマパークなどが\x01",
            "建ち並ぶ人気スポットとなった。\x02\x03",

            "《みっしぃ》と呼ばれる\x01",
            "ご当地マスコットキャラクターも\x01",
            "市民や観光客から人気を集めている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C17A")
    MenuTitle(-1, 25, 0, "遊撃士協会／ブレイサーギルド")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0501
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "地域の平和と民間人の保護のために働く\x01",
            "遊撃士#6Rブレイサー#たちの民間団体。\x01",
            "ゼムリア大陸各地に支部があるため、\x01",
            "少なからぬ影響力・発言力を持っている。\x02\x03",

            "何よりも民間人の安全を優先して\x01",
            "行動する理念は理想的とも言えるが、\x01",
            "逆に民間人の安全が脅かされない限り、\x01",
            "国家・公的権力に対して捜査権・逮捕権を\x01",
            "行使できないという組織規約上の弱点もある。\x02\x03",

            "ここクロスベルにおいては、\x01",
            "国際的な案件を多く抱えることから\x01",
            "《風の剣聖》アリオス・マクレインを始め\x01",
            "優秀な人材が集まり、市民の支持を得ている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C17A")

    Jump("loc_BD99")

    label("loc_C17F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_41_BD82 end

    def Function_42_C18C(): pass

    label("Function_42_C18C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C1A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C99B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "ラ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【ラインフォルト社】\x01",        # 0
            "【レミフェリア公国】\x01",        # 1
            "【レマン自治州】\x01",            # 2
            "【リベール王国】\x01",            # 3
            "【猟兵団／イェーガー】\x01",      # 4
            "【やめる】\x01",                  # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DB()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3D3")
    MenuTitle(-1, 25, 0, "ラインフォルト社")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0502
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレボニア帝国に本拠を置く\x01",
            "巨大総合技術メーカー。\x01",
            "元々は火薬を使った大砲・重火器の\x01",
            "製造を専門に行っていた兵器工房だった。\x02\x03",

            "オーブメントが発明されてからは、\x01",
            "導力銃・導力兵器のみならず、\x01",
            "導力鉄道や飛行船などの分野にも手を広げ、\x01",
            "カルバード共和国の《ヴェルヌ社》と並んで、\x01",
            "世界二大メーカーと称されるまでに成長した。 \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C3D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C574")
    MenuTitle(-1, 25, 0, "レミフェリア公国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0503
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸北部に位置する公国。\x01",
            "厳しい北国ではあるものの、\x01",
            "豊かな森と湖に恵まれており、\x01",
            "その風光明媚な景色に魅せられ、\x01",
            "観光目的で訪れる者も多い。\x02\x03",

            "また医療先進国としても有名で、\x01",
            "大陸を代表する医療機器メーカーが集中し、\x01",
            "多くの優秀な医師を輩出している。\x01",
            "クロスベル自治州の聖ウルスラ医科大学も\x01",
            "レミフェリア公国の協力によって設立された。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C574")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C668")
    MenuTitle(-1, 25, 0, "レマン自治州")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0504
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸中部にある自治州。\x01",
            "エプスタイン財団の本部があり、\x01",
            "Ｃ・エプスタイン博士の故郷でもある。\x02\x03",

            "その他、大陸各地に支部を持つ\x01",
            "遊撃士協会の総本部がある事でも有名。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C668")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C86F")
    MenuTitle(-1, 25, 0, "リベール王国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0505
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸南西部に位置する王国。\x01",
            "豊かな自然に彩られた伝統ある国家で、\x01",
            "現在は、老女王アリシアⅡ世の治世の下、\x01",
            "誇り高き平和を保っている。 \x02\x03",

            "周辺諸国より国力では劣るが、\x01",
            "豊富な七耀石資源と優れた技術、\x01",
            "巧みな外交政策によって\x01",
            "対等な関係を築いてきた。\x02\x03",

            "昨年、王国中央にあるヴァレリア湖上に\x01",
            "謎の巨大構造物（詳細不明）が出現し、\x01",
            "王国全土の導力が停止するという異変が\x01",
            "起きたが、軍や遊撃士協会の働きにより\x01",
            "無事解決され、落ち着きを取り戻している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0xBF, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C86F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C996")
    MenuTitle(-1, 25, 0, "猟兵団／イェーガー")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0506
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大陸諸国で活動する傭兵部隊の中でも\x01",
            "特に優秀な部隊を指して使われる称号。\x02\x03",

            "規模や目的に応じた柔軟な契約が行え、\x01",
            "高い戦闘力を期待できることから、\x01",
            "私兵として使われることが多く、\x01",
            "その運用を法律で禁じる国も存在する。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C996")

    Jump("loc_C1A3")

    label("loc_C99B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_42_C18C end

    def Function_43_C9A8(): pass

    label("Function_43_C9A8")

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
        "#6P#0000Fおじさん、こんにちは。\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xF,
        (
            "#11Pおお、ロイドくんか。\x01",
            "よく来たね。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xF,
        "#11P今日は本を借りに来たのかい？\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        (
            "#6P#0000Fいや、今日は仕事で来たんだ。\x02\x03",

            "特務支援課の方に\x01",
            "支援要請を出してたよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x102,
        (
            "#5P#0100F確か、延滞本の回収……\x01",
            "ということでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xF,
        (
            "#11Pおお、そうだそうだ。\x01",
            "確かに依頼を出させてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xF,
        (
            "#11P早速だが仕事の内容を\x01",
            "話させてもらっていいかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x5, 0x1, 0x0)
    Call(0, 45)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBBD")
    Call(0, 46)

    label("loc_CBBD")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_43_C9A8 end

    def Function_44_CBD1(): pass

    label("Function_44_CBD1")

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
            "#11P延滞本の回収について\x01",
            "依頼を出させてもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xF,
        (
            "#11P仕事の内容を\x01",
            "話させてもらっていいかね？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 45)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCD0")
    Call(0, 46)

    label("loc_CCD0")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_44_CBD1 end

    def Function_45_CCE4(): pass

    label("Function_45_CCE4")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDB0")

    #C0516
    ChrTalk(
        0x101,
        (
            "#6P#0006Fえっと……\x01",
            "ゴメン、今は都合が悪くて……\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xF,
        "#11Pふむ、そうかね？\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xF,
        (
            "#11Pそれでは手が空いたら\x01",
            "また頼むとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDB0")

    Return()

    # Function_45_CCE4 end

    def Function_46_CDB1(): pass

    label("Function_46_CDB1")


    #C0519
    ChrTalk(
        0x101,
        "#6P#0000Fああ、大丈夫だよ。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xF,
        "#11Pうむ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xF,
        (
            "#11P近頃、本の返却期限を\x01",
            "延滞している人が多くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xF,
        (
            "#11Pそういった人たちの所に出向いて\x01",
            "延滞本を回収してきて欲しいのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x103,
        "#6P#0203F……なるほど。\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x104,
        (
            "#5P#5P#0300Fま、そこまで難しそうな\x01",
            "仕事じゃなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれで……\x01",
            "延滞本を所持している人の\x01",
            "住所は分かってる？\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xF,
        (
            "#11Pうむ、貸出先は図書カードで\x01",
            "しっかり管理しているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xF,
        "#11Pでは読み上げるよ。\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xF,
        (
            "#11Pまずは……\x01",
            "西通りのアパルトメント\x01",
            "《ベルハイム》のフェイさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xF,
        (
            "#11P次に……\x01",
            "東通りのアパルトメント\x01",
            "《アカシア荘》のクラリスさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xF,
        (
            "#11P最後に……\x01",
            "行政区・クロスベル警察本部の\x01",
            "レイモンドさんだな。\x02",
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
        "#5P#0106Fレ、レイモンドさん……\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x101,
        (
            "#6P#0003Fご、ごめんおじさん。\x01",
            "身内にまで延滞者がいたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xF,
        "#11Pいや、いいのだよ。\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xF,
        (
            "#11P返却期限を忘れるほど\x01",
            "熱心に本を読んでいるのなら、\x01",
            "逆に感心してしまうくらいさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        (
            "#6P#0203F……全てがその限りでは\x01",
            "ないとは思いますけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 350)

    #C0536
    ChrTalk(
        0x103,
        "#6P#0211Fルーズな人は多いですから。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0537
    ChrTalk(
        0x104,
        (
            "#5P#0306Fな、なんだ\x01",
            "そのジットリとした眼差しは……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)

    #C0538
    ChrTalk(
        0x103,
        "#6P#0200Fいえ、別に。\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        (
            "#6P#0003Fと、とにかく。\x02\x03",

            "#0000F依頼内容は分かったから、\x01",
            "さっそく当たってみるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x5A, 0x1F4)

    #C0540
    ChrTalk(
        0xF,
        "#11Pああ、助かるよ。\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xF,
        (
            "#11P３冊の本が集まったら\x01",
            "私の所に持ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xF,
        (
            "#11Pではロイドくん、\x01",
            "よろしく頼んだよ。\x02",
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
            "クエスト【延滞本の回収】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x5, 0x1, 0x1)
    Return()

    # Function_46_CDB1 end

    def Function_47_D394(): pass

    label("Function_47_D394")

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
        "#11Pおや……\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xF,
        (
            "#11Pもしかして、延滞本の回収が\x01",
            "終わったのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x104,
        "#5P#0300Fモチのロンってヤツだぜ。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        "#6P#0000Fはい、おじさん。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0548
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を返した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を返した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0550
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を返した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x2D5, 1)
    SubItemNumber(0x2D6, 1)
    SubItemNumber(0x2D7, 1)

    #C0551
    ChrTalk(
        0xF,
        (
            "#11P……うむ、確かに。\x01",
            "きちんと３冊すべて\x01",
            "回収してきてくれたようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xF,
        (
            "#11Pいや、助かったよ。\x01",
            "ロイドくんたちの手を借りて\x01",
            "本当によかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x102,
        (
            "#5P#0100Fふふ……\x01",
            "そう言ってもらえて光栄です。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x103,
        "#6P#0200F……これにて任務完了ですね。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xF,
        (
            "#11Pああ、お疲れさま。\x01",
            "また何かあったら相談するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x101,
        "#6P#0000Fうん、任せてよ。\x02",
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
            "クエスト【延滞本の回収】\x07\x00",
            "を達成した！\x02",
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

    # Function_47_D394 end

    def Function_48_D709(): pass

    label("Function_48_D709")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D7B6")
    SetChrPos(0x109, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_D7E1")

    label("loc_D7B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D7E1")
    SetChrPos(0x10A, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_D7E1")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D971")

    #C0558
    ChrTalk(
        0x101,
        "#6P#0000Fおじさん、こんにちは。\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xF,
        (
            "#11Pおお、ロイドくんか。\x01",
            "よく来たね。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xF,
        "#11P今日は本を借りに来たのかい？\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x101,
        (
            "#6P#0000Fいや、今日は仕事で来たんだ。\x02\x03",

            "特務支援課の方に\x01",
            "支援要請を出してたよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x102,
        (
            "#5P#0100F確か、延滞本の回収……\x01",
            "ということでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xF,
        (
            "#11Pおお、そうだそうだ。\x01",
            "確かに依頼を出させてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xF,
        (
            "#11P早速だが仕事の内容を\x01",
            "話させてもらっていいかね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB35")

    label("loc_D971")


    #C0565
    ChrTalk(
        0x101,
        "#6P#0000Fおじさん、こんにちは。\x02",
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xF,
        (
            "#11Pおお、ロイドくんか。\x01",
            "よく来たね。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xF,
        "#11Pもしかして、今日は……？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        (
            "#6P#0000Fうん、仕事で来たんだ。\x02\x03",

            "特務支援課の方に\x01",
            "支援要請を出してたよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xF,
        (
            "#11Pおお、やはり……\x01",
            "依頼を確認してくれたのだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xF,
        "#11Pすまない、恩に着るよ。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x102,
        (
            "#5P#0100F延滞本の回収\x01",
            "ということでしたが、\x01",
            "もしかして……？\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xF,
        (
            "#11Pうむ、君たちに頼むのは\x01",
            "２度目になるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xF,
        (
            "#11P早速だが仕事の内容を\x01",
            "話させてもらっていいかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB35")

    OP_29(0x28, 0x1, 0x0)
    Call(0, 50)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB50")
    Call(0, 51)

    label("loc_DB50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DB75")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_DB75")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_48_D709 end

    def Function_49_DB89(): pass

    label("Function_49_DB89")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC36")
    SetChrPos(0x109, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_DC61")

    label("loc_DC36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC61")
    SetChrPos(0x10A, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_DC61")

    OP_0D()

    #C0574
    ChrTalk(
        0xF,
        (
            "#11P延滞本の回収について\x01",
            "依頼を出させてもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xF,
        (
            "#11P仕事の内容を\x01",
            "話させてもらっていいかね？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 50)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCE3")
    Call(0, 51)

    label("loc_DCE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DD08")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_DD08")

    SetChrPos(0x0, 5000, 150, 7800, 90)
    EventEnd(0x5)
    Return()

    # Function_49_DB89 end

    def Function_50_DD1C(): pass

    label("Function_50_DD1C")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDEE")

    #C0576
    ChrTalk(
        0x101,
        (
            "#6P#0006Fごめんおじさん、\x01",
            "今はちょっと都合が悪くて……\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xF,
        "#11Pふむ、そうかね？\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xF,
        (
            "#11Pそれでは手が空いたら\x01",
            "また頼むとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDEE")

    Return()

    # Function_50_DD1C end

    def Function_51_DDEF(): pass

    label("Function_51_DDEF")


    #C0579
    ChrTalk(
        0x101,
        "#6P#0000Fうん、大丈夫だよ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E04D")

    #C0580
    ChrTalk(
        0xF,
        "#11Pうむ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xF,
        (
            "#11P近頃、本の返却期限を\x01",
            "延滞している人が多くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xF,
        (
            "#11Pそういった人たちの所に出向いて\x01",
            "延滞本を回収してきて欲しいのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x103,
        "#6P#0203F……なるほど。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x104,
        (
            "#5P#0300Fま、そこまで難しそうな\x01",
            "仕事じゃなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xF,
        (
            "#11Pそれが……困ったことに、\x01",
            "そうもいかないのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x101,
        "#6P#0005F……っていうと？\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xF,
        (
            "#11P実は今回、延滞をしている人は\x01",
            "クロスベル市の市民ではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xF,
        "#11P皆、郊外に住む人なのだ。\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        "#5P#0103Fああ、それは骨が折れそうですね。\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれで……\x01",
            "延滞本を所持している人の\x01",
            "住所は分かってる？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2A1")

    label("loc_E04D")


    #C0591
    ChrTalk(
        0xF,
        "#11Pうむ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xF,
        (
            "#11P実はまた最近、本の返却期限を\x01",
            "延滞している人が増えてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xF,
        (
            "#11P申し訳ないとは思うが、\x01",
            "もう一度君たちに延滞本を\x01",
            "回収してきて欲しいのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x103,
        (
            "#6P#0200F相変わらず延滞者が\x01",
            "多いようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x104,
        (
            "#5P#0300Fま、今回もちゃちゃっと\x01",
            "片付けてやろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xF,
        (
            "#11Pそれが……困ったことに、\x01",
            "そうもいかないのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x101,
        "#6P#0005F……っていうと？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xF,
        (
            "#11P実は今回、延滞をしている人は\x01",
            "クロスベル市の市民ではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xF,
        "#11P皆、郊外に住む人なのだ。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x102,
        "#5P#0103Fああ、それは骨が折れそうですね。\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれで……今回も、\x01",
            "延滞本を所持している人の\x01",
            "住所は分かってる？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2A1")


    #C0602
    ChrTalk(
        0xF,
        "#11Pうむ、その辺は抜かりないぞ。\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xF,
        (
            "#11Pまずは……\x01",
            "アルモリカ村に住む\x01",
            "アルフレッドさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xF,
        (
            "#11P次に……\x01",
            "マインツに住む\x01",
            "鉱員のロージーさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xF,
        (
            "#11P最後に……\x01",
            "ウルスラ病院の研修医、\x01",
            "フローラさんだな。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E3FD")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_E3FD")

    Sleep(1000)

    #C0606
    ChrTalk(
        0x101,
        (
            "#6P#0003Fそれはまた……\x01",
            "随分と散らばったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x104,
        (
            "#5P#0306F自治州じゅうを\x01",
            "回るハメになりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x103,
        (
            "#6P#0211F………………\x01",
            "ルーズな人は苦手です。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        "#5P#0100Fま、まぁまぁ。\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xF,
        (
            "#11P……さすがに\x01",
            "今回ばかりは範囲が広すぎて、\x01",
            "私たちには手が回らないのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xF,
        (
            "#11Pどうだね……\x01",
            "やってくれるかね？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E60E")

    #C0612
    ChrTalk(
        0x109,
        (
            "#12P#0500F今なら私の装甲車が\x01",
            "使えますし……\x01",
            "労力は少なくて済むのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x101,
        (
            "#6P#0003Fそれもそうだな……\x02\x03",

            "#0000Fありがたく\x01",
            "頼らせてもらうよ、曹長。\x02\x03",

            "……では、さっそく\x01",
            "当たらせてもらうとするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8C6")

    label("loc_E60E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E882")

    #C0614
    ChrTalk(
        0x101,
        "#6P#0000Fうん、じゃあさっそく……\x02",
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

    def lambda_E6D5():
        OP_93(0x101, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E6D5)

    def lambda_E6E2():
        OP_93(0x102, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E6E2)

    def lambda_E6EF():
        OP_93(0x104, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E6EF)

    def lambda_E6FC():
        OP_93(0x103, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E6FC)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)

    #C0616
    ChrTalk(
        0x102,
        (
            "#0106F（さっきからダドリー捜査官の\x01",
            "  視線が痛いのだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x104,
        (
            "#5P#0303F（でも何にも言ってこねえよな。\x01",
            "  止める気もないみてえだし。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0618
    ChrTalk(
        0xF,
        "#11Pどうかしたのかね？\x02",
    )

    CloseMessageWindow()

    def lambda_E7DF():
        OP_93(0x101, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E7DF)

    def lambda_E7EC():
        OP_93(0x102, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E7EC)

    def lambda_E7F9():
        OP_93(0x104, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E7F9)

    def lambda_E806():
        OP_93(0x103, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E806)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)

    #C0619
    ChrTalk(
        0x101,
        (
            "#6P#0000Fいや、なんでもないよ。\x01",
            "さっそく当たってみるよ。\x01",
            "（なるべく手早く済ませよう……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8C6")

    label("loc_E882")


    #C0620
    ChrTalk(
        0x101,
        (
            "#6P#0000Fうん、任せてくれ。\x01",
            "さっそく当たらせてもらうとするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8C6")


    #C0621
    ChrTalk(
        0xF,
        "#11Pああ、助かるよ。\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xF,
        (
            "#11P３冊の本が集まったら\x01",
            "私の所に持ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xF,
        (
            "#11Pでは支援課のみなさん、\x01",
            "よろしく頼んだよ。\x02",
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
            "クエスト【自治州内延滞本の回収】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x28, 0x1, 0x1)
    Return()

    # Function_51_DDEF end

    def Function_52_E9B6(): pass

    label("Function_52_E9B6")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA5F")
    SetChrPos(0x109, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_EA8A")

    label("loc_EA5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA8A")
    SetChrPos(0x10A, 4250, 0, 6300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_EA8A")

    SetChrSubChip(0xF, 0x0)
    OP_0D()

    #C0625
    ChrTalk(
        0xF,
        "#11Pおや……\x02",
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xF,
        (
            "#11Pもしかして、延滞本の回収が\x01",
            "終わったのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x104,
        "#5P#0300Fああ、ようやくな。\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x101,
        "#6P#0000Fはい、おじさん。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0629
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を返した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0630
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を返した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    #A0631
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2DA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を返した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x2D8, 1)
    SubItemNumber(0x2D9, 1)
    SubItemNumber(0x2DA, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EC6D")

    #C0632
    ChrTalk(
        0xF,
        (
            "#11P……うむ、確かに。\x01",
            "きちんと３冊すべて\x01",
            "回収してきてくれたようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xF,
        (
            "#11Pいや、ロイド君たちには\x01",
            "また助けられてしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xF,
        (
            "#11P前回のことも含めて、\x01",
            "礼を言わせて貰うよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED03")

    label("loc_EC6D")


    #C0635
    ChrTalk(
        0xF,
        (
            "#11P……うむ、確かに。\x01",
            "きちんと３冊すべて\x01",
            "回収してきてくれたようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xF,
        (
            "#11Pいや、助かったよ。\x01",
            "ロイドくんたちの手を借りて\x01",
            "本当によかったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED03")


    #C0637
    ChrTalk(
        0x101,
        (
            "#6P#0000Fはは……おじさんにそういわれると\x01",
            "むずがゆいね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EDCE")

    #C0638
    ChrTalk(
        0x109,
        (
            "#12P#0506Fそれにしても、\x01",
            "支援要請というのも\x01",
            "なかなか大変ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x102,
        (
            "#5P#0100Fふふ、こういうのは\x01",
            "日常茶飯事よ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EED5")

    label("loc_EDCE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EE91")

    #C0640
    ChrTalk(
        0x10A,
        (
            "#12P#0603Fフン……これが支援課の\x01",
            "『支援要請』の仕事か。\x01",
            "時間を取ってくれるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x101,
        "#6P#0006Fうっ……す、すみません。\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x102,
        "#5P#0103F私たちの日常業務ですから……\x02",
    )

    CloseMessageWindow()
    Jump("loc_EED5")

    label("loc_EE91")


    #C0643
    ChrTalk(
        0x102,
        (
            "#5P#0100Fふふ、ちょっと大変だったけど\x01",
            "やった甲斐はあったわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EED5")


    #C0644
    ChrTalk(
        0x103,
        (
            "#6P#0203F……ともかく、これにて\x01",
            "任務完了ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xF,
        (
            "#11Pああ、お疲れさま。\x01",
            "本当にありがとうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x101,
        "#6P#0000Fどういたしまして。\x02",
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
            "クエスト【自治州内延滞本の回収】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 5000, 150, 7800, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EFF8")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_EFF8")

    OP_29(0x28, 0x2, 0x1F)
    OP_29(0x28, 0x1, 0xB)
    OP_29(0x28, 0x4, 0x10)
    OP_66(0x5, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x9, 0x1)
    EventEnd(0x5)
    Return()

    # Function_52_E9B6 end

    def Function_53_F018(): pass

    label("Function_53_F018")

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
            "#6P#0003F怪盗Ｂの言っていた『白ハヤブサ』は\x01",
            "リベール王国の国鳥みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x102,
        (
            "#5P#0100Fリベール王国は\x01",
            "クロスベルの近隣にあるし\x01",
            "一番の友好国よね。\x02\x03",

            "道理でどこかで\x01",
            "聞いた事があると思ったわ。\x02",
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

    # Function_53_F018 end

    def Function_54_F19F(): pass

    label("Function_54_F19F")

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
            "#1105F#5Pわー、すっごい！\x01",
            "本がいっぱいだーっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x101,
        (
            "#6P#0002Fえっと……キーアは\x01",
            "本を好きだったりするのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0x10E, 0x1F4)

    #C0652
    ChrTalk(
        0x153,
        (
            "#1110F#11Pんー、わかんないけど好き！\x02\x03",

            "#1109Fずらーってならんでると、\x01",
            "なんかワクワクする！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F42E")

    #C0653
    ChrTalk(
        0x102,
        (
            "#0109F#6Pじゃあ今度ゆっくり\x01",
            "遊びに来ましょうか。\x02\x03",

            "#0102Fクロスベルの市立図書館は\x01",
            "子供向けの本も\x01",
            "充実しているはずだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F52E")

    label("loc_F42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F4BA")

    #C0654
    ChrTalk(
        0x103,
        (
            "#0204F#6Pでは、今度ゆっくり\x01",
            "遊びに来ましょう。\x02\x03",

            "#0202Fクロスベルの市立図書館は\x01",
            "子供向けの本も\x01",
            "充実しているはずですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F52E")

    label("loc_F4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F52E")

    #C0655
    ChrTalk(
        0x104,
        (
            "#0309F#6Pなら今度ゆっくり\x01",
            "遊びに連れて来てやるか。\x02\x03",

            "#0300F見たとこ子供向けの本も\x01",
            "充実してそうだしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F52E")

    OP_5A()
    SetChrPos(0x0, 2500, 0, 0, 90)
    SetScenarioFlags(0xB7, 0)
    EventEnd(0x5)
    Return()

    # Function_54_F19F end

    SaveToFile()

Try(main)
