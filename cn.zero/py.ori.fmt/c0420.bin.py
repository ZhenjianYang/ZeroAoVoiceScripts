from ZeroScenarioHelper import *

def main():
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
        "伊莉娅",                 # 1
        "莉夏",                   # 2
        "巴尔萨摩经理",           # 3
        "接待员罗兰多",           # 4
        "亚邦剧团长",             # 5
        "海因兹",                 # 6
        "尤金",                   # 7
        "缇奥多尔",               # 8
        "尼克鲁",                 # 9
        "普莉埃",                 # 10
        "塞利娜",                 # 11
        "达德利搜查官",           # 12
        "艾玛搜查官",             # 13
        "雷克特",                 # 14
        "修利",                   # 15
        "搜查官",                 # 16
        "搜查官",                 # 17
        "观众",                   # 18
        "观众",                   # 19
        "观众",                   # 20
        "观众",                   # 21
        "女孩",                   # 22
        "观众",                   # 23
        "观众",                   # 24
        "观众",                   # 25
        "观众",                   # 26
        "麦克道尔市长",           # 27
        "阿奈斯特秘书",           # 28
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
        "Function_8_1651",         # 08, 8
        "Function_9_1795",         # 09, 9
        "Function_10_18B4",        # 0A, 10
        "Function_11_199B",        # 0B, 11
        "Function_12_21AE",        # 0C, 12
        "Function_13_244E",        # 0D, 13
        "Function_14_25C0",        # 0E, 14
        "Function_15_28FD",        # 0F, 15
        "Function_16_29F2",        # 10, 16
        "Function_17_2E2F",        # 11, 17
        "Function_18_2F49",        # 12, 18
        "Function_19_301B",        # 13, 19
        "Function_20_3121",        # 14, 20
        "Function_21_3455",        # 15, 21
        "Function_22_3D31",        # 16, 22
        "Function_23_3F11",        # 17, 23
        "Function_24_4008",        # 18, 24
        "Function_25_40EC",        # 19, 25
        "Function_26_431B",        # 1A, 26
        "Function_27_47A3",        # 1B, 27
        "Function_28_4899",        # 1C, 28
        "Function_29_4905",        # 1D, 29
        "Function_30_4AE0",        # 1E, 30
        "Function_31_4B30",        # 1F, 31
        "Function_32_4B8F",        # 20, 32
        "Function_33_4BD3",        # 21, 33
        "Function_34_4D5B",        # 22, 34
        "Function_35_4D96",        # 23, 35
        "Function_36_4F15",        # 24, 36
        "Function_37_507B",        # 25, 37
        "Function_38_50FA",        # 26, 38
        "Function_39_5158",        # 27, 39
        "Function_40_5CB2",        # 28, 40
        "Function_41_5CDF",        # 29, 41
        "Function_42_5D0C",        # 2A, 42
        "Function_43_5D23",        # 2B, 43
        "Function_44_5D3A",        # 2C, 44
        "Function_45_5D43",        # 2D, 45
        "Function_46_5D4C",        # 2E, 46
        "Function_47_5D55",        # 2F, 47
        "Function_48_5D5E",        # 30, 48
        "Function_49_5D8B",        # 31, 49
        "Function_50_5DB8",        # 32, 50
        "Function_51_5DCF",        # 33, 51
        "Function_52_5DE6",        # 34, 52
        "Function_53_5E05",        # 35, 53
        "Function_54_5E24",        # 36, 54
        "Function_55_5E43",        # 37, 55
        "Function_56_5E62",        # 38, 56
        "Function_57_5E9B",        # 39, 57
        "Function_58_5ED4",        # 3A, 58
        "Function_59_610A",        # 3B, 59
        "Function_60_6133",        # 3C, 60
        "Function_61_7690",        # 3D, 61
        "Function_62_76DB",        # 3E, 62
        "Function_63_798E",        # 3F, 63
        "Function_64_79B5",        # 40, 64
        "Function_65_8C7C",        # 41, 65
        "Function_66_8EB3",        # 42, 66
        "Function_67_9121",        # 43, 67
        "Function_68_914C",        # 44, 68
        "Function_69_9177",        # 45, 69
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DCB")

    #C0001
    ChrTalk(
        0xC,
        (
            "就调整一下今天公演的\x01",
            "角色分配，尽量撑过去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xC,
        (
            "……要是尼克鲁\x01",
            "能回来的话就\x01",
            "最好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164D")

    label("loc_DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DDC")
    Call(0, 12)
    Jump("loc_164D")

    label("loc_DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_F17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E81")

    #C0003
    ChrTalk(
        0xC,
        (
            "贵宾席的客人是\x01",
            "是由我来领位的。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xC,
        (
            "但是……今天有位\x01",
            "很奇怪的客人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xC,
        (
            "年纪轻轻就能来到贵宾席……\x01",
            "可能是在某些方面\x01",
            "有什么人脉吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F12")

    label("loc_E81")

    OP_4B(0x15, 0xFF)

    #C0006
    ChrTalk(
        0x15,
        (
            "#3509F哦哦，好豪华～\x01",
            "视野可真是太棒了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xC,
        (
            "哈哈哈……公演大约\x01",
            "在十分钟后开始。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xC,
        (
            "请尽情欣赏\x01",
            "『金之太阳、银之月』吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x15, 0xFF)

    label("loc_F12")

    Jump("loc_164D")

    label("loc_F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1061")
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F92")

    #C0009
    ChrTalk(
        0xC,
        (
            "我也没有说过\x01",
            "绝对不会去外国演出……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xC,
        (
            "……巴尔萨摩，很抱歉，\x01",
            "你可以再考虑一下这件事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1058")

    label("loc_F92")


    #C0011
    ChrTalk(
        0xC,
        "嗯，演出的事啊……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xC,
        (
            "我听了雾香小姐的话，\x01",
            "也有点动心了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        (
            "那个人似乎\x01",
            "深刻理解了\x01",
            "彩虹剧团的艺术性……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        (
            "……巴尔萨摩，很抱歉，\x01",
            "你可以再考虑一下吗？\x01",
            "不好意思，把这些事都推给你了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1058")

    OP_4C(0xA, 0xFF)
    Jump("loc_164D")

    label("loc_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10EE")

    #C0015
    ChrTalk(
        0xC,
        (
            "因为有伊莉娅的指导，\x01",
            "莉夏的实力也大幅度提高了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xC,
        (
            "其他团员若是也能加把劲儿的话，\x01",
            "肯定能演出一场完美的舞台剧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1191")

    label("loc_10EE")


    #C0017
    ChrTalk(
        0xC,
        "哎呀，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xC,
        (
            "虽然发生了各种各样的事情，大家都手忙脚乱的，\x01",
            "但也得继续排练啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        (
            "莉夏的演技最近\x01",
            "正在显著提高……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xC,
        "其他人也得一起努力才行啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1191")

    Jump("loc_164D")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_133A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1238")

    #C0021
    ChrTalk(
        0xC,
        (
            "（搜查一科的人来得很快呢，\x01",
            "  一大早就开始进行案情调查了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xC,
        (
            "（可是……伊莉娅\x01",
            "  怎么偏偏在今天迟到呢，\x01",
            "  真是让人捏了一把冷汗。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1335")

    label("loc_1238")

    OP_4B(0x13, 0xFF)
    TurnDirection(0xC, 0x13, 0)

    #C0023
    ChrTalk(
        0xC,
        "剧场的平面图吗……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xC,
        (
            "应该刊登在彩虹剧团的\x01",
            "宣传册子上了……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x13,
        (
            "#0603F不，最好能给我\x01",
            "施工时期的设计图。\x02\x03",

            "#0600F出入口、器材搬运通道、仓库、\x01",
            "舞台设备和换气管道都在哪里。\x01",
            "……我全都需要了解。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xC,
        (
            "我、我知道了。\x01",
            "这就去找找看……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 0)

    label("loc_1335")

    Jump("loc_164D")

    label("loc_133A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_13CC")

    #C0027
    ChrTalk(
        0xC,
        (
            "总之，只要能查出事情的真伪，\x01",
            "就算是帮了我们的大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        "真是非常感谢大家的协助。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "日后我会把门票送过去的，\x01",
            "还敬请期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164D")

    label("loc_13CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_152F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1447")

    #C0030
    ChrTalk(
        0xC,
        (
            "新剧上演之前，\x01",
            "后勤部门的工作也会变得很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xC,
        (
            "那封恐吓信……\x01",
            "希望只是个单纯的恶作剧啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152A")

    label("loc_1447")


    #C0032
    ChrTalk(
        0xC,
        (
            "这次的新剧在彩虹剧团\x01",
            "的支持者中也非常受欢迎呢。\x01",
            "仅凭这点，就能预想到届时拥挤的场面。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xC,
        (
            "剧团的使命就是将一切准备妥当，\x01",
            "在万全的体制下迎接客人，让客人可以充分欣赏表演……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xC,
        (
            "为了完成这一使命，\x01",
            "必须要进行周密的准备。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_152A")

    Jump("loc_164D")

    label("loc_152F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15A1")

    #C0035
    ChrTalk(
        0xC,
        (
            "由警方来帮助我们调查，\x01",
            "真是让人安心了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xC,
        (
            "恐吓信的事件就拜托各位了，\x01",
            "请一定要查清此事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164D")

    label("loc_15A1")


    #C0037
    ChrTalk(
        0xC,
        (
            "对于自己被犯人盯上这件事，\x01",
            "伊莉娅要是也能稍微\x01",
            "在意一下就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xC,
        (
            "……咳咳，总之，\x01",
            "恐吓信一事就交给各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xC,
        (
            "要是查清了什么线索，\x01",
            "请立刻告诉我。\x01",
            "万事拜托了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_164D")

    TalkEnd(0xFE)
    Return()

    # Function_7_D5B end

    def Function_8_1651(): pass

    label("Function_8_1651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1703")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166F")
    Call(0, 9)
    Jump("loc_16FE")

    label("loc_166F")


    #C0040
    ChrTalk(
        0xA,
        (
            "其实，我正在考虑要不要\x01",
            "去共和国进行演出呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xA,
        (
            "前些日子，从共和国前来的雾香小姐\x01",
            "提出了十分诱人的条件。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "我认为很有认真考虑\x01",
            "的价值。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FE")

    Jump("loc_1791")

    label("loc_1703")


    #C0043
    ChrTalk(
        0xA,
        (
            "虽然不知道恐吓信的真假，\x01",
            "但作为经理，\x01",
            "必须要确保剧场的安全……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "嗯，在正式开演之前，\x01",
            "加强剧场内的巡视工作吧。\x01",
            "总比什么都不做要好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1791")

    TalkEnd(0xFE)
    Return()

    # Function_8_1651 end

    def Function_9_1795(): pass

    label("Function_9_1795")


    #C0045
    ChrTalk(
        0xFE,
        (
            "对了对了，本剧团新雇了一个\x01",
            "打杂的孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "名字叫做修利。\x01",
            "要是见到的话，还请多关照她哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18B0")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1841")

    #C0047
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，修利好像\x01",
            "干得还不错嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B0")

    label("loc_1841")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_187B")

    #C0048
    ChrTalk(
        0x103,
        (
            "#0200F……看来她\x01",
            "干得还不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B0")

    label("loc_187B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18B0")

    #C0049
    ChrTalk(
        0x104,
        (
            "#0300F嘿，看来她\x01",
            "干得还挺好嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B0")

    SetScenarioFlags(0xD1, 6)
    Return()

    # Function_9_1795 end

    def Function_10_18B4(): pass

    label("Function_10_18B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_192A")

    #C0050
    ChrTalk(
        0xB,
        (
            "我也在帮忙做些\x01",
            "排练的准备工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "距离预演只有\x01",
            "不到两周时间了，\x01",
            "我得让大家都能安心排练啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1997")

    label("loc_192A")


    #C0052
    ChrTalk(
        0xB,
        "嗯，下一个场景的照明设置，还有……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "哎呀呀，都是因为搜查一科\x01",
            "的人到处乱转，\x01",
            "准备工作都被耽误了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1997")

    TalkEnd(0xFE)
    Return()

    # Function_10_18B4 end

    def Function_11_199B(): pass

    label("Function_11_199B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A0E")

    #C0054
    ChrTalk(
        0x8,
        (
            "#1701F这么说来的话，他昨天晚上\x01",
            "好像很奇怪呢。\x02\x03",

            "#1706F……虽然是现在回想起来才发觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8B")

    label("loc_1A0E")


    #C0055
    ChrTalk(
        0x8,
        (
            "#1706F说起来，他昨晚\x01",
            "感觉特别奇怪呢。\x02\x03",

            "#1701F不知该形容为亢奋还是什么……\x01",
            "还狠狠瞪着我呢。\x02\x03",

            "#1709F我当然也回瞪过去了！\x02",
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
            "#0012F该说什么好呢……\x01",
            "真像是伊莉娅小姐的作风啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0108F不过，竟然对伊莉娅小姐\x01",
            "摆出那样的态度……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        (
            "#0303F嗯……\x01",
            "实在不像是新人该有的样子啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1B8B")

    Jump("loc_21AA")

    label("loc_1B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1BA1")
    Call(0, 12)
    Jump("loc_21AA")

    label("loc_1BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1BF9")

    #C0059
    ChrTalk(
        0x8,
        (
            "#1701F#11P──那里！\x01",
            "动感再强一点！\x02\x03",

            "对，抓准节拍！\x01",
            "要像弹起来一样！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AA")

    label("loc_1BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1C94")

    #C0060
    ChrTalk(
        0x8,
        (
            "#1703F不能让警察弟弟负责此事，\x01",
            "实在很遗憾呢……\x02\x03",

            "#1700F唉，但也没办法了。\x02\x03",

            "#1706F……唉，我原以为\x01",
            "只是个恶作剧，\x01",
            "没想到变得越来越麻烦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AA")

    label("loc_1C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1F51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1D0F")

    #C0061
    ChrTalk(
        0x8,
        (
            "#1704F莉夏还有继续成长的潜力，\x01",
            "我对她抱有很大期望呢。\x02\x03",

            "#1702F呵呵，我自己也\x01",
            "必须要不断进步啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4C")

    label("loc_1D0F")


    #C0062
    ChrTalk(
        0x8,
        (
            "#1703F如果只是我一个人的表演，\x01",
            "目前已经可以算是完美了。\x02\x03",

            "#1700F不过，莉夏的演技\x01",
            "可是相当优秀呢。\x02\x03",

            "我要是不继续提升水平的话，\x01",
            "就无法完成最精彩的表演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0002F哎……她竟然\x01",
            "如此有才能啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#0305F是啊，虽说是被破格提拔，\x01",
            "选定为二号主演的重量级新星，\x01",
            "但却一点都没有那种感觉呢。\x02\x03",

            "#0309F硬要说的话，\x01",
            "她应该算是治愈系或是温柔系吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#1702F呵呵，那孩子在我们剧团里\x01",
            "也算得上是顶级水准的演员呢。\x02\x03",

            "#1704F虽然她自己可能\x01",
            "并没有注意到，\x01",
            "但她的潜力与我不相上下。\x02\x03",

            "#1701F不，将来\x01",
            "有可能还会超越我。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#0105F真、真的吗……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x103,
        (
            "#0204F……真想看看\x01",
            "莉夏小姐的演出啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1F4C")

    Jump("loc_21AA")

    label("loc_1F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_21A7")

    #C0068
    ChrTalk(
        0x8,
        (
            "#1704F呵呵，\x01",
            "这次的演出阵容可是很强大的哦～\x02\x03",

            "#1702F象征着太阳的我，\x01",
            "与象征着月亮的莉夏产生对比。\x02\x03",

            "虽然会发生激烈的冲突，\x01",
            "但两道光芒最终将相互融合，共同升华，\x01",
            "创造出同一个耀眼的舞台……\x02\x03",

            "#1709F距离正式演出已经没有几天了，\x01",
            "我必须要继续提高自己的水平才行！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AF")

    #C0069
    ChrTalk(
        0x101,
        (
            "#0012F（嗯，已经满脑子\x01",
            "  都是演出的事了啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219F")

    label("loc_20AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20F3")

    #C0070
    ChrTalk(
        0x102,
        (
            "#0102F（似乎满脑子\x01",
            "  都在想演出的事呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219F")

    label("loc_20F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213D")

    #C0071
    ChrTalk(
        0x103,
        (
            "#0202F（她的脑子里现在好像\x01",
            "  只有表演的事了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219F")

    label("loc_213D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_219F")

    #C0072
    ChrTalk(
        0x104,
        (
            "#0309F（真不愧是伊莉娅·普拉提耶，\x01",
            "  恐吓信那种小事，\x01",
            "  早就忘到脑后去了吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219F")

    SetScenarioFlags(0x0, 3)

    label("loc_21A2")

    Jump("loc_21AA")

    label("loc_21A7")

    Call(0, 13)

    label("loc_21AA")

    TalkEnd(0xFE)
    Return()

    # Function_11_199B end

    def Function_12_21AE(): pass

    label("Function_12_21AE")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22A6")

    #C0073
    ChrTalk(
        0xC,
        "对了对了，还有之前那件事……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "#1705F#11P哦，是指尼克鲁吧。\x02\x03",

            "#1706F他最近的状态确实莫名地好，\x01",
            "不过考虑到他的角色，\x01",
            "还是有些欠缺平衡感呢～\x02\x03",

            "#1709F对了！\x01",
            "干脆追加一幕他和缇奥多尔\x01",
            "的决斗场面如何！？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xC,
        "唉，饶了我吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2445")

    label("loc_22A6")


    #C0076
    ChrTalk(
        0x8,
        (
            "#1703F#11P嗯～我个人也认为\x01",
            "那种演出不太可行。\x02\x03",

            "#1701F如果真要追加剧情的话，\x01",
            "应该选择更能牢牢\x01",
            "抓住观众心灵的那种。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        (
            "嗯……但是考虑到整个演出，\x01",
            "我不想换成别的。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        (
            "我很尊重你的意见，\x01",
            "不过能否再稍微考虑一下呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        "#1706F#11P──不要。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0080
    ChrTalk(
        0xC,
        "我就知道你会这么说……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        (
            "#0200F（似乎在讨论演出内容呢……\x01",
            "  剧团长的意见被否决了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0000F（我们就别在\x01",
            "  这里打扰他们了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2445")

    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_21AE end

    def Function_13_244E(): pass

    label("Function_13_244E")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0083
    ChrTalk(
        0x8,
        (
            "#1702F好了，莉夏，\x01",
            "我们就继续昨天的练习吧。\x02\x03",

            "#1704F排练的时候，\x01",
            "必须要把握住自己的节奏。\x02\x03",

            "光是一味去配合对方是不行的，\x01",
            "当然啦，只把自己的步调强加于人也不可以。\x02\x03",

            "#1700F关于这些，很难具体解释清楚，\x01",
            "也只能靠你自己来慢慢找感觉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        "总之，就是这么回事。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xC,
        (
            "已经没什么时间了，\x01",
            "立刻开始练习吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "#1800F好、好的！\x01",
            "请多指教！\x02",
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

    # Function_13_244E end

    def Function_14_25C0(): pass

    label("Function_14_25C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2642")

    #C0087
    ChrTalk(
        0x9,
        (
            "#1806F尼克鲁先生\x01",
            "最近的样子很奇怪。\x01",
            "甚至可以说，连性格都改变了……\x02\x03",

            "#1808F………………………………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E0")

    label("loc_2642")


    #C0088
    ChrTalk(
        0x9,
        (
            "#1806F尼克鲁先生最近\x01",
            "的样子很奇怪。\x02\x03",

            "#1808F………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0000F莉夏，别担心，\x01",
            "我们会负责调查的。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "#1810F好的……\x01",
            "那就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_26E0")

    Jump("loc_28F9")

    label("loc_26E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_286C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_277D")

    #C0091
    ChrTalk(
        0x9,
        (
            "#1806F预演也已经临近了，\x01",
            "必须要抓紧时间多加练习，\x01",
            "所以总是不自觉地感到焦虑。\x02\x03",

            "#1810F伊莉娅小姐今天也迟到了，\x01",
            "着急也没用啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2867")

    label("loc_277D")


    #C0092
    ChrTalk(
        0x9,
        (
            "#1802F啊，各位……\x01",
            "早上好啊。\x02\x03",

            "#1804F真是非常感谢\x01",
            "大家帮忙调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，不用客气。\x02\x03",

            "#0000F……搜查一科的人\x01",
            "好像也来得很快啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#1809F啊哈哈……我也\x01",
            "被叫去询问了呢。\x02\x03",

            "#1810F伊莉娅小姐今天也迟到了，\x01",
            "着急也没用啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2867")

    Jump("loc_28F9")

    label("loc_286C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_287D")
    Call(0, 15)
    Jump("loc_28F9")

    label("loc_287D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_28F6")

    #C0095
    ChrTalk(
        0x9,
        (
            "#1806F对不起，\x01",
            "我还要排练……\x02\x03",

            "#1802F不过，能和大家商量一下，\x01",
            "真是太好了。\x02\x03",

            "恐吓信一事\x01",
            "就拜托大家了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F9")

    label("loc_28F6")

    Call(0, 13)

    label("loc_28F9")

    TalkEnd(0xFE)
    Return()

    # Function_14_25C0 end

    def Function_15_28FD(): pass

    label("Function_15_28FD")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0096
    ChrTalk(
        0xD,
        (
            "我知道了，\x01",
            "从第十八场开始，再来一次是吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "我整理一下舞台，\x01",
            "请稍等。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        "#6201F好的，拜托您了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E9")

    #C0099
    ChrTalk(
        0x101,
        "#0005F（好像挺忙的啊……）\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0304F（为了预演，正在做最后的调整……\x01",
            "  呼，要是打扰到人家就不好啦。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_29E9")

    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_28FD end

    def Function_16_29F2(): pass

    label("Function_16_29F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2A52")

    #C0101
    ChrTalk(
        0xE,
        "不好意思，正在进行排练呢。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        "如果想参观的话，请坐在观众席上。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B09")

    label("loc_2A52")

    OP_4B(0xF, 0xFF)

    #C0103
    ChrTalk(
        0xE,
        "很好，下面进行最后一幕。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xE,
        (
            "呵……刚睡醒的剑士啊，\x01",
            "你愿意跟我走吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xF,
        "……最后一幕是吗，没问题……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xF,
        "………有『月之姬』出场吗？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xE,
        "喂喂，给我认真点啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 5)
    OP_4C(0xF, 0xFF)

    label("loc_2B09")

    Jump("loc_2E2B")

    label("loc_2B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2B6E")

    #C0108
    ChrTalk(
        0xE,
        "主要问题还是尼克鲁啊……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xE,
        (
            "那家伙也下功夫了，\x01",
            "但却总是欠点火候。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C03")

    label("loc_2B6E")


    #C0110
    ChrTalk(
        0xE,
        (
            "缇奥多尔那家伙，\x01",
            "一登上舞台就能发挥出\x01",
            "令人震惊的高超演技。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xE,
        (
            "哎呀呀，而且\x01",
            "今天的状态似乎格外好呢。\x01",
            "连我这个超一流的大明星都有些佩服他了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2C03")

    Jump("loc_2E2B")

    label("loc_2C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2C52")

    #C0112
    ChrTalk(
        0xE,
        (
            "啊，另外……\x01",
            "这件事可别跟别人说啊。\x01",
            "因为是秘密特训呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E2B")

    label("loc_2C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2CF6")

    #C0113
    ChrTalk(
        0xE,
        (
            "跟那个伊莉娅演对手戏的时候，\x01",
            "连我也得多下功夫才行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xE,
        (
            "……莉夏就更别说了，\x01",
            "肯定非常辛苦的。\x01",
            "我对她表示同情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xE,
        "对了，这可是秘密啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2E2B")

    label("loc_2CF6")


    #C0116
    ChrTalk(
        0xE,
        "呼，差不多也就到此为止了吧……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xE, 0x0, 750)
    Sleep(750)

    #C0117
    ChrTalk(
        0xE,
        (
            "什、什么啊，是警察吧。\x01",
            "真是的，别吓唬人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0005F那个……\x01",
            "你在这里练习吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xE,
        (
            "是啊，因为这次要和\x01",
            "那个伊莉娅\x01",
            "演对手戏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xE,
        (
            "为了不影响到\x01",
            "她绽放出的强烈光芒，\x01",
            "也为了让我的角色能够发光……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xE,
        (
            "就算是我，\x01",
            "也得多下点功夫啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_2E2B")

    TalkEnd(0xFE)
    Return()

    # Function_16_29F2 end

    def Function_17_2E2F(): pass

    label("Function_17_2E2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2EA5")

    #C0122
    ChrTalk(
        0xF,
        (
            "说起来……\x01",
            "团里新来了个打杂的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xF,
        (
            "……她的动作好像\x01",
            "挺灵活的……\x01",
            "那家伙也许挺有才能呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F45")

    label("loc_2EA5")


    #C0124
    ChrTalk(
        0xF,
        (
            "……明明是休息日，\x01",
            "还被尤金给叫了出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0125
    ChrTalk(
        0xF,
        "有点困啊……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#0003F（剧团成员……\x01",
            "  平时跟演出时的样子，差别可真大啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_2F45")

    TalkEnd(0xFE)
    Return()

    # Function_17_2E2F end

    def Function_18_2F49(): pass

    label("Function_18_2F49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2FB4")

    #C0127
    ChrTalk(
        0x11,
        (
            "尼克鲁总是容易陷入烦恼，\x01",
            "我早就注意到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x11,
        (
            "呼……他去哪里了，\x01",
            "正在做些什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3017")

    label("loc_2FB4")


    #C0129
    ChrTalk(
        0x11,
        (
            "既然剧本做出调整了，\x01",
            "演技也不得不改变一下了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x11,
        (
            "呼……尼克鲁的事情，\x01",
            "我也挺担心的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_3017")

    TalkEnd(0xFE)
    Return()

    # Function_18_2F49 end

    def Function_19_301B(): pass

    label("Function_19_301B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3074")

    #C0131
    ChrTalk(
        0x12,
        (
            "不仅是莉夏，连尼克鲁都\x01",
            "有可能会超过我呢……\x01",
            "我也必须得加把劲儿了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_311D")

    label("loc_3074")


    #C0132
    ChrTalk(
        0x12,
        (
            "尼、尼克鲁\x01",
            "最近的状态超级好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x12,
        (
            "今天彩排时，\x01",
            "他也发挥出了高超的演技。\x02",
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
            "……不、不好。\x01",
            "不仅是莉夏，连尼克鲁都\x01",
            "有可能会超过我呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_311D")

    TalkEnd(0xFE)
    Return()

    # Function_19_301B end

    def Function_20_3121(): pass

    label("Function_20_3121")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_322D")
    OP_64(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3186")

    #C0135
    ChrTalk(
        0x10,
        (
            "唉，人生可真是\x01",
            "坎坷啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x10,
        (
            "莉夏完全得到了大家认可，\x01",
            "而我却……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3216")

    label("loc_3186")


    #C0137
    ChrTalk(
        0x10,
        (
            "在昨天的公演中，\x01",
            "我出了个大差错啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x10,
        (
            "呜呜，在纪念庆典时，\x01",
            "我也犯过很多小错误……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x10,
        (
            "我已经非常认真地练习了，\x01",
            "真令人失落啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_3216")

    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_3451")

    label("loc_322D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_32C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_325E")

    #C0140
    ChrTalk(
        0xFE,
        "唉，真是不顺利啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_32C3")

    label("loc_325E")


    #C0141
    ChrTalk(
        0x10,
        (
            "这里要这样做，\x01",
            "然后接上旋转动作……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……嗯，还是有点不太对啊。\x01",
            "进行得一点也不顺利呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_32C3")

    Jump("loc_3451")

    label("loc_32C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DB")

    #C0143
    ChrTalk(
        0xFE,
        "在这次的新剧里，我也有角色了。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "虽然只是个跑龙套的，\x01",
            "但即使如此，毕竟也是彩虹剧团的舞台啊。\x01",
            "对于我来说，已经很想大喊万岁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "但是……莉夏\x01",
            "却能出演二号主角呢。\x01",
            "入团时间明明比我还晚……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "呜呜，真让人着急啊，\x01",
            "我果然和她不是同一个级别的吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3451")

    label("loc_33DB")


    #C0147
    ChrTalk(
        0xFE,
        (
            "莉夏的才能是货真价实的。\x01",
            "能出演重要的角色，也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "和她一比，我可真是……\x01",
            "……呜呜，真让人着急啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3451")

    TalkEnd(0xFE)
    Return()

    # Function_20_3121 end

    def Function_21_3455(): pass

    label("Function_21_3455")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_35B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3534")
    OP_4B(0x16, 0xFF)

    #C0149
    ChrTalk(
        0xD,
        "帷幕的上卷速度要改变……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xD,
        (
            "突显舞台的方式改成方案Ｂ，\x01",
            "照明和音乐也要把握时机……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x16,
        "……知道了，就是这样吧？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xD,
        (
            "对，就是这样，这样就好……\x01",
            "正式演出的时候也按这样来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x16, 0xFF)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x1, 3)
    Jump("loc_35AF")

    label("loc_3534")


    #C0153
    ChrTalk(
        0xD,
        (
            "在这个时间点调整剧本，\x01",
            "后台也忙坏了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xD,
        (
            "呼，但好在有修利在这里，\x01",
            "可真是帮大忙了。\x01",
            "帷幕的控制也交给她控制好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AF")

    Jump("loc_3D2D")

    label("loc_35B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_362B")

    #C0155
    ChrTalk(
        0xD,
        (
            "纪念庆典之后，尼克鲁先生\x01",
            "似乎有点想不开。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xD,
        (
            "然后就开始拼命练习……\x01",
            "我们也有点担心他呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3680")

    label("loc_362B")


    #C0157
    ChrTalk(
        0xD,
        "没想到尼克鲁先生会失踪……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        (
            "他最近练习得\x01",
            "特别拼命，\x01",
            "会不会和这个有关呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_3680")

    Jump("loc_3D2D")

    label("loc_3685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3780")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_36EE")

    #C0159
    ChrTalk(
        0xD,
        (
            "尼克鲁先生到底要到\x01",
            "什么时候才肯去休息啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "最近他似乎有点\x01",
            "努力过头了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377B")

    label("loc_36EE")


    #C0161
    ChrTalk(
        0xD,
        (
            "昨晚又擅自动用了\x01",
            "舞台装置……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xD,
        (
            "尼克鲁先生好像\x01",
            "独自一人练习了一整夜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xD,
        (
            "热心练习虽然是件好事，\x01",
            "但这是不是也有点\x01",
            "太过火了呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_377B")

    Jump("loc_3D2D")

    label("loc_3780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_38A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382A")

    #C0164
    ChrTalk(
        0xFE,
        (
            "其实，我前两天去了\x01",
            "一个熟人的工房……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "结果有个特别可爱的小女孩\x01",
            "出来迎接我，大概是他的孙女吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "我都不知道那位老人\x01",
            "还有个孙女呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_389F")

    label("loc_382A")


    #C0167
    ChrTalk(
        0xFE,
        (
            "那个工房帮忙制作了\x01",
            "彩虹剧团的舞台装置。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "但是……我还真不知道\x01",
            "那位老人有个孙女呢。\x01",
            "……哈，真是吓了一大跳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389F")

    Jump("loc_3D2D")

    label("loc_38A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_39B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3915")

    #C0169
    ChrTalk(
        0xD,
        (
            "正式演出的时候，搜查官们\x01",
            "好像会站在各处把守。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xD,
        (
            "希望不要影响\x01",
            "舞台上的照明效果啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AF")

    label("loc_3915")


    #C0171
    ChrTalk(
        0xD,
        (
            "嗯，这一场景的照明角度\x01",
            "这样就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xD,
        (
            "但是……等到正式演出的时候，\x01",
            "搜查官们好像会站在各处把守呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xD,
        (
            "我很担心他们会\x01",
            "挡住舞台上的照明光源呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_39AF")

    Jump("loc_3D2D")

    label("loc_39B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3ADC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A64")

    #C0174
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的舞台装置需要既\x01",
            "纤细又大胆的表现力。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "所以说，不是一朝一夕\x01",
            "就能简单完工的。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "在某个熟人的工房的帮助下，\x01",
            "总算是渐渐接近完成了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_3AD7")

    label("loc_3A64")


    #C0177
    ChrTalk(
        0xFE,
        (
            "支撑了彩虹剧团的\x01",
            "这个舞台装置，\x01",
            "也算是一个艺术品啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "在某个熟人的工房的帮助下，\x01",
            "如今已经渐渐接近完工了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD7")

    Jump("loc_3D2D")

    label("loc_3ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3AED")
    Call(0, 15)
    Jump("loc_3D2D")

    label("loc_3AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3B6F")

    #C0179
    ChrTalk(
        0xD,
        (
            "哎呀呀，\x01",
            "伊莉娅小姐可真是爱难为人啊。\x01",
            "也不知道那种调整能不能做得到。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xD,
        "当然了，不管是否可行，总要先试试看。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D2D")

    label("loc_3B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3BE7")

    #C0181
    ChrTalk(
        0xD,
        (
            "伊莉娅小姐为了舞台表演\x01",
            "而献出的热情是很让人钦佩的。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xD,
        (
            "她甚至会直接向\x01",
            "身为导演的剧团长提出意见呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D2D")

    label("loc_3BE7")


    #C0183
    ChrTalk(
        0xD,
        (
            "各位就是……剧团长\x01",
            "所提到的警察吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xD,
        (
            "参观是没问题，\x01",
            "但请不要触碰任何东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#0005F这是……\x01",
            "舞台装置吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xD,
        (
            "是啊，是为了彩虹剧团的舞台表演\x01",
            "而特别定制的舞台装置。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xD,
        (
            "伊莉娅小姐\x01",
            "亲自提出要求了，\x01",
            "所以现在正为了演出而进行调整呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xD,
        (
            "哎呀呀，又提出这种困难的要求啊。\x01",
            "那个人对于舞台，简直比剧团长还要热情呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_3D2D")

    TalkEnd(0xFE)
    Return()

    # Function_21_3455 end

    def Function_22_3D31(): pass

    label("Function_22_3D31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D4F")
    Call(0, 24)
    Jump("loc_3DD2")

    label("loc_3D4F")


    #C0189
    ChrTalk(
        0xFE,
        (
            "#0603F……特别任务支援科别在这里转来转去。\x02\x03",

            "还是说，你们听不懂我的话？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#0006F不，对、对不起。\x01",
            "（好像有点太大胆了啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD2")

    Jump("loc_3F0D")

    label("loc_3DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E96")
    OP_4B(0x14, 0xFF)
    TurnDirection(0xFE, 0xC, 0)

    #C0191
    ChrTalk(
        0xFE,
        (
            "#0600F原来如此，我了解状况了。\x02\x03",

            "#0603F艾玛，把这封恐吓信\x01",
            "交给鉴定科。\x02\x03",

            "#0601F虽然应该查不出具体的指纹，\x01",
            "但多少能收集到一些线索吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x14,
        "是，我立刻去办。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    OP_4C(0x14, 0xFF)
    Jump("loc_3F0D")

    label("loc_3E96")


    #C0193
    ChrTalk(
        0xFE,
        (
            "#0600F你们几个……\x01",
            "这里应该已经没你们什么事了吧？\x02\x03",

            "#0603F别再继续纠缠不休了，\x01",
            "赶紧离开，\x01",
            "这里已经交由我们管辖了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0D")

    TalkEnd(0xFE)
    Return()

    # Function_22_3D31 end

    def Function_23_3F11(): pass

    label("Function_23_3F11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3F6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2F")
    Call(0, 24)
    Jump("loc_3F6A")

    label("loc_3F2F")


    #C0194
    ChrTalk(
        0xFE,
        (
            "果然应该重点注意预演啊……\x01",
            "我马上就去准备必要的文件。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F6A")

    Jump("loc_4004")

    label("loc_3F6F")


    #C0195
    ChrTalk(
        0xFE,
        (
            "……希望你们不要\x01",
            "给我们搜查一科添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "还是说，你们支援科成员\x01",
            "的兴趣就是争着出风头呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0001F（说、说得还真是\x01",
            "  丝毫不留情面啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4004")

    TalkEnd(0xFE)
    Return()

    # Function_23_3F11 end

    def Function_24_4008(): pass

    label("Function_24_4008")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x2D, 0x0)

    #C0198
    ChrTalk(
        0x14,
        "这里是最适合狙击的位置啊……\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x13,
        (
            "#0601F可恶，这个剧场的构造本身就有问题，\x01",
            "疏漏之处实在是太多了。\x02\x03",

            "#0600F……艾玛，由我来守卫这里，\x01",
            "警卫计划变更为Ｂ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x14,
        (
            "我知道了，\x01",
            "马上变更人员配置。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_24_4008 end

    def Function_25_40EC(): pass

    label("Function_25_40EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_429F")

    #C0201
    ChrTalk(
        0x101,
        (
            "#0005F哎，雷、雷克特先生……？\x01",
            "你在这里做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x15,
        (
            "#3502F哈哈哈，那还用说吗？\x01",
            "当然是来参观彩虹剧团了！\x02\x03",

            "#3504F哎呀～我以为会迟到，\x01",
            "中途还跑了几步呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x104,
        (
            "#0309F哈哈，能够理解……\x02\x03",

            "#0307F……等、等一下！！\x01",
            "这里好像是贵宾席吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        (
            "#0101F应该不是一般人\x01",
            "能进入的场所……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x15,
        (
            "#3507F噢，那是因为宰相──咳咳。\x02\x03",

            "#3509F哎呀～我家那个老头子，\x01",
            "偶尔也还有点用处嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x103,
        "#0211F（完全看不透他的行动模式……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 4)
    Jump("loc_4317")

    label("loc_429F")


    #C0207
    ChrTalk(
        0x15,
        (
            "#3504F嗯嗯，这沙发\x01",
            "坐着可真舒服啊。\x02\x03",

            "#3510F……那就睡到演出开始吧！！\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        (
            "#0206F（完全看不透\x01",
            "  他的行动模式……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4317")

    TalkEnd(0xFE)
    Return()

    # Function_25_40EC end

    def Function_26_431B(): pass

    label("Function_26_431B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4338")
    Call(0, 27)
    Jump("loc_479F")

    label("loc_4338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_45D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 1)), scpexpr(EXPR_END)), "loc_43AF")

    #C0209
    ChrTalk(
        0xFE,
        (
            "说起来，莉夏真是好慢啊……\x01",
            "她好像说把东西忘在家里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "没办法，一会去\x01",
            "接她过来吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CB")

    label("loc_43AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4584")

    #C0211
    ChrTalk(
        0xFE,
        (
            "还要对剧本进行调整，\x01",
            "剧团现在超级忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        "别在这里碍手碍脚的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_457C")

    #C0213
    ChrTalk(
        0x101,
        (
            "#0006F抱歉，\x01",
            "我只是稍微有点在意……\x02\x03",

            "#0000F不过再怎么说，\x01",
            "演出应该也能顺利进行吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "那、那当然了。\x01",
            "我也一直在拼命帮忙啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    #C0215
    ChrTalk(
        0xFE,
        (
            "就算硬着头皮，\x01",
            "也要设法让演出取得成功啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "……那个，这些用不着\x01",
            "你们来担心啦。\x01",
            "赶快回去工作吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x104,
        "#0300F哈哈，真是少见的可靠言辞啊。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0000F谢啦，\x01",
            "那我们这就回去工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "……嗯，\x01",
            "你们也加油吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 1)

    label("loc_457C")

    SetScenarioFlags(0x1, 7)
    Jump("loc_45CB")

    label("loc_4584")


    #C0220
    ChrTalk(
        0xFE,
        "你们几个怎么回事……\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "剧团现在可是超级忙。\x01",
            "别在这里碍手碍脚！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CB")

    Jump("loc_479F")

    label("loc_45D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_46E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466C")

    #C0222
    ChrTalk(
        0xFE,
        (
            "尼克鲁那家伙，\x01",
            "好像有点奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "又去找莉夏麻烦，\x01",
            "又去招惹伊莉娅小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "我正要冲上去打他，\x01",
            "就被伊莉娅小姐阻止了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_46DD")

    label("loc_466C")


    #C0225
    ChrTalk(
        0xFE,
        (
            "说起来，那家伙在\x01",
            "纪念庆典的最后一天表演失误，\x01",
            "似乎非常失落呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "好像是从那时开始，\x01",
            "他就变得很奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46DD")

    Jump("loc_479F")

    label("loc_46E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_479F")

    #C0227
    ChrTalk(
        0xFE,
        "莉夏真是太温柔了。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "根本就不用因为\x01",
            "那种人说的话而退让啊……\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_479C")

    #C0229
    ChrTalk(
        0x101,
        "#0000F发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)

    #C0230
    ChrTalk(
        0xFE,
        (
            "没什么……\x01",
            "也不是我该乱讲的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_479C")

    SetScenarioFlags(0x1, 7)

    label("loc_479F")

    TalkEnd(0xFE)
    Return()

    # Function_26_431B end

    def Function_27_47A3(): pass

    label("Function_27_47A3")


    #C0231
    ChrTalk(
        0x101,
        (
            "#0005F咦……？\x01",
            "剧团里还有这样的孩子吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4812")

    #C0232
    ChrTalk(
        0xFE,
        (
            "……你是干什么的，\x01",
            "难道认识伊莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4843")

    label("loc_4812")


    #C0233
    ChrTalk(
        0xFE,
        (
            "……你们是干什么的，\x01",
            "难道认识伊莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4843")


    #C0234
    ChrTalk(
        0xFE,
        (
            "哼……\x01",
            "无关人员禁止进入剧团。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "就算认识伊莉娅小姐，\x01",
            "也别厚着脸皮进来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Return()

    # Function_27_47A3 end

    def Function_28_4899(): pass

    label("Function_28_4899")

    TalkBegin(0xFE)

    #C0236
    ChrTalk(
        0xFE,
        (
            "疏漏之处的确很多……\x01",
            "这不是从哪个方向\x01",
            "都能随便狙击舞台吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "可恶……犯人也真会\x01",
            "给人添乱啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_4899 end

    def Function_29_4905(): pass

    label("Function_29_4905")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7C")

    #C0238
    ChrTalk(
        0xFE,
        (
            "至预演开始为止，\x01",
            "必须要做好万全的警备体制……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "伊莉娅·普拉提耶要是出了什么事，\x01",
            "对自治州政府来说，可是个极其严重的问题。\x01",
            "……有可能会演变为政治问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#0005F（艾莉……真的吗？）\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#0103F（确实有这种可能性……\x01",
            "  伊莉娅小姐是一位对周边诸国\x01",
            "  都有着很大影响力的人物。）\x02\x03",

            "#0101F（她这种公众人物有了麻烦，\x01",
            "  议员们大概也都无法坐视不管吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_4ADC")

    label("loc_4A7C")


    #C0242
    ChrTalk(
        0xFE,
        (
            "喂，来凑热闹的特别任务支援科。\x01",
            "你们应该已经不负责这件事了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "无关人员就\x01",
            "快点走开吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ADC")

    TalkEnd(0xFE)
    Return()

    # Function_29_4905 end

    def Function_30_4AE0(): pass

    label("Function_30_4AE0")

    TalkBegin(0xFE)

    #C0244
    ChrTalk(
        0xFE,
        (
            "我就是为了这一天，\x01",
            "才从帝国远道而来。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "哈哈哈，真是让人期待啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_4AE0 end

    def Function_31_4B30(): pass

    label("Function_31_4B30")

    TalkBegin(0xFE)

    #C0246
    ChrTalk(
        0xFE,
        (
            "我还是第一次观看\x01",
            "彩虹剧团的演出呢，\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "这部新剧的人气特别高，\x01",
            "所以就更加期待了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_4B30 end

    def Function_32_4B8F(): pass

    label("Function_32_4B8F")

    TalkBegin(0xFE)

    #C0248
    ChrTalk(
        0xFE,
        "马上就能看彩虹剧团的表演了！\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        "#4S……伊莉娅小姐！！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_4B8F end

    def Function_33_4BD3(): pass

    label("Function_33_4BD3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C67")
    Jump("loc_4CB1")

    label("loc_4C67")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C87")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB1")

    label("loc_4C87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CA7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB1")

    label("loc_4CA7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CB1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0250
    ChrTalk(
        0xFE,
        (
            "嗯，我对这个叫莉夏·毛的新人\x01",
            "也挺有兴趣的。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "她似乎得到了很高的评价……\x01",
            "今天就让我好好见识一下\x01",
            "她在舞台上的表演吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_4BD3 end

    def Function_34_4D5B(): pass

    label("Function_34_4D5B")

    TalkBegin(0xFE)

    #C0252
    ChrTalk(
        0xFE,
        "爸爸，还没开始吗？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "呜，我已经等不及了啦。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_4D5B end

    def Function_35_4D96(): pass

    label("Function_35_4D96")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E2A")
    Jump("loc_4E74")

    label("loc_4E2A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E4A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E74")

    label("loc_4E4A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E6A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E74")

    label("loc_4E6A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E74")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0254
    ChrTalk(
        0xFE,
        (
            "其实我在公演第一天时就已经看过一次了，\x01",
            "但看完之后的那种兴奋感实在是无法消退。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "结果不知不觉\x01",
            "就又买了张票。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_4D96 end

    def Function_36_4F15(): pass

    label("Function_36_4F15")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4FA9")
    Jump("loc_4FF3")

    label("loc_4FA9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FC9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FF3")

    label("loc_4FC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FE9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FF3")

    label("loc_4FE9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FF3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0256
    ChrTalk(
        0xFE,
        "呵呵……果然还是Ｓ区好啊。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "要想完美体验彩虹剧团的表演，\x01",
            "必须要在Ｓ区欣赏才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_4F15 end

    def Function_37_507B(): pass

    label("Function_37_507B")

    TalkBegin(0xFE)
    OP_4B(0x21, 0xFF)

    #C0258
    ChrTalk(
        0xFE,
        (
            "对了，我得先去\x01",
            "上个洗手间。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "不好意思啊，先帮我占下座吧！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x21,
        (
            "哈哈，你在说什么呢。\x01",
            "这里可是预约席啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x21, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_37_507B end

    def Function_38_50FA(): pass

    label("Function_38_50FA")

    TalkBegin(0xFE)

    #C0261
    ChrTalk(
        0xFE,
        (
            "从工作的地方拿到了票，\x01",
            "所以我也意外地能来看演出了。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        "哎呀，我可真是太幸运了！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_50FA end

    def Function_39_5158(): pass

    label("Function_39_5158")

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
            "#5P哦哦，是支援科的诸位……！\x01",
            "来得真是太巧了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#0005F剧团长……怎么了吗？\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xC,
        "#5P实、实际上……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "#5P啊啊，这件事\x01",
            "还希望各位能够保密……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "#5P我们有一个演员，\x01",
            "从早上开始就失踪了。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 3)), scpexpr(EXPR_END)), "loc_53C6")

    #C0268
    ChrTalk(
        0x9,
        (
            "#1806F#5P就是之前曾经提起过的\x01",
            "尼克鲁先生……\x02\x03",

            "#1801F好像从昨天开始，\x01",
            "他就连家都没有回过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542D")

    label("loc_53C6")


    #C0269
    ChrTalk(
        0x9,
        (
            "#1806F#5P是一个名叫尼克鲁，\x01",
            "和我同为新人的团员……\x02\x03",

            "#1801F听说他从昨天开始，\x01",
            "就连家都没有回过呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_542D")


    #C0270
    ChrTalk(
        0x11,
        (
            "#11P他的家人也\x01",
            "分头去寻找了，\x01",
            "但似乎还是没找到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "#5P我们也联络过了\x01",
            "所有能想到的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x103,
        (
            "#0201F……尼克鲁先生最近\x01",
            "有没有什么奇怪的举动呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0273
    ChrTalk(
        0xC,
        "#5P啊，有的，正如你所说。\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "#5P他原来是个非常内向，\x01",
            "总是出错的新演员……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "#5P但是，自从纪念庆典结束之后，\x01",
            "他就突然展现出了惊人的才能。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#0003F………………………………\x02\x03",

            "#0001F所谓的才能，具体是指……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "#5P──卓越的身体能力。\x01",
            "而且，需要热情表现力的表演，\x01",
            "他也可以轻松完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#1706F#5P不过……那简直就像是\x01",
            "被什么东西附了身一样。\x02\x03",

            "#1701F我感觉，那绝对不是\x01",
            "尼克鲁自己的演技。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x9,
        (
            "#1806F#5P嗯，而且\x01",
            "总有种狂热过头的怪异感觉……\x02\x03",

            "#1808F就好像是完全变了一个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        "#0303F……这就可以肯定……了啊。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        (
            "#0108F而且最后还落了个失踪的下场……\x01",
            "真是不容乐观的状况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        (
            "#0003F剧团长，尼克鲁先生的事情，\x01",
            "能交给我们支援科来调查吗？\x02\x03",

            "#0001F或许我们能用自己的方法\x01",
            "把他找到。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        "#5P真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "#5P如果是这样，不用各位开口，\x01",
            "应该是我来拜托各位才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#1702F#5P是啊，要是警察弟弟\x01",
            "能来负责这件事，应该就可以放心了。\x02\x03",

            "#1706F而且我们还得做好\x01",
            "演出的准备工作。\x02",
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
            "#0305F今天的公演……\x01",
            "你们该不会是想照常进行吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x11,
        (
            "#11P嗯，目前正在商量\x01",
            "一些细节方面的问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x11,
        (
            "#11P就算尼克鲁不回来，\x01",
            "我们也不可能放弃演出的。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x11,
        (
            "#11P只能调整一下角色的分配，\x01",
            "再进行表演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xA,
        (
            "#5P因为我们彩虹剧团从来都没有过\x01",
            "放弃舞台演出的先例呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xC,
        (
            "#5P啊，角色、剧本、演出\x01",
            "大概都要进行调整吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        (
            "实在不行的话，还可以推迟公演时间。\x01",
            "总之，无论如何也一定要上演。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x103,
        (
            "#0202F真令人震惊……\x01",
            "该说什么才好呢，真是可怕的执著心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x102,
        (
            "#0109F是、是啊……\x01",
            "只能说……\x01",
            "真不愧是彩虹剧团啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#0004F……我明白了，\x01",
            "大家就专心准备演出吧。\x02\x03",

            "#0001F但是，要时刻注意着\x01",
            "尼克鲁先生有没有回到\x01",
            "后台或观众席。\x02\x03",

            "如果找到他的话，\x01",
            "请立刻联系支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xC,
        "#5P知道了，我们会照做的。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        (
            "#1808F#5P……对不起，如果我多加留意的话，\x01",
            "就不会发生这样的事了……\x02\x03",

            "#1801F尼克鲁先生的事情\x01",
            "就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#0000F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C4E")
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0299
    ChrTalk(
        0x102,
        "#0101F……罗伊德，我们得快点走了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0300
    ChrTalk(
        0x101,
        (
            "#0001F#6P是啊，得赶快去确认\x01",
            "其他市民的情况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C4E")

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

    # Function_39_5158 end

    def Function_40_5CB2(): pass

    label("Function_40_5CB2")

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

    # Function_40_5CB2 end

    def Function_41_5CDF(): pass

    label("Function_41_5CDF")

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

    # Function_41_5CDF end

    def Function_42_5D0C(): pass

    label("Function_42_5D0C")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_5D0C end

    def Function_43_5D23(): pass

    label("Function_43_5D23")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_43_5D23 end

    def Function_44_5D3A(): pass

    label("Function_44_5D3A")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_5D3A end

    def Function_45_5D43(): pass

    label("Function_45_5D43")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_45_5D43 end

    def Function_46_5D4C(): pass

    label("Function_46_5D4C")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_46_5D4C end

    def Function_47_5D55(): pass

    label("Function_47_5D55")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_47_5D55 end

    def Function_48_5D5E(): pass

    label("Function_48_5D5E")

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

    # Function_48_5D5E end

    def Function_49_5D8B(): pass

    label("Function_49_5D8B")

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

    # Function_49_5D8B end

    def Function_50_5DB8(): pass

    label("Function_50_5DB8")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_5DB8 end

    def Function_51_5DCF(): pass

    label("Function_51_5DCF")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_51_5DCF end

    def Function_52_5DE6(): pass

    label("Function_52_5DE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E04")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_52_5DE6")

    label("loc_5E04")

    Return()

    # Function_52_5DE6 end

    def Function_53_5E05(): pass

    label("Function_53_5E05")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E23")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_53_5E05")

    label("loc_5E23")

    Return()

    # Function_53_5E05 end

    def Function_54_5E24(): pass

    label("Function_54_5E24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E42")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_54_5E24")

    label("loc_5E42")

    Return()

    # Function_54_5E24 end

    def Function_55_5E43(): pass

    label("Function_55_5E43")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E61")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_55_5E43")

    label("loc_5E61")

    Return()

    # Function_55_5E43 end

    def Function_56_5E62(): pass

    label("Function_56_5E62")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0x57E40, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_56_5E62 end

    def Function_57_5E9B(): pass

    label("Function_57_5E9B")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0xFFFA81C0, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_57_5E9B end

    def Function_58_5ED4(): pass

    label("Function_58_5ED4")

    Sleep(1500)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_95(0x9, -2110, 1250, 20950, 4500, 0x0)
    BeginChrThread(0x9, 2, 0, 41)

    def lambda_5F08():
        OP_9E(0x9, 0x0, 0x5AB4, 0xFFFEA070, 0x898, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_5F08)
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

    def lambda_5FA9():
        OP_93(0x9, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_5FA9)
    BeginChrThread(0x9, 2, 0, 41)
    OP_9D(0x9, 0xFFFFF9FC, 0x4E2, 0x5E38, 0xBB8, 0x4B0)
    SetChrChipByIndex(0x9, 0x21)
    Sound(50, 0, 100, 0)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    BeginChrThread(0x9, 2, 0, 41)

    def lambda_5FEF():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_5FEF)
    OP_9D(0x9, 0xFFFFF3C6, 0x4E2, 0x62F2, 0x3E8, 0x6A4)
    SetChrChipByIndex(0x9, 0x21)
    Sound(50, 0, 100, 0)
    SetChrSubChip(0x9, 0x2)
    Sleep(1500)

    def lambda_6024():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_6024)
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

    # Function_58_5ED4 end

    def Function_59_610A(): pass

    label("Function_59_610A")

    OP_95(0xFE, -5500, 1250, 24300, 3000, 0x0)
    OP_95(0xFE, -10500, 1250, 25300, 3000, 0x0)
    Return()

    # Function_59_610A end

    def Function_60_6133(): pass

    label("Function_60_6133")

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
        "紫发的女孩",
        "#6206F#5P#100W呼、呼、呼……\x02",
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
    SetChrName("紫发的女孩")

    #A0302
    AnonymousTalk(
        0xFF,
        "#30W太好了，总算是成功了……\x02",
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
        "女性的声音",
        "#2P嗯嗯，真不错。\x02",
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
        "紫发的女孩",
        "#6205F#30W伊莉娅小姐……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("金发的女性")

    #A0305
    AnonymousTalk(
        0xFF,
        (
            "速度和时机都把握得不错。\x02\x03",

            "再有就是要掌握好各节点之间的抑扬变化。\x02\x03",

            "以及，并不该按着音乐来跳，\x01",
            "而是要用舞蹈和演技来支配音乐。\x02\x03",

            "要安静地、圣洁地……\x01",
            "带着『月之姬』特有的威严。\x02",
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
        "紫发的女孩",
        (
            "#6202F#30W好、好的……\x02\x03",

            "#6208F#50W……啊………\x02",
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
        "金发的女性",
        (
            "#1706F无可挑剔……\x01",
            "真想这么评价呢。\x02",
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
        "金发的女性",
        (
            "#1702F#5P说真的，我很惊讶。\x02\x03",

            "因为至今为止，还没有任何一个人\x01",
            "能跟得上我的训练。\x02\x03",

            "#1709F嗯嗯，你真是很努力啊¤\x02",
        )
    )

    CloseMessageWindow()

    #N0309
    NpcTalk(
        0x9,
        "紫发的女孩",
        (
            "#6202F#2P伊莉娅小姐……\x02\x03",

            "#6203F但是我……果然还是很不安。\x02\x03",

            "担心会不会在正式表演时\x01",
            "拖伊莉娅小姐的后腿……\x02",
        )
    )

    CloseMessageWindow()

    #N0310
    NpcTalk(
        0x8,
        "金发的女性",
        (
            "#1704F#5P没关系的，你有作为演员的素质。\x02\x03",

            "#1702F而且，将来\x01",
            "还很有可能超过\x01",
            "我伊莉娅·普拉提耶。\x02\x03",

            "#1709F你就相信我的眼光吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0311
    NpcTalk(
        0x9,
        "紫发的女孩",
        (
            "#6209F#2P……但还、还是一点真实感\x01",
            "都没有呢……\x02\x03",

            "#6202F我怎么可能会\x01",
            "超过伊莉娅小姐呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0312
    NpcTalk(
        0x8,
        "金发的女性",
        (
            "#1702F#5P哼哼，当然了，\x01",
            "我也没打算那么简单就被你超越。\x02\x03",

            "#1704F所以说，越快越好，\x01",
            "请你尽快上升到与我对等的高度吧。\x02\x03",

            "#1701F快点成为，能与我同台竞争，\x01",
            "让我拿出全力来对抗的年轻劲敌吧！\x02",
        )
    )

    CloseMessageWindow()

    #N0313
    NpcTalk(
        0x9,
        "紫发的女孩",
        (
            "#6203F#2P呼……\x01",
            "请别说那种难为人的话了……\x02\x03",

            "#6208F啊啊，我为什么\x01",
            "会在这种地方呢……\x02\x03",

            "现在这个时候，我应该已经离开\x01",
            "克洛斯贝尔市，回到了家乡才对……\x02",
        )
    )

    CloseMessageWindow()

    #N0314
    NpcTalk(
        0x8,
        "金发的女性",
        (
            "#1709F#5P呵呵呵……\x02\x03",

            "来参观我的排练，\x01",
            "又被我抓到，你的好运也就到头啦！\x02\x03",

            "我是绝对不会让你逃掉的哦～\x02",
        )
    )

    CloseMessageWindow()

    #N0315
    NpcTalk(
        0x9,
        "紫发的女孩",
        "#6206F#2P呜呜呜，妈妈～……\x02",
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
        "金发的女性",
        "#1700F#5P哎呀，真的快撑不下去了吗？\x02",
    )

    CloseMessageWindow()

    #N0317
    NpcTalk(
        0x9,
        "紫发的女孩",
        (
            "#6202F#2P不……没关系的。\x02\x03",

            "#6203F并不是那样，只是……\x02\x03",

            "#6208F我对自己的实力不足而感到不安，\x01",
            "另外，也在担心那封信的事……\x02",
        )
    )

    CloseMessageWindow()

    #N0318
    NpcTalk(
        0x8,
        "金发的女性",
        (
            "#1705F#5P信……？\x02\x03",

            "什么信啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #N0319
    NpcTalk(
        0x9,
        "紫发的女孩",
        (
            "#6201F#2P就、就是寄给伊莉娅小姐\x01",
            "你的那封信啊～！\x02\x03",

            "那个叫『银』的人寄来的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0320
    NpcTalk(
        0x8,
        "金发的女性",
        (
            "#1705F#5P啊，你是说那个啊？\x02\x03",

            "#1704F太可笑了，\x01",
            "那只不过是个恶作剧吧？\x02\x03",

            "#1702F要是连那种鸡毛蒜皮的小事都在意，\x01",
            "我还怎么做明星呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0321
    NpcTalk(
        0x9,
        "紫发的女孩",
        "#6208F#2P可、可是……\x02",
    )

    CloseMessageWindow()

    #N0322
    NpcTalk(
        0x8,
        "金发的女性",
        (
            "#1702F#5P你也一样，在这次的演出中正式出道以后，\x01",
            "一定会收到一大堆崇拜者的来信。\x02\x03",

            "其中很可能会有一些奇怪的信，\x01",
            "必须要学会视而不见，不然非累死不可。\x02\x03",

            "#1709F特别是你那么丰满，\x01",
            "一定会迷死男人们的～\x02",
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
        "紫发的女孩",
        (
            "#6201F#2P真、真是的……！\x01",
            "伊莉娅小姐可真是……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)

    #C0324
    ChrTalk(
        0x8,
        (
            "#1705F哈哈……\x01",
            "好像有点兴奋起来了啊。\x02\x03",

            "#1702F让我稍微\x01",
            "揉一揉吧？\x02\x03",

            "#1709F没关系的，不会痛的～！\x02",
        )
    )

    CloseMessageWindow()

    #N0325
    NpcTalk(
        0x9,
        "紫发的女孩",
        "#6206F#2P啊——女神啊～……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, -9000, 1250, 24230, 270)

    #N0326
    NpcTalk(
        0xC,
        "男性的声音",
        "#2P呃——咳咳！\x02",
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

    def lambda_70C1():
        OP_95(0xFE, -1310, 1250, 24690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_70C1)
    Sleep(300)
    Fade(250)

    def lambda_70E3():

        label("loc_70E3")

        TurnDirection(0xFE, 0xC, 300)
        Yield()
        Jump("loc_70E3")

    QueueWorkItem2(0x8, 0, lambda_70E3)

    def lambda_70F5():

        label("loc_70F5")

        TurnDirection(0xFE, 0xC, 300)
        Yield()
        Jump("loc_70F5")

    QueueWorkItem2(0x9, 0, lambda_70F5)
    SetChrChipByIndex(0x8, 0x0)
    Sleep(1000)

    def lambda_710E():
        OP_96(0xFE, 0xFFFFFC18, 0x4E2, 0x5640, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_710E)
    WaitChrThread(0xC, 1)
    TurnDirection(0xC, 0x8, 500)
    Fade(500)
    SetChrChipByIndex(0x9, 0x24)
    OP_0D()

    #N0327
    NpcTalk(
        0x9,
        "紫发的女孩",
        "#6205F#12P剧、剧团长……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x8,
        "#1705F#6P哎呀，你在呀？\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xC,
        "呼，不是什么在不在的问题吧。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "虽然这么晚还在练习，真是辛苦你们了……\x01",
            "不过，在练习的过程中，\x01",
            "不妥当的言行是不是稍微有点多呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        "#1709F#6P这只是在指导演技啦，指导演技。\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    TurnDirection(0x8, 0x9, 500)

    #C0332
    ChrTalk(
        0x8,
        (
            "#1700F#5P──话说回来，莉夏。\x01",
            "今天已经很晚了，\x01",
            "就到我家来睡吧。\x02\x03",

            "不能让你在这种时间，\x01",
            "回到那么危险的地方去啊。\x02",
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
            "#6205F也、也不是什么\x01",
            "危险的地方吧？\x02\x03",

            "#6209F大家都是很温和的好人……\x01",
            "就像亲人一样照顾着\x01",
            "刚搬过去的我。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#1701F#5P那明显就是出于不良企图啦。\x02\x03",

            "#1706F本来就是个血气旺盛的\x01",
            "臭小子们聚集的地区……\x02\x03",

            "到了晚上，看到你这充满魅力的身体，\x01",
            "有可能会无法克制的哦。\x02\x03",

            "#1701F嗯嗯，肯定会不由分说地直接扑上来！\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        "会那么做的人也只有你吧。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xC,
        (
            "……对了，伊莉娅。\x01",
            "有人通过导力通讯联络你。\x02",
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
            "#1705F#6P哎……\x01",
            "难道是她打来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xC,
        "嗯，怎么办呢？\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        "#1709F#6P当然要去接啦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)

    #C0340
    ChrTalk(
        0x8,
        "#1702F#5P抱歉，我稍微离开一下哦。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x9,
        "#6202F啊，好的。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    OP_68(-1480, 3200, 22170, 2000)

    def lambda_7512():

        label("loc_7512")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7512")

    QueueWorkItem2(0xC, 0, lambda_7512)

    def lambda_7524():

        label("loc_7524")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7524")

    QueueWorkItem2(0x9, 0, lambda_7524)
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
            "#11P呼……\x01",
            "还是和以前一模一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xC,
        (
            "#11P我本来还以为，她会因为\x01",
            "那封信而产生一点动摇呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x9,
        (
            "#6202F#11P呵呵……\x01",
            "这才是伊莉娅小姐啊。\x02\x03",

            "#6204F无论在什么时候，她都像金色的\x01",
            "太阳一样，绽放着耀眼夺目的光芒……\x02\x03",

            "#6208F──但是，也正因如此，\x01",
            "她周围的人才更需要替她注意……\x02",
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

    # Function_60_6133 end

    def Function_61_7690(): pass

    label("Function_61_7690")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76DA")
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_61_7690")

    label("loc_76DA")

    Return()

    # Function_61_7690 end

    def Function_62_76DB(): pass

    label("Function_62_76DB")

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

    def lambda_7741():
        OP_9E(0x8, 0x0, 0x5DC0, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7741)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)

    def lambda_778F():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_778F)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x0)

    def lambda_77D4():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_77D4)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)

    def lambda_77EA():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_77EA)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    Sound(854, 0, 80, 0)
    Sound(50, 0, 100, 0)
    EndChrThread(0x8, 0x0)

    def lambda_782F():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_782F)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 52)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    Sound(814, 0, 80, 0)
    Sound(50, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 40)
    Sleep(100)

    def lambda_7877():
        OP_9E(0x8, 0x0, 0x636A, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7877)
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

    def lambda_78F2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_78F2)
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

    # Function_62_76DB end

    def Function_63_798E(): pass

    label("Function_63_798E")

    OP_95(0x9, 1300, 0, 15400, 1000, 0x0)

    def lambda_79A7():

        label("loc_79A7")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_79A7")

    QueueWorkItem2(0x9, 0, lambda_79A7)
    Return()

    # Function_63_798E end

    def Function_64_79B5(): pass

    label("Function_64_79B5")

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

    def lambda_7B0F():
        OP_95(0xFE, 650, 2700, 530, 1400, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7B0F)

    def lambda_7B29():
        OP_95(0xFE, -520, 2700, 410, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7B29)

    def lambda_7B43():
        OP_95(0xFE, 570, 2700, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7B43)

    def lambda_7B5D():
        OP_95(0xFE, -600, 2700, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7B5D)
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
        "#0005F#11P（哎……）\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x103,
        "#0205F#11P（这、这是……）\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        "#0105F#11P（……好厉害………）\x02",
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

    def lambda_7D2F():

        label("loc_7D2F")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_7D2F")

    QueueWorkItem2(0xC, 0, lambda_7D2F)

    def lambda_7D41():
        OP_96(0xFE, 0xFFFFF632, 0x0, 0x3714, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7D41)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0348
    ChrTalk(
        0x8,
        "#6105F哎呀……？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)

    def lambda_7D9E():
        OP_95(0xFE, 0, 1250, 18500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7D9E)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_68(60, 1500, 15290, 0)
    MoveCamera(63, 24, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(16000, 0)

    def lambda_7DF5():

        label("loc_7DF5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7DF5")

    QueueWorkItem2(0x101, 0, lambda_7DF5)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_7E18():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E18)
    Sleep(100)

    def lambda_7E30():
        OP_9B(0x1, 0xFE, 0x0, 0xD48, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E30)
    Sleep(50)

    def lambda_7E48():
        OP_9B(0x1, 0xFE, 0x0, 0xF3C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7E48)
    Sleep(80)

    def lambda_7E60():
        OP_9B(0x1, 0xFE, 0x0, 0xED8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E60)
    Sleep(1000)

    #C0349
    ChrTalk(
        0x9,
        "#1809F#5P啊，大家好。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        (
            "#0006F对、对不起，\x01",
            "打扰到你们了……\x02\x03",

            "#0002F那个……\x01",
            "该、该怎么说好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        (
            "#0206F……那、那个………\x02\x03",

            "#0201F好、好厉害呢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        (
            "#0302F哈哈……\x01",
            "让我看得都快丢了魂呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x102,
        (
            "#0104F……有幸欣赏到了\x01",
            "很精彩的表演。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x8,
        "#6109F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_68(-730, 1650, 13990, 2000)
    MoveCamera(47, 29, 0, 2000)
    OP_6E(730, 2000)
    SetCameraDistance(11500, 2000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sound(814, 0, 60, 0)

    def lambda_7FC3():
        OP_9D(0xFE, 0x0, 0x0, 0x3E80, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7FC3)
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
            "#6106F#5P不过，离臻于完美的状态\x01",
            "还差得远呢。\x02",
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
        "#0011F#6P哎！？\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        "#0205F#12P还、还要再提高完成度吗……？\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#6100F#5P那是当然了。\x02\x03",

            "#6104F这一场只不过是演出刚开始，\x01",
            "只有『太阳之姬』登场的剧目而已。\x02\x03",

            "如果再加入『月之姬』的表演，\x01",
            "将会产生好几倍的加乘效果……\x02\x03",

            "#6102F我觉得，最后的高潮部分\x01",
            "将会比刚才那场表演精彩好几十倍吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        "#0013F#6P（咽口水）……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x104,
        "#0301F#12P好、好厉害……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x102,
        "#0106F#12P无、无法想象……\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#6104F#5P呵呵……\x02\x03",

            "#6100F──莉夏。\x01",
            "他们就是你刚才提到过的……？\x02",
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
            "#1802F#11P是的，\x01",
            "是特别任务支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x8,
        (
            "#6100F#5P嗯，的确，\x01",
            "看上去完全不像是警察呢。\x02\x03",

            "#6106F不过，你们也需要做些\x01",
            "调查取证之类的事情吧？\x02\x03",

            "我可不想为了一个无聊的恶作剧\x01",
            "而花费那么多的时间和精力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xC,
        "#6P好啦好啦，伊莉娅。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xC,
        (
            "#6P大家都很担心你啊。\x01",
            "就稍微配合一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#6103F#5P嗯……就算你这么说。\x02\x03",

            "我的原则是不会在演出之前参与任何\x01",
            "会使自己心情变差的事情～\x02\x03",

            "#6102F要是莉夏肯让我揉揉胸的话，\x01",
            "我还是可以稍微考虑一下的～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0368
    ChrTalk(
        0x9,
        "#1801F#11P才、才不让你揉呢。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xC,
        "#6P唉，你可真是的……\x02",
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
            "#0012F#6P（和、和在舞台上的仪态\x01",
            "  可真是完全不同啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        "#0211F#12P（稍微有点怪叔叔的感觉呢……）\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#0106F#12P（嗯……\x01",
            "  虽然早就知道她是个女中豪杰……）\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x104,
        "#0302F#12P（哎呀～真是个性格鲜明的人啊。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    #C0374
    ChrTalk(
        0x9,
        (
            "#1806F#5P各、各位，真对不起。\x02\x03",

            "#1801F我一定会说服她的。\x01",
            "罗伊德警官还有各位，请你们先在休息室里稍微……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8641():

        label("loc_8641")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8641")

    QueueWorkItem2(0x8, 0, lambda_8641)

    #C0375
    ChrTalk(
        0x8,
        "#6105F#5P嗯……？\x02",
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
        "#0005F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x9,
        "#1805F#5P伊莉娅小姐……？\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x8,
        (
            "#6101F#5P『罗伊德』──\x01",
            "莉夏刚才是这么叫的吧？\x02\x03",

            "莫非指的就是你吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#0011F#6P啊，是的……是我。\x01",
            "（好近啊，离得太近了……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        "#6100F#5P全名是？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#0000F#6P那个……\x01",
            "罗伊德·班宁斯。\x02",
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
        "#6109F#5P#4S啊哈哈，果然！\x02",
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
        "#0105F哎！？\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        "#0301F#11P喂喂喂喂喂……！\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x9,
        "#1801F#5P伊、伊莉娅小姐……！？\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xC,
        "#12P这、这到底是怎么了！？\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x8,
        (
            "#6109F哎呀～这世界可真是太小啦！\x02\x03",

            "没想到能见到久闻大名的\x01",
            "那个弟弟啊！\x02\x03",

            "#6102F这么一说，我之前好像是\x01",
            "听说过你当上警察了……\x02\x03",

            "呵呵，外表和气质还真是\x01",
            "与某人形容的一模一样啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        (
            "#0011F#11P那、那个……莫非。\x02\x03",

            "伊莉娅小姐……\x01",
            "认识塞茜尔姐姐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "#6104F塞茜尔是我的好朋友。\x02\x03",

            "从在主日学校上课时算起，\x01",
            "都已经有十年以上的交情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        "#0012F#11P原、原来如此……\x02",
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
            "呵呵……\x01",
            "正式做一次自我介绍吧。\x02\x03",

            "伊莉娅·普拉提耶──\x01",
            "算是彩虹剧团\x01",
            "的招牌女演员吧。\x02\x03",

            "请多关照啦，警察弟弟还有大家！\x02",
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

    # Function_64_79B5 end

    def Function_65_8C7C(): pass

    label("Function_65_8C7C")

    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 0, 0, 61)
    BeginChrThread(0x9, 2, 0, 49)

    def lambda_8C97():
        OP_9D(0x9, 0xFA, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8C97)
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

    def lambda_8D0F():
        OP_9E(0x9, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8D0F)
    Sleep(33)

    def lambda_8D2D():

        label("loc_8D2D")

        TurnDirection(0x9, 0x8, 0)
        Yield()
        Jump("loc_8D2D")

    QueueWorkItem2(0x9, 3, lambda_8D2D)
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

    def lambda_8DD7():

        label("loc_8DD7")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_8DD7")

    QueueWorkItem2(0x9, 3, lambda_8DD7)
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

    def lambda_8E76():
        OP_9D(0x9, 0xF28, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E76)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 51)
    BeginChrThread(0x9, 3, 0, 54)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x0)

    def lambda_8EAA():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_8EAA)
    Return()

    # Function_65_8C7C end

    def Function_66_8EB3(): pass

    label("Function_66_8EB3")

    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 0, 0, 61)
    BeginChrThread(0x8, 2, 0, 41)

    def lambda_8ECE():
        OP_9D(0x8, 0xFFFFFF06, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8ECE)
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

    def lambda_8F4C():
        OP_9E(0x8, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8F4C)
    Sleep(33)

    def lambda_8F6A():

        label("loc_8F6A")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_8F6A")

    QueueWorkItem2(0x8, 3, lambda_8F6A)
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

    def lambda_902B():

        label("loc_902B")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_902B")

    QueueWorkItem2(0x8, 3, lambda_902B)
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

    def lambda_90E1():
        OP_9D(0x8, 0xFFFFF0D8, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_90E1)
    Sleep(1000)
    BeginChrThread(0x8, 2, 0, 43)
    BeginChrThread(0x8, 3, 0, 52)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)

    def lambda_9115():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_9115)
    Sleep(700)
    Return()

    # Function_66_8EB3 end

    def Function_67_9121(): pass

    label("Function_67_9121")

    OP_9B(0x1, 0xFE, 0x0, 0x1324, 0x7D0, 0x1)
    OP_95(0xFE, -1550, 0, 14280, 2000, 0x0)
    OP_93(0xFE, 0x168, 0x0)
    Return()

    # Function_67_9121 end

    def Function_68_914C(): pass

    label("Function_68_914C")

    OP_9B(0x1, 0xFE, 0x0, 0x12C0, 0x7D0, 0x1)
    OP_95(0xFE, 1550, 0, 14280, 2000, 0x0)
    OP_93(0xFE, 0x168, 0x0)
    Return()

    # Function_68_914C end

    def Function_69_9177(): pass

    label("Function_69_9177")

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

    def lambda_9397():
        OP_95(0xFE, 650, 2700, 530, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9397)

    def lambda_93B1():
        OP_95(0xFE, -520, 2700, 410, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_93B1)

    def lambda_93CB():
        OP_95(0xFE, 570, 2700, -900, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_93CB)

    def lambda_93E5():
        OP_95(0xFE, -600, 2700, -900, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_93E5)
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
        "#0105F#11P啊……\x02",
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
        "#6104F#40W呼……\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        "#6206F#40W哈……\x02",
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
        "#6105F#5P哎呀……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x9,
        "#6202F#11P各位……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x9, 0x20)

    def lambda_96AA():
        OP_96(0x8, 0xFFFFFB64, 0x4E2, 0x4948, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_96AA)
    Sleep(200)

    def lambda_96C7():
        OP_96(0x9, 0x4BA, 0x4E2, 0x4948, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_96C7)

    #C0400
    ChrTalk(
        0x104,
        "#0309F#12P#N呜哦哦哦，太棒了！！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0401
    ChrTalk(
        0x101,
        "#0002F#6P#N太、太棒了……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0402
    ChrTalk(
        0x103,
        "#0204F#6P#N……令人感动……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(300)

    #C0403
    ChrTalk(
        0x8,
        (
            "#6104F#5P呵呵，就这样继续练习下去的话，\x01",
            "这一幕应该会十分精彩。\x02\x03",

            "#6100F莉夏，这里虽然是月之姬表演的场面，\x01",
            "但表演还是要再收敛一点。\x02\x03",

            "太阳之姬也会加以配合，\x01",
            "随后再出其不意，两人一起展现演技。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    #C0404
    ChrTalk(
        0x9,
        "#6200F#11P好的……！\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x102,
        (
            "#0104F#12P#N好厉害呢……\x02\x03",

            "#0102F为了创造出一个精彩的舞台……\x01",
            "竟然一丝不苟到如此地步……\x02",
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
            "#6109F#5P呼，好不容易找到感觉了，\x01",
            "自然应该顺着这种感觉继续练下去啊。\x02\x03",

            "#6100F比起这个……\x01",
            "怎么了，是有了什么进展吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(150)

    #C0407
    ChrTalk(
        0x9,
        "#6205F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x102,
        "#0108F#12P#N……是的。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0409
    ChrTalk(
        0x101,
        (
            "#0006F#6P#N必须要向各位\x01",
            "做出一个令人遗憾的报告……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0410
    ChrTalk(
        0x9,
        "#6201F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "#6103F#5P嗯……好的。\x02\x03",

            "#6100F我把剧团长也叫来，\x01",
            "就在这里说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    OP_93(0x8, 0x13B, 0x190)

    def lambda_99F6():
        OP_95(0xFE, -6050, 1250, 24120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_99F6)
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
            "#5P『银』……\x01",
            "没想到会是那么危险的家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x9,
        (
            "#6205F怎、怎么会……\x02\x03",

            "#6201F那种可怕的人真的在这座城市中……？\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x8,
        (
            "#6105F嘿，这不是挺有趣的吗。\x02\x03",

            "#6102F在东方人街被颂为传说，\x01",
            "有如影子般的不死杀手……\x02\x03",

            "#6109F嗯，真不错呀～！\x01",
            "是个很适合被搬上舞台的角色呢！\x02\x03",

            "#6102F对了！\x01",
            "在第三幕的巫女装表演中，\x01",
            "是不是可以套用一下那种感觉！？\x02",
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

    def lambda_9CA7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_9CA7)
    Sleep(50)
    TurnDirection(0xC, 0x8, 500)
    Sleep(300)

    #C0415
    ChrTalk(
        0xC,
        "#6P呃，伊莉娅……\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x9,
        (
            "#6206F#12P现在可不是悠闲地研究\x01",
            "那些的场合啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x102,
        (
            "#0103F#12P……有证据表明，\x01",
            "那个叫『黑月』的势力确实 \x01",
            "雇佣了叫做『银』的罪犯。\x02\x03",

            "#0108F但是，至于『银』为何要\x01",
            "向伊莉娅小姐寄恐吓信，\x01",
            "我们目前还没有查明……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        (
            "#0001F#6P总之，恶作剧的可能性\x01",
            "似乎已经很低了。\x02\x03",

            "那个，如果先把公演中止──\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x8,
        (
            "#6104F那是不可能的。\x02\x03",

            "就算有人寄来恐吓信说要炸掉剧院，\x01",
            "我们也不会放弃表演的。\x02\x03",

            "#6100F对吧，剧团长？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(150)

    #C0420
    ChrTalk(
        0xC,
        "嗯……确实可以这么说。\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xC,
        (
            "虽然还没到伊莉娅的那种程度，\x01",
            "但我们剧团里的人，多少也都属于那种\x01",
            "被名为『舞台』的魔物所魅惑的人群。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xC,
        (
            "在我们剧团的演员里，\x01",
            "恐怕没有一个人\x01",
            "会选择放弃表演吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(150)

    #C0423
    ChrTalk(
        0x9,
        (
            "#6206F那、那个……\x01",
            "我虽然只是个新人，不过也有同感。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x104,
        (
            "#0306F#12P哎呀呀……\x01",
            "都是些愿意为表演而献身的伟大艺术家吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x103,
        (
            "#0200F#12P也就是说，让其它部门的人员\x01",
            "接手警卫工作也没问题吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x8,
        (
            "#6103F呼，说实话，那虽然确实很烦人，\x01",
            "但如今也是没办法的事。\x02\x03",

            "#6100F是叫搜查一科吧……\x01",
            "负责人是个什么样的人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x101,
        (
            "#0011F#6P呃，这个……\x02\x03",

            "#0012F一眼看上去就会感觉他很能干，\x01",
            "散发着精英的气质……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#0103F#12P我认为，他实际上也相当优秀。\x02\x03",

            "#0100F因为搜查一科这个部门在警察局中，\x01",
            "也是个名副其实的精英集团。\x02\x03",

            "应该能以毫不显眼的形式\x01",
            "完美地做好警卫工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#6106F呼……真是不想和他们打交道啊。\x02\x03",

            "#6101F不过，到时候剧场里也会有客人来，\x01",
            "为了他们的安全，也只能忍忍了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 500)
    Sleep(150)

    #C0430
    ChrTalk(
        0xC,
        "#6P嗯，就忍耐一下吧。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xC,
        (
            "#6P这也没什么大不了的。\x01",
            "你只要站在舞台上，集中精神演出，\x01",
            "自然就会对其它东西视而不见了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 500)
    Sleep(150)

    #C0432
    ChrTalk(
        0x8,
        (
            "#6101F真失礼啊，我在表演时会一直注意着观众呢。\x02\x03",

            "#6104F所谓的演出，必须要由演员与观众们产生共鸣，\x01",
            "才能算真正意义上的完成……\x02\x03",

            "#6100F剧团长不是总这样说吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xC,
        (
            "#6P嗯，但我觉得\x01",
            "你并不是这种会这么想的类型啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xC,
        (
            "#6P比起共鸣，你应该会强硬地\x01",
            "把观众卷入到自己的节奏中。\x02",
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
        "#0012F#6P（该、该怎么说才好呢……）\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x103,
        (
            "#0202F#12P（这些人全都是\x01",
            "  为表演痴狂的人啊……）\x02",
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
            "#6201F那、那个，罗伊德警官……\x02\x03",

            "从现在开始，你们就\x01",
            "不负责调查的事了……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    def lambda_A4A6():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A4A6)
    Sleep(50)

    def lambda_A4B6():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A4B6)
    Sleep(50)

    def lambda_A4C6():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A4C6)
    Sleep(50)

    def lambda_A4D6():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A4D6)
    Sleep(50)
    TurnDirection(0xC, 0x101, 500)
    Sleep(100)

    #C0438
    ChrTalk(
        0x101,
        (
            "#0006F#6P是的……十分抱歉。\x02\x03",

            "#0000F不过，之后会由一科继续负责，\x01",
            "我想也没什么好担心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x9,
        "#6206F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x8,
        (
            "#6100F哎，不能让警察弟弟来负责，\x01",
            "稍微有点遗憾啊……\x02\x03",

            "非常感谢你们做了这么多的调查。\x02\x03",

            "#6109F作为回礼，会送给你们门票的。\x01",
            "人人有份，不过也只能等到高峰期过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xC,
        (
            "嗯，是啊。\x01",
            "纪念庆典期间的票实在是无能为力了……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xC,
        (
            "如果不介意票是下个月的，\x01",
            "就送给大家当礼物吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 500)

    def lambda_A67B():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A67B)
    Sleep(50)

    def lambda_A68B():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A68B)
    Sleep(50)

    def lambda_A69B():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A69B)
    Sleep(50)

    def lambda_A6AB():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A6AB)
    TurnDirection(0x9, 0xC, 500)
    Sleep(100)

    #C0443
    ChrTalk(
        0x104,
        (
            "#0305F#11P真、真的吗！？\x02\x03",

            "#0309F哎呀～原本还以为要等到下下个月呢，\x01",
            "这就已经是意外之喜了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        "#0202F#11P……您真慷慨。\x02",
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
        "#0001F#6P（艾莉……？）\x02",
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

    # Function_69_9177 end

    SaveToFile()

Try(main)
