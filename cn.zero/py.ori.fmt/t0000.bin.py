from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t0000.bin",                # FileName
        "t0000",                    # MapName
        "t0000",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 4, 0, 5],
    )

    BuildStringList((
        "t0000",                  # 0
        "艾尔琴",                 # 1
        "卡米尤",                 # 2
        "普莉",                   # 3
        "塞拉姆",                 # 4
        "迪利克",                 # 5
        "安洁",                   # 6
        "米莉亚",                 # 7
        "史蒂芬",                 # 8
        "彼德",                   # 9
        "特级钓师罗伊德",         # 10
        "克潘",                   # 11
        "游客",                   # 12
        "游客",                   # 13
        "游客姆拉修",             # 14
        "游客艾尔缇",             # 15
        "车",                     # 16
        "哈罗德",                 # 17
        "巴士",                   # 18
        "SE控制",                 # 19
        "阿尔摩利卡古道",         # 20
    ))

    AddCharChip((
        "chr/ch24400.itc",                   # 00
        "chr/ch24600.itc",                   # 01
        "chr/ch24700.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch24300.itc",                   # 05
        "chr/ch23700.itc",                   # 06
        "chr/ch33100.itc",                   # 07
        "chr/ch34300.itc",                   # 08
        "chr/ch32200.itc",                   # 09
        "chr/ch21200.itc",                   # 0A
        "chr/ch20600.itc",                   # 0B
        "apl/ch50165.itc",                   # 0C
        "apl/ch50169.itc",                   # 0D
        "apl/ch50166.itc",                   # 0E
        "chr/ch23600.itc",                   # 0F
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

    DeclNpc(8409,    0,       -12479,  17,   261,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-560,    0,       18309,   135,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(250,     0,       26870,   135,  261,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(13050,   0,       9680,    270,  261,  0x0, 0,   3,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(12779,   3500,    40220,   298,  389,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-9899,   0,       25219,   86,   389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(16590,   3500,    42799,   135,  389,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-9899,   0,       25219,   86,   389,  0x0, 0,   11,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-759,    289,     3460,    90,   405,  0x0, 0,   12,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(-740,    439,     5239,    90,   405,  0x0, 0,   13,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(-500,    500,     6000,    90,   405,  0x0, 0,   14,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(6030,    0,       15279,   178,  389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(7050,    0,       15500,   178,  389,  0x0, 0,   8,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-5989,   0,       -7019,   265,  385,  0x0, 0,   9,   0,   0,   3,   0,   26,  255,  0)
    DeclNpc(-7639,   0,       13699,   180,  385,  0x0, 0,   10,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-2000,   0,       -15000,  1500,    -2000,   1500,    -15000,  0x007C, 0,  30, 0x0000)
    DeclActor(11740,   0,       3950,    1200,    10890,   -1450,   1210,    0x007C, 0,  29, 0x0000)
    DeclActor(15160,   0,       -19080,  1200,    15160,   2000,    -19080,  0x007C, 0,  11, 0x0000)
    DeclActor(-16320,  3500,    61370,   5000,    -16320,  3500,    61370,   0x007C, 0,  41, 0x0000)

    PlaceName(28.0, 0.0, -40.0, 0x0000, 0x0000, "阿尔摩利卡古道")
    PlaceName(-25.0, 0.0, 20.0, 0x0000, 0x0053, "")
    PlaceName(20.399999618530273, 0.0, 25.25, 0x0000, 0x0052, "")
    PlaceName(-2.0, 0.0, -14.699999809265137, 0x0000, 0x0055, "")
    PlaceName(16.399999618530273, 0.0, -17.799999237060547, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_4C4",          # 00, 0
        "Function_1_57C",          # 01, 1
        "Function_2_5A7",          # 02, 2
        "Function_3_5D2",          # 03, 3
        "Function_4_5FD",          # 04, 4
        "Function_5_943",          # 05, 5
        "Function_6_B2B",          # 06, 6
        "Function_7_C10",          # 07, 7
        "Function_8_D51",          # 08, 8
        "Function_9_DE6",          # 09, 9
        "Function_10_136A",        # 0A, 10
        "Function_11_1459",        # 0B, 11
        "Function_12_1467",        # 0C, 12
        "Function_13_2371",        # 0D, 13
        "Function_14_2C0C",        # 0E, 14
        "Function_15_3047",        # 0F, 15
        "Function_16_375A",        # 10, 16
        "Function_17_40F2",        # 11, 17
        "Function_18_4A3D",        # 12, 18
        "Function_19_4FA7",        # 13, 19
        "Function_20_51FB",        # 14, 20
        "Function_21_5424",        # 15, 21
        "Function_22_548A",        # 16, 22
        "Function_23_5501",        # 17, 23
        "Function_24_5A1D",        # 18, 24
        "Function_25_5B0B",        # 19, 25
        "Function_26_5BE7",        # 1A, 26
        "Function_27_5D39",        # 1B, 27
        "Function_28_5E3B",        # 1C, 28
        "Function_29_6848",        # 1D, 29
        "Function_30_6910",        # 1E, 30
        "Function_31_699A",        # 1F, 31
        "Function_32_7195",        # 20, 32
        "Function_33_7668",        # 21, 33
        "Function_34_76CB",        # 22, 34
        "Function_35_772E",        # 23, 35
        "Function_36_7791",        # 24, 36
        "Function_37_77E3",        # 25, 37
        "Function_38_7B40",        # 26, 38
        "Function_39_8BE9",        # 27, 39
        "Function_40_8C05",        # 28, 40
        "Function_41_8C48",        # 29, 41
        "Function_42_977E",        # 2A, 42
        "Function_43_9D18",        # 2B, 43
    ))


    def Function_0_4C4(): pass

    label("Function_0_4C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_504"),
        (1, "loc_510"),
        (2, "loc_51C"),
        (3, "loc_528"),
        (4, "loc_534"),
        (5, "loc_540"),
        (6, "loc_54C"),
        (SWITCH_DEFAULT, "loc_558"),
    )


    label("loc_504")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_510")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_51C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_528")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_534")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_540")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_54C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_558")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_564")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_57B")

    Return()

    # Function_0_4C4 end

    def Function_1_57C(): pass

    label("Function_1_57C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A6")
    OP_94(0xFE, 0xFFFFECDC, 0x49FC, 0x7D0, 0x588E, 0x3E8)
    Sleep(250)
    Jump("Function_1_57C")

    label("loc_5A6")

    Return()

    # Function_1_57C end

    def Function_2_5A7(): pass

    label("Function_2_5A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D1")
    OP_94(0xFE, 0xFFFFECDC, 0x5BEA, 0xC62, 0x7242, 0x3E8)
    Sleep(300)
    Jump("Function_2_5A7")

    label("loc_5D1")

    Return()

    # Function_2_5A7 end

    def Function_3_5D2(): pass

    label("Function_3_5D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FC")
    OP_94(0xFE, 0xFFFFDF58, 0xFFFFDA3A, 0xFFFFF3BC, 0xFFFFEDF4, 0x7D0)
    Sleep(300)
    Jump("Function_3_5D2")

    label("loc_5FC")

    Return()

    # Function_3_5D2 end

    def Function_4_5FD(): pass

    label("Function_4_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_64D")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7830, 0, 23860, 107)
    SetChrPos(0x9, -6870, 0, 24790, 180)
    SetChrPos(0xA, -6110, 0, 23270, 315)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_69D")
    SetChrPos(0x9, -7700, 0, 24530, 0)
    SetChrPos(0xA, -7700, 0, 25980, 180)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -18070, 3500, 60260, 267)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6ED")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7830, 0, 23860, 107)
    SetChrPos(0x9, -6870, 0, 24790, 180)
    SetChrPos(0xA, -6110, 0, 23270, 315)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_6ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_727")
    SetChrPos(0x9, -8980, 0, 25880, 225)
    SetChrPos(0xA, -8960, 0, 24860, 315)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_8B9")

    label("loc_727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_746")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_8B9")

    label("loc_746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_78A")
    SetChrPos(0x9, -8980, 0, 25880, 225)
    SetChrPos(0xA, -8960, 0, 24860, 315)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_8B9")

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B3")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_8B9")

    label("loc_7B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7CD")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_8B9")

    label("loc_7CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7FD")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -18070, 3500, 60260, 267)
    Jump("loc_8B9")

    label("loc_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_837")
    SetChrPos(0x9, -6350, 0, 25950, 180)
    SetChrPos(0xA, -6330, 0, 24330, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_8B9")

    label("loc_837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_860")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_END)), "loc_889")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_8B9")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8B9")
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -18070, 3500, 60260, 267)
    ClearChrFlags(0xD, 0x80)

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EF")
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x1, 3)
    Event(0, 31)
    Jump("loc_91B")

    label("loc_8EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_905")
    Event(0, 32)
    Jump("loc_91B")

    label("loc_905")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91B")
    Event(0, 37)

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_92A")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_942")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_942")

    Return()

    # Function_4_5FD end

    def Function_5_943(): pass

    label("Function_5_943")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_964")
    Jump("loc_995")

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_978")
    ClearMapObjFlags(0x8, 0x4)
    Jump("loc_995")

    label("loc_978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_986")
    Jump("loc_995")

    label("loc_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_995")
    ClearMapObjFlags(0x8, 0x4)

    label("loc_995")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9A7")
    Jump("loc_9E4")

    label("loc_9A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9E4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9C1")
    Jump("loc_9E4")

    label("loc_9C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_9D3")
    Jump("loc_9E4")

    label("loc_9D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_9E4")
    OP_66(0x3, 0x1)

    label("loc_9E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('咪雪缎带', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber('进击刻印', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('超·必胜扎头巾', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('超·斗魂腰带', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('正义徽章', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('幸运刻印', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A35")
    OP_65(0x1, 0x1)

    label("loc_A35")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 10890, -1450, 1210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x9, 0x4)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC6")
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    ClearMapObjFlags(0x9, 0x4)
    OP_66(0x2, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ACB")

    label("loc_AC6")

    OP_16(0x3, 0x4, 0x1, 0x0)

    label("loc_ACB")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE3")
    OP_1B(0x0, 0x0, 0x2B)

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AF4")
    OP_24(0x7B)
    Jump("loc_B2A")

    label("loc_AF4")

    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E1(0x1B26, 0x1F4, 0x143C)
    OP_E1(0x7936, 0x1F4, 0xFFFFFD6C)

    label("loc_B2A")

    Return()

    # Function_5_943 end

    def Function_6_B2B(): pass

    label("Function_6_B2B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市东出口\x01",      # 0
            "唐古拉姆门\x01",              # 1
            "停靠站（三岔路）\x01",        # 2
            "放弃\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC3")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_C08")

    label("loc_BC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE8")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_C08")

    label("loc_BE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C08")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_C08")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_B2B end

    def Function_7_C10(): pass

    label("Function_7_C10")

    Fade(1000)
    OP_68(4100, 1500, -16270, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(17000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -400, 0, -15300, 135)
    SetChrPos(0x1, -1230, 0, -15500, 135)
    SetChrPos(0x2, -2000, 0, -15700, 135)
    SetChrPos(0x3, -2750, 0, -15900, 135)
    ClearChrFlags(0x19, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x2)
    OP_78(0x7, 0x19)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x19, 15920, 0, -24600, 0)
    OP_D3(0x19, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_0D()
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)

    def lambda_CEC():
        OP_95(0xFE, 10630, 0, -20520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_CEC)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x19, 1)

    def lambda_D16():
        OP_9E(0xFE, 0x1770, 0xFFFF987C, 0xFFFF0DD0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_D16)
    WaitChrThread(0x19, 1)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x7)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_C10 end

    def Function_8_D51(): pass

    label("Function_8_D51")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -700, 0, -13900, 135)
    SetChrPos(0x1, -700, 0, -13900, 135)
    SetChrPos(0x2, -700, 0, -13900, 135)
    SetChrPos(0x3, -700, 0, -13900, 135)
    OP_68(-690, 1500, -13900, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_D51 end

    def Function_9_DE6(): pass

    label("Function_9_DE6")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1362")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FF")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8C")
    MenuCmd(1, 1, "★克洛斯贝尔·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_EA6")

    label("loc_E8C")

    MenuCmd(1, 1, "　克洛斯贝尔·中央广场")

    label("loc_EA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED6")
    MenuCmd(1, 1, "★克洛斯贝尔·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_EEE")

    label("loc_ED6")

    MenuCmd(1, 1, "　克洛斯贝尔·东出口")

    label("loc_EEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1E")
    MenuCmd(1, 1, "★克洛斯贝尔·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_F36")

    label("loc_F1E")

    MenuCmd(1, 1, "　克洛斯贝尔·西出口")

    label("loc_F36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F66")
    MenuCmd(1, 1, "★克洛斯贝尔·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_F7E")

    label("loc_F66")

    MenuCmd(1, 1, "　克洛斯贝尔·南出口")

    label("loc_F7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAE")
    MenuCmd(1, 1, "★克洛斯贝尔·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_FC6")

    label("loc_FAE")

    MenuCmd(1, 1, "　克洛斯贝尔·北出口")

    label("loc_FC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEE")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_FFE")

    label("loc_FEE")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_FFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1026")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1036")

    label("loc_1026")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_1036")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1064")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_107A")

    label("loc_1064")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_107A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A4")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_10B6")

    label("loc_10A4")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_10B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E0")
    MenuCmd(1, 1, "★玛因兹矿山镇")
    MenuCmd(3, 1, 0x9)
    Jump("loc_10F2")

    label("loc_10E0")

    MenuCmd(1, 1, "　玛因兹矿山镇")

    label("loc_10F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1122")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_113A")

    label("loc_1122")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_113A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1160")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_116E")

    label("loc_1160")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_116E")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F0")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x9)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1243"),
        (1, "loc_1251"),
        (2, "loc_125F"),
        (3, "loc_126D"),
        (4, "loc_127B"),
        (5, "loc_1289"),
        (6, "loc_1297"),
        (7, "loc_12A5"),
        (8, "loc_12B3"),
        (9, "loc_12C1"),
        (10, "loc_12CF"),
        (11, "loc_12DD"),
        (SWITCH_DEFAULT, "loc_12EB"),
    )


    label("loc_1243")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_1251")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_125F")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_126D")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_127B")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_1289")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_1297")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_12A5")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_12B3")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_12C1")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_12CF")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_12DD")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12EB")

    label("loc_12EB")

    Jump("loc_12FA")

    label("loc_12F0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12FA")

    Jump("loc_135D")

    label("loc_12FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_134A")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_135D")

    label("loc_134A")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_135D")

    Jump("loc_E00")

    label("loc_1362")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_DE6 end

    def Function_10_136A(): pass

    label("Function_10_136A")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 13840, 0, -19790, 225)
    SetChrPos(0x1, 13840, 0, -19790, 225)
    SetChrPos(0x2, 13840, 0, -19790, 225)
    SetChrPos(0x3, 13840, 0, -19790, 225)
    SetChrPos(0x4, 13840, 0, -19790, 225)
    SetChrPos(0x5, 13840, 0, -19790, 225)
    Sleep(1)
    OP_68(13840, 1500, -19790, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_143E")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_1444")

    label("loc_143E")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_1444")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_136A end

    def Function_11_1459(): pass

    label("Function_11_1459")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_11_1459 end

    def Function_12_1467(): pass

    label("Function_12_1467")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151A")

    #C0002
    ChrTalk(
        0xFE,
        (
            "啊，找到书了啊。\x01",
            "太好了～……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "因为这本书是关于彩虹剧团的，\x01",
            "所以一直想看得不得了。\x01",
            "好说歹说才硬借了过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "这就是彩虹剧团的\x01",
            "魔力吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_151A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A1")

    #C0005
    ChrTalk(
        0xFE,
        (
            "我把书借给了\x01",
            "农夫多纳尔德先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "他应该在雷欧鲁杂货店\x01",
            "隔壁的民居里。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "唉，真是万分抱歉……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_15A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BE")
    Call(0, 42)
    TalkEnd(0xFE)
    Return()

    label("loc_15BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1670")

    #C0008
    ChrTalk(
        0xFE,
        (
            "嗯嗯～真是个清爽的早晨啊，\x01",
            "是最适合开车兜风的好天气……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "……俺现在就已经\x01",
            "等不及去送菜了哇！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "……咳咳，\x01",
            "我已经迫不及待地想去送蔬菜了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16F5")

    label("loc_1670")


    #C0011
    ChrTalk(
        0xFE,
        (
            "嗯，一说到车子，\x01",
            "就忍不住兴奋过头，带上了口音啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "平时都装模作样地讲普通话，\x01",
            "偶尔一露出口音就更丢人……\x01",
            "下次可要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F5")

    Jump("loc_236D")

    label("loc_16FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_177D")

    #C0013
    ChrTalk(
        0xFE,
        (
            "早上去克洛斯贝尔市\x01",
            "送蔬菜的时候，\x01",
            "发现有一群人聚集在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "听说是黑手党之间展开争斗了。\x01",
            "哎，真是不太平啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236D")

    label("loc_177D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A14")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1907")

    #C0015
    ChrTalk(
        0xFE,
        "呼啊～……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "不好不好，日子太过和平，\x01",
            "忍不住就打呵欠了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0xFE, 0x73, 0x1F4)

    #C0017
    ChrTalk(
        0xFE,
        (
            "话说……那个难不成……\x01",
            "是警备队的轻型装甲车吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "没有装载粗野的武器，\x01",
            "这超凡脱俗的外形……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "嗯～真是太帅了啊！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x109,
        (
            "#0505F哦哦……您真有见识呢！\x02\x03",

            "#0509F呵呵，果然只有懂行的人\x01",
            "才能明白它的优点啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#0306F嗯～真是个难以理解的世界啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19A0")

    label("loc_1907")


    #C0022
    ChrTalk(
        0xFE,
        "……咳咳。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "我记得，警备队的轻型装甲车\x01",
            "虽然战斗力较低，\x01",
            "但是造型很优美呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "这么好的车，\x01",
            "可要注意别撞到哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        "#0500F呵呵，谢谢您的忠告。\x02",
    )

    CloseMessageWindow()

    label("loc_19A0")

    Jump("loc_1A0F")

    label("loc_19A5")


    #C0026
    ChrTalk(
        0xFE,
        "呼啊～……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "不好不好，日子太过和平，\x01",
            "忍不住就打呵欠了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "要注意不要放松过头，\x01",
            "撞到车才是啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0F")

    Jump("loc_236D")

    label("loc_1A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA2")

    #C0029
    ChrTalk(
        0xFE,
        "今年的纪念庆典到今天就结束了啊。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "迪利克开了露天店、\x01",
            "游客闯进了古战场……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "还挺刺激的，过得很开心呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AF6")

    label("loc_1AA2")


    #C0032
    ChrTalk(
        0xFE,
        (
            "又是迪利克开露天店，\x01",
            "又是游客闯进古战场……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "今年的纪念庆典\x01",
            "还真够刺激啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF6")

    Jump("loc_236D")

    label("loc_1AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B6F")

    #C0034
    ChrTalk(
        0xFE,
        (
            "因为是纪念庆典的最终日，\x01",
            "所以明天一天会放假。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "我要不要去把送货用的卡车\x01",
            "借来，然后兜兜风呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236D")

    label("loc_1B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C31")

    #C0036
    ChrTalk(
        0xFE,
        (
            "和往年一样，纪念庆典的\x01",
            "游客也会来我们村子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "而且，因为今年\x01",
            "在露天店上费了很多心思，\x01",
            "游客的数量似乎也多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "导力巴士\x01",
            "会有这么多班次，\x01",
            "可是很少见的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C7F")

    label("loc_1C31")


    #C0039
    ChrTalk(
        0xFE,
        (
            "和往年一样，\x01",
            "纪念庆典的游客\x01",
            "也会来我们村子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "导力巴士果然方便啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1C7F")

    Jump("loc_236D")

    label("loc_1C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D13")

    #C0041
    ChrTalk(
        0xFE,
        "村里来了好几个游客呢。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "米莉亚姐姐\x01",
            "在纪念庆典期间似乎\x01",
            "代替迪利克进了养蜂场……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "嗯，不管怎么说，\x01",
            "热闹一点是好事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236D")

    label("loc_1D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1E5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD0")

    #C0044
    ChrTalk(
        0xFE,
        (
            "村长的儿子迪利克好像要在\x01",
            "纪念庆典时到市里开露天店。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "为了搬运商品和器材，\x01",
            "要使用村里的卡车……\x01",
            "还说让我驾驶。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "……呀嗬！\x01",
            "俺一定要出色地完成工作哇！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E56")

    label("loc_1DD0")


    #C0047
    ChrTalk(
        0xFE,
        (
            "呵呵，在工作之外\x01",
            "还能开卡车……好期待哇！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "俺一定要\x01",
            "出色地完成工作哇！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "……啊，不好。\x01",
            "一兴奋，说话就带口音了。\x01",
            "嘿嘿……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E56")

    Jump("loc_236D")

    label("loc_1E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1F7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFD")

    #C0050
    ChrTalk(
        0xFE,
        (
            "好了，差不多也该把农作物\x01",
            "送到克洛斯贝尔市的店里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "虽然与个体户的生意变多了，\x01",
            "但克洛斯贝尔市的商场和百货店\x01",
            "也是不可忽视的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F7A")

    label("loc_1EFD")


    #C0052
    ChrTalk(
        0xFE,
        (
            "毕竟会稳定收购\x01",
            "大量农作物的，\x01",
            "还是市里的商店啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "虽然和哈罗德先生他们的生意也很重要，\x01",
            "不过主要的大客户还要算那边。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7A")

    Jump("loc_236D")

    label("loc_1F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2001")

    #C0054
    ChrTalk(
        0xFE,
        (
            "巴士的数量很少，\x01",
            "对导力车爱好者来说，\x01",
            "实在不够满足啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "虽说我们村子\x01",
            "基本都是自给自足的，\x01",
            "也不会很不方便。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236D")

    label("loc_2001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_210A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209C")

    #C0056
    ChrTalk(
        0xFE,
        (
            "导力巴士每天都会来几班，\x01",
            "但几乎没有从克洛斯贝尔市\x01",
            "过来的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "村里人乘坐巴士，\x01",
            "也只是偶尔出去买东西，\x01",
            "然后回来而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2105")

    label("loc_209C")


    #C0058
    ChrTalk(
        0xFE,
        (
            "这里虽然通了导力巴士，\x01",
            "但克洛斯贝尔市的人\x01",
            "却很少会过来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "也就是偶尔有游击士\x01",
            "接到委托才会来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2105")

    Jump("loc_236D")

    label("loc_210A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_227A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220C")

    #C0060
    ChrTalk(
        0xFE,
        (
            "出事那天早上，卡车的车身\x01",
            "满是创伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "……一想起来，\x01",
            "俺就火冒三丈哇……！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "卡车可是村里不可或缺的\x01",
            "重要之物哇！\x01",
            "竟敢把它……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "……唔，咳咳。\x01",
            "总而言之，那种爪痕……\x01",
            "一定是狼形魔兽干的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2204")
    SetScenarioFlags(0x68, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2204")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2275")

    label("loc_220C")


    #C0064
    ChrTalk(
        0xFE,
        (
            "……只要一激动，说话就会\x01",
            "露出口音呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "唉，为什么只有我会这样呢。\x01",
            "米莉亚姐姐\x01",
            "完全都没有口音……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2275")

    Jump("loc_236D")

    label("loc_227A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_236D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231D")

    #C0066
    ChrTalk(
        0xFE,
        "你们是克洛斯贝尔市的人？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "这就怪了，\x01",
            "巴士才刚刚离开……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "……什么，你们是走着过来的！？\x01",
            "唉，真是不明白市里人都在想什么啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_236D")

    label("loc_231D")


    #C0069
    ChrTalk(
        0xFE,
        "嗯？找村长有事吗？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "村长家在\x01",
            "村子最里面哦。\x01",
            "顺着路直走过去就能看见了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_236D")

    TalkEnd(0xFE)
    Return()

    # Function_12_1467 end

    def Function_13_2371(): pass

    label("Function_13_2371")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_243A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238F")
    Call(0, 14)
    Jump("loc_2435")

    label("loc_238F")

    OP_93(0xFE, 0xB4, 0x0)
    OP_4B(0xA, 0xFF)

    #C0071
    ChrTalk(
        0xFE,
        (
            "好～那就来决定\x01",
            "游击士游戏的角色吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "……我是亚里欧斯先生了！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        "我当狼魔兽～！！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xA, 500)
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0074
    ChrTalk(
        0xFE,
        "当那个没问题吗……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_2435")

    Jump("loc_2C08")

    label("loc_243A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_24C8")
    OP_4B(0xA, 0xFF)

    #C0075
    ChrTalk(
        0xFE,
        (
            "史蒂芬那家伙说，\x01",
            "今天要在『白蜡亭』休息一天呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "嗯～该不是生病了吧？\x01",
            "待会要不要去看看他呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        "要不要去呢～\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_2C08")

    label("loc_24C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_25F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259F")
    OP_93(0xFE, 0xB4, 0x0)

    #C0078
    ChrTalk(
        0xFE,
        (
            "史蒂芬，你跑得好慢啊～\x01",
            "竟然会被普莉抓住，也太慢了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "你要是真的搬来村里，\x01",
            "一定要正式进行跑步特训才行啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x109,
        (
            "#0502F呵呵……好悠闲啊。\x02\x03",

            "真希望能将这种和平\x01",
            "永远守护下去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25F2")

    label("loc_259F")


    #C0081
    ChrTalk(
        0xFE,
        (
            "嗯，先不说这些啦……\x01",
            "接下来轮到史蒂芬当鬼！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "太阳下山之前可要抓到我们哦～\x02",
    )

    CloseMessageWindow()

    label("loc_25F2")

    Jump("loc_2C08")

    label("loc_25F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_265F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2612")
    Call(0, 14)
    Jump("loc_265A")

    label("loc_2612")


    #C0083
    ChrTalk(
        0xFE,
        (
            "纪念庆典……\x01",
            "还是好想去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "算啦，下次让史蒂芬\x01",
            "讲给我就行了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_265A")

    Jump("loc_2C08")

    label("loc_265F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_26C7")

    #C0085
    ChrTalk(
        0xFE,
        (
            "是吗，纪念庆典\x01",
            "到明天就要结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "感觉真是转瞬即逝啊。\x01",
            "不能去玩，真是遗憾啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C08")

    label("loc_26C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E2")
    Call(0, 14)
    Jump("loc_2723")

    label("loc_26E2")


    #C0087
    ChrTalk(
        0xFE,
        (
            "游击士、警察和不良团伙的\x01",
            "混合大竞赛……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "呜～好想看啊！\x02",
    )

    CloseMessageWindow()

    label("loc_2723")

    Jump("loc_2C08")

    label("loc_2728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_277F")

    #C0089
    ChrTalk(
        0xFE,
        (
            "啊～虽然想去创立纪念庆典……\x01",
            "可是妈妈太忙了，不带我去。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        "嘁……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C08")

    label("loc_277F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_28C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2852")

    #C0091
    ChrTalk(
        0xFE,
        (
            "『彩虹剧团』的伊莉娅小姐\x01",
            "有个很帅气的称号。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "那就是『炎之舞姬』！\x01",
            "呼～太激动人心了！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "『风之剑圣』啊，\x01",
            "『雷鸣之勇者』啊，『大海之子』什么的……\x01",
            "我也想要这种帅气的称号啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28BE")

    label("loc_2852")


    #C0094
    ChrTalk(
        0xFE,
        (
            "『炎之舞姬』这个称号\x01",
            "真帅气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "我也想像伊莉娅小姐和亚里欧斯先生那样，\x01",
            "被人用帅气的绰号来称呼啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28BE")

    Jump("loc_2C08")

    label("loc_28C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2937")

    #C0096
    ChrTalk(
        0xFE,
        (
            "听说啊～克洛斯贝尔市那边\x01",
            "有个很厉害的剧团。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "是叫……『彩虹剧团』吧？\x01",
            "真好啊，好想去看看啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C08")

    label("loc_2937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_29CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2952")
    Call(0, 14)
    Jump("loc_29C8")

    label("loc_2952")


    #C0098
    ChrTalk(
        0xFE,
        (
            "嗯～……\x01",
            "普莉当魔兽的话，\x01",
            "好像没什么紧张感啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "要是那个叫史蒂芬的家伙\x01",
            "愿意加入我们，\x01",
            "应该就能玩各种游戏了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C8")

    Jump("loc_2C08")

    label("loc_29CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_2AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A61")

    #C0100
    ChrTalk(
        0xFE,
        (
            "唉，亚里欧斯先生什么时候再来呀。\x01",
            "他真是太帅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "之前鸡逃掉的时候，\x01",
            "他也是一下子就抓住了。\x01",
            "哎呀，真令人憧憬啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AA1")

    label("loc_2A61")


    #C0102
    ChrTalk(
        0xFE,
        (
            "嗯，我还是……\x01",
            "决定要当个像亚里欧斯先生\x01",
            "一样厉害的游击士！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA1")

    Jump("loc_2C08")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_2B83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B41")

    #C0103
    ChrTalk(
        0xFE,
        (
            "听村长说了，\x01",
            "犯人好像是\x01",
            "什么『神狼』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "什～么嘛，不用担心啦。\x01",
            "下次再敢来村里的话，我卡米尤大人\x01",
            "一定会把它们打倒的！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B7E")

    label("loc_2B41")


    #C0105
    ChrTalk(
        0xFE,
        (
            "因为我可是未来的游击士。\x01",
            "当然可以守护这个村子的和平啦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7E")

    Jump("loc_2C08")

    label("loc_2B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2C08")

    #C0106
    ChrTalk(
        0xFE,
        (
            "嘁，这个村子真是平静得让人无聊。\x01",
            "不过空气很清新，倒是还算不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "唉～唉，什么时候要是再发生一次\x01",
            "那种大骚乱就好了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C08")

    TalkEnd(0xFE)
    Return()

    # Function_13_2371 end

    def Function_14_2C0C(): pass

    label("Function_14_2C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2CB1")
    OP_93(0xF, 0x6B, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0xA, 0x13B, 0x0)
    OP_4B(0xF, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0108
    ChrTalk(
        0x9,
        "好，今天的天气也不错……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        "就来玩玩久违的游击士游戏吧！\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        "好啊～！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xF,
        "（到底是小孩子啊……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3043")

    label("loc_2CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CBF")
    Jump("loc_3043")

    label("loc_2CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CCD")
    Jump("loc_3043")

    label("loc_2CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2DED")
    OP_93(0xF, 0x56, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xA, 0x13B, 0x0)
    OP_4B(0xF, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0112
    ChrTalk(
        0x9,
        (
            "哦～史蒂芬，你回来了！\x01",
            "好早啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xF,
        (
            "嗯，是啊。\x01",
            "妈妈说『闭幕式一定会很拥挤，\x01",
            "所以要在那之前回来』……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        "哦～\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "……那么，\x01",
            "下次有空的话，要给我们\x01",
            "多讲讲纪念庆典的事哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        "多讲点、多讲点！\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xF,
        "嗯、嗯，那当然可以……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3043")

    label("loc_2DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2DFB")
    Jump("loc_3043")

    label("loc_2DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2F1C")
    OP_93(0xD, 0x56, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xA, 0x13B, 0x0)
    OP_4B(0xD, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0118
    ChrTalk(
        0x9,
        (
            "从克洛斯贝尔市\x01",
            "过来的人说……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "好像有一场游击士、警察和不良团伙的\x01",
            "混合大竞赛。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xD,
        (
            "……是真的吗？\x01",
            "哎呀呀，真是不太平啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "打架？\x01",
            "打架了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#0006F（连、连这种地方都有传闻了……）\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        "#0306F（传得还挺广呢……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3043")

    label("loc_2F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F2A")
    Jump("loc_3043")

    label("loc_2F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F38")
    Jump("loc_3043")

    label("loc_2F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2F46")
    Jump("loc_3043")

    label("loc_2F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_301E")
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0124
    ChrTalk(
        0xA,
        "嗷呜～！　我是狼～！\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "可恶的魔兽……！\x01",
            "竟敢践踏村子！\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "只要有我超ＡＡＡ级\x01",
            "的游击士卡米尤大人在，\x01",
            "就绝不容许你破坏村子的和平！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "呀哈哈！\x01",
            "嗷呜～！　嗷呜～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3043")

    label("loc_301E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_302C")
    Jump("loc_3043")

    label("loc_302C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_303A")
    Jump("loc_3043")

    label("loc_303A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3043")

    label("loc_3043")

    SetScenarioFlags(0x0, 1)
    Return()

    # Function_14_2C0C end

    def Function_15_3047(): pass

    label("Function_15_3047")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_30A4")

    #C0128
    ChrTalk(
        0xFE,
        (
            "嘿嘿，果然还是和大家\x01",
            "一起玩最开心啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "我最喜欢哥哥\x01",
            "和史蒂芬了～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3756")

    label("loc_30A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_30EB")

    #C0130
    ChrTalk(
        0xFE,
        "今天玩什么呢～\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "我还是喜欢可以\x01",
            "到处跑的游戏呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3756")

    label("loc_30EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_31F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B0")

    #C0132
    ChrTalk(
        0xFE,
        (
            "我和哥哥、史蒂芬\x01",
            "三个人在玩抓鬼游戏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "普莉跑得很快哦～\x01",
            "嘿嘿！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#0002F……这些孩子们，跟琪雅\x01",
            "应该也会很合得来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        (
            "#0304F嗯，下次带她来似乎\x01",
            "也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31EF")

    label("loc_31B0")


    #C0136
    ChrTalk(
        0xFE,
        (
            "我和哥哥、史蒂芬\x01",
            "三个人在玩抓鬼游戏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "好开心哦～！\x02",
    )

    CloseMessageWindow()

    label("loc_31EF")

    Jump("loc_3756")

    label("loc_31F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_320F")
    Call(0, 14)
    Jump("loc_326B")

    label("loc_320F")

    OP_93(0xFE, 0x13B, 0x0)
    OP_4B(0xF, 0xFF)

    #C0138
    ChrTalk(
        0xFE,
        "那个那个～礼物呢？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xF,
        (
            "啊……\x01",
            "倒也买了一些，待会给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "哇～¤\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    label("loc_326B")

    Jump("loc_3756")

    label("loc_3270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3336")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32FF")

    #C0141
    ChrTalk(
        0xFE,
        (
            "哥哥说了\x01",
            "好多次，\x01",
            "想去市里逛逛纪念庆典。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "但普莉觉得\x01",
            "现在就已经很开心了！\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "因为和哥哥\x01",
            "玩了好多游戏嘛～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3331")

    label("loc_32FF")


    #C0144
    ChrTalk(
        0xFE,
        (
            "因为和哥哥\x01",
            "玩了好多游戏，\x01",
            "所以普莉很开心哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3331")

    Jump("loc_3756")

    label("loc_3336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3351")
    Call(0, 14)
    Jump("loc_339B")

    label("loc_3351")


    #C0145
    ChrTalk(
        0xFE,
        (
            "玩是没关系，\x01",
            "但不能打架哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "要是被妈妈骂了，\x01",
            "可不关普莉的事哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_339B")

    Jump("loc_3756")

    label("loc_33A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_33EB")

    #C0147
    ChrTalk(
        0xFE,
        "村里来了不认识的人。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "既然来了，\x01",
            "能不能陪普莉玩呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3756")

    label("loc_33EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3447")

    #C0149
    ChrTalk(
        0xFE,
        (
            "虽然也很想看\x01",
            "彩虹剧团的演出……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "但普莉能和哥哥\x01",
            "一起玩，这就足够了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3756")

    label("loc_3447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_34DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A6")

    #C0151
    ChrTalk(
        0xFE,
        (
            "彩虹……剧团，\x01",
            "哦～？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "要是哥哥想去看的话，\x01",
            "我也想去看呀～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34D8")

    label("loc_34A6")


    #C0153
    ChrTalk(
        0xFE,
        (
            "彩虹剧团……\x01",
            "要是哥哥想去看的话\x01",
            "我也想去看～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D8")

    Jump("loc_3756")

    label("loc_34DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F8")
    Call(0, 14)
    Jump("loc_3540")

    label("loc_34F8")


    #C0154
    ChrTalk(
        0xFE,
        (
            "嗷呜～！\x01",
            "哥哥，嗷呜～！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "我～要～吃～了～你～！\x01",
            "……呀哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3540")

    Jump("loc_3756")

    label("loc_3545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_35DC")

    #C0156
    ChrTalk(
        0xFE,
        (
            "从前一阵子开始就\x01",
            "住在『白蜡亭』的\x01",
            "那个小哥哥……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "要是偶尔也跟我们\x01",
            "一起玩玩该多好啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "……哎，算了。\x01",
            "反正有哥哥\x01",
            "陪我玩嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3756")

    label("loc_35DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_369D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3639")

    #C0159
    ChrTalk(
        0xFE,
        (
            "嗯～……\x01",
            "狼先生做了\x01",
            "那么坏的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "普莉都不太记得了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3698")

    label("loc_3639")


    #C0161
    ChrTalk(
        0xFE,
        (
            "从前些日子开始，\x01",
            "在外面玩的时候，\x01",
            "妈妈都会在旁边守着……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "这和狼先生的出现\x01",
            "有关系吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3698")

    Jump("loc_3756")

    label("loc_369D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3722")

    #C0163
    ChrTalk(
        0xFE,
        "大哥哥，你们是谁？\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        "……警察啊？嗯～……？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        "#0006F（……这、这反应给人一种微妙的沮丧感啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3756")

    label("loc_3722")


    #C0166
    ChrTalk(
        0xFE,
        "警·察。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "……………………哦～那是什么啊？\x02",
    )

    CloseMessageWindow()

    label("loc_3756")

    TalkEnd(0xFE)
    Return()

    # Function_15_3047 end

    def Function_16_375A(): pass

    label("Function_16_375A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382C")

    #C0168
    ChrTalk(
        0xFE,
        (
            "以前我总是找理由\x01",
            "逃避挑战……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "不过我决定了！要拜托今天来这里钓鱼的\x01",
            "那位钓公师团成员，请他收我入团！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "因为我太怕生，上次连\x01",
            "钓公师团的屋子都没敢进去，\x01",
            "这次一定要……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_385D")

    label("loc_382C")


    #C0171
    ChrTalk(
        0xFE,
        (
            "为了享受垂钓人生，\x01",
            "这次一定要加入钓公师团！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385D")

    Jump("loc_40EE")

    label("loc_3862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_38CF")

    #C0172
    ChrTalk(
        0xFE,
        (
            "……那位钓公师团的人……\x01",
            "一直在那里边钓鱼\x01",
            "边发呆。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "……真好啊，\x01",
            "我也想悠闲地垂钓……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EE")

    label("loc_38CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3930")

    #C0174
    ChrTalk(
        0xFE,
        "钓公师团的人又来钓鱼了……\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "怎、怎么办，\x01",
            "这似乎是加入钓公师团的好机会……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EE")

    label("loc_3930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39D5")

    #C0176
    ChrTalk(
        0xFE,
        (
            "……结果，在纪念庆典期间，\x01",
            "我也没能走进钓公师团的大门。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "唉，没办法呢。\x01",
            "庆典期间，各处的人好像都很忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "……唉，\x01",
            "真是痛恨自己的软弱啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EE")

    label("loc_39D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A62")

    #C0179
    ChrTalk(
        0xFE,
        (
            "游客倒是来了不少……\x01",
            "不过，今天好像没看到\x01",
            "钓公师团的团员啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……是不是应该放弃被他们挖掘，\x01",
            "然后邀请入团那件事了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EE")

    label("loc_3A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AF1")

    #C0181
    ChrTalk(
        0xFE,
        (
            "那边的桥上，\x01",
            "有人在钓鱼吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "看起来，似乎是钓公师团的人……\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "……啊啊，怎么办啊！\x01",
            "要不要搭话试试呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B60")

    label("loc_3AF1")


    #C0184
    ChrTalk(
        0xFE,
        "我所憧憬的钓公师团成员如今就在那里……\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "虽然很想搭话看看……\x01",
            "呜呜，可是人家在钓鱼，会给他们添麻烦吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B60")

    Jump("loc_40EE")

    label("loc_3B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0D")

    #C0186
    ChrTalk(
        0xFE,
        (
            "……我看到这次\x01",
            "来了好多游客。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "钓公师团的人说不定也会来，\x01",
            "所以我就在这里边看鱼边等。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "你问为什么……\x01",
            "当然是在等他们招我入团了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C64")

    label("loc_3C0D")


    #C0189
    ChrTalk(
        0xFE,
        (
            "为了等待钓公师团的人招我加入，\x01",
            "我在这里装作若无其事地看鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        "……会不会来呢？\x02",
    )

    CloseMessageWindow()

    label("loc_3C64")

    Jump("loc_40EE")

    label("loc_3C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3D89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D4D")

    #C0191
    ChrTalk(
        0xFE,
        (
            "……昨天，我下定决心，\x01",
            "去了克洛斯贝尔市的\x01",
            "钓公师团分部。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "只要入了团，\x01",
            "就有整天钓鱼的快乐生活在等待我！\x01",
            "……我是这么想的。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "……但也只是站在门口看了看而已。\x01",
            "啊啊，真痛恨我这内向的性格啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D84")

    label("loc_3D4D")


    #C0194
    ChrTalk(
        0xFE,
        (
            "唉……我真是傻瓜，\x01",
            "加入钓公师团的道路真是遥远啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D84")

    Jump("loc_40EE")

    label("loc_3D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E10")

    #C0195
    ChrTalk(
        0xFE,
        (
            "我想过了，\x01",
            "光是想钓鱼\x01",
            "还是不够啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "待会我就坐巴士去\x01",
            "克洛斯贝尔市，接受\x01",
            "钓公师团分部的入团考试！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E76")

    label("loc_3E10")


    #C0197
    ChrTalk(
        0xFE,
        (
            "待会我打算去\x01",
            "克洛斯贝尔市的钓公师团分部。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "……唉～好紧张啊。\x01",
            "不知道他们会不会让我入团呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E76")

    Jump("loc_40EE")

    label("loc_3E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3EEF")

    #C0199
    ChrTalk(
        0xFE,
        "唉……好想钓鱼～\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "如果加入钓公师团，\x01",
            "他们会给我钓具吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "果然还是应该\x01",
            "想办法入团才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EE")

    label("loc_3EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_3FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5F")

    #C0202
    ChrTalk(
        0xFE,
        (
            "啊……你们\x01",
            "是从克洛斯贝尔市来的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "那边有个\x01",
            "钓公师团分部吧，\x01",
            "好憧憬啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FAB")

    label("loc_3F5F")


    #C0204
    ChrTalk(
        0xFE,
        "钓公师团……好憧憬啊。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "成员一定是整天\x01",
            "都在钓鱼度日吧。\x01",
            "好羡慕……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FAB")

    Jump("loc_40EE")

    label("loc_3FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_4035")

    #C0206
    ChrTalk(
        0xFE,
        (
            "狼形魔兽入侵的那天晚上……？\x01",
            "嗯～这个啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "唔～唔唔唔……\x01",
            "那件事都过去将近三个星期了啊。\x01",
            "抱歉，我不太记得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EE")

    label("loc_4035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_40EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_409E")

    #C0208
    ChrTalk(
        0xFE,
        (
            "清澈的水流……\x01",
            "反射着太阳光，闪闪发亮的\x01",
            "鱼身表面……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        "……真漂亮啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40EE")

    label("loc_409E")


    #C0210
    ChrTalk(
        0xFE,
        (
            "啊！！\x01",
            "刚才好像看到鱼影了！\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "……啊～我还是好想要个\x01",
            "自己专用的钓竿啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40EE")

    TalkEnd(0xFE)
    Return()

    # Function_16_375A end

    def Function_17_40F2(): pass

    label("Function_17_40F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4232")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C2")

    #C0212
    ChrTalk(
        0xFE,
        (
            "我并不打算用打破传统\x01",
            "或者破坏自然的方式\x01",
            "来发展村子。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "只是想为了让村民们过上富裕的生活\x01",
            "而做出最好的选择而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "为此，还是需要吸引人们来村里，\x01",
            "让村里热闹起来才行……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_422D")

    label("loc_41C2")


    #C0215
    ChrTalk(
        0xFE,
        (
            "我只是想为了让村民们\x01",
            "过上富裕的生活\x01",
            "而做出最好的选择而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "为什么老爸……\x01",
            "村长就不能理解我呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_422D")

    Jump("loc_4A39")

    label("loc_4232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_437B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4312")

    #C0217
    ChrTalk(
        0xFE,
        (
            "为什么克洛斯贝尔市\x01",
            "会发展得如此迅速……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "与其相比，为什么阿尔摩利卡村\x01",
            "还是和从前一样，几乎都没有任何变化，\x01",
            "一直过着朴素的生活……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "如果不看清其中的差异，\x01",
            "恐怕就很难使村子\x01",
            "有所发展吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4376")

    label("loc_4312")


    #C0220
    ChrTalk(
        0xFE,
        (
            "为什么克洛斯贝尔市\x01",
            "会发展得如此迅速……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "为了阿尔摩利卡村的发展，\x01",
            "似乎有必要搞清楚这一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4376")

    Jump("loc_4A39")

    label("loc_437B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441F")

    #C0222
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，我们通过开设露天店铺，\x01",
            "吸引了不少游客来村子里观光。\x01",
            "但庆典结束之后，却一下就没人来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "必须再想点\x01",
            "新的办法……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4463")

    label("loc_441F")


    #C0224
    ChrTalk(
        0xFE,
        (
            "身为下任村长……\x01",
            "为了让村子继续发展下去，\x01",
            "必须要想出各种办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4463")

    Jump("loc_4A39")

    label("loc_4468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4476")
    Jump("loc_4A39")

    label("loc_4476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4484")
    Jump("loc_4A39")

    label("loc_4484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4492")
    Jump("loc_4A39")

    label("loc_4492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_44A0")
    Jump("loc_4A39")

    label("loc_44A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_44AE")
    Jump("loc_4A39")

    label("loc_44AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_45EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4580")

    #C0225
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市即将\x01",
            "召开创立纪念庆典……\x01",
            "我提议去那里开设露天店铺。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "因为到时似乎会有\x01",
            "很多游客去市里呢，\x01",
            "这是向他们宣传本村的好机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "还是出售本村的特产——蜂蜜\x01",
            "比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45E6")

    label("loc_4580")


    #C0228
    ChrTalk(
        0xFE,
        (
            "在创立纪念庆典开设的露天店……\x01",
            "最好还是出售本村的\x01",
            "特产蜂蜜吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "也跟雷欧鲁先生商量看看吧……\x02",
    )

    CloseMessageWindow()

    label("loc_45E6")

    Jump("loc_4A39")

    label("loc_45EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_46F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4690")

    #C0230
    ChrTalk(
        0xFE,
        (
            "身为村长之子的我\x01",
            "在养蜂场工作\x01",
            "很奇怪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "……正因为是村长的儿子，才更要如此啊。\x01",
            "不了解支撑着村子发展的农务，\x01",
            "可是当不了村长的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_46EB")

    label("loc_4690")


    #C0232
    ChrTalk(
        0xFE,
        (
            "不了解基层的人\x01",
            "就不可能领导别人。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "我可不想当山大王，\x01",
            "而是真的想让村子\x01",
            "变得更好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46EB")

    Jump("loc_4A39")

    label("loc_46F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_4815")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C4")

    #C0234
    ChrTalk(
        0xFE,
        (
            "多亏有哈罗德先生\x01",
            "那种善良诚实的商人在，\x01",
            "村子才得以勉强维持发展。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "村里的年轻人们，\x01",
            "渐渐都会去克洛斯贝尔市发展吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "这样下去的话，\x01",
            "村子只会越来越衰落。\x01",
            "……必须想点办法啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4810")

    label("loc_47C4")


    #C0237
    ChrTalk(
        0xFE,
        (
            "为了让村子存续下去，\x01",
            "一直用以前的老方式是不行的。\x01",
            "……必须想点办法啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4810")

    Jump("loc_4A39")

    label("loc_4815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_4938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C7")

    #C0238
    ChrTalk(
        0xFE,
        (
            "村长好像说了『神狼』\x01",
            "什么的。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "……虽然他是我的父亲，\x01",
            "但是思想实在太陈腐，真是伤脑筋。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "为了让村子有所发展，\x01",
            "真希望他能采取点合适的措施。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4933")

    label("loc_48C7")


    #C0241
    ChrTalk(
        0xFE,
        (
            "众多家畜受害，\x01",
            "这是防范意识不足招致的结果。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "这个村子必须有所改变。\x01",
            "村长……我父亲的做法太陈腐了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4933")

    Jump("loc_4A39")

    label("loc_4938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4A39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49DF")
    OP_93(0xFE, 0x12A, 0x0)

    #C0243
    ChrTalk(
        0xFE,
        (
            "……再这样下去的话，这个村子\x01",
            "也撑不了多久吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0244
    ChrTalk(
        0xFE,
        "……什么事？我现在很忙。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "什么，找村长有事？\x01",
            "村长家就在那边哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A39")

    label("loc_49DF")


    #C0246
    ChrTalk(
        0xFE,
        (
            "你们找村长有事吧？\x01",
            "村长家就在那边。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "虽然现在有客人……\x01",
            "不过事情应该快谈完了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A39")

    TalkEnd(0xFE)
    Return()

    # Function_17_40F2 end

    def Function_18_4A3D(): pass

    label("Function_18_4A3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A4E")
    Jump("loc_4FA3")

    label("loc_4A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4B5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B28")
    OP_93(0xD, 0x56, 0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0248
    ChrTalk(
        0xFE,
        (
            "为了今天的点心时间，\x01",
            "我烤了苹果派……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "嗯～史蒂芬要是不来的话，\x01",
            "这个就先不吃了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4AD1():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4AD1)

    def lambda_4ADE():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4ADE)
    WaitChrThread(0xA, 1)

    #C0250
    ChrTalk(
        0x9,
        "不是吧！？\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xA,
        "不要～！！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    SetScenarioFlags(0x0, 5)
    Jump("loc_4B55")

    label("loc_4B28")


    #C0252
    ChrTalk(
        0xFE,
        (
            "史蒂芬要是不来，\x01",
            "点心就先留起来不吃吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B55")

    Jump("loc_4FA3")

    label("loc_4B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4B68")
    Jump("loc_4FA3")

    label("loc_4B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4B76")
    Jump("loc_4FA3")

    label("loc_4B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4B84")
    Jump("loc_4FA3")

    label("loc_4B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B9F")
    Call(0, 14)
    Jump("loc_4BBB")

    label("loc_4B9F")


    #C0253
    ChrTalk(
        0xFE,
        "哎呀呀，城市真危险啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4BBB")

    Jump("loc_4FA3")

    label("loc_4BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4BCE")
    Jump("loc_4FA3")

    label("loc_4BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4BDC")
    Jump("loc_4FA3")

    label("loc_4BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4BEA")
    Jump("loc_4FA3")

    label("loc_4BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4CDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C8C")

    #C0254
    ChrTalk(
        0xFE,
        (
            "哎呀呀，玩游击士游戏时，\x01",
            "居然让妹妹当魔兽。\x01",
            "我儿子还真是以自我为中心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "……不过，普莉本人似乎也很开心，\x01",
            "还是不要在意好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4CD5")

    label("loc_4C8C")

    OP_93(0xD, 0x56, 0x0)

    #C0256
    ChrTalk(
        0xFE,
        "喂，卡米尤！\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "你可是哥哥呀，\x01",
            "之后也要让普莉\x01",
            "当游击士哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD5")

    Jump("loc_4FA3")

    label("loc_4CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_4DD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D65")
    OP_93(0xD, 0x56, 0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0258
    ChrTalk(
        0xD,
        (
            "卡米尤、普莉！\x01",
            "该回家啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x9,
        "我们还要玩～！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xA,
        "还要玩～！\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xD,
        "……唉，真是的。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_4DCE")

    label("loc_4D65")


    #C0262
    ChrTalk(
        0xFE,
        (
            "小孩子啊，总是要玩到\x01",
            "精疲力尽才肯罢休呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "不过，玩累了以后，\x01",
            "胃口也会大开，\x01",
            "倒是有利于健康啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DCE")

    Jump("loc_4FA3")

    label("loc_4DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_4F2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAB")

    #C0264
    ChrTalk(
        0xFE,
        (
            "我丈夫在村子外边的\x01",
            "田地里干农活。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        "现在回家来吃午饭了。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "……之前还发生了魔兽灾害，\x01",
            "真希望他不要\x01",
            "走太远呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "自那以来，我一直很担心。\x01",
            "所以随时留意，\x01",
            "绝不让孩子们离开视线。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4F25")

    label("loc_4EAB")


    #C0268
    ChrTalk(
        0xFE,
        (
            "之前还发生了魔兽灾害，\x01",
            "希望丈夫也不要\x01",
            "走太远啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "从那以来，我一直很担心。\x01",
            "所以随时留意，\x01",
            "绝不让孩子们离开视线。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F25")

    Jump("loc_4FA3")

    label("loc_4F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4FA3")

    #C0270
    ChrTalk(
        0xFE,
        (
            "这两个小孩是我的孩子。\x01",
            "呵呵，很可爱吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "最近刚出了那种事，\x01",
            "让他们在外面玩的话，\x01",
            "实在是有点担心……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4FA3")

    TalkEnd(0xFE)
    Return()

    # Function_18_4A3D end

    def Function_19_4FA7(): pass

    label("Function_19_4FA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FB8")
    Jump("loc_51F7")

    label("loc_4FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4FC6")
    Jump("loc_51F7")

    label("loc_4FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4FD4")
    Jump("loc_51F7")

    label("loc_4FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_503E")

    #C0272
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "迪利克也快回来了，管理养蜂场的工作\x01",
            "也就到今天为止了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        "呼～真是不容易啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_51F7")

    label("loc_503E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_50BC")

    #C0274
    ChrTalk(
        0xFE,
        (
            "有人来村里是不错……\x01",
            "不过还是有些在意那些视线呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "虽然理解他们的好奇心情……\x01",
            "但做事时会觉得不自在呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51F7")

    label("loc_50BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_512E")

    #C0276
    ChrTalk(
        0xFE,
        (
            "话说，我们村里\x01",
            "也来了不少游客呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "他们喜欢这里，我是很开心……\x01",
            "但希望不要打扰我干农活啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51F7")

    label("loc_512E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_51A8")

    #C0278
    ChrTalk(
        0xFE,
        (
            "迪利克亲自去\x01",
            "经营露天店铺了。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "所以在纪念庆典期间，\x01",
            "养蜂场就交给我来管。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        "嗯，马上开始干活吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_51F7")

    label("loc_51A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_51B6")
    Jump("loc_51F7")

    label("loc_51B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_51C4")
    Jump("loc_51F7")

    label("loc_51C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_51D2")
    Jump("loc_51F7")

    label("loc_51D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_51E0")
    Jump("loc_51F7")

    label("loc_51E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_51EE")
    Jump("loc_51F7")

    label("loc_51EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_51F7")

    label("loc_51F7")

    TalkEnd(0xFE)
    Return()

    # Function_19_4FA7 end

    def Function_20_51FB(): pass

    label("Function_20_51FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_52C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5269")

    #C0281
    ChrTalk(
        0xFE,
        (
            "……果然，\x01",
            "这个村子的生活也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "要不要跟妈妈说，\x01",
            "搬过来也行呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_52C3")

    label("loc_5269")


    #C0283
    ChrTalk(
        0xFE,
        (
            "虽然同龄的孩子都很幼稚，\x01",
            "这里又是个土里土气的乡下地方……\x01",
            "但村里的生活倒也不算坏呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52C3")

    Jump("loc_5420")

    label("loc_52C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_52D6")
    Jump("loc_5420")

    label("loc_52D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5349")

    #C0284
    ChrTalk(
        0xFE,
        (
            "呼、呼……\x01",
            "没想到跟女孩子\x01",
            "赛跑还会输……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "看来，只要在这边生活，\x01",
            "就会自然而然得到锻炼呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5420")

    label("loc_5349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_53A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5364")
    Call(0, 14)
    Jump("loc_53A2")

    label("loc_5364")


    #C0286
    ChrTalk(
        0xFE,
        (
            "（这些家伙\x01",
            "  好像也不是坏孩子呢，\x01",
            "  经常邀请我去玩……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53A2")

    Jump("loc_5420")

    label("loc_53A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_53B5")
    Jump("loc_5420")

    label("loc_53B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_53C3")
    Jump("loc_5420")

    label("loc_53C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_53D1")
    Jump("loc_5420")

    label("loc_53D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_53DF")
    Jump("loc_5420")

    label("loc_53DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_53ED")
    Jump("loc_5420")

    label("loc_53ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_53FB")
    Jump("loc_5420")

    label("loc_53FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_5409")
    Jump("loc_5420")

    label("loc_5409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_5417")
    Jump("loc_5420")

    label("loc_5417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5420")

    label("loc_5420")

    TalkEnd(0xFE)
    Return()

    # Function_20_51FB end

    def Function_21_5424(): pass

    label("Function_21_5424")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5486")

    #C0287
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村\x01",
            "是个悠闲的地方，真不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "用白天钓上来的鲤鱼\x01",
            "慰劳自己一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5486")

    TalkEnd(0xFE)
    Return()

    # Function_21_5424 end

    def Function_22_548A(): pass

    label("Function_22_548A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_54FD")

    #C0289
    ChrTalk(
        0xFE,
        (
            "原来如此，这村子的\x01",
            "气候似乎不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "生长在这条小河里的\x01",
            "鲤鱼一定很美味吧，\x01",
            "我现在就很期待了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54FD")

    TalkEnd(0xFE)
    Return()

    # Function_22_548A end

    def Function_23_5501(): pass

    label("Function_23_5501")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5595")
    Jump("loc_55DF")

    label("loc_5595")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55B5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55DF")

    label("loc_55B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55D5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55DF")

    label("loc_55D5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55DF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_571A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5694")

    #C0291
    ChrTalk(
        0xFE,
        (
            "有传闻说，在阿尔摩利卡古道\x01",
            "和玛因兹那边的某处\x01",
            "栖息着梦幻之鱼的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "嗯，要是有兴趣的话，\x01",
            "不如去看看如何～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5715")

    label("loc_5694")


    #C0293
    ChrTalk(
        0xFE,
        (
            "有传闻说，在阿尔摩利卡古道\x01",
            "和玛因兹那边的某处\x01",
            "栖息着梦幻之鱼的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "不过，没有『熬炼丸子ＤＸ』的话，\x01",
            "是不可能钓到的吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5715")

    Jump("loc_5A15")

    label("loc_571A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_575C")

    #C0295
    ChrTalk(
        0xFE,
        "………（发呆～）…………\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        "有蝴蝶在飞的说～\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A15")

    label("loc_575C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_57E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57BD")

    #C0297
    ChrTalk(
        0xFE,
        (
            "特级钓师罗伊德先生\x01",
            "回利贝尔去了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "嘁～又要变得\x01",
            "无聊了啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_57DB")

    label("loc_57BD")


    #C0299
    ChrTalk(
        0xFE,
        "………（发呆～）…………\x02",
    )

    CloseMessageWindow()

    label("loc_57DB")

    Jump("loc_5A15")

    label("loc_57E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_58C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_586B")

    #C0300
    ChrTalk(
        0x12,
        "啊～天气真好的说～……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x12,
        (
            "不过，再钓一会\x01",
            "就得回市里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x12,
        (
            "因为我和分部长约好在傍晚之后\x01",
            "一起去夜钓呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_58BF")

    label("loc_586B")


    #C0303
    ChrTalk(
        0x12,
        (
            "顺带一提，分部长\x01",
            "这个人有点奇怪的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x12,
        (
            "分部就在东街，\x01",
            "你们可以去见他一面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58BF")

    Jump("loc_5A15")

    label("loc_58C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_5A15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F8")
    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F3")
    SetScenarioFlags(0x68, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58F3")

    Jump("loc_5A15")

    label("loc_58F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59BB")

    #C0305
    ChrTalk(
        0x12,
        (
            "阿尔摩利卡村附近\x01",
            "有很多钓鱼点，\x01",
            "我经常来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x12,
        "这里还有间酒馆，也很方便的说。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        "#0000F哈哈，您是这里的常客吧。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x12,
        (
            "是这种感觉的说。\x01",
            "这个村子很安逸，能令人心情放松～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5A15")

    label("loc_59BB")


    #C0309
    ChrTalk(
        0x12,
        (
            "对了对了，东街\x01",
            "有钓公师团分部的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x12,
        (
            "嗯，要是你们有机会去东街的话，\x01",
            "可以去看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A15")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_5501 end

    def Function_24_5A1D(): pass

    label("Function_24_5A1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AB3")

    #C0311
    ChrTalk(
        0xFE,
        (
            "因为已经欣赏过首要目标\x01",
            "——『彩虹剧团』的演出了，\x01",
            "就到这个村里来看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "在纪念庆典结束之前，\x01",
            "就在这个村子里悠闲度过吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5B07")

    label("loc_5AB3")


    #C0313
    ChrTalk(
        0xFE,
        (
            "『彩虹剧团』的演出也看完了……\x01",
            "在纪念庆典结束之前，\x01",
            "就在这个村子里悠闲度过吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B07")

    TalkEnd(0xFE)
    Return()

    # Function_24_5A1D end

    def Function_25_5B0B(): pass

    label("Function_25_5B0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B85")

    #C0314
    ChrTalk(
        0xFE,
        "嘿……这里真是宁静闲适啊。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "看过克洛斯贝尔市拥挤的人群之后，\x01",
            "真想不到这里也同处于自治州啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5BE3")

    label("loc_5B85")


    #C0316
    ChrTalk(
        0xFE,
        (
            "风景也优美……\x01",
            "跟着他过来，似乎是个正确的选择呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "那边有酒馆呢，\x01",
            "赶快去订个房间吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BE3")

    TalkEnd(0xFE)
    Return()

    # Function_25_5B0B end

    def Function_26_5BE7(): pass

    label("Function_26_5BE7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CB9")

    #C0318
    ChrTalk(
        0xFE,
        (
            "虽说同样属于自治州的范围之内，\x01",
            "但这里的文化氛围和城市简直是截然不同啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "我本还以为，一定会使用各种导力器\x01",
            "来进行高科技农业生产呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "不过，我觉得保留一些\x01",
            "从前的旧事物也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_5D35")

    label("loc_5CB9")


    #C0321
    ChrTalk(
        0xFE,
        (
            "我觉得保留一些从前的\x01",
            "旧事物也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "要是连这个村子也变得和克洛斯贝尔市\x01",
            "一样的话，也许反而会让人觉得精神疲劳吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D35")

    TalkEnd(0xFE)
    Return()

    # Function_26_5BE7 end

    def Function_27_5D39(): pass

    label("Function_27_5D39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DC2")

    #C0323
    ChrTalk(
        0xFE,
        (
            "小河流水，小鸟鸣唱，\x01",
            "美丽的自然风光……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "要是在这里吃便当，\x01",
            "一定会觉得很美味吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        "……肚子好像饿了呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_5E37")

    label("loc_5DC2")


    #C0326
    ChrTalk(
        0xFE,
        (
            "要是在这里吃便当，\x01",
            "一定会觉得很美味吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "在雪白的饭团上撒上盐……\x01",
            "啊啊，光是想象一下，\x01",
            "就忍不住要流口水了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E37")

    TalkEnd(0xFE)
    Return()

    # Function_27_5D39 end

    def Function_28_5E3B(): pass

    label("Function_28_5E3B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1250, 1750, 6100, 0)
    MoveCamera(316, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, -2000, 500, 6000, 90)
    SetChrPos(0x102, -2200, 400, 7250, 135)
    SetChrPos(0x103, -1800, 410, 4760, 45)
    SetChrPos(0x104, -3000, 450, 5750, 90)
    SetChrSubChip(0x12, 0x0)
    OP_0D()

    #C0328
    ChrTalk(
        0x12,
        (
            "………（发呆～）…………\x01",
            "天气真好的说～……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetChrSubChip(0x12, 0x2)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x12, 0xF)
    SetChrSubChip(0x12, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_93(0x12, 0x10E, 0x1F4)

    #C0329
    ChrTalk(
        0x12,
        (
            "啊，你们好。\x01",
            "各位也是来钓鱼的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        (
            "#0005F啊，不……我们是\x01",
            "克洛斯贝尔警察局的人。\x02\x03",

            "#0001F正在打听关于三周前\x01",
            "那起魔兽骚乱的情报。\x02\x03",

            "您似乎不是\x01",
            "阿尔摩利卡村的人，\x01",
            "不过，有什么线索吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x12,
        "啊～那件事啊。\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x12,
        (
            "没记错的话，当时我\x01",
            "正在尝试钓起暗纹蛇鱼，\x01",
            "所以没有来过村里的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x12,
        (
            "传闻什么的，\x01",
            "后来倒是听人说了一些～\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        (
            "#0103F是这样吗……\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x12,
        "……没能帮上忙，很抱歉的说。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x12,
        (
            "话说回来，竟然\x01",
            "还要跑到这种乡下地方来工作，\x01",
            "警察也真辛苦的说～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0337
    ChrTalk(
        0x12,
        (
            "……对了，各位，\x01",
            "你们钓不钓鱼呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x12,
        (
            "难得天气这么好，\x01",
            "不放松一下可就亏了的说。\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x12, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0339
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('咪雪缎带', 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x18B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('虹丸ＥＸ', 10)
    AddItemNumber('熬炼丸子', 10)

    #C0341
    ChrTalk(
        0x12,
        (
            "啊，对了，\x01",
            "把这个也给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('钓鱼手册', 10)
    OP_98(0x12, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)

    #C0343
    ChrTalk(
        0x12,
        (
            "这本手册可是\x01",
            "垂钓者之友的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x12,
        (
            "钓到的鱼，还有其具体信息，\x01",
            "都可以记录上去。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#0005F这、这样好吗？\x01",
            "收您这么多东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x12,
        "不必介意的说。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x12,
        (
            "我所属的『钓公师团』\x01",
            "姑且算是普及垂钓文化的\x01",
            "组织吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x12,
        (
            "碰到可能对垂钓有兴趣的人\x01",
            "就赠送一套钓具，\x01",
            "这是我们的习惯。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_63FA")

    #C0349
    ChrTalk(
        0x101,
        (
            "#0003F（之前倒也进去看过……\x01",
            "　原来是从事这种活动\x01",
            "　的组织啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6420")

    label("loc_63FA")


    #C0350
    ChrTalk(
        0x101,
        "#0003F（竟然还有这种组织吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_6420")


    #C0351
    ChrTalk(
        0x104,
        (
            "#0300F嗯，这不是挺好吗？\x01",
            "在工作的间隙\x01",
            "似乎还能放松一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        (
            "#0200F是呀，在那期间\x01",
            "也能让身体得到休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x102,
        "#0100F休息也是很有必要的呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_653F")

    #C0354
    ChrTalk(
        0x101,
        (
            "#0011F缇欧、艾莉，\x01",
            "你们还觉得累啊。\x02\x03",

            "#0000F……嗯，那我们\x01",
            "就不客气地收下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x12,
        (
            "好的，\x01",
            "请加油。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_681E")

    label("loc_653F")


    #C0356
    ChrTalk(
        0x101,
        (
            "#0006F缇欧，艾莉，\x01",
            "你们还觉得累啊。\x02\x03",

            "#0008F（不过，说起垂钓……\x01",
            "  自从当年大哥教过我之后，一直都没自己试过呢。）\x02\x03",

            "#0003F（大哥当上警察以后，\x01",
            "  也完全没时间带我钓鱼了……\x01",
            "  趁此机会，再来试试吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x12,
        (
            "如果要钓鱼的话，\x01",
            "阿尔摩利卡村里\x01",
            "也有不错的钓鱼点。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9520, 1750, -180, 5000)
    MoveCamera(329, 23, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(18580, 5000)
    OP_93(0x12, 0x5A, 0x12C)
    OP_6F(0x79)

    #C0358
    ChrTalk(
        0x12,
        (
            "就在那边的栈桥附近的说。\x01",
            "今天似乎也有很多鱼聚集呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#0000F栈桥附近是吧。\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※水面上扩张的波纹就代表\x01",
            "  那处是可以钓鱼的『钓鱼点』。\x02\x03",

            "※调查钓鱼点，\x01",
            "  并选择所持有的『钓竿』和『鱼饵』，\x01",
            "  罗伊德就会开始钓鱼。\x02\x03",

            "※当 ！标志出现时，迅速按下○键，  \x01",
            "  就能钓到鱼了。\x01",
            "  （运气不好时，鱼也可能会逃掉。）\x02\x03",

            "※钓到的鱼，及其具体信息会被记录在『钓鱼手册』上，\x01",
            "  随时都可以阅览。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_681E")

    SetChrPos(0x0, -2000, 500, 6000, 90)
    OP_93(0x12, 0x5A, 0x0)
    SetChrChipByIndex(0x12, 0xE)
    SetChrSubChip(0x12, 0x0)
    SetScenarioFlags(0x69, 1)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_28_5E3B end

    def Function_29_6848(): pass

    label("Function_29_6848")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0361
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
    )

    CloseMessageWindow()
    OP_68(11620, 1500, 1410, 1500)
    MoveCamera(328, 26, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(16250, 1500)
    Sleep(1000)
    SetChrName("")

    #A0362
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_690B")
    OP_E0(0x2)
    MiniGame(0x6, 0x17, 0x300C, 0x0, 0x1478, 0xB4, 0x2A8A, 0xFFFFFA56, 0x4BA)

    label("loc_690B")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_29_6848 end

    def Function_30_6910(): pass

    label("Function_30_6910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6926")
    Call(0, 38)
    Jump("loc_6999")

    label("loc_6926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6937")
    Call(0, 6)
    Jump("loc_6999")

    label("loc_6937")

    TalkBegin(0xFF)
    SetChrName("")

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0364
    ChrTalk(
        0x101,
        (
            "#0003F难得来到这里，\x01",
            "先调查了有关魔兽的情报再回去吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_6999")

    Return()

    # Function_30_6910 end

    def Function_31_699A(): pass

    label("Function_31_699A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_68(16300, 1500, -24840, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15300, 0)
    OP_68(15110, 1350, -23260, 2500)
    SetChrPos(0x101, 17180, 0, -23450, 315)
    SetChrPos(0x102, 18600, 0, -25290, 315)
    SetChrPos(0x103, 17790, 0, -26560, 315)
    SetChrPos(0x104, 16230, 0, -24520, 315)

    def lambda_6A38():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A38)

    def lambda_6A52():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A52)

    def lambda_6A6C():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A6C)

    def lambda_6A86():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A86)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Sleep(300)

    #C0365
    ChrTalk(
        0x101,
        (
            "#11P#0002F呼……\x01",
            "这里就是阿尔摩利卡村吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6AEE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AEE)

    def lambda_6AFB():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6AFB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    #C0366
    ChrTalk(
        0x101,
        "#0000F#5P艾莉、缇欧，你们还好吧？\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x102,
        (
            "#0102F#12P嗯……\x01",
            "刚才已经休息过了嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    #C0368
    ChrTalk(
        0x103,
        (
            "#0206F#6P……我也还好。\x02\x03",

            "#0202F话说回来……\x01",
            "……这村子好美呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_E5()
    OP_24(0x7B)
    OP_68(15110, 2350, -23260, 2500)

    def lambda_6BC5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BC5)

    def lambda_6BD2():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BD2)
    Sleep(100)

    def lambda_6BE2():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6BE2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Sleep(1000)
    Fade(1000)
    OP_68(-37350, 1500, 69780, 0)
    MoveCamera(338, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(53190, 0)
    OP_68(-21000, 1500, 74410, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(7400, 1500, 48380, 0)
    MoveCamera(323, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(37470, 0)
    OP_68(-12130, 1500, 35080, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(-1020, 5100, 4110, 0)
    MoveCamera(338, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44250, 0)
    PlaceName2(340, 40, "c_plac14", 0x0, 3000)
    OP_68(-1020, 2800, 4110, 7000)
    OP_6F(0x1)
    Fade(1000)
    OP_68(15110, 1350, -23260, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    OP_E6()

    #C0369
    ChrTalk(
        0x102,
        (
            "#0109F#12P鲜花盛开的田园风光……\x01",
            "这里竟然是如此漂亮的地方啊。\x02\x03",

            "#0105F而且……\x01",
            "好像还有种甘甜的芳香……\x02\x03",

            "#0102F莫非是……蜂蜜的香味？\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        (
            "#0300F#6P应该是的，\x01",
            "对面还有蜂箱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        (
            "#0202F#6P根据数据库显示，\x01",
            "阿尔摩利卡村的蜂蜜\x01",
            "似乎是其特产之一呢。\x02\x03",

            "因为品质极好，\x01",
            "所以也会出口到周边国家。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#0004F#6P嗯，似乎是这样呢。\x02\x03",

            "#0000F杂货店也经常有卖，\x01",
            "原来是在这种地方生产的吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x102,
        (
            "#0103F#12P……是呀……\x02\x03",

            "#0108F……书本知识和实际了解，\x01",
            "原来有这么大差距啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_6F36():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F36)
    Sleep(50)

    def lambda_6F46():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F46)
    Sleep(50)

    def lambda_6F56():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6F56)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0374
    ChrTalk(
        0x101,
        "#0005F#5P艾莉……？\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        "#0104F#12P……不，没什么。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0376
    ChrTalk(
        0x102,
        (
            "#0101F#12P话说回来……\x01",
            "就是这个和平的村子\x01",
            "遭到了魔兽的破坏呢。\x02\x03",

            "真有点难以置信……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x104,
        (
            "#0306F#5P算是吧～不过这村子看上去\x01",
            "就很悠闲，对危险没什么防备呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_704C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_704C)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0378
    ChrTalk(
        0x103,
        (
            "#6P#0200F根据警备队的调查书……\x02\x03",

            "他们似乎曾向这个村子的村长\x01",
            "询问过案件情况。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70B2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70B2)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0379
    ChrTalk(
        0x101,
        (
            "#0000F#5P嗯，我们也先去\x01",
            "听听村长先生怎么说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        (
            "#0100F#12P村长先生的家……\x01",
            "到底在哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15500, 0, -23930, 315)
    SetScenarioFlags(0x60, 4)
    OP_29(0x3F, 0x1, 0x2)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E1(0x1B26, 0x1F4, 0x143C)
    OP_E1(0x7936, 0x1F4, 0xFFFFFD6C)
    ClearScenarioFlags(0x1, 3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_699A end

    def Function_32_7195(): pass

    label("Function_32_7195")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2170, 4650, 55620, 0)
    MoveCamera(326, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21430, 0)
    SetChrPos(0x101, -2170, 3760, 56260, 180)
    SetChrPos(0x102, -2170, 3760, 56260, 180)
    SetChrPos(0x103, -2170, 3760, 56260, 180)
    SetChrPos(0x104, -2170, 3760, 56260, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    Sleep(500)
    OP_68(-2170, 4650, 51620, 6000)
    BeginChrThread(0x101, 3, 0, 33)
    Sleep(900)
    BeginChrThread(0x102, 3, 0, 34)
    Sleep(900)
    BeginChrThread(0x103, 3, 0, 35)
    Sleep(900)
    BeginChrThread(0x104, 3, 0, 36)
    Sleep(500)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0381
    ChrTalk(
        0x104,
        (
            "#11P#0303F『神狼』吗……\x02\x03",

            "#0300F突然听到了\x01",
            "有趣的故事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#6P#0003F是啊……\x02\x03",

            "#0001F『神狼』是否真的存在，\x01",
            "目前还不清楚……\x02\x03",

            "不过，也许可以将它们\x01",
            "列入嫌犯候补吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0383
    ChrTalk(
        0x102,
        (
            "#5P#0102F呵呵……这话真有你的风格呢。\x02\x03",

            "#0103F的确，既然留下了足迹，\x01",
            "狼形魔兽应该是真实存在的。\x02\x03",

            "#0101F但除此之外，它们又没有留下任何痕迹，\x01",
            "就消失得无影无踪……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0384
    ChrTalk(
        0x103,
        (
            "#2P#0203F很奇怪呢……\x02\x03",

            "#0200F既然在村里留下了足迹，\x01",
            "应该可以顺着足迹追寻到它们的去向才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#6P#0001F的确，这也是一个疑点。\x02\x03",

            "#0008F竟然能甩脱\x01",
            "警备队的追踪调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        (
            "#11P#0306F话说，要是它们钻进了险峻的小道，\x01",
            "人类也就无计可施了啊。\x02\x03",

            "#0300F现在想太深\x01",
            "也无济于事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        (
            "#6P#0003F……是啊。\x02\x03",

            "#0000F好，那么就\x01",
            "马上开始探听情报吧。\x02\x03",

            "而且，已经中午了……\x01",
            "顺便也吃个午饭吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x102,
        (
            "#5P#0104F呵呵，是呀。\x02\x03",

            "#0100F走了这么远的路，\x01",
            "肚子都饿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x103,
        "#2P#0202F……我也是。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x104,
        (
            "#11P#0302F那么，就一边探听情报，\x01",
            "一边往酒馆走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2100, 3500, 51200, 180)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x60, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_7195 end

    def Function_33_7668(): pass

    label("Function_33_7668")


    def lambda_766D():
        OP_95(0xFE, -2280, 3500, 51520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_766D)

    def lambda_7687():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7687)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    def lambda_76A0():
        OP_95(0xFE, -2230, 3500, 50390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76A0)
    WaitChrThread(0x101, 1)

    def lambda_76BE():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76BE)
    WaitChrThread(0x101, 1)
    Return()

    # Function_33_7668 end

    def Function_34_76CB(): pass

    label("Function_34_76CB")


    def lambda_76D0():
        OP_95(0xFE, -2350, 3500, 52640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76D0)

    def lambda_76EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_76EA)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)

    def lambda_7703():
        OP_95(0xFE, -3520, 3500, 51770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7703)
    WaitChrThread(0x102, 1)

    def lambda_7721():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7721)
    WaitChrThread(0x102, 1)
    Return()

    # Function_34_76CB end

    def Function_35_772E(): pass

    label("Function_35_772E")


    def lambda_7733():
        OP_95(0xFE, -2340, 3500, 53740, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7733)

    def lambda_774D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_774D)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)

    def lambda_7766():
        OP_95(0xFE, -940, 3500, 51820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7766)
    WaitChrThread(0x103, 1)

    def lambda_7784():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7784)
    WaitChrThread(0x103, 1)
    Return()

    # Function_35_772E end

    def Function_36_7791(): pass

    label("Function_36_7791")


    def lambda_7796():
        OP_95(0xFE, -2430, 3500, 54990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7796)

    def lambda_77B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_77B0)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)

    def lambda_77C9():
        OP_95(0xFE, -2260, 3500, 53110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_77C9)
    WaitChrThread(0x104, 1)
    Return()

    # Function_36_7791 end

    def Function_37_77E3(): pass

    label("Function_37_77E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1760, 750, 20490, 0)
    MoveCamera(332, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18850, 0)
    SetChrPos(0x101, -1500, 0, 19000, 0)
    SetChrPos(0x102, -1500, 0, 21000, 180)
    SetChrPos(0x103, -500, 0, 20000, 270)
    SetChrPos(0x104, -2500, 0, 20000, 90)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    SetCameraDistance(17850, 2000)
    OP_6F(0x10)
    OP_0D()

    #C0391
    ChrTalk(
        0x103,
        (
            "#12P#0200F……这样就算是\x01",
            "基本探听完了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        "#6P#0000F嗯，差不多了吧。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x104,
        (
            "#5P#0306F不过与预期的有所偏差，\x01",
            "都没打听到什么有用的情报啊。\x02\x03",

            "#0301F没有目击情报也就算了，\x01",
            "但我本以为至少也该有人\x01",
            "听到过狼的远吠呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x102,
        "#11P#0103F是啊……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#6P#0006F……嗯～\x02\x03",

            "#0000F也罢，总而言之，\x01",
            "在这个村子里能做的调查已经到此结束了。\x02\x03",

            "接下来是医科大学……\x01",
            "先回市里一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#11P#0100F嗯，明白了。\x02\x03",

            "#0106F回去的话，\x01",
            "无论如何也不想再走路了……\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x103,
        (
            "#12P#0206F同感……\x01",
            "实在太累人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x104,
        "#5P#0302F哈哈，没办法啦。\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        (
            "#6P#0012F那么，就去巴士站\x01",
            "查查下一班车的发车时间吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -1500, 0, 20000, 135)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x9, 1570, 0, 22510, 135)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x61, 0)
    OP_29(0x3F, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_37_77E3 end

    def Function_38_7B40(): pass

    label("Function_38_7B40")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch09300.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00254.itc", 0x20)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(770, 1400, -15710, 0)
    MoveCamera(290, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -1460, 0, -15390, 315)
    SetChrPos(0x102, -40, 0, -16470, 315)
    SetChrPos(0x103, 1890, 0, -16120, 270)
    SetChrPos(0x104, 300, 0, -14900, 270)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 0, 0, -5910, 180)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03600.itp")
    FadeToBright(1000, 0)
    OP_0D()

    #C0400
    ChrTalk(
        0x101,
        "#0000F#5P下一班车到达的时间是……三十分钟后啊。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x104,
        (
            "#0306F#12P又是个说长不长，说短不短的时间啊。\x02\x03",

            "#0301F干等着太无聊，回酒馆喝一杯的话，\x01",
            "时间好像又有些紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#0106F#6P先不说时间问题，在工作中\x01",
            "随便饮酒本身就很不合适吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 39)

    #C0403
    ChrTalk(
        0x103,
        "#0200F#11P？？\x02",
    )

    CloseMessageWindow()

    def lambda_7D84():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D84)
    Sleep(50)

    def lambda_7D94():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D94)
    Sleep(50)

    def lambda_7DA4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7DA4)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0404
    ChrTalk(
        0x101,
        "#0005F#5P缇欧……？\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x102,
        "#0105F怎么了吗？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    #C0406
    ChrTalk(
        0x103,
        (
            "#0208F#11P没什么……\x01",
            "只是感觉好像从远方传来了什么声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x104,
        "#0301F唔……？\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x103,
        (
            "#0203F#11P……对不起，\x01",
            "我将传感器调到最大试试。\x02\x03",

            "#0200F请稍微安静一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        "#0005F#5P啊，好的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    VolumeBGM(0x3C, 0x3E8)
    Sound(1278, 255, 90, 0)    #voice#Tio
    OP_68(1340, 1400, -15920, 2000)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    BeginChrThread(0x1A, 1, 0, 40)
    Sound(820, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    TurnDirection(0x103, 0x101, 300)
    Sleep(500)

    #C0410
    ChrTalk(
        0x103,
        (
            "#0203F#6P……对不起，\x01",
            "好像只是我的错觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        (
            "#0001F#5P不……\x01",
            "这倒是没关系。\x02\x03",

            "但你最开始听到的\x01",
            "到底是怎样的声音？\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        (
            "#0208F#6P那是……\x02\x03",

            "#0201F……我感觉好像是有什么东西\x01",
            "在远处吠叫。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0413
    ChrTalk(
        0x104,
        "#0301F#2P那是……\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        "#0101F#1P是那些狼形魔兽……？\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x103,
        (
            "#0206F#6P不……说不定\x01",
            "只是我听错了。\x02\x03",

            "也有可能是\x01",
            "传感器运作有误……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(300)

    #C0416
    ChrTalk(
        0x102,
        (
            "#0101F#6P……怎么办？\x01",
            "要在这附近搜索看看吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        (
            "#0003F#5P说得也是啊……\x02\x03",

            "#0001F缇欧，那个传感器的\x01",
            "感知范围大概有多大？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8284():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8284)
    Sleep(300)

    #C0418
    ChrTalk(
        0x103,
        (
            "#0203F#6P这个嘛……\x02\x03",

            "#0200F大约有５０赛尔矩\x01",
            "左右吧。\x02\x03",

            "只是，在声音顺风的情况下，\x01",
            "范围有时也可能会倍增。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x104,
        (
            "#0305F#2P哦哦～！\x01",
            "有那么远啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        (
            "#0108F#1P这样的话，就实在无法断定\x01",
            "声音是从何处传来的了……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        (
            "#0006F#5P嗯……目前\x01",
            "也只能先留意一下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0422
    ChrTalk(
        0x103,
        (
            "#0208F#6P……那个。\x02\x03",

            "你们难道不认为\x01",
            "是我听错了吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0423
    ChrTalk(
        0x101,
        "#0005F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x102,
        "#0105F#1P但是，你确实听到了吧？\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x103,
        (
            "#0203F#6P以我的主观判断来说……的确是的。\x02\x03",

            "#0208F可是，只有我听到了\x01",
            "普通人听不到的声音……\x02\x03",

            "#0201F通常情况下，不是应该觉得我在说谎，\x01",
            "或者产生了错觉之类的才对吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x104)
    OP_64(0x102)

    #C0426
    ChrTalk(
        0x104,
        (
            "#0306F#2P……话是这么说啦。\x02\x03",

            "#0300F但我们大家都知道\x01",
            "阿缇的确很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x103,
        "#0205F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#0102F#1P呵呵，而且，你根本就\x01",
            "没有必要说谎吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x101,
        (
            "#0004F#5P虽然我们认识的时间还不长……\x01",
            "但是缇欧已经帮了我们许多次。\x02\x03",

            "#0000F我认为，没有任何理由\x01",
            "怀疑你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x103,
        (
            "#0205F#6P……………………………………\x02\x03",

            "#0203F……对不起，\x01",
            "我好像说了奇怪的话。\x02\x03",

            "#0200F刚才的那些话，请大家忘掉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#0002F#5P啊？\x01",
            "可以倒是可以啦……\x02",
        )
    )

    CloseMessageWindow()
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    #N0432
    NpcTalk(
        0x18,
        "男性的声音",
        "#3P哎呀，是各位啊……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8767():

        label("loc_8767")

        TurnDirection(0x101, 0x18, 500)
        Yield()
        Jump("loc_8767")

    QueueWorkItem2(0x101, 1, lambda_8767)

    def lambda_8779():

        label("loc_8779")

        TurnDirection(0x102, 0x18, 500)
        Yield()
        Jump("loc_8779")

    QueueWorkItem2(0x102, 1, lambda_8779)

    def lambda_878B():

        label("loc_878B")

        TurnDirection(0x103, 0x18, 500)
        Yield()
        Jump("loc_878B")

    QueueWorkItem2(0x103, 1, lambda_878B)

    def lambda_879D():

        label("loc_879D")

        TurnDirection(0x104, 0x18, 500)
        Yield()
        Jump("loc_879D")

    QueueWorkItem2(0x104, 1, lambda_879D)
    Fade(1000)
    OP_68(1210, 1500, -15280, 0)
    MoveCamera(332, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)

    def lambda_87E2():
        OP_95(0xFE, 470, 0, -11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_87E2)
    WaitChrThread(0x18, 1)
    OP_0D()

    #C0433
    ChrTalk(
        0x101,
        "#0000F啊，哈罗德先生。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0434
    AnonymousTalk(
        0x18,
        (
            "莫非各位也要\x01",
            "回克洛斯贝尔市吗？\x02",
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

    #C0435
    ChrTalk(
        0x102,
        (
            "#0100F#6P嗯，是的……\x02\x03",

            "哈罗德先生也要回去吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x18,
        (
            "#3609F#11P嗯，送给我太太和孩子的\x01",
            "礼物也已经买好了。\x02\x03",

            "#3600F对了，各位\x01",
            "是打算坐巴士吗？\x02\x03",

            "下一班车的发车时间是几点？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x103,
        (
            "#0200F#6P……从时刻表上看，\x01",
            "应该是在三十分钟后呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x104,
        (
            "#0300F#6P要和我们一起\x01",
            "在这里聊天等车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x18,
        (
            "#3605F#11P啊，其实……\x02\x03",

            "#3600F对了，五个人的话，\x01",
            "应该刚好可以吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x5A, 0x190)

    def lambda_8A18():
        OP_95(0xFE, 5640, 0, -14430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8A18)

    def lambda_8A32():

        label("loc_8A32")

        TurnDirection(0x101, 0x18, 500)
        Yield()
        Jump("loc_8A32")

    QueueWorkItem2(0x101, 1, lambda_8A32)

    def lambda_8A44():

        label("loc_8A44")

        TurnDirection(0x102, 0x18, 500)
        Yield()
        Jump("loc_8A44")

    QueueWorkItem2(0x102, 1, lambda_8A44)

    def lambda_8A56():

        label("loc_8A56")

        TurnDirection(0x103, 0x18, 500)
        Yield()
        Jump("loc_8A56")

    QueueWorkItem2(0x103, 1, lambda_8A56)

    def lambda_8A68():

        label("loc_8A68")

        TurnDirection(0x104, 0x18, 500)
        Yield()
        Jump("loc_8A68")

    QueueWorkItem2(0x104, 1, lambda_8A68)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Sleep(1500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Fade(1000)
    OP_68(10480, 1500, -13970, 0)
    MoveCamera(54, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    EndChrThread(0x18, 0x1)
    SetChrPos(0x18, 11830, 0, -13810, 270)
    SetChrSubChip(0x18, 0x0)
    TurnDirection(0x101, 0x18, 0)
    TurnDirection(0x102, 0x18, 0)
    TurnDirection(0x103, 0x18, 0)
    TurnDirection(0x104, 0x18, 0)
    OP_0D()

    #C0440
    ChrTalk(
        0x18,
        (
            "#3609F#11P──各位，不嫌弃的话，\x01",
            "要不要坐我的车回去呢？\x02\x03",

            "#3600F我可以送你们到克洛斯贝尔市哦。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18870, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CA(0x1, 0xFF, 0x0)
    EndChrThread(0x1A, 0x1)
    OP_24(0x348)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_7B40 end

    def Function_39_8BE9(): pass

    label("Function_39_8BE9")

    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(200)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_39_8BE9 end

    def Function_40_8C05(): pass

    label("Function_40_8C05")

    OP_25(0x348, 0x5A)
    Sleep(50)
    OP_25(0x348, 0x50)
    Sleep(50)
    OP_25(0x348, 0x46)
    Sleep(50)
    OP_25(0x348, 0x3C)
    Sleep(50)
    OP_25(0x348, 0x32)
    Sleep(50)
    OP_25(0x348, 0x28)
    Sleep(50)
    OP_25(0x348, 0x1E)
    Sleep(50)
    OP_25(0x348, 0x14)
    Sleep(50)
    OP_25(0x348, 0xA)
    Sleep(50)
    OP_24(0x348)
    Return()

    # Function_40_8C05 end

    def Function_41_8C48(): pass

    label("Function_41_8C48")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-18160, 4700, 64330, 0)
    MoveCamera(339, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18530, 0)
    LoadChrToIndex("apl/ch50387.itc", 0x1E)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -17500, 3500, 60470, 330)
    SetChrPos(0x102, -19270, 3500, 61620, 15)
    SetChrPos(0x103, -15110, 3500, 62020, 330)
    SetChrPos(0x104, -15900, 3500, 59800, 330)
    FadeToBright(500, 0)
    OP_0D()

    #C0441
    ChrTalk(
        0x101,
        (
            "#6P#0000F是阿尔摩利卡村的花田，\x01",
            "还放置了养蜂箱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x103,
        (
            "#12P#0200F克洛斯贝尔唯一的农村……\x02\x03",

            "我觉得在观光指南上介绍\x01",
            "一下这样的风景应该不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x104,
        "#12P#0300F哦～这风景的确不错啊。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        (
            "#6P#0100F因为空气清新，\x01",
            "所以可以看得很远呢。\x02\x03",

            "在克洛斯贝尔自治州内，\x01",
            "说不定只有在这里才能\x01",
            "看到如此美丽的远景吧。\x02\x03",

            "要是没有人在干农活的话，\x01",
            "画面应该会更加适合欣赏吧……\x01",
            "但似乎不会有那么巧呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x101,
        (
            "#6P#0000F不过……\x01",
            "格蕾丝小姐委托我们拍摄的照片，\x01",
            "在这里似乎能拍到很不错的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_943E")
    TurnDirection(0x101, 0x102, 500)

    #C0446
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么艾莉，\x01",
            "可以拜托你来拍照吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0447
    ChrTalk(
        0x102,
        (
            "#6P#0108F哎，好的。\x01",
            "虽然我没什么自信……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x104,
        (
            "#12P#0300F哪里哪里，应该没问题吧。\x02\x03",

            "只要看看镜头，\x01",
            "然后咔嚓一下拍下来\x01",
            "不就搞定了嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0449
    ChrTalk(
        0x102,
        (
            "#6P#0103F我说你啊……\x01",
            "要拍出好照片，\x01",
            "可没有那么简单哦。\x02\x03",

            "#0100F要注意确认\x01",
            "拍摄对象有没有被收入取景框中，\x01",
            "还要构思摄影角度……\x02\x03",

            "而且受到天气和风的影响，\x01",
            "照片所呈现出的感觉也会有很大不同。\x02\x03",

            "有时只要错过那一瞬的时机，\x01",
            "就再也拍不到\x01",
            "那么好的风景了。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x103,
        (
            "#12P#0203F外行和专家所拍出的照片，\x01",
            "差别可是一目了然的。\x02\x03",

            "#0200F不过，某些粗神经的人\x01",
            "大概无法理解这种细致的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0451
    ChrTalk(
        0x104,
        (
            "#12P#0306F唔……\x01",
            "你在说谁啊，说谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x101,
        (
            "#6P#0000F好啦好啦，\x01",
            "总之就交给艾莉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x102,
        (
            "#6P#0100F那么……\x01",
            "我来试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0xF, 0x1F4)
    OP_93(0x101, 0x14A, 0x1F4)
    OP_93(0x103, 0x14A, 0x1F4)
    OP_93(0x104, 0x14A, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0454
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "为了保险起见，我多拍了几张。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        (
            "#6P#0000F看样子，似乎已经拍好了呢。\x02\x03",

            "感觉怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x102,
        (
            "#6P#0100F在没有实际显像出来之前，\x01",
            "还无法确定……\x02\x03",

            "不过，我觉得至少\x01",
            "不会很差吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x103,
        (
            "#12P#0200F艾莉前辈似乎\x01",
            "找回感觉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        (
            "#12P#0300F哼……\x01",
            "反正只有我完全搞不懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#6P#0000F如果发现了这种风景漂亮的地方，\x01",
            "就再拍些照片吧。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9748")

    label("loc_943E")

    TurnDirection(0x101, 0x102, 500)

    #C0460
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "艾莉，麻烦你拍照了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x102,
        "#6P#0100F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0xF, 0x1F4)
    OP_93(0x101, 0x14A, 0x1F4)
    OP_93(0x103, 0x14A, 0x1F4)
    OP_93(0x104, 0x14A, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0462
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "大概就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_95C0")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_95D7")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_95EE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_9605")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9605")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_961C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_961C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_9633")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9633")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_964A")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_964A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_9661")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9661")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_9678")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9678")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9708")

    #C0463
    ChrTalk(
        0x101,
        (
            "#6P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "这样一来，就拍完了格蕾丝小姐\x01",
            "所要求的五张照片了。\x01",
            "现在随时都可以去交付了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9748")

    label("loc_9708")


    #C0464
    ChrTalk(
        0x101,
        (
            "#6P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9748")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -16320, 3500, 61370, 330)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x1E)
    OP_29(0x18, 0x1, 0x3)
    Sleep(500)
    OP_65(0x3, 0x1)
    EventEnd(0x5)
    Return()

    # Function_41_8C48 end

    def Function_42_977E(): pass

    label("Function_42_977E")

    EventBegin(0x0)
    Fade(500)
    OP_68(7350, 1500, -13970, 0)
    MoveCamera(6, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23390, 0)
    SetChrPos(0x101, 7060, 0, -13810, 45)
    SetChrPos(0x102, 5760, 0, -14490, 45)
    SetChrPos(0x103, 7000, 0, -15130, 45)
    SetChrPos(0x104, 5890, 0, -13280, 45)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9836")
    SetChrPos(0x109, 8160, 0, -14550, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_9861")

    label("loc_9836")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9861")
    SetChrPos(0x10A, 8160, 0, -14550, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_9861")

    OP_0D()

    #C0465
    ChrTalk(
        0x101,
        (
            "#6P#0000F请问……\x01",
            "您是艾尔琴先生吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x8,
        "#11P嗯？找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        (
            "#6P#0000F我们是克洛斯贝尔警察局的人，\x01",
            "有点事要问您……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0468
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将回收延期图书\x01",
            "的事由进行了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0469
    ChrTalk(
        0x8,
        "#11P啊……我的确借过那本书。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x102,
        "#6P#0100F那您现在还带着那本书吗……？\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        "#11P这个，其实啊……\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x8,
        "#11P我……我又借给别人了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A2B")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_9A2B")

    Sleep(1000)

    #C0473
    ChrTalk(
        0x101,
        "#6P#0005F不、不是吧……？\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x104,
        (
            "#5P#0306F三重转借啊……\x01",
            "这情况真是不得了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AB4")

    #C0475
    ChrTalk(
        0x109,
        "#12P#0505F这可真令人惊讶……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AEC")

    label("loc_9AB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AEC")

    #C0476
    ChrTalk(
        0x10A,
        "#12P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_9AEC")


    #C0477
    ChrTalk(
        0x102,
        (
            "#6P#0100F话说回来……\x01",
            "这么多人都想借的书，\x01",
            "到底是本什么样的书啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x8,
        "#11P实、实在抱歉啊！！\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x8,
        (
            "#11P因为人家很有诚意，\x01",
            "不断恳求我，所以我\x01",
            "忍不住就借出去啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x8,
        (
            "#11P我本以为让他\x01",
            "马上归还就没问题了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x101,
        (
            "#6P#0005F请、请冷静一下！\x01",
            "既然都已经借出去了，\x01",
            "那也没办法了！\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x103,
        "#6P#0205F那么，您接下来又借给谁了……？\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x8,
        "#11P……咳咳。\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        (
            "#11P嗯，这个嘛……\x01",
            "是农夫多纳尔德。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x8,
        (
            "#11P他应该就在雷欧鲁杂货店\x01",
            "隔壁的民居里。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        (
            "#6P#0006F呼……\x01",
            "没办法，过去找他拿回图书吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CF3")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_9CF3")

    SetChrPos(0x0, 7060, 0, -13810, 45)
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    OP_29(0x28, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_42_977E end

    def Function_43_9D18(): pass

    label("Function_43_9D18")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D7A")

    #C0487
    ChrTalk(
        0x101,
        (
            "#0005F啊，得向村里所有人\x01",
            "都打听一遍才行啊。\x02\x03",

            "#0000F说不定有人\x01",
            "知道魔兽的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DE9")

    #C0488
    ChrTalk(
        0x101,
        (
            "#0004F……唔，回去时就乘坐巴士吧。\x02\x03",

            "#0000F只要前往巴士站，\x01",
            "应该就能查到下班车的发车时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DE9")

    Sleep(50)
    SetChrPos(0x0, 17090, 0, -25640, 321)
    EventEnd(0x4)
    Return()

    # Function_43_9D18 end

    SaveToFile()

Try(main)
