from ZeroScenarioHelper import *

def main():
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
        "滴",                     # 1
        "米海尔",                 # 2
        "米海尔",                 # 3
        "盖巴尔议员",             # 4
        "塞茜尔",                 # 5
        "希伦护士",               # 6
        "梅菲尔护士",             # 7
        "约亚西姆副教授",         # 8
        "勤杂工戴森",             # 9
        "艾丝蒂尔",               # 10
        "约修亚",                 # 11
        "游客马修",               # 12
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
        "Function_5_179C",         # 05, 5
        "Function_6_1BBA",         # 06, 6
        "Function_7_2567",         # 07, 7
        "Function_8_257E",         # 08, 8
        "Function_9_26F2",         # 09, 9
        "Function_10_2804",        # 0A, 10
        "Function_11_3A6C",        # 0B, 11
        "Function_12_3CFA",        # 0C, 12
        "Function_13_488B",        # 0D, 13
        "Function_14_4AB8",        # 0E, 14
        "Function_15_4B68",        # 0F, 15
        "Function_16_4E36",        # 10, 16
        "Function_17_4FDD",        # 11, 17
        "Function_18_5128",        # 12, 18
        "Function_19_51AF",        # 13, 19
        "Function_20_51EA",        # 14, 20
        "Function_21_68C7",        # 15, 21
        "Function_22_6EF5",        # 16, 22
        "Function_23_6F60",        # 17, 23
        "Function_24_74C0",        # 18, 24
        "Function_25_7ED8",        # 19, 25
        "Function_26_8B7F",        # 1A, 26
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
    Jump("loc_1794")

    label("loc_8EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_96A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_907")
    Call(0, 5)
    Jump("loc_965")

    label("loc_907")


    #C0001
    ChrTalk(
        0x8,
        (
            "#1500F明天爸爸会来接我，\x01",
            "今天要早点睡才行呢。\x02\x03",

            "#1502F呵呵……太期待了，\x01",
            "可能会睡不着呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_965")

    Jump("loc_1794")

    label("loc_96A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_985")
    Call(0, 5)
    Jump("loc_9CA")

    label("loc_985")


    #C0002
    ChrTalk(
        0x8,
        (
            "#1502F明天的外出日，\x01",
            "我打算顺便去找小琪雅。\x02\x03",

            "呵呵……好期待哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CA")

    Jump("loc_1794")

    label("loc_9CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EA")
    Call(0, 15)
    Jump("loc_C58")

    label("loc_9EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC3")

    #C0003
    ChrTalk(
        0x8,
        (
            "#1500F各位，真是\x01",
            "谢谢你们了。\x02\x03",

            "#1508F感觉好像\x01",
            "把多余的东西给了你们，\x01",
            "真有点对不起大家……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，没那回事啦。\x01",
            "我们会好好珍惜的。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#1500F这样的话，\x01",
            "我也会……非常开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B0A")

    label("loc_AC3")


    #C0006
    ChrTalk(
        0x8,
        (
            "#1500F做好的礼物，\x01",
            "爸爸一定\x01",
            "也会喜欢的。\x02\x03",

            "各位，真是\x01",
            "谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0A")

    Jump("loc_C58")

    label("loc_B0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B44")
    Call(0, 25)
    Jump("loc_C58")

    label("loc_B44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_BD9")

    #C0007
    ChrTalk(
        0x8,
        (
            "#1508F各位，真抱歉，\x01",
            "突然说这种\x01",
            "任性的话……\x02\x03",

            "拜托大家……\x01",
            "麻烦你们费心了。\x02\x03",

            "#1508F那个……真的只要\x01",
            "在空闲的时候帮我就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C58")

    label("loc_BD9")


    #C0008
    ChrTalk(
        0x8,
        (
            "#1500F小琪雅对我来说也是\x01",
            "非常重要的朋友。\x02\x03",

            "#1502F呵呵，真不可思议呢。\x01",
            "才刚刚认识，\x01",
            "就可以成为朋友。\x02\x03",

            "好期待下次再见呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C58")

    Jump("loc_1794")

    label("loc_C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_C6B")
    Jump("loc_1794")

    label("loc_C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_C79")
    Jump("loc_1794")

    label("loc_C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2A")

    #C0009
    ChrTalk(
        0x8,
        (
            "#1500F今天塞茜尔小姐\x01",
            "要带我出去散步。\x02\x03",

            "虽然我的眼睛看不见，\x01",
            "但是有她陪着我，\x01",
            "所以一定会很开心。\x02\x03",

            "#1502F呵呵……好羡慕罗伊德警官\x01",
            "有那样的姐姐哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D6B")

    label("loc_D2A")


    #C0010
    ChrTalk(
        0x8,
        (
            "#1500F塞茜尔小姐\x01",
            "要带我出去散步。\x02\x03",

            "呵呵，希望她能早点来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6B")

    Jump("loc_1794")

    label("loc_D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E35")

    #C0011
    ChrTalk(
        0x8,
        (
            "#1500F爸爸今天似乎\x01",
            "也要去很多地方。\x02\x03",

            "最近他经常\x01",
            "去外国出差……\x02\x03",

            "#1505F……啊，那个……\x01",
            "我并没有觉得寂寞哦。\x02\x03",

            "#1502F不如说，大家都很信赖爸爸，\x01",
            "所以让我觉得很自豪呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E81")

    label("loc_E35")


    #C0012
    ChrTalk(
        0x8,
        (
            "#1500F爸爸今天似乎\x01",
            "也要去很多地方。\x02\x03",

            "呵呵，爸爸很受欢迎嘛，\x01",
            "没办法呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E81")

    Jump("loc_1794")

    label("loc_E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E97")
    Call(0, 13)
    Jump("loc_1794")

    label("loc_E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_FB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4E")

    #C0013
    ChrTalk(
        0x8,
        (
            "#1505F啊，罗伊德警官，是你们……\x02\x03",

            "#1508F……现在是纪念庆典吧，\x01",
            "可我好像没什么现实感……\x02\x03",

            "明明身边发生着很多令人开心的事，\x01",
            "却感觉那些似乎离我很遥远……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FAD")

    label("loc_F4E")


    #C0014
    ChrTalk(
        0x8,
        (
            "#1502F……对不起，\x01",
            "你们难得来一趟，\x01",
            "我却说这种丧气话。\x02\x03",

            "我没事的，\x01",
            "请大家不要放在心上哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAD")

    Jump("loc_1794")

    label("loc_FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1272")

    #C0015
    ChrTalk(
        0x8,
        (
            "#1505F啊……莫非……\x01",
            "是特别任务支援科的各位？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0005F哎！？\x01",
            "我们还没出声，\x01",
            "你就知道了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#1500F呵呵，我觉得\x01",
            "脚步声好像有点熟悉嘛。\x02\x03",

            "像塞茜尔小姐和罗伊德警官你们\x01",
            "这种有特色的脚步声，我很容易记住的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0005F脚步声……\x01",
            "光凭这个就能判断来人是谁，\x01",
            "真的很了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#1500F嘿嘿……\x02\x03",

            "#1500F不过，每个人的脚步声\x01",
            "其实都有所差别哦。\x02\x03",

            "比如说……经常来看我的\x01",
            "游击士哥哥姐姐，还有爸爸，\x01",
            "走起路时，那种毫无破绽的感觉更加强烈呢。\x02",
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
        "#0306F……原来我们有很多破绽啊。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        "#0206F有点受打击。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0100F好啦好啦……\x01",
            "和亚里欧斯先生相比的话，\x01",
            "谁都不可能得到太高的评价吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 7)
    Jump("loc_12FA")

    label("loc_1272")


    #C0023
    ChrTalk(
        0x8,
        (
            "#1508F哎，那个……\x01",
            "我好像说了什么\x01",
            "失礼的话……？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0000F不，没有没有，你不用介意。\x01",
            "我们的实力确实\x01",
            "还远远不够呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "#1505F？\x02",
    )

    CloseMessageWindow()

    label("loc_12FA")

    Jump("loc_1794")

    label("loc_12FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_156E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CB")

    #C0026
    ChrTalk(
        0x8,
        (
            "#1500F啊，罗伊德警官，是你们……\x01",
            "午安。\x02\x03",

            "之前我听塞茜尔小姐\x01",
            "说了大家的光荣事迹。\x02\x03",

            "听说是罗伊德警官你们\x01",
            "解决了袭击利顿医生的魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#0100F其实，光靠我们的力量\x01",
            "是无法解决那起事件的。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        "#0203F多亏有蔡特施以援手。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#1500F哪里，即使是这样……\x01",
            "听说认识的人大显身手，\x01",
            "我也觉得很开心。\x02\x03",

            "#1502F我想各位的工作一定很辛苦……\x01",
            "不过今后也请加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0002F嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0309F有小滴这么\x01",
            "可爱的孩子加油，\x01",
            "我们就精神百倍啦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 6)
    Jump("loc_1569")

    label("loc_14CB")


    #C0032
    ChrTalk(
        0x8,
        (
            "#1500F要是特别任务支援科\x01",
            "继续这样努力下去……\x02\x03",

            "呵呵……\x01",
            "罗伊德警官，你们是不是\x01",
            "也会变得跟爸爸一样强呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0000F好、好像相当困难，\x01",
            "不过我们会加油的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1569")

    Jump("loc_1794")

    label("loc_156E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_176F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_171B")

    #C0034
    ChrTalk(
        0x8,
        (
            "#1500F自从眼睛失明之后，\x01",
            "我的听觉好像就变得很灵敏了……\x01",
            "我确实听到过声音的。\x02\x03",

            "#1508F可是，那声奇怪的『嘟～』\x01",
            "到底是什么，\x01",
            "我就不知道了……\x02\x03",

            "#1505F……对不起。\x01",
            "这情报似乎\x01",
            "派不上什么用场呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#0004F不……\x01",
            "你为我们提供了在之前的调查中\x01",
            "从没有听到过的新情报。\x02\x03",

            "#0000F多亏你，我们刚才在调查时\x01",
            "做出的猜想也得到了证实。\x02\x03",

            "那个声音一定也会是\x01",
            "能够推进调查的重要线索吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "#1502F啊……那我就很开心了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_176A")

    label("loc_171B")


    #C0037
    ChrTalk(
        0x8,
        (
            "#1500F请大家加油调查吧。\x02\x03",

            "我听到的声音……\x01",
            "这条线索要是能帮上忙就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176A")

    Jump("loc_1794")

    label("loc_176F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_177D")
    Jump("loc_1794")

    label("loc_177D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_178B")
    Jump("loc_1794")

    label("loc_178B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1794")

    label("loc_1794")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_4_7DB end

    def Function_5_179C(): pass

    label("Function_5_179C")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18CE")

    #C0038
    ChrTalk(
        0x8,
        (
            "#1505F啊，是各位……！\x02\x03",

            "#1502F昨天真是\x01",
            "多谢大家了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，不用啦。\x01",
            "我们也收到了好东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#0100F话说，小滴，\x01",
            "你今天好像很高兴啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1913")

    label("loc_18CE")


    #C0041
    ChrTalk(
        0x8,
        "#1502F啊……大家好！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，你好。\x01",
            "今天好像很高兴啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1913")


    #C0043
    ChrTalk(
        0x8,
        (
            "#1502F啊，嘿嘿……\x02\x03",

            "那个，明天是外出日，\x01",
            "可以去市里玩了。\x02\x03",

            "爸爸的工作\x01",
            "似乎也告一段落了……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0305F嘿，那个超级忙碌的大叔\x01",
            "竟然能闲下来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A68")

    #C0045
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，不是很好嘛。\x02\x03",

            "这样就可以把昨天做的\x01",
            "礼物送给他了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#1500F嘿嘿，是呀……！\x02\x03",

            "#1505F……啊……\x01",
            "对了，要是方便的话……\x02\x03",

            "#1502F我想去支援科那里\x01",
            "见见小琪雅……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ADA")

    label("loc_1A68")


    #C0047
    ChrTalk(
        0x102,
        "#0102F呵呵，不是很好嘛。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#1500F是、是呀。\x01",
            "对了，要是方便的话……\x02\x03",

            "#1502F我想去支援科那里\x01",
            "见见小琪雅……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADA")


    #C0049
    ChrTalk(
        0x101,
        (
            "#0002F可以啊，当然欢迎啦。\x02\x03",

            "我们虽然有工作要外出，\x01",
            "不过科长和琪雅应该在的。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        (
            "#0204F……琪雅开心的笑容\x01",
            "好像已经浮现在眼前了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#1502F……谢谢大家！\x02\x03",

            "呵呵……要好好\x01",
            "打扮一下再去呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -99230, 0, 55030, 45)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0xCC, 2)
    EventEnd(0x5)
    Return()

    # Function_5_179C end

    def Function_6_1BBA(): pass

    label("Function_6_1BBA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C4E")
    Jump("loc_1C98")

    label("loc_1C4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C6E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C98")

    label("loc_1C6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C8E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C98")

    label("loc_1C8E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C98")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D17")

    #C0052
    ChrTalk(
        0xFE,
        (
            "小滴今天去\x01",
            "克洛斯贝尔市了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "平时她很少出去，\x01",
            "希望她能玩得开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255F")

    label("loc_1D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1D25")
    Jump("loc_255F")

    label("loc_1D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1DF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA3")

    #C0054
    ChrTalk(
        0xFE,
        "咳、咳……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "啊，没事……\x01",
            "只是病情稍微发作了，\x01",
            "不用担心啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "待会塞茜尔姐姐\x01",
            "也会来的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DEF")

    label("loc_1DA3")


    #C0057
    ChrTalk(
        0xFE,
        "咳、咳……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "我没事……\x01",
            "只要吃点药，马上就会好起来的，\x01",
            "不用担心啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DEF")

    Jump("loc_255F")

    label("loc_1DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F49")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E67")

    #C0059
    ChrTalk(
        0xFE,
        (
            "小滴后天\x01",
            "就能见到爸爸了呢。\x01",
            "真羡慕呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "希望她能连同我的份一起，\x01",
            "好好玩个痛快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F44")

    label("loc_1E67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1EC8")

    #C0061
    ChrTalk(
        0xFE,
        (
            "我也想为\x01",
            "小滴做点什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "虽然只有\x01",
            "盒子可以给她……\x01",
            "不过能帮上忙就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F44")

    label("loc_1EC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1EDC")
    Call(0, 26)
    Jump("loc_1F44")

    label("loc_1EDC")


    #C0063
    ChrTalk(
        0xFE,
        (
            "不久前，住在列曼自治州的\x01",
            "爸爸妈妈给我寄来了\x01",
            "信和礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "里面放有我想要的\x01",
            "玩具……\x01",
            "我好高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F44")

    Jump("loc_255F")

    label("loc_1F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1FBF")

    #C0065
    ChrTalk(
        0xFE,
        (
            "我的手术……要是能成功就好了，\x01",
            "万一失败的话，爸爸妈妈的米拉\x01",
            "就白费了……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "我该怎么办才好呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_255F")

    label("loc_1FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDA")
    Call(0, 9)
    Jump("loc_1FF8")

    label("loc_1FDA")


    #C0067
    ChrTalk(
        0xFE,
        "果然还是很怕做手术啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1FF8")

    Jump("loc_255F")

    label("loc_1FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2129")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BC")

    #C0068
    ChrTalk(
        0xFE,
        (
            "住在列曼自治州的爸爸妈妈\x01",
            "寄信来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "爸爸妈妈也在为了\x01",
            "我的住院费和手术费\x01",
            "拼命努力工作呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "虽然很难见面，会觉得寂寞……\x01",
            "不过还有小滴在，我没问题的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2124")

    label("loc_20BC")


    #C0071
    ChrTalk(
        0xFE,
        (
            "住在列曼自治州的爸爸妈妈\x01",
            "寄信来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "虽然很难见面，会觉得寂寞……\x01",
            "不过还有小滴在，我没问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2124")

    Jump("loc_255F")

    label("loc_2129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2137")
    Jump("loc_255F")

    label("loc_2137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21AE")

    #C0073
    ChrTalk(
        0xFE,
        "明天有纪念庆典的游行吧。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "可以的话，我也想\x01",
            "和小滴一起去看……\x01",
            "但今年是不行了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21D3")

    label("loc_21AE")


    #C0075
    ChrTalk(
        0xFE,
        (
            "游行……好想和\x01",
            "小滴一起去看呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D3")

    Jump("loc_255F")

    label("loc_21D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_222B")

    #C0076
    ChrTalk(
        0xFE,
        "纪念庆典啊……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生，\x01",
            "现在是不是在开心地钓鱼呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255F")

    label("loc_222B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_227D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2246")
    Call(0, 8)
    Jump("loc_2278")

    label("loc_2246")


    #C0078
    ChrTalk(
        0xFE,
        (
            "咳咳……\x01",
            "我……看来是\x01",
            "不能去纪念庆典了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2278")

    Jump("loc_255F")

    label("loc_227D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_231D")

    #C0079
    ChrTalk(
        0xFE,
        (
            "虽然我年纪比较小，\x01",
            "不过和小滴是好朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "我们经常一起去散步，\x01",
            "或者在小滴的\x01",
            "病房里聊天呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "我和小滴都是长期住院，\x01",
            "所以比较合得来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255F")

    label("loc_231D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2389")

    #C0082
    ChrTalk(
        0xFE,
        (
            "小滴经常\x01",
            "和我聊天呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "……眼睛看不见，\x01",
            "会是怎样的心情呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "一定会很寂寞吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_255F")

    label("loc_2389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_23EE")

    #C0085
    ChrTalk(
        0xFE,
        (
            "塞茜尔姐姐\x01",
            "刚才特意过来\x01",
            "和我聊天了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "……我将来也想成为\x01",
            "那么温柔体贴的人呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255F")

    label("loc_23EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2556")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D5")

    #C0087
    ChrTalk(
        0xFE,
        (
            "啊……塞茜尔姐姐，\x01",
            "你好。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x136,
        "#1300F米海尔，身体感觉怎么样？\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "嗯……感觉似乎好多了。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x136,
        (
            "#1304F是吗……太好了。\x02\x03",

            "#1300F有什么事的话，就马上按铃叫护士哦。\x01",
            "我们会马上赶过来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "嗯……谢谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2551")

    label("loc_24D5")


    #C0092
    ChrTalk(
        0xFE,
        (
            "我是从列曼自治州\x01",
            "转到这家医院来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "医生跟我说一定要做\x01",
            "外科手术才能治好病……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "……我果然还是很怕做手术啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2551")

    Jump("loc_255F")

    label("loc_2556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_255F")

    label("loc_255F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1BBA end

    def Function_7_2567(): pass

    label("Function_7_2567")

    TalkBegin(0xFE)

    #C0095
    ChrTalk(
        0xFE,
        "呼、呼……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_2567 end

    def Function_8_257E(): pass

    label("Function_8_257E")

    TurnDirection(0xF, 0x9, 0)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0xF, 0xFF)

    #C0096
    ChrTalk(
        0x9,
        "咳、咳咳……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xF,
        (
            "#2403F嗯～似乎有点发作呢。\x01",
            "待会要吃药哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        "好……咳、咳。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "……对了，约亚西姆医生您\x01",
            "在纪念庆典期间有什么安排呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xF,
        (
            "#2405F嗯～……难说呢。\x02\x03",

            "#2400F说不定会和平时一样，\x01",
            "找个地方去钓鱼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "哎……不去看庆典吗？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xF,
        (
            "#2406F我不太喜欢\x01",
            "吵闹的地方呢。\x02\x03",

            "要是在那里钓鱼的话，鱼都会被吓跑的。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        "您真是热爱钓鱼呢……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_8_257E end

    def Function_9_26F2(): pass

    label("Function_9_26F2")

    TurnDirection(0xC, 0x9, 0)
    SetChrSubChip(0x9, 0x1)
    OP_4B(0xC, 0xFF)

    #C0104
    ChrTalk(
        0xC,
        (
            "#1300F米海尔……\x01",
            "你还是下不了决心接受手术吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "也不是啦，只是……\x01",
            "果然还是觉得好可怕……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        (
            "#1304F……呵呵，这样啊。\x01",
            "没关系的，不要勉强。\x02\x03",

            "#1300F在米海尔下定决心之前，\x01",
            "医生们会尽一切努力来照料好他的。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        "……谢谢你，塞茜尔姐姐……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_9_26F2 end

    def Function_10_2804(): pass

    label("Function_10_2804")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2898")
    Jump("loc_28E2")

    label("loc_2898")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28B8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28E2")

    label("loc_28B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28D8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28E2")

    label("loc_28D8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28E2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B27")

    #C0108
    ChrTalk(
        0xFE,
        (
            "从昨天开始，我就一直\x01",
            "怀疑哈尔特曼议长是不是\x01",
            "打算除掉我……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "既然是哈尔特曼议长安排我住院的，\x01",
            "就一定会派人监视我……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "我、我得想办法逃出医院，\x01",
            "远走高飞，逃到帝国那边去……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B1F")

    #C0111
    ChrTalk(
        0x10A,
        (
            "#0600F（……之前被发现有逃税嫌疑的\x01",
            "  帝国派盖巴尔议员……\x01",
            "  原来藏在这种地方啊。）\x02\x03",

            "#0603F（不过，自那以来，事件就完全被掩盖……\x01",
            "  关于盖巴尔议员的事，\x01",
            "  就没再听人提起过了。）\x02\x03",

            "#0600F（哈尔特曼议长必然是\x01",
            "  完全舍弃了他，\x01",
            "  根本不至于有生命危险的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#0103F（连这种事都没有察觉，\x01",
            "  真是个悲哀的人啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1F")

    SetScenarioFlags(0x0, 2)
    Jump("loc_2B93")

    label("loc_2B27")


    #C0113
    ChrTalk(
        0xFE,
        (
            "总、总而言之……\x01",
            "必须尽快想个办法\x01",
            "逃出医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "不赶快的话，\x01",
            "哈尔特曼议长一定会\x01",
            "派人来除掉我的……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B93")

    Jump("loc_3A64")

    label("loc_2B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC0")

    #C0115
    ChrTalk(
        0xFE,
        (
            "我的违法行为被曝光之后，\x01",
            "建议我来医院藏身的人\x01",
            "就是哈尔特曼议长……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "但是，过了这么久，\x01",
            "他还是没通知我复出的时机……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "莫非，哈尔特曼议长\x01",
            "已经知道我暗中在各界打通门路，\x01",
            "逐步稳固立场……？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "这、这样的话……我岂不是很快\x01",
            "就会被除掉了吗……！？\x01",
            "呜、呜呜……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D62")

    label("loc_2CC0")


    #C0119
    ChrTalk(
        0xFE,
        (
            "我、我并没有打算脱离\x01",
            "哈尔特曼议长，自立门户啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "只不过是占一点\x01",
            "小便宜而已啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "但、但是，这样下去的话，\x01",
            "很快就会被除掉的。\x01",
            "必、必须要想个办法……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D62")

    Jump("loc_3A64")

    label("loc_2D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2E60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E05")

    #C0122
    ChrTalk(
        0xFE,
        (
            "本想在逃税事件的风头过去之前，\x01",
            "暂时住院藏身……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "看样子，负责看护我的人\x01",
            "换成那个护士长了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "唔唔唔，真是\x01",
            "住不下去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E5B")

    label("loc_2E05")


    #C0125
    ChrTalk(
        0xFE,
        "那个护士长不听命令，实在难对付。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "可恶，身为议员的我要为何要遭受这种待遇……\x02",
    )

    CloseMessageWindow()

    label("loc_2E5B")

    Jump("loc_3A64")

    label("loc_2E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0A")

    #C0127
    ChrTalk(
        0xFE,
        "真是难以置信……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "不过是进了一下\x01",
            "护士休息室，\x01",
            "为什么要把我赶出来啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "可、可是那个护士长太有魄力了，\x01",
            "不知为何，就是无法反抗她……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F8C")

    label("loc_2F0A")


    #C0130
    ChrTalk(
        0xFE,
        "不知为何，因为那个护士长的魄力，我就是没办法反抗她……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "身为自治州议员，\x01",
            "拥有绝对权力的我，\x01",
            "竟然会屈服于医院内的权力……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    Jump("loc_3A64")

    label("loc_2F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_305A")

    #C0132
    ChrTalk(
        0xFE,
        (
            "……唉……\x01",
            "就算搞个恶作剧，叫护士来\x01",
            "打发时间，也不足以解气。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "我逃税的事情，在住院期间，\x01",
            "哈尔特曼议长应该\x01",
            "已经帮我抹消掉了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "到底要等到何时，\x01",
            "我才能重回自治州议会啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A64")

    label("loc_305A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_30A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3075")
    Call(0, 11)
    Jump("loc_30A0")

    label("loc_3075")


    #C0135
    ChrTalk(
        0xFE,
        (
            "最近的小孩子真是……\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A0")

    Jump("loc_3A64")

    label("loc_30A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_31B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_314A")

    #C0136
    ChrTalk(
        0xFE,
        (
            "暂时在医院住院一段时间，\x01",
            "等违法行为被曝光的风头过去再……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "哈尔特曼议长是这么说的。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "我、我到底要在这里\x01",
            "躲到什么时候啊……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31AD")

    label("loc_314A")


    #C0139
    ChrTalk(
        0xFE,
        (
            "我那些逃税之类的行为，\x01",
            "市民们应该\x01",
            "早就忘记了……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "我、我到底要在这里\x01",
            "躲到什么时候啊……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AD")

    Jump("loc_3A64")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_335B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F5")

    #C0141
    ChrTalk(
        0xFE,
        (
            "明天是在米修拉姆\x01",
            "举办那个活动的日子……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "今年是这个状态，\x01",
            "所以没收到邀请函，\x01",
            "不过明年一定要……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#0005F（米修拉姆……记得是可以从市内港湾区\x01",
            "  坐水上巴士过去的疗养地吧。）\x02\x03",

            "#0000F（这样的人也会去玩啊……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#0300F（那里可是高级精品店和\x01",
            "  西餐厅林立的地方啊，\x01",
            "  也不算奇怪吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3356")

    label("loc_32F5")


    #C0145
    ChrTalk(
        0xFE,
        (
            "米修拉姆明天\x01",
            "要举办那个活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "今年是这个状态，\x01",
            "所以没收到邀请函，\x01",
            "不过明年一定要……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3356")

    Jump("loc_3A64")

    label("loc_335B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3425")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DC")

    #C0147
    ChrTalk(
        0xFE,
        "这家医院的娱乐太少，好无聊。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "到了纪念庆典，\x01",
            "原本应该每晚参加宴会，\x01",
            "让欢乐街的女公关作陪……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3420")

    label("loc_33DC")


    #C0149
    ChrTalk(
        0xFE,
        (
            "要是向护士出手的话，\x01",
            "那个护士长应该不会坐视不理……\x01",
            "唔唔唔……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3420")

    Jump("loc_3A64")

    label("loc_3425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3515")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34EF")

    #C0150
    ChrTalk(
        0xFE,
        (
            "从昨天开始，就听说\x01",
            "伙食会有所改善……\x01",
            "结果就是豆腐肉饼？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "骗小孩子还差不多，\x01",
            "午饭当然要吃\x01",
            "牛排加红酒了！\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0006F（这、这个人以前过的是\x01",
            "  何等奢侈的生活啊……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3510")

    label("loc_34EF")


    #C0153
    ChrTalk(
        0xFE,
        (
            "午饭当然要吃\x01",
            "牛排加红酒了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3510")

    Jump("loc_3A64")

    label("loc_3515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B1")

    #C0154
    ChrTalk(
        0xFE,
        (
            "这么说来，下个月\x01",
            "就是克洛斯贝尔创立纪念庆典了。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "说到纪念庆典……\x01",
            "对了，有那个活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "哼哼哼，\x01",
            "我开始期待起来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_360C")

    label("loc_35B1")


    #C0157
    ChrTalk(
        0xFE,
        (
            "那个活动……\x01",
            "去年靠哈尔特曼议长的门路，\x01",
            "我也参加了。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "呼呼呼，\x01",
            "我开始期待起来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360C")

    Jump("loc_3A64")

    label("loc_3611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_368A")

    #C0159
    ChrTalk(
        0xFE,
        (
            "医院的伙食太简单无味。\x01",
            "我说要加份牛排和红酒，\x01",
            "但是谁都不理我。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "啧……真是个没有\x01",
            "服务精神的医院。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A64")

    label("loc_368A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_36F3")

    #C0161
    ChrTalk(
        0xFE,
        (
            "医院里好像设置了\x01",
            "阻挡魔兽的栏杆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "呵呵，明白就好。\x01",
            "我的安全可要\x01",
            "保障好才行啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A64")

    label("loc_36F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3704")
    Call(0, 16)
    Jump("loc_3A64")

    label("loc_3704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3A5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39BA")

    #C0163
    ChrTalk(
        0xFE,
        (
            "听说在一周前，\x01",
            "这家医院的职员\x01",
            "遭到了魔兽袭击。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "到底是怎么回事？\x01",
            "在这里能够\x01",
            "保证我的安全吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        (
            "#0301F（这大叔是什么人啊……\x01",
            "  虽然住在单人病房，\x01",
            "  但却莫名地有精神啊？）\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#0101F（这个人……\x01",
            "  我不久前在克洛斯贝尔时代周刊上\x01",
            "  看到过呢。）\x02\x03",

            "#0103F（记得是违法行为被曝光之后，\x01",
            "  马上就以身体不适为由\x01",
            "  而住院的议员……）\x02\x03",

            "#0101F（其实只是想在事态平静下来之前，\x01",
            "  暂时到医院来藏身吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        (
            "#0200F（装个病还要霸占\x01",
            "  单人病房吗……\x01",
            "  真是太恶劣了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        (
            "#0101F（因为是帝国派议长的跟班，\x01",
            "  是为了保持形象，\x01",
            "  才把他推到这里来的吧。）\x02\x03",

            "#0103F（现在他就算回去，\x01",
            "  政府里肯定也没有他的位置了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#0003F（也就是所谓的蜥蜴断尾吗……\x01",
            "  真有点可怜啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 2)
    Jump("loc_3A56")

    label("loc_39BA")


    #C0170
    ChrTalk(
        0xFE,
        (
            "听说在一周前，\x01",
            "这家医院的职员\x01",
            "遭到了魔兽袭击。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "……他们是不是对设备投资\x01",
            "有所怠慢啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "要是我被魔兽袭击了，\x01",
            "哈尔特曼议长可是不会坐视不理的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A56")

    Jump("loc_3A64")

    label("loc_3A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3A64")

    label("loc_3A64")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_2804 end

    def Function_11_3A6C(): pass

    label("Function_11_3A6C")

    TurnDirection(0xE, 0xB, 0)
    SetChrSubChip(0xB, 0x1)
    OP_4B(0xE, 0xFF)

    #C0173
    ChrTalk(
        0xB,
        (
            "我说你，明明是我先叫护士的，\x01",
            "你竟然优先护理别的患者，\x01",
            "这是怎么回事！\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xB,
        (
            "我可是克洛斯贝尔自治州议会的\x01",
            "议员哦！？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xE,
        (
            "很、很抱歉，\x01",
            "因为那边的患者\x01",
            "情况比较紧急……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xE,
        (
            "（不过就是买个杂志，\x01",
            "  有什么必要叫\x01",
            "  护士啊～……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        "#0001F（气氛好像很紧张……）\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x153,
        (
            "#1111F……喂～叔叔，\x01",
            "你要是太任性的话，\x01",
            "会被打屁股的哦。\x02",
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
        "什、什么……？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xE,
        "噗……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xB,
        (
            "喂、喂，笑什么！！\x01",
            "……最近的小孩子可真是……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3C73")

    #C0182
    ChrTalk(
        0x102,
        "#0100F呵呵，小琪雅真是机灵呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CEB")

    label("loc_3C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3CAD")

    #C0183
    ChrTalk(
        0x103,
        "#0203F不愧是琪雅，真是天不怕地不怕呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CEB")

    label("loc_3CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3CEB")

    #C0184
    ChrTalk(
        0x104,
        (
            "#0309F哈哈，不愧是阿琪，\x01",
            "议员先生也无言以对了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CEB")

    SetChrSubChip(0xB, 0x0)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_11_3A6C end

    def Function_12_3CFA(): pass

    label("Function_12_3CFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3D0B")
    Jump("loc_4887")

    label("loc_3D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3E79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF0")

    #C0185
    ChrTalk(
        0xC,
        (
            "#1304F米海尔他\x01",
            "吃过药之后就睡熟了。\x02\x03",

            "#1300F他的病经常会突然发作，\x01",
            "所以很令人担心……\x02\x03",

            "但小滴的存在和父母的来信\x01",
            "支撑着他，让他可以努力\x01",
            "与病魔抗争，这真是太好了。\x02\x03",

            "#1308F接下来，只要他肯接受手术……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3E74")

    label("loc_3DF0")


    #C0186
    ChrTalk(
        0xC,
        (
            "#1300F米海尔的病情发作虽然令人担心……\x01",
            "不过，多亏有小滴和他的父母，\x01",
            "才能让他坚强面对疾病。\x02\x03",

            "#1308F接下来，只要他肯接受手术……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E74")

    Jump("loc_4887")

    label("loc_3E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3F05")

    #C0187
    ChrTalk(
        0xC,
        (
            "#1302F（呵呵……\x01",
            "  昨天真是谢谢了。）\x02\x03",

            "#1304F（对小滴来说，\x01",
            "  真是好事不断呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#0005F？？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F6B")

    label("loc_3F05")


    #C0189
    ChrTalk(
        0xC,
        (
            "#1300F（啊，罗伊德。\x01",
            "  你来得正好呢。）\x02\x03",

            "（能不能去和\x01",
            "  小滴说说话？）\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        "#0005F（嗯、嗯……）\x02",
    )

    CloseMessageWindow()

    label("loc_3F6B")

    Jump("loc_4092")

    label("loc_3F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4028")

    #C0191
    ChrTalk(
        0xC,
        (
            "#1300F呵呵，这好像是小滴\x01",
            "住院以来最开心的时刻呢。\x02\x03",

            "#1304F要是我能见到伊莉娅，\x01",
            "一定也是那样的表情吧。\x02\x03",

            "#1302F她平时不能离开这里太远，\x01",
            "希望能趁这次机会好好开心一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4092")

    label("loc_4028")


    #C0192
    ChrTalk(
        0xC,
        (
            "#1300F呵呵，这好像是小滴\x01",
            "住院以来最开心的时刻呢。\x02\x03",

            "可以和爸爸一起出门，\x01",
            "还能见到朋友，当然会很开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4092")

    Jump("loc_4887")

    label("loc_4097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B2")
    Call(0, 15)
    Jump("loc_453F")

    label("loc_40B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4457")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B1")

    #C0193
    ChrTalk(
        0xC,
        (
            "#1302F呵呵，谢谢大家。\x01",
            "谢谢你们帮助小滴。\x02\x03",

            "#1301F话说回来……\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#0005F怎、怎么了，塞茜尔姐姐？\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "#1302F呵呵，没想到你在和\x01",
            "警备队的女孩子交往呢。\x02\x03",

            "#1309F罗伊德可真是不能小看啊¤\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41C9")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_41C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41F1")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_41F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4219")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4219")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4241")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4241")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4269")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4269")

    Sleep(1000)

    #C0196
    ChrTalk(
        0x109,
        (
            "#0505F哎……？\x02\x03",

            "是、是说我吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0011F不、不是啦，塞茜尔姐姐……！\x01",
            "这位是诺艾尔上士，\x01",
            "只是因为任务才和我们同行的……\x02\x03",

            "#0006F话说，难道我每次带女性过来，\x01",
            "你都打算做出这个反应吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        "#0106F（嗯、嗯～还是老样子……）\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        "#0200F（正是塞茜尔小姐的风格呢。）\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        "#0309F（性格很有特色哦，塞茜尔小姐！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 1)
    Jump("loc_4452")

    label("loc_43B1")


    #C0201
    ChrTalk(
        0xC,
        (
            "#1305F怎么……原来诺艾尔小姐\x01",
            "也不是你的女朋友啊。\x02\x03",

            "#1306F真是的，姐姐要到什么时候\x01",
            "才能见到侄子或侄女的脸啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#0006F塞茜尔姐姐，\x01",
            "我都懒得再说什么了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4452")

    Jump("loc_453F")

    label("loc_4457")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448C")
    Call(0, 25)
    Jump("loc_453F")

    label("loc_448C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_452F")

    #C0203
    ChrTalk(
        0xC,
        (
            "#1300F小滴似乎\x01",
            "想送礼物\x01",
            "给她爸爸。\x02\x03",

            "如果在乌尔斯拉医院里\x01",
            "找到了材料，\x01",
            "可以麻烦你们拿过来吗？\x02\x03",

            "我想你们一定\x01",
            "能找到合适的材料，\x01",
            "拜托大家了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_453F")

    label("loc_452F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_453F")
    Call(0, 24)

    label("loc_453F")

    Jump("loc_4887")

    label("loc_4544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4740")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C0")

    #C0204
    ChrTalk(
        0xC,
        (
            "#1300F哎呀，罗伊德……\x01",
            "和约亚西姆医生谈过了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#0006F嗯，关、关于这件事……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将琪雅不愿意住院，\x01",
            "自己逃掉的事由做了说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xC,
        "#1305F哎……是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#0001F总之，我们现在\x01",
            "正在找琪雅……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xC,
        (
            "#1303F嗯～很不巧，我没看见她呢。\x02\x03",

            "#1308F如果刚刚才跑掉的话，\x01",
            "我想应该不会走得太远吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "不好意思，谢啦，塞茜尔姐姐。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 4)
    Jump("loc_473B")

    label("loc_46C0")


    #C0211
    ChrTalk(
        0xC,
        (
            "#1308F小琪雅的话，\x01",
            "我觉得应该不会\x01",
            "故意藏到哪里去……\x02\x03",

            "#1300F总之，先到各处找找看吧。\x01",
            "我要是看见她的话，也会联系你的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_473B")

    Jump("loc_4887")

    label("loc_4740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_47EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475B")
    Call(0, 9)
    Jump("loc_47EA")

    label("loc_475B")


    #C0212
    ChrTalk(
        0xC,
        (
            "#1300F约亚西姆医生\x01",
            "应该在楼顶的研究楼吧。\x02\x03",

            "虽然平时有点漫不经心，\x01",
            "但他是位非常优秀的医生哦。\x02\x03",

            "关于小琪雅的失忆，\x01",
            "说不定他会知道些什么呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47EA")

    Jump("loc_4887")

    label("loc_47EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_47FD")
    Jump("loc_4887")

    label("loc_47FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_480B")
    Jump("loc_4887")

    label("loc_480B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_481C")
    Call(0, 13)
    Jump("loc_4887")

    label("loc_481C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_482A")
    Jump("loc_4887")

    label("loc_482A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4838")
    Jump("loc_4887")

    label("loc_4838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_4846")
    Jump("loc_4887")

    label("loc_4846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4854")
    Jump("loc_4887")

    label("loc_4854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4862")
    Jump("loc_4887")

    label("loc_4862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4870")
    Jump("loc_4887")

    label("loc_4870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_487E")
    Jump("loc_4887")

    label("loc_487E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4887")

    label("loc_4887")

    TalkEnd(0xFE)
    Return()

    # Function_12_3CFA end

    def Function_13_488B(): pass

    label("Function_13_488B")

    TurnDirection(0xC, 0x8, 0)
    SetChrSubChip(0x8, 0x2)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3E")

    #C0213
    ChrTalk(
        0x8,
        (
            "#1502F塞茜尔小姐\x01",
            "在庆典第一天请了假吧？\x02\x03",

            "纪念庆典怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "#1300F呵呵，非常开心哦。\x02\x03",

            "#1304F和罗伊德看了彩虹剧团的公演，\x01",
            "之后和伊莉娅她们一起吃了饭……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        "#1500F哇，好羡慕呢。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        (
            "#1304F……那个，小滴。\x02\x03",

            "#1300F虽然今年的庆典我已经没假了……\x01",
            "不过，明年的纪念庆典要不要一起去呢？\x02\x03",

            "#1309F叫上罗伊德他们和亚里欧斯先生，\x01",
            "大家一起去玩吧。\x01",
            "一定会很开心的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "#1502F……好的！\x01",
            "请一定带我去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4AAF")

    label("loc_4A3E")


    #C0218
    ChrTalk(
        0xC,
        (
            "#1309F明年的纪念庆典，\x01",
            "叫上罗伊德他们和亚里欧斯先生，\x01",
            "大家一起去玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "#1502F……好的！\x01",
            "请一定带我去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AAF")

    SetChrSubChip(0x8, 0x0)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_488B end

    def Function_14_4AB8(): pass

    label("Function_14_4AB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B29")

    #C0220
    ChrTalk(
        0xFE,
        "哦～好宽敞的医院啊。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "不过……\x01",
            "我觉得我家\x01",
            "比这里更宽更大。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "……是、是真的啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4B64")

    label("loc_4B29")


    #C0223
    ChrTalk(
        0xFE,
        (
            "我家比这个医院\x01",
            "更宽敞更大哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "……是、是真的啦。\x02",
    )

    CloseMessageWindow()

    label("loc_4B64")

    TalkEnd(0xFE)
    Return()

    # Function_14_4AB8 end

    def Function_15_4B68(): pass

    label("Function_15_4B68")

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
            "#5P#1302F哎呀，罗伊德。\x01",
            "呵呵，欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        "#11P#1502F啊……大家好！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#6P#0000F你们好。\x02\x03",

            "小滴，\x01",
            "之前谢谢你了。\x02\x03",

            "谢谢你和琪雅做朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#11P#1505F哪、哪里，\x01",
            "该道谢的是我……\x02\x03",

            "#1502F对了，小琪雅她还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x104,
        (
            "#12P#0300F嗯，精神过头了，\x01",
            "反而让人伤脑筋呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#6P#0102F呵呵，\x01",
            "她每天都十分活泼快乐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x103,
        (
            "#12P#0203F……不过记忆方面\x01",
            "还是毫无线索。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        (
            "#11P#1508F是吗……\x02\x03",

            "#1502F那个，请转告小琪雅……\x01",
            "我一定会去找她玩的……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，好的，\x01",
            "到时候我们也会热烈欢迎你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xC,
        "#5P#1302F嘻……\x02",
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

    # Function_15_4B68 end

    def Function_16_4E36(): pass

    label("Function_16_4E36")

    TalkBegin(0xD)
    TurnDirection(0xD, 0xB, 0)
    SetChrSubChip(0xB, 0x1)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F6C")

    #C0235
    ChrTalk(
        0xB,
        (
            "你……是昨天\x01",
            "在我的床单上弄了\x01",
            "番茄酱的护士吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        "怎么，是来谢罪的吗？\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xD,
        (
            "嗯……是的，\x01",
            "真是十分抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xD,
        (
            "弄脏的床单也洗好了，\x01",
            "顺便帮您换上吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xD,
        (
            "……啊哈哈，弄脏的\x01",
            "地方留下印迹了。\x01",
            "就好像尿床了一样～\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        (
            "瞧、瞧不起我吗……？\x01",
            "这种时候，一般\x01",
            "都应该拿新的来吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4FD1")

    label("loc_4F6C")


    #C0241
    ChrTalk(
        0xD,
        (
            "啊哈哈，看这床单啊～\x01",
            "好像尿床了一样～\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xB,
        (
            "可、可恶，不准笑！\x01",
            "被人听见的话，\x01",
            "不知会怎么想我呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD1")

    SetChrSubChip(0xB, 0x0)
    OP_4C(0xD, 0xFF)
    TalkEnd(0xD)
    Return()

    # Function_16_4E36 end

    def Function_17_4FDD(): pass

    label("Function_17_4FDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4FEE")
    Jump("loc_5124")

    label("loc_4FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_5054")

    #C0243
    ChrTalk(
        0xFE,
        (
            "好痛好痛……\x01",
            "被一个小女孩撞倒，\x01",
            "摔了个四脚朝天。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "真是的，那孩子在干什么呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5124")

    label("loc_5054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_5124")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506F")
    Call(0, 11)
    Jump("loc_5124")

    label("loc_506F")


    #C0245
    ChrTalk(
        0xFE,
        (
            "（呵呵……本来还被蛮不讲理的大叔惹得\x01",
            "  满腔怨气，但听了这孩子的话之后，\x01",
            "  一下就平静了来。）\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "（谢谢了，小姑娘。）\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x153,
        (
            "#1100F嗯？嘿嘿……\x01",
            "虽然不太明白，不过真是太好了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5124")

    TalkEnd(0xFE)
    Return()

    # Function_17_4FDD end

    def Function_18_5128(): pass

    label("Function_18_5128")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_513D")
    Call(0, 8)
    Jump("loc_51AB")

    label("loc_513D")


    #C0248
    ChrTalk(
        0xFE,
        (
            "#2400F接下来……要是有机会偷懒就好了。\x01",
            "在纪念庆典中\x01",
            "也有很多工作呢。\x02\x03",

            "#2406F哎呀呀，当副教授也不轻松啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51AB")

    TalkEnd(0xFE)
    Return()

    # Function_18_5128 end

    def Function_19_51AF(): pass

    label("Function_19_51AF")

    TalkBegin(0xFE)

    #C0249
    ChrTalk(
        0xFE,
        "哦……都这么晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "我也该回去写日记了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_51AF end

    def Function_20_51EA(): pass

    label("Function_20_51EA")

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

    def lambda_5306():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5306)

    def lambda_531B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_531B)
    Sleep(100)

    def lambda_532F():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_532F)

    def lambda_5344():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5344)
    Sleep(50)

    def lambda_5358():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5358)

    def lambda_536D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_536D)
    Sleep(80)

    def lambda_5381():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5381)

    def lambda_5396():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5396)
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
        "#0005F#12P啊，塞茜尔姐姐……\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_544A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_544A)
    WaitChrThread(0xC, 1)

    #C0252
    ChrTalk(
        0xC,
        "#1305F#5P哎呀，罗伊德。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #N0253
    NpcTalk(
        0x8,
        "少女",
        "#1505F#5P啊……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_68(-99570, 1000, 55330, 2500)
    SetCameraDistance(27360, 2500)

    def lambda_54B5():
        OP_95(0xFE, -99720, 0, 54250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54B5)
    Sleep(200)

    def lambda_54D2():
        OP_95(0xFE, -100830, 0, 54280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54D2)
    Sleep(100)

    def lambda_54EF():
        OP_95(0xFE, -100790, 0, 53070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_54EF)
    Sleep(150)

    def lambda_550C():
        OP_95(0xFE, -99570, 0, 53110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_550C)
    OP_93(0xC, 0x10E, 0x12C)

    def lambda_552D():
        OP_95(0xFE, -100070, 0, 55900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_552D)
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
            "#0000F#12P我听护士长说\x01",
            "你在这里。\x02\x03",

            "那个，是不是打扰你们了？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        "#1309F#5P呵呵，没关系啦。\x02",
    )

    CloseMessageWindow()

    def lambda_55D0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_55D0)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0256
    ChrTalk(
        0xC,
        (
            "#1302F#6P──小滴，\x01",
            "这几位就是我刚刚跟你说的哥哥姐姐哦。\x02\x03",

            "他们可是隶属于克洛斯贝尔警察局的，\x01",
            "正义的巡逻警官哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        "#0011F#12P正、正义的……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        (
            "#0109F#6P这个实在是有点\x01",
            "夸张了吧……\x02",
        )
    )

    CloseMessageWindow()

    #N0259
    NpcTalk(
        0x8,
        "少女",
        "#1502F#5P……嘻嘻。\x02",
    )

    CloseMessageWindow()
    OP_68(-98580, 1000, 56100, 2000)

    def lambda_56D0():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56D0)
    Sleep(50)

    def lambda_56E0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_56E0)
    Sleep(50)

    def lambda_56F0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_56F0)
    Sleep(50)

    def lambda_5700():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5700)
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
            "嗯，那个……\x01",
            "各位工作辛苦了。\x02\x03",

            "我叫滴……\x01",
            "滴·马克莱因。\x02",
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
        "#0009F#6P哈哈……你好。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0262
    ChrTalk(
        0x101,
        "#0005F#6P嗯……咦……？\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        "#0105F#6P马克莱因……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        "#0303F#12P嗯～好像曾在哪里听到过呢。\x02",
    )

    CloseMessageWindow()

    def lambda_585B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_585B)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0265
    ChrTalk(
        0xC,
        (
            "#1304F#5P呵呵，说不定\x01",
            "你们其实见过的。\x02\x03",

            "#1300F小滴的爸爸\x01",
            "就是那位亚里欧斯先生。\x02",
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
        "#0011F#6P哎！？\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x103,
        "#0205F#6P『风之剑圣』……\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x104,
        "#0305F#12P那位大叔，竟然还有女儿啊！？\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x8,
        (
            "#1505F#5P那个……各位\x01",
            "认识我爸爸吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_59BA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_59BA)

    #C0270
    ChrTalk(
        0x101,
        (
            "#0012F#6P不、不，也不算认识啦。\x02\x03",

            "#0000F之前遭遇危险的时候，\x01",
            "承蒙他出手相救……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#1500F#5P呵呵，是这样啊……\x02\x03",

            "我爸爸的态度比较冷淡，\x01",
            "没有冒犯各位吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#0011F#6P哪、哪里的话，完全没有那回事。\x02\x03",

            "#0003F只是，见识到了还有那么厉害的人存在，\x01",
            "忍不住就紧张了起来……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        (
            "#0104F#6P他虽然严厉，但是很会关心人，\x01",
            "看起来也很可靠。\x02\x03",

            "#0102F呵呵，真是个好父亲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "#1502F#5P嘿嘿……\x01",
            "谢谢大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "#1309F#6P呵呵，小滴\x01",
            "是最爱爸爸的孩子嘛。\x02\x03",

            "#1302F但爸爸来探望的时候，\x01",
            "她却还是有所顾虑，不太撒娇……\x02\x03",

            "#1309F其实，说声『最喜欢爸爸了！』，\x01",
            "然后扑进他的怀里不就好了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        "#1501F#5P塞、塞茜尔小姐真是的……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        "#0009F#6P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x104,
        (
            "#0302F#12P（那个实力超强的大叔\x01",
            "  面对女儿撒娇的画面吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        "#0204F#6P（真有点难以想象呢……）\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5CB8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5CB8)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0280
    ChrTalk(
        0xC,
        (
            "#1301F#5P说起来，关于那件事。\x02\x03",

            "其实，小滴似乎\x01",
            "有什么发现。\x02",
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
        "#0005F#6P发现……？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "#1508F#5P嗯，那个……\x01",
            "就在利顿医生遇袭\x01",
            "的那天晚上。\x02\x03",

            "我睡不着，\x01",
            "就开始读盲文书……\x02\x03",

            "就在那时，好像\x01",
            "听见了惨叫声。\x02",
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
        "#0001F#6P真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        "#0101F#6P后来呢……后来怎么样了？\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#1508F#5P那个，我有点担心，\x01",
            "就打开了那边的窗子\x01",
            "仔细听了听……\x02\x03",

            "但是没有再听到惨叫声，\x01",
            "反而听到了『呼呼呼』\x01",
            "这样的喘气声……\x02\x03",

            "过了一会，又听到『咚咚』声，\x01",
            "好像是什么东西在蹦跳的声音……\x02\x03",

            "嗯……然后就没了。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        (
            "#0003F#6P是吗……\x02\x03",

            "#0001F这件事，你告诉过警备队的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        (
            "#1501F#5P那个，我一直以为\x01",
            "自己是在做梦……\x02\x03",

            "刚才听了塞茜尔小姐说的话，\x01",
            "才想起这件事来……\x02\x03",

            "#1508F对、对不起……\x01",
            "我应该早点说出来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        "#0002F#6P不，没关系的。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        "#0104F#6P谢谢你告诉我们。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        (
            "#0203F#6P不过……这证言完全\x01",
            "证实了楼顶的调查呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x104,
        (
            "#0303F#12P嗯，最初的惨叫\x01",
            "是那个实习医生昏过去时发出的……\x02\x03",

            "#0301F然后似乎是狼形魔兽的呼吸声，\x01",
            "还有跳到那些木箱上\x01",
            "逃跑时的声音吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        (
            "#1501F#5P还、还有……\x02\x03",

            "那个，也可能只是我\x01",
            "幻听了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0293
    ChrTalk(
        0x101,
        (
            "#0000F#6P……没关系的。\x01",
            "想到什么的话，都说出来就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "#1501F#5P好、好的。\x02\x03",

            "那个……在刚才说的\x01",
            "那些声音之间……\x02\x03",

            "好像……\x01",
            "还听到了『嘟～』的一声\x01",
            "很刺耳的声音。\x02",
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
        "#0205F#6P刺耳的『嘟～』……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        (
            "#0301F#12P唔，难道是某种魔兽\x01",
            "所特有的叫声吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        "#0101F#6P那个声音，平时没听到过吧？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x8,
        (
            "#1505F#5P嗯……\x01",
            "应该只有在那天晚上听到过。\x02\x03",

            "#1508F那个……可能还是\x01",
            "我幻听了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0004F#6P不……\x01",
            "这证言很宝贵，谢谢你。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6389():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6389)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0300
    ChrTalk(
        0x101,
        (
            "#0001F#12P──塞茜尔姐姐。\x01",
            "我们查明了不少事情，\x01",
            "先向你报告一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xC,
        "#1304F#5P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_6400():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6400)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0302
    ChrTalk(
        0xC,
        (
            "#1300F#6P那么，小滴。\x01",
            "晚饭的时候我再来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "#1502F#5P好的，\x01",
            "工作请加油。\x02\x03",

            "罗伊德警官，你们也是……\x01",
            "调查请加油哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_648F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_648F)
    WaitChrThread(0x101, 1)

    #C0304
    ChrTalk(
        0x101,
        "#0002F#6P嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        "#0102F#6P我们会再来玩的。\x02",
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

    def lambda_659A():
        OP_95(0xFE, -22510, 0, 31530, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_659A)

    def lambda_65B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_65B4)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xC, 2)

    def lambda_65CD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_65CD)
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
            "#0001F#12P塞茜尔姐姐。\x01",
            "那个，她……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6628():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6628)
    WaitChrThread(0xC, 1)
    Sleep(300)

    #C0307
    ChrTalk(
        0xC,
        (
            "#1303F#5P嗯……在几年前的事故中，\x01",
            "眼睛失明了。\x02\x03",

            "#1300F不过，并不是完全\x01",
            "没有恢复的希望。\x02\x03",

            "现在正在逐渐接受康复治疗，\x01",
            "同时过着疗养生活。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        "#0003F#12P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        "#0206F#6P……真辛苦啊。\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xC,
        (
            "#1304F#5P呵呵……\x01",
            "她是个很坚强的孩子呢。\x02\x03",

            "爸爸是个大忙人，\x01",
            "很少有机会见面，明明觉得很寂寞，\x01",
            "却刻意表现得很开朗……\x02\x03",

            "#1302F要是方便的话，\x01",
            "也请你们今后多陪陪她哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        "#0000F#12P嗯……乐意之至。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        (
            "#0104F#6P是呀，\x01",
            "她看起来也是个很乖巧的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#0202F#6P……是啊。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x104,
        (
            "#0309F#12P就用我诙谐幽默的话语，\x01",
            "让那孩子露出笑容吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "#1309F#5P呵呵，谢谢。\x02\x03",

            "#1300F那么……\x01",
            "你们查明了些什么呢？\x02\x03",

            "能不能详细说给我听听？\x02",
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

    # Function_20_51EA end

    def Function_21_68C7(): pass

    label("Function_21_68C7")

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
            "#0802F#6P嘿，好有趣～！\x01",
            "原来还有盲文的画册啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x12,
        "#0902F#6P是吗，连画也是立体的啊。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#1500F#5P呵呵……就是数量\x01",
            "还不太多。\x02\x03",

            "我希望自己将来\x01",
            "也能够出版\x01",
            "这样的书。\x02\x03",

            "#1510F即使是眼睛看不见的我，\x01",
            "应该也能做到吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        "#0808F#6P小滴……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x12,
        (
            "#0901F#6P……以你的情况来说，\x01",
            "还是有可能\x01",
            "恢复视力的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x8,
        (
            "#1510F#5P……嗯，医生们\x01",
            "是这样说的……\x02\x03",

            "不过，我觉得也有必要考虑到\x01",
            "无法恢复的情况……\x02\x03",

            "#1508F……对、对不起，\x01",
            "和艾丝蒂尔姐姐你们\x01",
            "说这种话也无济于事……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x11,
        (
            "#0801F#6P我说啊～！\x01",
            "不要再这样见外啦！\x02",
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
            "艾丝蒂尔紧紧握住了小滴的手。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0324
    ChrTalk(
        0x8,
        "#1505F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x11,
        (
            "#0802F#6P这不是很好嘛！\x01",
            "创作眼睛看得见的孩子\x01",
            "和看不见的孩子都会喜欢的画册！\x02\x03",

            "#0809F我觉得这是一件非常美妙的事哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x12,
        (
            "#0904F#6P的确，因为光是用手触摸，\x01",
            "就能从这本画册中\x01",
            "感觉到作者的真心与温暖呢……\x02\x03",

            "#0900F我觉得你应该珍惜\x01",
            "想创作这种作品的\x01",
            "心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "#1505F#5P艾丝蒂尔姐姐、约修亚哥哥……\x02\x03",

            "#1510F呜……\x01",
            "谢谢你们……\x02",
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
            "#0805F#6P哇哇！\x01",
            "等一下，小滴……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x12,
        (
            "#0902F#6P哈哈……\x01",
            "抱歉，好像说了奇怪的话呢。\x02",
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
            "#0002F（嗯～……\x01",
            "  虽然进去拜访一下倒也无妨……）\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        (
            "#0109F（但、但看现在这种气氛，\x01",
            "  最好还是不要打扰他们了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x104,
        "#0304F#5P（嗯，下次有机会的话，再来看她吧。）\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        "#0202F（是啊……）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -22600, 0, 31500, 0)
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    SetScenarioFlags(0xB7, 1)
    EventEnd(0x5)
    Return()

    # Function_21_68C7 end

    def Function_22_6EF5(): pass

    label("Function_22_6EF5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　　　　 织物仓库 　　　　　　\x01",
            "※非职员请勿入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_6EF5 end

    def Function_23_6F60(): pass

    label("Function_23_6F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70B3")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7076")
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("医生的声音")

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……感觉怎么样？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("少女的声音")

    #A0336
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……啊，那个。\x01",
            "没什么变化。\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("医生的声音")

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "怎么了，\x01",
            "好像没什么精神……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("少女的声音")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哎……不，没有。\x01",
            "没什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x136,
        "#1303F……医生好像在进行诊察呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x68, 1)

    label("loc_7076")


    #C0340
    ChrTalk(
        0x101,
        (
            "#0000F虽然想探听情报……\x01",
            "但还是待会再来这里吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_74BD")

    label("loc_70B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_713F")
    TalkBegin(0xFF)
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("女性的声音")

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……然后呢……就……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("少女的声音")

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……嘻嘻……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#0003F（好像正在谈话啊……）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_74BD")

    label("loc_713F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_722E")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 1)), scpexpr(EXPR_END)), "loc_7223")
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("小滴的声音")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "对、对不起，突然\x01",
            "哭了出来……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("艾丝蒂尔的声音")

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊哈哈，没事没事。\x02\x03",

            "……好吧，小滴，\x01",
            "今天就尽情地\x01",
            "向姐姐撒娇吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#0004F（好像不方便打扰啊。\x01",
            "  ……还是走吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7226")

    label("loc_7223")

    Call(0, 21)

    label("loc_7226")

    TalkEnd(0xFF)
    Jump("loc_74BD")

    label("loc_722E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74BD")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_747B")
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("医生的声音")

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "小滴，感觉怎么样？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("小滴的声音")

    #A0348
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我很好，贝尔达因医生。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("医生的声音")

    #A0349
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "唔？\x01",
            "脸色似乎比平时好啊。\x02\x03",

            "是不是遇到什么好事了呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("小滴的声音")

    #A0350
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，那个……\x01",
            "今天有些事比较令人期待。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("医生的声音")

    #A0351
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是吗……\x01",
            "真不错啊。\x02\x03",

            "……好，\x01",
            "那我就开始诊察啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("小滴的声音")

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#0003F小滴……\x01",
            "好像正在接受诊察呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x153,
        "#1111F罗伊德，这间病房是……？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x101,
        (
            "#0005F啊，如此说来，\x01",
            "琪雅还不知道呢。\x02\x03",

            "#0000F好吧，那就\x01",
            "待会再过来\x01",
            "看看吧。\x02\x03",

            "到时候再把她介绍给琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x153,
        (
            "#1106F嗯～？\x02\x03",

            "#1110F虽然不太明白，\x01",
            "不过好吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 0)
    Jump("loc_74BA")

    label("loc_747B")


    #C0357
    ChrTalk(
        0x101,
        (
            "#0000F小滴正在接受诊察。\x02\x03",

            "先去约亚西姆医生那里\x01",
            "问问看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74BA")

    TalkEnd(0xFF)

    label("loc_74BD")

    SetChrName("")
    Return()

    # Function_23_6F60 end

    def Function_24_74C0(): pass

    label("Function_24_74C0")

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
            "#5P#1305F啊，说起来……\x02\x03",

            "#1300F……那个，各位。\x01",
            "如果有时间的话，\x01",
            "能不能帮个忙？\x02",
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
            "#11P#1505F啊……！\x01",
            "难、难道说……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x101,
        (
            "#6P#0005F？？？\x01",
            "好像有什么内情？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x8,
        (
            "#11P#1505F塞、塞茜尔小姐，\x01",
            "算了啦……！\x02\x03",

            "那只是我的一个\x01",
            "任性要求而已……！\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xC,
        (
            "#5P#1309F真是的，不用\x01",
            "这么客气啦。\x02\x03",

            "#1300F──其实呢，小滴的\x01",
            "爸爸的生日快到了。\x02\x03",

            "所以小滴\x01",
            "想给爸爸\x01",
            "准备一个礼物……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#12P#0105F哦……\x01",
            "是亚里欧斯先生的生日啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x104,
        (
            "#12P#0309F那个实力超强的大叔\x01",
            "也会有生日啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x103,
        "#12P#0203F兰迪前辈，那是当然的。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#6P#0000F原来如此，莫非是不知\x01",
            "要送什么，想和我们商量吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#11P#1505F不、不是的，那个……\x02\x03",

            "#1500F我想送给\x01",
            "爸爸一个\x01",
            "手制的护身符……\x02\x03",

            "正打算找些可以\x01",
            "当作材料的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        "#6P#0000F啊，原来如此！\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x109,
        (
            "#6P#0504F呵呵，使用身边\x01",
            "『刚好合适的东西』，\x01",
            "为重要的人制作护身符……\x02\x03",

            "#0500F是克洛斯贝尔自古以来的传统风俗呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        "#12P#0300F嘿，还有这种风俗啊。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#12P#0102F呵呵，我以前也给外公\x01",
            "做过类似的护身符呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x103,
        (
            "#12P#0200F那么，只要在\x01",
            "这家医院里面找出\x01",
            "适合制作护身符的材料……\x02\x03",

            "这样就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        "#11P#1502F……是、是的……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xC,
        (
            "#5P#1304F我想你们一定能\x01",
            "找到合适的材料。\x02\x03",

            "#1300F如果找到的话，\x01",
            "可以麻烦你们拿过来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#6P#0000F嗯，当然可以了。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x104,
        (
            "#12P#0300F既然是为了小滴，\x01",
            "自然要鼎力相助啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#11P#1500F不、不好意思……\x01",
            "麻烦各位了……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        (
            "#6P#0003F接下来的问题就是要做什么了，\x01",
            "希望你能给我们一个\x01",
            "收集东西的基本方向……\x02\x03",

            "#0000F你有没有决定好\x01",
            "要做什么样的东西呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#11P#1505F这、这个嘛……\x02\x03",

            "#1502F其实，在不久前，\x01",
            "我和塞茜尔小姐散步的时候，\x01",
            "捡到了一块触感很好的石头。\x02\x03",

            "让塞茜尔小姐帮我看过之后，\x01",
            "发现那是块很漂亮的石头，\x01",
            "所以就一直很小心地保存着……\x02\x03",

            "我想，能不能用这个做点什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xC,
        (
            "#5P#1300F是啊，我也觉得用那个当材料很不错。\x02\x03",

            "小滴给我看过，\x01",
            "摸起来能感觉到淡淡的温暖，\x01",
            "是块很神奇的石头呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x104,
        "#12P#0305F嘿，竟然有这种东西啊。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x102,
        (
            "#12P#0102F既然如此，\x01",
            "那就仔细想想怎样才能\x01",
            "充分利用上那块石头吧。\x02\x03",

            "#0104F还有，既然是\x01",
            "意义重大的礼物，自然也要\x01",
            "准备包装用的盒子呢。\x02\x03",

            "#0100F顺便也找找\x01",
            "盒子和丝带吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#6P#0000F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x8,
        (
            "#11P#1508F不、不好意思，\x01",
            "给大家添了这么多麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#6P#0000F不，别在意。\x01",
            "而且多亏有你的石头，才能将\x01",
            "收集材料的方向决定下来啊。\x02\x03",

            "那么，就赶快\x01",
            "去找找看吧。\x02",
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
            "任务【送给父亲的礼物】\x07\x00",
            "开始！\x02",
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

    # Function_24_74C0 end

    def Function_25_7ED8(): pass

    label("Function_25_7ED8")

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
        "#5P#1305F哎呀，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        "#11P#1502F莫非……？\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，我们找到了\x01",
            "几件似乎可以\x01",
            "当作材料的东西。\x02",
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
            "交出了。\x02",
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
            "交出了。\x02",
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
            "#11P#1502F哇……这个，\x01",
            "是做挂坠的材料吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        (
            "#6P#0000F还有就是\x01",
            "包装礼物用的盒子，\x01",
            "我们把这些也找来了哦。\x02",
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
            "交出了。\x02",
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
            "交出了。\x02",
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
            "#5P#1305F……真是有点吃惊呢。\x01",
            "仅是在乌尔斯拉医院里，\x01",
            "竟然也能找到这么好的东西呀。\x02\x03",

            "#1300F怎么样，小滴。\x01",
            "你觉得用这些东西\x01",
            "够给爸爸做个礼物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x8,
        (
            "#11P#1502F嗯……嗯！\x01",
            "已经足够了。\x02\x03",

            "这个挂坠扣好像\x01",
            "非常结实……\x02\x03",

            "这个皮绳也是，\x01",
            "爸爸戴在身上\x01",
            "应该也不会碍事。\x02\x03",

            "各位，真是\x01",
            "太谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#6P#0009F哈哈，能让你这么开心，\x01",
            "我们找得再累也值得哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x104,
        (
            "#12P#0304F毕竟是这～么可爱的\x01",
            "女孩子的请求嘛。\x02\x03",

            "#0300F大哥哥我们\x01",
            "可是拼命努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x102,
        "#12P#0102F呵呵，真是得意忘形啊。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x103,
        "#12P#0204F……嗯，但也不能否认他所说的呢。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xC,
        (
            "#5P#1300F对了，小滴……\x01",
            "难得把东西找齐了，\x01",
            "马上来试着制作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x8,
        (
            "#11P#1505F啊，好的，说得也是呢。\x02\x03",

            "#1502F罗伊德警官……\x01",
            "方便的话，你们要不要\x01",
            "留下来看看完成品？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，那就不客气了。\x01",
            "说不定还能\x01",
            "帮上忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x109,
        (
            "#6P#0500F虽然力量微薄，\x01",
            "但我也会努力帮忙的。\x02",
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
            "#1500F──嗯……\x02\x03",

            "接下来，只要把嵌好石头的\x01",
            "挂坠拴到皮绳上……\x02",
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
            "#11P#1505F做、做好了……！\x02\x03",

            "#1502F怎么样，各位。\x01",
            "做得还好吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        "#6P#0000F嗯，做得很好哦。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xC,
        (
            "#5P#1302F嗯，收到这么棒的礼物，\x01",
            "小滴的爸爸一定会很开心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x8,
        "#11P#1502F呼，太好了……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x104,
        (
            "#12P#0300F话说回来，\x01",
            "小滴捡到的石头\x01",
            "还真是挺不可思议呢。\x02\x03",

            "#0304F只是稍微打磨了一下，\x01",
            "就能刚好镶嵌在\x01",
            "挂坠扣里。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x102,
        (
            "#12P#0100F嗯，真的呢。\x01",
            "简直像是原本就\x01",
            "嵌在里面的一样。\x02\x03",

            "皮绳也能很自然地\x01",
            "和挂坠组合在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x103,
        (
            "#12P#0200F虽然十分朴素，\x01",
            "但反而更能\x01",
            "衬托出典雅的风格。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x109,
        (
            "#6P#0500F是呀……\x01",
            "就算放在珠宝店，\x01",
            "也不会显得逊色呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xC,
        "#5P#1300F呵呵，的确是呢。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x8,
        (
            "#11P#1502F……塞茜尔小姐，各位……\x01",
            "真是太谢谢你们了。\x01",
            "连拼装时都帮了我这么多忙……\x02\x03",

            "那个，这是我的一点点心意。\x01",
            "不嫌弃的话……\x02",
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
            "收下了。\x02",
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
            "#6P#0005F嵌着好漂亮的石头……\x01",
            "莫非和那个挂坠中的\x01",
            "石头是一样的？\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x8,
        (
            "#11P#1502F是的，其实我\x01",
            "当时捡了两块一样的石头。\x02\x03",

            "这块就嵌在\x01",
            "我以前坏掉的\x01",
            "胸针上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        (
            "#12P#0105F可、可是……\x01",
            "真的可以给我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "#11P#1500F嗯，当然了。\x02\x03",

            "因为我自己\x01",
            "一个人肯定做不出\x01",
            "这么好的礼物……\x02\x03",

            "所以，之前就打算把这个\x01",
            "送给帮助我的人。\x02\x03",

            "#1502F一开始是打算送给\x01",
            "塞茜尔小姐的，但刚才和\x01",
            "她商量了一下，所以就……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xC,
        (
            "#5P#1304F就是这样。\x02\x03",

            "#1300F你们帮忙收集了这么棒的材料，\x01",
            "自然有收下这个的资格啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        (
            "#12P#0309F啊哈哈，话都说到这份上了，\x01",
            "再拒绝就失礼了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x103,
        (
            "#12P#0200F我们就收下\x01",
            "人家的一片心意吧，罗伊德前辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x101,
        (
            "#6P#0004F……嗯，说得也是啊。\x02\x03",

            "#0000F谢谢你，小滴。\x01",
            "我们会善加使用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x8,
        (
            "#11P#1502F嗯，请务必让它派上用场吧。\x02\x03",

            "那么，各位，\x01",
            "真是太谢谢你们了。\x02",
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
            "任务【送给父亲的礼物】\x07\x00",
            "完成！\x02",
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

    # Function_25_7ED8 end

    def Function_26_8B7F(): pass

    label("Function_26_8B7F")

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
            "#5P不久前，住在列曼自治州的\x01",
            "爸爸妈妈给我寄来了\x01",
            "信和礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x9,
        (
            "#5P里面放有我想要的\x01",
            "玩具……\x01",
            "我真的很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x101,
        (
            "#12P#0000F哈哈，那太好啦。\x02\x03",

            "#0003F（话说，礼物吗……\x01",
            "  也许……）\x02\x03",

            "#0000F对了……\x01",
            "那礼物的盒子\x01",
            "你还留着吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x9,
        "#5P盒子？\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x9,
        (
            "#5P嗯，塞茜尔姐姐\x01",
            "帮我收起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x9,
        (
            "#5P她说那是重要的礼物，\x01",
            "所以最好把盒子也好好保存起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x104,
        (
            "#12P#0305F嘿……\x01",
            "女性在这方面\x01",
            "还真是细心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x103,
        (
            "#12P#0203F我觉得是兰迪前辈\x01",
            "你太马虎了而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x9,
        (
            "#5P嗯，大哥哥，你们\x01",
            "需要这个盒子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        "#12P#0000F嗯，其实……\x02",
    )

    CloseMessageWindow()

    #A0438
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德说明了正在收集\x01",
            "礼物材料的事由。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0439
    ChrTalk(
        0x101,
        (
            "#12P#0000F……就是这样了，\x01",
            "我们正在找礼物的\x01",
            "包装盒……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x9,
        "#5P是吗，小滴她……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x9,
        (
            "#5P小滴也真是的，既然这样的话，\x01",
            "早点跟我说就好了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x9,
        "#5P给，就是这个。\x02",
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
            "收下了。\x02",
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
            "#12P#0100F呀，保存得真好呢。\x02\x03",

            "这正是适合包装礼品的\x01",
            "漂亮盒子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x109,
        (
            "#6P#0500F……可以收下吗？\x01",
            "毕竟是你特意保存下来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x9,
        "#5P嗯，没关系。\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x9,
        (
            "#5P里面的玩具我已经拿出来了，\x01",
            "要不是塞茜尔姐姐叫我留下的话，\x01",
            "说不定都已经扔掉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x9,
        (
            "#5P而且，\x01",
            "我也想为\x01",
            "小滴做点什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        (
            "#12P#0000F是吗……\x01",
            "那我们就\x01",
            "不客气地收下啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x104,
        (
            "#12P#0304F哈哈，你还真是个\x01",
            "小小男子汉呢。\x02\x03",

            "#0300F将来一定很受女性欢迎哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x9,
        "#5P嘿嘿……\x02",
    )

    CloseMessageWindow()
    OP_29(0x2C, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_918B")
    OP_29(0x2C, 0x1, 0x5)

    #C0452
    ChrTalk(
        0x101,
        (
            "#12P#0000F（可以做礼物的材料都收集齐了，\x01",
            "  也找到了包装用的盒子和丝带……）\x02\x03",

            "（好，差不多该拿去\x01",
            "  给小滴了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_918B")

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

    # Function_26_8B7F end

    SaveToFile()

Try(main)
