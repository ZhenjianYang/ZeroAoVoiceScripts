from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0150.bin",                # FileName
        "c0150",                    # MapName
        "c0150",                    # Location
        0x0007,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 7, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0150",                  # 0
        "ホイストフ",             # 1
        "ブラウン",               # 2
        "セルテオ",               # 3
        "ノンノ",                 # 4
        "秘書アーネスト",         # 5
        "グレイス",               # 6
        "フロテ",                 # 7
        "キンドール",             # 8
        "ビジネスマン",           # 9
        "ビジネスマン",           # 10
        "観光客",                 # 11
        "市民",                   # 12
        "市民",                   # 13
        "市民",                   # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "観光客",                 # 17
        "観光客",                 # 18
        "仲立ち人",               # 19
        "青年",                   # 20
        "女性",                   # 21
        "観光客",                 # 22
        "観光客",                 # 23
        "観光客",                 # 24
        "ジロンド",               # 25
        "ドノバン警部",           # 26
        "レイモンド捜査官",       # 27
        "ロバーツ主任",           # 28
        "フラン",                 # 29
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch21302.itc",                   # 04
        "chr/ch27600.itc",                   # 05
        "chr/ch20402.itc",                   # 06
        "chr/ch32302.itc",                   # 07
        "chr/ch33202.itc",                   # 08
        "chr/ch21002.itc",                   # 09
        "chr/ch22002.itc",                   # 0A
        "chr/ch20502.itc",                   # 0B
        "chr/ch24102.itc",                   # 0C
        "chr/ch21202.itc",                   # 0D
        "chr/ch24502.itc",                   # 0E
        "chr/ch23702.itc",                   # 0F
        "chr/ch21802.itc",                   # 10
        "chr/ch20200.itc",                   # 11
        "chr/ch27602.itc",                   # 12
        "chr/ch02302.itc",                   # 13
        "chr/ch30300.itc",                   # 14
        "chr/ch30200.itc",                   # 15
        "chr/ch06002.itc",                   # 16
        "chr/ch29300.itc",                   # 17
        "chr/ch34302.itc",                   # 18
    ))

    DeclNpc(-509,    0,       12449,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-42889,  0,       5699,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-52029,  0,       3650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-8880,   0,       3240,    45,   261,  0x0, 0,   3,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(-3250,   150,     4570,    180,  469,  0x0, 0,   19,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-3299,   0,       4480,    180,  469,  0x0, 0,   22,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(-7449,   150,     8510,    270,  341,  0x0, 0,   24,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(2450,    5150,    17559,   180,  469,  0x0, 0,   16,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(8739,    5000,    14520,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(2450,    5150,    13479,   0,    469,  0x0, 0,   18,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(4559,    150,     5920,    180,  469,  0x0, 0,   6,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(3259,    150,     -6150,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   21,  255,  0)
    DeclNpc(1009,    0,       -3920,   90,   469,  0x0, 0,   12,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(1009,    0,       -3920,   90,   469,  0x0, 0,   9,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   6,   0,   255, 255, 0,   24,  255,  0)
    DeclNpc(6400,    5150,    13449,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(6400,    5150,    17700,   180,  469,  0x0, 0,   11,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(1009,    0,       -3920,   90,   469,  0x0, 0,   13,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   6,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   4,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(3210,    150,     -1879,   180,  469,  0x0, 0,   15,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(3210,    150,     -6130,   0,    469,  0x0, 0,   14,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-1159,   150,     2180,    270,  469,  0x0, 0,   7,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(60580,   -1000,   -8600,   270,  261,  0x0, 0,   17,  0,   0,   0,   0,   5,   255,  0)
    DeclNpc(56610,   -1000,   -11899,  270,  405,  0x0, 0,   20,  0,   0,   0,   0,   6,   255,  0)
    DeclNpc(55229,   -1000,   -11899,  90,   405,  0x0, 0,   21,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(57790,   -1000,   -12300,  90,   405,  0x0, 0,   23,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(59140,   -1000,   -8880,   1500,    60580,   500,     -8600,   0x007E, 0,  4,  0x0000)
    DeclActor(-510,    0,       10640,   1000,    -510,    1500,    12450,   0x007E, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_518",          # 00, 0
        "Function_1_5D0",          # 01, 1
        "Function_2_66D",          # 02, 2
        "Function_3_8B5",          # 03, 3
        "Function_4_8E9",          # 04, 4
        "Function_5_8ED",          # 05, 5
        "Function_6_2243",         # 06, 6
        "Function_7_2824",         # 07, 7
        "Function_8_2903",         # 08, 8
        "Function_9_2907",         # 09, 9
        "Function_10_33B4",        # 0A, 10
        "Function_11_411C",        # 0B, 11
        "Function_12_43CC",        # 0C, 12
        "Function_13_50AF",        # 0D, 13
        "Function_14_5A70",        # 0E, 14
        "Function_15_5B25",        # 0F, 15
        "Function_16_5E54",        # 10, 16
        "Function_17_6E45",        # 11, 17
        "Function_18_712F",        # 12, 18
        "Function_19_7294",        # 13, 19
        "Function_20_7491",        # 14, 20
        "Function_21_7675",        # 15, 21
        "Function_22_787F",        # 16, 22
        "Function_23_79F6",        # 17, 23
        "Function_24_7C52",        # 18, 24
        "Function_25_7E9F",        # 19, 25
        "Function_26_7FA9",        # 1A, 26
        "Function_27_82A0",        # 1B, 27
        "Function_28_857A",        # 1C, 28
        "Function_29_8C3B",        # 1D, 29
        "Function_30_90F3",        # 1E, 30
        "Function_31_938C",        # 1F, 31
        "Function_32_9595",        # 20, 32
        "Function_33_9754",        # 21, 33
        "Function_34_975E",        # 22, 34
        "Function_35_9A3E",        # 23, 35
        "Function_36_9E17",        # 24, 36
        "Function_37_A2D3",        # 25, 37
        "Function_38_DEA0",        # 26, 38
        "Function_39_E763",        # 27, 39
        "Function_40_F483",        # 28, 40
        "Function_41_F6E6",        # 29, 41
        "Function_42_FE04",        # 2A, 42
    ))


    def Function_0_518(): pass

    label("Function_0_518")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_558"),
        (1, "loc_564"),
        (2, "loc_570"),
        (3, "loc_57C"),
        (4, "loc_588"),
        (5, "loc_594"),
        (6, "loc_5A0"),
        (SWITCH_DEFAULT, "loc_5AC"),
    )


    label("loc_558")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_564")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_570")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_57C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_588")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_594")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B8")

    label("loc_5CF")

    Return()

    # Function_0_518 end

    def Function_1_5D0(): pass

    label("Function_1_5D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66C")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_5D0")

    label("loc_66C")

    Return()

    # Function_1_5D0 end

    def Function_2_66D(): pass

    label("Function_2_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_67C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 37)

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6A6")
    SetChrPos(0xB, -7600, 0, 6990, 0)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_8B4")

    label("loc_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6B9")
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_8B4")

    label("loc_6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6D1")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_8B4")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_6DF")
    Jump("loc_8B4")

    label("loc_6DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6FC")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_8B4")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_70A")
    Jump("loc_8B4")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_74C")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrSubChip(0xD, 0x1)
    SetChrPos(0xB, -1730, 0, 4050, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_8B4")

    label("loc_74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_777")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_772")
    ClearChrFlags(0xC, 0x80)

    label("loc_772")

    Jump("loc_8B4")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7BC")
    SetChrPos(0xA, 6790, 0, 13090, 180)
    SetChrPos(0xB, 6790, 0, 11430, 0)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_8B4")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7E3")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_8B4")

    label("loc_7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_800")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_8B4")

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_82C")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_8B4")

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_84E")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_8B4")

    label("loc_84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_870")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_8B4")

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_897")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_8B4")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8B4")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    label("loc_8B4")

    Return()

    # Function_2_66D end

    def Function_3_8B5(): pass

    label("Function_3_8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8E8")

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8E8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8E8")

    label("loc_8E8")

    Return()

    # Function_3_8B5 end

    def Function_4_8E9(): pass

    label("Function_4_8E9")

    Call(0, 5)
    Return()

    # Function_4_8E9 end

    def Function_5_8ED(): pass

    label("Function_5_8ED")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA4")

    #C0001
    ChrTalk(
        0x20,
        (
            "へい、らっしゃい。\x01",
            "と言いてえところだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x20,
        (
            "坊主ら、クロスベルじゃ\x01",
            "許可証がなきゃ武器は売れねえんだぜ。\x01",
            "冷やかしなら帰るんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0000Fあ、いや俺たちは\x01",
            "クロスベル警察の者ですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x20,
        "お前らみたいなのが警察……？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x20,
        (
            "そうか、セルゲイの奴が\x01",
            "言っていた例の……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x20,
        (
            "フン、分かったぜ。\x01",
            "好きに見ていけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x20,
        (
            "武器を買うときは\x01",
            "俺に捜査手帳を見せな。\x01",
            "それが許可証代わりだからよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 2)

    label("loc_AA4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B2B")
    OP_AF(0x5)
    Jump("loc_B6D")

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B3B")
    OP_AF(0x4)
    Jump("loc_B6D")

    label("loc_B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B4B")
    OP_AF(0x3)
    Jump("loc_B6D")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B5B")
    OP_AF(0x2)
    Jump("loc_B6D")

    label("loc_B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B6B")
    OP_AF(0x1)
    Jump("loc_B6D")

    label("loc_B6B")

    OP_AF(0x0)

    label("loc_B6D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_223A")

    label("loc_B7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B90")
    Jump("loc_223A")

    label("loc_B90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 36)
    Jump("loc_223A")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFE")

    #C0008
    ChrTalk(
        0x20,
        (
            "へいらっしゃい、\x01",
            "と言いてえ所だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x20,
        (
            "そろそろ店を閉めるぜ。\x01",
            "買い物ならさっさとしてくんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#0300F店主さんも相変わらず\x01",
            "売る気ないッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x20,
        "おう、俺は売る気ゼロだぜ。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x20,
        (
            "そういや……空港の方で\x01",
            "何か事件があったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x20,
        "最近はどうも物騒な気がするぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D4D")

    label("loc_CFE")


    #C0014
    ChrTalk(
        0x20,
        (
            "空港の方で\x01",
            "何か事件があったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x20,
        "最近はどうも物騒な気がするぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_D4D")

    Jump("loc_223A")

    label("loc_D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_EE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8E")

    #C0016
    ChrTalk(
        0x20,
        "……ダドリーじゃねえか。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x20,
        (
            "支援課と行動してるなんて珍しいな。\x01",
            "あんたも焼きが回っちまったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10A,
        (
            "#0603F聞き捨てならんな、店主。\x02\x03",

            "#0600Fこいつらと行動しているんじゃない。\x01",
            "こいつらを率いて捜査中なんだ！\x02\x03",

            "……それと、この事は\x01",
            "他言無用にしておけよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x20,
        "へいへい、分かってるよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EE4")

    label("loc_E8E")


    #C0020
    ChrTalk(
        0x20,
        (
            "にしても一課のエースが\x01",
            "支援課となぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x20,
        (
            "珍しい組み合わせも\x01",
            "あったもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE4")

    Jump("loc_223A")

    label("loc_EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE2")

    #C0022
    ChrTalk(
        0x20,
        (
            "なんだ……朝っぱらから\x01",
            "武器を買いに来たのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x20,
        "無粋なことしやがるな。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x20,
        (
            "武器を選ぶなら\x01",
            "午後からにしたらどうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#0200F店主さんの場合\x01",
            "ただのんびりしたいだけでは……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x20,
        (
            "まあ一言で言えば\x01",
            "そういうことだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1041")

    label("loc_FE2")


    #C0027
    ChrTalk(
        0x20,
        (
            "午前中は雑誌でも読みつつ\x01",
            "のんびり過ごす事に決めてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x20,
        "あんま邪魔せんでくれんか。\x02",
    )

    CloseMessageWindow()

    label("loc_1041")

    Jump("loc_223A")

    label("loc_1046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1134")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F0")

    #C0029
    ChrTalk(
        0x20,
        (
            "へい、らっしゃい。\x01",
            "何か見ていくか？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x20,
        (
            "俺はあんま売る気がねえ。\x01",
            "適当に見ていってくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#0100Fあ、相変わらず\x01",
            "商売気がないですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_112F")

    label("loc_10F0")


    #C0032
    ChrTalk(
        0x20,
        (
            "俺はあんま売る気がねえ。\x01",
            "見たきゃ適当に見ていってくれや。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112F")

    Jump("loc_223A")

    label("loc_1134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_11B9")

    #C0033
    ChrTalk(
        0x20,
        (
            "なんでえ、支援課の\x01",
            "坊主たちじゃねえか。\x01",
            "こんな時間まで仕事か？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x20,
        (
            "うちはもう店じまいだぜ。\x01",
            "ほれ、帰った帰った！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_11B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1346")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12DD")

    #C0035
    ChrTalk(
        0x20,
        (
            "近頃ルバーチェの連中が\x01",
            "頻繁に揉め事を起こしてるだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x20,
        (
            "お陰で遊撃士の連中が\x01",
            "大忙しだってぼやいてやがったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x20,
        (
            "警察のお前らも\x01",
            "もう少し頑張った方が\x01",
            "いいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#0000Fははは……すみません。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#0300Fマフィア絡みは\x01",
            "捜査一課の担当だけどなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1341")

    label("loc_12DD")


    #C0040
    ChrTalk(
        0x20,
        (
            "近頃ルバーチェの連中が\x01",
            "頻繁に揉め事を起こしてるだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x20,
        (
            "お陰で遊撃士連中は\x01",
            "大活躍らしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1341")

    Jump("loc_223A")

    label("loc_1346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_16A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B0")

    #C0042
    ChrTalk(
        0x20,
        "……お前らか。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x20,
        (
            "最近見なかったな。\x01",
            "何してたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0000Fはは、少し色々と……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x153,
        (
            "#1110Fわー、なにこれー！\x01",
            "知らないモノがいっぱいだー！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x20,
        (
            "お嬢ちゃん、触っちゃ駄目だぜ。\x01",
            "ここにあるのは\x01",
            "みんな危ねえもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x20,
        (
            "ほらお前ら、\x01",
            "とっとと帰った帰った。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x20,
        (
            "子供づれに売るような\x01",
            "物は置いてねえぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 7)
    Jump("loc_169D")

    label("loc_14B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163F")

    #C0049
    ChrTalk(
        0x20,
        (
            "ほらお前ら、\x01",
            "とっとと帰った帰った。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x20,
        (
            "ウチには子供づれに\x01",
            "売るような物は置いてねえぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#0004F（……とか言いつつ\x01",
            "  頼めば出してくれるんだよな。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_159A")

    #C0052
    ChrTalk(
        0x102,
        (
            "#0100F（ここのご主人は\x01",
            "  中々いい人だものね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1637")

    label("loc_159A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_15EF")

    #C0053
    ChrTalk(
        0x103,
        (
            "#0200F（まあ、ここの店主さんは\x01",
            "  見かけによらずいい人ですから。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1637")

    label("loc_15EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1637")

    #C0054
    ChrTalk(
        0x104,
        (
            "#0300F（ま、ここのオッサン\x01",
            "  その辺りは常識人だからな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1637")

    SetScenarioFlags(0x0, 0)
    Jump("loc_169D")

    label("loc_163F")


    #C0055
    ChrTalk(
        0x20,
        (
            "ほらお前ら、\x01",
            "とっとと帰った帰った。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x20,
        (
            "ウチには子供づれに\x01",
            "売るような物は置いてねえぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_169D")

    Jump("loc_223A")

    label("loc_16A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_17A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1747")

    #C0057
    ChrTalk(
        0x20,
        (
            "近頃マフィア絡みの\x01",
            "事件が多いらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x20,
        "遊撃士の兄ちゃんから聞いたぜ。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x20,
        (
            "何でも……外国のマフィアと\x01",
            "抗争をやってるんだって？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17A3")

    label("loc_1747")


    #C0060
    ChrTalk(
        0x20,
        (
            "チッ、相変わらず\x01",
            "クロスベルは物騒な街だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x20,
        (
            "何も知らねえ観光客が\x01",
            "哀れに感じるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A3")

    Jump("loc_223A")

    label("loc_17A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_186B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1839")

    #C0062
    ChrTalk(
        0x20,
        "……朝から客か。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x20,
        (
            "ウチは自慢じゃないが\x01",
            "クロスベルで一番しけた店だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x20,
        (
            "朝くらい\x01",
            "ゆっくりさせてくれねえか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1866")

    label("loc_1839")


    #C0065
    ChrTalk(
        0x20,
        (
            "……仕方ねえ。\x01",
            "そろそろ店を開けるか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1866")

    Jump("loc_223A")

    label("loc_186B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_18D7")

    #C0066
    ChrTalk(
        0x20,
        (
            "ん……？\x01",
            "なんだ、こんな時間から。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x20,
        (
            "買い物ならさっさとしな。\x01",
            "ウチはそろそろ閉めるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_18D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1951")

    #C0068
    ChrTalk(
        0x20,
        (
            "チッ、今日は客が多いな……\x01",
            "おちおち雑誌も読んでられねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x20,
        (
            "お前ら、用が済んだら\x01",
            "とっとと帰れよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_1951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A05")

    #C0070
    ChrTalk(
        0x20,
        (
            "ルバーチェの連中は\x01",
            "もう釈放されちまったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x20,
        (
            "やれやれ、警察も\x01",
            "もう少し踏ん張れなかったのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x20,
        (
            "これじゃ市民にも\x01",
            "示しがつかんだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A6C")

    label("loc_1A05")


    #C0073
    ChrTalk(
        0x20,
        "フウ……まあ俺には関係ねえがな。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x20,
        (
            "いつもこの調子じゃ、市民が\x01",
            "警察を信用しないのも無理ねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6C")

    Jump("loc_223A")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B87")

    #C0075
    ChrTalk(
        0x20,
        (
            "お前らハルトマン議長って\x01",
            "知ってるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x20,
        (
            "帝国派議員どもの親玉、\x01",
            "クロスベルきっての\x01",
            "大物政治家の１人だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x20,
        (
            "実はヤツが\x01",
            "次の市長選に出馬するって\x01",
            "噂があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x20,
        (
            "そのために各方面に\x01",
            "コネクション作りしてるらしいぜ。\x01",
            "ったくゾッとしねえな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C1D")

    label("loc_1B87")


    #C0079
    ChrTalk(
        0x20,
        (
            "あのハルトマン議長が\x01",
            "次の市長選に出馬するって\x01",
            "噂があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x20,
        (
            "あんな男が市長なんかになったら\x01",
            "……クロスベルはこの先\x01",
            "どうなっちまうのかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1D")

    Jump("loc_223A")

    label("loc_1C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D24")

    #C0081
    ChrTalk(
        0x20,
        (
            "なんだ、また客か。\x01",
            "……ったく面倒だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#0012Fな、なんだか迷惑そうですが……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x20,
        "おう、迷惑だぜ？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x20,
        (
            "俺は一日ここに座って\x01",
            "のんびり雑誌が読めりゃあいいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x20,
        (
            "客なんて来ねえ方がいい。\x01",
            "お前らも用が済んだら帰れよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 1)
    Jump("loc_1E98")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E23")

    #C0086
    ChrTalk(
        0x20,
        (
            "クロスベルで武器を\x01",
            "扱ってる店は意外と少なくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x20,
        (
            "警察や遊撃士なんかは\x01",
            "よく立ち寄っていきやがるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x20,
        (
            "……ま、それは表の話で\x01",
            "物事には裏ってものがあるがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x20,
        (
            "旧市街の方には\x01",
            "でかい密輸店があるって噂だ。\x01",
            "あんま関わんなよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E98")

    label("loc_1E23")


    #C0090
    ChrTalk(
        0x20,
        (
            "旧市街の方には\x01",
            "でかい密輸店があるって噂だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x20,
        (
            "当然扱ってるのは\x01",
            "真っ当な品じゃないはずだ。\x01",
            "あんま関わんなよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E98")

    Jump("loc_223A")

    label("loc_1E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_20E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2052")
    SetScenarioFlags(0x4C, 4)

    #C0092
    ChrTalk(
        0x20,
        (
            "そういや嬢ちゃん、\x01",
            "あの男がまた来たぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x103,
        "#0205Fえ……主任ですか？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x20,
        (
            "ああ、前と同じように\x01",
            "魔導杖を置いていきやがった。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x20,
        (
            "買い取るなら\x01",
            "早いことお願いするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        "#0203Fりょ、了解です。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x102,
        (
            "#0100Fティオちゃんの上司って\x01",
            "何だかまどろっこしい事をする人ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0000Fああ……どうしてティオに\x01",
            "直接渡さないんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x103,
        (
            "#0201F（主任……\x01",
            "  いい加減にしないと\x01",
            "  怒りますよ？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E1")

    label("loc_2052")


    #C0100
    ChrTalk(
        0x20,
        (
            "そういや、今朝は\x01",
            "ダドリーのやつも来たんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x20,
        (
            "あいつも近頃忙しそうだな。\x01",
            "昔っから真面目一徹なヤロウだし、\x01",
            "体を壊さねえか心配だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E1")

    Jump("loc_223A")

    label("loc_20E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2178")

    #C0102
    ChrTalk(
        0x20,
        (
            "クロスベルじゃ、武器の携帯には\x01",
            "許可証が必要って事になってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x20,
        (
            "まあ偽造証も大量に出回ってるから\x01",
            "ほとんど意味ねえんだがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_2178")


    #C0104
    ChrTalk(
        0x20,
        (
            "安心しな、魔導杖は\x01",
            "嬢ちゃんにしか売らねえからよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x20,
        (
            "だが嬢ちゃんに渡すために\x01",
            "ウチに卸すってのも……\x01",
            "考えてみりゃあ妙な話だな？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x103,
        (
            "#0211F（主任、どこにいるんだろう……\x01",
            "  ぶつぶつ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223A")

    Jump("loc_AAE")

    label("loc_223F")

    TalkEnd(0x20)
    Return()

    # Function_5_8ED end

    def Function_6_2243(): pass

    label("Function_6_2243")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2744")
    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)
    TurnDirection(0x21, 0x0, 0)
    TurnDirection(0x22, 0x0, 0)

    #C0107
    ChrTalk(
        0x101,
        (
            "#0000Fドノバン警部にレイモンドさん……\x02\x03",

            "お疲れ様です、聞き込みですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x21,
        (
            "ああ、倉庫街であった\x01",
            "発砲事件の裏を取りにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x22,
        (
            "まあ十中八九、\x01",
            "ルバーチェ関係者だろうけどね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x22,
        (
            "あの連中、ここのトコ\x01",
            "トラブルばっかり起こしてるしさ。\x01",
            "ホラ、例のトラック事故とかね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#0105Fトラック事故……？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        "#0305F何スかそりゃあ……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#0201F気になりますね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    #C0114
    ChrTalk(
        0x21,
        (
            "レイモンド、お前は\x01",
            "相変わらず口が軽いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x22,
        "うげ、やっぱマズかったかな～。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x0, 500)
    Sleep(300)

    #C0116
    ChrTalk(
        0x21,
        "いや、二課に流れてきた噂なんだが……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x21,
        (
            "先週末に共和国方面であったトラック事故、\x01",
            "ありゃあどうも\x01",
            "ルバーチェの運搬車だったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x21,
        (
            "何者かに襲われて\x01",
            "最後は炎上したって話だったぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x101,
        "#0005Fな……そうだったんですか！？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x21,
        (
            "ああ……上層部は伏せてるが\x01",
            "近頃この手の話が増えててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x21,
        (
            "市民を巻き込む形じゃねえみたいだが……\x01",
            "たまに遊撃士も出張ってるらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x103,
        "#0200Fきな臭くなってきましたね。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0003Fルバーチェ側が襲われたって事は\x01",
            "襲撃者は黒月か……？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0303Fだろうな。\x01",
            "……他にそんな真似をするやつが\x01",
            "いるとは思えねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#0106F私達の出る幕じゃないとは思うけど\x01",
            "気に留めておいた方がよさそうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x21, 0xFF)
    OP_4C(0x22, 0xFF)
    OP_93(0x21, 0x10E, 0x0)
    OP_93(0x22, 0x5A, 0x0)
    SetScenarioFlags(0x94, 7)
    Jump("loc_2820")

    label("loc_2744")

    TurnDirection(0x21, 0x0, 0)

    #C0126
    ChrTalk(
        0xFE,
        (
            "一連のトラック事故は\x01",
            "一課が捜査中みてえだ。\x01",
            "俺らも詳しい事は聞いてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "ま、近頃事件が増えてるからな。\x01",
            "こっちもそれ所じゃねえんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "お前らも市内の見回りすんなら\x01",
            "街の様子に気をつけとけよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x10E, 0x0)

    label("loc_2820")

    TalkEnd(0xFE)
    Return()

    # Function_6_2243 end

    def Function_7_2824(): pass

    label("Function_7_2824")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2839")
    Call(0, 6)
    Jump("loc_28FF")

    label("loc_2839")

    OP_4B(0x21, 0xFF)

    #C0129
    ChrTalk(
        0xFE,
        (
            "警部～、そろそろ帰りましょうよ～。\x01",
            "オレ昨日も徹夜だったんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x21,
        (
            "何ぐだぐだ言ってやがる。\x01",
            "オラ次行くぞ、次！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        "うえ～ん、警部の鬼～！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#0000F（な、何だか忙しそうだな。）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x21, 0xFF)

    label("loc_28FF")

    TalkEnd(0xFE)
    Return()

    # Function_7_2824 end

    def Function_8_2903(): pass

    label("Function_8_2903")

    Call(0, 9)
    Return()

    # Function_8_2903 end

    def Function_9_2907(): pass

    label("Function_9_2907")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2914")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B0")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2972")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2972")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2992")
    OP_AF(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33AB")

    label("loc_2992")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29A6")
    Jump("loc_33AB")

    label("loc_29A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33AB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2A02")

    #C0133
    ChrTalk(
        0x8,
        (
            "やはりセルテオには\x01",
            "まだ早かったでしょうかね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_2A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A9E")

    #C0134
    ChrTalk(
        0x8,
        (
            "シェフが勝手に\x01",
            "ゲテモノ料理を配ってくる\x01",
            "という苦情が……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "……ゴホン、申し訳ありません。\x01",
            "当店のシェフがとんだご迷惑を。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AD5")

    label("loc_2A9E")


    #C0136
    ChrTalk(
        0x8,
        (
            "セルテオ、もう少し\x01",
            "真面目にやってくれないかね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD5")

    Jump("loc_33AB")

    label("loc_2ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2B6B")

    #C0137
    ChrTalk(
        0x8,
        (
            "……セルテオが\x01",
            "頻繁に厨房から出てきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "それにお客様に\x01",
            "勝手に料理を差し入れている\x01",
            "ようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        "あれは一体……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C45")

    #C0140
    ChrTalk(
        0x8,
        (
            "自分と当店のシェフ、ブラウンは\x01",
            "４０年来の親友でして。\x01",
            "共に修行を積んだ仲でもあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        "しかし問題は次の世代ですね。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "セルテオが真面目に修行し、\x01",
            "腕を上げてくれると良いのですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C7F")

    label("loc_2C45")


    #C0143
    ChrTalk(
        0x8,
        (
            "セルテオが\x01",
            "やる気になる方法は\x01",
            "無いものでしょうかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C7F")

    Jump("loc_33AB")

    label("loc_2C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2CFC")

    #C0144
    ChrTalk(
        0x8,
        (
            "今年の記念祭は\x01",
            "当店も最高益を挙げました。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "しかし祭りは祭り……\x01",
            "終わってしまうと寂しい物ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_2CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF1")

    #C0146
    ChrTalk(
        0x8,
        (
            "ノンノの一言で\x01",
            "セルテオが張り切りだしまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        "何でしたかな、あの一言は。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        (
            "『記念祭には女の子が\x01",
            "たくさん来るんでしょうね』\x01",
            "……でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "よく効くのはよいのですが、\x01",
            "今度は効き過ぎないかが心配です。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E5A")

    label("loc_2DF1")


    #C0150
    ChrTalk(
        0x8,
        (
            "ノンノの一言で\x01",
            "セルテオが張り切りだして\x01",
            "しまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "普段が不真面目なだけに\x01",
            "少々不安ですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E5A")

    Jump("loc_33AB")

    label("loc_2E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2EE8")

    #C0152
    ChrTalk(
        0x8,
        (
            "記念祭を見越して\x01",
            "早めにクロスベル入りする方も\x01",
            "いらっしゃるようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "ついでに市内観光を\x01",
            "楽しまれるのでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_2EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2F77")

    #C0154
    ChrTalk(
        0x8,
        (
            "店内、少々\x01",
            "騒がしくしておりまして\x01",
            "申し訳ございません。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "セルテオも……もう少し真面目に\x01",
            "働いてくれるといいんですがね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_2F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_302E")

    #C0156
    ChrTalk(
        0x8,
        (
            "当店の２階はご予約席として\x01",
            "中々人気なのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x8,
        (
            "中でも大切なお客様が\x01",
            "アリオス・マクレインさんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "月に一度、娘さんと一緒に\x01",
            "お食事を楽しまれるのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_302E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_30C8")

    #C0159
    ChrTalk(
        0x8,
        (
            "記念祭が近いと\x01",
            "予約がいくつも入りましてね。\x01",
            "調整が大変なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "仕入れの段取りに\x01",
            "飾りつけのデザイン……\x01",
            "何かと忙しくなりますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_30C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3161")

    #C0161
    ChrTalk(
        0x8,
        (
            "セルテオは忙しいと言いつつ\x01",
            "頻繁に厨房から出てくるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "妙齢の女性には\x01",
            "自分で料理を運びたいとか……\x01",
            "まったく困ったものです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_3161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_31F0")

    #C0163
    ChrTalk(
        0x8,
        (
            "仕入れに少々\x01",
            "トラブルがありましてね。\x01",
            "シェフと調整をしていたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x8,
        (
            "なに、ご心配なく。\x01",
            "当店の味は保証いたしますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_31F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_326C")

    #C0165
    ChrTalk(
        0x8,
        (
            "今日は新婚の方が\x01",
            "いらっしゃってましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x8,
        (
            "フフ、後で美味いワインでも\x01",
            "差し入れてあげましょうかねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_326C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_32FB")

    #C0167
    ChrTalk(
        0x8,
        (
            "２階のお客さんは\x01",
            "商談席のご予約のようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "フフ、２階はご予約が利くんですよ。\x01",
            "よろしかったら\x01",
            "ご覧になってください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_32FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_33AB")

    #C0169
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "《ヴァンセット》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        (
            "お食事でしょうか？\x01",
            "それともテイクアウト？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "当店はどちらでも可能ですからね、\x01",
            "注文の際に仰ってくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33AB")

    Jump("loc_2914")

    label("loc_33B0")

    TalkEnd(0x8)
    Return()

    # Function_9_2907 end

    def Function_10_33B4(): pass

    label("Function_10_33B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3418")

    #C0172
    ChrTalk(
        0xFE,
        "おっと、ディナータイム突入か。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "今夜も忙しくなりそうだなぁ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3482")

    label("loc_3418")


    #C0174
    ChrTalk(
        0xFE,
        (
            "セルテオには新作メニューに\x01",
            "集中させてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "１人で全注文を受けるのは\x01",
            "さすがに骨が折れるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3482")

    Jump("loc_4118")

    label("loc_3487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_357D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352D")

    #C0176
    ChrTalk(
        0xFE,
        (
            "……客から、頼んでもないのに\x01",
            "不気味なメニューが出てくるって\x01",
            "苦情が来てるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "困ったな、セルテオのやつの\x01",
            "試作品だと思うんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3578")

    label("loc_352D")


    #C0178
    ChrTalk(
        0xFE,
        (
            "なるべく好きに\x01",
            "やらせたいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "若手の教育ってのも難しいな。\x02",
    )

    CloseMessageWindow()

    label("loc_3578")

    Jump("loc_4118")

    label("loc_357D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_367A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3631")

    #C0180
    ChrTalk(
        0xFE,
        (
            "今朝は港湾区の方で\x01",
            "事件があったんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "ま、中央広場からは離れてるから\x01",
            "客入りに影響はないか……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "あまり事件が増えるのも\x01",
            "困ったもんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3675")

    label("loc_3631")


    #C0183
    ChrTalk(
        0xFE,
        "事件が増えると客足も遠のく。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        "あまり多いと困ったもんだな。\x02",
    )

    CloseMessageWindow()

    label("loc_3675")

    Jump("loc_4118")

    label("loc_367A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3793")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_372E")

    #C0185
    ChrTalk(
        0xFE,
        (
            "セルテオの奴には\x01",
            "課題を渡してあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "あいつはウチに来てからも\x01",
            "女の子ばかり追っかけてるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "少しは料理人の\x01",
            "修行もしてもらわないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_378E")

    label("loc_372E")


    #C0188
    ChrTalk(
        0xFE,
        (
            "新メニューの話は\x01",
            "セルテオに振ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "若手が育たなきゃ\x01",
            "安心して引退できないからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_378E")

    Jump("loc_4118")

    label("loc_3793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_38D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3854")

    #C0190
    ChrTalk(
        0xFE,
        (
            "記念祭の最終日は\x01",
            "我らが店長にも\x01",
            "厨房を手伝ってもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "ホイストフのやつ、\x01",
            "相変わらずいい腕してるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "……普段からその腕を\x01",
            "振るえばいいのになぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38CD")

    label("loc_3854")


    #C0193
    ChrTalk(
        0xFE,
        (
            "あいつは調理が早いし\x01",
            "味も申し分ない。\x01",
            "俺以上の腕の持ち主なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "もう並んで仕事をしては\x01",
            "くれないのかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38CD")

    Jump("loc_4118")

    label("loc_38D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39AD")

    #C0195
    ChrTalk(
        0xFE,
        (
            "記念祭はウチも\x01",
            "軽い催しをやるらしいぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "さっきセルテオが思いついたんだ。\x01",
            "今プランを考えているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "ちなみに……吹き込んだのは\x01",
            "ノンノだって話だぞ。\x01",
            "あいつ、中々分かってるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A0B")

    label("loc_39AD")


    #C0198
    ChrTalk(
        0xFE,
        (
            "記念祭はウチも\x01",
            "軽い催しをやるらしいぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "今セルテオの奴が\x01",
            "プランを考えているらしい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0B")

    Jump("loc_4118")

    label("loc_3A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AAB")

    #C0200
    ChrTalk(
        0xFE,
        (
            "ホイストフと\x01",
            "記念祭のスケジュールを\x01",
            "組み立ててるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "特に予約席は\x01",
            "献立のオーダーも入る。\x01",
            "色々予定を組まなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B17")

    label("loc_3AAB")


    #C0202
    ChrTalk(
        0xFE,
        (
            "ちなみに、予約席の献立は\x01",
            "ホイストフが考えてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "あいつはシェフとしても\x01",
            "まだまだ現役だからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B17")

    Jump("loc_4118")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3B71")

    #C0204
    ChrTalk(
        0xFE,
        "ノンノは姉さん女房だな。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "ありゃあ将来の\x01",
            "旦那さんが心配だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4118")

    label("loc_3B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3BDA")

    #C0206
    ChrTalk(
        0xFE,
        "働かざるもの食うべからず。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "セルテオにはもうちょい\x01",
            "真面目に働いて欲しいもんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4118")

    label("loc_3BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3C2C")

    #C0208
    ChrTalk(
        0xFE,
        "来月はいよいよ創立記念祭かぁ……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        "また忙しくなりそうだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4118")

    label("loc_3C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D27")

    #C0210
    ChrTalk(
        0xFE,
        (
            "ホイストフのやつは昔から\x01",
            "大衆向けのレストランを\x01",
            "やりたかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "にぎやかな店で\x01",
            "料理だけでなく雰囲気も\x01",
            "味わって欲しいんだと。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "一流シェフだったくせに\x01",
            "変わったことを考えるよな。\x01",
            "はは、乗っちまう俺も俺だけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D68")

    label("loc_3D27")


    #C0213
    ChrTalk(
        0xFE,
        (
            "まったく変わったことを考えるよな。\x01",
            "乗っちまう俺も俺だけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D68")

    Jump("loc_4118")

    label("loc_3D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3E7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E24")

    #C0214
    ChrTalk(
        0xFE,
        (
            "ちょこっと鉄道便が\x01",
            "遅れてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "ま、任せろ。\x01",
            "ホイストフが代わりのメニューを\x01",
            "即席で考えてくれたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "味はこっちで\x01",
            "軽く調整しておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E79")

    label("loc_3E24")


    #C0217
    ChrTalk(
        0xFE,
        (
            "ホイストフの奴は\x01",
            "即席でメニューを作っちまうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "頭の回転が速いんだよな。\x02",
    )

    CloseMessageWindow()

    label("loc_3E79")

    Jump("loc_4118")

    label("loc_3E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F15")

    #C0219
    ChrTalk(
        0xFE,
        "ほい２名様お待ち……\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "おっと注文なら\x01",
            "店の方でお願いするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "俺に直接言ってくれても\x01",
            "作っちゃうけどな、ははは。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F73")

    label("loc_3F15")


    #C0222
    ChrTalk(
        0xFE,
        (
            "試しに俺の耳元で\x01",
            "適当な料理を言ってみな。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "さくっと作っちゃうかも\x01",
            "しれんぞ、ははは。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F73")

    Jump("loc_4118")

    label("loc_3F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_402C")

    #C0224
    ChrTalk(
        0xFE,
        (
            "料理は根気、誠意、\x01",
            "そして遊び心だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "どんなに忙しくても\x01",
            "心のゆとりを無くしちゃダメなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "……セルテオにも\x01",
            "そろそろ料理人の心って物を\x01",
            "教えないとなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4118")

    label("loc_402C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D3")

    #C0227
    ChrTalk(
        0xFE,
        "今日の仕込みの出来はっと……\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "うーん、中々いい感じだ。\x01",
            "ここ３０年でもピカイチだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "よし、この味で\x01",
            "じゃんじゃん上げていこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4118")

    label("loc_40D3")


    #C0230
    ChrTalk(
        0xFE,
        (
            "ランチタイムに突入する前に\x01",
            "下ごしらえを済ませておかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4118")

    TalkEnd(0xFE)
    Return()

    # Function_10_33B4 end

    def Function_11_411C(): pass

    label("Function_11_411C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_413D")
    Call(0, 38)
    Return()

    label("loc_413D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43C5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4167")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C0")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "料理を渡す\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 12)
    Jump("loc_43BB")

    label("loc_41C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43BB")
    Call(0, 40)
    Call(0, 41)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_425D")

    #C0231
    ChrTalk(
        0xFE,
        (
            "……奇想天外な料理は……\x01",
            "持ってないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "１０種類以上集まったら\x01",
            "また来てくれ。\x01",
            "お礼は弾むからさ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43AC")

    label("loc_425D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42EA")

    #C0233
    ChrTalk(
        0xFE,
        (
            "それじゃあ数が足りねえよ。\x01",
            "最低１０種類は欲しい所だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "１０種類以上集まったら\x01",
            "また来てくれ。\x01",
            "お礼は弾むからさ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43AC")

    label("loc_42EA")


    #C0235
    ChrTalk(
        0xFE,
        "これで報告してくれるかい？\x02",
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【報告する】\x01",        # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434D")
    Call(0, 39)
    Return()

    label("loc_434D")


    #C0236
    ChrTalk(
        0xFE,
        (
            "そうか……\x01",
            "なるべく沢山あった方が\x01",
            "俺も嬉しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "また料理を集めて\x01",
            "ぜひ持って来てくれ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43AC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43BB")

    label("loc_43BB")

    Jump("loc_4167")

    label("loc_43C0")

    Jump("loc_43C8")

    label("loc_43C5")

    Call(0, 12)

    label("loc_43C8")

    TalkEnd(0xFE)
    Return()

    # Function_11_411C end

    def Function_12_43CC(): pass

    label("Function_12_43CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_44CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446F")

    #C0238
    ChrTalk(
        0xA,
        (
            "ようやく新メニューが\x01",
            "形になってきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xA,
        "今度のはマジ自信作だ！\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xA,
        (
            "よし、今日も可愛い子を探して\x01",
            "試食してもらうとすっかな～♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44C8")

    label("loc_446F")


    #C0241
    ChrTalk(
        0xA,
        (
            "ゲテモノ臭いって言われたから\x01",
            "見た目を改良したぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xA,
        "やっぱ客の意見は大事だよな。\x02",
    )

    CloseMessageWindow()

    label("loc_44C8")

    Jump("loc_50AE")

    label("loc_44CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_45BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4581")

    #C0243
    ChrTalk(
        0xA,
        (
            "この前から試作品を\x01",
            "客に振舞って回ってるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xA,
        "みんな手を付けてくれねえんだよ。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "ちっ、なんでだ。\x01",
            "やっぱ見た目が\x01",
            "ゲテモノ臭いのかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45BA")

    label("loc_4581")


    #C0246
    ChrTalk(
        0xA,
        (
            "新メニューって、あんま\x01",
            "奇抜じゃねえ方がいいのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45BA")

    Jump("loc_50AE")

    label("loc_45BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_46D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4646")

    #C0247
    ChrTalk(
        0xA,
        (
            "真ん中の席の子たち、\x01",
            "可愛いと思わないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "よし、俺の作った試作品を\x01",
            "サービスで届けてやるぜっ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46CB")

    label("loc_4646")


    #C0249
    ChrTalk(
        0xA,
        (
            "『君をイメージした\x01",
            "  オリジナルメニューさっ！』……\x01",
            "これでどんな子だってイチコロだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "試作品の感想も聞けて\x01",
            "一石二鳥だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46CB")

    Jump("loc_50AE")

    label("loc_46D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_47CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_478B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4705")
    Jump("loc_470C")

    label("loc_4705")

    OP_93(0xA, 0x10E, 0x0)

    label("loc_470C")


    #C0251
    ChrTalk(
        0xA,
        (
            "うむむ……肉料理や\x01",
            "魚料理ってカテゴリじゃ\x01",
            "従来の物と変わらねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "やっぱここは\x01",
            "珍しい素材をベースにして……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47C8")

    label("loc_478B")


    #C0253
    ChrTalk(
        0xA,
        (
            "新作メニューを考えてる所なんだ。\x01",
            "邪魔しないでくれよな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C8")

    Jump("loc_50AE")

    label("loc_47CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_486B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4839")

    #C0254
    ChrTalk(
        0xA,
        "記念祭も終わって余裕ができたぜ。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "今日は女の子ウォッチに\x01",
            "励むとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4866")

    label("loc_4839")


    #C0256
    ChrTalk(
        0xA,
        (
            "にひひ……午後の\x01",
            "お客さんが楽しみだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4866")

    Jump("loc_50AE")

    label("loc_486B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_48D4")

    #C0257
    ChrTalk(
        0xA,
        (
            "記念祭には、ピチピチのコが\x01",
            "たくさん食事にやってくる……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xA,
        "張り切っていくぞーっ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_50AE")

    label("loc_48D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_498B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4942")

    #C0259
    ChrTalk(
        0xA,
        (
            "記念祭が近いと\x01",
            "献立の調整だの何だのあってさー。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xA,
        "やる気出ないんだよなー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4986")

    label("loc_4942")


    #C0261
    ChrTalk(
        0xA,
        (
            "あー、表の広場に行って\x01",
            "カワイイ子を拝みてえなぁ。\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4986")

    Jump("loc_50AE")

    label("loc_498B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4A4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49A6")
    Call(0, 14)
    Jump("loc_4A46")

    label("loc_49A6")

    OP_93(0xA, 0xB4, 0x0)
    OP_4B(0xB, 0xFF)

    #C0262
    ChrTalk(
        0xA,
        (
            "オ、オレはそこの女の子に\x01",
            "料理を持ってきただけで……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "もう……またお客さんを\x01",
            "口説こうとしてますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xB,
        (
            "ダメですよ。\x01",
            "はい、仕事に戻る！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_4A46")

    Jump("loc_50AE")

    label("loc_4A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4B26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF0")

    #C0265
    ChrTalk(
        0xA,
        "スパ定食あがり～♪\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xA,
        (
            "こいつは中央テーブルの\x01",
            "カワイコちゃんのオーダーなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xA,
        (
            "にひひ、運ぶついでに\x01",
            "有意義な話ができそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B21")

    label("loc_4AF0")


    #C0268
    ChrTalk(
        0xA,
        (
            "女の子のオーダーには\x01",
            "自然と力が入るよな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B21")

    Jump("loc_50AE")

    label("loc_4B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4C44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE7")

    #C0269
    ChrTalk(
        0xA,
        (
            "ふーっ、ようやく\x01",
            "ランチタイムが終わったぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xA,
        (
            "記念祭が近いせいか\x01",
            "最近メチャ忙しいんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "ブラウンさんは\x01",
            "余裕たっぷりなんだけどなぁ……\x01",
            "なんでだろ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C3F")

    label("loc_4BE7")


    #C0272
    ChrTalk(
        0xA,
        (
            "オレもブラウンさんみたいに\x01",
            "仕事が速けりゃ、\x01",
            "もっと女の子とお喋りできんのになぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C3F")

    Jump("loc_50AE")

    label("loc_4C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D1A")

    #C0273
    ChrTalk(
        0xA,
        (
            "いつも店の奥で\x01",
            "コーヒー飲んでる子がいるだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "よく見たら結構可愛いからさ、\x01",
            "さっき暇をみて\x01",
            "話しかけてみたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xA,
        "まるで反応が無かったんだ。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        "くそっ……落ち込むぜ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D6A")

    label("loc_4D1A")


    #C0277
    ChrTalk(
        0xA,
        (
            "俺ってそんなに\x01",
            "イケてねえのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xA,
        (
            "さすがに\x01",
            "無視されると落ち込むぜ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D6A")

    Jump("loc_50AE")

    label("loc_4D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4E49")

    #C0279
    ChrTalk(
        0xA,
        "クロスベル人には美人が多いんだぜ。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xA,
        (
            "あの大スター、イリア・プラティエとか\x01",
            "財界きっての令嬢、\x01",
            "マリアベル・クロイスとかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xA,
        (
            "街行く子もみんなオシャレだし\x01",
            "やっぱランク高めだよな。\x01",
            "にひひひひ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50AE")

    label("loc_4E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4EC7")

    #C0282
    ChrTalk(
        0xA,
        (
            "ちっ、今日は\x01",
            "女の子の来店が少ないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xA,
        (
            "いやいや、勝負はこれからだ。\x01",
            "ランチタイムになるまで判らないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50AE")

    label("loc_4EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4F55")

    #C0284
    ChrTalk(
        0xA,
        (
            "くそっ、ランチタイムは地獄だぜ。\x01",
            "忙しいったらありゃしねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xA,
        (
            "はあ……客が全部キュートな\x01",
            "女の子だったらいいのになぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50AE")

    label("loc_4F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_50AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5021")

    #C0286
    ChrTalk(
        0xA,
        (
            "この店には毎日ものすごい数の\x01",
            "お客さんが来るんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xA,
        (
            "それも、若くて\x01",
            "ピチピチのお姉さんが多いと来た。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xA,
        (
            "なのに俺って一日中厨房の中……\x01",
            "忙しくって店内を窺う暇もねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_50AE")

    label("loc_5021")


    #C0289
    ChrTalk(
        0xA,
        (
            "俺がクロスベルに来たのは\x01",
            "忙しさに追われるためじゃねえ。\x01",
            "沢山の女の子と知り合うためなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xA,
        (
            "こんな所じゃ終わらねえぞ、\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50AE")

    Return()

    # Function_12_43CC end

    def Function_13_50AF(): pass

    label("Function_13_50AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_51B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5146")
    TurnDirection(0xFE, 0xE, 0)

    #C0291
    ChrTalk(
        0xFE,
        (
            "大変申し訳ありません。\x01",
            "当店の仕入れミスでして……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "お代わりが紅茶でよろしければ\x01",
            "すぐにお持ちしますが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51B2")

    label("loc_5146")


    #C0293
    ChrTalk(
        0xFE,
        (
            "（セルテオさんが\x01",
            "  コーヒー豆を大量に\x01",
            "  使っちゃったらしいんです。）\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        "（ふう、困ったものだわ……）\x02",
    )

    CloseMessageWindow()

    label("loc_51B2")

    Jump("loc_5A6C")

    label("loc_51B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5290")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_525A")

    #C0295
    ChrTalk(
        0xFE,
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "今日はお客さんが\x01",
            "ちょっと少ないみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "大勢すぎるのも大変ですけど\x01",
            "少ないのも困ったものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_528B")

    label("loc_525A")


    #C0298
    ChrTalk(
        0xFE,
        (
            "記念祭の時みたいに\x01",
            "客寄せでもしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_528B")

    Jump("loc_5A6C")

    label("loc_5290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_52F3")

    #C0299
    ChrTalk(
        0xFE,
        "今日は警察の人が多いですね……\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "朝からちらほら\x01",
            "パトロールしてるみたいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6C")

    label("loc_52F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_53FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53BE")

    #C0301
    ChrTalk(
        0xFE,
        (
            "セルテオさんが\x01",
            "何か悩んでるみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "私にまでお料理のことを\x01",
            "聞きに来たんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "『お前、ゲテモノ料理\x01",
            "知らないか？』ですって。\x01",
            "何を作るつもりなのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53FA")

    label("loc_53BE")


    #C0304
    ChrTalk(
        0xFE,
        (
            "セルテオさんって\x01",
            "時々ヘンな事を\x01",
            "口走ってるんですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53FA")

    Jump("loc_5A6C")

    label("loc_53FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_54B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5477")

    #C0305
    ChrTalk(
        0xFE,
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "あら、可愛いお嬢さんですね。\x01",
            "お子様ランチでも注文なさいます？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_54B2")

    label("loc_5477")


    #C0307
    ChrTalk(
        0xFE,
        (
            "今の時間は空席も多いんです。\x01",
            "３名様なら大歓迎ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B2")

    Jump("loc_5A6C")

    label("loc_54B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_54C8")
    Call(0, 34)
    Jump("loc_5A6C")

    label("loc_54C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_559E")

    #C0308
    ChrTalk(
        0xFE,
        (
            "店長が記念祭の準備を\x01",
            "進めてるみたいです。\x01",
            "私たちもそろそろ手伝わなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "毎年ドリンクサービスしたり\x01",
            "記念品をプレゼントしたり……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "あとお子様ランチの旗が\x01",
            "祝祭旗になったりするんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6C")

    label("loc_559E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_562A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B9")
    Call(0, 14)
    Jump("loc_5625")

    label("loc_55B9")


    #C0311
    ChrTalk(
        0xFE,
        (
            "セルテオさんは何かと\x01",
            "厨房から出てくるのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "忙しい時期なんだから\x01",
            "しっかり働いてもらわないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5625")

    Jump("loc_5A6C")

    label("loc_562A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5685")

    #C0313
    ChrTalk(
        0xFE,
        (
            "今日のお客さん、\x01",
            "何だかいい感じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        "応援したくなっちゃいます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A6C")

    label("loc_5685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_56CB")

    #C0315
    ChrTalk(
        0xFE,
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        "ご注文は何にしますか～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A6C")

    label("loc_56CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5754")

    #C0317
    ChrTalk(
        0xFE,
        (
            "２階席は予約が効くんですよ。\x01",
            "予約すればメニューの指定も\x01",
            "ばっちりＯＫです。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "家族連れで来る人も\x01",
            "結構多いんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6C")

    label("loc_5754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_581C")

    #C0319
    ChrTalk(
        0xFE,
        (
            "店長とブラウンさんって\x01",
            "親友同士なんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "経営方針も、いつも２人で\x01",
            "相談して決めているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "……大人になっても親友なんて\x01",
            "ちょっと憧れちゃいますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5884")

    label("loc_581C")


    #C0322
    ChrTalk(
        0xFE,
        (
            "店長とブラウンさんって\x01",
            "親友同士なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "経営方針も、いつも相談して\x01",
            "決めているみたいですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5884")

    Jump("loc_5A6C")

    label("loc_5889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5969")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5918")

    #C0324
    ChrTalk(
        0xFE,
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "ただ今モーニングサービス実施中です。\x01",
            "朝食がまだなら\x01",
            "さくっと注文しちゃって下さいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5964")

    label("loc_5918")


    #C0326
    ChrTalk(
        0xFE,
        (
            "モーニングサービス実施中です。\x01",
            "朝食がまだなら\x01",
            "注文しちゃって下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5964")

    Jump("loc_5A6C")

    label("loc_5969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_59D2")

    #C0327
    ChrTalk(
        0xFE,
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "ふう、ランチタイムは忙しいですね。\x01",
            "もう一息、頑張らないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6C")

    label("loc_59D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5A6C")

    #C0329
    ChrTalk(
        0xFE,
        (
            "お待ちどうさま～！\x01",
            "Ａランチ２つでーす！\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "あ、お客さん座ってください！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "うちは結構慌しいので\x01",
            "お客さんに立たれると\x01",
            "困ってしまいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6C")

    TalkEnd(0xFE)
    Return()

    # Function_13_50AF end

    def Function_14_5A70(): pass

    label("Function_14_5A70")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    #C0332
    ChrTalk(
        0xB,
        (
            "セルテオさん～？\x01",
            "頭ぐりぐりしてあげましょうか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xA,
        (
            "オ、オレは別に\x01",
            "悪いことなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        (
            "お仕事サボってるでしょう？\x01",
            "はい、厨房に戻る！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_14_5A70 end

    def Function_15_5B25(): pass

    label("Function_15_5B25")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5BB9")
    Jump("loc_5C03")

    label("loc_5BB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BD9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C03")

    label("loc_5BD9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BF9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C03")

    label("loc_5BF9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C03")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D77")

    #C0335
    ChrTalk(
        0xFE,
        "#2600Fやあ、君たち。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#0105Fアーネストさん。\x01",
            "お食事中ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "#2606Fいや、ただの休憩でね。\x02\x03",

            "#2600F夕方から市長の付き添いで\x01",
            "公聴会に出席するんだ。\x02\x03",

            "その時に提出する資料を\x01",
            "確認していたところだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x102,
        (
            "#0102Fそうですか……\x01",
            "本当にお疲れさまです。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#0000F（どうやら俺たち以上に\x01",
            "  忙しいみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5E4C")

    label("loc_5D77")

    SetChrSubChip(0xFE, 0x0)

    #C0340
    ChrTalk(
        0xFE,
        (
            "#2601Fうーん、こちらの資料だと\x01",
            "帝国派からの要求までは\x01",
            "かわし切れないな……\x02\x03",

            "#2603Fかといってこちらを提示すれば\x01",
            "共和国派の方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#0000F（邪魔しちゃ悪いな……）\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x102,
        "#0104F（ええ……行きましょう。）\x02",
    )

    CloseMessageWindow()

    label("loc_5E4C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_5B25 end

    def Function_16_5E54(): pass

    label("Function_16_5E54")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5EE8")
    Jump("loc_5F32")

    label("loc_5EE8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F08")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F32")

    label("loc_5F08")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F28")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F32")

    label("loc_5F28")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F32")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5FE0")

    #C0343
    ChrTalk(
        0xFE,
        (
            "……コーヒーを\x01",
            "切らしちゃったって言うのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "信じられないわ。\x01",
            "レストランでコーヒーが\x01",
            "出ないなんてありえないわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E3D")

    label("loc_5FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6034")

    #C0345
    ChrTalk(
        0xFE,
        "今朝はなんだか街が静かね。\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        "警官の数も少なかった気がするわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E3D")

    label("loc_6034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_60F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60CB")

    #C0347
    ChrTalk(
        0xFE,
        (
            "ずずーっ……\x01",
            "……………うっ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        "クロスベルタイムズが無い……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "出掛けに持ってくるの、\x01",
            "忘れちゃったかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_60F4")

    label("loc_60CB")


    #C0350
    ChrTalk(
        0xFE,
        (
            "議会がどうなったのか\x01",
            "気になるわ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F4")

    Jump("loc_6E3D")

    label("loc_60F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_621D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61DB")

    #C0351
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズ、\x01",
            "また予算議会の話題だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "大の大人が顔を赤くしちゃって、\x01",
            "みごとなヤジの飛ばし合いだったらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "いつものことだけど\x01",
            "滑稽で笑っちゃうわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6218")

    label("loc_61DB")


    #C0355
    ChrTalk(
        0xFE,
        (
            "議員達が本気でののしり合いなんて\x01",
            "滑稽で笑っちゃうわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6218")

    Jump("loc_6E3D")

    label("loc_621D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_633E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62EB")

    #C0356
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "ようやく街から記念祭気分が\x01",
            "抜けたのはいいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "アリオス・マクレインは\x01",
            "また出張に行っているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "あの人、ほとんど\x01",
            "自治州にいないじゃない。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6339")

    label("loc_62EB")


    #C0360
    ChrTalk(
        0xFE,
        (
            "アリオス・マクレイン、\x01",
            "クロスベル人のくせに\x01",
            "ほとんど自治州に居ないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6339")

    Jump("loc_6E3D")

    label("loc_633E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_645A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63DA")

    #C0361
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "警備隊の司令って\x01",
            "しょっちゅう接待を\x01",
            "受けてるらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "ろくに仕事もしないで\x01",
            "遊び歩いてるって噂よ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6455")

    label("loc_63DA")


    #C0364
    ChrTalk(
        0xFE,
        (
            "警備隊の司令って\x01",
            "大の接待好きらしいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "そのうちクロスベルタイムズに\x01",
            "すっぱ抜かれて\x01",
            "失脚するんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6455")

    Jump("loc_6E3D")

    label("loc_645A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6581")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64FD")

    #C0366
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのクロイス総裁は\x01",
            "慈善事業に熱心な事で有名なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "ただでさえ忙しいでしょうに、\x01",
            "よくあれだけ働けるわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_657C")

    label("loc_64FD")


    #C0369
    ChrTalk(
        0xFE,
        (
            "ＩＢＣといえば\x01",
            "世界最大の銀行グループよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "ただでさえ忙しいでしょうに\x01",
            "慈善事業だなんて。\x01",
            "クロイス総裁もよくやるわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_657C")

    Jump("loc_6E3D")

    label("loc_6581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6614")

    #C0371
    ChrTalk(
        0xFE,
        (
            "ずずーっ……\x01",
            "…………………………？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "コーヒー、切れちゃったわ。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "カップ一杯で粘るのは\x01",
            "そろそろ限界かしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6634")

    label("loc_6614")


    #C0374
    ChrTalk(
        0xFE,
        "……そろそろ帰らなくちゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_6634")

    Jump("loc_6E3D")

    label("loc_6639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6749")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E6")

    #C0375
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの準主役には\x01",
            "新人の子が抜擢されたそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "名前は……なんだったかしら。\x01",
            "雑誌には大きく出ていたんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6744")

    label("loc_66E6")


    #C0378
    ChrTalk(
        0xFE,
        (
            "新人の子は\x01",
            "まだ舞台の経験がないそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "よくそんなド素人が\x01",
            "準主役なんて取れたわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6744")

    Jump("loc_6E3D")

    label("loc_6749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_685C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6816")

    #C0380
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "アルカンシェルのチケットは\x01",
            "ひどい奪い合いだったらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        "諦めの悪い庶民はこれだから……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "どうせ手に入らないなら\x01",
            "関わらない方がよほど利口だわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6857")

    label("loc_6816")


    #C0384
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "……別に私が\x01",
            "ひがんでるわけじゃないのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6857")

    Jump("loc_6E3D")

    label("loc_685C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_69B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6947")

    #C0386
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "マインツといえば\x01",
            "北の山あいに囲まれた鉱山町よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "ある程度導力化されているし\x01",
            "アルモリカ村ほど\x01",
            "イモ臭くはないでしょうけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "やっぱり片田舎よね。\x01",
            "観光に行くような場所じゃないわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_69B3")

    label("loc_6947")


    #C0390
    ChrTalk(
        0xFE,
        (
            "マインツといえば\x01",
            "北の山あいに囲まれた鉱山町よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "所詮は片田舎ね。\x01",
            "わざわざ出かける場所じゃないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69B3")

    Jump("loc_6E3D")

    label("loc_69B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A98")

    #C0392
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "最近はアルモリカ村まで取引に行く\x01",
            "商人もいるらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "まあ野菜の質はいいし\x01",
            "多少は商売になるんでしょうけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "わざわざあんなド田舎まで\x01",
            "出向くなんて、よくやるわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6B04")

    label("loc_6A98")


    #C0396
    ChrTalk(
        0xFE,
        (
            "儲け話なら他に\x01",
            "いくらでもあるでしょうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "わざわざアルモリカ村まで\x01",
            "足を運ぶなんて、よくやるわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B04")

    Jump("loc_6E3D")

    label("loc_6B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6C00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB9")

    #C0398
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "旧市街のごたごたには\x01",
            "ついに警察も介入したそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "でも結局逮捕者は\x01",
            "出なかったんですって。\x01",
            "相変わらず生ぬるいやり方よね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6BFB")

    label("loc_6BB9")


    #C0401
    ChrTalk(
        0xFE,
        (
            "警察も生ぬるいわね。\x01",
            "犯罪者はびしっと\x01",
            "取り締まればいいのに。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BFB")

    Jump("loc_6E3D")

    label("loc_6C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6D55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CBA")

    #C0402
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズって\x01",
            "よく遊撃士を取り上げるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "ウケがいいのは分かるけど、\x01",
            "もっと議会や政府を\x01",
            "バンバン批判すべきだと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6D50")

    label("loc_6CBA")


    #C0405
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズは、\x01",
            "もっと議会や政府を\x01",
            "バンバン批判すべきだと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "……ま、難しいのかしらね。\x01",
            "私的にはそっちの方が\x01",
            "面白いと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D50")

    Jump("loc_6E3D")

    label("loc_6D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE5")

    #C0407
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        "わたしはこの店の喧騒が好きなの。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "ここでコーヒーを飲みながら\x01",
            "読書をすると落ち着くのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6E3D")

    label("loc_6DE5")


    #C0410
    ChrTalk(
        0xFE,
        (
            "わたしはこの店の喧騒が好きなの。\x01",
            "コーヒーを飲みながら\x01",
            "読書をすると落ち着くのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E3D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_5E54 end

    def Function_17_6E45(): pass

    label("Function_17_6E45")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6ED9")
    Jump("loc_6F23")

    label("loc_6ED9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6EF9")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F23")

    label("loc_6EF9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F19")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F23")

    label("loc_6F19")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F23")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x11, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7043")

    #C0411
    ChrTalk(
        0x11,
        (
            "いやはや、素晴らしい設計です！\x01",
            "さすがはキンドールさんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xF,
        "満足していただけたようで光栄です。\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xF,
        (
            "して……もう一件の\x01",
            "依頼したい仕事というのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x11,
        (
            "ええ、実はエレボニアの帝都に\x01",
            "新しいホテルビル計画がありまして……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7127")

    label("loc_7043")


    #C0415
    ChrTalk(
        0x11,
        (
            "我々もぜひチャレンジしてみたいと\x01",
            "思っているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xF,
        (
            "なるほど、あなたのお考えは\x01",
            "良く分かりますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xF,
        (
            "人は常に新しいものを求める。\x01",
            "我々はそれに応えねばなりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x11,
        (
            "はは、同意していただけたようで\x01",
            "何よりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7127")

    SetChrSubChip(0xF, 0x0)
    TalkEnd(0xF)
    Return()

    # Function_17_6E45 end

    def Function_18_712F(): pass

    label("Function_18_712F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_719E")

    #C0419
    ChrTalk(
        0xFE,
        (
            "ふむ……ついでだし\x01",
            "今日は食事をしていこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "念には念を入れ、\x01",
            "味を確認しておかねば。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7290")

    label("loc_719E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7290")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_722C")

    #C0421
    ChrTalk(
        0xFE,
        (
            "今度の商談相手は\x01",
            "大事なお客様なんだ。\x01",
            "万が一にも失敗は許されない。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "予約席を取って\x01",
            "しっかりやらないとな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7290")

    label("loc_722C")


    #C0423
    ChrTalk(
        0xFE,
        (
            "ここのレストランは\x01",
            "美味い料理で有名なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "今回は予約席を取って\x01",
            "先方をもてなすとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7290")

    TalkEnd(0xFE)
    Return()

    # Function_18_712F end

    def Function_19_7294(): pass

    label("Function_19_7294")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7328")
    Jump("loc_7372")

    label("loc_7328")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7348")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7372")

    label("loc_7348")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7368")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7372")

    label("loc_7368")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7372")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7413")

    #C0425
    ChrTalk(
        0xFE,
        (
            "ふう、満足満足。\x01",
            "いやあ申し分ない料理だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "今度クロスベルに来るときは\x01",
            "友達も連れてこようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7489")

    label("loc_7413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7489")

    #C0427
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "へええ、こりゃ美味いや。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "この値段で\x01",
            "これだけ料理が楽しめるなんて\x01",
            "お得感があるよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7489")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_7294 end

    def Function_20_7491(): pass

    label("Function_20_7491")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7525")
    Jump("loc_756F")

    label("loc_7525")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7545")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_756F")

    label("loc_7545")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7565")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_756F")

    label("loc_7565")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_756F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_75FC")

    #C0429
    ChrTalk(
        0xFE,
        (
            "週に一度、家族で\x01",
            "食事をするのが習慣なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "時々母の顔を\x01",
            "見ないと心配だしね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_766D")

    label("loc_75FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_766D")

    #C0431
    ChrTalk(
        0xFE,
        (
            "やはり家族での\x01",
            "食事はこの店に限るね。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "手軽な値段で美味しい料理。\x01",
            "昔から何も変わっていないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_766D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_7491 end

    def Function_21_7675(): pass

    label("Function_21_7675")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7709")
    Jump("loc_7753")

    label("loc_7709")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7729")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7753")

    label("loc_7729")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7749")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7753")

    label("loc_7749")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7753")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7808")
    SetChrSubChip(0xFE, 0x0)

    #C0433
    ChrTalk(
        0xFE,
        (
            "でもお義母さん、\x01",
            "一人暮らしなんて\x01",
            "危なくありません？\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xFE,
        (
            "気をつけてくださいねえ。\x01",
            "何かあったら\x01",
            "すぐに駆けつけますから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7877")

    label("loc_7808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7877")

    #C0435
    ChrTalk(
        0xFE,
        (
            "お義母さん遅いわねぇ。\x01",
            "一緒に食事をする約束でしたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        (
            "もうお年だし\x01",
            "心配になってしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7877")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_7675 end

    def Function_22_787F(): pass

    label("Function_22_787F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7913")
    Jump("loc_795D")

    label("loc_7913")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7933")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_795D")

    label("loc_7933")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7953")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_795D")

    label("loc_7953")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_795D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0437
    ChrTalk(
        0xFE,
        (
            "すまんの、出かけるのが\x01",
            "遅れてしもうたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "どれ、それじゃ何か\x01",
            "注文させてもらうとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_787F end

    def Function_23_79F6(): pass

    label("Function_23_79F6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A8A")
    Jump("loc_7AD4")

    label("loc_7A8A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7AAA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AD4")

    label("loc_7AAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7ACA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AD4")

    label("loc_7ACA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AD4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B14")
    Call(0, 25)
    Jump("loc_7B67")

    label("loc_7B14")


    #C0439
    ChrTalk(
        0xFE,
        "とほほ、よく食う奴だ。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "まあいい、帰ったら\x01",
            "ビシバシ練習させてやるからな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B67")

    Jump("loc_7C4A")

    label("loc_7B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7BCF")
    SetChrSubChip(0xFE, 0x0)

    #C0441
    ChrTalk(
        0xFE,
        "なにっ、歓楽街はダメだろ！\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "何か問題でもあれば\x01",
            "出場停止になっちまうぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C4A")

    label("loc_7BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BEA")
    Call(0, 25)
    Jump("loc_7C4A")

    label("loc_7BEA")


    #C0443
    ChrTalk(
        0xFE,
        (
            "我々は帝国の名門乗馬クラブ\x01",
            "《ナインツ》の者だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "大会に向けて\x01",
            "英気を養っておるのだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C4A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_79F6 end

    def Function_24_7C52(): pass

    label("Function_24_7C52")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7CE6")
    Jump("loc_7D30")

    label("loc_7CE6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7D06")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D30")

    label("loc_7D06")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D26")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D30")

    label("loc_7D26")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D30")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D70")
    Call(0, 25)
    Jump("loc_7DBD")

    label("loc_7D70")

    SetChrSubChip(0xFE, 0x0)

    #C0445
    ChrTalk(
        0xFE,
        (
            "むしゃむしゃぱくぱく\x01",
            "ばりばりごっくん……\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        "うっす、次頂きやす！\x02",
    )

    CloseMessageWindow()

    label("loc_7DBD")

    Jump("loc_7E97")

    label("loc_7DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7E2F")
    SetChrSubChip(0xFE, 0x0)

    #C0447
    ChrTalk(
        0xFE,
        (
            "きれーな建物だの風景だのに\x01",
            "興味はないっすね。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        "もっとぱーっと遊べる所がいいっす。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E97")

    label("loc_7E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E4A")
    Call(0, 25)
    Jump("loc_7E97")

    label("loc_7E4A")

    SetChrSubChip(0xFE, 0x0)

    #C0449
    ChrTalk(
        0xFE,
        (
            "むしゃむしゃぱくぱく\x01",
            "ばりばりごっくん……\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        "うっす、次頂きやす！\x02",
    )

    CloseMessageWindow()

    label("loc_7E97")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_7C52 end

    def Function_25_7E9F(): pass

    label("Function_25_7E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7F23")
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    #C0451
    ChrTalk(
        0x16,
        "観光に来たのに、結局食い物か……\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x16,
        (
            "まあいいだろ。\x01",
            "大会に向けてもりもり食え！\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x17,
        "うっす、コーチ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7FA8")

    label("loc_7F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7F31")
    Jump("loc_7FA8")

    label("loc_7F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7FA8")
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    #C0454
    ChrTalk(
        0x16,
        "もりもり食えよ！\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x16,
        (
            "今日一日で観光スポットを\x01",
            "全部見て回るんだからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x17,
        "うっす、コーチ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_7FA8")

    Return()

    # Function_25_7E9F end

    def Function_26_7FA9(): pass

    label("Function_26_7FA9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_803D")
    Jump("loc_8087")

    label("loc_803D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_805D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8087")

    label("loc_805D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_807D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8087")

    label("loc_807D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8087")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8135")

    #C0457
    ChrTalk(
        0xFE,
        (
            "な、なんてこった。\x01",
            "僕らの新婚旅行だってのに\x01",
            "こんな事になるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xFE,
        (
            "どこかで名誉挽回\x01",
            "しなきゃまずいじゃないか！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8298")

    label("loc_8135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81DE")

    #C0459
    ChrTalk(
        0xFE,
        (
            "ええっと、次はカジノで\x01",
            "夜は高級ホテルに泊まりの予定……\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        (
            "あれれ？\x01",
            "予約したホテルはどこだっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        "この近くだったはずなんだけど……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8233")

    label("loc_81DE")


    #C0462
    ChrTalk(
        0xFE,
        (
            "ま、参ったなぁ……\x01",
            "ホテルの場所を忘れちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        "何とか思い出さないと……\x02",
    )

    CloseMessageWindow()

    label("loc_8233")

    Jump("loc_8298")

    label("loc_8238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8298")

    #C0464
    ChrTalk(
        0xFE,
        "妻と新婚旅行に来たんだよ。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "クロスベル市って華やかだねえ。\x01",
            "目移りしちゃうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8298")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_7FA9 end

    def Function_27_82A0(): pass

    label("Function_27_82A0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8334")
    Jump("loc_837E")

    label("loc_8334")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8354")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_837E")

    label("loc_8354")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8374")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_837E")

    label("loc_8374")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_837E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_84A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8450")

    #C0466
    ChrTalk(
        0xFE,
        "昨晩歓楽街で道に迷っていたら……\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "ステキな少年が現れて\x01",
            "案内してくれたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xFE,
        (
            "はあ、あの子の微笑みが\x01",
            "まぶたに焼き付いて離れないのよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_84A3")

    label("loc_8450")


    #C0469
    ChrTalk(
        0xFE,
        (
            "まだ少年なのに\x01",
            "とっても神秘的な子だったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        "はあ、また会えないかしら～。\x02",
    )

    CloseMessageWindow()

    label("loc_84A3")

    Jump("loc_8572")

    label("loc_84A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_850B")

    #C0471
    ChrTalk(
        0xFE,
        "……さっきから夫が挙動不審なの。\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xFE,
        (
            "初めての外国旅行だし\x01",
            "緊張してるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8572")

    label("loc_850B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8572")

    #C0473
    ChrTalk(
        0xFE,
        (
            "新婚旅行の日程は\x01",
            "夫が全部予約を取ってくれたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xFE,
        (
            "これでばっちり\x01",
            "観光して回れるわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8572")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_82A0 end

    def Function_28_857A(): pass

    label("Function_28_857A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1A)
    ClearChrFlags(0x1A, 0x10)
    TurnDirection(0x1A, 0x0, 0)
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_860E")
    Jump("loc_8658")

    label("loc_860E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_862E")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8658")

    label("loc_862E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_864E")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8658")

    label("loc_864E")

    OP_52(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8658")

    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1A, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_873E")
    SetChrSubChip(0x1A, 0x0)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0475
    ChrTalk(
        0x1B,
        "きょ、今日は送ります。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x1C,
        "はい……\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x1A,
        "だああ、じれってえなぁ！！\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x1A,
        (
            "記念祭までに\x01",
            "ハナシ纏めたいって言ったの、\x01",
            "お前らだろ！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C33")

    label("loc_873E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_881F")
    SetChrSubChip(0x1A, 0x0)
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0479
    ChrTalk(
        0x1B,
        "……モジモジ………………\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x1C,
        "……モジモジ………………\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x1A,
        (
            "おーい、お見合いだからって\x01",
            "緊張すんなよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x1A,
        (
            "お前ら家近所なんだろ？\x01",
            "知らねえ仲じゃねえんだしさー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C33")

    label("loc_881F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_8995")
    SetChrSubChip(0x1A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8948")

    #C0483
    ChrTalk(
        0x1A,
        (
            "えー、それでは\x01",
            "お２人の趣味を教えてください……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0484
    ChrTalk(
        0x1B,
        "………読書…………かな………\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x1C,
        "…………か、華道を少々………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0486
    ChrTalk(
        0x1A,
        "１日かけてそれかよ……\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x1A,
        (
            "２人とも、もうちょい\x01",
            "リラックスしろって……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_8990")

    label("loc_8948")


    #C0488
    ChrTalk(
        0x1A,
        (
            "２人とも……もうちょい\x01",
            "リラックスしてくれよ……\x01",
            "お願いだからさ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8990")

    Jump("loc_8C33")

    label("loc_8995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8AF0")
    SetChrSubChip(0x1A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A7F")

    #C0489
    ChrTalk(
        0x1A,
        (
            "えー、それでは\x01",
            "お２人の出会いから……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x1B,
        "………………で、出会い…………\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x1C,
        "……………あの……えっと………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0492
    ChrTalk(
        0x1A,
        (
            "……２人とも、聞いてんのか？\x01",
            "カチコチになってんじゃん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_8AEB")

    label("loc_8A7F")


    #C0493
    ChrTalk(
        0x1A,
        (
            "えー、それでは\x01",
            "お２人の出会いから……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x1A,
        (
            "……おい２人とも聞いてんのか！？\x01",
            "カチコチになってんじゃん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AEB")

    Jump("loc_8C33")

    label("loc_8AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8C33")
    SetChrSubChip(0x1A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BC1")

    #C0495
    ChrTalk(
        0x1A,
        "えー、本日はお日柄もよく……\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x1B,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x1C,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0498
    ChrTalk(
        0x1A,
        (
            "おいお前ら、なんか話せよ！\x01",
            "ハナシが進まねーだろ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_8C33")

    label("loc_8BC1")


    #C0499
    ChrTalk(
        0x1A,
        "えー、本日はお日柄もよく……\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x1A,
        (
            "オイあんま緊張すんなって。\x01",
            "見合いつっても\x01",
            "知らない仲じゃねえんだからよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C33")

    SetChrSubChip(0x1A, 0x0)
    TalkEnd(0x1A)
    Return()

    # Function_28_857A end

    def Function_29_8C3B(): pass

    label("Function_29_8C3B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8CCF")
    Jump("loc_8D19")

    label("loc_8CCF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8CEF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D19")

    label("loc_8CEF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D0F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D19")

    label("loc_8D0F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D19")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D5D")
    Call(0, 28)
    Jump("loc_8DAE")

    label("loc_8D5D")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0501
    ChrTalk(
        0x1B,
        "きょ、今日は送ります。\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x1C,
        "はい……\x02",
    )

    CloseMessageWindow()

    label("loc_8DAE")

    Jump("loc_90EB")

    label("loc_8DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8E36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DCE")
    Call(0, 28)
    Jump("loc_8E31")

    label("loc_8DCE")

    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0503
    ChrTalk(
        0x1B,
        "……モジモジ………………\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x1C,
        "……モジモジ………………\x02",
    )

    CloseMessageWindow()

    label("loc_8E31")

    Jump("loc_90EB")

    label("loc_8E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_8F51")

    #C0505
    ChrTalk(
        0x1A,
        (
            "えー、それでは\x01",
            "お２人の趣味を教えてください……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0506
    ChrTalk(
        0x1B,
        "………読書…………かな………\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x1C,
        "…………か、華道を少々………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0508
    ChrTalk(
        0x1A,
        "１日かけてそれかよ……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x1A,
        (
            "２人とも、もうちょい\x01",
            "リラックスしろって……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_90EB")

    label("loc_8F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_902D")

    #C0510
    ChrTalk(
        0x1A,
        (
            "えー、それでは\x01",
            "お２人の出会いから……\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x1B,
        "………………で、出会い…………\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x1C,
        "……………あの……えっと………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0513
    ChrTalk(
        0x1A,
        (
            "……２人とも、聞いてんのか？\x01",
            "カチコチになってんじゃん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_90EB")

    label("loc_902D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_90EB")

    #C0514
    ChrTalk(
        0x1A,
        "えー、本日はお日柄もよく……\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x1B,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x1C,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0517
    ChrTalk(
        0x1A,
        (
            "おいお前ら、なんか話せよ！\x01",
            "ハナシが進まねーだろ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)

    label("loc_90EB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_8C3B end

    def Function_30_90F3(): pass

    label("Function_30_90F3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9187")
    Jump("loc_91D1")

    label("loc_9187")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_91A7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91D1")

    label("loc_91A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91C7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91D1")

    label("loc_91C7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91D1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9272")

    #C0518
    ChrTalk(
        0xFE,
        (
            "昨日ようやく\x01",
            "アルカンシェルの舞台が見れたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "やっぱ凄いわ～。\x01",
            "ファンブック買って帰んなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9384")

    label("loc_9272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9320")

    #C0520
    ChrTalk(
        0xFE,
        (
            "記念祭は終わっちゃったけど、\x01",
            "あたし達まだ滞在してるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xFE,
        (
            "だってミシュラム行ってないし、\x01",
            "アルカンシェルだって\x01",
            "まだ見てないんだも～ん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_9384")

    label("loc_9320")


    #C0522
    ChrTalk(
        0xFE,
        (
            "せめてミシュラム行くまでは\x01",
            "帰れないわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xFE,
        (
            "うんとショッピングを\x01",
            "楽しんでいかなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9384")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_90F3 end

    def Function_31_938C(): pass

    label("Function_31_938C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9420")
    Jump("loc_946A")

    label("loc_9420")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9440")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_946A")

    label("loc_9440")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9460")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_946A")

    label("loc_9460")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_946A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_950B")

    #C0524
    ChrTalk(
        0xFE,
        (
            "さっきからシェフの人が\x01",
            "ちらちら顔を見せるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "目が合うと手を振ってくるんだけど\x01",
            "……何なのアレ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_958D")

    label("loc_950B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_958D")

    #C0526
    ChrTalk(
        0xFE,
        (
            "あたしはアルカンシェル\x01",
            "狙いだったワケ。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        (
            "あたしの計算だと\x01",
            "今月のチケットなら\x01",
            "どっかで手に入るハズなんだけどー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_958D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_938C end

    def Function_32_9595(): pass

    label("Function_32_9595")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9627")

    #C0528
    ChrTalk(
        0xFE,
        (
            "さーて、市内を\x01",
            "観光させてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        (
            "クロスベルは治安が\x01",
            "イマイチって話だけど、まあ\x01",
            "そんな危ない目には遭わないよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9750")

    label("loc_9627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9708")

    #C0530
    ChrTalk(
        0xFE,
        (
            "今朝鉄道でクロスベルについてね、\x01",
            "ようやくウマイ物が食べられる～\x01",
            "と思ったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xFE,
        (
            "……なんかシェフが\x01",
            "変な料理を持ってくるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xFE,
        (
            "どういうことなんだろ。\x01",
            "注文を間違えたのかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_9750")

    label("loc_9708")


    #C0533
    ChrTalk(
        0xFE,
        (
            "うーむ、どういうことなんだろ。\x01",
            "やっぱり注文を\x01",
            "間違えたのかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9750")

    TalkEnd(0xFE)
    Return()

    # Function_32_9595 end

    def Function_33_9754(): pass

    label("Function_33_9754")

    TalkBegin(0xFE)
    Call(0, 34)
    TalkEnd(0xFE)
    Return()

    # Function_33_9754 end

    def Function_34_975E(): pass

    label("Function_34_975E")

    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0xB, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97F2")
    Jump("loc_983C")

    label("loc_97F2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9812")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_983C")

    label("loc_9812")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9832")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_983C")

    label("loc_9832")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_983C")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrSubChip(0xD, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_9913")

    #C0534
    ChrTalk(
        0xD,
        (
            "#2100Fさてと、市庁舎の受付で\x01",
            "また名簿を見せてもらって……\x02\x03",

            "#2103Fうーん、昨日のうちに\x01",
            "全部コピーしとくんだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xB,
        "もう、教えてくださいよ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A35")

    label("loc_9913")


    #C0536
    ChrTalk(
        0xD,
        (
            "#2100Fそうそう、この写真の\x01",
            "こっちの端に映ってるヒト。\x02\x03",

            "この人と会ってたんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xB,
        "あー、そうかもしれません。\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xB,
        (
            "なんか偉そうな感じの\x01",
            "中年のオジサンでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xB,
        "いったい誰なんですか？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xD,
        (
            "#2100Fふふっ、ヒミツ。\x02\x03",

            "でも大スクープを物にしたら\x01",
            "お礼をさせてもらうわね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_9A35")

    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_34_975E end

    def Function_35_9A3E(): pass

    label("Function_35_9A3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 7)), scpexpr(EXPR_END)), "loc_9B14")
    TurnDirection(0xFE, 0x0, 0)

    #C0541
    ChrTalk(
        0xFE,
        (
            "記念祭の後で、マフィアと\x01",
            "トラブルがあったと言うじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "その後噂を聞かないものだから\x01",
            "心配になってねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xFE,
        (
            "まあ、無事ならいいんだ。\x01",
            "警察の仕事、頑張ってくれたまえ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    Jump("loc_9E13")

    label("loc_9B14")


    #C0544
    ChrTalk(
        0xFE,
        "ギクギクッ……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    Sleep(300)

    #C0545
    ChrTalk(
        0xFE,
        "や、やあ、ティオ君……\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x103,
        "#0200F主任、お久し振りですね。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        (
            "#0000F確かエプスタイン財団の……\x02\x03",

            "……えっと、\x01",
            "またティオの武器を卸しに？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xFE,
        (
            "そ、そのね、君たち支援課が\x01",
            "危ない事に巻き込まれていたと聞いて……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        (
            "……こほん、店主の方に\x01",
            "噂話を聞きに来ただけだよ。\x01",
            "本当にそれだけだとも。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x103,
        (
            "#0203F………………………………\x01",
            "それはご心配をお掛けしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x104,
        (
            "#0300Fま、いろいろあったが\x01",
            "もう平気ッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#0100Fええ、ここ２、３週間は\x01",
            "すっかり落ち着きましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        "そ、そうか……ならいいんだ。\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        (
            "ティオ君、最新型の\x01",
            "魔導杖も持って来ておいた。\x01",
            "ぜひ役立ててくれたまえ！\x02",
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

    #C0555
    ChrTalk(
        0x103,
        (
            "#0211Fやっぱり\x01",
            "持ってきていたんですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    SetScenarioFlags(0xD0, 7)

    label("loc_9E13")

    TalkEnd(0xFE)
    Return()

    # Function_35_9A3E end

    def Function_36_9E17(): pass

    label("Function_36_9E17")

    EventBegin(0x0)
    Fade(500)
    OP_68(58650, 500, -8880, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 58000, -1000, -9000, 90)
    SetChrPos(0x102, 57900, -1000, -8200, 90)
    SetChrPos(0x103, 56550, -1000, -9000, 90)
    SetChrPos(0x104, 56450, -1000, -8200, 90)
    OP_93(0x20, 0x10E, 0x0)
    SetChrSubChip(0x20, 0x0)
    OP_0D()

    #C0556
    ChrTalk(
        0x20,
        (
            "#11Pそうそう、さっき\x01",
            "技術屋風の男が訪ねて来てな。\x01",
            "『魔導杖』なんて物を置いていったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x20,
        "#11P新開発の武器とか言ってたが……\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x20,
        (
            "#11Pこんな得体の知れねえ物、\x01",
            "誰に売りつけろってんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0559
    ChrTalk(
        0x102,
        (
            "#0105F#5P魔導杖って、確か……\x01",
            "ティオちゃんの\x01",
            "使っていた武器よね？\x02\x03",

            "まだ試験中の物だって\x01",
            "聞いたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x104,
        (
            "#0305F#5Pなんでそんな物が\x01",
            "売りに出されてんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x101,
        (
            "#0001F#5P技術屋風の男……か。\x01",
            "少し怪しいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x103,
        (
            "#0206F#6Pそれは……\x01",
            "多分わたしの上司です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A0C2():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0C2)
    Sleep(50)

    def lambda_A0D2():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0D2)
    Sleep(50)

    def lambda_A0E2():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A0E2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0563
    ChrTalk(
        0x104,
        "#0305F#5Pへ、上司……？\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x103,
        (
            "#0211F#6P……ええ、恐らく\x01",
            "魔導杖の改良評価版を\x01",
            "届けに来たのだと思います。\x02\x03",

            "#0206Fわたしに直接渡せばいいのに、\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0565
    ChrTalk(
        0x101,
        (
            "#0012F#11P（えっと……\x01",
            "  なんで直接渡しに来ないんだ？）\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x20,
        (
            "#11Pよく分かんねえが……\x01",
            "この武器は嬢ちゃんに\x01",
            "売っちまっていいんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x20,
        (
            "#11Pならとっとと買い取ってくれや。\x01",
            "一応仕入れ金を払っちまったんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 58000, -1000, -8600, 90)
    SetScenarioFlags(0x4C, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A2D0")
    SetScenarioFlags(0x4C, 4)

    label("loc_A2D0")

    EventEnd(0x5)
    Return()

    # Function_36_9E17 end

    def Function_37_A2D3(): pass

    label("Function_37_A2D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch06900.itc", 0x1E)
    LoadChrToIndex("chr/ch06902.itc", 0x1F)
    LoadChrToIndex("chr/ch37302.itc", 0x20)
    LoadChrToIndex("apl/ch50422.itc", 0x21)
    OP_68(6500, 1300, 9000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x24, 6500, 0, 7750, 0)
    SetChrPos(0x102, 6500, 0, 10250, 180)
    SetChrPos(0x103, 7750, 0, 9000, 270)
    SetChrPos(0x104, 5250, 0, 9000, 90)
    SetChrPos(0x101, 15000, 0, 9000, 270)
    SetChrPos(0x109, 17000, 0, 9000, 270)
    SetChrPos(0x19F, 16000, 0, 9000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0568
    ChrTalk(
        0x102,
        (
            "#5P#0103F……遅いわね、ロイド達。\x01",
            "いつまでかかっているのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x103,
        (
            "#11P#0200F女性を待たすなんて\x01",
            "失礼極まりないです。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x104,
        (
            "#6P#0304Fちっちっち……\x01",
            "男の身支度は、女の化粧と\x01",
            "同じくらい時間がかかるもんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x104, 500)

    #C0571
    ChrTalk(
        0x24,
        (
            "#12P#1900Fへぇ、ランディさんって\x01",
            "経験豊富なんですね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x24, 500)

    #C0572
    ChrTalk(
        0x104,
        (
            "#6P#0300Fハハ、分かる？\x02\x03",

            "#0300Fどうよ、今度俺とデートでも。\x01",
            "フランちゃんみたいな可愛い子なら、\x01",
            "取っておきの場所に連れてってやるぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x24,
        "#12P#1909Fもー、お上手なんですから。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0574
    ChrTalk(
        0x102,
        (
            "#11P#0111F（あのね……\x01",
            "  あなたがナンパして\x01",
            "  どうするのよ。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0575
    ChrTalk(
        0x104,
        (
            "#6P#0309F（いやいや、軽い冗談だって。\x01",
            "  なんとか場を持たせようとだな……）\x02",
        )
    )

    CloseMessageWindow()

    #N0576
    NpcTalk(
        0x101,
        "ロイドの声",
        "ごめん、待たせたみたいだな。\x02",
    )

    CloseMessageWindow()
    OP_68(7750, 1100, 9000, 3000)
    MoveCamera(33, 25, 0, 3000)

    def lambda_A6AF():
        OP_97(0x101, 0xFFFFE98A, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A6AF)

    def lambda_A6C9():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A6C9)
    Sleep(50)

    def lambda_A6DD():
        OP_97(0x19F, 0xFFFFE5A2, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_A6DD)

    def lambda_A6F7():
        OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19F, 2, lambda_A6F7)
    Sleep(50)

    def lambda_A70B():
        OP_97(0x109, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A70B)

    def lambda_A725():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A725)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_A781():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A781)
    Sleep(50)

    def lambda_A791():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A791)
    Sleep(50)

    def lambda_A7A1():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A7A1)
    Sleep(50)

    def lambda_A7B1():
        OP_93(0x24, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_A7B1)
    WaitChrThread(0x101, 1)

    def lambda_A7C2():
        OP_97(0x101, 0x0, 0x0, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A7C2)
    WaitChrThread(0x19F, 1)

    def lambda_A7E0():
        OP_97(0x19F, 0x0, 0x0, 0xFFFFFB1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_A7E0)
    WaitChrThread(0x101, 1)

    def lambda_A7FE():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A7FE)
    WaitChrThread(0x19F, 1)

    def lambda_A80F():
        OP_93(0x19F, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_A80F)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x19F, 1)
    OP_6F(0x79)

    #C0577
    ChrTalk(
        0x24,
        (
            "#6P#1905Fあ、ロイドさんにお姉ちゃん。\x01",
            "それに……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0578
    ChrTalk(
        0x19F,
        (
            "#11Pえ、えっと……\x01",
            "ども、コンニチワ。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x19F)

    #C0579
    ChrTalk(
        0x19F,
        (
            "#11Pひさしぶ……じゃなくて、\x01",
            "えっと、待たせてしまって\x01",
            "ごめんなさいデス。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x24,
        "#6P#1900Fこんにちは、アントンさん。\x02",
    )

    CloseMessageWindow()
    OP_63(0x19F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0581
    ChrTalk(
        0x19F,
        (
            "#11Pななっ……\x01",
            "なんで……僕の名前をっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x24,
        (
            "#6P#1900Fあ、さっきロイドさん達に\x01",
            "名前を教えてもらったんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x19F,
        (
            "#11Pは、ハハ……そういうことね……\x01",
            "（ぬか喜びしちゃったなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x102,
        (
            "#5P#0111F（ちょっと……\x01",
            "  遅かったじゃないの。）\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        (
            "#11P#0006F（ご、ごめん。\x01",
            "  プレゼント選びに時間が\x01",
            "  かかってしまってさ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x103,
        (
            "#12P#0200F（その様子だと、\x01",
            "  いちおう用意はできたんですね。）\x02\x03",

            "（いいものは買えたんですか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x109,
        (
            "#11P#0500F（ううん……\x01",
            "  多分、妙な事には\x01",
            "  ならないと思うけど。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x24, 500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x104)

    #C0588
    ChrTalk(
        0x104,
        (
            "#6P#0304Fはいはい、オフタリさん。\x01",
            "積もる話は\x01",
            "席についてからにしな。\x02\x03",

            "#0300Fフランちゃんも\x01",
            "そこまで長く休憩時間は\x01",
            "とれねぇだろ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x104, 500)

    #C0589
    ChrTalk(
        0x24,
        "#12P#1905Fあ、それもそうですね～。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x19F, 500)

    #C0590
    ChrTalk(
        0x24,
        (
            "#6P#1900F……それじゃ、アントンさん。\x01",
            "座りましょっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x19F,
        "#11Pは、はひっ！\x02",
    )

    CloseMessageWindow()

    def lambda_AC5C():
        OP_97(0x24, 0xFFFFE0C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_AC5C)
    Sleep(50)

    def lambda_AC79():
        OP_97(0x19F, 0xFFFFE0C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_AC79)
    Sleep(500)

    def lambda_AC96():
        OP_93(0x101, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC96)

    def lambda_ACA3():
        OP_93(0x102, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACA3)

    def lambda_ACB0():
        OP_93(0x103, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ACB0)

    def lambda_ACBD():
        OP_93(0x104, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ACBD)

    def lambda_ACCA():
        OP_93(0x109, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ACCA)
    WaitChrThread(0x24, 1)
    WaitChrThread(0x19F, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    TurnDirection(0x104, 0x101, 500)

    #C0592
    ChrTalk(
        0x104,
        (
            "#6P#0304F……さーて、そんじゃ俺たちは\x01",
            "２階のほうに移るとしようぜ。\x02\x03",

            "#0300F俺たちがここで見てちゃ、\x01",
            "色々とやりにくいだろうし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AD7D():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD7D)

    def lambda_AD8A():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD8A)

    def lambda_AD97():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AD97)

    def lambda_ADA4():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ADA4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)

    #C0593
    ChrTalk(
        0x101,
        "#11P#0005Fの、覗くつもりなのか……？\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        (
            "#6P#0309Fお前だって、どうなるか\x01",
            "気になるだろ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x103,
        (
            "#12P#0204F依頼人を見守るのも\x01",
            "我々の義務かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x102,
        (
            "#5P#0100Fふふ、そうよね。\x01",
            "当然の権利でもあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x109,
        (
            "#11P#0506F……すいません、\x01",
            "私も正直気になります。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0x101, 0x109, 500)
    Sleep(500)

    #C0598
    ChrTalk(
        0x101,
        (
            "#5P#0003F曹長まで……\x02\x03",

            "#0000Fまぁ、そうだよな……\x01",
            "アントンさんもガチガチに\x01",
            "緊張してるみたいだし……\x02\x03",

            "暴走しないように\x01",
            "見ておいた方がいいかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x104,
        (
            "#6P#0309Fいよ～し、そうと決まれば\x01",
            "とっとと行くぜ☆\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0600
    ChrTalk(
        0x101,
        "#11P#0006F（楽しそうだな……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(2000, 6500, 9730, 0)
    MoveCamera(48, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x19F, 0x20)
    SetChrSubChip(0x19F, 0x0)
    SetChrFlags(0x19F, 0x4)
    SetChrFlags(0x19F, 0x8000)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x19F, -1100, 100, 2300, 270)
    SetChrPos(0x24, -5350, 100, 2300, 90)
    SetChrPos(0x101, 0, 5000, 10000, 180)
    SetChrPos(0x102, 750, 5000, 9750, 180)
    SetChrPos(0x104, 1500, 5000, 10000, 180)
    SetChrPos(0x109, -750, 5000, 9750, 180)
    SetChrPos(0x103, -1500, 5000, 10000, 180)
    OP_68(0, 6500, 9750, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0x157C)
    OP_6F(0x79)
    Fade(500)
    OP_68(-3240, 1100, 2340, 0)
    MoveCamera(36, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    SetCameraDistance(19000, 3000)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)

    #C0601
    ChrTalk(
        0x19F,
        (
            "#11Pえ、えっと……なんでもフランさん、\x01",
            "僕のことを覚えてくれてたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x24,
        (
            "#6P#1909Fふふ、記念祭の、\x01",
            "しかも最終日のことですし\x01",
            "覚えていますよ～。\x02\x03",

            "#1900Fあの日は本当、大変でしたね～。\x01",
            "もうサイフを落としたりしてませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x19F,
        "#11Pも、もちろん！\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x19F,
        (
            "#11Pせっかくフランさんに\x01",
            "見つけてもらったんだ。\x01",
            "二度と手放すつもりはないよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x24)

    #C0605
    ChrTalk(
        0x24,
        (
            "#6P#1909Fあはは、アントンさんって\x01",
            "おもしろいですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x19F,
        (
            "#11P（や、やった……\x01",
            "  よくわかんないけど\x01",
            "  ウケてる……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x24,
        (
            "#6P#1905Fそういえばアントンさん、\x01",
            "サイフが見つかった後は\x01",
            "なんだかぼーっとしてましたね？\x02\x03",

            "#1900F熱でもあるのかと\x01",
            "心配しちゃいましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x19F,
        (
            "#11P#2Sそれはきっと、\x01",
            "君に見とれていたからさ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0609
    ChrTalk(
        0x24,
        "#6P#1905Fはい？　何か言いました？\x02",
    )

    CloseMessageWindow()
    OP_63(0x19F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0610
    ChrTalk(
        0x19F,
        (
            "#11Pあ、いや、なんでもないよ。\x01",
            "アハハ……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xFFFF)
    Fade(500)
    OP_68(0, 6500, 9730, 0)
    MoveCamera(48, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    #C0611
    ChrTalk(
        0x104,
        (
            "#5P#0304Fハハ、アントンくんは\x01",
            "まだまだだなァ。\x02\x03",

            "#0300Fその口説き文句を\x01",
            "ビシっと言えなきゃ\x01",
            "ナンパなんてできねぇぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x101,
        (
            "#5P#0000Fていうか……\x01",
            "フランも結構\x01",
            "和やかに話してるな。\x02\x03",

            "#0012Fアントンさんは\x01",
            "相変わらずガチガチに\x01",
            "緊張してるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x109,
        (
            "#5P#0503F……フランは私よりも\x01",
            "格段に社交性が高いですから。\x02\x03",

            "#0500F初対面の相手でも\x01",
            "あんな感じなんです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x109, 500)
    Sleep(150)

    #C0614
    ChrTalk(
        0x103,
        (
            "#6P#0205F……ノエルさん、\x01",
            "なんだかおかしいです。\x02\x03",

            "#0200F機嫌がよろしくない\x01",
            "ようですけど……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x109, 0x103, 500)
    Sleep(750)
    OP_64(0x109)

    #C0615
    ChrTalk(
        0x109,
        (
            "#11P#0502Fえっと、違うの。\x01",
            "機嫌が悪いとかいうんじゃ\x01",
            "なくって……\x02\x03",

            "#0506Fなんというか……\x01",
            "あの子、モテるのに今までそういう\x01",
            "浮いた話が全くなかったから。\x02\x03",

            "#0508Fなのに、あの子ったら\x01",
            "アントンさんには妙に好意的で……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0616
    ChrTalk(
        0x102,
        (
            "#11P#0102Fふふ、ノエルさんは\x01",
            "フランさんのことが心配なのね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0617
    ChrTalk(
        0x109,
        (
            "#6P#0505F……え、えっと……\x02\x03",

            "#0504F……はは、そうですね。\x01",
            "たった１人の妹ですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        (
            "#5P#0000F（姉ならではの心配ってやつかな。）\x02\x03",

            "#0006F（俺もこんなふうに、\x01",
            "  セシル姉に心配かけてるのかも……）\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x104,
        (
            "#5P#0305F──おっとぉ、見てみな。\x01",
            "アントンのあの意を決した顔。\x02\x03",

            "#0309Fやっこさん、\x01",
            "そろそろ勝負に出る気だぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_B919():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B919)

    def lambda_B926():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B926)

    def lambda_B933():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B933)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    Fade(500)
    OP_68(-3240, 1100, 2340, 0)
    MoveCamera(36, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    OP_0D()
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_64(0x24)
    OP_63(0x19F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_64(0x19F)
    OP_63(0x19F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x19F)

    #C0620
    ChrTalk(
        0x19F,
        "#11P……あ、あの……フランさん！\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x24,
        "#6P#1905Fはい？　どうしたんですか？\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x19F,
        (
            "#11P実はあなたを探していたのは\x01",
            "他でもないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x19F,
        (
            "#11Pこの間の記念祭で、懸命に\x01",
            "僕のサイフを探してくれたお礼……\x01",
            "それをしっかりしたくって。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x19F,
        "#11Pこれ、受け取ってもらえますか？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_BC79")
    OP_2C(0x2A, 0x1)
    SetChrName("")

    #A0625
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アントンはフランに『みっしぃのぬいぐるみ』を手渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0626
    ChrTalk(
        0x24,
        (
            "#6P#1905Fこれって……\x01",
            "みっしぃのぬいぐるみ\x01",
            "じゃないですか？\x02\x03",

            "#1909Fうわぁ、ありがとうございます！\x02\x03",

            "実は１体持ってるんですけど……\x01",
            "丁度もう１体欲しいなって\x01",
            "思ってたんです～。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x19F,
        (
            "#11P（も、持ってただって……？\x01",
            "  喜んでくれてるみたいだけど、\x01",
            "  計算外っ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x19F,
        (
            "#11P（……ええい、\x01",
            "  勝負するならここしかない！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C31B")

    label("loc_BC79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_BDEC")
    SetChrName("")

    #A0629
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アントンはフランに『アイスジャム』を手渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0630
    ChrTalk(
        0x24,
        (
            "#6P#1905Fこれって……\x01",
            "百貨店にしか置いてない\x01",
            "輸入ものの珍しいジャムですよね？\x02\x03",

            "#1900Fうふ、ありがとうございます。\x01",
            "なんだかお歳暮を\x01",
            "もらっちゃったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x19F,
        (
            "#11P（お、お歳暮って……\x01",
            "  的外れだったのか……！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x19F,
        (
            "#11P（で、でも……\x01",
            "  勝負するならここしかない！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C31B")

    label("loc_BDEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_BFAA")
    OP_2C(0x2A, 0x3)
    SetChrName("")

    #A0633
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アントンはフランに『ぽむぽむニット』を手渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0634
    ChrTalk(
        0x24,
        (
            "#6P#1905Fうわわ、これって……\x01",
            "白いポムのニット帽ですか？\x02\x03",

            "#1900Fお姉ちゃんも、\x01",
            "プライベートでは\x01",
            "白い帽子を被ってるんです。\x02\x03",

            "だから私、お揃いで\x01",
            "白い帽子が欲しいなぁって\x01",
            "思ってたんですよ。\x02\x03",

            "#1909Fありがとうございます、\x01",
            "大切にしますね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x19F,
        (
            "#11P（おお……\x01",
            "  すごく喜んでくれてる！）\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x19F,
        (
            "#11P（よ、よし！\x01",
            "  勝負するならここしかない！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C31B")

    label("loc_BFAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_C173")
    SetChrName("")

    #A0637
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アントンはフランに『ストレガー・ブーツ』を手渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0638
    ChrTalk(
        0x24,
        (
            "#6P#1905Fこれって……\x01",
            "ストレガー社の新作モデルですか？\x02\x03",

            "#1900F確か今、女の子の間で\x01",
            "人気のブーツなんですよね。\x01",
            "履いてる子を見かけましたよ～。\x02\x03",

            "私、ブーツってあんまり\x01",
            "得意じゃないんですけど……\x01",
            "大事にしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x19F,
        (
            "#11P（と、得意じゃないって……！\x01",
            "  ま、的外れなものを\x01",
            "  渡してしまったのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x19F,
        (
            "#11P（で、でも……\x01",
            "  勝負するならここしかない！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C31B")

    label("loc_C173")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_C31B")
    SetChrName("")

    #A0641
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アントンはフランに『ピンキームーン』を手渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0642
    ChrTalk(
        0x24,
        (
            "#6P#1905Fこれって……\x01",
            "この間雑誌で読んだ、\x01",
            "かなり高価なネックレス……！？\x02\x03",

            "そ、そんな……\x01",
            "こんなの受け取って\x01",
            "本当にいいんですか？\x02\x03",

            "#1900Fあ、ありがとうございます。\x01",
            "えと……大事にしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x19F,
        (
            "#11P（さ、さすがに初めて渡す\x01",
            "  プレゼントとしては\x01",
            "  重すぎたのか……！？）\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x19F,
        (
            "#11P（で、でも……\x01",
            "  勝負するならここしかない！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C31B")


    #C0645
    ChrTalk(
        0x19F,
        (
            "#11Pフ、フランさん……！\x01",
            "今、恋人とかっている！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x24)
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0646
    ChrTalk(
        0x24,
        (
            "#6P#1905Fえーっと……\x01",
            "恋人はいませんよ？\x02\x03",

            "#1904Fけど……\x02\x03",

            "#1909F大好きな人ならいます㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    StopBGM(0x1F4)
    Sound(889, 0, 100, 0)

    #C0647
    ChrTalk(
        0x19F,
        "#11P#4S！！！！！！！！！！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x24)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0648
    ChrTalk(
        0x24,
        (
            "#6P#1905F……あ、あれ？\x01",
            "アントンさん……\x01",
            "どうかしましたか？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x24)

    #C0649
    ChrTalk(
        0x104,
        (
            "#N#0306F（あっちゃあ……\x01",
            "  ド直球をド直球で\x01",
            "  返されちまったか。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0650
    ChrTalk(
        0x101,
        (
            "#N#0006F（フランに悪気がないのが\x01",
            "  余計に傷口を広げてるような……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0651
    ChrTalk(
        0x102,
        (
            "#N#0106F（うーん、こればかりは\x01",
            "  さすがに仕方ないと思うけど。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0652
    ChrTalk(
        0x103,
        "#N#0203F（合掌、ですね。）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0653
    ChrTalk(
        0x109,
        "#N#0505F（…………………）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    PlayBGM("ed7005", 0)

    #C0654
    ChrTalk(
        0x19F,
        "#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x19F,
        (
            "#11P…………は、はは。\x01",
            "そ、そうなん……だぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x19F,
        "#11P………………………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x19F, 0xFF)
    SetChrSubChip(0x19F, 0x0)
    SetChrPos(0x19F, -1100, 0, 3300, 270)
    Sound(820, 0, 100, 0)
    OP_0D()

    #C0657
    ChrTalk(
        0x24,
        "#6P#1905F……アントンさん？\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x19F,
        "#11P……ごめん、もう行かなくちゃ。\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x19F,
        (
            "#11P…………フランさん。\x01",
            "その人とのこと…………頑張ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x24,
        "#6P#1905Fえ……？\x02",
    )

    CloseMessageWindow()

    def lambda_C6E4():
        OP_97(0x19F, 0x1B58, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_C6E4)
    Sleep(3000)
    Fade(500)
    OP_68(7790, 1400, 6860, 0)
    MoveCamera(41, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19800, 0)
    EndChrThread(0x19F, 0x1)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrPos(0x19F, 7000, 0, 9000, 0)
    SetChrPos(0x24, 0, 0, 9000, 0)
    SetChrPos(0x101, 8500, 0, 4750, 0)
    SetChrPos(0x109, 7750, 0, 3750, 0)
    SetChrPos(0x102, 9250, 0, 4250, 0)
    SetChrPos(0x103, 7750, 0, 2750, 0)
    SetChrPos(0x104, 9250, 0, 3250, 0)

    def lambda_C7B3():
        OP_97(0x19F, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_C7B3)

    def lambda_C7CD():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C7CD)
    Sleep(30)

    def lambda_C7EA():
        OP_97(0x109, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C7EA)
    Sleep(30)

    def lambda_C807():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C807)
    Sleep(30)

    def lambda_C824():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C824)
    Sleep(30)

    def lambda_C841():
        OP_97(0x104, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C841)
    OP_0D()
    WaitChrThread(0x19F, 1)
    OP_93(0x19F, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_C8EE")

    #C0661
    ChrTalk(
        0x19F,
        "#5P……やあ、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x19F,
        (
            "#5P世話になったね。\x01",
            "……おかげでフランさんの\x01",
            "素敵な笑顔を見れたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA2")

    label("loc_C8EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_C959")

    #C0663
    ChrTalk(
        0x19F,
        "#5P……やあ、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x19F,
        (
            "#5Pプレゼント選びまで\x01",
            "付き合わせてしまって悪かったね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA2")

    label("loc_C959")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_C9D1")

    #C0665
    ChrTalk(
        0x19F,
        "#5P……やあ、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x19F,
        (
            "#5P世話になったね。\x01",
            "……おかげでフランさんの\x01",
            "最高の笑顔を見れたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA2")

    label("loc_C9D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_CA3C")

    #C0667
    ChrTalk(
        0x19F,
        "#5P……やあ、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x19F,
        (
            "#5Pプレゼント選びまで\x01",
            "付き合わせてしまって悪かったね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA2")

    label("loc_CA3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_CAA2")

    #C0669
    ChrTalk(
        0x19F,
        "#5P……やあ、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x19F,
        (
            "#5Pプレゼント選びまで\x01",
            "付き合わせてしまって悪かったね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAA2")


    #C0671
    ChrTalk(
        0x101,
        (
            "#12P#0006Fア、アントンさん……\x01",
            "なんていうか、その……\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x19F,
        (
            "#5P……フッ……\x01",
            "慰めならいらないよ。\x01",
            "いつものことさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x19F,
        (
            "#5P僕の人生はいつも、\x01",
            "いついつまでも、\x01",
            "トライ＆エラーなんだから。\x02",
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

    #C0674
    ChrTalk(
        0x103,
        "#12P#0206F……意味が分かりません。\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x19F,
        "#5Pふふ……気づいたのさ。\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x19F,
        (
            "#5P“大好きな人”を語った\x01",
            "フランさんのあの\x01",
            "安心しきった顔……\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x19F,
        (
            "#5Pあんな顔を見せられたら、\x01",
            "諦めるしかないってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x19F,
        "#5P…………それじゃ、そういうことで。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_CCB9():
        OP_97(0x19F, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_CCB9)
    Sleep(1000)

    def lambda_CCD6():
        OP_93(0x101, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CCD6)
    Sleep(50)

    def lambda_CCE6():
        OP_93(0x102, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CCE6)
    Sleep(50)

    def lambda_CCF6():
        OP_93(0x103, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CCF6)
    Sleep(50)

    def lambda_CD06():
        OP_93(0x104, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CD06)
    Sleep(50)

    def lambda_CD16():
        OP_93(0x109, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CD16)
    Sleep(1000)

    def lambda_CD26():
        OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19F, 2, lambda_CD26)
    WaitChrThread(0x19F, 1)
    WaitChrThread(0x19F, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0679
    ChrTalk(
        0x104,
        "#12P#0306Fありゃあ、重傷だな。\x02",
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x102,
        (
            "#12P#0100F意外とタフそうだから\x01",
            "大丈夫だとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0681
    NpcTalk(
        0x24,
        "フランの声",
        (
            "あれ～、\x01",
            "アントンさん、やっぱり\x01",
            "帰っちゃったんですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_CE55():
        OP_93(0x101, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CE55)

    def lambda_CE62():
        OP_93(0x102, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CE62)

    def lambda_CE6F():
        OP_93(0x103, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CE6F)

    def lambda_CE7C():
        OP_93(0x104, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CE7C)

    def lambda_CE89():
        OP_93(0x109, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CE89)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)

    def lambda_CE9E():
        OP_97(0x24, 0x2134, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_CE9E)
    Sleep(2500)

    def lambda_CEBB():
        OP_93(0x101, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CEBB)
    Sleep(50)

    def lambda_CECB():
        OP_93(0x102, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CECB)
    Sleep(50)

    def lambda_CEDB():
        OP_93(0x103, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CEDB)
    Sleep(50)

    def lambda_CEEB():
        OP_93(0x104, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CEEB)
    Sleep(50)

    def lambda_CEFB():
        OP_93(0x109, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CEFB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x24, 1)
    OP_93(0x24, 0xB4, 0x1F4)

    #C0682
    ChrTalk(
        0x24,
        (
            "#5P#1905Fうーん、帰りの飛行船の時間に\x01",
            "なってしまったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x109,
        "#6P#0507Fフ、フラン！\x02",
    )

    CloseMessageWindow()
    OP_97(0x109, 0x0, 0x0, 0xCB2, 0x1388, 0x0)
    TurnDirection(0x109, 0x24, 0)
    TurnDirection(0x24, 0x109, 500)

    #C0684
    ChrTalk(
        0x24,
        (
            "#11P#1905Fお姉ちゃん……？\x01",
            "どうしたの、血相変えて……\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x109,
        (
            "#6P#0503Fフラン……\x02\x03",

            "#0501F#4S大好きな人って誰なのっ！？\x02\x03",

            "#0501F#4Sひょっとしてロイドさん！？\x02\x03",

            "#0505F#4Sまさか……ランディ先輩じゃ！？\x02",
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

    #C0686
    ChrTalk(
        0x101,
        "#12P#0011Fそ、曹長……！？\x02",
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x103,
        (
            "#12P#0206F（……さっきから\x01",
            "  ずっと黙ってると思ったら……\x01",
            "  そんなことを考えてたんですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x104,
        (
            "#11P#0309Fハッ、やーれやれ。\x01",
            "バレちゃあ仕方が──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0689
    ChrTalk(
        0x102,
        (
            "#5P#0109F……ランディ？\x01",
            "話がややこしくなるから\x01",
            "やめておきましょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x104,
        "#11P#0306F（え、笑顔が怖い……）\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)

    #C0691
    ChrTalk(
        0x109,
        (
            "#6P#0508Fあたしに何でも話すフランに\x01",
            "大好きな人がいたなんて……\x02\x03",

            "#0510Fま、まさか人に言えないような\x01",
            "問題のある人なんじゃ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x24,
        (
            "#11P#1906Fちょ、ちょっと落ち着いてよ～。\x01",
            "皆さんが見てるのに～……\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x109,
        (
            "#6P#0501Fいいからお姉ちゃんに\x01",
            "ちゃんと話しなさいっ！\x02\x03",

            "皆さんのことはジャガイモか何かだと\x01",
            "思っていいから！\x02",
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
    OP_63(0x24, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0694
    ChrTalk(
        0x24,
        (
            "#11P#1906Fもう、お姉ちゃんったら……\x01",
            "仕方ないなぁ。\x02\x03",

            "#1900Fえっと、それじゃあ……\x01",
            "ヒントを出すね。\x02\x03",

            "#1904F……その人は、\x01",
            "警備隊に務めてる人でね。\x01",
            "とっても正義感が強くて……\x02\x03",

            "#1902Fそれでいて、いつも私に\x01",
            "優しくしてくれる人なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x109,
        (
            "#6P#0505Fけ、警備隊……！？\x01",
            "まさかタングラム門にいるの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x24,
        "#11P#1909F……うん㈱\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x109,
        (
            "#6P#0506Fそ、そんな……\x01",
            "そんな人が警備隊にいたなんて……！\x02\x03",

            "#0508Fジャック隊員……それとも、バレル隊員！？\x01",
            "いや、食堂のティマスさんってことも……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x101,
        "#12P#0006Fな、なんか収拾つかなくなってるぞ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0699
    ChrTalk(
        0x24,
        (
            "#11P#1906Fはぁ……\x01",
            "お姉ちゃんたら\x01",
            "意外と鈍いんだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0700
    ChrTalk(
        0x109,
        "#6P#0501Fえ……\x02",
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x24,
        (
            "#11P#1902Fもう、はっきり言わせないでよ～。\x02\x03",

            "#1909Fそんなの……\x01",
            "お姉ちゃんに決まってるじゃない㈱\x02",
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
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0702
    ChrTalk(
        0x109,
        "#6P#0505F#4S……え。\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x24,
        (
            "#11P#1905F……って、いけない、\x01",
            "そろそろ休憩時間が終わっちゃう！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x24, 0x101, 500)

    #C0704
    ChrTalk(
        0x24,
        (
            "#5P#1909F皆さん、そういうわけですから\x01",
            "私はこれで失礼しますね！\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#12P#0012Fあ……うん。\x01",
            "気を付けてな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D812():
        OP_97(0x24, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_D812)
    Sleep(1000)

    def lambda_D82F():
        OP_93(0x101, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D82F)
    Sleep(50)

    def lambda_D83F():
        OP_93(0x102, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D83F)
    Sleep(50)

    def lambda_D84F():
        OP_93(0x103, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D84F)
    Sleep(50)

    def lambda_D85F():
        OP_93(0x104, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D85F)
    Sleep(1000)

    def lambda_D86F():
        OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_D86F)
    WaitChrThread(0x19F, 1)
    WaitChrThread(0x19F, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0706
    ChrTalk(
        0x104,
        (
            "#12P#0304Fハハ……そういうことか。\x02\x03",

            "#0300Fフランちゃん、あの分じゃしばらくは\x01",
            "恋だの何だのには縁がなさそうだな。\x02\x03",

            "#0309Fま、ノエルもこれで安心できるだろ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x109, 0x21)
    Sleep(200)
    SetChrSubChip(0x109, 0x0)
    Sleep(200)
    SetChrSubChip(0x109, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(200)
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    #C0707
    ChrTalk(
        0x109,
        "#5P#0506F#40Wはぁ～～…………\x02",
    )

    CloseMessageWindow()

    def lambda_D9D5():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9D5)
    Sleep(50)

    def lambda_D9E5():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D9E5)
    Sleep(50)

    def lambda_D9F5():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D9F5)
    Sleep(50)

    def lambda_DA05():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DA05)
    WaitChrThread(0x101, 1)

    def lambda_DA16():
        OP_97(0x101, 0x0, 0x0, 0x640, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA16)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x109, 500)

    #C0708
    ChrTalk(
        0x101,
        "#11P#0011Fちょっ……大丈夫か、曹長！？\x02",
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x109,
        (
            "#5P#0509Fあ……す、すみません。\x01",
            "なんだか気が抜けちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x102,
        (
            "#12P#0102Fふふ、フランさんのこと、\x01",
            "本当に心配してたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x109,
        (
            "#5P#0506Fつい取り乱してしまって……\x01",
            "みなさんには見苦しいところを\x01",
            "見られてしまいました。\x02\x03",

            "#0500Fでも……ありがとうございます。\x01",
            "色々と気を遣っていただいて……\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x101,
        (
            "#11P#0012Fはは……アントンさんには\x01",
            "残念な結果に\x01",
            "なっちゃったけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x103,
        (
            "#12P#0204Fロイドさんにとっても\x01",
            "残念じゃないんですか？\x02\x03",

            "#0202Fフランさんの『大好きな人』に\x01",
            "ちょっと期待してたフシを\x01",
            "感じたような。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0714
    ChrTalk(
        0x101,
        (
            "#5P#0011Fそ、そんなわけないだろ！？\x01",
            "まったく、適当なことを\x01",
            "言わないでくれよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x104,
        (
            "#12P#0304Fま、アントンの方は\x01",
            "あとで手が空いてたら\x01",
            "様子を見に行ってやろうぜ。\x02\x03",

            "#0300Fとりあえず、\x01",
            "依頼は達成って感じだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそうだな……\x02\x03",

            "よし、そろそろ行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0717
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【真心の恩返し】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x19F, 0x80)
    SetChrBattleFlags(0x19F, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    RemoveParty(0x9E, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_68(8500, 1500, 9000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 8500, 0, 9000, 180)
    SetChrPos(0x1, 8500, 0, 9000, 180)
    SetChrPos(0x2, 8500, 0, 9000, 180)
    SetChrPos(0x3, 8500, 0, 9000, 180)
    OP_29(0x2A, 0x1, 0x9)
    OP_29(0x2A, 0x4, 0x10)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_37_A2D3 end

    def Function_38_DEA0(): pass

    label("Function_38_DEA0")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x0, 0xA, 0)
    Fade(800)
    OP_68(-51320, 1500, 3430, 0)
    MoveCamera(41, 23, -2, 0)
    OP_6E(540, 0)
    SetCameraDistance(13800, 0)
    SetChrPos(0x101, -50000, 0, 3500, 270)
    SetChrPos(0x102, -48800, 0, 3500, 270)
    SetChrPos(0x103, -50000, 0, 4900, 270)
    SetChrPos(0x104, -48800, 0, 4900, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF54")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, -47860, 0, 4640, 270)
    Jump("loc_DF7F")

    label("loc_DF54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF7F")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, -47860, 0, 4640, 270)

    label("loc_DF7F")

    OP_0D()

    #C0718
    ChrTalk(
        0xA,
        (
            "#6Pうおおお……\x01",
            "どうすればいいんだー！\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0xA,
        (
            "#6P店長もブラウンさんも\x01",
            "手伝ってくれねえし……\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x101,
        (
            "#11P#0000Fあの、すみません。\x01",
            "依頼を出された\x01",
            "セルテオさんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-50110, 1300, 4210, 1000)
    OP_95(0xA, -51650, 0, 4140, 2000, 0x0)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(200)

    #C0721
    ChrTalk(
        0xA,
        (
            "#6Pおっ、来てくれたか！！\x01",
            "君たちが……えっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x103,
        (
            "#11P#0200Fクロスベル警察、特務支援課です。\x01",
            "どうぞよろしく。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x102,
        (
            "#11P#0100Fご依頼、受けさせて\x01",
            "いただきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x104,
        "#11P#0309Fお客様は神様だぜ。\x02",
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x101,
        (
            "#11P#0000Fえっと、よろしくお願いします。\x01",
            "（最近所帯じみてきたよな……）\x02\x03",

            "それで……ご依頼では\x01",
            "何かを探してらっしゃると\x01",
            "いう事でしたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0xA,
        (
            "#6Pそうそう、そうなんだ。\x01",
            "とにかく助けてくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0xA,
        (
            "#6P実は店長に言われて\x01",
            "全く新しい料理の開発に\x01",
            "取り組んでるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xA,
        (
            "#6Pそう上手くいかなくてな。\x01",
            "どうにも行き詰まってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x102,
        (
            "#11P#0100Fなるほど……\x01",
            "そういう事もあるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x104,
        (
            "#11P#0303Fプロのシェフともなれば\x01",
            "適当にさくっとっつーわけにも\x01",
            "いかないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0xA,
        (
            "#6Pそうなんだ、ウチは\x01",
            "有名人なんかも利用するしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xA,
        (
            "#6Pで……君らの手を\x01",
            "借りたいってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0xA,
        (
            "#6P市民に溶け込んだ部署らしいし\x01",
            "あちこちの食事処にも\x01",
            "通じてるんじゃないかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0xA,
        (
            "#6P……探してるのはズバリ、\x01",
            "料理の過程でまれにできてしまう\x01",
            "『奇想天外な一品』だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x103,
        (
            "#11P#0203F『奇想天外な一品』……\x02\x03",

            "#0200Fオムライスを作ろうとしたのに\x01",
            "別の物が出来てしまったりする\x01",
            "アレですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xA,
        "#6Pそう、それこそ創作料理の真髄だ！\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0xA,
        (
            "#6P失敗ではないギリギリのライン！\x01",
            "そこに全く新しい発想があるんだ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0738
    ChrTalk(
        0xA,
        (
            "#6P……って君たちも料理をするのか？\x01",
            "よかった、これは期待大だぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x101,
        (
            "#11P#0012Fはは、プロの方に\x01",
            "見せるほどの物じゃないですが……\x02\x03",

            "#0000Fまあ事情は判りました。\x01",
            "奇想天外な料理を\x01",
            "お持ちすればいいんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xA,
        (
            "#6Pああ、色々食べ比べたいから\x01",
            "最低でも１０種類は欲しい所だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0xA,
        (
            "#6Pというか……\x01",
            "多ければ多いほどいい。\x01",
            "なるべく沢山集めてきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0xA,
        (
            "#6Pじゃあよろしく頼むぜ！\x01",
            "楽しみに待ってるからさ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0743
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【求む創作料理！】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -50150, 0, 4140, 270)
    SetChrPos(0xA, -52030, 0, 3650, 270)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E75A")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_E75A")

    OP_29(0x29, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_38_DEA0 end

    def Function_39_E763(): pass

    label("Function_39_E763")

    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(800)
    OP_68(-50110, 1300, 4210, 0)
    MoveCamera(41, 23, -2, 0)
    OP_6E(540, 0)
    SetCameraDistance(13800, 0)
    SetChrPos(0x101, -50000, 0, 3500, 270)
    SetChrPos(0x102, -48800, 0, 3500, 270)
    SetChrPos(0x103, -50000, 0, 4900, 270)
    SetChrPos(0x104, -48800, 0, 4900, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E813")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, -47860, 0, 4640, 270)
    Jump("loc_E83E")

    label("loc_E813")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E83E")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, -47860, 0, 4640, 270)

    label("loc_E83E")

    SetChrPos(0xA, -51650, 0, 4140, 90)
    OP_0D()

    #C0744
    ChrTalk(
        0xA,
        (
            "#6Pよしっ、それじゃ\x01",
            "早速預からせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E8E9")

    #C0745
    ChrTalk(
        0xA,
        (
            "#6Pふむ、数は少なめだが\x01",
            "この中に発想をインスパイア\x01",
            "してくれるモンがあるだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB61")

    label("loc_E8E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E957")
    OP_2C(0x29, 0x2)

    #C0746
    ChrTalk(
        0xA,
        (
            "#6Pふむ……これだけあれば十分だ。\x01",
            "へっ、試食を重ねて\x01",
            "いい料理に仕上げてやるぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB61")

    label("loc_E957")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E9D6")
    OP_2C(0x29, 0x4)

    #C0747
    ChrTalk(
        0xA,
        (
            "#6Pしかしこんなに\x01",
            "持って来てくれるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0xA,
        (
            "#6P素晴らしい！\x01",
            "こいつは斬新な料理ができそうだ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB61")

    label("loc_E9D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB61")
    OP_2C(0x29, 0x6)

    #C0749
    ChrTalk(
        0xA,
        (
            "#6Pしかし……君らは何者なんだ？\x01",
            "あらゆる料理を網羅した\x01",
            "この品揃えは……\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0xA,
        (
            "#6Pまるでクロスベルの料理を\x01",
            "知り尽くしてるみたいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x101,
        (
            "#11P#0000Fはは、大した事は。\x02\x03",

            "ウチは基本的に自炊で\x01",
            "日常的に料理してますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x104,
        (
            "#11P#0300Fいつの間にか\x01",
            "それぞれ得意料理を持ってるよな。\x01",
            "俺はマーボーとか大得意だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0xA,
        (
            "#6Pそうか、君らも\x01",
            "料理人の心を\x01",
            "持っているようだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB61")

    Call(0, 42)

    #C0754
    ChrTalk(
        0xA,
        (
            "#6Pいや～、だが助かったぜ。\x01",
            "新レシピが纏められなかったら\x01",
            "どうなっていた事か……\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x101,
        "#11P#0005Fどうなるんですか？\x02",
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0xA,
        (
            "#6Pい、いや、なんでもない。\x01",
            "大した話じゃねえんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0757
    ChrTalk(
        0xA,
        (
            "#6Pそうだ、今回の礼と言っちゃなんだが\x01",
            "試作品を食べていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0xA,
        (
            "#6P『トリュフと魚目玉のスープ』\x01",
            "まだ味の方がイマイチなんだが……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED3A")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_ED3A")

    Sleep(1200)

    #C0759
    ChrTalk(
        0x103,
        "#11P#0211F味以前に見た目がグロいです。\x02",
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x102,
        "#11P#0106F完全にゲテモノね……\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x104,
        "#11P#0300F気持ちだけ受け取っとくぜ。\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0xA,
        (
            "#6Pそうか……そいつは残念だな。\x01",
            "感想を聞きたかったんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_F1FA")

    #C0763
    ChrTalk(
        0xA,
        (
            "#6Pまあいいや、なら代わりに\x01",
            "こいつをやるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF6E")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0764
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピをもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0765
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x10)

    #C0766
    ChrTalk(
        0xA,
        (
            "#6Pさっきあんたらがくれた料理に\x01",
            "クリーミーなスープがあったろ？\x01",
            "それを見てパッと思いついたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0xA,
        (
            "#6Pだが普通すぎて\x01",
            "恐らく客受けはしねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0xA,
        (
            "#6Pよかったら君らで\x01",
            "食べてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F05C")

    label("loc_EF6E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0769
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をもらった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1BE, 1)

    #C0770
    ChrTalk(
        0xA,
        (
            "#6P『トリュフと魚目玉のスープ』を\x01",
            "ベースにした一品なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0xA,
        (
            "#6Pこんなんじゃ普通すぎて\x01",
            "とても客には出せねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0xA,
        (
            "#6Pよかったら君らで\x01",
            "食べてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F05C")


    #C0773
    ChrTalk(
        0x101,
        (
            "#11P#0000Fありがとうございます……\x02\x03",

            "#0003Fというか、創作料理って\x01",
            "こういう普通の物でいいんじゃ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0774
    ChrTalk(
        0xA,
        "#6Pん、何か言ったか？\x02",
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x101,
        "#11P#0006Fいえ、別に……\x02",
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x102,
        (
            "#11P#0100F（ちょっと感覚の\x01",
            "  ずれた人みたいね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0xA,
        (
            "#6Pうっし、んじゃあオレは\x01",
            "料理の試食に入るとするか……\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0xA,
        (
            "#6P君らには世話になったな。\x01",
            "また何かあったらよろしく頼むぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x103,
        "#11P#0200Fええ、いつでもどうぞ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_F3CB")

    label("loc_F1FA")


    #C0780
    ChrTalk(
        0xA,
        (
            "#6Pまあいいや、なら代わりに\x01",
            "こいつを渡しておこう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0781
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F5, 1)

    #C0782
    ChrTalk(
        0xA,
        (
            "#6P食中毒になった時のために\x01",
            "常備してるもんだ。\x01",
            "君らで使ってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x101,
        (
            "#11P#0005Fあ、ありがとうございます……\x02\x03",

            "#0006Fというか、そこまで\x01",
            "打ち込んでるんですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0xA,
        (
            "#6Pフ……今回は色々と賭けてるんだ。\x01",
            "オレも料理人だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0xA,
        (
            "#6P君らには世話になったな。\x01",
            "また何かあったらよろしく頼むぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x101,
        "#11P#0000Fええ、いつでもどうぞ。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_F3CB")

    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0787
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【求む創作料理！】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -50150, 0, 4140, 270)
    SetChrPos(0xA, -52030, 0, 3650, 270)
    OP_4C(0xA, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F475")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_F475")

    OP_29(0x29, 0x4, 0x10)
    OP_29(0x29, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_39_E763 end

    def Function_40_F483(): pass

    label("Function_40_F483")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_END)), "loc_F4A6")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_END)), "loc_F4BF")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_END)), "loc_F4D8")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_END)), "loc_F4F1")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_END)), "loc_F50A")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F50A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_END)), "loc_F523")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F523")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_END)), "loc_F53C")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F53C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_END)), "loc_F555")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F555")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_END)), "loc_F56E")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F56E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_END)), "loc_F587")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F587")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_END)), "loc_F5A0")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F5A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_END)), "loc_F5B9")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F5B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_END)), "loc_F5D2")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F5D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_END)), "loc_F5EB")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F5EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_END)), "loc_F604")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F604")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_END)), "loc_F61D")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F61D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_END)), "loc_F636")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F636")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_END)), "loc_F64F")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F64F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_END)), "loc_F668")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F668")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_END)), "loc_F681")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F681")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_END)), "loc_F69A")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F69A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_END)), "loc_F6B3")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_END)), "loc_F6CC")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_END)), "loc_F6E5")
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6E5")

    Return()

    # Function_40_F483 end

    def Function_41_F6E6(): pass

    label("Function_41_F6E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6FA")
    Jump("loc_FE03")

    label("loc_F6FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F744")

    #C0788
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F744")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F78E")

    #C0789
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "２種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F78E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7D8")

    #C0790
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "３種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F7D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F822")

    #C0791
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "４種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F822")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F86C")

    #C0792
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "５種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F86C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8B6")

    #C0793
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "６種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F8B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F900")

    #C0794
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "７種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F900")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F94A")

    #C0795
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "８種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F94A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F994")

    #C0796
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "９種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F994")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9E0")

    #C0797
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１０種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_F9E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA2C")

    #C0798
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１１種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FA2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA78")

    #C0799
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１２種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FA78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAC4")

    #C0800
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１３種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FAC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB10")

    #C0801
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１４種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FB10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB5C")

    #C0802
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１５種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FB5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBA8")

    #C0803
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１６種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FBA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBF4")

    #C0804
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１７種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FBF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC40")

    #C0805
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１８種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FC40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC8C")

    #C0806
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "１９種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FC8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCD8")

    #C0807
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "２０種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FCD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD24")

    #C0808
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "２１種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FD24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD70")

    #C0809
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "２２種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FD70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDBC")

    #C0810
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "２３種類だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE03")

    label("loc_FDBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE03")

    #C0811
    ChrTalk(
        0xA,
        (
            "君らが持ってる\x01",
            "奇想天外な料理は……\x01",
            "２４種類だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE03")

    Return()

    # Function_41_F6E6 end

    def Function_42_FE04(): pass

    label("Function_42_FE04")

    ClearScenarioFlags(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_END)), "loc_FE17")
    SubItemNumber(0x192, 1)

    label("loc_FE17")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_END)), "loc_FE27")
    SubItemNumber(0x195, 1)

    label("loc_FE27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_END)), "loc_FE37")
    SubItemNumber(0x198, 1)

    label("loc_FE37")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_END)), "loc_FE47")
    SubItemNumber(0x19B, 1)

    label("loc_FE47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_END)), "loc_FE57")
    SubItemNumber(0x19E, 1)

    label("loc_FE57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_END)), "loc_FE67")
    SubItemNumber(0x1A1, 1)

    label("loc_FE67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_END)), "loc_FE77")
    SubItemNumber(0x1A4, 1)

    label("loc_FE77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_END)), "loc_FE87")
    SubItemNumber(0x1A7, 1)

    label("loc_FE87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_END)), "loc_FE97")
    SubItemNumber(0x1AA, 1)

    label("loc_FE97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_END)), "loc_FEA7")
    SubItemNumber(0x1AD, 1)

    label("loc_FEA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_END)), "loc_FEB7")
    SubItemNumber(0x1B0, 1)

    label("loc_FEB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_END)), "loc_FEC7")
    SubItemNumber(0x1B3, 1)

    label("loc_FEC7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_END)), "loc_FED7")
    SubItemNumber(0x1B6, 1)

    label("loc_FED7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_END)), "loc_FEE7")
    SubItemNumber(0x1B9, 1)

    label("loc_FEE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_END)), "loc_FEFA")
    SubItemNumber(0x1BC, 1)
    SetScenarioFlags(0x2, 1)

    label("loc_FEFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_END)), "loc_FF0A")
    SubItemNumber(0x1BF, 1)

    label("loc_FF0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_END)), "loc_FF1A")
    SubItemNumber(0x1C2, 1)

    label("loc_FF1A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_END)), "loc_FF2A")
    SubItemNumber(0x1C5, 1)

    label("loc_FF2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_END)), "loc_FF3A")
    SubItemNumber(0x1C8, 1)

    label("loc_FF3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_END)), "loc_FF4A")
    SubItemNumber(0x1CB, 1)

    label("loc_FF4A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_END)), "loc_FF5A")
    SubItemNumber(0x1CE, 1)

    label("loc_FF5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_END)), "loc_FF6A")
    SubItemNumber(0x1D1, 1)

    label("loc_FF6A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_END)), "loc_FF7A")
    SubItemNumber(0x1D4, 1)

    label("loc_FF7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_END)), "loc_FF8A")
    SubItemNumber(0x1D7, 1)

    label("loc_FF8A")

    Return()

    # Function_42_FE04 end

    SaveToFile()

Try(main)
