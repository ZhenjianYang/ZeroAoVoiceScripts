from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t0020.bin",                # FileName
        "t0020",                    # MapName
        "t0020",                    # Location
        0x003A,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 58, 0, 3, 0, 4],
    )

    BuildStringList((
        "t0020",                  # 0
        "雷欧鲁老人",             # 1
        "杰克",                   # 2
        "格方",                   # 3
        "席莉",                   # 4
        "奇斯",                   # 5
        "奇斯",                   # 6
        "阿尔弗雷德",             # 7
        "阿蕾莎",                 # 8
        "阿蕾莎",                 # 9
        "史蒂芬",                 # 10
        "史蒂芬",                 # 11
        "琪露露",                 # 12
        "迪利克",                 # 13
        "克潘",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "游客",                   # 17
        "游客",                   # 18
        "游客",                   # 19
        "哈罗德",                 # 20
        "艾丝蒂尔",               # 21
        "约修亚",                 # 22
        "游击士林",               # 23
        "游击士艾欧莉娅",         # 24
        "游击士斯克特",           # 25
        "亚里欧斯",               # 26
        "游客布拉德",             # 27
        "游客米莉亚",             # 28
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch25200.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch24402.itc",                   # 04
        "chr/ch21002.itc",                   # 05
        "chr/ch22702.itc",                   # 06
        "chr/ch20600.itc",                   # 07
        "chr/ch09300.itc",                   # 08
        "chr/ch20502.itc",                   # 09
        "chr/ch32300.itc",                   # 0A
        "chr/ch33100.itc",                   # 0B
        "chr/ch34300.itc",                   # 0C
        "chr/ch33102.itc",                   # 0D
        "chr/ch34302.itc",                   # 0E
        "chr/ch32200.itc",                   # 0F
        "chr/ch20602.itc",                   # 10
        "chr/ch22700.itc",                   # 11
        "chr/ch23602.itc",                   # 12
        "chr/ch00602.itc",                   # 13
        "chr/ch00700.itc",                   # 14
        "chr/ch32002.itc",                   # 15
        "chr/ch32102.itc",                   # 16
        "chr/ch24400.itc",                   # 17
        "chr/ch26700.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch32400.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-40529,  0,       3470,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-48360,  0,       769,     90,   261,  0x0, 0,   1,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-39,     0,       6039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(699,     0,       2049,    90,   389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-750,    0,       1500,    90,   389,  0x0, 0,   23,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(7849,    180,     2460,    0,    341,  0x0, 0,   4,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-2059,   180,     4000,    0,    341,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(141600,  0,       -2000,   315,  389,  0x0, 0,   17,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(139320,  500,     360,     180,  468,  0x0, 0,   6,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(142940,  0,       -769,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(139320,  300,     360,     180,  469,  0x0, 0,   16,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(3390,    180,     -1909,   57,   469,  0x0, 0,   9,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-41720,  0,       3490,    90,   389,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2539,   180,     1019,    240,  405,  0x0, 0,   18,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(77720,   0,       -990,    45,   389,  0x0, 0,   11,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-5150,   180,     -180,    90,   469,  0x0, 0,   13,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(78529,   0,       -180,    225,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-2700,   180,     1029,    237,  469,  0x0, 0,   14,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-41930,  0,       3480,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(112559,  0,       -509,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(82040,   180,     -1399,   45,   469,  0x0, 0,   19,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(81720,   0,       219,     135,  389,  0x0, 0,   20,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(-5110,   150,     -200,    90,   469,  0x0, 0,   21,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-2630,   150,     1100,    225,  469,  0x0, 0,   22,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(115069,  0,       -2319,   180,  385,  0x0, 0,   24,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(-43650,  0,       -1460,   180,  385,  0x0, 0,   26,  0,   0,   0,   0,   36,  255,  0)

    DeclActor(270,     0,       4460,    1000,    -40,     1500,    6040,    0x007E, 0,  25, 0x0000)
    DeclActor(-46360,  0,       30,      1000,    -48360,  1500,    770,     0x007E, 0,  27, 0x0000)
    DeclActor(6590,    0,       8770,    1000,    6590,    2000,    8770,    0x007C, 0,  34, 0x0000)

    ScpFunction((
        "Function_0_534",          # 00, 0
        "Function_1_5EC",          # 01, 1
        "Function_2_69D",          # 02, 2
        "Function_3_6C8",          # 03, 3
        "Function_4_9BB",          # 04, 4
        "Function_5_A14",          # 05, 5
        "Function_6_163F",         # 06, 6
        "Function_7_174E",         # 07, 7
        "Function_8_19A2",         # 08, 8
        "Function_9_2451",         # 09, 9
        "Function_10_24DA",        # 0A, 10
        "Function_11_3150",        # 0B, 11
        "Function_12_42FC",        # 0C, 12
        "Function_13_4A5A",        # 0D, 13
        "Function_14_4AE0",        # 0E, 14
        "Function_15_5391",        # 0F, 15
        "Function_16_5870",        # 10, 16
        "Function_17_5A15",        # 11, 17
        "Function_18_5B83",        # 12, 18
        "Function_19_5BFE",        # 13, 19
        "Function_20_5D49",        # 14, 20
        "Function_21_5DA6",        # 15, 21
        "Function_22_6183",        # 16, 22
        "Function_23_6277",        # 17, 23
        "Function_24_6595",        # 18, 24
        "Function_25_660D",        # 19, 25
        "Function_26_6611",        # 1A, 26
        "Function_27_7542",        # 1B, 27
        "Function_28_7546",        # 1C, 28
        "Function_29_81FC",        # 1D, 29
        "Function_30_864D",        # 1E, 30
        "Function_31_87EF",        # 1F, 31
        "Function_32_888F",        # 20, 32
        "Function_33_8A99",        # 21, 33
        "Function_34_8C74",        # 22, 34
        "Function_35_8DC1",        # 23, 35
        "Function_36_8EB5",        # 24, 36
        "Function_37_8F71",        # 25, 37
        "Function_38_937D",        # 26, 38
        "Function_39_96B9",        # 27, 39
        "Function_40_AFF8",        # 28, 40
        "Function_41_C111",        # 29, 41
        "Function_42_CB30",        # 2A, 42
    ))


    def Function_0_534(): pass

    label("Function_0_534")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_574"),
        (1, "loc_580"),
        (2, "loc_58C"),
        (3, "loc_598"),
        (4, "loc_5A4"),
        (5, "loc_5B0"),
        (6, "loc_5BC"),
        (SWITCH_DEFAULT, "loc_5C8"),
    )


    label("loc_574")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_580")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_58C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_598")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5EB")

    Return()

    # Function_0_534 end

    def Function_1_5EC(): pass

    label("Function_1_5EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69C")
    OP_95(0xFE, 700, 0, 2050, 2000, 0x0)
    OP_95(0xFE, 6210, 0, 2640, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 2810, 0, 1030, 2000, 0x0)
    OP_95(0xFE, 3120, 0, -560, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -2050, 0, -820, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    Jump("Function_1_5EC")

    label("loc_69C")

    Return()

    # Function_1_5EC end

    def Function_2_69D(): pass

    label("Function_2_69D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C7")
    OP_94(0xFE, 0x229CA, 0xFFFFF754, 0x23212, 0xFFFFFF9C, 0x3E8)
    Sleep(250)
    Jump("Function_2_69D")

    label("loc_6C7")

    Return()

    # Function_2_69D end

    def Function_3_6C8(): pass

    label("Function_3_6C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E0")
    Event(0, 40)

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6FE")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    Jump("loc_9A2")

    label("loc_6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_721")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    Jump("loc_9A2")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_766")
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -41720, 0, 3490, 90)
    OP_93(0x8, 0x10E, 0x0)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_9A2")

    label("loc_766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_783")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_9A2")

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_84C")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    OP_93(0x8, 0x10E, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D5")
    SetChrPos(0x17, 84000, 180, -2040, 283)
    SetChrPos(0x19, 82190, 180, -1670, 103)
    Jump("loc_847")

    label("loc_7D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_811")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, 750, 0, 1500, 270)
    Jump("loc_847")

    label("loc_811")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_847")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrPos(0xA, 0, 0, 3700, 360)
    SetChrFlags(0xA, 0x10)

    label("loc_847")

    Jump("loc_9A2")

    label("loc_84C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_864")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_9A2")

    label("loc_864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_87C")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_9A2")

    label("loc_87C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8B1")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0x14, 0x80)
    OP_93(0x8, 0x10E, 0x0)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    Jump("loc_9A2")

    label("loc_8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8EA")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2350, 0, -720, 135)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_9A2")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_913")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    Jump("loc_9A2")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_946")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    Jump("loc_9A2")

    label("loc_946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_974")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    ClearChrFlags(0x1B, 0x80)
    Jump("loc_9A2")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9A2")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BA")
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)

    label("loc_9BA")

    Return()

    # Function_3_6C8 end

    def Function_4_9BB(): pass

    label("Function_4_9BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9D3")
    SetMapObjFrame(0xFF, "tuika00", 0x0, 0x1)

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A13")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9ED")
    Jump("loc_A13")

    label("loc_9ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_A03")
    OP_65(0x0, 0x1)
    Jump("loc_A13")

    label("loc_A03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_A13")
    OP_65(0x0, 0x1)

    label("loc_A13")

    Return()

    # Function_4_9BB end

    def Function_5_A14(): pass

    label("Function_5_A14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD8")

    #C0001
    ChrTalk(
        0xFE,
        (
            "这个杂货店的历史很悠久，\x01",
            "是从我曾祖父的时代开始\x01",
            "世代相传的老店。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "可是，杰克那家伙\x01",
            "一点也不明白其中的可贵之处。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "真希望他在工作的时候\x01",
            "能多带点自豪感啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B39")

    label("loc_AD8")


    #C0004
    ChrTalk(
        0xFE,
        (
            "希望杰克\x01",
            "在工作的时候\x01",
            "能再多带点自豪感啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "这家店要变成『杰克杂货店』\x01",
            "得等到几时呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B39")

    Jump("loc_163B")

    label("loc_B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF1")

    #C0006
    ChrTalk(
        0xFE,
        (
            "因为杰克工作太懒散，\x01",
            "我训了他一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "他偶尔也会胡说些\x01",
            "『要进城做一番大事业』之类的梦话……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "有那种闲工夫的话，\x01",
            "还不如多学点\x01",
            "店里的手艺呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C67")

    label("loc_BF1")


    #C0009
    ChrTalk(
        0xFE,
        (
            "杰克那家伙，偶尔会\x01",
            "胡说些『要进城做一番大事业』\x01",
            "之类的梦话……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "有那闲工夫的话，\x01",
            "还不如多学点\x01",
            "店里的手艺呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C67")

    Jump("loc_163B")

    label("loc_C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D25")
    OP_4B(0x1B, 0xFF)
    TurnDirection(0xFE, 0x1B, 0)

    #C0011
    ChrTalk(
        0xFE,
        (
            "每次都承蒙\x01",
            "你的照顾呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "来，今天就额外\x01",
            "多送你一瓶蜂蜜，\x01",
            "和家人一起吃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x1B,
        (
            "#3609F呵呵……感激不尽，\x01",
            "我的太太和孩子都会很开心的。 \x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_D9B")

    label("loc_D25")


    #C0014
    ChrTalk(
        0xFE,
        (
            "和哈罗德相比，\x01",
            "我家的杰克可真是……\x01",
            "始终都成不了气候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "既然撑过了纪念庆典，\x01",
            "希望他能多少赶上\x01",
            "哈罗德一些。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9B")

    Jump("loc_163B")

    label("loc_DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E23")

    #C0016
    ChrTalk(
        0xFE,
        (
            "游客一回克洛斯贝尔市，\x01",
            "这里马上就冷清下来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "……杰克似乎在偷懒啊。\x01",
            "好，我去呵斥他一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E68")

    label("loc_E23")


    #C0018
    ChrTalk(
        0xFE,
        (
            "站柜台的人\x01",
            "怎么可以那么无精打采呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "好，我去呵斥他一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_E68")

    Jump("loc_163B")

    label("loc_E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_EEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E88")
    Call(0, 7)
    Jump("loc_EE6")

    label("loc_E88")


    #C0020
    ChrTalk(
        0xFE,
        "呵呵，生意真是近年少有的红火啊。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "去年的纪念庆典\x01",
            "可没有这么好的生意呢，\x01",
            "真是难得啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE6")

    Jump("loc_163B")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_F53")

    #C0022
    ChrTalk(
        0xFE,
        (
            "呵呵呵，游客们\x01",
            "买了很多蜂蜜\x01",
            "当土特产呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "真是太好了，\x01",
            "还好采用了\x01",
            "迪利克的点子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_163B")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_104C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDA")

    #C0024
    ChrTalk(
        0xFE,
        (
            "在纪念庆典开露天店，\x01",
            "第一天的销量\x01",
            "相当不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "多亏『彩虹』剧团\x01",
            "帮我们吸引了这么多客人。\x01",
            "呵呵呵。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1047")

    label("loc_FDA")


    #C0026
    ChrTalk(
        0xFE,
        (
            "多亏『彩虹』剧团\x01",
            "帮我们吸引了这么多客人，\x01",
            "露天店的销量十分不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "希望能这样一直\x01",
            "保持到最终日……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1047")

    Jump("loc_163B")

    label("loc_104C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1067")
    Call(0, 7)
    Jump("loc_10DE")

    label("loc_1067")


    #C0028
    ChrTalk(
        0xFE,
        (
            "迪利克那家伙，\x01",
            "还挺能干的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "似乎已经有继任\x01",
            "下任村长的自觉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "……真希望杰克\x01",
            "也能有继承家业的自觉啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DE")

    Jump("loc_163B")

    label("loc_10E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_11C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1189")

    #C0031
    ChrTalk(
        0xFE,
        (
            "迪利克那家伙提出的『在创立纪念庆典\x01",
            "开设露天店铺』，可真是个不错的点子。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "我们村子已经渐渐\x01",
            "失去了往日的活力，\x01",
            "那样做说不定很不错。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11C4")

    label("loc_1189")


    #C0033
    ChrTalk(
        0xFE,
        (
            "为了让村子恢复活力，\x01",
            "我很乐意去创立纪念庆典开露天店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C4")

    Jump("loc_163B")

    label("loc_11C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_12D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126C")

    #C0034
    ChrTalk(
        0xFE,
        (
            "唔，今天到后面的农场\x01",
            "去进一点蜂蜜吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "其实我也想\x01",
            "教杰克一点\x01",
            "进货的基础……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "不过现在看店都已经够忙了。\x01",
            "下次有机会再说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12D0")

    label("loc_126C")


    #C0037
    ChrTalk(
        0xFE,
        (
            "既然要卖东西，\x01",
            "进货也必须做好才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "虽然我也很想把这些知识教给杰克……\x01",
            "不过还为时过早吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D0")

    Jump("loc_163B")

    label("loc_12D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_13B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F0")
    Call(0, 6)
    Jump("loc_13AD")

    label("loc_12F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1361")

    #C0039
    ChrTalk(
        0xFE,
        (
            "我想早点让孙子继承店铺，\x01",
            "然后退休呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "但杰克那小子\x01",
            "学什么都学不会……\x01",
            "真是伤脑筋啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13AD")

    label("loc_1361")


    #C0041
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "有个不中用的孙子可真让人头疼。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "我也差不多\x01",
            "想退休了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AD")

    Jump("loc_163B")

    label("loc_13B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_157D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CF")

    #C0043
    ChrTalk(
        0xFE,
        (
            "因为那起狼形魔兽事件，搞得养蜂场乱七八糟的。\x01",
            "虽然我们店的受害情况还不算严重，\x01",
            "但多少还是受了点损失。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "……仔细想想的话，还真奇怪啊。\x01",
            "如果是魔兽干的，\x01",
            "应该会破坏得更彻底吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "嗯，大概是运气好吧。\x01",
            "对空之女神不胜感谢啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C7")
    SetScenarioFlags(0x68, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14C7")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1578")

    label("loc_14CF")


    #C0046
    ChrTalk(
        0xFE,
        (
            "说起来，在遭遇了狼形魔兽的侵害，\x01",
            "情况最为窘困的时候，哈罗德他\x01",
            "特意出高价进了我的货呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "做生意，最讲究的就是诚信与人品。\x01",
            "他还那么年轻，就已经是个很出色的人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1578")

    Jump("loc_163B")

    label("loc_157D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_163B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D5")

    #C0048
    ChrTalk(
        0xFE,
        "唔，有客人吗？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "推荐村里的特产蜂蜜哦，\x01",
            "多买几瓶吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_163B")

    label("loc_15D5")


    #C0050
    ChrTalk(
        0xFE,
        (
            "……哦，失礼。\x01",
            "买东西的话，请去柜台那边吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "虽然是个不中用的孙子在站柜台，\x01",
            "但还请多多捧场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163B")

    TalkEnd(0xFE)
    Return()

    # Function_5_A14 end

    def Function_6_163F(): pass

    label("Function_6_163F")


    #C0052
    ChrTalk(
        0xFE,
        (
            "哦，客人……\x01",
            "冒昧地问一句，您要不要书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "这是哈罗德在进货的时候\x01",
            "顺便送给我的……\x01",
            "但很不巧，我并没有读书的习惯呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "比起留在不看的人手中，\x01",
            "转送给爱看书的人，\x01",
            "这本书也会比较幸福吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2C7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C7, 1)
    SetScenarioFlags(0x9C, 1)
    Return()

    # Function_6_163F end

    def Function_7_174E(): pass

    label("Function_7_174E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_175C")
    Jump("loc_199E")

    label("loc_175C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_176A")
    Jump("loc_199E")

    label("loc_176A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1778")
    Jump("loc_199E")

    label("loc_1778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1786")
    Jump("loc_199E")

    label("loc_1786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1826")
    OP_4B(0x8, 0xFF)
    OP_4B(0x1A, 0xFF)
    TurnDirection(0x8, 0x1A, 0)
    TurnDirection(0x1A, 0x8, 0)

    #C0056
    ChrTalk(
        0x1A,
        (
            "我想带给共和国的家人\x01",
            "当礼物。\x01",
            "能不能给我打包三瓶？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "嗯嗯，\x01",
            "那真是不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "那么，付款\x01",
            "请到那边的柜台。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x1A, 0xFF)
    Jump("loc_199E")

    label("loc_1826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1834")
    Jump("loc_199E")

    label("loc_1834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1842")
    Jump("loc_199E")

    label("loc_1842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_195D")
    OP_4B(0x8, 0xFF)
    OP_4B(0x14, 0xFF)
    TurnDirection(0x8, 0x14, 0)
    TurnDirection(0x14, 0x8, 0)

    #C0059
    ChrTalk(
        0x14,
        (
            "唔……\x01",
            "这样的话，开设露天店用的商品\x01",
            "应该就足够了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "今年遭受了魔兽的灾害，\x01",
            "但收获量还算过得去嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "不过还要安排销售员，\x01",
            "以及其它的商品和露天店地点……\x01",
            "要考虑的事还多得是呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x14,
        (
            "我明白，\x01",
            "稍后慢慢决定吧。\x01",
            "那么，接下来是……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x14, 0xFF)
    Jump("loc_199E")

    label("loc_195D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_196B")
    Jump("loc_199E")

    label("loc_196B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1979")
    Jump("loc_199E")

    label("loc_1979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_1987")
    Jump("loc_199E")

    label("loc_1987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_1995")
    Jump("loc_199E")

    label("loc_1995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_199E")

    label("loc_199E")

    SetScenarioFlags(0x0, 0)
    Return()

    # Function_7_174E end

    def Function_8_19A2(): pass

    label("Function_8_19A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B18")

    #C0063
    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "嗯～……今天的客人\x01",
            "也只有常客啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "我说，你们几位，\x01",
            "要不要试试\x01",
            "『整个菜单从上到下全来一份』……？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#0006F呃～这就免了吧，\x01",
            "我们也吃不了那么多……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "嘁。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B10")

    #C0068
    ChrTalk(
        0x10A,
        (
            "#0601F（这是什么服务态度……\x01",
            "  就这样也能当餐厅的店员吗！？）\x02\x03",

            "#0603F（哼，还是让我\x01",
            "  亲自指导一下……）\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#0106F（请、请冷静一点啦。）\x02",
    )

    CloseMessageWindow()

    label("loc_1B10")

    SetScenarioFlags(0x0, 1)
    Jump("loc_1B86")

    label("loc_1B18")


    #C0070
    ChrTalk(
        0xFE,
        (
            "客人，听好了哦，\x01",
            "做人不豪放一点的话，可是不受欢迎的哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "你们干脆就狂点一大堆，\x01",
            "给我们补贴点家计吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B86")

    Jump("loc_244D")

    label("loc_1B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1CC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C56")

    #C0072
    ChrTalk(
        0xFE,
        (
            "父亲总认为悠闲地经营一家小店就好了，\x01",
            "但我可不喜欢贫穷的生活。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "……唉，迪利克先生能不能\x01",
            "再想点什么计划呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "说来说去，\x01",
            "最近赚得最多的生意\x01",
            "还是纪念庆典的露天店啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CC1")

    label("loc_1C56")


    #C0075
    ChrTalk(
        0xFE,
        (
            "纪念庆典真好啊。\x01",
            "虽然很忙，但真是没少赚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "迪利克先生\x01",
            "想推进村子改革的心情，\x01",
            "我似乎也能理解了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC1")

    Jump("loc_244D")

    label("loc_1CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1DA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6E")

    #C0077
    ChrTalk(
        0xFE,
        (
            "现在，二楼房间里\x01",
            "住进了两位游击士。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "这样看来，游击士中好像\x01",
            "还有不少女性呢，有点意外。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "同为女性，\x01",
            "不由得就想为她们加油鼓气呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DA0")

    label("loc_1D6E")


    #C0080
    ChrTalk(
        0xFE,
        (
            "稍后去给那两位游击士\x01",
            "附送一杯\x01",
            "餐后的咖啡吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA0")

    Jump("loc_244D")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1DB3")
    Jump("loc_244D")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1DC1")
    Jump("loc_244D")

    label("loc_1DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DCF")
    Jump("loc_244D")

    label("loc_1DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DDD")
    Jump("loc_244D")

    label("loc_1DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDC")
    OP_4B(0xA, 0xFF)

    #C0081
    ChrTalk(
        0xFE,
        (
            "创立纪念庆典啊～……\x01",
            "热热闹闹得应该会很开心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "要是能顺利吸引到客人，\x01",
            "说不定还能赚很多钱。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "呜呜，但是要变得更忙碌了。\x01",
            "我都习惯这种没生意的日子了，\x01",
            "真不想那么辛苦……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0084
    ChrTalk(
        0xA,
        "……喂，我听到啦。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F3F")

    label("loc_1EDC")


    #C0085
    ChrTalk(
        0xFE,
        (
            "如果一直生意好的话，\x01",
            "就算忙起来也不怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "不过，估计也不会有\x01",
            "那么多客人来啦。\x01",
            "……大概吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3F")

    Jump("loc_244D")

    label("loc_1F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_20A1")
    TurnDirection(0xFE, 0x13, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2020")
    OP_4B(0xA, 0xFF)

    #C0087
    ChrTalk(
        0xFE,
        (
            "哦～是特地从克洛斯贝尔市\x01",
            "走过来的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "好啦，不介意的话，就多吃点吧。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "我老爸虽然看起来没精打采的，\x01",
            "不过做的料理可是很美味哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0090
    ChrTalk(
        0xA,
        "……喂，我听到啦。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_209C")

    label("loc_2020")


    #C0091
    ChrTalk(
        0xFE,
        (
            "要不要尝尝\x01",
            "我们店里\x01",
            "最贵的菜啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "是老爸的得意之作，\x01",
            "很好吃的哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x13,
        (
            "……虽然很吸引人，不过还是算了。\x01",
            "我没钱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_209C")

    Jump("loc_244D")

    label("loc_20A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2137")

    #C0094
    ChrTalk(
        0xFE,
        (
            "常客阿尔弗雷德先生\x01",
            "和老爸的关系很好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "常常趁着店里不忙的时候，\x01",
            "过来聊天呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "这也是自家营业\x01",
            "的特有优点吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_218B")

    label("loc_2137")


    #C0097
    ChrTalk(
        0xFE,
        (
            "阿尔弗雷德先生\x01",
            "似乎和老爸很要好。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "……说实话，我觉得\x01",
            "应该多干活少说话的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218B")

    Jump("loc_244D")

    label("loc_2190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_227E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2206")

    #C0099
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "阿尔弗雷德先生和奇斯\x01",
            "坐得还真久啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "既然要坐，\x01",
            "就不能多点些东西吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2279")

    label("loc_2206")


    #C0101
    ChrTalk(
        0xFE,
        (
            "白天基本没什么客人，\x01",
            "干坐着其实\x01",
            "也无所谓……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "不过既然要坐，还是希望他们能点些东西啊。\x01",
            "这样可赚不了钱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2279")

    Jump("loc_244D")

    label("loc_227E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_2377")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2324")

    #C0103
    ChrTalk(
        0xFE,
        (
            "哈罗德先生\x01",
            "说快要回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "你不觉得哈罗德先生很帅吗？\x01",
            "为人诚实，表里如一。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "竟然都结婚了，而且还有孩子，\x01",
            "真是羡慕他的太太啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2372")

    label("loc_2324")


    #C0106
    ChrTalk(
        0xFE,
        (
            "想找哈罗德先生吗，\x01",
            "他回二楼的房间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "他什么时候才会再来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2372")

    Jump("loc_244D")

    label("loc_2377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_244D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E9")

    #C0108
    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "……哎呀，是第一次来的客人吧？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "现在正好比较闲。\x01",
            "请慢慢坐哦⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_244D")

    label("loc_23E9")


    #C0111
    ChrTalk(
        0xFE,
        (
            "我老爸的料理可是绝品哦。\x01",
            "有兴趣的话就点些尝尝吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "而且吃点东西也能恢复体力，\x01",
            "有益无害哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_244D")

    TalkEnd(0xFE)
    Return()

    # Function_8_19A2 end

    def Function_9_2451(): pass

    label("Function_9_2451")

    TalkBegin(0xFE)

    #C0113
    ChrTalk(
        0xC,
        (
            "事情变得\x01",
            "麻烦起来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xC,
        (
            "本想让老板\x01",
            "看看我的本事，\x01",
            "但还是太急躁了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "不过，不仅是警察，\x01",
            "连游击士也在，我就放心了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_2451 end

    def Function_10_24DA(): pass

    label("Function_10_24DA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_256E")
    Jump("loc_25B8")

    label("loc_256E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_258E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25B8")

    label("loc_258E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25AE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25B8")

    label("loc_25AE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25B8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_271B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26DA")

    #C0116
    ChrTalk(
        0xFE,
        (
            "席莉的魅力\x01",
            "就是不会刻意装可爱吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "总是让我们这些常客\x01",
            "点贵的东西，\x01",
            "坦率就是优点啊！\x02",
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

    #C0118
    ChrTalk(
        0x103,
        "#0211F您这喜好有点特殊呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2716")

    label("loc_26DA")


    #C0119
    ChrTalk(
        0xFE,
        (
            "席莉的魅力\x01",
            "就在于不会刻意装可爱，\x01",
            "而是坦率地表现自己。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2716")

    Jump("loc_3148")

    label("loc_271B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2796")

    #C0120
    ChrTalk(
        0xFE,
        (
            "只点杯咖啡就坐着不走的话，\x01",
            "可是会被席莉\x01",
            "用掸子打的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "她可是最喜欢米拉了……\x01",
            "没办法，点些小吃吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3148")

    label("loc_2796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_288D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285A")

    #C0122
    ChrTalk(
        0xFE,
        (
            "呼～……\x01",
            "有席莉在的店\x01",
            "真是很治愈啊～……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间见不到她的寂寞，\x01",
            "可要好好治愈一下才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#0006F……纪念庆典都已经过去\x01",
            "一个月了……\x01",
            "还没治愈好吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2888")

    label("loc_285A")


    #C0125
    ChrTalk(
        0xFE,
        (
            "呼～……\x01",
            "有席莉在的店\x01",
            "真是很治愈啊～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2888")

    Jump("loc_3148")

    label("loc_288D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_296A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290A")

    #C0126
    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "唉……要死了。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "……我要振作一点。\x01",
            "撑到明天，席莉\x01",
            "就会回来了……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2965")

    label("loc_290A")


    #C0129
    ChrTalk(
        0xFE,
        (
            "五天都见不到席莉，\x01",
            "真是意料之外……\x01",
            "但也只到今天为止了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "快点回来吧～\x01",
            "席莉～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2965")

    Jump("loc_3148")

    label("loc_296A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2ADA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A15")

    #C0131
    ChrTalk(
        0xD,
        (
            "呼，那对情侣能\x01",
            "平安回来，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xD,
        (
            "在席莉去克洛斯贝尔市的这段期间，\x01",
            "店里的客人要是出了什么事，\x01",
            "她一定会很伤心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        "……大概吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AD5")

    label("loc_2A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A89")

    #C0134
    ChrTalk(
        0xFE,
        (
            "只有老板，阿尔弗雷德先生，\x01",
            "还有陌生游客们的店……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "要说不足的话，那就是……\x01",
            "没有席莉啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2AD5")

    label("loc_2A89")


    #C0136
    ChrTalk(
        0xFE,
        (
            "虽然我明知道\x01",
            "席莉不在，\x01",
            "却还是来了这家店……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "……唉……好空虚啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2AD5")

    Jump("loc_3148")

    label("loc_2ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4E")

    #C0138
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "虽然早就知道……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "席莉不在店里……\x01",
            "但是没想到，这里竟会\x01",
            "变得如此寂廖……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B8C")

    label("loc_2B4E")


    #C0140
    ChrTalk(
        0xFE,
        (
            "啊，席莉……\x01",
            "纪念庆典什么的赶快结束吧，\x01",
            "你快回来吧～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8C")

    Jump("loc_3148")

    label("loc_2B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2C1E")

    #C0141
    ChrTalk(
        0xFE,
        (
            "没、没想到席莉\x01",
            "竟然会去开露天店……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "而且还和迪利克那小子\x01",
            "两人一起！\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "可恶，要不是工作忙的话，\x01",
            "我马上就去捧场了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3148")

    label("loc_2C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA1")

    #C0144
    ChrTalk(
        0xFE,
        (
            "呼～有游客来的话，\x01",
            "这家店一定也会很拥挤吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "要是大家都被席莉的魅力\x01",
            "迷住了，可该怎么办啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CFA")

    label("loc_2CA1")


    #C0146
    ChrTalk(
        0xFE,
        (
            "这家店要是有新客人来的话，\x01",
            "一定会迷上席莉的……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "……游客什么的，还是别来的好。\x02",
    )

    CloseMessageWindow()

    label("loc_2CFA")

    Jump("loc_3148")

    label("loc_2CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2E3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DBD")

    #C0148
    ChrTalk(
        0xFE,
        (
            "席莉……\x01",
            "好像对哈罗德先生\x01",
            "很有好感似的。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "可恶，怎么能让已婚的好男人\x01",
            "抢走席莉呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "……虽然想这么说，\x01",
            "但哈罗德先生对我也很好，\x01",
            "我不能说他的坏话～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E39")

    label("loc_2DBD")


    #C0151
    ChrTalk(
        0xFE,
        (
            "总、总之，现在也\x01",
            "只能每天来这里坐坐，\x01",
            "努力和席莉拉近距离。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "可是啊～……\x01",
            "情敌竟然是哈罗德先生，\x01",
            "对手也太强大了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E39")

    Jump("loc_3148")

    label("loc_2E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC2")

    #C0153
    ChrTalk(
        0xFE,
        (
            "啊～席莉今天\x01",
            "也好可爱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "……啊？狼形魔兽？\x01",
            "谁管那种事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "能不能不要打扰\x01",
            "我的幸福时光？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F1B")

    label("loc_2EC2")


    #C0156
    ChrTalk(
        0xFE,
        (
            "啊～席莉今天\x01",
            "也好可爱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "即使这个村子毁灭了，\x01",
            "只要还有席莉在，\x01",
            "我就能活下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F1B")

    Jump("loc_3148")

    label("loc_2F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_300B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FAA")

    #C0158
    ChrTalk(
        0xFE,
        (
            "有席莉在，\x01",
            "还有老板的美味料理……\x01",
            "这家店果然是最棒的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "……虽然我来的次数太多，\x01",
            "钱都快花光了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3006")

    label("loc_2FAA")


    #C0160
    ChrTalk(
        0xFE,
        (
            "从刚才开始，\x01",
            "席莉的视线就好锐利啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……没办法，再点些东西吧。\x01",
            "这个月很严峻啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3006")

    Jump("loc_3148")

    label("loc_300B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_3115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30BA")

    #C0162
    ChrTalk(
        0xFE,
        (
            "嗯～？\x01",
            "狼形魔兽的事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "我管理的田地\x01",
            "也遭到了一定的破坏。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "而且竟然没人见到其踪影，\x01",
            "看来那魔兽相当聪明吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B2")
    SetScenarioFlags(0x68, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30B2")

    SetScenarioFlags(0x0, 2)
    Jump("loc_3110")

    label("loc_30BA")


    #C0165
    ChrTalk(
        0xFE,
        (
            "我管理的田地\x01",
            "也遭到了一定的破坏。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "要恢复的话，可得花不少时间啊。\x01",
            "哎呀呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3110")

    Jump("loc_3148")

    label("loc_3115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3148")

    #C0167
    ChrTalk(
        0xFE,
        "席莉真的好可爱啊。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "笑容迷死人！\x02",
    )

    CloseMessageWindow()

    label("loc_3148")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_24DA end

    def Function_11_3150(): pass

    label("Function_11_3150")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31E4")
    Jump("loc_322E")

    label("loc_31E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3204")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322E")

    label("loc_3204")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3224")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_322E")

    label("loc_3224")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_322E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3307")

    #C0169
    ChrTalk(
        0xFE,
        (
            "唔唔，没想到那本书几经辗转，\x01",
            "最后到了那种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "哎呀，一切的起因\x01",
            "都是我转借给了别人啊。\x01",
            "真是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "下次我会注意\x01",
            "遵守还书期限的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3307")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3393")

    #C0172
    ChrTalk(
        0xFE,
        (
            "格方把书借给了\x01",
            "经常待在村子入口处\x01",
            "摆弄导力车的艾尔琴。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "呀，真是不好意思啊。\x01",
            "给你们添麻烦了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33B4")
    Call(0, 42)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_33B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_34DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3480")
    OP_4B(0xA, 0xFF)

    #C0174
    ChrTalk(
        0xFE,
        (
            "《牌技师杰克》……\x01",
            "这书很有意思呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0175
    ChrTalk(
        0xA,
        "哦哦，你已经看完了吗？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xA,
        (
            "我也是这部小说的书迷，\x01",
            "店里打烊之后，\x01",
            "可以好好聊聊了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        "嗯，这可值得期待了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_34D8")

    label("loc_3480")


    #C0178
    ChrTalk(
        0xFE,
        (
            "好，再从头开始\x01",
            "重新看一遍吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "哎呀呀，还借了其它的书呢，\x01",
            "看来都没时间看了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D8")

    Jump("loc_42F4")

    label("loc_34DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_360D")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0180
    ChrTalk(
        0xFE,
        (
            "《牌技师杰克》……\x01",
            "这书很有意思呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0181
    ChrTalk(
        0xA,
        (
            "那本书我也知道哦。\x01",
            "我记得结局是杰克他──\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "喂，这习惯可不好哦，格方。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "竟然想把故事的结局说出来，\x01",
            "不解风情也要有个限度吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "真是的，我都不知道\x01",
            "被你害过多少次了……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "抱、抱歉，\x01",
            "我不说话了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3680")

    label("loc_360D")


    #C0186
    ChrTalk(
        0xFE,
        (
            "没有比把故事的结局\x01",
            "或核心剧情告诉别人\x01",
            "更让人不快的事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "就算是好朋友格方，\x01",
            "也希望他能在这方面克制一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3680")

    Jump("loc_42F4")

    label("loc_3685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_371E")

    #C0188
    ChrTalk(
        0xFE,
        (
            "我从克洛斯贝尔市的图书馆\x01",
            "借来了很多书呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "那里有很多不错的书，\x01",
            "忍不住就借了一大堆。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "离还书期限还有三天，\x01",
            "不知能不能看完……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F4")

    label("loc_371E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_37D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3786")

    #C0191
    ChrTalk(
        0xFE,
        (
            "店里也安静下来了，\x01",
            "借来的书\x01",
            "也看完了……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "今天就悠闲地\x01",
            "吃点东西吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37CD")

    label("loc_3786")


    #C0193
    ChrTalk(
        0xFE,
        "还书……明天再去就好了吧。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市今天\x01",
            "好像很拥挤呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37CD")

    Jump("loc_42F4")

    label("loc_37D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_39CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_384D")

    #C0195
    ChrTalk(
        0xE,
        (
            "呼……\x01",
            "总算能松口气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xE,
        (
            "哎呀呀，格方那个可恶的家伙。\x01",
            "就算是朋友，\x01",
            "也不要这样使唤人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C5")

    label("loc_384D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3959")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0197
    ChrTalk(
        0xFE,
        "唔……唔唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0198
    ChrTalk(
        0xA,
        (
            "阿尔弗雷德，还在看吗……\x01",
            "《彩虹·FanBook》。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        "这书有那么好看吗？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "因为这书很稀有，\x01",
            "所以想在返还之前\x01",
            "好好欣赏欣赏。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "话说，\x01",
            "这张伊莉娅·普拉提耶\x01",
            "的照片可真不错啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xA,
        "……适可而止啊。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_39C5")

    label("loc_3959")


    #C0203
    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "似乎是倍受期待的新星\x01",
            "『莉夏·毛』入团以前的书呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "本来也想看看\x01",
            "她的照片……\x01",
            "真是遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C5")

    Jump("loc_42F4")

    label("loc_39CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ACD")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0205
    ChrTalk(
        0xFE,
        (
            "《彩虹·FanBook》……\x01",
            "找到了一本很稀有的书呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0206
    ChrTalk(
        0xA,
        (
            "哦……\x01",
            "竟然还出版过这种书啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "似乎是狂热的崇拜者们\x01",
            "自发制作出版的图书，\x01",
            "发行数量好像很少。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "……我都有点舍不得\x01",
            "还给图书馆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xA,
        "喂喂……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B2D")

    label("loc_3ACD")


    #C0210
    ChrTalk(
        0xFE,
        (
            "听说这是本很受欢迎的书，\x01",
            "也不知道还能不能再借到。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "没办法，\x01",
            "只好趁现在认真欣赏欣赏了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2D")

    Jump("loc_42F4")

    label("loc_3B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B93")

    #C0212
    ChrTalk(
        0xFE,
        (
            "这边的工作\x01",
            "也总算就绪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "稍后我也去克洛斯贝尔市\x01",
            "逛逛吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3BD9")

    label("loc_3B93")


    #C0214
    ChrTalk(
        0xFE,
        (
            "稍后要不要去\x01",
            "克洛斯贝尔市逛逛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "反正也想\x01",
            "去借点新书来看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD9")

    Jump("loc_42F4")

    label("loc_3BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE8")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0216
    ChrTalk(
        0xFE,
        (
            "《日常猫语会话入门》……\x01",
            "这本书可真有趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "喵～～咕。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "喵～哦。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "喵啊～～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0220
    ChrTalk(
        0xA,
        (
            "……喂，阿尔弗雷德啊，\x01",
            "你该不会是在说什么失礼的话吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "哈哈，如果想知道刚才那些话的意思，\x01",
            "你也看看这本书就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D4A")

    label("loc_3CE8")


    #C0222
    ChrTalk(
        0xFE,
        (
            "嗯，图书馆在纪念庆典期间\x01",
            "也照常开馆吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "如果图书馆闭馆，无法借到新书，\x01",
            "可就太无聊了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D4A")

    Jump("loc_42F4")

    label("loc_3D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3EDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E98")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0224
    ChrTalk(
        0xFE,
        (
            "『红耀石』……\x01",
            "唔唔，这本书很有意思啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0225
    ChrTalk(
        0xA,
        (
            "我记得这部小说\x01",
            "在有段时间曾经\x01",
            "倍受关注呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xA,
        (
            "还有传闻说，其中的内容\x01",
            "似乎都是根据真事改编的。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "如果真是这样，\x01",
            "那也挺有意思的……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "无论是不是真的，小说本身已经很有趣了，\x01",
            "这样不就足够了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xA,
        "虽然我还是非常好奇……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3ED7")

    label("loc_3E98")


    #C0230
    ChrTalk(
        0xFE,
        "好，接下来该看哪本书呢？\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "想看一些\x01",
            "比较奇怪的书呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED7")

    Jump("loc_42F4")

    label("loc_3EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_409E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4033")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0232
    ChrTalk(
        0xFE,
        (
            "《克洛斯贝尔市\x01",
            "  优秀饮食店特辑》……\x01",
            "唔唔，介绍了不少不错的店呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0233
    ChrTalk(
        0xA,
        (
            "……喂，阿尔弗雷德，\x01",
            "你也照顾一下我的感受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "呵呵……你也努力让这家店\x01",
            "被刊登上去不就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xA,
        (
            "那本书好像只介绍市区本地的店的吧？\x01",
            "就算没被登上去，\x01",
            "我做的料理也一定不会输给他们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "哈哈，你还真敢说啊。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_4099")

    label("loc_4033")


    #C0237
    ChrTalk(
        0xFE,
        (
            "好吧，接下来……\x01",
            "看看小说\x01",
            "似乎也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "下次有空的时候，\x01",
            "就到克洛斯贝尔市图书馆\x01",
            "去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4099")

    Jump("loc_42F4")

    label("loc_409E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_41A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4153")

    #C0239
    ChrTalk(
        0xFE,
        (
            "好吧，就趁现在看看\x01",
            "之前去克洛斯贝尔市\x01",
            "图书馆借来的书吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "《克洛斯贝尔市\x01",
            "  优秀饮食店特辑》……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "……哈哈，\x01",
            "在这里看这种书，似乎有点失礼啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41A4")

    label("loc_4153")


    #C0242
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市的图书馆中\x01",
            "有各种各样的书，很有趣的。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        "你们不妨也去看看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_41A4")

    Jump("loc_42F4")

    label("loc_41A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_42EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C4")
    Call(0, 12)
    Jump("loc_42E6")

    label("loc_41C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_428D")

    #C0244
    ChrTalk(
        0xFE,
        (
            "那天赶得很巧，\x01",
            "每家人都要在第二天早起干活。\x01",
            "所以大家全都很早就熟睡了。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xE,
        (
            "#1P然后，魔兽就像是看准了这个\x01",
            "时机一样，在当夜冒了出来……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "总之就是运气不好，\x01",
            "也只能这么说了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42E6")

    label("loc_428D")


    #C0247
    ChrTalk(
        0xFE,
        (
            "各家受到的损害\x01",
            "都不算很严重。\x01",
            "这算是不幸中的万幸吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "希望不要\x01",
            "再发生这种事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E6")

    Jump("loc_42F4")

    label("loc_42EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_42F4")

    label("loc_42F4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_3150 end

    def Function_12_42FC(): pass

    label("Function_12_42FC")

    EventBegin(0x0)
    Fade(500)
    OP_68(360, 1500, 3610, 0)
    MoveCamera(312, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22780, 0)
    SetChrPos(0x101, -470, 0, 2360, 0)
    SetChrPos(0x102, -1200, 0, 1520, 0)
    SetChrPos(0x103, 880, 0, 1830, 0)
    SetChrPos(0x104, 80, 0, 1070, 0)
    SetChrFlags(0xB, 0x80)
    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xA, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrPos(0xE, -2060, 180, 4000, 0)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Sleep(500)

    #C0249
    ChrTalk(
        0xE,
        "#5P（嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xE,
        (
            "#5P……嗯，好吃。\x01",
            "格方做的蛋包饭\x01",
            "真是绝世美味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xA,
        (
            "#11P哈哈，你能这么说，\x01",
            "我也算没白做了。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        "#0000F#6P那个，抱歉打扰一下。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)
    Fade(500)
    SetChrSubChip(0xE, 0x2)
    OP_93(0xE, 0x5A, 0x0)
    OP_0D()

    #C0253
    ChrTalk(
        0xA,
        "#11P哦，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#0003F#6P我们是克洛斯贝尔市\x01",
            "警察局的人……\x02\x03",

            "#0001F关于之前发生的\x01",
            "狼形魔兽侵害事件，\x01",
            "能向二位打听一些情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xE,
        (
            "#5P是三周前的那件事吗？\x01",
            "嗯，这个嘛……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xE,
        (
            "#5P那天赶得很巧，\x01",
            "每家人都要在第二天早起干活。\x01",
            "所以大家全都很早就睡熟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xE,
        (
            "#5P然后，魔兽就像是看准了这个\x01",
            "时机一样，在当夜冒了出来……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        (
            "#5P总之就是运气不好，\x01",
            "也只能这么说了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xA,
        "#11P我能提供的信息差不多也是一样。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xA,
        (
            "#11P那天住店的人们\x01",
            "也全说什么都没看见。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        "#0106F#6P是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x104,
        (
            "#0306F#6P并没有什么\x01",
            "决定性的证据呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        (
            "#0002F#5P嗯，调查就是这样的啊。\x01",
            "探听情报时，必须要坚持不懈，\x01",
            "才能得出结果的。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x103,
        (
            "#0206F#6P总而言之……\x01",
            "要不要先休息一下？\x02\x03",

            "#0211F差不多也快饿到极点了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0265
    ChrTalk(
        0xA,
        (
            "#11P怎么，你们\x01",
            "还没吃午饭吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xA,
        (
            "#11P好，机会难得，\x01",
            "就请你们尝尝本店的招牌\x01",
            "蛋包饭吧，算我请客。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#0011F#6P不，那怎么可以！\x01",
            "怎么能让您破费呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xA,
        "#11P没关系，就当是交个朋友啦。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "#11P或者说打个广告也行，\x01",
            "下次来村里的时候，\x01",
            "再到我们店里来吃饭就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x104,
        "#0309F#6P哈哈，真是大方呀。\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x102,
        (
            "#0102F#6P罗伊德，难得人家\x01",
            "一番好意……\x01",
            "我们就恭敬不如从命吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x103,
        "#0204F#6P赞成。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#0006F#6P嗯、嗯～……也是啊。\x02\x03",

            "#0002F那么，我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        "#11P好～\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xA,
        (
            "#11P那你们就找个空位子坐下，\x01",
            "稍等一阵吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")

    #A0276
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "过了一会，新鲜出锅的蛋包饭\x01",
            "便被端到了罗伊德等人的面前。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "尽情享用了一餐乡村特有的质朴美味的料理，\x01",
            "罗伊德等人从郊外一路走来的疲惫感也完全消散了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Sleep(1000)
    Sound(13, 0, 100, 0)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(4000)
    OP_1F()
    SetChrPos(0xE, -2060, 180, 4000, 0)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0x0, -260, 0, 2660, 0)
    ClearChrFlags(0xB, 0x80)
    SetScenarioFlags(0x69, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_12_42FC end

    def Function_13_4A5A(): pass

    label("Function_13_4A5A")

    TalkBegin(0xFE)

    #C0278
    ChrTalk(
        0xFE,
        (
            "史蒂芬可真是的，\x01",
            "平时明明缺乏运动，\x01",
            "还要到处跑……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        "呵呵，不过，我也算放心了。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "他似乎和村里的\x01",
            "孩子成了好朋友呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_4A5A end

    def Function_14_4AE0(): pass

    label("Function_14_4AE0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B74")
    Jump("loc_4BBE")

    label("loc_4B74")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B94")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4BBE")

    label("loc_4B94")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BB4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4BBE")

    label("loc_4BB4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BBE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C79")

    #C0281
    ChrTalk(
        0xFE,
        (
            "史蒂芬，今天似乎\x01",
            "也去卡米尤那里玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "待在克洛斯贝尔市的时候，\x01",
            "明明是那么无精打采的……\x01",
            "呵呵，是环境改变了他吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CCD")

    label("loc_4C79")


    #C0283
    ChrTalk(
        0xFE,
        (
            "史蒂芬开始在外面玩耍了，\x01",
            "我也很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "下次要去安洁太太\x01",
            "那里道谢才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CCD")

    Jump("loc_5389")

    label("loc_4CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4CE0")
    Jump("loc_5389")

    label("loc_4CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4D4E")

    #C0285
    ChrTalk(
        0xFE,
        (
            "史蒂芬最近\x01",
            "似乎常和村里的孩子们一起玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "要正式搬到这个村里，\x01",
            "似乎也不是很遥远的事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5389")

    label("loc_4D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E02")

    #C0287
    ChrTalk(
        0xFE,
        (
            "创立纪念庆典快结束了，\x01",
            "我赶在拥挤的闭幕式之前\x01",
            "回到这边了。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "虽然很开心，\x01",
            "不过人实在是太多了，\x01",
            "好累哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "呼～这个村子里的空气\x01",
            "真是很治愈啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E67")

    label("loc_4E02")


    #C0290
    ChrTalk(
        0xFE,
        (
            "史蒂芬说要去给村里的\x01",
            "孩子们送礼物……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "……真有点意外呢，\x01",
            "那孩子终于也\x01",
            "喜欢上这个村子了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E67")

    Jump("loc_5389")

    label("loc_4E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4E7A")
    Jump("loc_5389")

    label("loc_4E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E88")
    Jump("loc_5389")

    label("loc_4E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4E96")
    Jump("loc_5389")

    label("loc_4E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4F48")

    #C0292
    ChrTalk(
        0xFE,
        (
            "村里好像有人要出去开露天店，\x01",
            "会卖些什么东西呢，好期待哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "这孩子似乎很想\x01",
            "回克洛斯贝尔市……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "在这边也待了挺长时间了，\x01",
            "趁此机会回去一趟\x01",
            "似乎也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5389")

    label("loc_4F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF0")

    #C0295
    ChrTalk(
        0xFE,
        (
            "『彩虹剧团』啊……\x01",
            "我也去看过几次呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "伊莉娅·普拉提耶的表演，\x01",
            "真是连空之女神都会叹为观止，\x01",
            "精彩绝伦哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "嗯～还想再去看看呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5050")

    label("loc_4FF0")


    #C0298
    ChrTalk(
        0xFE,
        (
            "伊莉娅·普拉提耶的表演……⊥\x01",
            "啊，我又回想起上次欣赏时\x01",
            "的感动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        "嗯～还想再去看看呢。\x02",
    )

    CloseMessageWindow()

    label("loc_5050")

    Jump("loc_5389")

    label("loc_5055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_517D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5114")

    #C0300
    ChrTalk(
        0xFE,
        (
            "我们正在认真考虑，\x01",
            "要不要搬到这个村子住。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "结果，这里的店主\x01",
            "就说『反正有空房间』，\x01",
            "然后把房间便宜地租给我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "呵呵，在城市里很少\x01",
            "能遇见这种好事呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5178")

    label("loc_5114")


    #C0303
    ChrTalk(
        0xFE,
        (
            "我们正在认真考虑，\x01",
            "要不要搬到这个村子住。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "多亏店主的好意，\x01",
            "我们才能长住下来，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5178")

    Jump("loc_5389")

    label("loc_517D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_522E")

    #C0305
    ChrTalk(
        0xFE,
        (
            "嗯～虽然我一直\x01",
            "憧憬乡村生活……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "但如果今后还会发生魔兽灾害的话，\x01",
            "那还是待在克洛斯贝尔市比较安全吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "即使如此，这种平静的生活\x01",
            "还是让人难以放弃啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5389")

    label("loc_522E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_52C8")

    #C0308
    ChrTalk(
        0xFE,
        (
            "那起骚动真是吓了我一跳呢。\x01",
            "明明是个宁静的夜晚，\x01",
            "天亮时竟然发现出了那种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "虽说是乡村，\x01",
            "但魔兽闯进人类居住的地方\x01",
            "也真是很诡异呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5389")

    label("loc_52C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5389")

    #C0310
    ChrTalk(
        0xFE,
        (
            "哎呀，你们也是\x01",
            "从克洛斯贝尔市来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "我们是从前一阵子开始\x01",
            "暂住在这里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "远离都市喧嚣的宁静生活……\x01",
            "嗯～我所憧憬的生活环境就是这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "是不是应该\x01",
            "正式搬到这边住呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5389")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_4AE0 end

    def Function_15_5391(): pass

    label("Function_15_5391")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_53A2")
    Jump("loc_586C")

    label("loc_53A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_53B0")
    Jump("loc_586C")

    label("loc_53B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_53BE")
    Jump("loc_586C")

    label("loc_53BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_53CC")
    Jump("loc_586C")

    label("loc_53CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_53DA")
    Jump("loc_586C")

    label("loc_53DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_53E8")
    Jump("loc_586C")

    label("loc_53E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_53F6")
    Jump("loc_586C")

    label("loc_53F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5490")

    #C0314
    ChrTalk(
        0xFE,
        (
            "为了创立纪念庆典，\x01",
            "说不定会回\x01",
            "克洛斯贝尔市一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "如果借此机会，能让妈妈重新\x01",
            "考虑一下，不要搬来村里就好了……\x01",
            "但应该没什么希望吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_586C")

    label("loc_5490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_55C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5574")

    #C0316
    ChrTalk(
        0xFE,
        (
            "广场上有对兄妹在玩吧？\x01",
            "虽然他们常来邀请我一起玩，\x01",
            "不过我总是没那个心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "还以为要玩什么呢，\x01",
            "竟然说『来玩游击士游戏吧』。\x01",
            "开什么玩笑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "乡下的孩子果然幼稚啊。\x01",
            "唉，好想回克洛斯贝尔市啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_55BF")

    label("loc_5574")


    #C0319
    ChrTalk(
        0xFE,
        (
            "虽然年龄相近，\x01",
            "但乡下的孩子果然幼稚啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "好想回克洛斯贝尔市啊……\x02",
    )

    CloseMessageWindow()

    label("loc_55BF")

    Jump("loc_586C")

    label("loc_55C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5663")

    #C0321
    ChrTalk(
        0xFE,
        (
            "这个村里的人……\x01",
            "实在是善良过头了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "只是说可能会搬来，\x01",
            "就把我们当成自己人来对待。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "虽然我并不想搬来，\x01",
            "但不知为什么，也有点矛盾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_586C")

    label("loc_5663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_56F3")

    #C0324
    ChrTalk(
        0xFE,
        (
            "由于那场狼形魔兽事件，\x01",
            "妈妈好像开始犹豫要不要搬家了……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "不过她是那种不会积蓄烦恼的类型。\x01",
            "到了明天，一定就会全部忘光吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_586C")

    label("loc_56F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_5791")

    #C0326
    ChrTalk(
        0xFE,
        (
            "话说，真难以置信啊。\x01",
            "竟然会有狼形魔兽潜进来，\x01",
            "在克洛斯贝尔市是肯定不会发生这种事的。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "唉，好烦好烦。\x01",
            "妈妈怎么会想\x01",
            "搬到这种地方来呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_586C")

    label("loc_5791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_586C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5810")

    #C0328
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "这里实在是令人难以置信的土气啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "唉～唉，要搬的话，怎么不搬去\x01",
            "米修拉姆那边呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_586C")

    label("loc_5810")


    #C0330
    ChrTalk(
        0xFE,
        (
            "这里没有百货店，又没有剧场，\x01",
            "之前还发生了那种骚动……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "好想回克洛斯贝尔市啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_586C")

    TalkEnd(0xFE)
    Return()

    # Function_15_5391 end

    def Function_16_5870(): pass

    label("Function_16_5870")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5904")
    Jump("loc_594E")

    label("loc_5904")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5924")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_594E")

    label("loc_5924")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5944")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_594E")

    label("loc_5944")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_594E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59EF")

    #C0332
    ChrTalk(
        0xFE,
        "好痛好痛……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "昨天只跑了那么点路，\x01",
            "就痛成这样，\x01",
            "真是丢人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        "……不过，昨天玩得真开心啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A0D")

    label("loc_59EF")


    #C0335
    ChrTalk(
        0xFE,
        "……昨天玩得真开心啊……\x02",
    )

    CloseMessageWindow()

    label("loc_5A0D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_5870 end

    def Function_17_5A15(): pass

    label("Function_17_5A15")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AA9")
    Jump("loc_5AF3")

    label("loc_5AA9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AC9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AF3")

    label("loc_5AC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5AE9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AF3")

    label("loc_5AE9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AF3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0336
    ChrTalk(
        0xFE,
        (
            "牧草的味道……\x01",
            "还有鸡和蜂蜜的香气\x01",
            "正在引诱我。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "一定有什么好吃的，\x01",
            "……要不要点些什么呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_5A15 end

    def Function_18_5B83(): pass

    label("Function_18_5B83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B98")
    Call(0, 7)
    Jump("loc_5BFA")

    label("loc_5B98")


    #C0338
    ChrTalk(
        0xFE,
        (
            "唔……开露天店也是\x01",
            "一件很辛苦的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "但是，为了给村子带来活力，\x01",
            "我一定要办成这件事……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BFA")

    TalkEnd(0xFE)
    Return()

    # Function_18_5B83 end

    def Function_19_5BFE(): pass

    label("Function_19_5BFE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C92")
    Jump("loc_5CDC")

    label("loc_5C92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5CB2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CDC")

    label("loc_5CB2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CD2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CDC")

    label("loc_5CD2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CDC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0340
    ChrTalk(
        0xFE,
        (
            "好了，肚子\x01",
            "已经填饱的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "差不多也该\x01",
            "去享受垂钓了吧～\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_5BFE end

    def Function_20_5D49(): pass

    label("Function_20_5D49")

    TalkBegin(0xFE)

    #C0342
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "这个村子\x01",
            "真是个好地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "将来真想在\x01",
            "这种宁静的地方\x01",
            "悠闲度过余生啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_5D49 end

    def Function_21_5DA6(): pass

    label("Function_21_5DA6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E3A")
    Jump("loc_5E84")

    label("loc_5E3A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E5A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E84")

    label("loc_5E5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E7A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E84")

    label("loc_5E7A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E84")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F77")

    #C0344
    ChrTalk(
        0xFE,
        (
            "我打算今天\x01",
            "回共和国了……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "可是女朋友从昨天起\x01",
            "就一直说想留在克洛斯贝尔，\x01",
            "根本听不进我的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "呜，那个叫斯克特的可恶游击士……\x01",
            "趁我不在的时候，\x01",
            "对我女朋友做了什么！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5FFA")

    label("loc_5F77")


    #C0347
    ChrTalk(
        0xFE,
        (
            "丢下女朋友不管，\x01",
            "竟然这么快就遭到了报应……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "总而言之，就算是来硬的，\x01",
            "也要把她拖回共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "绝对要让她\x01",
            "重新喜欢上我！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FFA")

    Jump("loc_617B")

    label("loc_5FFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_60E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_607E")

    #C0350
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "刚才忘记说了，\x01",
            "谢谢你们救了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "当时要是没有你们的话，\x01",
            "我可能就已经……（抖）。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_60DB")

    label("loc_607E")


    #C0352
    ChrTalk(
        0xFE,
        (
            "话、话说回来……\x01",
            "从刚才开始，\x01",
            "我女朋友的样子就好奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "脸红红的……\x01",
            "到底是怎么了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60DB")

    Jump("loc_617B")

    label("loc_60E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6158")

    #C0354
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "我也去克洛斯贝尔市的露天店吃过了，\x01",
            "不过还是这边的东西更加美味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "哎呀，真是来对了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_617B")

    label("loc_6158")


    #C0356
    ChrTalk(
        0xFE,
        (
            "嗯，美味美味。\x01",
            "真是来对了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_617B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_5DA6 end

    def Function_22_6183(): pass

    label("Function_22_6183")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_621F")

    #C0357
    ChrTalk(
        0xFE,
        (
            "在村长家的旁边可以看到的\x01",
            "花田风景……真是美丽怡人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "如果住在克洛斯贝尔市的旅店，\x01",
            "一定是欣赏不到的吧。\x01",
            "呵呵，还好来了这边。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6273")

    label("loc_621F")


    #C0359
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市\x01",
            "现在应该很热闹吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "我不太喜欢人多的地方……\x01",
            "还好来了这边呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6273")

    TalkEnd(0xFE)
    Return()

    # Function_22_6183 end

    def Function_23_6277(): pass

    label("Function_23_6277")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_630B")
    Jump("loc_6355")

    label("loc_630B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_632B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6355")

    label("loc_632B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_634B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6355")

    label("loc_634B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6355")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_64A7")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6454")

    #C0361
    ChrTalk(
        0xFE,
        (
            "喂，不要说\x01",
            "斯克特先生的坏话啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "比起把我丢下，\x01",
            "自己一个人逃跑的你来说，\x01",
            "人家可要有男子汉气概多了！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x17,
        (
            "我、我都说过\x01",
            "那只是误会了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x17,
        (
            "那个，求你了，\x01",
            "跟我一起回共和国吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_64A2")

    label("loc_6454")


    #C0365
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "回到共和国，\x01",
            "就再也见不到斯克特先生了……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        "真不想回去啊～……\x02",
    )

    CloseMessageWindow()

    label("loc_64A2")

    Jump("loc_658D")

    label("loc_64A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_654A")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_651E")

    #C0367
    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "他叫\x01",
            "斯克特吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        "…………⊥\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x17,
        "那个心形是什么啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6545")

    label("loc_651E")


    #C0371
    ChrTalk(
        0xFE,
        (
            "他叫\x01",
            "斯克特吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "…………⊥\x02",
    )

    CloseMessageWindow()

    label("loc_6545")

    Jump("loc_658D")

    label("loc_654A")


    #C0373
    ChrTalk(
        0xFE,
        (
            "我老公似乎很中意\x01",
            "这里的料理呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        "呵呵，明年要不要再来呢。\x02",
    )

    CloseMessageWindow()

    label("loc_658D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_6277 end

    def Function_24_6595(): pass

    label("Function_24_6595")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65AA")
    Call(0, 7)
    Jump("loc_6609")

    label("loc_65AA")


    #C0375
    ChrTalk(
        0xFE,
        (
            "昨天听说了养蜂场的事，\x01",
            "突然很想\x01",
            "买点蜂蜜。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "可是，之后该怎么\x01",
            "拿回去呢……应该很重吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6609")

    TalkEnd(0xFE)
    Return()

    # Function_24_6595 end

    def Function_25_660D(): pass

    label("Function_25_660D")

    Call(0, 26)
    Return()

    # Function_25_660D end

    def Function_26_6611(): pass

    label("Function_26_6611")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_662A")
    Call(0, 39)
    Return()

    label("loc_662A")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6637")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_753E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "休息\x01",      # 2
            "放弃\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6696")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6696")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66B6")
    OP_AF(0x48)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7539")

    label("loc_66B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66D6")
    OP_AF(0x46)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7539")

    label("loc_66D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66EA")
    Jump("loc_7539")

    label("loc_66EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7539")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6781")

    #C0377
    ChrTalk(
        0xA,
        (
            "多谢你们帮忙找到了书，\x01",
            "这样我也就放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xA,
        (
            "我今后会小心，\x01",
            "不再把借来的东西转借出去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_6781")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67EF")

    #C0379
    ChrTalk(
        0xA,
        (
            "将书转手借给艾尔琴的事，\x01",
            "我真的觉得很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xA,
        (
            "客人拜托我，\x01",
            "我就很难拒绝呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_67EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C1")

    #C0381
    ChrTalk(
        0xA,
        (
            "呀，欢迎。\x01",
            "要不要来份早点？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xC,
        (
            "老板～\x01",
            "我还是老样子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xC, 500)

    #C0383
    ChrTalk(
        0xA,
        (
            "喂喂，我现在是在问\x01",
            "这位客人要点什么哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x0, 500)

    #C0384
    ChrTalk(
        0xA,
        (
            "……哎呀，抱歉了。\x01",
            "想好要点什么的话，\x01",
            "随时都可以和我说哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_694C")

    label("loc_68C1")


    #C0385
    ChrTalk(
        0xA,
        (
            "奇斯和阿尔弗雷德之类的家伙，\x01",
            "点菜的时候总是说『老样子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xA,
        (
            "即使这么说，我也能听明白，\x01",
            "说明他们来得真是够多了，\x01",
            "所以我也挺开心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_694C")

    Jump("loc_7539")

    label("loc_6951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6A7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69FE")

    #C0387
    ChrTalk(
        0xA,
        (
            "创造一个能让村里人放松的环境……\x01",
            "我就是抱着这种想法，才开了这家店。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xA,
        "所以，并不需要赚太多钱的。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xA,
        (
            "……不过，说这种话\x01",
            "会惹席莉生气呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6A78")

    label("loc_69FE")


    #C0390
    ChrTalk(
        0xA,
        (
            "虽然我觉得\x01",
            "不需要赚太多钱，\x01",
            "但席莉却是不以为然。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xA,
        (
            "……嗯，要是连女儿\x01",
            "也说不用赚钱的话，\x01",
            "这家店大概早就倒闭了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A78")

    Jump("loc_7539")

    label("loc_6A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6B0F")

    #C0392
    ChrTalk(
        0xA,
        (
            "在二楼定了房间的阿蕾莎夫人母子\x01",
            "似乎是真心喜欢上了我们村子。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xA,
        (
            "虽然只是长期暂住，\x01",
            "不过，只要村里的同伴增加了，我就热烈欢迎。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7539")

    label("loc_6B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B82")

    #C0394
    ChrTalk(
        0xA,
        (
            "游客的数量也终于\x01",
            "开始少下来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xA,
        (
            "能让各式各样的人品尝料理，\x01",
            "我是非常开心的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6BDB")

    label("loc_6B82")


    #C0396
    ChrTalk(
        0xA,
        (
            "嗯～露天摊位该撤摊了，\x01",
            "席莉也快回来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xA,
        (
            "从明天开始，\x01",
            "又要努力\x01",
            "招呼常客们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BDB")

    Jump("loc_7539")

    label("loc_6BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6D4D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6C53")

    #C0398
    ChrTalk(
        0xA,
        (
            "谢谢你们\x01",
            "把重要的客人\x01",
            "平安带回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xA,
        (
            "要是以后再有什么事的话，\x01",
            "可又要麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D48")

    label("loc_6C53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_6CC8")

    #C0400
    ChrTalk(
        0xA,
        (
            "要去古战场的话，\x01",
            "只要走过阿尔摩利卡古道\x01",
            "中途的石桥就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xA,
        (
            "游客的事……\x01",
            "就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D48")

    label("loc_6CC8")


    #C0402
    ChrTalk(
        0xA,
        (
            "最近好像有人\x01",
            "说是观光纪念什么的，\x01",
            "擅自进入了养蜂场。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xA,
        (
            "农场和养蜂场这些地方中\x01",
            "也有不少危险的东西，\x01",
            "希望他们多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D48")

    Jump("loc_7539")

    label("loc_6D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE3")

    #C0404
    ChrTalk(
        0xA,
        (
            "从昨天开始，就有好几个\x01",
            "来观光的人住在这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xA,
        (
            "在平时，来住店的大多都是些\x01",
            "哈罗德先生那样的商人，\x01",
            "所以觉得挺新鲜呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6E69")

    label("loc_6DE3")


    #C0406
    ChrTalk(
        0xA,
        (
            "我们店也在市里开设了露天店，\x01",
            "有些客人在那里品尝过料理后，\x01",
            "觉得好吃就过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xA,
        (
            "哎呀，\x01",
            "真让我感动呢，\x01",
            "这种事实在是令人开心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E69")

    Jump("loc_7539")

    label("loc_6E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6FA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F41")

    #C0408
    ChrTalk(
        0xA,
        (
            "我们要在纪念庆典开设露天店，\x01",
            "然后贩卖本店的料理呢，\x01",
            "所以小女过去帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xA,
        (
            "本店的料理\x01",
            "现在也可以在\x01",
            "克洛斯贝尔市的露天店吃到哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xA,
        (
            "好，应该会有\x01",
            "游客来住店……\x01",
            "我也要加油了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6FA0")

    label("loc_6F41")


    #C0411
    ChrTalk(
        0xA,
        (
            "我家女儿也去\x01",
            "纪念庆典的露天店\x01",
            "帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xA,
        (
            "本店的料理，\x01",
            "现在也可以在市里的露天店吃到哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FA0")

    Jump("loc_7539")

    label("loc_6FA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_703F")

    #C0413
    ChrTalk(
        0xA,
        (
            "关于在纪念庆典推出的商品，\x01",
            "他们似乎还在热烈讨论呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xA,
        (
            "嗯～机会难得，\x01",
            "希望也能出售我们店的料理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xA,
        "顺便也能向游客们宣传宣传嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7539")

    label("loc_703F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7109")

    #C0416
    ChrTalk(
        0xA,
        "那件魔兽骚乱事件解决之后，已过了一个月……\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔时代周刊\x01",
            "虽然没有详细报道，\x01",
            "不过，是你们解决的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xA,
        (
            "多亏你们，总算可以放心睡觉了，\x01",
            "我一直想向你们表示感谢。\x01",
            "真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7539")

    label("loc_7109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_720A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71C6")

    #C0419
    ChrTalk(
        0xA,
        (
            "村长昨天通知说，\x01",
            "要我们小心狼形魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xA,
        (
            "听说那起事件\x01",
            "影响的范围相当大？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xA,
        (
            "我觉得野生的魔兽\x01",
            "应该会在固定的\x01",
            "地盘内活动的……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xA,
        "但也会有这种稀罕事啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7205")

    label("loc_71C6")


    #C0423
    ChrTalk(
        0xA,
        (
            "那些狼形魔兽\x01",
            "的活动地盘好广啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xA,
        "莫非是什么新品种吗？\x02",
    )

    CloseMessageWindow()

    label("loc_7205")

    Jump("loc_7539")

    label("loc_720A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_72E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72A4")

    #C0425
    ChrTalk(
        0xA,
        (
            "没想到，事到如今\x01",
            "还会提到那次的魔兽事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xA,
        (
            "事情已经过去挺久了，\x01",
            "我都快忘了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xA,
        (
            "既然还没找到，\x01",
            "那就不能大意呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_72E2")

    label("loc_72A4")


    #C0428
    ChrTalk(
        0xA,
        (
            "给村子带来灾害的魔兽……\x01",
            "既然还没找到，\x01",
            "那就不能大意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E2")

    Jump("loc_7539")

    label("loc_72E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_7412")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7306")
    Call(0, 12)
    TalkEnd(0xA)
    Return()

    label("loc_7306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73A9")

    #C0429
    ChrTalk(
        0xA,
        (
            "午饭的时候，\x01",
            "出去干农活的人都会回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xA,
        (
            "但还谈不上什么生意兴隆……\x01",
            "嗯，这里毕竟是乡下嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xA,
        (
            "只要有常客来光顾，\x01",
            "我就觉得这店开得值了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_740D")

    label("loc_73A9")


    #C0432
    ChrTalk(
        0xA,
        (
            "哈罗德先生来村里的时候，\x01",
            "也经常会光顾我们店。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xA,
        (
            "他也算是常客了，\x01",
            "偶尔也要给他点优惠才是呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_740D")

    Jump("loc_7539")

    label("loc_7412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74BE")

    #C0434
    ChrTalk(
        0xA,
        (
            "哟，欢迎。\x01",
            "要不要喝点什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xA,
        (
            "看起来，你们好像很疲惫呢。\x01",
            "可不要太勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xA,
        (
            "要不来吃点什么吧？\x01",
            "别的不说，简单的家常料理我们还是有的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7539")

    label("loc_74BE")


    #C0437
    ChrTalk(
        0xA,
        (
            "唔，一说到吃饭，我想起来了……\x01",
            "就快到中午了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xA,
        (
            "出去干农活的人们\x01",
            "差不多也该回来吃午饭了。\x01",
            "我得赶快准备准备才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7539")

    Jump("loc_6637")

    label("loc_753E")

    TalkEnd(0xA)
    Return()

    # Function_26_6611 end

    def Function_27_7542(): pass

    label("Function_27_7542")

    Call(0, 28)
    Return()

    # Function_27_7542 end

    def Function_28_7546(): pass

    label("Function_28_7546")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7553")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75A3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_75A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_75C2")
    OP_AF(0x4C)
    Jump("loc_75C4")

    label("loc_75C2")

    OP_AF(0x4B)

    label("loc_75C4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81F3")

    label("loc_75D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75E7")
    Jump("loc_81F3")

    label("loc_75E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76B8")

    #C0439
    ChrTalk(
        0x9,
        (
            "爷爷经常训斥我，\x01",
            "要我精神一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x9,
        (
            "但说实话，我真是没什么干劲呢。\x01",
            "什么祖祖辈辈相传的店，我可不懂……\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x9,
        (
            "祖先也真是的，要是开家\x01",
            "更赚钱的店该多好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7720")

    label("loc_76B8")


    #C0442
    ChrTalk(
        0x9,
        (
            "祖先也真是的，要是开家\x01",
            "更赚钱的店该多好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x9,
        (
            "假如我是ＩＢＣ总裁的儿子，\x01",
            "倒是很乐意继承家业啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7720")

    Jump("loc_81F3")

    label("loc_7725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7832")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77BF")

    #C0444
    ChrTalk(
        0x9,
        (
            "唉……又被爷爷\x01",
            "骂了。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x9,
        (
            "不然，干脆丢下这种店，\x01",
            "进城打拼去好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x9,
        (
            "……但要是这样的话，\x01",
            "爷爷就会变成孤身一人了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_782D")

    label("loc_77BF")


    #C0447
    ChrTalk(
        0x9,
        (
            "不然，干脆丢下这种店，\x01",
            "进城打拼去好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x9,
        (
            "……但那样的话，爷爷就会孤身一人了，\x01",
            "所以我是不会那么做的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_782D")

    Jump("loc_81F3")

    label("loc_7832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_794B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78D1")

    #C0449
    ChrTalk(
        0x9,
        (
            "爷爷……\x01",
            "似乎心情很好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x9,
        (
            "因为爷爷很喜欢\x01",
            "哈罗德先生呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x9,
        (
            "……哼，反正我就是个\x01",
            "在纪念庆典也毫无作为的\x01",
            "前·无业游民啦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7946")

    label("loc_78D1")


    #C0452
    ChrTalk(
        0x9,
        (
            "要说我在纪念庆典时学到的本事，\x01",
            "也就是计算商品的速度\x01",
            "变得更快了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x9,
        (
            "……嗯～感觉还是\x01",
            "停留在打下手的水准啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7946")

    Jump("loc_81F3")

    label("loc_794B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7A01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79BF")

    #C0454
    ChrTalk(
        0x9,
        (
            "呼啊啊～……\x01",
            "昨天之前的忙碌\x01",
            "真是夸张啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x9,
        (
            "不过呢，这下总算\x01",
            "恢复到轻松的日子了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_79FC")

    label("loc_79BF")


    #C0456
    ChrTalk(
        0x9,
        (
            "……感觉爷爷\x01",
            "好像在瞪着这边呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x9,
        "有要挨骂的预感……\x02",
    )

    CloseMessageWindow()

    label("loc_79FC")

    Jump("loc_81F3")

    label("loc_7A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7AD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A80")

    #C0458
    ChrTalk(
        0x9,
        (
            "那个客人也真是的，\x01",
            "为什么要找爷爷说话啊。\x01",
            "站柜台的明明是我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x9,
        "……莫非我看起来就不可靠？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7AD4")

    label("loc_7A80")


    #C0460
    ChrTalk(
        0x9,
        "……我是不是很不可靠呢。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x9,
        (
            "……算了，爷爷\x01",
            "谈好价钱的话，\x01",
            "我这边倒也轻松了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AD4")

    Jump("loc_81F3")

    label("loc_7AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7B4D")

    #C0462
    ChrTalk(
        0x9,
        (
            "从昨天开始，\x01",
            "客人突然变多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x9,
        (
            "虽然爷爷莫名奇妙地干劲十足，\x01",
            "但说实话，我可是忙得晕头转向啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F3")

    label("loc_7B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7C06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC4")

    #C0464
    ChrTalk(
        0x9,
        (
            "村里的蜂蜜\x01",
            "似乎很好卖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x9,
        (
            "……要是平时也能卖这么多的话，\x01",
            "我也就可以轻松过活了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7C01")

    label("loc_7BC4")


    #C0466
    ChrTalk(
        0x9,
        (
            "虽然没有客人来才轻松……\x01",
            "但真希望蜂蜜能再多卖出一点啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C01")

    Jump("loc_81F3")

    label("loc_7C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C8B")

    #C0467
    ChrTalk(
        0x9,
        (
            "迪利克和爷爷\x01",
            "从刚才开始就一直在说话……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x9,
        "嗯～但我完全听不懂。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x9,
        (
            "我好像真是\x01",
            "不适合做生意啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7CB4")

    label("loc_7C8B")


    #C0470
    ChrTalk(
        0x9,
        (
            "迪利克和爷爷\x01",
            "到底在说些什么呢……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CB4")

    Jump("loc_81F3")

    label("loc_7CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7DBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D50")

    #C0471
    ChrTalk(
        0x9,
        (
            "最近我开始看\x01",
            "《克洛斯贝尔时代周刊》了。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x9,
        (
            "你们原来\x01",
            "上过杂志啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x9,
        (
            "嗯～我也想\x01",
            "去克洛斯贝尔市，\x01",
            "过上光鲜的日子啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7DB9")

    label("loc_7D50")


    #C0474
    ChrTalk(
        0x9,
        (
            "有朝一日，\x01",
            "我也会成为能上\x01",
            "《克洛斯贝尔时代周刊》的大人物的。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x9,
        (
            "……不过暂时还是\x01",
            "打算在店里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DB9")

    Jump("loc_81F3")

    label("loc_7DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7EB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E5E")

    #C0476
    ChrTalk(
        0x9,
        (
            "唉……\x01",
            "爷爷最近老是\x01",
            "拿我跟哈罗德先生比较。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x9,
        (
            "说什么\x01",
            "『你也跟人家学学啊』之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x9,
        (
            "我可是新手，\x01",
            "不要给我\x01",
            "那么大压力嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7EB4")

    label("loc_7E5E")


    #C0479
    ChrTalk(
        0x9,
        (
            "爷爷似乎\x01",
            "很喜欢哈罗德先生。\x01",
            "总是拿我跟他比。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x9,
        (
            "唉……\x01",
            "不要给我\x01",
            "那么大压力嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EB4")

    Jump("loc_81F3")

    label("loc_7EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_7FF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F8D")

    #C0481
    ChrTalk(
        0x9,
        (
            "我只是个无业游民，\x01",
            "可爷爷老是要我继承\x01",
            "这家店，好烦的。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x9,
        (
            "唉～唉……\x01",
            "继承这种破旧的店有什么好的。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x9,
        (
            "既然身为男子汉，\x01",
            "就应该去克洛斯贝尔碰碰运气，\x01",
            "做番事业，当个大人物才是啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7FF0")

    label("loc_7F8D")


    #C0484
    ChrTalk(
        0x9,
        (
            "有朝一日，真想去克洛斯贝尔\x01",
            "做一番大事业啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x9,
        (
            "……不过暂时\x01",
            "在店里帮忙也不错啦。\x01",
            "反正轻松。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF0")

    Jump("loc_81F3")

    label("loc_7FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_8106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80B5")

    #C0486
    ChrTalk(
        0x9,
        (
            "新月那天晚上的事？\x01",
            "……哦，那件在村里\x01",
            "闹得沸沸扬扬的事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x9,
        (
            "那时我睡得很沉，\x01",
            "所以什么也不记得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x9,
        (
            "听说损失已经填补回来了，\x01",
            "我觉得应该\x01",
            "不用太在意了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8101")

    label("loc_80B5")


    #C0489
    ChrTalk(
        0x9,
        (
            "村长说遭受的损失\x01",
            "已经填补回来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x9,
        (
            "魔兽什么的，\x01",
            "还是忘掉为好吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8101")

    Jump("loc_81F3")

    label("loc_8106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_81F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8180")

    #C0491
    ChrTalk(
        0x9,
        (
            "您、您好。\x01",
            "欢迎……光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x9,
        (
            "……哇，咬到舌头了！\x01",
            "咳咳。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x9,
        (
            "呃，欢迎光临。\x01",
            "请随便看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_81F3")

    label("loc_8180")


    #C0494
    ChrTalk(
        0x9,
        (
            "唉……爷爷真欺负人。\x01",
            "让我接待客人，根本就不行嘛。\x01",
            "你也这么认为吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x9,
        (
            "……哦，又忘了说敬语。\x01",
            "呃～十分抱歉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F3")

    Jump("loc_7553")

    label("loc_81F8")

    TalkEnd(0x9)
    Return()

    # Function_28_7546 end

    def Function_29_81FC(): pass

    label("Function_29_81FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8212")
    Call(0, 41)
    Jump("loc_864C")

    label("loc_8212")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8223")
    Jump("loc_8649")

    label("loc_8223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8231")
    Jump("loc_8649")

    label("loc_8231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_83FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_82A0")

    #C0496
    ChrTalk(
        0x1B,
        (
            "#3600F我太太最近也很努力地\x01",
            "支持我的工作。\x02\x03",

            "今后，我们一家会\x01",
            "齐心协力，努力打拼的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83F9")

    label("loc_82A0")


    #C0497
    ChrTalk(
        0x1B,
        (
            "#3605F呀，各位\x01",
            "也来进蜂蜜吗？\x02\x03",

            "#3600F哈哈哈，不好意思，\x01",
            "在进货方面，你们可是赢不了我的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x104,
        (
            "#0300F不，我们怎么可能\x01",
            "是来做生意的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        (
            "#0000F听说纪念庆典之后，\x01",
            "您暂时休业了一段时间……\x01",
            "现在又重新开始做生意了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x1B,
        (
            "#3600F嗯，虽说是休业，\x01",
            "其实也只是休养一下身体而已。\x02\x03",

            "多亏如此，总算是恢复精神了。\x01",
            "今后我会更加努力，\x01",
            "做好生意的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_83F9")

    Jump("loc_8649")

    label("loc_83FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_840C")
    Jump("loc_8649")

    label("loc_840C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_841A")
    Jump("loc_8649")

    label("loc_841A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8428")
    Jump("loc_8649")

    label("loc_8428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8436")
    Jump("loc_8649")

    label("loc_8436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8444")
    Jump("loc_8649")

    label("loc_8444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8452")
    Jump("loc_8649")

    label("loc_8452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8460")
    Jump("loc_8649")

    label("loc_8460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_84B9")

    #C0501
    ChrTalk(
        0x1B,
        (
            "#3604F那么……\x01",
            "差不多也该准备回去了。\x02\x03",

            "#3608F嗯，钥匙放在哪里了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8649")

    label("loc_84B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_8640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85BC")

    #C0502
    ChrTalk(
        0x1B,
        (
            "#3610F很不巧，我当时并不在\x01",
            "受灾现场呢。\x01",
            "真抱歉，帮不上忙。\x02\x03",

            "#3608F……如果魔兽灾害继续在各地发生，\x01",
            "住在克洛斯贝尔的\x01",
            "人们也会感到不安的。\x02\x03",

            "#3600F特别任务支援科的各位，\x01",
            "事件的调查就有劳你们多加努力了，\x01",
            "我也会在心里为各位加油的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_863B")

    label("loc_85BC")


    #C0503
    ChrTalk(
        0x1B,
        (
            "#3604F各位的调查\x01",
            "一定会使情况好转起来……\x01",
            "我有这种感觉。\x02\x03",

            "#3600F事件的调查，还请各位多加努力，\x01",
            "我也会在心里为各位加油的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_863B")

    Jump("loc_8649")

    label("loc_8640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8649")

    label("loc_8649")

    TalkEnd(0x1B)

    label("loc_864C")

    Return()

    # Function_29_81FC end

    def Function_30_864D(): pass

    label("Function_30_864D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86E1")
    Jump("loc_872B")

    label("loc_86E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8701")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_872B")

    label("loc_8701")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8721")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_872B")

    label("loc_8721")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_872B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_87E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_876B")
    Call(0, 37)
    Jump("loc_87E7")

    label("loc_876B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_877D")
    Call(0, 38)
    Jump("loc_87E7")

    label("loc_877D")


    #C0504
    ChrTalk(
        0x1C,
        (
            "#0803F好啦……小憩之后，\x01",
            "就去其它地方看看吧。\x02\x03",

            "#0800F必须要去确认一下\x01",
            "有没有影响到巴士运行等问题呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87E7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_864D end

    def Function_31_87EF(): pass

    label("Function_31_87EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_888B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_880D")
    Call(0, 37)
    Jump("loc_888B")

    label("loc_880D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_881F")
    Call(0, 38)
    Jump("loc_888B")

    label("loc_881F")


    #C0505
    ChrTalk(
        0x1D,
        (
            "#0903F据说，除了以前通缉过的\x01",
            "魔兽之外，还有人目击了\x01",
            "之前从未见过的危险魔兽。\x02\x03",

            "#0901F你们也要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_888B")

    TalkEnd(0xFE)
    Return()

    # Function_31_87EF end

    def Function_32_888F(): pass

    label("Function_32_888F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8923")
    Jump("loc_896D")

    label("loc_8923")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8943")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_896D")

    label("loc_8943")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8963")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_896D")

    label("loc_8963")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_896D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A32")
    SetChrSubChip(0x1E, 0x0)

    #C0506
    ChrTalk(
        0x1E,
        (
            "郊区各地似乎也\x01",
            "来了不少游客。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x1E,
        (
            "艾欧莉娅，\x01",
            "要注意制止他们\x01",
            "前往危险的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x1F,
        "明白。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x1F,
        "……不过，先吃了这个再去吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_8A91")

    label("loc_8A32")


    #C0510
    ChrTalk(
        0xFE,
        (
            "一眼看去，郊外似乎\x01",
            "没什么危险的地方，\x01",
            "但其实却有不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        (
            "要注意别让游客们\x01",
            "误入才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A91")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_888F end

    def Function_33_8A99(): pass

    label("Function_33_8A99")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B2D")
    Jump("loc_8B77")

    label("loc_8B2D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8B4D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B77")

    label("loc_8B4D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B6D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B77")

    label("loc_8B6D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B77")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8C6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C05")

    #C0512
    ChrTalk(
        0xFE,
        (
            "今天是来\x01",
            "清剿通缉魔兽的。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xFE,
        (
            "只要一段时间不管，\x01",
            "它们就会再次冒出来呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_8C6C")

    label("loc_8C05")


    #C0514
    ChrTalk(
        0xFE,
        (
            "旅游旺季的时候，\x01",
            "郊外的情况特别令人担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "虽然不能久留，\x01",
            "但待在这边的时候\x01",
            "要多加注意才是。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C6C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_8A99 end

    def Function_34_8C74(): pass

    label("Function_34_8C74")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D78")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0516
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "★白蜡亭·推荐料理★\x01",
            "～乡村风味蛋包饭～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0517
    ChrTalk(
        0x101,
        (
            "#0000F嘿，蛋包饭吗……\x01",
            "好像很美味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        (
            "#0100F还写着食谱呢。\x01",
            "难得见到，就记下来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0519
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x9)
    Jump("loc_8DBD")

    label("loc_8D78")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0520
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "★白蜡亭·推荐料理★\x01",
            "～乡村风味蛋包饭～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_8DBD")

    TalkEnd(0xFF)
    Return()

    # Function_34_8C74 end

    def Function_35_8DC1(): pass

    label("Function_35_8DC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E4B")

    #C0521
    ChrTalk(
        0xFE,
        (
            "这个村子的气氛真不错啊，\x01",
            "真想一直躺在原野上\x01",
            "晒太阳啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "等我上了年纪以后，真想\x01",
            "在这种地方悠闲度过余生啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_8EB1")

    label("loc_8E4B")


    #C0523
    ChrTalk(
        0xFE,
        (
            "虽然在市里的『巴鲁卡』之类的地方\x01",
            "喧闹玩乐很开心……\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xFE,
        (
            "不过在这种宁静的地方\x01",
            "悠闲度日也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EB1")

    TalkEnd(0xFE)
    Return()

    # Function_35_8DC1 end

    def Function_36_8EB5(): pass

    label("Function_36_8EB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F1D")

    #C0525
    ChrTalk(
        0xFE,
        (
            "以这么便宜的价格\x01",
            "就能买到新鲜蔬菜啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        (
            "一定要趁此机会\x01",
            "大量购买\x01",
            "才行呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_8F6D")

    label("loc_8F1D")


    #C0527
    ChrTalk(
        0xFE,
        (
            "马铃薯、洋葱……\x01",
            "特产的蜂蜜……！\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        (
            "哦呵呵呵呵……！\x01",
            "便宜……好便宜呀！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F6D")

    TalkEnd(0xFE)
    Return()

    # Function_36_8EB5 end

    def Function_37_8F71(): pass

    label("Function_37_8F71")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1D, 0xFF)
    OP_68(80860, 1500, -980, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 80000, 0, 0, 90)
    SetChrPos(0x102, 79750, 0, -1000, 90)
    SetChrPos(0x103, 78500, 0, 750, 90)
    SetChrPos(0x104, 78250, 0, -250, 90)
    SetChrPos(0x109, 78750, 0, -1250, 90)
    SetChrPos(0x1C, 81630, 170, -1650, 270)
    SetChrSubChip(0x1C, 0x2)
    OP_93(0x1D, 0x10E, 0x0)
    SetChrSubChip(0x1D, 0x0)
    OP_0D()

    #C0529
    ChrTalk(
        0x1C,
        "#0805F#6P啊，是罗伊德和大家。\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x1D,
        (
            "#0900F#12P辛苦了。\x01",
            "你们也来工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x101,
        (
            "#0002F#5P嗯，但做的都是一些\x01",
            "琐碎的工作啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x104,
        (
            "#0305F#5P你们莫非\x01",
            "在这里住店吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x1C,
        (
            "#0806F#6P啊，是的。\x01",
            "其实昨天在清剿魔兽时费了点时间，\x01",
            "结果赶不上巴士了……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x1D,
        (
            "#0903F#12P所以就在这家旅店\x01",
            "住了下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x102,
        (
            "#0101F#5P竟然会有连艾丝蒂尔你们\x01",
            "都感到棘手的魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x103,
        (
            "#0205F#5P那魔兽那么\x01",
            "难对付吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x1C,
        (
            "#0806F#6P嗯～好像是之前\x01",
            "也出现过的通缉魔兽……\x02\x03",

            "#0801F但在郊外地区一下\x01",
            "出现了很多只呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x1D,
        (
            "#0906F#12P而且似乎变得比以前\x01",
            "更强了……\x02\x03",

            "#0901F不光是这一带，\x01",
            "其它的地区似乎也有类似的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        "#0001F#5P是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x109,
        (
            "#0503F#5P……警备队这边\x01",
            "也接到了类似的报告呢。\x02\x03",

            "#0500F幸好没有对\x01",
            "巴士或车子的运行造成影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        (
            "#0306F#5P那倒是，\x01",
            "可以说是不幸中的万幸了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x102,
        "#0108F#5P不过，还是有点令人担心呢……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 80000, 0, -500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1C, 82040, 180, -1400, 45)
    SetChrSubChip(0x1C, 0x0)
    OP_93(0x1D, 0x87, 0x0)
    OP_4C(0x1D, 0xFF)
    SetScenarioFlags(0xCF, 5)
    EventEnd(0x5)
    Return()

    # Function_37_8F71 end

    def Function_38_937D(): pass

    label("Function_38_937D")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1D, 0xFF)
    OP_68(80860, 1500, -980, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 80000, 0, 0, 90)
    SetChrPos(0x102, 79750, 0, -1000, 90)
    SetChrPos(0x103, 78500, 0, 750, 90)
    SetChrPos(0x104, 78250, 0, -250, 90)
    SetChrPos(0x109, 78750, 0, -1250, 90)
    SetChrPos(0x1C, 81630, 170, -1650, 270)
    SetChrSubChip(0x1C, 0x0)
    OP_93(0x1D, 0xE1, 0x0)
    SetChrSubChip(0x1D, 0x0)
    OP_0D()

    #C0543
    ChrTalk(
        0x1C,
        (
            "#0802F#6P这个暂且不提……\x01",
            "你们这次好像在和一位特别人物同行啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x1D,
        "#0900F#12P是克洛斯贝尔警备队的成员吗？\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x109,
        (
            "#0500F#5P我是唐古拉姆门的\x01",
            "诺艾尔·希卡上士。\x02\x03",

            "两位是游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x1C,
        (
            "#0800F#6P嗯，我是克洛斯贝尔分部的\x01",
            "艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x1D,
        (
            "#0904F#12P初次见面，\x01",
            "我是约修亚·布莱特。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0548
    ChrTalk(
        0x109,
        (
            "#0505F#5P你、你们就是……\x02\x03",

            "#0502F我在克洛斯贝尔时代周刊上看过报道！\x01",
            "你们就是解决了利贝尔异变事件的\x01",
            "年轻英雄吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x1C,
        (
            "#0809F#6P啊哈哈……\x01",
            "是格蕾丝小姐的报道吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x1D,
        (
            "#0904F#12P其实那并不仅是\x01",
            "我们的功劳……\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        (
            "#0012F#5P（嗯～艾丝蒂尔他们\x01",
            "  果然是名人啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 80000, 0, -500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x1C, 82040, 180, -1400, 45)
    SetChrSubChip(0x1C, 0x0)
    OP_93(0x1D, 0x87, 0x0)
    OP_4C(0x1D, 0xFF)
    SetScenarioFlags(0xCF, 6)
    EventEnd(0x5)
    Return()

    # Function_38_937D end

    def Function_39_96B9(): pass

    label("Function_39_96B9")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)
    LoadChrToIndex("chr/ch27200.itc", 0x1E)
    OP_68(40, 1200, 2180, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22400, 0)
    SetChrPos(0x101, 0, 0, 2000, 360)
    SetChrPos(0x102, -1000, 0, 1500, 360)
    SetChrPos(0x103, 1000, 0, 500, 360)
    SetChrPos(0x104, 0, 0, -250, 360)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 0, 0, -6860, 0)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -6860, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0552
    ChrTalk(
        0xA,
        (
            "#5P啊啊……客人要是\x01",
            "出了什么事，可就不得了啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xA,
        "#5P拜托，一定要平安无事啊～……\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#6P#0003F打扰一下，请问\x01",
            "#0001F您是格方先生吗？\x02\x03",

            "我们是特别任务支援科的人。\x01",
            "您之前好像给我们发出了支援请求，\x01",
            "所以前来咨询相关情况……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(750)
    TurnDirection(0xA, 0x101, 750)

    #C0555
    ChrTalk(
        0xA,
        "#11P哦哦，你们就是……！\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xA,
        (
            "#11P总算来了！\x01",
            "啊，总之就是出大事了！\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xA,
        (
            "#11P要是早知道会变成这样，\x01",
            "就算用拴的，也要\x01",
            "把他们留在村里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xA,
        "#11P啊啊，这全都是我的责任……！\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#6P#0006F请您镇静一点，\x01",
            "慢慢说给我们听吧。\x02\x03",

            "#0001F到底出了什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xA,
        (
            "#11P……啊，那个。\x01",
            "抱歉，一时失态了。\x01",
            "我从头说起吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xA,
        (
            "#11P有一对外国的情侣游客，\x01",
            "从昨天开始入住在我们这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xA,
        (
            "#11P今天早上，给他们送早餐去的时候，\x01",
            "发现房间里已经没人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xA,
        (
            "#11P看样子，好像是去了\x01",
            "位于阿尔摩利卡古道途中，\x01",
            "那个名叫『古战场』的地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x101,
        "#0005F#6P古战场吗……？\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x102,
        (
            "#5P#0106F之前我也说过，古道那一带\x01",
            "有中世纪时代的战场遗迹。\x02\x03",

            "#0105F只不过，石桥在很早以前\x01",
            "就已经坏了，应该是过不去的吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xA,
        (
            "#11P嗯，本来应该是这样的……\x01",
            "可就在前几天，修缮工程刚好结束了。\x01",
            "所以现在什么人都能进去。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xA,
        (
            "#11P……那对情侣昨天\x01",
            "就说想去那里观光，\x01",
            "怎么都不肯听我劝告……\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xA,
        (
            "#11P我明明提醒过他们，\x01",
            "千万不要随便进去的……\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x104,
        (
            "#6P#0303F唔～古战场这名字，听起来\x01",
            "就像是个观光景点……\x02\x03",

            "#0301F会是需要那样小心警惕的\x01",
            "危险场所吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xA,
        (
            "#11P嗯……从很久以前开始，\x01",
            "那里就是以危险魔兽的生息之地而闻名的。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xA,
        (
            "#11P连村里的人都小心翼翼，\x01",
            "从不敢靠近呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xA,
        (
            "#11P而且，自从石桥坏了以后，\x01",
            "这段时间一直都没有进行过维护。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xA,
        (
            "#11P说实话，\x01",
            "目前甚至都不能确认\x01",
            "里面已经变成什么样子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x103,
        (
            "#6P#0203F一无所知的游客\x01",
            "竟然闯进了那种地方……\x02\x03",

            "#0201F的确很不妙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x102,
        "#5P#0101F嗯……情况似乎相当紧急啊。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xA,
        (
            "#11P……拜托你们了。\x01",
            "能不能找到那些游客，\x01",
            "把他们带回来？\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xA,
        (
            "#11P我已经让朋友阿尔弗雷德\x01",
            "去那边盯守，以免再有人\x01",
            "进入古战场了……\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xA,
        (
            "#11P这样下去的话，重要的客人\x01",
            "恐怕就要遭遇危险了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x101,
        (
            "#6P#0004F……我明白了，\x01",
            "就交给我们吧。\x02\x03",

            "#0000F我们一定会找到\x01",
            "那两位游客的。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x104,
        (
            "#6P#0306F唉，没办法呢。\x02\x03",

            "#0300F不听忠告的游客啊……\x01",
            "赶快把他们找出来，\x01",
            "然后好好训斥一顿吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xA,
        (
            "#11P嗯……谢谢！\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xA,
        "#11P就拜托你们──\x02",
    )

    CloseMessageWindow()

    #N0583
    NpcTalk(
        0xC,
        "青年的声音",
        "老板～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A028():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A028)
    Sleep(30)

    def lambda_A038():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A038)

    def lambda_A045():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A045)
    Sleep(30)

    def lambda_A055():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A055)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    OP_68(0, 1200, 750, 0)
    MoveCamera(303, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25990, 0)
    OP_68(0, 1200, 750, 3000)
    SetCameraDistance(22990, 3000)
    Sound(103, 0, 100, 0)

    def lambda_A0C5():
        OP_97(0xC, 0x0, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A0C5)

    def lambda_A0DF():
        OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_A0DF)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xC, 2)

    #C0584
    ChrTalk(
        0x101,
        "#11P#0005F（……是常客吗？）\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xA,
        (
            "#11P……奇斯，\x01",
            "到底怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xA,
        (
            "#11P我现在正和他们\x01",
            "谈些重要的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xC,
        (
            "#6P现在可不是\x01",
            "悠闲谈话的时候吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xC,
        (
            "#6P您不是说有游客失踪，\x01",
            "情况很不妙吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xA,
        (
            "#11P哦，关于这件事，\x01",
            "我刚才就在和这几位警察……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xC,
        "#6P不必了，您就放心吧。\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xC,
        (
            "#6P为了发愁的老板……\x01",
            "我已经请来了强有力的帮手啊！\x02",
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
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0592
    ChrTalk(
        0x102,
        "#11P#0105F强有力的……帮手？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x20, 500)

    #C0593
    ChrTalk(
        0xC,
        (
            "#12P来来！\x01",
            "快点来听听老板\x01",
            "怎么说吧！\x02",
        )
    )

    CloseMessageWindow()

    #N0594
    NpcTalk(
        0x20,
        "男性的声音",
        "……嗯，当然。\x02",
    )

    CloseMessageWindow()
    OP_68(-110, 1200, 580, 2000)
    SetCameraDistance(24140, 2000)

    def lambda_A34E():
        OP_97(0x20, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A34E)

    def lambda_A368():
        OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_A368)
    OP_98(0xC, 0xFFFFFD12, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_A38D():
        OP_93(0xC, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A38D)
    WaitChrThread(0x20, 1)
    WaitChrThread(0x20, 2)

    #C0595
    ChrTalk(
        0x20,
        (
            "#6P……我是游击士协会的\x01",
            "斯克特。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x20,
        (
            "#6P听说您需要寻找\x01",
            "行踪不明的游客……\x01",
            "能马上把事情的详细情况告诉我吗？\x02",
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

    #C0597
    ChrTalk(
        0x101,
        "#11P#0011F游……游击士！？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x102,
        "#11P#0105F怎、怎么会……\x02",
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x20, 0x101, 500)
    Sleep(500)

    #C0599
    ChrTalk(
        0x20,
        (
            "#6P……哦？\x01",
            "你们不是特别任务支援科的……\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x20,
        (
            "#6P真巧……呃，\x01",
            "现在的气氛似乎不适合说这个啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xA,
        (
            "#11P奇、奇斯，\x01",
            "这位游击士怎么会来这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x2D, 0x1F4)

    #C0602
    ChrTalk(
        0xC,
        (
            "#5P您说什么呢，老板。\x01",
            "遇到困难时就该找游击士，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xC,
        (
            "#5P今早听了您的话之后，\x01",
            "我就火速赶往克洛斯贝尔市的协会，\x01",
            "递交了委托啊！\x02",
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
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0604
    ChrTalk(
        0xA,
        (
            "#11P唉……\x01",
            "你的好意我十分感激……\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x103,
        "#11P#0211F……原来是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x104,
        "#11P#0306F某种意义上来说，时机真是巧得过头了啊。\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xC,
        (
            "#5P……咦，\x01",
            "你们怎么是这种反应啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x20,
        (
            "#6P……看起来，事情好像\x01",
            "变得有点复杂了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x20,
        (
            "#6P不好意思，能不能麻烦\x01",
            "你们简短地说明一下情况？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        (
            "#11P#0011F好、好的。\x01",
            "嗯，其实是……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0611
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将自己一行也是接受了\x01",
            "同一委托而来到这里的情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0612
    ChrTalk(
        0x20,
        (
            "#6P……原来如此，\x01",
            "是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x20,
        (
            "#6P这可真是意料之外的\x01",
            "重复委托啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x103,
        (
            "#12P#0203F可是……\x01",
            "在这种情况下，应该怎么办呢？\x02\x03",

            "#0200F警察和游击士\x01",
            "同时接受了\x01",
            "同一件委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x104,
        (
            "#11P#0302F……这不就变成\x01",
            "单纯的竞争了吗？\x02\x03",

            "#0309F看看谁能抢先完成委托吧！\x01",
            "……就是这种感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x102,
        (
            "#11P#0106F真是的……\x01",
            "问题并不在那里吧。\x02\x03",

            "#0108F罗伊德，你看该怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x101,
        "#11P#0003F这个啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0618
    ChrTalk(
        0x101,
        (
            "#11P#0001F斯克特先生，\x01",
            "关于这次的事……\x02\x03",

            "我们就结成统一战线吧，\x01",
            "您意下如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_AA42():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA42)

    def lambda_AA4F():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AA4F)

    def lambda_AA5C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA5C)
    Sleep(1000)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0619
    ChrTalk(
        0x20,
        (
            "#6P哈哈，看来我们挺合拍啊。\x01",
            "我也和你想到一起去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x102,
        "#5P#0105F统一战线……\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x104,
        (
            "#6P#0305F也就是说，一起去\x01",
            "古战场那里寻找游客吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x101,
        (
            "#11P#0000F不，我的意思是分头找。\x02\x03",

            "#0003F听店主说，那里似乎长期无人管理，\x01",
            "已经变成了魔兽的栖息地。\x02\x03",

            "因此必须要争分夺秒，\x01",
            "尽快找到那对情侣游客。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x20,
        (
            "#6P我对这一带的地形虽然有一定了解，\x01",
            "但古战场确实是一片相当广阔的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x20,
        (
            "#6P分头搜索的话，\x01",
            "想必能提高成功救援的概率吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x20,
        (
            "#6P如果再使用艾尼格玛，随时保持联络，\x01",
            "搜索就会更有效率了。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x104,
        "#6P#0300F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x103,
        (
            "#6P#0204F的确……\x01",
            "看来，这是最合理的选择了。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xA,
        "#11P嗯，这样的话，我也就更加放心了。\x02",
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xA,
        (
            "#11P人命关天，\x01",
            "人手越多越好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xA,
        "#11P那就拜托各位了。\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x20,
        (
            "#6P委托人也同意了……\x01",
            "那就这么决定了。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x101,
        "#11P#0000F嗯，请您多多关照。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0633
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德与斯克特\x01",
            "相互交换了艾尼格玛的通讯号码。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0634
    ChrTalk(
        0x20,
        "#6P那么，事不宜迟。\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x20,
        (
            "#6P我就先走一步，前往古战场了。\x01",
            "你们准备完毕之后，也赶快跟来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x20,
        "#6P那么，待会见。\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0xB4, 0x1F4)

    def lambda_AE25():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE25)

    def lambda_AE32():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AE32)

    def lambda_AE3F():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AE3F)

    def lambda_AE4C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_AE4C)
    OP_97(0x20, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)

    #C0637
    ChrTalk(
        0x101,
        (
            "#11P#0003F……好。\x01",
            "我们也赶快做好准备，\x01",
            "前往古战场吧。\x02\x03",

            "#0001F可不能落在\x01",
            "斯克特先生\x01",
            "的后面啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0638
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【搜寻失踪游客的委托】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_68(0, 1500, 0, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 0, 0, 0, 0)
    SetChrPos(0x1, 0, 0, 0, 0)
    SetChrPos(0x2, 0, 0, 0, 0)
    SetChrPos(0x3, 0, 0, 0, 0)
    SetChrPos(0xA, 750, 0, 1500, 270)
    SetChrPos(0xC, -750, 0, 1500, 90)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x40)
    OP_29(0x1F, 0x1, 0x0)
    SetScenarioFlags(0xD9, 4)
    FadeToBright(500, 0)
    OP_0D()
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_39_96B9 end

    def Function_40_AFF8(): pass

    label("Function_40_AFF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27200.itc", 0x1E)
    LoadChrToIndex("chr/ch02400.itc", 0x1F)
    OP_4B(0xA, 0xFF)
    OP_68(40, 1200, 2180, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24460, 0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrPos(0x101, 0, 0, 2000, 360)
    SetChrPos(0x102, -1000, 0, 1500, 360)
    SetChrPos(0x103, 1000, 0, 500, 360)
    SetChrPos(0x104, 0, 0, -250, 360)
    SetChrPos(0xA, 0, 0, 3700, 180)
    SetChrPos(0x20, -7270, 2220, -4080, 90)
    SetChrPos(0x21, -8270, 2530, -4140, 90)
    SetCameraDistance(23460, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0639
    ChrTalk(
        0xA,
        (
            "#11P游客们被平安带回，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xA,
        "#11P各位，十分感谢啊。\x02",
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x101,
        (
            "#6P#0000F不，哪里。\x01",
            "基本上，全都是斯克特先生\x01",
            "与亚里欧斯先生的功劳……\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x104,
        (
            "#6P#0306F刚才也是他们带\x01",
            "那对情侣去房间休息的呢。\x02\x03",

            "#0301F怎么说呢～实力那么强，\x01",
            "而且还那么细心……\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x102,
        (
            "#5P#0104F呵呵……这种体贴\x01",
            "或许也是游击士的特色吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    #C0644
    ChrTalk(
        0x102,
        (
            "#5P#0100F好了……这样一来，姑且就算是\x01",
            "完成了一件工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0645
    ChrTalk(
        0x103,
        (
            "#6P#0203F嗯，不过……\x01",
            "还有一个问题。\x02\x03",

            "#0200F这次任务虽然是警察与协会\x01",
            "共同执行的……\x02\x03",

            "但最终来说，究竟\x01",
            "应该怎样判断呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xAA, 0x1F4)
    Sleep(300)

    #C0646
    ChrTalk(
        0x104,
        (
            "#6P#0305F说来也是啊。\x02\x03",

            "#0300F……你说呢，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x101,
        (
            "#11P#0003F嗯～……\x01",
            "刚才我也说了……\x02\x03",

            "这次的委托，如果没有\x01",
            "斯克特先生和亚里欧斯先生帮忙，\x01",
            "恐怕是无法顺利解决的。\x02\x03",

            "#0000F所以，这次应该算是\x01",
            "他们完成了委托……\x02",
        )
    )

    CloseMessageWindow()

    #N0648
    NpcTalk(
        0x20,
        "斯克特的声音",
        "#1P那可不敢当。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_B481():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B481)

    def lambda_B48E():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B48E)

    def lambda_B49B():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B49B)

    def lambda_B4A8():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B4A8)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    Fade(500)
    OP_68(-7560, 2000, -4170, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22120, 0)
    OP_68(210, 1500, -390, 5000)
    MoveCamera(305, 22, 0, 5000)
    SetCameraDistance(24390, 5000)

    def lambda_B534():
        OP_95(0x20, -3270, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_B534)

    def lambda_B54E():
        OP_95(0x21, -3270, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B54E)
    WaitChrThread(0x20, 1)

    def lambda_B56C():
        OP_95(0x20, 500, 0, -1770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_B56C)
    WaitChrThread(0x21, 1)

    def lambda_B58A():
        OP_95(0x21, -500, 0, -2580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B58A)

    def lambda_B5A4():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5A4)

    def lambda_B5B1():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B5B1)

    def lambda_B5BE():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B5BE)

    def lambda_B5CB():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B5CB)
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x0, 0x0)
    WaitChrThread(0x21, 1)
    OP_93(0x21, 0x0, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0649
    ChrTalk(
        0x102,
        "#11P#0105F亚里欧斯先生、斯克特先生……\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x21,
        (
            "#6P#1403F……店主，那两人好像\x01",
            "打算稍后向您道歉。\x02\x03",

            "#1400F对于不听忠告，\x01",
            "擅自进入古战场这件事，\x01",
            "似乎已经深刻反省过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xA,
        (
            "#11P啊，这样啊。\x01",
            "我倒是不会介意……\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x104,
        (
            "#11P#0304F哈哈，有过这么一场遭遇，\x01",
            "倒也不失为一剂良药啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x103,
        (
            "#11P#0205F话说回来……\x01",
            "您说『不敢当』是指？\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x20,
        (
            "#6P嗯，我刚才已经和\x01",
            "亚里欧斯先生说过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x20,
        (
            "#6P这次的委托，\x01",
            "就算由你们\x01",
            "完成的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0656
    ChrTalk(
        0x101,
        (
            "#11P#0005F哎，这个……\x01",
            "这样好吗？\x02\x03",

            "#0003F我认为，在这次的任务中，\x01",
            "明显还是二位游击士\x01",
            "的功劳更大……\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x20,
        "#6P不，没那回事。\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x20,
        (
            "#6P多亏你们先去解救另一位先生，\x01",
            "我才能专心护理那位女士……\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x20,
        (
            "#6P而且如果不是你们\x01",
            "及时赶到的话，那位先生\x01",
            "说不定也没救了。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x20,
        (
            "#6P从结果上来看，\x01",
            "风头好像都被我们抢去了，\x01",
            "但实际上却是你们的功劳更大。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x104,
        (
            "#11P#0309F哈哈……竟然会被身为\x01",
            "竞争对手的游击士表扬，\x01",
            "真是让人有些难为情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x21,
        (
            "#6P#1404F……我们原本就不是\x01",
            "什么竞争对手吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x21)

    #C0663
    ChrTalk(
        0x21,
        (
            "#6P#1403F特别任务支援科……\x01",
            "与初次见面时相比，\x01",
            "你们似乎也有所成长了啊。\x02\x03",

            "#1400F特别是你……是叫罗伊德吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0664
    ChrTalk(
        0x101,
        "#11P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x21,
        (
            "#6P#1400F在地下空间初次见面\x01",
            "时的事情，还记得吗？\x02\x03",

            "当时，你面对\x01",
            "无法战胜的魔兽，\x01",
            "轻易选择了自我牺牲……\x02\x03",

            "#1404F而这次你却没有那样做。\x01",
            "虽然情况看似没有任何胜算，\x01",
            "但你却在努力寻找脱险的办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x101,
        "#11P#0005F……………………\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x21,
        (
            "#6P#1403F无论在多么不利的状况下，\x01",
            "都要拼尽全力，寻找最佳对策……\x01",
            "想做到这一点，便需要毫不动摇的坚强信念。\x02\x03",

            "这种坚强，要比轻易选择牺牲性命\x01",
            "的觉悟可贵百倍。\x02\x03",

            "#1402F虽然还无法否认，你的实力仍有所不足……\x01",
            "但能做到这一点，就证明\x01",
            "你已经成长了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x101,
        "#11P#0002F……谢谢您。\x02",
    )

    CloseMessageWindow()
    OP_93(0x21, 0xB4, 0x1F4)
    Sleep(300)

    #C0669
    ChrTalk(
        0x21,
        (
            "#11P#1404F呼……\x01",
            "我似乎有些多言了。\x02\x03",

            "#1402F……斯克特，\x01",
            "回协会报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x10E, 0x2EE)

    #C0670
    ChrTalk(
        0x20,
        "#11P明白，亚里欧斯先生。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x101, 500)
    Sleep(300)

    #C0671
    ChrTalk(
        0x20,
        (
            "#6P那么，再见啦，特别任务支援科。\x01",
            "希望以后还有机会\x01",
            "和你们并肩作战。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x101,
        "#11P#0000F嗯，再见。\x02",
    )

    CloseMessageWindow()

    def lambda_BD6E():
        OP_97(0x21, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_BD6E)
    OP_93(0x20, 0xB4, 0x2EE)

    def lambda_BD8F():
        OP_97(0x20, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_BD8F)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x20, 1)
    Sound(104, 0, 100, 0)
    OP_68(-100, 1000, 2110, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(23460, 3000)
    OP_6F(0x79)

    #C0673
    ChrTalk(
        0x103,
        (
            "#12P#0200F该怎么说好呢……竟然被\x01",
            "最出乎意料的人激励了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0674
    ChrTalk(
        0x102,
        (
            "#5P#0109F缇、缇欧，别这么说嘛……\x01",
            "虽然确实是有点意外。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0675
    ChrTalk(
        0x104,
        (
            "#6P#0309F哈哈，这不是皆大欢喜嘛。\x02\x03",

            "#0300F这样应该算是顺利完成了委托吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xA,
        "#11P嗯，真是辛苦各位了。\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xA,
        (
            "#11P那么……\x01",
            "特别任务支援科的诸位，请容我再次郑重道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0xA,
        "#11P以后如果再有什么事，还请多多关照。\x02",
    )

    CloseMessageWindow()

    def lambda_BF4D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF4D)
    Sleep(50)

    def lambda_BF5D():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BF5D)
    Sleep(50)

    def lambda_BF6D():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BF6D)
    Sleep(50)

    def lambda_BF7D():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BF7D)
    Sleep(300)

    #C0679
    ChrTalk(
        0x101,
        (
            "#6P#0000F好的，彼此彼此。\x01",
            "随时恭候您的联络。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(0, 1500, 3000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 0, 0, 3000, 0)
    SetChrPos(0x1, 0, 0, 3000, 0)
    SetChrPos(0x2, 0, 0, 3000, 0)
    SetChrPos(0x3, 0, 0, 3000, 0)
    SetChrPos(0xA, -40, 0, 6040, 180)
    SetChrPos(0x17, 84000, 180, -2040, 283)
    SetChrPos(0x19, 82190, 180, -1670, 103)
    OP_66(0x0, 0x1)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0680
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【搜寻失踪游客的委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x1F, 0x1, 0x4)
    OP_29(0x1F, 0x4, 0x10)
    FadeToBright(500, 0)
    OP_0D()
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_40_AFF8 end

    def Function_41_C111(): pass

    label("Function_41_C111")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4B(0x1B, 0xFF)
    OP_68(113700, 1200, -1000, 0)
    MoveCamera(324, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25940, 0)
    SetChrPos(0x101, 114420, 0, -1180, 270)
    SetChrPos(0x102, 114420, 0, 0, 270)
    SetChrPos(0x103, 115760, 0, -1180, 270)
    SetChrPos(0x104, 115760, 0, 0, 270)
    SetChrPos(0x1B, 112560, 0, -510, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03600.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(24940, 2000)
    OP_6F(0x10)
    OP_0D()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0681
    NpcTalk(
        0x1B,
        "面容温和的男性",
        "#3605F#5P哎呀，各位是……\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x101,
        "#0005F#12P啊，是刚才的……\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x102,
        (
            "#0100F您就是……克洛斯贝尔市\x01",
            "的那位贸易商先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0684
    NpcTalk(
        0x1B,
        "面容温和的男性",
        (
            "#3609F#5P哈哈，你们是听\x01",
            "村长提起过我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("面容温和的男性")

    #A0685
    AnonymousTalk(
        0xFF,
        (
            "──初次见面。\x01",
            "我叫哈罗德·海瓦斯。\x02\x03",

            "在克洛斯贝尔市\x01",
            "做点小生意……\x02\x03",

            "各位莫非\x01",
            "也是来进货的吗？\x02",
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

    #C0686
    ChrTalk(
        0x101,
        "#0000F#12P不、不是，我们是──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0687
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人进行了自我介绍，\x01",
            "说明了前来阿尔摩利卡村的缘由。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0688
    ChrTalk(
        0x1B,
        (
            "#3605F#5P各位原来是警察局的吗……\x01",
            "真是失礼了。\x02\x03",

            "#3603F话说，『特别任务支援科』……\x01",
            "好像在哪里听过似的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0689
    ChrTalk(
        0x1B,
        (
            "#3600F#5P对了！\x01",
            "克洛斯贝尔时代周刊！\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x101,
        (
            "#0012F#12P唉……\x01",
            "您果然看过了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x102,
        (
            "#0106F#2P那个……\x01",
            "实在惭愧。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x1B,
        (
            "#3609F#5P哈哈，不必\x01",
            "觉得难为情啊……\x02\x03",

            "#3600F虽说刚刚成立，\x01",
            "但各位不是很努力嘛。\x02\x03",

            "虽然那篇报道的确\x01",
            "带了点讽刺的意味……\x02\x03",

            "不过，对各位的努力，\x01",
            "似乎还是持善意的肯定态度哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x101,
        "#0000F#12P是、是这样吗……？\x02",
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x103,
        (
            "#0206F#12P……如果真要善意地加以解释，\x01",
            "倒是也可以这么理解……\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x104,
        (
            "#0309F#2P哈哈，也许是因为我们认识写\x01",
            "那篇文章的人，所以很难坦率地接受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x1B,
        (
            "#3608F#5P话说回来，狼形魔兽啊。\x02\x03",

            "在医科大学也有所耳闻，\x01",
            "令人略有些担心呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0697
    ChrTalk(
        0x101,
        (
            "#0005F#12P哈罗德先生，\x01",
            "您在医科大学那边也有业务吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x1B,
        (
            "#3604F#5P嗯，我会批发给他们\x01",
            "一些医院用的必需品。\x02\x03",

            "#3601F据传闻说，那边还\x01",
            "出现了伤员……\x02\x03",

            "还有矿山镇那边，\x01",
            "似乎也遭到袭击了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        (
            "#0001F#12P嗯，警备队现在\x01",
            "似乎正在进行搜索呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x1B,
        (
            "#3608F#5P是这样啊……\x02\x03",

            "#3610F唔，看样子，最近也要\x01",
            "去那边打个招呼才行……\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x102,
        (
            "#0100F#2P说起来……\x02\x03",

            "听说您在采购土特产时，\x01",
            "给出的价格非常慷慨呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x1B,
        (
            "#3609F#5P哈哈……\x01",
            "是听村长说的吗？\x02\x03",

            "#3600F这倒也不是出于\x01",
            "想要做慈善之类的理由啦。\x02\x03",

            "最近这段时间，这个村里的土特产\x01",
            "的评价日渐上升，尤其是蜂蜜。\x02\x03",

            "所以就想趁此机会，\x01",
            "尽量给村里人留下一个好印象，\x01",
            "其实我只是打了这种小算盘而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x104,
        "#0309F#2P哈哈，原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x103,
        (
            "#0202F#12P做生意讲究诚信第一……\x01",
            "是这样吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x102,
        (
            "#0102F#2P呵呵，看来您的生意\x01",
            "做得很不错啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x1B,
        (
            "#3600F#5P哪里，我也不过\x01",
            "就是个初出茅庐的新手罢了。\x02\x03",

            "#3610F不过，真是抱歉呢……\x02\x03",

            "要是能为各位提供\x01",
            "更加有用的情报就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x101,
        (
            "#0011F#12P不，哪里的话。\x01",
            "请您不必介意。\x02\x03",

            "#0000F真是不好意思，\x01",
            "耽误您的时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x1B,
        (
            "#3600F#5P哪里哪里，\x01",
            "请各位加油探听情报吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 115180, 0, -450, 270)
    OP_93(0x1B, 0x10E, 0x0)
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x60, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_41_C111 end

    def Function_42_CB30(): pass

    label("Function_42_CB30")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1200, 1200, 3000, 0)
    MoveCamera(306, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -470, 0, 2360, 315)
    SetChrPos(0x102, -1200, 0, 1520, 315)
    SetChrPos(0x103, 880, 0, 1830, 315)
    SetChrPos(0x104, 80, 0, 1070, 315)
    SetChrFlags(0xB, 0x80)
    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xA, 0x2)
    SetChrPos(0xE, -1420, 180, 3810, 90)
    SetChrSubChip(0xE, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CBFB")
    SetChrPos(0x109, -690, 0, 240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_CC26")

    label("loc_CBFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC26")
    SetChrPos(0x10A, -690, 0, 240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_CC26")

    OP_0D()

    #C0709
    ChrTalk(
        0x101,
        (
            "#6P#0000F请问……\x01",
            "您是阿尔弗雷德先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0xE,
        "#11P哦，你们是……\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0xE,
        (
            "#11P记得是……以前搜索过\x01",
            "古战场的特别任务支援科成员吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0xE,
        "#11P找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，其实……我们今天\x01",
            "是接受了图书馆管理员的\x01",
            "委托而来的。\x02\x03",

            "希望能收回\x01",
            "逾期未还的书……\x01",
            "您有没有印象呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0714
    ChrTalk(
        0xE,
        (
            "#11P哦哦，原来是那件事啊，\x01",
            "我还真是犯迷糊了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)

    #C0715
    ChrTalk(
        0xE,
        (
            "#11P稍等一下哦，\x01",
            "我应该正好带着……\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0xE,
        "#11P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE74")
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_CE74")

    Sleep(1000)

    #C0717
    ChrTalk(
        0x101,
        "#6P#0005F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x102,
        (
            "#6P#0106F莫非是\x01",
            "弄丢了吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)

    #C0719
    ChrTalk(
        0xE,
        (
            "#11P不、不会，应该\x01",
            "不会弄丢的啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0xE,
        (
            "#11P嗯～……\x01",
            "放哪里了呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0721
    ChrTalk(
        0xE,
        "#11P哦哦，对了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)

    #C0722
    ChrTalk(
        0xE,
        (
            "#5P格方。\x01",
            "之前借你的书，还带着吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x1F4)
    OP_93(0x101, 0x0, 0x190)
    OP_93(0x103, 0x0, 0x190)
    OP_93(0x104, 0x0, 0x190)
    OP_93(0x102, 0x0, 0x190)

    #C0723
    ChrTalk(
        0xA,
        "#11P书……？\x02",
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xE,
        (
            "#5P嘿，就是那本啦。\x01",
            "你说想看，我就借给你看\x01",
            "的那本书……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0725
    ChrTalk(
        0xA,
        (
            "#11P……啊，那本书啊！\x01",
            "的确是借给我了呢。\x01",
            "稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D021():
        OP_95(0xFE, -1940, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D021)
    WaitChrThread(0xA, 1)

    def lambda_D03F():
        OP_95(0xFE, -1940, 0, 6800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D03F)
    WaitChrThread(0xA, 1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0E0")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_D0E0")

    Sleep(1000)

    #C0726
    ChrTalk(
        0x104,
        (
            "#6P#0306F话、话说～……\x01",
            "竟然把图书馆的书\x01",
            "转借给了别人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x103,
        "#12P#0200F真是够随便的呢……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D176")

    #C0728
    ChrTalk(
        0x109,
        "#6P#0509F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D1AD")

    label("loc_D176")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D1AD")

    #C0729
    ChrTalk(
        0x10A,
        "#6P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_D1AD")

    SetChrSubChip(0xE, 0x2)

    #C0730
    ChrTalk(
        0xE,
        (
            "#11P唉，真丢脸。\x01",
            "其实我平时很少\x01",
            "会这样的……\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0xE,
        (
            "#11P因为我看的书实在太多了，\x01",
            "一不小心就忘记了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)

    #C0732
    ChrTalk(
        0xE,
        (
            "#5P那么……\x01",
            "格方，找到书了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    #C0733
    ChrTalk(
        0xA,
        "#11P………………没。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D301")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_D301")

    Sleep(1000)

    #C0734
    ChrTalk(
        0xE,
        (
            "#5P什、什么……？\x01",
            "难道你弄丢了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x101,
        "#6P#0012F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xA,
        (
            "#11P不，稍等一下，\x01",
            "我正在努力回想呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0737
    ChrTalk(
        0xA,
        "#11P…………对了！\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xA,
        (
            "#11P我想起来了，那本书……\x01",
            "因为客人不停央求，\x01",
            "我就忍不住借给他了！\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x101,
        "#6P#0011F咦咦咦咦咦！！\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x104,
        "#6P#0305F二重转借吗……！？\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x102,
        (
            "#6P#0106F这、这可真是\x01",
            "在预料之外呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        (
            "#12P#0203F……何止是预料之外……\x01",
            "我觉得简直是难以置信。\x02\x03",

            "#0200F那么，您之后又\x01",
            "转借给谁了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xA,
        (
            "#11P我借给了经常在村子入口\x01",
            "摆弄导力车的艾尔琴。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xA,
        (
            "#11P哎呀，真是很抱歉……\x01",
            "事情就是这样，请原谅我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        (
            "#6P#0006F没、没关系。\x01",
            "既然已经借出去了，\x01",
            "那就没办法了。\x02\x03",

            "#0000F那么……\x01",
            "我们就去找艾尔琴先生，\x01",
            "收回那本图书吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D5D1")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_D5D1")

    SetChrPos(0x0, -470, 0, 2360, 315)
    SetChrPos(0xE, -2060, 180, 4000, 0)
    SetChrPos(0xA, -40, 0, 6040, 180)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    OP_29(0x28, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_42_CB30 end

    SaveToFile()

Try(main)
