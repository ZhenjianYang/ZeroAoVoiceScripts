from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1040.bin",                # FileName
        "t1040",                    # MapName
        "t1040",                    # Location
        0x0044,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 68, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1040",                  # 0
        "キリカ",                 # 1
        "リュート",               # 2
        "メーシェ",               # 3
        "男の子",                 # 4
        "男性",                   # 5
        "男性",                   # 6
        "女性",                   # 7
        "娘",                     # 8
        "青年",                   # 9
        "観光客",                 # 10
        "老人",                   # 11
        "老婦人",                 # 12
        "ウィノナ",               # 13
        "ドローナ",               # 14
        "娘",                     # 15
        "青年",                   # 16
    ))

    AddCharChip((
        "chr/ch07302.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34500.itc",                   # 02
        "chr/ch21302.itc",                   # 03
        "chr/ch21202.itc",                   # 04
        "chr/ch24602.itc",                   # 05
        "chr/ch24202.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch20302.itc",                   # 08
        "chr/ch27900.itc",                   # 09
        "chr/ch26600.itc",                   # 0A
        "chr/ch21602.itc",                   # 0B
        "chr/ch33002.itc",                   # 0C
        "chr/ch21702.itc",                   # 0D
        "chr/ch21300.itc",                   # 0E
        "chr/ch21200.itc",                   # 0F
    ))

    DeclNpc(-97889,  0,       18979,   45,   469,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-104069, 0,       2980,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-101099, 0,       5880,    90,   257,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-103029, 0,       10760,   225,  469,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-104839, 0,       8949,    45,   469,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-93879,  0,       11039,   225,  469,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-95839,  0,       9050,    45,   469,  0x0, 0,   8,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-104949, 0,       8989,    45,   469,  0x0, 0,   3,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-102970, 0,       10960,   225,  469,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-93940,  0,       11039,   225,  469,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-97919,  0,       18979,   45,   469,  0x0, 0,   12,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-97930,  0,       20979,   135,  469,  0x0, 0,   13,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-1860,   0,       10640,   180,  257,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-6250,   0,       6099,    180,  257,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-6019,   0,       4829,    90,   385,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-7389,   0,       3789,    45,   385,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)

    DeclActor(-1770,   0,       8810,    1000,    -1860,   1500,    10640,   0x007E, 0,  17, 0x0000)
    DeclActor(-101650, 0,       2470,    1000,    -104070, 1500,    2980,    0x007E, 0,  5,  0x0000)
    DeclActor(-102930, 0,       14990,   1200,    -102930, 800,     14990,   0x007C, 0,  33, 0x0000)

    ScpFunction((
        "Function_0_388",          # 00, 0
        "Function_1_440",          # 01, 1
        "Function_2_4C9",          # 02, 2
        "Function_3_591",          # 03, 3
        "Function_4_656",          # 04, 4
        "Function_5_8A0",          # 05, 5
        "Function_6_8A4",          # 06, 6
        "Function_7_B34",          # 07, 7
        "Function_8_E63",          # 08, 8
        "Function_9_EB9",          # 09, 9
        "Function_10_10C9",        # 0A, 10
        "Function_11_1274",        # 0B, 11
        "Function_12_13AC",        # 0C, 12
        "Function_13_1578",        # 0D, 13
        "Function_14_1796",        # 0E, 14
        "Function_15_19A9",        # 0F, 15
        "Function_16_1B38",        # 10, 16
        "Function_17_1CD2",        # 11, 17
        "Function_18_1CD6",        # 12, 18
        "Function_19_1E33",        # 13, 19
        "Function_20_1E80",        # 14, 20
        "Function_21_1EDB",        # 15, 21
        "Function_22_1F94",        # 16, 22
        "Function_23_1FFA",        # 17, 23
        "Function_24_2049",        # 18, 24
        "Function_25_2EC9",        # 19, 25
        "Function_26_2F22",        # 1A, 26
        "Function_27_2F7B",        # 1B, 27
        "Function_28_2FD4",        # 1C, 28
        "Function_29_302D",        # 1D, 29
        "Function_30_3086",        # 1E, 30
        "Function_31_3949",        # 1F, 31
        "Function_32_4233",        # 20, 32
        "Function_33_4C2D",        # 21, 33
    ))


    def Function_0_388(): pass

    label("Function_0_388")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3C8"),
        (1, "loc_3D4"),
        (2, "loc_3E0"),
        (3, "loc_3EC"),
        (4, "loc_3F8"),
        (5, "loc_404"),
        (6, "loc_410"),
        (SWITCH_DEFAULT, "loc_41C"),
    )


    label("loc_3C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_404")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_410")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_41C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_428")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_43F")

    Return()

    # Function_0_388 end

    def Function_1_440(): pass

    label("Function_1_440")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C8")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_440")

    label("loc_4C8")

    Return()

    # Function_1_440 end

    def Function_2_4C9(): pass

    label("Function_2_4C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E3")
    Event(0, 24)

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4F1")
    Jump("loc_58A")

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_58A")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_50D")
    Jump("loc_58A")

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_51B")
    Jump("loc_58A")

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_529")
    Jump("loc_58A")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_550")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_58A")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_581")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_58A")

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_58A")

    label("loc_58A")

    BeginChrThread(0xA, 0, 0, 1)
    Return()

    # Function_2_4C9 end

    def Function_3_591(): pass

    label("Function_3_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C8")
    SetMapObjFrame(0xFF, "t1040_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky_y", 0x1, 0x1)
    Jump("loc_5EC")

    label("loc_5C8")

    SetMapObjFrame(0xFF, "t1040_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1040_sky_y", 0x0, 0x1)

    label("loc_5EC")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_655")
    LoadEffect(0x0, "event\\eva00_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -102930, 800, 14990, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_655")

    Return()

    # Function_3_591 end

    def Function_4_656(): pass

    label("Function_4_656")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EA")
    Jump("loc_734")

    label("loc_6EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_734")

    label("loc_70A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_734")

    label("loc_72A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_734")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811")
    SetChrSubChip(0xFE, 0x0)

    #C0001
    ChrTalk(
        0xFE,
        (
            "#3403Fふむ……\x01",
            "さすがは高級レストランと\x01",
            "銘打つだけはある。\x02\x03",

            "#3400F……だけど……\x02\x03",

            "#3404F（フフ……\x01",
            "  マオ婆さんの素朴な料理の方が\x01",
            "  私には合っているわね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_898")

    label("loc_811")


    #C0002
    ChrTalk(
        0xFE,
        (
            "#3405F……あら、あなた達も\x01",
            "食事を取りに来たのかしら。\x02\x03",

            "#3400F値は張るけど\x01",
            "なかなかの味をしているわ。\x01",
            "気が向いたら注文してはどう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_898")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_656 end

    def Function_5_8A0(): pass

    label("Function_5_8A0")

    Call(0, 6)
    Return()

    # Function_5_8A0 end

    def Function_6_8A4(): pass

    label("Function_6_8A4")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B30")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_90F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B2B")

    label("loc_92F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_943")
    Jump("loc_B2B")

    label("loc_943")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_96A")
    Jump("loc_B2B")

    label("loc_96A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_978")
    Jump("loc_B2B")

    label("loc_978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_986")
    Jump("loc_B2B")

    label("loc_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_994")
    Jump("loc_B2B")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_9A2")
    Jump("loc_B2B")

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A44")

    #C0003
    ChrTalk(
        0x9,
        (
            "日も落ちてきました。\x01",
            "そろそろミシュラム帰りのお客様も\x01",
            "入ってくる頃でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "今のうちに夜に向けて\x01",
            "仕込みをしておかなければ\x01",
            "いけませんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2B")

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_B22")

    #C0005
    ChrTalk(
        0x9,
        (
            "よくぞいらっしゃいました。\x01",
            "レストラン《フォルトゥナ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "私が丹精込めて作った料理を\x01",
            "どうか味わっていってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "最高級の食材を用いた料理は\x01",
            "お客様を必ずや\x01",
            "幸福の渦へと誘うでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2B")

    label("loc_B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B2B")

    label("loc_B2B")

    Jump("loc_8B1")

    label("loc_B30")

    TalkEnd(0x9)
    Return()

    # Function_6_8A4 end

    def Function_7_B34(): pass

    label("Function_7_B34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_B45")
    Jump("loc_E5F")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_B53")
    Jump("loc_E5F")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_B61")
    Jump("loc_E5F")

    label("loc_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B6F")
    Jump("loc_E5F")

    label("loc_B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_B7D")
    Jump("loc_E5F")

    label("loc_B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58")

    #C0008
    ChrTalk(
        0xFE,
        (
            "時々、妙に汗をかいたおじさんが\x01",
            "昼食をとりにくることがあるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "多分どこかの施設の\x01",
            "従業員だと思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "……もしかして、みっしぃの中の……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "……ううん、なんでもないわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CE5")

    label("loc_C58")


    #C0012
    ChrTalk(
        0xFE,
        (
            "時々、妙に汗をかいたおじさんが\x01",
            "昼食をとりにくることがあるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "……もしかしたらみっしぃの中の……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "……ううん、なんでもないわ。\x02",
    )

    CloseMessageWindow()

    label("loc_CE5")

    Jump("loc_E5F")

    label("loc_CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_E56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD3")

    #C0015
    ChrTalk(
        0xFE,
        (
            "あの東方風の女性……\x01",
            "なんだか難しい顔をして食べてるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "……まさか、\x01",
            "ライバル店のスパイかしら……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "………………………………！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……良く考えたら\x01",
            "この店にライバルなんて\x01",
            "いなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E51")

    label("loc_DD3")


    #C0019
    ChrTalk(
        0xFE,
        (
            "ふふ、良く考えたら\x01",
            "この店にライバルなんて\x01",
            "いなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "お客さんをスパイと\x01",
            "勘違いするなんて失礼よね。\x01",
            "反省、反省。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E51")

    Jump("loc_E5F")

    label("loc_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E5F")

    label("loc_E5F")

    TalkEnd(0xFE)
    Return()

    # Function_7_B34 end

    def Function_8_E63(): pass

    label("Function_8_E63")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        "むしゃむしゃむしゃ……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "おとーさん、早く食べて\x01",
            "テーマパークに戻ろう！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_E63 end

    def Function_9_EB9(): pass

    label("Function_9_EB9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F4D")
    Jump("loc_F97")

    label("loc_F4D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F6D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F97")

    label("loc_F6D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F8D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F97")

    label("loc_F8D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F97")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1078")

    #C0023
    ChrTalk(
        0xFE,
        (
            "テーマパークの中に食べたい店が\x01",
            "なかったものだからね。\x01",
            "一度出てここで食事をとっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        "むしゃむしゃむしゃ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    #C0025
    ChrTalk(
        0xFE,
        "こらこら、少し落ち着いて食べなさい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_10C1")

    label("loc_1078")

    SetChrSubChip(0xFE, 0x0)

    #C0026
    ChrTalk(
        0xFE,
        (
            "テーマパークで遊びたいのは分かるが\x01",
            "食事時くらい落ち着きなさい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_EB9 end

    def Function_10_10C9(): pass

    label("Function_10_10C9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_115D")
    Jump("loc_11A7")

    label("loc_115D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_117D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11A7")

    label("loc_117D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_119D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11A7")

    label("loc_119D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11A7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0027
    ChrTalk(
        0xFE,
        (
            "ミシュラムの開発が\x01",
            "ＩＢＣによって行われていることは\x01",
            "知っているだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "このレストランはＩＢＣの審査会で\x01",
            "一番優秀だったコックが\x01",
            "開いている店らしいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_10C9 end

    def Function_11_1274(): pass

    label("Function_11_1274")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1308")
    Jump("loc_1352")

    label("loc_1308")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1328")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1352")

    label("loc_1328")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1348")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1352")

    label("loc_1348")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1352")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0029
    ChrTalk(
        0xFE,
        (
            "へぇ……すごいのね、\x01",
            "ここのコックさん。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_1274 end

    def Function_12_13AC(): pass

    label("Function_12_13AC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1440")
    Jump("loc_148A")

    label("loc_1440")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1460")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_148A")

    label("loc_1460")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1480")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_148A")

    label("loc_1480")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_148A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1539")

    #C0030
    ChrTalk(
        0xFE,
        (
            "いいドレスは買えたけど……\x01",
            "宝飾店は一見様お断りっていうじゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "んもー、腹が立つ！\x01",
            "こうなったらヤケ食いよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1570")

    label("loc_1539")


    #C0032
    ChrTalk(
        0xFE,
        (
            "宝飾店に入れなかった\x01",
            "腹いせに、今日はヤケ食いよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1570")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_13AC end

    def Function_13_1578(): pass

    label("Function_13_1578")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_160C")
    Jump("loc_1656")

    label("loc_160C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_162C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1656")

    label("loc_162C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_164C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1656")

    label("loc_164C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1656")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1750")

    #C0033
    ChrTalk(
        0xFE,
        (
            "正直、宝飾店に\x01",
            "入れなくて助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "ブティックで買ったドレスの上に\x01",
            "宝石なんか買ってたら\x01",
            "破産するところだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……でも、このレストランも\x01",
            "結構高そうだなぁ。\x01",
            "……大丈夫かなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_178E")

    label("loc_1750")


    #C0036
    ChrTalk(
        0xFE,
        (
            "このレストランも\x01",
            "結構高そうだなぁ。\x01",
            "……大丈夫かなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_1578 end

    def Function_14_1796(): pass

    label("Function_14_1796")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_182A")
    Jump("loc_1874")

    label("loc_182A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_184A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1874")

    label("loc_184A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_186A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1874")

    label("loc_186A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1874")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1942")

    #C0037
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "ふむむ、さすがの味じゃな！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "Ｂ級グルメから\x01",
            "三ツ星レストランまでを渡り歩く\x01",
            "このわしの舌を唸らせるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "うむ、天晴れじゃ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_19A1")

    label("loc_1942")


    #C0040
    ChrTalk(
        0xFE,
        (
            "さすが高級保養地のレストラン……\x01",
            "このわしの舌を唸らせるとはのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "うむ、天晴れじゃ！\x02",
    )

    CloseMessageWindow()

    label("loc_19A1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_1796 end

    def Function_15_19A9(): pass

    label("Function_15_19A9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A3D")
    Jump("loc_1A87")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A5D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A87")

    label("loc_1A5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A7D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A87")

    label("loc_1A7D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A87")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0042
    ChrTalk(
        0xFE,
        (
            "今夜、妻をハルトマン議長の主催する\x01",
            "パーティに連れて行くのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "なかなか刺激的な場所だからね。\x01",
            "ふふ、妻の反応が楽しみだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_19A9 end

    def Function_16_1B38(): pass

    label("Function_16_1B38")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BCC")
    Jump("loc_1C16")

    label("loc_1BCC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1BEC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C16")

    label("loc_1BEC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C0C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C16")

    label("loc_1C0C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C16")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0044
    ChrTalk(
        0xFE,
        (
            "今日は夫とゆっくり\x01",
            "観覧車などに乗って楽しんでいたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "激しい乗り物に乗らなくても\x01",
            "十二分に楽しめるのは\x01",
            "なかなか素晴らしいことだわね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_1B38 end

    def Function_17_1CD2(): pass

    label("Function_17_1CD2")

    Call(0, 18)
    Return()

    # Function_17_1CD2 end

    def Function_18_1CD6(): pass

    label("Function_18_1CD6")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D41")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1D41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D61")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E2A")

    label("loc_1D61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D75")
    Jump("loc_1E2A")

    label("loc_1D75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0046
    ChrTalk(
        0x14,
        (
            "ブティック《コルセリカ》では\x01",
            "フォーマルからカジュアルまで\x01",
            "多数ご用意していますのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x14,
        (
            "よろしければ係の者が\x01",
            "お客様に似合う服を\x01",
            "見繕いいたしますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E2A")

    Jump("loc_1CE3")

    label("loc_1E2F")

    TalkEnd(0x14)
    Return()

    # Function_18_1CD6 end

    def Function_19_1E33(): pass

    label("Function_19_1E33")

    TalkBegin(0xFE)
    TurnDirection(0x15, 0x16, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4F")
    Call(0, 21)
    Jump("loc_1E7C")

    label("loc_1E4F")


    #C0048
    ChrTalk(
        0xFE,
        (
            "うふふ……\x01",
            "よくお似合いになってますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7C")

    TalkEnd(0xFE)
    Return()

    # Function_19_1E33 end

    def Function_20_1E80(): pass

    label("Function_20_1E80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9C")
    OP_93(0xFE, 0x5A, 0x0)
    Call(0, 21)
    Jump("loc_1ED7")

    label("loc_1E9C")


    #C0049
    ChrTalk(
        0x16,
        (
            "うーん、確かにこの清楚さ……\x01",
            "あたしに似合ってるかも㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED7")

    TalkEnd(0xFE)
    Return()

    # Function_20_1E80 end

    def Function_21_1EDB(): pass

    label("Function_21_1EDB")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0050
    ChrTalk(
        0x15,
        (
            "お客様、そちらのドレス……\x01",
            "とってもお似合いですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x16,
        (
            "うふふ、そうかしら？\x01",
            "じゃあ決めちゃおうっかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x15,
        (
            "でしたら早速、\x01",
            "奥のほうでサイズを測りますよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_21_1EDB end

    def Function_22_1F94(): pass

    label("Function_22_1F94")

    TalkBegin(0xFE)

    #C0053
    ChrTalk(
        0xFE,
        (
            "着いて間もないってのに\x01",
            "もうあんな高そうな買い物を……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "……ひぃい、僕の貯金が……！！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1F94 end

    def Function_23_1FFA(): pass

    label("Function_23_1FFA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32A, 1)
    Return()

    # Function_23_1FFA end

    def Function_24_2049(): pass

    label("Function_24_2049")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 0, -3000, 0)
    SetChrPos(0x102, 0, 0, -3000, 0)
    SetChrPos(0x103, 0, 0, -3000, 0)
    SetChrPos(0x104, 0, 0, -3000, 0)
    SetChrPos(0x151, 0, 0, -3000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, 1860, 0, 5910, 90)
    OP_68(-2760, 200, 3570, 0)
    MoveCamera(345, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(21520, 0)
    FadeToBright(1000, 0)
    OP_68(-2760, 200, 5070, 7000)
    BeginChrThread(0x101, 3, 0, 25)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 27)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 28)
    Sleep(1000)
    BeginChrThread(0x151, 3, 0, 29)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x151, 3)
    OP_6F(0x1)
    OP_0D()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0011F#12Pうーん……\x01",
            "しかし高そうな店だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#0304F#6Pま、いわゆる\x01",
            "高級ブランド店だな。\x02\x03",

            "#0300Fフォーマルな服から\x01",
            "キレイめのカジュアルまで\x01",
            "何でも揃ってるみたいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x151,
        (
            "#5704F#6Pフフ……\x01",
            "その分、いい値段だけどね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0059
    ChrTalk(
        0x102,
        (
            "#0100F#6P値段のことは気にしないで。\x02\x03",

            "それでロイド……\x01",
            "誰を連れていくか決まった？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22BE():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22BE)
    Sleep(100)

    def lambda_22CE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22CE)

    def lambda_22DB():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_22DB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x151, 1)
    Sleep(300)

    #C0060
    ChrTalk(
        0x101,
        "#0004F#11P──ああ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【エリィに同行してもらう】\x01",        # 0
            "【ティオに同行してもらう】\x01",        # 1
            "【ランディに同行してもらう】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_239F"),
        (1, "loc_2651"),
        (2, "loc_2980"),
        (SWITCH_DEFAULT, "loc_2E84"),
    )


    label("loc_239F")

    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 1)
    OP_29(0x47, 0x1, 0x6)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0061
    ChrTalk(
        0x101,
        (
            "#0000F#11Pエリィ──\x01",
            "一緒に来てくれるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x102,
        (
            "#0104F#6P……うん、分かったわ。\x02\x03",

            "#0102Fまあ一番、\x01",
            "さり気なく中に入れそうな\x01",
            "組み合わせかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#0002F#11Pああ、そう思ってさ。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x151,
        (
            "#5702F#6Pフフ、君たちの場合なら\x01",
            "普通にカップルとして装うのが\x01",
            "一番だろうね。\x02\x03",

            "#5703F行動的な資産家のお嬢様が\x01",
            "庶民出のボーイフレンドを連れて\x01",
            "話題のパーティに参加してみた……\x02\x03",

            "#5700Fそんな感じで行ってみたら？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0005F#11Pなるほど……\x01",
            "説得力はありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#0106F#6P……そこは怒っても\x01",
            "いいところだと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#0309F#6Pはは、いいからとっとと\x01",
            "コーディネイトしちまえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#0202F#12Pどう変身するのか……\x01",
            "ちょっと楽しみです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E84")

    label("loc_2651")

    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 2)
    OP_29(0x47, 0x1, 0x7)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0069
    ChrTalk(
        0x101,
        (
            "#0000F#5P──ティオ。\x01",
            "一緒に来てくれるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x103,
        (
            "#0205F#12P……いいんですか？\x02\x03",

            "#0206Fわたしは子供ではありませんが、\x01",
            "その、やっぱり少々\x01",
            "目立つのではないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#0004F#5Pああ、分かってる。\x02\x03",

            "#0000Fでも逆に、ティオが一緒なら\x01",
            "警察の人間には見えにくいんじゃ\x01",
            "ないかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        "#0205F#12Pあ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(300)

    #C0073
    ChrTalk(
        0x151,
        (
            "#5702F#6Pフフ、君くらいの子なら\x01",
            "去年も見かけたことはあるよ。\x02\x03",

            "#5704F辺境の小国あたりから来た\x01",
            "世慣れていない貴族の兄妹……\x02\x03",

            "#5700Fそんな設定でいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_286C():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_286C)

    def lambda_2879():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2879)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0074
    ChrTalk(
        0x101,
        "#0005F#11Pな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#0205F#11Pわたしとロイドさんが\x01",
            "兄妹ですか……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28E4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28E4)
    Sleep(50)

    def lambda_28F4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_28F4)
    Sleep(300)

    #C0076
    ChrTalk(
        0x102,
        (
            "#0109F#5Pふふ、全然似てないけど\x01",
            "それっぽくはなりそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#0302F#6Pそんじゃあ、とっとと\x01",
            "コーディネイトしちまうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E84")

    label("loc_2980")

    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA9, 3)
    OP_29(0x47, 0x1, 0x8)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0078
    ChrTalk(
        0x101,
        (
            "#0000F#5P──ランディ。\x01",
            "一緒に来てくれるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x104,
        (
            "#0305F#6P俺は構わねぇが……\x01",
            "男２人ってのは目立たねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#0006F#5Pああ、それは思ったけど……\x02",
    )

    CloseMessageWindow()

    def lambda_2A52():
        OP_93(0xFE, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A52)

    def lambda_2A5F():
        OP_93(0xFE, 0x10E, 0xC8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A5F)

    def lambda_2A6C():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A6C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)

    #C0081
    ChrTalk(
        0x101,
        (
            "#0008F#5P（マフィアもいる会場だろ？\x01",
            "  女の子連れってのもさ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        "#0300F#6P（ま、そりゃ確かにな。）\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0111F#5Pえっと……\x01",
            "何をヒソヒソ話してるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#0211F#12Pもしかして……\x01",
            "いつの間にかそんな関係に？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)

    #C0085
    ChrTalk(
        0x101,
        "#0012F#5P違います。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#0309F#6Pいや～、お前がその気なら\x01",
            "俺はいつでもウェルカムだけどな！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x151,
        (
            "#5702F#6Pフフ、男２人ってのも\x01",
            "見かけないわけじゃないよ。\x02\x03",

            "#5704F#6P真面目な良家の坊ちゃんを\x01",
            "悪い遊びに誘う年上の悪友……\x02\x03",

            "#5700Fそんな感じでどうだい？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C72():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C72)
    Sleep(50)

    def lambda_2C82():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C82)
    Sleep(50)

    def lambda_2C92():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C92)
    Sleep(50)

    def lambda_2CA2():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CA2)
    Sleep(300)

    #C0088
    ChrTalk(
        0x101,
        "#0005F#11Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        "#0302F#12Pハハ、確かにそれっぽいな。\x02",
    )

    CloseMessageWindow()

    def lambda_2CF8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CF8)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0090
    ChrTalk(
        0x102,
        (
            "#0105F#5Pとなると、ランディは\x01",
            "少し派手目にまとめたいわね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D4C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D4C)
    WaitChrThread(0x102, 1)
    Sleep(300)

    #C0091
    ChrTalk(
        0x102,
        (
            "#0109F#5P逆にロイドは、トラッドで\x01",
            "爽やかな感じがいいかしら……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DA4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DA4)
    WaitChrThread(0x103, 1)

    #C0092
    ChrTalk(
        0x103,
        (
            "#0202F#12Pせっかくですから\x01",
            "色々試してみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_2E21():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E21)
    Sleep(300)

    #C0093
    ChrTalk(
        0x101,
        "#0011F#5Pあの～……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0094
    ChrTalk(
        0x104,
        (
            "#0306F#6Pま、大人しく\x01",
            "着せ替え人形になっとこうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E84")

    SetCameraDistance(22020, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2EAB")
    Call(0, 30)
    Jump("loc_2EC8")

    label("loc_2EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2EBC")
    Call(0, 31)
    Jump("loc_2EC8")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2EC8")
    Call(0, 32)

    label("loc_2EC8")

    Return()

    # Function_24_2049 end

    def Function_25_2EC9(): pass

    label("Function_25_2EC9")


    def lambda_2ECE():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2ECE)

    def lambda_2EE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EE8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2F01():
        OP_95(0xFE, 0, 0, 2020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F01)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_25_2EC9 end

    def Function_26_2F22(): pass

    label("Function_26_2F22")


    def lambda_2F27():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F27)

    def lambda_2F41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F41)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2F5A():
        OP_95(0xFE, -790, 0, 650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F5A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_2F22 end

    def Function_27_2F7B(): pass

    label("Function_27_2F7B")


    def lambda_2F80():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F80)

    def lambda_2F9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F9A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2FB3():
        OP_95(0xFE, 870, 0, 920, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FB3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_27_2F7B end

    def Function_28_2FD4(): pass

    label("Function_28_2FD4")


    def lambda_2FD9():
        OP_95(0xFE, 0, 0, -1440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FD9)

    def lambda_2FF3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FF3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_300C():
        OP_95(0xFE, 0, 0, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_300C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_2FD4 end

    def Function_29_302D(): pass

    label("Function_29_302D")


    def lambda_3032():
        OP_95(0xFE, -460, 0, -1690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3032)

    def lambda_304C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_304C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3065():
        OP_95(0xFE, -1630, 0, -530, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3065)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_29_302D end

    def Function_30_3086(): pass

    label("Function_30_3086")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    SetChrChipPat(0x1, 0x1, 0x4D)
    LoadChrChipPat()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05300.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetChrPos(0x101, -7700, 0, 9950, 180)
    SetChrPos(0x102, -6350, 0, 9950, 180)
    SetChrPos(0x103, -6350, 0, 8150, 0)
    SetChrPos(0x104, -7000, 0, 6850, 0)
    SetChrPos(0x151, -7700, 0, 8150, 0)
    FadeToBright(1000, 0)
    OP_68(-7640, 900, 9240, 0)
    MoveCamera(311, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2500)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0095
    AnonymousTalk(
        0x102,
        "ふふっ、お待たせ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0096
    AnonymousTalk(
        0x101,
        "一応、着てみたけど……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0097
    ChrTalk(
        0x104,
        (
            "#0305F#6Pへえ……いいじゃん。\x02\x03",

            "#0309Fさすがに慣れてるだけあって\x01",
            "お嬢のドレス姿は言うことねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#0204F#6Pはい……とっても素敵です。\x02\x03",

            "#0202Fそれにロイドさんも、\x01",
            "中々お似合いだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#5005F#11Pそ、そうかな……？\x02\x03",

            "#5006Fさすがにエリィの横に立つと\x01",
            "釣り合っていない感じだけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    #C0100
    ChrTalk(
        0x102,
        (
            "#5304F#12Pふふっ、そんな事ないわ。\x02\x03",

            "#5302Fあなた、肩幅が結構あるから\x01",
            "スーツ姿も似合うみたいね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0101
    ChrTalk(
        0x101,
        (
            "#5004F#5Pはは、ありがとう。\x02\x03",

            "#5000F何とかエリィのボーイフレンドに\x01",
            "見えればいいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#5313F#12Pえ、ええ……\x01",
            "ちゃんと見えると思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x151,
        (
            "#5704F#6Pフフ、どうやら余計な\x01",
            "アドバイスは必要無さそうだね。\x02\x03",

            "#5702Fそうだ、ついでに\x01",
            "これも持って行くといい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3588():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3588)

    def lambda_3595():

        label("loc_3595")

        TurnDirection(0x102, 0x101, 200)
        Yield()
        Jump("loc_3595")

    QueueWorkItem2(0x102, 1, lambda_3595)

    def lambda_35A7():

        label("loc_35A7")

        TurnDirection(0x103, 0x101, 200)
        Yield()
        Jump("loc_35A7")

    QueueWorkItem2(0x103, 1, lambda_35A7)

    def lambda_35B9():

        label("loc_35B9")

        TurnDirection(0x104, 0x101, 200)
        Yield()
        Jump("loc_35B9")

    QueueWorkItem2(0x104, 1, lambda_35B9)

    def lambda_35CB():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_35CB)
    WaitChrThread(0x151, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)

    #C0104
    ChrTalk(
        0x101,
        "#5005F#11Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x151,
        (
            "#5703F#6P女性はドレスアップすると\x01",
            "かなり雰囲気が変わるけど……\x02\x03",

            "#5700F君の方は、フォーマルな格好でも\x01",
            "そこまで印象は変わらないからね。\x02\x03",

            "せめて会場にいる時くらい\x01",
            "付けた方がいいんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#5000F#11Pなるほど……助かるよ。\x02",
    )

    CloseMessageWindow()

    def lambda_36F7():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_36F7)
    WaitChrThread(0x151, 1)
    Sleep(300)
    Fade(1000)
    Sound(820, 0, 100, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0107
    AnonymousTalk(
        0x101,
        "……どうかな？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0108
    ChrTalk(
        0x151,
        "#5702F#6Pへえ……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        (
            "#5302F#12P驚いた……\x01",
            "結構、印象が変わるものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#0202F#6Pしかも意外と似合ってます。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x104,
        (
            "#0309F#6Pはは、これを期に\x01",
            "メガネ男子になったらどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#5106F#11Pいや、別に目は悪くないし。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    #C0113
    ChrTalk(
        0x101,
        (
            "#5004F#11P──よし。\x01",
            "これで準備は整ったな。\x02\x03",

            "#5000F後は《競売会》が\x01",
            "開場するのを待つだけだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_3086 end

    def Function_31_3949(): pass

    label("Function_31_3949")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    SetChrChipPat(0x2, 0x1, 0x4E)
    LoadChrChipPat()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05400.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetChrPos(0x101, -7700, 0, 9950, 180)
    SetChrPos(0x102, -6350, 0, 8150, 0)
    SetChrPos(0x103, -6350, 0, 9950, 180)
    SetChrPos(0x104, -7000, 0, 6850, 0)
    SetChrPos(0x151, -7700, 0, 8150, 0)
    FadeToBright(1000, 0)
    OP_68(-7640, 900, 9240, 0)
    MoveCamera(311, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2500)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0114
    AnonymousTalk(
        0x101,
        "うん、こんなもんか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0115
    AnonymousTalk(
        0x103,
        (
            "……似合っているかどうか\x01",
            "よく分かりませんけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0116
    ChrTalk(
        0x102,
        (
            "#0109F#6Pあら、いいじゃない！\x02\x03",

            "#0102Fロイドも似合っているけど\x01",
            "ティオちゃん、凄く可愛いわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#0304F#6Pま、ティオすけの私服姿は\x01",
            "殆んど見たことがないからな。\x02\x03",

            "#0300Fそういう格好は新鮮だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x103,
        "#5405F#11Pそ、そうでしょうか……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    #C0119
    ChrTalk(
        0x101,
        (
            "#5002F#5Pいや、ホント似合ってるよ。\x02\x03",

            "#5004Fこりゃあ、兄妹って言うには\x01",
            "かなり不釣合いかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x151,
        (
            "#5702F#6Pそれじゃあ、お嬢様に従う\x01",
            "若い執事って設定はどうだい？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x151, 400)

    #C0121
    ChrTalk(
        0x101,
        "#5000F#11Pそれだ……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    #C0122
    ChrTalk(
        0x103,
        (
            "#5403F#12P……いえ、兄妹で結構です。\x02\x03",

            "#5402Fお嬢様という柄でもありませんし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0123
    ChrTalk(
        0x101,
        "#5005F#5Pそ、そうか……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x151,
        (
            "#5704F#6Pフフ、色々と\x01",
            "こだわりがあるみたいだね。\x02\x03",

            "#5702Fまあいい、ついでに\x01",
            "これも持って行くといい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E70():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E70)

    def lambda_3E7D():

        label("loc_3E7D")

        TurnDirection(0x102, 0x101, 200)
        Yield()
        Jump("loc_3E7D")

    QueueWorkItem2(0x102, 1, lambda_3E7D)

    def lambda_3E8F():

        label("loc_3E8F")

        TurnDirection(0x103, 0x101, 200)
        Yield()
        Jump("loc_3E8F")

    QueueWorkItem2(0x103, 1, lambda_3E8F)

    def lambda_3EA1():

        label("loc_3EA1")

        TurnDirection(0x104, 0x101, 200)
        Yield()
        Jump("loc_3EA1")

    QueueWorkItem2(0x104, 1, lambda_3EA1)

    def lambda_3EB3():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3EB3)
    WaitChrThread(0x151, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)

    #C0125
    ChrTalk(
        0x101,
        "#5005F#11Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x151,
        (
            "#5703F#6P女の子はドレスアップすると\x01",
            "かなり雰囲気が変わるけど……\x02\x03",

            "#5700F君の方は、フォーマルな格好でも\x01",
            "そこまで印象は変わらないからね。\x02\x03",

            "せめて会場にいる時くらい\x01",
            "付けた方がいいんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#5000F#11Pなるほど……助かるよ。\x02",
    )

    CloseMessageWindow()

    def lambda_3FE1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3FE1)
    WaitChrThread(0x151, 1)
    Sleep(300)
    Fade(1000)
    Sound(820, 0, 100, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0128
    AnonymousTalk(
        0x101,
        "……どうかな？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0129
    ChrTalk(
        0x151,
        "#5702F#6Pへえ……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        (
            "#0102F#6P驚いた……\x01",
            "結構、印象が変わるものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        "#5402F#12Pしかも意外と似合ってます。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0309F#6Pはは、これを期に\x01",
            "メガネ男子になったらどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#5106F#11Pいや、別に目は悪くないし。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    #C0134
    ChrTalk(
        0x101,
        (
            "#5004F#11P──よし。\x01",
            "これで準備は整ったな。\x02\x03",

            "#5000F後は《競売会》が\x01",
            "開場するのを待つだけだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_3949 end

    def Function_32_4233(): pass

    label("Function_32_4233")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    SetChrChipPat(0x3, 0x1, 0x4F)
    LoadChrChipPat()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05600.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetChrPos(0x101, -7700, 0, 9950, 180)
    SetChrPos(0x102, -7000, 0, 6850, 0)
    SetChrPos(0x103, -6350, 0, 8150, 0)
    SetChrPos(0x104, -6350, 0, 9950, 180)
    SetChrPos(0x151, -7700, 0, 8150, 0)
    FadeToBright(1000, 0)
    OP_68(-7640, 900, 9240, 0)
    MoveCamera(311, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(23000, 2500)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0135
    AnonymousTalk(
        0x101,
        "──お待たせ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0136
    AnonymousTalk(
        0x104,
        "ま、こんなもんかね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0137
    ChrTalk(
        0x102,
        "#0105F#6Pあら……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        "#0201F#6P……ふむ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0139
    ChrTalk(
        0x101,
        (
            "#5011F#11Pえっと……\x01",
            "やっぱり似合ってないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        (
            "#5605F#11P俺的には結構、\x01",
            "イカスと思うんだけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            "#0102F#6Pううん、２人とも\x01",
            "とてもよく似合ってるわ。\x02\x03",

            "#0109Fふふっ、何だか本当に\x01",
            "さっきの設定通りな感じだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        (
            "#0204F#6P真面目な良家の坊ちゃんを\x01",
            "悪い遊びに誘う年上の悪友……\x02\x03",

            "#0202F確かにそのまんまですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    #C0143
    ChrTalk(
        0x101,
        "#5005F#5Pそ、そうかな……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    #C0144
    ChrTalk(
        0x104,
        (
            "#5609F#12Pハハ、そんじゃご期待通り、\x01",
            "悪い遊びを仕込んでやるかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#0107F#6Pそ、それはダメ！\x02\x03",

            "#0111Fただでさえこの人、ちょっと\x01",
            "タチが悪い所があるのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x103,
        (
            "#0211F#6P悪い遊びを覚えてしまったら\x01",
            "手が付けられなくなりそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x104,
        "#5603F#12Pなるほど……確かに危険だな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0148
    ChrTalk(
        0x101,
        (
            "#5011F#5P──ちょっと待て。\x02\x03",

            "#5013Fとんでもなく理不尽な評価を\x01",
            "されている気がするんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x151,
        (
            "#5709F#6Pフフ、君もずいぶん\x01",
            "愛されているみたいだねぇ。\x02\x03",

            "#5702Fそうそう、ついでに\x01",
            "これも持って行くといい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4865():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4865)

    def lambda_4872():

        label("loc_4872")

        TurnDirection(0x102, 0x101, 200)
        Yield()
        Jump("loc_4872")

    QueueWorkItem2(0x102, 1, lambda_4872)

    def lambda_4884():

        label("loc_4884")

        TurnDirection(0x103, 0x101, 200)
        Yield()
        Jump("loc_4884")

    QueueWorkItem2(0x103, 1, lambda_4884)

    def lambda_4896():

        label("loc_4896")

        TurnDirection(0x104, 0x101, 200)
        Yield()
        Jump("loc_4896")

    QueueWorkItem2(0x104, 1, lambda_4896)

    def lambda_48A8():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_48A8)
    WaitChrThread(0x151, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)

    #C0150
    ChrTalk(
        0x101,
        "#5005F#11Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x151,
        (
            "#5703F#6Pランディは派手目にまとめたから\x01",
            "かなり印象が変わってるけど……\x02\x03",

            "#5700F君の方は、フォーマルな格好でも\x01",
            "そこまで印象は変わらないからね。\x02\x03",

            "せめて会場にいる時くらい\x01",
            "付けた方がいいんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#5000F#11Pなるほど……助かるよ。\x02",
    )

    CloseMessageWindow()

    def lambda_49DC():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_49DC)
    WaitChrThread(0x151, 1)
    Sleep(300)
    Fade(1000)
    Sound(820, 0, 100, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0153
    AnonymousTalk(
        0x101,
        "……どうかな？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0154
    ChrTalk(
        0x151,
        "#5702F#6Pへえ……\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#0102F#6P驚いた……\x01",
            "結構、印象が変わるものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        "#0202F#6Pしかも意外と似合ってます。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#5609F#12Pはは、これを期に\x01",
            "メガネ男子になったらどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#5106F#5Pいや、別に目は悪くないし。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    #C0159
    ChrTalk(
        0x101,
        (
            "#5004F#11P──よし。\x01",
            "これで準備は整ったな。\x02\x03",

            "#5000F後は《競売会》が\x01",
            "開場するのを待つだけだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(2000)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_4233 end

    def Function_33_4C2D(): pass

    label("Function_33_4C2D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-102630, 1400, 14570, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21880, 0)
    SetChrPos(0x101, -101580, 0, 14400, 270)
    SetChrPos(0x102, -101560, 0, 15620, 225)
    SetChrPos(0x103, -101840, 0, 13530, 315)
    SetChrPos(0x104, -100390, 0, 14710, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4CC0")
    SetChrPos(0x151, -100780, 0, 13600, 270)

    label("loc_4CC0")

    StopEffect(0x0, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34E, 1)

    #C0161
    ChrTalk(
        0x101,
        "#11P#0005Fこんな所に指輪が……？\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x103,
        (
            "#6P#0200Fトマさんの言っていた\x01",
            "婚約指輪の可能性があります。\x02\x03",

            "後でホテルの部屋を訪ねて\x01",
            "確認してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x5)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, -101580, 0, 14400, 270)
    ClearChrFlags(0xA, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_4C2D end

    SaveToFile()

Try(main)
