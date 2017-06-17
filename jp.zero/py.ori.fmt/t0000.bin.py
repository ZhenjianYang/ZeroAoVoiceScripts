from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "エルキン",               # 1
        "カミーユ",               # 2
        "プーリー",               # 3
        "セイラーム",             # 4
        "デリック",               # 5
        "アンジェ",               # 6
        "ミリア",                 # 7
        "ステファン",             # 8
        "ペーター",               # 9
        "特級釣師ロイド",         # 10
        "コパン",                 # 11
        "観光客",                 # 12
        "観光客",                 # 13
        "観光客ムラシュ",         # 14
        "観光客エルテ",           # 15
        "車",                     # 16
        "ハロルド",               # 17
        "バス",                   # 18
        "SE制御",                 # 19
        "アルモリカ古道",         # 20
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

    PlaceName(28.0, 0.0, -40.0, 0x0000, 0x0000, "アルモリカ古道")
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
        "Function_7_C16",          # 07, 7
        "Function_8_D57",          # 08, 8
        "Function_9_DEC",          # 09, 9
        "Function_10_139E",        # 0A, 10
        "Function_11_148D",        # 0B, 11
        "Function_12_149B",        # 0C, 12
        "Function_13_266F",        # 0D, 13
        "Function_14_3072",        # 0E, 14
        "Function_15_3547",        # 0F, 15
        "Function_16_3E22",        # 10, 16
        "Function_17_492A",        # 11, 17
        "Function_18_53AD",        # 12, 18
        "Function_19_5A39",        # 13, 19
        "Function_20_5CE3",        # 14, 20
        "Function_21_5F4C",        # 15, 21
        "Function_22_5FC4",        # 16, 22
        "Function_23_6047",        # 17, 23
        "Function_24_65F7",        # 18, 24
        "Function_25_66F7",        # 19, 25
        "Function_26_67E9",        # 1A, 26
        "Function_27_6937",        # 1B, 27
        "Function_28_6A65",        # 1C, 28
        "Function_29_75FD",        # 1D, 29
        "Function_30_76D1",        # 1E, 30
        "Function_31_775D",        # 1F, 31
        "Function_32_7FE6",        # 20, 32
        "Function_33_8549",        # 21, 33
        "Function_34_85AC",        # 22, 34
        "Function_35_860F",        # 23, 35
        "Function_36_8672",        # 24, 36
        "Function_37_86C4",        # 25, 37
        "Function_38_8A6B",        # 26, 38
        "Function_39_9C56",        # 27, 39
        "Function_40_9C72",        # 28, 40
        "Function_41_9CB5",        # 29, 41
        "Function_42_A90D",        # 2A, 42
        "Function_43_AF0B",        # 2B, 43
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

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x32, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x37, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A35")
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
            "バス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市東口\x01",      # 0
            "タングラム門\x01",          # 1
            "停留所（三叉路）\x01",      # 2
            "やめる\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC9")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_C0E")

    label("loc_BC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEE")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_C0E")

    label("loc_BEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0E")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_C0E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_B2B end

    def Function_7_C16(): pass

    label("Function_7_C16")

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

    def lambda_CF2():
        OP_95(0xFE, 10630, 0, -20520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_CF2)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x19, 1)

    def lambda_D1C():
        OP_9E(0xFE, 0x1770, 0xFFFF987C, 0xFFFF0DD0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_D1C)
    WaitChrThread(0x19, 1)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x7)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_C16 end

    def Function_8_D57(): pass

    label("Function_8_D57")

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

    # Function_8_D57 end

    def Function_9_DEC(): pass

    label("Function_9_DEC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1396")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1333")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9C")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_EB8")

    label("loc_E9C")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_EB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEA")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_F04")

    label("loc_EEA")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_F04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F36")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_F50")

    label("loc_F36")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_F50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F82")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_F9C")

    label("loc_F82")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_F9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCE")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_FE8")

    label("loc_FCE")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_FE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1012")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1024")

    label("loc_1012")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_1024")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104E")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1060")

    label("loc_104E")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_1060")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108E")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_10A4")

    label("loc_108E")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_10A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CE")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_10E0")

    label("loc_10CE")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_10E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110C")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1120")

    label("loc_110C")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_1120")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1152")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_116C")

    label("loc_1152")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_116C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1192")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_11A0")

    label("loc_1192")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_11A0")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1324")
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
        (0, "loc_1277"),
        (1, "loc_1285"),
        (2, "loc_1293"),
        (3, "loc_12A1"),
        (4, "loc_12AF"),
        (5, "loc_12BD"),
        (6, "loc_12CB"),
        (7, "loc_12D9"),
        (8, "loc_12E7"),
        (9, "loc_12F5"),
        (10, "loc_1303"),
        (11, "loc_1311"),
        (SWITCH_DEFAULT, "loc_131F"),
    )


    label("loc_1277")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_1285")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_1293")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_12A1")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_12AF")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_12BD")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_12CB")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_12D9")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_12E7")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_12F5")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_1303")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_1311")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_131F")

    label("loc_131F")

    Jump("loc_132E")

    label("loc_1324")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_132E")

    Jump("loc_1391")

    label("loc_1333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137E")
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
    Jump("loc_1391")

    label("loc_137E")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1391")

    Jump("loc_E06")

    label("loc_1396")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_DEC end

    def Function_10_139E(): pass

    label("Function_10_139E")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1472")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_1478")

    label("loc_1472")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_1478")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_139E end

    def Function_11_148D(): pass

    label("Function_11_148D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_11_148D end

    def Function_12_149B(): pass

    label("Function_12_149B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157C")

    #C0002
    ChrTalk(
        0xFE,
        (
            "あ、本は見つかったんだね。\x01",
            "よかった～……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの本とあっちゃ、\x01",
            "どうも見たくて仕方なくてね。\x01",
            "無理を言って借りちゃったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "これぞアルカンシェルの\x01",
            "魔力ってやつかな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_157C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1621")

    #C0005
    ChrTalk(
        0xFE,
        (
            "僕が本を貸してしまったのは\x01",
            "農家のドナルドさんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "レオール雑貨店の\x01",
            "隣の民家にいるはずさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "はぁ、本当に申し訳ない……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_1621")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_163E")
    Call(0, 42)
    TalkEnd(0xFE)
    Return()

    label("loc_163E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1798")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F0")

    #C0008
    ChrTalk(
        0xFE,
        (
            "んん～っ、いい朝だな。\x01",
            "絶好のドライブ日和……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "……今から野菜を卸しに行くのが\x01",
            "楽しみでならねぇだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "……コホン。\x01",
            "楽しみでならない、よ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1793")

    label("loc_16F0")


    #C0011
    ChrTalk(
        0xFE,
        (
            "ううん、車のことになると\x01",
            "どうも興奮して訛りが出ちゃうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "普段気取って標準語使ってるだけに、\x01",
            "訛りがバレると恥ずかしいし……\x01",
            "今度から気を付けようっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1793")

    Jump("loc_266B")

    label("loc_1798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_182B")

    #C0013
    ChrTalk(
        0xFE,
        (
            "朝のうちにクロスベル市に\x01",
            "野菜を卸しに行ったら、\x01",
            "妙に人だかりができててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "マフィアの抗争だってさ。\x01",
            "いやぁ、物騒だよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266B")

    label("loc_182B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B2A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DD")

    #C0015
    ChrTalk(
        0xFE,
        "くぁ～……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "いかんいかん、平和すぎて\x01",
            "思わずアクビがでちゃうね。\x02",
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
            "って……あれはもしかして……\x01",
            "警備隊の軽装甲車でねぇだか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "武骨な武器を搭載しない\x01",
            "この洗練されたフォルム……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "う～ん、かっこいいだァ！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x109,
        (
            "#0505Fおお……話せますね！\x02\x03",

            "#0509Fふふ、やっぱり分かる人には\x01",
            "良さが分かるんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#0306Fん～、理解しがたい世界だな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A9E")

    label("loc_19DD")


    #C0022
    ChrTalk(
        0xFE,
        "……コホン。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "警備隊の軽装甲車は\x01",
            "確かに戦闘力は低いけど\x01",
            "美しい造形だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "せっかくのいい車なんだ、\x01",
            "ぶつけないように注意してくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        "#0500Fふふ、ご忠告ありがとうございます。\x02",
    )

    CloseMessageWindow()

    label("loc_1A9E")

    Jump("loc_1B25")

    label("loc_1AA3")


    #C0026
    ChrTalk(
        0xFE,
        "くぁ～……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "いかんいかん、平和すぎて\x01",
            "思わずアクビがでちゃうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "気が抜けすぎて\x01",
            "車をぶつけないように注意しないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B25")

    Jump("loc_266B")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCE")

    #C0029
    ChrTalk(
        0xFE,
        "今日で今年の記念祭も終わりかぁ。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "デリックが出店やったり、\x01",
            "観光客が古戦場に踏み込んだり……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "なかなか刺激的で楽しかったよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C3A")

    label("loc_1BCE")


    #C0032
    ChrTalk(
        0xFE,
        (
            "デリックが出店やったり、\x01",
            "観光客が古戦場に踏み込んだり……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "今年の記念祭は\x01",
            "なんだか刺激的だったね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C3A")

    Jump("loc_266B")

    label("loc_1C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CC3")

    #C0034
    ChrTalk(
        0xFE,
        (
            "記念祭最終日だから、\x01",
            "明日だけ仕事が休みになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "運搬用のトラックを借りて、\x01",
            "ドライブでもしようかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266B")

    label("loc_1CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAF")

    #C0036
    ChrTalk(
        0xFE,
        (
            "例年通り、記念祭の観光客が\x01",
            "この村に流れてきてるみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "しかも今年は、\x01",
            "出店に本格的に力を入れてるせいか\x01",
            "観光客の数が多いみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "導力バスが\x01",
            "こんな頻度で使われるなんて\x01",
            "滅多にないことだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E19")

    label("loc_1DAF")


    #C0039
    ChrTalk(
        0xFE,
        (
            "例年通り、\x01",
            "記念祭の観光客が\x01",
            "この村に流れてきてるみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "やっぱり、導力バスって便利だよね。\x02",
    )

    CloseMessageWindow()

    label("loc_1E19")

    Jump("loc_266B")

    label("loc_1E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1EC3")

    #C0041
    ChrTalk(
        0xFE,
        "村に何人か観光客が来てるよ。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "ミリア姉さんも\x01",
            "記念祭中はデリックの代わりに\x01",
            "養蜂場に入るらしいし……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "ま、賑やかになるのは\x01",
            "大変結構だよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266B")

    label("loc_1EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_204B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAC")

    #C0044
    ChrTalk(
        0xFE,
        (
            "村長の息子のデリックが\x01",
            "記念祭に店を出すらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "商品やら機材やらの運搬に\x01",
            "村のトラックを使うんだけど……\x01",
            "俺に運転を任せてくれるんだとさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "……いやっほい！\x01",
            "バッチリ仕事をこなしてやるだよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2046")

    label("loc_1FAC")


    #C0047
    ChrTalk(
        0xFE,
        (
            "ふふ、仕事以外での\x01",
            "トラックの運転……楽しみだァ！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "バッチリ仕事を\x01",
            "こなしてやるだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "……おっとと。\x01",
            "興奮して言葉が訛っちゃったよ。\x01",
            "へへ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2046")

    Jump("loc_266B")

    label("loc_204B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_21B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2111")

    #C0050
    ChrTalk(
        0xFE,
        (
            "さて、そろそろクロスベル市の店に\x01",
            "作物を卸しに行かないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "個人の商人相手の商売は増えてきたけど\x01",
            "やっぱりクロスベル市のデパートや百貨店も\x01",
            "疎かにできないからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21AC")

    label("loc_2111")


    #C0052
    ChrTalk(
        0xFE,
        (
            "作物を安定して\x01",
            "大量に引き取ってくれるのは\x01",
            "やっぱり市内の店なんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "ハロルドさんたちとの商売も大事だけど、\x01",
            "こっちのほうがまだまだ主流なのさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AC")

    Jump("loc_266B")

    label("loc_21B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2247")

    #C0054
    ChrTalk(
        0xFE,
        (
            "バスの本数が少ないのは\x01",
            "導力車好きとしては\x01",
            "寂しい限りだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "ま、この村は\x01",
            "殆ど自給自足で賄ってるから\x01",
            "それほど不便はないけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266B")

    label("loc_2247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_2384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FE")

    #C0056
    ChrTalk(
        0xFE,
        (
            "導力バスは日に何本か来るけど\x01",
            "クロスベル市から乗ってくる人は\x01",
            "ほとんどいないんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "村人がバスを使うのも\x01",
            "たまに買い出しに行って\x01",
            "戻るくらいだし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_237F")

    label("loc_22FE")


    #C0058
    ChrTalk(
        0xFE,
        (
            "導力バスは通ってるけど、\x01",
            "クロスベル市から人が来るのは\x01",
            "結構稀なんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "たまに遊撃士が\x01",
            "呼ばれて来るくらいのもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_237F")

    Jump("loc_266B")

    label("loc_2384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_254A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D8")

    #C0060
    ChrTalk(
        0xFE,
        (
            "あの事件の朝、トラックのボディが\x01",
            "傷だらけになっててさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "……思い出したら\x01",
            "ムカッ腹が立ってきただァ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "トラックは村に欠かせない\x01",
            "そりゃあもう大切なモノなんだァ！\x01",
            "よくもそれを……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "……ご、ごほん。\x01",
            "とにかく、あの爪あとの感じ……\x01",
            "狼型の魔獣の仕業にはちがいないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D0")
    SetScenarioFlags(0x68, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24D0")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2545")

    label("loc_24D8")


    #C0064
    ChrTalk(
        0xFE,
        (
            "……興奮すると言葉が\x01",
            "訛っちゃうんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "はぁ、何で俺だけ。\x01",
            "ミリア姉さんは\x01",
            "全く訛ってないのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2545")

    Jump("loc_266B")

    label("loc_254A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_266B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2607")

    #C0066
    ChrTalk(
        0xFE,
        "君たち、クロスベル市の人？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "おかしいなぁ、\x01",
            "さっきバスが出たばっかりなのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "……なに、歩いて来ただって！？\x01",
            "はぁ、都会人の考えることはわからんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_266B")

    label("loc_2607")


    #C0069
    ChrTalk(
        0xFE,
        "ん、村長に用事かい？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "村長の家なら、\x01",
            "村の一番奥にあるよ。\x01",
            "道なりに行けばすぐ分かるはずさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_266B")

    TalkEnd(0xFE)
    Return()

    # Function_12_149B end

    def Function_13_266F(): pass

    label("Function_13_266F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268D")
    Call(0, 14)
    Jump("loc_2761")

    label("loc_268D")

    OP_93(0xFE, 0xB4, 0x0)
    OP_4B(0xA, 0xFF)

    #C0071
    ChrTalk(
        0xFE,
        (
            "よーし、じゃあ遊撃士ごっこの\x01",
            "役を決めよーぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "……おれ、アリオスさんとった！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        "あたし、おおかみまじゅーさんとったー！！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xA, 500)
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0074
    ChrTalk(
        0xFE,
        "……いいのかよ、それで。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_2761")

    Jump("loc_306E")

    label("loc_2766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2810")
    OP_4B(0xA, 0xFF)

    #C0075
    ChrTalk(
        0xFE,
        (
            "今日はステファンのやつは\x01",
            "《トネリコ亭》でゆっくりしてるってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "んー、病気でもしたのかな？\x01",
            "あとで見舞いに行ってやるかー。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        "やるかー。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_306E")

    label("loc_2810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_296F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290F")
    OP_93(0xFE, 0xB4, 0x0)

    #C0078
    ChrTalk(
        0xFE,
        (
            "ステファンお前、足遅いなー。\x01",
            "プーリーに捕まるなんてよっぽどだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "こりゃ、村に引っ越してきたら\x01",
            "本格的にかけっこのトックンだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x109,
        (
            "#0502Fふふ……のどかですね。\x02\x03",

            "こんな平和を\x01",
            "いつまでも守っていきたいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_296A")

    label("loc_290F")


    #C0081
    ChrTalk(
        0xFE,
        (
            "ま、それはさておき……\x01",
            "次はステファンがオニな！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "日が暮れる前に捕まえてくれよ～？\x02",
    )

    CloseMessageWindow()

    label("loc_296A")

    Jump("loc_306E")

    label("loc_296F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_29EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298A")
    Call(0, 14)
    Jump("loc_29EA")

    label("loc_298A")


    #C0083
    ChrTalk(
        0xFE,
        (
            "記念祭……\x01",
            "やっぱ行きたかったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "ま、今度ステファンに話してもらえば\x01",
            "それでいいや！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29EA")

    Jump("loc_306E")

    label("loc_29EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A69")

    #C0085
    ChrTalk(
        0xFE,
        (
            "そっか、明日で\x01",
            "記念祭も終わりだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "なんてか、あっという間だったな。\x01",
            "行けなかったのが残念だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306E")

    label("loc_2A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2ACE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A84")
    Call(0, 14)
    Jump("loc_2AC9")

    label("loc_2A84")


    #C0087
    ChrTalk(
        0xFE,
        (
            "遊撃士と警察と不良の\x01",
            "バトル大会……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "くぅ～見たかったなぁ！\x02",
    )

    CloseMessageWindow()

    label("loc_2AC9")

    Jump("loc_306E")

    label("loc_2ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2B39")

    #C0089
    ChrTalk(
        0xFE,
        (
            "あ～、創立記念祭に行きたかったけど……\x01",
            "母さんが忙しいからダメだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        "ちぇっ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_306E")

    label("loc_2B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2CAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2E")

    #C0091
    ChrTalk(
        0xFE,
        (
            "《アルカンシェル》のイリアさんには\x01",
            "かっこいいアダ名があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "その名も《炎の舞姫》！\x01",
            "くぅ～、シビれるっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "おれも《風の剣聖》とか\x01",
            "《雷鳴の勇者》とか《大海坊主》とか……\x01",
            "すごいアダ名で呼ばれてみたいぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CA8")

    label("loc_2C2E")


    #C0094
    ChrTalk(
        0xFE,
        (
            "《炎の舞姫》ってアダ名\x01",
            "かっこいいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "おれもイリアさんやアリオスさんみたいに\x01",
            "すごいアダ名で呼ばれてみたいぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA8")

    Jump("loc_306E")

    label("loc_2CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2D3F")

    #C0096
    ChrTalk(
        0xFE,
        (
            "なんかさー、クロスベル市のほうで\x01",
            "すっごい劇があるらしいじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "《アルカンシェル》……だっけ？\x01",
            "いいなぁ、見てみたいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306E")

    label("loc_2D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D5A")
    Call(0, 14)
    Jump("loc_2DDC")

    label("loc_2D5A")


    #C0098
    ChrTalk(
        0xFE,
        (
            "うーん……\x01",
            "プーリーが魔獣役だと\x01",
            "なんか緊張感がないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "あのステファンってヤツが\x01",
            "入ってくれると\x01",
            "色々遊べそうなのになぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDC")

    Jump("loc_306E")

    label("loc_2DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_2EE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E91")

    #C0100
    ChrTalk(
        0xFE,
        (
            "はぁ、またアリオスさん来ないかなぁ。\x01",
            "すっごいカッコいいんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "前に鶏が逃げた時も\x01",
            "あっという間に捕まえてくれたし。\x01",
            "いやぁ、憧れるなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EDB")

    label("loc_2E91")


    #C0102
    ChrTalk(
        0xFE,
        (
            "うん、やっぱりおれ……\x01",
            "アリオスさんみたいな\x01",
            "すごい遊撃士を目指すぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EDB")

    Jump("loc_306E")

    label("loc_2EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_2FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9B")

    #C0103
    ChrTalk(
        0xFE,
        (
            "村長に聞いたんだけど、\x01",
            "『シンロウ』とかいうのが\x01",
            "犯人だったんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "なーに心配いらないって。\x01",
            "次に村に来たら、このカミーユさまが\x01",
            "ばっちり倒してやるさ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FDE")

    label("loc_2F9B")


    #C0105
    ChrTalk(
        0xFE,
        (
            "おれは未来の遊撃士だからな。\x01",
            "この村の平和くらい守ってやるぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FDE")

    Jump("loc_306E")

    label("loc_2FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_306E")

    #C0106
    ChrTalk(
        0xFE,
        (
            "ちぇっ、この村も平和だなぁ。\x01",
            "空気がうまくていいんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "あーあ、またこないだみたいな\x01",
            "大騒ぎが起こればいいのにな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306E")

    TalkEnd(0xFE)
    Return()

    # Function_13_266F end

    def Function_14_3072(): pass

    label("Function_14_3072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_312D")
    OP_93(0xF, 0x6B, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0xA, 0x13B, 0x0)
    OP_4B(0xF, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0108
    ChrTalk(
        0x9,
        "よし、今日は天気もいいことだし……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        "久しぶりに遊撃士ごっこでもやろーぜ！\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        "やるー！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xF,
        "（やっぱコドモだなぁ……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3543")

    label("loc_312D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_313B")
    Jump("loc_3543")

    label("loc_313B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3149")
    Jump("loc_3543")

    label("loc_3149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3289")
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
            "おー、ステファンお帰り！\x01",
            "早かったじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xF,
        (
            "う、うん。\x01",
            "母さんが『閉会式は絶対混むから、\x01",
            "それの前に帰ろう』って……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        "ふーん。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "……じゃ、\x01",
            "今度でいいから記念祭の話\x01",
            "いっぱい聞かせてくれよな！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        "聞かせて聞かせて！\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xF,
        "う、うん、別にいいけど……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3543")

    label("loc_3289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3297")
    Jump("loc_3543")

    label("loc_3297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33E6")
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
            "クロスベル市から来た人が\x01",
            "言ってたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "遊撃士と警察と不良の\x01",
            "バトル大会があったんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xD,
        (
            "……本当かい？\x01",
            "やれやれ、物騒な話だねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "けんか？\x01",
            "けんかしちゃったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#0006F（こ、こんな所にまで噂が……）\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        "#0306F（微妙に広まっちまってるなぁ……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3543")

    label("loc_33E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_33F4")
    Jump("loc_3543")

    label("loc_33F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3402")
    Jump("loc_3543")

    label("loc_3402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3410")
    Jump("loc_3543")

    label("loc_3410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_351E")
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0124
    ChrTalk(
        0xA,
        "がおー！　おおかみさんだぞー！\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "魔獣めぇ……！\x01",
            "よくも村を荒らしてくれたなぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "この超ＡＡＡ級遊撃士#6Rブレイサー#の\x01",
            "カミーユさまがいるかぎり、\x01",
            "この村の平和は乱させないぞっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "きゃははっ！\x01",
            "がおー！　がおーん！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3543")

    label("loc_351E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_352C")
    Jump("loc_3543")

    label("loc_352C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_353A")
    Jump("loc_3543")

    label("loc_353A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3543")

    label("loc_3543")

    SetScenarioFlags(0x0, 1)
    Return()

    # Function_14_3072 end

    def Function_15_3547(): pass

    label("Function_15_3547")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_35BE")

    #C0128
    ChrTalk(
        0xFE,
        (
            "えへへ、やっぱり\x01",
            "みんなであそぶとたのしいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "おにいちゃんもステファンくんも\x01",
            "だいすきー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E1E")

    label("loc_35BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_361B")

    #C0130
    ChrTalk(
        0xFE,
        "今日は何してあそぼっか～。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "やっぱりはしりまわれる遊びが\x01",
            "すきだなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E1E")

    label("loc_361B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_376C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3716")

    #C0132
    ChrTalk(
        0xFE,
        (
            "おにいちゃんとステファンくんと\x01",
            "３人でおにごっこしてたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "プーリー、足速いんだよ～。\x01",
            "えっへん！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#0002F……この子たち、キーアとも\x01",
            "気が合いそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        (
            "#0304Fあぁ、今度連れてきてやるのも\x01",
            "いいかもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3767")

    label("loc_3716")


    #C0136
    ChrTalk(
        0xFE,
        (
            "おにいちゃんとステファンくんと\x01",
            "３人でおにごっこしてたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "たのしーな！\x02",
    )

    CloseMessageWindow()

    label("loc_3767")

    Jump("loc_3E1E")

    label("loc_376C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_37F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3787")
    Call(0, 14)
    Jump("loc_37F1")

    label("loc_3787")

    OP_93(0xFE, 0x13B, 0x0)
    OP_4B(0xF, 0xFF)

    #C0138
    ChrTalk(
        0xFE,
        "ねーねー、おみやげは？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xF,
        (
            "あ、うん……\x01",
            "一応買ってるから後であげるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "わーい♪\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    label("loc_37F1")

    Jump("loc_3E1E")

    label("loc_37F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_390C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38BB")

    #C0141
    ChrTalk(
        0xFE,
        (
            "おにいちゃん、\x01",
            "きねんさい行きたかったーって\x01",
            "なんかいも言ってんの。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "プーリーはきねんさい、\x01",
            "たのしかったよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "おにいちゃんに\x01",
            "いっぱい遊んでもらったからね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3907")

    label("loc_38BB")


    #C0144
    ChrTalk(
        0xFE,
        (
            "おにいちゃんに\x01",
            "いっぱい遊んでもらったから\x01",
            "プーリーはたのしかったよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3907")

    Jump("loc_3E1E")

    label("loc_390C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_399A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3927")
    Call(0, 14)
    Jump("loc_3995")

    label("loc_3927")


    #C0145
    ChrTalk(
        0xFE,
        (
            "あそびならいいけど、\x01",
            "けんかはしちゃだめなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "おかあさんに怒られちゃっても\x01",
            "プーリーしらないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3995")

    Jump("loc_3E1E")

    label("loc_399A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3A01")

    #C0147
    ChrTalk(
        0xFE,
        "村に知らない人がきてるの。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "せっかくだから、\x01",
            "プーリーとあそんでくれないかなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E1E")

    label("loc_3A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3A6B")

    #C0149
    ChrTalk(
        0xFE,
        (
            "あるかんしえるは\x01",
            "見てみたいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "プーリーはおにいちゃんと\x01",
            "あそぶからいいもん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E1E")

    label("loc_3A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AE0")

    #C0151
    ChrTalk(
        0xFE,
        (
            "あるかん……しえる。\x01",
            "ふ～ん？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "おにいちゃんがいきたいなら\x01",
            "あたしもいきたいな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B28")

    label("loc_3AE0")


    #C0153
    ChrTalk(
        0xFE,
        (
            "あるかんしえる……\x01",
            "おにいちゃんがいきたいなら\x01",
            "あたしもいきた～い。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B28")

    Jump("loc_3E1E")

    label("loc_3B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B48")
    Call(0, 14)
    Jump("loc_3B9C")

    label("loc_3B48")


    #C0154
    ChrTalk(
        0xFE,
        (
            "がおー！\x01",
            "おにいちゃん、がおー！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "たーべーちゃーうーぞー！\x01",
            "……きゃははは！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B9C")

    Jump("loc_3E1E")

    label("loc_3BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_3C5C")

    #C0156
    ChrTalk(
        0xFE,
        (
            "こないだから\x01",
            "《トネリコ亭》に泊まってる\x01",
            "おにいちゃん……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "たまには\x01",
            "遊んでくれたらいいのになー。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "……ま、いっか。\x01",
            "プーリーのおにいちゃんが\x01",
            "遊んでくれるもんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E1E")

    label("loc_3C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_3D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD3")

    #C0159
    ChrTalk(
        0xFE,
        (
            "んー……\x01",
            "おおかみさんって\x01",
            "そんなに悪いことしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "プーリー、よく覚えてないや。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D4A")

    label("loc_3CD3")


    #C0161
    ChrTalk(
        0xFE,
        (
            "ちょっと前から、\x01",
            "あそぶときにお母さんが\x01",
            "ついてくるようになったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "おおかみさんが出たのと\x01",
            "カンケイある？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D4A")

    Jump("loc_3E1E")

    label("loc_3D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3E1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE0")

    #C0163
    ChrTalk(
        0xFE,
        "おにいちゃんたち、だあれ？\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        "……けいさつ？　ふ～ん……？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        "#0006F（……な、なんか微妙にヘコむ反応だな。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E1E")

    label("loc_3DE0")


    #C0166
    ChrTalk(
        0xFE,
        "け・い・さ・つ。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "……………………ふ～ん、何だっけ？\x02",
    )

    CloseMessageWindow()

    label("loc_3E1E")

    TalkEnd(0xFE)
    Return()

    # Function_15_3547 end

    def Function_16_3E22(): pass

    label("Function_16_3E22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3F48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EFE")

    #C0168
    ChrTalk(
        0xFE,
        (
            "いままで何かと理由をつけて\x01",
            "挑戦を避けてきたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "今日来ている釣公師団の人に、\x01",
            "入れてもらえるよう頼んでみるわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "前回は人見知りで\x01",
            "建物にすら入れなかったけど、\x01",
            "今度こそ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F43")

    label("loc_3EFE")


    #C0171
    ChrTalk(
        0xFE,
        (
            "釣りライフを楽しむためにも、\x01",
            "今度こそ釣公師団に入れてもらうの！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F43")

    Jump("loc_4926")

    label("loc_3F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3FD5")

    #C0172
    ChrTalk(
        0xFE,
        (
            "……あの釣公師団の人……\x01",
            "ずっとああやってぼ～っと\x01",
            "釣り糸をたらしてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "……いいなぁ。\x01",
            "私もゆっくり釣りをしたい……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_3FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_404A")

    #C0174
    ChrTalk(
        0xFE,
        "また釣公師団の人が釣りに来てるわ……\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "ど、どうしよう。\x01",
            "釣公師団に入れてもらえるチャンス……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_404A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4103")

    #C0176
    ChrTalk(
        0xFE,
        (
            "……結局、記念祭中も\x01",
            "釣公師団の敷居はまたげなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "まぁ、仕方ないわよね。\x01",
            "お祭りモードでどこも忙しそうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "……はぁ。\x01",
            "自分のダメさが嫌になるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_4103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4198")

    #C0179
    ChrTalk(
        0xFE,
        (
            "結構観光客が来てるけど……\x01",
            "今日は釣公師団の団員らしき人は\x01",
            "見かけないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……やっぱりスカウト待ちは\x01",
            "あきらめるべきかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_4198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_424D")

    #C0181
    ChrTalk(
        0xFE,
        (
            "あそこの橋のところで\x01",
            "釣りをしている人がいるでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "どうやら釣公師団の人らしいけど……\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "……ああっ、どうしよう！\x01",
            "話しかけてみようかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42B2")

    label("loc_424D")


    #C0184
    ChrTalk(
        0xFE,
        "憧れの釣公師団の人が今そこに……\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "話しかけてみたいけど……\x01",
            "うう、釣りをしてるのに迷惑よね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42B2")

    Jump("loc_4926")

    label("loc_42B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_43DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4377")

    #C0186
    ChrTalk(
        0xFE,
        (
            "……今回、観光客が\x01",
            "どっさり来ると見たわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "釣公師団の人も来るかもしれないから\x01",
            "ここで魚を眺めて待ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "何をって……\x01",
            "スカウトに決まってるじゃない！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43D8")

    label("loc_4377")


    #C0189
    ChrTalk(
        0xFE,
        (
            "釣公師団の人にスカウトされるために、\x01",
            "ここでさりげなく魚を眺めてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        "……来るかなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_43D8")

    Jump("loc_4926")

    label("loc_43DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C1")

    #C0191
    ChrTalk(
        0xFE,
        (
            "……昨日、思い切って\x01",
            "クロスベル市の釣公師団の支部まで\x01",
            "行ってきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "入団したら\x01",
            "釣り三昧の生活が待っている！\x01",
            "……と思ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "……行ってきたダケだけど。\x01",
            "あぁっ、わたしの人見知りが憎い！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44FC")

    label("loc_44C1")


    #C0194
    ChrTalk(
        0xFE,
        (
            "はぁ……わたしのあほう。\x01",
            "釣公師団入団への道は遠いわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44FC")

    Jump("loc_4926")

    label("loc_4501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B4")

    #C0195
    ChrTalk(
        0xFE,
        (
            "私、思ったの。\x01",
            "やっぱり釣りがしたいって\x01",
            "思ってるだけじゃだめね。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "あとでバスでクロスベル市に行って、\x01",
            "釣公師団支部の\x01",
            "入団試験を受けに行くわ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4634")

    label("loc_45B4")


    #C0197
    ChrTalk(
        0xFE,
        (
            "あとでクロスベル市の釣公師団支部に\x01",
            "行こうと思うの。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "……はぁ～ドキドキしてきた。\x01",
            "ちゃんと入団させてもらえるかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4634")

    Jump("loc_4926")

    label("loc_4639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_46C9")

    #C0199
    ChrTalk(
        0xFE,
        "あぁ……釣りがしたーい。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "釣公師団に入れば\x01",
            "釣具を譲ってもらえるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "やっぱり、\x01",
            "なんとか入れてもらわなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_46C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_47B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4751")

    #C0202
    ChrTalk(
        0xFE,
        (
            "あ……あなたたち\x01",
            "クロスベル市から来てたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "あそこには\x01",
            "釣公師団の支部があるのよね。\x01",
            "いいなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47B3")

    label("loc_4751")


    #C0204
    ChrTalk(
        0xFE,
        "釣公師団……いいなぁ。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "さぞ、釣りばっかりして\x01",
            "過ごしてるんでしょうね。\x01",
            "うらやましい……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B3")

    Jump("loc_4926")

    label("loc_47B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_484F")

    #C0206
    ChrTalk(
        0xFE,
        (
            "狼型魔獣の被害があった夜……？\x01",
            "うーん、そうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "うーむむむ……\x01",
            "３週間近くも前のことだしなぁ。\x01",
            "悪いけどあんまり覚えてないわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4926")

    label("loc_484F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C2")

    #C0208
    ChrTalk(
        0xFE,
        (
            "清らかな水の流れ……\x01",
            "太陽の光をギラギラ反射する\x01",
            "お魚の表面……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        "……素敵よね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4926")

    label("loc_48C2")


    #C0210
    ChrTalk(
        0xFE,
        (
            "あ！！\x01",
            "今、魚影が見えた気がするわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "……あーん、やっぱり\x01",
            "あたし専用の釣りざおが欲しいっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4926")

    TalkEnd(0xFE)
    Return()

    # Function_16_3E22 end

    def Function_17_492A(): pass

    label("Function_17_492A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4AA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A20")

    #C0212
    ChrTalk(
        0xFE,
        (
            "俺は別に、伝統を崩したり\x01",
            "自然を損ねてまで\x01",
            "村を発展させたいわけじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "ただ村人が豊かに暮らせるように\x01",
            "最良の選択をしていきたいだけなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "その為にはやはり村に人を集め、\x01",
            "賑やかにしていかなくては……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4AA3")

    label("loc_4A20")


    #C0215
    ChrTalk(
        0xFE,
        (
            "俺はただ、\x01",
            "村人が豊かに暮らせるように\x01",
            "最良の選択をしていきたいだけなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "なぜ親父は……\x01",
            "村長は分かってくれないんだ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AA3")

    Jump("loc_53A9")

    label("loc_4AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4C11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B98")

    #C0217
    ChrTalk(
        0xFE,
        (
            "なぜクロスベル市は\x01",
            "あんなに発展したのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "それに比べ、なぜアルモリカ村は\x01",
            "昔とほとんど変わらない\x01",
            "質素な暮らしをしているのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "その違いを見極めなければ\x01",
            "村を発展させることは\x01",
            "相当に難しいだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4C0C")

    label("loc_4B98")


    #C0220
    ChrTalk(
        0xFE,
        (
            "なぜクロスベル市は\x01",
            "あんなに発展したのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "アルモリカの発展のためには、\x01",
            "それを見極める必要がありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C0C")

    Jump("loc_53A9")

    label("loc_4C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4CF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA3")

    #C0222
    ChrTalk(
        0xFE,
        (
            "記念祭に店を出したときに\x01",
            "村に来ていた観光客も\x01",
            "最近ではぱったりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "またなにか新しいやり方を\x01",
            "考えなければ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CF1")

    label("loc_4CA3")


    #C0224
    ChrTalk(
        0xFE,
        (
            "次期村長として……\x01",
            "村の歴史を途絶えさせないよう\x01",
            "色々と手を考えなければ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CF1")

    Jump("loc_53A9")

    label("loc_4CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4D04")
    Jump("loc_53A9")

    label("loc_4D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4D12")
    Jump("loc_53A9")

    label("loc_4D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4D20")
    Jump("loc_53A9")

    label("loc_4D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4D2E")
    Jump("loc_53A9")

    label("loc_4D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4D3C")
    Jump("loc_53A9")

    label("loc_4D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4EB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E34")

    #C0225
    ChrTalk(
        0xFE,
        (
            "今度クロスベル市で開かれる\x01",
            "創立記念祭……\x01",
            "そこに店を出すことを提案したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "多くの観光客が\x01",
            "訪れているようだからね。\x01",
            "村の名前を知ってもらういい機会だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "やはり、特産品のハチミツを\x01",
            "出品するのがいいだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4EAC")

    label("loc_4E34")


    #C0228
    ChrTalk(
        0xFE,
        (
            "創立記念祭に出す店……\x01",
            "特産品のハチミツを出品するのが\x01",
            "やはりベストだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "レオールさんにも相談してみるか……\x02",
    )

    CloseMessageWindow()

    label("loc_4EAC")

    Jump("loc_53A9")

    label("loc_4EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4FE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F66")

    #C0230
    ChrTalk(
        0xFE,
        (
            "村長の息子である俺が\x01",
            "養蜂場で働いているのが\x01",
            "おかしいか？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "……息子、だからこそだよ。\x01",
            "村を支える農作業を知らずして\x01",
            "村長になれるわけがないからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4FDF")

    label("loc_4F66")


    #C0232
    ChrTalk(
        0xFE,
        (
            "現場を知らない人間が\x01",
            "人の上に立てるわけが無い。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "俺はお山の大将じゃなく\x01",
            "本当に村を良くしたいと\x01",
            "思っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FDF")

    Jump("loc_53A9")

    label("loc_4FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_512B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50D0")

    #C0234
    ChrTalk(
        0xFE,
        (
            "ハロルドさんのような\x01",
            "良識のある商人のお陰で\x01",
            "村はなんとか保っている状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "村の若者も、そのうち\x01",
            "クロスベル市に出て行ってしまうだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "村はこのままでは\x01",
            "衰退するばかりだ。\x01",
            "……何とかしないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5126")

    label("loc_50D0")


    #C0237
    ChrTalk(
        0xFE,
        (
            "村を存続させるには\x01",
            "今までと同じようにやっていてはダメだ。\x01",
            "……何とかしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5126")

    Jump("loc_53A9")

    label("loc_512B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_5282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51EB")

    #C0238
    ChrTalk(
        0xFE,
        (
            "村長、『神狼』がどうとか\x01",
            "言っていたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "……彼は俺の父なんだが\x01",
            "どうにも考えが古くて困る。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "もっと村を発展させる為に\x01",
            "なんとかして欲しいものだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_527D")

    label("loc_51EB")


    #C0241
    ChrTalk(
        0xFE,
        (
            "多くの家畜に被害を出したのは\x01",
            "防衛意識の足りなさが招いた結果だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "やはり、この村は変わらないといけない。\x01",
            "村長の……父のやり方は古いんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_527D")

    Jump("loc_53A9")

    label("loc_5282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_53A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5335")
    OP_93(0xFE, 0x12A, 0x0)

    #C0243
    ChrTalk(
        0xFE,
        (
            "……このままではこの村も\x01",
            "長くないだろうな……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0244
    ChrTalk(
        0xFE,
        "……なんだ？　俺は今忙しいんだ。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "なに、村長に用がある？\x01",
            "家ならすぐそこだぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53A9")

    label("loc_5335")


    #C0246
    ChrTalk(
        0xFE,
        (
            "村長に用があるんだろう？\x01",
            "家ならすぐそこだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "もっとも、今は来客中だが……\x01",
            "そろそろ話もまとまった頃だろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53A9")

    TalkEnd(0xFE)
    Return()

    # Function_17_492A end

    def Function_18_53AD(): pass

    label("Function_18_53AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_53BE")
    Jump("loc_5A35")

    label("loc_53BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_54EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54B2")
    OP_93(0xD, 0x56, 0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0248
    ChrTalk(
        0xFE,
        (
            "今日はおやつの時間に\x01",
            "アップルパイを焼いたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "んー、ステファン君が来ないなら\x01",
            "これはお預けだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5459():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5459)

    def lambda_5466():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5466)
    WaitChrThread(0xA, 1)

    #C0250
    ChrTalk(
        0x9,
        "うそっ！？\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xA,
        "やだーっ！！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    SetScenarioFlags(0x0, 5)
    Jump("loc_54E7")

    label("loc_54B2")


    #C0252
    ChrTalk(
        0xFE,
        (
            "ステファン君が来ないなら\x01",
            "おやつはお預けだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54E7")

    Jump("loc_5A35")

    label("loc_54EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_54FA")
    Jump("loc_5A35")

    label("loc_54FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5508")
    Jump("loc_5A35")

    label("loc_5508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5516")
    Jump("loc_5A35")

    label("loc_5516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5531")
    Call(0, 14)
    Jump("loc_5553")

    label("loc_5531")


    #C0253
    ChrTalk(
        0xFE,
        "やれやれ、都会は物騒だねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_5553")

    Jump("loc_5A35")

    label("loc_5558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5566")
    Jump("loc_5A35")

    label("loc_5566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5574")
    Jump("loc_5A35")

    label("loc_5574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5582")
    Jump("loc_5A35")

    label("loc_5582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_56B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5642")

    #C0254
    ChrTalk(
        0xFE,
        (
            "やれやれ、遊撃士#6Rブレイサー#ごっこで\x01",
            "妹を魔獣役に仕立てるなんて、\x01",
            "我が子ながらほんと自分本位ねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "……ま、当のプーリーが\x01",
            "楽しそうだからいいとするかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_56AF")

    label("loc_5642")

    OP_93(0xD, 0x56, 0x0)

    #C0256
    ChrTalk(
        0xFE,
        "これ、カミーユ！\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "あんたお兄ちゃんなんだから\x01",
            "あとでプーリーにも\x01",
            "遊撃士役させてやんなさいよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56AF")

    Jump("loc_5A35")

    label("loc_56B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_57DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5753")
    OP_93(0xD, 0x56, 0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0258
    ChrTalk(
        0xD,
        (
            "カミーユ、プーリー！\x01",
            "そろそろお家に入るよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x9,
        "まだ遊ぶー！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xA,
        "遊ぶー！\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xD,
        "……はぁ、やれやれだ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_57D6")

    label("loc_5753")


    #C0262
    ChrTalk(
        0xFE,
        (
            "子供ってのは、ほっとくと\x01",
            "力尽きるまで遊んでるねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "まぁ、その分ご飯を\x01",
            "もりもり食べてくれるから\x01",
            "健康的でいいんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57D6")

    Jump("loc_5A35")

    label("loc_57DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_599E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F7")

    #C0264
    ChrTalk(
        0xFE,
        (
            "旦那は、村から少し離れた畑で\x01",
            "農作業をしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        "今は昼食をとりに家に戻ってるよ。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "……こないだの魔獣被害の件もあるし\x01",
            "あまり遠くへ行って欲しくは\x01",
            "ないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "あれ以来なんだか心配でね。\x01",
            "子供からも目を離さないように\x01",
            "気をつけてるのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5999")

    label("loc_58F7")


    #C0268
    ChrTalk(
        0xFE,
        (
            "こないだの魔獣被害の件もあるし\x01",
            "旦那にも遠くへ行って欲しくは\x01",
            "ないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "あれ以来なんだか心配でね。\x01",
            "子供からも目を離さないように\x01",
            "気をつけてるのさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5999")

    Jump("loc_5A35")

    label("loc_599E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5A35")

    #C0270
    ChrTalk(
        0xFE,
        (
            "この子らはあたしの子供たちさ。\x01",
            "ふふ、かわいいだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "最近あんなことがあったから、\x01",
            "外で遊ばせるのはちょっと\x01",
            "心配なんだけどねぇ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5A35")

    TalkEnd(0xFE)
    Return()

    # Function_18_53AD end

    def Function_19_5A39(): pass

    label("Function_19_5A39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5A4A")
    Jump("loc_5CDF")

    label("loc_5A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A58")
    Jump("loc_5CDF")

    label("loc_5A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5A66")
    Jump("loc_5CDF")

    label("loc_5A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5ADE")

    #C0272
    ChrTalk(
        0xFE,
        (
            "よっと……\x01",
            "そろそろデリックも帰ってくるし\x01",
            "養蜂場の世話も今日までね。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        "はー、やっぱ大変だったわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CDF")

    label("loc_5ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5B74")

    #C0274
    ChrTalk(
        0xFE,
        (
            "村に人が来るのはいいんだけど……\x01",
            "ちょっと視線が気になっちゃうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "物珍しいのは分かるんだけど……\x01",
            "手元が狂っちゃいそうだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CDF")

    label("loc_5B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5C02")

    #C0276
    ChrTalk(
        0xFE,
        (
            "しかし、この村にも随分と\x01",
            "観光客が来たわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "楽しんでくれるのはうれしいけど……\x01",
            "農作業の邪魔にはならないでほしいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CDF")

    label("loc_5C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C90")

    #C0278
    ChrTalk(
        0xFE,
        (
            "デリックが\x01",
            "出店の店番を自ら申し出たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "私は記念祭の間\x01",
            "養蜂場の面倒を任されたってワケ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        "ん、さっそくやりますか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CDF")

    label("loc_5C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5C9E")
    Jump("loc_5CDF")

    label("loc_5C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5CAC")
    Jump("loc_5CDF")

    label("loc_5CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5CBA")
    Jump("loc_5CDF")

    label("loc_5CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_5CC8")
    Jump("loc_5CDF")

    label("loc_5CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_5CD6")
    Jump("loc_5CDF")

    label("loc_5CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5CDF")

    label("loc_5CDF")

    TalkEnd(0xFE)
    Return()

    # Function_19_5A39 end

    def Function_20_5CE3(): pass

    label("Function_20_5CE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5DC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D6D")

    #C0281
    ChrTalk(
        0xFE,
        (
            "……やっぱ、\x01",
            "この村での暮らしも悪かないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "お母さんに引っ越してもいいよって\x01",
            "言ってみようかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5DBB")

    label("loc_5D6D")


    #C0283
    ChrTalk(
        0xFE,
        (
            "同年代はコドモっぽいし、\x01",
            "すごい田舎だけど……\x01",
            "村での暮らしも悪かないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DBB")

    Jump("loc_5F48")

    label("loc_5DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5DCE")
    Jump("loc_5F48")

    label("loc_5DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5E5D")

    #C0284
    ChrTalk(
        0xFE,
        (
            "はぁ、はぁ……\x01",
            "まさか女の子にかけっこで\x01",
            "負けちゃうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "やっぱりこっちで暮らしてると\x01",
            "自然と鍛えられるのかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F48")

    label("loc_5E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E78")
    Call(0, 14)
    Jump("loc_5ECA")

    label("loc_5E78")


    #C0286
    ChrTalk(
        0xFE,
        (
            "（こいつらも、\x01",
            "  悪いヤツじゃないんだよね。\x01",
            "  よく遊びに誘ってくれるし……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ECA")

    Jump("loc_5F48")

    label("loc_5ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5EDD")
    Jump("loc_5F48")

    label("loc_5EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5EEB")
    Jump("loc_5F48")

    label("loc_5EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5EF9")
    Jump("loc_5F48")

    label("loc_5EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5F07")
    Jump("loc_5F48")

    label("loc_5F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F15")
    Jump("loc_5F48")

    label("loc_5F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5F23")
    Jump("loc_5F48")

    label("loc_5F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_5F31")
    Jump("loc_5F48")

    label("loc_5F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_5F3F")
    Jump("loc_5F48")

    label("loc_5F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5F48")

    label("loc_5F48")

    TalkEnd(0xFE)
    Return()

    # Function_20_5CE3 end

    def Function_21_5F4C(): pass

    label("Function_21_5F4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5FC0")

    #C0287
    ChrTalk(
        0xFE,
        (
            "アルモリカ村は\x01",
            "のんびりしていて良いですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "お昼は釣り上げた\x01",
            "カルプとしゃれ込みましょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FC0")

    TalkEnd(0xFE)
    Return()

    # Function_21_5F4C end

    def Function_22_5FC4(): pass

    label("Function_22_5FC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6043")

    #C0289
    ChrTalk(
        0xFE,
        (
            "なるほど、気候の\x01",
            "良さそうな村だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "ここの小川で育った\x01",
            "カルプならさぞかし美味だろう。\x01",
            "今から楽しみだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6043")

    TalkEnd(0xFE)
    Return()

    # Function_22_5FC4 end

    def Function_23_6047(): pass

    label("Function_23_6047")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60DB")
    Jump("loc_6125")

    label("loc_60DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_60FB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6125")

    label("loc_60FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_611B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6125")

    label("loc_611B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6125")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61DE")

    #C0291
    ChrTalk(
        0xFE,
        (
            "アルモリカ古道や\x01",
            "マインツ方面のどこかには\x01",
            "幻の魚がいるって噂っすー。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "ま、気が向いたら\x01",
            "行ってみたらどうすかー？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_626D")

    label("loc_61DE")


    #C0293
    ChrTalk(
        0xFE,
        (
            "アルモリカ古道や\x01",
            "マインツ方面のどこかには\x01",
            "幻の魚がいるって噂っすー。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "まあ『練り団子ＤＸ』でもないと\x01",
            "釣るのは無理じゃないっすかねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_626D")

    Jump("loc_65EF")

    label("loc_6272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_62BE")

    #C0295
    ChrTalk(
        0xFE,
        "………ぼけ～…………\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        "チョウチョ、飛んでるっすねー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_65EF")

    label("loc_62BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6368")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6349")

    #C0297
    ChrTalk(
        0xFE,
        (
            "特級釣師のロイドさん、\x01",
            "リベールに帰っちゃったっすねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "ちぇ～、またつまんなく\x01",
            "なっちまったっすねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6363")

    label("loc_6349")


    #C0299
    ChrTalk(
        0xFE,
        "………ぼけ～…………\x02",
    )

    CloseMessageWindow()

    label("loc_6363")

    Jump("loc_65EF")

    label("loc_6368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_6478")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_640B")

    #C0300
    ChrTalk(
        0x12,
        "あー、いい天気っすねー……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x12,
        (
            "でももうちょい釣ったら\x01",
            "街に帰らないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x12,
        (
            "夕方からは支部長と\x01",
            "夜釣りに出かける予定なんすよねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6473")

    label("loc_640B")


    #C0303
    ChrTalk(
        0x12,
        (
            "ちなみに支部長は\x01",
            "ちょっと変わった人っすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x12,
        (
            "東通りの支部にいるんで\x01",
            "一度会ってみるといいっす。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6473")

    Jump("loc_65EF")

    label("loc_6478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_65EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64AC")
    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A7")
    SetScenarioFlags(0x68, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64A7")

    Jump("loc_65EF")

    label("loc_64AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_657D")

    #C0305
    ChrTalk(
        0x12,
        (
            "アルモリカ村は\x01",
            "近くに釣り場も多いんで、\x01",
            "よく来るんすよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x12,
        "宿酒場も使い勝手がいいっすから。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        "#0000Fはは、常連客なんですね。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x12,
        (
            "そんな感じっすね。\x01",
            "この村、気楽で落ち着くしー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_65EF")

    label("loc_657D")


    #C0309
    ChrTalk(
        0x12,
        (
            "そうそう、東通りには\x01",
            "釣公師団の支部があるっすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x12,
        (
            "ま、東通りに行く機会があったら\x01",
            "寄ってみるといいっす。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65EF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_6047 end

    def Function_24_65F7(): pass

    label("Function_24_65F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6695")

    #C0311
    ChrTalk(
        0xFE,
        (
            "目当ての《アルカンシェル》も\x01",
            "見ることが出来たから、\x01",
            "この村に来てみたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "記念祭が終わるまでは、\x01",
            "この村でのんびりしようかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_66F3")

    label("loc_6695")


    #C0313
    ChrTalk(
        0xFE,
        (
            "《アルカンシェル》も見終わったし……\x01",
            "記念祭が終わるまでは、\x01",
            "この村でのんびりしようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F3")

    TalkEnd(0xFE)
    Return()

    # Function_24_65F7 end

    def Function_25_66F7(): pass

    label("Function_25_66F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6771")

    #C0314
    ChrTalk(
        0xFE,
        "へぇ……のどかなところじゃない。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "クロスベル市の人ごみを見たら\x01",
            "同じ自治州とは思えないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_67E5")

    label("loc_6771")


    #C0316
    ChrTalk(
        0xFE,
        (
            "景色もいいし……\x01",
            "彼についてきて正解だったかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "そこに宿酒場があるわね。\x01",
            "さっそく部屋を借りるとしましょ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67E5")

    TalkEnd(0xFE)
    Return()

    # Function_25_66F7 end

    def Function_26_67E9(): pass

    label("Function_26_67E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68BB")

    #C0318
    ChrTalk(
        0xFE,
        (
            "同じ自治州の中とはいえ、\x01",
            "街とはまるで文化が違うなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "てっきり、導力器をガンガン使って\x01",
            "ハイテク農業でもやってるのかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "ま、変わらないものが\x01",
            "あるのはいいことだと思うがね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_6933")

    label("loc_68BB")


    #C0321
    ChrTalk(
        0xFE,
        (
            "変わらないものがあるのは\x01",
            "いいことだと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "この村までクロスベル市みたいだと\x01",
            "なんだか疲れちゃうだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6933")

    TalkEnd(0xFE)
    Return()

    # Function_26_67E9 end

    def Function_27_6937(): pass

    label("Function_27_6937")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69DC")

    #C0323
    ChrTalk(
        0xFE,
        (
            "川のせせらぎ、小鳥の鳴き声、\x01",
            "美しい自然の風景……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "ここで弁当を食べたら\x01",
            "さぞ美味いことだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        "……なんだか腹が減ってきたよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6A61")

    label("loc_69DC")


    #C0326
    ChrTalk(
        0xFE,
        (
            "ここで弁当を食べたら\x01",
            "さぞ美味いことだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "真っ白な握り飯に塩をふって……\x01",
            "ああ、想像しただけで\x01",
            "よだれがとまらないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A61")

    TalkEnd(0xFE)
    Return()

    # Function_27_6937 end

    def Function_28_6A65(): pass

    label("Function_28_6A65")

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
            "……ぼけ～…………\x01",
            "いい天気っすねー……\x02",
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
            "あ、どうもっす。\x01",
            "皆さんも釣りに来たっすか？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        (
            "#0005Fあ、いえ……自分たちは\x01",
            "クロスベル警察の者です。\x02\x03",

            "#0001F３週間ほど前の魔獣騒ぎについて\x01",
            "聞きこんでる所なんです。\x02\x03",

            "あなたはアルモリカ村の方では\x01",
            "なさそうですけど、\x01",
            "何か心当たりないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x12,
        "あー、その話っすか。\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x12,
        (
            "確かその頃は\x01",
            "パイソンヘッドを追ってたんで、\x01",
            "村には来てないっすねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x12,
        (
            "噂話くらいは\x01",
            "後から聞いたっすけどー。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        (
            "#0103Fそうですか……\x01",
            "それじゃ仕方ないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x12,
        "……お役に立てなくて悪いっす。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x12,
        (
            "にしても、こんな田舎まで\x01",
            "仕事に来るなんて\x01",
            "警察も大変っすねー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0337
    ChrTalk(
        0x12,
        (
            "……そうだ、皆さんも\x01",
            "釣り、するっすか？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x12,
        (
            "せっかくいい天気っすし、\x01",
            "息抜きぐらいしないと損っすよ。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32, 1)
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
            "×１０を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x18B, 10)
    AddItemNumber(0x187, 10)

    #C0341
    ChrTalk(
        0x12,
        (
            "あ、それと\x01",
            "これも渡しておくっす。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x3, 10)
    OP_98(0x12, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)

    #C0343
    ChrTalk(
        0x12,
        (
            "この手帳は釣り人の\x01",
            "お供みたいなものっすねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x12,
        (
            "釣れた魚とかを\x01",
            "書きこんでいくといいっすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#0005Fい、いいんですか？\x01",
            "こんなの貰ってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x12,
        "気にしなくていいっす。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x12,
        (
            "オレの所属してる『釣公師団』は\x01",
            "いちおー釣り文化の普及とか\x01",
            "やってる集まりなんで。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x12,
        (
            "興味ありそうな人には\x01",
            "釣り道具一式を進呈する\x01",
            "慣わしがあるんすよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_70F4")

    #C0349
    ChrTalk(
        0x101,
        (
            "#0003F（前に覗いた事はあるけど……\x01",
            "　そういう活動を\x01",
            "　やってる集まりだったのか。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7120")

    label("loc_70F4")


    #C0350
    ChrTalk(
        0x101,
        "#0003F（そんな集まりがあったのか……）\x02",
    )

    CloseMessageWindow()

    label("loc_7120")


    #C0351
    ChrTalk(
        0x104,
        (
            "#0300Fま、いいんじゃね？\x01",
            "仕事の合間に\x01",
            "リフレッシュできそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        (
            "#0200Fそうですね、その間に\x01",
            "体も休められますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x102,
        "#0100F休息は必要よね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_7273")

    #C0354
    ChrTalk(
        0x101,
        (
            "#0011Fティオとエリィ、\x01",
            "まだ疲れてるんだな。\x02\x03",

            "#0000F……えっと、それじゃあ\x01",
            "有り難く使わせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x12,
        (
            "うっす。\x01",
            "頑張ってくださいっす。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75D3")

    label("loc_7273")


    #C0356
    ChrTalk(
        0x101,
        (
            "#0006Fティオとエリィ、\x01",
            "まだ疲れてるんだな。\x02\x03",

            "#0008F（でも釣りといえば……\x01",
            "  昔、兄貴に教わって以来だな。）\x02\x03",

            "#0003F（兄貴が警察に入ってからは\x01",
            "  全然やらなくなってたけど……\x01",
            "  久し振りに始めてみるかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x12,
        (
            "釣りをするなら、\x01",
            "アルモリカ村の中にも\x01",
            "いい釣りポイントがあるっすよ。\x02",
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
            "そこの桟橋のあたりっす。\x01",
            "今日も魚が集まってるみたいっすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#0000F桟橋のあたりですね。\x01",
            "どうもありがとうございます。\x02",
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
            "※水面に広がっている波紋が\x01",
            "  魚釣りのできる『釣りポイント』です。\x02\x03",

            "※釣りポイントを調べて\x01",
            "  持っている『釣り竿』と『エサ』を選ぶと\x01",
            "  ロイドが魚釣りを始めます。\x02\x03",

            "※！マークが出たときに素早く○ボタンを押すと\x01",
            "  魚を釣り上げることができます。\x01",
            "  （運悪くバラしてしまうこともあります。）\x02\x03",

            "※釣った魚のデータは『釣り手帳』に記録され、\x01",
            "  いつでも閲覧できるようになります。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_75D3")

    SetChrPos(0x0, -2000, 500, 6000, 90)
    OP_93(0x12, 0x5A, 0x0)
    SetChrChipByIndex(0x12, 0xE)
    SetChrSubChip(0x12, 0x0)
    SetScenarioFlags(0x69, 1)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_28_6A65 end

    def Function_29_75FD(): pass

    label("Function_29_75FD")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0361
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76CC")
    OP_E0(0x2)
    MiniGame(0x6, 0x17, 0x300C, 0x0, 0x1478, 0xB4, 0x2A8A, 0xFFFFFA56, 0x4BA)

    label("loc_76CC")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_29_75FD end

    def Function_30_76D1(): pass

    label("Function_30_76D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76E7")
    Call(0, 38)
    Jump("loc_775C")

    label("loc_76E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_76F8")
    Call(0, 6)
    Jump("loc_775C")

    label("loc_76F8")

    TalkBegin(0xFF)
    SetChrName("")

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0364
    ChrTalk(
        0x101,
        (
            "#0003F折角来たんだし、\x01",
            "魔獣について調べてから帰ろう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_775C")

    Return()

    # Function_30_76D1 end

    def Function_31_775D(): pass

    label("Function_31_775D")

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

    def lambda_77FB():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77FB)

    def lambda_7815():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7815)

    def lambda_782F():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_782F)

    def lambda_7849():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7849)
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
            "#11P#0002Fふう……\x01",
            "ここがアルモリカ村か。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_78B1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_78B1)

    def lambda_78BE():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_78BE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    #C0366
    ChrTalk(
        0x101,
        "#0000F#5Pエリィ、ティオ、大丈夫か？\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x102,
        (
            "#0102F#12Pええ……\x01",
            "さっき休ませてもらったし。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    #C0368
    ChrTalk(
        0x103,
        (
            "#0206F#6P……わたしも何とか。\x02\x03",

            "#0202Fそれにしても……\x01",
            "……綺麗な村ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_E5()
    OP_24(0x7B)
    OP_68(15110, 2350, -23260, 2500)

    def lambda_799E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_799E)

    def lambda_79AB():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_79AB)
    Sleep(100)

    def lambda_79BB():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_79BB)
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
            "#0109F#12P花咲き乱れる田園風景……\x01",
            "こんなに綺麗な所だったのね。\x02\x03",

            "#0105Fそれに何だか……\x01",
            "甘い香りがするけれど……\x02\x03",

            "#0102Fもしかして……蜂蜜の香り？\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        (
            "#0300F#6Pだな。\x01",
            "向こうに蜜蜂の巣箱があるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        (
            "#0202F#6Pデータベースによると\x01",
            "アルモリカ村の蜂蜜といえば\x01",
            "特産品の一つみたいですね。\x02\x03",

            "品質も極めて高いため\x01",
            "周辺国にも輸出されているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#0004F#6Pああ、そうみたいだな。\x02\x03",

            "#0000F雑貨屋でもよく売ってるけど\x01",
            "こんな場所で作っていたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x102,
        (
            "#0103F#12P……そうね……\x02\x03",

            "#0108F……知識として知っているのと\x01",
            "実際を知るのとでは大違い、か。\x02",
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

    def lambda_7D61():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D61)
    Sleep(50)

    def lambda_7D71():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7D71)
    Sleep(50)

    def lambda_7D81():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7D81)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0374
    ChrTalk(
        0x101,
        "#0005F#5Pエリィ……？\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        "#0104F#12P……ううん、何でもない。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0376
    ChrTalk(
        0x102,
        (
            "#0101F#12Pそれよりも……\x01",
            "この平和そうな村が\x01",
            "魔獣の被害に遭っているのよね。\x02\x03",

            "ちょっと信じられないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x104,
        (
            "#0306F#5Pまーな。\x01",
            "呑気そうな村に見えるが。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E81():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7E81)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0378
    ChrTalk(
        0x103,
        (
            "#6P#0200F警備隊の調書によれば……\x02\x03",

            "この村の村長から\x01",
            "事情聴取を行ったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EEB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7EEB)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0379
    ChrTalk(
        0x101,
        (
            "#0000F#5Pああ、まずは俺たちも\x01",
            "村長さんから話を聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        (
            "#0100F#12P村長さんの家……\x01",
            "一体どこにあるのかしら？\x02",
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

    # Function_31_775D end

    def Function_32_7FE6(): pass

    label("Function_32_7FE6")

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
            "#11P#0303F『神狼』か……\x02\x03",

            "#0300Fいきなり面白い話に\x01",
            "出くわしちまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#6P#0003Fそうだな……\x02\x03",

            "#0001F本当に『神狼』がいるのか\x01",
            "現時点では分からないけど……\x02\x03",

            "容疑者の候補くらいには\x01",
            "考えてもいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0383
    ChrTalk(
        0x102,
        (
            "#5P#0102Fふふ……貴方らしい言い方ね。\x02\x03",

            "#0103F確かに、足跡が残っていた以上、\x01",
            "狼型魔獣がいたのは事実みたい。\x02\x03",

            "#0101Fそして痕跡一つ残さず、\x01",
            "どこかに消えてしまった……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0384
    ChrTalk(
        0x103,
        (
            "#2P#0203Fおかしいですね……\x02\x03",

            "#0200F村に足跡が残っていたのなら\x01",
            "その跡も辿れそうですけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#6P#0001F確かに、それもそうだな。\x02\x03",

            "#0008F警備隊の追跡調査を\x01",
            "振り切ったということか……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        (
            "#11P#0306Fま、険しい獣道に入られたら\x01",
            "人間にはお手上げだろうしな。\x02\x03",

            "#0300Fあんまり深く考えても\x01",
            "仕方ないんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        (
            "#6P#0003F……そうだな。\x02\x03",

            "#0000Fよし、それじゃあ\x01",
            "さっそく聞き込みを始めよう。\x02\x03",

            "それと昼時だし……\x01",
            "ついでにランチでも取ろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x102,
        (
            "#5P#0104Fふふ、そうね。\x02\x03",

            "#0100F歩き回ったおかげで\x01",
            "お腹が空いちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x103,
        "#2P#0202F……わたしもです。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x104,
        (
            "#11P#0302Fそんじゃま、聞き込みしながら\x01",
            "宿酒場にでも向かいますか。\x02",
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

    # Function_32_7FE6 end

    def Function_33_8549(): pass

    label("Function_33_8549")


    def lambda_854E():
        OP_95(0xFE, -2280, 3500, 51520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_854E)

    def lambda_8568():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8568)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    def lambda_8581():
        OP_95(0xFE, -2230, 3500, 50390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8581)
    WaitChrThread(0x101, 1)

    def lambda_859F():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_859F)
    WaitChrThread(0x101, 1)
    Return()

    # Function_33_8549 end

    def Function_34_85AC(): pass

    label("Function_34_85AC")


    def lambda_85B1():
        OP_95(0xFE, -2350, 3500, 52640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85B1)

    def lambda_85CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_85CB)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)

    def lambda_85E4():
        OP_95(0xFE, -3520, 3500, 51770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85E4)
    WaitChrThread(0x102, 1)

    def lambda_8602():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8602)
    WaitChrThread(0x102, 1)
    Return()

    # Function_34_85AC end

    def Function_35_860F(): pass

    label("Function_35_860F")


    def lambda_8614():
        OP_95(0xFE, -2340, 3500, 53740, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8614)

    def lambda_862E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_862E)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)

    def lambda_8647():
        OP_95(0xFE, -940, 3500, 51820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8647)
    WaitChrThread(0x103, 1)

    def lambda_8665():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8665)
    WaitChrThread(0x103, 1)
    Return()

    # Function_35_860F end

    def Function_36_8672(): pass

    label("Function_36_8672")


    def lambda_8677():
        OP_95(0xFE, -2430, 3500, 54990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8677)

    def lambda_8691():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8691)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)

    def lambda_86AA():
        OP_95(0xFE, -2260, 3500, 53110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_86AA)
    WaitChrThread(0x104, 1)
    Return()

    # Function_36_8672 end

    def Function_37_86C4(): pass

    label("Function_37_86C4")

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
            "#12P#0200F……これで一通り\x01",
            "聞き込みは終わりでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        "#6P#0000Fああ、こんなもんだろう。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x104,
        (
            "#5P#0306Fしかし思ったほど\x01",
            "大した情報は聞けなかったな。\x02\x03",

            "#0301F目撃情報はともかく、\x01",
            "狼の遠吠えでも聞いてるヤツが\x01",
            "いないかと思ったんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x102,
        "#11P#0103Fそうね……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#6P#0006F……うーん。\x02\x03",

            "#0000Fまあいい、とりあえず、\x01",
            "この村で出来る捜査は終了だ。\x02\x03",

            "次は医科大学……\x01",
            "いったん街に戻るとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#11P#0100Fええ、わかったわ。\x02\x03",

            "#0106Fさすがに帰りは\x01",
            "歩いて帰りたくはないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x103,
        (
            "#12P#0206F同感です……\x01",
            "というか面倒くさすぎです。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x104,
        "#5P#0302Fはは、まあ仕方ねぇか。\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        (
            "#6P#0012Fそれじゃあ、バス停で\x01",
            "次の発車時刻を調べてみよう。\x02",
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

    # Function_37_86C4 end

    def Function_38_8A6B(): pass

    label("Function_38_8A6B")

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
        "#0000F#5P次の時刻は……３０分後か。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x104,
        (
            "#0306F#12Pまた微妙に中途半端な時間だな。\x02\x03",

            "#0301F宿酒場に戻って\x01",
            "一杯引っ掛けるのもやりにくいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#0106F#6Pそれ以前に勤務中に\x01",
            "飲酒はどうかと思うけど……\x02",
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

    def lambda_8C91():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C91)
    Sleep(50)

    def lambda_8CA1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CA1)
    Sleep(50)

    def lambda_8CB1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8CB1)
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
        "#0005F#5Pティオ……？\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x102,
        "#0105Fどうかしたの？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    #C0406
    ChrTalk(
        0x103,
        (
            "#0208F#11Pいえ……\x01",
            "何か遠くで聞こえた気がして。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x104,
        "#0301Fふむ……？\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x103,
        (
            "#0203F#11P……すみません。\x01",
            "センサーを最大にしてみます。\x02\x03",

            "#0200F少し静かにしていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        "#0005F#5Pあ、ああ……\x02",
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
            "#0203F#6P……すみません。\x01",
            "気のせいだったみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        (
            "#0001F#5Pいや……\x01",
            "それは別にいいけど。\x02\x03",

            "最初に聞いたっていうのは\x01",
            "一体、どんな音だったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        (
            "#0208F#6Pそれが……\x02\x03",

            "#0201F……何かの\x01",
            "遠吠えだったような気が。\x02",
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
        "#0301F#2Pそいつは……\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        "#0101F#1P例の狼型魔獣……？\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x103,
        (
            "#0206F#6Pいえ……ただの\x01",
            "聞き間違えかもしれません。\x02\x03",

            "センサーの誤動作という\x01",
            "可能性もありますし……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(300)

    #C0416
    ChrTalk(
        0x102,
        (
            "#0101F#6P……どうする？\x01",
            "この付近を捜索してみる？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        (
            "#0003F#5Pそうだな……\x02\x03",

            "#0001Fティオ、そのセンサーの\x01",
            "感知範囲はどのくらいなんだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_91F5():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91F5)
    Sleep(300)

    #C0418
    ChrTalk(
        0x103,
        (
            "#0203F#6Pそうですね……\x02\x03",

            "#0200Fおよそ５０セルジュと\x01",
            "いったところでしょうか。\x02\x03",

            "ただ、音が風に乗っていた場合、\x01",
            "その倍になる時もあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x104,
        (
            "#0305F#2Pヒューッ！\x01",
            "そんなにあんのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x102,
        (
            "#0108F#1Pそうなると、どこから聞こえたか\x01",
            "皆目見当がつかないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        (
            "#0006F#5Pああ……現時点では\x01",
            "気に留めておくしかないだろう。\x02",
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
            "#0208F#6P……あの。\x02\x03",

            "わたしが聞き間違ったって\x01",
            "思わないんですか……？\x02",
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
        "#0005F#5Pへ……\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x102,
        "#0105F#1Pでも、聞こえたんでしょう？\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x103,
        (
            "#0203F#6Pわたしの主観では……そうです。\x02\x03",

            "#0208Fでも、普通の人には聞こえない音が\x01",
            "わたしにだけは聞こえた……\x02\x03",

            "#0201F普通は嘘とか、気のせいだって\x01",
            "考えるものなのでは……？\x02",
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
            "#0306F#2P……と言われてもな。\x02\x03",

            "#0300Fティオすけが凄いってのは\x01",
            "俺たち全員が知ってるしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x103,
        "#0205F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#0102F#1Pふふ、それにあなたが嘘をつく\x01",
            "理由なんてどこにもないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x101,
        (
            "#0004F#5Pまだ短い付き合いだけど……\x01",
            "ティオには何度も助けられている。\x02\x03",

            "#0000F俺たちが疑問に思う余地なんて\x01",
            "これっぽっちも無いと思うけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x103,
        (
            "#0205F#6P……………………………………\x02\x03",

            "#0203F……すみません。\x01",
            "変な事を言い出したみたいです。\x02\x03",

            "#0200F今のは忘れていただけると。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#0002F#5Pあ、ああ？\x01",
            "別に構わないけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    #N0432
    NpcTalk(
        0x18,
        "男性の声",
        "#3Pおや、皆さん……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_978C():

        label("loc_978C")

        TurnDirection(0x101, 0x18, 500)
        Yield()
        Jump("loc_978C")

    QueueWorkItem2(0x101, 1, lambda_978C)

    def lambda_979E():

        label("loc_979E")

        TurnDirection(0x102, 0x18, 500)
        Yield()
        Jump("loc_979E")

    QueueWorkItem2(0x102, 1, lambda_979E)

    def lambda_97B0():

        label("loc_97B0")

        TurnDirection(0x103, 0x18, 500)
        Yield()
        Jump("loc_97B0")

    QueueWorkItem2(0x103, 1, lambda_97B0)

    def lambda_97C2():

        label("loc_97C2")

        TurnDirection(0x104, 0x18, 500)
        Yield()
        Jump("loc_97C2")

    QueueWorkItem2(0x104, 1, lambda_97C2)
    Fade(1000)
    OP_68(1210, 1500, -15280, 0)
    MoveCamera(332, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)

    def lambda_9807():
        OP_95(0xFE, 470, 0, -11600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9807)
    WaitChrThread(0x18, 1)
    OP_0D()

    #C0433
    ChrTalk(
        0x101,
        "#0000Fあ、ハロルドさん。\x02",
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
            "もしかして皆さんも\x01",
            "クロスベル市にお戻りに？\x02",
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
            "#0100F#6Pええ、そうですけど……\x02\x03",

            "ハロルドさんもお帰りですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x18,
        (
            "#3609F#11Pええ、妻と息子への\x01",
            "お土産も確保しましたしね。\x02\x03",

            "#3600Fそうだ、皆さんは\x01",
            "バスをお使いですよね？\x02\x03",

            "次の発車時刻は何時ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x103,
        (
            "#0200F#6P……時刻表によると\x01",
            "３０分後くらいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x104,
        (
            "#0300F#6P一緒にオレたちと\x01",
            "ここでダベって待つかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x18,
        (
            "#3605F#11Pああ、実は……\x02\x03",

            "#3600Fそうだな、５人だったら\x01",
            "ギリギリ大丈夫か……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x5A, 0x190)

    def lambda_9A7D():
        OP_95(0xFE, 5640, 0, -14430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9A7D)

    def lambda_9A97():

        label("loc_9A97")

        TurnDirection(0x101, 0x18, 500)
        Yield()
        Jump("loc_9A97")

    QueueWorkItem2(0x101, 1, lambda_9A97)

    def lambda_9AA9():

        label("loc_9AA9")

        TurnDirection(0x102, 0x18, 500)
        Yield()
        Jump("loc_9AA9")

    QueueWorkItem2(0x102, 1, lambda_9AA9)

    def lambda_9ABB():

        label("loc_9ABB")

        TurnDirection(0x103, 0x18, 500)
        Yield()
        Jump("loc_9ABB")

    QueueWorkItem2(0x103, 1, lambda_9ABB)

    def lambda_9ACD():

        label("loc_9ACD")

        TurnDirection(0x104, 0x18, 500)
        Yield()
        Jump("loc_9ACD")

    QueueWorkItem2(0x104, 1, lambda_9ACD)
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
            "#3609F#11P──皆さん、良かったら\x01",
            "私の車に乗っていきませんか？\x02\x03",

            "#3600Fクロスベル市までお送りしますよ？\x02",
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

    # Function_38_8A6B end

    def Function_39_9C56(): pass

    label("Function_39_9C56")

    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(200)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_39_9C56 end

    def Function_40_9C72(): pass

    label("Function_40_9C72")

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

    # Function_40_9C72 end

    def Function_41_9CB5(): pass

    label("Function_41_9CB5")

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
            "#6P#0000Fアルモリカ村の畑だ。\x01",
            "養蜂箱も設置されているな。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x103,
        (
            "#12P#0200Fクロスベル唯一の農村……\x02\x03",

            "その風景を見せるのは\x01",
            "観光ガイドとして悪くないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x104,
        "#12P#0300Fほーっ、確かにいい景色じゃねぇか。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        (
            "#6P#0100F空気が綺麗だから\x01",
            "遠くまでしっかりと見えるのよね。\x02\x03",

            "クロスベルでも\x01",
            "ここまで美しい遠景を見れるのは\x01",
            "この場所だけかもしれないわ。\x02\x03",

            "農作業をする人がいれば、\x01",
            "もっと映える画になるかもだけど……\x01",
            "そう上手くはいかないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x101,
        (
            "#6P#0000Fでも……\x01",
            "グレイスさんに依頼された写真、\x01",
            "ここならいいものが撮れそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A58B")
    TurnDirection(0x101, 0x102, 500)

    #C0446
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれじゃあエリィ、\x01",
            "撮影をお願いできるかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0447
    ChrTalk(
        0x102,
        (
            "#6P#0108Fえ、ええ。\x01",
            "ちょっと自信はないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x104,
        (
            "#12P#0300Fいやいや、大丈夫だろ。\x02\x03",

            "ちょっとレンズを覗いて\x01",
            "パチリと撮っちまえば\x01",
            "終わりじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0449
    ChrTalk(
        0x102,
        (
            "#6P#0103Fあのねぇ……\x01",
            "いい写真を撮るのは\x01",
            "そんな簡単なことじゃないのよ。\x02\x03",

            "#0100Fフレームの中に\x01",
            "対象物をどう収めるか、\x01",
            "構成を練らなきゃいけないし……\x02\x03",

            "天気や風の影響で\x01",
            "写真の印象もガラリと変わってしまう。\x02\x03",

            "ある一瞬を逃したら\x01",
            "二度と撮れないことだって\x01",
            "あるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x103,
        (
            "#12P#0203F素人とプロの写真を見比べると\x01",
            "一目で違いが分かりますからね。\x02\x03",

            "#0200F粗雑な人には、その繊細さが\x01",
            "理解できないかも知れませんが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0451
    ChrTalk(
        0x104,
        (
            "#12P#0306Fぐっ……\x01",
            "誰のことを言ってんだ、誰の。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x101,
        (
            "#6P#0000Fま、まぁまぁ。\x01",
            "ここはエリィに任せてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x102,
        (
            "#6P#0100Fそれじゃあ……\x01",
            "やってみるわね。\x02",
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
            "#6P#0103F……ふぅ。\x01",
            "念のため何枚か撮っておいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        (
            "#6P#0000Fどうやら撮れたみたいだな。\x02\x03",

            "出来栄えはどんな感じだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x102,
        (
            "#6P#0100F実際に現像してみないと\x01",
            "分からないけど……\x02\x03",

            "少なくとも、\x01",
            "悪い写真ではないとは思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x103,
        (
            "#12P#0200Fエリィさんも\x01",
            "カンを取り戻せたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        (
            "#12P#0300Fふーん……\x01",
            "俺にはさっぱりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#6P#0000Fまたこういう場所を見つけたら\x01",
            "写真に収めていこう。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8D7")

    label("loc_A58B")

    TurnDirection(0x101, 0x102, 500)

    #C0460
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれじゃあ……\x01",
            "エリィ、撮影を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x102,
        "#6P#0100Fええ、分かったわ。\x02",
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
            "#6P#0103F……ふぅ。\x01",
            "こんなところかしら。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_A721")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A721")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_A738")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A738")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_A74F")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A74F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_A766")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_A77D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A77D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_A794")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A794")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_A7AB")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_A7C2")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_A7D9")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A883")

    #C0463
    ChrTalk(
        0x101,
        (
            "#6P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "これでグレイスさんに提示された\x01",
            "５枚ってノルマは達成できた。\x01",
            "これでいつでも提出できそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8D7")

    label("loc_A883")


    #C0464
    ChrTalk(
        0x101,
        (
            "#6P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8D7")

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

    # Function_41_9CB5 end

    def Function_42_A90D(): pass

    label("Function_42_A90D")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9C5")
    SetChrPos(0x109, 8160, 0, -14550, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_A9F0")

    label("loc_A9C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9F0")
    SetChrPos(0x10A, 8160, 0, -14550, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_A9F0")

    OP_0D()

    #C0465
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあの……\x01",
            "エルキンさん、ですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x8,
        "#11Pん？　僕に何か用かい？\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        (
            "#6P#0000Fクロスベル警察のものです。\x01",
            "実は、お話がありまして……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0468
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは延滞本の回収をしている\x01",
            "事情を話した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0469
    ChrTalk(
        0x8,
        "#11Pあ……確かにその本、借りたよ。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x102,
        "#6P#0100F今、持っていますか……？\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        "#11Pええっと実はその……\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x8,
        "#11Pか……貸しちゃったんだよね。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABDC")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_ABDC")

    Sleep(1000)

    #C0473
    ChrTalk(
        0x101,
        "#6P#0005Fウ、ウソだろ……？\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x104,
        (
            "#5P#0306F又又又貸しって……\x01",
            "すげぇことになってんな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC71")

    #C0475
    ChrTalk(
        0x109,
        "#12P#0505F流石に驚きです……\x02",
    )

    CloseMessageWindow()
    Jump("loc_ACA9")

    label("loc_AC71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACA9")

    #C0476
    ChrTalk(
        0x10A,
        "#12P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_ACA9")


    #C0477
    ChrTalk(
        0x102,
        (
            "#6P#0100Fというか……\x01",
            "そこまで借りたい人が多い本って\x01",
            "どんな本なんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x8,
        "#11Pも、申し訳ねぇだぁ！！\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x8,
        (
            "#11Pあんまり熱心に\x01",
            "頼まれるもんだから\x01",
            "ついつい貸しちまっただよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x8,
        (
            "#11Pすぐ返してもらえば\x01",
            "迷惑かからねェと思って……！\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x101,
        (
            "#6P#0005Fお、落ち着いてください！\x01",
            "もう貸してしまったものは\x01",
            "仕方ないですし！\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x103,
        "#6P#0205Fそれで、次はどちらの方に……？\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x8,
        "#11P……コホン。\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        (
            "#11Pえ、えっと……\x01",
            "農家のドナルドさんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x8,
        (
            "#11Pレオール雑貨店の\x01",
            "隣の民家にいるはずさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        (
            "#6P#0006Fふぅ……\x01",
            "仕方ない、回収に行くか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AEE6")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_AEE6")

    SetChrPos(0x0, 7060, 0, -13810, 45)
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    OP_29(0x28, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_42_A90D end

    def Function_43_AF0B(): pass

    label("Function_43_AF0B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF8F")

    #C0487
    ChrTalk(
        0x101,
        (
            "#0005Fおっと、村の人に一通り\x01",
            "聞き込みをしてみないと。\x02\x03",

            "#0000F魔獣について知っている人が\x01",
            "いるかもしれないしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFF8")

    #C0488
    ChrTalk(
        0x101,
        (
            "#0004F……まあ、帰りはバスを使おう。\x02\x03",

            "#0000Fバス停に行けば\x01",
            "次の発車時刻が判るはずだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFF8")

    Sleep(50)
    SetChrPos(0x0, 17090, 0, -25640, 321)
    EventEnd(0x4)
    Return()

    # Function_43_AF0B end

    SaveToFile()

Try(main)
