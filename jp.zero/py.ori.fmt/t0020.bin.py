from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "レオール老人",           # 1
        "ジェイク",               # 2
        "ゴーファン",             # 3
        "シーリィ",               # 4
        "キース",                 # 5
        "キース",                 # 6
        "アルフレッド",           # 7
        "アレサ",                 # 8
        "アレサ",                 # 9
        "ステファン",             # 10
        "ステファン",             # 11
        "チルル",                 # 12
        "デリック",               # 13
        "コパン",                 # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "観光客",                 # 17
        "観光客",                 # 18
        "観光客",                 # 19
        "ハロルド",               # 20
        "エステル",               # 21
        "ヨシュア",               # 22
        "遊撃士リン",             # 23
        "遊撃士エオリア",         # 24
        "遊撃士スコット",         # 25
        "アリオス",               # 26
        "観光客ブラッド",         # 27
        "観光客エミリアーナ",     # 28
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
        "Function_6_190A",         # 06, 6
        "Function_7_1A2F",         # 07, 7
        "Function_8_1CE3",         # 08, 8
        "Function_9_2996",         # 09, 9
        "Function_10_2A4B",        # 0A, 10
        "Function_11_3987",        # 0B, 11
        "Function_12_4DEF",        # 0C, 12
        "Function_13_566F",        # 0D, 13
        "Function_14_5709",        # 0E, 14
        "Function_15_6132",        # 0F, 15
        "Function_16_66A7",        # 10, 16
        "Function_17_6864",        # 11, 17
        "Function_18_69FC",        # 12, 18
        "Function_19_6A93",        # 13, 19
        "Function_20_6BF0",        # 14, 20
        "Function_21_6C6F",        # 15, 21
        "Function_22_709A",        # 16, 22
        "Function_23_71BC",        # 17, 23
        "Function_24_7544",        # 18, 24
        "Function_25_75E8",        # 19, 25
        "Function_26_75EC",        # 1A, 26
        "Function_27_8791",        # 1B, 27
        "Function_28_8795",        # 1C, 28
        "Function_29_9797",        # 1D, 29
        "Function_30_9C86",        # 1E, 30
        "Function_31_9E3A",        # 1F, 31
        "Function_32_9EEC",        # 20, 32
        "Function_33_A120",        # 21, 33
        "Function_34_A32D",        # 22, 34
        "Function_35_A4C4",        # 23, 35
        "Function_36_A5D8",        # 24, 36
        "Function_37_A6CA",        # 25, 37
        "Function_38_AB6C",        # 26, 38
        "Function_39_AEE2",        # 27, 39
        "Function_40_CAEF",        # 28, 40
        "Function_41_DDB8",        # 29, 41
        "Function_42_E94B",        # 2A, 42
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE8")

    #C0001
    ChrTalk(
        0xFE,
        (
            "この雑貨店は、\x01",
            "わしの曽祖父の代から続く\x01",
            "由緒正しい店なんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "だが、ジェイクのやつは\x01",
            "そこの所をよく分かっておらん。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "もっと誇りをもって\x01",
            "仕事に臨んでほしいもんじゃて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B6B")

    label("loc_AE8")


    #C0004
    ChrTalk(
        0xFE,
        (
            "ジェイクには、\x01",
            "もっと誇りをもって\x01",
            "この仕事に臨んでほしいもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "この店が《ジェイク雑貨店》になるのは\x01",
            "いつの話やら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6B")

    Jump("loc_1906")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C59")

    #C0006
    ChrTalk(
        0xFE,
        (
            "仕事ぶりがだらしないから\x01",
            "ジェイクを叱り付けてやったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "たまに『街にでて大物になる』などと\x01",
            "寝言をほざいておるようじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "そんな暇があったら\x01",
            "店の仕事を一つでも多く\x01",
            "覚えろというんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CF7")

    label("loc_C59")


    #C0009
    ChrTalk(
        0xFE,
        (
            "ジェイクのやつ、たまに\x01",
            "『街にでて大物になる』などと\x01",
            "寝言をほざいておるようじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "そんな暇があったら\x01",
            "店の仕事を一つでも多く\x01",
            "覚えろというんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF7")

    Jump("loc_1906")

    label("loc_CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE4")
    OP_4B(0x1B, 0xFF)
    TurnDirection(0xFE, 0x1B, 0)

    #C0011
    ChrTalk(
        0xFE,
        (
            "毎度ハロルド君には\x01",
            "世話になっておるなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "どれ、今日はハチミツを一瓶\x01",
            "おまけしてやるかの。\x01",
            "家族で楽しむがよかろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x1B,
        (
            "#3609Fふふ……ありがとうございます。\x01",
            "妻と息子も喜びますよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_E86")

    label("loc_DE4")


    #C0014
    ChrTalk(
        0xFE,
        (
            "ハロルド君に比べて\x01",
            "うちのジェイクときたら……\x01",
            "いつまでたっても半人前のままじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "記念祭を乗り切ったんじゃから\x01",
            "少しでもハロルド君に\x01",
            "近づいてほしいのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E86")

    Jump("loc_1906")

    label("loc_E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F34")

    #C0016
    ChrTalk(
        0xFE,
        (
            "観光客がクロスベル市に帰ったら\x01",
            "とたんに寂しくなったのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "……ジェイクもヒマしておるようじゃな。\x01",
            "どれ、いっちょう喝をいれてやるか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F95")

    label("loc_F34")


    #C0018
    ChrTalk(
        0xFE,
        (
            "カウンターに立つものが\x01",
            "あんな腑抜けていてはイカン。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "どれ、いっちょう喝をいれてやるか。\x02",
    )

    CloseMessageWindow()

    label("loc_F95")

    Jump("loc_1906")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_102A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB5")
    Call(0, 7)
    Jump("loc_1025")

    label("loc_FB5")


    #C0020
    ChrTalk(
        0xFE,
        "ほほ、近年まれに見る繁盛じゃわい。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "去年の記念祭では\x01",
            "こうはいかんかったからのう。\x01",
            "ありがたいことじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1025")

    Jump("loc_1906")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10C8")

    #C0022
    ChrTalk(
        0xFE,
        (
            "ほほほ、観光客が土産として\x01",
            "沢山ハチミツを\x01",
            "買っていってくれてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "うちとしても大助かりじゃ。\x01",
            "デリックの案に乗って\x01",
            "正解じゃったのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1906")

    label("loc_10C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1167")

    #C0024
    ChrTalk(
        0xFE,
        (
            "記念祭の出店、\x01",
            "初日の売り上げは\x01",
            "なかなか好調だったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "《アルカンシェル》が\x01",
            "客を集めてくれたお陰じゃの。\x01",
            "ほっほっほ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11E4")

    label("loc_1167")


    #C0026
    ChrTalk(
        0xFE,
        (
            "《アルカンシェル》が\x01",
            "客を集めてくれたお陰で、\x01",
            "出店の出だしは好調じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "このまま最終日まで\x01",
            "行ってくれるといいが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E4")

    Jump("loc_1906")

    label("loc_11E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1204")
    Call(0, 7)
    Jump("loc_12AF")

    label("loc_1204")


    #C0028
    ChrTalk(
        0xFE,
        (
            "デリックめ、\x01",
            "なかなか話の出来る奴じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "次期村長の自覚が\x01",
            "しっかりできとるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "……ジェイクにも、店を継ぐ自覚を\x01",
            "しっかり持って欲しいもんじゃがのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AF")

    Jump("loc_1906")

    label("loc_12B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_13B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1368")

    #C0031
    ChrTalk(
        0xFE,
        (
            "デリックの奴が進めておる\x01",
            "創立記念祭の出店は良い考えじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "この村もだんだん昔のような活気が\x01",
            "なくなっておるし、\x01",
            "それもまたいいのかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13AD")

    label("loc_1368")


    #C0033
    ChrTalk(
        0xFE,
        (
            "村に活気を取り戻す為にも、\x01",
            "創立記念祭への出店は大いに結構じゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AD")

    Jump("loc_1906")

    label("loc_13B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_150A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1491")

    #C0034
    ChrTalk(
        0xFE,
        (
            "ふむ、今日は奥の農場から\x01",
            "ハチミツを仕入れてくるとするかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "本当ならジェイクにも\x01",
            "仕入れのイロハを\x01",
            "教えたいもんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "今は店番で一杯一杯じゃからな。\x01",
            "またの機会にするとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1505")

    label("loc_1491")


    #C0037
    ChrTalk(
        0xFE,
        (
            "モノを売るなら仕入れもきちんと\x01",
            "できなければイカン。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "ジェイクにも教えたいもんじゃが……\x01",
            "まだ早いかろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1505")

    Jump("loc_1906")

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_1615")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1525")
    Call(0, 6)
    Jump("loc_1610")

    label("loc_1525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B4")

    #C0039
    ChrTalk(
        0xFE,
        (
            "店は孫にさっさと継がせて\x01",
            "隠居しようと思っとってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "だがジェイクの奴、\x01",
            "中々仕事を覚えんでのう……\x01",
            "困ったもんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1610")

    label("loc_15B4")


    #C0041
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "出来が悪い孫を持つと大変じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "わしもそろそろ\x01",
            "隠居したいんじゃがの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1610")

    Jump("loc_1906")

    label("loc_1615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_180E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1764")

    #C0043
    ChrTalk(
        0xFE,
        (
            "例の狼騒ぎで、養蜂場が荒らされてな。\x01",
            "うちの店も大損というほどではないが\x01",
            "それなりの被害を被ったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "……考えてみるとそれも変じゃな。\x01",
            "魔獣の仕業だとしたら、それこそ\x01",
            "根こそぎやられてしまうこともあろうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "まぁ、運が良かったんじゃろうな。\x01",
            "空の女神に感謝、感謝じゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175C")
    SetScenarioFlags(0x68, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_175C")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1809")

    label("loc_1764")


    #C0046
    ChrTalk(
        0xFE,
        (
            "そういえば、あのハロルド君。\x01",
            "狼型魔獣の被害で一番大変な時に\x01",
            "商品を高く仕入れてくれてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "商売は誠実さと信用が第一。\x01",
            "まだ若いようだが、よくできた男じゃて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1809")

    Jump("loc_1906")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188A")

    #C0048
    ChrTalk(
        0xFE,
        "む、お客さんか。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "おすすめは村の特産物のハチミツじゃ。\x01",
            "なんぼでも買って行ってくだされ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1906")

    label("loc_188A")


    #C0050
    ChrTalk(
        0xFE,
        (
            "……おっと失礼。\x01",
            "買い物はカウンターで頼みますぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "出来の悪い孫が立っておりますが\x01",
            "どうか沢山買っていってくだされ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1906")

    TalkEnd(0xFE)
    Return()

    # Function_5_A14 end

    def Function_6_190A(): pass

    label("Function_6_190A")


    #C0052
    ChrTalk(
        0xFE,
        (
            "おお、お客さん……\x01",
            "突然だが、本は要らんかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "ハロルド君が仕入れのおまけにと\x01",
            "譲ってくれたものなのだが……\x01",
            "生憎、本を読む癖がなくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "読まん者より\x01",
            "読む者が持っていたほうが\x01",
            "この本も幸せじゃろう。\x02",
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
            "を受け取った。\x02",
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

    # Function_6_190A end

    def Function_7_1A2F(): pass

    label("Function_7_1A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A3D")
    Jump("loc_1CDF")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1A4B")
    Jump("loc_1CDF")

    label("loc_1A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A59")
    Jump("loc_1CDF")

    label("loc_1A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A67")
    Jump("loc_1CDF")

    label("loc_1A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B45")
    OP_4B(0x8, 0xFF)
    OP_4B(0x1A, 0xFF)
    TurnDirection(0x8, 0x1A, 0)
    TurnDirection(0x1A, 0x8, 0)

    #C0056
    ChrTalk(
        0x1A,
        (
            "共和国の家族に\x01",
            "お土産にしようと思ってね。\x01",
            "３瓶ほど包んでもらえるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "ふむふむ、それは\x01",
            "良いことですなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "では、お支払いはそちらの\x01",
            "カウンターでお願いしますじゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x1A, 0xFF)
    Jump("loc_1CDF")

    label("loc_1B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B53")
    Jump("loc_1CDF")

    label("loc_1B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B61")
    Jump("loc_1CDF")

    label("loc_1B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C9E")
    OP_4B(0x8, 0xFF)
    OP_4B(0x14, 0xFF)
    TurnDirection(0x8, 0x14, 0)
    TurnDirection(0x14, 0x8, 0)

    #C0059
    ChrTalk(
        0x14,
        (
            "ふむ……\x01",
            "これなら出店するのに\x01",
            "充分な量の商品が確保できますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "今年は獣の被害はあったが\x01",
            "収穫量はそれなりじゃったしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "だが売り子の用意や\x01",
            "他の商品、出店場所の確保……\x01",
            "考えることは一杯あるぞい。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x14,
        (
            "承知してます。\x01",
            "追々決めていきましょう。\x01",
            "それじゃ、次は……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x14, 0xFF)
    Jump("loc_1CDF")

    label("loc_1C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1CAC")
    Jump("loc_1CDF")

    label("loc_1CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1CBA")
    Jump("loc_1CDF")

    label("loc_1CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_1CC8")
    Jump("loc_1CDF")

    label("loc_1CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_1CD6")
    Jump("loc_1CDF")

    label("loc_1CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1CDF")

    label("loc_1CDF")

    SetScenarioFlags(0x0, 0)
    Return()

    # Function_7_1A2F end

    def Function_8_1CE3(): pass

    label("Function_8_1CE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9D")

    #C0063
    ChrTalk(
        0xFE,
        "いらっしゃ～い。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "ん～……今日もお客さんは\x01",
            "常連さんだけかあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "ねぇ、あなた達。\x01",
            "『メニューの上から下まで！』\x01",
            "……とか言ってみない？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#0006Fえーっと、遠慮しとくよ。\x01",
            "そんなに食べきれないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "ちぇっ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E95")

    #C0068
    ChrTalk(
        0x10A,
        (
            "#0601F（なんという接客態度だ……\x01",
            "  それでも喫茶店の店員なのか！？）\x02\x03",

            "#0603F（ええい、ここは一つ\x01",
            "  私がじきじきに指導して……）\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#0106F（お、落ち着いてくださいよ。）\x02",
    )

    CloseMessageWindow()

    label("loc_1E95")

    SetScenarioFlags(0x0, 1)
    Jump("loc_1F13")

    label("loc_1E9D")


    #C0070
    ChrTalk(
        0xFE,
        (
            "いい？　お客さん。\x01",
            "人間、羽振りが悪いとモテないわよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "ガツンと注文して、\x01",
            "うちの家計を助けてちょうだいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F13")

    Jump("loc_2992")

    label("loc_1F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_20A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200D")

    #C0072
    ChrTalk(
        0xFE,
        (
            "お父さんはのんびり店がやれればいい\x01",
            "みたいだけど、私は貧乏暮らしはいやなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "……はぁ、またデリックさんが\x01",
            "なにか計画してくれないかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "なんだかんだで\x01",
            "ここ最近で一番儲かったのは\x01",
            "記念祭の出店なんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20A0")

    label("loc_200D")


    #C0075
    ChrTalk(
        0xFE,
        (
            "記念祭のころはよかったなぁ。\x01",
            "忙しかったけどじゃんじゃん儲かったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "デリックさんが\x01",
            "村の改革を推し進めたい気持ちが\x01",
            "なんとなく分かったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A0")

    Jump("loc_2992")

    label("loc_20A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2171")

    #C0077
    ChrTalk(
        0xFE,
        (
            "今、２階の部屋に２人組の\x01",
            "遊撃士さんが来てるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "こうして見ると遊撃士さんって、\x01",
            "意外と女の人が多いわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "あたしも同じ女として、\x01",
            "思わず応援に熱が入るってもんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21B7")

    label("loc_2171")


    #C0080
    ChrTalk(
        0xFE,
        (
            "あとで遊撃士さんに\x01",
            "食後のコーヒーでも\x01",
            "サービスしてあげよっかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B7")

    Jump("loc_2992")

    label("loc_21BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_21CA")
    Jump("loc_2992")

    label("loc_21CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_21D8")
    Jump("loc_2992")

    label("loc_21D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21E6")
    Jump("loc_2992")

    label("loc_21E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_21F4")
    Jump("loc_2992")

    label("loc_21F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2393")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2317")
    OP_4B(0xA, 0xFF)

    #C0081
    ChrTalk(
        0xFE,
        (
            "創立記念祭かぁ～……\x01",
            "賑やかで楽しいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "うまくこっちにお客が流れてきたら\x01",
            "ガッポガッポ儲かるかもしれないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "うう、でも忙しくなるわね。\x01",
            "この繁盛してなさ加減に慣れてるから\x01",
            "苦労しそ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0084
    ChrTalk(
        0xA,
        "……おい、聞こえてるぞ。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_238E")

    label("loc_2317")


    #C0085
    ChrTalk(
        0xFE,
        (
            "いっつも大繁盛なら\x01",
            "忙しくなっても困らないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "ま、ごった返すほどは\x01",
            "お客も来ないでしょ。\x01",
            "……たぶん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238E")

    Jump("loc_2992")

    label("loc_2393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_251C")
    TurnDirection(0xFE, 0x13, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247F")
    OP_4B(0xA, 0xFF)

    #C0087
    ChrTalk(
        0xFE,
        (
            "へぇ～、クロスベル市から\x01",
            "わざわざ歩いてねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "まぁま、よかったら食べてってよ。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "うちのお父さんは顔は冴えないけど\x01",
            "料理はうまいんだから。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0090
    ChrTalk(
        0xA,
        "……おい、聞こえてるぞ。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2517")

    label("loc_247F")


    #C0091
    ChrTalk(
        0xFE,
        (
            "何だったらこの店で\x01",
            "いっちばん高いメニューを\x01",
            "頼んでみない？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "お父さんの自信作だから\x01",
            "うんまいわよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x13,
        (
            "……魅力的だけど、いい。\x01",
            "お金ないし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2517")

    Jump("loc_2992")

    label("loc_251C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2643")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D4")

    #C0094
    ChrTalk(
        0xFE,
        (
            "常連のアルフレッドさんは\x01",
            "お父さんと仲がいいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "お店がヒマなときを見計らって\x01",
            "よく話してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "こういうのって\x01",
            "自営業ならではの良さよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_263E")

    label("loc_25D4")


    #C0097
    ChrTalk(
        0xFE,
        (
            "アルフレッドさんは\x01",
            "お父さんと仲がいいみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "……正直、喋ってないで\x01",
            "仕事しろって感じだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_263E")

    Jump("loc_2992")

    label("loc_2643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_275B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D1")

    #C0099
    ChrTalk(
        0xFE,
        (
            "にしても……\x01",
            "アルフレッドさんもキースくんも\x01",
            "随分居座るなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "どうせなら\x01",
            "ガンガン注文してくれないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2756")

    label("loc_26D1")


    #C0101
    ChrTalk(
        0xFE,
        (
            "昼間は基本的に空いてるから\x01",
            "別に居座ってくれても\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "どうせなら注文してほしいもんだわ。\x01",
            "儲けに繋がらないしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2756")

    Jump("loc_2992")

    label("loc_275B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_2886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281D")

    #C0103
    ChrTalk(
        0xFE,
        (
            "ハロルドさんが\x01",
            "そろそろ帰るんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "ハロルドさんって素敵と思わない？\x01",
            "誠実で裏表が無いし。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "結婚してお子さんもいるなんて、\x01",
            "奥さんがうらやましいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2881")

    label("loc_281D")


    #C0106
    ChrTalk(
        0xFE,
        (
            "ハロルドさんなら\x01",
            "２階にとってある部屋に戻ってるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "はぁ……\x01",
            "次はいつ来てくれるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2881")

    Jump("loc_2992")

    label("loc_2886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2992")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2910")

    #C0108
    ChrTalk(
        0xFE,
        "いらっしゃ～い。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "……あら、初めてのお客さんね？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "ちょうど暇な時間帯なの。\x01",
            "ゆっくりしていってね㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2992")

    label("loc_2910")


    #C0111
    ChrTalk(
        0xFE,
        (
            "ウチのお父さんの料理は絶品よ。\x01",
            "良かったら食べて行ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "料理を食べれば体力も取り戻せるし、\x01",
            "いいこと尽くめなんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2992")

    TalkEnd(0xFE)
    Return()

    # Function_8_1CE3 end

    def Function_9_2996(): pass

    label("Function_9_2996")

    TalkBegin(0xFE)

    #C0113
    ChrTalk(
        0xC,
        (
            "なんだかややこしいことを\x01",
            "しちゃったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xC,
        (
            "親父さんにいいとこ\x01",
            "見せたかったけど\x01",
            "はやまっちゃったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "でもまぁ、警察だけじゃなくて\x01",
            "遊撃士もいた方が安心だよな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_2996 end

    def Function_10_2A4B(): pass

    label("Function_10_2A4B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2ADF")
    Jump("loc_2B29")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AFF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B29")

    label("loc_2AFF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B1F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B29")

    label("loc_2B1F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B29")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7D")

    #C0116
    ChrTalk(
        0xFE,
        (
            "シーリィちゃんの魅力は\x01",
            "変に可愛い子ぶってない所だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "俺たち常連客に高い注文させようと\x01",
            "するところなんか、\x01",
            "自分に正直でいいよな！\x02",
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
        "#0211F微妙に特殊な嗜好ですね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CCD")

    label("loc_2C7D")


    #C0119
    ChrTalk(
        0xFE,
        (
            "シーリィちゃんの魅力は\x01",
            "変に可愛い子ぶってない所や\x01",
            "自分に正直なところだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCD")

    Jump("loc_397F")

    label("loc_2CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2D75")

    #C0120
    ChrTalk(
        0xFE,
        (
            "コーヒーだけ頼んで居座ってたら\x01",
            "シーリィちゃんに\x01",
            "ハタキで叩かれちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "彼女、ミラが大好きだからなぁ……\x01",
            "しかたない、軽食でも頼むかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397F")

    label("loc_2D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E69")

    #C0122
    ChrTalk(
        0xFE,
        (
            "はぁ～……\x01",
            "やっぱりシーリィちゃんがいるこの店は\x01",
            "癒されるぜぇ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "記念祭で会えなかった分の寂しさを\x01",
            "存分に癒さなきゃなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#0006F……記念祭からもう１ヵ月は\x01",
            "経つんだけど……\x01",
            "まだ癒されてはいないのか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EB1")

    label("loc_2E69")


    #C0125
    ChrTalk(
        0xFE,
        (
            "はぁ～……\x01",
            "やっぱりシーリィちゃんがいるこの店は\x01",
            "癒されるぜぇ～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EB1")

    Jump("loc_397F")

    label("loc_2EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2FCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F45")

    #C0126
    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "はっ……死んでた。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "……元気出せ、俺。\x01",
            "明日になればシーリィちゃんが\x01",
            "帰ってくる……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FCA")

    label("loc_2F45")


    #C0129
    ChrTalk(
        0xFE,
        (
            "５日間もシーリィちゃん分を\x01",
            "摂取できないとは予想外だったが……\x01",
            "それも今日までだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "早く帰ってきてくれ～\x01",
            "シーリィちゃーん……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCA")

    Jump("loc_397F")

    label("loc_2FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3175")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_308E")

    #C0131
    ChrTalk(
        0xD,
        (
            "ま、あのカップルが\x01",
            "無事に戻ってきてよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xD,
        (
            "自分がクロスベル市に行ってる間に\x01",
            "店のお客さんに何かあったら、\x01",
            "シーリィちゃんが悲しむしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        "……多分。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3170")

    label("loc_308E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3110")

    #C0134
    ChrTalk(
        0xFE,
        (
            "親父さんとアルフレッドさんと\x01",
            "見慣れない観光客がいる店……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "足りないもの、それは……\x01",
            "シーリィちゃんだ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3170")

    label("loc_3110")


    #C0136
    ChrTalk(
        0xFE,
        (
            "シーリィちゃんが\x01",
            "いないと知りつつも\x01",
            "この店に来てしまう俺……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "……はぁ……むなしいぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_3170")

    Jump("loc_397F")

    label("loc_3175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3256")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3203")

    #C0138
    ChrTalk(
        0xFE,
        (
            "はぁ……\x01",
            "シーリィちゃんがいない……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "分かってはいたけど、\x01",
            "この空間がこんなに寂しいもの\x01",
            "だったなんてな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3251")

    label("loc_3203")


    #C0140
    ChrTalk(
        0xFE,
        (
            "あぁ、シーリィちゃん……\x01",
            "記念祭なんか早く終わらせて\x01",
            "帰ってきてくれー……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3251")

    Jump("loc_397F")

    label("loc_3256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_330B")

    #C0141
    ChrTalk(
        0xFE,
        (
            "ま、まさかシーリィちゃんが\x01",
            "出店に行っちゃうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "しかもデリックのやつと\x01",
            "二人きりで、だぜ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "くそっ、仕事が忙しくなきゃ\x01",
            "すぐにでも応援に行くのに！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397F")

    label("loc_330B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3412")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339E")

    #C0144
    ChrTalk(
        0xFE,
        (
            "はー、この店も観光客が来たら\x01",
            "混んじゃうんだろか……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "みんなシーリィちゃんの魅力に\x01",
            "とりつかれたらどうしよう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_340D")

    label("loc_339E")


    #C0146
    ChrTalk(
        0xFE,
        (
            "この店に新しい客が来たら、\x01",
            "きっとシーリィちゃんにホレちまう……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "……観光客なんて来なきゃいいのにな。\x02",
    )

    CloseMessageWindow()

    label("loc_340D")

    Jump("loc_397F")

    label("loc_3412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_35AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351E")

    #C0148
    ChrTalk(
        0xFE,
        (
            "シーリィちゃん……\x01",
            "どうやらハロルドさんに\x01",
            "憧れちゃってるらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "くそっ、既婚の優男なんかに\x01",
            "シーリィちゃんをとられてたまるか！\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "……って言いたいとこだけど、\x01",
            "ハロルドさんは良くしてくれるから\x01",
            "なんか悪く言えないんだよなー……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35A6")

    label("loc_351E")


    #C0151
    ChrTalk(
        0xFE,
        (
            "と、とにかく今は\x01",
            "毎日通ってシーリィちゃんとの\x01",
            "距離を縮めなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "でもなー……\x01",
            "恋敵がハロルドさんなんて\x01",
            "相手が悪すぎるぜ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A6")

    Jump("loc_397F")

    label("loc_35AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_36C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3657")

    #C0153
    ChrTalk(
        0xFE,
        (
            "はぁ～今日も可愛いぜ\x01",
            "シーリィちゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "……は？　狼型魔獣？\x01",
            "そんなことどうでもいいって。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "この俺の素敵時間を\x01",
            "邪魔しないでくんない？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36C4")

    label("loc_3657")


    #C0156
    ChrTalk(
        0xFE,
        (
            "はぁ～今日も可愛いぜ\x01",
            "シーリィちゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "この村が滅んでも\x01",
            "シーリィちゃんがいれば\x01",
            "生きていけるな、俺。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C4")

    Jump("loc_397F")

    label("loc_36C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_37F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3775")

    #C0158
    ChrTalk(
        0xFE,
        (
            "シーリィちゃんがいて\x01",
            "親父さんのウマイ料理があって……\x01",
            "やっぱこの店は至高の空間だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "……いい加減通いすぎて\x01",
            "お金が足りないんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37EB")

    label("loc_3775")


    #C0160
    ChrTalk(
        0xFE,
        (
            "なんかさっきから\x01",
            "シーリィちゃんの視線が痛いんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……仕方ない、追加注文するかなぁ。\x01",
            "今月厳しいけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EB")

    Jump("loc_397F")

    label("loc_37F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_393A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C9")

    #C0162
    ChrTalk(
        0xFE,
        (
            "ん～？\x01",
            "狼型魔獣の話ねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "ウチの管理してる畑も\x01",
            "それなりに被害があってさぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "しかも、誰も姿を見てないってんだから\x01",
            "よっぽど頭のいい魔獣なんだろうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C1")
    SetScenarioFlags(0x68, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38C1")

    SetScenarioFlags(0x0, 2)
    Jump("loc_3935")

    label("loc_38C9")


    #C0165
    ChrTalk(
        0xFE,
        (
            "ウチの管理してる麦畑も\x01",
            "それなりに被害があったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "ありゃ、立て直しが大変だったよ。\x01",
            "やれやれ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3935")

    Jump("loc_397F")

    label("loc_393A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_397F")

    #C0167
    ChrTalk(
        0xFE,
        "シーリィちゃん、やっぱ可愛いぜ。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "笑顔がたまらん！\x02",
    )

    CloseMessageWindow()

    label("loc_397F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_2A4B end

    def Function_11_3987(): pass

    label("Function_11_3987")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A1B")
    Jump("loc_3A65")

    label("loc_3A1B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A3B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A65")

    label("loc_3A3B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A5B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A65")

    label("loc_3A5B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A65")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B68")

    #C0169
    ChrTalk(
        0xFE,
        (
            "ううむ、まさか本が巡り巡って\x01",
            "そんなところに……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "いや、全ての発端は\x01",
            "私が又貸しなどしてしまったからだな。\x01",
            "本当にすまなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "今度からはきちんと\x01",
            "返却期限を守るようにするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3B68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C1E")

    #C0172
    ChrTalk(
        0xFE,
        (
            "ゴーファンが本を貸したのは、\x01",
            "いつも村の入り口で\x01",
            "導力車をいじっているエルキン君だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "いや、本当にすまないな。\x01",
            "手間をかけさせてしまって……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3C1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C3F")
    Call(0, 42)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D2B")
    OP_4B(0xA, 0xFF)

    #C0174
    ChrTalk(
        0xFE,
        (
            "《賭博師ジャック》……\x01",
            "なかなか面白い本だったよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0175
    ChrTalk(
        0xA,
        "おぉ、読み終わったか。\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xA,
        (
            "僕もその小説のファンでな、\x01",
            "店が終わったら\x01",
            "色々と話そうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        "ああ、楽しみにしておこう。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DA5")

    label("loc_3D2B")


    #C0178
    ChrTalk(
        0xFE,
        (
            "どれ、もう一度最初から\x01",
            "読み返してみるとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "やれやれ、他にも本を借りてるのに\x01",
            "読む時間がつくれそうにないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA5")

    Jump("loc_4DE7")

    label("loc_3DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F06")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0180
    ChrTalk(
        0xFE,
        (
            "《賭博師ジャック》……\x01",
            "なかなかスリルのある本だ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0181
    ChrTalk(
        0xA,
        (
            "その本なら僕も知ってるよ。\x01",
            "たしか結末はジャックが──\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "おい、悪い癖だぞゴーファン。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "物語の結末を言おうとするなんて\x01",
            "不粋にも程がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "まったく、俺が何度それで\x01",
            "泣きを見たことか……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "す、すまない。\x01",
            "黙っているとするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F89")

    label("loc_3F06")


    #C0186
    ChrTalk(
        0xFE,
        (
            "物語の結末や核心を\x01",
            "人に聞かされることほど\x01",
            "不快なことはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "いくら親友のゴーファンでも\x01",
            "それだけはやめてほしいものだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F89")

    Jump("loc_4DE7")

    label("loc_3F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4049")

    #C0188
    ChrTalk(
        0xFE,
        (
            "クロスベル市の図書館で\x01",
            "色々と本を借りてきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "あそこにはいい本がたくさんあるんで\x01",
            "ついつい沢山借りすぎてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "返却期限までの３日間で\x01",
            "読破できるかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DE7")

    label("loc_4049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_412F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D7")

    #C0191
    ChrTalk(
        0xFE,
        (
            "店も落ち着いてきたし、\x01",
            "借りてきた本も\x01",
            "もう読んでしまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "今日くらいは\x01",
            "ゆっくり食事をとるとするかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_412A")

    label("loc_40D7")


    #C0193
    ChrTalk(
        0xFE,
        "本の返却は……明日でいいか。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "今日のクロスベル市は\x01",
            "混雑してそうだしな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_412A")

    Jump("loc_4DE7")

    label("loc_412F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4396")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41C0")

    #C0195
    ChrTalk(
        0xE,
        (
            "ふぅ……\x01",
            "ようやく一息ついたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xE,
        (
            "やれやれ、ゴーファンめ。\x01",
            "いくら友達だからって\x01",
            "あまりこき使わないでほしいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4391")

    label("loc_41C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4305")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0197
    ChrTalk(
        0xFE,
        "ふむ……ふむふむ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0198
    ChrTalk(
        0xA,
        (
            "アルフ、まだ読んでたのか……\x01",
            "『アルカンシェル・ファンブック』。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        "そんなに面白い本なのか？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "希少な本らしいから\x01",
            "返却する前に\x01",
            "充分に堪能しようと思ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "しかし、\x01",
            "このイリア・プラティエの\x01",
            "写真はいいものだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xA,
        "……ほどほどにしとけよ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_4391")

    label("loc_4305")


    #C0203
    ChrTalk(
        0xFE,
        (
            "ふむふむ……\x01",
            "期待の新星『リーシャ・マオ』が\x01",
            "入団する前の本のようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "是非彼女の写真も\x01",
            "見たかったものだが……\x01",
            "残念でならないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4391")

    Jump("loc_4DE7")

    label("loc_4396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C4")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0205
    ChrTalk(
        0xFE,
        (
            "『アルカンシェル・ファンブック』……\x01",
            "なかなか珍しい本を見つけたよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0206
    ChrTalk(
        0xA,
        (
            "ほう……\x01",
            "そんな本が出ていたとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "有志が集まって\x01",
            "作られた本らしくてね。\x01",
            "発行部数自体少ないらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "……図書館に返すのが\x01",
            "惜しくなってきたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xA,
        "おいおい……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_452C")

    label("loc_44C4")


    #C0210
    ChrTalk(
        0xFE,
        (
            "人気の本らしいから\x01",
            "また借りられるかもわからない。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "仕方ない、\x01",
            "じっくり読ませてもらうとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_452C")

    Jump("loc_4DE7")

    label("loc_4531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4615")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45AE")

    #C0212
    ChrTalk(
        0xFE,
        (
            "こっちの仕事のめども\x01",
            "そろそろつきそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "僕も後でクロスベル市を\x01",
            "覗きに行ってみるか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4610")

    label("loc_45AE")


    #C0214
    ChrTalk(
        0xFE,
        (
            "後でクロスベル市を\x01",
            "覗きに行ってみようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "新しい本を\x01",
            "借りに行きたかったところだしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4610")

    Jump("loc_4DE7")

    label("loc_4615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_478C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4725")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0216
    ChrTalk(
        0xFE,
        (
            "《日常猫語会話入門》……\x01",
            "こいつはおもしろい。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "にゃ～～ご。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "にゃーお。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "にゃあ～～。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0220
    ChrTalk(
        0xA,
        (
            "……おい、アルフよ。\x01",
            "失礼なことを言ってないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "はは、今の意味を知りたいなら\x01",
            "君も読んでみたらいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_4787")

    label("loc_4725")


    #C0222
    ChrTalk(
        0xFE,
        (
            "さて、記念祭中も\x01",
            "図書館は開くのだろうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "新しい本が借りられないと\x01",
            "つまらないからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4787")

    Jump("loc_4DE7")

    label("loc_478C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_494F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F7")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0224
    ChrTalk(
        0xFE,
        (
            "《カーネリア》……\x01",
            "ふむふむ、興味深い本だ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0225
    ChrTalk(
        0xA,
        (
            "それに関しては\x01",
            "一時期話題になってるのを\x01",
            "見たことがあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xA,
        (
            "なんでも実話かもしれん、\x01",
            "という噂なんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "だとしたらそれはそれで\x01",
            "面白いかもしれんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "純粋に面白い小説がここにある。\x01",
            "それだけでいいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xA,
        "僕は結構気になるけどなぁ……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_494A")

    label("loc_48F7")


    #C0230
    ChrTalk(
        0xFE,
        "さて、次はどんな本を読むかな。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "少し変わった本を\x01",
            "読んでみたいものだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_494A")

    Jump("loc_4DE7")

    label("loc_494F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA6")
    SetChrSubChip(0xFE, 0x0)
    OP_4B(0xA, 0xFF)

    #C0232
    ChrTalk(
        0xFE,
        (
            "《クロスベル市\x01",
            "  良質飲食店特集》……\x01",
            "ふむふむ、中々いい店が載ってる。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xE, 500)

    #C0233
    ChrTalk(
        0xA,
        (
            "……おい、アルフ。\x01",
            "少しは気を遣ってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "フフ……この店も載れるように\x01",
            "がんばったらいいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xA,
        (
            "その本は市街地限定だろ？\x01",
            "載ってなくても\x01",
            "僕の料理だってきっと負けてないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "はは、言うねぇ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B2C")

    label("loc_4AA6")


    #C0237
    ChrTalk(
        0xFE,
        (
            "さて、次は……\x01",
            "小説に手を出してみるのも\x01",
            "いいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "また暇が空いたときに\x01",
            "クロスベル市の図書館へ\x01",
            "足を運ぶとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B2C")

    Jump("loc_4DE7")

    label("loc_4B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_4C56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF2")

    #C0239
    ChrTalk(
        0xFE,
        (
            "さて、この間クロスベル市の\x01",
            "図書館で借りてきた本でも\x01",
            "読むとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "《クロスベル市\x01",
            "  良質飲食店特集》……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "……はは、\x01",
            "ここで読むには配慮が足りないかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C51")

    label("loc_4BF2")


    #C0242
    ChrTalk(
        0xFE,
        (
            "クロスベル市の図書館は\x01",
            "色々な本が揃ってて面白いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        "君たちも一度行ってみたらどうだ？\x02",
    )

    CloseMessageWindow()

    label("loc_4C51")

    Jump("loc_4DE7")

    label("loc_4C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_4DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C71")
    Call(0, 12)
    Jump("loc_4DD9")

    label("loc_4C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D66")

    #C0244
    ChrTalk(
        0xFE,
        (
            "あの時はたまたま、\x01",
            "どの家も次の日の仕事が早くてね。\x01",
            "みんな早くに寝静まってしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xE,
        (
            "#1Pそこに、まるで狙ったかのような\x01",
            "タイミングで魔獣が現れてしまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "とにかく運が悪かった、\x01",
            "としか言いようがないかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DD9")

    label("loc_4D66")


    #C0247
    ChrTalk(
        0xFE,
        (
            "各家の被害は\x01",
            "そこまで大きく無かった。\x01",
            "それは不幸中の幸いだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "もうあんなことは\x01",
            "無い様にしたいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DD9")

    Jump("loc_4DE7")

    label("loc_4DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4DE7")

    label("loc_4DE7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_3987 end

    def Function_12_4DEF(): pass

    label("Function_12_4DEF")

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
        "#5Pもぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xE,
        (
            "#5P……うん、うまい。\x01",
            "ゴーファンのオムライスは\x01",
            "本当に絶品だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xA,
        (
            "#11Pはは、そう言ってもらえると\x01",
            "作った甲斐があるってもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        "#0000F#6Pあの、すみません。\x02",
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
        "#11Pおや、どうしたね？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#0003F#6P自分たちはクロスベル市の\x01",
            "警察の者なんですが……\x02\x03",

            "#0001F以前起こったという\x01",
            "狼型魔獣の被害について\x01",
            "お話を聞いてもいいでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xE,
        (
            "#5P３週間前のあの事件のことか。\x01",
            "うん、そうだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xE,
        (
            "#5Pあの時はたまたまどの家も\x01",
            "次の日の仕事が早くてね。\x01",
            "みんな早くに寝静まってしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xE,
        (
            "#5Pそこに、まるで狙ったかのような\x01",
            "タイミングで魔獣が現れてしまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        (
            "#5Pとにかく運が悪かった、\x01",
            "としか言いようがないかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xA,
        "#11P僕も似たような事しか言えないねぇ。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xA,
        (
            "#11Pその日宿泊していた人達も\x01",
            "何も見ていないって言っていたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        "#0106F#6Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x104,
        (
            "#0306F#6P決定的な証拠ってのは\x01",
            "なかなかないもんだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        (
            "#0002F#5Pまぁ、そんなもんさ。\x01",
            "聞き込みは粘り強くやって\x01",
            "ようやく実を結ぶものだしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x103,
        (
            "#0206F#6Pとりあえず……\x01",
            "一旦休憩としませんか？\x02\x03",

            "#0211Fそろそろ空腹が限界です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0265
    ChrTalk(
        0xA,
        (
            "#11Pなんだ君たち、\x01",
            "昼食はまだだったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xA,
        (
            "#11Pよし、せっかくだし\x01",
            "当店自慢のオムライスを\x01",
            "ご馳走してあげよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#0011F#6Pいえ、そんな！\x01",
            "さすがにご馳走になるわけには……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xA,
        "#11Pま、お近づきの印にってやつさ。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "#11P代わりと言っちゃなんだが、\x01",
            "今度村に来たときには\x01",
            "またウチに食べに来てくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x104,
        "#0309F#6Pははっ、太っ腹だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x102,
        (
            "#0102F#6Pロイド、せっかくこう言って\x01",
            "下さってるのだし……\x01",
            "甘えさせていただきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x103,
        "#0204F#6P賛成です。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#0006F#6Pう、う～ん……そうだな。\x02\x03",

            "#0002Fそれじゃあ、よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        "#11Pよしきた。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xA,
        (
            "#11Pそれじゃ、空いている席に座って\x01",
            "待っててくれよ。\x02",
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
            "しばらくして、ロイドたちの座る席に\x01",
            "出来たてのオムライスが運ばれてきた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "農村ならではの素朴な味を堪能し、\x01",
            "ロイドたちは街道を歩いた疲れを充分に癒せた。\x07\x00\x02",
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

    # Function_12_4DEF end

    def Function_13_566F(): pass

    label("Function_13_566F")

    TalkBegin(0xFE)

    #C0278
    ChrTalk(
        0xFE,
        (
            "ステファンったら\x01",
            "普段運動不足なのに\x01",
            "走り回っちゃうから……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        "ふふ、それでも安心したわ。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "この村の子といい友達に\x01",
            "なれたみたいだからね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_566F end

    def Function_14_5709(): pass

    label("Function_14_5709")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_579D")
    Jump("loc_57E7")

    label("loc_579D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57BD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57E7")

    label("loc_57BD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57DD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57E7")

    label("loc_57DD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57E7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_593F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58CC")

    #C0281
    ChrTalk(
        0xFE,
        (
            "ステファン、今日もカミーユくんの所に\x01",
            "遊びに行ってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "クロスベル市にいたときは\x01",
            "かなりのもやしっ子だったのに……\x01",
            "ふふ、環境が変えてくれたのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_593A")

    label("loc_58CC")


    #C0283
    ChrTalk(
        0xFE,
        (
            "ステファンが外で遊ぶようになって\x01",
            "私も嬉しいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "アンジェさんトコには\x01",
            "今度お礼を言いに行かないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_593A")

    Jump("loc_612A")

    label("loc_593F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_594D")
    Jump("loc_612A")

    label("loc_594D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_59D9")

    #C0285
    ChrTalk(
        0xFE,
        (
            "ステファン、最近は\x01",
            "村の子供たちとよく遊んでるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "この村に正式に引っ越せるのも\x01",
            "そう遠くない話かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_612A")

    label("loc_59D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5B3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AAB")

    #C0287
    ChrTalk(
        0xFE,
        (
            "創立記念祭も終わるし、\x01",
            "閉会式で混む前に\x01",
            "こっちに戻ってきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "楽しかったけど、\x01",
            "やっぱり凄く混んでたから\x01",
            "疲れちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "はぁ～、この村の空気には\x01",
            "やっぱり癒されるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5B3A")

    label("loc_5AAB")


    #C0290
    ChrTalk(
        0xFE,
        (
            "ステファンは村の子供たちに\x01",
            "お土産を渡してくるって言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "……なんだか意外ね。\x01",
            "あの子もやっと村を\x01",
            "気に入ってくれたのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B3A")

    Jump("loc_612A")

    label("loc_5B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5B4D")
    Jump("loc_612A")

    label("loc_5B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5B5B")
    Jump("loc_612A")

    label("loc_5B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5B69")
    Jump("loc_612A")

    label("loc_5B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5C3B")

    #C0292
    ChrTalk(
        0xFE,
        (
            "村で出す出店っていうの、\x01",
            "どんなものになるか楽しみだわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "この子も随分クロスベル市に\x01",
            "帰りたがってるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "随分長く滞在したけど、\x01",
            "いい機会だから\x01",
            "一度戻ってみるのもいいかもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_612A")

    label("loc_5C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D09")

    #C0295
    ChrTalk(
        0xFE,
        (
            "《アルカンシェル》かぁ……\x01",
            "何度か行ったことがあるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "イリア・プラティエの舞台ときたら、\x01",
            "空の女神も真っ青ってくらい\x01",
            "モノすごいのよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "うーん、また行きたいわねぇ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5D7F")

    label("loc_5D09")


    #C0298
    ChrTalk(
        0xFE,
        (
            "イリア・プラティエの舞台……㈱\x01",
            "あぁ、前に一度見た時の感動を\x01",
            "思い出しちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        "うーん、また行きたいわねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_5D7F")

    Jump("loc_612A")

    label("loc_5D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5EDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E65")

    #C0300
    ChrTalk(
        0xFE,
        (
            "私達、この村に引っ越そうか\x01",
            "本気で迷っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "そしたら、こちらの主人が\x01",
            "『部屋が空いてるから』って\x01",
            "格安で部屋を借してくれたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "ふふ、都会ではこういうことって\x01",
            "なかなか無いわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5ED7")

    label("loc_5E65")


    #C0303
    ChrTalk(
        0xFE,
        (
            "私達、この村に引っ越そうか\x01",
            "本気で迷っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "主人のご厚意のおかげで\x01",
            "長く滞在できそうでよかったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ED7")

    Jump("loc_612A")

    label("loc_5EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_5F93")

    #C0305
    ChrTalk(
        0xFE,
        (
            "うーん、田舎暮らしは\x01",
            "夢だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "これからも魔獣被害が起こるようなら\x01",
            "クロスベル市にいた方が安全かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "それでもこの穏やかな暮らしは\x01",
            "捨てがたいし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_612A")

    label("loc_5F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_604B")

    #C0308
    ChrTalk(
        0xFE,
        (
            "あの騒動にはビックリしたわ。\x01",
            "静かでいい夜が明けたと思ったら\x01",
            "あんなことが起こってるんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "いくら田舎と言っても\x01",
            "魔獣が人の集落に入ってくるなんて\x01",
            "不気味よね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_612A")

    label("loc_604B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_612A")

    #C0310
    ChrTalk(
        0xFE,
        (
            "あら、あなた達も\x01",
            "クロスベル市から来たの？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "わたし達、ちょっと前から\x01",
            "ここに滞在してるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "都会の喧騒の無い穏やかな生活……\x01",
            "うーん、憧れの生活が今ここに。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "やっぱりこっちに\x01",
            "引っ越してこようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_612A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_5709 end

    def Function_15_6132(): pass

    label("Function_15_6132")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6143")
    Jump("loc_66A3")

    label("loc_6143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6151")
    Jump("loc_66A3")

    label("loc_6151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_615F")
    Jump("loc_66A3")

    label("loc_615F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_616D")
    Jump("loc_66A3")

    label("loc_616D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_617B")
    Jump("loc_66A3")

    label("loc_617B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6189")
    Jump("loc_66A3")

    label("loc_6189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6197")
    Jump("loc_66A3")

    label("loc_6197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6233")

    #C0314
    ChrTalk(
        0xFE,
        (
            "創立記念祭のために\x01",
            "一度クロスベル市に\x01",
            "戻るかもしれないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "そのまま村への引越しも\x01",
            "思い直してくれたらいいけど……\x01",
            "無理だろうなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66A3")

    label("loc_6233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_638B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_632D")

    #C0316
    ChrTalk(
        0xFE,
        (
            "広場で兄妹が遊んでるだろ？\x01",
            "よく遊びに誘いに来るけど\x01",
            "なんだか気乗りしなくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "何かと思えば\x01",
            "『ブレイサーごっこやろう』だよ。\x01",
            "やってらんないって。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "やっぱ田舎の子はガキだなぁ。\x01",
            "はぁ、クロスベル市に帰りたいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6386")

    label("loc_632D")


    #C0319
    ChrTalk(
        0xFE,
        (
            "同じくらいの歳でも、\x01",
            "やっぱ田舎の子はガキだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "クロスベル市に帰りたいなぁ……\x02",
    )

    CloseMessageWindow()

    label("loc_6386")

    Jump("loc_66A3")

    label("loc_638B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_644E")

    #C0321
    ChrTalk(
        0xFE,
        (
            "この村の人……\x01",
            "お人好し過ぎるよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "引っ越してくるかもしれないってだけで\x01",
            "まるでもう村の人間みたいに扱ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "僕は引っ越したくないんだけど\x01",
            "なんだか調子狂っちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66A3")

    label("loc_644E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_64F6")

    #C0324
    ChrTalk(
        0xFE,
        (
            "お母さん、狼魔獣事件のせいで\x01",
            "引越しをためらってるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "あまり悩みを溜めないタイプだからなぁ。\x01",
            "明日にはコロッと忘れちゃうんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66A3")

    label("loc_64F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_65B6")

    #C0326
    ChrTalk(
        0xFE,
        (
            "ていうか、信じられないよね。\x01",
            "狼型魔獣が忍び込んでくるなんて\x01",
            "クロスベル市ならまず起きない事件だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "はぁ、やだやだ。\x01",
            "どーしてお母さんはこんな所に\x01",
            "引っ越したいんだろ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66A3")

    label("loc_65B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_66A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6639")

    #C0328
    ChrTalk(
        0xFE,
        (
            "はぁ……\x01",
            "信じらんないよ、この田舎加減。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "あーあ、どうせならミシュラムの方に\x01",
            "引っ越したいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66A3")

    label("loc_6639")


    #C0330
    ChrTalk(
        0xFE,
        (
            "デパートも劇場も無いし\x01",
            "こないだはあんな騒ぎが起きるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "はぁあ。\x01",
            "クロスベル市に帰りたいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A3")

    TalkEnd(0xFE)
    Return()

    # Function_15_6132 end

    def Function_16_66A7(): pass

    label("Function_16_66A7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_673B")
    Jump("loc_6785")

    label("loc_673B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_675B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6785")

    label("loc_675B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_677B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6785")

    label("loc_677B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6785")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_683A")

    #C0332
    ChrTalk(
        0xFE,
        "いててて……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "昨日あれくらい走っただけで\x01",
            "こんなことになるなんて\x01",
            "情けないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        "……でも、昨日は楽しかったなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_685C")

    label("loc_683A")


    #C0335
    ChrTalk(
        0xFE,
        "……昨日は楽しかったなぁ……\x02",
    )

    CloseMessageWindow()

    label("loc_685C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_66A7 end

    def Function_17_6864(): pass

    label("Function_17_6864")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_68F8")
    Jump("loc_6942")

    label("loc_68F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6918")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6942")

    label("loc_6918")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6938")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6942")

    label("loc_6938")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6942")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0336
    ChrTalk(
        0xFE,
        (
            "牧草のにおいと……\x01",
            "それにニワトリと蜂蜜のにおいに\x01",
            "誘われてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "きっとおいしいものがあるに違いない。\x01",
            "……何か頼んでみようかな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_6864 end

    def Function_18_69FC(): pass

    label("Function_18_69FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A11")
    Call(0, 7)
    Jump("loc_6A8F")

    label("loc_6A11")


    #C0338
    ChrTalk(
        0xFE,
        (
            "ふむ……出店を出すというのも\x01",
            "なかなか大変なものだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "だが村に活気を与える為にも、\x01",
            "かならず成し遂げて見せるぞ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A8F")

    TalkEnd(0xFE)
    Return()

    # Function_18_69FC end

    def Function_19_6A93(): pass

    label("Function_19_6A93")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6B27")
    Jump("loc_6B71")

    label("loc_6B27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B71")

    label("loc_6B47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B67")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B71")

    label("loc_6B67")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B71")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0340
    ChrTalk(
        0xFE,
        (
            "さてと、腹ごしらえも\x01",
            "済んだっすし。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "そろそろ釣り糸を\x01",
            "垂れるっすかねー。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_6A93 end

    def Function_20_6BF0(): pass

    label("Function_20_6BF0")

    TalkBegin(0xFE)

    #C0342
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "やはりなかなかいい所だね、\x01",
            "この村は。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "将来はこんな静かな場所で\x01",
            "ゆっくりと余生を\x01",
            "過ごしたいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_6BF0 end

    def Function_21_6C6F(): pass

    label("Function_21_6C6F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D03")
    Jump("loc_6D4D")

    label("loc_6D03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6D23")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D4D")

    label("loc_6D23")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D43")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D4D")

    label("loc_6D43")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D4D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6EEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4C")

    #C0344
    ChrTalk(
        0xFE,
        (
            "今日、共和国に帰るつもり\x01",
            "なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "彼女が昨日から、\x01",
            "クロスベルに居たいって\x01",
            "聞かないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "くぅ、スコットとかいう遊撃士め……\x01",
            "僕の見ていない間に\x01",
            "彼女になにをしたんだ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6EE5")

    label("loc_6E4C")


    #C0347
    ChrTalk(
        0xFE,
        (
            "彼女を置いていってしまった\x01",
            "ツケが、こんなところで……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "とにかく、無理矢理にでも\x01",
            "共和国に連れて帰らないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "絶対に惚れ直させて\x01",
            "やるからな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EE5")

    Jump("loc_7092")

    label("loc_6EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F73")

    #C0350
    ChrTalk(
        0xFE,
        (
            "あ……\x01",
            "さっき言い忘れてたけど、\x01",
            "助けてくれてありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "君たちがいなかったら、\x01",
            "今頃……ぞぞっ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6FE2")

    label("loc_6F73")


    #C0352
    ChrTalk(
        0xFE,
        (
            "そ、それよりも……\x01",
            "なんだかさっきから\x01",
            "彼女の様子が変なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "顔が赤いけど……\x01",
            "どうしたっていうんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FE2")

    Jump("loc_7092")

    label("loc_6FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7065")

    #C0354
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "クロスベル市の出店でも食べたけど、\x01",
            "こっちの方が断然美味しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "いやぁ、来てよかったよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7092")

    label("loc_7065")


    #C0356
    ChrTalk(
        0xFE,
        (
            "うん、美味い美味い。\x01",
            "来てよかったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7092")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_6C6F end

    def Function_22_709A(): pass

    label("Function_22_709A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7148")

    #C0357
    ChrTalk(
        0xFE,
        (
            "村長さんの家の横から見える\x01",
            "畑の風景……すごかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "クロスベル市で宿をとっていたら\x01",
            "まず味わえなかったわよね。\x01",
            "ふふ、こっちに来てよかった。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_71B8")

    label("loc_7148")


    #C0359
    ChrTalk(
        0xFE,
        (
            "クロスベル市は\x01",
            "今も賑やかにしてるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "私あんまり人ごみ好きじゃないし……\x01",
            "こっちに来て良かったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71B8")

    TalkEnd(0xFE)
    Return()

    # Function_22_709A end

    def Function_23_71BC(): pass

    label("Function_23_71BC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7250")
    Jump("loc_729A")

    label("loc_7250")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7270")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_729A")

    label("loc_7270")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7290")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_729A")

    label("loc_7290")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_729A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7412")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73BD")

    #C0361
    ChrTalk(
        0xFE,
        (
            "ちょっと、スコットさんのこと\x01",
            "悪く言うのやめてよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "私を置いてさっさと\x01",
            "逃げちゃったあなたより\x01",
            "何倍も男らしいんだから！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x17,
        (
            "だ、だからそれは\x01",
            "誤解だって言ってるだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x17,
        (
            "なぁ、たのむから一緒に\x01",
            "共和国に帰ろうよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_740D")

    label("loc_73BD")


    #C0365
    ChrTalk(
        0xFE,
        (
            "はぁ……\x01",
            "共和国に帰ったら\x01",
            "スコットさんにはもう……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        "帰りたくな～い……\x02",
    )

    CloseMessageWindow()

    label("loc_740D")

    Jump("loc_753C")

    label("loc_7412")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_74D7")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_749B")

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
            "スコットさん、\x01",
            "って言うのかぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        "…………㈱\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x17,
        "何そのハートマーク！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_74D2")

    label("loc_749B")


    #C0371
    ChrTalk(
        0xFE,
        (
            "スコットさん、\x01",
            "って言うのかぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "…………㈱\x02",
    )

    CloseMessageWindow()

    label("loc_74D2")

    Jump("loc_753C")

    label("loc_74D7")


    #C0373
    ChrTalk(
        0xFE,
        (
            "主人ったら、よっぽどここの料理を\x01",
            "気に入っちゃったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        "ふふ、来年も来ようかしら。\x02",
    )

    CloseMessageWindow()

    label("loc_753C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_71BC end

    def Function_24_7544(): pass

    label("Function_24_7544")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7559")
    Call(0, 7)
    Jump("loc_75E4")

    label("loc_7559")


    #C0375
    ChrTalk(
        0xFE,
        (
            "昨日、養蜂場の話を聞いたら、\x01",
            "無性にハチミツが\x01",
            "欲しくなってしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "さて、後はどうやって持って帰るかな。\x01",
            "……重いだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75E4")

    TalkEnd(0xFE)
    Return()

    # Function_24_7544 end

    def Function_25_75E8(): pass

    label("Function_25_75E8")

    Call(0, 26)
    Return()

    # Function_25_75E8 end

    def Function_26_75EC(): pass

    label("Function_26_75EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7605")
    Call(0, 39)
    Return()

    label("loc_7605")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7612")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_878D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7685")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7685")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76A5")
    OP_AF(0x48)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8788")

    label("loc_76A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76C5")
    OP_AF(0x46)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8788")

    label("loc_76C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76D9")
    Jump("loc_8788")

    label("loc_76D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8788")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7780")

    #C0377
    ChrTalk(
        0xA,
        (
            "本が見つかってくれて\x01",
            "僕もひと安心だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xA,
        (
            "借りたものを貸すなんてことは\x01",
            "今後はしないように気を付けるよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_7780")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_780E")

    #C0379
    ChrTalk(
        0xA,
        (
            "エルキン君に又貸ししたのは\x01",
            "本当にすまないと思っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xA,
        (
            "どうも、お客さんに頼まれると\x01",
            "断りきれなくてねぇ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    label("loc_780E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_79A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_790E")

    #C0381
    ChrTalk(
        0xA,
        (
            "やぁ、いらっしゃい。\x01",
            "モーニングでもいかがかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xC,
        (
            "親父さ～ん、\x01",
            "俺、いつものね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xC, 500)

    #C0383
    ChrTalk(
        0xA,
        (
            "こらこら、今はこちらのお客さんの\x01",
            "注文を聞いてるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x0, 500)

    #C0384
    ChrTalk(
        0xA,
        (
            "……いや、すまんね。\x01",
            "注文が決まったらいつでも\x01",
            "言ってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_79A1")

    label("loc_790E")


    #C0385
    ChrTalk(
        0xA,
        (
            "キース君やアルフのやつは\x01",
            "注文するときは大体『いつもの』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xA,
        (
            "それが通じるくらい\x01",
            "通ってもらってるってことだから\x01",
            "こっちとしては嬉しいよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79A1")

    Jump("loc_8788")

    label("loc_79A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A73")

    #C0387
    ChrTalk(
        0xA,
        (
            "村人がのんびりできる場所を……\x01",
            "そんな風に思って店を開いたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xA,
        "だから、必要以上の儲けはいらないよ。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xA,
        (
            "……まぁ、こんなことを言うと\x01",
            "シーリィには怒られてしまうがね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7B17")

    label("loc_7A73")


    #C0390
    ChrTalk(
        0xA,
        (
            "必要以上に儲からなくてもいいと\x01",
            "僕は思っているんだが\x01",
            "シーリィには大不評でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xA,
        (
            "……まぁ、娘まで\x01",
            "儲けなくていいなんて言ってたら\x01",
            "とっくにこの店潰れてるよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B17")

    Jump("loc_8788")

    label("loc_7B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7BB4")

    #C0392
    ChrTalk(
        0xA,
        (
            "２階に部屋をとっているアレサさん親子は\x01",
            "本当に村を気に入ってくれたようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xA,
        (
            "長期滞在になったけど、\x01",
            "村の仲間が増えるなら大歓迎さ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8788")

    label("loc_7BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C41")

    #C0394
    ChrTalk(
        0xA,
        (
            "ようやく観光客の数も\x01",
            "落ち着いてきた感じだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xA,
        (
            "色んな人に料理を食べてもらえて、\x01",
            "僕としては楽しかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7CBC")

    label("loc_7C41")


    #C0396
    ChrTalk(
        0xA,
        (
            "さーて、シーリィも\x01",
            "出店が終わったら帰ってくるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xA,
        (
            "明日からはまた、\x01",
            "いつもどおり常連さん相手に\x01",
            "頑張らないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CBC")

    Jump("loc_8788")

    label("loc_7CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7E66")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D46")

    #C0398
    ChrTalk(
        0xA,
        (
            "大事なお客さんを\x01",
            "無事に連れ戻してくれて\x01",
            "ありがとうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xA,
        (
            "また何かあったら\x01",
            "よろしくおねがいするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E61")

    label("loc_7D46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_7DC9")

    #C0400
    ChrTalk(
        0xA,
        (
            "古戦場へは、\x01",
            "アルモリカ古道の途中の\x01",
            "石橋を渡ればすぐだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xA,
        (
            "観光客たちのこと……\x01",
            "どうかよろしくたのむよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E61")

    label("loc_7DC9")


    #C0402
    ChrTalk(
        0xA,
        (
            "どうも、観光記念とか言って\x01",
            "勝手に養蜂場に入るような人が\x01",
            "いるらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xA,
        (
            "農場や養蜂場には\x01",
            "危険なものも多いから、\x01",
            "気をつけて欲しいんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E61")

    Jump("loc_8788")

    label("loc_7E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EF6")

    #C0404
    ChrTalk(
        0xA,
        (
            "昨日から観光の人が\x01",
            "何人か泊まっててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xA,
        (
            "いつもならハロルドさんたち\x01",
            "商人が多いから\x01",
            "ちょっと新鮮な気分だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7F88")

    label("loc_7EF6")


    #C0406
    ChrTalk(
        0xA,
        (
            "出店で料理を食べて\x01",
            "美味しかったから来た\x01",
            "ってお客さんがいてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xA,
        (
            "いやぁ、なんだか\x01",
            "ホロッときちゃったよ。\x01",
            "嬉しいもんだねぇ、こういうの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F88")

    Jump("loc_8788")

    label("loc_7F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_80FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8082")

    #C0408
    ChrTalk(
        0xA,
        (
            "記念祭の出店に\x01",
            "うちの料理を出すことになってね。\x01",
            "娘が手伝いに行ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xA,
        (
            "この店で出してる料理も\x01",
            "今ならクロスベル市の出店で\x01",
            "食べられるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xA,
        (
            "さて、観光客が\x01",
            "宿をとりに来るだろうし……\x01",
            "僕も頑張らないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_80F7")

    label("loc_8082")


    #C0411
    ChrTalk(
        0xA,
        (
            "うちの娘も\x01",
            "記念祭の出店の手伝いに\x01",
            "行ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xA,
        (
            "この店で出してる料理も\x01",
            "今なら出店で食べることができるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80F7")

    Jump("loc_8788")

    label("loc_80FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_819C")

    #C0413
    ChrTalk(
        0xA,
        (
            "記念祭に出す商品、\x01",
            "少し揉めてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xA,
        (
            "うーん、せっかくだしうちの店も\x01",
            "料理を出したいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xA,
        "観光客へのいい宣伝になりそうだしね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8788")

    label("loc_819C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_827C")

    #C0416
    ChrTalk(
        0xA,
        "あの魔獣騒動解決から１ヶ月……\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xA,
        (
            "クロスベルタイムズには\x01",
            "詳しいことは書かれてなかったけど\x01",
            "君たちが解決したんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xA,
        (
            "安心して眠れるようになったから\x01",
            "一度お礼を言っておきたかったんだ。\x01",
            "ありがとうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8788")

    label("loc_827C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_83D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_837D")

    #C0419
    ChrTalk(
        0xA,
        (
            "昨日、狼型魔獣に気をつけるよう\x01",
            "村長からお達しがあってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xA,
        (
            "なんでもあの事件は\x01",
            "かなり広い範囲で起きてるんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xA,
        (
            "野生の魔獣ってのは\x01",
            "一定の縄張りの中でしか\x01",
            "活動しないと思っていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xA,
        "珍しいこともあるもんだね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_83D4")

    label("loc_837D")


    #C0423
    ChrTalk(
        0xA,
        (
            "件の狼型魔獣ってのは\x01",
            "随分縄張りが広いんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xA,
        "もしかして、新種かなにかかね？\x02",
    )

    CloseMessageWindow()

    label("loc_83D4")

    Jump("loc_8788")

    label("loc_83D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_84D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8489")

    #C0425
    ChrTalk(
        0xA,
        (
            "しかし魔獣の話が\x01",
            "今になって出てくるとはね……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xA,
        (
            "あれから随分経つから\x01",
            "忘れかけてた所だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xA,
        (
            "まだ見つかってないなら\x01",
            "油断はできないね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_84CD")

    label("loc_8489")


    #C0428
    ChrTalk(
        0xA,
        (
            "村に被害を与えた魔獣……\x01",
            "見つかってないなら\x01",
            "油断はできないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84CD")

    Jump("loc_8788")

    label("loc_84D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_8645")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84F1")
    Call(0, 12)
    TalkEnd(0xA)
    Return()

    label("loc_84F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85BE")

    #C0429
    ChrTalk(
        0xA,
        (
            "昼食時で、農作業に出てた人が\x01",
            "戻ってきてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xA,
        (
            "大繁盛、とまでは行かないけど……\x01",
            "まぁ、所詮こんな田舎だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xA,
        (
            "常連さんが来てくれるだけで\x01",
            "店をやっててよかったって思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8640")

    label("loc_85BE")


    #C0432
    ChrTalk(
        0xA,
        (
            "ハロルドさんも、こっちに来る時は\x01",
            "よくウチを利用してくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xA,
        (
            "彼も常連さんなんだし\x01",
            "たまにはサービスしてあげないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8640")

    Jump("loc_8788")

    label("loc_8645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_870B")

    #C0434
    ChrTalk(
        0xA,
        (
            "おや、いらっしゃい。\x01",
            "なにか飲むかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xA,
        (
            "見たところ、結構疲れてるようだね。\x01",
            "無理をしちゃあいけないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xA,
        (
            "なんだったら食事でもとるかね？\x01",
            "簡単なものなら出せるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8788")

    label("loc_870B")


    #C0437
    ChrTalk(
        0xA,
        (
            "ふむ、食事で思い出したが……\x01",
            "もうすぐ昼だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xA,
        (
            "農作業に出ていた人達が\x01",
            "昼食をとりに来る頃だ。\x01",
            "準備しておかないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8788")

    Jump("loc_7612")

    label("loc_878D")

    TalkEnd(0xA)
    Return()

    # Function_26_75EC end

    def Function_27_8791(): pass

    label("Function_27_8791")

    Call(0, 28)
    Return()

    # Function_27_8791 end

    def Function_28_8795(): pass

    label("Function_28_8795")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9793")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8800")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8830")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_881F")
    OP_AF(0x4C)
    Jump("loc_8821")

    label("loc_881F")

    OP_AF(0x4B)

    label("loc_8821")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_978E")

    label("loc_8830")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8844")
    Jump("loc_978E")

    label("loc_8844")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_978E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_89D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8941")

    #C0439
    ChrTalk(
        0x9,
        (
            "じいちゃんにはよく\x01",
            "シャキッとしてろって怒られるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x9,
        (
            "でも正直、やる気出ないんだよね。\x01",
            "一族代々の店だか知らないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x9,
        (
            "ご先祖さまも、もっと儲かる店を\x01",
            "始めてくれてたら良かったのになぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_89CB")

    label("loc_8941")


    #C0442
    ChrTalk(
        0x9,
        (
            "ご先祖さまも、もっと儲かる店を\x01",
            "始めてくれてたら良かったのになぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x9,
        (
            "仮に俺がＩＢＣ総裁の息子だったら\x01",
            "喜んで家業を継ぐんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89CB")

    Jump("loc_978E")

    label("loc_89D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A98")

    #C0444
    ChrTalk(
        0x9,
        (
            "はぁ……まーたじいちゃんに\x01",
            "叱られちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x9,
        (
            "こんな店なんかほっといて、\x01",
            "ほんとに街に行っちまうかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x9,
        (
            "……んなことしたら\x01",
            "じいちゃんが独りになっちまうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8B1A")

    label("loc_8A98")


    #C0447
    ChrTalk(
        0x9,
        (
            "こんな店なんかほっといて、\x01",
            "ほんとに街に行っちまうかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x9,
        (
            "……じいちゃんが独りになっちまうから\x01",
            "そんなことしないけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B1A")

    Jump("loc_978E")

    label("loc_8B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8C88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BF0")

    #C0449
    ChrTalk(
        0x9,
        (
            "じいちゃん……\x01",
            "機嫌よさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x9,
        (
            "ハロルドさんはじいちゃんの\x01",
            "お気に入りだからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x9,
        (
            "……へっ、どーせ俺なんか\x01",
            "記念祭でなんも活躍しなかった\x01",
            "ただの元プー太郎ですよーだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8C83")

    label("loc_8BF0")


    #C0452
    ChrTalk(
        0x9,
        (
            "記念祭で俺が掴んだことといえば、\x01",
            "商品の計算が早くなったって\x01",
            "ことくらいだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x9,
        (
            "……んー、未だに家事手伝いの粋を\x01",
            "出てない気がするなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C83")

    Jump("loc_978E")

    label("loc_8C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D1C")

    #C0454
    ChrTalk(
        0x9,
        (
            "ふぁぁああぁ～……\x01",
            "昨日までの忙しさが\x01",
            "ウソみてぇだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x9,
        (
            "でもまぁ、これでようやく\x01",
            "楽な日々に戻れるってもんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8D69")

    label("loc_8D1C")


    #C0456
    ChrTalk(
        0x9,
        (
            "……なんかじいちゃんが\x01",
            "こっちを睨んでるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x9,
        "これは怒られる予感……\x02",
    )

    CloseMessageWindow()

    label("loc_8D69")

    Jump("loc_978E")

    label("loc_8D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E03")

    #C0458
    ChrTalk(
        0x9,
        (
            "あの客も、なんでじいちゃんに\x01",
            "話をもちかけるかね。\x01",
            "カウンターにいるのは俺だぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x9,
        "……俺ってもしかして、頼りない？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8E6B")

    label("loc_8E03")


    #C0460
    ChrTalk(
        0x9,
        "……俺、頼りないのかなぁ。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x9,
        (
            "……ま、じいちゃんが\x01",
            "商談を進めてくれるなら\x01",
            "俺はラクでいいけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E6B")

    Jump("loc_978E")

    label("loc_8E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8EF4")

    #C0462
    ChrTalk(
        0x9,
        (
            "昨日辺りから\x01",
            "急に客が来るようになってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x9,
        (
            "じいちゃんが妙に張り切ってるけど、\x01",
            "正直忙しくて目が回っちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_978E")

    label("loc_8EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8FC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F77")

    #C0464
    ChrTalk(
        0x9,
        (
            "村のハチミツ、\x01",
            "結構売れたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x9,
        (
            "……普段もそれだけ売れりゃ、\x01",
            "俺もラクに暮らせるのになぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8FC4")

    label("loc_8F77")


    #C0466
    ChrTalk(
        0x9,
        (
            "客が来ないのもラクっちゃラクだけど……\x01",
            "もっと売れて欲しいよ、ハチミツ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FC4")

    Jump("loc_978E")

    label("loc_8FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_90AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9070")

    #C0467
    ChrTalk(
        0x9,
        (
            "デリックとじいちゃんが\x01",
            "さっきから話してるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x9,
        "うーん、全然意味がわかんねぇ。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x9,
        (
            "やっぱ俺、商売人にゃ\x01",
            "向いてないかもなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_90A9")

    label("loc_9070")


    #C0470
    ChrTalk(
        0x9,
        (
            "デリックとじいちゃん、\x01",
            "さっきから何話してんだ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90A9")

    Jump("loc_978E")

    label("loc_90AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9183")

    #C0471
    ChrTalk(
        0x9,
        (
            "最近《クロスベルタイムズ》を\x01",
            "読むようになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x9,
        (
            "君ら、雑誌に載るような\x01",
            "人達だったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x9,
        (
            "うーん、俺もやっぱり\x01",
            "クロスベル市に進出して、\x01",
            "ゴージャスな人生を送りたいぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_920C")

    label("loc_9183")


    #C0474
    ChrTalk(
        0x9,
        (
            "俺もいつかは\x01",
            "《クロスベルタイムズ》に紹介される\x01",
            "ビッグな男になってやるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x9,
        (
            "……まっ、当分は\x01",
            "店の手伝いやってるつもりだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_920C")

    Jump("loc_978E")

    label("loc_9211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92F1")

    #C0476
    ChrTalk(
        0x9,
        (
            "はぁ……\x01",
            "じいちゃん、最近やたらと\x01",
            "ハロルドさんと俺を比べてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x9,
        (
            "『お前もあれくらいの男になれ』\x01",
            "なーんて言っちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x9,
        (
            "こちとら新米なんだし\x01",
            "あまりプレッシャーを\x01",
            "かけないで欲しいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_937D")

    label("loc_92F1")


    #C0479
    ChrTalk(
        0x9,
        (
            "じいちゃん、ハロルドさんが\x01",
            "随分お気に入りみたいでね。\x01",
            "やたらと俺と比べるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x9,
        (
            "はぁ……\x01",
            "あまりプレッシャーを\x01",
            "かけないで欲しいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_937D")

    Jump("loc_978E")

    label("loc_9382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_94DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9462")

    #C0481
    ChrTalk(
        0x9,
        (
            "俺、プーだったんだけど\x01",
            "じいちゃんが\x01",
            "店を継げってうるさくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x9,
        (
            "あーあ……\x01",
            "こんなボロい店継ぐのもなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x9,
        (
            "男として生まれたんだ、\x01",
            "クロスベル市で一山当てて\x01",
            "ビッグになってみたいもんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_94D9")

    label("loc_9462")


    #C0484
    ChrTalk(
        0x9,
        (
            "いつかはクロスベル市に出て\x01",
            "ビックになりたいもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x9,
        (
            "……ま、しばらく\x01",
            "店の手伝いもいいけどな。\x01",
            "気楽でいいし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94D9")

    Jump("loc_978E")

    label("loc_94DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_9641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95D2")

    #C0486
    ChrTalk(
        0x9,
        (
            "新月の夜の話？\x01",
            "……ああ、\x01",
            "やたらと村が騒がしかったアレかぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x9,
        (
            "あの時は俺はぐっすり寝てたからなぁ。\x01",
            "なーんも覚えちゃないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x9,
        (
            "もう損した分は取り返したらしいし\x01",
            "そんなに気にしないほうが\x01",
            "いいと思うけどねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_963C")

    label("loc_95D2")


    #C0489
    ChrTalk(
        0x9,
        (
            "村長はもう被害額分は\x01",
            "取り戻せたっつってたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x9,
        (
            "魔獣のことなんて\x01",
            "もう忘れた方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_963C")

    Jump("loc_978E")

    label("loc_9641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_978E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96EF")

    #C0491
    ChrTalk(
        0x9,
        (
            "ど、どもども。\x01",
            "いらせられれませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x9,
        (
            "……どわっ、噛んじゃった！\x01",
            "ゴホンゴホン。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x9,
        (
            "えぇっと、イラッシャイマセ。\x01",
            "お好きに見てってクダサイ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_978E")

    label("loc_96EF")


    #C0494
    ChrTalk(
        0x9,
        (
            "はぁ……じいちゃんも人が悪いぜ。\x01",
            "俺に客商売なんて無理だっての。\x01",
            "あんたもそう思わない？\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x9,
        (
            "……っと、ついタメ口使っちゃいました。\x01",
            "えーと、ゴメンナサイ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_978E")

    Jump("loc_87A2")

    label("loc_9793")

    TalkEnd(0x9)
    Return()

    # Function_28_8795 end

    def Function_29_9797(): pass

    label("Function_29_9797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97AD")
    Call(0, 41)
    Jump("loc_9C85")

    label("loc_97AD")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_97BE")
    Jump("loc_9C82")

    label("loc_97BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_97CC")
    Jump("loc_9C82")

    label("loc_97CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_99E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_9853")

    #C0496
    ChrTalk(
        0x1B,
        (
            "#3600F最近は妻も頑張って\x01",
            "仕事を支えてくれるんです。\x02\x03",

            "これからは家族一丸となって\x01",
            "頑張らせていただきますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99E2")

    label("loc_9853")


    #C0497
    ChrTalk(
        0x1B,
        (
            "#3605Fおや、皆さんも\x01",
            "蜂蜜の買い付けですか？\x02\x03",

            "#3600Fははは、生憎ですけど\x01",
            "買い付けじゃ私には勝てませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x104,
        (
            "#0300Fいやあ、俺たちが商談に\x01",
            "来るわけないじゃないスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        (
            "#0000F記念祭の後はしばらく\x01",
            "休業していたと聞きましたけど……\x01",
            "再開なさったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x1B,
        (
            "#3600Fええ、休業と言っても\x01",
            "身体休めのようなものでしたから。\x02\x03",

            "お陰で英気も養えました。\x01",
            "これからは一層商売に\x01",
            "励ませていただきますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_99E2")

    Jump("loc_9C82")

    label("loc_99E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_99F5")
    Jump("loc_9C82")

    label("loc_99F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9A03")
    Jump("loc_9C82")

    label("loc_9A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9A11")
    Jump("loc_9C82")

    label("loc_9A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9A1F")
    Jump("loc_9C82")

    label("loc_9A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9A2D")
    Jump("loc_9C82")

    label("loc_9A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9A3B")
    Jump("loc_9C82")

    label("loc_9A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9A49")
    Jump("loc_9C82")

    label("loc_9A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_9ABA")

    #C0501
    ChrTalk(
        0x1B,
        (
            "#3604Fさて、と……\x01",
            "そろそろ帰る準備をしなければ。\x02\x03",

            "#3608Fええっと、鍵はどこにしまったかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C82")

    label("loc_9ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_9C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BEB")

    #C0502
    ChrTalk(
        0x1B,
        (
            "#3610F生憎、私も被害が起きた現場に\x01",
            "いたわけではありませんからね。\x01",
            "お力になれず申し訳ないです。\x02\x03",

            "#3608F……このまま各地で被害が続けば、\x01",
            "クロスベルに住む皆が\x01",
            "不安を抱えていくことなります。\x02\x03",

            "#3600F特務支援課の皆さん。\x01",
            "捜査のほう、頑張ってください。\x01",
            "私も陰ながら応援してます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9C74")

    label("loc_9BEB")


    #C0503
    ChrTalk(
        0x1B,
        (
            "#3604Fきっと皆さんの捜査が\x01",
            "事件を好転させる……\x01",
            "そんな気がします。\x02\x03",

            "#3600F捜査のほう、頑張ってください。\x01",
            "私も陰ながら応援してます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C74")

    Jump("loc_9C82")

    label("loc_9C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9C82")

    label("loc_9C82")

    TalkEnd(0x1B)

    label("loc_9C85")

    Return()

    # Function_29_9797 end

    def Function_30_9C86(): pass

    label("Function_30_9C86")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D1A")
    Jump("loc_9D64")

    label("loc_9D1A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9D3A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D64")

    label("loc_9D3A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D5A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D64")

    label("loc_9D5A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D64")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DA4")
    Call(0, 37)
    Jump("loc_9E32")

    label("loc_9DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DB6")
    Call(0, 38)
    Jump("loc_9E32")

    label("loc_9DB6")


    #C0504
    ChrTalk(
        0x1C,
        (
            "#0803Fさてと……一休みしたら\x01",
            "他の街道にも行ってみようかな。\x02\x03",

            "#0800F本当にバスとかの運行に\x01",
            "支障がないか確かめないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E32")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_9C86 end

    def Function_31_9E3A(): pass

    label("Function_31_9E3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9EE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E58")
    Call(0, 37)
    Jump("loc_9EE8")

    label("loc_9E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E6A")
    Call(0, 38)
    Jump("loc_9EE8")

    label("loc_9E6A")


    #C0505
    ChrTalk(
        0x1D,
        (
            "#0903F以前手配された魔獣以外にも\x01",
            "見たこともない危険な魔獣が\x01",
            "確認されているらしい。\x02\x03",

            "#0901F君たちもくれぐれも気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EE8")

    TalkEnd(0xFE)
    Return()

    # Function_31_9E3A end

    def Function_32_9EEC(): pass

    label("Function_32_9EEC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F80")
    Jump("loc_9FCA")

    label("loc_9F80")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FA0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9FCA")

    label("loc_9FA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FC0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9FCA")

    label("loc_9FC0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9FCA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0AB")
    SetChrSubChip(0x1E, 0x0)

    #C0506
    ChrTalk(
        0x1E,
        (
            "地方にも割と\x01",
            "観光客が訪れているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x1E,
        (
            "エオリア、\x01",
            "彼らが変な場所に入らないよう\x01",
            "注意していよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x1F,
        "了解。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x1F,
        "……でも、これを食べてからね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A118")

    label("loc_A0AB")


    #C0510
    ChrTalk(
        0xFE,
        (
            "街道はパッと見、\x01",
            "危険の分からない所が\x01",
            "結構あるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        (
            "観光客が入り込まないよう\x01",
            "注意していないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A118")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_9EEC end

    def Function_33_A120(): pass

    label("Function_33_A120")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A1B4")
    Jump("loc_A1FE")

    label("loc_A1B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1D4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1FE")

    label("loc_A1D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1F4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1FE")

    label("loc_A1F4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1FE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2A0")

    #C0512
    ChrTalk(
        0xFE,
        (
            "今日はちょっと\x01",
            "手配魔獣を片付けにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xFE,
        (
            "放っておくといつの間にか\x01",
            "沸いてきちゃうのよね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A325")

    label("loc_A2A0")


    #C0514
    ChrTalk(
        0xFE,
        (
            "観光シーズン中は\x01",
            "街道の方は特に心配なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "あまり長居はできないけど、\x01",
            "滞在している間くらいは\x01",
            "気にかけておかなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A325")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_A120 end

    def Function_34_A32D(): pass

    label("Function_34_A32D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A46B")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0516
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "★トネリコ亭・おすすめ料理★\x01",
            "　～　田舎風オムライス　～\x02",
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
            "#0000Fへぇ、オムライスか……\x01",
            "なかなか美味そうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        (
            "#0100Fレシピも載ってるわね。\x01",
            "せっかくだしメモしておきましょうよ。\x02",
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
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x9)
    Jump("loc_A4C0")

    label("loc_A46B")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0520
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "★トネリコ亭・おすすめ料理★\x01",
            "　～　田舎風オムライス　～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_A4C0")

    TalkEnd(0xFF)
    Return()

    # Function_34_A32D end

    def Function_35_A4C4(): pass

    label("Function_35_A4C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A56A")

    #C0521
    ChrTalk(
        0xFE,
        (
            "いいよなぁ、この村の雰囲気。\x01",
            "ず～っと野原で日向ぼっこを\x01",
            "していたいような……\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "歳を食ったら、こういう所で\x01",
            "ノンビリと余生を過ごしたいぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A5D4")

    label("loc_A56A")


    #C0523
    ChrTalk(
        0xFE,
        (
            "街のカジノとかで\x01",
            "賑やかに遊ぶのもいいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xFE,
        (
            "こういう静かな所で\x01",
            "のんびり過ごすのも悪くないよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5D4")

    TalkEnd(0xFE)
    Return()

    # Function_35_A4C4 end

    def Function_36_A5D8(): pass

    label("Function_36_A5D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A66A")

    #C0525
    ChrTalk(
        0xFE,
        (
            "新鮮なお野菜がこんなに\x01",
            "安い値段で置いているなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        (
            "これは、今のうちに\x01",
            "たくさん買っておかないと\x01",
            "いけませんわね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_A6C6")

    label("loc_A66A")


    #C0527
    ChrTalk(
        0xFE,
        (
            "ポテト、オニオン……\x01",
            "特産品のハチミツ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        (
            "オホホホホ……！\x01",
            "安い……安いですわ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6C6")

    TalkEnd(0xFE)
    Return()

    # Function_36_A5D8 end

    def Function_37_A6CA(): pass

    label("Function_37_A6CA")

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
        "#0805F#6Pあ、ロイド君たち。\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x1D,
        (
            "#0900F#12Pお疲れさま。\x01",
            "君たちも仕事かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x101,
        (
            "#0002F#5Pああ、色々と細かい仕事を\x01",
            "している最中だけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x104,
        (
            "#0305F#5Pそっちはもしかして\x01",
            "この宿に泊まったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x1C,
        (
            "#0806F#6Pあ、うん。\x01",
            "実は昨日、魔獣退治に手こずって\x01",
            "バスが無くなっちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x1D,
        (
            "#0903F#12Pそれでこちらの宿に\x01",
            "泊まることになったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x102,
        (
            "#0101F#5Pエステルさんたちが\x01",
            "手こずるほどの魔獣なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x103,
        (
            "#0205F#5Pそこまで手強い\x01",
            "相手だったのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x1C,
        (
            "#0806F#6Pうーん、前にも出没していた\x01",
            "手配魔獣みたいだけど……\x02\x03",

            "#0801Fそれが何匹も街道に\x01",
            "現れているみたいなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x1D,
        (
            "#0906F#12Pしかも以前よりも\x01",
            "強くなっているみたいだし……\x02\x03",

            "#0901Fこの辺りだけじゃなくて\x01",
            "他の街道も似た状況らしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        "#0001F#5Pそうなのか……\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x109,
        (
            "#0503F#5P……警備隊の方にも\x01",
            "似たような報告が来ていますね。\x02\x03",

            "#0500F幸い、バスや車の運行には\x01",
            "支障はないみたいですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        (
            "#0306F#5Pそりゃま、\x01",
            "不幸中の幸いと言うべきか。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x102,
        "#0108F#5Pでも、少し気になるわね……\x02",
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

    # Function_37_A6CA end

    def Function_38_AB6C(): pass

    label("Function_38_AB6C")

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
            "#0802F#6Pそれはそうと……\x01",
            "珍しい人を連れてるわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x1D,
        "#0900F#12Pクロスベル警備隊の方ですか？\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x109,
        (
            "#0500F#5Pタングラム門所属、\x01",
            "ノエル・シーカー曹長です。\x02\x03",

            "お２人は遊撃士の方ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x1C,
        (
            "#0800F#6Pうん、クロスベル支部所属の\x01",
            "エステル・ブライトよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x1D,
        (
            "#0904F#12P初めまして。\x01",
            "ヨシュア・ブライトです。\x02",
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
            "#0505F#5Pあ、あなた方が……\x02\x03",

            "#0502Fクロスベルタイムズで見ました！\x01",
            "リベールの異変を食い止めた\x01",
            "若き英雄だそうですね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x1C,
        (
            "#0809F#6Pあ、あはは……\x01",
            "グレイスさんの記事ね……\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x1D,
        (
            "#0904F#12P実際には僕たちだけの\x01",
            "功績ではないんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        (
            "#0012F#5P（うーん、やっぱり\x01",
            "  エステルたちは有名だなぁ。）\x02",
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

    # Function_38_AB6C end

    def Function_39_AEE2(): pass

    label("Function_39_AEE2")

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
            "#5Pあぁ……お客さんに\x01",
            "何かあったら大変だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xA,
        "#5Pどうか無事でいてくれよ～……\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#6P#0003Fあの、すみません。\x01",
            "#0001Fゴーファンさんでしょうか？\x02\x03",

            "特務支援課の者です。\x01",
            "支援要請が出ていたようなので\x01",
            "伺ったのですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(750)
    TurnDirection(0xA, 0x101, 750)

    #C0555
    ChrTalk(
        0xA,
        "#11Pおお、君たちは……！\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xA,
        (
            "#11Pよく来てくれたよ！\x01",
            "ああとにかく、大変なんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xA,
        (
            "#11Pこんなことになるなら、\x01",
            "縛り付けてでも\x01",
            "村に留めるべきだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xA,
        "#11Pああ、僕の責任だ……！\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#6P#0006Fどうか落ち着いて\x01",
            "ゆっくり話してください。\x02\x03",

            "#0001F一体、何があったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xA,
        (
            "#11P……あ、ああ。\x01",
            "すまない、取り乱してしまったね。\x01",
            "順を追って話そう。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xA,
        (
            "#11P昨日から、外国人観光客のカップルが\x01",
            "うちに宿をとっていたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xA,
        (
            "#11P今朝、朝食を運びに行ったら\x01",
            "部屋がもぬけの殻でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xA,
        (
            "#11Pどうやら、アルモリカ古道の途中にある\x01",
            "《古戦場》という場所に\x01",
            "行ってしまったようなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x101,
        "#0005F#6P古戦場……ですか？\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x102,
        (
            "#5P#0106F前も言ったけど、あの辺りには\x01",
            "中世の時代の戦場跡があるの。\x02\x03",

            "#0105Fただ、かなり前に石橋が壊れて\x01",
            "行けなくなったそうですけど……？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xA,
        (
            "#11Pああ、そうだったんだが……\x01",
            "つい先日、修繕が終わったらしくてね。\x01",
            "誰でも入れる状態になっていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xA,
        (
            "#11P……あのカップル、昨日から\x01",
            "観光してみたいって言って\x01",
            "聞かなくてね……\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xA,
        (
            "#11P絶対に勝手に入ったりしないように\x01",
            "注意はしたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x104,
        (
            "#6P#0303Fふーむ、古戦場なんていかにも\x01",
            "観光スポットって響きだが……\x02\x03",

            "#0301Fそんなに注意しなきゃならんほど\x01",
            "危ない場所なんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xA,
        (
            "#11Pああ……あそこは昔から、\x01",
            "危険な魔獣が生息する場所として有名でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xA,
        (
            "#11P村の人間ですら、用心して\x01",
            "近づかないようにしてるくらいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xA,
        (
            "#11Pしかも、石橋が壊れてからは\x01",
            "しばらく整備も行き届いてないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xA,
        (
            "#11P正直、中がどんな様子に\x01",
            "なっているのかすら\x01",
            "確認できていない状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x103,
        (
            "#6P#0203Fそんな場所に何も知らない\x01",
            "観光客が入り込んでしまった……\x02\x03",

            "#0201F確かにまずそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x102,
        "#5P#0101Fええ……緊急度はかなり高そうね。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xA,
        (
            "#11P……どうかお願いだ。\x01",
            "あの観光客を探し出して、\x01",
            "連れ帰ってきてくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xA,
        (
            "#11P一応、友人のアルフレッドに\x01",
            "これ以上古戦場に入る人が出ないよう\x01",
            "見張ってもらってるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xA,
        (
            "#11Pこのままじゃ、大事なお客さんが\x01",
            "危険な目にあってしまうよ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x101,
        (
            "#6P#0004F……分かりました。\x01",
            "俺たちにお任せ下さい。\x02\x03",

            "#0000F観光客たちはきっと\x01",
            "見つけ出してみせます。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x104,
        (
            "#6P#0306Fま、しゃーないわな。\x02\x03",

            "#0300F忠告も聞かない観光客……\x01",
            "とっとと見つけて\x01",
            "叱りつけてやるとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xA,
        (
            "#11Pああ……ありがとう！\x01",
            "本当に助かるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xA,
        "#11Pどうか、よろしく頼──\x02",
    )

    CloseMessageWindow()

    #N0583
    NpcTalk(
        0xC,
        "青年の声",
        "親父さ～ん！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B9A9():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B9A9)
    Sleep(30)

    def lambda_B9B9():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B9B9)

    def lambda_B9C6():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B9C6)
    Sleep(30)

    def lambda_B9D6():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B9D6)
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

    def lambda_BA46():
        OP_97(0xC, 0x0, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BA46)

    def lambda_BA60():
        OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_BA60)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xC, 2)

    #C0584
    ChrTalk(
        0x101,
        "#11P#0005F（……常連さん、かな？）\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xA,
        (
            "#11P……キース君、\x01",
            "一体どうしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xA,
        (
            "#11P今は、この人たちと\x01",
            "大事な話を……\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xC,
        (
            "#6Pのんきに話なんか\x01",
            "してる場合じゃねえだろ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xC,
        (
            "#6P観光客が行方不明になって\x01",
            "大変だって言ってたじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xA,
        (
            "#11Pああ、その話なら\x01",
            "こちらの警察の方に……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xC,
        "#6Pいや、安心してくれ。\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xC,
        (
            "#6P困っている親父さんのために……\x01",
            "強力な助っ人を呼んでおいたからさ！\x02",
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
        "#11P#0105F強力な……助っ人？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x20, 500)

    #C0593
    ChrTalk(
        0xC,
        (
            "#12Pほらほら！\x01",
            "早く親父さんの話を\x01",
            "聞いてやってくれよ！\x02",
        )
    )

    CloseMessageWindow()

    #N0594
    NpcTalk(
        0x20,
        "男の声",
        "……ああ、もちろんだ。\x02",
    )

    CloseMessageWindow()
    OP_68(-110, 1200, 580, 2000)
    SetCameraDistance(24140, 2000)

    def lambda_BD23():
        OP_97(0x20, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_BD23)

    def lambda_BD3D():
        OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_BD3D)
    OP_98(0xC, 0xFFFFFD12, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_BD62():
        OP_93(0xC, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BD62)
    WaitChrThread(0x20, 1)
    WaitChrThread(0x20, 2)

    #C0595
    ChrTalk(
        0x20,
        (
            "#6P……遊撃士協会の\x01",
            "スコットという者です。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x20,
        (
            "#6P行方不明の観光客を\x01",
            "探して欲しいとのことですが……\x01",
            "早速、詳しい話を伺えませんか？\x02",
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
        "#11P#0011Fゆっ……遊撃士！？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x102,
        "#11P#0105Fど、どうして……\x02",
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x20, 0x101, 500)
    Sleep(500)

    #C0599
    ChrTalk(
        0x20,
        (
            "#6P……おっと？\x01",
            "君らは確か、特務支援課の。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x20,
        (
            "#6P偶然……って\x01",
            "雰囲気じゃなさそうだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xA,
        (
            "#11Pキ、キース君。\x01",
            "何で遊撃士の方がここに……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x2D, 0x1F4)

    #C0602
    ChrTalk(
        0xC,
        (
            "#5Pなに言ってんだよ親父さん。\x01",
            "困ったときの遊撃士だろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xC,
        (
            "#5P今朝話を聞いてから、\x01",
            "大急ぎでクロスベル市のギルドに\x01",
            "依頼を出したのさ！\x02",
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
            "#11Pはぁ……\x01",
            "その気持ちはありがたいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x103,
        "#11P#0211F……そういうことですか。\x02",
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x104,
        "#11P#0306Fある意味、タイミングよすぎだな。\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xC,
        (
            "#5P……あ、あれ。\x01",
            "なんだか反応悪くない？\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x20,
        (
            "#6P……どうやら、ややこしい事に\x01",
            "なっているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x20,
        (
            "#6Pすまんが手短に\x01",
            "状況を説明してもらえるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        (
            "#11P#0011Fわ、分かりました。\x01",
            "ええっと、実は……\x02",
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
            "ロイドは自分たちも同じ依頼を受けて\x01",
            "ここに来たことを説明した。\x07\x00\x02",
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
            "#6P……なるほど、\x01",
            "そういうことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x20,
        (
            "#6Pそいつは、思わぬ多重依頼に\x01",
            "なってしまったわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x103,
        (
            "#12P#0203Fしかし……\x01",
            "この場合、どうなるのでしょう。\x02\x03",

            "#0200F同じ依頼を警察と遊撃士が\x01",
            "同時に受けていることに\x01",
            "なりますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x104,
        (
            "#11P#0302F……単純に、\x01",
            "競争になんじゃねぇのか？\x02\x03",

            "#0309Fどっちが先に依頼を達成するか！\x01",
            "……って感じで。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x102,
        (
            "#11P#0106Fもう……\x01",
            "そういう問題じゃないでしょう。\x02\x03",

            "#0108Fロイド、どうしたらいいかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x101,
        "#11P#0003Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0618
    ChrTalk(
        0x101,
        (
            "#11P#0001Fスコットさん、\x01",
            "今回の件ですが……\x02\x03",

            "共同戦線、というのは\x01",
            "いかがでしょう。\x02",
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

    def lambda_C4AD():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C4AD)

    def lambda_C4BA():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C4BA)

    def lambda_C4C7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C4C7)
    Sleep(1000)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0619
    ChrTalk(
        0x20,
        (
            "#6Pはは、気が合うな。\x01",
            "俺も同じことを考えてた所さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x102,
        "#5P#0105F共同戦線……\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x104,
        (
            "#6P#0305F一緒に古戦場って所を\x01",
            "探索しようってことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x101,
        (
            "#11P#0000Fいや、手分けする意味でさ。\x02\x03",

            "#0003F聞けば、長いあいだ放置されて\x01",
            "魔獣の住処になっている場所みたいだ。\x02\x03",

            "その観光客のカップルは\x01",
            "一刻も早く保護する必要がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x20,
        (
            "#6P俺には少々土地勘があるが\x01",
            "古戦場ってのはかなり広い場所だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x20,
        (
            "#6P手分けして捜索した方が\x01",
            "保護できる確率も上がるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x20,
        (
            "#6Pお互い、エニグマで連絡が付けば\x01",
            "より効率的に探索できるだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x104,
        "#6P#0300Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x103,
        (
            "#6P#0204F確かに……\x01",
            "最も合理的な選択のようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xA,
        "#11Pああ、僕もその方が心強いよ。\x02",
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xA,
        (
            "#11P人の命がかかってるんだ、\x01",
            "人手は多ければ多い方がいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xA,
        "#11Pどうかよろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x20,
        (
            "#6P依頼者の承諾も取れた……\x01",
            "決まりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x101,
        "#11P#0000Fええ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0633
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとスコットは\x01",
            "互いのエニグマの通信番号を交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0634
    ChrTalk(
        0x20,
        "#6Pそれじゃ、善は急げだ。\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x20,
        (
            "#6P俺は一足先に古戦場へ向かう。\x01",
            "君らも準備を済ませたら来るといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x20,
        "#6Pそれじゃあ、また後でな。\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0xB4, 0x1F4)

    def lambda_C8FC():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C8FC)

    def lambda_C909():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C909)

    def lambda_C916():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C916)

    def lambda_C923():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C923)
    OP_97(0x20, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)

    #C0637
    ChrTalk(
        0x101,
        (
            "#11P#0003F……よし。\x01",
            "俺たちも準備が出来たら\x01",
            "古戦場に向かおう。\x02\x03",

            "#0001Fスコットさんに\x01",
            "遅れをとらないように\x01",
            "しないとな。\x02",
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
            "クエスト【観光客の捜索願い】\x07\x00",
            "を開始した！\x02",
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

    # Function_39_AEE2 end

    def Function_40_CAEF(): pass

    label("Function_40_CAEF")

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
            "#11P無事に観光客を\x01",
            "連れ戻してくれて助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xA,
        "#11P皆さん、どうもありがとうな。\x02",
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x101,
        (
            "#6P#0000Fいえ、そんな。\x01",
            "ほとんどスコットさんと\x01",
            "アリオスさんのおかげですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x104,
        (
            "#6P#0306F今だって、あのカップルを\x01",
            "部屋で休ませてるんだよな。\x02\x03",

            "#0301Fなんつーか、あんだけ強いのに\x01",
            "マメすぎるっつーの……\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x102,
        (
            "#5P#0104Fふふ……そのあたりの気配りも\x01",
            "遊撃士ならではかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    #C0644
    ChrTalk(
        0x102,
        (
            "#5P#0100Fさて……これでひとまず、\x01",
            "仕事は完了という事かしら。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0645
    ChrTalk(
        0x103,
        (
            "#6P#0203Fええ、ですが……\x01",
            "問題が一つあります。\x02\x03",

            "#0200F今回、警察とギルドの\x01",
            "共同任務という形でしたが……\x02\x03",

            "最終的にどういう\x01",
            "判断になるんでしょう？\x02",
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
            "#6P#0305Fそういや、そうだな。\x02\x03",

            "#0300F……で、どうなるんだロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x101,
        (
            "#11P#0003Fうーん……\x01",
            "さっきも言ったけど……\x02\x03",

            "今回の依頼はスコットさんと\x01",
            "アリオスさんがいなかったら\x01",
            "解決しなかったはずだ。\x02\x03",

            "#0000Fだったら今回は彼らが\x01",
            "依頼を達成したということに……\x02",
        )
    )

    CloseMessageWindow()

    #N0648
    NpcTalk(
        0x20,
        "スコットの声",
        "#1Pそれには及ばない。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_D00C():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D00C)

    def lambda_D019():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D019)

    def lambda_D026():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D026)

    def lambda_D033():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D033)
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

    def lambda_D0BF():
        OP_95(0x20, -3270, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D0BF)

    def lambda_D0D9():
        OP_95(0x21, -3270, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_D0D9)
    WaitChrThread(0x20, 1)

    def lambda_D0F7():
        OP_95(0x20, 500, 0, -1770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D0F7)
    WaitChrThread(0x21, 1)

    def lambda_D115():
        OP_95(0x21, -500, 0, -2580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_D115)

    def lambda_D12F():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D12F)

    def lambda_D13C():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D13C)

    def lambda_D149():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D149)

    def lambda_D156():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D156)
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x0, 0x0)
    WaitChrThread(0x21, 1)
    OP_93(0x21, 0x0, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0649
    ChrTalk(
        0x102,
        "#11P#0105Fアリオスさん、スコットさん……\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x21,
        (
            "#6P#1403F……主人、あの２人が\x01",
            "後で貴方に謝りたいそうだ。\x02\x03",

            "#1400F忠告を聞かずに\x01",
            "勝手に古戦場に入った事を\x01",
            "深く反省しているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xA,
        (
            "#11Pああ、そうでしたか。\x01",
            "こっちは気にしてないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x104,
        (
            "#11P#0304Fハハ、あんな目に遭えば\x01",
            "いい薬になったろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x103,
        (
            "#11P#0205Fところで……\x01",
            "『それには及ばない』とは？\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x20,
        (
            "#6Pああ、アリオスさんには\x01",
            "もう話したんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x20,
        (
            "#6P今回の依頼は、君たちが\x01",
            "達成したということに\x01",
            "しておいてくれ。\x02",
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
            "#11P#0005Fえ、えっと……\x01",
            "それでいいんですか？\x02\x03",

            "#0003F今回の件は\x01",
            "明らかに遊撃士のお２人の\x01",
            "手柄が大きいと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x20,
        "#6Pいや、そんな事はないだろう。\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x20,
        (
            "#6P君らが先行してくれたおかげで\x01",
            "俺は女性の介抱に専念できたわけだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x20,
        (
            "#6Pもう一人の彼だって、\x01",
            "君らが間に合わなかったら\x01",
            "助からなかったかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x20,
        (
            "#6P結果的においしいところは\x01",
            "こっちが頂いてしまった形だが\x01",
            "むしろ功績はそちらの方が大きいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x104,
        (
            "#11P#0309Fハハ……ライバルの遊撃士に\x01",
            "褒められるなんて、\x01",
            "なんだかこそばゆいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x21,
        (
            "#6P#1404F……元々競争相手でも\x01",
            "なんでもないのだがな。\x02",
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
            "#6P#1403F特務支援課……\x01",
            "最初に会った時よりは\x01",
            "少しはマシになったようだな。\x02\x03",

            "#1400F特に……ロイド、だったか。\x02",
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
        "#11P#0011Fえ……\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x21,
        (
            "#6P#1400Fジオフロントで\x01",
            "初めて会った時を覚えているか？\x02\x03",

            "あの時のお前は\x01",
            "勝ち目のない魔獣に対して、\x01",
            "安易な自己犠牲を選ぼうとしたが……\x02\x03",

            "#1404F今回はそうしなかった。\x01",
            "勝てないにしろ、なんとか\x01",
            "切り抜ける方法を探したはずだ。\x02",
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
            "#6P#1403Fどんな不利な状況でも\x01",
            "最善を尽くすこと……\x01",
            "それには揺るぎない強さが必要だ。\x02\x03",

            "それこそ、命を投げ出す覚悟に\x01",
            "何倍も勝るほどの強さがな。\x02\x03",

            "#1402Fまだ、力不足は否めないが……\x01",
            "それが出来るようになったのは\x01",
            "強くなったという証拠だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x101,
        "#11P#0002F……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_93(0x21, 0xB4, 0x1F4)
    Sleep(300)

    #C0669
    ChrTalk(
        0x21,
        (
            "#11P#1404Fフ……\x01",
            "少々語りすぎたようだな。\x02\x03",

            "#1402F……スコット。\x01",
            "ギルドに報告に戻るぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x10E, 0x2EE)

    #C0670
    ChrTalk(
        0x20,
        "#11P了解です、アリオスさん。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x101, 500)
    Sleep(300)

    #C0671
    ChrTalk(
        0x20,
        (
            "#6Pそれじゃあな、特務支援課。\x01",
            "また力を合わせられるような\x01",
            "機会があるといいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x101,
        "#11P#0000Fええ、また。\x02",
    )

    CloseMessageWindow()

    def lambda_D9E1():
        OP_97(0x21, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_D9E1)
    OP_93(0x20, 0xB4, 0x2EE)

    def lambda_DA02():
        OP_97(0x20, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_DA02)
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
            "#12P#0200Fなんというか……最も意外な人に\x01",
            "激励されてしまいましたね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0674
    ChrTalk(
        0x102,
        (
            "#5P#0109Fティ、ティオちゃんったら……\x01",
            "確かにちょっと意外だったけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0675
    ChrTalk(
        0x104,
        (
            "#6P#0309Fハハッ、まぁよかったじゃねぇか。\x02\x03",

            "#0300F無事依頼達成って事になりそうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xA,
        "#11Pああ、本当にお疲れ様だった。\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xA,
        (
            "#11Pそれじゃ改めて……\x01",
            "特務支援課の諸君、礼を言うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0xA,
        "#11Pまた何かあったらよろしくな。\x02",
    )

    CloseMessageWindow()

    def lambda_DBE4():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBE4)
    Sleep(50)

    def lambda_DBF4():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DBF4)
    Sleep(50)

    def lambda_DC04():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DC04)
    Sleep(50)

    def lambda_DC14():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DC14)
    Sleep(300)

    #C0679
    ChrTalk(
        0x101,
        (
            "#6P#0000Fはい、こちらこそ。\x01",
            "ご連絡、お待ちしてます。\x02",
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
            "クエスト【観光客の捜索願い】\x07\x00",
            "を達成した！\x02",
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

    # Function_40_CAEF end

    def Function_41_DDB8(): pass

    label("Function_41_DDB8")

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
        "温和そうな男性",
        "#3605F#5Pおや、あなた方は……\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x101,
        "#0005F#12Pあ、さっきの……\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x102,
        (
            "#0100F確か……クロスベル市で\x01",
            "貿易商をされている方ですね？\x02",
        )
    )

    CloseMessageWindow()

    #N0684
    NpcTalk(
        0x1B,
        "温和そうな男性",
        (
            "#3609F#5Pはは、村長から\x01",
            "お聞きになりましたか。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("温和そうな男性")

    #A0685
    AnonymousTalk(
        0xFF,
        (
            "──初めまして。\x01",
            "ハロルド・ヘイワースといいます。\x02\x03",

            "クロスベル市で小さな\x01",
            "貿易商を営んでおりまして……\x02\x03",

            "皆さんもひょっとして\x01",
            "買い付けにいらっしゃったんですか？\x02",
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
        "#0000F#12Pい、いえ、自分たちは──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0687
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは自己紹介をして\x01",
            "アルモリカ村に来た事情を説明した。\x07\x00\x02",
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
            "#3605F#5P警察の方だったんですか……\x01",
            "これは失礼しました。\x02\x03",

            "#3603Fしかし『特務支援課』……\x01",
            "どこかで聞いた事があるような。\x02",
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
            "#3600F#5Pそうです！\x01",
            "クロスベル・タイムズ！\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x101,
        (
            "#0012F#12Pはぁ……\x01",
            "やっぱり読まれていましたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x102,
        (
            "#0106F#2Pその……\x01",
            "お恥ずかしい限りです。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x1B,
        (
            "#3609F#5Pはは、そんなに\x01",
            "恥ずかしがらなくても……\x02\x03",

            "#3600F設立されたばかりだというのに\x01",
            "頑張ってるみたいじゃないですか。\x02\x03",

            "あの記事だって、確かに少々\x01",
            "皮肉めいた書き方でしたけど……\x02\x03",

            "あなた方の頑張りを\x01",
            "好意的に捉えていたと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x101,
        "#0000F#12Pそ、そうですかね……？\x02",
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x103,
        (
            "#0206F#12P……好意的に解釈すれば\x01",
            "そう取れなくもないですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x104,
        (
            "#0309F#2Pハハ、書いた本人を知ってるから\x01",
            "素直には頷きにくいかもなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x1B,
        (
            "#3608F#5Pしかし、狼型魔獣ですか。\x02\x03",

            "医科大学でも聞きましたが\x01",
            "少しばかり心配ですね……\x02",
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
            "#0005F#12Pハロルドさんは\x01",
            "医科大学の方でもお仕事が？\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x1B,
        (
            "#3604F#5Pええ、病院で必要な備品を\x01",
            "卸させてもらっているんです。\x02\x03",

            "#3601Fあちらでは怪我人が\x01",
            "出たという噂もありますし……\x02\x03",

            "それに鉱山町でも\x01",
            "被害が起きているそうですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        (
            "#0001F#12Pええ、現在警備隊の方で\x01",
            "捜索が行われているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x1B,
        (
            "#3608F#5Pそうですか……\x02\x03",

            "#3610Fふむ、そちらの方にも\x01",
            "近いうちに挨拶に伺わないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x102,
        (
            "#0100F#2Pそういえば……\x02\x03",

            "ずいぶん良心的な価格で\x01",
            "特産品をお買い上げになったとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x1B,
        (
            "#3609F#5Pはは……\x01",
            "村長から聞いたんですか。\x02\x03",

            "#3600F別に慈善とか、\x01",
            "そういう訳でもないんです。\x02\x03",

            "蜂蜜を始め、この村の特産品は\x01",
            "最近評価が上がっていましてね。\x02\x03",

            "これを機に、少しでも\x01",
            "村の方々の印象を良くできればと\x01",
            "そんな打算もあるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x104,
        "#0309F#2Pはは、なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x103,
        (
            "#0202F#12P商売は信用第一……\x01",
            "そういうわけですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x102,
        (
            "#0102F#2Pふふ、いい商売を\x01",
            "なさっているみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x1B,
        (
            "#3600F#5Pいや、私などまだまだ\x01",
            "駆け出しもいいところですよ。\x02\x03",

            "#3610Fしかし申し訳ないですね……\x02\x03",

            "もう少し皆さんのお役に立てる\x01",
            "情報があれば良かったんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x101,
        (
            "#0011F#12Pいや、そんな。\x01",
            "気にしないでください。\x02\x03",

            "#0000F済みませんでした。\x01",
            "時間を取らせてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x1B,
        (
            "#3600F#5Pいえいえ。\x01",
            "聞き込み、頑張ってください。\x02",
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

    # Function_41_DDB8 end

    def Function_42_E94B(): pass

    label("Function_42_E94B")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA16")
    SetChrPos(0x109, -690, 0, 240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_EA41")

    label("loc_EA16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA41")
    SetChrPos(0x10A, -690, 0, 240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_EA41")

    OP_0D()

    #C0709
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあの……\x01",
            "アルフレッドさんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0xE,
        "#11Pおや、君たちは……\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0xE,
        (
            "#11P確か以前、古戦場を探索した\x01",
            "特務支援課、だったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0xE,
        "#11P私に何か用かい？\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x101,
        (
            "#6P#0000Fえっと、実は今日、\x01",
            "図書館の司書さんから\x01",
            "依頼を受けて来たんです。\x02\x03",

            "返却期限を過ぎている本を\x01",
            "回収したいのですが……\x01",
            "心当たりありませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0714
    ChrTalk(
        0xE,
        (
            "#11Pおお、そういうことか。\x01",
            "私としたことがうっかりしていたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)

    #C0715
    ChrTalk(
        0xE,
        (
            "#11Pちょっと待ってくれたまえ、\x01",
            "丁度、持ってきてたはずだ……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECDF")
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_ECDF")

    Sleep(1000)

    #C0717
    ChrTalk(
        0x101,
        "#6P#0005Fあ、あの？\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x102,
        (
            "#6P#0106Fもしかして、紛失して\x01",
            "しまったんでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)

    #C0719
    ChrTalk(
        0xE,
        (
            "#11Pい、いや、そんなことは\x01",
            "無いはずなんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0xE,
        (
            "#11Pうーん……\x01",
            "どこにやったか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0721
    ChrTalk(
        0xE,
        "#11Pおお、そうだ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)

    #C0722
    ChrTalk(
        0xE,
        (
            "#5Pゴーファン。\x01",
            "この間貸した本、持っているか？\x02",
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
        "#11P本……？\x02",
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xE,
        (
            "#5Pほら、アレだよアレ。\x01",
            "お前が読みたいって言うから\x01",
            "貸した本……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0725
    ChrTalk(
        0xA,
        (
            "#11P……ああ、あの本か！\x01",
            "確かに借りたな。\x01",
            "ちょっと待ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EED6():
        OP_95(0xFE, -1940, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EED6)
    WaitChrThread(0xA, 1)

    def lambda_EEF4():
        OP_95(0xFE, -1940, 0, 6800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EEF4)
    WaitChrThread(0xA, 1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF95")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_EF95")

    Sleep(1000)

    #C0726
    ChrTalk(
        0x104,
        (
            "#6P#0306Fつ、つーか……\x01",
            "図書館の本を\x01",
            "又貸ししてたのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x103,
        "#12P#0200Fずぼらですね……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F029")

    #C0728
    ChrTalk(
        0x109,
        "#6P#0509Fあ、あはは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F060")

    label("loc_F029")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F060")

    #C0729
    ChrTalk(
        0x10A,
        "#6P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_F060")

    SetChrSubChip(0xE, 0x2)

    #C0730
    ChrTalk(
        0xE,
        (
            "#11Pいや、面目ない。\x01",
            "普段ならこういうことは\x01",
            "滅多にないのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0xE,
        (
            "#11Pなにぶん読んでいる本が多くてね。\x01",
            "ついつい忘れていたんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x1)

    #C0732
    ChrTalk(
        0xE,
        (
            "#5Pそれで……\x01",
            "ゴーファン、本は見つかったか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    #C0733
    ChrTalk(
        0xA,
        "#11P………………ない。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F1E6")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_F1E6")

    Sleep(1000)

    #C0734
    ChrTalk(
        0xE,
        (
            "#5Pな、何……？\x01",
            "まさかなくしてしまったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x101,
        "#6P#0012Fあ、あの……\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xA,
        (
            "#11Pいや、ちょっと待ってくれ。\x01",
            "今頑張って思い出そうとしている。\x02",
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
        "#11P…………そうだ！\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xA,
        (
            "#11P確かあの本……\x01",
            "お客さんにせがまれて、\x01",
            "ついつい貸してしまったんだった！\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x101,
        "#6P#0011Fえええええぇっ！！\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x104,
        "#6P#0305F又又貸しかよ……！？\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x102,
        (
            "#6P#0106Fさ、さすがにそれは\x01",
            "予想できなかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        (
            "#12P#0203F……と、いいますか……\x01",
            "ありえないかと。\x02\x03",

            "#0200Fで、どちらに\x01",
            "貸してしまったのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xA,
        (
            "#11P貸したのは、いつも村の入り口で\x01",
            "導力車をいじっているエルキン君だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xA,
        (
            "#11Pいや、本当にすまない……\x01",
            "この通りだ、許してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        (
            "#6P#0006Fい、いえ。\x01",
            "やってしまったものは\x01",
            "もう仕方ないですよ。\x02\x03",

            "#0000Fそれじゃあ……\x01",
            "回収しに行ってみるか。\x01",
            "その、エルキンさんの所に。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F528")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_F528")

    SetChrPos(0x0, -470, 0, 2360, 315)
    SetChrPos(0xE, -2060, 180, 4000, 0)
    SetChrPos(0xA, -40, 0, 6040, 180)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    OP_29(0x28, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_42_E94B end

    SaveToFile()

Try(main)
