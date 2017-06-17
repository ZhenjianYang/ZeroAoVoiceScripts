from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ビクセン町長",           # 1
        "ビクセン町長",           # 2
        "アンナ夫人",             # 3
        "アンナ夫人",             # 4
        "鉱員マルロ",             # 5
        "鉱員マックス",           # 6
        "鉱員マックス",           # 7
        "ルリエダ",               # 8
        "ミランダ",               # 9
        "ビルマ婆さん",           # 10
        "鉱山長ホフマン",         # 11
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
        "Function_4_71B",          # 04, 4
        "Function_5_11CD",         # 05, 5
        "Function_6_1BC2",         # 06, 6
        "Function_7_2038",         # 07, 7
        "Function_8_24F4",         # 08, 8
        "Function_9_2915",         # 09, 9
        "Function_10_337F",        # 0A, 10
        "Function_11_3F9C",        # 0B, 11
        "Function_12_4112",        # 0C, 12
        "Function_13_4D5C",        # 0D, 13
        "Function_14_51E6",        # 0E, 14
        "Function_15_65AD",        # 0F, 15
        "Function_16_73E9",        # 10, 16
        "Function_17_7DBE",        # 11, 17
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68C")

    #C0001
    ChrTalk(
        0x8,
        "よく危険な廃坑へと挑んでくれたよ。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "君たちには何かと世話になるな。\x01",
            "またよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_717")

    label("loc_68C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_714")

    #C0003
    ChrTalk(
        0x8,
        (
            "廃坑へは、鉱山の奥にある扉で\x01",
            "その鍵を使えば入れる。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "魔獣退治の件、よろしく頼んだよ。\x01",
            "充分気をつけてな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_717")

    label("loc_714")

    Call(0, 16)

    label("loc_717")

    TalkEnd(0xFE)
    Return()

    # Function_3_615 end

    def Function_4_71B(): pass

    label("Function_4_71B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7AF")
    Jump("loc_7F9")

    label("loc_7AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F9")

    label("loc_7CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F9")

    label("loc_7EF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_82C")
    Jump("loc_11C5")

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_891")

    #C0005
    ChrTalk(
        0xFE,
        (
            "ガンツのこと、\x01",
            "どうか宜しくお願いする。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "何か分かったら私の家に連絡してくれ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11C5")

    label("loc_891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_931")
    SetChrSubChip(0x9, 0x1)

    #C0007
    ChrTalk(
        0xFE,
        "もう２週間も経つか……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "おかしなトラブルに\x01",
            "巻き込まれてなければいいのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "彼のギャンブル癖を考えると\x01",
            "さすがに心配だな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Jump("loc_11C5")

    label("loc_931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A36")

    #C0010
    ChrTalk(
        0xFE,
        (
            "昨日、帝国の商人のフリージア君が\x01",
            "七耀石の結晶を譲って欲しいと\x01",
            "再び交渉に来てね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "かなり以前から打診されていたのだが、\x01",
            "結局あの熱意に負けて売り渡したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "いやはや、あの粘り強さ……\x01",
            "流石、大商人の娘というだけはあるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AAA")

    label("loc_A36")


    #C0013
    ChrTalk(
        0xFE,
        (
            "フリージア君は\x01",
            "なかなか面白い商人だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "いやはや、あの粘り強さ……\x01",
            "流石、大商人の娘というだけはあるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAA")

    Jump("loc_11C5")

    label("loc_AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B65")

    #C0015
    ChrTalk(
        0xFE,
        (
            "今晩はフリージア君が\x01",
            "七耀石の取り引き交渉に\x01",
            "来る予定なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "彼女はなかなか熱意ある\x01",
            "商人のようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "今日の話次第では\x01",
            "譲ってやってもいいかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C5")

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BD7")

    #C0018
    ChrTalk(
        0xFE,
        (
            "町にちらほらと\x01",
            "観光客が訪れているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "鉱山に入らないよう、\x01",
            "私が注意しておかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C5")

    label("loc_BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9D")

    #C0020
    ChrTalk(
        0xFE,
        (
            "昨日は、記念祭初日を祝って\x01",
            "宴会を催したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "ふふ、若い鉱員たちの食いっぷりは\x01",
            "なかなか壮観だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "皆楽しんでもらえたようだから\x01",
            "大成功だったといえるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D24")

    label("loc_C9D")


    #C0023
    ChrTalk(
        0xFE,
        (
            "若い鉱員たちは\x01",
            "クロスベル市のほうに\x01",
            "遊びに行っているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "日頃の疲れもたまっているだろう、\x01",
            "存分に楽しんできてほしいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D24")

    Jump("loc_11C5")

    label("loc_D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_ECE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2A")

    #C0025
    ChrTalk(
        0xFE,
        (
            "最近町で取引をさせてもらっている\x01",
            "商人の……フリージア君だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "あの押しの強さと心意気は買うが、\x01",
            "商人としてはまだまだといった感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "彼女はどうやら七耀石の結晶を\x01",
            "狙っているようだが……\x01",
            "ふむ、どうしたものかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EC9")

    label("loc_E2A")


    #C0028
    ChrTalk(
        0xFE,
        (
            "フリージア君はかなり長い間\x01",
            "こちらに滞在するつもりのようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "見たところ若い娘なのに\x01",
            "懐はなかなか豊からしい。\x01",
            "そこは、さすが商人と言ったところか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC9")

    Jump("loc_11C5")

    label("loc_ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1050")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCB")

    #C0030
    ChrTalk(
        0xFE,
        (
            "《特務支援課》の諸君……\x01",
            "件の事件では本当に助けられた。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "まさか、一連の事件が\x01",
            "人間の手によるものだったとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "危うく、マフィアの狡猾な手口に\x01",
            "嵌められるところだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "助けてもらって\x01",
            "本当に感謝しているよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_104B")

    label("loc_FCB")


    #C0034
    ChrTalk(
        0xFE,
        (
            "魔獣被害で出ていた発掘計画の遅れも\x01",
            "もうすぐ取り戻せる。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "鉱員たちには申し訳ないが、\x01",
            "今しばらく頑張ってもらわないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104B")

    Jump("loc_11C5")

    label("loc_1050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_105E")
    Jump("loc_11C5")

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_11BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1143")

    #C0036
    ChrTalk(
        0xFE,
        (
            "……警備隊も頼れないし、\x01",
            "多忙な遊撃士に\x01",
            "警備を頼むのは忍びない。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "ましてや、さっきの連中に関わるのは\x01",
            "気が進まなかったところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "うむ……『解決できる』と言った\x01",
            "君たちを信じてみるとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11B7")

    label("loc_1143")


    #C0039
    ChrTalk(
        0xFE,
        (
            "《特務支援課》か……\x01",
            "聞きなれない名前だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "うむ……『解決できる』と言った\x01",
            "君たちを信じてみるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B7")

    Jump("loc_11C5")

    label("loc_11BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_11C5")

    label("loc_11C5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_71B end

    def Function_5_11CD(): pass

    label("Function_5_11CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1234")

    #C0041
    ChrTalk(
        0xFE,
        (
            "あなたたちのおかげで\x01",
            "助かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "本当にありがとうございます。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_1234")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12BE")

    #C0043
    ChrTalk(
        0xFE,
        (
            "廃坑は長年進められた\x01",
            "発掘作業のために、\x01",
            "かなり深くまで続いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "どうか怪我など\x01",
            "なさらないで下さいね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_12BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_12CC")
    Jump("loc_1BBE")

    label("loc_12CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1391")

    #C0045
    ChrTalk(
        0xFE,
        (
            "ビクセンはガンツさんに会いに、\x01",
            "クロスベル市の方へ向かいましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "……なんでも、ガンツさんの様子が\x01",
            "おかしかったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "一体何があったんでしょう……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_140F")

    label("loc_1391")


    #C0048
    ChrTalk(
        0xFE,
        (
            "……ともあれ、ガンツさんの無事が\x01",
            "確認できてほっとしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "町の人々に伝えましたら\x01",
            "皆さんも随分安心されたようです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140F")

    Jump("loc_1BBE")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_14A2")

    #C0050
    ChrTalk(
        0xFE,
        (
            "彼になにがあったかは存じませんが……\x01",
            "できれば早く見つけてあげてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "他の鉱員たちも、\x01",
            "随分心配していますから……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBE")

    label("loc_14A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_14B0")
    Jump("loc_1BBE")

    label("loc_14B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B2")

    #C0052
    ChrTalk(
        0xFE,
        (
            "フリージアさんは\x01",
            "帝国の人と聞いて、\x01",
            "私は少し尻込みしていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "思った以上に和やかな\x01",
            "いい娘さんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "帝国というと軍人さんのような\x01",
            "威圧的なイメージがあったんですが……\x01",
            "案外、ああいう方も多いのかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_164F")

    label("loc_15B2")


    #C0055
    ChrTalk(
        0xFE,
        (
            "帝国というと軍人さんのような\x01",
            "威圧的なイメージがあったんですが……\x01",
            "和やかな方も多いのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "偏見の目で見ていた自分が\x01",
            "少し恥ずかしいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164F")

    Jump("loc_1BBE")

    label("loc_1654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_16C6")

    #C0057
    ChrTalk(
        0xFE,
        (
            "主人はあなた達のことも、\x01",
            "応援しているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "頑張っている若者に\x01",
            "弱いんでしょうね、きっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBE")

    label("loc_16C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_175A")

    #C0059
    ChrTalk(
        0xFE,
        (
            "この町に観光に来る人なんて、\x01",
            "例年はそこまでいなかったんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "創立７０周年とあって、\x01",
            "多くの人が訪れているのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBE")

    label("loc_175A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_17F5")

    #C0061
    ChrTalk(
        0xFE,
        (
            "夫も日々の発掘計画を立てたりで\x01",
            "鉱員に負けず劣らず\x01",
            "苦労しているでしょうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "せめて記念祭のうちは、\x01",
            "私が夫を労ってあげなくてはね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBE")

    label("loc_17F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_19EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1967")

    #C0063
    ChrTalk(
        0xFE,
        (
            "土地柄、このあたりでは\x01",
            "食材などがなかなか揃いません。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "導力バスで何度も買出しにでるのは\x01",
            "とても大変だったのですが……\x01",
            "最近はその苦労も減りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "ハロルド・ヘイワースという\x01",
            "クロスベル市の貿易商さんが\x01",
            "定期的に作物を卸してくれるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "わざわざアルモリカ村の方から\x01",
            "美味しい作物を届けて下さるので、\x01",
            "大変助かっているんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19E7")

    label("loc_1967")


    #C0067
    ChrTalk(
        0xFE,
        (
            "ハロルドさんは自治州内の\x01",
            "需要をよく分かっていらっしゃるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "クロスベルの商人さんとしては\x01",
            "とても堅実で好感が持てます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E7")

    Jump("loc_1BBE")

    label("loc_19EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A96")

    #C0069
    ChrTalk(
        0xFE,
        (
            "夫は、鉱山の責任者の\x01",
            "ホフマン鉱山長と一緒に\x01",
            "日々の発掘計画を立てているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "政府に取り決められた発掘量を\x01",
            "超えないようにしないと\x01",
            "いけませんからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBE")

    label("loc_1A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1AA4")
    Jump("loc_1BBE")

    label("loc_1AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B75")

    #C0071
    ChrTalk(
        0xFE,
        (
            "それにしても、\x01",
            "さっきの黒服の人達……\x01",
            "どうにも信用できないわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "警備隊も早々に引き上げる件を\x01",
            "わざわざ引き受けようなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "一体どこから\x01",
            "そんな自信が来るのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BB0")

    label("loc_1B75")


    #C0074
    ChrTalk(
        0xFE,
        (
            "さっきの黒服の人達……\x01",
            "一体どういうつもりなのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB0")

    Jump("loc_1BBE")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1BBE")

    label("loc_1BBE")

    TalkEnd(0xFE)
    Return()

    # Function_5_11CD end

    def Function_6_1BC2(): pass

    label("Function_6_1BC2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C56")
    Jump("loc_1CA0")

    label("loc_1C56")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C76")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CA0")

    label("loc_1C76")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C96")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CA0")

    label("loc_1C96")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CA0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1EA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5E")

    #C0075
    ChrTalk(
        0xFE,
        (
            "ガンツさんのことについては、\x01",
            "主人から通信で一通り聞きました。\x01",
            "今朝、いなくなってしまった事も……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "こんなこと、町の人達に伝えるには\x01",
            "ショックが大きすぎるでしょう……\x01",
            "私にはどうしようもありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "とにかく今は、\x01",
            "ガンツさんが無事に戻ってくるのを\x01",
            "女神さまにお祈りしなければ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E56")

    #C0078
    ChrTalk(
        0x10A,
        (
            "#0600Fこうしてはいられんな……\x01",
            "はやくルバーチェのアジトを\x01",
            "調べに戻るぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E56")

    SetScenarioFlags(0x0, 1)
    Jump("loc_1EA4")

    label("loc_1E5E")


    #C0079
    ChrTalk(
        0xFE,
        (
            "ああ、女神様……\x01",
            "どうかガンツさんを\x01",
            "無事に帰してくださいまし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA4")

    Jump("loc_2030")

    label("loc_1EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1EB7")
    Jump("loc_2030")

    label("loc_1EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1EC5")
    Jump("loc_2030")

    label("loc_1EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1ED3")
    Jump("loc_2030")

    label("loc_1ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F65")
    SetChrSubChip(0xB, 0x2)

    #C0080
    ChrTalk(
        0xFE,
        (
            "そうねぇ……\x01",
            "早いうちに手を打ったほうが\x01",
            "いいと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "危険な目にあっていたりしたら\x01",
            "一刻を争うもの。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FB2")

    label("loc_1F65")


    #C0082
    ChrTalk(
        0xFE,
        (
            "おや、あなた達……\x01",
            "その節はどうも。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "ゆっくりしていってくださいね。\x02",
    )

    CloseMessageWindow()

    label("loc_1FB2")

    Jump("loc_2030")

    label("loc_1FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FC5")
    Jump("loc_2030")

    label("loc_1FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1FD3")
    Jump("loc_2030")

    label("loc_1FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1FE1")
    Jump("loc_2030")

    label("loc_1FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FEF")
    Jump("loc_2030")

    label("loc_1FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1FFD")
    Jump("loc_2030")

    label("loc_1FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_200B")
    Jump("loc_2030")

    label("loc_200B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_2019")
    Jump("loc_2030")

    label("loc_2019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2027")
    Jump("loc_2030")

    label("loc_2027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2030")

    label("loc_2030")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1BC2 end

    def Function_7_2038(): pass

    label("Function_7_2038")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2049")
    Jump("loc_24F0")

    label("loc_2049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2057")
    Jump("loc_24F0")

    label("loc_2057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_2065")
    Jump("loc_24F0")

    label("loc_2065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2073")
    Jump("loc_24F0")

    label("loc_2073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2081")
    Jump("loc_24F0")

    label("loc_2081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_208F")
    Jump("loc_24F0")

    label("loc_208F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_209D")
    Jump("loc_24F0")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20AB")
    Jump("loc_24F0")

    label("loc_20AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_20B9")
    Jump("loc_24F0")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_20C7")
    Jump("loc_24F0")

    label("loc_20C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_20D5")
    Jump("loc_24F0")

    label("loc_20D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_20E3")
    Jump("loc_24F0")

    label("loc_20E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_21C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218C")

    #C0084
    ChrTalk(
        0xFE,
        (
            "あー……\x01",
            "そろそろ仕事が終わる頃か。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "……くそっ。\x01",
            "魔獣に襲われたりなんか\x01",
            "しなけりゃなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "こんな生活じゃ\x01",
            "体がなまっちまうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_21BE")

    label("loc_218C")


    #C0087
    ChrTalk(
        0xFE,
        (
            "あー……\x01",
            "こんな生活じゃ\x01",
            "体がなまっちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BE")

    Jump("loc_24F0")

    label("loc_21C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_END)), "loc_2332")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E5")
    SetScenarioFlags(0x67, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22AA")

    #C0088
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "後輩に情けねぇ姿を\x01",
            "見せちまったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "それもこれも……\x01",
            "あの得体の知れない\x01",
            "オオカミ野郎のせいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "今度また現れやがったら\x01",
            "スコップでブチのめしてやるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_232D")

    label("loc_22AA")


    #C0091
    ChrTalk(
        0xFE,
        (
            "あの得体の知れない\x01",
            "黒いオオカミのせいで、\x01",
            "しばらく仕事ができねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "今度また現れやがったら\x01",
            "スコップでブチのめしてやるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232D")

    Jump("loc_24F0")

    label("loc_2332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_24F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2354")
    SetScenarioFlags(0x67, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2354")

    TurnDirection(0xC, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245E")

    #C0093
    ChrTalk(
        0xC,
        "マックスさん、具合はどうっすか？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xC,
        "魔獣に足を噛まれたそうですけど……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xD,
        (
            "ああ、ケガ自体は\x01",
            "大したことねぇんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xD,
        (
            "鉱山長に\x01",
            "しばらく鉱山に入るなって\x01",
            "言われちまってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xC,
        (
            "そうですか……\x01",
            "まぁ、無理はしないほうが\x01",
            "いいですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24F0")

    label("loc_245E")


    #C0098
    ChrTalk(
        0xD,
        (
            "かーっ、情けねぇ。\x01",
            "こんな怪我くらい\x01",
            "どうってことねぇんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xC,
        (
            "まぁ、休んでたほうがいいですよ。\x01",
            "動き回ってちゃ\x01",
            "治りも悪いでしょうし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F0")

    TalkEnd(0xFE)
    Return()

    # Function_7_2038 end

    def Function_8_24F4(): pass

    label("Function_8_24F4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2588")
    Jump("loc_25D2")

    label("loc_2588")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25A8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25D2")

    label("loc_25A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25C8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25D2")

    label("loc_25C8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25D2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267C")

    #C0100
    ChrTalk(
        0xFE,
        "今日で記念祭もおわりか……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "鉱山長と町長とロージーを\x01",
            "《赤レンガ亭》に呼んで\x01",
            "宴会でもするかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26E9")

    label("loc_267C")


    #C0102
    ChrTalk(
        0xFE,
        (
            "また皆を\x01",
            "《赤レンガ亭》に呼んで\x01",
            "宴会でもするかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "町長にもおごってもらった\x01",
            "お返しをしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E9")

    Jump("loc_290D")

    label("loc_26EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2775")

    #C0104
    ChrTalk(
        0xFE,
        (
            "家庭があるってのは\x01",
            "本当にいいことだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "俺が鉱員の仕事を\x01",
            "頑張ってられるのは、\x01",
            "支えてくれる奥さんがいるからさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290D")

    label("loc_2775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2835")

    #C0106
    ChrTalk(
        0xFE,
        (
            "どんだけキツかろうが、\x01",
            "俺は鉱員の仕事が好きだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "発掘計画は鉱山長が立てるし\x01",
            "あとは実現する筋力があればいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "考えるのが苦手な俺にとっちゃ\x01",
            "天職だぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28AC")

    label("loc_2835")


    #C0109
    ChrTalk(
        0xFE,
        (
            "この仕事はとにかく、\x01",
            "体力がありさえすれば\x01",
            "後はどうにでもなる。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "考えるのが苦手な俺にとっちゃ\x01",
            "鉱員は天職だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28AC")

    Jump("loc_290D")

    label("loc_28B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_290D")

    #C0111
    ChrTalk(
        0xFE,
        "昨日は楽しかったなぁ。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "何杯飲んだか覚えてないくらい\x01",
            "酔っ払っちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_24F4 end

    def Function_9_2915(): pass

    label("Function_9_2915")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_29C6")

    #C0113
    ChrTalk(
        0xFE,
        (
            "旦那のマックスは最近、\x01",
            "今まで以上に張り切って\x01",
            "仕事をしているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "やる気があるのはいいことだわ。\x01",
            "ケガにだけは気を付けて\x01",
            "しっかり働いてきて欲しいわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337B")

    label("loc_29C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2A68")

    #C0115
    ChrTalk(
        0xFE,
        (
            "昨日まではたまに遺跡の方から\x01",
            "鐘のような音が\x01",
            "聞こえてきてたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "今日になったら\x01",
            "とんと聞こえなくなったわ。\x01",
            "結局なんだったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337B")

    label("loc_2A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_2AF4")

    #C0117
    ChrTalk(
        0xFE,
        (
            "さぁ、そろそろ男どもが\x01",
            "鉱山から降りてくる頃だわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "一日の疲れをしっかり癒して、\x01",
            "また明日からがんばって貰わなきゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337B")

    label("loc_2AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2B7E")

    #C0119
    ChrTalk(
        0xFE,
        (
            "最近はロージーさんがよく働くって\x01",
            "夫が嬉しそうに話すのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "ロージーさんもようやく\x01",
            "鉱員の自覚ができてきたのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337B")

    label("loc_2B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2C48")

    #C0121
    ChrTalk(
        0xFE,
        (
            "今日もうちの夫は\x01",
            "鉱山でがんばってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "クロスベルの鉱山を掘ることは\x01",
            "マインツだけでなく\x01",
            "クロスベル全体にとっても重要なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "あたしゃ、\x01",
            "そんな仕事をしてる夫を誇りに思うよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337B")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2CCF")

    #C0124
    ChrTalk(
        0xFE,
        (
            "長い休暇を終えて、\x01",
            "明日からまた旦那が\x01",
            "鉱山に働きに出るよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "よし、明日の弁当は思いっきり\x01",
            "豪華にいくとするかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337B")

    label("loc_2CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D58")

    #C0126
    ChrTalk(
        0xFE,
        (
            "マックスがこんなに\x01",
            "家でゆっくりしているのが\x01",
            "私にはうれしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "どれ、お茶でも淹れて\x01",
            "ティータイムでもしようかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337B")

    label("loc_2D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2DFA")

    #C0128
    ChrTalk(
        0xFE,
        (
            "旦那のマックスは\x01",
            "若手の鉱員の中じゃ\x01",
            "一番仕事が出来るって評判なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "ま、ちょっとバカなのが\x01",
            "たまにキズだけどね。\x01",
            "そこがまたかわいいのさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337B")

    label("loc_2DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2E7B")

    #C0130
    ChrTalk(
        0xFE,
        (
            "せっかくの記念祭、\x01",
            "飲むのはいいけど\x01",
            "ほどほどにしてほしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "私にはマックスの体が\x01",
            "一番大事なんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337B")

    label("loc_2E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F60")

    #C0132
    ChrTalk(
        0xFE,
        (
            "あたしゃ、毎朝早起きして\x01",
            "旦那に弁当こさえるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "力仕事で腹が減るだろうから\x01",
            "これでもかってくらい\x01",
            "弁当箱を満杯にしてやってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "帰ってきたとき弁当箱が空だと\x01",
            "なんだか嬉しい気持ちになるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FEF")

    label("loc_2F60")


    #C0135
    ChrTalk(
        0xFE,
        (
            "早起きして目一杯に詰め込んだ\x01",
            "弁当箱を持たせるのが\x01",
            "あたしの毎朝の日課さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "帰ってきたとき弁当箱が空だと\x01",
            "なんだか嬉しい気持ちになるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEF")

    Jump("loc_337B")

    label("loc_2FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_30EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3083")

    #C0137
    ChrTalk(
        0xFE,
        (
            "魔獣に襲われて怪我してた旦那も\x01",
            "この間やっとこさ治ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "休んでた分を取り戻さなきゃって\x01",
            "意気込んでるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_30E6")

    label("loc_3083")


    #C0139
    ChrTalk(
        0xFE,
        (
            "魔獣に襲われて怪我してた旦那も\x01",
            "この間やっとこさ治ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "今日も元気に鉱山に入ってるよ。\x02",
    )

    CloseMessageWindow()

    label("loc_30E6")

    Jump("loc_337B")

    label("loc_30EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_30F9")
    Jump("loc_337B")

    label("loc_30F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319B")

    #C0141
    ChrTalk(
        0xFE,
        (
            "ああもう、うるっさいんだから。\x01",
            "大の男がうだうだうだうだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "怪我したものは\x01",
            "しょうがないんだから、\x01",
            "大人しく寝てなさいっての。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_322C")

    label("loc_319B")


    #C0143
    ChrTalk(
        0xFE,
        (
            "大の男がうだうだうだうだ……\x01",
            "女々しいったらありゃしない。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "その程度の怪我で済んで\x01",
            "休みまで貰ってるんだから、\x01",
            "大人しく寝てなさいっての。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_322C")

    Jump("loc_337B")

    label("loc_3231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_337B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3253")
    SetScenarioFlags(0x67, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32FD")

    #C0145
    ChrTalk(
        0xFE,
        (
            "うちの旦那、\x01",
            "この間の仕事帰りに\x01",
            "魔獣に襲われちまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "ま、怪我は大したことないし……\x01",
            "休みがもらえてラッキー☆\x01",
            "くらいに思っておけばいいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_337B")

    label("loc_32FD")


    #C0147
    ChrTalk(
        0xFE,
        (
            "夜、突然魔獣に襲われた……なんて\x01",
            "誰にだって防ぎようがないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "休みがもらえてラッキー☆\x01",
            "くらいに思っておけばいいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_337B")

    TalkEnd(0xFE)
    Return()

    # Function_9_2915 end

    def Function_10_337F(): pass

    label("Function_10_337F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3431")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339E")
    Call(0, 11)
    Jump("loc_342C")

    label("loc_339E")


    #C0149
    ChrTalk(
        0xFE,
        (
            "うちの旦那、昨日の夜に町長夫人から\x01",
            "なにか相談されてたみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "あの深刻そうな顔を見ると\x01",
            "あまりいいニュースじゃなさそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342C")

    Jump("loc_3F98")

    label("loc_3431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34DD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344D")
    Call(0, 11)
    Jump("loc_34D8")

    label("loc_344D")


    #C0151
    ChrTalk(
        0xFE,
        "はぁよかった、ガンツさんがみつかって。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "ほら、遺跡に幽霊が出るなんて\x01",
            "噂もあったでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "神隠しにでもあったのかと思ったわ。\x02",
    )

    CloseMessageWindow()

    label("loc_34D8")

    Jump("loc_3F98")

    label("loc_34DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3576")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F9")
    Call(0, 11)
    Jump("loc_3571")

    label("loc_34F9")


    #C0154
    ChrTalk(
        0xFE,
        (
            "鉱員さんは、この町を支える\x01",
            "重要な役割を担っているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "だからビクセン町長は\x01",
            "鉱員さんを特に大事にしているのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3571")

    Jump("loc_3F98")

    label("loc_3576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_35F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3592")
    Call(0, 11)
    Jump("loc_35F4")

    label("loc_3592")


    #C0156
    ChrTalk(
        0xFE,
        (
            "さっき、旦那にお弁当を\x01",
            "差し入れしてあげたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "あんなに喜んでもらえると\x01",
            "私も嬉しいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F4")

    Jump("loc_3F98")

    label("loc_35F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3692")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3615")
    Call(0, 11)
    Jump("loc_368D")

    label("loc_3615")


    #C0158
    ChrTalk(
        0xFE,
        "ホフマン、今日もがんばってるかしら……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "忙しくてお昼がまだだろうし、\x01",
            "あとでお弁当をもっていって\x01",
            "あげないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368D")

    Jump("loc_3F98")

    label("loc_3692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_380D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3791")

    #C0160
    ChrTalk(
        0xFE,
        (
            "アレク、鉱員たちが\x01",
            "必ずしも楽しくやってるわけじゃない\x01",
            "って気づいちゃったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "正直、私としては\x01",
            "危険な鉱員の仕事より\x01",
            "安全な仕事をして欲しいと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "帰ってくるまで\x01",
            "ずっと心配してるなんて\x01",
            "夫一人で沢山だもの……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3808")

    label("loc_3791")


    #C0163
    ChrTalk(
        0xFE,
        (
            "息子には、安全な仕事を\x01",
            "目指して欲しいと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "帰ってくるまで\x01",
            "ずっと心配してるなんて\x01",
            "夫一人で沢山だもの……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3808")

    Jump("loc_3F98")

    label("loc_380D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_386A")

    #C0165
    ChrTalk(
        0xFE,
        (
            "アレク、昨日からなんだか\x01",
            "元気が無いのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "何かあったのかしら……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F98")

    label("loc_386A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3949")

    #C0167
    ChrTalk(
        0xFE,
        (
            "夫のホフマンは鉱山長として\x01",
            "鉱員たちを纏めてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "どうやらアレクは夫の影響で\x01",
            "『鉱員になりたい』なんて\x01",
            "言ってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "父親に憧れてくれるのは\x01",
            "私としても嬉しいけど、\x01",
            "危険な仕事だから複雑だな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F98")

    label("loc_3949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_39B7")

    #C0170
    ChrTalk(
        0xFE,
        (
            "ホフマン……\x01",
            "昨日の宴会の酒が\x01",
            "体に残ってないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        "わが夫ながら恐ろしいタフさね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F98")

    label("loc_39B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB7")

    #C0172
    ChrTalk(
        0xFE,
        (
            "まったくアレクったら……\x01",
            "昨日は案の定、\x01",
            "傷だらけで帰ってきたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "擦りむいたくらいでよかったものの、\x01",
            "下手したらガケの下まで\x01",
            "真っ逆さまだったかも知れないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "これだから男ってのは……\x01",
            "心配する身にもなって欲しいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B3B")

    label("loc_3AB7")


    #C0175
    ChrTalk(
        0xFE,
        (
            "よく足元を見ないで走り回るから\x01",
            "あんな転び方するのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "アレクといい、鉱員の旦那といい……\x01",
            "心配する身にもなって欲しいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B3B")

    Jump("loc_3F98")

    label("loc_3B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3C95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C26")

    #C0177
    ChrTalk(
        0xFE,
        (
            "アレクったら、\x01",
            "今日も町を走り回ってるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "町の中には重い機材も置いてるし\x01",
            "ガケもあるから\x01",
            "気をつけて欲しいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "一度ちゃんと注意しないと、\x01",
            "いつか大怪我して\x01",
            "帰ってきちゃうわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3C90")

    label("loc_3C26")


    #C0180
    ChrTalk(
        0xFE,
        (
            "アレクには一度、\x01",
            "注意した方がいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "大怪我して帰ってこられたら\x01",
            "後の祭りだもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C90")

    Jump("loc_3F98")

    label("loc_3C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3CA3")
    Jump("loc_3F98")

    label("loc_3CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3E1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9E")

    #C0182
    ChrTalk(
        0xFE,
        (
            "昔から七耀石の鉱山は\x01",
            "危険な場所として知られているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "七耀石に引き寄せられた魔獣が\x01",
            "鉱山内に巣を作っちゃうのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "今は導力灯のお陰で\x01",
            "安全になってきたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "旦那をそんな所に送り出すのは\x01",
            "今でも怖いのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E18")

    label("loc_3D9E")


    #C0186
    ChrTalk(
        0xFE,
        (
            "さて、日も暮れてきたし……\x01",
            "アレクを家に帰らせないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "マックスさんみたいな目に\x01",
            "あわせるわけにはいかないもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E18")

    Jump("loc_3F98")

    label("loc_3E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3F98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3F")
    SetScenarioFlags(0x67, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F18")

    #C0188
    ChrTalk(
        0xFE,
        (
            "子供が\x01",
            "いつも危険な場所に入りたがって\x01",
            "困っちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "また鉱山に入って\x01",
            "迷惑かけてなきゃいいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "近頃、町の中に魔獣が出るとかで\x01",
            "なんだか物騒だし、\x01",
            "もっと気をつけてほしいんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F98")

    label("loc_3F18")


    #C0191
    ChrTalk(
        0xFE,
        (
            "アレクときたら\x01",
            "いつも危険な場所に入りたがって\x01",
            "困っちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "男の子ってのは、\x01",
            "なんであんな危ない場所が\x01",
            "好きなのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F98")

    TalkEnd(0xFE)
    Return()

    # Function_10_337F end

    def Function_11_3F9C(): pass

    label("Function_11_3F9C")


    #C0193
    ChrTalk(
        0xFE,
        (
            "最近また鉱山のほうが\x01",
            "忙しくなってるみたいねぇ。\x01",
            "ウチの旦那が体を壊さなきゃいいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "……まぁ、旦那はいつだって\x01",
            "私の真心のこもったお弁当を\x01",
            "食べてるから大丈夫よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "あなたたちもお仕事忙しそうね。\x01",
            "せっかくだしお弁当の作り方を\x01",
            "教えてあげるわ。\x02",
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
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xE)
    Return()

    # Function_11_3F9C end

    def Function_12_4112(): pass

    label("Function_12_4112")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_41C9")

    #C0198
    ChrTalk(
        0xFE,
        (
            "ロージーはなんだかんだ\x01",
            "文句を言いながらも、\x01",
            "きちんと仕事をしているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "長男なのにサボり癖があるから\x01",
            "心配だったけど……\x01",
            "この様子ならなんとかなりそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_41C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4263")

    #C0200
    ChrTalk(
        0xFE,
        (
            "ガンツさんが戻ってくるとなると……\x01",
            "ロージーがまたサボリださないか心配ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "せっかく働いたのだから\x01",
            "これを機に続けていって欲しいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_42EF")

    #C0202
    ChrTalk(
        0xFE,
        (
            "さて、ロージーとアミーが\x01",
            "家に帰ってくるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "特にロージーは最近よく働くから\x01",
            "とびきりのご馳走をしてあげなくてはね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_42EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4388")

    #C0204
    ChrTalk(
        0xFE,
        (
            "今日はロージーは珍しくちゃんと\x01",
            "鉱山で働いているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "……ガンツさんがいないから\x01",
            "サボリにくいっていうのも\x01",
            "あるんでしょうけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_442B")

    #C0206
    ChrTalk(
        0xFE,
        (
            "マインツの南西の崖に\x01",
            "遺跡があるのは知ってる？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "わたしが子供のころからあるのだけど\x01",
            "大昔の修道院跡であるという以外は\x01",
            "何も分かっていないのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_442B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_44BE")

    #C0208
    ChrTalk(
        0xFE,
        (
            "ロージー……\x01",
            "あの子のサボリ癖が本当に心配だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "この際鉱員じゃなくてもいいから、\x01",
            "熱中できることを\x01",
            "してほしいものだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_44BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_454B")

    #C0210
    ChrTalk(
        0xFE,
        (
            "孫娘のアミーときたら、\x01",
            "町に来ていた観光客を\x01",
            "いきなりナンパしたらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "あの子の悪い癖は\x01",
            "本当によくならないわね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_454B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4619")

    #C0212
    ChrTalk(
        0xFE,
        (
            "クロスベル自治州が\x01",
            "帝国と共和国に取り合われて、\x01",
            "この町も随分振り回されてきたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "《不戦条約》のお陰で\x01",
            "安定はしてきたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "この町の人の政府への不信感は\x01",
            "相当なものでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D58")

    label("loc_4619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4752")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E2")

    #C0215
    ChrTalk(
        0xFE,
        (
            "昨日、孫のロージーは\x01",
            "お酒が飲めないくせに\x01",
            "宴会に出かけたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "案の定、昨日は家に\x01",
            "帰って来れなかったみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "やれやれ、後で宿酒場に\x01",
            "様子を見に行くかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_474D")

    label("loc_46E2")


    #C0218
    ChrTalk(
        0xFE,
        (
            "全く、アミーが『付き合い悪い』なんて\x01",
            "たきつけたりするから……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "やれやれ、後で様子を見に行くかね。\x02",
    )

    CloseMessageWindow()

    label("loc_474D")

    Jump("loc_4D58")

    label("loc_4752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_48A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4836")

    #C0220
    ChrTalk(
        0xFE,
        (
            "最近はね、\x01",
            "進んで鉱員になりたいっていう\x01",
            "若い子は殆どいないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "それよりも町で商人なんかして\x01",
            "華やかな生活を送りたい……\x01",
            "そんな子が増えてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "少し寂しいけど……\x01",
            "これも時代の流れかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_48A2")

    label("loc_4836")


    #C0223
    ChrTalk(
        0xFE,
        (
            "鉱員になるよりも、\x01",
            "商人なんかを目指す子が増えてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "少し寂しいけど……\x01",
            "これも時代の流れかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48A2")

    Jump("loc_4D58")

    label("loc_48A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49A1")

    #C0225
    ChrTalk(
        0xFE,
        (
            "この鉱山で発掘される七耀石は\x01",
            "質も良く、量も多いから\x01",
            "とても重宝されているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "それに、７色ある七耀石のすべてが\x01",
            "採取できる鉱山はとても貴重なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "外国の商人さんたちが\x01",
            "わざわざ買い付けに来るほど\x01",
            "評価が高いのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4A2C")

    label("loc_49A1")


    #C0228
    ChrTalk(
        0xFE,
        (
            "この鉱山で発掘される七耀石は\x01",
            "質も良く、量も多いの。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "最近では発掘量は\x01",
            "少しずつ減ってきたけど……\x01",
            "商人さんたちには評価が高いのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A2C")

    Jump("loc_4D58")

    label("loc_4A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_4A3F")
    Jump("loc_4D58")

    label("loc_4A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_4BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B4C")

    #C0230
    ChrTalk(
        0xFE,
        (
            "私には二人、孫がいるのだけど……\x01",
            "どちらもちょっと問題アリでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "兄のロージーは鉱員なのに\x01",
            "よくサボって鉱山の外に\x01",
            "出てきているし……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "妹のアミーは何かにつけて\x01",
            "ボーイフレンド探しに精を出す始末なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "育て方を間違ったかしら……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4BA9")

    label("loc_4B4C")


    #C0234
    ChrTalk(
        0xFE,
        "私の孫兄妹はどちらも問題児でね……\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "ロージーとアミー……\x01",
            "育て方を間違ったかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA9")

    Jump("loc_4D58")

    label("loc_4BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD0")
    SetScenarioFlags(0x67, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CCE")

    #C0236
    ChrTalk(
        0xFE,
        (
            "このクロスベルは昔から\x01",
            "帝国と共和国の間で所有権を\x01",
            "争われていたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "その理由の大部分は、\x01",
            "この七耀石の産地である\x01",
            "鉱山の存在にあるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "今では金融業が中心になったけど、\x01",
            "それでも自治州を支える\x01",
            "重要な場所には間違いないわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D58")

    label("loc_4CCE")


    #C0239
    ChrTalk(
        0xFE,
        (
            "帝国と共和国の間で\x01",
            "この自治州の所有権が\x01",
            "争われてきたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "その理由の大部分は、\x01",
            "七耀石の産地である\x01",
            "この鉱山の存在にあるのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D58")

    TalkEnd(0xFE)
    Return()

    # Function_12_4112 end

    def Function_13_4D5C(): pass

    label("Function_13_4D5C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4DF0")
    Jump("loc_4E3A")

    label("loc_4DF0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E10")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E3A")

    label("loc_4E10")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E30")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E3A")

    label("loc_4E30")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E3A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F3C")

    #C0241
    ChrTalk(
        0xFE,
        (
            "鉱山内の廃坑のほうが\x01",
            "ちょいと面倒なことに\x01",
            "なっててな……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "……まぁ、気にしても\x01",
            "しょうがねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "どっちにしろ人手が足りねぇんだ、\x01",
            "若い連中が帰ってきてから\x01",
            "対策にあたるとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 1)
    Jump("loc_51DE")

    label("loc_4F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4FCB")

    #C0244
    ChrTalk(
        0xFE,
        (
            "ミランダにはいつも心配を\x01",
            "かけちまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "だが、鉱員の仕事は町の誇りだ。\x01",
            "いくら危険でも逃げるわけには\x01",
            "いかねぇんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DE")

    label("loc_4FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5085")

    #C0246
    ChrTalk(
        0xFE,
        (
            "雑貨屋のベッカライさんは\x01",
            "俺の先輩なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "鉱員としての技術は\x01",
            "あの人に一から十まで教わった。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "鉱山を任されるようになった\x01",
            "今でも頭が上がらねぇぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_50FC")

    label("loc_5085")


    #C0249
    ChrTalk(
        0xFE,
        (
            "雑貨屋のベッカライさんは\x01",
            "俺の先輩なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "あの人へは恩がある。\x01",
            "鉱員として一人前になっても\x01",
            "頭が上がらねぇぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50FC")

    Jump("loc_51DE")

    label("loc_5101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_515F")

    #C0251
    ChrTalk(
        0xFE,
        (
            "ウチの息子も鉱員に\x01",
            "憧れてくれてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "父親として\x01",
            "誇らしい気分だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DE")

    label("loc_515F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_51DE")

    #C0253
    ChrTalk(
        0xFE,
        (
            "ガンツやマルロは記念祭中、\x01",
            "クロスベル市に滞在するそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "ま、年寄りは町で\x01",
            "ゆっくりとさせてもらうとするさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51DE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_4D5C end

    def Function_14_51E6(): pass

    label("Function_14_51E6")

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

    def lambda_5326():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5326)

    def lambda_5340():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5340)
    Sleep(100)

    def lambda_5354():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5354)

    def lambda_536E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_536E)
    Sleep(50)

    def lambda_5382():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5382)

    def lambda_539C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_539C)
    Sleep(80)

    def lambda_53B0():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_53B0)

    def lambda_53CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_53CA)
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
        "男性の声",
        "#3P──また来たのかね。\x02",
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
        "#0005F#6Pえ……\x02",
    )

    CloseMessageWindow()
    OP_68(500, 2250, 2500, 3000)
    OP_6F(0x1)

    #C0257
    ChrTalk(
        0x8,
        (
            "#11Pすぐには決められないと\x01",
            "言ったばかりだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        "#11P今日のところはお引取り──\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0259
    ChrTalk(
        0x8,
        "#11Pおや……？\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xA,
        (
            "#5Pあら、先ほどの方たちじゃ\x01",
            "ないみたいですよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500, 2250, 0, 3000)

    def lambda_5591():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5591)
    Sleep(100)

    def lambda_55AE():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_55AE)
    Sleep(50)

    def lambda_55CB():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_55CB)
    Sleep(80)

    def lambda_55E8():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_55E8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0261
    ChrTalk(
        0x8,
        "#11Pお、おお……これは失礼。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        "#0000F#6Pその……失礼します。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#0100F#6Pお取り込みのところに\x01",
            "お邪魔して申し訳ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x8,
        (
            "#11Pあ、ああ……\x01",
            "それは別に構わんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        "#11Pその……君たちは？\x02",
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
            "#1P──クロスベル警察、\x01",
            "特務支援課に所属する者です。\x02\x03",

            "こちらで起きた魔獣被害について\x01",
            "話を聞かせて頂きたいのですが……\x02",
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
            "#5Pなるほど……\x01",
            "街の警察の方だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "#5Pてっきり遊撃士協会の新人が\x01",
            "訪ねてきたのかと思ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#0012F#12P……その、よく言われます。\x02\x03",

            "#0001Fそれで……\x01",
            "町の方々にも色々と話を\x01",
            "聞かせてもらったんですが。\x02\x03",

            "タチの悪い被害が\x01",
            "続いているそうですね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x8,
        (
            "#5Pああ……今までに\x01",
            "３回ほど被害に遭っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#5Pどれも夜のことで、\x01",
            "最初は人的被害も無かったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        "#5P先日、ついにケガ人が出てね。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xA,
        (
            "#11P軽傷だったのが幸いだけど、\x01",
            "徐々に被害が大きくなっているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "#11Pそれで町のみんなも\x01",
            "すっかり恐がってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#0003F#12Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        (
            "#0101F#2Pその、警備隊が\x01",
            "パトロールに来ている間は\x01",
            "何も起こらなかったんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x8,
        "#5Pああ、その通りなんだ。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#5Pどうやら狼どもは\x01",
            "相当ズル賢いようでね……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        "#5Pしかし、警備隊も警備隊だ！\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "#5P何も解決できていないのに\x01",
            "突然我々を見捨てるとは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        "#5P君たちもそう思わないかね！？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        (
            "#0006F#12Pええ……確かに。\x01",
            "（色々あるみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x104,
        (
            "#0305F#2Pところで、遊撃士協会を\x01",
            "頼ったりしなかったんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "#5P実は、警備隊が来る前に\x01",
            "一度ギルドに依頼してみたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#5Pただ、基本的に彼らは\x01",
            "とても忙しいみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "#5P毎日警備をしてもらう訳にもいかず、\x01",
            "結局は警備隊が出動したんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        (
            "#0203F#6Pなのに今朝、警備隊が\x01",
            "いきなり撤収してしまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "#5Pああ……\x01",
            "弱り目に祟り目とはこの事さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x8,
        (
            "#5P仕方ないから、ダメ元で\x01",
            "もう一度ギルドに相談してみようと\x01",
            "思っていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        "#5Pそこにあの連中が訪ねてきたんだ。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        "#0001F#12P《ルバーチェ商会》の者ですね。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x102,
        (
            "#0101F#2Pその……\x01",
            "彼らは一体、どんな話をしに？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        "#5Pそれがねぇ……\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "#5P撤収した警備隊に代わって\x01",
            "用心棒を申し出てきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        "#5Pいつ魔獣が来てもいいようにとね。\x02",
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
        "#0005F#12Pよ、用心棒……？\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x104,
        (
            "#0301F#2Pそりゃあ……\x01",
            "勿論、タダじゃないッスよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x8,
        (
            "#5Pいや……\x01",
            "ミラを取るつもりはないらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "#5P代わりに、七耀石#6Rセプチウム#の取引を\x01",
            "その間だけ独占させて欲しいそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#0105F#2P七耀石の取引権を……\x02\x03",

            "#0101F確か鉱山そのもの採掘権は\x01",
            "自治州が持っているはずですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        (
            "#5Pああ、あまり採掘しすぎないよう、\x01",
            "政府の決めた量を守る必要がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x8,
        (
            "#5P七耀石には国際的な相場もあるから\x01",
            "無茶な取引はそもそも出来ないしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "#5Pただ、採掘した七耀石を\x01",
            "どこに買い取ってもらうかは\x01",
            "この町の裁量に任されているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        (
            "#0200F#6Pすると、彼らにとっては\x01",
            "用心棒の手間に見合うだけの\x01",
            "ビジネスになるという訳ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xA,
        (
            "#5Pそうは言っても、付き合いのある\x01",
            "商人さん達もいることですしねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xA,
        (
            "#5Pどうしたものかと\x01",
            "困り果てていた所なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#0103F#2Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#0306F#2Pやれやれ、妙な連中が絡んで\x01",
            "面倒くさい事になって来たな……\x02",
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
            "#0003F#12P──町長、できればこの件、\x01",
            "自分たちに任せてもらえませんか？\x02\x03",

            "#0000Fひょっとしたら……\x01",
            "何とか解決できるかもしれません。\x02",
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
        "#0105F#2Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        "#0205F#6P……ロイドさん……？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "#5Pふむ……\x01",
            "《特務支援課》といったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x8,
        (
            "#5P警備隊でも遊撃士でもなく、\x01",
            "街の警察に頼ってもいいのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0004F#12Pええ、お任せください。\x02\x03",

            "#0000F早ければ明日中には\x01",
            "全て解決できると思います。\x02",
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

    # Function_14_51E6 end

    def Function_15_65AD(): pass

    label("Function_15_65AD")

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
            "#0000F#6P──失礼します。\x01",
            "特務支援課の者ですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    #C0316
    ChrTalk(
        0x8,
        "#11Pおお、待っておったよ。\x02",
    )

    CloseMessageWindow()
    OP_68(600, 2450, -3350, 2500)

    def lambda_6724():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6724)

    def lambda_6739():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6739)

    def lambda_674E():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_674E)

    def lambda_6763():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6763)

    def lambda_6778():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6778)

    def lambda_678D():
        OP_95(0xFE, -190, 750, -830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_678D)
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
        "#11Pわざわざ来てくれてすまない。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#11P本当ならこちらから\x01",
            "出向こうと思ったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#0004F#6Pいえ、近くで他の仕事が\x01",
            "あったついでですから。\x02\x03",

            "#0001Fそれで……\x01",
            "早速話を伺ってもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        "#11Pああ、座ってくれたまえ。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xA,
        "#5Pすぐにお茶でも淹れますね。\x02",
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
            "#0003F#12P──なるほど。\x02\x03",

            "#0001Fでは、そのガンツさんという鉱員が\x01",
            "２週間前にクロスベル市に行ったきり\x01",
            "帰って来ていないと……？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x8,
        "#5Pああ、そうなんだ……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        "#5Pとにかく大のギャンブル好きでね。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "#5Pそれまでにも週末のたびに\x01",
            "クロスベルの歓楽街にあるカジノに\x01",
            "遊びに行っていたようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xA,
        (
            "#11Pそれが何の連絡もなく、\x01",
            "２週間も帰って来てなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xA,
        (
            "#11P何かあったんじゃないかと\x01",
            "みんなで心配しているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        "#0108F#12P確かに……それは心配ですね。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#0208F#6P何かの事件に巻き込まれたか、\x01",
            "それとも帰れない事情があるのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x109,
        (
            "#0506F#11Pうーん、街の外に出て\x01",
            "魔獣に襲われたとかじゃなければ\x01",
            "いいんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0331
    ChrTalk(
        0x104,
        (
            "#0305F#11P──そういや、その鉱員が\x01",
            "ギャンブルで大勝ちした可能性は\x01",
            "あるんじゃねえか？\x02\x03",

            "#0309Fそれで今ごろ、ミシュラムあたりで\x01",
            "女連れで豪遊してるとか。\x02",
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
            "#0006F#12Pいや……\x01",
            "ランディじゃないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        (
            "#0202F#6Pでも、可能性としては\x01",
            "あり得るかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        "#5Pう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x8,
        (
            "#5P残念ながらその可能性は\x01",
            "無いと思うんだがねぇ……\x02",
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
        "#0005F#12Pそれはまた、どうして？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x102,
        (
            "#0102F#12Pギャンブル好きだけど\x01",
            "根は真面目な方なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#5Pハハ、お世辞にも\x01",
            "真面目とは言いがたいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        (
            "#5Pギャンブルについては\x01",
            "とにかく下手の横好きでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x8,
        (
            "#5Pおまけにツキもカンも無いから\x01",
            "毎回、有り金のほとんどを\x01",
            "スって帰ってくるくらいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#0012F#12Pな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#0303F#11P確かに宝クジなら大穴もあるが\x01",
            "ギャンブルだと実力もないと\x01",
            "大儲けは難しいかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x103,
        (
            "#0211F#6Pでは、街で借金をして\x01",
            "それが返せずに失踪とか……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        (
            "#0106F#12Pそ、そうね……\x01",
            "可能性としてはあり得るかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        (
            "#5P……実は私たちの方も\x01",
            "そのあたりを疑っていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xA,
        (
            "#11Pもしそうだった場合、\x01",
            "どう連絡を取ればいいのか……\x02",
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
            "#0004F#12P──分かりました。\x01",
            "この件はお任せください。\x02\x03",

            "#0000Fとりあえず、カジノを始め、\x01",
            "ガンツさんの寄りそうな場所を\x01",
            "聞き込みしてみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "#5Pありがたい……\x01",
            "どうか宜しくお願いする。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x8,
        (
            "#5P何か分かったら私の家に\x01",
            "通信で連絡してもらえるかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        (
            "#0000F#12Pええ、それでは番号を\x01",
            "控えさせていただければ……\x02",
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

    # Function_15_65AD end

    def Function_16_73E9(): pass

    label("Function_16_73E9")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7482")
    OP_93(0x8, 0x0, 0x0)
    Jump("loc_7489")

    label("loc_7482")

    OP_93(0x8, 0xB4, 0x0)

    label("loc_7489")

    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79BD")

    #C0351
    ChrTalk(
        0x8,
        "#11Pふむ……困った……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x8,
        (
            "#11P流石に鉱山長一人で\x01",
            "退治に行かせるわけにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#6P#0000Fこんにちは、ビクセン町長。\x02\x03",

            "特務支援課ただいま到着しました。\x02",
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
            "#11Pおお、君たち……！\x01",
            "待っておったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x102,
        (
            "#6P#0100F支援要請を出されていましたよね。\x02\x03",

            "鉱山に魔獣が出た、\x01",
            "とのことでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        "#11Pうむ……その通りじゃ。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x8,
        (
            "#11P実は、鉱山の奥には\x01",
            "発掘を終えた廃坑があるのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#11P夜中のうちに\x01",
            "魔獣が沸いてしまって\x01",
            "困っているのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#6P#0005F鉱山内に魔獣が……\x01",
            "それは大変でしたね。\x02\x03",

            "こういうことは\x01",
            "よくあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x103,
        (
            "#6P#0203F……七耀石の採掘場所近辺に\x01",
            "魔獣が大量発生する例は、\x01",
            "各国で多数報告されています。\x02\x03",

            "#0200F理屈は分かりませんが、\x01",
            "魔獣は七耀石に惹かれる性質を\x01",
            "持っていますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#6P#0301Fそういや俺も\x01",
            "何度か聞いたことがあるなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#6P#0105F私も聞き覚えがあるわ。\x01",
            "どこの国でも、鉱山には\x01",
            "危険が付き物なんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        "#6P#0003Fそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x8,
        (
            "#11P本来ならば、鉱山の魔獣くらいなら\x01",
            "鉱員たちだけでも\x01",
            "なんとか追い払えるのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x8,
        (
            "#11P記念祭中は休暇で、\x01",
            "若い鉱員が町を出ていてね。\x01",
            "すぐには対処できない状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#11P今は廃坑の入り口は封鎖しているが……\x01",
            "このまま放っておくと\x01",
            "どんな危険があるか分からん。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#11Pそこで君たちに\x01",
            "魔獣どもを退治してほしいのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x8,
        (
            "#11Pどうかね。\x01",
            "引き受けてもらえるだろうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1C, 0x1, 0x0)
    Jump("loc_7A98")

    label("loc_79BD")


    #C0369
    ChrTalk(
        0x8,
        (
            "#11P実は、鉱山の奥には\x01",
            "発掘を終えた廃坑があるのだが……\x01",
            "魔獣が沸いてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        (
            "#11P君たちには、\x01",
            "なんとか記念祭が終わるまでに\x01",
            "魔獣どもを退治してほしいのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x8,
        (
            "#11Pどうかね。\x01",
            "引き受けてもらえるだろうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A98")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7ADE"),
        (1, "loc_7CA8"),
        (SWITCH_DEFAULT, "loc_7D7E"),
    )


    label("loc_7ADE")

    OP_60(0x0)

    #C0372
    ChrTalk(
        0x101,
        (
            "#6P#0000F分かりました。\x01",
            "確かに引き受けさせて\x01",
            "いただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        "#11P……そうか、恩に着るよ。\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "#11Pそれでは、これを\x01",
            "預かっていてくれたまえ。\x02",
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
            "を受け取った。\x02",
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
            "#11P廃坑へは、鉱山の奥にある扉で\x01",
            "その鍵を使えば入れる。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#11Pそれでは、よろしく頼んだよ。\x01",
            "充分気をつけてな。\x02",
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
            "クエスト【鉱山の魔獣退治】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x1C, 0x1, 0x1)
    SetScenarioFlags(0x1, 0)
    Jump("loc_7D8D")

    label("loc_7CA8")

    OP_60(0x0)

    #C0379
    ChrTalk(
        0x101,
        (
            "#6P#0006Fすみませんが……\x01",
            "今すぐには引き受けられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        "#11Pううむ、そうか……\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11P鉱山は今のところは安全だが、\x01",
            "放っておくのは忍びない。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#11Pもし引き受けられそうなら\x01",
            "またお願いするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D8D")

    label("loc_7D7E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D8D")

    label("loc_7D8D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x0, -610, 750, -2790, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_73E9 end

    def Function_17_7DBE(): pass

    label("Function_17_7DBE")

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
            "#11Pふむ、魔獣を残らず\x01",
            "退治してくれたようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        "#6P#0000Fええ、確かに殲滅を確認しました。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x103,
        (
            "#6P#0200F当分は魔獣が居つくことも\x01",
            "ないでしょう。\x02\x03",

            "記念祭が終わって\x01",
            "鉱員さんたちが戻るまで位なら\x01",
            "安全は保障されると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x8,
        (
            "#11Pおお、そうかね……\x01",
            "なんとお礼を言っていいものか。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        (
            "#11P……そうだ、\x01",
            "よければこれを\x01",
            "受け取ってくれるかね？\x02",
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
            "#56I地のセピス×２００\x01\x07\x02",

            "#57I水のセピス×２００\x01\x07\x02",

            "#58I火のセピス×２００\x01\x07\x02",

            "#59I風のセピス×２００\x01\x07\x02",

            "#62I時のセピス×２００\x01\x07\x02",

            "#60I空のセピス×２００\x01\x07\x02",

            "#61I幻のセピス×２００\x01\x07\x00",
            "を手に入れた。\x02",
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
        "#6P#0205Fこんなに多くのセピスを……？\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x104,
        (
            "#6P#0309Fうひょー、貰っちゃって\x01",
            "いいんッスか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#6P#0011Fい、いいわけないだろ！？\x02\x03",

            "#0003F町長、俺たちは遊撃士みたいに\x01",
            "こういう報酬をもらうわけには\x01",
            "いかないんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x102,
        (
            "#6P#0105Fそれに、これって\x01",
            "ここで採掘された\x01",
            "大事な商品ではないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        "#11Pいや、いいんだ。\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x8,
        (
            "#11Pセピスは七耀石のかけら……\x01",
            "言ってみれば、採掘のついでに出た\x01",
            "おまけのようなものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x8,
        (
            "#11P政府に取引量の決められた\x01",
            "七耀石ならまだしも、\x01",
            "セピスを渡す分には問題もなかろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x8,
        (
            "#11Pむしろ余り物しか\x01",
            "用意できなくて\x01",
            "申し訳ないくらいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        "#6P#0005Fそ、そんなことは……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x8,
        (
            "#11Pフフ……君たちには何度も\x01",
            "世話になっているからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x8,
        (
            "#11P個人的なお礼だと思って\x01",
            "気にせず貰ってくれたまえ。\x02",
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
            "#6P#0003F……わかりました。\x01",
            "そういうことなら……\x01",
            "ありがたく頂戴させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x8,
        "#11Pうむ。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x8,
        (
            "#11Pでは改めて、今回のことには\x01",
            "お礼を言わせていただこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x8,
        "#11Pまた何かあったらよろしく頼むよ。\x02",
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
            "クエスト【鉱山の魔獣退治】\x07\x00",
            "を達成した！\x02",
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

    # Function_17_7DBE end

    SaveToFile()

Try(main)
