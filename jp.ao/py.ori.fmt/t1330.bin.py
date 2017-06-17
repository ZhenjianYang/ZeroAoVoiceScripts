from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1330.bin",                # FileName
        "t1330",                    # MapName
        "t1330",                    # Location
        0x00B7,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -16000, 0, 0, 1, 183, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1330",                  # 0
        "エリィ",                 # 1
        "ティオ",                 # 2
        "ランディ",               # 3
        "ノエル",                 # 4
        "ワジ",                   # 5
        "キーア",                 # 6
        "フラン",                 # 7
        "セシル",                 # 8
        "シュリ",                 # 9
        "メルスン",               # 10
        "コロナ",                 # 11
        "リマ",                   # 12
        "ＭＷＬスタッフ",         # 13
        "観光客",                 # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "観光客",                 # 17
        "観光客",                 # 18
        "みーしぇ",               # 19
        "ダミー",                 # 20
        "男",                     # 21
        "女",                     # 22
        "ワンダーランド入口広場方面",# 23
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch00300.itc",                   # 02
        "chr/ch02900.itc",                   # 03
        "chr/ch03000.itc",                   # 04
        "chr/ch08200.itc",                   # 05
        "chr/ch08500.itc",                   # 06
        "chr/ch07500.itc",                   # 07
        "chr/ch10100.itc",                   # 08
        "chr/ch26200.itc",                   # 09
        "chr/ch22700.itc",                   # 0A
        "chr/ch20700.itc",                   # 0B
        "chr/ch44600.itc",                   # 0C
        "chr/ch22100.itc",                   # 0D
        "chr/ch24500.itc",                   # 0E
        "chr/ch22000.itc",                   # 0F
        "chr/ch20500.itc",                   # 10
        "chr/ch32300.itc",                   # 11
        "chr/ch03002.itc",                   # 12
        "chr/ch45400.itc",                   # 13
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

    DeclNpc(8600,    9,       -15670,  25,   389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(2970,    3549,    -33750,  25,   389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-7480,   9,       -15380,  205,  389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7869,    9,       -16059,  295,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(11350,   200,     -12800,  225,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(10130,   9,       -17000,  115,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(9850,    9,       -15010,  205,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-3990,   2309,    -28940,  250,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-1360,   0,       -17809,  295,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-2420,   0,       -17649,  25,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-2279,   0,       -16440,  160,  389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-949,    0,       -14699,  160,  389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-3170,   4619,    -37919,  115,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-2150,   4739,    -38400,  295,  389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-5900,   9,       -13130,  295,  389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-6829,   9,       -12550,  115,  389,  0x0, 0,   16,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-5030,   9,       -17719,  25,   389,  0x0, 0,   17,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9819,    0,       -10560,  315,  389,  0x0, 0,   19,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 56,  -0.23999999463558197,  -12.220000267028809,   0.0,                   144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   0.029999999329447746,  4.073333740234375,     -0.0,                  1.0])

    DeclActor(8730,    0,       -11330,  1000,    9820,    1500,    -10560,  0x007E, 0,  51, 0x0000)
    DeclActor(-5950,   0,       -12040,  1200,    -5950,   2000,    -12040,  0x007C, 0,  55, 0x0000)

    PlaceName(-0.38999998569488525, 0.0, -83.0999984741211, 0x0000, 0x0000, "ワンダーランド入口広場方面")

    ChipFrameInfo(1300, 0)                                       # 0

    ScpFunction((
        "Function_0_514",          # 00, 0
        "Function_1_5CC",          # 01, 1
        "Function_2_658",          # 02, 2
        "Function_3_6B3",          # 03, 3
        "Function_4_77D",          # 04, 4
        "Function_5_833",          # 05, 5
        "Function_6_A22",          # 06, 6
        "Function_7_AE0",          # 07, 7
        "Function_8_C10",          # 08, 8
        "Function_9_CDD",          # 09, 9
        "Function_10_E68",         # 0A, 10
        "Function_11_F22",         # 0B, 11
        "Function_12_FF8",         # 0C, 12
        "Function_13_109F",        # 0D, 13
        "Function_14_1157",        # 0E, 14
        "Function_15_1200",        # 0F, 15
        "Function_16_132F",        # 10, 16
        "Function_17_1387",        # 11, 17
        "Function_18_13DF",        # 12, 18
        "Function_19_149C",        # 13, 19
        "Function_20_153A",        # 14, 20
        "Function_21_1640",        # 15, 21
        "Function_22_1700",        # 16, 22
        "Function_23_17BE",        # 17, 23
        "Function_24_1881",        # 18, 24
        "Function_25_1A8A",        # 19, 25
        "Function_26_253D",        # 1A, 26
        "Function_27_257A",        # 1B, 27
        "Function_28_25B7",        # 1C, 28
        "Function_29_26C2",        # 1D, 29
        "Function_30_2724",        # 1E, 30
        "Function_31_2793",        # 1F, 31
        "Function_32_280A",        # 20, 32
        "Function_33_2875",        # 21, 33
        "Function_34_28E0",        # 22, 34
        "Function_35_292B",        # 23, 35
        "Function_36_299C",        # 24, 36
        "Function_37_2ADB",        # 25, 37
        "Function_38_2B19",        # 26, 38
        "Function_39_2B61",        # 27, 39
        "Function_40_2BA1",        # 28, 40
        "Function_41_35D7",        # 29, 41
        "Function_42_4147",        # 2A, 42
        "Function_43_4C9C",        # 2B, 43
        "Function_44_56AC",        # 2C, 44
        "Function_45_6153",        # 2D, 45
        "Function_46_6BEA",        # 2E, 46
        "Function_47_7665",        # 2F, 47
        "Function_48_80A3",        # 30, 48
        "Function_49_8CC3",        # 31, 49
        "Function_50_96C2",        # 32, 50
        "Function_51_A136",        # 33, 51
        "Function_52_A9B9",        # 34, 52
        "Function_53_BBA3",        # 35, 53
        "Function_54_BC39",        # 36, 54
        "Function_55_BCCF",        # 37, 55
        "Function_56_BD0D",        # 38, 56
    ))


    def Function_0_514(): pass

    label("Function_0_514")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_554"),
        (1, "loc_560"),
        (2, "loc_56C"),
        (3, "loc_578"),
        (4, "loc_584"),
        (5, "loc_590"),
        (6, "loc_59C"),
        (SWITCH_DEFAULT, "loc_5A8"),
    )


    label("loc_554")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_560")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_56C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_578")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_584")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_590")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_59C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5CB")

    Return()

    # Function_0_514 end

    def Function_1_5CC(): pass

    label("Function_1_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_5DA")
    Jump("loc_648")

    label("loc_5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_5E8")
    Jump("loc_648")

    label("loc_5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5F6")
    Jump("loc_648")

    label("loc_5F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_607")
    Call(0, 24)
    Jump("loc_648")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_615")
    Jump("loc_648")

    label("loc_615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_623")
    Jump("loc_648")

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_631")
    Jump("loc_648")

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_63F")
    Jump("loc_648")

    label("loc_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_648")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_657")
    ClearScenarioFlags(0x22, 0)
    Event(0, 52)

    label("loc_657")

    Return()

    # Function_1_5CC end

    def Function_2_658(): pass

    label("Function_2_658")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x1C2)
    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_679")
    OP_24(0x335)
    Jump("loc_67F")

    label("loc_679")

    Sound(821, 1, 50, 0)

    label("loc_67F")

    Sound(126, 1, 80, 0)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B2")
    OP_66(0x0, 0x1)

    label("loc_6B2")

    Return()

    # Function_2_658 end

    def Function_3_6B3(): pass

    label("Function_3_6B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC")
    Jump("loc_779")

    label("loc_6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    Jump("loc_779")

    label("loc_6E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_705")
    Call(0, 21)
    Jump("loc_74D")

    label("loc_705")


    #C0001
    ChrTalk(
        0x8,
        (
            "#00102Fふふ、飲み物を買ってきますから\x01",
            "ゆっくりと休んでてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74D")

    Jump("loc_779")

    label("loc_752")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768")
    Jump("loc_779")

    label("loc_768")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_779")

    label("loc_779")

    TalkEnd(0xFE)
    Return()

    # Function_3_6B3 end

    def Function_4_77D(): pass

    label("Function_4_77D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_796")
    Jump("loc_82F")

    label("loc_796")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B9")
    Call(0, 22)
    Jump("loc_7ED")

    label("loc_7B9")


    #C0002
    ChrTalk(
        0x9,
        (
            "#00204Fさすがフランさん……\x01",
            "話が分かりますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ED")

    Jump("loc_82F")

    label("loc_7F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_808")
    Jump("loc_82F")

    label("loc_808")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E")
    Jump("loc_82F")

    label("loc_81E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82F")

    label("loc_82F")

    TalkEnd(0xFE)
    Return()

    # Function_4_77D end

    def Function_5_833(): pass

    label("Function_5_833")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84C")
    Jump("loc_A1E")

    label("loc_84C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862")
    Jump("loc_A1E")

    label("loc_862")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_878")
    Jump("loc_A1E")

    label("loc_878")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97E")

    #C0003
    ChrTalk(
        0xA,
        (
            "#00300Fさっき、観覧車から出てきた\x01",
            "ちょっと好みのお姉さんを\x01",
            "ナンパしようと思ったんだが……\x02\x03",

            "#00306Fどうやら思いっきり\x01",
            "カップルで来てたみたいでな。\x02\x03",

            "#00302Fいやー、さすがにテーマパーク内で\x01",
            "ナンパすんのは無理があったかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A08")

    label("loc_97E")


    #C0004
    ChrTalk(
        0xA,
        (
            "#00306F考えてみりゃ、カップル客とか\x01",
            "ファミリー客が多いんだよな。\x02\x03",

            "#00302Fさすがにテーマパーク内で\x01",
            "ナンパすんのは無理があったかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A08")

    Jump("loc_A1E")

    label("loc_A0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1E")

    label("loc_A1E")

    TalkEnd(0xFE)
    Return()

    # Function_5_833 end

    def Function_6_A22(): pass

    label("Function_6_A22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3B")
    Jump("loc_ADC")

    label("loc_A3B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A51")
    Jump("loc_ADC")

    label("loc_A51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A67")
    Jump("loc_ADC")

    label("loc_A67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7D")
    Jump("loc_ADC")

    label("loc_A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA0")
    Call(0, 23)
    Jump("loc_ADC")

    label("loc_AA0")


    #C0005
    ChrTalk(
        0xB,
        (
            "#10100Fあ、ロイドさん。\x01",
            "最後に何に乗るか決まりました？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADC")

    TalkEnd(0xFE)
    Return()

    # Function_6_A22 end

    def Function_7_AE0(): pass

    label("Function_7_AE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B76")

    #C0006
    ChrTalk(
        0xC,
        (
            "#10304Fこうして人間観察を\x01",
            "しているのも悪くない。\x02\x03",

            "#10302Fフフ、案外どこかに\x01",
            "みっしぃの中の人がいたりして。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_BB4")

    label("loc_B76")


    #C0007
    ChrTalk(
        0xC,
        (
            "#10302Fフフ、案外どこかに\x01",
            "みっしぃの中の人がいたりして。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB4")

    Jump("loc_C0C")

    label("loc_BB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCF")
    Jump("loc_C0C")

    label("loc_BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE5")
    Jump("loc_C0C")

    label("loc_BE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFB")
    Jump("loc_C0C")

    label("loc_BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C")

    label("loc_C0C")

    TalkEnd(0xFE)
    Return()

    # Function_7_AE0 end

    def Function_8_C10(): pass

    label("Function_8_C10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C29")
    Jump("loc_CD9")

    label("loc_C29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3F")
    Jump("loc_CD9")

    label("loc_C3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB2")

    #C0008
    ChrTalk(
        0xD,
        (
            "#01102Fやっぱり、\x01",
            "ここの湖ってキレイだねー。\x02\x03",

            "#01109F底の方まで透き通ってる気がするー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD9")

    label("loc_CB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC8")
    Jump("loc_CD9")

    label("loc_CC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD9")

    label("loc_CD9")

    TalkEnd(0xFE)
    Return()

    # Function_8_C10 end

    def Function_9_CDD(): pass

    label("Function_9_CDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF6")
    Jump("loc_E64")

    label("loc_CF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D19")
    Call(0, 22)
    Jump("loc_D6C")

    label("loc_D19")


    #C0009
    ChrTalk(
        0xE,
        (
            "#06409Fティオちゃんの言うとおり、\x01",
            "きっとあの太陽の顔が\x01",
            "人気の秘訣ですよね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6C")

    Jump("loc_E64")

    label("loc_D71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D87")
    Jump("loc_E64")

    label("loc_D87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9D")
    Jump("loc_E64")

    label("loc_D9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC0")
    Call(0, 23)
    Jump("loc_E64")

    label("loc_DC0")


    #C0010
    ChrTalk(
        0xE,
        (
            "#06402Fこの時間帯だと、\x01",
            "観覧車からの眺めが\x01",
            "抜群にいいみたいですよ～。\x02\x03",

            "#06409F乗るものが決まってないなら、\x01",
            "ロイドさんも誰かと一緒に\x01",
            "乗ってみたらどうですか～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E64")

    TalkEnd(0xFE)
    Return()

    # Function_9_CDD end

    def Function_10_E68(): pass

    label("Function_10_E68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E81")
    Jump("loc_F1E")

    label("loc_E81")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E97")
    Jump("loc_F1E")

    label("loc_E97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBA")
    Call(0, 21)
    Jump("loc_EF2")

    label("loc_EBA")


    #C0011
    ChrTalk(
        0xF,
        (
            "#05909Fふふ、それなら\x01",
            "お言葉に甘えちゃおうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF2")

    Jump("loc_F1E")

    label("loc_EF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0D")
    Jump("loc_F1E")

    label("loc_F0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1E")

    label("loc_F1E")

    TalkEnd(0xFE)
    Return()

    # Function_10_E68 end

    def Function_11_F22(): pass

    label("Function_11_F22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3B")
    Jump("loc_FF4")

    label("loc_F3B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F51")
    Jump("loc_FF4")

    label("loc_F51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F67")
    Jump("loc_FF4")

    label("loc_F67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE3")

    #C0012
    ChrTalk(
        0x10,
        (
            "#14006Fはー、結構遊んだから\x01",
            "なんだか疲れちゃったな。\x02\x03",

            "#14000Fしばらく風にでも\x01",
            "あたってようっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF4")

    label("loc_FE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF4")

    label("loc_FF4")

    TalkEnd(0xFE)
    Return()

    # Function_11_F22 end

    def Function_12_FF8(): pass

    label("Function_12_FF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1011")
    Jump("loc_109B")

    label("loc_1011")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105E")

    #C0013
    ChrTalk(
        0x11,
        (
            "はは、リマは本当に\x01",
            "観覧車が気に入ったみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_105E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1074")
    Jump("loc_109B")

    label("loc_1074")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108A")
    Jump("loc_109B")

    label("loc_108A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109B")

    label("loc_109B")

    TalkEnd(0xFE)
    Return()

    # Function_12_FF8 end

    def Function_13_109F(): pass

    label("Function_13_109F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B8")
    Jump("loc_1153")

    label("loc_10B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1116")

    #C0014
    ChrTalk(
        0x12,
        (
            "あらあら、リマったら……\x01",
            "まだまだアトラクションは\x01",
            "他にもあるのよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1153")

    label("loc_1116")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112C")
    Jump("loc_1153")

    label("loc_112C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1142")
    Jump("loc_1153")

    label("loc_1142")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1153")

    label("loc_1153")

    TalkEnd(0xFE)
    Return()

    # Function_13_109F end

    def Function_14_1157(): pass

    label("Function_14_1157")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1170")
    Jump("loc_11FC")

    label("loc_1170")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BF")

    #C0015
    ChrTalk(
        0x13,
        (
            "パパ、もう一回乗ろー！\x01",
            "またオルキスタワー見たーい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FC")

    label("loc_11BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
    Jump("loc_11FC")

    label("loc_11D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EB")
    Jump("loc_11FC")

    label("loc_11EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FC")

    label("loc_11FC")

    TalkEnd(0xFE)
    Return()

    # Function_14_1157 end

    def Function_15_1200(): pass

    label("Function_15_1200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132B")
    TalkBegin(0xFE)

    #C0016
    ChrTalk(
        0xFE,
        (
            "こちらのアトラクションは、\x01",
            "観覧車《サンシャインモール》です！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "ゆっくりと一周するゴンドラから、\x01",
            "ミシュラム最高の景色を\x01",
            "ごゆっくりお楽しみいただけます。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00000F（みーしぇとかくれんぼ中だし……\x01",
            "　今アトラクションで遊ぶのは\x01",
            "　やめておくとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_132E")

    label("loc_132B")

    Call(0, 25)

    label("loc_132E")

    Return()

    # Function_15_1200 end

    def Function_16_132F(): pass

    label("Function_16_132F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1383")

    #C0019
    ChrTalk(
        0x15,
        (
            "観覧車乗りましょうよ！\x01",
            "すっごく眺めがいいんだから～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1383")

    label("loc_1383")

    TalkEnd(0xFE)
    Return()

    # Function_16_132F end

    def Function_17_1387(): pass

    label("Function_17_1387")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DB")

    #C0020
    ChrTalk(
        0x16,
        (
            "ダメだって、あたし高い所が\x01",
            "すっごい苦手なんだから～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DB")

    label("loc_13DB")

    TalkEnd(0xFE)
    Return()

    # Function_17_1387 end

    def Function_18_13DF(): pass

    label("Function_18_13DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_143C")

    #C0021
    ChrTalk(
        0x17,
        (
            "うぷ……\x01",
            "ゆらゆら揺れるゴンドラに\x01",
            "すっかり酔ってしまったよ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1498")

    label("loc_143C")


    #C0022
    ChrTalk(
        0x17,
        (
            "な、なあ……\x01",
            "やっぱり最後に乗るのは\x01",
            "別のにしないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x17,
        "また酔ったらたまんないし……\x02",
    )

    CloseMessageWindow()

    label("loc_1498")

    TalkEnd(0xFE)
    Return()

    # Function_18_13DF end

    def Function_19_149C(): pass

    label("Function_19_149C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EE")

    #C0024
    ChrTalk(
        0x18,
        (
            "もう、せっかくのデートなんだから\x01",
            "しっかりしてよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1536")

    label("loc_14EE")


    #C0025
    ChrTalk(
        0x18,
        (
            "大丈夫大丈夫！\x01",
            "頂上から夕日を見たら、\x01",
            "酔いなんて気になんないから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1536")

    TalkEnd(0xFE)
    Return()

    # Function_19_149C end

    def Function_20_153A(): pass

    label("Function_20_153A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15BB")

    #C0026
    ChrTalk(
        0x19,
        (
            "１人で観覧車に乗るのは\x01",
            "かなりの勇気が必要だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x19,
        (
            "……やっぱり男友達とでも\x01",
            "一緒に来るんだった。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_163C")

    label("loc_15BB")


    #C0028
    ChrTalk(
        0x19,
        (
            "頂上からの眺めが最高だった。\x01",
            "やっぱり勇気を出して\x01",
            "乗って正解だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x19,
        (
            "まあ、１人で乗るのは\x01",
            "普通に寂しかったけどね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163C")

    TalkEnd(0xFE)
    Return()

    # Function_20_153A end

    def Function_21_1640(): pass

    label("Function_21_1640")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0030
    ChrTalk(
        0x8,
        (
            "#00100Fそれじゃあ私、\x01",
            "飲み物かなにか買ってきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xF,
        (
            "#05905Fあら、そんな。\x01",
            "だったら私が買ってくるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#00102Fふふ、セシルさんは\x01",
            "ゆっくりと休んでてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_21_1640 end

    def Function_22_1700(): pass

    label("Function_22_1700")

    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0033
    ChrTalk(
        0x9,
        (
            "#00204Fやはり、観覧車も\x01",
            "大人気のようですね。\x02\x03",

            "#00200F真ん中にある太陽の顔……\x01",
            "まさにあれが決め手\x01",
            "なのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xE,
        "#06409Fあはは、きっとそうだね～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xE, 0x10)
    Return()

    # Function_22_1700 end

    def Function_23_17BE(): pass

    label("Function_23_17BE")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0035
    ChrTalk(
        0xE,
        (
            "#06400Fガイドブックによると、\x01",
            "この時間帯は観覧車からの眺めが\x01",
            "抜群にいいんだって～！\x02\x03",

            "#06409Fお姉ちゃん、後で一緒に乗ろうよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        "#10100Fふふ、そうしよっか。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_17BE end

    def Function_24_1881(): pass

    label("Function_24_1881")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18E6")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_18E6")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1944")
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x12)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_1A89")

    label("loc_1944")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_199D")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3970, 3590, -33910, 25)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    Jump("loc_1A89")

    label("loc_199D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CC")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    Jump("loc_1A89")

    label("loc_19CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A44")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_1A16")
    SetChrFlags(0xA, 0x80)
    Jump("loc_1A24")

    label("loc_1A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 1)), scpexpr(EXPR_END)), "loc_1A24")
    SetChrFlags(0x10, 0x80)

    label("loc_1A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A3F")
    ClearChrFlags(0x1A, 0x80)

    label("loc_1A3F")

    Jump("loc_1A89")

    label("loc_1A44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A89")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 6760, 10, -15090, 115)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x10)

    label("loc_1A89")

    Return()

    # Function_24_1881 end

    def Function_25_1A8A(): pass

    label("Function_25_1A8A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-950, 1300, -15300, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(8500, 0)
    OP_4B(0x14, 0xFF)
    SetChrPos(0x101, -950, 0, -16000, 0)
    Call(0, 26)
    OP_0D()

    #C0037
    ChrTalk(
        0x14,
        (
            "こちらのアトラクションは、\x01",
            "観覧車《サンシャインモール》です！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x14,
        (
            "ゆっくりと一周するゴンドラから、\x01",
            "ミシュラム最高の景色を\x01",
            "ごゆっくりお楽しみいただけます。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x14,
        (
            "よろしければ、\x01",
            "どなたかとご一緒にいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00004F#12P（……誰を誘おうかな？）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K誰を誘う？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "エリィ")
    MenuCmd(1, 0, "ティオ")
    MenuCmd(1, 0, "ランディ")
    MenuCmd(1, 0, "ノエル")
    MenuCmd(1, 0, "ワジ")
    MenuCmd(1, 0, "キーア")
    MenuCmd(1, 0, "フラン")
    MenuCmd(1, 0, "セシル")
    MenuCmd(1, 0, "イリア")
    MenuCmd(1, 0, "リーシャ")
    MenuCmd(1, 0, "シュリ")
    MenuCmd(1, 0, "やめる")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1C9E")
    MenuCmd(3, 0, 0x0)

    label("loc_1C9E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CB0")
    MenuCmd(3, 0, 0x1)

    label("loc_1CB0")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CC2")
    MenuCmd(3, 0, 0x2)

    label("loc_1CC2")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CD4")
    MenuCmd(3, 0, 0x3)

    label("loc_1CD4")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CE6")
    MenuCmd(3, 0, 0x4)

    label("loc_1CE6")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CF8")
    MenuCmd(3, 0, 0x5)

    label("loc_1CF8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D0A")
    MenuCmd(3, 0, 0x6)

    label("loc_1D0A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D1C")
    MenuCmd(3, 0, 0x7)

    label("loc_1D1C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D2E")
    MenuCmd(3, 0, 0x8)

    label("loc_1D2E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D40")
    MenuCmd(3, 0, 0x9)

    label("loc_1D40")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1D52")
    MenuCmd(3, 0, 0xA)

    label("loc_1D52")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24DB")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DD8"),
        (1, "loc_1E19"),
        (2, "loc_1E5A"),
        (3, "loc_1E9D"),
        (4, "loc_1EDE"),
        (5, "loc_1F1D"),
        (6, "loc_1F5E"),
        (7, "loc_1F9F"),
        (8, "loc_1FE2"),
        (9, "loc_2027"),
        (10, "loc_206A"),
        (SWITCH_DEFAULT, "loc_20AB"),
    )


    label("loc_1DD8")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0042
    ChrTalk(
        0x101,
        "#00000F#12P（よし……エリィを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1E19")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0043
    ChrTalk(
        0x101,
        "#00000F#12P（よし……ティオを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1E5A")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0044
    ChrTalk(
        0x101,
        "#00000F#12P（よし……ランディを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1E9D")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0045
    ChrTalk(
        0x101,
        "#00000F#12P（よし……ノエルを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1EDE")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0046
    ChrTalk(
        0x101,
        "#00000F#12P（よし……ワジを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1F1D")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0047
    ChrTalk(
        0x101,
        "#00000F#12P（よし……キーアを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1F5E")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0048
    ChrTalk(
        0x101,
        "#00000F#12P（よし……フランを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1F9F")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0049
    ChrTalk(
        0x101,
        "#00000F#12P（よし……セシル姉を誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_1FE2")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0050
    ChrTalk(
        0x101,
        "#00000F#12P（よし……イリアさんを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_2027")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0051
    ChrTalk(
        0x101,
        "#00000F#12P（よし……リーシャを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_206A")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0052
    ChrTalk(
        0x101,
        "#00000F#12P（よし……シュリを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_20AB")

    label("loc_20AB")

    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch05100.itc", 0x20)
    LoadChrToIndex("chr/ch05200.itc", 0x21)
    LoadChrToIndex("apl/ch51356.itc", 0x22)
    LoadChrToIndex("chr/ch10000.itc", 0x23)
    SoundLoad(148)
    ClearChrFlags(0x1B, 0x80)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2128"),
        (1, "loc_2137"),
        (2, "loc_2146"),
        (3, "loc_2155"),
        (4, "loc_2164"),
        (5, "loc_216D"),
        (6, "loc_217C"),
        (7, "loc_218B"),
        (8, "loc_219A"),
        (9, "loc_21A9"),
        (10, "loc_21B8"),
        (SWITCH_DEFAULT, "loc_21C7"),
    )


    label("loc_2128")

    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_21C7")

    label("loc_2137")

    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_21C7")

    label("loc_2146")

    LoadChrToIndex("chr/ch00302.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_21C7")

    label("loc_2155")

    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_21C7")

    label("loc_2164")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_21C7")

    label("loc_216D")

    LoadChrToIndex("chr/ch08202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_21C7")

    label("loc_217C")

    LoadChrToIndex("chr/ch08502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_21C7")

    label("loc_218B")

    LoadChrToIndex("chr/ch07502.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_21C7")

    label("loc_219A")

    LoadChrToIndex("chr/ch05102.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_21C7")

    label("loc_21A9")

    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_21C7")

    label("loc_21B8")

    LoadChrToIndex("chr/ch10002.itc", 0x1F)
    SetChrChipByIndex(0x1B, 0x8)
    Jump("loc_21C7")

    label("loc_21C7")

    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x101, -950, 0, -16000, 0)
    SetChrPos(0x1B, -250, 0, -16700, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0053
    ChrTalk(
        0x14,
        "では、チケットをお預かりしますね。\x02",
    )

    CloseMessageWindow()
    SubItemNumber(0x35D, 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スタッフにチケットを１枚渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0055
    ChrTalk(
        0x14,
        "２名様、ご案内いたしま～す！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22CA")
    SetChrChipByIndex(0x1B, 0x12)
    Jump("loc_22CE")

    label("loc_22CA")

    SetChrChipByIndex(0x1B, 0x1F)

    label("loc_22CE")

    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 999000, 200, 0, 90)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2341"),
        (1, "loc_2349"),
        (2, "loc_2351"),
        (3, "loc_2359"),
        (4, "loc_2361"),
        (5, "loc_2369"),
        (6, "loc_2371"),
        (7, "loc_2379"),
        (8, "loc_2381"),
        (9, "loc_2389"),
        (10, "loc_2391"),
        (SWITCH_DEFAULT, "loc_2399"),
    )


    label("loc_2341")

    Call(0, 40)
    Jump("loc_2399")

    label("loc_2349")

    Call(0, 41)
    Jump("loc_2399")

    label("loc_2351")

    Call(0, 42)
    Jump("loc_2399")

    label("loc_2359")

    Call(0, 43)
    Jump("loc_2399")

    label("loc_2361")

    Call(0, 44)
    Jump("loc_2399")

    label("loc_2369")

    Call(0, 45)
    Jump("loc_2399")

    label("loc_2371")

    Call(0, 46)
    Jump("loc_2399")

    label("loc_2379")

    Call(0, 47)
    Jump("loc_2399")

    label("loc_2381")

    Call(0, 48)
    Jump("loc_2399")

    label("loc_2389")

    Call(0, 49)
    Jump("loc_2399")

    label("loc_2391")

    Call(0, 50)
    Jump("loc_2399")

    label("loc_2399")

    SetChrFlags(0x1B, 0x80)
    OP_49()
    OP_D7(0x1E)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B1")
    OP_D7(0x1F)

    label("loc_23B1")

    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2404"),
        (1, "loc_2412"),
        (2, "loc_2420"),
        (3, "loc_242E"),
        (4, "loc_243C"),
        (5, "loc_244A"),
        (6, "loc_2458"),
        (7, "loc_2466"),
        (8, "loc_2474"),
        (9, "loc_2482"),
        (10, "loc_2490"),
        (SWITCH_DEFAULT, "loc_249E"),
    )


    label("loc_2404")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2412")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2420")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_242E")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_243C")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_244A")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2458")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2466")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2474")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2482")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_2490")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_249E")

    label("loc_249E")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D6")
    StopSound(821, 1000, 40)
    StopSound(126, 1000, 70)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_24D6")

    Jump("loc_2522")

    label("loc_24DB")


    #C0056
    ChrTalk(
        0x14,
        "あら、お止めになりますか？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x14,
        "またのご来場をお待ちしてます！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2522")

    Call(0, 27)
    OP_4C(0x14, 0xFF)
    SetChrPos(0x0, 0, 0, -16500, 180)
    EventEnd(0x5)
    Return()

    # Function_25_1A8A end

    def Function_26_253D(): pass

    label("Function_26_253D")

    SetChrFlags(0xC, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    Return()

    # Function_26_253D end

    def Function_27_257A(): pass

    label("Function_27_257A")

    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    Return()

    # Function_27_257A end

    def Function_28_25B7(): pass

    label("Function_28_25B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2658")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_26C1")

    label("loc_2658")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_in", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y_in", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y_in", 0x0, 0x1)

    label("loc_26C1")

    Return()

    # Function_28_25B7 end

    def Function_29_26C2(): pass

    label("Function_29_26C2")

    Sleep(500)
    FadeToBright(1000, 0)
    OP_68(-11850, 18700, -640, 0)
    OP_68(-11850, 21700, -640, 5000)
    MoveCamera(35, 22, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(26940, 0)
    OP_0D()
    Sleep(3000)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    VolumeBGM(0x46, 0x1F4)
    Return()

    # Function_29_26C2 end

    def Function_30_2724(): pass

    label("Function_30_2724")

    StopSound(148, 500, 70)
    Sound(821, 2, 50, 0)
    Sound(126, 2, 80, 0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_68(1020, 38900, 2930, 0)
    MoveCamera(330, 11, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(31100, 0)
    SetCameraDistance(28100, 5000)
    OP_0D()
    Sleep(3000)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    VolumeBGM(0x46, 0x1F4)
    Return()

    # Function_30_2724 end

    def Function_31_2793(): pass

    label("Function_31_2793")

    StopSound(148, 500, 70)
    Sound(821, 2, 50, 0)
    Sound(126, 2, 80, 0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_68(11580, 21300, -1090, 0)
    OP_68(11580, 18300, -1090, 5000)
    MoveCamera(331, 30, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(26940, 0)
    OP_0D()
    Sleep(3000)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    VolumeBGM(0x46, 0x1F4)
    Return()

    # Function_31_2793 end

    def Function_32_280A(): pass

    label("Function_32_280A")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop00")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2856")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_2861")

    label("loc_2856")

    MoveCamera(45, 23, 0, 0)

    label("loc_2861")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_32_280A end

    def Function_33_2875(): pass

    label("Function_33_2875")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "loop01")
    OP_68(1000000, 1350, 0, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C1")
    MoveCamera(30, 23, 0, 0)
    Jump("loc_28CC")

    label("loc_28C1")

    MoveCamera(45, 23, 0, 0)

    label("loc_28CC")

    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_33_2875 end

    def Function_34_28E0(): pass

    label("Function_34_28E0")

    Sound(148, 2, 80, 0)
    Fade(1000)
    SetMapObjFrame(0xFF, "Null_in", 0x2, "goal")
    OP_68(1000000, 1350, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Return()

    # Function_34_28E0 end

    def Function_35_292B(): pass

    label("Function_35_292B")

    Sleep(500)
    SetChrPos(0x101, 400, 0, -15500, 90)
    SetChrPos(0x1B, 1600, 0, -15500, 270)
    FadeToBright(1000, 0)
    OP_68(1100, 1700, -15500, 0)
    OP_68(1100, 1300, -15500, 2500)
    MoveCamera(45, 24, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(7500, 0)
    OP_6F(0x79)
    OP_0D()
    Return()

    # Function_35_292B end

    def Function_36_299C(): pass

    label("Function_36_299C")

    Fade(250)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A00"),
        (1, "loc_2A09"),
        (2, "loc_2A12"),
        (3, "loc_2A1B"),
        (4, "loc_2A24"),
        (5, "loc_2A2D"),
        (6, "loc_2A36"),
        (7, "loc_2A3F"),
        (8, "loc_2A48"),
        (9, "loc_2A51"),
        (10, "loc_2A5A"),
        (SWITCH_DEFAULT, "loc_2A63"),
    )


    label("loc_2A00")

    SetChrChipByIndex(0x1B, 0x0)
    Jump("loc_2A63")

    label("loc_2A09")

    SetChrChipByIndex(0x1B, 0x1)
    Jump("loc_2A63")

    label("loc_2A12")

    SetChrChipByIndex(0x1B, 0x2)
    Jump("loc_2A63")

    label("loc_2A1B")

    SetChrChipByIndex(0x1B, 0x3)
    Jump("loc_2A63")

    label("loc_2A24")

    SetChrChipByIndex(0x1B, 0x4)
    Jump("loc_2A63")

    label("loc_2A2D")

    SetChrChipByIndex(0x1B, 0x5)
    Jump("loc_2A63")

    label("loc_2A36")

    SetChrChipByIndex(0x1B, 0x6)
    Jump("loc_2A63")

    label("loc_2A3F")

    SetChrChipByIndex(0x1B, 0x7)
    Jump("loc_2A63")

    label("loc_2A48")

    SetChrChipByIndex(0x1B, 0x20)
    Jump("loc_2A63")

    label("loc_2A51")

    SetChrChipByIndex(0x1B, 0x21)
    Jump("loc_2A63")

    label("loc_2A5A")

    SetChrChipByIndex(0x1B, 0x23)
    Jump("loc_2A63")

    label("loc_2A63")

    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x101, 999300, 0, 0, 90)
    SetChrPos(0x1B, 1000700, 0, 0, 270)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x1B, 3, 0, 38)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x1B, 3)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    StopSound(148, 500, 70)
    Sound(821, 2, 50, 0)
    Sound(126, 2, 80, 0)
    VolumeBGM(0x64, 0x1F4)
    Return()

    # Function_36_299C end

    def Function_37_2ADB(): pass

    label("Function_37_2ADB")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2AE7():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AE7)
    Sleep(500)

    def lambda_2B04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B04)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_37_2ADB end

    def Function_38_2B19(): pass

    label("Function_38_2B19")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(600)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2B2F():
        OP_96(0xFE, 0xF4240, 0x0, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B2F)
    Sleep(500)

    def lambda_2B4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B4C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_2B19 end

    def Function_39_2B61(): pass

    label("Function_39_2B61")


    def lambda_2B66():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B66)
    OP_93(0x1B, 0xB4, 0x1F4)

    def lambda_2B7A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2B7A)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x1B, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_39_2B61 end

    def Function_40_2BA1(): pass

    label("Function_40_2BA1")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0058
    NpcTalk(
        0x1B,
        "エリィ",
        (
            "#00105Fゴンドラがどんどん高く上がっていく……\x02\x03",

            "#00102Fふふ、なんだか緊張してきちゃった。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEA")

    #C0059
    ChrTalk(
        0x101,
        (
            "#00002F#6Pああ、俺も観覧車は初めてだし\x01",
            "ドキドキしてきたよ。\x02\x03",

            "#00005F……って、エリィは前に\x01",
            "テーマパークに来たこと\x01",
            "あるんじゃなかったか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D80")

    label("loc_2CEA")


    #C0060
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、観覧車は初めてじゃないけど\x01",
            "俺もドキドキしてきたよ。\x02\x03",

            "#00005F……って、エリィは前に\x01",
            "テーマパークに来たこと\x01",
            "あるんじゃなかったか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D80")

    SetChrSubChip(0x1B, 0x0)

    #N0061
    NpcTalk(
        0x1B,
        "エリィ",
        (
            "#00104Fええ、そうだけど……\x02\x03",

            "#00100F前に来たときは\x01",
            "他のアトラクションを\x01",
            "回っていたのよね。\x02\x03",

            "#00106Fやっぱり、一日じゃ\x01",
            "とても回りきれなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00004F#6Pなるほど、そういうことか。\x02\x03",

            "#00009Fはは、それじゃあ\x01",
            "これから楽しみだな。\x02",
        )
    )

    CloseMessageWindow()

    #N0063
    NpcTalk(
        0x1B,
        "エリィ",
        (
            "#00102Fええ、頂上の景色は\x01",
            "どんなものなのかしら……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    #N0064
    NpcTalk(
        0x1B,
        "エリィ",
        "#00102Fあら……見て、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00002F#6Pああ……\x01",
            "すごくいい眺めだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3114")

    #N0066
    NpcTalk(
        0x1B,
        "エリィ",
        (
            "#00109Fええ、本当に。\x01",
            "夕焼けで湖が真っ赤に染まって……\x02\x03",

            "#00104Fはあ……思わずため息が出ちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00002F#6Pああ……\x01",
            "いい時間帯に乗れたみたいだ。\x02\x03",

            "#00009F最後のチケットを\x01",
            "とっておいて正解だったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("エリィ")

    #A0068
    AnonymousTalk(
        0xFF,
        (
            "ふふ、ロイド。\x01",
            "誘ってくれてありがとう。\x02\x03",

            "この素敵な光景は\x01",
            "しばらく忘れられそうにないわ。\x02",
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

    #C0069
    ChrTalk(
        0x101,
        "#00000F#6Pはは、どういたしまして。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_3114")


    #N0070
    NpcTalk(
        0x1B,
        "エリィ",
        (
            "#00102Fええ、本当に。\x01",
            "湖にお日様の光が反射して、\x01",
            "キラキラ輝いて……\x02\x03",

            "#00104Fはあ……思わずため息が出ちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#00000F#6Pはは、ほんとにな。\x02",
    )

    CloseMessageWindow()

    label("loc_31B1")

    SetChrSubChip(0x1B, 0x0)
    Sleep(300)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0072
    NpcTalk(
        0x1B,
        "エリィ",
        "#00105F……あっ…………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x2)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x101,
        "#00005F#6Pエリィ、どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #N0074
    NpcTalk(
        0x1B,
        "エリィ",
        (
            "#00112Fい、いや、その……\x02\x03",

            "#00113F後続のゴンドラに\x01",
            "カップルが乗ってて……\x02\x03",

            "彼らがその、キ、キスを……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#00005F#6Pえ……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00012F#6Pは、はは……その。\x01",
            "アツアツだったな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0077
    NpcTalk(
        0x1B,
        "エリィ",
        (
            "#00109Fあ、あはは……そうね。\x01",
            "カップルにも人気だって\x01",
            "聞いていたけど……\x02\x03",

            "#00106F#1Sも、もしかして私たちも\x01",
            "そういう関係に見えてたり……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#00005F#6Pえっ……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0079
    NpcTalk(
        0x1B,
        "エリィ",
        (
            "#00109Fい、いえ、なんでもないわ。\x01",
            "おほほほ……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#00012F#6Pあ、あははは……\x01",
            "（なんだか気まずくなっちゃったな。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0081
    ChrTalk(
        0x101,
        "#00000F#6P……そろそろ到着みたいだな。\x05\x02",
    )

    CloseMessageWindow()

    #N0082
    NpcTalk(
        0x1B,
        "エリィ",
        "#00100Fええ、降りるとしましょうか。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0083
    NpcTalk(
        0x1B,
        "エリィ",
        (
            "#00100F#11Pふふ、ありがとうロイド。\x01",
            "一緒に乗れて楽しかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0085
    NpcTalk(
        0x1B,
        "エリィ",
        "#00100F#11Pうん、またね。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_40_2BA1 end

    def Function_41_35D7(): pass

    label("Function_41_35D7")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0086
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00203F……ふむ、これは\x01",
            "どういう事態なんでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0087
    ChrTalk(
        0x101,
        "#00005F#6Pへっ、なにがだ？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0088
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00203F初めてのテーマパーク、\x01",
            "観覧車でロイドさんと２人きり……\x02\x03",

            "#00200F考えてみれば、かなり\x01",
            "特殊な状況だと思いまして。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37AC")

    #C0089
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは……ゴメン、\x01",
            "俺も観覧車は初めてだし\x01",
            "なんだか緊張しててさ。\x02\x03",

            "#00006F言われてみれば、\x01",
            "もう何人か呼んだほうが\x01",
            "楽しかったかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3827")

    label("loc_37AC")


    #C0090
    ChrTalk(
        0x101,
        (
            "#00003F#6Pうーん、そういえばそうか。\x02\x03",

            "#00012Fまあ、言われてみれば、\x01",
            "もう何人か呼んだほうが\x01",
            "楽しかったかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3827")


    #N0091
    NpcTalk(
        0x1B,
        "ティオ",
        "#00211Fそういう意味ではないのですが……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #N0092
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00202F……まあいいでしょう。\x01",
            "せっかくですし、色々と\x01",
            "お話でもしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00000F#6Pはは、そうだな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    #N0094
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00203F……つまり、みっしぃの愛らしさは\x01",
            "あの八の字眉毛に集約される──\x01",
            "そう言っても過言ではないのです。\x02\x03",

            "#00201Fあの角度が少しでもズレていたならば、\x01",
            "今の大陸は暗黒時代もかくやという\x01",
            "激動の時代であったと、専門家も……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x101,
        (
            "#00012F#6Pあ、あのー、ティオさん？\x01",
            "そろそろ頂上なんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0096
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00205F……つい熱中してしまいました。\x02\x03",

            "#00204Fでは、講義の続きは\x01",
            "また後でということで……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#00006F#6P（いつから講義に……！？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D2C")
    SetChrSubChip(0x1B, 0x2)

    #N0098
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00205F……なんて綺麗……\x01",
            "あの広大なエルム湖が\x01",
            "真っ赤に染まっていますね。\x02\x03",

            "#00204F街の港湾区から見える風景とは\x01",
            "また違った風情を感じます。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    #C0099
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ……\x01",
            "いい時間帯に乗れたみたいだ。\x02\x03",

            "#00009F最後のチケットを\x01",
            "とっておいて正解だったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("ティオ")

    #A0100
    AnonymousTalk(
        0xFF,
        (
            "……ロイドさん、誘ってくれて\x01",
            "ありがとうございます。\x02\x03",

            "この光景、とてもいい\x01",
            "思い出になりそうです。\x02",
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

    #C0101
    ChrTalk(
        0x101,
        "#00000F#6Pはは、どういたしまして。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBA")

    label("loc_3D2C")

    SetChrSubChip(0x1B, 0x1)

    #N0102
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00205Fロイドさん、中央広場の方を\x01",
            "見てみてください。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0103
    ChrTalk(
        0x101,
        (
            "#00005F#6Pああ……花壇にあった\x01",
            "みっしぃの顔が見えるな。\x02\x03",

            "#00009Fはは、あれを見ると\x01",
            "本当にテーマパークに\x01",
            "来たんだって気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #N0104
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00202Fふふ、そうですね。\x02\x03",

            "#00204F支援課の屋上にも\x01",
            "あれとおなじガーデニングを\x01",
            "したくなります。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00006F#6Pか、勘弁してくれ。\x01",
            "さすがにユニークすぎる部署に\x01",
            "なっちゃいそうだし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EBA")

    SetChrSubChip(0x1B, 0x0)

    #N0106
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00203F……コホン、では気分が乗った所で\x01",
            "講義の後半に移るとしましょうか。\x02\x03",

            "#00201Fみっしぃの愛らしさが眉毛にあり、\x01",
            "といった話を先ほどしましたが、\x01",
            "最近の研究によれば……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0107
    ChrTalk(
        0x101,
        (
            "#00006F#6P（どうやら降りるまでずっと\x01",
            "  付き合わされそうだな……）\x02\x03",

            "#00012F（ま、楽しそうだからいいか。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0108
    ChrTalk(
        0x101,
        "#00000F#6P……そろそろ到着みたいだな。\x05\x02",
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0x1B,
        "ティオ",
        "#00200Fそうですね、降りるとしましょう。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0110
    NpcTalk(
        0x1B,
        "ティオ",
        (
            "#00200Fありがとうございます、ロイドさん。\x01",
            "おかげで楽しかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0112
    NpcTalk(
        0x1B,
        "ティオ",
        "#00200Fええ、ではまた。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_41_35D7 end

    def Function_42_4147(): pass

    label("Function_42_4147")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    Sleep(500)
    SetChrSubChip(0x1B, 0x0)

    #N0113
    NpcTalk(
        0x1B,
        "ランディ",
        (
            "#00306Fはあ、まさか野郎と２人で\x01",
            "観覧車に乗るハメになるとはな。\x02\x03",

            "#00301Fロイド、お前……マジで俺を\x01",
            "狙ってんじゃねえだろうな？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4318")

    #C0114
    ChrTalk(
        0x101,
        (
            "#00006F#6Pあのな……\x01",
            "そういう趣味はないから。\x02\x03",

            "#00000Fただ、前に来たことがある\x01",
            "ランディなら、テーマパークにも\x01",
            "色々と詳しそうだからさ。\x02\x03",

            "#00002F初めて観覧車から見る風景も\x01",
            "１００％楽しめそうだと思って。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F7")

    label("loc_4318")


    #C0115
    ChrTalk(
        0x101,
        (
            "#00006F#6Pあのな……\x01",
            "そういう趣味はないから。\x02\x03",

            "#00000Fただ、前に来たことがある\x01",
            "ランディなら、テーマパークにも\x01",
            "色々と詳しそうだからさ。\x02\x03",

            "#00002F観覧車から見える風景にも、\x01",
            "また何か新しい発見が\x01",
            "あるんじゃないかと思って。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F7")


    #N0116
    NpcTalk(
        0x1B,
        "ランディ",
        (
            "#00305Fなんだ、俺は\x01",
            "ガイドブック代わりかよ？\x02\x03",

            "#00308F所詮俺なんか、お前には\x01",
            "都合のいい男ってわけか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0117
    ChrTalk(
        0x101,
        (
            "#00011F#6Pだああっ、いちいち\x01",
            "いかがわしい言い方を\x01",
            "するなっての！\x02",
        )
    )

    CloseMessageWindow()

    #N0118
    NpcTalk(
        0x1B,
        "ランディ",
        "#00309Fわはは、冗談だっつーの。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    #C0119
    ChrTalk(
        0x101,
        "#00002F#6P……もうすぐ頂上だな。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x2)

    #N0120
    NpcTalk(
        0x1B,
        "ランディ",
        (
            "#00304Fああ、そろそろだ。\x02\x03",

            "#00300Fオルキスタワーほどじゃねえが\x01",
            "高度もかなりあるし、\x01",
            "ここからの眺めは絶景だぜ。\x02\x03",

            "その上、この密閉された\x01",
            "ゴンドラの中はムード抜群、\x01",
            "攻略成功確率も倍々に跳ね上がる。\x02\x03",

            "#00309F男女が次のステップに進むには、\x01",
            "まさにうってつけの場所ってわけだな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x101,
        "#00006F#6P……何の話をしてるんだよ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4936")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("ランディ")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            "はは、ちょっとした\x01",
            "恋愛指南ってヤツだ。\x02\x03",

            "しかし、それにしても……\x01",
            "この夕日の差す絶妙な時間帯に\x01",
            "俺なんかを誘っちまうなんてよ。\x02\x03",

            "女の子を落とすには\x01",
            "最高級のタイミングだってのに、\x01",
            "お前ともあろうものがどうしたよ？\x02",
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

    #C0123
    ChrTalk(
        0x101,
        (
            "#00012F#6Pお、俺をなんだと思ってるんだ？\x02\x03",

            "#00000F……まあ、今回は成り行きで女性陣が\x01",
            "かなり多くなっちゃったからさ。\x02\x03",

            "たまにはランディとこうして\x01",
            "話す時間を作るのも悪くないかなって。\x02\x03",

            "#00009Fでも、こんな夕日が見れるなんて……\x01",
            "最後のチケットをとっておいて正解だったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AD4")

    label("loc_4936")


    #N0124
    NpcTalk(
        0x1B,
        "ランディ",
        (
            "#00309Fはは、ちょっとした\x01",
            "恋愛指南ってヤツだ。\x02\x03",

            "#00303Fしかし、それにしても……\x01",
            "せっかくの観覧車に\x01",
            "俺なんかを誘っちまうなんてよ。\x02\x03",

            "#00301F女の子を落とす絶好の場所だってのに、\x01",
            "お前ともあろうものがどうしたよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#00012F#6Pお、俺をなんだと思ってるんだ？\x02\x03",

            "#00000F……まあ、今回は成り行きで女性陣が\x01",
            "かなり多くなっちゃったからさ。\x02\x03",

            "#00004Fたまにはランディとこうして\x01",
            "話す時間を作るのも悪くないかなって。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD4")

    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0126
    NpcTalk(
        0x1B,
        "ランディ",
        (
            "#00306Fったく、これだから\x01",
            "天然ジゴロって奴は……\x02\x03",

            "#00300Fま、気持ちだけは\x01",
            "ありがたく受け取っておくぜ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 34)
    Sleep(3000)

    #C0127
    ChrTalk(
        0x101,
        "#00000F#6P……そろそろ到着みたいだな。\x05\x02",
    )

    CloseMessageWindow()

    #N0128
    NpcTalk(
        0x1B,
        "ランディ",
        "#00300Fああ、降りるとすっか。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0129
    NpcTalk(
        0x1B,
        "ランディ",
        (
            "#00300F誘ってくれてありがとよ。\x01",
            "まあまあ楽しめたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0131
    NpcTalk(
        0x1B,
        "ランディ",
        "#00300Fおう、そんじゃな。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_42_4147 end

    def Function_43_4C9C(): pass

    label("Function_43_4C9C")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10101.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0132
    NpcTalk(
        0x1B,
        "ノエル",
        "#10101F………………………………\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#00005F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #N0134
    NpcTalk(
        0x1B,
        "ノエル",
        "#10106F………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0135
    ChrTalk(
        0x101,
        (
            "#00006F#6P……その、ノエル。\x01",
            "なんでさっきから黙ってるんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x0)

    #N0136
    NpcTalk(
        0x1B,
        "ノエル",
        (
            "#10105Fあっ、いえ！　その……\x01",
            "男の人と観覧車に乗るのは\x01",
            "初めてなものですから。\x02\x03",

            "#10100F前に乗ったときは、\x01",
            "フランとでしたし。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ECA")

    #C0137
    ChrTalk(
        0x101,
        (
            "#00009F#6Pあ、ああ……そういうことか。\x02\x03",

            "#00000Fまあ、俺も乗るのは初めてだからさ。\x01",
            "色々教えてくれると助かるかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F4F")

    label("loc_4ECA")


    #C0138
    ChrTalk(
        0x101,
        (
            "#00009F#6Pあ、ああ……そういうことか。\x02\x03",

            "#00000Fまあ、俺もまだそんなに\x01",
            "乗ってるわけじゃないし……\x01",
            "色々教えてくれると助かるかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4F")


    #N0139
    NpcTalk(
        0x1B,
        "ノエル",
        "#10102Fは、はいっ！　任せてください！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    #N0140
    NpcTalk(
        0x1B,
        "ノエル",
        (
            "#10100Fかなり高くなってきましたね。\x02\x03",

            "#10104Fうーん、やっぱりここからの\x01",
            "眺めは素晴らしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#00009F#6Pああ、確かにいい眺めだよな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)
    SetChrSubChip(0x1B, 0x0)

    #N0142
    NpcTalk(
        0x1B,
        "ノエル",
        (
            "#10106Fその……ロイドさん、\x01",
            "ホントにあたしなんか\x01",
            "誘って良かったんですか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0143
    ChrTalk(
        0x101,
        "#00005F#6Pえ、どうしてだ？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52CE")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("ノエル")

    #A0144
    AnonymousTalk(
        0xFF,
        (
            "その、せっかくこんなに\x01",
            "夕日が綺麗なんですし。\x02\x03",

            "エリィさんやセシルさんとか、\x01",
            "もっと素敵な女性と一緒の方が……\x02",
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

    #C0145
    ChrTalk(
        0x101,
        (
            "#00003F#6Pうーん、そんなに自分を\x01",
            "下げなくてもいいと思うけどな。\x02\x03",

            "#00000Fほら、ノエルだって\x01",
            "可愛いところがあると思うし。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0146
    NpcTalk(
        0x1B,
        "ノエル",
        "#10114F#4Sえ゛。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#00009F#6Pそれにしてもこの夕日……\x01",
            "最後のチケットを\x01",
            "とっておいて正解だったかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C0")

    label("loc_52CE")


    #N0148
    NpcTalk(
        0x1B,
        "ノエル",
        (
            "#10108Fその、せっかくの観覧車なんですし。\x02\x03",

            "エリィさんやセシルさんとか、\x01",
            "もっと素敵な女性と一緒の方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00003F#6Pうーん、そんなに自分を\x01",
            "下げなくてもいいと思うけどな。\x02\x03",

            "#00000Fほら、ノエルだって\x01",
            "可愛いところがあると思うし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C0")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    #C0150
    ChrTalk(
        0x101,
        (
            "#00005F#6Pあ、あれ？\x01",
            "なんか俺、変なこと言ったか？\x02",
        )
    )

    CloseMessageWindow()

    #N0151
    NpcTalk(
        0x1B,
        "ノエル",
        (
            "#10109Fい、いえ……\x01",
            "その、ありがとうございます。\x02\x03",

            "#10106F（今のを特別な言葉に感じてないって……）\x02\x03",

            "#10101F（ロイドさんって、思っていた以上に\x01",
            "  危険な人物な気がしてきました。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0152
    ChrTalk(
        0x101,
        (
            "#00006F#6P（う、うーん……\x01",
            "  また黙り込んじゃったぞ。\x01",
            "  やっぱり変なこと言ったのかな……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0153
    ChrTalk(
        0x101,
        "#00000F#6P……そろそろ到着みたいだな。\x05\x02",
    )

    CloseMessageWindow()

    #N0154
    NpcTalk(
        0x1B,
        "ノエル",
        (
            "#10100Fあ、はい。\x01",
            "降りるとしましょうか。\x05\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0155
    NpcTalk(
        0x1B,
        "ノエル",
        (
            "#10100F誘っていただいて\x01",
            "ありがとうございました。\x01",
            "おかげ様で楽しかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0157
    NpcTalk(
        0x1B,
        "ノエル",
        "#10100Fはい、また！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_43_4C9C end

    def Function_44_56AC(): pass

    label("Function_44_56AC")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)

    #C0158
    ChrTalk(
        0x101,
        (
            "#00000F#6P……そういえばワジは、\x01",
            "観覧車には乗ったことあるのか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0159
    NpcTalk(
        0x1B,
        "ワジ",
        (
            "#10309Fフフ、実はあんまり。\x02\x03",

            "#10300Fクラブの客とミシュラムに来る時は、\x01",
            "バーみたいな静かな場所なんかで\x01",
            "会ってることが多いからね。\x02\x03",

            "#10304Fそういう意味では、\x01",
            "テーマパーク自体も割と新鮮かな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58BE")

    #C0160
    ChrTalk(
        0x101,
        (
            "#00000F#6Pへえ……なんだか意外だな。\x02\x03",

            "#00003F俺のほうは、\x01",
            "初めて観覧車に乗るからか\x01",
            "結構緊張してるんだ。\x02\x03",

            "#00002Fはは、考えてみれば\x01",
            "絶叫系でもないのに変な話だよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596A")

    label("loc_58BE")


    #C0161
    ChrTalk(
        0x101,
        (
            "#00000F#6Pへえ……なんだか意外だな。\x02\x03",

            "#00003F俺はさっきも観覧車に乗ったけど、\x01",
            "まだ慣れなくて緊張してるよ。\x02\x03",

            "#00002Fはは、考えてみれば\x01",
            "絶叫系でもないのに変な話だよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596A")


    #N0162
    NpcTalk(
        0x1B,
        "ワジ",
        (
            "#10300Fいや、観覧車ってのは意外と\x01",
            "怖い乗り物に分類されると思うよ。\x02\x03",

            "#10304F高い所ってだけで苦手な人もいるし……\x02\x03",

            "#10302F万が一、ゴンドラを吊っている\x01",
            "連結部が壊れたりしたら\x01",
            "大惨事になっちゃうだろうしね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0163
    ChrTalk(
        0x101,
        (
            "#00006F#6Pいきなり不安になるようなことを\x01",
            "言うなよな……\x02",
        )
    )

    CloseMessageWindow()

    #N0164
    NpcTalk(
        0x1B,
        "ワジ",
        (
            "#10309Fフフ、スリルが生まれていいじゃない？\x02\x03",

            "#10304Fまあ、今は観覧車を楽しもうよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    #C0165
    ChrTalk(
        0x101,
        "#00000F#6Pそろそろ頂上につく頃か……\x02",
    )

    CloseMessageWindow()

    #N0166
    NpcTalk(
        0x1B,
        "ワジ",
        (
            "#10304Fさすがに高くなってきたけど、\x01",
            "ゴンドラの動き自体は\x01",
            "意外とゆっくりなんだね。\x02\x03",

            "長く景色を楽しめるようにって\x01",
            "ワケなんだろうけど……\x02\x03",

            "#10302Fフフ、いわゆる吊り橋効果も考えて\x01",
            "そうなってるのかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0167
    ChrTalk(
        0x101,
        (
            "#00005F#6Pああ、恐怖で早くなる鼓動を、\x01",
            "恋愛感情と錯覚するっていう……\x01",
            "なんだか聞いたことがあるな。\x02\x03",

            "#00009Fカップルも多いって話だし\x01",
            "案外当たってるかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E90")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("ワジ")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            "フフ、僕にいたっては\x01",
            "こんなに綺麗な夕日まで\x01",
            "見せてもらってるわけだ。\x02\x03",

            "君との愛が芽生えてしまっても\x01",
            "何らおかしくない状況だよね。\x02",
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
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x101,
        (
            "#00012F#6Pイ、イヤイヤイヤイヤ……\x02\x03",

            "こんな夕日が見れて、\x01",
            "最後のチケットをとっておいて\x01",
            "正解だったな、とは思ったけど……\x02\x03",

            "#00003Fないない、それはないから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F6C")

    label("loc_5E90")


    #N0170
    NpcTalk(
        0x1B,
        "ワジ",
        (
            "#10304Fフフ、密室に２人きりのこの状況……\x02\x03",

            "#10309F君との愛が芽生えてしまっても\x01",
            "何らおかしくない状況だよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0171
    ChrTalk(
        0x101,
        (
            "#00012F#6Pイ、イヤイヤイヤイヤ……\x02\x03",

            "#00003Fないない、それはないから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F6C")


    #N0172
    NpcTalk(
        0x1B,
        "ワジ",
        (
            "#10304Fフフ、つれないなあ。\x01",
            "僕の気持ちは本気なんだよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x101,
        (
            "#00011F#6Pだ、だからそういうのは\x01",
            "やめてくれって！\x02",
        )
    )

    CloseMessageWindow()

    #N0174
    NpcTalk(
        0x1B,
        "ワジ",
        (
            "#10309Fフフ、やっぱり君って\x01",
            "からかいがいがあるよね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0175
    ChrTalk(
        0x101,
        "#00000F#6P……そろそろ到着みたいだな。\x05\x02",
    )

    CloseMessageWindow()

    #N0176
    NpcTalk(
        0x1B,
        "ワジ",
        "#10300Fああ、降りるとしようか。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0177
    NpcTalk(
        0x1B,
        "ワジ",
        "#10300Fフフ、なかなか楽しかったよ。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0179
    NpcTalk(
        0x1B,
        "ワジ",
        "#10300Fああ、また後で。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_44_56AC end

    def Function_45_6153(): pass

    label("Function_45_6153")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01102.itp")
    Call(0, 29)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x1B, 1000260, 0, 970, 0)
    SetChrChipByIndex(0x1B, 0x5)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0180
    NpcTalk(
        0x1B,
        "キーア",
        "#01105F#11Pわー、どんどん上がってくよー！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    Sleep(100)
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0181
    ChrTalk(
        0x101,
        (
            "#00012F#6Pキ、キーア、揺れて危ないから\x01",
            "ゴンドラの中では座ってような。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0xE1, 0x1F4)

    #N0182
    NpcTalk(
        0x1B,
        "キーア",
        (
            "#01105F#11Pあー、それもそうだねー。\x02\x03",

            "#01109Fえへへ、キーアはしゃいじゃった。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_95(0x1B, 1000610, 0, 40, 2000, 0x0)
    OP_93(0x1B, 0x10E, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    OP_0D()

    #N0183
    NpcTalk(
        0x1B,
        "キーア",
        (
            "#01100Fねーねー、ロイドー。\x02\x03",

            "#01109Fてっぺんはやっぱり\x01",
            "すっごい景色がいいのかなー？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_641B")

    #C0184
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、俺も初めてだから\x01",
            "まだ分からないけど……\x02\x03",

            "#00000Fきっと期待していいはずだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6481")

    label("loc_641B")


    #C0185
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、さっきも乗ったけど、\x01",
            "かなりいい景色だったよ。\x02\x03",

            "#00000Fきっと期待していいと思う。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6481")

    OP_63(0x1B, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    #N0186
    NpcTalk(
        0x1B,
        "キーア",
        (
            "#01109Fわくわくっ……\x01",
            "すっごく楽しみだねー！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x1B, 0x5)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, 1000610, 0, 40, 270)
    OP_0D()
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    Sleep(100)
    OP_9C(0x1B, 0x0, 0x0, 0x0, 0x12C, 0x7D0)
    OP_82(0x0, 0x32, 0x5DC, 0x12C)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x101,
        "#00011F#6Pわ、分かったから落ち着いてくれっ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x1B, 1000260, 0, 970, 0)
    SetChrChipByIndex(0x1B, 0x5)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 33)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677A")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("キーア")

    #A0188
    AnonymousTalk(
        0xFF,
        (
            "わあああっ、高ーい！！\x02\x03",

            "それに、空が真っ赤で\x01",
            "すっごくキレー！！\x02",
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

    #C0189
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ……\x01",
            "いい時間帯に乗れたみたいだ。\x02\x03",

            "#00009F最後のチケットを\x01",
            "とっておいて正解だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0190
    NpcTalk(
        0x1B,
        "キーア",
        (
            "#01102F#11Pえへへ、誘ってくれてありがと。\x02\x03",

            "#01110Fあっ、見て見てロイド！\x01",
            "今お魚が跳ねたよー！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67DE")

    label("loc_677A")


    #N0191
    NpcTalk(
        0x1B,
        "キーア",
        (
            "#01110F#11Pわあああっ、高ーい！！\x02\x03",

            "#01109Fあっ、見て見てロイド！\x01",
            "今お魚が跳ねたよー！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67DE")


    #C0192
    ChrTalk(
        0x101,
        (
            "#00002F#6Pああ、あれは何の魚だろうな。\x01",
            "さすがによく見えなかったけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)
    OP_93(0x1B, 0xE1, 0x1F4)

    #N0193
    NpcTalk(
        0x1B,
        "キーア",
        (
            "#01105F#11Pそういえば……\x02\x03",

            "#01100Fねーねー、ここの景色と、\x01",
            "オルキスタワーからの景色、\x01",
            "どっちが眺めがいいのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#00005F#6Pん？　そうだなあ。\x01",
            "高さでいえば断然に\x01",
            "オルキスタワーだけど……\x02\x03",

            "#00003Fこことは景色が全然違うから、\x01",
            "一概にどっちがいいとは\x01",
            "言えないかな。\x02",
        )
    )

    CloseMessageWindow()

    #N0195
    NpcTalk(
        0x1B,
        "キーア",
        (
            "#01103F#11Pむうう、なるほどー……\x02\x03",

            "#01109F……深いね、ロイド！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0196
    ChrTalk(
        0x101,
        (
            "#00012F#6P相当テンションが上がってるなあ……\x02\x03",

            "#00004F（……まあ、元気が出て何よりか。\x01",
            "  ひとまずは安心かな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0197
    NpcTalk(
        0x1B,
        "キーア",
        "#01110F#11Pあっ、またお魚が跳ねた！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, 1001000, 200, 0, 270)
    Call(0, 34)
    Sleep(3000)

    #C0198
    ChrTalk(
        0x101,
        (
            "#00000F#6Pそろそろ到着みたいだ。\x01",
            "キーア、降りようか。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0199
    NpcTalk(
        0x1B,
        "キーア",
        "#01100Fうん、オッケー！\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0200
    NpcTalk(
        0x1B,
        "キーア",
        (
            "#01109Fえへへ、眺めがよくって\x01",
            "すっごく楽しかったねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0202
    NpcTalk(
        0x1B,
        "キーア",
        "#01100Fうん！　またね、ロイド！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_45_6153 end

    def Function_46_6BEA(): pass

    label("Function_46_6BEA")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #N0203
    NpcTalk(
        0x1B,
        "フラン",
        (
            "#06404Fこの、地面がだんだんと\x01",
            "離れていってしまう感覚……\x02\x03",

            "#06409F観覧車に乗ると、いっつも\x01",
            "ドキドキしちゃうんですよね～。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D57")

    #C0204
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、俺も初めて乗るけど\x01",
            "本当に緊張するな。\x02\x03",

            "#00000Fフランはどっちかっていうと\x01",
            "ワクワクしてるって感じだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DD6")

    label("loc_6D57")


    #C0205
    ChrTalk(
        0x101,
        (
            "#00004F#6Pはは、気持ちは分かるよ。\x01",
            "本当に緊張するよな。\x02\x03",

            "#00000Fフランはどっちかっていうと\x01",
            "ワクワクしてるって感じだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DD6")

    SetChrSubChip(0x1B, 0x0)

    #N0206
    NpcTalk(
        0x1B,
        "フラン",
        (
            "#06402Fあ、分かります～？\x02\x03",

            "#06404Fなんせ、男の人と観覧車に乗るなんて\x01",
            "滅多にない経験ですからね～。\x02\x03",

            "#06409Fしかも、相手はロイドさんですし！\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは、『しかも』ってほどの\x01",
            "相手は務まらないかもしれないけど……\x02\x03",

            "#00000F考えてみれば君と２人きりってのも\x01",
            "なかなか珍しい機会だよな。\x02",
        )
    )

    CloseMessageWindow()

    #N0208
    NpcTalk(
        0x1B,
        "フラン",
        (
            "#06409Fふふ、せっかくですから\x01",
            "色々とお話しましょうね～！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 33)

    #N0209
    NpcTalk(
        0x1B,
        "フラン",
        "#06400Fあっ、ロイドさん見てください！\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#00000F#6Pああ、そろそろ頂上だな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7199")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("フラン")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            "はあああ～、たまりませんね。\x02\x03",

            "真っ赤な夕日が差して、\x01",
            "すっごくロマンチックです～！\x02",
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

    #C0212
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ……\x01",
            "いい時間帯に乗れたみたいだ。\x02\x03",

            "#00009F最後のチケットを\x01",
            "とっておいて正解だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0213
    NpcTalk(
        0x1B,
        "フラン",
        (
            "#06402Fふふ、誘ってくれて\x01",
            "本当にありがとうございました！\x02\x03",

            "前にお姉ちゃんとも乗りましたけど、\x01",
            "やっぱりすごくいい眺めです～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7213")

    label("loc_7199")


    #N0214
    NpcTalk(
        0x1B,
        "フラン",
        (
            "#06402Fはあああ～、たまりませんね。\x02\x03",

            "#06409F前にお姉ちゃんとも乗りましたけど、\x01",
            "やっぱりすごくいい眺めです～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7213")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x0)

    #C0215
    ChrTalk(
        0x101,
        (
            "#00005F#6Pそういえばフランは、\x01",
            "今まで男の人と付き合ったり\x01",
            "したことはないのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x0)

    #N0216
    NpcTalk(
        0x1B,
        "フラン",
        (
            "#06405Fええ、そうですけど……\x01",
            "なんでですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00012F#6Pい、いや……\x01",
            "特別な意味は無いんだけど。\x02\x03",

            "#00000Fフランだったらやっぱり、\x01",
            "かなりモテるんじゃないかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #N0218
    NpcTalk(
        0x1B,
        "フラン",
        (
            "#06402Fあはは、わたしなんて全然ですよ～？\x02\x03",

            "#06404Fそれに、お姉ちゃんより\x01",
            "かっこよくって頼りになる\x01",
            "男の人もなかなかいませんし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0219
    ChrTalk(
        0x101,
        "#00012F#6Pフランの基準はそこなのか……\x02",
    )

    CloseMessageWindow()

    #N0220
    NpcTalk(
        0x1B,
        "フラン",
        (
            "#06409Fえへへ、もちろんですよ。\x02\x03",

            "子供の頃から、わたしの一番は\x01",
            "いつだってお姉ちゃんですから！\x02\x03",

            "#06400Fあ、でもロイドさんだったら\x01",
            "ギリギリ及第点かもしれませんね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは……そりゃどうも。\x01",
            "（本当に姉妹仲がいいなあ……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0222
    ChrTalk(
        0x101,
        (
            "#00000F#6Pそろそろ到着みたいだ。\x01",
            "フラン、降りようか。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0223
    NpcTalk(
        0x1B,
        "フラン",
        "#06400Fはい、そうしましょう。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0224
    NpcTalk(
        0x1B,
        "フラン",
        (
            "#06400Fえへへ、眺めもよくって\x01",
            "とても楽しかったです～！\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0226
    NpcTalk(
        0x1B,
        "フラン",
        "#06400Fはい！　ではまた～。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_46_6BEA end

    def Function_47_7665(): pass

    label("Function_47_7665")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05900.itp")
    Call(0, 29)
    Call(0, 32)

    #N0227
    NpcTalk(
        0x1B,
        "セシル",
        (
            "#05900Fへえ……ゴンドラの中は\x01",
            "こんな風になっているのね。\x02\x03",

            "#05904Fまるで大きな揺りかごみたい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7792")

    #C0228
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、俺も初めて乗るけど\x01",
            "確かにそんな感じだね。\x02\x03",

            "#00000F結構揺れると思うし、\x01",
            "セシル姉、気をつけてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77F4")

    label("loc_7792")


    #C0229
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、確かにそんな感じかな。\x02\x03",

            "#00000F結構揺れるから、\x01",
            "セシル姉、気をつけてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77F4")


    #N0230
    NpcTalk(
        0x1B,
        "セシル",
        (
            "#05900Fふふ、ありがとうロイド。\x02\x03",

            "#05904Fロイドと２人っきりなのも\x01",
            "記念祭のアルカンシェル公演を\x01",
            "一緒に観に行って以来ね。\x02\x03",

            "#05909Fせっかくだから、\x01",
            "色々とおしゃべりましょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        (
            "#00005F#6Pあ、ああ……そうだね。\x02\x03",

            "#00003F（そう思うとなんだか\x01",
            "  緊張してきたな……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    #N0232
    NpcTalk(
        0x1B,
        "セシル",
        (
            "#05904Fふふ、それにしても\x01",
            "テーマパークって本当に楽しい所ね。\x02\x03",

            "#05902F可愛いみっしぃが出迎えてくれて、\x01",
            "楽しいアトラクションが沢山で……\x01",
            "まるで夢の世界に迷い込んだみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        "#00002F#6Pはは……確かにね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0234
    ChrTalk(
        0x101,
        (
            "#00008F#6P兄貴が生きてたら……\x01",
            "一緒に来てみたかった？\x02",
        )
    )

    CloseMessageWindow()

    #N0235
    NpcTalk(
        0x1B,
        "セシル",
        (
            "#05904Fふふ……ちょっとだけね。\x01",
            "あの頃はまだ、クロスベルに\x01",
            "こんな場所はなかったから。\x02\x03",

            "#05900Fでも、ガイさんと\x01",
            "何度か行ったデートも\x01",
            "負けないくらい楽しかったわ。\x02\x03",

            "#05909Fお食事に行った時なんか、\x01",
            "オススメの屋台とかを\x01",
            "沢山紹介してもらったし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0236
    ChrTalk(
        0x101,
        (
            "#00012F#6Pデ、デートで屋台かあ……\x02\x03",

            "#00006Fせっかくなんだから、\x01",
            "兄貴もお洒落な店とかを\x01",
            "探せばよかったのに。\x02",
        )
    )

    CloseMessageWindow()

    #N0237
    NpcTalk(
        0x1B,
        "セシル",
        (
            "#05905Fあら、とっても美味しくて\x01",
            "私は気に入ってたんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#00003F#6P（うーん……セシル姉と兄貴って、\x01",
            "  やっぱりお似合いだったんだよな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E56")

    #N0239
    NpcTalk(
        0x1B,
        "セシル",
        (
            "#05905Fあ……そろそろ頂上ね。\x02\x03",

            "#05909F赤い夕日がとっても綺麗……\x01",
            "病院から見える風景とは\x01",
            "また違って見えるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    #C0240
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ……\x01",
            "いい時間帯に乗れたみたいだ。\x02\x03",

            "#00009F最後のチケットを\x01",
            "とっておいて正解だったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1B, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("セシル")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            "ふふ、誘ってくれてありがとう。\x02\x03",

            "この夕日も、とっても素敵な\x01",
            "思い出になったわ。\x02",
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
    Jump("loc_7F2E")

    label("loc_7E56")


    #N0242
    NpcTalk(
        0x1B,
        "セシル",
        (
            "#05905Fあ……そろそろ頂上ね。\x02\x03",

            "#05909F湖がとっても綺麗……\x01",
            "病院から見える風景とは\x01",
            "また違って見えるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)

    #C0243
    ChrTalk(
        0x101,
        "#00002F#6Pああ……本当だね。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0244
    NpcTalk(
        0x1B,
        "セシル",
        (
            "#05902Fふふ、とっても素敵な\x01",
            "思い出になったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F2E")

    SetChrSubChip(0x101, 0x0)

    #C0245
    ChrTalk(
        0x101,
        "#00009F#6Pはは、喜んでくれて俺も嬉しいよ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0246
    ChrTalk(
        0x101,
        (
            "#00000F#6Pそろそろ到着みたいだ。\x01",
            "セシル姉、降りようか。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0247
    NpcTalk(
        0x1B,
        "セシル",
        "#05900Fうん、そうしましょう。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0248
    NpcTalk(
        0x1B,
        "セシル",
        (
            "#05900Fふふ、とても楽しかったわ。\x01",
            "ありがとうロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後で。\x02",
        )
    )

    CloseMessageWindow()

    #N0250
    NpcTalk(
        0x1B,
        "セシル",
        "#05900Fええ、また後でね。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_47_7665 end

    def Function_48_80A3(): pass

    label("Function_48_80A3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0251
    NpcTalk(
        0x1B,
        "イリア",
        (
            "#01704Fふむふむ……\x01",
            "あたし的にはちょっとだけ\x01",
            "物足りないところだけど……\x02\x03",

            "#01700Fこんなのんびりした乗り物も\x01",
            "たまには悪くないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824A")

    #C0252
    ChrTalk(
        0x101,
        (
            "#00002F#6Pはは、そう言ってもらえると\x01",
            "俺としても気が楽ですよ。\x02\x03",

            "#00004Fなんでも、頂上までいけば\x01",
            "かなり景色がいいらしいですし……\x02\x03",

            "#00000Fイリアさんにも充分に\x01",
            "楽しんでもらえると思いますけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8307")

    label("loc_824A")


    #C0253
    ChrTalk(
        0x101,
        (
            "#00002F#6Pはは、そう言ってもらえると\x01",
            "俺としても気が楽ですよ。\x02\x03",

            "#00004Fもっとも、頂上までいけば\x01",
            "かなり景色がいいですし……\x02\x03",

            "#00000Fイリアさんにも充分に\x01",
            "楽しんでもらえると思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8307")

    SetChrSubChip(0x1B, 0x0)

    #N0254
    NpcTalk(
        0x1B,
        "イリア",
        (
            "#01709Fそんなに眺めがいいんだ？\x01",
            "フフ、期待しちゃおうかしら。\x02\x03",

            "#01703Fんー、でもこのスピードだと\x01",
            "頂上までは少しかかりそうね。\x02\x03",

            "#01702Fふふ、折角の機会だから\x01",
            "腹を割って話でもしようじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#00012F#6Pえ、ええ、いいですよ。\x01",
            "（ちょっとイヤな予感がするけど……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)

    #N0256
    NpcTalk(
        0x1B,
        "イリア",
        (
            "#01709Fだからさー、\x01",
            "弟君が狙ってるのは結局誰なの？\x02\x03",

            "#01705Fやっぱりセシル？\x01",
            "それとも同僚のコたちの誰か？\x01",
            "もしかして、あたしやリーシャだったり？\x02\x03",

            "#01704Fあ、言っとくけどシュリはまだダメよ？\x01",
            "保護者として、立派に成長するまでは……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x101,
        (
            "#00006F#6Pちょ、ちょっと待ってください！\x02\x03",

            "#00011F誰狙いとかどうとか、\x01",
            "矢継ぎ早に質問されても……\x01",
            "その、困りますから！\x02",
        )
    )

    CloseMessageWindow()

    #N0258
    NpcTalk(
        0x1B,
        "イリア",
        (
            "#01706Fえー、いいじゃない。\x01",
            "勢いに任せてコッソリ教えてよ。\x02\x03",

            "#01700Fあたしはセシルの親友なんだし、\x01",
            "弟君にとってはもう１人の\x01",
            "お姉さんみたいなもんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#00012F#6Pそ、その理屈もおかしいんじゃ……\x01",
            "セシル姉も実姉じゃありませんし。\x02",
        )
    )

    CloseMessageWindow()

    #N0260
    NpcTalk(
        0x1B,
        "イリア",
        (
            "#01709Fえーい、ノリが悪い！\x01",
            "こうなったらくすぐってでも\x01",
            "吐かすわよ～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        (
            "#00011F#6P（ま、まずい、\x01",
            "  なんとか話題を変えないと……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    #C0262
    ChrTalk(
        0x101,
        (
            "#00005F#6Pあ、ああっイリアさん！\x01",
            "そうこうしてる間に、もうすぐ\x01",
            "頂上につくみたいですよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x1B, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C7")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("イリア")

    #A0263
    AnonymousTalk(
        0xFF,
        (
            "へえ……！\x01",
            "確かに相当景色がいいわね。\x02\x03",

            "それに、夕焼けで\x01",
            "湖が朱色に染まってるおかげで、\x01",
            "すっごく郷愁的っていうか……\x02",
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

    #C0264
    ChrTalk(
        0x101,
        (
            "#00004F#6Pええ……\x01",
            "いい時間帯に乗れたみたいです。\x02\x03",

            "#00009F最後のチケットを\x01",
            "とっておいて正解でしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0265
    NpcTalk(
        0x1B,
        "イリア",
        (
            "#01709Fフフ、正直言って想像以上よ。\x01",
            "誘ってくれてありがと。\x02\x03",

            "#01703Fうーん、このイメージを\x01",
            "何とかステージに生かせないかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AC2")

    label("loc_89C7")


    #N0266
    NpcTalk(
        0x1B,
        "イリア",
        (
            "#01705Fへえ……！\x01",
            "確かに相当景色がいいわね。\x02\x03",

            "#01709F大都市であるクロスベルで\x01",
            "こんな自然が見られるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#00000F#6Pはは……\x01",
            "考えてみれば意外ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #N0268
    NpcTalk(
        0x1B,
        "イリア",
        (
            "#01703Fうーん、このイメージを\x01",
            "何とかステージに生かせないかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AC2")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    #C0269
    ChrTalk(
        0x101,
        (
            "#00006F#6P（ふう……\x01",
            "  なんとか気が逸れてくれたか。）\x02\x03",

            "#00002F（それにしても、本当にどんな時でも\x01",
            "  ステージの事を考えてるんだな。\x01",
            "  さすがイリアさんっていうか……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0270
    ChrTalk(
        0x101,
        (
            "#00000F#6Pそろそろ到着みたいだ。\x01",
            "イリアさん、降りましょう。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0271
    NpcTalk(
        0x1B,
        "イリア",
        "#01700Fはいはい～っと。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0272
    NpcTalk(
        0x1B,
        "イリア",
        (
            "#01700Fフフ、なかなか楽しかったわ。\x01",
            "ありがとう、弟君。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#00000F#6P俺も誘ってよかったです。\x02\x03",

            "それじゃ、また後で。\x02",
        )
    )

    CloseMessageWindow()

    #N0274
    NpcTalk(
        0x1B,
        "イリア",
        "#01700Fうん、また後でね～。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_48_80A3 end

    def Function_49_8CC3(): pass

    label("Function_49_8CC3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)

    #N0275
    NpcTalk(
        0x1B,
        "リーシャ",
        (
            "#01802Fはあ……\x01",
            "観覧車っていいものですね。\x02\x03",

            "#01804Fゆったりしていて、静かで、\x01",
            "とても落ち着くというか。\x02\x03",

            "#01802F家族連れやカップルに\x01",
            "人気があるというのも、\x01",
            "なんだか分かる気がします。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E37")

    #C0276
    ChrTalk(
        0x101,
        (
            "#00004F#6Pはは、確かにな。\x02\x03",

            "#00000Fそれに聞いた話だと、\x01",
            "頂上からの景色も格別だそうだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E99")

    label("loc_8E37")


    #C0277
    ChrTalk(
        0x101,
        (
            "#00004F#6Pはは、確かにな。\x02\x03",

            "#00002Fそれにさっきも乗ったけど、\x01",
            "頂上からの景色も格別だったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E99")

    SetChrSubChip(0x1B, 0x0)

    #N0278
    NpcTalk(
        0x1B,
        "リーシャ",
        (
            "#01809Fふふ、それは楽しみですね。\x02\x03",

            "#01802Fそれじゃあ、頂上につくまで\x01",
            "色々お話でもしませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0279
    ChrTalk(
        0x101,
        (
            "#00002F#6Pああ、それなりに\x01",
            "時間がかかるだろうし\x01",
            "いいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    SetChrFlags(0x1B, 0x2)
    SetChrChipByIndex(0x1B, 0x22)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 33)

    #N0280
    NpcTalk(
        0x1B,
        "リーシャ",
        "#01804F……うつら……うつら……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#00012F#6P（うーん、なんだか眠そうにしてるな。）\x02\x03",

            "#00006F（毎日練習で大変だろうし、\x01",
            "  ビーチの疲れもあるのかも。）\x02\x03",

            "#00002F（もうすぐ頂上につきそうだけど、\x01",
            "  このまま寝かしてあげようかな……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x2)
    OP_0D()
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0282
    NpcTalk(
        0x1B,
        "リーシャ",
        "#01805Fはっ……\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        "#00005F#6Pっと、起きちゃったか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0284
    NpcTalk(
        0x1B,
        "リーシャ",
        (
            "#01805Fす、すみません！\x01",
            "つい、うとうとしてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#00009F#6Pはは、謝ることなんてないさ。\x01",
            "それより……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(250)
    SetChrSubChip(0x1B, 0x2)
    Sleep(250)
    OP_63(0x1B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_932E")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("リーシャ")

    #A0286
    AnonymousTalk(
        0xFF,
        (
            "あ……もう頂上なんですね。\x02\x03",

            "夕焼けの光が水面を朱に染めて……\x01",
            "とっても綺麗な眺めです。\x02",
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

    #C0287
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ……\x01",
            "いい時間帯に乗れたみたいだ。\x02\x03",

            "#00009F最後のチケットを\x01",
            "とっておいて正解だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0288
    NpcTalk(
        0x1B,
        "リーシャ",
        (
            "#01809Fふふ、誘っていただいて\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93C4")

    label("loc_932E")


    #N0289
    NpcTalk(
        0x1B,
        "リーシャ",
        (
            "#01805Fあ……もう頂上なんですね。\x02\x03",

            "#01802F周囲が広大な湖に囲まれて……\x01",
            "とっても綺麗な眺めです。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#00002F#6Pああ……いい景色だよな。\x02",
    )

    CloseMessageWindow()

    label("loc_93C4")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1B)

    #N0291
    NpcTalk(
        0x1B,
        "リーシャ",
        (
            "#01808F（……でも、こんな密室で２人きりの時に\x01",
            "  眠ってしまいそうになるなんて……）\x02\x03",

            "#01803F（いくら安らいでいたとはいえ、\x01",
            "  もし相手が《銀》の標的だったら……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0292
    ChrTalk(
        0x101,
        (
            "#00005F#6P……えっと、リーシャ？\x02\x03",

            "#00002Fもしまだ眠いんだったら、\x01",
            "気にせず寝ててもいいんだぞ？\x02\x03",

            "下に着いたら起こしてあげるしさ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0293
    NpcTalk(
        0x1B,
        "リーシャ",
        (
            "#01804F……いえ……\x01",
            "あまり綺麗なので呆けていました。\x02\x03",

            "#01802Fふふ、気にしないでください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0294
    ChrTalk(
        0x101,
        (
            "#00000F#6Pそろそろ到着みたいだ。\x01",
            "リーシャ、降りようか。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0295
    NpcTalk(
        0x1B,
        "リーシャ",
        "#01802Fはい。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    Call(0, 35)

    #N0296
    NpcTalk(
        0x1B,
        "リーシャ",
        (
            "#01802Fえっと、とても楽しかったです。\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0298
    NpcTalk(
        0x1B,
        "リーシャ",
        "#01802Fはい、また後で。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_49_8CC3 end

    def Function_50_96C2(): pass

    label("Function_50_96C2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04201.itp")
    Call(0, 29)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)
    Call(0, 32)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0299
    NpcTalk(
        0x1B,
        "シュリ",
        (
            "#04211Fわわっ、ぐんぐん上ってく……\x02\x03",

            "#04206Fお、おいこれ大丈夫なのか！？\x01",
            "こんな箱、ちょっとした衝撃で\x01",
            "簡単に落ちちまうんじゃ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0300
    ChrTalk(
        0x101,
        (
            "#00004F#6Pはは、心配しなくても\x01",
            "落ちる事なんてないって。\x02\x03",

            "#00002Fアルカンシェルの練習でも\x01",
            "高い所で飛んだりするんだし、\x01",
            "そんな怖がる事でも……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1B, 0x0)

    #N0301
    NpcTalk(
        0x1B,
        "シュリ",
        (
            "#04206Fこ、怖いわけじゃねーけど……\x01",
            "高さが段違いだろ！？\x02\x03",

            "#04201Fったく……\x01",
            "これで大した事なかったら\x01",
            "ぶん殴ってやるからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99A5")

    #C0302
    ChrTalk(
        0x101,
        (
            "#00006F#6P女の子がそんなこと\x01",
            "言うもんじゃないと思うけど……\x02\x03",

            "#00002Fまあ、聞いた話だと\x01",
            "頂上からの眺めは相当凄いらしい。\x02\x03",

            "怖さに見合うだけの価値は\x01",
            "充分にあるんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A59")

    label("loc_99A5")


    #C0303
    ChrTalk(
        0x101,
        (
            "#00006F#6P女の子がそんなこと\x01",
            "言うもんじゃないと思うけど……\x02\x03",

            "#00002Fまあ、さっきも乗ったけど\x01",
            "頂上からの眺めは相当凄いよ。\x02\x03",

            "怖さに見合うだけの価値は\x01",
            "充分にあるんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A59")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0304
    NpcTalk(
        0x1B,
        "シュリ",
        "#04206Fだ、だから怖がってなんかねーっつの！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 30)
    Call(0, 33)
    SetChrSubChip(0x1B, 0x2)
    SetChrSubChip(0x101, 0x1)

    #C0305
    ChrTalk(
        0x101,
        (
            "#00002F#6Pおっと……\x01",
            "このあたりが頂上付近だな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0306
    NpcTalk(
        0x1B,
        "シュリ",
        (
            "#04211Fあわわ……\x01",
            "や、やっぱり、高すぎ……！\x02\x03",

            "#04207Fお、降ろせ！　今すぐ降ろせ！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0307
    ChrTalk(
        0x101,
        (
            "#00012F#6Pどうどう、落ち着けって。\x02\x03",

            "#00002F下ばかり見てるから怖くなるんだ。\x01",
            "……ほら、向こうの方を見てみな。\x02",
        )
    )

    CloseMessageWindow()

    #N0308
    NpcTalk(
        0x1B,
        "シュリ",
        "#04205Fむ、向こうって……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E7A")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("シュリ")

    #A0309
    AnonymousTalk(
        0xFF,
        (
            "あ……\x02\x03",

            "水上バスでは分からなかったけど、\x01",
            "ここってこんなたくさんの水に\x01",
            "囲まれてたのか……\x02\x03",

            "それに、湖全体が夕焼けで\x01",
            "真っ赤に染まってすっごく綺麗だ……\x02",
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
        0x101,
        (
            "#00004F#6Pああ……\x01",
            "いい時間帯に乗れたみたいだ。\x02\x03",

            "#00009F最後のチケットを\x01",
            "とっておいて正解だったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0311
    NpcTalk(
        0x1B,
        "シュリ",
        (
            "#04203Fフ、フン……\x01",
            "礼なんか言わないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは……素直じゃないな。\x02\x03",

            "#00000Fでも、高い所にいる怖さなんか\x01",
            "吹っ飛んだんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F4A")

    label("loc_9E7A")


    #N0313
    NpcTalk(
        0x1B,
        "シュリ",
        (
            "#04205Fあ……\x02\x03",

            "水上バスでは分からなかったけど、\x01",
            "ここってこんなたくさんの水に\x01",
            "囲まれてたのか……\x02\x03",

            "#04202F……綺麗な眺めだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#00000F#6Pはは……高い所にいる怖さなんか\x01",
            "吹っ飛んだんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F4A")

    OP_63(0x1B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x1B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0315
    NpcTalk(
        0x1B,
        "シュリ",
        (
            "#04211Fう、うわっ！　高い高い！！\x02\x03",

            "#04206Fも、もーっ！！\x01",
            "思い出させるんじゃねーっての！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0316
    ChrTalk(
        0x101,
        "#00006F#6Pゴ、ゴメン。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 31)
    Call(0, 34)
    Sleep(3000)

    #C0317
    ChrTalk(
        0x101,
        (
            "#00000F#6Pそろそろ到着みたいだ。\x01",
            "シュリ、降りようか。\x05\x02",
        )
    )

    CloseMessageWindow()

    #N0318
    NpcTalk(
        0x1B,
        "シュリ",
        "#04200F……う、うん。\x05\x02",
    )

    CloseMessageWindow()
    Call(0, 36)
    Call(0, 28)
    Call(0, 24)
    SetChrChipByIndex(0x1B, 0x8)
    SetChrSubChip(0x1B, 0x0)
    Call(0, 35)

    #N0319
    NpcTalk(
        0x1B,
        "シュリ",
        (
            "#14012Fま、まあ……\x01",
            "そこそこ楽しかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00000F#6Pああ、俺も誘ってよかったよ。\x02\x03",

            "それじゃ、また後でな。\x02",
        )
    )

    CloseMessageWindow()

    #N0321
    NpcTalk(
        0x1B,
        "シュリ",
        "#14000Fフン、じゃあな。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 39)
    WaitChrThread(0x1B, 3)
    Return()

    # Function_50_96C2 end

    def Function_51_A136(): pass

    label("Function_51_A136")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(12330, 4300, -17760, 0)
    MoveCamera(336, 16, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(3220, 0)
    SetChrPos(0x101, 7370, 0, -12510, 45)
    SetChrPos(0xEF, 8660, 0, -13430, 20)
    OP_4B(0x1A, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0322
    ChrTalk(
        0x101,
        "#00005Fいた……！\x02",
    )

    CloseMessageWindow()
    OP_9C(0x1A, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x1A, 0x101, 500)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0323
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "きゃっ、見つかっちゃった☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8240, 4300, -19760, 0)
    MoveCamera(356, 30, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(3220, 0)
    SetChrPos(0x1A, 8450, 0, -12880, 200)
    SetChrPos(0x101, 7200, 0, -14240, 20)
    SetChrPos(0xEF, 8750, 0, -14780, 300)
    FadeToBright(1000, 0)
    OP_0D()

    #C0324
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、おにーさんって\x01",
            "本当に探すのが上手だネ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "本気のあたしを見つけ出すなんて、\x01",
            "並大抵のことじゃないんだから。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#00006Fそ、そこまで大層なことじゃ\x01",
            "ないような気がするんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "とにかく、あと２回見つけたら\x01",
            "おにーさんの勝ちだヨ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、がんばってネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A3BE():

        label("loc_A3BE")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_A3BE")

    QueueWorkItem2(0x101, 1, lambda_A3BE)

    def lambda_A3D0():

        label("loc_A3D0")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_A3D0")

    QueueWorkItem2(0xEF, 1, lambda_A3D0)
    SetChrFlags(0x1A, 0x1000)
    OP_95(0x1A, 10920, 0, -15100, 5000, 0x0)
    OP_95(0x1A, 6460, 0, -18160, 5000, 0x0)

    def lambda_A40F():
        OP_95(0xFE, 710, 0, -17500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A40F)
    Sleep(800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(-3070, 5000, -23400, 0)
    MoveCamera(39, 36, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(3220, 0)
    SetChrPos(0x101, -540, 0, -18390, 180)
    SetChrPos(0xEF, 530, 0, -18400, 180)
    SetChrFlags(0x1A, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    #C0329
    ChrTalk(
        0x101,
        (
            "#00012Fうーん、なんだかすごく\x01",
            "気に入られてる気がする……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_A537")

    #C0330
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、よかったじゃない。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_A597")

    #C0331
    ChrTalk(
        0x103,
        (
            "#00200F個人的には羨ましいです。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_A60E")

    #C0332
    ChrTalk(
        0x104,
        (
            "#00300Fハハ、ティオすけが見たら\x01",
            "羨ましがりそうだな。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_A670")

    #C0333
    ChrTalk(
        0x109,
        (
            "#10100Fふふ、いいじゃないですか。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_A6D4")

    #C0334
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、モテる男は辛いね。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみるとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_A734")

    #C0335
    ChrTalk(
        0x153,
        (
            "#01100Fえへへ、よかったねーロイド。\x02\x03",

            "それじゃ、次の隠れ場所を\x01",
            "探してみよー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_A7A2")

    #C0336
    ChrTalk(
        0x156,
        (
            "#06400Fふふ、よかったじゃないですか。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみるとしましょう～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A7A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_A815")

    #C0337
    ChrTalk(
        0x14C,
        (
            "#05900Fふふ、ロイドったら\x01",
            "本当にモテモテね。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみるとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_A879")

    #C0338
    ChrTalk(
        0x134,
        (
            "#01700Fふふ、よかったじゃない。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみるとしましょ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_A8E5")

    #C0339
    ChrTalk(
        0x135,
        (
            "#01802Fふふ、よかったじゃないですか。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみるとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A939")

    label("loc_A8E5")


    #C0340
    ChrTalk(
        0x166,
        (
            "#14000Fフン、いいじゃねえか。\x02\x03",

            "とにかく、次の隠れ場所を\x01",
            "探してみるとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_A96A")

    #C0341
    ChrTalk(
        0x101,
        "#00000Fええ、そうしましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A989")

    label("loc_A96A")


    #C0342
    ChrTalk(
        0x101,
        "#00000Fああ、そうしよう。\x02",
    )

    CloseMessageWindow()

    label("loc_A989")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C9, 5)
    OP_65(0x0, 0x1)
    OP_29(0x7F, 0x1, 0xD)
    SetChrPos(0x0, -200, 10, -18640, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_51_A136 end

    def Function_52_A9B9(): pass

    label("Function_52_A9B9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch24400.itc", 0x20)
    LoadChrToIndex("chr/ch24500.itc", 0x21)
    LoadChrToIndex("apl/ch50387.itc", 0x22)
    LoadEffect(0x0, "event\\eva02_00.eff")
    LoadEffect(0x1, "battle/ms00109.eff")
    SoundLoad(810)
    SoundLoad(862)
    SoundLoad(645)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x21)
    SetChrFlags(0x1D, 0x8000)
    OP_68(-510, 3010, -21510, 0)
    MoveCamera(48, 32, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(6590, 0)
    SetChrPos(0x101, 840, 1910, -27360, 0)
    SetChrPos(0x103, -60, 2190, -28450, 0)
    SetChrPos(0x102, 2750, 0, -18900, 180)
    SetChrPos(0x104, 2750, 90, -20300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_68(-1330, 3010, -21710, 3000)
    SetCameraDistance(8010, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_AAF6():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AAF6)
    Sleep(50)

    def lambda_AB13():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AB13)
    Sleep(500)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AB8A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB8A)
    Sleep(50)

    def lambda_AB9A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AB9A)
    Sleep(300)

    #C0343
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200Fあ、エリィにランディ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(6870, 3000)

    def lambda_ABDA():

        label("loc_ABDA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_ABDA")

    QueueWorkItem2(0x102, 1, lambda_ABDA)

    def lambda_ABEC():

        label("loc_ABEC")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_ABEC")

    QueueWorkItem2(0x104, 1, lambda_ABEC)

    def lambda_ABFE():
        OP_95(0xFE, 860, 0, -18960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABFE)
    Sleep(50)

    def lambda_AC1B():
        OP_95(0xFE, -120, 50, -20150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC1B)
    WaitChrThread(0x101, 1)

    def lambda_AC39():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC39)
    WaitChrThread(0x103, 1)

    def lambda_AC4A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC4A)
    OP_6F(0x10)
    Sleep(300)

    #C0344
    ChrTalk(
        0x104,
        "#00309Fいよっ、お疲れ。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        (
            "#00100Fうふふ、２人とも\x01",
            "がんばってるみたいね。\x02\x03",

            "調子はどうかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212Fいや、なかなか大変でさ……\x01",
            "着ぐるみの中も、暑いのなんの。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0347
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526Fロイドさん……\x01",
            "巡回は散歩じゃありません。\x02\x03",

            "#05521F愛想をふりまきつつ、\x01",
            "『見つけてラッキー☆』\x01",
            "な感じを出さないと。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206Fあ、ああ……分かったよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#00109Fティオちゃん……\x01",
            "みっしぃのこととなると\x01",
            "迫力が違うわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        "#00304Fはは、ロイドも形無しだなあ。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 2880, 1730, -1360, 170)

    #N0351
    NpcTalk(
        0x1D,
        "女性の声",
        "あっ、みっしぃだ～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AEBC():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AEBC)
    Sleep(50)

    def lambda_AECC():
        OP_95(0xFE, -7940, 0, -14050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AECC)
    Sleep(50)

    def lambda_AEE9():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AEE9)
    Sleep(50)

    def lambda_AEF9():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AEF9)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1C, 2710, 800, -7600, 180)
    SetChrPos(0x1D, 1300, 1050, -7030, 180)
    OP_68(-1280, 3010, -20050, 3000)

    def lambda_AF43():
        OP_95(0xFE, 1930, 0, -16000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_AF43)
    Sleep(50)

    def lambda_AF60():
        OP_95(0xFE, 830, 0, -15580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_AF60)
    OP_6F(0x1)
    WaitChrThread(0x1C, 1)
    OP_93(0x1C, 0xE1, 0x1F4)
    Sleep(300)

    #C0352
    ChrTalk(
        0x1C,
        (
            "ハハ、ホントだ。\x01",
            "観覧車帰りに会うなんて\x01",
            "ラッキーだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x1D,
        (
            "や～ん、カワイイ☆\x01",
            "ね、写真撮ってもらおうよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x1C,
        "ああ、そうだな。\x02",
    )

    CloseMessageWindow()
    OP_95(0x1C, 2800, 0, -17840, 2000, 0x0)
    TurnDirection(0x1C, 0x102, 500)

    def lambda_B030():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B030)
    Sleep(50)

    def lambda_B040():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B040)
    Sleep(300)

    #C0355
    ChrTalk(
        0x1C,
        (
            "あの、すみません。\x01",
            "こいつで写真とって\x01",
            "もらっていいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x102,
        "#00100Fええ、いいですよ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    OP_68(-1870, 3010, -20590, 3000)
    OP_95(0x102, 0, 690, -22620, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(300)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    OP_0D()

    #C0357
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F（しゃ、写真かぁ……\x01",
            "  こういうときは\x01",
            "  どうするべきかな？）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
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
            "彼氏の横に立つ\x01",      # 0
            "彼女の横に立つ\x01",      # 1
            "２人の間に立つ\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2290, 3010, -22170, 0)
    MoveCamera(35, 29, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(5360, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B1EF"),
        (1, "loc_B2D0"),
        (2, "loc_B3D5"),
        (SWITCH_DEFAULT, "loc_B498"),
    )


    label("loc_B1EF")

    SetChrPos(0x101, 0, 0, -18900, 180)
    SetChrPos(0x1C, 1000, 0, -18900, 180)
    SetChrPos(0x1D, -1000, 0, -18900, 180)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 53)
    WaitChrThread(0x101, 3)
    Sleep(500)
    OP_63(0x1D, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0358
    ChrTalk(
        0x1D,
        "きゃっ、ずる～い！\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x1C,
        (
            "ははは、\x01",
            "いいだろいいだろ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        (
            "#00109Fそれじゃあ、撮りますね。\x02\x03",

            "#00102Fはい、チーズ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B498")

    label("loc_B2D0")

    SetChrPos(0x101, 0, 0, -18900, 180)
    SetChrPos(0x1C, 1000, 0, -18900, 180)
    SetChrPos(0x1D, -1000, 0, -18900, 180)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 54)
    WaitChrThread(0x101, 3)
    Sleep(500)

    #C0361
    ChrTalk(
        0x1D,
        (
            "きゃっ、やったあ！\x01",
            "みっしぃひとりじめ～♪\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x1C,
        (
            "は、ははは……\x01",
            "（もやっ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#00111F（もやっ……）\x02\x03",

            "#00109F……え、えっと。\x01",
            "それじゃあ、撮りますね。\x02\x03",

            "#00102Fはい、チーズ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B498")

    label("loc_B3D5")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 7)
    SetChrPos(0x101, 0, 0, -18900, 180)
    SetChrPos(0x1C, 1000, 0, -18900, 180)
    SetChrPos(0x1D, -1000, 0, -18900, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0364
    ChrTalk(
        0x1D,
        (
            "うふふ、\x01",
            "今日はみっしぃ記念日ね☆\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x1C,
        "よろしくッス～。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x102,
        (
            "#00109Fそれじゃあ、撮りますね。\x02\x03",

            "#00102Fはい、チーズ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B498")

    label("loc_B498")

    Sound(810, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0367
    ChrTalk(
        0x1D,
        "ありがとうございました～。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x1C,
        "どもっす。\x02",
    )

    CloseMessageWindow()

    def lambda_B50D():
        OP_95(0xFE, 0, 440, -21620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B50D)
    Sleep(50)

    def lambda_B52A():
        OP_95(0xFE, -1000, 440, -20620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B52A)
    WaitChrThread(0x1D, 1)

    def lambda_B548():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B548)
    WaitChrThread(0x1C, 1)

    def lambda_B559():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B559)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(500)

    #C0369
    ChrTalk(
        0x102,
        "#00100Fはい、どうぞ。\x02",
    )

    CloseMessageWindow()
    OP_97(0x1C, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_B5A8():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_B5A8)
    Sleep(50)

    def lambda_B5C5():
        OP_95(0xFE, -940, 2840, -31020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B5C5)
    Sleep(50)

    def lambda_B5E2():
        OP_95(0xFE, 0, 0, -18900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5E2)

    def lambda_B5FC():
        OP_95(0xFE, -400, 0, -17600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B5FC)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7A7")

    #C0370
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204Fふう……\x01",
            "今のでよかったのかな？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    #Sound(2680, 255, 100, 0)    #voice#Tio

    #C0371
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524Fバッチリです、ロイドさん。\x02\x03",

            "#05520Fみっしぃはいわば、\x01",
            "テーマパークの象徴……\x01",
            "歩く観光名所のようなものです。\x02\x03",

            "#05524Fああいう場合は、\x01",
            "きちんと真ん中に立つのが\x01",
            "モア・ベターだと思います。\x02\x03",

            "#05522Fなかなかみっしぃも\x01",
            "板についてきましたね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0372
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05209Fはは、ありがとう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x5)
    Jump("loc_BA32")

    label("loc_B7A7")


    #C0373
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204Fふう……\x01",
            "今のでよかっ──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x103, 0x101, 0xFA, 0x1388, 0x0)
    PlayEffect(0x1, 0x0, 0xFF, 0x0, 0, 300, -18900, 180, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(645, 0, 30, 0)
    Sound(862, 0, 50, 0)
    Sound(811, 0, 100, 0)
    OP_9B(0x1, 0x103, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    #Sound(3318, 255, 100, 0)    #voice#Lloyd

    #C0374
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211Fどわっ！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCF6)
    TurnDirection(0x101, 0x103, 500)
    #Sound(2682, 255, 100, 0)    #voice#Tio

    #C0375
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F……ロイドさんにはがっかりです。\x02\x03",

            "#05531F……なぜ、わざわざ\x01",
            "立ち位置を変えたんです？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205Fい、いや……\x01",
            "カップルの間に入るのも\x01",
            "どうかと思って……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526Fはあ……\x01",
            "よく考えてください。\x02\x03",

            "#05520Fみっしぃはいわば、\x01",
            "テーマパークの象徴……\x01",
            "歩く観光名所のようなものです。\x02\x03",

            "#05531Fああいう場合は、\x01",
            "きちんと真ん中に立つのが\x01",
            "モア・ベターだと思います。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206Fそ、そうか……\x01",
            "（余計なことを\x01",
            "  しなきゃよかったな……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x6)

    label("loc_BA32")


    #C0379
    ChrTalk(
        0x102,
        (
            "#00104Fふふ、その調子だと\x01",
            "ティオちゃんがいれば\x01",
            "きっと大丈夫ね。\x02\x03",

            "#00100F二人とも、がんばって。\x01",
            "私たちも見守ってるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x104,
        (
            "#00309Fがはは、\x01",
            "デートがてらにな！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 1000)
    Sleep(300)

    #C0381
    ChrTalk(
        0x102,
        "#00103F違います。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)
    Sleep(300)

    #C0382
    ChrTalk(
        0x104,
        "#00306Fぐはっ、即答……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0383
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200Fはは……できるだけ\x01",
            "上手くこなしてみるよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520Fでは、次にいきましょう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_A9B9 end

    def Function_53_BBA3(): pass

    label("Function_53_BBA3")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0x6A4, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_BBE4():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BBE4)
    Sleep(50)

    def lambda_BC01():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC01)
    WaitChrThread(0x1C, 1)

    def lambda_BC1F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_BC1F)
    WaitChrThread(0x101, 1)

    def lambda_BC30():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC30)
    Return()

    # Function_53_BBA3 end

    def Function_54_BC39(): pass

    label("Function_54_BC39")

    OP_97(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x101, 0xFFFFF95C, 0x0, 0x0, 0x7D0, 0x0)
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)

    def lambda_BC7A():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BC7A)
    Sleep(50)

    def lambda_BC97():
        OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC97)
    WaitChrThread(0x1D, 1)

    def lambda_BCB5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BCB5)
    WaitChrThread(0x101, 1)

    def lambda_BCC6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCC6)
    Return()

    # Function_54_BC39 end

    def Function_55_BCCF(): pass

    label("Function_55_BCCF")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0385
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "テーマパークの\x01",
            "見取り図が描かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_55_BCCF end

    def Function_56_BD0D(): pass

    label("Function_56_BD0D")

    EventBegin(0x1)
    TurnDirection(0x14, 0x0, 500)
    OP_4B(0x14, 0xFF)

    #C0386
    ChrTalk(
        0x14,
        (
            "お客様、観覧車にお乗りの際は\x01",
            "こちらの方にチケットを\x01",
            "お渡しくださいませー。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -330, 0, -15900, 350)
    OP_93(0x14, 0xA0, 0x0)
    OP_4C(0x14, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_56_BD0D end

    SaveToFile()

Try(main)
