from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0420.bin",                # FileName
        "c0420",                    # MapName
        "c0420",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0420",                  # 0
        "イリア",                 # 1
        "リーシャ",               # 2
        "支配人バルサモ",         # 3
        "受付ローランド",         # 4
        "アバン劇団長",           # 5
        "ハインツ",               # 6
        "ユージーン",             # 7
        "テオドール",             # 8
        "ニコル",                 # 9
        "プリエ",                 # 10
        "セリーヌ",               # 11
        "ダドリー捜査官",         # 12
        "エマ捜査官",             # 13
        "レクター",               # 14
        "シュリ",                 # 15
        "捜査官",                 # 16
        "捜査官",                 # 17
        "観客",                   # 18
        "観客",                   # 19
        "観客",                   # 20
        "観客",                   # 21
        "女の子",                 # 22
        "観客",                   # 23
        "観客",                   # 24
        "観客",                   # 25
        "観客",                   # 26
        "マクダエル市長",         # 27
        "秘書アーネスト",         # 28
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch25800.itc",                   # 02
        "chr/ch25900.itc",                   # 03
        "chr/ch27500.itc",                   # 04
        "chr/ch24200.itc",                   # 05
        "chr/ch28700.itc",                   # 06
        "chr/ch28800.itc",                   # 07
        "chr/ch28900.itc",                   # 08
        "chr/ch29000.itc",                   # 09
        "chr/ch29100.itc",                   # 0A
        "chr/ch36600.itc",                   # 0B
        "chr/ch36700.itc",                   # 0C
        "chr/ch36800.itc",                   # 0D
        "chr/ch09800.itc",                   # 0E
        "chr/ch00900.itc",                   # 0F
        "chr/ch30500.itc",                   # 10
        "chr/ch07400.itc",                   # 11
        "chr/ch10100.itc",                   # 12
        "chr/ch27600.itc",                   # 13
        "chr/ch27700.itc",                   # 14
        "chr/ch21600.itc",                   # 15
        "chr/ch21700.itc",                   # 16
        "chr/ch21900.itc",                   # 17
        "chr/ch33102.itc",                   # 18
        "chr/ch22302.itc",                   # 19
        "chr/ch33002.itc",                   # 1A
        "chr/ch33302.itc",                   # 1B
        "chr/ch22000.itc",                   # 1C
        "chr/ch32300.itc",                   # 1D
    ))

    DeclNpc(-209,    0,       15550,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-209,    0,       13819,   360,  261,  0x0, 0,   1,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(769,     15199,   -6840,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(3710,    1799,    6079,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-1879,   9,       15239,   135,  261,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-66489,  0,       7329,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(64750,   0,       3480,    135,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-2549,   1250,    19700,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(64750,   0,       3480,    135,  261,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2250,    0,       14750,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-68129,  0,       2140,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(209,     0,       15229,   270,  389,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(1019,    0,       14640,   270,  389,  0x0, 0,   16,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-22120,  15199,   6940,    45,   389,  0x0, 0,   17,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(67370,   0,       2470,    90,   389,  0x0, 0,   18,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-21100,  15199,   5230,    0,    389,  0x0, 0,   19,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-26899,  15199,   6300,    0,    389,  0x0, 0,   20,  0,   0,   4,   0,   29,  255,  0)
    DeclNpc(-2690,   15199,   -7989,   0,    389,  0x0, 0,   21,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-3779,   15199,   -8229,   0,    389,  0x0, 0,   22,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(-3450,   15199,   -3289,   0,    389,  0x0, 0,   23,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(-8149,   15350,   -3289,   45,   469,  0x0, 0,   24,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(-7150,   15350,   -3680,   0,    469,  0x0, 0,   25,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(2069,    15350,   -4349,   0,    469,  0x0, 0,   26,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(3170,    15350,   -4349,   0,    469,  0x0, 0,   27,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(8800,    15199,   -6800,   315,  405,  0x0, 0,   29,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(7789,    15199,   -5789,   135,  389,  0x0, 0,   28,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 39,  0.0,                   11.880000114440918,    0.0,                   14.0625,               [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.4000000059604645,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.752000331878662,    -0.0,                  1.0])

    ScpFunction((
        "Function_0_594",          # 00, 0
        "Function_1_64C",          # 01, 1
        "Function_2_677",          # 02, 2
        "Function_3_774",          # 03, 3
        "Function_4_7C7",          # 04, 4
        "Function_5_7F2",          # 05, 5
        "Function_6_C4C",          # 06, 6
        "Function_7_D5B",          # 07, 7
        "Function_8_17A3",         # 08, 8
        "Function_9_1919",         # 09, 9
        "Function_10_1A76",        # 0A, 10
        "Function_11_1B7F",        # 0B, 11
        "Function_12_2468",        # 0C, 12
        "Function_13_2750",        # 0D, 13
        "Function_14_28E0",        # 0E, 14
        "Function_15_2CCF",        # 0F, 15
        "Function_16_2DE2",        # 10, 16
        "Function_17_328B",        # 11, 17
        "Function_18_33C5",        # 12, 18
        "Function_19_34C9",        # 13, 19
        "Function_20_35FF",        # 14, 20
        "Function_21_3975",        # 15, 21
        "Function_22_43E5",        # 16, 22
        "Function_23_45F1",        # 17, 23
        "Function_24_4708",        # 18, 24
        "Function_25_47FA",        # 19, 25
        "Function_26_4A73",        # 1A, 26
        "Function_27_4FAF",        # 1B, 27
        "Function_28_50BB",        # 1C, 28
        "Function_29_512D",        # 1D, 29
        "Function_30_531C",        # 1E, 30
        "Function_31_5370",        # 1F, 31
        "Function_32_53DF",        # 20, 32
        "Function_33_542B",        # 21, 33
        "Function_34_55B5",        # 22, 34
        "Function_35_5604",        # 23, 35
        "Function_36_5785",        # 24, 36
        "Function_37_58E7",        # 25, 37
        "Function_38_596A",        # 26, 38
        "Function_39_59E0",        # 27, 39
        "Function_40_6688",        # 28, 40
        "Function_41_66B5",        # 29, 41
        "Function_42_66E2",        # 2A, 42
        "Function_43_66F9",        # 2B, 43
        "Function_44_6710",        # 2C, 44
        "Function_45_6719",        # 2D, 45
        "Function_46_6722",        # 2E, 46
        "Function_47_672B",        # 2F, 47
        "Function_48_6734",        # 30, 48
        "Function_49_6761",        # 31, 49
        "Function_50_678E",        # 32, 50
        "Function_51_67A5",        # 33, 51
        "Function_52_67BC",        # 34, 52
        "Function_53_67DB",        # 35, 53
        "Function_54_67FA",        # 36, 54
        "Function_55_6819",        # 37, 55
        "Function_56_6838",        # 38, 56
        "Function_57_6871",        # 39, 57
        "Function_58_68AA",        # 3A, 58
        "Function_59_6AE0",        # 3B, 59
        "Function_60_6B09",        # 3C, 60
        "Function_61_81C0",        # 3D, 61
        "Function_62_820B",        # 3E, 62
        "Function_63_84BE",        # 3F, 63
        "Function_64_84E5",        # 40, 64
        "Function_65_9892",        # 41, 65
        "Function_66_9AC9",        # 42, 66
        "Function_67_9D37",        # 43, 67
        "Function_68_9D62",        # 44, 68
        "Function_69_9D8D",        # 45, 69
    ))


    def Function_0_594(): pass

    label("Function_0_594")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5D4"),
        (1, "loc_5E0"),
        (2, "loc_5EC"),
        (3, "loc_5F8"),
        (4, "loc_604"),
        (5, "loc_610"),
        (6, "loc_61C"),
        (SWITCH_DEFAULT, "loc_628"),
    )


    label("loc_5D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_5E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_5EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_5F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_604")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_610")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_61C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_628")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_634")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_634")

    label("loc_64B")

    Return()

    # Function_0_594 end

    def Function_1_64C(): pass

    label("Function_1_64C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_676")
    OP_94(0xFE, 0xF4D8, 0x532, 0x1054A, 0x15AE, 0x3E8)
    Sleep(300)
    Jump("Function_1_64C")

    label("loc_676")

    Return()

    # Function_1_64C end

    def Function_2_677(): pass

    label("Function_2_677")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_773")
    OP_95(0xFE, -2550, 1250, 19700, 5000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x2EE)
    Sleep(300)
    BeginChrThread(0xFE, 1, 0, 53)
    OP_9D(0xFE, 0xFFFFF830, 0x4E2, 0x4CF4, 0x12C, 0x5DC)
    OP_9D(0xFE, 0xFFFFFC18, 0x4E2, 0x4CF4, 0x1F4, 0x3E8)
    BeginChrThread(0xFE, 1, 0, 52)
    OP_9D(0xFE, 0x7D0, 0x4E2, 0x4CF4, 0x2BC, 0x2BC)
    EndChrThread(0xFE, 0x1)
    OP_95(0xFE, 2550, 1250, 19700, 5000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x2EE)
    Sleep(300)
    BeginChrThread(0xFE, 1, 0, 53)
    OP_9D(0xFE, 0x7D0, 0x4E2, 0x4CF4, 0x12C, 0x5DC)
    OP_9D(0xFE, 0x3E8, 0x4E2, 0x4CF4, 0x1F4, 0x3E8)
    BeginChrThread(0xFE, 1, 0, 52)
    OP_9D(0xFE, 0xFFFFF830, 0x4E2, 0x4CF4, 0x2BC, 0x2BC)
    EndChrThread(0xFE, 0x1)
    Jump("Function_2_677")

    label("loc_773")

    Return()

    # Function_2_677 end

    def Function_3_774(): pass

    label("Function_3_774")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C6")
    OP_95(0xFE, 61750, 0, 3480, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x2EE)
    Sleep(300)
    OP_95(0xFE, 66750, 0, 3480, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x2EE)
    Sleep(300)
    Jump("Function_3_774")

    label("loc_7C6")

    Return()

    # Function_3_774 end

    def Function_4_7C7(): pass

    label("Function_4_7C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F1")
    OP_94(0xFE, 0xFFFF9C32, 0x1C0C, 0xFFFF8F8A, 0x1108, 0x3E8)
    Sleep(300)
    Jump("Function_4_7C7")

    label("loc_7F1")

    Return()

    # Function_4_7C7 end

    def Function_5_7F2(): pass

    label("Function_5_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_808")
    Event(0, 64)
    Jump("loc_819")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_819")
    Event(0, 69)

    label("loc_819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_828")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 60)

    label("loc_828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_880")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0xD, -65800, 0, 6680, 0)
    SetChrPos(0x16, -66490, 0, 7330, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87B")
    SetChrFlags(0xD, 0x10)

    label("loc_87B")

    Jump("loc_C4B")

    label("loc_880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_901")
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x9, 0, 0, 14000, 0)
    SetChrPos(0x8, 750, 0, 15500, 225)
    SetChrPos(0xC, -750, 0, 15500, 135)
    SetChrPos(0x16, -68150, 0, 2150, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FC")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2250, 0, 14250, 90)

    label("loc_8FC")

    Jump("loc_C4B")

    label("loc_901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_93B")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x16, 0x80)
    TurnDirection(0xC, 0x8, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_C4B")

    label("loc_93B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_9AF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0xC, -21940, 15200, 4850, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97D")
    SetChrFlags(0xC, 0x10)

    label("loc_97D")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_C4B")

    label("loc_9AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A2E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xA, -20, 0, 14380, 315)
    SetChrPos(0xE, -910, 1250, 25550, 90)
    SetChrPos(0xF, 940, 1250, 25550, 270)
    SetChrPos(0x10, 66420, 0, 1580, 90)
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A29")
    SetChrFlags(0xE, 0x10)

    label("loc_A29")

    Jump("loc_C4B")

    label("loc_A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A55")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_C4B")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_A63")
    Jump("loc_C4B")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_B32")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0xC, -1940, 900, 10160, 0)
    SetChrPos(0x8, 1860, 900, 10150, 0)
    SetChrPos(0xE, -5140, 1350, 8470, 0)
    SetChrPos(0x10, 0, 1250, 22620, 180)
    SetChrPos(0xD, 960, 1800, 6150, 0)
    SetChrPos(0x13, 2670, 15200, -7100, 0)
    SetChrPos(0x14, 1690, 15200, -8109, 0)
    SetChrChipByIndex(0xF, 0xC)
    SetChrChipByIndex(0x10, 0xD)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x14, 0x10)
    BeginChrThread(0xF, 0, 0, 2)
    Jump("loc_C4B")

    label("loc_B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B8A")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    TurnDirection(0xC, 0x13, 0)
    SetChrPos(0x9, -68120, 0, 2180, 270)
    SetChrChipByIndex(0xE, 0xB)
    BeginChrThread(0xE, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B85")
    SetChrFlags(0xE, 0x10)

    label("loc_B85")

    Jump("loc_C4B")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_BDB")
    SetChrFlags(0x10, 0x80)
    TurnDirection(0xC, 0x8, 0)
    TurnDirection(0x8, 0xC, 0)
    SetChrChipByIndex(0x9, 0xE)
    SetChrPos(0x9, 4150, 1250, 24490, 225)
    SetChrPos(0xD, 3170, 1250, 23150, 45)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_C4B")

    label("loc_BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_C31")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xC, -700, 15200, -6830, 90)
    SetChrPos(0x8, 650, 1250, 25470, 270)
    SetChrPos(0xD, -650, 1250, 25470, 90)
    SetChrFlags(0x10, 0x10)
    BeginChrThread(0x10, 0, 0, 3)
    Jump("loc_C4B")

    label("loc_C31")

    BeginChrThread(0x10, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4B")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_C4B")

    Return()

    # Function_5_7F2 end

    def Function_6_C4C(): pass

    label("Function_6_C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C64")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C7B")

    label("loc_C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x213), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_CA3")
    SetMapObjFrame(0xFF, "pos01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x1, 0x1)
    Jump("loc_CBD")

    label("loc_CA3")

    SetMapObjFrame(0xFF, "pos01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pos02", 0x0, 0x1)

    label("loc_CBD")

    SetMapObjFlags(0x1C, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD7")
    ClearMapObjFlags(0x1C, 0x4)

    label("loc_CD7")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_CEA")
    Jump("loc_D02")

    label("loc_CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D02")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3A")
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xF, -2550, 1250, 19700, 0)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x1)
    BeginChrThread(0xF, 0, 0, 2)

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5A")
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_D5A")

    Return()

    # Function_6_C4C end

    def Function_7_D5B(): pass

    label("Function_7_D5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DD9")

    #C0001
    ChrTalk(
        0xC,
        (
            "今日の公演は\x01",
            "役をやりくりして何とかしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xC,
        (
            "……ニコル君が\x01",
            "戻ってきてくれるのが\x01",
            "一番いいんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179F")

    label("loc_DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DEA")
    Call(0, 12)
    Jump("loc_179F")

    label("loc_DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_F69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EB5")

    #C0003
    ChrTalk(
        0xC,
        (
            "貴賓席のお客様は\x01",
            "私がご案内する事にしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xC,
        (
            "だが……今日は\x01",
            "変わったお客様だね……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xC,
        (
            "それもこの歳で貴賓席なんて……\x01",
            "そういった方面にツテでも\x01",
            "ある人なんだろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F64")

    label("loc_EB5")

    OP_4B(0x15, 0xFF)

    #C0006
    ChrTalk(
        0x15,
        (
            "#3509Fおお、リッチ～。\x01",
            "見晴らしイイじゃん？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xC,
        (
            "ははは……公演時刻は\x01",
            "約１０分後となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xC,
        (
            "『金の太陽、銀の月』、\x01",
            "どうぞごゆっくりお楽しみ下さい。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x15, 0xFF)

    label("loc_F64")

    Jump("loc_179F")

    label("loc_F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10E9")
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FF4")

    #C0009
    ChrTalk(
        0xC,
        (
            "私も外国公演はしないと\x01",
            "決めているわけではないんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xC,
        (
            "……バルサモ君、悪いが\x01",
            "一度検討してくれるかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E0")

    label("loc_FF4")


    #C0011
    ChrTalk(
        0xC,
        "ふむ、興行の話だね……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xC,
        (
            "私もキリカさんの話には\x01",
            "心を動かされるものがあったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        (
            "あの人はどうやら\x01",
            "アルカンシェルの芸術性を\x01",
            "理解しているようだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        (
            "……バルサモ君、悪いが\x01",
            "検討してみてくれるかな。\x01",
            "任せきりで悪いんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10E0")

    OP_4C(0xA, 0xFF)
    Jump("loc_179F")

    label("loc_10E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1188")

    #C0015
    ChrTalk(
        0xC,
        (
            "イリア君の指導のかいあって\x01",
            "リーシャ君の実力も上がっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xC,
        (
            "残りのメンバーが付いてこれれば\x01",
            "素晴らしい舞台になるはずだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123D")

    label("loc_1188")


    #C0017
    ChrTalk(
        0xC,
        "おや、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xC,
        (
            "色々ごたごたしてしまっているが、\x01",
            "稽古は進めないとねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        (
            "リーシャ君も近頃めきめきと\x01",
            "演技力を上げている……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xC,
        "みんなにも頑張ってもらわないとね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_123D")

    Jump("loc_179F")

    label("loc_1242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_143C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12FA")

    #C0021
    ChrTalk(
        0xC,
        (
            "（捜査一課の方が早速やってきてね。\x01",
            "  朝から事情聴取なんだ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xC,
        (
            "（しかし……こんな日に限って\x01",
            "  イリア君は寝坊でね。\x01",
            "  まったく冷や冷やさせてくれるよ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1437")

    label("loc_12FA")

    OP_4B(0x13, 0xFF)
    TurnDirection(0xC, 0x13, 0)

    #C0023
    ChrTalk(
        0xC,
        "劇場内の見取り図ですか……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xC,
        (
            "アルカンシェルのパンフレットに\x01",
            "一応記載はされているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x13,
        (
            "#0603Fいえ、できれば施工当時の\x01",
            "設計図でお願いしたい。\x02\x03",

            "#0600F通用口、資材搬入路、物置き、\x01",
            "舞台装置や換気ダクトの配置ポイント。\x01",
            "……全てです。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xC,
        (
            "わ、分かりました。\x01",
            "すぐに探してみましょう……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 0)

    label("loc_1437")

    Jump("loc_179F")

    label("loc_143C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_14EA")

    #C0027
    ChrTalk(
        0xC,
        (
            "ともかく、ことの真偽が\x01",
            "分かっただけでも助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        "君達の協力には本当に感謝する。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "チケットは後日送らせてもらうから\x01",
            "楽しみにしていてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179F")

    label("loc_14EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1655")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_156F")

    #C0030
    ChrTalk(
        0xC,
        (
            "新作の公開前には\x01",
            "事務方の仕事も忙しくなるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xC,
        (
            "例の脅迫状の一件……\x01",
            "ただの悪戯であればいいんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1650")

    label("loc_156F")


    #C0032
    ChrTalk(
        0xC,
        (
            "今度の新作は\x01",
            "ファンの間でも人気が高くてね。\x01",
            "ただでさえ混雑が予想されるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xC,
        (
            "万全の体制をもってお客様を迎え、\x01",
            "心の底から楽しんでもらうこと……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xC,
        (
            "劇場の使命を果たすためにも\x01",
            "綿密な打ち合わせは欠かせないんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1650")

    Jump("loc_179F")

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16D3")

    #C0035
    ChrTalk(
        0xC,
        (
            "警察の方で捜査を\x01",
            "引き受けてくれるとは心強い。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xC,
        (
            "脅迫文の事は全てお任せしよう。\x01",
            "どうかよろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179F")

    label("loc_16D3")


    #C0037
    ChrTalk(
        0xC,
        (
            "自分が狙われているんだ、\x01",
            "イリア君も少しは\x01",
            "心配してくれればいいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xC,
        (
            "……こほん、ともかく\x01",
            "脅迫文の事は君達にお任せしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xC,
        (
            "何か分かったら\x01",
            "すぐに教えてくれたまえ。\x01",
            "よろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_179F")

    TalkEnd(0xFE)
    Return()

    # Function_7_D5B end

    def Function_8_17A3(): pass

    label("Function_8_17A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_187B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C1")
    Call(0, 9)
    Jump("loc_1876")

    label("loc_17C1")


    #C0040
    ChrTalk(
        0xA,
        (
            "実は共和国での公演を\x01",
            "検討している所なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xA,
        (
            "先日共和国からいらした\x01",
            "キリカ殿の打診は中々魅力的でしたもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "一度じっくり検討してみる\x01",
            "価値があるように思うのです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1876")

    Jump("loc_1915")

    label("loc_187B")


    #C0043
    ChrTalk(
        0xA,
        (
            "脅迫文の真偽は判りませんが、\x01",
            "支配人として\x01",
            "劇場の安全は守らねば……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "ふむ、公演前の見回りを\x01",
            "強化いたしましょうか。\x01",
            "何もしないよりは良いでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1915")

    TalkEnd(0xFE)
    Return()

    # Function_8_17A3 end

    def Function_9_1919(): pass

    label("Function_9_1919")


    #C0045
    ChrTalk(
        0xFE,
        (
            "そうそう、当劇団では\x01",
            "新しい下働きの子を雇いましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "シュリと申します。\x01",
            "見かけたら仲良くしてやって下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A72")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19E1")

    #C0047
    ChrTalk(
        0x102,
        (
            "#0100Fふふ、元気にやっている\x01",
            "みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A72")

    label("loc_19E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A2D")

    #C0048
    ChrTalk(
        0x103,
        (
            "#0200F……どうやら元気に\x01",
            "やっているみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A72")

    label("loc_1A2D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A72")

    #C0049
    ChrTalk(
        0x104,
        (
            "#0300Fへっ、どうやら\x01",
            "元気にやってるみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A72")

    SetScenarioFlags(0xD1, 6)
    Return()

    # Function_9_1919 end

    def Function_10_1A76(): pass

    label("Function_10_1A76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B0C")

    #C0050
    ChrTalk(
        0xB,
        (
            "自分も稽古の準備を\x01",
            "手伝っているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "プレ公演まで\x01",
            "もう二週間を切っていますし、\x01",
            "皆さんには仕上げに専念して頂かないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7B")

    label("loc_1B0C")


    #C0052
    ChrTalk(
        0xB,
        "次のシーンの照明は、と……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "やれやれ、捜査一課の方が\x01",
            "うろうろなさるから\x01",
            "準備が遅れてしまいますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1B7B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A76 end

    def Function_11_1B7F(): pass

    label("Function_11_1B7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1DBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1BFE")

    #C0054
    ChrTalk(
        0x8,
        (
            "#1701Fそういえば、昨日の夜は\x01",
            "特に様子がおかしかったわね。\x02\x03",

            "#1706F……今思い返せば、なんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB5")

    label("loc_1BFE")


    #C0055
    ChrTalk(
        0x8,
        (
            "#1706Fそういえば、昨晩は\x01",
            "特に様子がおかしかったわね。\x02\x03",

            "#1701Fハイになってるっていうか……\x01",
            "あたしのことも睨んできたもの。\x02\x03",

            "#1709Fもちろん睨み返してやったけどね！\x02",
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

    #C0056
    ChrTalk(
        0x101,
        (
            "#0012F何と言いますか……\x01",
            "イリアさんらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0108Fでも、よりによってイリアさんに\x01",
            "そんな態度を取るなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        (
            "#0303Fふむ……\x01",
            "とても新人とは思えねぇな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1DB5")

    Jump("loc_2464")

    label("loc_1DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1DCB")
    Call(0, 12)
    Jump("loc_2464")

    label("loc_1DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1E2F")

    #C0059
    ChrTalk(
        0x8,
        (
            "#1701F#11P──そこ！\x01",
            "もっと躍動感を出して！\x02\x03",

            "そう、リズムを取って！\x01",
            "弾むように！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2464")

    label("loc_1E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1EE0")

    #C0060
    ChrTalk(
        0x8,
        (
            "#1703F弟君に担当して\x01",
            "もらえないのは残念だけど……\x02\x03",

            "#1700Fま、今回は仕方ないわね。\x02\x03",

            "#1706F……はあ、ただの\x01",
            "嫌がらせだと思ったのに\x01",
            "面倒な事になってきたわね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2464")

    label("loc_1EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_21FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F67")

    #C0061
    ChrTalk(
        0x8,
        (
            "#1704Fリーシャはまだまだ伸びる。\x01",
            "あの子には期待してるわ。\x02\x03",

            "#1702Fフフ、こっちもレベル\x01",
            "上げていかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_1F67")


    #C0062
    ChrTalk(
        0x8,
        (
            "#1703Fあたし一人の舞台なら\x01",
            "文句のない完成度なんだけど。\x02\x03",

            "#1700Fリーシャったら\x01",
            "かなり良い演技をするのよ。\x02\x03",

            "あたしの方もレベル上げていかないと\x01",
            "良い舞台にならないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0002Fへえ……彼女って\x01",
            "やっぱり才能あるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#0305Fそういや、準主役へ抜擢された\x01",
            "大型新人の割には\x01",
            "そんな雰囲気ないッスよね。\x02\x03",

            "#0309Fどっちかっていうと\x01",
            "癒し系っつーか、和み系っつーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#1702Fふふっ、あの子はウチの中でも\x01",
            "トップクラスでしょうね。\x02\x03",

            "#1704Fあの子自身、\x01",
            "気付いてないかもしれないけど、\x01",
            "潜在能力はあたしと同等の力がある。\x02\x03",

            "#1701Fううん、将来は\x01",
            "あたしを越えるかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#0105Fそ、そんなに……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x103,
        (
            "#0204F……リーシャさんの演技も\x01",
            "一度観てみたいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_21FA")

    Jump("loc_2464")

    label("loc_21FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2461")

    #C0068
    ChrTalk(
        0x8,
        (
            "#1704Fふふっ、\x01",
            "今度の公演は凄いわよ～。\x02\x03",

            "#1702F太陽を象徴するあたしと\x01",
            "月を象徴するリーシャの対比。\x02\x03",

            "激しく衝突しながらも\x01",
            "二つの光は融けあい、やがて\x01",
            "一つの舞台へと昇華していく……\x02\x03",

            "#1709Fお披露目まで日数もないし\x01",
            "もっと飛ばしていかないとね！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235B")

    #C0069
    ChrTalk(
        0x101,
        (
            "#0012F（うーん、もう舞台のことで\x01",
            "  頭が一杯みたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2459")

    label("loc_235B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A1")

    #C0070
    ChrTalk(
        0x102,
        (
            "#0102F（舞台のことで\x01",
            "  頭が一杯みたいね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2459")

    label("loc_23A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23EB")

    #C0071
    ChrTalk(
        0x103,
        (
            "#0202F（舞台のことで\x01",
            "  頭が一杯みたいですね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2459")

    label("loc_23EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2459")

    #C0072
    ChrTalk(
        0x104,
        (
            "#0309F（さすがはイリア・プラティエ。\x01",
            "  脅迫状のことなんざ\x01",
            "  もう忘れちまったみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2459")

    SetScenarioFlags(0x0, 3)

    label("loc_245C")

    Jump("loc_2464")

    label("loc_2461")

    Call(0, 13)

    label("loc_2464")

    TalkEnd(0xFE)
    Return()

    # Function_11_1B7F end

    def Function_12_2468(): pass

    label("Function_12_2468")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2582")

    #C0073
    ChrTalk(
        0xC,
        "そうそう、それと例の話だが……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "#1705F#11Pああ、ニコルね。\x02\x03",

            "#1706F確かに妙に調子はいいけど、\x01",
            "あの子の役柄を考えると\x01",
            "バランス的にはちょっとね～。\x02\x03",

            "#1709Fそうだ！\x01",
            "いっそ彼とテオの一騎打ちを\x01",
            "追加シーンにしてみるとか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xC,
        "はぁ、勘弁してくれたまえ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2747")

    label("loc_2582")


    #C0076
    ChrTalk(
        0x8,
        (
            "#1703F#11Pん～、あたし的には\x01",
            "そんな演出はあり得ないわね。\x02\x03",

            "#1701F追加シーンを入れるんなら\x01",
            "もっとガッチリ\x01",
            "心を掴む物をやるべきだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        (
            "ふむ……しかし舞台として\x01",
            "別物にはしたくないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        (
            "君の意見は尊重するが\x01",
            "何とか考えてくれないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        "#1706F#11P──ヤダ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0080
    ChrTalk(
        0xC,
        "そう言うと思ったよ……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        (
            "#0200F（舞台の相談中みたいですね……\x01",
            "  劇団長さんが押されていますが。）\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0000F（俺たちは\x01",
            "  邪魔しないでおこう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2747")

    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_2468 end

    def Function_13_2750(): pass

    label("Function_13_2750")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0083
    ChrTalk(
        0x8,
        (
            "#1702Fそれじゃリーシャ、\x01",
            "昨日の続きに行くわよ。\x02\x03",

            "#1704F舞台合わせの場合は\x01",
            "自分なりのタイミングを掴む事。\x02\x03",

            "相手に合わせるだけじゃダメだし\x01",
            "自分のペースを押し付けてもダメよ。\x02\x03",

            "#1700Fこの辺り、最後は\x01",
            "自分で掴むしかないと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        "まあそういう事だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xC,
        (
            "あまり時間もないし\x01",
            "ともかく合わせに入ってみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "#1800Fは、はいっ！\x01",
            "よろしくお願いします！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_2750 end

    def Function_14_28E0(): pass

    label("Function_14_28E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2974")

    #C0087
    ChrTalk(
        0x9,
        (
            "#1806Fニコルさん、最近\x01",
            "様子がおかしかったんです。\x01",
            "性格が変わってしまったというか……\x02\x03",

            "#1808F………………………………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A42")

    label("loc_2974")


    #C0088
    ChrTalk(
        0x9,
        (
            "#1806Fニコルさん、最近\x01",
            "様子がおかしかったんです。\x02\x03",

            "#1808F………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0000Fリーシャ、心配しないでくれ。\x01",
            "俺たちで調べてみるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "#1810Fはい……\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2A42")

    Jump("loc_2CCB")

    label("loc_2A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2AE9")

    #C0091
    ChrTalk(
        0x9,
        (
            "#1806Fプレ公演も近いし、\x01",
            "もっと稽古しないとって\x01",
            "気が焦っちゃうんですけど。\x02\x03",

            "#1810F今日はイリアさんも遅刻だし\x01",
            "焦っても仕方ないのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C15")

    label("loc_2AE9")


    #C0092
    ChrTalk(
        0x9,
        (
            "#1802Fあ、皆さん……\x01",
            "おはようございます。\x02\x03",

            "#1804Fあの、調査の方は本当に\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0012Fはは、どういたしまして。\x02\x03",

            "#0000F……捜査一課も\x01",
            "早速来てるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#1809Fあはは……私も\x01",
            "事情聴取されてしまいました。\x02\x03",

            "#1810F今日はイリアさんも遅刻だし\x01",
            "焦っても仕方ないですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2C15")

    Jump("loc_2CCB")

    label("loc_2C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2C2B")
    Call(0, 15)
    Jump("loc_2CCB")

    label("loc_2C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2CC8")

    #C0095
    ChrTalk(
        0x9,
        (
            "#1806Fすみません、\x01",
            "稽古が立て込んでいて……\x02\x03",

            "#1802Fでも、やっぱり皆さんに\x01",
            "相談して良かったです。\x02\x03",

            "脅迫状のこと、\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CCB")

    label("loc_2CC8")

    Call(0, 13)

    label("loc_2CCB")

    TalkEnd(0xFE)
    Return()

    # Function_14_28E0 end

    def Function_15_2CCF(): pass

    label("Function_15_2CCF")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0096
    ChrTalk(
        0xD,
        (
            "分かりました、\x01",
            "シーン１８からもう一度ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "舞台をセットしますから\x01",
            "少し待っていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        "#6201Fはい、よろしくお願いします！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD9")

    #C0099
    ChrTalk(
        0x101,
        "#0005F（忙しそうだな……）\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0304F（プレ公演に向けた最終調整……\x01",
            "  ま、邪魔しちゃ悪いな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2DD9")

    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_2CCF end

    def Function_16_2DE2(): pass

    label("Function_16_2DE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2E3C")

    #C0101
    ChrTalk(
        0xE,
        "悪いな、稽古中なんだ。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        "見学なら客席からお願いするぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F11")

    label("loc_2E3C")

    OP_4B(0xF, 0xFF)

    #C0103
    ChrTalk(
        0xE,
        "オーケー、次は最終幕に行こう。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xE,
        (
            "フッ……寝起きの剣士よ。\x01",
            "私に付いて来れるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xF,
        "……最終幕だな、問題ない……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xF,
        "………《月の姫》のシーンだったか？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xE,
        "オイオイ、真面目にやれよな！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 5)
    OP_4C(0xF, 0xFF)

    label("loc_2F11")

    Jump("loc_3287")

    label("loc_2F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3032")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F86")

    #C0108
    ChrTalk(
        0xE,
        "問題はニコルだな……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xE,
        (
            "あいつも努力はしてるんだが\x01",
            "イマイチぱっとしないんだよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302D")

    label("loc_2F86")


    #C0110
    ChrTalk(
        0xE,
        (
            "テオドールのヤツは\x01",
            "舞台に上がると\x01",
            "恐ろしく雄弁な演技をしやがるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xE,
        (
            "やれやれ、しかも今日は\x01",
            "一段と調子がいいみたいだな。\x01",
            "超一流スターのオレも舌を巻くぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_302D")

    Jump("loc_3287")

    label("loc_3032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_308A")

    #C0112
    ChrTalk(
        0xE,
        (
            "あ、それと……\x01",
            "この事も誰にも言うなよ。\x01",
            "一応秘密の練習なんだからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3287")

    label("loc_308A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_313A")

    #C0113
    ChrTalk(
        0xE,
        (
            "あのイリア相手じゃ\x01",
            "オレだって仕上げに時間を掛けるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xE,
        (
            "……リーシャなんて\x01",
            "そりゃもう大変だろうな。\x01",
            "同情しちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xE,
        "おっと、これは内緒だけどな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3287")

    label("loc_313A")


    #C0116
    ChrTalk(
        0xE,
        "ふう、こんなところか……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xE, 0x0, 750)
    Sleep(750)

    #C0117
    ChrTalk(
        0xE,
        (
            "な、なんだ警察の人か。\x01",
            "ったく驚かすなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0005Fえっと……\x01",
            "こんな所で稽古ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xE,
        (
            "ああ、今回は\x01",
            "あのイリアとの\x01",
            "対面シーンがあるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xE,
        (
            "彼女の強烈な光を\x01",
            "打ち消さないよう、かつ\x01",
            "こっちの役も負けないように……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xE,
        (
            "オレだって\x01",
            "仕上げに時間を掛けるぜ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_3287")

    TalkEnd(0xFE)
    Return()

    # Function_16_2DE2 end

    def Function_17_328B(): pass

    label("Function_17_328B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3319")

    #C0122
    ChrTalk(
        0xF,
        (
            "そういえば……\x01",
            "下働きの子が入ったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xF,
        (
            "……なかなかいい\x01",
            "身のこなしをしていた……\x01",
            "あいつは才能があるかもな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C1")

    label("loc_3319")


    #C0124
    ChrTalk(
        0xF,
        (
            "……休日だというのに\x01",
            "ユージーンに呼び出された。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0125
    ChrTalk(
        0xF,
        "少し眠い……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#0003F（劇団の人って……\x01",
            "  演技中とのギャップが凄いよな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_33C1")

    TalkEnd(0xFE)
    Return()

    # Function_17_328B end

    def Function_18_33C5(): pass

    label("Function_18_33C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3446")

    #C0127
    ChrTalk(
        0x11,
        (
            "ニコル君は悩むタイプなの。\x01",
            "前から気に掛けてはいたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x11,
        (
            "ふう……どこで　\x01",
            "何をしてるのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C5")

    label("loc_3446")


    #C0129
    ChrTalk(
        0x11,
        (
            "脚本の調整が入るって事は\x01",
            "演技も変えないといけないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x11,
        (
            "ふう……ニコル君のことは\x01",
            "私も気に掛けていたんだけどね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_34C5")

    TalkEnd(0xFE)
    Return()

    # Function_18_33C5 end

    def Function_19_34C9(): pass

    label("Function_19_34C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3536")

    #C0131
    ChrTalk(
        0x12,
        (
            "リーシャばかりでなくニコルにも\x01",
            "抜かれてしまいそうですわ……\x01",
            "わたくしも頑張りませんと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FB")

    label("loc_3536")


    #C0132
    ChrTalk(
        0x12,
        (
            "ニ、ニコルは\x01",
            "最近絶好調ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x12,
        (
            "今日のリハーサルも\x01",
            "素晴らしい演技でしたわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x12)

    #C0134
    ChrTalk(
        0x12,
        (
            "……い、いけない。\x01",
            "リーシャばかりでなくニコルにも\x01",
            "抜かれてしまいそうですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_35FB")

    TalkEnd(0xFE)
    Return()

    # Function_19_34C9 end

    def Function_20_35FF(): pass

    label("Function_20_35FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_372F")
    OP_64(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3678")

    #C0135
    ChrTalk(
        0x10,
        (
            "はあ、世の中はうまく\x01",
            "いかないもんだよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x10,
        (
            "リーシャはあんなに\x01",
            "認められてるのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3718")

    label("loc_3678")


    #C0137
    ChrTalk(
        0x10,
        (
            "昨日の公演で\x01",
            "大失敗をやらかしちまったんだ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x10,
        (
            "ううっ、記念祭でも\x01",
            "細かいミスが多かったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x10,
        (
            "まじめに稽古してるつもりなのに、\x01",
            "落ち込むよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_3718")

    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3971")

    label("loc_372F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_37DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3770")

    #C0140
    ChrTalk(
        0xFE,
        "はあ、ちっともうまく行かないなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37D7")

    label("loc_3770")


    #C0141
    ChrTalk(
        0x10,
        (
            "ここからこうで、\x01",
            "回転に繋げて……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……うーん、何か違うな。\x01",
            "ちっともうまく行かないぞ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_37D7")

    Jump("loc_3971")

    label("loc_37DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38FF")

    #C0143
    ChrTalk(
        0xFE,
        "今度の新作、僕も役をもらえたんだよ。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "一番下の端役だけど、\x01",
            "それでもアルカンシェルの舞台だしね。\x01",
            "まあ僕的には万々歳かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "でも……リーシャは\x01",
            "準主役を貰ったんだよな。\x01",
            "僕より後に入団したはずなのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "ううっ、焦っちまうよ。\x01",
            "やっぱり僕なんかとは違うのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3971")

    label("loc_38FF")


    #C0147
    ChrTalk(
        0xFE,
        (
            "リーシャの才能は本物だよ。\x01",
            "大役を貰ったのも頷けるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "それに較べて僕は……\x01",
            "……ううっ、焦っちまうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3971")

    TalkEnd(0xFE)
    Return()

    # Function_20_35FF end

    def Function_21_3975(): pass

    label("Function_21_3975")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3B12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A74")
    OP_4B(0x16, 0xFF)

    #C0149
    ChrTalk(
        0xD,
        "ええと、天幕の巻き上げ速度を変更……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xD,
        (
            "舞台のせり出し方はＢにセットして\x01",
            "照明と音楽もタイミングを取って……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x16,
        "……分かった、こうだな？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xD,
        (
            "ええ、そのまま、そのまま……\x01",
            "本番もこの通りにお願いしますよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x16, 0xFF)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x1, 3)
    Jump("loc_3B0D")

    label("loc_3A74")


    #C0153
    ChrTalk(
        0xD,
        (
            "こんな時間から台本を調整だなんて、\x01",
            "舞台裏は大変ですよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xD,
        (
            "はあ、でもシュリさんが\x01",
            "居てくださって助かった。\x01",
            "天幕の制御はお任せしてしまおうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0D")

    Jump("loc_43E1")

    label("loc_3B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3BA5")

    #C0155
    ChrTalk(
        0xD,
        (
            "記念祭の後、ニコルさんは\x01",
            "思いつめていたようでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xD,
        (
            "その後の根を詰めての稽古……\x01",
            "私達も少し心配していたんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C10")

    label("loc_3BA5")


    #C0157
    ChrTalk(
        0xD,
        "ニコルさんが居なくなったとか……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        (
            "最近根を詰めて\x01",
            "稽古していたようですし、\x01",
            "そのせいでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_3C10")

    Jump("loc_43E1")

    label("loc_3C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3D48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3C88")

    #C0159
    ChrTalk(
        0xD,
        (
            "ニコルさんはいつ\x01",
            "休まれているのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "近頃少々熱を入れすぎな\x01",
            "気がしますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D43")

    label("loc_3C88")


    #C0161
    ChrTalk(
        0xD,
        (
            "昨晩も舞台装置が\x01",
            "勝手に動かされていましてね……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xD,
        (
            "どうやらまたニコルさんが\x01",
            "徹夜で稽古なさっていたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xD,
        (
            "熱心なのはよいのですが、\x01",
            "少々熱を入れすぎでは\x01",
            "ないでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_3D43")

    Jump("loc_43E1")

    label("loc_3D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E14")

    #C0164
    ChrTalk(
        0xFE,
        (
            "実は先日、知り合いの\x01",
            "工房を訪ねたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "なんと可愛らしい\x01",
            "お孫さんが迎えてくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "ふむ、あのご老人にお孫さんが\x01",
            "いらっしゃるとは知りませんでしたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_3EBD")

    label("loc_3E14")


    #C0167
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの舞台装置に関して\x01",
            "手をお借りしている工房がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "しかし……あの方にお孫さんが\x01",
            "いらっしゃるとは知りませんでした。\x01",
            "……いや、驚きましたね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EBD")

    Jump("loc_43E1")

    label("loc_3EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3FFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3F49")

    #C0169
    ChrTalk(
        0xD,
        (
            "本番は捜査官の方が\x01",
            "あちこちに立たれるそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xD,
        (
            "照明をさえぎる事になったり\x01",
            "しなければいいんですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_3F49")


    #C0171
    ChrTalk(
        0xD,
        (
            "ふむ、このシーンの照明角度は\x01",
            "こんなものでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xD,
        (
            "しかし……本番は捜査官の方が\x01",
            "あちこちに立たれるそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xD,
        (
            "照明をさえぎることに\x01",
            "ならないか心配ですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_3FF7")

    Jump("loc_43E1")

    label("loc_3FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_417A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40DC")

    #C0174
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの舞台装置には\x01",
            "繊細かつ大胆な表現力が求められます。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "ですから一朝一夕に、\x01",
            "というわけにはいきません。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "知り合いの工房の手なども借りて\x01",
            "少しずつ完成に近づけていくのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4175")

    label("loc_40DC")


    #C0177
    ChrTalk(
        0xFE,
        (
            "アルカンシェルを支える\x01",
            "この舞台装置もまた、\x01",
            "一つの芸術品のようなものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "知り合いの工房の手なども借りて\x01",
            "一歩一歩完成に近づけていくのですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4175")

    Jump("loc_43E1")

    label("loc_417A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_418B")
    Call(0, 15)
    Jump("loc_43E1")

    label("loc_418B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4207")

    #C0179
    ChrTalk(
        0xD,
        (
            "やれやれ、\x01",
            "イリアさんも無茶を仰りますね。\x01",
            "そんな調整ができるかどうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xD,
        "勿論、試してはみますけれど。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43E1")

    label("loc_4207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4281")

    #C0181
    ChrTalk(
        0xD,
        (
            "イリアさんの舞台に\x01",
            "掛ける熱意は大したものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xD,
        (
            "監督である劇団長に\x01",
            "意見を付けるくらいですからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E1")

    label("loc_4281")


    #C0183
    ChrTalk(
        0xD,
        (
            "これは……劇団長の\x01",
            "仰っていた警察の方ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xD,
        (
            "見学なら構いませんが、\x01",
            "手を触れないようお願いしますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#0005Fこれは……\x01",
            "舞台装置ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xD,
        (
            "ええ、アルカンシェルの\x01",
            "劇を支える特注の舞台装置です。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xD,
        (
            "イリアさんから\x01",
            "注文がつきましてね、\x01",
            "演出を調整中なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xD,
        (
            "やれやれ、また難しい注文をなさる。\x01",
            "あの人の熱意は劇団長以上ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_43E1")

    TalkEnd(0xFE)
    Return()

    # Function_21_3975 end

    def Function_22_43E5(): pass

    label("Function_22_43E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4403")
    Call(0, 24)
    Jump("loc_4490")

    label("loc_4403")


    #C0189
    ChrTalk(
        0xFE,
        (
            "#0603F……特務支援課、ウロウロするな。\x02\x03",

            "それとも私の言葉が判らないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#0006Fいえ、す、すみません。\x01",
            "（さすがに大胆すぎたか……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4490")

    Jump("loc_45ED")

    label("loc_4495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4562")
    OP_4B(0x14, 0xFF)
    TurnDirection(0xFE, 0xC, 0)

    #C0191
    ChrTalk(
        0xFE,
        (
            "#0600Fなるほど、状況は判りました。\x02\x03",

            "#0603Fエマ君、この脅迫状は\x01",
            "鑑識にまわせ。\x02\x03",

            "#0601F指紋は無理だろうが\x01",
            "多少の手がかりにはなるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x14,
        "ええ、すぐに分析させます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    OP_4C(0x14, 0xFF)
    Jump("loc_45ED")

    label("loc_4562")


    #C0193
    ChrTalk(
        0xFE,
        (
            "#0600Fお前たち……\x01",
            "もうこの場に用事はないはずだが？\x02\x03",

            "#0603F未練がましい真似はやめて\x01",
            "とっとと失せるんだな。\x01",
            "ここはすでに我々の管轄だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45ED")

    TalkEnd(0xFE)
    Return()

    # Function_22_43E5 end

    def Function_23_45F1(): pass

    label("Function_23_45F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_464F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460F")
    Call(0, 24)
    Jump("loc_464A")

    label("loc_460F")


    #C0194
    ChrTalk(
        0xFE,
        (
            "やはりプレ公演ですね……\x01",
            "すぐに必要書類を用意します。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_464A")

    Jump("loc_4704")

    label("loc_464F")


    #C0195
    ChrTalk(
        0xFE,
        (
            "……我々捜査一課の\x01",
            "邪魔をしないで頂きたいものですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "それとも支援課のメンバーは\x01",
            "でしゃばるのが趣味なのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0001F（な、なんだか\x01",
            "  カチンとくる物言いだなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4704")

    TalkEnd(0xFE)
    Return()

    # Function_23_45F1 end

    def Function_24_4708(): pass

    label("Function_24_4708")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x2D, 0x0)

    #C0198
    ChrTalk(
        0x14,
        "狙撃には最適のポイントですね……\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x13,
        (
            "#0601Fくそっ、大体この劇場は\x01",
            "構造に隙が多すぎるぞ。\x02\x03",

            "#0600F……エマ君、ここは私が守る。\x01",
            "警護プランをＢに変更だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x14,
        (
            "判りました、すぐに\x01",
            "配置シフトを変更します。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_24_4708 end

    def Function_25_47FA(): pass

    label("Function_25_47FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E1")

    #C0201
    ChrTalk(
        0x101,
        (
            "#0005Fあ、あれ、レクターさん……？\x01",
            "こんな所で一体何を……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x15,
        (
            "#3502Fフハハ、決まってるだろ。\x01",
            "劇団アルカンシェルの見物だ！\x02\x03",

            "#3504Fいや～、遅れるかと思って\x01",
            "途中で走っちまったぜ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x104,
        (
            "#0309Fハハ、あるある……\x02\x03",

            "#0307F……って、いやいや！\x01",
            "ここ、貴賓席だろうが！？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        (
            "#0101F普通の人が入れる場所じゃ\x01",
            "ないはずですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x15,
        (
            "#3507Fおう、そこは宰相──ゴホンゴホン。\x02\x03",

            "#3509Fいや～あのオッサンも\x01",
            "たまには使えんじゃ～ん？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x103,
        "#0211F（行動パターンが読めない……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 4)
    Jump("loc_4A6F")

    label("loc_49E1")


    #C0207
    ChrTalk(
        0x15,
        (
            "#3504Fうむ、中々居心地の\x01",
            "よさそうなソファーだな。\x02\x03",

            "#3510F……公演時間まで寝るか！！\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        (
            "#0206F（行動パターンが\x01",
            "  まったく読めない……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A6F")

    TalkEnd(0xFE)
    Return()

    # Function_25_47FA end

    def Function_26_4A73(): pass

    label("Function_26_4A73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A90")
    Call(0, 27)
    Jump("loc_4FAB")

    label("loc_4A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 1)), scpexpr(EXPR_END)), "loc_4B25")

    #C0209
    ChrTalk(
        0xFE,
        (
            "そういやリーシャ、遅いなぁ……\x01",
            "家に忘れ物をしたって言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "仕方ねえ、後でひとっ走り\x01",
            "迎えに行ってくるか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8F")

    label("loc_4B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3E")

    #C0211
    ChrTalk(
        0xFE,
        (
            "台本に調整が入って、\x01",
            "今劇団はチョー忙しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        "あんまウロウロすんなよな。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D36")

    #C0213
    ChrTalk(
        0x101,
        (
            "#0006F悪い、ちょっと\x01",
            "様子が気になってさ……\x02\x03",

            "#0000Fでも公演の方も\x01",
            "何とかなりそうなんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "そ、そりゃあな。\x01",
            "オレもこうやって手伝ってるんだし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    #C0215
    ChrTalk(
        0xFE,
        (
            "こっちは意地でも\x01",
            "成功させてやるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "……その、あんたらは\x01",
            "心配しなくてもいいんだ。\x01",
            "とっとと仕事に戻れよな！\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x104,
        "#0300Fハハ、珍しく頼もしい言葉だな。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0000Fサンキュー、\x01",
            "そうさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "……うん。\x01",
            "そっちも頑張れよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 1)

    label("loc_4D36")

    SetScenarioFlags(0x1, 7)
    Jump("loc_4D8F")

    label("loc_4D3E")


    #C0220
    ChrTalk(
        0xFE,
        "何だよお前ら……\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "今劇団はチョー忙しいんだ。\x01",
            "あんまウロウロすんなよな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D8F")

    Jump("loc_4FAB")

    label("loc_4D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E5E")

    #C0222
    ChrTalk(
        0xFE,
        (
            "あのニコルってやつ、\x01",
            "何だか様子がおかしかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "リーシャに絡んだり\x01",
            "イリアさんにまでガン付けたり……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "ぶん殴ってやろうとしたら\x01",
            "イリアさんに止められたけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_4EDB")

    label("loc_4E5E")


    #C0225
    ChrTalk(
        0xFE,
        (
            "そういえばあいつ、\x01",
            "記念祭の最終日にポカやらかして\x01",
            "すげー落ち込んでたな……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "あの後から\x01",
            "おかしくなった気がするけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EDB")

    Jump("loc_4FAB")

    label("loc_4EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4FAB")

    #C0227
    ChrTalk(
        0xFE,
        "リーシャは優しすぎるんだ。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "あんな奴に言われて\x01",
            "引き下がる事ないのに……\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FA8")

    #C0229
    ChrTalk(
        0x101,
        "#0000F何かあったのか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)

    #C0230
    ChrTalk(
        0xFE,
        (
            "別に……\x01",
            "オレの口から言う事じゃねえし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FA8")

    SetScenarioFlags(0x1, 7)

    label("loc_4FAB")

    TalkEnd(0xFE)
    Return()

    # Function_26_4A73 end

    def Function_27_4FAF(): pass

    label("Function_27_4FAF")


    #C0231
    ChrTalk(
        0x101,
        (
            "#0005Fあれ……？\x01",
            "劇団にこんな子、いたっけな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5022")

    #C0232
    ChrTalk(
        0xFE,
        (
            "……何だお前、\x01",
            "イリアさんの知り合いか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5051")

    label("loc_5022")


    #C0233
    ChrTalk(
        0xFE,
        (
            "……何だお前ら、\x01",
            "イリアさんの知り合いか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5051")


    #C0234
    ChrTalk(
        0xFE,
        (
            "フン……\x01",
            "劇団は一般人立ち入り禁止だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "いくら知り合いだからって\x01",
            "図々しく上がってくんなよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Return()

    # Function_27_4FAF end

    def Function_28_50BB(): pass

    label("Function_28_50BB")

    TalkBegin(0xFE)

    #C0236
    ChrTalk(
        0xFE,
        (
            "確かに隙が多い……\x01",
            "どこからでも舞台を\x01",
            "狙い放題ではないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "クソ……賊も\x01",
            "厄介な事を考えたものだ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_50BB end

    def Function_29_512D(): pass

    label("Function_29_512D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A8")

    #C0238
    ChrTalk(
        0xFE,
        (
            "プレ公演までに\x01",
            "万全の警備体制を敷かねばな……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "イリア・プラティエに何かあっては\x01",
            "自治州政府にとっても大きな痛手。\x01",
            "……政治問題にも発展しかねんぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#0005F（エリィ……そうなのか？）\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#0103F（可能性はあるわね……\x01",
            "  イリアさんは周辺諸国にも\x01",
            "  影響力がある人だもの。）\x02\x03",

            "#0101F（公#2Rおおやけ#になれば、議員たちも\x01",
            "  黙ってはいられないでしょう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_5318")

    label("loc_52A8")


    #C0242
    ChrTalk(
        0xFE,
        (
            "おい、寄せ集めの特務支援課。\x01",
            "お前たちは担当を外れたはずだが？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "部外者はとっとと\x01",
            "立ち去ってもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5318")

    TalkEnd(0xFE)
    Return()

    # Function_29_512D end

    def Function_30_531C(): pass

    label("Function_30_531C")

    TalkBegin(0xFE)

    #C0244
    ChrTalk(
        0xFE,
        (
            "この日のために\x01",
            "はるばる帝国から来たんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "ははは、楽しみじゃな。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_531C end

    def Function_31_5370(): pass

    label("Function_31_5370")

    TalkBegin(0xFE)

    #C0246
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの舞台を\x01",
            "見るのは初めてなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "今回の新作、人気が高いだけに\x01",
            "期待してしまうわね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_5370 end

    def Function_32_53DF(): pass

    label("Function_32_53DF")

    TalkBegin(0xFE)

    #C0248
    ChrTalk(
        0xFE,
        "いよいよアルカンシェルの舞台よっ！\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        "#4S……イリア様～っ！！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_53DF end

    def Function_33_542B(): pass

    label("Function_33_542B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54BF")
    Jump("loc_5509")

    label("loc_54BF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54DF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5509")

    label("loc_54DF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54FF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5509")

    label("loc_54FF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5509")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0250
    ChrTalk(
        0xFE,
        (
            "ふむ、リーシャ・マオという\x01",
            "新人にも興味があるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "大した評判らしいが……\x01",
            "今日の舞台で存分に\x01",
            "見せてもらうとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_542B end

    def Function_34_55B5(): pass

    label("Function_34_55B5")

    TalkBegin(0xFE)

    #C0252
    ChrTalk(
        0xFE,
        "パパぁ、まだ始まらないの？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "ぶー、あたし待ちくたびれちゃった。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_55B5 end

    def Function_35_5604(): pass

    label("Function_35_5604")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5698")
    Jump("loc_56E2")

    label("loc_5698")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56B8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56E2")

    label("loc_56B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56D8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56E2")

    label("loc_56D8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56E2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0254
    ChrTalk(
        0xFE,
        (
            "私は公演初日にも観たのだが、\x01",
            "どうしても興奮が忘れられなくてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "ついついチケットを\x01",
            "買い求めてしまったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_5604 end

    def Function_36_5785(): pass

    label("Function_36_5785")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5819")
    Jump("loc_5863")

    label("loc_5819")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5839")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5863")

    label("loc_5839")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5859")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5863")

    label("loc_5859")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5863")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0256
    ChrTalk(
        0xFE,
        "おほほ……やはりＳ席はいいわね。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "アルカンシェルを堪能するなら\x01",
            "Ｓ席に限るわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_5785 end

    def Function_37_58E7(): pass

    label("Function_37_58E7")

    TalkBegin(0xFE)
    OP_4B(0x21, 0xFF)

    #C0258
    ChrTalk(
        0xFE,
        (
            "おっと、お手洗いを\x01",
            "済ませておかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "悪いけど席、頼むぜ！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x21,
        (
            "はは、何言ってんだ。\x01",
            "ここは予約席だぜ？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x21, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_37_58E7 end

    def Function_38_596A(): pass

    label("Function_38_596A")

    TalkBegin(0xFE)

    #C0261
    ChrTalk(
        0xFE,
        (
            "仕事先からチケットを貰っちまってね、\x01",
            "思いがけず観れることになったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        "いやあ、俺たち超ラッキーだな！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_596A end

    def Function_39_59E0(): pass

    label("Function_39_59E0")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_68(0, 1500, 13250, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -750, 450, 11500, 0)
    SetChrPos(0x102, 250, 450, 11250, 0)
    SetChrPos(0x103, -750, 900, 10000, 0)
    SetChrPos(0x104, 250, 900, 9750, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0x11, 0xE1, 0x0)
    OP_93(0xA, 0x87, 0x0)
    OP_0D()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0263
    ChrTalk(
        0xC,
        (
            "#5Pおお、支援課の諸君……！\x01",
            "丁度良い所に……！\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#0005F劇団長……どうかしたんですか？\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xC,
        "#5Pじ、実は……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "#5Pああ、これは内密に\x01",
            "お願いするんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "#5P朝から、うちのアーティストの\x01",
            "一人が行方不明なんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_END)), "loc_5C72")

    #C0268
    ChrTalk(
        0x9,
        (
            "#1806F#5P前に少しお話した\x01",
            "ニコルさんなんですけど……\x02\x03",

            "#1801F昨日から家の方にも\x01",
            "帰ってないそうなんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CE9")

    label("loc_5C72")


    #C0269
    ChrTalk(
        0x9,
        (
            "#1806F#5Pニコルさんといって、\x01",
            "私と同じ新人の方なんですけど……\x02\x03",

            "#1801F昨日から家の方にも\x01",
            "帰ってないそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CE9")


    #C0270
    ChrTalk(
        0x11,
        (
            "#11P家族の方でも手分けして\x01",
            "探しているらしいんだけど、\x01",
            "見つからないらしいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "#5P私どもの知っている連絡先は\x01",
            "全て当たってみたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x103,
        (
            "#0201F……ニコルさん、最近様子が\x01",
            "おかしかったのではありませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0273
    ChrTalk(
        0xC,
        "#5Pあ、ああ、その通りだ。\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "#5P気が弱くて、ミスの目立つ\x01",
            "新人アーティストだったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "#5P記念祭の後くらいからかな。\x01",
            "急に驚異的な才能を見せ始めたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#0003F………………………………\x02\x03",

            "#0001F才能というのは、具体的には……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "#5P──卓越した身体能力だ。\x01",
            "それに情熱的な演技も\x01",
            "難なくこなすようになった。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#1706F#5Pでもあれって……まるで\x01",
            "憑き物がついたような感じよね。\x02\x03",

            "#1701F絶対ニコルがやるような\x01",
            "演技じゃないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x9,
        (
            "#1806F#5Pええ、それに何だか\x01",
            "熱に浮かされたような雰囲気で……\x02\x03",

            "#1808Fまるで別人みたいでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        "#0303F……決まり……だな。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        (
            "#0108Fしかも失踪済み……\x01",
            "良くない状況ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        (
            "#0003F劇団長、ニコルさんの事は\x01",
            "支援課に任せて頂けないでしょうか。\x02\x03",

            "#0001Fもしかすると、自分たちの方で\x01",
            "探し出せるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        "#5P本当かね……？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "#5Pもしそうなら願ってもない。\x01",
            "是非頼みたい所だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#1702F#5Pそうね、弟君たちが\x01",
            "担当してくれるなら安心かも。\x02\x03",

            "#1706Fそれにあたしたちも、公演の段取りを\x01",
            "付けないといけないしね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(12)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(13)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0286
    ChrTalk(
        0x104,
        (
            "#0305F今日の公演……\x01",
            "まさかやるつもりなんスか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x11,
        (
            "#11Pええ、それも\x01",
            "話し合っていた所なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x11,
        (
            "#11Pニコル君が戻らなくても\x01",
            "舞台をやめるわけにはいかないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x11,
        (
            "#11P何とか役をやりくりして\x01",
            "上演するつもりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xA,
        (
            "#5P劇団アルカンシェルが\x01",
            "舞台を降りる事などありえませんからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xC,
        (
            "#5Pああ、役や台本、演出も\x01",
            "調整しなければならないだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        (
            "公演時間を遅らせるという手もある。\x01",
            "何とかして実現するつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x103,
        (
            "#0202F驚きました……\x01",
            "何というか、さすがの執念ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x102,
        (
            "#0109Fそ、そうね……\x01",
            "さすがアルカンシェルとしか\x01",
            "言えないかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#0004F……分かりました。\x01",
            "皆さんは公演の方をお願いします。\x02\x03",

            "#0001Fただし、楽屋や客席に\x01",
            "ニコルさんが戻っていないか\x01",
            "常に注意しておいてください。\x02\x03",

            "もし見つけた場合は\x01",
            "すぐに支援課の方に連絡を。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xC,
        "#5P分かった、そうしよう。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        (
            "#1808F#5P……すみません、私がもっと\x01",
            "注意していればこんな事には……\x02\x03",

            "#1801Fニコルさんのこと、\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#0000Fああ、任せてくれ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6624")
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0299
    ChrTalk(
        0x102,
        "#0101F……ロイド、先を急いだ方がいいわ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0300
    ChrTalk(
        0x101,
        (
            "#0001F#6Pそうだな、なるべく速やかに\x01",
            "残りの市民の確認を取ろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6624")

    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 0, 450, 11500, 360)
    OP_93(0x8, 0xE1, 0x0)
    OP_93(0x9, 0x168, 0x0)
    OP_93(0x11, 0x10E, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0xC8, 0)
    OP_29(0x4C, 0x1, 0x7)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0x11, 0xFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_39_59E0 end

    def Function_40_6688(): pass

    label("Function_40_6688")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_40_6688 end

    def Function_41_66B5(): pass

    label("Function_41_66B5")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_41_66B5 end

    def Function_42_66E2(): pass

    label("Function_42_66E2")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_66E2 end

    def Function_43_66F9(): pass

    label("Function_43_66F9")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_43_66F9 end

    def Function_44_6710(): pass

    label("Function_44_6710")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_6710 end

    def Function_45_6719(): pass

    label("Function_45_6719")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_45_6719 end

    def Function_46_6722(): pass

    label("Function_46_6722")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_46_6722 end

    def Function_47_672B(): pass

    label("Function_47_672B")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_47_672B end

    def Function_48_6734(): pass

    label("Function_48_6734")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_48_6734 end

    def Function_49_6761(): pass

    label("Function_49_6761")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_49_6761 end

    def Function_50_678E(): pass

    label("Function_50_678E")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_678E end

    def Function_51_67A5(): pass

    label("Function_51_67A5")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_51_67A5 end

    def Function_52_67BC(): pass

    label("Function_52_67BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67DA")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_52_67BC")

    label("loc_67DA")

    Return()

    # Function_52_67BC end

    def Function_53_67DB(): pass

    label("Function_53_67DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67F9")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_53_67DB")

    label("loc_67F9")

    Return()

    # Function_53_67DB end

    def Function_54_67FA(): pass

    label("Function_54_67FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6818")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_54_67FA")

    label("loc_6818")

    Return()

    # Function_54_67FA end

    def Function_55_6819(): pass

    label("Function_55_6819")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6837")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_55_6819")

    label("loc_6837")

    Return()

    # Function_55_6819 end

    def Function_56_6838(): pass

    label("Function_56_6838")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0x57E40, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_56_6838 end

    def Function_57_6871(): pass

    label("Function_57_6871")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0xFFFA81C0, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_57_6871 end

    def Function_58_68AA(): pass

    label("Function_58_68AA")

    Sleep(1500)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_95(0x9, -2110, 1250, 20950, 4500, 0x0)
    BeginChrThread(0x9, 2, 0, 41)

    def lambda_68DE():
        OP_9E(0x9, 0x0, 0x5AB4, 0xFFFEA070, 0x898, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_68DE)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    Sleep(1)
    Sound(820, 0, 100, 0)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x578, 0x2BC)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    Sound(50, 0, 100, 0)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 43)
    BeginChrThread(0x9, 3, 0, 54)
    Sound(820, 0, 100, 0)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x2BC)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1F)
    Sound(50, 0, 100, 0)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)

    def lambda_697F():
        OP_93(0x9, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_697F)
    BeginChrThread(0x9, 2, 0, 41)
    OP_9D(0x9, 0xFFFFF9FC, 0x4E2, 0x5E38, 0xBB8, 0x4B0)
    SetChrChipByIndex(0x9, 0x21)
    Sound(50, 0, 100, 0)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    BeginChrThread(0x9, 2, 0, 41)

    def lambda_69C5():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_69C5)
    OP_9D(0x9, 0xFFFFF3C6, 0x4E2, 0x62F2, 0x3E8, 0x6A4)
    SetChrChipByIndex(0x9, 0x21)
    Sound(50, 0, 100, 0)
    SetChrSubChip(0x9, 0x2)
    Sleep(1500)

    def lambda_69FA():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_69FA)
    BeginChrThread(0x9, 2, 0, 41)
    OP_9D(0x9, 0xFFFFFA74, 0x4E2, 0x6496, 0x7D0, 0xA28)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x9, 2, 0, 43)
    BeginChrThread(0x9, 3, 0, 54)
    OP_9D(0x9, 0x58C, 0x4E2, 0x6496, 0x7D0, 0xA28)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x9, 2, 0, 44)
    BeginChrThread(0x9, 3, 0, 54)
    OP_9D(0x9, 0xF28, 0x4E2, 0x6496, 0x7D0, 0xA28)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    Sound(50, 0, 100, 0)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_9E(0x9, 0xF28, 0x55F0, 0xFFFEA070, 0xBB8, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 55)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 43)
    BeginChrThread(0x9, 3, 0, 54)
    Sleep(1800)
    EndChrThread(0x9, 0x3)
    Sound(820, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_58_68AA end

    def Function_59_6AE0(): pass

    label("Function_59_6AE0")

    OP_95(0xFE, -5500, 1250, 24300, 3000, 0x0)
    OP_95(0xFE, -10500, 1250, 25300, 3000, 0x0)
    Return()

    # Function_59_6AE0 end

    def Function_60_6B09(): pass

    label("Function_60_6B09")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0xC, 0xFF)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x14, 0x1E, 0x0)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0x1A, "02back", 0x0, 0x1)
    SetMapObjFrame(0x1A, "02moon_add", 0x0, 0x1)
    SetMapObjFrame(0x1A, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x1A, "02water02_add", 0x0, 0x1)
    SetMapObjFrame(0x1A, "main02", 0x0, 0x1)
    LoadChrToIndex("apl/ch50265.itc", 0x1E)
    LoadChrToIndex("apl/ch50266.itc", 0x1F)
    LoadChrToIndex("apl/ch50267.itc", 0x20)
    LoadChrToIndex("apl/ch50268.itc", 0x21)
    LoadChrToIndex("apl/ch50269.itc", 0x22)
    LoadChrToIndex("apl/ch50270.itc", 0x23)
    LoadChrToIndex("chr/ch09800.itc", 0x24)
    LoadChrToIndex("apl/ch50200.itc", 0x28)
    LoadChrToIndex("apl/ch50201.itc", 0x29)
    LoadChrToIndex("apl/ch50202.itc", 0x2A)
    LoadChrToIndex("apl/ch50549.itc", 0x2B)
    EndChrThread(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, 0, 1250, 23220, 225)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06200.itp")
    OP_68(-70, 2500, 24310, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20500, 0)
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x2, 0x0, 0x0, 0x1388, 0x0)
    OP_C9(0x2, 0x1, 0x3E8, 0x44C, 0x0)
    OP_E5()
    PlayBGM("ed7501", 1)
    Sleep(1000)
    FadeToBright(8000, 0)
    OP_6E(620, 25000)
    Sleep(5700)
    OP_C9(0x2, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x2328)
    OP_C9(0x2, 0x1, 0xBB8, 0xBB8, 0x2328)
    Sleep(900)
    BeginChrThread(0x101, 3, 0, 58)
    WaitChrThread(0x101, 3)
    StopBGM(0x1770)
    Sleep(3000)
    Fade(500)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    Sleep(300)
    OP_E6()
    #Sound(1632, 255, 80, 0)    #voice#Rixia

    #N0301
    NpcTalk(
        0x9,
        "紫髪の娘",
        "#6206F#5P#100Wはあっ、はあっ、はあっ……\x02",
    )

    CloseMessageWindow()
    OP_11(0x0, 0x0, 0x0, 0x32, 0xC8, 0x3E8)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)
    SetChrName("紫髪の娘")

    #A0302
    AnonymousTalk(
        0xFF,
        "#30Wよかった、何とかここまでは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -9000, 1250, 24230, 270)

    #N0303
    NpcTalk(
        0x8,
        "女性の声",
        "#2Pうんうん、いいわね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(1635, 255, 100, 0)    #voice#Rixia
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7513", 0)
    TurnDirection(0x9, 0x8, 300)
    Fade(1000)
    OP_68(-6200, 3200, 23140, 0)
    MoveCamera(336, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(-1330, 2500, 22900, 5000)
    OP_95(0x8, -1730, 1250, 23430, 2000, 0x0)
    TurnDirection(0x8, 0x9, 500)
    OP_6F(0x1)

    #N0304
    NpcTalk(
        0x9,
        "紫髪の娘",
        "#6205F#30Wイ、イリアさん……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("金髪の女性")

    #A0305
    AnonymousTalk(
        0xFF,
        (
            "スピードとタイミングは良いわ。\x02\x03",

            "後は節目節目で抑揚を付けること。\x02\x03",

            "音楽に乗るんじゃなくて\x01",
            "踊りと演技で音楽を支配なさい。\x02\x03",

            "あくまで静かに、清らかに……\x01",
            "《月の姫》ならではの威厳をもって。\x02",
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

    #N0306
    NpcTalk(
        0x9,
        "紫髪の娘",
        (
            "#6202F#30Wは、はい……\x02\x03",

            "#6208F#50W……ぁ………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_68(-1330, 2400, 22900, 800)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(1300)

    #N0307
    NpcTalk(
        0x8,
        "金髪の女性",
        (
            "#1706Fだらしがないわねぇ……\x01",
            "と言いたいところだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(170, 3020, 21070, 2000)
    SetCameraDistance(16500, 2000)
    SetChrFlags(0x8, 0x8000)
    OP_95(0x8, -750, 1250, 22350, 1000, 0x0)
    TurnDirection(0x8, 0x9, 500)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #N0308
    NpcTalk(
        0x8,
        "金髪の女性",
        (
            "#1702F#5P正直、驚いてるわ。\x02\x03",

            "今まで誰一人、あたしの稽古に\x01",
            "付いて来られる人間はいなかったから。\x02\x03",

            "#1709Fうんうん、よく頑張っているじゃない♪\x02",
        )
    )

    CloseMessageWindow()

    #N0309
    NpcTalk(
        0x9,
        "紫髪の娘",
        (
            "#6202F#2Pイリア、さん……\x02\x03",

            "#6203Fでも私……やっぱり不安で。\x02\x03",

            "本番でイリアさんの足を\x01",
            "引っ張ったらどうしようって……\x02",
        )
    )

    CloseMessageWindow()

    #N0310
    NpcTalk(
        0x8,
        "金髪の女性",
        (
            "#1704F#5P大丈夫、あんたには素質があるわ。\x02\x03",

            "#1702Fそれこそ将来あたしを、\x01",
            "このイリア・プラティエを\x01",
            "超えられる可能性を持っている。\x02\x03",

            "#1709Fあたしの目を信じなさいってーの！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0311
    NpcTalk(
        0x9,
        "紫髪の娘",
        (
            "#6209F#2P……な、なんだか全然、\x01",
            "実感が湧かないっていうか……\x02\x03",

            "#6202Fイリアさんを超えるなんて\x01",
            "そんなの無理に決まってますよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0312
    NpcTalk(
        0x8,
        "金髪の女性",
        (
            "#1702F#5Pフフン、まああたしも\x01",
            "簡単には抜かれるつもりはないし。\x02\x03",

            "#1704Fだから一刻も早く\x01",
            "あたしのいる所まで上がってきなさい。\x02\x03",

            "#1701Fあたしと本気でやり合える\x01",
            "ライバルの卵くらいにはなりなさい！\x02",
        )
    )

    CloseMessageWindow()

    #N0313
    NpcTalk(
        0x9,
        "紫髪の娘",
        (
            "#6203F#2Pはあ……\x01",
            "無茶言わないでくださいよ……\x02\x03",

            "#6208Fああ、どうして私、\x01",
            "こんな所にいるのかしら……\x02\x03",

            "今ごろ、クロスベルを出て\x01",
            "故郷に帰っているハズなのに……\x02",
        )
    )

    CloseMessageWindow()

    #N0314
    NpcTalk(
        0x8,
        "金髪の女性",
        (
            "#1709F#5Pフッフッフッ……\x02\x03",

            "あたしの稽古を見学に来て\x01",
            "捕まったのが運の尽きだったわね。\x02\x03",

            "もう絶対に逃がさないわよ～？\x02",
        )
    )

    CloseMessageWindow()

    #N0315
    NpcTalk(
        0x9,
        "紫髪の娘",
        "#6206F#2Pううう、おかあさ～ん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0316
    NpcTalk(
        0x8,
        "金髪の女性",
        "#1700F#5Pあら、本当にバテちゃった？\x02",
    )

    CloseMessageWindow()

    #N0317
    NpcTalk(
        0x9,
        "紫髪の娘",
        (
            "#6202F#2Pいえ……大丈夫です。\x02\x03",

            "#6203Fそうじゃなくて、その……\x02\x03",

            "#6208F自分の実力不足も不安ですけど\x01",
            "それとは別に、あの手紙が……\x02",
        )
    )

    CloseMessageWindow()

    #N0318
    NpcTalk(
        0x8,
        "金髪の女性",
        (
            "#1705F#5P手紙……？\x02\x03",

            "なんだっけ、それ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0319
    NpcTalk(
        0x9,
        "紫髪の娘",
        (
            "#6201F#2Pイ、イリアさんに送られて来た\x01",
            "あの手紙のことですよ～！\x02\x03",

            "《銀》とかいう人からの……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0320
    NpcTalk(
        0x8,
        "金髪の女性",
        (
            "#1705F#5Pああ、あれ？\x02\x03",

            "#1704Fバカバカしい。\x01",
            "ただのイタズラでしょ？\x02\x03",

            "#1702Fそんなの一々気にしてたら\x01",
            "スターなんてやってらんないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0321
    NpcTalk(
        0x9,
        "紫髪の娘",
        "#6208F#2Pで、でも……\x02",
    )

    CloseMessageWindow()

    #N0322
    NpcTalk(
        0x8,
        "金髪の女性",
        (
            "#1702F#5Pあんたも今度の公演でデビューしたら\x01",
            "山ほどファンレターを貰うはずよ。\x02\x03",

            "中には変なのだってあるから\x01",
            "適当に流していかないと。\x02\x03",

            "#1709F特にあんたの場合は、その胸で\x01",
            "男どもを釘付けにしそうだしね～。\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(350, 20, 0, 1000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_96(0x8, 0xFFFFFE02, 0x4B0, 0x5528, 0x320, 0x0)
    Fade(250)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x8, 0x1)
    Sound(858, 0, 100, 0)
    Sleep(250)
    SetChrSubChip(0x8, 0x0)
    Sleep(250)
    SetChrSubChip(0x8, 0x1)
    Sound(858, 0, 100, 0)
    Sleep(250)
    SetChrSubChip(0x8, 0x0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(800)
    Sound(1633, 255, 100, 0)    #voice#Rixia
    Fade(250)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #N0323
    NpcTalk(
        0x9,
        "紫髪の娘",
        (
            "#6201F#2Pも、もう……！\x01",
            "イリアさんったら……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)

    #C0324
    ChrTalk(
        0x8,
        (
            "#1705Fハアハア……\x01",
            "何か興奮してきたわね。\x02\x03",

            "#1702Fちょっとだけでいいから\x01",
            "揉みしだかせてくれない？\x02\x03",

            "#1709F大丈夫、痛くしないから～！\x02",
        )
    )

    CloseMessageWindow()

    #N0325
    NpcTalk(
        0x9,
        "紫髪の娘",
        "#6206F#2Pあーん、女神さま～……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, -9000, 1250, 24230, 270)

    #N0326
    NpcTalk(
        0xC,
        "男性の声",
        "#2Pえー、ゴホンゴホン！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xC, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-530, 3200, 22200, 3000)
    MoveCamera(340, 24, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(18000, 3000)

    def lambda_7BAF():
        OP_95(0xFE, -1310, 1250, 24690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7BAF)
    Sleep(300)
    Fade(250)

    def lambda_7BD1():

        label("loc_7BD1")

        TurnDirection(0xFE, 0xC, 300)
        Yield()
        Jump("loc_7BD1")

    QueueWorkItem2(0x8, 0, lambda_7BD1)

    def lambda_7BE3():

        label("loc_7BE3")

        TurnDirection(0xFE, 0xC, 300)
        Yield()
        Jump("loc_7BE3")

    QueueWorkItem2(0x9, 0, lambda_7BE3)
    SetChrChipByIndex(0x8, 0x0)
    Sleep(1000)

    def lambda_7BFC():
        OP_96(0xFE, 0xFFFFFC18, 0x4E2, 0x5640, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7BFC)
    WaitChrThread(0xC, 1)
    TurnDirection(0xC, 0x8, 500)
    Fade(500)
    SetChrChipByIndex(0x9, 0x24)
    OP_0D()

    #N0327
    NpcTalk(
        0x9,
        "紫髪の娘",
        "#6205F#12Pげ、劇団長さん……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x8,
        "#1705F#6Pあら、いたの？\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xC,
        "ハア、いたのは無いだろう。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "遅くまでご苦労さんだが……\x01",
            "少々、稽古というには\x01",
            "不適切な言動が多くはないかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        "#1709F#6P演技指導よ、演技指導。\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    TurnDirection(0x8, 0x9, 500)

    #C0332
    ChrTalk(
        0x8,
        (
            "#1700F#5P──それより、リーシャ。\x01",
            "今日はもう遅いから\x01",
            "あたしのメゾンに泊まんなさい。\x02\x03",

            "こんな時間に、あんな危ない所に\x01",
            "あんたを帰すわけにはいかないわ。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x0)
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    #C0333
    ChrTalk(
        0x9,
        (
            "#6205Fべ、別にそんなに\x01",
            "危険って所じゃないですよ？\x02\x03",

            "#6209F皆さん良い人ばかりで……\x01",
            "越してきたばかりの私にも\x01",
            "親身になってくれますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#1701F#5Pそれが下心だっつーの。\x02\x03",

            "#1706F血の気の多い小僧どもが\x01",
            "ただでさえ多い地区なのに……\x02\x03",

            "夜、この魅惑のボディを見たら\x01",
            "我慢できなくなる可能性はあるわ。\x02\x03",

            "#1701Fううん、問答無用で襲うわね！\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        "それは君だけだろう。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xC,
        (
            "……ところでイリア君。\x01",
            "君に通信が来ているんだが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0xC, 500)

    #C0337
    ChrTalk(
        0x8,
        (
            "#1705F#6Pあら……\x01",
            "ひょっとして彼女から？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xC,
        "ああ、どうする？\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        "#1709F#6Pもちろん出るわ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)

    #C0340
    ChrTalk(
        0x8,
        "#1702F#5Pゴメン、少し外すわね。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x9,
        "#6202Fあ、はい。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    OP_68(-1480, 3200, 22170, 2000)

    def lambda_8038():

        label("loc_8038")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_8038")

    QueueWorkItem2(0xC, 0, lambda_8038)

    def lambda_804A():

        label("loc_804A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_804A")

    QueueWorkItem2(0x9, 0, lambda_804A)
    BeginChrThread(0x8, 0, 0, 59)
    Sleep(500)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    Sleep(1000)

    #C0342
    ChrTalk(
        0xC,
        (
            "#11Pはあ……\x01",
            "いつもと全く変わらないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xC,
        (
            "#11P少しはあの手紙に\x01",
            "動揺してるかと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x9,
        (
            "#6202F#11Pふふ……\x01",
            "それがイリアさんですから。\x02\x03",

            "#6204Fどんな時にも金色の太陽みたいに\x01",
            "目の眩むような光を放っている人……\x02\x03",

            "#6208F──でも、それなら尚更、\x01",
            "他の人が気をつけていないと……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_60_6B09 end

    def Function_61_81C0(): pass

    label("Function_61_81C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_820A")
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_61_81C0")

    label("loc_820A")

    Return()

    # Function_61_81C0 end

    def Function_62_820B(): pass

    label("Function_62_820B")

    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 1, 0, 61)
    SetChrFlags(0x8, 0x4)
    BeginChrThread(0x8, 2, 0, 40)
    Sound(814, 0, 80, 0)
    Sleep(100)
    OP_9D(0x8, 0xA, 0x4E2, 0x636A, 0xFA0, 0x3E8)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 43)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 53)

    def lambda_8271():
        OP_9E(0x8, 0x0, 0x5DC0, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8271)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)

    def lambda_82BF():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_82BF)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x0)

    def lambda_8304():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_8304)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)

    def lambda_831A():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_831A)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    Sound(854, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x0)

    def lambda_835F():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_835F)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 52)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)

    def lambda_83A7():
        OP_9E(0x8, 0x0, 0x636A, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_83A7)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    Sound(854, 0, 80, 0)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 52)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)

    def lambda_8422():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_8422)
    BeginChrThread(0x8, 2, 0, 41)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0x7D0, 0x7D0)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x8, 3, 0, 52)
    BeginChrThread(0x8, 2, 0, 43)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0xBB8, 0x9C4)
    Sound(50, 0, 100, 0)
    Sound(51, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    OP_82(0x0, 0x64, 0x5DC, 0x96)
    EndChrThread(0x8, 0x1)
    Sleep(1000)
    Return()

    # Function_62_820B end

    def Function_63_84BE(): pass

    label("Function_63_84BE")

    OP_95(0x9, 1300, 0, 15400, 1000, 0x0)

    def lambda_84D7():

        label("loc_84D7")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_84D7")

    QueueWorkItem2(0x9, 0, lambda_84D7)
    Return()

    # Function_63_84BE end

    def Function_64_84E5(): pass

    label("Function_64_84E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0xC, 0xFF)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFrame(0x19, "01back", 0x0, 0x1)
    LoadEffect(0x0, "event\\ev290_01.eff")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x2, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x2, 0x1, 0xBB8, 0xBB8, 0x0)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("chr/ch09700.itc", 0x24)
    LoadChrToIndex("apl/ch50207.itc", 0x28)
    SetChrPos(0x8, 10, 1250, 25450, 225)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06100.itp")
    SetChrPos(0x101, 650, 2700, -1530, 0)
    SetChrPos(0x102, -520, 2700, -1410, 0)
    SetChrPos(0x104, 570, 2700, -2900, 0)
    SetChrPos(0x103, -600, 2700, -2900, 0)

    def lambda_863F():
        OP_95(0xFE, 650, 2700, 530, 1400, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_863F)

    def lambda_8659():
        OP_95(0xFE, -520, 2700, 410, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8659)

    def lambda_8673():
        OP_95(0xFE, 570, 2700, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8673)

    def lambda_868D():
        OP_95(0xFE, -600, 2700, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_868D)
    SetChrPos(0xC, -3230, 0, 13720, 0)
    SetChrPos(0x9, 2160, 0, 13710, 0)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x9, 0xFF)
    OP_68(650, 4000, 530, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(730, 0)
    SetCameraDistance(14000, 0)
    VolumeBGM(0x64, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)

    #C0345
    ChrTalk(
        0x101,
        "#0005F#11P（え……）\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x103,
        "#0205F#11P（こ、これは……）\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        "#0105F#11P（……すごい………）\x02",
    )

    CloseMessageWindow()
    OP_68(650, 4000, 2530, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-70, 4000, 24310, 0)
    MoveCamera(0, -5, -5, 0)
    OP_6E(900, 0)
    SetCameraDistance(13000, 0)
    OP_68(510, 3200, 24660, 17000)
    MoveCamera(312, 21, -10, 17000)
    OP_6E(800, 17000)
    SetCameraDistance(11000, 17000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 3, 0, 62)
    WaitChrThread(0x101, 3)
    SetChrPos(0x101, -650, 700, 10950, 0)
    SetChrPos(0x102, 490, 900, 10470, 0)
    SetChrPos(0x103, -600, 1350, 8220, 0)
    SetChrPos(0x104, 500, 1350, 8220, 0)
    StopBGM(0xFA0)
    Sleep(1500)
    Sound(853, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x9, 1, 0, 63)

    def lambda_8861():

        label("loc_8861")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_8861")

    QueueWorkItem2(0xC, 0, lambda_8861)

    def lambda_8873():
        OP_96(0xFE, 0xFFFFF632, 0x0, 0x3714, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8873)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0348
    ChrTalk(
        0x8,
        "#6105Fあら……？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)

    def lambda_88D0():
        OP_95(0xFE, 0, 1250, 18500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_88D0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_68(60, 1500, 15290, 0)
    MoveCamera(63, 24, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(16000, 0)

    def lambda_8927():

        label("loc_8927")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_8927")

    QueueWorkItem2(0x101, 0, lambda_8927)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_894A():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_894A)
    Sleep(100)

    def lambda_8962():
        OP_9B(0x1, 0xFE, 0x0, 0xD48, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8962)
    Sleep(50)

    def lambda_897A():
        OP_9B(0x1, 0xFE, 0x0, 0xF3C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_897A)
    Sleep(80)

    def lambda_8992():
        OP_9B(0x1, 0xFE, 0x0, 0xED8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8992)
    Sleep(1000)

    #C0349
    ChrTalk(
        0x9,
        "#1809F#5Pあ、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        (
            "#0006Fす、すみません。\x01",
            "お邪魔してしまって……\x02\x03",

            "#0002Fその……\x01",
            "な、何て言ったらいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        (
            "#0206F……あ、あの………\x02\x03",

            "#0201Fす、すごかったです……！\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        (
            "#0302Fはは……\x01",
            "ちょっと魂抜かれかけたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x102,
        (
            "#0104F……素晴らしいものを\x01",
            "見せていただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x8,
        "#6109Fふふ、ありがと。\x02",
    )

    CloseMessageWindow()
    OP_68(-730, 1650, 13990, 2000)
    MoveCamera(47, 29, 0, 2000)
    OP_6E(730, 2000)
    SetCameraDistance(11500, 2000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sound(814, 0, 60, 0)

    def lambda_8B1F():
        OP_9D(0xFE, 0x0, 0x0, 0x3E80, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8B1F)
    Sleep(450)
    SetChrSubChip(0x8, 0x3)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sound(43, 0, 100, 0)
    OP_95(0x8, 0, 0, 15800, 1500, 0x0)
    OP_6F(0x1)

    #C0355
    ChrTalk(
        0x8,
        (
            "#6106F#5Pま、完成というには\x01",
            "まだ程遠い状態なんだけどね。\x02",
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

    #C0356
    ChrTalk(
        0x101,
        "#0011F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        "#0205F#12Pま、まだ上があるんですか……？\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#6100F#5Pあったりまえじゃない。\x02\x03",

            "#6104Fこのシーンはあくまで冒頭の\x01",
            "《太陽の姫》だけのシーン。\x02\x03",

            "これに《月の姫》が加わることで\x01",
            "何倍にも相乗効果が生まれる……\x02\x03",

            "#6102F最後のクライマックスシーンは\x01",
            "今の数十倍は凄いと思うわよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        "#0013F#6Pごくっ……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x104,
        "#0301F#12Pす、凄いッスね……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x102,
        "#0106F#12Pそ、想像すらできません……\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#6104F#5Pふふっ……\x02\x03",

            "#6100F──リーシャ。\x01",
            "彼らがさっき言ってた？\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x0)
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    #C0363
    ChrTalk(
        0x9,
        (
            "#1802F#11Pはい。\x01",
            "特務支援課の方々です。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x8,
        (
            "#6100F#5Pふーん、確かに全然、\x01",
            "警察っぽくは見えないけど。\x02\x03",

            "#6106Fでもねぇ。\x01",
            "事情聴取とかするんでしょ？\x02\x03",

            "たかがイタズラごときに\x01",
            "そこまで付き合いたくないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xC,
        "#6Pまあまあ、イリア君。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xC,
        (
            "#6Pみんな心配してるんだ。\x01",
            "少しくらいいいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#6103F#5Pんー、そう言われても。\x02\x03",

            "公演前にテンション下がることは\x01",
            "一切しないのがスタイルだし～。\x02\x03",

            "#6102Fリーシャが胸を揉ませてくれたら\x01",
            "少しは考えるかもしれないけど～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0368
    ChrTalk(
        0x9,
        "#1801F#11Pも、揉ませませんっ。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xC,
        "#6Pはあ、まったく君ときたら……\x02",
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

    #C0370
    ChrTalk(
        0x101,
        (
            "#0012F#6P（な、なんか\x01",
            "  舞台の上とのギャップが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        "#0211F#12P（微妙にオジサンっぽいです……）\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#0106F#12P（うーん……\x01",
            "  女傑らしいのは知ってたけど。）\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x104,
        "#0302F#12P（いや～、強烈な人だよなぁ。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    #C0374
    ChrTalk(
        0x9,
        (
            "#1806F#5Pす、すみません皆さん。\x02\x03",

            "#1801F何とか説得してみますから\x01",
            "ロイドさん達は控え室にでも……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_91E3():

        label("loc_91E3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_91E3")

    QueueWorkItem2(0x8, 0, lambda_91E3)

    #C0375
    ChrTalk(
        0x8,
        "#6105F#5Pあら……？\x02",
    )

    CloseMessageWindow()
    OP_68(-1030, 1650, 13570, 1300)
    OP_96(0x8, 0xFFFFFE5C, 0x0, 0x39D0, 0x5DC, 0x0)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0376
    ChrTalk(
        0x101,
        "#0005F#6Pえっ……\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x9,
        "#1805F#5Pイリアさん……？\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x8,
        (
            "#6101F#5Pロイドって──\x01",
            "今、そう言ってたわね。\x02\x03",

            "ひょっとしてあなたのこと？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#0011F#6Pえ、ええ……まあ。\x01",
            "（近い、近すぎるって……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        "#6100F#5Pフルネームは？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#0000F#6Pその……\x01",
            "ロイド・バニングスですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x8, 0x40)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0382
    ChrTalk(
        0x8,
        "#6109F#5P#4Sあはは、やっぱり！\x02",
    )

    CloseMessageWindow()
    OP_9A(0x8, 0x101, 0x190, 0x708, 0x0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    Sound(804, 0, 100, 0)
    Sound(864, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-440, 1450, 14120, 0)
    MoveCamera(123, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12500, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x9, 0xC, 0)
    OP_0D()

    #C0383
    ChrTalk(
        0x101,
        "#0011F#11P！！！？？？\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x103,
        "#0205F#11P……！？\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x102,
        "#0105Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        "#0301F#11Pおいおいおいおい……！\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x9,
        "#1801F#5Pイ、イリアさん……！？\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xC,
        "#12Pな、何をしてるのかね！？\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x8,
        (
            "#6109Fいや～、世間は狭いわねぇ！\x02\x03",

            "まさか噂の弟君と\x01",
            "こうして会えるなんて！\x02\x03",

            "#6102Fそう言えば、警察に入ったって\x01",
            "聞いたことがあったっけ……\x02\x03",

            "ふふ、聞いていたイメージと\x01",
            "ホントそっくりじゃないの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        (
            "#0011F#11Pあ、あの……ひょっとして。\x02\x03",

            "イリアさん……\x01",
            "セシル姉の知り合いだったり？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "#6104Fセシルはあたしの親友よ。\x02\x03",

            "日曜学校以来だから\x01",
            "もう１０年以上になるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        "#0012F#11Pな、なるほど……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-780, 1650, 13530, 0)
    MoveCamera(47, 29, 0, 0)
    OP_6E(730, 0)
    SetCameraDistance(11500, 0)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    OP_96(0x8, 0xFFFFFD1C, 0x0, 0x3B9C, 0x3E8, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0393
    AnonymousTalk(
        0x8,
        (
            "ふふ……\x01",
            "改めて自己紹介するわね。\x02\x03",

            "イリア・プラティエ──\x01",
            "劇団アルカンシェルの看板を\x01",
            "背負#4Rしょ#って立たせてもらってるわ。\x02\x03",

            "よろしくね、弟君たち！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(12000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x87, 3)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_64_84E5 end

    def Function_65_9892(): pass

    label("Function_65_9892")

    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 0, 0, 61)
    BeginChrThread(0x9, 2, 0, 49)

    def lambda_98AD():
        OP_9D(0x9, 0xFA, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_98AD)
    Sleep(200)
    BeginChrThread(0x9, 2, 0, 51)
    BeginChrThread(0x9, 3, 0, 54)
    WaitChrThread(0x9, 1)
    OP_9D(0x9, 0x726, 0x4E2, 0x5C58, 0x1F4, 0x5DC)
    EndChrThread(0x9, 0x3)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    OP_9E(0x9, 0x0, 0x5DC0, 0x20F58, 0x1770, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)

    def lambda_9925():
        OP_9E(0x9, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9925)
    Sleep(33)

    def lambda_9943():

        label("loc_9943")

        TurnDirection(0x9, 0x8, 0)
        Yield()
        Jump("loc_9943")

    QueueWorkItem2(0x9, 3, lambda_9943)
    BeginChrThread(0x9, 2, 0, 49)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x9, 2, 0, 49)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x9, 3, 0, 54)
    BeginChrThread(0x9, 2, 0, 51)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xBB8, 0x3E8)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    OP_9E(0x9, 0x0, 0x5DC0, 0x50910, 0x1388, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 48)

    def lambda_99ED():

        label("loc_99ED")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_99ED")

    QueueWorkItem2(0x9, 3, lambda_99ED)
    OP_9D(0x9, 0xFFFFEFF2, 0x4E2, 0x5DDE, 0xBB8, 0x3E8)
    EndChrThread(0x9, 0x3)
    EndChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    SetChrSubChip(0x9, 0x1)
    Sleep(150)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)
    Sleep(900)
    SetChrChipByIndex(0x9, 0x29)
    OP_95(0x9, -1420, 1250, 24000, 6000, 0x0)
    BeginChrThread(0x9, 2, 0, 47)
    BeginChrThread(0x9, 3, 0, 54)
    BeginChrThread(0x9, 0, 0, 61)
    OP_9D(0x9, 0x384, 0x4E2, 0x5BC2, 0x7D0, 0xDAC)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 57)

    def lambda_9A8C():
        OP_9D(0x9, 0xF28, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9A8C)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 51)
    BeginChrThread(0x9, 3, 0, 54)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x0)

    def lambda_9AC0():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_9AC0)
    Return()

    # Function_65_9892 end

    def Function_66_9AC9(): pass

    label("Function_66_9AC9")

    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 0, 0, 61)
    BeginChrThread(0x8, 2, 0, 41)

    def lambda_9AE4():
        OP_9D(0x8, 0xFFFFFF06, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9AE4)
    Sleep(200)
    BeginChrThread(0x8, 2, 0, 43)
    BeginChrThread(0x8, 3, 0, 52)
    WaitChrThread(0x8, 1)
    OP_9D(0x8, 0xFFFFF8DA, 0x4E2, 0x5C58, 0x1F4, 0x5DC)
    EndChrThread(0x8, 0x3)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_9E(0x8, 0x0, 0x5DC0, 0x20F58, 0x1770, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 3, 0, 52)

    def lambda_9B62():
        OP_9E(0x8, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9B62)
    Sleep(33)

    def lambda_9B80():

        label("loc_9B80")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_9B80")

    QueueWorkItem2(0x8, 3, lambda_9B80)
    BeginChrThread(0x8, 2, 0, 41)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 2, 0, 41)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 3, 0, 52)
    BeginChrThread(0x8, 2, 0, 43)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xBB8, 0x3E8)
    CancelBlur(0)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    OP_9E(0x8, 0x0, 0x5DC0, 0x50910, 0x1388, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 40)

    def lambda_9C41():

        label("loc_9C41")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_9C41")

    QueueWorkItem2(0x8, 3, lambda_9C41)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_9D(0x8, 0x100E, 0x4E2, 0x5DDE, 0xBB8, 0x3E8)
    CancelBlur(0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1)
    Sleep(150)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(900)
    SetChrChipByIndex(0x8, 0x1F)
    OP_95(0x8, 1420, 1250, 23000, 6000, 0x0)
    BeginChrThread(0x8, 2, 0, 44)
    BeginChrThread(0x8, 3, 0, 52)
    BeginChrThread(0x8, 0, 0, 61)
    OP_9D(0x8, 0xFFFFFC7C, 0x4E2, 0x5BC2, 0x7D0, 0xDAC)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 56)

    def lambda_9CF7():
        OP_9D(0x8, 0xFFFFF0D8, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9CF7)
    Sleep(1000)
    BeginChrThread(0x8, 2, 0, 43)
    BeginChrThread(0x8, 3, 0, 52)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)

    def lambda_9D2B():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_9D2B)
    Sleep(700)
    Return()

    # Function_66_9AC9 end

    def Function_67_9D37(): pass

    label("Function_67_9D37")

    OP_9B(0x1, 0xFE, 0x0, 0x1324, 0x7D0, 0x1)
    OP_95(0xFE, -1550, 0, 14280, 2000, 0x0)
    OP_93(0xFE, 0x168, 0x0)
    Return()

    # Function_67_9D37 end

    def Function_68_9D62(): pass

    label("Function_68_9D62")

    OP_9B(0x1, 0xFE, 0x0, 0x12C0, 0x7D0, 0x1)
    OP_95(0xFE, 1550, 0, 14280, 2000, 0x0)
    OP_93(0xFE, 0x168, 0x0)
    Return()

    # Function_68_9D62 end

    def Function_69_9D8D(): pass

    label("Function_69_9D8D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0xC, 0xFF)
    LoadEffect(0x0, "event\\ev290_01.eff")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x2, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x2, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFrame(0x1B, "04Bback", 0x0, 0x1)
    SetMapObjFrame(0x1B, "04light_add", 0x0, 0x1)
    SetMapObjFrame(0x1B, "04Aback", 0x0, 0x1)
    SetMapObjFrame(0x1B, "04moon_add", 0x0, 0x1)
    SetMapObjFrame(0x1B, "04main2", 0x0, 0x1)
    SetMapObjFrame(0x1B, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x1B, "02water02_add", 0x0, 0x1)
    SetMapObjFrame(0x1B, "ball", 0x0, 0x1)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("chr/ch09700.itc", 0x24)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("apl/ch50270.itc", 0x2D)
    LoadChrToIndex("chr/ch09800.itc", 0x2E)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrPos(0x8, -2000, 1250, 24200, 90)
    SetChrPos(0x9, 2000, 1250, 24200, 270)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 650, 2700, -1530, 0)
    SetChrPos(0x102, -520, 2700, -1410, 0)
    SetChrPos(0x104, 570, 2700, -2900, 0)
    SetChrPos(0x103, -600, 2700, -2900, 0)

    def lambda_9FAD():
        OP_95(0xFE, 650, 2700, 530, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FAD)

    def lambda_9FC7():
        OP_95(0xFE, -520, 2700, 410, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FC7)

    def lambda_9FE1():
        OP_95(0xFE, 570, 2700, -900, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9FE1)

    def lambda_9FFB():
        OP_95(0xFE, -600, 2700, -900, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9FFB)
    OP_68(1010, 3000, 740, 0)
    MoveCamera(49, 26, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
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

    #C0394
    ChrTalk(
        0x101,
        "#0011F#11P！！\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x102,
        "#0105F#11Pあ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-70, 3200, 24310, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(790, 0)
    SetCameraDistance(10500, 0)
    OP_68(470, 3200, 23470, 17000)
    MoveCamera(345, 21, -10, 17000)
    OP_6E(600, 17000)
    SetCameraDistance(17000, 17000)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    PlayBGM("ed7530", 1)
    BeginChrThread(0x101, 0, 0, 66)
    BeginChrThread(0x101, 1, 0, 65)
    WaitChrThread(0x101, 0)
    StopBGM(0xFA0)
    Sleep(2000)
    Fade(500)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x2)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x2)
    OP_0D()
    Sleep(300)

    #C0396
    ChrTalk(
        0x8,
        "#6104F#40Wふう……\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        "#6206F#40Wはあ……\x02",
    )

    CloseMessageWindow()
    Sound(853, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    Fade(500)
    SetChrPos(0x8, -1390, 1250, 21930, 180)
    SetChrPos(0x9, 1390, 1250, 21930, 180)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x101, -650, 0, 14950, 0)
    SetChrPos(0x102, 360, 0, 14950, 0)
    SetChrPos(0x103, -1410, 0, 14460, 0)
    SetChrPos(0x104, 1200, 0, 14370, 0)
    OP_68(160, 2200, 16370, 0)
    MoveCamera(0, 8, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(13470, 0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_0D()
    Sleep(300)

    #C0398
    ChrTalk(
        0x8,
        "#6105F#5Pあら……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x9,
        "#6202F#11P皆さん……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x9, 0x20)

    def lambda_A2C6():
        OP_96(0x8, 0xFFFFFB64, 0x4E2, 0x4948, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A2C6)
    Sleep(200)

    def lambda_A2E3():
        OP_96(0x9, 0x4BA, 0x4E2, 0x4948, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A2E3)

    #C0400
    ChrTalk(
        0x104,
        "#0309F#12P#Nうおおお、最高ッスよ！！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0401
    ChrTalk(
        0x101,
        "#0002F#6P#Nす、凄かった……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0402
    ChrTalk(
        0x103,
        "#0204F#6P#N……じんとしました……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(300)

    #C0403
    ChrTalk(
        0x8,
        (
            "#6104F#5Pふふ、このまま詰めていけば\x01",
            "中々のシーンにはなりそうよね。\x02\x03",

            "#6100Fリーシャ、月の姫のターンだけど\x01",
            "ほんの少しタメを作りましょ。\x02\x03",

            "太陽の姫もそれを受けて\x01",
            "虚を突かれる演技を入れるから。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    #C0404
    ChrTalk(
        0x9,
        "#6200F#11Pはいっ……！\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x102,
        (
            "#0104F#12P#N凄いですね……\x02\x03",

            "#0102F一つの舞台を作り上げる……\x01",
            "それだけのためにここまで……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    #C0406
    ChrTalk(
        0x8,
        (
            "#6109F#5Pま、せっかく良くできるんなら\x01",
            "とことんやるのが筋ってもんでしょ。\x02\x03",

            "#6100Fそれよりも……\x01",
            "どうしたの、何か進展でもあった？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(150)

    #C0407
    ChrTalk(
        0x9,
        "#6205F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x102,
        "#0108F#12P#N……はい。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0409
    ChrTalk(
        0x101,
        (
            "#0006F#6P#N少々、残念な報告も\x01",
            "しなくてはいけませんが……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0410
    ChrTalk(
        0x9,
        "#6201F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "#6103F#5Pふむ……いいわ。\x02\x03",

            "#6100F劇団長も呼んでくるから\x01",
            "ここで話を聞かせてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    OP_93(0x8, 0x13B, 0x190)

    def lambda_A64C():
        OP_95(0xFE, -6050, 1250, 24120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A64C)
    TurnDirection(0x9, 0x8, 500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_68(110, 1000, 17000, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(28500, 0)
    OP_68(110, 1000, 17000, 7000)
    MoveCamera(25, 24, 0, 13000)
    OP_6E(420, 13000)
    SetCameraDistance(22000, 13000)
    EndChrThread(0x8, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -1180, 1250, 18760, 180)
    SetChrPos(0xC, -3170, 0, 16329, 60)
    TurnDirection(0xC, 0x101, 0)
    EndChrThread(0xC, 0xFF)
    FadeToBright(4000, 0)
    OP_0D()
    Sleep(1000)

    #C0412
    ChrTalk(
        0xC,
        (
            "#5P《銀#2Rイン#》……\x01",
            "まさかそんな危険なヤツが……\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x9,
        (
            "#6205Fそ、そんな……\x02\x03",

            "#6201F本当にそんな人がこの街に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x8,
        (
            "#6105Fへえ、面白いじゃない。\x02\x03",

            "#6102F東方人街に伝説と謳われた\x01",
            "影のごとき不死の暗殺者か……\x02\x03",

            "#6109Fうーん、いいわね～！\x01",
            "舞台向きのキャラだわ！\x02\x03",

            "#6102Fそうだ！\x01",
            "第三幕の白装束のイメージに\x01",
            "使えるんじゃないかしら！？\x02",
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
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_A903():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_A903)
    Sleep(50)
    TurnDirection(0xC, 0x8, 500)
    Sleep(300)

    #C0415
    ChrTalk(
        0xC,
        "#6Pふう、イリア君……\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x9,
        (
            "#6206F#12Pそんな呑気なことを\x01",
            "言ってる場合じゃないですよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x102,
        (
            "#0103F#12P……《黒月》という勢力が\x01",
            "《銀》という犯罪者を\x01",
            "雇っているのは確かなようです。\x02\x03",

            "#0108Fその《銀》がどうして\x01",
            "イリアさんに脅迫状を送ったのか\x01",
            "そこまでは判りませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        (
            "#0001F#6Pどうも、ただの悪戯であるという\x01",
            "可能性は低くなってきたみたいです。\x02\x03",

            "その、公演を中止するというのは──\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x8,
        (
            "#6104Fあり得ないわね。\x02\x03",

            "たとえ劇場の爆破予告があったとしても\x01",
            "あたしたちは舞台から降りたりしない。\x02\x03",

            "#6100Fそうでしょう、劇団長？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(150)

    #C0420
    ChrTalk(
        0xC,
        "まあ……そうだね。\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xC,
        (
            "イリア君ほどではないにせよ、\x01",
            "私たちは多かれ少なかれ、\x01",
            "舞台という魔物に魅入られた人種だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xC,
        (
            "おそらく、ただの１人として\x01",
            "ウチのアーティストたちが\x01",
            "出場を辞退することは無いだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(150)

    #C0423
    ChrTalk(
        0x9,
        (
            "#6206Fそ、その……\x01",
            "私も新米ですけど同感です。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x104,
        (
            "#0306F#12Pやれやれ……\x01",
            "素晴らしきは舞台の亡者たちか。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x103,
        (
            "#0200F#12Pとなると、他の部署に警備などを\x01",
            "引き継ぐ形になっても構わないと……？\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x8,
        (
            "#6103Fま、正直うっとうしいけど\x01",
            "背に腹は代えられないわね。\x02\x03",

            "#6100F捜査一課だっけ……\x01",
            "どういう人なの、その担当者って。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x101,
        (
            "#0011F#6Pえ、えっと……\x02\x03",

            "#0012F見るからに有能そうというか、\x01",
            "エリートといった感じで……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#0103F#12P実際、相当優秀だとは思います。\x02\x03",

            "#0100F捜査一課というのは警察でも\x01",
            "名実共にエリート集団ですから。\x02\x03",

            "あくまで目立たない形で\x01",
            "完璧に警備するのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#6106Fうげ……勘弁して欲しいわね。\x02\x03",

            "#6101Fでもまあ、お客さんもいる事だし、\x01",
            "安全には配慮するしかないか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 500)
    Sleep(150)

    #C0430
    ChrTalk(
        0xC,
        "#6Pまあ、我慢してくれたまえ。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xC,
        (
            "#6Pどうせ君のことだ。\x01",
            "舞台に集中し始めたら他のことは\x01",
            "一切どうでもよくなるんだろう？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 500)
    Sleep(150)

    #C0432
    ChrTalk(
        0x8,
        (
            "#6101F失礼ね、客には気を配ってるわよ。\x02\x03",

            "#6104F舞台は観客とも響き合うことで\x01",
            "初めて真の意味で完成する……\x02\x03",

            "#6100F劇団長がいつも言ってることじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xC,
        (
            "#6Pうーん、君の場合は\x01",
            "とてもそう思えないんだがねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xC,
        (
            "#6P響き合うというより、無理矢理\x01",
            "自分のリズムに引きずり込むというか。\x02",
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

    #C0435
    ChrTalk(
        0x101,
        "#0012F#6P（な、なんて言うか……）\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x103,
        (
            "#0202F#12P（つくづく本当に\x01",
            "  舞台バカなんですね……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x9)
    TurnDirection(0x9, 0x101, 500)

    #C0437
    ChrTalk(
        0x9,
        (
            "#6201Fあ、あの、それじゃあ……\x02\x03",

            "ロイドさんたちは\x01",
            "これで捜査の方は……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    def lambda_B19D():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B19D)
    Sleep(50)

    def lambda_B1AD():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B1AD)
    Sleep(50)

    def lambda_B1BD():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B1BD)
    Sleep(50)

    def lambda_B1CD():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B1CD)
    Sleep(50)
    TurnDirection(0xC, 0x101, 500)
    Sleep(100)

    #C0438
    ChrTalk(
        0x101,
        (
            "#0006F#6Pああ……申し訳ないけど。\x02\x03",

            "#0000Fまあ、後は一課が引き継ぐし、\x01",
            "心配することはないと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x9,
        "#6206Fそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x8,
        (
            "#6100Fま、弟君に担当してもらえないのは\x01",
            "ちょっと残念だけど……\x02\x03",

            "色々と調べてくれて感謝するわ。\x02\x03",

            "#6109Fお礼にチケット、全員分贈るから\x01",
            "暇な時にでも見に来てちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xC,
        (
            "ふむ、そうだね。\x01",
            "記念祭中の分は無理だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xC,
        (
            "来月分のチケットでよければ\x01",
            "プレゼントさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 500)

    def lambda_B38A():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B38A)
    Sleep(50)

    def lambda_B39A():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B39A)
    Sleep(50)

    def lambda_B3AA():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B3AA)
    Sleep(50)

    def lambda_B3BA():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B3BA)
    TurnDirection(0x9, 0xC, 500)
    Sleep(100)

    #C0443
    ChrTalk(
        0x104,
        (
            "#0305F#11Pマ、マジっスか！？\x02\x03",

            "#0309Fいや～、再来月分になるって\x01",
            "諦めかけてたんだけどな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        "#0202F#11P……太っ腹です。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x102,
        "#0108F#11P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    #C0446
    ChrTalk(
        0x101,
        "#0001F#6P（エリィ……？）\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_69_9D8D end

    SaveToFile()

Try(main)
