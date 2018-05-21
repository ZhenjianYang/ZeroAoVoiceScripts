from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1550.bin",                # FileName
        "t1550",                    # MapName
        "t1550",                    # Location
        0x0052,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 82, 0, 1, 0, 3],
    )

    BuildStringList((
        "t1550",                  # 0
        "シズク",                 # 1
        "ミハイル",               # 2
        "ミハイル",               # 3
        "ゲバル議員",             # 4
        "セシル",                 # 5
        "看護師シロン",           # 6
        "看護師メイファ",         # 7
        "ヨアヒム准教授",         # 8
        "ダイソン用務員",         # 9
        "エステル",               # 10
        "ヨシュア",               # 11
        "観光客マシュ",           # 12
    ))

    AddCharChip((
        "chr/ch29900.itc",                   # 00
        "apl/ch50137.itc",                   # 01
        "apl/ch50145.itc",                   # 02
        "apl/ch50105.itc",                   # 03
        "chr/ch05300.itc",                   # 04
        "chr/ch07100.itc",                   # 05
        "chr/ch29800.itc",                   # 06
        "chr/ch20200.itc",                   # 07
        "apl/ch50144.itc",                   # 08
        "chr/ch00600.itc",                   # 09
        "chr/ch00700.itc",                   # 0A
        "chr/ch34400.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
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

    DeclNpc(-97739,  699,     56169,   180,  341,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(6050,    699,     -47549,  270,  341,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(6050,    400,     -47549,  0,    469,  0x0, 0,   8,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-55299,  699,     -47750,  270,  341,  0x0, 0,   1,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-100589, 0,       57319,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-55020,  0,       -49520,  0,    389,  0x0, 0,   0,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-55020,  0,       -49520,  0,    389,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4809,    0,       -48900,  45,   389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-5579,   0,       7090,    0,    389,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-99220,  0,       55110,   45,   405,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-99819,  0,       55990,   90,   405,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-8310,   0,       25229,   90,   385,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)

    DeclActor(-22570,  0,       32610,   1200,    -22570,  1500,    32610,   0x007C, 0,  23, 0x0000)
    DeclActor(-98310,  0,       54690,   1200,    -97740,  1500,    56170,   0x007E, 0,  4,  0x0000)
    DeclActor(-6430,   0,       25360,   1200,    -6430,   1500,    25360,   0x007C, 0,  22, 0x0000)

    ScpFunction((
        "Function_0_334",          # 00, 0
        "Function_1_3EC",          # 01, 1
        "Function_2_5C3",          # 02, 2
        "Function_3_5CA",          # 03, 3
        "Function_4_7DB",          # 04, 4
        "Function_5_1AA4",         # 05, 5
        "Function_6_1F92",         # 06, 6
        "Function_7_2BAD",         # 07, 7
        "Function_8_2BC8",         # 08, 8
        "Function_9_2D92",         # 09, 9
        "Function_10_2ECA",        # 0A, 10
        "Function_11_447C",        # 0B, 11
        "Function_12_479A",        # 0C, 12
        "Function_13_54E3",        # 0D, 13
        "Function_14_575E",        # 0E, 14
        "Function_15_585E",        # 0F, 15
        "Function_16_5BB4",        # 10, 16
        "Function_17_5DE1",        # 11, 17
        "Function_18_5F3E",        # 12, 18
        "Function_19_5FDF",        # 13, 19
        "Function_20_6030",        # 14, 20
        "Function_21_7A05",        # 15, 21
        "Function_22_80F7",        # 16, 22
        "Function_23_8172",        # 17, 23
        "Function_24_87B8",        # 18, 24
        "Function_25_9384",        # 19, 25
        "Function_26_A28B",        # 1A, 26
    ))


    def Function_0_334(): pass

    label("Function_0_334")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_374"),
        (1, "loc_380"),
        (2, "loc_38C"),
        (3, "loc_398"),
        (4, "loc_3A4"),
        (5, "loc_3B0"),
        (6, "loc_3BC"),
        (SWITCH_DEFAULT, "loc_3C8"),
    )


    label("loc_374")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_380")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_38C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_398")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D4")

    label("loc_3EB")

    Return()

    # Function_0_334 end

    def Function_1_3EC(): pass

    label("Function_1_3EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_404")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 2)

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_417")
    SetChrFlags(0x8, 0x80)
    Jump("loc_595")

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_44A")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, 4810, 0, -48900, 45)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_595")

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_45D")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_595")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_481")
    SetChrPos(0xC, -99220, 0, 56180, 90)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_595")

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4C0")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, 4810, 0, -48900, 45)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, -10240, 0, 7490, 0)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_595")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4E9")
    SetChrPos(0xC, 4810, 0, -48900, 45)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_595")

    label("loc_4E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4F7")
    Jump("loc_595")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_50A")
    SetChrFlags(0x9, 0x80)
    Jump("loc_595")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_52E")
    SetChrPos(0xC, -99220, 0, 56180, 90)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_595")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_53C")
    Jump("loc_595")

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_54F")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_595")

    label("loc_54F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_55D")
    Jump("loc_595")

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_56B")
    Jump("loc_595")

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_57E")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_595")

    label("loc_57E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_58C")
    Jump("loc_595")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_595")

    label("loc_595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8")
    ClearChrFlags(0x13, 0x80)

    label("loc_5A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C2")
    Event(0, 20)

    label("loc_5C2")

    Return()

    # Function_1_3EC end

    def Function_2_5C3(): pass

    label("Function_2_5C3")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_5C3 end

    def Function_3_5CA(): pass

    label("Function_3_5CA")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_61E")
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Jump("loc_705")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_62C")
    Jump("loc_705")

    label("loc_62C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_63A")
    Jump("loc_705")

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_648")
    Jump("loc_705")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_663")
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Jump("loc_705")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_671")
    Jump("loc_705")

    label("loc_671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_67F")
    Jump("loc_705")

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_69A")
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    Jump("loc_705")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6A8")
    Jump("loc_705")

    label("loc_6A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6B6")
    Jump("loc_705")

    label("loc_6B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6C4")
    Jump("loc_705")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6D2")
    Jump("loc_705")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_6E0")
    Jump("loc_705")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_6EE")
    Jump("loc_705")

    label("loc_6EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_6FC")
    Jump("loc_705")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_705")

    label("loc_705")

    ClearMapObjFlags(0x2, 0x10)
    SetMapObjFlags(0x3, 0x10)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x0, 0x1)

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_745")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x0, 0x1)

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75D")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x0, 0x1)

    label("loc_75D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_775")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x0, 0x1)

    label("loc_775")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78B")
    OP_66(0x1, 0x1)

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A7")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7DA")

    label("loc_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7DA")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DA")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_7DA")

    Return()

    # Function_3_5CA end

    def Function_4_7DB(): pass

    label("Function_4_7DB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86F")
    Jump("loc_8B9")

    label("loc_86F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_88F")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B9")

    label("loc_88F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AF")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B9")

    label("loc_8AF")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B9")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8EC")
    Jump("loc_1A9C")

    label("loc_8EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_98C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_907")
    Call(0, 5)
    Jump("loc_987")

    label("loc_907")


    #C0001
    ChrTalk(
        0x8,
        (
            "#1500F明日はお父さんが迎えに来るので\x01",
            "今日は早く寝ないといけませんね。\x02\x03",

            "#1502Fふふ……楽しみすぎて、\x01",
            "あんまり眠れないかも。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_987")

    Jump("loc_1A9C")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A7")
    Call(0, 5)
    Jump("loc_A02")

    label("loc_9A7")


    #C0002
    ChrTalk(
        0x8,
        (
            "#1502F明日の外出日はキーアちゃんにも\x01",
            "会いに行こうと思ってます。\x02\x03",

            "ふふ……楽しみだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A02")

    Jump("loc_1A9C")

    label("loc_A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A22")
    Call(0, 15)
    Jump("loc_D32")

    label("loc_A22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B31")

    #C0003
    ChrTalk(
        0x8,
        (
            "#1500F皆さん、本当に\x01",
            "ありがとうございました。\x02\x03",

            "#1508Fなんだか余り物を\x01",
            "渡してしまったようで\x01",
            "ちょっと気が引けますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0000Fはは、そんなこと無いよ。\x01",
            "大事にさせてもらうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#1500Fそうしていただけると\x01",
            "すごく……嬉しいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BA4")

    label("loc_B31")


    #C0006
    ChrTalk(
        0x8,
        (
            "#1500F完成したプレゼント、\x01",
            "お父さんもきっと\x01",
            "喜んでくれると思います。\x02\x03",

            "皆さん、本当に\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA4")

    Jump("loc_D32")

    label("loc_BA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BDE")
    Call(0, 25)
    Jump("loc_D32")

    label("loc_BDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_C89")

    #C0007
    ChrTalk(
        0x8,
        (
            "#1508Fすみません、皆さん。\x01",
            "突然ワガママを\x01",
            "聞いてもらって……\x02\x03",

            "どうか……\x01",
            "よろしくお願いしますね。\x02\x03",

            "#1508Fあの、本当に時間が\x01",
            "あったらで結構ですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D32")

    label("loc_C89")


    #C0008
    ChrTalk(
        0x8,
        (
            "#1500Fキーアちゃんは、私にとっても\x01",
            "気の置けない大事な友達です。\x02\x03",

            "#1502Fふふ、不思議ですよね。\x01",
            "出会ってすぐに\x01",
            "友達になれちゃうなんて。\x02\x03",

            "また会うのが楽しみだなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D32")

    Jump("loc_1A9C")

    label("loc_D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_D45")
    Jump("loc_1A9C")

    label("loc_D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_D53")
    Jump("loc_1A9C")

    label("loc_D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E42")

    #C0009
    ChrTalk(
        0x8,
        (
            "#1500F今日はセシルさんに\x01",
            "散歩に連れて行ってもらうんです。\x02\x03",

            "私は目は見えないですけど\x01",
            "セシルさんがいてくれるから\x01",
            "とっても楽しいんですよ。\x02\x03",

            "#1502Fふふ……あんなお姉さんがいて\x01",
            "ロイドさんが凄くうらやましいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E95")

    label("loc_E42")


    #C0010
    ChrTalk(
        0x8,
        (
            "#1500Fセシルさんに散歩に\x01",
            "連れて行ってもらうんです。\x02\x03",

            "ふふ、早く来ないかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E95")

    Jump("loc_1A9C")

    label("loc_E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1010")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F97")

    #C0011
    ChrTalk(
        0x8,
        (
            "#1500Fお父さんは今日も色んな場所を\x01",
            "飛び回ってるみたいです。\x02\x03",

            "最近では外国の方に\x01",
            "出張することも多くなって……\x02\x03",

            "#1505F……あ、えっと……\x01",
            "寂しくはないんですよ？\x02\x03",

            "#1502Fむしろ、みんなから頼られていて\x01",
            "鼻が高いくらいなんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100B")

    label("loc_F97")


    #C0012
    ChrTalk(
        0x8,
        (
            "#1500Fお父さんは今日も色んな場所を\x01",
            "飛び回ってるみたいです。\x02\x03",

            "ふふ、お父さんは売れっ子ですから\x01",
            "仕方ないんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100B")

    Jump("loc_1A9C")

    label("loc_1010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1021")
    Call(0, 13)
    Jump("loc_1A9C")

    label("loc_1021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_116C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EA")

    #C0013
    ChrTalk(
        0x8,
        (
            "#1505Fあっ、ロイドさん達……\x02\x03",

            "#1508F……今って、記念祭なんですよね。\x01",
            "なんだか実感が湧かなくて……\x02\x03",

            "すぐそこで楽しいことが起こっているのに\x01",
            "まるで遠い世界のことみたい……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1167")

    label("loc_10EA")


    #C0014
    ChrTalk(
        0x8,
        (
            "#1502F……すみません、\x01",
            "折角来てくれたのに\x01",
            "こんな話をしてしまって。\x02\x03",

            "わたしは大丈夫ですから\x01",
            "あまり気にしないで下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1167")

    Jump("loc_1A9C")

    label("loc_116C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_152D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1482")

    #C0015
    ChrTalk(
        0x8,
        (
            "#1505Fあ……もしかして……\x01",
            "特務支援課の皆さん？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0005Fえっ！？\x01",
            "まだ声をかけてないのに\x01",
            "よく分かったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#1500Fふふ、なんとなく\x01",
            "聞いたことのある足音だと思って。\x02\x03",

            "セシルさんやロイドさんたちみたいな\x01",
            "印象深い人の足音は結構覚えてるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0005F足音って……\x01",
            "それで判断できるのって\x01",
            "かなりすごいことだと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#1500Fえ、えへへ……\x02\x03",

            "#1500Fでもほんと、足音って\x01",
            "人それぞれなんですよ。\x02\x03",

            "例えば……よくお見舞いに来て下さる\x01",
            "遊撃士の方やお父さんなんかは、\x01",
            "歩き方にもっと隙がない感じですし。\x02",
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

    #C0020
    ChrTalk(
        0x104,
        "#0306F……隙だらけなのかな、俺たち。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        "#0206Fちょっとショックです。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0100Fまぁまぁ……\x01",
            "アリオスさんに比べたら誰だって\x01",
            "過小評価にはなっちゃうわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 7)
    Jump("loc_1528")

    label("loc_1482")


    #C0023
    ChrTalk(
        0x8,
        (
            "#1508Fえ、ええっと……\x01",
            "なにか失礼なことを\x01",
            "言っちゃいましたか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0000Fい、いやいや気にしないで。\x01",
            "俺たちがまだまだ\x01",
            "力不足ってだけだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "#1505F？\x02",
    )

    CloseMessageWindow()

    label("loc_1528")

    Jump("loc_1A9C")

    label("loc_152D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_182A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1773")

    #C0026
    ChrTalk(
        0x8,
        (
            "#1500Fあ、ロイドさんたち……\x01",
            "こんにちは。\x02\x03",

            "この前、セシルさんに\x01",
            "皆さんの活躍を聞きました。\x02\x03",

            "リットンさんを襲った魔獣たちを\x01",
            "ロイドさん達がやっつけたって……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#0100F実際は、わたし達の力だけじゃ\x01",
            "解決できなかったでしょうけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        "#0203Fツァイトの力添えあってこそでした。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#1500Fいえ、それでも……\x01",
            "知り合いが活躍したって聞いて\x01",
            "なんだか嬉しかったです。\x02\x03",

            "#1502F大変なお仕事だと思いますけど……\x01",
            "これからもがんばってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0002Fうん、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0309Fシズクちゃんみたいな\x01",
            "可愛い子ちゃんの応援がありゃ\x01",
            "パワー１００倍だっつーの！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 6)
    Jump("loc_1825")

    label("loc_1773")


    #C0032
    ChrTalk(
        0x8,
        (
            "#1500Fこのまま特務支援課が\x01",
            "大活躍していったら……\x02\x03",

            "ふふっ……\x01",
            "ロイドさんたちもお父さんくらい\x01",
            "強くなっちゃうのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0000Fか、かなり難しそうだけど\x01",
            "頑張らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1825")

    Jump("loc_1A9C")

    label("loc_182A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1A77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A15")

    #C0034
    ChrTalk(
        0x8,
        (
            "#1500Fわたし、目が見えなくなってから\x01",
            "耳がよくなったみたいなので……\x01",
            "音を聞いたことは間違いないと思います。\x02\x03",

            "#1508Fだけど、あのキーンっていう\x01",
            "おかしな音の正体は\x01",
            "よく分からなくて……\x02\x03",

            "#1505F……すみません。\x01",
            "あまり役立つ情報じゃ\x01",
            "なかったですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#0004Fいや……\x01",
            "君は今まで捜査上にない\x01",
            "新しい情報をくれたんだ。\x02\x03",

            "#0000Fお陰でさっきは\x01",
            "捜査の裏も取れたしね。\x02\x03",

            "その音も、きっと捜査を進める上で\x01",
            "重要なヒントになると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "#1502Fあ……だったら嬉しいです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A72")

    label("loc_1A15")


    #C0037
    ChrTalk(
        0x8,
        (
            "#1500F調査、頑張ってください。\x02\x03",

            "わたしの聞いた音……\x01",
            "何かの役に立てばいいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A72")

    Jump("loc_1A9C")

    label("loc_1A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1A85")
    Jump("loc_1A9C")

    label("loc_1A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1A93")
    Jump("loc_1A9C")

    label("loc_1A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1A9C")

    label("loc_1A9C")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_4_7DB end

    def Function_5_1AA4(): pass

    label("Function_5_1AA4")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xC, 0xFF)
    OP_68(-97720, 1000, 55960, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -99230, 0, 55030, 45)
    SetChrPos(0x102, -99560, 0, 54100, 45)
    SetChrPos(0x103, -99230, 0, 56050, 90)
    SetChrPos(0x104, -98280, 0, 53800, 0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0x8, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C04")

    #C0038
    ChrTalk(
        0x8,
        (
            "#1505Fあっ、皆さん……！\x02\x03",

            "#1502F昨日は本当に\x01",
            "ありがとうございました……！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0000Fはは、いいって。\x01",
            "こっちも良い物貰っちゃったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#0100Fしかし、シズクさん。\x01",
            "今日はずいぶん嬉しそうですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5F")

    label("loc_1C04")


    #C0041
    ChrTalk(
        0x8,
        "#1502Fあっ……こんにちは！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0000Fはは、こんにちは。\x01",
            "なんだか随分うれしそうだね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5F")


    #C0043
    ChrTalk(
        0x8,
        (
            "#1502Fあ、えへへ……\x02\x03",

            "その、明日の外出日に\x01",
            "街に行くことになったんです。\x02\x03",

            "お父さんの仕事が\x01",
            "一区切りがついたらしくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0305Fへぇ、あの超多忙なオッサンが\x01",
            "よく都合がついたじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E06")

    #C0045
    ChrTalk(
        0x102,
        (
            "#0102Fふふ、良かったじゃない。\x02\x03",

            "これで昨日のプレゼントも\x01",
            "ちゃんと渡せるわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#1500Fえへへ、はい……！\x02\x03",

            "#1505F……あ……\x01",
            "それで、もし良かったら……\x02\x03",

            "#1502Fキーアちゃんに会いに\x01",
            "お邪魔したいんですけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E92")

    label("loc_1E06")


    #C0047
    ChrTalk(
        0x102,
        "#0102Fふふ、良かったじゃない。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#1500Fは、はい。\x01",
            "それで、もし良かったら……\x02\x03",

            "#1502Fキーアちゃんに会いに\x01",
            "お邪魔したいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E92")


    #C0049
    ChrTalk(
        0x101,
        (
            "#0002Fああ、もちろん歓迎するよ。\x02\x03",

            "俺たちは仕事だけど、\x01",
            "課長とキーアはいるだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        (
            "#0204F……キーアの喜ぶ顔が\x01",
            "眼に浮かびますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#1502F……ありがとうございます！\x02\x03",

            "ふふ……精一杯おめかしして\x01",
            "行っちゃいますね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -99230, 0, 55030, 45)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0xCC, 2)
    EventEnd(0x5)
    Return()

    # Function_5_1AA4 end

    def Function_6_1F92(): pass

    label("Function_6_1F92")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2026")
    Jump("loc_2070")

    label("loc_2026")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2046")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2070")

    label("loc_2046")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2066")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2070")

    label("loc_2066")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2070")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2127")

    #C0052
    ChrTalk(
        0xFE,
        (
            "今日はシズクちゃん、\x01",
            "クロスベル市の方に出かけるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "普段あまり外に出れないんだから\x01",
            "しっかり楽しんできてほしいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_2127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2135")
    Jump("loc_2BA5")

    label("loc_2135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2240")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E5")

    #C0054
    ChrTalk(
        0xFE,
        "コホ、コホ……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "あ、大丈夫……\x01",
            "ちょっと発作が出ているだけだから\x01",
            "心配しなくていいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "あとでセシルさんが来てくれることに\x01",
            "なってるしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_223B")

    label("loc_21E5")


    #C0057
    ChrTalk(
        0xFE,
        "コホ、コホ……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "大丈夫……\x01",
            "薬を飲んだらすぐに収まるから\x01",
            "心配しなくていいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223B")

    Jump("loc_2BA5")

    label("loc_2240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2411")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22D3")

    #C0059
    ChrTalk(
        0xFE,
        (
            "シズクちゃん、明後日には\x01",
            "お父さんと会えるんだよね。\x01",
            "うらやましいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "僕のぶんもいっぱい\x01",
            "楽しんできてほしいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240C")

    label("loc_22D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2362")

    #C0061
    ChrTalk(
        0xFE,
        (
            "僕も、シズクちゃんのために\x01",
            "何かしてあげたかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "箱くらいしか\x01",
            "あげるものはないけど……\x01",
            "役に立ててよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240C")

    label("loc_2362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2376")
    Call(0, 26)
    Jump("loc_240C")

    label("loc_2376")


    #C0063
    ChrTalk(
        0xFE,
        (
            "この前、レマン自治州にいる\x01",
            "お父さんたちから手紙と一緒に\x01",
            "贈り物が届いたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "僕が欲しがってた\x01",
            "おもちゃが入っててさ……\x01",
            "あれは嬉しかったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240C")

    Jump("loc_2BA5")

    label("loc_2411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_249F")

    #C0065
    ChrTalk(
        0xFE,
        (
            "僕の手術……成功すればいいけど、\x01",
            "失敗すればお父さんたちのミラは\x01",
            "ムダになっちゃうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "僕はどうしたらいいんだろう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_249F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_24DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24BA")
    Call(0, 9)
    Jump("loc_24DA")

    label("loc_24BA")


    #C0067
    ChrTalk(
        0xFE,
        "やっぱり、手術は怖いよ……\x02",
    )

    CloseMessageWindow()

    label("loc_24DA")

    Jump("loc_2BA5")

    label("loc_24DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_265D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D2")

    #C0068
    ChrTalk(
        0xFE,
        (
            "レマン自治州にいるお父さんたちから\x01",
            "手紙が届いたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "お父さんたちも、\x01",
            "僕の入院費と手術費のために\x01",
            "一生懸命働いてくれてるんだね……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "なかなか会えなくて寂しいけど……\x01",
            "シズクちゃんもいるし僕は大丈夫だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2658")

    label("loc_25D2")


    #C0071
    ChrTalk(
        0xFE,
        (
            "レマン自治州にいるお父さんたちから\x01",
            "手紙が届いたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "なかなか会えなくて寂しいけど……\x01",
            "シズクちゃんもいるし僕は大丈夫だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2658")

    Jump("loc_2BA5")

    label("loc_265D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_266B")
    Jump("loc_2BA5")

    label("loc_266B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_273C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26FC")

    #C0073
    ChrTalk(
        0xFE,
        "明日は記念祭のパレードだね。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "ボクも出来ればシズクちゃんと一緒に\x01",
            "見にいきたかったけど……\x01",
            "今年は無理かな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2737")

    label("loc_26FC")


    #C0075
    ChrTalk(
        0xFE,
        (
            "パレード……シズクちゃんと一緒に\x01",
            "見に行きたかったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2737")

    Jump("loc_2BA5")

    label("loc_273C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2793")

    #C0076
    ChrTalk(
        0xFE,
        "記念祭かぁ……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生は、\x01",
            "今頃釣りを楽しんでるのかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_2793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_27EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AE")
    Call(0, 8)
    Jump("loc_27EA")

    label("loc_27AE")


    #C0078
    ChrTalk(
        0xFE,
        (
            "こほこほ……\x01",
            "ボクは……記念祭は\x01",
            "行けそうにないかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27EA")

    Jump("loc_2BA5")

    label("loc_27EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_28C7")

    #C0079
    ChrTalk(
        0xFE,
        (
            "ボクの方が少し年下だけど、\x01",
            "シズクちゃんとはお友達なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "よく一緒に散歩したり、\x01",
            "シズクちゃんの病室で\x01",
            "おしゃべりしたりしてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "ボクもシズクちゃんも\x01",
            "入院して長いから、気が合うのかもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_28C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_295F")

    #C0082
    ChrTalk(
        0xFE,
        (
            "シズクちゃんは\x01",
            "ボクともよくお話してくれるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "……目が見えないのって\x01",
            "どんな気持ちなんだろう……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "きっとすっごく寂しいよね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_295F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_29DE")

    #C0085
    ChrTalk(
        0xFE,
        (
            "セシルおねえちゃん、\x01",
            "さっきわざわざ\x01",
            "声をかけにきてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "……ボクもあんな\x01",
            "優しい人になりたいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_29DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF3")

    #C0087
    ChrTalk(
        0xFE,
        (
            "あ……セシルおねえちゃん、\x01",
            "こんにちは。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x136,
        "#1300Fミハイル君、体の具合はどう？\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "うん……大分調子はいいみたいだよ。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x136,
        (
            "#1304Fそっか……よかった。\x02\x03",

            "#1300F何かあったらナースコールしてね。\x01",
            "私達がすぐに飛んでいくから。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "うん……ありがと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B97")

    label("loc_2AF3")


    #C0092
    ChrTalk(
        0xFE,
        (
            "ボク、レマン自治州からこの病院に\x01",
            "入院してきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "先生には、外科手術をしないと\x01",
            "治らないって言われたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "……やっぱり怖いな、手術なんて……\x02",
    )

    CloseMessageWindow()

    label("loc_2B97")

    Jump("loc_2BA5")

    label("loc_2B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2BA5")

    label("loc_2BA5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1F92 end

    def Function_7_2BAD(): pass

    label("Function_7_2BAD")

    TalkBegin(0xFE)

    #C0095
    ChrTalk(
        0xFE,
        "すう、すう……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_2BAD end

    def Function_8_2BC8(): pass

    label("Function_8_2BC8")

    TurnDirection(0xF, 0x9, 0)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0xF, 0xFF)

    #C0096
    ChrTalk(
        0x9,
        "こほ、こほこほ……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xF,
        (
            "#2403Fんー、少し発作が出てるね。\x01",
            "あとで薬を飲んでおきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        "はい……こほ、こほ。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "……ところで、ヨアヒム先生は\x01",
            "記念祭の間はどうするの？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xF,
        (
            "#2405Fんー……どうだろうねぇ。\x02\x03",

            "#2400Fいつもどおりどこかで釣り糸を\x01",
            "垂らしてるかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "え……お祭りは見に行かないの？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xF,
        (
            "#2406Fあまりゴミゴミした所は\x01",
            "好きじゃないんだよね。\x02\x03",

            "釣りだと魚が逃げる状況だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        "とことん釣り好きなんだね……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_8_2BC8 end

    def Function_9_2D92(): pass

    label("Function_9_2D92")

    TurnDirection(0xC, 0x9, 0)
    SetChrSubChip(0x9, 0x1)
    OP_4B(0xC, 0xFF)

    #C0104
    ChrTalk(
        0xC,
        (
            "#1300Fミハイル君……\x01",
            "やっぱり、まだ手術の決心はできない？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "うん、でも……\x01",
            "やっぱり怖くて……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        (
            "#1304F……ふふ、そっか。\x01",
            "いいのよ、無理しなくても。\x02\x03",

            "#1300F先生たちは、ミハイル君が決心のつくまで\x01",
            "出来る限りのことをしてくれるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        "……ありがとう、セシルお姉ちゃん……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_9_2D92 end

    def Function_10_2ECA(): pass

    label("Function_10_2ECA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F5E")
    Jump("loc_2FA8")

    label("loc_2F5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FA8")

    label("loc_2F7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F9E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FA8")

    label("loc_2F9E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FA8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_32DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323F")

    #C0108
    ChrTalk(
        0xFE,
        (
            "昨日から、ハルトマン議長が\x01",
            "わしを消そうとしているという\x01",
            "疑念が尽きん……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長の口添えで入院した以上、\x01",
            "わしにも監視がついてるに違いない……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "な、なんとか病院を抜けて、\x01",
            "帝国方面にでも高飛びしなければ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3237")

    #C0111
    ChrTalk(
        0x10A,
        (
            "#0600F（……以前脱税疑惑が発覚した\x01",
            "  帝国派のゲバル議員……\x01",
            "  こんな所に隠れていたのか。）\x02\x03",

            "#0603F（だがあれ以来、事件は完全に隠され……\x01",
            "  ゲバル議員の話など\x01",
            "  まったく耳にしていない。）\x02\x03",

            "#0600F（ハルトマン議長は完全に\x01",
            "  彼を見捨てたと見て間違いない。\x01",
            "  命の危険などないだろうに……）\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#0103F（その事にも気づいていないなんて\x01",
            "  哀れな人ですね……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3237")

    SetScenarioFlags(0x0, 2)
    Jump("loc_32D5")

    label("loc_323F")


    #C0113
    ChrTalk(
        0xFE,
        (
            "と、とにかく……\x01",
            "一刻も早く病院を抜け出す方法を\x01",
            "考えなくては。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "早くしなければ、\x01",
            "ハルトマン議長が私を消すために\x01",
            "仕掛けてくるに違いない……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D5")

    Jump("loc_4474")

    label("loc_32DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3515")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_343C")

    #C0115
    ChrTalk(
        0xFE,
        (
            "不正が発覚したわしに\x01",
            "病院に身を隠せと助言してくれた\x01",
            "ハルトマン議長……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "だが、いつまでたっても\x01",
            "わしには復帰の時期が伝えられぬ……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "よもやハルトマン議長、\x01",
            "わしが秘密裏に各界にコネを作り、\x01",
            "足場を固めていたのを知っていたのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "だ、だとすると……わしは近いうちに\x01",
            "消されてしまうんじゃ……！？\x01",
            "ひ、ひぃいい……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3510")

    label("loc_343C")


    #C0119
    ChrTalk(
        0xFE,
        (
            "わ、わしは別にハルトマン議長を\x01",
            "出し抜こうとしたわけじゃない……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "ほんのちょっぴりウマイ汁を\x01",
            "すすろうとしただけなんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "し、しかしこのままでは\x01",
            "近いうちに消されてしまう。\x01",
            "な、なんとかしなければ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3510")

    Jump("loc_4474")

    label("loc_3515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E3")

    #C0122
    ChrTalk(
        0xFE,
        (
            "不正のほとぼりが冷めるまで\x01",
            "入院して身を隠すつもりだったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "どうやら、わしの担当が\x01",
            "あの師長になってしまったようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "うぬぬ、どうにも住みにくく\x01",
            "なってきおったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_363B")

    label("loc_35E3")


    #C0125
    ChrTalk(
        0xFE,
        "あの師長には命令をしづらくてかなわん。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "くそ、なんで議員のわしがこんな目に……\x02",
    )

    CloseMessageWindow()

    label("loc_363B")

    Jump("loc_4474")

    label("loc_3640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3789")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3708")

    #C0127
    ChrTalk(
        0xFE,
        "まったく信じられん……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "ちょっとナースステーションに\x01",
            "入ったくらいで、何でこのわしが\x01",
            "叩き出されねばならん！\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "だ、だがあの師長の迫力には\x01",
            "何故だか逆らえんわい……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3784")

    label("loc_3708")


    #C0130
    ChrTalk(
        0xFE,
        "あの師長の迫力には何故だか逆らえん……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "自治州議員として\x01",
            "絶対の権力を持つこのわしが、\x01",
            "病院内の権力に屈するとは……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3784")

    Jump("loc_4474")

    label("loc_3789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3876")

    #C0132
    ChrTalk(
        0xFE,
        (
            "……はぁ……\x01",
            "いたずらに看護師を呼んで\x01",
            "暇を潰しても、気は晴れん。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "わしの不正など、入院しているうちに\x01",
            "ハルトマン議長が\x01",
            "もみ消してくれるはずなのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "いつになったらわしは\x01",
            "自治州議会に復帰できるんじゃろうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4474")

    label("loc_3876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_38C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3891")
    Call(0, 11)
    Jump("loc_38C4")

    label("loc_3891")


    #C0135
    ChrTalk(
        0xFE,
        (
            "まったく近頃の子供は……\x01",
            "ぶつぶつぶつ…………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38C4")

    Jump("loc_4474")

    label("loc_38C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3990")

    #C0136
    ChrTalk(
        0xFE,
        (
            "病院にしばらく入院したことにして\x01",
            "不正発覚のほとぼりが冷めるのを待て……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "ハルトマン議長はそう言ったのだ。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "わ、わしはいつまでここに\x01",
            "隠れていればいいんだ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A19")

    label("loc_3990")


    #C0139
    ChrTalk(
        0xFE,
        (
            "わしがやってしまった脱税など、\x01",
            "もう市民の頭から\x01",
            "忘れられていていいはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "わ、わしはいつまでここに\x01",
            "隠れていればいいんだ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A19")

    Jump("loc_4474")

    label("loc_3A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3C09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B95")

    #C0141
    ChrTalk(
        0xFE,
        (
            "明日はミシュラムで\x01",
            "アレが行われる日だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "今年はこんな状態のせいで\x01",
            "招待状は届かなかったが\x01",
            "来年こそは……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#0005F（ミシュラム……確か市内港湾区からの\x01",
            "  水上バスで行ける保養地だったか。）\x02\x03",

            "#0000F（こういう人が遊びに行くんだな……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#0300F（高級ブティックやらレストランが\x01",
            "  立ち並ぶところだからな。\x01",
            "  まぁ不思議じゃないだろ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C04")

    label("loc_3B95")


    #C0145
    ChrTalk(
        0xFE,
        (
            "ミシュラムで明日、\x01",
            "アレが行われる……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "今年はこんな状態のせいで\x01",
            "招待状は届かなかったが\x01",
            "来年こそは……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C04")

    Jump("loc_4474")

    label("loc_3C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3CF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CA2")

    #C0147
    ChrTalk(
        0xFE,
        "この病院は娯楽が少なくてつまらん。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "本来記念祭ともなれば、\x01",
            "毎晩宴会に参加して歓楽街で\x01",
            "ホステスをはべらせるものを……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CEE")

    label("loc_3CA2")


    #C0149
    ChrTalk(
        0xFE,
        (
            "ナースに手を出そうとすれば\x01",
            "あの師長が黙ってないだろうし……\x01",
            "うぬぬ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CEE")

    Jump("loc_4474")

    label("loc_3CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DED")

    #C0150
    ChrTalk(
        0xFE,
        (
            "昨日から少しは食事がマシになると\x01",
            "聞いておったが……\x01",
            "豆腐のハンバーグだと？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "まったく子供だましもいいところだ。\x01",
            "昼はステーキにワインと\x01",
            "決まっておるだろうが！\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0006F（ど、どんだけ贅沢に\x01",
            "  暮らしてたんだ……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E20")

    label("loc_3DED")


    #C0153
    ChrTalk(
        0xFE,
        (
            "昼はステーキにワインと\x01",
            "決まっておるだろうが！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E20")

    Jump("loc_4474")

    label("loc_3E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED7")

    #C0154
    ChrTalk(
        0xFE,
        (
            "そういえば来月はもう、\x01",
            "クロスベルの創立記念祭だのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "記念祭といえば……\x01",
            "そうじゃ、あのイベントが……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "くくく、\x01",
            "楽しみになってきたわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F50")

    label("loc_3ED7")


    #C0157
    ChrTalk(
        0xFE,
        (
            "あのイベント……\x01",
            "昨年はハルトマン議長のツテで\x01",
            "参加させてもらったんじゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "くくく、\x01",
            "楽しみになってきたわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F50")

    Jump("loc_4474")

    label("loc_3F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3FF4")

    #C0159
    ChrTalk(
        0xFE,
        (
            "病院食が質素でつまらんのでな。\x01",
            "ステーキとワインを追加するよう言ったが\x01",
            "だれも聞く耳を持たん。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "ちっ……サービスのなってない\x01",
            "病院だわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4474")

    label("loc_3FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4083")

    #C0161
    ChrTalk(
        0xFE,
        (
            "魔物よけのフェンスが\x01",
            "設置されたようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "ふっふっふ、分かればいい。\x01",
            "このわしの安全は\x01",
            "しかと守ってもらわんとな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4474")

    label("loc_4083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4094")
    Call(0, 16)
    Jump("loc_4474")

    label("loc_4094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_446B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B0")

    #C0163
    ChrTalk(
        0xFE,
        (
            "聞けば一週間前、\x01",
            "この病院の職員が\x01",
            "魔獣の襲撃にあったという。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "一体どうなっとるんだ。\x01",
            "わしの安全は\x01",
            "保証されてるんだろうな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        (
            "#0301F（なんだこのオッサン……\x01",
            "  個室に入院してるにしちゃ\x01",
            "  妙に元気だな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#0101F（この人……\x01",
            "  ちょっと前にクロスベルタイムズで\x01",
            "  見たことがあるわ。）\x02\x03",

            "#0103F（確か、不正が発覚した直後に\x01",
            "  体調不良で入院した\x01",
            "  議員の人だったと思うけど……）\x02\x03",

            "#0101F（実際は、ほとぼりが覚めるまで\x01",
            "  病院に隠れているって所でしょう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        (
            "#0200F（仮病で個室を\x01",
            "  陣取ってるわけですか……\x01",
            "  最悪ですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        (
            "#0101F（帝国派の議長の腰巾着だったから\x01",
            "  印象を悪くしないように\x01",
            "  ここに押し込められたのね。）\x02\x03",

            "#0103F（きっと今、戻ってきても\x01",
            "  政府に彼のポストはないでしょう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#0003F（トカゲの尻尾切りってやつか……\x01",
            "  なんだか哀れだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 2)
    Jump("loc_4466")

    label("loc_43B0")


    #C0170
    ChrTalk(
        0xFE,
        (
            "聞けば一週間前、\x01",
            "この病院の職員が\x01",
            "魔獣の襲撃にあったという。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "……設備投資を\x01",
            "怠ったんじゃあるまいな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "わしが魔獣に襲われたりしたら\x01",
            "ハルトマン議長が黙っちゃおらんぞ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4466")

    Jump("loc_4474")

    label("loc_446B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4474")

    label("loc_4474")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_2ECA end

    def Function_11_447C(): pass

    label("Function_11_447C")

    TurnDirection(0xE, 0xB, 0)
    SetChrSubChip(0xB, 0x1)
    OP_4B(0xE, 0xFF)

    #C0173
    ChrTalk(
        0xB,
        (
            "おい君、わしの方が先に呼んだのに\x01",
            "別の患者を優先するとは\x01",
            "どういうことかね！\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xB,
        (
            "わしはクロスベル自治州議会の\x01",
            "議員なのだぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xE,
        (
            "す、すみません。\x01",
            "ちょっとそちらの患者さんの方が\x01",
            "緊急を要したものですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xE,
        (
            "（雑誌を買いに行くくらいで\x01",
            "  看護師を使おうと\x01",
            "  するなっつーの……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        "#0001F（険悪なムードだなぁ……）\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x153,
        (
            "#1111F……ねー、おじさん。\x01",
            "あんまりワガママばっかり言ってたら\x01",
            "おしりをたたかれちゃうよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x153, 500)

    #C0179
    ChrTalk(
        0xB,
        "な、なにぃ……？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xE,
        "ぷっ……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xB,
        (
            "こ、こら、何を笑っておるか！！\x01",
            "……まったく最近の子供は……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4703")

    #C0182
    ChrTalk(
        0x102,
        "#0100Fふふ、キーアちゃんったら賢いんだから。\x02",
    )

    CloseMessageWindow()
    Jump("loc_478B")

    label("loc_4703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4743")

    #C0183
    ChrTalk(
        0x103,
        "#0203Fさすが、キーアは怖いもの知らずですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_478B")

    label("loc_4743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_478B")

    #C0184
    ChrTalk(
        0x104,
        (
            "#0309Fハハッ、さすがキー坊。\x01",
            "議員センセイも形無しだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478B")

    SetChrSubChip(0xB, 0x0)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_11_447C end

    def Function_12_479A(): pass

    label("Function_12_479A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_47AB")
    Jump("loc_54DF")

    label("loc_47AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_4943")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48AE")

    #C0185
    ChrTalk(
        0xC,
        (
            "#1304Fミハイル君、\x01",
            "薬を飲んだらぐっすり寝ちゃったわ。\x02\x03",

            "#1300F発作は突然来るから\x01",
            "やっぱり心配だけど……\x02\x03",

            "シズクちゃんの存在や\x01",
            "ご両親の手紙に支えられて\x01",
            "病気に負けずにいるのはいいことよね。\x02\x03",

            "#1308Fあとは手術さえ受けてくれれば……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_493E")

    label("loc_48AE")


    #C0186
    ChrTalk(
        0xC,
        (
            "#1300Fミハイル君の発作は心配だけど……\x01",
            "シズクちゃんやご両親のおかげで\x01",
            "心が折れずに済んでるみたい。\x02\x03",

            "#1308Fあとは手術さえ受けてくれれば……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_493E")

    Jump("loc_54DF")

    label("loc_4943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49E9")

    #C0187
    ChrTalk(
        0xC,
        (
            "#1302F（ふふっ……\x01",
            "  昨日はどうもありがとう。）\x02\x03",

            "#1304F（シズクちゃんにとっては\x01",
            "  良い事が連続したわね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#0005F？？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A6B")

    label("loc_49E9")


    #C0189
    ChrTalk(
        0xC,
        (
            "#1300F（あ、ロイド。\x01",
            "  いい所に来てくれたわ。）\x02\x03",

            "（シズクちゃんの話を\x01",
            "  聞いてあげてくれる？）\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        "#0005F（あ、ああ……？）\x02",
    )

    CloseMessageWindow()

    label("loc_4A6B")

    Jump("loc_4BD6")

    label("loc_4A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B4C")

    #C0191
    ChrTalk(
        0xC,
        (
            "#1300Fうふふ、シズクちゃんったら\x01",
            "今までの入院生活で一番嬉しそうね。\x02\x03",

            "#1304F私もイリアに会えるってなったら、\x01",
            "やっぱりあんな顔をすると思うし。\x02\x03",

            "#1302F普段あまり遠くに行けない分、\x01",
            "楽しんで来てほしいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD6")

    label("loc_4B4C")


    #C0192
    ChrTalk(
        0xC,
        (
            "#1300Fうふふ、シズクちゃんったら\x01",
            "今までの入院生活で一番嬉しそうね。\x02\x03",

            "お父さんとお出かけできる上に\x01",
            "友達とも会えるんだもの、当然よね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD6")

    Jump("loc_54DF")

    label("loc_4BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_513E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF6")
    Call(0, 15)
    Jump("loc_5139")

    label("loc_4BF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F3F")

    #C0193
    ChrTalk(
        0xC,
        (
            "#1302Fふふ、みんなありがとう。\x01",
            "シズクちゃんに協力してくれて。\x02\x03",

            "#1301Fそれはそうと……\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#0005Fど、どうしたのセシル姉？\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "#1302Fふふっ、まさか警備隊の\x01",
            "娘さんと付き合ってるなんて。\x02\x03",

            "#1309Fロイドも隅におけないんだから♪\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D35")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4D35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D5D")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4D5D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D85")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4D85")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DAD")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4DAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DD5")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4DD5")

    Sleep(1000)

    #C0196
    ChrTalk(
        0x109,
        (
            "#0505Fへっ……？\x02\x03",

            "あ、あたしの事ですか……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0011Fち、違うってばセシル姉……！\x01",
            "こちらはノエル曹長といって\x01",
            "任務で同行してくれてるだけで……\x02\x03",

            "#0006Fっていうか、女性を連れてくるたびに\x01",
            "その反応をするつもりかよっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        "#0106F（う、うーん、相変わらず……）\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        "#0200F（セシルさんらしいですね。）\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        "#0309F（いいキャラだぜ、セシルさん！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 1)
    Jump("loc_5000")

    label("loc_4F3F")


    #C0201
    ChrTalk(
        0xC,
        (
            "#1305Fなんだ……結局ノエルさんも\x01",
            "彼女じゃないのね。\x02\x03",

            "#1306Fまったく、お姉ちゃんはいつになったら\x01",
            "甥っ子か姪っ子の顔を見られるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#0006Fセシル姉、\x01",
            "ツッコむのもいい加減疲れるよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5000")

    Jump("loc_5139")

    label("loc_5005")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_503A")
    Call(0, 25)
    Jump("loc_5139")

    label("loc_503A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5129")

    #C0203
    ChrTalk(
        0xC,
        (
            "#1300Fシズクちゃんが\x01",
            "お父さんにプレゼントを\x01",
            "渡したいらしいの。\x02\x03",

            "ウルスラ病院内で\x01",
            "材料になるものが見つかったら、\x01",
            "持って来てもらえる？\x02\x03",

            "あなたたちならきっと、\x01",
            "素敵な材料を見つけられると思うわ。\x01",
            "どうかよろしくお願いね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5139")

    label("loc_5129")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5139")
    Call(0, 24)

    label("loc_5139")

    Jump("loc_54DF")

    label("loc_513E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_5388")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52EE")

    #C0204
    ChrTalk(
        0xC,
        (
            "#1300Fあらロイド……\x01",
            "ヨアヒム先生とは話せたかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#0006Fああ、そ、それなんだけど……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キーアが検査入院を嫌がって\x01",
            "逃げてしまった事を説明した。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xC,
        "#1305Fまぁ……そうだったの。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#0001Fとにかく、今はキーアを\x01",
            "探しているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xC,
        (
            "#1303Fうーん、生憎見ていないわ。\x02\x03",

            "#1308Fさっきの今なら、そう遠くへは\x01",
            "行っていないとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#0000Fそっか……\x01",
            "悪い、ありがとうセシル姉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 4)
    Jump("loc_5383")

    label("loc_52EE")


    #C0211
    ChrTalk(
        0xC,
        (
            "#1308Fキーアちゃんのことだから\x01",
            "何処かに隠れたりとかは\x01",
            "してないと思うけど……\x02\x03",

            "#1300Fとにかく、色々と探してみなさい。\x01",
            "私も見かけたら連絡するわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5383")

    Jump("loc_54DF")

    label("loc_5388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_5447")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53A3")
    Call(0, 9)
    Jump("loc_5442")

    label("loc_53A3")


    #C0212
    ChrTalk(
        0xC,
        (
            "#1300Fヨアヒム先生なら\x01",
            "屋上の研究棟にいると思うわ。\x02\x03",

            "呑気そうな人だけど\x01",
            "とても優秀なお医者様なのよ。\x02\x03",

            "キーアちゃんのことも、\x01",
            "何か分かるかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5442")

    Jump("loc_54DF")

    label("loc_5447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5455")
    Jump("loc_54DF")

    label("loc_5455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5463")
    Jump("loc_54DF")

    label("loc_5463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5474")
    Call(0, 13)
    Jump("loc_54DF")

    label("loc_5474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5482")
    Jump("loc_54DF")

    label("loc_5482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5490")
    Jump("loc_54DF")

    label("loc_5490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_549E")
    Jump("loc_54DF")

    label("loc_549E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_54AC")
    Jump("loc_54DF")

    label("loc_54AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_54BA")
    Jump("loc_54DF")

    label("loc_54BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_54C8")
    Jump("loc_54DF")

    label("loc_54C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_54D6")
    Jump("loc_54DF")

    label("loc_54D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_54DF")

    label("loc_54DF")

    TalkEnd(0xFE)
    Return()

    # Function_12_479A end

    def Function_13_54E3(): pass

    label("Function_13_54E3")

    TurnDirection(0xC, 0x8, 0)
    SetChrSubChip(0x8, 0x2)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D8")

    #C0213
    ChrTalk(
        0x8,
        (
            "#1502Fセシルさんは初日に\x01",
            "休暇をとってたんですよね？\x02\x03",

            "記念祭はどうでした？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "#1300Fふふ、とっても楽しかったわよ。\x02\x03",

            "#1304Fロイドとアルカンシェルの公演を見て、\x01",
            "そのあとイリアたちとご飯を食べて……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        "#1500Fわぁ、よかったですね。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        (
            "#1304F……ね、シズクちゃん。\x02\x03",

            "#1300F今年はもう休みが取れないけれど……\x01",
            "来年の記念祭は一緒に行かない？\x02\x03",

            "#1309Fロイドたちとアリオスさんと、\x01",
            "みんなで行きましょ。\x01",
            "きっと楽しいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "#1502F……はい！\x01",
            "ぜひご一緒させてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5755")

    label("loc_56D8")


    #C0218
    ChrTalk(
        0xC,
        (
            "#1309F来年の記念祭は\x01",
            "ロイドたちとアリオスさんと、\x01",
            "みんなで行きましょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "#1502F……はい！\x01",
            "ぜひご一緒させてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5755")

    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_54E3 end

    def Function_14_575E(): pass

    label("Function_14_575E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F9")

    #C0220
    ChrTalk(
        0xFE,
        "ふーん、とっても広い病院ね。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "まぁ……\x01",
            "わたしのおうちの方が\x01",
            "もっと広くて大きいと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "……ほ、ほんとなんだからっ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_585A")

    label("loc_57F9")


    #C0223
    ChrTalk(
        0xFE,
        (
            "この病院より、わたしのおうちの方が\x01",
            "もっと広くて大きいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "……ほ、ほんとなんだからっ。\x02",
    )

    CloseMessageWindow()

    label("loc_585A")

    TalkEnd(0xFE)
    Return()

    # Function_14_575E end

    def Function_15_585E(): pass

    label("Function_15_585E")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xC, 0xFF)
    OP_68(-98260, 800, 56110, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19530, 0)
    SetChrPos(0x101, -99650, 0, 54550, 45)
    SetChrPos(0x102, -100000, 0, 53550, 45)
    SetChrPos(0x103, -98500, 0, 53800, 0)
    SetChrPos(0x104, -97830, 0, 53030, 0)
    SetChrPos(0x109, -100480, 0, 55530, 89)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0xC, 0xB4, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0x8, 0x2)
    OP_0D()

    #C0225
    ChrTalk(
        0xC,
        (
            "#5P#1302Fあら、ロイド。\x01",
            "ふふっ、いらっしゃい。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        "#11P#1502Fあっ……こんにちは！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#6P#0000F２人とも、こんにちは。\x02\x03",

            "シズクちゃん。\x01",
            "この前はどうもありがとう。\x02\x03",

            "キーアと友達になってくれてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#11P#1505Fそ、そんな。\x01",
            "わたしの方こそ……\x02\x03",

            "#1502Fあの、キーアちゃん元気ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x104,
        (
            "#12P#0300Fあぁ、元気すぎて\x01",
            "困っちまうくらいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#6P#0102Fふふっ。\x01",
            "毎日どたばたして楽しいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x103,
        (
            "#12P#0203F……相変わらず記憶の方は\x01",
            "手がかりナシ、ですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        (
            "#11P#1508Fそうですか……\x02\x03",

            "#1502Fあの、キーアちゃんに伝えてください。\x01",
            "いつか遊びに行くねって……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、分かった。\x01",
            "その時は俺たちも大歓迎するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xC,
        "#5P#1302Fくす……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -99250, 0, 54950, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0xCC, 0)
    EventEnd(0x5)
    Return()

    # Function_15_585E end

    def Function_16_5BB4(): pass

    label("Function_16_5BB4")

    TalkBegin(0xD)
    TurnDirection(0xD, 0xB, 0)
    SetChrSubChip(0xB, 0x1)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D52")

    #C0235
    ChrTalk(
        0xB,
        (
            "キサマ……昨日、\x01",
            "わしのシーツにトマトソースを\x01",
            "ぶちまけた看護師か。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        "なんだ、謝罪にでも来たのか？\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xD,
        (
            "えっと……そうなんです。\x01",
            "どうもごめんなさいでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xD,
        (
            "こぼしたシーツも洗ったので\x01",
            "ついでに交換しに来ました。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xD,
        (
            "……あはは、ソースを\x01",
            "こぼした所がシミになってる。\x01",
            "おねしょしたみたーい。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        (
            "な、なめておるのか……？\x01",
            "そういう時は普通、\x01",
            "新品を持ってくるじゃろうが！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5DD5")

    label("loc_5D52")


    #C0241
    ChrTalk(
        0xD,
        (
            "あはは、やだこのシーツ～。\x01",
            "おねしょしたみたーい。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xB,
        (
            "え、ええい、笑うな！\x01",
            "他人に聞かれたら\x01",
            "どう思われるか分からんだろうが！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD5")

    SetChrSubChip(0xB, 0x0)
    OP_4C(0xD, 0xFF)
    TalkEnd(0xD)
    Return()

    # Function_16_5BB4 end

    def Function_17_5DE1(): pass

    label("Function_17_5DE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5DF2")
    Jump("loc_5F3A")

    label("loc_5DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_5E66")

    #C0243
    ChrTalk(
        0xFE,
        (
            "あいたた……\x01",
            "女の子にぶつかって\x01",
            "思わず尻餅ついちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "まったく、なんなのよあの子は……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3A")

    label("loc_5E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_5F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E81")
    Call(0, 11)
    Jump("loc_5F3A")

    label("loc_5E81")


    #C0245
    ChrTalk(
        0xFE,
        (
            "（ぷぷ……理不尽な事で\x01",
            "  怒られてムカっときてたけど、\x01",
            "  なんだか和んじゃったわ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "（ありがとね、お嬢ちゃん。）\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x153,
        (
            "#1100Fうん？　……えへへ、\x01",
            "よく分かんないけどよかったね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F3A")

    TalkEnd(0xFE)
    Return()

    # Function_17_5DE1 end

    def Function_18_5F3E(): pass

    label("Function_18_5F3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F53")
    Call(0, 8)
    Jump("loc_5FDB")

    label("loc_5F53")


    #C0248
    ChrTalk(
        0xFE,
        (
            "#2400Fあとは……サボる機会があればいいなぁ。\x01",
            "記念祭中もガッツリと\x01",
            "仕事が入ってるんだよね。\x02\x03",

            "#2406Fやれやれ、准教授も楽じゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FDB")

    TalkEnd(0xFE)
    Return()

    # Function_18_5F3E end

    def Function_19_5FDF(): pass

    label("Function_19_5FDF")

    TalkBegin(0xFE)

    #C0249
    ChrTalk(
        0xFE,
        "おっと……こんな時間か。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "私もそろそろ日誌を書きに戻るとしよう。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_5FDF end

    def Function_20_6030(): pass

    label("Function_20_6030")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50105.itc", 0x1E)
    OP_68(-99110, 1000, 54740, 0)
    MoveCamera(52, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(29860, 0)
    SetChrPos(0x101, -99440, 50, 49020, 0)
    SetChrPos(0x102, -100540, 50, 49020, 0)
    SetChrPos(0x103, -100540, 0, 47910, 0)
    SetChrPos(0x104, -99440, 0, 47910, 0)
    SetChrPos(0xC, -99210, 0, 55670, 90)
    SetChrSubChip(0x8, 0x2)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01500.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(28860, 2000)

    def lambda_614C():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_614C)

    def lambda_6161():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6161)
    Sleep(100)

    def lambda_6175():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6175)

    def lambda_618A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_618A)
    Sleep(50)

    def lambda_619E():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_619E)

    def lambda_61B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_61B3)
    Sleep(80)

    def lambda_61C7():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_61C7)

    def lambda_61DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_61DC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0251
    ChrTalk(
        0x101,
        "#0005F#12Pあ、セシル姉……\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_628E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_628E)
    WaitChrThread(0xC, 1)

    #C0252
    ChrTalk(
        0xC,
        "#1305F#5Pあら、ロイド。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #N0253
    NpcTalk(
        0x8,
        "少女",
        "#1505F#5Pあ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_68(-99570, 1000, 55330, 2500)
    SetCameraDistance(27360, 2500)

    def lambda_62F9():
        OP_95(0xFE, -99720, 0, 54250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62F9)
    Sleep(200)

    def lambda_6316():
        OP_95(0xFE, -100830, 0, 54280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6316)
    Sleep(100)

    def lambda_6333():
        OP_95(0xFE, -100790, 0, 53070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6333)
    Sleep(150)

    def lambda_6350():
        OP_95(0xFE, -99570, 0, 53110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6350)
    OP_93(0xC, 0x10E, 0x12C)

    def lambda_6371():
        OP_95(0xFE, -100070, 0, 55900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6371)
    WaitChrThread(0xC, 1)
    SetChrSubChip(0x8, 0x2)
    OP_93(0xC, 0xB4, 0x12C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    #C0254
    ChrTalk(
        0x101,
        (
            "#0000F#12P師長さんから\x01",
            "ここにいるって聞いてさ。\x02\x03",

            "その、お邪魔だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        "#1309F#5Pふふ、大丈夫よ。\x02",
    )

    CloseMessageWindow()

    def lambda_6422():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6422)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0256
    ChrTalk(
        0xC,
        (
            "#1302F#6P──シズクちゃん。\x01",
            "いま話してたお兄さんたちよ。\x02\x03",

            "クロスベル警察に勤めてる\x01",
            "正義のお巡りさんなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        "#0011F#12Pせ、正義のって……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        (
            "#0109F#6Pさすがにそれは\x01",
            "過大評価だと思いますけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0259
    NpcTalk(
        0x8,
        "少女",
        "#1502F#5P……クスクス。\x02",
    )

    CloseMessageWindow()
    OP_68(-98580, 1000, 56100, 2000)

    def lambda_6534():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6534)
    Sleep(50)

    def lambda_6544():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6544)
    Sleep(50)

    def lambda_6554():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6554)
    Sleep(50)

    def lambda_6564():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6564)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("少女")

    #A0260
    AnonymousTalk(
        0xFF,
        (
            "えっと、その……\x01",
            "お仕事、お疲れさまです。\x02\x03",

            "わたしはシズク……\x01",
            "シズク・マクレインっていいます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0261
    ChrTalk(
        0x101,
        "#0009F#6Pはは……ありがとう。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0262
    ChrTalk(
        0x101,
        "#0005F#6Pって、あれ……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        "#0105F#6Pマクレインって……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        "#0303F#12Pんー、どこかで聞いたような。\x02",
    )

    CloseMessageWindow()

    def lambda_66F3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_66F3)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0265
    ChrTalk(
        0xC,
        (
            "#1304F#5Pふふ、ひょっとしたら\x01",
            "面識があるかもしれないわね。\x02\x03",

            "#1300Fシズクちゃんのお父さんは\x01",
            "アリオスさんっていうんだけど。\x02",
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

    #C0266
    ChrTalk(
        0x101,
        "#0011F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x103,
        "#0205F#6P《風の剣聖》……\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x104,
        "#0305F#12Pあのオッサン、娘がいたのかよ！？\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x8,
        (
            "#1505F#5Pえっと……皆さんは、\x01",
            "お父さんのお知り合いなんですか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_689E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_689E)

    #C0270
    ChrTalk(
        0x101,
        (
            "#0012F#6Pい、いやぁ、知り合いというか。\x02\x03",

            "#0000F前に危ないところを\x01",
            "助けてもらったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#1500F#5Pふふ、そうだったんですか。\x02\x03",

            "うちのお父さん、無愛想だから\x01",
            "お気を悪くされませんでした？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#0011F#6Pそ、そんな、とんでもない。\x02\x03",

            "#0003Fこんな凄い人がいるんだなって\x01",
            "身が引き締まったっていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        (
            "#0104F#6P厳しいけど思いやりがあって、\x01",
            "頼りになりそうな方だったわ。\x02\x03",

            "#0102Fふふ、素敵なお父様ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "#1502F#5Pえ、えへへ……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "#1309F#6Pうふふ、シズクちゃんは\x01",
            "お父さんっ子だものねぇ。\x02\x03",

            "#1302Fそのくせ、お父さんが訪ねても\x01",
            "遠慮してあんまり甘えないし……\x02\x03",

            "#1309F『お父さん大好き！』とか言って\x01",
            "抱きついちゃえばいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        "#1501F#5Pセ、セシルさんったらぁ……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        "#0009F#6Pはは……\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x104,
        (
            "#0302F#12P（あの凄腕のオッサンが\x01",
            "  娘に甘えられてる構図か……）\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        "#0204F#6P（少し想像しにくいですね……）\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6BFE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6BFE)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0280
    ChrTalk(
        0xC,
        (
            "#1301F#5Pそういえば、例の件なんだけど。\x02\x03",

            "実は、ここにいるシズクちゃんが\x01",
            "気付いたことがあるらしくって。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x101,
        "#0005F#6P気付いたこと……？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "#1508F#5Pえっと、その……\x01",
            "リットンさんが襲われた\x01",
            "晩のことなんですけど。\x02\x03",

            "わたし、眠れなかったから\x01",
            "点字の本を読んでいて……\x02\x03",

            "その時、悲鳴みたいなのが\x01",
            "聞こえてきたんです。\x02",
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

    #C0283
    ChrTalk(
        0x101,
        "#0001F#6P本当かい……！？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        "#0101F#6Pそれで……どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#1508F#5Pその、気になったので\x01",
            "そこの窓を開けて\x01",
            "耳を澄ませたんですけど……\x02\x03",

            "それ以上、悲鳴は聞こえなくて\x01",
            "かわりにハッハッハッって\x01",
            "息づかいみたいな音が聞こえて……\x02\x03",

            "しばらくしたらタンタンって\x01",
            "何かはねるような音が聞こえて……\x02\x03",

            "えっと……それで終わりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        (
            "#0003F#6Pそっか……\x02\x03",

            "#0001Fその事は、警備隊の人には？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        (
            "#1501F#5Pその、わたしずっと\x01",
            "夢でも見たのかと思ってて……\x02\x03",

            "さっきセシルさんから話を聞いて\x01",
            "初めてその事だって気づいて……\x02\x03",

            "#1508Fご、ごめんなさい……\x01",
            "もっと早くに言ってれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        "#0002F#6Pいや、いいんだよ。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        "#0104F#6Pありがとう、教えてくれて。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        (
            "#0203F#6Pしかし……屋上での調査を\x01",
            "完全に裏付ける証言ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x104,
        (
            "#0303F#12Pああ、最初の悲鳴ってのが\x01",
            "あの研修医が気絶した時……\x02\x03",

            "#0301Fそして、狼型魔獣の息遣いと\x01",
            "あの木箱やらに飛び乗って\x01",
            "逃げていった時の音みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        (
            "#1501F#5Pそ、それと……\x02\x03",

            "その、わたしの空耳かも\x01",
            "しれないですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0293
    ChrTalk(
        0x101,
        (
            "#0000F#6P……いいよ。\x01",
            "気になった事は何でも言ってみて。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "#1501F#5Pは、はい。\x02\x03",

            "その……さっき話した音が\x01",
            "聞こえてる最中なんですけど……\x02\x03",

            "なにか……\x01",
            "キーンってかすれた音が\x01",
            "聞こえたような気がしたんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0295
    ChrTalk(
        0x103,
        "#0205F#6Pキーンとかすれた音……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        (
            "#0301F#12Pふむ、特定の魔獣が発する、\x01",
            "独自の鳴き声かなんかか……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        "#0101F#6Pその音は、普段は聞こえないのね？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x8,
        (
            "#1505F#5Pはい……\x01",
            "あの晩だけだと思います。\x02\x03",

            "#1508Fその……やっぱりわたしの\x01",
            "空耳の可能性もあるかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0004F#6Pいや……\x01",
            "貴重な証言、ありがとう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7429():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7429)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0300
    ChrTalk(
        0x101,
        (
            "#0001F#12P──セシル姉。\x01",
            "色々と分かったことがあるから\x01",
            "一通り報告させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xC,
        "#1304F#5Pうん、分かったわ。\x02",
    )

    CloseMessageWindow()

    def lambda_74B4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_74B4)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0302
    ChrTalk(
        0xC,
        (
            "#1300F#6Pそれじゃあシズクちゃん。\x01",
            "また夕食の時に来るわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "#1502F#5Pはい。\x01",
            "お仕事頑張ってください。\x02\x03",

            "ロイドさんたちも……\x01",
            "調査、頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7567():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7567)
    WaitChrThread(0x101, 1)

    #C0304
    ChrTalk(
        0x101,
        "#0002F#6Pうん、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        "#0102F#6Pまた遊びに来るわね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-22470, 1000, 30420, 0)
    MoveCamera(38, 19, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27250, 0)
    SetChrPos(0xC, -22510, 0, 32970, 180)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -21910, 0, 29950, 0)
    SetChrPos(0x102, -23180, 0, 29950, 0)
    SetChrPos(0x103, -23180, 0, 28850, 0)
    SetChrPos(0x104, -21910, 0, 28850, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x3)
    FadeToBright(1000, 0)
    SetCameraDistance(26250, 2000)
    OP_6F(0x10)

    def lambda_767E():
        OP_95(0xFE, -22510, 0, 31530, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_767E)

    def lambda_7698():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_7698)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xC, 2)

    def lambda_76B1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_76B1)
    WaitChrThread(0xC, 1)
    Sleep(300)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    Sleep(500)

    #C0306
    ChrTalk(
        0x101,
        (
            "#0001F#12Pセシル姉。\x01",
            "その、彼女は……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_770E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_770E)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0307
    ChrTalk(
        0xC,
        (
            "#1303F#5Pうん……数年前の事故で\x01",
            "目の光をね。\x02\x03",

            "#1300Fでも、まったく回復の\x01",
            "見込みがないわけじゃないの。\x02\x03",

            "少しずつ回復治療を受けながら\x01",
            "療養生活をしているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        "#0003F#12Pそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        "#0206F#6P……大変ですね。\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xC,
        (
            "#1304F#5Pふふ……\x01",
            "とっても健気な子でね。\x02\x03",

            "お父さんが忙しい人だから\x01",
            "滅多に会えずに寂しいでしょうに\x01",
            "わざと明るく振る舞って……\x02\x03",

            "#1302Fあなたたちも良かったら\x01",
            "今後とも仲良くしてあげてね？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        "#0000F#12Pああ……よろこんで。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        (
            "#0104F#6Pそうですね。\x01",
            "とっても良い子みたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#0202F#6P……ですね。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x104,
        (
            "#0309F#12P俺の素敵トークで\x01",
            "あの子を笑顔にしてやりますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "#1309F#5Pふふ、ありがとう。\x02\x03",

            "#1300Fさてと……\x01",
            "何か分かったんでしょう？\x02\x03",

            "改めて聞かせてもらえるかしら？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    AddParty(0x35, 0xFF, 0xFF)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_6030 end

    def Function_21_7A05(): pass

    label("Function_21_7A05")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-98750, 1100, 54900, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16000, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrSubChip(0x8, 0x2)
    OP_68(-98640, 1200, 56080, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0316
    ChrTalk(
        0x11,
        (
            "#0802F#6Pへえ、面白い～！\x01",
            "点字付きの絵本なんてあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x12,
        "#0902F#6Pそうか、絵も立体的なんだね。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#1500F#5Pふふ……まだあんまり\x01",
            "数は多くないみたいですけど。\x02\x03",

            "わたし、将来は\x01",
            "こういうものを作れるように\x01",
            "なりたいんです。\x02\x03",

            "#1510F目が見えないわたしでも\x01",
            "何とかなるかなって……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        "#0808F#6Pシズクちゃん……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x12,
        (
            "#0901F#6P……君の場合、\x01",
            "いずれ視力を取り戻せる\x01",
            "可能性があるんだよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x8,
        (
            "#1510F#5P……はい、先生たちは\x01",
            "そう言ってくれるんですけど……\x02\x03",

            "ダメだった時のことも\x01",
            "考えておかないとって思って……\x02\x03",

            "#1508F……ご、ごめんなさい。\x01",
            "こんなことエステルさんたちに\x01",
            "言っても仕方ないのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x11,
        (
            "#0801F#6Pこ～ら！\x01",
            "そんな風に遠慮しないの！\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x11, 0xFA, 0x0, 0xFA, 0x3E8, 0x0)
    SetChrName("")

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エステルはシズクの手をぎゅっと握りしめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0324
    ChrTalk(
        0x8,
        "#1505F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x11,
        (
            "#0802F#6Pいいじゃない！\x01",
            "目が見える子も、見えない子も\x01",
            "一緒に楽しめる絵本作り！\x02\x03",

            "#0809Fあたしはすっごく素敵だと思うな！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x12,
        (
            "#0904F#6P確かにこの絵本からは\x01",
            "作者の真心やぬくもりが\x01",
            "手触りで感じられるからね……\x02\x03",

            "#0900Fそういったものを\x01",
            "作りたいと思う気持ちは\x01",
            "大切にしていいと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "#1505F#5Pエステルさん、ヨシュアさん……\x02\x03",

            "#1510Fぐすっ……\x01",
            "ありがとうございます……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    #C0328
    ChrTalk(
        0x11,
        (
            "#0805F#6Pわわっ！\x01",
            "ちょっとシズクちゃん……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x12,
        (
            "#0902F#6Pはは……\x01",
            "変なこと言ってゴメンね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_68(-22870, 1300, 33250, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -22180, 0, 32330, 315)
    SetChrPos(0x102, -23190, 0, 32030, 45)
    SetChrPos(0x103, -22730, 0, 31110, 0)
    SetChrPos(0x104, -24450, 0, 31390, 45)
    OP_71(0x3, 0x5, 0x5, 0x0, 0x0)
    OP_68(-22870, 1300, 32250, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0330
    ChrTalk(
        0x101,
        (
            "#0002F（うーん……\x01",
            "  訪ねてみたはいいけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        (
            "#0109F（な、何だかちょっと\x01",
            "  邪魔しちゃ悪そうな雰囲気ね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x104,
        "#0304F#5P（ま、次の機会に訪ねようぜ。）\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        "#0202F（ですね……）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -22600, 0, 31500, 0)
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    SetScenarioFlags(0xB7, 1)
    EventEnd(0x5)
    Return()

    # Function_21_7A05 end

    def Function_22_80F7(): pass

    label("Function_22_80F7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　　　　 リネン室 　　　　　　\x01",
            "※職員以外の立入はご遠慮ください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_80F7 end

    def Function_23_8172(): pass

    label("Function_23_8172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82EF")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82A8")
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("医師の声")

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……くん、調子はどうかね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("少女の声")

    #A0336
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……あ、はい。\x01",
            "変わりありません。\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("医師の声")

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうしたね、\x01",
            "元気がないようだが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("少女の声")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "え……い、いえ。\x01",
            "何でもないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x136,
        "#1303F……先生が診察に来ているみたい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x68, 1)

    label("loc_82A8")


    #C0340
    ChrTalk(
        0x101,
        (
            "#0000F聞き込みをしたかったけど……\x01",
            "ここは後回しにしよう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_87B5")

    label("loc_82EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8387")
    TalkBegin(0xFF)
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("女性の声")

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……それでね……なのよ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("少女の声")

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……クスクス……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#0003F（取り込み中みたいだな……）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_87B5")

    label("loc_8387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_849E")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 1)), scpexpr(EXPR_END)), "loc_8493")
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("シズクの声")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "す、すみません、突然\x01",
            "泣き出したりしちゃって……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("エステルの声")

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あはは、いいのいいの。\x02\x03",

            "……よしシズクちゃん、\x01",
            "今日はお姉さんに\x01",
            "たーんと甘えてよね！\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#0004F（邪魔しちゃ悪いな。\x01",
            "  ……もう行こうか。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8496")

    label("loc_8493")

    Call(0, 21)

    label("loc_8496")

    TalkEnd(0xFF)
    Jump("loc_87B5")

    label("loc_849E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87B5")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875D")
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("医師の声")

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "シズクくん、調子はどうかね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("シズクの声")

    #A0348
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、ベルダイン先生。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("医師の声")

    #A0349
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふむ？\x01",
            "いつもより血色がいいな。\x02\x03",

            "何かいいことでもあったのかね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("シズクの声")

    #A0350
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、えっと……\x01",
            "今日はちょっと楽しみがあって。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("医師の声")

    #A0351
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そうか……\x01",
            "いいことだな。\x02\x03",

            "……まあいい。\x01",
            "では診察を始めさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("シズクの声")

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "えぇ、よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#0003Fシズクちゃん……\x01",
            "診察中みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x153,
        "#1111Fロイド、このお部屋は？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x101,
        (
            "#0005Fああ、そういえばキーアは\x01",
            "知らなかったか。\x02\x03",

            "#0000Fよし、それじゃあ\x01",
            "あとでもう一回\x01",
            "顔を出しに来てみよう。\x02\x03",

            "キーアにはその時紹介するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x153,
        (
            "#1106Fうーん？\x02\x03",

            "#1110Fよくわかんないけど、\x01",
            "わかった～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 0)
    Jump("loc_87B2")

    label("loc_875D")


    #C0357
    ChrTalk(
        0x101,
        (
            "#0000Fシズクちゃんは診察中だ。\x02\x03",

            "先にヨアヒム先生のところを\x01",
            "尋ねてみるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B2")

    TalkEnd(0xFF)

    label("loc_87B5")

    SetChrName("")
    Return()

    # Function_23_8172 end

    def Function_24_87B8(): pass

    label("Function_24_87B8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-98260, 800, 56110, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19530, 0)
    SetChrPos(0x101, -99650, 0, 54550, 45)
    SetChrPos(0x102, -100000, 0, 53550, 45)
    SetChrPos(0x103, -98500, 0, 53800, 0)
    SetChrPos(0x104, -97830, 0, 53030, 0)
    SetChrPos(0x109, -100480, 0, 55530, 89)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0358
    ChrTalk(
        0xC,
        (
            "#5P#1305Fあ、そういえば……\x02\x03",

            "#1300F……ねえ、みんな。\x01",
            "もし時間が空いていたら\x01",
            "手伝ってもらえないかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0359
    ChrTalk(
        0x8,
        (
            "#11P#1505Fあ……！\x01",
            "も、もしかして……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x101,
        (
            "#6P#0005F？？？\x01",
            "何か事情があるみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x8,
        (
            "#11P#1505Fセ、セシルさん、\x01",
            "いいんです……！\x02\x03",

            "ただのわたしの\x01",
            "ワガママですから……！\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xC,
        (
            "#5P#1309Fもう、そんな風に\x01",
            "遠慮ばっかりしないの。\x02\x03",

            "#1300F──実はね、シズクちゃんの\x01",
            "お父さんの誕生日が近づいてるの。\x02\x03",

            "それでシズクちゃん、\x01",
            "プレゼントをお父さんに\x01",
            "渡したいみたいなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#12P#0105Fへえ……\x01",
            "アリオスさんの誕生日ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x104,
        (
            "#12P#0309Fあの凄腕のオッサンにも\x01",
            "そんなモンがあるんだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x103,
        "#12P#0203Fランディさん、当たり前です。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#6P#0000Fなるほど、ひょっとして\x01",
            "プレゼント選びを相談したいとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#11P#1505Fい、いえ、その……\x02\x03",

            "#1500Fわたし、手作りのお守りを\x01",
            "お父さんにプレゼントしようと\x01",
            "思ってて……\x02\x03",

            "その材料になりそうなものを\x01",
            "探そうと思ってるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        "#6P#0000Fああ、そういう事か！\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x109,
        (
            "#6P#0504Fふふ、身の回りにある\x01",
            "『ちょっと良いもの』を使って\x01",
            "大切な人へのお守りを作る……\x02\x03",

            "#0500F昔からのクロスベルの風習ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        "#12P#0300Fへえ、そんなのがあんのか。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#12P#0102Fふふっ、私も昔おじいさまに\x01",
            "似たようなお守りを作ったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x103,
        (
            "#12P#0200Fそれでは、この病院の中から\x01",
            "お守りになりそうな材料を\x01",
            "探してくる……\x02\x03",

            "それでいいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        "#11P#1502F……は、はい……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xC,
        (
            "#5P#1304Fあなたたちならきっと、\x01",
            "素敵な材料を見つけられると思うの。\x02\x03",

            "#1300Fもし見つかったらでいいから\x01",
            "持ってきてくれないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#6P#0000Fああ、もちろん喜んで。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x104,
        (
            "#12P#0300Fシズクちゃんのためとあれば、\x01",
            "一肌脱ぐしかないだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#11P#1500Fす、すみません……\x01",
            "よろしくお願いします……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        (
            "#6P#0003Fあとは、何を作るかが問題だな。\x01",
            "集めるものの指針が\x01",
            "欲しいところだけど……\x02\x03",

            "#0000F何か、作りたいものとかは\x01",
            "決まっているかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#11P#1505Fそ、そうですね……\x02\x03",

            "#1502F実はこの前、\x01",
            "セシルさんと散歩中に、\x01",
            "手触りのいい石を拾ったんです。\x02\x03",

            "セシルさんに確認してもらったら、\x01",
            "とても美しい石だというので\x01",
            "大事にしまっているんですが……\x02\x03",

            "それが何かに使えないかなって。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xC,
        (
            "#5P#1300Fそうね、私もそれが良いと思う。\x02\x03",

            "見せてもらったけど、\x01",
            "触ると優しい温かさを感じる\x01",
            "不思議な石なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x104,
        "#12P#0305Fへぇ、そんなものがあるのか。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x102,
        (
            "#12P#0102Fだったら、\x01",
            "その石を何かに活かす形で\x01",
            "考えた方がよさそうね。\x02\x03",

            "#0104Fそれと、せっかく\x01",
            "プレゼントするなら\x01",
            "包装用の箱も用意しなきゃ。\x02\x03",

            "#0100F箱とリボンも一緒に\x01",
            "探してみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#6P#0000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x8,
        (
            "#11P#1508Fす、すみません、\x01",
            "面倒なことを言ってしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、大丈夫だよ。\x01",
            "おかげで集める材料の指針も\x01",
            "決まったし。\x02\x03",

            "それじゃ、さっそく\x01",
            "探しに行ってみるとするか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0386
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【父へのプレゼント】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50500, 1000, 57500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_29(0x2C, 0x4, 0x2)
    SetChrPos(0x0, -99300, 0, 54000, 0)
    SetChrPos(0x1, -99300, 0, 54000, 0)
    SetChrPos(0x2, -99300, 0, 54000, 0)
    SetChrPos(0x3, -99300, 0, 54000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    TurnDirection(0xC, 0x8, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_87B8 end

    def Function_25_9384(): pass

    label("Function_25_9384")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-98260, 800, 56110, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19530, 0)
    SetChrPos(0x101, -99650, 0, 54550, 45)
    SetChrPos(0x102, -100000, 0, 53550, 45)
    SetChrPos(0x103, -98500, 0, 53800, 0)
    SetChrPos(0x104, -97830, 0, 53030, 0)
    SetChrPos(0x109, -100480, 0, 55530, 89)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    #C0387
    ChrTalk(
        0xC,
        "#5P#1305Fあら、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        "#11P#1502Fもしかして……？\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、いくつか\x01",
            "材料になりそうなものを\x01",
            "見繕って来たよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x342),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    #A0391
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x343),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x342, 1)
    SubItemNumber(0x343, 1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0392
    ChrTalk(
        0x8,
        (
            "#11P#1502Fわぁ……これって、\x01",
            "ペンダントの材料ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあと、プレゼント用の箱だね。\x01",
            "こっちも首尾よく\x01",
            "そろえることができたよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0394
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x344),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    #A0395
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x345),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x344, 1)
    SubItemNumber(0x345, 1)

    #C0396
    ChrTalk(
        0xC,
        (
            "#5P#1305F……ちょっと驚いたわ。\x01",
            "ウルスラ病院の中だけで\x01",
            "立派なものが揃うなんてね。\x02\x03",

            "#1300Fどう、シズクちゃん。\x01",
            "これでお父さんへのプレゼントは\x01",
            "作ることができそう？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x8,
        (
            "#11P#1502Fは……はい！\x01",
            "充分すぎるくらいです。\x02\x03",

            "ペンダントトップは\x01",
            "とっても頑丈にできているし……\x02\x03",

            "この皮の編み紐も、\x01",
            "お父さんが身に付けていても\x01",
            "邪魔にならなそうです。\x02\x03",

            "皆さん、本当に\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#6P#0009Fはは、そんなに喜んでもらえると\x01",
            "探した甲斐があったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x104,
        (
            "#12P#0304Fなんたって\x01",
            "こ～んなカワイコちゃんの頼みだしな。\x02\x03",

            "#0300Fお兄さんたち、\x01",
            "ちっと張り切っちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x102,
        "#12P#0102Fふふ、調子いいんだから。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x103,
        "#12P#0204F……まぁ、否定はしませんが。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xC,
        (
            "#5P#1300Fそうね、シズクちゃん……\x01",
            "せっかくだし今から組み立てて\x01",
            "しまいましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x8,
        (
            "#11P#1505Fあ、はい、そうですね。\x02\x03",

            "#1502Fロイドさんたちも……\x01",
            "良かったら完成品を\x01",
            "見ていってもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、そうさせてもらうよ。\x01",
            "まだ手伝えることも\x01",
            "あるだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x109,
        (
            "#6P#0500F私も微力ながら\x01",
            "力添えさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0406
    AnonymousTalk(
        0x8,
        (
            "#1500F──えっと……\x02\x03",

            "あとは、皮の編み紐に\x01",
            "石の嵌ったペンダントトップを……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0407
    ChrTalk(
        0x8,
        (
            "#11P#1505Fで、できました……！\x02\x03",

            "#1502Fどうですか、皆さん。\x01",
            "いいものができたでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        "#6P#0000Fああ、立派にできてるよ。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xC,
        (
            "#5P#1302Fうん、これならきっと\x01",
            "お父さんも喜んでくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x8,
        "#11P#1502Fほっ、よかったぁ……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x104,
        (
            "#12P#0300Fしっかしまぁ、\x01",
            "シズクちゃんの持ってた石ってのは\x01",
            "なかなか不思議だねぇ。\x02\x03",

            "#0304F少し磨いたくらいで\x01",
            "綺麗にペンダントトップに\x01",
            "嵌るんだからよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x102,
        (
            "#12P#0100Fええ、ほんと。\x01",
            "まるで元々その場所に\x01",
            "収まってたみたい。\x02\x03",

            "皮の編み紐も、ペンダントトップに\x01",
            "違和感無く組み合わせられたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x103,
        (
            "#12P#0200F地味目ではありますが、\x01",
            "それが逆に上品さを\x01",
            "引き立てているかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x109,
        (
            "#6P#0500Fそうですね……\x01",
            "ジュエリーショップに\x01",
            "置いていても遜色なさそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xC,
        "#5P#1300Fふふ、確かにね。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x8,
        (
            "#11P#1502F……セシルさん、皆さん……\x01",
            "本当にありがとうございました。\x01",
            "組み立てまで手伝っていただいて……\x02\x03",

            "あの、これはほんの気持ちです。\x01",
            "よかったら……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0417
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x62),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x62, 1)

    #C0418
    ChrTalk(
        0x101,
        (
            "#6P#0005F綺麗な石が嵌ってる……\x01",
            "これってもしかして、\x01",
            "そのペンダントの石じゃあ？\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x8,
        (
            "#11P#1502Fはい、実は２つ、\x01",
            "同じものを拾っていたんです。\x02\x03",

            "こっちは、私の持っていた\x01",
            "壊れたブローチに\x01",
            "嵌めたものですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        (
            "#12P#0105Fで、でも……\x01",
            "本当に貰ってもいいの？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "#11P#1500Fはい、もちろんです。\x02\x03",

            "私は自分ひとりじゃ\x01",
            "絶対にプレゼントは作れない\x01",
            "と思ってましたから……\x02\x03",

            "これは手伝ってくれる誰かに\x01",
            "渡そうと思ったんです。\x02\x03",

            "#1502F最初はセシルさんに\x01",
            "渡そうと思ったんですけど、\x01",
            "さっき相談して……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xC,
        (
            "#5P#1304Fそういうこと。\x02\x03",

            "#1300F立派な材料を集めてくれたのだし、\x01",
            "あなた達に貰う権利があるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        (
            "#12P#0309Fたはは、そこまで言われちゃ\x01",
            "断るのも失礼ってもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x103,
        (
            "#12P#0200Fありがたく\x01",
            "いただきましょう、ロイドさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x101,
        (
            "#6P#0004F……ああ、そうだな。\x02\x03",

            "#0000Fありがとう、シズクちゃん。\x01",
            "大事に使わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x8,
        (
            "#11P#1502Fええ、ぜひ役立ててください。\x02\x03",

            "それじゃあみなさん、\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50500, 1000, 57500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0427
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【父へのプレゼント】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x2C, 0x1, 0x6)
    OP_29(0x2C, 0x4, 0x10)
    SetChrPos(0x0, -100060, 50, 50620, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    TurnDirection(0xC, 0x8, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_9384 end

    def Function_26_A28B(): pass

    label("Function_26_A28B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(5720, 1000, -48480, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19220, 0)
    SetChrPos(0x101, 5800, 0, -49500, 0)
    SetChrPos(0x102, 4500, 0, -49500, 45)
    SetChrPos(0x103, 5800, 0, -50800, 0)
    SetChrPos(0x104, 4500, 0, -50800, 45)
    SetChrPos(0x109, 3200, 0, -50150, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x9, 0x1)
    FadeToBright(500, 0)
    OP_0D()

    #C0428
    ChrTalk(
        0x9,
        (
            "#5Pこの前、レマン自治州にいる\x01",
            "お父さんたちから手紙と一緒に\x01",
            "贈り物が届いたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x9,
        (
            "#5P僕が欲しがってた\x01",
            "おもちゃが入っててさ……\x01",
            "あれは嬉しかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x101,
        (
            "#12P#0000Fはは、それは良かったね。\x02\x03",

            "#0003F（それにしても贈り物か……\x01",
            "  もしかすると……）\x02\x03",

            "#0000Fところで……\x01",
            "その贈り物の箱って\x01",
            "とってあるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x9,
        "#5P箱？\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x9,
        (
            "#5Pうん、セシルお姉ちゃんが\x01",
            "綺麗に畳んでくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x9,
        (
            "#5Pせっかくの贈り物なんだから\x01",
            "大事にしておいた方がいいって。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x104,
        (
            "#12P#0305Fへぇ……\x01",
            "女の人っていうのは\x01",
            "そういうとこマメだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x103,
        (
            "#12P#0203Fランディさんが\x01",
            "ずぼらなだけかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x9,
        (
            "#5Pえっと、お兄ちゃんたちは\x01",
            "箱が必要なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        "#12P#0000Fああ、実は……\x02",
    )

    CloseMessageWindow()

    #A0438
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは、プレゼントの材料集めを\x01",
            "していることを説明した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0439
    ChrTalk(
        0x101,
        (
            "#12P#0000F……っていうことでね。\x01",
            "プレゼントの包装箱も一緒に\x01",
            "探してるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x9,
        "#5Pそっか、シズクちゃんが……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x9,
        (
            "#5Pシズクちゃんもそうならそうと\x01",
            "早く言ってくれればいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x9,
        "#5Pはい、これ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0443
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x345),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x345, 1)

    #C0444
    ChrTalk(
        0x102,
        (
            "#12P#0100Fまぁ、綺麗にとってあるのね。\x02\x03",

            "贈り物用に綺麗に仕立てた\x01",
            "立派な箱じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x109,
        (
            "#6P#0500F……いいの？\x01",
            "大事にとってあったんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x9,
        "#5Pううん、いいんだ。\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x9,
        (
            "#5P中のおもちゃはもう貰ってるし、\x01",
            "セシルお姉ちゃんが言わなきゃ\x01",
            "捨てちゃってたと思うし。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x9,
        (
            "#5Pそれに僕も、\x01",
            "シズクちゃんのために\x01",
            "何かしてあげたかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそっか……\x01",
            "じゃあ、ありがたく\x01",
            "いただいていくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x104,
        (
            "#12P#0304Fはは、なかなか男として\x01",
            "立派じゃないか。\x02\x03",

            "#0300F将来きっとモテるぜ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x9,
        "#5Pえへへ……\x02",
    )

    CloseMessageWindow()
    OP_29(0x2C, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9DD")
    OP_29(0x2C, 0x1, 0x5)

    #C0452
    ChrTalk(
        0x101,
        (
            "#12P#0000F（プレゼントの材料になりそうな物も揃ったし\x01",
            "  包装用の箱とリボンも手に入ったな……）\x02\x03",

            "（よし、そろそろシズクちゃんの所に\x01",
            "  持っていってあげよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9DD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(5800, 1000, -49500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 5800, 0, -49500, 0)
    SetChrPos(0x1, 5800, 0, -49500, 0)
    SetChrPos(0x2, 5800, 0, -49500, 0)
    SetChrPos(0x3, 5800, 0, -49500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x9, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_26_A28B end

    SaveToFile()

Try(main)
