from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1110.bin",                # FileName
        "c1110",                    # MapName
        "c1110",                    # Location
        0x0017,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 23, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1110",                  # 0
        "接待小姐希恩",           # 1
        "库利普主任",             # 2
        "阿奈斯特秘书",           # 3
        "麦克道尔市长",           # 4
        "弗兰茨巡警",             # 5
        "市政府职员",             # 6
        "市政府职员",             # 7
        "市政府职员",             # 8
        "雷因兹",                 # 9
        "格蕾丝",                 # 10
        "紫发的女孩",             # 11
        "运输公司员工",           # 12
        "运输公司员工",           # 13
        "哈尔特曼议长",           # 14
        "议员",                   # 15
        "议员",                   # 16
    ))

    AddCharChip((
        "chr/ch34600.itc",                   # 00
        "chr/ch28000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch02300.itc",                   # 03
        "chr/ch05802.itc",                   # 04
        "chr/ch30000.itc",                   # 05
        "chr/ch28100.itc",                   # 06
        "chr/ch28200.itc",                   # 07
        "chr/ch27600.itc",                   # 08
        "chr/ch06000.itc",                   # 09
        "chr/ch05200.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
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

    DeclNpc(0,       0,       7400,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3529,    4000,    16209,   315,  261,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-44990,  250,     14710,   180,  469,  0x0, 0,   4,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-13510,  4000,    14529,   135,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-4429,   0,       4460,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       7400,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       7400,    180,  389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2670,    0,       -1090,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1730,    0,       5389,    315,  389,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       5159,    360,  389,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 18,  0.0,                   3.5,                   0.0,                   517.5625,              [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3076923191547394,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -1.076923131942749,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 19,  -6.400000095367432,    16.75,                 4.0,                   3136.0,                [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.4571428894996643,    -2.09375,              -0.800000011920929,    1.0])

    DeclActor(0,       0,       6000,    1500,    0,       1500,    7460,    0x007E, 0,  5,  0x0000)
    DeclActor(-44940,  0,       13190,   1500,    -44990,  1500,    14710,   0x007E, 0,  9,  0x0000)
    DeclActor(-8100,   4000,    19780,   1500,    -8100,   5500,    19780,   0x007C, 0,  36, 0x0000)
    DeclActor(8000,    4120,    19640,   1500,    8000,    5520,    19640,   0x007C, 0,  37, 0x0000)

    ScpFunction((
        "Function_0_4B4",          # 00, 0
        "Function_1_56C",          # 01, 1
        "Function_2_597",          # 02, 2
        "Function_3_5C2",          # 03, 3
        "Function_4_8E1",          # 04, 4
        "Function_5_AE4",          # 05, 5
        "Function_6_AE8",          # 06, 6
        "Function_7_279D",         # 07, 7
        "Function_8_3C98",         # 08, 8
        "Function_9_3F45",         # 09, 9
        "Function_10_3F49",        # 0A, 10
        "Function_11_4F4F",        # 0B, 11
        "Function_12_4FD0",        # 0C, 12
        "Function_13_5241",        # 0D, 13
        "Function_14_52B5",        # 0E, 14
        "Function_15_530F",        # 0F, 15
        "Function_16_540F",        # 10, 16
        "Function_17_5755",        # 11, 17
        "Function_18_729B",        # 12, 18
        "Function_19_7C51",        # 13, 19
        "Function_20_84B5",        # 14, 20
        "Function_21_8516",        # 15, 21
        "Function_22_85CC",        # 16, 22
        "Function_23_864F",        # 17, 23
        "Function_24_9351",        # 18, 24
        "Function_25_985D",        # 19, 25
        "Function_26_9D75",        # 1A, 26
        "Function_27_A42C",        # 1B, 27
        "Function_28_A659",        # 1C, 28
        "Function_29_ABEA",        # 1D, 29
        "Function_30_B1B6",        # 1E, 30
        "Function_31_C3DD",        # 1F, 31
        "Function_32_C41C",        # 20, 32
        "Function_33_D241",        # 21, 33
        "Function_34_D264",        # 22, 34
        "Function_35_D28D",        # 23, 35
        "Function_36_D306",        # 24, 36
        "Function_37_D51F",        # 25, 37
    ))


    def Function_0_4B4(): pass

    label("Function_0_4B4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4F4"),
        (1, "loc_500"),
        (2, "loc_50C"),
        (3, "loc_518"),
        (4, "loc_524"),
        (5, "loc_530"),
        (6, "loc_53C"),
        (SWITCH_DEFAULT, "loc_548"),
    )


    label("loc_4F4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_500")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_50C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_518")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_524")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_530")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_53C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_548")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_554")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_554")

    label("loc_56B")

    Return()

    # Function_0_4B4 end

    def Function_1_56C(): pass

    label("Function_1_56C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_596")
    OP_94(0xFE, 0x193C, 0x3B1A, 0x672, 0x41BE, 0x3E8)
    Sleep(300)
    Jump("Function_1_56C")

    label("loc_596")

    Return()

    # Function_1_56C end

    def Function_2_597(): pass

    label("Function_2_597")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C1")
    OP_94(0xFE, 0xFFFFEB74, 0x37FA, 0xFFFFF5F6, 0x43EE, 0x3E8)
    Sleep(300)
    Jump("Function_2_597")

    label("loc_5C1")

    Return()

    # Function_2_597 end

    def Function_3_5C2(): pass

    label("Function_3_5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5EC")
    SetChrPos(0x9, -46210, 0, 12030, 0)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_611")
    SetChrPos(0x9, -40440, 0, 11040, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_8B6")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_61F")
    Jump("loc_8B6")

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_632")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_8B6")

    label("loc_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_645")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_68C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, -1820, 4000, 17030, 225)
    SetChrPos(0xD, -3170, 4000, 16140, 45)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_6F7")

    label("loc_68C")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 3830, 4000, 18150, 0)
    SetChrPos(0xD, -5310, 4000, 15540, 225)
    SetChrPos(0xE, -6700, 4000, 14240, 45)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_6F7")
    SetChrPos(0x9, 4870, 4000, 17950, 180)

    label("loc_6F7")

    Jump("loc_8B6")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_721")
    SetChrPos(0x9, -40440, 0, 11040, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_8B6")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_74B")
    SetChrPos(0x9, -40440, 0, 11040, 90)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7B0")
    SetChrPos(0xF, -5160, 4000, 16030, 90)
    SetChrPos(0x9, -3740, 4000, 16030, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -6520, 4000, 15440, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7DA")
    SetChrPos(0x9, -46210, 0, 12030, 0)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8B6")

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_815")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -5160, 4000, 16030, 90)
    SetChrPos(0x9, -3740, 4000, 16030, 270)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_8B6")

    label("loc_815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_823")
    Jump("loc_8B6")

    label("loc_823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_842")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    TurnDirection(0x8, 0x11, 0)
    Jump("loc_8B6")

    label("loc_842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_850")
    Jump("loc_8B6")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_85E")
    Jump("loc_8B6")

    label("loc_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_86C")
    Jump("loc_8B6")

    label("loc_86C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_87A")
    Jump("loc_8B6")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_89F")
    SetChrPos(0x9, -4070, 4000, 16180, 180)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_8B6")

    label("loc_89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8AD")
    Jump("loc_8B6")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8B6")

    label("loc_8B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1")
    ClearChrFlags(0x12, 0x80)
    Event(0, 25)

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_8E0")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 32)

    label("loc_8E0")

    Return()

    # Function_3_5C2 end

    def Function_4_8E1(): pass

    label("Function_4_8E1")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_8F3")
    Jump("loc_8FC")

    label("loc_8F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8FC")

    label("loc_8FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_90E")
    OP_66(0x1, 0x1)
    Jump("loc_96D")

    label("loc_90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_91C")
    Jump("loc_96D")

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_92E")
    OP_66(0x1, 0x1)
    Jump("loc_96D")

    label("loc_92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_93C")
    Jump("loc_96D")

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_94E")
    OP_66(0x1, 0x1)
    Jump("loc_96D")

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_960")
    OP_66(0x1, 0x1)
    Jump("loc_96D")

    label("loc_960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_96D")
    OP_66(0x1, 0x1)

    label("loc_96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_997")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_997")
    SetMapObjFrame(0xFF, "model06", 0x0, 0x1)

    label("loc_997")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B0")
    OP_10(0x0, 0x0)
    OP_10(0x6, 0x1)
    Jump("loc_9B6")

    label("loc_9B0")

    OP_10(0x0, 0x1)
    OP_10(0x6, 0x0)

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_9E9")

    label("loc_9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9E9")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_9E9")

    label("loc_9E9")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A05")
    OP_1B(0x2, 0x0, 0x23)

    label("loc_A05")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A28")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_A28")

    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    ClearMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A4C")
    SetMapObjFlags(0x3, 0x4)

    label("loc_A4C")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A64")
    Jump("loc_AE3")

    label("loc_A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_AE3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A7E")
    Jump("loc_AE3")

    label("loc_A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 7)), scpexpr(EXPR_END)), "loc_A91")
    OP_1B(0x1, 0x0, 0x17)
    Jump("loc_AE3")

    label("loc_A91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB0")
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_AE3")

    label("loc_AB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_ACB")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Jump("loc_AE3")

    label("loc_ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 6)), scpexpr(EXPR_END)), "loc_AE3")
    ModifyEventFlags(1, 0, 0x80)
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_AE3")

    Return()

    # Function_4_8E1 end

    def Function_5_AE4(): pass

    label("Function_5_AE4")

    Call(0, 6)
    Return()

    # Function_5_AE4 end

    def Function_6_AE8(): pass

    label("Function_6_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFE")
    Call(0, 24)
    Jump("loc_279C")

    label("loc_AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B44")
    OP_4B(0x8, 0xFF)
    TurnDirection(0x0, 0x8, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3C")
    Call(0, 26)
    Jump("loc_B3F")

    label("loc_B3C")

    Call(0, 27)

    label("loc_B3F")

    Jump("loc_279C")

    label("loc_B44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B84")
    OP_4B(0x8, 0xFF)
    TurnDirection(0x0, 0x8, 0)
    Call(0, 29)
    Jump("loc_279C")

    label("loc_B84")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAC")

    #C0001
    ChrTalk(
        0x8,
        (
            "今天实在是\x01",
            "太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "特别任务支援科……吗，\x01",
            "据说是为了向市民提供服务\x01",
            "而设立的部门……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "不过，连我们都沾光受助了，\x01",
            "真是十分感谢啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0009F哈哈哈……\x01",
            "（被这么称赞，还真是不好意思啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#0100F如果以后再有什么事情，\x01",
            "请不用客气，随时提出委托哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D3E")

    label("loc_CAC")


    #C0006
    ChrTalk(
        0x8,
        (
            "今天实在是\x01",
            "太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "特别任务支援科……吗，\x01",
            "据说是为了向市民提供服务\x01",
            "而设立的部门……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "不过，连我们都沾光受助了，\x01",
            "真是十分感谢啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3E")

    Jump("loc_2799")

    label("loc_D43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD2")

    #C0009
    ChrTalk(
        0x8,
        (
            "三处空房都确认完毕之后，\x01",
            "就请来通知我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "文件的内容也许会有\x01",
            "一些遗漏或错误之处，\x01",
            "还请多加注意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2799")

    label("loc_DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC5")

    #C0011
    ChrTalk(
        0x8,
        (
            "自治州议会在不久前\x01",
            "总算结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "这样一来，财务科的各位\x01",
            "也就可以安心回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "不过……市长今天似乎也像往常一样，\x01",
            "准备一直加班到深夜。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "好像是急着把预算方面的文件整理完……\x01",
            "真希望他不要太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F2B")

    label("loc_EC5")


    #C0015
    ChrTalk(
        0x8,
        (
            "市长今天似乎也像往日一样，\x01",
            "准备一直加班到深夜。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "他真是位一丝不苟的人……\x01",
            "好担心他的身体呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2B")

    Jump("loc_2799")

    label("loc_F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1117")

    #C0017
    ChrTalk(
        0x8,
        (
            "从今天早上开始，就不断有人来询问\x01",
            "空港被封锁的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "真是麻烦啊，因为警察局的人\x01",
            "说过要暂时保密，稳定事态，\x01",
            "所以我只能敷衍说是要临时进行设备检查……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "这种理由到底能撑到什么时候呢……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A6")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        "#0005F（空港那边似乎是发生了什么事啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_110F")

    label("loc_10A6")


    #C0021
    ChrTalk(
        0x103,
        (
            "#0203F（对外公布的官方消息\x01",
            "  好像是『对设备进行临时检查』。）\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0001F（市政府这边也很难办呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_110F")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1180")

    label("loc_1117")


    #C0023
    ChrTalk(
        0x8,
        (
            "从今天早上开始，就不断有人来询问\x01",
            "空港被封锁的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "唉，这种敷衍的理由到底能撑到什么时候呢……\x02",
    )

    CloseMessageWindow()

    label("loc_1180")

    Jump("loc_2799")

    label("loc_1185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_136B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FA")

    #C0025
    ChrTalk(
        0x8,
        (
            "自治州议会今天好像也\x01",
            "纠纷不断呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "呼……议员先生们那种难看的样子，\x01",
            "无论如何也不能被市民们看到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "大家的态度都十分恶劣，\x01",
            "互相谩骂的场面此起彼伏。\x02",
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

    #C0028
    ChrTalk(
        0x104,
        "#0303F（……那种场面，确实是不想看见啊。）\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#0108F（这就是议会的现实啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1366")

    label("loc_12FA")


    #C0030
    ChrTalk(
        0x8,
        (
            "自治州议会今天好像也\x01",
            "纠纷不断呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "呼……议员先生们那种难看的样子，\x01",
            "无论如何也不能被市民们看到啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1366")

    Jump("loc_2799")

    label("loc_136B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1535")

    #C0032
    ChrTalk(
        0x8,
        (
            "这里是克洛斯贝尔\x01",
            "市政厅的接待处……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13E8")

    #C0033
    ChrTalk(
        0x8,
        "啊，是各位啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_140A")

    label("loc_13E8")


    #C0034
    ChrTalk(
        0x8,
        "啊，各位是……警察局的人吧。\x02",
    )

    CloseMessageWindow()

    label("loc_140A")


    #C0035
    ChrTalk(
        0x8,
        (
            "呼，我还以为是来\x01",
            "抱怨的市民呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#0105F来抱怨的市民？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "嗯，按照计划安排，预算会议\x01",
            "本来是应该截止到昨天就结束的……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "但和往年一样，辩论过程中纠纷不断，\x01",
            "直到现在，还在对预算问题争执不休。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "会期大概又要\x01",
            "延长好几天了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#0106F（唉……自治州议会\x01",
            "  也还是老样子呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1594")

    label("loc_1535")


    #C0041
    ChrTalk(
        0x8,
        (
            "今年的议会也要延长会期……\x01",
            "所以预算计划的执行也会随之推迟。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "给市民们带来了不少麻烦。\x02",
    )

    CloseMessageWindow()

    label("loc_1594")

    Jump("loc_2799")

    label("loc_1599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_180D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15F5")

    #C0043
    ChrTalk(
        0x8,
        (
            "各位……\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "请容我代表市政厅，\x01",
            "向各位表示谢意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1808")

    label("loc_15F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1670")

    #C0045
    ChrTalk(
        0x8,
        (
            "已经把市长喜欢的饮料\x01",
            "买回来了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "我想他一定会很高兴的。\x01",
            "那就请各位直接\x01",
            "去交给市长吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1808")

    label("loc_1670")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_16FB")

    #C0047
    ChrTalk(
        0x8,
        (
            "果汁店\x01",
            "搬地方了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "抱歉，我也不知道\x01",
            "搬到了什么地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "但我觉得，应该还在市内的\x01",
            "某个地方正常营业吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1808")

    label("loc_16FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_17A8")

    #C0050
    ChrTalk(
        0x8,
        (
            "市长喜欢的饮料，\x01",
            "可以在喷泉广场的\x01",
            "果汁店买到。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "但一般不公开对外出售，\x01",
            "算是特别饮料哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "虽然有些麻烦，但还是拜托各位\x01",
            "去买回来，然后交给市长。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1808")

    label("loc_17A8")


    #C0053
    ChrTalk(
        0x8,
        (
            "从明天开始，预算会议\x01",
            "就要在议事堂正式召开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "媒体的人也会过来……\x01",
            "应该又会开始忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1808")

    Jump("loc_2799")

    label("loc_180D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AB")

    #C0055
    ChrTalk(
        0x8,
        (
            "今天晚上五点\x01",
            "将要召开闭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "不过，会场大概会\x01",
            "非常混乱嘈杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "至于闭幕宣言，请通过市政厅前方广场的\x01",
            "扩音器来收听吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1900")

    label("loc_18AB")


    #C0058
    ChrTalk(
        0x8,
        (
            "会场大概会\x01",
            "非常混乱嘈杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "请通过市政厅前方\x01",
            "广场的扩音器\x01",
            "来收听闭幕宣言吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1900")

    Jump("loc_2799")

    label("loc_1905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1978")

    #C0060
    ChrTalk(
        0x8,
        "游行总算是顺利结束了呢。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "呼……太好了。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "各位市民好像也都玩得很尽兴，\x01",
            "这就最好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2799")

    label("loc_1978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DA")

    #C0063
    ChrTalk(
        0x8,
        "游行终于要开始了啊……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "呼，希望今年也能\x01",
            "平安无事地展开啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A15")

    label("loc_19DA")


    #C0065
    ChrTalk(
        0x8,
        (
            "每年的游行活动中都会发生很多事故，\x01",
            "真是很令人头疼……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A15")

    Jump("loc_2799")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A91")

    #C0066
    ChrTalk(
        0x8,
        (
            "如果想旁听今天的国际研讨会，\x01",
            "需要事先提出申请。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "实在非常抱歉，\x01",
            "今天的旁听申请名额\x01",
            "已经没有了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2799")

    label("loc_1A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B33")

    #C0068
    ChrTalk(
        0x8,
        (
            "我们这里在配发\x01",
            "纪念庆典的宣传手册。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "纪念庆典的日程表，主要店铺，\x01",
            "还有游行队伍的经过路线都有\x01",
            "详细记录哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "还请多加利用。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B7F")

    label("loc_1B33")


    #C0071
    ChrTalk(
        0x8,
        (
            "我们这里在配发\x01",
            "纪念庆典的宣传手册。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "当然是免费的，\x01",
            "还请多加使用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B7F")

    Jump("loc_2799")

    label("loc_1B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CED")

    #C0073
    ChrTalk(
        0x8,
        (
            "啊，各位……\x01",
            "事情已经办完了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#0100F嗯，托您的福。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x104,
        (
            "#0300F虽然事态又变得\x01",
            "很棘手了…\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0076
    ChrTalk(
        0x8,
        "这个，虽然不是很明白……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "不过，以后如果还准备\x01",
            "进入地下空间的话，\x01",
            "钥匙就放在你们那里也没关系哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        "请各位随意使用吧。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#0000F是吗，那我们就不客气了。\x02\x03",

            "#0003F（果然还是有些\x01",
            "  在意约纳呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 2)
    Jump("loc_1DD9")

    label("loc_1CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D77")

    #C0080
    ChrTalk(
        0x8,
        (
            "市政厅今天也有些混乱忙碌呢，\x01",
            "一直都人来人往的。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "因为要进行纪念庆典开幕式的预先演习。\x01",
            "……真是给各位添麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DD9")

    label("loc_1D77")


    #C0082
    ChrTalk(
        0x8,
        (
            "今天要在大会堂内进行\x01",
            "纪念庆典开幕式的预先演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "所以暂时谢绝市民们入内，\x01",
            "还请多加谅解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD9")

    Jump("loc_2799")

    label("loc_1DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_END)), "loc_1E50")

    #C0084
    ChrTalk(
        0x8,
        (
            "地下空间Ｂ区域的入口\x01",
            "在住宅街的水道附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "以前就有人把钥匙弄丢过，\x01",
            "所以还请各位多加注意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2799")

    label("loc_1E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECD")

    #C0086
    ChrTalk(
        0x8,
        (
            "今天要在大会堂内进行\x01",
            "纪念庆典开幕式的预先演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "所以暂时谢绝市民们入内，\x01",
            "还请多加谅解。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F41")

    label("loc_1ECD")


    #C0088
    ChrTalk(
        0x8,
        (
            "说起来，警察们好像\x01",
            "也在进行游行活动的预先演习呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "呼……随着纪念庆典的临近，\x01",
            "各种各样的活动都接踵而来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F41")

    Jump("loc_2799")

    label("loc_1F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1F98")

    #C0090
    ChrTalk(
        0x8,
        (
            "呼……\x01",
            "克洛斯贝尔时代周刊的人\x01",
            "一直纠缠不休，真是让人头疼啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2799")

    label("loc_1F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_20CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2062")

    #C0091
    ChrTalk(
        0x8,
        (
            "下个月，庆祝自治州\x01",
            "创立七十周年的\x01",
            "纪念庆典终于要开幕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "为了庆祝七十周年这个大日子，\x01",
            "会期要比往年更长，\x01",
            "总共将要召开五天。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "至于详细情况，\x01",
            "请就参考宣传手册吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20CA")

    label("loc_2062")


    #C0094
    ChrTalk(
        0x8,
        (
            "下个月将要召开克洛斯贝尔自治州\x01",
            "建立七十周年的纪念庆典。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "至于详细的情况，\x01",
            "请就参考宣传手册吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CA")

    Jump("loc_2799")

    label("loc_20CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_22CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225E")

    #C0096
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔自治州今年将要迎来\x01",
            "创立七十周年纪念日。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "在创立纪念庆典中，\x01",
            "将会举办各种各样的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "详细情报也会刊登在\x01",
            "克洛斯贝尔市刊上，\x01",
            "请一定要多留意哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0305F克洛斯贝尔市刊……？\x01",
            "嘿，还有那种刊物啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x8,
        (
            "嗯，就是放在接待处柜台旁边\x01",
            "的那些宣传手册。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "虽然不太显眼，\x01",
            "但其实每个月都会更新的。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#0003F（以前都不知道……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22CA")

    label("loc_225E")


    #C0103
    ChrTalk(
        0x8,
        (
            "读市刊的人果然\x01",
            "很少啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "要是内容能再精彩\x01",
            "一点就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        "#0106F（接待人员也真是很辛苦呢……）\x02",
    )

    CloseMessageWindow()

    label("loc_22CA")

    Jump("loc_2799")

    label("loc_22CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_2391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2357")

    #C0106
    ChrTalk(
        0x8,
        (
            "有一辆巴士\x01",
            "失去了联络……\x01",
            "交通科的人已经前去探查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "是发生什么故障了吗……\x01",
            "稍微有些让人担心呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_238C")

    label("loc_2357")


    #C0108
    ChrTalk(
        0x8,
        (
            "巴士时不时就会出现故障，\x01",
            "但愿别出什么事就好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238C")

    Jump("loc_2799")

    label("loc_2391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2428")

    #C0109
    ChrTalk(
        0x8,
        "欢迎来到克洛斯贝尔市政厅。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "如果想知道巴士的运行时刻，\x01",
            "可以随时来本接待处\x01",
            "进行咨询哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "导力巴士的运行是由\x01",
            "交通科来管辖的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2799")

    label("loc_2428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2598")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2512")

    #C0112
    ChrTalk(
        0x8,
        (
            "我来为您介绍一下\x01",
            "市政厅内的机构设置吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "这座市政厅包括\x01",
            "两部分区域。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "上楼之后，左手方向就是大会堂，\x01",
            "右手边是克洛斯贝尔议事堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "大会堂内经常举办各种活动，\x01",
            "各位市民对那个地方\x01",
            "应该也很熟悉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2593")

    label("loc_2512")


    #C0116
    ChrTalk(
        0x8,
        (
            "上楼之后，左手方向就是大会堂，\x01",
            "右手边是克洛斯贝尔议事堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "大会堂内经常举办各种活动，\x01",
            "各位市民对那个地方\x01",
            "应该也很熟悉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2593")

    Jump("loc_2799")

    label("loc_2598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2654")

    #C0118
    ChrTalk(
        0x8,
        (
            "这里是克洛斯贝尔\x01",
            "市政厅的接待处。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "如果想支付各种费用，\x01",
            "或是申请迁居，\x01",
            "就请来这里办理手续。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#0000F啊哈哈……\x01",
            "（市政厅的接待人员好像也很辛苦呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26B9")

    label("loc_2654")


    #C0121
    ChrTalk(
        0x8,
        (
            "这里是克洛斯贝尔\x01",
            "市政厅的接待处。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "如果想支付各种费用，\x01",
            "或是申请迁居，\x01",
            "就请来这里办理手续。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B9")

    Jump("loc_2799")

    label("loc_26BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271F")

    #C0123
    ChrTalk(
        0x8,
        "刚才那个女孩子，不要紧吧……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "虽然我向她介绍了\x01",
            "旧城区的公寓，不过……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2799")

    label("loc_271F")


    #C0125
    ChrTalk(
        0x8,
        (
            "刚才来了一位紫头发的女孩，\x01",
            "让我为她介绍房租最便宜\x01",
            "的公寓。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "虽然我向她介绍了\x01",
            "旧城区的公寓，不过……\x01",
            "不要紧吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2799")

    TalkEnd(0x8)

    label("loc_279C")

    Return()

    # Function_6_AE8 end

    def Function_7_279D(): pass

    label("Function_7_279D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27BE")
    Call(0, 30)
    Return()

    label("loc_27BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_285C")

    #C0127
    ChrTalk(
        0xFE,
        (
            "预算会议总算是\x01",
            "结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "听说市长今天也坚持要继续加班，\x01",
            "处理剩下的文件……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "嗯～真是不忍心看下去了。\x01",
            "既然如此，我也来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_285C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_291E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C2")

    #C0130
    ChrTalk(
        0xFE,
        "市长最近也一直在加班工作。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "希望预算方案能在今天\x01",
            "讨论出个结果啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2919")

    label("loc_28C2")


    #C0132
    ChrTalk(
        0xFE,
        "市长最近也一直在加班工作。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "他都已经上年纪了……\x01",
            "这样下去，真担心他的身体呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2919")

    Jump("loc_3C94")

    label("loc_291E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2A61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F8")

    #C0134
    ChrTalk(
        0xFE,
        (
            "在议会召开的期间，职员们也必须要\x01",
            "做好充足的准备，以回答各种问题。\x01",
            "相关部门一直加班加点地工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "大家好像都很忙啊……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "不过，我们科倒是很清闲，\x01",
            "唯一的工作就是管理办公用品而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A5C")

    label("loc_29F8")


    #C0137
    ChrTalk(
        0xFE,
        (
            "不过，看着那些忙碌的同事们，\x01",
            "总是觉得有些不好意思呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "至少也应该替他们\x01",
            "把走廊清扫干净啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5C")

    Jump("loc_3C94")

    label("loc_2A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B08")

    #C0139
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长\x01",
            "去出席议会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "昨天的争论也处于白热化状态……\x01",
            "但到了最后，预算方案还是没能定下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "……唉，市长也真是不容易呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B3D")

    label("loc_2B08")


    #C0142
    ChrTalk(
        0xFE,
        (
            "我很担心市长的身体啊，\x01",
            "希望他不要太勉强自己……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3D")

    Jump("loc_3C94")

    label("loc_2B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2FFB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BCB")

    #C0143
    ChrTalk(
        0xFE,
        (
            "市长从以前开始就一直\x01",
            "很喜欢吃苦西红柿。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "不过……那种东西毕竟不是人人都能接受的呢。\x01",
            "至少我就受不了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_2BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C21")

    #C0145
    ChrTalk(
        0xFE,
        (
            "唉……每次都是如此，\x01",
            "一看见哈尔特曼议长，我就紧张得要窒息。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_2C21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D63")

    #C0146
    ChrTalk(
        0xFE,
        (
            "哦哦，各位，听我说啊。\x01",
            "『圣徒的祈祷』已经找回来了！\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "那座雕像可是市政厅的象征啊。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "其实，在纪念庆典期间，\x01",
            "那个，曾经被人盗走了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "不过，就在前几天，搜查一科的人\x01",
            "终于帮忙找回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "哈哈哈，太好了……\x01",
            "如果这雕像丢失，克洛斯贝尔注定\x01",
            "会沦为笑料，这耻辱永远都无法洗刷。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DDC")

    label("loc_2D63")


    #C0151
    ChrTalk(
        0xFE,
        (
            "能找回『圣徒的祈祷』，\x01",
            "真是太好了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "不过是在纪念庆典期间被盗走的，\x01",
            "所以还是让各位外国人士\x01",
            "看了个大笑话啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDC")

    Jump("loc_2FF6")

    label("loc_2DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E98")

    #C0153
    ChrTalk(
        0xFE,
        (
            "这不是各位警察嘛，\x01",
            "前几天真是承蒙相助了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "如你们所见，『圣徒的祈祷』\x01",
            "今日已经气度威严地坐镇于此了。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "我一定会倍加小心地看守，\x01",
            "绝对不会让它再次被盗了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 5)
    Jump("loc_2FF6")

    label("loc_2E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F8E")

    #C0156
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长是个很亲切的人，\x01",
            "对待我们这些下属职员也都和蔼有礼。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "可是……虽然态度亲切和善，\x01",
            "但他绝不会轻易吐露自己的真实想法呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "身为政治家，以自身的立场来说，\x01",
            "这也是理所当然的行事方式。\x01",
            "……但还是稍微有些失落啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FF6")

    label("loc_2F8E")


    #C0159
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长绝对不会轻易\x01",
            "向我们吐露自己的真实想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "会不会出现一个能让市长\x01",
            "完全信赖的人呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF6")

    Jump("loc_3C94")

    label("loc_2FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_328B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_30C6")

    #C0161
    ChrTalk(
        0xFE,
        (
            "虽、虽然不太明白，\x01",
            "不过真是得救了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "现在正忙着准备闭幕式呢。\x01",
            "……虽然无法正式向你们表示谢意，\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "但实在是很感谢各位的帮忙。\x01",
            "如果以后再有什么事情，还请继续关照啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3286")

    label("loc_30C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3177")

    #C0164
    ChrTalk(
        0xFE,
        (
            "今天可是闭幕式召开的日子，\x01",
            "居然会发生这种事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "各位，无论如何，也请尽早\x01",
            "把『圣徒的祈祷』找回来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "事态真的是十万火急，拜托了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_320E")

    label("loc_3177")


    #C0167
    ChrTalk(
        0xFE,
        (
            "从下午开始，就会有参加\x01",
            "闭幕式的人员入馆了……\x01",
            "如果到那个时候，雕像仍然没找回的话，可就……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "各位，无论如何，请尽早\x01",
            "把『圣徒的祈祷』找回来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_320E")

    Jump("loc_3286")

    label("loc_3213")


    #C0169
    ChrTalk(
        0xFE,
        (
            "哈，这叫什么事啊……\x01",
            "在市长外出期间，\x01",
            "居然会发生这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "如今，也只有拜托他们了啊……\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3286")

    Jump("loc_3C94")

    label("loc_328B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3311")

    #C0171
    ChrTalk(
        0xFE,
        (
            "市长已经前去和\x01",
            "各位大人物进行会谈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "应该也会见到ＩＢＣ的\x01",
            "库罗伊斯总裁等人。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "大概又要很晚才能回来吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_3311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3386")

    #C0174
    ChrTalk(
        0xFE,
        (
            "市长好像又\x01",
            "消瘦了一点……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "在这种时期，休息也许\x01",
            "确实是奢望……\x01",
            "但还是希望他不要太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_3386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33DB")

    #C0176
    ChrTalk(
        0xFE,
        (
            "啊，媒体人士比想象中的\x01",
            "还要多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        "必须要增设一些座位才行啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_33DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3457")

    #C0178
    ChrTalk(
        0xFE,
        (
            "……我最近一直都在给\x01",
            "麦克道尔市长帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "因为市长毕竟遇到了\x01",
            "那样的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "而且我平时都很闲呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_3457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_34DE")

    #C0181
    ChrTalk(
        0xFE,
        (
            "哎呀呀，还好有阿奈斯特先生\x01",
            "帮忙安排，总算得救了。\x01",
            "听证会好像可以顺利召开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "市长一直都很忙，\x01",
            "平时很难找到他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_34DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_360F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AC")

    #C0183
    ChrTalk(
        0xFE,
        (
            "真是无奈啊，今天就要召开听证会了，\x01",
            "但市长却不见人影。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "他平时一直都很忙，所以早就习惯了，\x01",
            "总觉得到时候自然就能找到……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "呼，至少也要找到首席秘书\x01",
            "阿奈斯特先生才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_360A")

    label("loc_35AC")


    #C0186
    ChrTalk(
        0xFE,
        (
            "如果没有市长的印章，\x01",
            "听证会就不能召开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "至少也要找到首席秘书\x01",
            "阿奈斯特先生才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360A")

    Jump("loc_3C94")

    label("loc_360F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_36A2")

    #C0188
    ChrTalk(
        0xFE,
        (
            "说起来，明天好像\x01",
            "要召开听证会吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "需要布置大会堂，\x01",
            "归纳市民们的请愿……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "市长到时也会出席的，\x01",
            "必须要事先谈好才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_36A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_37E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A1")

    #C0191
    ChrTalk(
        0xFE,
        (
            "……关于明年预算方案的\x01",
            "洽谈会已经开始了。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "政府会举办活动，解答各界对预算会议结果提出的质疑，\x01",
            "而媒体界对这项活动的关注度可是相当之高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "年轻的议员肯定会被压制，\x01",
            "只有那些重量级的政治家\x01",
            "才能摆出一副架子，侃侃而谈。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_37E4")

    label("loc_37A1")


    #C0194
    ChrTalk(
        0xFE,
        (
            "最近正是议员先生们\x01",
            "意气风发的时期啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "呼，真让人郁闷啊。\x02",
    )

    CloseMessageWindow()

    label("loc_37E4")

    Jump("loc_3C94")

    label("loc_37E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3861")

    #C0196
    ChrTalk(
        0xFE,
        (
            "昨天的巴士故障事件，\x01",
            "原因好像只是因为平时的维护工作不足。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "哎呀呀，这种琐碎的事情\x01",
            "还真是够多的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_3861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_38C5")

    #C0198
    ChrTalk(
        0xFE,
        (
            "刚才，交通科的人\x01",
            "急匆匆地跑出去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "交通科的人总是那么忙，\x01",
            "真令人同情啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_38C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_39C8")

    #C0200
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市近年来\x01",
            "为了服务市民，一直都在\x01",
            "大力推动导力巴士的发展。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "话虽如此……但其实谁都明白，\x01",
            "这只是议员们为了讨好市民，赢得人气，\x01",
            "通过增加投资预算才建造出的产物。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "算了，不管动机如何，只要能让\x01",
            "大家的生活越来越方便，那就是好事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_39C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3AF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA3")

    #C0203
    ChrTalk(
        0xFE,
        (
            "这边的大门通向市政厅的\x01",
            "左翼区域。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "市长的办公室就在里面。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "而另一边的大门……\x01",
            "通向市政厅的右翼区域，\x01",
            "里面有议长的办公室。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "这两位全是在自治州内外都拥有\x01",
            "相当影响力的大政治家。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3AF1")

    label("loc_3AA3")


    #C0207
    ChrTalk(
        0xFE,
        (
            "市长和议长\x01",
            "现在都不在哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "他们两位都是大政治家，\x01",
            "所以平时都很忙的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF1")

    Jump("loc_3C94")

    label("loc_3AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3BE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B93")

    #C0209
    ChrTalk(
        0xFE,
        "我在总务二科工作。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "议事堂和大会堂的管理工作\x01",
            "都由我负责，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "平时还是很闲啊。\x01",
            "需要做的只有扫除之类的事情而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BDC")

    label("loc_3B93")


    #C0212
    ChrTalk(
        0xFE,
        (
            "不过，议会一旦召开，\x01",
            "那就又该有得忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "平时倒是一直都很闲啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3BDC")

    Jump("loc_3C94")

    label("loc_3BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C51")

    #C0214
    ChrTalk(
        0xFE,
        "好啦，扫除扫除……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "今天就把会场给\x01",
            "打扫干净吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "也没什么其它事情可做。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C94")

    label("loc_3C51")


    #C0217
    ChrTalk(
        0xFE,
        "哎呀……请问有何贵干？\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "如果有事，请去找\x01",
            "接待处的希恩吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C94")

    TalkEnd(0xFE)
    Return()

    # Function_7_279D end

    def Function_8_3C98(): pass

    label("Function_8_3C98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E75")
    OP_4B(0x9, 0xFF)
    TurnDirection(0xA, 0x9, 0)

    #C0219
    ChrTalk(
        0x9,
        (
            "那么，阿奈斯特先生，\x01",
            "拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        (
            "#2600F谢谢，\x01",
            "我会善加利用的。\x02\x03",

            "#2604F很好，只要有这个，\x01",
            "听证会总算就可以……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 500)

    #C0221
    ChrTalk(
        0xA,
        (
            "#2600F哈哈，从市民们那里收集来的\x01",
            "意见和请愿，已经整理好了。\x02\x03",

            "如果在听证会中正式提出，\x01",
            "对那些议员们争权夺利的行为，\x01",
            "应该也能起到些警示作用吧。\x02\x03",

            "#2603F那么，在听证会开始之前，\x01",
            "必须要和市长商量一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        "#0108F………………………………\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#0003F（艾莉……果然还是\x01",
            "  对政治之道有所留恋吧？）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F41")

    label("loc_3E75")


    #C0224
    ChrTalk(
        0xA,
        (
            "#2600F从市民们那里收集来的意见和请愿，\x01",
            "已经整理成资料了……\x02\x03",

            "如果在听证会中正式提出，\x01",
            "对那些议员们争权夺利的行为，\x01",
            "应该也能起到些警示作用吧。\x02\x03",

            "#2603F那么，在听证会开始之前，\x01",
            "必须要和市长商量一下……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F41")

    TalkEnd(0xFE)
    Return()

    # Function_8_3C98 end

    def Function_9_3F45(): pass

    label("Function_9_3F45")

    Call(0, 10)
    Return()

    # Function_9_3F45 end

    def Function_10_3F49(): pass

    label("Function_10_3F49")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FDD")
    Jump("loc_4027")

    label("loc_3FDD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FFD")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4027")

    label("loc_3FFD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_401D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4027")

    label("loc_401D")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4027")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_445F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43CC")
    SetChrSubChip(0xB, 0x0)

    #C0225
    ChrTalk(
        0xB,
        (
            "#2501F嗯，马上准备好吧，\x01",
            "我来检查那些文件。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_413D")
    Jump("loc_4187")

    label("loc_413D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_415D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4187")

    label("loc_415D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_417D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4187")

    label("loc_417D")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4187")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0226
    ChrTalk(
        0xB,
        (
            "#2500F哦，是你们啊。\x01",
            "……有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#0000F啊，不……只是在调查的过程中\x01",
            "正好路过，就顺便过来看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x102,
        (
            "#0100F外公好像\x01",
            "相当忙啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xB,
        (
            "#2503F嗯，会期延长了\x01",
            "整整三天啊。\x02\x03",

            "#2500F各方面的预算安排，\x01",
            "都必须要加急处理好。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        "#0101F………………………………\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xB,
        (
            "#2500F哈哈，你们好像在担心\x01",
            "我加班会不会累坏身体吧。\x02\x03",

            "#2503F用不着替我担心，这种繁忙的\x01",
            "状态大概也只会持续到今天为止。\x02\x03",

            "#2500F艾莉，如果你正在工作，\x01",
            "就要集中精力处理自己那边的正事。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        "#0103F……是的，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        "#0200F那么，我们就快去医院吧。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        "#0300F是啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 5)
    Jump("loc_445A")

    label("loc_43CC")

    OP_4B(0x9, 0xFF)
    SetChrSubChip(0xB, 0x0)

    #C0235
    ChrTalk(
        0xB,
        (
            "#2503F库利普，不好意思啊，\x01",
            "联络财务科的事就交给你了。\x02\x03",

            "#2500F至于哈尔特曼议长那边，\x01",
            "就由我把文件送给他。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x9,
        "是的，明白了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)

    label("loc_445A")

    Jump("loc_4F47")

    label("loc_445F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_446D")
    Jump("loc_4F47")

    label("loc_446D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_447B")
    Jump("loc_4F47")

    label("loc_447B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4489")
    Jump("loc_4F47")

    label("loc_4489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4826")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_481E")

    #C0237
    ChrTalk(
        0xB,
        (
            "#2509F多亏你们给我送来的饮料，\x01",
            "让我下午也能干劲十足地继续工作。\x02\x03",

            "#2503F（啜饮）……\x01",
            "嗯，很美味！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4819")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_471E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4560")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_45B5")

    label("loc_4560")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_458D")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_45B5")

    label("loc_458D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45B5")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_45B5")

    Sleep(1000)

    #C0238
    ChrTalk(
        0x101,
        "#0006F（好像真是很喜欢啊……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_463B")

    #C0239
    ChrTalk(
        0x102,
        (
            "#0103F（真不愧是外公……\x01",
            "  在动荡的时代中崛起的\x01",
            "  著名政治家啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46EA")

    label("loc_463B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_468F")

    #C0240
    ChrTalk(
        0x103,
        (
            "#0206F（竟然能把味道那么苦的奶昔……\x01",
            "  真是值得尊敬呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46EA")

    label("loc_468F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46EA")

    #C0241
    ChrTalk(
        0x104,
        (
            "#0303F（竟然能把味道那么苦的奶昔……\x01",
            "  身为男人，他真是值得尊敬啊！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46EA")


    #C0242
    ChrTalk(
        0x153,
        (
            "#1105F（哎～怎么了？\x01",
            "  本来就很美味啊～）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4816")

    label("loc_471E")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4763")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_47B8")

    label("loc_4763")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4790")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_47B8")

    label("loc_4790")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47B8")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_47B8")

    Sleep(1000)

    #C0243
    ChrTalk(
        0x153,
        "#1111F（不错啊，好像很美味呢～）\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#0006F（当、当时是不是\x01",
            "  应该稍微尝一下呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4816")

    SetScenarioFlags(0x0, 3)

    label("loc_4819")

    Jump("loc_4821")

    label("loc_481E")

    Call(0, 17)

    label("loc_4821")

    Jump("loc_4F47")

    label("loc_4826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4834")
    Jump("loc_4F47")

    label("loc_4834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4842")
    Jump("loc_4F47")

    label("loc_4842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4A7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49FA")

    #C0245
    ChrTalk(
        0xB,
        (
            "#2503F嗯，今天的游行活动，\x01",
            "参与人数好像是至今为止最多的一次呢。\x02\x03",

            "#2500F在游行开始之前，\x01",
            "必须要去和大家打个招呼才行。\x01",
            "……但还真是有点紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        "#0005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x104,
        "#0300F那个……您是在开玩笑吧？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#0106F呼……\x01",
            "对外公来说，这种程度的小场面，\x01",
            "根本没理由会紧张吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xB,
        (
            "#2509F呵呵……\x02\x03",

            "#2500F游行结束之后，纪念庆典\x01",
            "的主要节目也就算是彻底落幕了。\x02\x03",

            "你们的工作大概也能恢复轻松了吧，\x01",
            "希望一切都能进展顺利啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A76")

    label("loc_49FA")


    #C0250
    ChrTalk(
        0xB,
        (
            "#2500F游行结束之后，纪念庆典\x01",
            "的主要节目也就算是彻底落幕了。\x02\x03",

            "你们的工作大概也能恢复轻松了吧，\x01",
            "希望一切都能进展顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A76")

    Jump("loc_4F47")

    label("loc_4A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BB1")

    #C0251
    ChrTalk(
        0xB,
        (
            "#2500F今天召开的这场研讨会\x01",
            "是由我提议的。\x02\x03",

            "针对克洛斯贝尔的现状与将来，\x01",
            "以完全公开的形式展开讨论。\x02\x03",

            "#2503F对政治方面的影响也许是微不足道的，\x01",
            "但来自各国的有识之士都齐聚一堂。\x02\x03",

            "#2500F在自治州建立七十周年的这个日子里，\x01",
            "通过这种活动来仔细审视一下克洛斯贝尔，\x01",
            "也算是个不算的契机吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C38")

    label("loc_4BB1")


    #C0252
    ChrTalk(
        0xB,
        (
            "#2500F今天召开的这场研讨会\x01",
            "是由我提议的。\x02\x03",

            "针对克洛斯贝尔的现状与将来，\x01",
            "以完全公开的形式展开讨论。\x01",
            "一定会是一场很有意义的讨论吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C38")

    Jump("loc_4F47")

    label("loc_4C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAD")

    #C0253
    ChrTalk(
        0xB,
        (
            "#2500F哦，艾莉。\x01",
            "还有支援科的诸位也来了啊。\x02\x03",

            "#2503F不好意思啊，在纪念庆典时期，\x01",
            "也有一大堆事情等着我去处理。\x02\x03",

            "本来还打算和你们一起吃顿饭，\x01",
            "结果也一直没有机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#0005F哪、哪里……\x01",
            "请您不必在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#0200F比起这些，您的身体\x01",
            "已经不要紧了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        (
            "#2503F不要紧了，只不过是那种程度的小事而已，\x01",
            "怎么可能这么轻易就让我倒下啊。\x02\x03",

            "#2501F帝国与共和国之间的纷争还在持续，\x01",
            "与三十年前比起来……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        (
            "#0103F外公……先别说这些了。\x01",
            "那种话题，只要一旦开始说，就会没完没了的。\x02\x03",

            "#0100F至于吃饭，\x01",
            "以后总会有机会的。\x02\x03",

            "您的身体才是最重要的，\x01",
            "请一定不要太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xB,
        (
            "#2500F嗯，我知道了。\x01",
            "谢谢你，艾莉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F47")

    label("loc_4EAD")


    #C0259
    ChrTalk(
        0xB,
        (
            "#2500F在纪念庆典期间，\x01",
            "也有一大堆事情等着我去办呢。\x02\x03",

            "#2503F本来还想找个机会，和你们\x01",
            "轻轻松松闲谈一次的，可是……\x02\x03",

            "#2500F嗯，还是等以后有机会再说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F47")

    SetChrSubChip(0xB, 0x0)
    TalkEnd(0xB)
    Return()

    # Function_10_3F49 end

    def Function_11_4F4F(): pass

    label("Function_11_4F4F")

    TalkBegin(0xFE)

    #C0260
    ChrTalk(
        0xFE,
        "啊，是罗伊德还有各位吗。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "在今天的研讨会上，\x01",
            "麦克道尔市长和外国的\x01",
            "ＶＩＰ都会出席哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        "那阵容真是相当壮观啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_4F4F end

    def Function_12_4FD0(): pass

    label("Function_12_4FD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5145")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_509D")

    #C0263
    ChrTalk(
        0xFE,
        (
            "『圣者的祈祷』已经找回来了啊。\x01",
            "太好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "不对不对，现在可不是高兴的时候。\x01",
            "闭幕式的准备工作\x01",
            "都快来不及做了。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "距离闭幕式的召开还有三个小时……\x01",
            "必须要抓紧时间啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5140")

    label("loc_509D")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0266
    ChrTalk(
        0xD,
        (
            "哇啊啊……\x01",
            "竟然在市长不在的时候……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0267
    ChrTalk(
        0xE,
        (
            "总、总之，必须要尽快\x01",
            "做好闭幕式的准备工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xE,
        (
            "我这就去准备会场中\x01",
            "的椅子哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)

    label("loc_5140")

    Jump("loc_523D")

    label("loc_5145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_523D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51BE")

    #C0269
    ChrTalk(
        0xFE,
        (
            "准备旁听国际研讨会的各位，\x01",
            "还请稍等一下～\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "到了开场时间之后，\x01",
            "我会立即引领您入场的～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_523D")

    label("loc_51BE")


    #C0271
    ChrTalk(
        0xFE,
        (
            "呼，国际研讨会总算是\x01",
            "可以顺利召开了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "顺便一说，亚里欧斯·马克莱因\x01",
            "也来到了会场呢。\x01",
            "会场中的警备工作已经没问题了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_523D")

    TalkEnd(0xFE)
    Return()

    # Function_12_4FD0 end

    def Function_13_5241(): pass

    label("Function_13_5241")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5255")
    Call(0, 12)
    Jump("loc_52B1")

    label("loc_5255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_52B1")
    OP_93(0xFE, 0x5A, 0x0)

    #C0273
    ChrTalk(
        0xFE,
        (
            "那个，已经\x01",
            "没有时间了……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "我想，差不多也该请\x01",
            "各位出席者入场了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52B1")

    TalkEnd(0xFE)
    Return()

    # Function_13_5241 end

    def Function_14_52B5(): pass

    label("Function_14_52B5")

    TalkBegin(0xFE)

    #C0275
    ChrTalk(
        0xFE,
        (
            "今天也有活动召开，\x01",
            "我们总务二科也是很忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        "……虽然平时是很清闲的部门。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_52B5 end

    def Function_15_530F(): pass

    label("Function_15_530F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_539D")

    #C0277
    ChrTalk(
        0xFE,
        (
            "最近，在总编的命令下，\x01",
            "我暂时要给格蕾丝前辈\x01",
            "当助手……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "……前辈经常要去现场采访，\x01",
            "每到这种时候就把我丢在一边不管。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_540B")

    label("loc_539D")


    #C0279
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈去\x01",
            "报道议会的情况了。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "可是，不要紧吗……\x01",
            "她又是在没有许可证的情况下\x01",
            "偷偷潜入进去的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_540B")

    TalkEnd(0xFE)
    Return()

    # Function_15_530F end

    def Function_16_540F(): pass

    label("Function_16_540F")

    TalkBegin(0xFE)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_54E9")

    #C0281
    ChrTalk(
        0x11,
        (
            "#2103F再怎么说，我也是克洛斯贝尔的市民，\x01",
            "平时都有依法纳税的啊～\x02\x03",

            "#2100F那些人可都是靠我们交的税金发薪过活的，\x01",
            "把他们的联络方式告诉我有什么不可以的～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "啊～那个，\x01",
            "听你这么一说，确实……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_574D")

    label("loc_54E9")


    #C0283
    ChrTalk(
        0x11,
        (
            "#2104F嗯～很好，针对这一点，\x01",
            "继续乘胜追击、不断紧逼，\x01",
            "她应该就会告诉我了吧？\x02\x03",

            "#2109F议员们的紧急联络方式，\x01",
            "你应该都有记录吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "事务所之外的联络方式是绝对\x01",
            "不能透露的，这可是硬性规定。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        "还请您多加理解啊。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x11,
        (
            "#2106F啊啊～！\x01",
            "不要这么说嘛～\x02\x03",

            "#2100F那么，至少把\x01",
            "秘书们的联络方式告诉我啊，\x01",
            "这总可以了吧？\x02\x03",

            "#2109F那些官方机构的秘书，\x01",
            "应该都登记在册的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        "就、就算你这么说，我也……\x02",
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

    #C0288
    ChrTalk(
        0x101,
        (
            "#0006F（格蕾丝小姐……\x01",
            "  可真是喜欢强人所难啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#0100F（趁她的矛头还没有转向我们，\x01",
            "  还是赶快逃跑吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_574D")

    OP_4C(0x8, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_16_540F end

    def Function_17_5755(): pass

    label("Function_17_5755")

    EventBegin(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch06500.itc", 0x1E)
    LoadChrToIndex("chr/ch27800.itc", 0x1F)
    LoadChrToIndex("chr/ch27400.itc", 0x20)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02700.itp")
    OP_68(-45850, 1600, 12420, 0)
    MoveCamera(44, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21760, 0)
    SetChrPos(0x101, -45750, 0, 10750, 0)
    SetChrPos(0x153, -45000, 0, 12250, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5817")
    SetChrPos(0x102, -44250, 0, 11500, 0)
    Jump("loc_585E")

    label("loc_5817")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_583D")
    SetChrPos(0x103, -44250, 0, 11500, 0)
    Jump("loc_585E")

    label("loc_583D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_585E")
    SetChrPos(0x104, -44250, 0, 11500, 0)

    label("loc_585E")

    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, -45000, 120, 3000, 0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x16, -45750, 120, 1750, 0)
    SetChrPos(0x17, -44250, 120, 2500, 0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrSubChip(0xB, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5939")

    #C0290
    ChrTalk(
        0xB,
        (
            "#5P#2505F哦，艾莉，\x01",
            "还有罗伊德也来了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59BE")

    label("loc_5939")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_597E")

    #C0291
    ChrTalk(
        0xB,
        (
            "#5P#2505F哦，罗伊德……\x01",
            "还有缇欧也来了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59BE")

    label("loc_597E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59BE")

    #C0292
    ChrTalk(
        0xB,
        (
            "#5P#2505F哦，罗伊德……\x01",
            "还有兰迪也来了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A64")

    #C0293
    ChrTalk(
        0x102,
        (
            "#12P#0103F外公……\x01",
            "那个，最近一直都没能和您联络，\x01",
            "实在是对不起。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#6P#0003F之前那件事情，\x01",
            "承蒙您的多方关照……\x01",
            "真是不知该如何感谢才好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ACB")

    label("loc_5A64")


    #C0295
    ChrTalk(
        0x101,
        (
            "#6P#0000F市长……好久不见了。\x02\x03",

            "#0003F之前那件事情，\x01",
            "承蒙您的多方关照……\x01",
            "真是不知该如何感谢才好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ACB")


    #C0296
    ChrTalk(
        0xB,
        (
            "#5P#2503F哪里，没什么大不了的。\x02\x03",

            "#2500F我只不过是去拜托那些参加了『竞拍会』\x01",
            "的议员，让他们对详细情况做个说明而已。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B93")

    #C0297
    ChrTalk(
        0x102,
        (
            "#12P#0100F不，正是因为有您的帮忙，\x01",
            "才能够牵制住议长。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C32")

    label("loc_5B93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BE5")

    #C0298
    ChrTalk(
        0x103,
        (
            "#12P#0200F不过，正是因为您的帮忙，\x01",
            "才能将议长牵制住……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C32")

    label("loc_5BE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C32")

    #C0299
    ChrTalk(
        0x104,
        (
            "#12P#0300F哈，但正是因为有您帮忙，\x01",
            "才能够牵制住议长啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C32")


    #C0300
    ChrTalk(
        0x101,
        (
            "#6P#0000F总而言之……\x01",
            "实在是太感谢您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "#5P#2509F哈哈，如果连这点小事也值得如此在意，\x01",
            "那么蒙你们相救的我，\x01",
            "可该如何感谢才好啊。\x02\x03",

            "#2503F──嗯，先不说这些，\x01",
            "那位小姑娘莫非就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        (
            "#6P#0000F啊，是的，\x01",
            "她的名字叫琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x153,
        (
            "#6P#1110F初次见面～\x02\x03",

            "#1109F老爷爷，你的胡子全都白了，\x01",
            "真是好帅气啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "#5P#2509F帅气……\x01",
            "哈哈，真是个有趣的小姑娘啊。\x02\x03",

            "#2500F嗯，性格阳光又开朗，\x01",
            "而且好像有种不可思议的魅力……\x02\x03",

            "#2501F……听说她丧失了记忆，\x01",
            "到现在还没有查明身份来历吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E47")

    #C0305
    ChrTalk(
        0x102,
        "#12P#0103F嗯，现在还没有……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EAC")

    label("loc_5E47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E7E")

    #C0306
    ChrTalk(
        0x103,
        "#12P#0203F是的，目前还没有。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EAC")

    label("loc_5E7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EAC")

    #C0307
    ChrTalk(
        0x104,
        "#12P#0306F嗯，暂时还没。\x02",
    )

    CloseMessageWindow()

    label("loc_5EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_END)), "loc_5EFC")

    #C0308
    ChrTalk(
        0x101,
        (
            "#6P#0001F不过，我们已经委托游击士协会\x01",
            "帮忙调查她的身世了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F41")

    label("loc_5EFC")


    #C0309
    ChrTalk(
        0x101,
        (
            "#6P#0001F不过，我们正准备\x01",
            "去委托游击士协会\x01",
            "帮忙调查她的身世……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F41")


    #C0310
    ChrTalk(
        0xB,
        (
            "#5P#2500F嗯，交给他们确实是最合适的。\x01",
            "现在也只能尽量\x01",
            "使用一切能够想到的手段了。\x02\x03",

            "#2503F──不管怎么说，\x01",
            "以后如果遇到什么困难，\x01",
            "随时都可以来找我商量。\x02\x03",

            "虽然我只是个行事受限，\x01",
            "没什么用的市长……\x02\x03",

            "#2500F不过，我至少还没有窝囊到那种程度，\x01",
            "会对这种连小小幼女都企图\x01",
            "加害的愚蠢恶徒视而不见。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6090")

    #C0311
    ChrTalk(
        0x102,
        "#12P#0102F外公……\x02",
    )

    CloseMessageWindow()
    Jump("loc_60F3")

    label("loc_6090")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60C1")

    #C0312
    ChrTalk(
        0x103,
        "#12P#0202F市长先生……\x02",
    )

    CloseMessageWindow()
    Jump("loc_60F3")

    label("loc_60C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60F3")

    #C0313
    ChrTalk(
        0x104,
        "#12P#0302F噢噢，市长先生……\x02",
    )

    CloseMessageWindow()

    label("loc_60F3")


    #C0314
    ChrTalk(
        0x101,
        (
            "#6P#0004F……光凭您的这一番话，\x01",
            "就能给我们带来莫大勇气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x153,
        "#6P#1109F嘿嘿嘿，老爷爷果然很帅！\x02",
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)

    #N0316
    NpcTalk(
        0x15,
        "男人的声音",
        (
            "──麦克道尔市长，\x01",
            "可以稍微打扰一下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61FE")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_6247")

    label("loc_61FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6225")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_6247")

    label("loc_6225")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6247")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6247")

    Sleep(1000)

    #C0317
    ChrTalk(
        0xB,
        "#5P#2501F嗯……\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_68(-45000, 1500, 9000, 3000)

    def lambda_627B():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_627B)
    Sleep(50)

    def lambda_628B():
        OP_93(0x153, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_628B)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62B8")

    def lambda_62AB():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62AB)
    Jump("loc_62F7")

    label("loc_62B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62DA")

    def lambda_62CD():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_62CD)
    Jump("loc_62F7")

    label("loc_62DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62F7")

    def lambda_62EF():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62EF)

    label("loc_62F7")


    def lambda_62FC():
        OP_97(0x15, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_62FC)

    def lambda_6316():
        OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6316)
    Sleep(50)

    def lambda_632A():
        OP_97(0x16, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_632A)

    def lambda_6344():
        OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_6344)
    Sleep(50)

    def lambda_6358():
        OP_97(0x17, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6358)

    def lambda_6372():
        OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_6372)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63CB")
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jump("loc_6428")

    label("loc_63CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63FC")
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jump("loc_6428")

    label("loc_63FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6428")
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_6428")

    Sleep(1000)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)

    #C0318
    ChrTalk(
        0x101,
        "#6P#0005F（什么……！）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6491")

    #C0319
    ChrTalk(
        0x102,
        "#11P#0105F（哈尔特曼议长……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_64FC")

    label("loc_6491")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64C6")

    #C0320
    ChrTalk(
        0x103,
        "#11P#0205F（帝国派的……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_64FC")

    label("loc_64C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64FC")

    #C0321
    ChrTalk(
        0x104,
        "#11P#0301F（帝国派的首领吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_64FC")

    OP_68(-45850, 1600, 12420, 2000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_653C")

    def lambda_6522():
        OP_97(0x102, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6522)
    Jump("loc_6595")

    label("loc_653C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_656B")

    def lambda_6551():
        OP_97(0x103, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6551)
    Jump("loc_6595")

    label("loc_656B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6595")

    def lambda_6580():
        OP_97(0x104, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6580)

    label("loc_6595")

    Sleep(50)

    def lambda_659D():
        OP_97(0x101, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_659D)
    Sleep(50)

    def lambda_65BA():
        OP_97(0x153, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_65BA)

    def lambda_65D4():
        OP_97(0x15, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_65D4)
    Sleep(50)

    def lambda_65F1():
        OP_97(0x16, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_65F1)
    Sleep(50)

    def lambda_660E():
        OP_97(0x17, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_660E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6649")
    WaitChrThread(0x102, 1)

    def lambda_663C():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_663C)
    Jump("loc_6690")

    label("loc_6649")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_666F")
    WaitChrThread(0x103, 1)

    def lambda_6662():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6662)
    Jump("loc_6690")

    label("loc_666F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6690")
    WaitChrThread(0x104, 1)

    def lambda_6688():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6688)

    label("loc_6690")

    WaitChrThread(0x101, 1)

    def lambda_6699():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6699)
    WaitChrThread(0x153, 1)

    def lambda_66AA():
        OP_93(0x153, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_66AA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)

    #C0322
    ChrTalk(
        0xB,
        (
            "#5P#2500F哈尔特曼议长，有何贵干呢？\x02\x03",

            "如您所见，我正在接待客人。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0323
    AnonymousTalk(
        0x15,
        (
            "这可真是失礼了──不过，\x01",
            "我也稍微有点急事要找您。\x02\x03",

            "关于帝国政府于前日提出的建议，\x01",
            "希望能与您再次商讨一下。\x02",
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
    OP_6F(0x79)

    #C0324
    ChrTalk(
        0xB,
        "#5P#2503F可是，那个……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x15,
        (
            "#12P#2703F我明白市长您的意思。\x01",
            "不过，希望您也能考虑一下我的立场。\x02\x03",

            "#2702F还是说……\x01",
            "您想借此机会，同坎贝尔议员\x01",
            "他们联盟呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xB,
        (
            "#5P#2503F……我并没打算\x01",
            "与共和国派的人联成一线。\x02\x03",

            "#2501F当然，关于此点，对你们帝国派也是一样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x15,
        (
            "#12P#2702F既然如此，就请您把那种\x01",
            "平衡调控的能力充分发挥出来吧。\x02\x03",

            "#2703F因为我那小小的聚会\x01",
            "被搞得不欢而散，\x01",
            "而给整个自治州带来了负面影响……\x02\x03",

            "#2700F就算是为了把这笔账结清，您也该……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        (
            "#5P#2503F……看来，接下来确实有必要\x01",
            "与您再谈一次啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    #C0329
    ChrTalk(
        0xB,
        (
            "#5P#2500F……诸位，\x01",
            "你们难得前来拜访，却遇到这种事，\x01",
            "实在是不好意思……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A23():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A23)
    Sleep(50)

    def lambda_6A33():
        TurnDirection(0x153, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_6A33)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A5A")
    TurnDirection(0x102, 0xB, 500)
    Jump("loc_6A8D")

    label("loc_6A5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A76")
    TurnDirection(0x103, 0xB, 500)
    Jump("loc_6A8D")

    label("loc_6A76")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A8D")
    TurnDirection(0x104, 0xB, 500)

    label("loc_6A8D")


    #C0330
    ChrTalk(
        0x101,
        (
            "#11P#0005F哪、哪里，\x01",
            "请您不要在意。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AF3")

    #C0331
    ChrTalk(
        0x102,
        "#11P#0103F那我们这就告辞了，外公。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B56")

    label("loc_6AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B24")

    #C0332
    ChrTalk(
        0x103,
        "#11P#0203F……告辞了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B56")

    label("loc_6B24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B56")

    #C0333
    ChrTalk(
        0x104,
        "#11P#0300F那我们就先失陪啦。\x02",
    )

    CloseMessageWindow()

    label("loc_6B56")


    #C0334
    ChrTalk(
        0x153,
        (
            "#5P#1109F再见啦～！\x01",
            "大胡子的老爷爷！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_68(-7040, 5500, 17890, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19810, 0)
    SetChrPos(0x101, -7590, 4000, 19290, 135)
    SetChrPos(0x153, -7450, 4000, 17650, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C35")
    SetChrPos(0x102, -6220, 4000, 18950, 270)
    CloseMessageWindow()
    Jump("loc_6C7E")

    label("loc_6C35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C5C")
    SetChrPos(0x103, -6220, 4000, 18950, 270)
    CloseMessageWindow()
    Jump("loc_6C7E")

    label("loc_6C5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C7E")
    SetChrPos(0x104, -6220, 4000, 18950, 270)
    CloseMessageWindow()

    label("loc_6C7E")

    FadeToBright(1000, 0)
    OP_0D()

    #C0335
    ChrTalk(
        0x101,
        "#5P#0001F市长……可真是不容易呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D65")

    #C0336
    ChrTalk(
        0x102,
        (
            "#11P#0101F……嗯……\x02\x03",

            "类似的场面，我以前\x01",
            "也曾见过不知多少次了……\x02\x03",

            "#0108F不过，自己明明就是\x01",
            "举办违法竞拍会的的幕后首脑，\x01",
            "竟然还能如此理直气壮地提出要求……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E59")

    label("loc_6D65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DD8")

    #C0337
    ChrTalk(
        0x103,
        (
            "#11P#0203F那位议长……\x01",
            "还真是恬不知耻呢。\x02\x03",

            "#0200F那场违法竞拍会\x01",
            "明明就是他自己举办的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E59")

    label("loc_6DD8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E59")

    #C0338
    ChrTalk(
        0x104,
        (
            "#11P#0306F话说回来，那个议长\x01",
            "可真是不知羞耻啊。\x02\x03",

            "#0301F明明举办了那种\x01",
            "违法的竞拍会，态度竟然还能\x01",
            "如此坦然。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E59")


    #C0339
    ChrTalk(
        0x101,
        (
            "#5P#0001F像这种程度的事情，\x01",
            "他大概完全有自信能控制好，\x01",
            "不使其成为丑闻吧……\x02\x03",

            "#0006F从某种意义上来说，他远比\x01",
            "那些黑手党还要坏得多啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x153,
        (
            "#6P#1110F喂喂，罗伊德～\x02\x03",

            "那个老爷爷\x01",
            "不只是帅，\x01",
            "而且也很强吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_6F41():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F41)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F77")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x102, 0x153, 500)
    Jump("loc_6FCE")

    label("loc_6F77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FA5")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x103, 0x153, 500)
    Jump("loc_6FCE")

    label("loc_6FA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FCE")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x104, 0x153, 500)

    label("loc_6FCE")

    Sleep(500)
    WaitChrThread(0x101, 1)

    #C0341
    ChrTalk(
        0x101,
        (
            "#5P#0005F很强……\x01",
            "你为什么会这么想呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x153,
        (
            "#6P#1111F因为，那个看上去好像很嚣张的大叔，\x01",
            "不是和同伴们一起来的吗？\x02\x03",

            "#1110F他肯定是因为知道自己\x01",
            "一个人不是老爷爷的对手，\x01",
            "所以才带着别人一起来的吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#5P#0005F啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7139")

    #C0344
    ChrTalk(
        0x102,
        (
            "#11P#0105F虽然议长带去的人\x01",
            "都是帝国派的重要议员……\x02\x03",

            "#0104F呵呵，不过，你这种看问题\x01",
            "的角度确实也有些道理呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71F8")

    label("loc_7139")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7189")

    #C0345
    ChrTalk(
        0x103,
        (
            "#11P#0205F原来如此……\x01",
            "这种看问题的角度也颇有道理呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71F8")

    label("loc_7189")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71F8")

    #C0346
    ChrTalk(
        0x104,
        (
            "#11P#0304F哈哈，原来如此啊。\x02\x03",

            "#0300F没错，确实可以这么说，\x01",
            "他根本就没有和市长单挑的自信。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71F8")


    #C0347
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯～是啊，像我们这种后辈，\x01",
            "为市长担心根本就是不自量力吧。\x02\x03",

            "（话虽如此，不过，\x01",
            "  要是能为他做些什么就好了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    ModifyEventFlags(1, 0, 0x80)
    SetChrPos(0x0, -7590, 4000, 19290, 135)
    SetScenarioFlags(0xBE, 6)
    EventEnd(0x5)
    Return()

    # Function_17_5755 end

    def Function_18_729B(): pass

    label("Function_18_729B")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7320")
    OP_68(-3140, 1500, 3700, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19330, 0)
    SetChrPos(0x101, -4500, 130, 2900, 90)
    SetChrPos(0x153, -5250, 130, 3650, 90)
    SetChrPos(0xEF, -6000, 130, 2150, 90)
    Jump("loc_7381")

    label("loc_7320")

    OP_68(3140, 1500, 3700, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19330, 0)
    SetChrPos(0x101, 4500, 130, 2900, 270)
    SetChrPos(0x153, 5250, 130, 3650, 270)
    SetChrPos(0xEF, 6000, 130, 2150, 270)

    label("loc_7381")

    TurnDirection(0x8, 0x101, 0)
    OP_0D()

    #C0348
    ChrTalk(
        0x8,
        "啊，各位……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x8,
        (
            "那个，市长室的情况\x01",
            "怎么样了……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_73C7():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73C7)
    Sleep(50)

    def lambda_73D7():
        TurnDirection(0x153, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_73D7)
    Sleep(50)
    TurnDirection(0xEF, 0x8, 500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)

    #C0350
    ChrTalk(
        0x101,
        "#0005F哎……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7482")
    OP_68(-1290, 1500, 4900, 2500)
    SetChrFlags(0xEF, 0x40)

    def lambda_742E():
        OP_95(0xFE, -2360, 0, 4980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_742E)
    Sleep(50)

    def lambda_744B():
        OP_95(0xFE, -3140, 0, 5670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_744B)
    Sleep(50)

    def lambda_7468():
        OP_95(0xFE, -3710, 0, 4340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_7468)
    Jump("loc_74EC")

    label("loc_7482")

    OP_68(1290, 1500, 4900, 2500)
    SetChrFlags(0xEF, 0x40)

    def lambda_749D():
        OP_95(0xFE, 2360, 0, 4980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_749D)
    Sleep(50)

    def lambda_74BA():
        OP_95(0xFE, 3140, 0, 5670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_74BA)
    Sleep(50)

    def lambda_74D7():
        OP_95(0xFE, 3710, 0, 4340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_74D7)

    label("loc_74EC")

    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    ClearChrFlags(0xEF, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_752A")

    #C0351
    ChrTalk(
        0x102,
        "#0105F您是说……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7581")

    label("loc_752A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_755B")

    #C0352
    ChrTalk(
        0x103,
        "#0205F您的意思是……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7581")

    label("loc_755B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7581")

    #C0353
    ChrTalk(
        0x104,
        "#0305F你是指…？\x02",
    )

    CloseMessageWindow()

    label("loc_7581")


    #C0354
    ChrTalk(
        0x8,
        (
            "那个，哈尔特曼议长\x01",
            "刚才带着几个跟班议员，\x01",
            "气势汹汹地进去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x8,
        (
            "虽然对这种事早就司空见惯了，\x01",
            "但还是有些担心呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#0000F啊，是说那件事啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7672")

    #C0357
    ChrTalk(
        0x102,
        (
            "#0100F虽然稍微有点担心……\x01",
            "不过，我想市长应该是不会有问题的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7717")

    label("loc_7672")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76CA")

    #C0358
    ChrTalk(
        0x103,
        (
            "#0200F虽然稍微有些担心……\x01",
            "不过，市长先生的话，应该没问题的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7717")

    label("loc_76CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7717")

    #C0359
    ChrTalk(
        0x104,
        (
            "#0300F虽然稍微有点担心，\x01",
            "不过，市长先生他肯定应付得了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7717")


    #C0360
    ChrTalk(
        0x8,
        "是吗……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x8,
        (
            "……在这种时候，\x01",
            "我们市政厅的职员总是无能为力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "至少也应该去给\x01",
            "百忙之中的市长\x01",
            "送些慰问品才对……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#0006F……是啊，\x01",
            "我也是这么想的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x153,
        (
            "#1105F要给老爷爷\x01",
            "送东西吗～？\x02\x03",

            "#1110F那就给老爷爷\x01",
            "送些他喜欢吃的东西，\x01",
            "好不好～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    #C0365
    ChrTalk(
        0x101,
        "#0005F有、有道理。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78CD")

    #C0366
    ChrTalk(
        0x102,
        (
            "#0100F确实，要送慰问品的话，\x01",
            "这应该是个很好的选择。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7964")

    label("loc_78CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_791B")

    #C0367
    ChrTalk(
        0x103,
        (
            "#0203F确实，如果要送慰问品的话，\x01",
            "这个选择应该不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7964")

    label("loc_791B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7964")

    #C0368
    ChrTalk(
        0x104,
        (
            "#0304F确实，送慰问品的话，\x01",
            "这应该是个不错的主意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7964")

    TurnDirection(0x101, 0x8, 500)

    #C0369
    ChrTalk(
        0x8,
        "呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        "……那么，各位。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x8,
        (
            "如果方便的话，能不能帮忙\x01",
            "去买些市长喜欢的饮料呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x8,
        (
            "在喷泉广场的果汁店\x01",
            "应该就可以买到了，\x01",
            "就在这附近……\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        (
            "#0000F明白了，\x01",
            "这种小事当然没问题。\x02\x03",

            "那个，您知道市长喜欢的是\x01",
            "哪种饮料吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "具体名称我也不太清楚，\x01",
            "不过好像是平时不会公开销售\x01",
            "的特别饮料呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "只要去问问店主，\x01",
            "应该就能知道了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B0E")

    #C0376
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，那我们就\x01",
            "快点去喷泉广场\x01",
            "的果汁店吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B97")

    label("loc_7B0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B56")

    #C0377
    ChrTalk(
        0x103,
        (
            "#0200F那么，我们就快些去\x01",
            "喷泉广场的果汁店吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B97")

    label("loc_7B56")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B97")

    #C0378
    ChrTalk(
        0x104,
        (
            "#0300F那好，我们赶快去\x01",
            "喷泉广场的果汁店吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B97")


    #C0379
    ChrTalk(
        0x153,
        "#1109F出发啦～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0380
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【给市长的慰问品】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C28")
    SetChrPos(0x0, -2360, 0, 4980, 45)
    Jump("loc_7C39")

    label("loc_7C28")

    SetChrPos(0x0, 2360, 0, 4980, 315)

    label("loc_7C39")

    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x26, 0x4, 0x2)
    EventEnd(0x5)
    Return()

    # Function_18_729B end

    def Function_19_7C51(): pass

    label("Function_19_7C51")

    EventBegin(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch06500.itc", 0x1E)
    LoadChrToIndex("chr/ch27800.itc", 0x1F)
    LoadChrToIndex("chr/ch27400.itc", 0x20)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 8119, 4000, 14200, 315)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7D5A")
    OP_68(-7680, 5500, 15150, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -9250, 4000, 14500, 45)
    SetChrPos(0x153, -10350, 4000, 14450, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D0E")
    SetChrPos(0x102, -9600, 4000, 13150, 45)
    Jump("loc_7D55")

    label("loc_7D0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D34")
    SetChrPos(0x103, -9600, 4000, 13150, 45)
    Jump("loc_7D55")

    label("loc_7D34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D55")
    SetChrPos(0x104, -9600, 4000, 13150, 45)

    label("loc_7D55")

    Jump("loc_7E17")

    label("loc_7D5A")

    OP_68(-4800, 5500, 16000, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -1500, 4000, 14500, 270)
    SetChrPos(0x153, -750, 4000, 15250, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DD0")
    SetChrPos(0x102, -500, 4000, 13750, 270)
    Jump("loc_7E17")

    label("loc_7DD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DF6")
    SetChrPos(0x103, -500, 4000, 13750, 270)
    Jump("loc_7E17")

    label("loc_7DF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E17")
    SetChrPos(0x104, -500, 4000, 13750, 270)

    label("loc_7E17")

    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, -8400, 4000, 20200, 135)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x16, -8800, 4000, 21500, 135)
    SetChrPos(0x17, -9750, 4000, 21050, 135)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_0D()

    #N0381
    NpcTalk(
        0x15,
        "声音",
        "#2P──哼，告辞了。\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x1)

    def lambda_7EEA():
        OP_97(0x15, 0xDAC, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7EEA)

    def lambda_7F04():
        OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_7F04)
    Sleep(50)

    def lambda_7F18():
        OP_97(0x16, 0xDAC, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7F18)

    def lambda_7F32():
        OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_7F32)
    Sleep(50)

    def lambda_7F46():
        OP_97(0x17, 0xDAC, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7F46)

    def lambda_7F60():
        OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_7F60)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)

    #C0382
    ChrTalk(
        0x16,
        (
            "#11P真是的！\x01",
            "怎么会有如此顽固的老人！\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x17,
        (
            "#5P竟然回绝了议长阁下\x01",
            "难得提出的建议……！\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x15,
        (
            "#11P#2702F哼，也罢，\x01",
            "至少也算是给了他一个警告。\x02\x03",

            "#2703F……坎贝尔他们那边，\x01",
            "就像往常一样处理就可以了……\x02\x03",

            "#2701F问题还是鲁巴彻那边，\x01",
            "真是一群没用的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x16,
        "#11P说、说得也是呢！\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x17,
        (
            "#5P全靠议长的支持，他们才能风光下去，\x01",
            "看来有必要再次提醒那些家伙一下，\x01",
            "免得他们忘掉这个事实……\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x15,
        (
            "#11P#2703F嗯，暂时就先\x01",
            "不和马尔克尼会面了。\x02\x03",

            "#2702F还有，已经有很久没开会了，\x01",
            "今天晚上让大家集合一下吧。\x02\x03",

            "给我通知帝国派的所有人。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x16,
        "#11P明白了！\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x17,
        "#5P这就向他们发出紧急召集令！\x02",
    )

    CloseMessageWindow()
    OP_68(6200, 5500, 17600, 6000)
    BeginChrThread(0x15, 3, 0, 20)
    BeginChrThread(0x16, 3, 0, 21)
    BeginChrThread(0x17, 3, 0, 22)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8238")
    Sleep(1000)

    def lambda_820B():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_820B)
    Sleep(50)

    def lambda_821B():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_821B)
    Sleep(50)

    def lambda_822B():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_822B)
    Jump("loc_8268")

    label("loc_8238")

    Sleep(2500)

    def lambda_8240():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8240)
    Sleep(50)

    def lambda_8250():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8250)
    Sleep(50)

    def lambda_8260():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_8260)

    label("loc_8268")

    WaitChrThread(0x15, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x16, 3)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_82D3")
    Fade(500)
    OP_68(-8100, 5500, 13450, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Jump("loc_8307")

    label("loc_82D3")

    Fade(500)
    OP_68(-820, 4500, 15700, 0)
    MoveCamera(11, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    label("loc_8307")


    #C0390
    ChrTalk(
        0x101,
        (
            "#5P#0003F呼……\x01",
            "事情好像已经谈完了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8379")

    #C0391
    ChrTalk(
        0x102,
        (
            "#12P#0100F就趁现在，把慰问品\x01",
            "给外公送去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8406")

    label("loc_8379")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83C1")

    #C0392
    ChrTalk(
        0x103,
        (
            "#12P#0200F就趁现在，把慰问品\x01",
            "送给市长先生吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8406")

    label("loc_83C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8406")

    #C0393
    ChrTalk(
        0x104,
        (
            "#12P#0300F就趁现在，把慰问品\x01",
            "给市长先生送去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8406")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_68(-6390, 5500, 17440, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, -6390, 4000, 17440, 315)
    SetChrPos(0x1, -6390, 4000, 17440, 315)
    SetChrPos(0x153, -6390, 4000, 17440, 315)
    OP_4C(0x9, 0xFF)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x1, 0x0, 0x17)
    SetScenarioFlags(0xBE, 7)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_19_7C51 end

    def Function_20_84B5(): pass

    label("Function_20_84B5")


    def lambda_84BA():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84BA)
    WaitChrThread(0xFE, 1)

    def lambda_84D8():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84D8)
    Sleep(1000)

    def lambda_84E8():
        OP_97(0xFE, 0xFA0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84E8)
    Sleep(2000)

    def lambda_8505():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8505)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_84B5 end

    def Function_21_8516(): pass

    label("Function_21_8516")


    def lambda_851B():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_851B)
    WaitChrThread(0xFE, 1)

    def lambda_8539():
        OP_95(0xFE, 6720, 4000, 19320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8539)
    WaitChrThread(0xFE, 1)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)

    def lambda_856C():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_856C)
    WaitChrThread(0xFE, 1)
    Sleep(2000)

    def lambda_8580():
        OP_95(0xFE, 7210, 4000, 18830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8580)
    WaitChrThread(0xFE, 1)

    def lambda_859E():
        OP_97(0xFE, 0xBB8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_859E)
    Sleep(1000)

    def lambda_85BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_85BB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_8516 end

    def Function_22_85CC(): pass

    label("Function_22_85CC")


    def lambda_85D1():
        OP_97(0xFE, 0x2904, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85D1)
    WaitChrThread(0xFE, 1)

    def lambda_85EF():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85EF)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_8603():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8603)
    WaitChrThread(0xFE, 1)

    def lambda_8621():
        OP_97(0xFE, 0xFA0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8621)
    Sleep(2000)

    def lambda_863E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_863E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_85CC end

    def Function_23_864F(): pass

    label("Function_23_864F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    OP_68(-45000, 1500, 11000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -45750, 0, 1500, 0)
    SetChrPos(0x153, -45000, 0, 2750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86D7")
    SetChrPos(0x102, -44250, 0, 2000, 0)
    Jump("loc_871E")

    label("loc_86D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86FD")
    SetChrPos(0x103, -44250, 0, 2000, 0)
    Jump("loc_871E")

    label("loc_86FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_871E")
    SetChrPos(0x104, -44250, 0, 2000, 0)

    label("loc_871E")

    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -45000, 0, 11500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0394
    ChrTalk(
        0x101,
        (
            "#0000F对不起，\x01",
            "我们又来打扰了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(500)

    #C0395
    ChrTalk(
        0xB,
        (
            "#5P#2500F哦，是你们啊。\x01",
            "刚才真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_87B7():
        OP_98(0x153, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_87B7)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87FE")

    def lambda_87E4():
        OP_98(0x102, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_87E4)
    Jump("loc_8857")

    label("loc_87FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_882D")

    def lambda_8813():
        OP_98(0x103, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8813)
    Jump("loc_8857")

    label("loc_882D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8857")

    def lambda_8842():
        OP_98(0x104, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8842)

    label("loc_8857")

    Sleep(50)

    def lambda_885F():
        OP_98(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_885F)
    OP_68(-45000, 1100, 10500, 3000)
    OP_6F(0x79)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 1)

    #C0396
    ChrTalk(
        0x101,
        (
            "#12P#0001F哪里……\x01",
            "刚才事态好像很棘手呢，辛苦您了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8908")

    #C0397
    ChrTalk(
        0x102,
        (
            "#11P#0108F外公……\x01",
            "那个，您不要紧吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89A3")

    label("loc_8908")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8962")

    #C0398
    ChrTalk(
        0x103,
        (
            "#11P#0200F那些人的态度好像\x01",
            "很不友好，提出的要求也很让您为难……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89A3")

    label("loc_8962")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89A3")

    #C0399
    ChrTalk(
        0x104,
        (
            "#11P#0301F您没事吧？\x01",
            "那些人好像来势不善啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89A3")


    #C0400
    ChrTalk(
        0xB,
        (
            "#5P#2509F哦，那伙人还是很好打发的。\x01",
            "那种程度的威胁，\x01",
            "对我来说不过是家常便饭而已。\x02\x03",

            "#2500F话说回来，你们还有什么事吗？\x01",
            "是不是落下什么东西了？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        (
            "#12P#0005F啊，没有……\x02\x03",

            "#0002F……去吧，琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x153,
        "#6P#1100F嗯。\x02",
    )

    CloseMessageWindow()
    OP_98(0x153, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    SetChrName("")

    #A0403
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅把特制苦西红柿奶昔\x01",
            "交给了麦克道尔市长。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x358, 1)
    OP_98(0x153, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)

    #C0404
    ChrTalk(
        0xB,
        (
            "#5P#2505F这是……我喜欢喝的饮料啊。\x02\x03",

            "难道说……\x01",
            "你们是特意为我买来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x153,
        (
            "#6P#1110F这是大家送给老爷爷的慰问品～\x02\x03",

            "#1109F因为老爷爷看上去一直都\x01",
            "非常努力呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xB,
        "#5P#2509F哦……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#12P#0003F那个，是市政厅的接待员\x01",
            "委托我们给您送慰问品的……\x02\x03",

            "#0000F而且，果汁店的店长\x01",
            "也免费将它赠送给我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xB,
        (
            "#5P#2503F是吗……\x01",
            "确实，这可真是大家\x01",
            "送给我的慰劳品啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D0F")

    #C0409
    ChrTalk(
        0xB,
        (
            "#5P#2500F谢谢你们，罗伊德、艾莉，\x01",
            "还有琪雅。\x02\x03",

            "#2509F托你们的福，我已经精神百倍了，\x01",
            "下午也可以干劲十足地工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x102,
        (
            "#11P#0102F呵呵，不过还是请您不要\x01",
            "太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E88")

    label("loc_8D0F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DC8")

    #C0411
    ChrTalk(
        0xB,
        (
            "#5P#2500F谢谢你们，罗伊德、缇欧，\x01",
            "还有琪雅。\x02\x03",

            "#2509F托你们的福，我已经精神百倍了，\x01",
            "下午也可以干劲十足地工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        (
            "#11P#0200F但最好还是不要\x01",
            "太勉强自己啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E88")

    label("loc_8DC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E88")

    #C0413
    ChrTalk(
        0xB,
        (
            "#5P#2500F谢谢你们，罗伊德、兰迪，\x01",
            "还有琪雅。\x02\x03",

            "#2509F托你们的福，我已经精神百倍了，\x01",
            "下午也可以干劲十足地工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x104,
        (
            "#11P#0300F哈哈，那就好啊，\x01",
            "不过您还是别太勉强自己呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E88")


    #C0415
    ChrTalk(
        0xB,
        (
            "#5P#2503F嗯，对了。\x02\x03",

            "既然收到了让我如此\x01",
            "开心的慰劳品……\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0xB, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    SetChrName("")

    #A0416
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "麦克道尔市长从下面的柜子中\x01",
            "取出了一个小纸包。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F5E")
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jump("loc_8FB3")

    label("loc_8F5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F8B")
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jump("loc_8FB3")

    label("loc_8F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FB3")
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_8FB3")

    OP_97(0xB, 0xFFFFEA84, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0xB, 0xB4, 0x0)

    #C0417
    ChrTalk(
        0xB,
        (
            "#5P#2500F这是共和国的朋友以前\x01",
            "送给我的贵重东方药品。\x02\x03",

            "希望你们能收下。\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0xB, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
    Sleep(500)
    OP_98(0xB, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0418
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1FE, 1)

    #C0419
    ChrTalk(
        0x101,
        (
            "#12P#0005F这、这个……\x01",
            "我们不能收这么贵重的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xB,
        (
            "#5P#2503F不必客气啊，这东西留在我这里也没有用。\x02\x03",

            "而你们这些年轻警察经常会\x01",
            "遭遇危险，正需要它。\x01",
            "我只是希望能物尽其用而已。\x02\x03",

            "#2500F总之，请你们收下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        "#12P#0000F……明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91BF")

    #C0422
    ChrTalk(
        0x102,
        (
            "#11P#0102F呵呵……\x01",
            "那我们就不再客气了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_923A")

    label("loc_91BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91FA")

    #C0423
    ChrTalk(
        0x103,
        "#11P#0202F那么，我们就不客气了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_923A")

    label("loc_91FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_923A")

    #C0424
    ChrTalk(
        0x104,
        "#11P#0309F既然您都这么说了，那就不客气啦！\x02",
    )

    CloseMessageWindow()

    label("loc_923A")


    #C0425
    ChrTalk(
        0x153,
        "#6P#1109F老爷爷～谢谢啦～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0426
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【给市长的慰问品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xB, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_68(-45000, 1500, 12000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -45000, 0, 12000, 0)
    SetChrPos(0x1, -45000, 0, 12000, 0)
    SetChrPos(0x153, -45000, 0, 12000, 0)
    SetChrPos(0xB, -45000, 250, 14700, 180)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_29(0x26, 0x4, 0x10)
    OP_29(0x26, 0x1, 0x6)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_23_864F end

    def Function_24_9351(): pass

    label("Function_24_9351")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(0, 1100, 6000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x103, -700, 0, 3600, 0)
    SetChrPos(0x104, 700, 0, 3600, 0)
    OP_0D()

    #C0427
    ChrTalk(
        0x8,
        (
            "#5P欢迎。\x01",
            "欢迎来到克洛斯贝尔市政厅。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_9465")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0428
    ChrTalk(
        0x8,
        (
            "#5P啊……\x01",
            "各位好像是警察吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        "#5P是要与哪位工作人员会面吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9524")

    label("loc_9465")


    #C0430
    ChrTalk(
        0x8,
        "#5P来此有何贵干呢？\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#12P#0000F是的，我们是克洛斯贝尔\x01",
            "警察局的人……\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrName("")

    #A0432
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将调查手册出示给对方。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0433
    ChrTalk(
        0x8,
        "#5P啊，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        "#5P那么，是要与哪位工作人员会面吗？\x02",
    )

    CloseMessageWindow()

    label("loc_9524")


    #C0435
    ChrTalk(
        0x102,
        "#0103F不，其实是……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0436
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "提出了为进行调查工作，\x01",
            "希望能借用一下地下空间Ｂ区域的钥匙。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0437
    ChrTalk(
        0x8,
        (
            "#5P地下空间Ｂ区域……\x01",
            "应该是城市西北部的那个区域吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x8,
        "#5P请稍等一下。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_95ED():
        OP_95(0xFE, 0, 0, 9400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_95ED)
    OP_0D()
    WaitChrThread(0x8, 1)
    Sleep(500)
    OP_93(0x8, 0x0, 0x0)

    def lambda_9616():
        OP_95(0xFE, 0, 0, 7400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9616)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)

    #C0439
    ChrTalk(
        0x8,
        "#5P就是这把。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0440
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x322),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x322, 1)

    #C0441
    ChrTalk(
        0x101,
        "#12P#0002F多谢，那我们就暂时借用一下了。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x103,
        (
            "#12P#0200F不过，竟然这么爽快\x01",
            "就借给我们了啊……？\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x8,
        (
            "#5P嗯，因为上面吩咐我们要尽量\x01",
            "协助克洛斯贝尔警察局的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x8,
        (
            "#5P顺便一说，我们也将同样的钥匙\x01",
            "借给游击士协会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x101,
        "#12P#0012F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x8,
        (
            "#5P地下空间Ｂ区域的入口\x01",
            "就在住宅街的水道附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x8,
        (
            "#5P以前就曾有人把钥匙弄丢过，\x01",
            "所以还请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        "#0100F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x104,
        "#12P#0309F这位姐姐，多谢啦。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 4000, 180)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x83, 2)
    OP_29(0x43, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_24_9351 end

    def Function_25_985D(): pass

    label("Function_25_985D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x12, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_68(0, 900, 6560, 0)
    MoveCamera(54, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -650, 0, -3500, 0)
    SetChrPos(0x102, 650, 0, -3500, 0)
    SetChrPos(0x103, -900, 0, -4800, 0)
    SetChrPos(0x104, 900, 0, -4800, 0)
    FadeToBright(2000, 0)
    OP_0D()

    #C0450
    ChrTalk(
        0x8,
        (
            "#5P最便宜的出租公寓……\x01",
            "……是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x8,
        (
            "#5P我们这里有些资料，\x01",
            "应该可以作为您的参考……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x12,
        (
            "#12P#1805F啊，原来还有这种租房指南呀！\x02\x03",

            "#1809F太好了……\x01",
            "………这本手册，\x01",
            "我可不可以借去看看呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x8,
        (
            "#5P嗯，这是可以随意领取的，\x01",
            "直接拿回去看也没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x8,
        "#5P不过，那个，太便宜的地方其实有些……\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x12,
        (
            "#12P#1806F呼，必须要早点找到住所，\x01",
            "集中精神来练习啊……\x02\x03",

            "#1802F#3S……啊，不好意思。\x01",
            "非常感谢你为我介绍。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)
    OP_68(0, 1500, -1030, 3000)

    def lambda_9AA3():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AA3)
    Sleep(50)

    def lambda_9AC0():
        OP_95(0xFE, 0, 0, 1140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9AC0)

    def lambda_9ADA():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9ADA)
    Sleep(50)

    def lambda_9AF7():
        OP_98(0x103, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9AF7)
    Sleep(50)

    def lambda_9B14():
        OP_98(0x104, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9B14)
    Sleep(350)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0456
    ChrTalk(
        0x12,
        "#5P#1805F啊，对不起！\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        "#12P#0005F哪里，应该是我们道歉才对……\x02",
    )

    CloseMessageWindow()

    def lambda_9B9D():
        OP_98(0x101, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B9D)
    Sleep(50)

    def lambda_9BBA():
        OP_98(0x102, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9BBA)
    Sleep(25)

    def lambda_9BD7():
        OP_98(0x103, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9BD7)
    Sleep(25)

    def lambda_9BF4():
        OP_98(0x104, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BF4)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x0)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x0)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x2D, 0x0)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x13B, 0x0)

    #C0458
    ChrTalk(
        0x12,
        "#5P#1804F………………（低头行礼）\x02",
    )

    CloseMessageWindow()

    def lambda_9C61():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFDF94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9C61)
    Sleep(500)

    def lambda_9C7E():

        label("loc_9C7E")

        TurnDirection(0x101, 0x12, 500)
        Yield()
        Jump("loc_9C7E")

    QueueWorkItem2(0x101, 2, lambda_9C7E)

    def lambda_9C90():

        label("loc_9C90")

        TurnDirection(0x102, 0x12, 500)
        Yield()
        Jump("loc_9C90")

    QueueWorkItem2(0x102, 2, lambda_9C90)

    def lambda_9CA2():

        label("loc_9CA2")

        TurnDirection(0x103, 0x12, 500)
        Yield()
        Jump("loc_9CA2")

    QueueWorkItem2(0x103, 2, lambda_9CA2)

    def lambda_9CB4():

        label("loc_9CB4")

        TurnDirection(0x104, 0x12, 500)
        Yield()
        Jump("loc_9CB4")

    QueueWorkItem2(0x104, 2, lambda_9CB4)
    Sleep(1200)

    def lambda_9CC9():
        OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9CC9)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x12, 2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    Sleep(300)

    #C0459
    ChrTalk(
        0x101,
        "#5P#0000F那个女孩，好像是刚才见过的那个……\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        (
            "#5P#0102F呵呵，好像总能\x01",
            "和她巧遇啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, -1720, 0)
    OP_4C(0x12, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x53, 0)
    EventEnd(0x5)
    Return()

    # Function_25_985D end

    def Function_26_9D75(): pass

    label("Function_26_9D75")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 1200, 6000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x103, -700, 0, 3600, 0)
    SetChrPos(0x104, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0461
    ChrTalk(
        0x8,
        (
            "#5P这里是克洛斯贝尔\x01",
            "市政厅的接待处。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "#5P如果想支付各种费用，\x01",
            "或是申请迁居，\x01",
            "就请来这里办理手续吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#12P#0000F那个，不好意思。\x01",
            "我们是克洛斯贝尔警察局的人。\x02\x03",

            "前来处理市政厅\x01",
            "发来的支援请求……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0464
    ChrTalk(
        0x8,
        "#5P啊，原来各位是警察局的人啊！\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x8,
        (
            "#5P太好了，来得这么早，\x01",
            "真是出乎意料呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#11P#0100F呵呵，可以请您尽快\x01",
            "将委托的内容交代给我们吗？\x02\x03",

            "好像是关于确认\x01",
            "无人住所之类的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x8,
        "#5P嗯，我立刻进行说明。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        (
            "#5P……各位应该知道\x01",
            "什么是『住户登记』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x8,
        (
            "#5P市民在搬到克洛斯贝尔定居\x01",
            "的时候，都要来这里\x01",
            "进行住户登记申请。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x8,
        (
            "#5P可是……实际上，也有很多人在没有\x01",
            "经过申请的情况下就直接入住或离开。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "#5P我们市政厅也无法\x01",
            "完全掌握到具体情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x103,
        "#12P#0200F是吗……\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x8,
        (
            "#5P所以，希望各位能\x01",
            "帮忙确认一下空房。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x8,
        (
            "#5P特别是，在登记为空房的住所中，\x01",
            "可能也会存在一些不准确的记录。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        (
            "#5P居民科的人好像也\x01",
            "没空来处理……\x01",
            "所以希望各位能帮忙进行确认。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x104,
        (
            "#0300F总而言之，也就是让我们\x01",
            "替政府机关的大人物们跑一趟嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0477
    ChrTalk(
        0x101,
        (
            "#12P#0006F兰迪，这么说也太失礼了。\x02\x03",

            "#0001F说起空房，从防止犯罪的角度来说，\x01",
            "也绝对是一项不容忽视的问题。\x01",
            "所以确认工作还是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x104,
        "#0305F哦，原来还有这种说法啊。\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x102,
        (
            "#11P#0100F算了，只不过是在市内转一圈而已，\x01",
            "也不是什么坏事嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x8,
        (
            "#5P……那个，既然如此，\x01",
            "各位愿意接受这项工作吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_29(0x3, 0x1, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A352")
    Call(0, 28)
    Return()

    label("loc_A352")


    #C0481
    ChrTalk(
        0x101,
        (
            "#12P#0006F抱歉，\x01",
            "虽然大致情况已经了解了，\x01",
            "但我们现在还有其它工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x8,
        (
            "#5P是吗……那就麻烦各位\x01",
            "有空的时候再来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x8,
        (
            "#5P只要是在今天之内，\x01",
            "随便什么时候都可以的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, 4000, 180)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x1, 0x1F)
    EventEnd(0x5)
    Return()

    # Function_26_9D75 end

    def Function_27_A42C(): pass

    label("Function_27_A42C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 1200, 6000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x103, -700, 0, 3600, 0)
    SetChrPos(0x104, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0484
    ChrTalk(
        0x8,
        (
            "#5P希望各位能帮忙\x01",
            "确认一下市内的空房。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x8,
        (
            "#5P居民科的人好像也\x01",
            "没空来处理……\x01",
            "各位愿意接受这项工作吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_29(0x3, 0x1, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A57F")
    Call(0, 28)
    Return()

    label("loc_A57F")


    #C0486
    ChrTalk(
        0x101,
        (
            "#12P#0006F抱歉，\x01",
            "虽然大致情况已经了解了，\x01",
            "但我们现在还有其它工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x8,
        (
            "#5P是吗……那就麻烦各位\x01",
            "有空的时候再来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x8,
        (
            "#5P只要是在今天之内，\x01",
            "随便什么时候都可以的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, 4000, 180)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x1, 0x1F)
    EventEnd(0x5)
    Return()

    # Function_27_A42C end

    def Function_28_A659(): pass

    label("Function_28_A659")

    OP_29(0x3, 0x2, 0x1F)

    #C0489
    ChrTalk(
        0x8,
        (
            "#5P非常感谢，\x01",
            "那我这就把文件交给你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x8,
        (
            "#5P……这就是此次工作\x01",
            "的相关文件。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x101,
        "#12P#0000F嗯，那就暂时由我们保管了。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_95(0x101, -70, 0, 5240, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0492
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x35A, 1)
    OP_96(0x101, 0xFFFFFDA8, 0x0, 0x125C, 0x3E8, 0x0)
    Sleep(400)

    def lambda_A762():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A762)
    Sleep(200)

    def lambda_A772():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A772)

    def lambda_A77F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A77F)

    def lambda_A78C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A78C)
    Sleep(500)

    #C0493
    ChrTalk(
        0x101,
        (
            "#6P#0005F嗯，一共有三处啊。\x02\x03",

            "#0003F住宅街有一处。\x01",
            "看起来，好像在接近出口的位置呢。\x02\x03",

            "东街也有一处……\x01",
            "从地址来看，好像紧挨着\x01",
            "游击士协会的右侧啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A8FA")

    #C0494
    ChrTalk(
        0x104,
        (
            "#0300F挨着协会的右边吗？\x01",
            "那倒是很好记啊。\x02\x03",

            "#0305F最后的一处……好像在旧城区啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x102,
        (
            "#11P#0103F旧城区的公寓\x01",
            "『莲花公馆』有三处空房……\x02\x03",

            "#0105F稍等一下，\x01",
            "我先把这些记录在调查手册里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9D6")

    label("loc_A8FA")


    #C0496
    ChrTalk(
        0x104,
        (
            "#0303F挨着协会的右边吗？\x01",
            "那倒是很好记啊。\x02\x03",

            "#0305F最后的这个地方……\x01",
            "是在哪里啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        (
            "#11P#0100F这个地方，如今被称作旧城区哦。\x02\x03",

            "#0103F『莲花公馆』公寓中\x01",
            "有三处空房……\x02\x03",

            "#0105F稍等一下，\x01",
            "我先把这些记录在调查手册里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9D6")


    #C0498
    ChrTalk(
        0x102,
        "#11P#0103F（认真记录……）\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    #C0499
    ChrTalk(
        0x102,
        "#11P#0100F嗯，记好了。\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#6P#0000F谢啦，艾莉。\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_AA38():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA38)

    def lambda_AA45():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA45)

    def lambda_AA52():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AA52)

    def lambda_AA5F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA5F)
    Sleep(500)

    #C0501
    ChrTalk(
        0x101,
        (
            "#12P#0000F那我们现在就出发，\x01",
            "去确认那些空房吧。\x02\x03",

            "完成之后，来这里报告就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x8,
        (
            "#5P嗯，三处空房都确认完毕之后，\x01",
            "过来通知我就可以了。\x01",
            "拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0503
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【无人住所的确认】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 1500, 4000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 0, 0, 4000, 0)
    SetChrPos(0x1, 0, 0, 4000, 0)
    SetChrPos(0x2, 0, 0, 4000, 0)
    SetChrPos(0x3, 0, 0, 4000, 0)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_A659 end

    def Function_29_ABEA(): pass

    label("Function_29_ABEA")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 1200, 6000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x103, -700, 0, 3600, 0)
    SetChrPos(0x104, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0504
    ChrTalk(
        0x8,
        (
            "#5P啊，各位，\x01",
            "确认空房的工作还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，已经全部\x01",
            "确认完毕了，\x01",
            "现在就来报告。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_95(0x101, -70, 0, 5240, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    Sleep(400)
    SetChrName("")

    #A0506
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "提交了修正过错误的文件。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Sleep(300)
    OP_96(0x101, 0xFFFFFDA8, 0x0, 0x125C, 0x3E8, 0x0)
    Sleep(400)
    SubItemNumber(0x35A, 1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0507
    ChrTalk(
        0x8,
        (
            "#5P啊，标记了房间号，\x01",
            "旁边还加上了批注呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x8,
        (
            "#5P真是太感谢了，\x01",
            "居民科的人一定也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x104,
        (
            "#0306F哈哈，不过，\x01",
            "如果可以的话，希望他们能把\x01",
            "列表整理得稍微像样一点啊。\x02\x03",

            "错漏百出，害得我们\x01",
            "四处乱跑，走了不少冤枉路呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x103,
        (
            "#12P#0200F身为警察，我们也许\x01",
            "无权指责这些，\x01",
            "但管理未免也太混乱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x8,
        (
            "#5P真、真抱歉……\x01",
            "居民科的人其实也在努力，\x01",
            "希望能确保资料的正确性。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x8,
        (
            "#5P……但他们那边经常会承受\x01",
            "很多来自议员们的压力……\x01",
            "所以，实在是非常抱歉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#12P#0005F哪、哪里……原来还有这种事啊。\x01",
            "（看来，在政府机关里也会有很多麻烦事呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x102,
        (
            "#11P#0108F（嗯……在克洛斯贝尔，\x01",
            "  议员的力量是相当强大的……）\x02\x03",

            "#0100F总之，能帮上忙就好。\x02\x03",

            "毕竟市政厅的人也不容易……\x01",
            "如果以后再有什么事情，欢迎来找我们支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x103,
        (
            "#12P#0200F是啊，像这种程度的事情，\x01",
            "我们应该能帮上一点忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        "#0300F哈，总之不用客气，有事就随时开口吧。\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x8,
        (
            "#5P好的……非常感谢。\x01",
            "那到时候就麻烦各位了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0518
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【无人住所的确认】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(0, 1500, 4000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 0, 0, 4000, 0)
    SetChrPos(0x1, 0, 0, 4000, 0)
    SetChrPos(0x2, 0, 0, 4000, 0)
    SetChrPos(0x3, 0, 0, 4000, 0)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x2, 0x1E)
    OP_29(0x3, 0x1, 0x8)
    OP_29(0x3, 0x4, 0x10)
    SetScenarioFlags(0x0, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_ABEA end

    def Function_30_B1B6(): pass

    label("Function_30_B1B6")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4650, 5200, 16390, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 4160, 4000, 16219, 0)
    SetChrPos(0x102, 5480, 4000, 16219, 0)
    SetChrPos(0x103, 4160, 4000, 14800, 0)
    SetChrPos(0x104, 5480, 4000, 14800, 0)
    SetChrPos(0x9, 4870, 4000, 18550, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    FadeToBright(1000, 0)
    OP_0D()

    #C0519
    ChrTalk(
        0x9,
        (
            "#5P呼啊啊，真是的，\x01",
            "怎么会有这种事……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0520
    ChrTalk(
        0x9,
        (
            "#5P啊，你们！\x01",
            "是警察局·特别任务支援科的人，没错吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x9, 4870, 4000, 17950, 2000, 0x0)

    #C0521
    ChrTalk(
        0x101,
        (
            "#6P#0000F是的，没错。\x01",
            "我们是为了接受支援请求而来的。\x02\x03",

            "那个，听说是出了\x01",
            "很严重的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x102,
        "#12P#0100F莫非是什么东西被盗了吗？\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x9,
        "#5P那、那个……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0x1F4)

    #C0524
    ChrTalk(
        0x9,
        (
            "#5P#4S正是如此啊！！\x01",
            "有个非常重要的东西被盗走了！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0525
    ChrTalk(
        0x103,
        "#12P#0205F原来还真的是盗窃案啊。\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x104,
        (
            "#12P#0305F竟然能从市政厅里\x01",
            "把东西偷走？\x02\x03",

            "#0306F虽然早就知道纪念庆典中应该会有很多风波，\x01",
            "但真没想到会出现这么胆大妄为的家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        "#6P#0001F那么，被盗走的东西是……\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x9,
        (
            "#5P啊啊……就是原本放置在那里的\x01",
            "巨大雕像啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2790, 4200, 19050, 2000)
    MoveCamera(26, 25, 0, 2000)

    def lambda_B56D():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B56D)

    def lambda_B57A():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B57A)

    def lambda_B587():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B587)

    def lambda_B594():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B594)

    def lambda_B5A1():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B5A1)
    Sleep(2000)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)

    #C0529
    ChrTalk(
        0x101,
        (
            "#6P#0003F这、这么一说……\x01",
            "好像确实能感觉到\x01",
            "那里缺了点什么东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x103,
        (
            "#12P#0205F真的被盗了呢。\x01",
            "……稍微有些难以置信。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x9,
        (
            "#5P我也是一样\x01",
            "难以置信啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(4650, 5200, 16390, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_B6D6():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B6D6)
    Sleep(10)

    def lambda_B6E6():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B6E6)

    def lambda_B6F3():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B6F3)
    Sleep(18)

    def lambda_B703():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B703)
    Sleep(300)

    #C0532
    ChrTalk(
        0x9,
        (
            "#5P那座雕像名叫『圣徒的祈祷』，\x01",
            "是克洛斯贝尔自治州刚刚成立之际，\x01",
            "由著名的雕刻家创作的雕像作品。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x102,
        (
            "#12P#0100F马格纳斯·海克特创作的\x01",
            "『圣徒的祈祷』啊。\x02\x03",

            "#0103F出生于克洛斯贝尔的稀世雕刻家，\x01",
            "为了歌颂自治州的诞生所雕刻出的杰作……\x02\x03",

            "#0100F据我所知，正因为它有着那样的历史背景，\x01",
            "所以一直都被视为市政厅的象征呢。\x02\x03",

            "#0108F但在这座雕像的面前，召开那种\x01",
            "让帝国派与共和国派谋取私利的议会，\x01",
            "倒真是很具有讽刺意义呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x9,
        "#5P哈哈，我完全赞同。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x9,
        (
            "#5P算了，先不管这些。\x01",
            "总之，那座雕像可以说是克洛斯贝尔\x01",
            "的骄傲，绝对是十分重要的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x9,
        (
            "#5P更何况，今天下午还要举办\x01",
            "闭幕式与宾客的招待会……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x9,
        (
            "#5P呼，在这种难得的庆祝日，\x01",
            "实在是不能让大家看到\x01",
            "这种丢脸的情景啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x101,
        (
            "#6P#0003F确实如此，再这么下去，\x01",
            "克洛斯贝尔将会成为各国的笑料。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x104,
        (
            "#12P#0301F至少克洛斯贝尔警察的\x01",
            "形象与公信力会一落千丈吧。\x02\x03",

            "#0306F克洛斯贝尔时代周刊之类的媒体\x01",
            "肯定也会再写一堆恐怖的讽刺文章。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(8)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1400)

    #C0540
    ChrTalk(
        0x103,
        (
            "#12P#0203F兰迪前辈……\x01",
            "请不要说那些多余的话了。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        (
            "#12P#0306F不好意思啊，只是我的\x01",
            "脑子里一下就想到这些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#6P#0003F这些情况都很有可能成真，\x01",
            "就这点来说，也完全让人笑不出来啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x9,
        (
            "#5P呼……还是别再说这种\x01",
            "不吉利的话了……\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x9,
        (
            "#5P市政厅本来就已经\x01",
            "丑闻不断，屡遭曝光了，\x01",
            "所以经不起这么大的折腾了……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x102,
        (
            "#12P#0103F看来，我们还是尽早展开调查为好啊……\x02\x03",

            "#0105F不过，库利普先生，\x01",
            "您有什么关于犯人的线索吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x9,
        (
            "#5P啊……这个嘛，\x01",
            "在现场倒是发现了这种东西。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0547
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "库利普掏出了一张卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0548
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "警察局特别任务支援科的诸位，\x01",
            "挑战我的谜题，以展现你们的智慧吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　    最初的钥匙\x01",
            "  在不夜之城的象征处\x01",
            "抬头仰望那昏暗的天空吧\x01",
            "　　　　    ──怪盗Ｂ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0550
    ChrTalk(
        0x101,
        "#6P#0005F怪……怪盗Ｂ……！？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#12P#0105F……他竟然会现身于克洛斯贝尔……\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x104,
        (
            "#12P#0300F哈，只是一个偷东西的贼而已，\x01",
            "竟然还给自己取个\x01",
            "那么拉风帅气的外号。\x02\x03",

            "#0303F……嗯？等一下，那个名字……\x01",
            "我以前好像在什么地方听到过呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x103,
        (
            "#12P#0203F我也感觉好像\x01",
            "有所耳闻呢。\x02\x03",

            "#0200F……你们两位\x01",
            "知道些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#6P#0003F我也只是稍有耳闻而已……\x02\x03",

            "#0001F好像是个在外国不断犯案，\x01",
            "超级有名的犯罪者。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x102,
        (
            "#12P#0103F……以帝国为中心进行活动，\x01",
            "曾经盗走过无数美术珍品，\x01",
            "是个神出鬼没的怪人……\x02\x03",

            "#0100F这就是被称为『怪盗Ｂ』的人物。\x02\x03",

            "他的行动非常胆大妄为，在行动之前，\x01",
            "总要事先送出记录着犯罪预告的卡片。\x01",
            "但从来都没有被逮捕过。\x02\x03",

            "他会使用多种不可思议的神奇秘术，\x01",
            "轻而易举地将目标完美盗走。\x01",
            "所以也有一些人视他为英雄……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x103,
        (
            "#12P#0203F也就是说，那个怪盗……\x01",
            "这次是将挑战书\x01",
            "发给了我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x9,
        (
            "#5P嗯，所以这次没有找游击士，\x01",
            "而是叫你们来帮忙，原因就在这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x9,
        (
            "#5P因为他清清楚楚地指名\x01",
            "要你们『特别任务支援科』来处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x104,
        "#12P#0304F……嘿，还挺有意思的嘛。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    #C0560
    ChrTalk(
        0x104,
        (
            "#12P#0300F喂，罗伊德，\x01",
            "虽然不清楚这怪盗究竟是何方神圣，\x01",
            "但不管怎么样，我们赶快去抓住他吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C245():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C245)

    def lambda_C252():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C252)

    def lambda_C25F():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C25F)
    Sleep(300)

    #C0561
    ChrTalk(
        0x101,
        (
            "#6P#0001F嗯，被他盗走的雕像\x01",
            "也必须要夺回来……\x01",
            "他的挑战，我们接受了！\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x102,
        "#12P#0100F说得对，我们行动吧。\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x103,
        (
            "#12P#0200F谜题的提示是\x01",
            "『不夜之城的象征』啊……\x01",
            "看样子，应该就在市内吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x104,
        (
            "#12P#0300F好，那我们就在市内\x01",
            "寻找线索吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0565
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【市政厅的紧急请求】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5080, 4000, 14410, 180)
    OP_4C(0x9, 0xFF)
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x22, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_B1B6 end

    def Function_31_C3DD(): pass

    label("Function_31_C3DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C41B")
    OP_95(0xFE, 3550, 4000, 18550, 1000, 0x0)
    Sleep(200)
    OP_95(0xFE, 5980, 4000, 18550, 1000, 0x0)
    Sleep(200)
    Jump("Function_31_C3DD")

    label("loc_C41B")

    Return()

    # Function_31_C3DD end

    def Function_32_C41C(): pass

    label("Function_32_C41C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch26000.itc", 0x1E)
    OP_4B(0x9, 0xFF)
    OP_68(-40, 5500, 20590, 0)
    MoveCamera(1, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25270, 0)
    SetChrPos(0x101, -580, 4000, 15800, 0)
    SetChrPos(0x102, 550, 4000, 15800, 0)
    SetChrPos(0x103, -580, 4000, 14500, 0)
    SetChrPos(0x104, 550, 4000, 14500, 0)
    SetChrPos(0x9, -1850, 4000, 16820, 45)
    SetChrPos(0x13, -1790, 4000, 19380, 90)
    SetChrPos(0x14, 470, 4000, 18500, 0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x1)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x1)
    BeginChrThread(0x13, 0, 0, 0)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetMapObjFrame(0xFF, "model06", 0x1, 0x1)
    MoveCamera(1, 19, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x40)
    Fade(800)
    OP_68(30, 4500, 17170, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(19220, 0)
    OP_0D()

    #C0566
    ChrTalk(
        0x9,
        (
            "#6P真没想到，竟然这么快\x01",
            "就找回来了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C5A6():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C5A6)
    Sleep(20)

    def lambda_C5B6():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C5B6)
    Sleep(12)

    def lambda_C5C6():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C5C6)

    def lambda_C5D3():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C5D3)
    Sleep(15)

    def lambda_C5E3():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C5E3)
    Sleep(400)

    #C0567
    ChrTalk(
        0x9,
        (
            "#6P支援科的各位，真是多谢了。\x01",
            "我发自内心地感谢你们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        (
            "#11P#0012F哈哈哈……虽然费了不少周折，\x01",
            "但最终能顺利解决，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x14, 1, 0, 33)

    #C0569
    ChrTalk(
        0x102,
        (
            "#11P#0100F这样一来，闭幕式和招待会\x01",
            "也就可以顺利进行了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x9,
        (
            "#6P嗯，是啊。\x01",
            "如此一来，我也就可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 1)
    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)

    def lambda_C6FB():
        OP_95(0xFE, -1570, 4000, 18500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C6FB)
    OP_95(0x14, -1570, 4000, 18500, 1000, 0x0)
    OP_95(0x14, -490, 4000, 18500, 1000, 0x0)
    OP_93(0x14, 0xB4, 0x1F4)

    #C0571
    ChrTalk(
        0x13,
        "#5P好，安放完毕了！\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x14,
        "#11P感谢您的惠顾～！\x02",
    )

    CloseMessageWindow()

    def lambda_C777():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C777)
    Sleep(20)

    def lambda_C787():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C787)
    Sleep(12)

    def lambda_C797():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C797)

    def lambda_C7A4():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C7A4)
    Sleep(15)

    def lambda_C7B4():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C7B4)
    Sleep(300)

    #C0573
    ChrTalk(
        0x9,
        (
            "#6P噢，好的，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x104,
        "#12P#0300F多谢，帮大忙了啊。\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x13,
        "#5P哈哈，可真是件不得了的大行李啊。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x14,
        (
            "#11P那么，我就先\x01",
            "失陪啦～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C850():

        label("loc_C850")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_C850")

    QueueWorkItem2(0x0, 1, lambda_C850)

    def lambda_C862():

        label("loc_C862")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_C862")

    QueueWorkItem2(0x1, 1, lambda_C862)

    def lambda_C874():

        label("loc_C874")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_C874")

    QueueWorkItem2(0x2, 1, lambda_C874)

    def lambda_C886():

        label("loc_C886")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_C886")

    QueueWorkItem2(0x3, 1, lambda_C886)

    def lambda_C898():

        label("loc_C898")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_C898")

    QueueWorkItem2(0x9, 1, lambda_C898)
    BeginChrThread(0x13, 0, 0, 34)
    BeginChrThread(0x14, 0, 0, 34)
    Sleep(3500)

    #C0577
    ChrTalk(
        0x9,
        (
            "#6P呼……也给他们\x01",
            "添了不少麻烦啊。\x01",
            "稍后可得多给人家些小费才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_C923():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C923)

    def lambda_C930():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C930)

    def lambda_C93D():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C93D)

    def lambda_C94A():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C94A)

    def lambda_C957():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C957)
    Sleep(300)

    #C0578
    ChrTalk(
        0x9,
        (
            "#6P对了对了，作为我个人的褒奖，\x01",
            "也要送给你们一些薄礼。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x9, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(200)
    SetChrName("")
    Sound(17, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0579
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从库利普主任处收下了包裹。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_9B(0x1, 0x9, 0xB4, 0x1F4, 0x3E8, 0x0)

    #C0580
    ChrTalk(
        0x101,
        (
            "#11P#0005F这可真是……\x01",
            "多谢您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x9,
        (
            "#6P那么，我就先失陪了，\x01",
            "还得去送送搬运公司\x01",
            "的员工呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CA66():

        label("loc_CA66")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_CA66")

    QueueWorkItem2(0x0, 1, lambda_CA66)

    def lambda_CA78():

        label("loc_CA78")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_CA78")

    QueueWorkItem2(0x1, 1, lambda_CA78)

    def lambda_CA8A():

        label("loc_CA8A")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_CA8A")

    QueueWorkItem2(0x2, 1, lambda_CA8A)

    def lambda_CA9C():

        label("loc_CA9C")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_CA9C")

    QueueWorkItem2(0x3, 1, lambda_CA9C)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_95(0x9, -7660, 4000, 12460, 2000, 0x0)
    Sleep(300)

    #C0582
    ChrTalk(
        0x104,
        "#12P#0303F呼，一块石头落了地啊。\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x102,
        (
            "#11P#0100F虽然四处奔波、不断碰壁，\x01",
            "但总算顺利解决了。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x103, 0x1)
    TurnDirection(0x103, 0x101, 400)
    Sleep(200)

    #C0584
    ChrTalk(
        0x103,
        (
            "#12P#0205F罗伊德前辈，包裹里\x01",
            "是什么东西呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        "#5P#0005F啊，对了，我看看。\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_CBAF():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CBAF)

    def lambda_CBBC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CBBC)

    def lambda_CBC9():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CBC9)

    def lambda_CBD6():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CBD6)
    Sleep(400)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0586
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "包裹中装有『射手珠』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0587
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0xA1, 1)

    #C0588
    ChrTalk(
        0x103,
        (
            "#12P#0200F这是……结晶回路啊。\x01",
            "看起来，好像是无法通过一般渠道\x01",
            "购得的种类呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x104,
        (
            "#12P#0305F市政厅的职员会有这种东西，\x01",
            "还真有些令人意外啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x101,
        (
            "#5P#0005F是啊，他为什么会有\x01",
            "这种东西……\x02",
        )
    )

    CloseMessageWindow()
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -15910, 4000, 10130, 39)

    #N0591
    NpcTalk(
        0x9,
        "男性的声音",
        "啊啊，各位……！\x02",
    )

    CloseMessageWindow()
    SetMapObjFlags(0x3, 0x4)

    def lambda_CD53():

        label("loc_CD53")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_CD53")

    QueueWorkItem2(0x0, 1, lambda_CD53)

    def lambda_CD65():

        label("loc_CD65")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_CD65")

    QueueWorkItem2(0x1, 1, lambda_CD65)

    def lambda_CD77():

        label("loc_CD77")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_CD77")

    QueueWorkItem2(0x2, 1, lambda_CD77)

    def lambda_CD89():

        label("loc_CD89")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_CD89")

    QueueWorkItem2(0x3, 1, lambda_CD89)
    OP_68(-12890, 5500, 12540, 2200)
    Sleep(2200)

    def lambda_CDAF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CDAF)
    OP_68(-1650, 5500, 16000, 3500)
    OP_95(0x9, -9550, 4000, 14890, 4000, 0x0)
    OP_95(0x9, -4010, 4000, 16140, 4000, 0x0)
    OP_6F(0x1)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    #C0592
    ChrTalk(
        0x9,
        (
            "#6P听说雕像已经找回来了，\x01",
            "是真的吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x1F4)
    Sleep(100)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0593
    ChrTalk(
        0x9,
        (
            "#6P哦，是真的！\x01",
            "是你们帮忙找到的吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x9,
        (
            "#6P竟然都已经搬回来了，\x01",
            "哎呀，真是了不起啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(200)

    #C0595
    ChrTalk(
        0x9,
        "#6P太感谢了，特别任务支援科的诸位！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0596
    ChrTalk(
        0x101,
        (
            "#11P#0005F那、那个，库利普先生……\x01",
            "您不是刚刚才\x01",
            "从市政厅出去了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x9,
        "#6P哎，你在说什么啊？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x9,
        (
            "#6P我刚才一直在对面的大厅里\x01",
            "商讨闭幕式的相关事宜。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x102,
        (
            "#11P#0105F难、难道说……\x01",
            "……怎么会…………\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        (
            "#12P#0203F那就是怪盗Ｂ的易容术吗……\x01",
            "实在是太惊人了……\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x104,
        (
            "#12P#0301F真不愧是国际有名的怪盗……\x01",
            "好像不是那么轻易就能抓到的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x9,
        "#6P那个，怎么了吗？\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x9,
        (
            "#6P不管怎么说，真是多谢各位了！\x01",
            "这样一来，就能安心召开闭幕式啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x101,
        (
            "#11P#0000F哈哈哈，是啊。\x02\x03",

            "#0003F（怪盗Ｂ吗……\x01",
            "  虽然看起来好像没有什么恶意，\x01",
            "  但毫无疑问是个犯罪者呢。）\x02\x03",

            "#0001F（真希望有朝一日能与他\x01",
            "  做个彻底的了断啊……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0605
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【市政厅的紧急请求】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 0, -2210, 180)
    OP_4C(0x9, 0xFF)
    OP_D5(0x1E)
    ClearMapObjFlags(0x3, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0x9, -1820, 4000, 17030, 225)
    SetChrPos(0xD, -3170, 4000, 16140, 45)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xD, 0x10)
    OP_29(0x22, 0x4, 0x10)
    OP_29(0x22, 0x1, 0x7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_C41C end

    def Function_33_D241(): pass

    label("Function_33_D241")

    OP_95(0x14, -1610, 4000, 18500, 1000, 0x0)
    OP_93(0x14, 0x0, 0x1F4)
    OP_93(0x13, 0xB4, 0x1F4)
    Return()

    # Function_33_D241 end

    def Function_34_D264(): pass

    label("Function_34_D264")

    OP_95(0xFE, -4770, 4000, 17860, 2000, 0x0)
    OP_95(0xFE, -8119, 4000, 12220, 2000, 0x0)
    Return()

    # Function_34_D264 end

    def Function_35_D28D(): pass

    label("Function_35_D28D")

    EventBegin(0x1)

    #C0606
    ChrTalk(
        0x101,
        (
            "#0000F（研讨会会场的警备工作\x01",
            "  有一科和亚里欧斯先生在负责……）\x02\x03",

            "（还是不要过去打扰他们了。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -13650, 4000, 12700, 45)
    EventEnd(0x4)
    Return()

    # Function_35_D28D end

    def Function_36_D306(): pass

    label("Function_36_D306")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_D384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 6)), scpexpr(EXPR_END)), "loc_D37F")
    SetChrName("")

    #A0607
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门内传来了市长和议员们的声音，\x01",
            "好像正在谈论沉闷严肃的话题……\x02\x03",

            "还是不要打扰他们为好。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D37F")

    Jump("loc_D51B")

    label("loc_D384")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0608
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克洛斯贝尔自治州政府\x01",
            "　　 市长办公室 　　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4FA")

    #C0609
    ChrTalk(
        0x101,
        (
            "#0000F这里好像就是……麦克道尔市长\x01",
            "的办公室啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x102,
        (
            "#0100F说起来，\x01",
            "外公之前也说过\x01",
            "让我们随时过来拜访他呢……\x02\x03",

            "但他平时非常忙碌，\x01",
            "不知道现在是否\x01",
            "在房间里。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        (
            "#0003F是吗……\x02\x03",

            "#0000F不过，既然如此，\x01",
            "我们还是应该找个时间去与他\x01",
            "打声招呼比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 6)
    OP_65(0x2, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_D51B")

    label("loc_D4FA")

    Sound(810, 0, 100, 0)

    #A0612
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门好像上着锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D51B")

    TalkEnd(0xFF)
    Return()

    # Function_36_D306 end

    def Function_37_D51F(): pass

    label("Function_37_D51F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0613
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克洛斯贝尔自治州政府\x01",
            "   市政厅行政区域\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A8")

    #C0614
    ChrTalk(
        0x101,
        (
            "#0003F好像没有必要\x01",
            "进去啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_D5A8")

    TalkEnd(0xFF)
    Return()

    # Function_37_D51F end

    SaveToFile()

Try(main)
