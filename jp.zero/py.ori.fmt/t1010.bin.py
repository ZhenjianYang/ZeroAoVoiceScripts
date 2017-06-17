from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1010.bin",                # FileName
        "t1010",                    # MapName
        "t1010",                    # Location
        0x0042,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1010",                  # 0
        "エミー",                 # 1
        "ゼル",                   # 2
        "カビラン",               # 3
        "ルーグマン",             # 4
        "男性",                   # 5
        "議長邸方面",             # 6
        "ホテル・デルフィニア方面",# 7
    ))

    AddCharChip((
        "chr/ch27700.itc",                   # 00
        "chr/ch22302.itc",                   # 01
        "chr/ch22202.itc",                   # 02
        "chr/ch33100.itc",                   # 03
        "chr/ch33000.itc",                   # 04
    ))

    DeclNpc(2279,    -3700,   -12430,  180,  341,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(3660,    -3700,   -12430,  180,  341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(26860,   -2000,   2200,    270,  257,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1970,   -2000,   34720,   180,  257,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2400,    -1799,   55840,   0,    385,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)

    DeclEvent(0x0000, 0, 13,  -6.460000038146973,    -16.520000457763672,   -3.799999952316284,    156.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.2920000553131104,    3.30400013923645,      0.7599999904632568,    1.0])

    DeclActor(-6460,   -3800,   -16520,  1200,    -6210,   -5800,   -21830,  0x007C, 0,  12, 0x0000)

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "議長邸方面")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")

    ScpFunction((
        "Function_0_21C",          # 00, 0
        "Function_1_2D4",          # 01, 1
        "Function_2_335",          # 02, 2
        "Function_3_396",          # 03, 3
        "Function_4_3C1",          # 04, 4
        "Function_5_43E",          # 05, 5
        "Function_6_531",          # 06, 6
        "Function_7_7A8",          # 07, 7
        "Function_8_9F5",          # 08, 8
        "Function_9_10B0",         # 09, 9
        "Function_10_12CA",        # 0A, 10
        "Function_11_14EC",        # 0B, 11
        "Function_12_1571",        # 0C, 12
        "Function_13_1673",        # 0D, 13
        "Function_14_1806",        # 0E, 14
    ))


    def Function_0_21C(): pass

    label("Function_0_21C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_25C"),
        (1, "loc_268"),
        (2, "loc_274"),
        (3, "loc_280"),
        (4, "loc_28C"),
        (5, "loc_298"),
        (6, "loc_2A4"),
        (SWITCH_DEFAULT, "loc_2B0"),
    )


    label("loc_25C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_268")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_274")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_280")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_28C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_298")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2D3")

    Return()

    # Function_0_21C end

    def Function_1_2D4(): pass

    label("Function_1_2D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_334")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_2D4")

    label("loc_334")

    Return()

    # Function_1_2D4 end

    def Function_2_335(): pass

    label("Function_2_335")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_395")
    OP_95(0xFE, -1970, -2000, 34720, 2000, 0x0)
    OP_95(0xFE, -1970, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 34720, 2000, 0x0)
    Jump("Function_2_335")

    label("loc_395")

    Return()

    # Function_2_335 end

    def Function_3_396(): pass

    label("Function_3_396")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C0")
    OP_94(0xFE, 0xFFFFEB1A, 0xB9D2, 0xF8C, 0xD67E, 0x3E8)
    Sleep(300)
    Jump("Function_3_396")

    label("loc_3C0")

    Return()

    # Function_3_396 end

    def Function_4_3C1(): pass

    label("Function_4_3C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_3CF")
    Jump("loc_431")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_431")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_3EB")
    Jump("loc_431")

    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3F9")
    Jump("loc_431")

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_407")
    Jump("loc_431")

    label("loc_407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_415")
    Jump("loc_431")

    label("loc_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_428")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_431")

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_431")

    label("loc_431")

    BeginChrThread(0xA, 0, 0, 1)
    BeginChrThread(0xB, 0, 0, 2)
    Return()

    # Function_4_3C1 end

    def Function_5_43E(): pass

    label("Function_5_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47E")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1010_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1010_sky_y", 0x1, 0x1)
    Jump("loc_4A2")

    label("loc_47E")

    SetMapObjFrame(0xFF, "t1010_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1010_sky_y", 0x0, 0x1)

    label("loc_4A2")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C2")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4C2")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    OP_66(0x0, 0x1)
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -6210, -5800, -21830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_52A")

    Sound(126, 1, 80, 0)
    Return()

    # Function_5_43E end

    def Function_6_531(): pass

    label("Function_6_531")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C5")
    Jump("loc_60F")

    label("loc_5C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60F")

    label("loc_5E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_605")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60F")

    label("loc_605")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_642")
    Jump("loc_7A0")

    label("loc_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_650")
    Jump("loc_7A0")

    label("loc_650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_65E")
    Jump("loc_7A0")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_66C")
    Jump("loc_7A0")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_7A0")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_695")
    Call(0, 8)
    Jump("loc_710")

    label("loc_695")


    #C0001
    ChrTalk(
        0xFE,
        (
            "ゼルったらダメねぇ。\x01",
            "ホントダメ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "ゼルがお医者様になったら\x01",
            "毎日あたしは寂しく留守番してなきゃ\x01",
            "いけないじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_710")

    Jump("loc_7A0")

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_730")
    Call(0, 8)
    Jump("loc_792")

    label("loc_730")


    #C0003
    ChrTalk(
        0xFE,
        (
            "ゼルったらダメねぇ。\x01",
            "ホントダメ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "そんなことで将来、\x01",
            "あたしを幸せに出来るつもりかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_792")

    Jump("loc_7A0")

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7A0")

    label("loc_7A0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_531 end

    def Function_7_7A8(): pass

    label("Function_7_7A8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83C")
    Jump("loc_886")

    label("loc_83C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_85C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_886")

    label("loc_85C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_886")

    label("loc_87C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_886")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_8B9")
    Jump("loc_9ED")

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_8C7")
    Jump("loc_9ED")

    label("loc_8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_8D5")
    Jump("loc_9ED")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_8E3")
    Jump("loc_9ED")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_8F1")
    Jump("loc_9ED")

    label("loc_8F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90C")
    Call(0, 8)
    Jump("loc_943")

    label("loc_90C")


    #C0005
    ChrTalk(
        0xFE,
        (
            "エミーはわがままだよ。\x01",
            "僕にだって夢があるのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_943")

    Jump("loc_9ED")

    label("loc_948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_9E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_963")
    Call(0, 8)
    Jump("loc_9DF")

    label("loc_963")


    #C0006
    ChrTalk(
        0xFE,
        (
            "エミーの言うことは\x01",
            "子供の僕にはよくわからないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "許婚なんて親が言ってるだけだし\x01",
            "僕なんかに構わなきゃいいのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DF")

    Jump("loc_9ED")

    label("loc_9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9ED")

    label("loc_9ED")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_7A8 end

    def Function_8_9F5(): pass

    label("Function_8_9F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_A03")
    Jump("loc_10A4")

    label("loc_A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_A11")
    Jump("loc_10A4")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_A1F")
    Jump("loc_10A4")

    label("loc_A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_A2D")
    Jump("loc_10A4")

    label("loc_A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_A3B")
    Jump("loc_10A4")

    label("loc_A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_DA9")
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x9, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AD8")
    Jump("loc_B22")

    label("loc_AD8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF8")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B22")

    label("loc_AF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B18")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B22")

    label("loc_B18")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B22")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BDB")
    Jump("loc_C25")

    label("loc_BDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BFB")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C25")

    label("loc_BFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1B")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C25")

    label("loc_C1B")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C25")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    #C0008
    ChrTalk(
        0x8,
        (
            "いいこと、ゼル？\x01",
            "あなたはあたしの許婚なんだから\x01",
            "きちんとした将来設計が必要だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "なにかやりたい仕事とかは\x01",
            "ないのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "えっと……ウルスラ病院で\x01",
            "お医者さんになりたいなぁ\x01",
            "なんて思ってるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "ダメ。\x01",
            "お医者様になったら\x01",
            "なかなかお家に帰れないと聞くわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "家庭をかえりみない夫になるのは\x01",
            "感心しないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        "そ、そんなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A4")

    label("loc_DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_109B")
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x9, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E46")
    Jump("loc_E90")

    label("loc_E46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E66")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E90")

    label("loc_E66")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E86")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E90")

    label("loc_E86")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E90")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F49")
    Jump("loc_F93")

    label("loc_F49")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F69")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F93")

    label("loc_F69")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F89")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F93")

    label("loc_F89")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F93")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    #C0014
    ChrTalk(
        0x8,
        (
            "いいこと、ゼル？\x01",
            "あなたはあたしの許婚なんだから\x01",
            "シャキッとしてないとダメよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        "えっと……どうすれば……？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "そんなことは自分で考えなさい。\x01",
            "きっとそれがシャキっとすると\x01",
            "いうことなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        "む、むずかしいよ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A4")

    label("loc_109B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_10A4")

    label("loc_10A4")

    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_8_9F5 end

    def Function_9_10B0(): pass

    label("Function_9_10B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_10C1")
    Jump("loc_12C6")

    label("loc_10C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_10CF")
    Jump("loc_12C6")

    label("loc_10CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_10DD")
    Jump("loc_12C6")

    label("loc_10DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_10EB")
    Jump("loc_12C6")

    label("loc_10EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_10F9")
    Jump("loc_12C6")

    label("loc_10F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_11BD")

    #C0018
    ChrTalk(
        0xFE,
        (
            "おいおい、\x01",
            "そんな格好でこの住宅街に\x01",
            "足を踏み入れないでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "人にはそれぞれの身なりに\x01",
            "相応しい場所があるもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "せめてブティックでマシな服に\x01",
            "着替えてから来るんだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C6")

    label("loc_11BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_12BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1252")

    #C0021
    ChrTalk(
        0xFE,
        "……おやおや？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "庶民の方々が\x01",
            "この高級住宅街に何の用かね？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "観光するつもりなら\x01",
            "テーマパークの方に戻りたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12B8")

    label("loc_1252")


    #C0024
    ChrTalk(
        0xFE,
        (
            "観光するなら\x01",
            "テーマパークの方に戻りたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "我々の屋敷を庶民が見ても\x01",
            "うらやましいだけだぞ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B8")

    Jump("loc_12C6")

    label("loc_12BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_12C6")

    label("loc_12C6")

    TalkEnd(0xFE)
    Return()

    # Function_9_10B0 end

    def Function_10_12CA(): pass

    label("Function_10_12CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_12DB")
    Jump("loc_14E8")

    label("loc_12DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_12E9")
    Jump("loc_14E8")

    label("loc_12E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_12F7")
    Jump("loc_14E8")

    label("loc_12F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1305")
    Jump("loc_14E8")

    label("loc_1305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_1313")
    Jump("loc_14E8")

    label("loc_1313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_13AB")

    #C0026
    ChrTalk(
        0xFE,
        (
            "なんでも今日は、ハルトマン議長邸で\x01",
            "記念祭を祝したパーティがあるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "近隣諸国からも議長の友人などが\x01",
            "呼ばれているらしいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E8")

    label("loc_13AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_14DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145A")

    #C0028
    ChrTalk(
        0xFE,
        (
            "この先へ進むと\x01",
            "ハルトマン議長の邸宅があるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "初めて見るとその豪勢さに\x01",
            "びっくりするかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "いやはや、私もあやかりたいものだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_14DA")

    label("loc_145A")


    #C0031
    ChrTalk(
        0xFE,
        "この先はハルトマン議長の邸宅だ。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "あれだけの屋敷、\x01",
            "維持するだけでも大変だろうに……\x01",
            "いやはや、私もあやかりたいものだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DA")

    Jump("loc_14E8")

    label("loc_14DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_14E8")

    label("loc_14E8")

    TalkEnd(0xFE)
    Return()

    # Function_10_12CA end

    def Function_11_14EC(): pass

    label("Function_11_14EC")

    TalkBegin(0xFE)

    #C0033
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長邸は\x01",
            "たしかこっちの方向じゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "確か、客室が用意されとるはずじゃ。\x01",
            "さっさと行って休むとするかの。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_14EC end

    def Function_12_1571(): pass

    label("Function_12_1571")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0035
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(-3780, -2000, -21590, 1500)
    MoveCamera(315, 25, 0, 1500)
    OP_6E(320, 1500)
    SetCameraDistance(39000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1654")
    OP_E0(0x2)
    ClearScenarioFlags(0x0, 3)
    MiniGame(0x6, 0x4, 0xFFFFE6D8, 0xFFFFF128, 0xFFFFC36A, 0xB4, 0xFFFFE7BE, 0xFFFFE958, 0xFFFFAABA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1654")
    SetScenarioFlags(0x0, 3)

    label("loc_1654")

    OP_E0(0x2)
    EventEnd(0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1672")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1672")
    Call(0, 14)

    label("loc_1672")

    Return()

    # Function_12_1571 end

    def Function_13_1673(): pass

    label("Function_13_1673")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4510, -2000, -17230, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24740, 0)
    SetChrPos(0x101, -7200, -3800, -15000, 180)
    SetChrPos(0x102, -6000, -3800, -15000, 180)
    SetChrPos(0x103, -7200, -3800, -13800, 180)
    SetChrPos(0x104, -6000, -3800, -13800, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1706")
    SetChrPos(0x151, -4800, -3800, -14400, 180)

    label("loc_1706")

    StopEffect(0x1, 0x2)
    OP_0D()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_176D")
    OP_63(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_176D")

    Sleep(1000)
    OP_68(-2980, -2000, -24760, 3000)
    SetCameraDistance(21000, 3000)
    OP_6F(0x79)
    LoadEffect(0x0, "event\\eva00_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -6210, -5800, -21830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(860, 0, 100, 0)
    Sleep(3000)
    StopEffect(0x0, 0x2)
    Sleep(2000)
    OP_29(0x24, 0x1, 0x8)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, -7200, -3800, -15000, 180)
    EventEnd(0x5)
    Return()

    # Function_13_1673 end

    def Function_14_1806(): pass

    label("Function_14_1806")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4510, -2000, -17230, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24740, 0)
    SetChrPos(0x101, -7200, -3800, -15000, 180)
    SetChrPos(0x102, -6000, -3800, -15000, 180)
    SetChrPos(0x103, -7200, -3800, -13800, 180)
    SetChrPos(0x104, -6000, -3800, -13800, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1899")
    SetChrPos(0x151, -4800, -3800, -14400, 180)

    label("loc_1899")

    StopEffect(0x1, 0x2)
    OP_0D()

    #C0037
    ChrTalk(
        0x101,
        (
            "#5P#0005Fこ、これってもしかして……\x01",
            "トマさんの婚約指輪か？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            "#5P#0205F湖に落ちた指輪を\x01",
            "飲み込んでいた……\x01",
            "そういうことでしょうか。\x02\x03",

            "#0206F……天文学的低確率の\x01",
            "現象かと思われますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#12P#0106Fそ、そうね……\x01",
            "さすがにこれは\x01",
            "予想できなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_19DD")

    #C0040
    ChrTalk(
        0x151,
        (
            "#11P#5709Fあっはっは！\x01",
            "そんなまさか、だよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DD")


    #C0041
    ChrTalk(
        0x104,
        (
            "#11P#0306F散々歩かされて\x01",
            "結果がこれってのも\x01",
            "なんか釈然としねぇ気がするが……\x02\x03",

            "#0300Fま、とりあえず見つかって\x01",
            "結果オーライってとこか。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそうだな……\x01",
            "一応、トマさんにも\x01",
            "確認してもらうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x9)
    OP_65(0x0, 0x1)
    SetChrPos(0x0, -7200, -3800, -15000, 180)
    StopEffect(0x8, 0x2)
    EventEnd(0x5)
    Return()

    # Function_14_1806 end

    SaveToFile()

Try(main)
