from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "受付嬢シオン",           # 1
        "クリップ主任",           # 2
        "秘書アーネスト",         # 3
        "マクダエル市長",         # 4
        "フランツ巡査",           # 5
        "市役所職員",             # 6
        "市役所職員",             # 7
        "市役所職員",             # 8
        "レインズ",               # 9
        "グレイス",               # 10
        "紫髪の娘",               # 11
        "運送会社スタッフ",       # 12
        "運送会社スタッフ",       # 13
        "ハルトマン議長",         # 14
        "議員",                   # 15
        "議員",                   # 16
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
        "Function_7_2BC5",         # 07, 7
        "Function_8_41AA",         # 08, 8
        "Function_9_4465",         # 09, 9
        "Function_10_4469",        # 0A, 10
        "Function_11_54CB",        # 0B, 11
        "Function_12_5554",        # 0C, 12
        "Function_13_57EB",        # 0D, 13
        "Function_14_5875",        # 0E, 14
        "Function_15_58DB",        # 0F, 15
        "Function_16_59FD",        # 10, 16
        "Function_17_5D45",        # 11, 17
        "Function_18_79CD",        # 12, 18
        "Function_19_847F",        # 13, 19
        "Function_20_8CFB",        # 14, 20
        "Function_21_8D5C",        # 15, 21
        "Function_22_8E12",        # 16, 22
        "Function_23_8E95",        # 17, 23
        "Function_24_9C41",        # 18, 24
        "Function_25_A1BD",        # 19, 25
        "Function_26_A6F9",        # 1A, 26
        "Function_27_AE00",        # 1B, 27
        "Function_28_B051",        # 1C, 28
        "Function_29_B688",        # 1D, 29
        "Function_30_BCB4",        # 1E, 30
        "Function_31_CF5B",        # 1F, 31
        "Function_32_CF9A",        # 20, 32
        "Function_33_DE7D",        # 21, 33
        "Function_34_DEA0",        # 22, 34
        "Function_35_DEC9",        # 23, 35
        "Function_36_DF46",        # 24, 36
        "Function_37_E19D",        # 25, 37
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
    Jump("loc_2BC4")

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

    Jump("loc_2BC4")

    label("loc_B44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B84")
    OP_4B(0x8, 0xFF)
    TurnDirection(0x0, 0x8, 0)
    Call(0, 29)
    Jump("loc_2BC4")

    label("loc_B84")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_D89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCC")

    #C0001
    ChrTalk(
        0x8,
        (
            "本日はどうも\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "特務支援課……でしたか。\x01",
            "市民の様々な要望に応える\x01",
            "部署だそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "私達が助けられてしまって。\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0009Fははは……\x01",
            "（そう言われるとこそばゆいな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#0100Fまた何かあれば\x01",
            "遠慮なく依頼を回してくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D84")

    label("loc_CCC")


    #C0006
    ChrTalk(
        0x8,
        (
            "本日はどうも\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "特務支援課……でしたか。\x01",
            "市民の様々な要望に応える\x01",
            "部署だそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "私達が助けられてしまって。\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D84")

    Jump("loc_2BC1")

    label("loc_D89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E34")

    #C0009
    ChrTalk(
        0x8,
        (
            "３箇所の空家が確認できたら\x01",
            "私の方に知らせてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "書類の内容には不備や間違いが\x01",
            "あると思いますから、\x01",
            "気を付けてくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC1")

    label("loc_E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F35")

    #C0011
    ChrTalk(
        0x8,
        (
            "自治州議会は\x01",
            "先ほどようやく終了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "これで財務課の方々も\x01",
            "安心して帰宅できますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "でも……市長は今日も\x01",
            "深夜まで残業をなさるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "予算の書類を急いで纏めたいとか……\x01",
            "無理をなさらないといいんですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F95")

    label("loc_F35")


    #C0015
    ChrTalk(
        0x8,
        (
            "市長は今日も\x01",
            "深夜まで残業をなさるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "真面目な方ですから……\x01",
            "お体が心配ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F95")

    Jump("loc_2BC1")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_11EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117B")

    #C0017
    ChrTalk(
        0x8,
        (
            "今朝から、空港が封鎖されているという\x01",
            "問い合わせが相次いでいるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "困りましたね、警察の方には\x01",
            "伏せるように言われているので\x01",
            "臨時の設備検査と言ってあるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "いつまで持つのかしら……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1114")
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
        "#0005F（空港で何かあったのかな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1173")

    label("loc_1114")


    #C0021
    ChrTalk(
        0x103,
        (
            "#0203F（公式見解は\x01",
            "  『臨時の設備検査』のようですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0001F（市役所も大変だな。）\x02",
    )

    CloseMessageWindow()

    label("loc_1173")

    SetScenarioFlags(0x0, 0)
    Jump("loc_11EA")

    label("loc_117B")


    #C0023
    ChrTalk(
        0x8,
        (
            "今朝から、空港が封鎖されているという\x01",
            "問い合わせが相次いでいるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "ふう、いつまで持つのかしら……\x02",
    )

    CloseMessageWindow()

    label("loc_11EA")

    Jump("loc_2BC1")

    label("loc_11EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1382")

    #C0025
    ChrTalk(
        0x8,
        (
            "自治州議会は\x01",
            "今日も紛糾しているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "ふう……議員先生方のあんな姿、\x01",
            "とても市民の皆さんにはお見せできません。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "挙げればきりがないくらい\x01",
            "皆さん態度が悪いんですから。\x02",
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
        "#0303F（……見たくねえなぁ、そんな物は。）\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#0108F（それが議会の現実なのよね……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1400")

    label("loc_1382")


    #C0030
    ChrTalk(
        0x8,
        (
            "自治州議会は\x01",
            "今日も紛糾しているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "ふう……議員先生方のあんな姿、\x01",
            "とても市民の皆さんにはお見せできません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1400")

    Jump("loc_2BC1")

    label("loc_1405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F5")

    #C0032
    ChrTalk(
        0x8,
        (
            "こちらはクロスベル\x01",
            "市庁舎の受付となります……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1492")

    #C0033
    ChrTalk(
        0x8,
        "あ、皆さんでしたか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B2")

    label("loc_1492")


    #C0034
    ChrTalk(
        0x8,
        "あ、警察の方……ですよね。\x02",
    )

    CloseMessageWindow()

    label("loc_14B2")


    #C0035
    ChrTalk(
        0x8,
        (
            "ふう、市民の方からの\x01",
            "苦情かと思いました。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#0105F苦情が来ているんですか？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "ええ、予算議会の日程は\x01",
            "本当は昨日までなのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "例年通り議論が紛糾していて\x01",
            "まだ予算が纏まっていないのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "また何日も会期が\x01",
            "延長されることになりそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#0106F（ふう……自治州議会も\x01",
            "  相変わらずね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_166E")

    label("loc_15F5")


    #C0041
    ChrTalk(
        0x8,
        (
            "今年も議会が延長されているので……\x01",
            "予算の執行も遅れることになりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "市民の皆様にはご迷惑をお掛けします。\x02",
    )

    CloseMessageWindow()

    label("loc_166E")

    Jump("loc_2BC1")

    label("loc_1673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1983")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16F3")

    #C0043
    ChrTalk(
        0x8,
        (
            "皆さん……\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "市庁舎の職員を代表して\x01",
            "お礼をさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_16F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1798")

    #C0045
    ChrTalk(
        0x8,
        (
            "市長のお気に入りを\x01",
            "買ってきて頂けたんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "とてもお喜びになると思います。\x01",
            "どうか皆さんの方から\x01",
            "直接、差し入れてあげて下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_1798")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1847")

    #C0047
    ChrTalk(
        0x8,
        (
            "ジューススタンドが\x01",
            "移動していた……？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "すみません、どこに移動したかは\x01",
            "ちょっと分かりませんね……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "恐らく市内のどこかで\x01",
            "営業していると思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_1847")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1918")

    #C0050
    ChrTalk(
        0x8,
        (
            "市長のお気に入りは\x01",
            "噴水広場のジューススタンドで\x01",
            "売っていると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "普通に売っているものではなく\x01",
            "裏メニューみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "お手数ですが、買ってきて\x01",
            "市長に差し上げてください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197E")

    label("loc_1918")


    #C0053
    ChrTalk(
        0x8,
        (
            "明日からは議事堂で\x01",
            "予算議会が始まります。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "マスコミの人たちも来て……\x01",
            "また忙しくなりますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197E")

    Jump("loc_2BC1")

    label("loc_1983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A37")

    #C0055
    ChrTalk(
        0x8,
        (
            "本日は夕方５時より\x01",
            "閉会式が執り行われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "ですが、会場は大変\x01",
            "混雑が予想されますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "閉会宣言は市庁舎前広場の\x01",
            "拡声器にて傍聴ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AA0")

    label("loc_1A37")


    #C0058
    ChrTalk(
        0x8,
        (
            "閉会式会場は大変\x01",
            "混雑が予想されます。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "どうか閉会宣言は\x01",
            "市庁舎前広場の\x01",
            "拡声器にて傍聴ください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA0")

    Jump("loc_2BC1")

    label("loc_1AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1B2A")

    #C0060
    ChrTalk(
        0x8,
        "パレードも無事終わりましたね。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "ふう……よかったです。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "市民の皆さんにも\x01",
            "楽しんで頂けたようで何よりです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC1")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1BD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B98")

    #C0063
    ChrTalk(
        0x8,
        "いよいよパレードですね……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "ふう、今年は何事もなければ\x01",
            "いいんですけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BD1")

    label("loc_1B98")


    #C0065
    ChrTalk(
        0x8,
        (
            "毎年パレードはトラブルが多くて\x01",
            "大変なんですよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD1")

    Jump("loc_2BC1")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C6B")

    #C0066
    ChrTalk(
        0x8,
        (
            "本日の国際シンポジウムの傍聴には\x01",
            "事前申し込みが必要となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "申し訳ありませんが、\x01",
            "当日のお申し込みは\x01",
            "ご遠慮くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC1")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D25")

    #C0068
    ChrTalk(
        0x8,
        (
            "こちらでは記念祭の\x01",
            "案内パンフレットを配布しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "記念祭の日程や主な屋台、\x01",
            "パレードの道順なども\x01",
            "記されていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "ぜひご活用くださいね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D93")

    label("loc_1D25")


    #C0071
    ChrTalk(
        0x8,
        (
            "こちらでは記念祭の\x01",
            "案内パンフレットを配布しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "もちろん無料ですから\x01",
            "ぜひご活用くださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D93")

    Jump("loc_2BC1")

    label("loc_1D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_205C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F45")

    #C0073
    ChrTalk(
        0x8,
        (
            "あら、みなさん……\x01",
            "ご用はお済になりましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#0100Fええ、お陰様で。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x104,
        (
            "#0300Fまた厄介な事に\x01",
            "なっちまったけどな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0076
    ChrTalk(
        0x8,
        "ええと、よく判りませんが……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "またジオフロントに行かれる\x01",
            "予定がおありなら、\x01",
            "鍵はお持ちになっていて構いませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        "どうぞご自由にお使いください。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#0000Fじゃあ、そうさせて貰おうかな。\x02\x03",

            "#0003F（やっぱりヨナの事も\x01",
            "  気になるしな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 2)
    Jump("loc_2057")

    label("loc_1F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD5")

    #C0080
    ChrTalk(
        0x8,
        (
            "今日は市役所も\x01",
            "少しバタバタしていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "記念祭開会式の予行演習があるんですよ。\x01",
            "……皆様にはご迷惑をおかけします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2057")

    label("loc_1FD5")


    #C0082
    ChrTalk(
        0x8,
        (
            "今日はセレモニーホールで\x01",
            "記念祭開会式の予行演習があるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "市民の方は立ち入りできません。\x01",
            "どうかご了承くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2057")

    Jump("loc_2BC1")

    label("loc_205C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_END)), "loc_20EC")

    #C0084
    ChrTalk(
        0x8,
        (
            "ジオフロントＢ区画の扉は\x01",
            "住宅街の水路付近にあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "以前、鍵を無くされた方もいるので\x01",
            "くれぐれも紛失にご注意ください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC1")

    label("loc_20EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2206")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2187")

    #C0086
    ChrTalk(
        0x8,
        (
            "今日はセレモニーホールで\x01",
            "記念祭開会式の予行演習があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "市民の方は立ち入りできません。\x01",
            "どうかご了承くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2201")

    label("loc_2187")


    #C0088
    ChrTalk(
        0x8,
        (
            "そういえば警察の方も\x01",
            "パレードの予行演習をするそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "ふう……記念祭が近づくと\x01",
            "色々と行事ごとが増えますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2201")

    Jump("loc_2BC1")

    label("loc_2206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2252")

    #C0090
    ChrTalk(
        0x8,
        (
            "ふう……\x01",
            "クロスベルタイムズの方は\x01",
            "しつこくて困ります……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC1")

    label("loc_2252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_23C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2340")

    #C0091
    ChrTalk(
        0x8,
        (
            "来月には、いよいよ\x01",
            "自治州の創立７０周年を祝う\x01",
            "記念祭が開かれます。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "７０周年の節目を祝うため、\x01",
            "会期も例年より伸び\x01",
            "５日間の開催となっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "詳しい事は案内パンフレットを\x01",
            "ご覧になってください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23C0")

    label("loc_2340")


    #C0094
    ChrTalk(
        0x8,
        (
            "来月には、クロスベル自治州の\x01",
            "創立７０周年の記念祭が開かれます。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "詳しい事は案内パンフレットを\x01",
            "ご覧になってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C0")

    Jump("loc_2BC1")

    label("loc_23C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_262B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2584")

    #C0096
    ChrTalk(
        0x8,
        (
            "今年はクロスベル自治州の\x01",
            "創立７０周年に当たります。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "創立記念祭には様々な\x01",
            "催し物が開かれる予定ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "詳しい情報はクロスベル市報にも\x01",
            "掲載されるので、\x01",
            "ぜひお読みになってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0305Fクロスベル市報……？\x01",
            "へえ、そんなのがあったのか。\x02",
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
            "えっと、受付の横に\x01",
            "置かれているパンフレットです。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "目立ちませんが\x01",
            "毎月更新されているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#0003F（知らなかった……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2626")

    label("loc_2584")


    #C0103
    ChrTalk(
        0x8,
        (
            "やっぱり市報を読んでらっしゃる\x01",
            "方なんて少ないですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "もっと受けのいい\x01",
            "パンフレットならいいんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        "#0106F（受付の人も苦労してるわね……）\x02",
    )

    CloseMessageWindow()

    label("loc_2626")

    Jump("loc_2BC1")

    label("loc_262B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_2711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C5")

    #C0106
    ChrTalk(
        0x8,
        (
            "バスの１台と\x01",
            "連絡が取れなくなったとかで……\x01",
            "交通課の人が走っていきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "トラブルでしょうか……\x01",
            "少し心配ですね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_270C")

    label("loc_26C5")


    #C0108
    ChrTalk(
        0x8,
        (
            "バスは時々トラブルがあるんです。\x01",
            "何事もなければいいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270C")

    Jump("loc_2BC1")

    label("loc_2711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_27B8")

    #C0109
    ChrTalk(
        0x8,
        "クロスベル市庁舎へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "バスの運行時刻でしたら\x01",
            "当受付に問い合わせていただく事も\x01",
            "出来ますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "導力バスの運行は\x01",
            "交通課の管轄ですので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC1")

    label("loc_27B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D6")

    #C0112
    ChrTalk(
        0x8,
        (
            "施設ご利用の案内を\x01",
            "させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "この市庁舎には２つの\x01",
            "施設が併設されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "向かって左手がセレモニーホール、\x01",
            "右手がクロスベル議事堂です。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "セレモニーホールでは各種催事が\x01",
            "行われますから、市民の皆さんにも\x01",
            "お馴染みかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_296F")

    label("loc_28D6")


    #C0116
    ChrTalk(
        0x8,
        (
            "向かって左手がセレモニーホール、\x01",
            "右手がクロスベル議事堂です。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "セレモニーホールでは\x01",
            "各種催事が行われますから、\x01",
            "お馴染みの施設かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296F")

    Jump("loc_2BC1")

    label("loc_2974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A3C")

    #C0118
    ChrTalk(
        0x8,
        (
            "こちらはクロスベル\x01",
            "市庁舎の受付となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "公共料金のお支払いや\x01",
            "住所の転居届けは\x01",
            "こちらをご利用ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#0000Fあはは……\x01",
            "（市庁舎の受付も大変そうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2AB1")

    label("loc_2A3C")


    #C0121
    ChrTalk(
        0x8,
        (
            "こちらはクロスベル市庁舎の\x01",
            "受付となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "公共料金のお支払いや\x01",
            "住所の転居届けは\x01",
            "こちらをご利用ください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB1")

    Jump("loc_2BC1")

    label("loc_2AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B27")

    #C0123
    ChrTalk(
        0x8,
        "さっきの娘さん、大丈夫かしら……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "つい旧市街のアパートまで\x01",
            "紹介してしまったけれど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BC1")

    label("loc_2B27")


    #C0125
    ChrTalk(
        0x8,
        (
            "さっき、紫髪の娘さんに\x01",
            "一番安いアパートを\x01",
            "紹介してほしいと言われたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "つい旧市街のアパートまで\x01",
            "紹介してしまったけれど……\x01",
            "大丈夫かしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC1")

    TalkEnd(0x8)

    label("loc_2BC4")

    Return()

    # Function_6_AE8 end

    def Function_7_2BC5(): pass

    label("Function_7_2BC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BE6")
    Call(0, 30)
    Return()

    label("loc_2BE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2C8E")

    #C0127
    ChrTalk(
        0xFE,
        (
            "ようやく予算議会が\x01",
            "終わったんだがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "市長は今日も残業して\x01",
            "書類を作成されると言うんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "うーん、忍びない。\x01",
            "こうなったら私も手伝うよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_2C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2D56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFE")

    #C0130
    ChrTalk(
        0xFE,
        "市長も最近残業続きなんだ。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "今日こそ予算が\x01",
            "纏まってくれるといいんだがなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D51")

    label("loc_2CFE")


    #C0132
    ChrTalk(
        0xFE,
        "市長は最近残業続きなんだ。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "もうお歳だし……\x01",
            "このままではお体が心配だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D51")

    Jump("loc_41A6")

    label("loc_2D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2E89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2C")

    #C0134
    ChrTalk(
        0xFE,
        (
            "議会が開かれている間は\x01",
            "職員も質疑応答の準備に追われてね。\x01",
            "担当部署は残業が続くんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "みんな大変そうだなぁ……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "まあ、うちの課は暇だけどね。\x01",
            "備品管理くらいしかしてないし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E84")

    label("loc_2E2C")


    #C0137
    ChrTalk(
        0xFE,
        (
            "なんだか忙しい職員達に\x01",
            "申し訳ないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "せめて廊下の\x01",
            "掃除でもしておくかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E84")

    Jump("loc_41A6")

    label("loc_2E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F3C")

    #C0139
    ChrTalk(
        0xFE,
        (
            "マクダエル市長なら\x01",
            "議会に出席なさっているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "昨日も議論が白熱したんだが……\x01",
            "結局予算が纏まらなかったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "……ふう、市長も大変だよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F7B")

    label("loc_2F3C")


    #C0142
    ChrTalk(
        0xFE,
        (
            "私は市長のお体が心配だよ。\x01",
            "無理なされないといいんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F7B")

    Jump("loc_41A6")

    label("loc_2F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3461")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3017")

    #C0143
    ChrTalk(
        0xFE,
        (
            "市長は以前から、にがトマトを\x01",
            "大層気に入っておられるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "しかし……あれは人を選ぶよね。\x01",
            "少なくとも私は苦手かな……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_3017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_306F")

    #C0145
    ChrTalk(
        0xFE,
        (
            "ふう……毎度の事だけど、\x01",
            "ハルトマン議長を見ると息が詰まるよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_306F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3249")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31BD")

    #C0146
    ChrTalk(
        0xFE,
        (
            "おお君たち、聞いてくれたまえ！\x01",
            "『聖者の祈り』が帰ってきたんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "この市庁舎の象徴たる彫像だよ。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "記念祭の間に、実は、その\x01",
            "盗まれてしまっていてね……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "でも先日、捜査一課の人が\x01",
            "見つけてきてくれてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "はああ、よかった……\x01",
            "いつまでもこの彫像が不在だと\x01",
            "クロスベルはますます笑い物だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3244")

    label("loc_31BD")


    #C0151
    ChrTalk(
        0xFE,
        (
            "『聖者の祈り』が\x01",
            "帰ってきてよかったよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "記念祭の間に盗まれたものだから、\x01",
            "諸外国には恥ずかしい所を\x01",
            "見せちゃった訳だけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3244")

    Jump("loc_345C")

    label("loc_3249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330C")

    #C0153
    ChrTalk(
        0xFE,
        (
            "警察の諸君じゃないか。\x01",
            "先日は世話になったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "ご覧の通り、『聖者の祈り』は\x01",
            "今日も堂々と鎮座しているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "もう二度と盗まれないように\x01",
            "私も気を付けておかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 5)
    Jump("loc_345C")

    label("loc_330C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33EA")

    #C0156
    ChrTalk(
        0xFE,
        (
            "マクダエル市長は私達職員にも\x01",
            "穏やかに接して下さる人だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "だけど……穏やかな反面\x01",
            "決して本音を明かされないんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "政治家であるお立場上\x01",
            "当然のことなんだろうけど\x01",
            "……少し寂しい気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_345C")

    label("loc_33EA")


    #C0159
    ChrTalk(
        0xFE,
        (
            "マクダエル市長は\x01",
            "私達にも絶対に本音を明かされないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "市長には心許せる人が\x01",
            "おられるんだろうかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_345C")

    Jump("loc_41A6")

    label("loc_3461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_36F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_352C")

    #C0161
    ChrTalk(
        0xFE,
        (
            "よ、よく判らないけど\x01",
            "本当に助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "今日は閉会式の準備に忙しくてね\x01",
            "……ろくにお礼も出来ないんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "君たちには世話になった。\x01",
            "また何かあったらよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36EC")

    label("loc_352C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3671")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E3")

    #C0164
    ChrTalk(
        0xFE,
        (
            "今日は閉会式という時に\x01",
            "まさかこんな事になるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "君たち、なるべく早く\x01",
            "『聖者の祈り』を取り戻してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "本当に、本当に急ぎで頼むよ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_366C")

    label("loc_35E3")


    #C0167
    ChrTalk(
        0xFE,
        (
            "午後からは閉会式の\x01",
            "入館者も出てくるんだ……\x01",
            "その時にあの彫像がないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "君たち、なるべく早く\x01",
            "『聖者の祈り』を取り戻してくれ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_366C")

    Jump("loc_36EC")

    label("loc_3671")


    #C0169
    ChrTalk(
        0xFE,
        (
            "はああ、何てことだ……\x01",
            "市長がお出掛けの間に\x01",
            "こんな事になるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "ここは彼らを頼るしかないか……\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36EC")

    Jump("loc_41A6")

    label("loc_36F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_378F")

    #C0171
    ChrTalk(
        0xFE,
        (
            "市長は有力者の方々との\x01",
            "会談に向かわれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのクロイス総裁とも\x01",
            "お会いになっているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "また帰りは遅くなるんだろうな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_378F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3814")

    #C0174
    ChrTalk(
        0xFE,
        (
            "市長はまた少し\x01",
            "痩せられたようだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "こんな時期に休む事など\x01",
            "できないんだろうが……\x01",
            "無理はしないで頂きたいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_3814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_387B")

    #C0176
    ChrTalk(
        0xFE,
        (
            "ああ、マスコミの関係者が\x01",
            "思ったよりも多いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        "何とか席を増やせないものかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_387B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3925")

    #C0178
    ChrTalk(
        0xFE,
        (
            "……最近ね、マクダエル市長の\x01",
            "お手伝いをしているんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "いやだって、市長は\x01",
            "あんな事件がおありになったわけだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "私は普段暇にしているからね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_3925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_39BE")

    #C0181
    ChrTalk(
        0xFE,
        (
            "やれやれ、アーネストさんが\x01",
            "取り計らってくれて助かった。\x01",
            "無事公聴会も開けそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "市長はお忙しくて、\x01",
            "中々捕まらないんだよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_39BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3AF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A8C")

    #C0183
    ChrTalk(
        0xFE,
        (
            "参ったな、今日は公聴会があるのに\x01",
            "市長が捕まらないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "いつもお忙しいから\x01",
            "もしや、とは思っていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "はあ、せめて第一秘書の\x01",
            "アーネストさんを探さないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3AF4")

    label("loc_3A8C")


    #C0186
    ChrTalk(
        0xFE,
        (
            "市長のハンコがないと\x01",
            "公聴会は開けないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "せめて第一秘書の\x01",
            "アーネストさんを探さないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF4")

    Jump("loc_41A6")

    label("loc_3AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3BAE")

    #C0188
    ChrTalk(
        0xFE,
        (
            "そういえば明日は\x01",
            "公聴会があるんだったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "セレモニーホールの準備をして、\x01",
            "市民からの陳情を纏めて……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "市長も出席なさるから\x01",
            "打ち合わせもしなくちゃなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_3BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3CC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C77")

    #C0191
    ChrTalk(
        0xFE,
        (
            "……来年度予算の\x01",
            "すり合わせが始まったねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "予算議会の質疑応答は\x01",
            "マスコミの注目が高くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "若手議員なんかは抑えて\x01",
            "必ず大物政治家が\x01",
            "もったいぶって話すんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CC2")

    label("loc_3C77")


    #C0194
    ChrTalk(
        0xFE,
        (
            "議員先生が意気揚々と\x01",
            "乗り込んでくる時期だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "はあ、憂鬱だなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_3CC2")

    Jump("loc_41A6")

    label("loc_3CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D3F")

    #C0196
    ChrTalk(
        0xFE,
        (
            "昨日のバスのトラブルは\x01",
            "整備不備だったみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "やれやれ、こういう事って\x01",
            "結構多いんだよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_3D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_END)), "loc_3DA9")

    #C0198
    ChrTalk(
        0xFE,
        (
            "さっき交通課の人が\x01",
            "走っていったなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "交通課の人は\x01",
            "いつも忙しそうで気の毒だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_3DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3E96")

    #C0200
    ChrTalk(
        0xFE,
        (
            "クロスベル市が近年\x01",
            "力を入れている市民サービスが\x01",
            "導力バスだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "といっても……どちらかと言うと\x01",
            "議員たちが人気取りのために\x01",
            "予算を増額しているような物だけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "まあ動機はどうあれ、\x01",
            "便利になるのはいいことだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A6")

    label("loc_3E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3FCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F71")

    #C0203
    ChrTalk(
        0xFE,
        (
            "ここの扉は市庁舎の\x01",
            "左翼に通じているんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "市長の執務室がある所だね。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "もう一つの扉……\x01",
            "市庁舎の右翼側には\x01",
            "議長の執務室がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "どちらも内外に\x01",
            "影響力をもつ大物政治家だね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FC9")

    label("loc_3F71")


    #C0207
    ChrTalk(
        0xFE,
        (
            "市長も議長も\x01",
            "今はいらっしゃらないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "２人とも大物政治家で\x01",
            "お忙しいからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC9")

    Jump("loc_41A6")

    label("loc_3FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_40D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4085")

    #C0209
    ChrTalk(
        0xFE,
        "私は総務二課に勤めていてね。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "議事堂やセレモニーホールなんかの\x01",
            "運営を任されているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "暇なんだよねぇ。\x01",
            "掃除くらいしかする事がないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_40D0")

    label("loc_4085")


    #C0212
    ChrTalk(
        0xFE,
        (
            "議会が開会すれば\x01",
            "また忙しくなるんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "普段は暇なんだよねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_40D0")

    Jump("loc_41A6")

    label("loc_40D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_41A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4157")

    #C0214
    ChrTalk(
        0xFE,
        "さて、掃除掃除……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "今日はセレモニーホールの\x01",
            "掃除もしようかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "他にする事もないしね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41A6")

    label("loc_4157")


    #C0217
    ChrTalk(
        0xFE,
        "おや……なにかご用かな。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "それなら受付の\x01",
            "シオン君の方へお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41A6")

    TalkEnd(0xFE)
    Return()

    # Function_7_2BC5 end

    def Function_8_41AA(): pass

    label("Function_8_41AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43A9")
    OP_4B(0x9, 0xFF)
    TurnDirection(0xA, 0x9, 0)

    #C0219
    ChrTalk(
        0x9,
        (
            "それではアーネストさん。\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        (
            "#2600Fありがとうございます。\x01",
            "活用させていただきます。\x02\x03",

            "#2604Fよし、これがあれば\x01",
            "何とか公聴会で……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x0, 500)

    #C0221
    ChrTalk(
        0xA,
        (
            "#2600Fはは、市民から届いた\x01",
            "意見要望をまとめたものでね。\x02\x03",

            "公聴会に提出することで\x01",
            "議員たちの利権争いに\x01",
            "一石を投じられるはずなんだ。\x02\x03",

            "#2603Fさて、公聴会の前までに\x01",
            "市長に相談してみないと……\x02",
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
            "#0003F（エリィ……やっぱり\x01",
            "  政治の道に未練があるのかな？）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_4461")

    label("loc_43A9")


    #C0224
    ChrTalk(
        0xA,
        (
            "#2600F市民から届いた意見要望を\x01",
            "まとめた資料……\x02\x03",

            "公聴会に提出することで\x01",
            "議員たちの利権争いに\x01",
            "一石を投じられるはずなんだ。\x02\x03",

            "#2603Fさて、公聴会の前までに\x01",
            "市長に相談してみないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4461")

    TalkEnd(0xFE)
    Return()

    # Function_8_41AA end

    def Function_9_4465(): pass

    label("Function_9_4465")

    Call(0, 10)
    Return()

    # Function_9_4465 end

    def Function_10_4469(): pass

    label("Function_10_4469")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44FD")
    Jump("loc_4547")

    label("loc_44FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_451D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4547")

    label("loc_451D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_453D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4547")

    label("loc_453D")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4547")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_49C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4926")
    SetChrSubChip(0xB, 0x0)

    #C0225
    ChrTalk(
        0xB,
        (
            "#2501Fああ、すぐに用意してくれ。\x01",
            "私は書類を調えよう。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4667")
    Jump("loc_46B1")

    label("loc_4667")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4687")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46B1")

    label("loc_4687")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46A7")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46B1")

    label("loc_46A7")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46B1")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0226
    ChrTalk(
        0xB,
        (
            "#2500Fおお、君たちか。\x01",
            "……何かあったのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#0000Fあ、いえ……捜査中に少し\x01",
            "立ち寄らせてもらっただけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x102,
        (
            "#0100Fおじいさまの方は\x01",
            "随分お忙しそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xB,
        (
            "#2503Fああ、議会が３日も\x01",
            "伸びてしまったのでな。\x02\x03",

            "#2500F各方面への予算の手配を\x01",
            "急がなくてはならんのだ。\x02",
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
            "#2500Fはは、残業続きなことを\x01",
            "案じているようだな。\x02\x03",

            "#2503F私の事なら心配はいらない。\x01",
            "この忙しさも今日限りだろうからな。\x02\x03",

            "#2500Fエリィ、仮にも仕事中なら\x01",
            "そちらに集中しなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        "#0103F……はい、そうします。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        "#0200Fでは病院に急ぎましょうか。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        "#0300Fだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 5)
    Jump("loc_49BE")

    label("loc_4926")

    OP_4B(0x9, 0xFF)
    SetChrSubChip(0xB, 0x0)

    #C0235
    ChrTalk(
        0xB,
        (
            "#2503Fクリップ君、すまないな。\x01",
            "財務課への連絡は任せる。\x02\x03",

            "#2500Fハルトマン議長には\x01",
            "私から書類を回すとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x9,
        "はい、承知しました。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)

    label("loc_49BE")

    Jump("loc_54C3")

    label("loc_49C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_49D1")
    Jump("loc_54C3")

    label("loc_49D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49DF")
    Jump("loc_54C3")

    label("loc_49DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_49ED")
    Jump("loc_54C3")

    label("loc_49ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4D9C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D94")

    #C0237
    ChrTalk(
        0xB,
        (
            "#2509F君たちの差し入れのおかげで\x01",
            "午後もバリバリ働けそうだ。\x02\x03",

            "#2503Fズズズズズ……\x01",
            "うむ、美味い！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D8F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_4C8C")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AC4")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4B19")

    label("loc_4AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AF1")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4B19")

    label("loc_4AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B19")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4B19")

    Sleep(1000)

    #C0238
    ChrTalk(
        0x101,
        "#0006F（本当にお気に入りなんだな……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BB5")

    #C0239
    ChrTalk(
        0x102,
        (
            "#0103F（流石おじいさま……\x01",
            "  激動の時代を生きてきた\x01",
            "  名政治家なだけはあるわ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C58")

    label("loc_4BB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C07")

    #C0240
    ChrTalk(
        0x103,
        (
            "#0206F（あの激ニガシェイクを……\x01",
            "  尊敬に値しますね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C58")

    label("loc_4C07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C58")

    #C0241
    ChrTalk(
        0x104,
        (
            "#0303F（あの激ニガシェイクを……\x01",
            "  男として尊敬できるぜ！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C58")


    #C0242
    ChrTalk(
        0x153,
        (
            "#1105F（えー？\x01",
            "  ホントおいしーのにー。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8C")

    label("loc_4C8C")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CD1")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4D26")

    label("loc_4CD1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CFE")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4D26")

    label("loc_4CFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D26")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4D26")

    Sleep(1000)

    #C0243
    ChrTalk(
        0x153,
        "#1111F（いいなぁ、おいしそー。）\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#0006F（ちょ、ちょっとだけ\x01",
            "  試せば良かったかな……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D8C")

    SetScenarioFlags(0x0, 3)

    label("loc_4D8F")

    Jump("loc_4D97")

    label("loc_4D94")

    Call(0, 17)

    label("loc_4D97")

    Jump("loc_54C3")

    label("loc_4D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4DAA")
    Jump("loc_54C3")

    label("loc_4DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4DB8")
    Jump("loc_54C3")

    label("loc_4DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F7C")

    #C0245
    ChrTalk(
        0xB,
        (
            "#2503Fふむ、今日のパレードは\x01",
            "過去最大の人出になりそうだな。\x02\x03",

            "#2500Fパレードが始まる前に\x01",
            "挨拶をせねばならんのだが、\x01",
            "……にわかに緊張してきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        "#0005Fええっ……？\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x104,
        "#0300Fいやぁ……冗談ッスよね？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#0106Fふう……\x01",
            "おじいさまがこの程度で\x01",
            "緊張なさるわけないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xB,
        (
            "#2509Fふふふ……\x02\x03",

            "#2500Fパレードが終われば\x01",
            "記念祭のメインイベントは終了だ。\x02\x03",

            "君達の仕事も楽になるだろう。\x01",
            "問題なく進む事を祈るとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4FFA")

    label("loc_4F7C")


    #C0250
    ChrTalk(
        0xB,
        (
            "#2500Fパレードが終われば\x01",
            "記念祭のメインイベントは終了だ。\x02\x03",

            "君達の仕事も楽になるだろう。\x01",
            "問題なく進む事を祈るとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FFA")

    Jump("loc_54C3")

    label("loc_4FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_51C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5123")

    #C0251
    ChrTalk(
        0xB,
        (
            "#2500F今日開催されるシンポジウムは\x01",
            "私が提言したものでね。\x02\x03",

            "クロスベルの現状と将来について\x01",
            "公開形式で討論するというものだ。\x02\x03",

            "#2503F政治的な意味合いは薄いが、\x01",
            "諸外国から識者も集まっている。\x02\x03",

            "#2500F自治州７０周年の節目に\x01",
            "クロスベルを見返す\x01",
            "良い契機となるだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_51BE")

    label("loc_5123")


    #C0252
    ChrTalk(
        0xB,
        (
            "#2500F今日開催されるシンポジウムは\x01",
            "私が提言したものなのだ。\x02\x03",

            "クロスベルの現状と将来について\x01",
            "公開形式で討論するのだ。\x01",
            "きっと有意義なものとなるだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51BE")

    Jump("loc_54C3")

    label("loc_51C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_54C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5431")

    #C0253
    ChrTalk(
        0xB,
        (
            "#2500Fおお、エリィ。\x01",
            "それに支援課の諸君か。\x02\x03",

            "#2503Fすまないな、記念祭中も\x01",
            "色々と用事が立て込んでいる。\x02\x03",

            "一度くらいは君たちと\x01",
            "食事でもと思っていたのだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#0005Fい、いえ……\x01",
            "どうかお気になさらず。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#0200Fそれよりお身体の方は\x01",
            "もう大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        (
            "#2503Fなに、あれくらいの事で\x01",
            "倒れるほどヤワではないさ。\x02\x03",

            "#2501F帝国と共和国の紛争が続いた\x01",
            "３０年前に比べれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        (
            "#0103Fおじいさま……\x01",
            "その話になると長くなりますから。\x02\x03",

            "#0100F食事ならまた、\x01",
            "いつでも機会がありますわ。\x02\x03",

            "それより、どうかご無理だけは\x01",
            "なさらないでくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xB,
        (
            "#2500Fうむ、分かっているよ。\x01",
            "ありがとうエリィ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_54C3")

    label("loc_5431")


    #C0259
    ChrTalk(
        0xB,
        (
            "#2500F記念祭中も\x01",
            "用事が立て込んでいてね。\x02\x03",

            "#2503F君たちとは一度ゆっくり\x01",
            "話をしてみたかったのだが……\x02\x03",

            "#2500Fうむ、また機会を待つとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C3")

    SetChrSubChip(0xB, 0x0)
    TalkEnd(0xB)
    Return()

    # Function_10_4469 end

    def Function_11_54CB(): pass

    label("Function_11_54CB")

    TalkBegin(0xFE)

    #C0260
    ChrTalk(
        0xFE,
        "やあロイド達か。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "今日のシンポジウムには\x01",
            "マクダエル市長や\x01",
            "外国のＶＩＰも出席なさるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        "結構壮観な顔ぶれらしいよ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_54CB end

    def Function_12_5554(): pass

    label("Function_12_5554")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_56CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_561F")

    #C0263
    ChrTalk(
        0xFE,
        (
            "『聖者の祈り』が戻ってきたんだな。\x01",
            "よかったぜ……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "とと、喜んでる場合じゃない。\x01",
            "ただでさえ閉会式の\x01",
            "準備が遅れてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "閉会式まであと３時間……\x01",
            "急がないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56C8")

    label("loc_561F")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0266
    ChrTalk(
        0xD,
        (
            "はああ……\x01",
            "市長が不在のこんな時に……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0267
    ChrTalk(
        0xE,
        (
            "と、とにかく閉会式の\x01",
            "準備を進めませんと……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xE,
        (
            "私、会場の椅子を\x01",
            "確保してきますね！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)

    label("loc_56C8")

    Jump("loc_57E7")

    label("loc_56CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_57E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5754")

    #C0269
    ChrTalk(
        0xFE,
        (
            "国際シンポジウム傍聴の方は\x01",
            "今しばらくお待ちくださ～い。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "開場時間になり次第、\x01",
            "ご案内いたしま～す。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_57E7")

    label("loc_5754")


    #C0271
    ChrTalk(
        0xFE,
        (
            "ふう、国際シンポジウムも\x01",
            "なんとか無事に開催できそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "ちなみに会場には\x01",
            "アリオス・マクレインも来てるんだぜ。\x01",
            "会場警備はばっちりだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57E7")

    TalkEnd(0xFE)
    Return()

    # Function_12_5554 end

    def Function_13_57EB(): pass

    label("Function_13_57EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_57FF")
    Call(0, 12)
    Jump("loc_5871")

    label("loc_57FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5871")
    OP_93(0xFE, 0x5A, 0x0)

    #C0273
    ChrTalk(
        0xFE,
        (
            "あの、もう\x01",
            "時間がありませんけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "そろそろ出席者の方々も\x01",
            "お出でになると思いますし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5871")

    TalkEnd(0xFE)
    Return()

    # Function_13_57EB end

    def Function_14_5875(): pass

    label("Function_14_5875")

    TalkBegin(0xFE)

    #C0275
    ChrTalk(
        0xFE,
        (
            "今日も催し物があるんだ。\x01",
            "我ら総務二課も大忙しだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        "……普段は暇な部署なんだけどね。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_5875 end

    def Function_15_58DB(): pass

    label("Function_15_58DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_597F")

    #C0277
    ChrTalk(
        0xFE,
        (
            "最近、編集長の命令で\x01",
            "グレイス先輩のストッパー役に\x01",
            "使われるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "……先輩は直撃取材ばかりなので\x01",
            "いつも置いてきぼりなんですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F9")

    label("loc_597F")


    #C0279
    ChrTalk(
        0xFE,
        (
            "グレイス先輩は\x01",
            "議会の取材に行ってるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "でも大丈夫かなぁ……\x01",
            "また許可証なしで\x01",
            "潜り込んじゃったしなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_59F9")

    TalkEnd(0xFE)
    Return()

    # Function_15_58DB end

    def Function_16_59FD(): pass

    label("Function_16_59FD")

    TalkBegin(0xFE)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5AC1")

    #C0281
    ChrTalk(
        0x11,
        (
            "#2103Fあたしだってクロスベルの\x01",
            "税金を払ってる市民なんだしさ～。\x02\x03",

            "#2100F税金から給料が出てる人間の\x01",
            "連絡先くらいいんじゃない～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "う、うーん。\x01",
            "それを言われますと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D3D")

    label("loc_5AC1")


    #C0283
    ChrTalk(
        0x11,
        (
            "#2104Fんー、そこのところを\x01",
            "もう少し突っ込んで\x01",
            "教えてくれないかなぁ？\x02\x03",

            "#2109F議員がたの緊急連絡先、\x01",
            "一通り把握してるんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "事務所以外の連絡先は\x01",
            "お教えできない決まりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        "どうかお引取りください。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x11,
        (
            "#2106Fあ～ん！\x01",
            "そんな事言わないでさ～。\x02\x03",

            "#2100Fじゃあじゃあ、せめて\x01",
            "秘書さんたちの連絡先だけでも\x01",
            "教えてくれない？\x02\x03",

            "#2109F公設秘書だったら\x01",
            "名簿だってあるんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        "そ、そう言われましても……\x02",
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
            "#0006F（グレイスさん……\x01",
            "  さすがの強引さだなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#0100F（矛先を変えられないよう\x01",
            "  さっさと行きましょう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5D3D")

    OP_4C(0x8, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_16_59FD end

    def Function_17_5D45(): pass

    label("Function_17_5D45")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E07")
    SetChrPos(0x102, -44250, 0, 11500, 0)
    Jump("loc_5E4E")

    label("loc_5E07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E2D")
    SetChrPos(0x103, -44250, 0, 11500, 0)
    Jump("loc_5E4E")

    label("loc_5E2D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E4E")
    SetChrPos(0x104, -44250, 0, 11500, 0)

    label("loc_5E4E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F2B")

    #C0290
    ChrTalk(
        0xB,
        (
            "#5P#2505Fおお、エリィ。\x01",
            "それにロイド君か。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FC6")

    label("loc_5F2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F7A")

    #C0291
    ChrTalk(
        0xB,
        (
            "#5P#2505Fおお、ロイド君……\x01",
            "それにティオ君だったか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FC6")

    label("loc_5F7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FC6")

    #C0292
    ChrTalk(
        0xB,
        (
            "#5P#2505Fおお、ロイド君……\x01",
            "それにランディ君だったか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_608A")

    #C0293
    ChrTalk(
        0x102,
        (
            "#12P#0103Fおじいさま……\x01",
            "その、しばらく連絡できずに\x01",
            "申しわけありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#6P#0003F例の一件に関しては\x01",
            "各方面に口添えして頂いたようで……\x01",
            "なんとお礼を言ったらいいか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_610F")

    label("loc_608A")


    #C0295
    ChrTalk(
        0x101,
        (
            "#6P#0000F市長……ご無沙汰しています。\x02\x03",

            "#0003F例の一件に関しては\x01",
            "各方面に口添えして頂いたようで……\x01",
            "なんとお礼を言ったらいいか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_610F")


    #C0296
    ChrTalk(
        0xB,
        (
            "#5P#2503Fなに、大した事はしていない。\x02\x03",

            "#2500F《競売会》に参加していた議員に\x01",
            "詳しい事情の説明を頼んだだけさ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61E1")

    #C0297
    ChrTalk(
        0x102,
        (
            "#12P#0100Fいえ、それがあったからこそ\x01",
            "議長への牽制になったと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6296")

    label("loc_61E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_623D")

    #C0298
    ChrTalk(
        0x103,
        (
            "#12P#0200Fまあ、それがあったからこそ\x01",
            "議長への牽制になったかと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6296")

    label("loc_623D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6296")

    #C0299
    ChrTalk(
        0x104,
        (
            "#12P#0300Fま、それがあったからこそ\x01",
            "議長への牽制になったワケですし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6296")


    #C0300
    ChrTalk(
        0x101,
        (
            "#6P#0000Fとにかく……\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "#5P#2509Fはは、そんな風に畏#2Rかしこ#まられたら\x01",
            "命を救ってもらった私など\x01",
            "どれだけ君達に感謝すればいいか。\x02\x03",

            "#2503F──ふむ、それはそうと、\x01",
            "そちらのお嬢ちゃんが例の……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあ、はい。\x01",
            "キーアといいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x153,
        (
            "#6P#1110Fはじめましてー。\x02\x03",

            "#1109Fおじいちゃん、オヒゲが\x01",
            "まっしろでカッコいいねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "#5P#2509Fカッコいい……\x01",
            "ハハ、面白いお嬢ちゃんだ。\x02\x03",

            "#2500Fふむ、明るく朗らかで\x01",
            "不思議な愛嬌がある……\x02\x03",

            "#2501F……記憶喪失と聞いたが\x01",
            "身元はまだ判らないのかね？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64DF")

    #C0305
    ChrTalk(
        0x102,
        "#12P#0103Fええ、今のところは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_654C")

    label("loc_64DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6518")

    #C0306
    ChrTalk(
        0x103,
        "#12P#0203Fはい、今のところは。\x02",
    )

    CloseMessageWindow()
    Jump("loc_654C")

    label("loc_6518")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_654C")

    #C0307
    ChrTalk(
        0x104,
        "#12P#0306Fええ、今のところは。\x02",
    )

    CloseMessageWindow()

    label("loc_654C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_END)), "loc_659A")

    #C0308
    ChrTalk(
        0x101,
        (
            "#6P#0001F一応、遊撃士協会に\x01",
            "身元調査を依頼したんですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_659A")


    #C0309
    ChrTalk(
        0x101,
        (
            "#6P#0001F一応、遊撃士協会に\x01",
            "身元調査を依頼しようと\x01",
            "思っているんですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E9")


    #C0310
    ChrTalk(
        0xB,
        (
            "#5P#2500Fふむ、餅は餅屋だ。\x01",
            "出来る限りの手は\x01",
            "打っておくべきだろう。\x02\x03",

            "#2503F──いずれにせよ、\x01",
            "もし困ったことになったら\x01",
            "いつでも相談してくれたまえ。\x02\x03",

            "しがらみに縛られた\x01",
            "不甲斐ない市長とはいえ……\x02\x03",

            "#2500Fこんな幼気#4Rいたいけ#な少女に仇なす\x01",
            "愚か者どもを放っておくほど\x01",
            "腑抜けではないつもりだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6744")

    #C0311
    ChrTalk(
        0x102,
        "#12P#0102Fおじいさま……\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A7")

    label("loc_6744")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6775")

    #C0312
    ChrTalk(
        0x103,
        "#12P#0202F市長さん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A7")

    label("loc_6775")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67A7")

    #C0313
    ChrTalk(
        0x104,
        "#12P#0302Fおお、市長さん……\x02",
    )

    CloseMessageWindow()

    label("loc_67A7")


    #C0314
    ChrTalk(
        0x101,
        (
            "#6P#0004F……その言葉だけでも\x01",
            "本当に勇気づけられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x153,
        "#6P#1109Fえへへ、やっぱカッコいい！\x02",
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)

    #N0316
    NpcTalk(
        0x15,
        "男の声",
        (
            "──マクダエル市長。\x01",
            "少々、よろしいですかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68B2")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_68FB")

    label("loc_68B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68D9")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_68FB")

    label("loc_68D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68FB")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_68FB")

    Sleep(1000)

    #C0317
    ChrTalk(
        0xB,
        "#5P#2501Fむ……\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_68(-45000, 1500, 9000, 3000)

    def lambda_692F():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_692F)
    Sleep(50)

    def lambda_693F():
        OP_93(0x153, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_693F)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_696C")

    def lambda_695F():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_695F)
    Jump("loc_69AB")

    label("loc_696C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_698E")

    def lambda_6981():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6981)
    Jump("loc_69AB")

    label("loc_698E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69AB")

    def lambda_69A3():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_69A3)

    label("loc_69AB")


    def lambda_69B0():
        OP_97(0x15, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_69B0)

    def lambda_69CA():
        OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_69CA)
    Sleep(50)

    def lambda_69DE():
        OP_97(0x16, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_69DE)

    def lambda_69F8():
        OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_69F8)
    Sleep(50)

    def lambda_6A0C():
        OP_97(0x17, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6A0C)

    def lambda_6A26():
        OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_6A26)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A7F")
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jump("loc_6ADC")

    label("loc_6A7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AB0")
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jump("loc_6ADC")

    label("loc_6AB0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6ADC")
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_6ADC")

    Sleep(1000)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)

    #C0318
    ChrTalk(
        0x101,
        "#6P#0005F（なっ……！）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B47")

    #C0319
    ChrTalk(
        0x102,
        "#11P#0105F（ハルトマン議長……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BB2")

    label("loc_6B47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B7C")

    #C0320
    ChrTalk(
        0x103,
        "#11P#0205F（帝国派の……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BB2")

    label("loc_6B7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BB2")

    #C0321
    ChrTalk(
        0x104,
        "#11P#0301F（帝国派の親玉か……）\x02",
    )

    CloseMessageWindow()

    label("loc_6BB2")

    OP_68(-45850, 1600, 12420, 2000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BF2")

    def lambda_6BD8():
        OP_97(0x102, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BD8)
    Jump("loc_6C4B")

    label("loc_6BF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C21")

    def lambda_6C07():
        OP_97(0x103, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C07)
    Jump("loc_6C4B")

    label("loc_6C21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C4B")

    def lambda_6C36():
        OP_97(0x104, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C36)

    label("loc_6C4B")

    Sleep(50)

    def lambda_6C53():
        OP_97(0x101, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C53)
    Sleep(50)

    def lambda_6C70():
        OP_97(0x153, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_6C70)

    def lambda_6C8A():
        OP_97(0x15, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6C8A)
    Sleep(50)

    def lambda_6CA7():
        OP_97(0x16, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6CA7)
    Sleep(50)

    def lambda_6CC4():
        OP_97(0x17, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6CC4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CFF")
    WaitChrThread(0x102, 1)

    def lambda_6CF2():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CF2)
    Jump("loc_6D46")

    label("loc_6CFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D25")
    WaitChrThread(0x103, 1)

    def lambda_6D18():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6D18)
    Jump("loc_6D46")

    label("loc_6D25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D46")
    WaitChrThread(0x104, 1)

    def lambda_6D3E():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6D3E)

    label("loc_6D46")

    WaitChrThread(0x101, 1)

    def lambda_6D4F():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D4F)
    WaitChrThread(0x153, 1)

    def lambda_6D60():
        OP_93(0x153, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_6D60)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)

    #C0322
    ChrTalk(
        0xB,
        (
            "#5P#2500Fハルトマン議長、何用かな？\x02\x03",

            "見ての通り接客中なのだが。\x02",
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
            "これは失礼──ですが、\x01",
            "こちらも少々急ぎの用でしてな。\x02\x03",

            "先日の帝国政府からの申し出、\x01",
            "改めて検討して頂きたいのですよ。\x02",
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
        "#5P#2503Fだが、それは……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x15,
        (
            "#12P#2703F市長の仰ることも判ります。\x01",
            "だが、私の立場も考えて頂きたい。\x02\x03",

            "#2702Fそれとも……\x01",
            "これを機にキャンベル議員たちと\x01",
            "結託されるおつもりかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xB,
        (
            "#5P#2503F……私は別に\x01",
            "共和国派に与するつもりはない。\x02\x03",

            "#2501Fもちろん君たち帝国派にもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x15,
        (
            "#12P#2702Fならば、そのバランス感覚を\x01",
            "存分に発揮して頂きましょう。\x02\x03",

            "#2703F私のささやかなパーティが\x01",
            "台無しになった事による\x01",
            "自治州全体へのマイナス……\x02\x03",

            "#2700Fそれを帳消しにするためにもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        (
            "#5P#2503F……君とは今一度、\x01",
            "話し合う必要がありそうだな……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    #C0329
    ChrTalk(
        0xB,
        (
            "#5P#2500F……諸君。\x01",
            "せっかく訪ねてくれたのに\x01",
            "申しわけないが……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70F3():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70F3)
    Sleep(50)

    def lambda_7103():
        TurnDirection(0x153, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7103)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_712A")
    TurnDirection(0x102, 0xB, 500)
    Jump("loc_715D")

    label("loc_712A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7146")
    TurnDirection(0x103, 0xB, 500)
    Jump("loc_715D")

    label("loc_7146")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_715D")
    TurnDirection(0x104, 0xB, 500)

    label("loc_715D")


    #C0330
    ChrTalk(
        0x101,
        (
            "#11P#0005Fい、いえ。\x01",
            "どうかお気になさらずに。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71CD")

    #C0331
    ChrTalk(
        0x102,
        "#11P#0103F失礼します、おじいさま。\x02",
    )

    CloseMessageWindow()
    Jump("loc_723C")

    label("loc_71CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7204")

    #C0332
    ChrTalk(
        0x103,
        "#11P#0203F……失礼しました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_723C")

    label("loc_7204")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_723C")

    #C0333
    ChrTalk(
        0x104,
        "#11P#0300Fそんじゃ、失礼しまッス。\x02",
    )

    CloseMessageWindow()

    label("loc_723C")


    #C0334
    ChrTalk(
        0x153,
        (
            "#5P#1109Fまたねー！\x01",
            "オヒゲのおじいちゃん！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7321")
    SetChrPos(0x102, -6220, 4000, 18950, 270)
    CloseMessageWindow()
    Jump("loc_736A")

    label("loc_7321")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7348")
    SetChrPos(0x103, -6220, 4000, 18950, 270)
    CloseMessageWindow()
    Jump("loc_736A")

    label("loc_7348")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_736A")
    SetChrPos(0x104, -6220, 4000, 18950, 270)
    CloseMessageWindow()

    label("loc_736A")

    FadeToBright(1000, 0)
    OP_0D()

    #C0335
    ChrTalk(
        0x101,
        "#5P#0001F市長……大変そうだったな。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7451")

    #C0336
    ChrTalk(
        0x102,
        (
            "#11P#0101F……ええ……\x02\x03",

            "昔から似たような場面は\x01",
            "何度も見ているけれど……\x02\x03",

            "#0108Fでも、犯罪まがいの\x01",
            "競売会を開いていた張本人が\x01",
            "あそこまで開き直るなんて……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7563")

    label("loc_7451")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74D0")

    #C0337
    ChrTalk(
        0x103,
        (
            "#11P#0203Fあの議長さん……\x01",
            "つくづく恥知らずですね。\x02\x03",

            "#0200F犯罪まがいの競売会を\x01",
            "開いていたくせに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7563")

    label("loc_74D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7563")

    #C0338
    ChrTalk(
        0x104,
        (
            "#11P#0306Fしかしあの議長も、\x01",
            "とことん恥知らずだよな。\x02\x03",

            "#0301F犯罪まがいの競売会を\x01",
            "開いてたくせに\x01",
            "ぬけぬけと開き直りやがって。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7563")


    #C0339
    ChrTalk(
        0x101,
        (
            "#5P#0001Fその程度じゃ\x01",
            "スキャンダルにもならない\x01",
            "自信があるわけか……\x02\x03",

            "#0006Fある意味、マフィアより\x01",
            "遥かにタチが悪そうだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x153,
        (
            "#6P#1110Fねえねえ、ロイドー。\x02\x03",

            "あのおじいちゃん、\x01",
            "カッコいいだけじゃなくって\x01",
            "すごくツヨイんだねー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_7665():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7665)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_769B")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x102, 0x153, 500)
    Jump("loc_76F2")

    label("loc_769B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76C9")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x103, 0x153, 500)
    Jump("loc_76F2")

    label("loc_76C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76F2")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x104, 0x153, 500)

    label("loc_76F2")

    Sleep(500)
    WaitChrThread(0x101, 1)

    #C0341
    ChrTalk(
        0x101,
        (
            "#5P#0005Fすごく強いって……\x01",
            "どうしてそう思うんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x153,
        (
            "#6P#1111Fだって、あのエラそーなオジサン、\x01",
            "ナカマといっしょだったでしょ？\x02\x03",

            "#1110Fそれってひとりだと\x01",
            "おじいちゃんに負けそーだから\x01",
            "つれてきたんじゃないのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#5P#0005Fあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7867")

    #C0344
    ChrTalk(
        0x102,
        (
            "#11P#0105F議長が連れていたのは\x01",
            "帝国派の有力議員だけど……\x02\x03",

            "#0104Fふふ、確かに\x01",
            "そういう見方もあるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7920")

    label("loc_7867")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78B3")

    #C0345
    ChrTalk(
        0x103,
        (
            "#11P#0205Fなるほど……\x01",
            "そういう見方もありますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7920")

    label("loc_78B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7920")

    #C0346
    ChrTalk(
        0x104,
        (
            "#11P#0304Fはは、なるほどな。\x02\x03",

            "#0300F確かにタイマン張れる自信が\x01",
            "無かったとも言えるよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7920")


    #C0347
    ChrTalk(
        0x101,
        (
            "#5P#0003Fうーん、俺たちみたいなヒヨッ子が\x01",
            "市長を心配するのもおこがましいか。\x02\x03",

            "（それでも何かしてあげられると\x01",
            "  いいんだけど……）\x02",
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

    # Function_17_5D45 end

    def Function_18_79CD(): pass

    label("Function_18_79CD")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A52")
    OP_68(-3140, 1500, 3700, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19330, 0)
    SetChrPos(0x101, -4500, 130, 2900, 90)
    SetChrPos(0x153, -5250, 130, 3650, 90)
    SetChrPos(0xEF, -6000, 130, 2150, 90)
    Jump("loc_7AB3")

    label("loc_7A52")

    OP_68(3140, 1500, 3700, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19330, 0)
    SetChrPos(0x101, 4500, 130, 2900, 270)
    SetChrPos(0x153, 5250, 130, 3650, 270)
    SetChrPos(0xEF, 6000, 130, 2150, 270)

    label("loc_7AB3")

    TurnDirection(0x8, 0x101, 0)
    OP_0D()

    #C0348
    ChrTalk(
        0x8,
        "あ、皆さん……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x8,
        (
            "その、市長室の様子は\x01",
            "いかがでしたか……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B03():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B03)
    Sleep(50)

    def lambda_7B13():
        TurnDirection(0x153, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7B13)
    Sleep(50)
    TurnDirection(0xEF, 0x8, 500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)

    #C0350
    ChrTalk(
        0x101,
        "#0005Fえ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7BBE")
    OP_68(-1290, 1500, 4900, 2500)
    SetChrFlags(0xEF, 0x40)

    def lambda_7B6A():
        OP_95(0xFE, -2360, 0, 4980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B6A)
    Sleep(50)

    def lambda_7B87():
        OP_95(0xFE, -3140, 0, 5670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7B87)
    Sleep(50)

    def lambda_7BA4():
        OP_95(0xFE, -3710, 0, 4340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_7BA4)
    Jump("loc_7C28")

    label("loc_7BBE")

    OP_68(1290, 1500, 4900, 2500)
    SetChrFlags(0xEF, 0x40)

    def lambda_7BD9():
        OP_95(0xFE, 2360, 0, 4980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BD9)
    Sleep(50)

    def lambda_7BF6():
        OP_95(0xFE, 3140, 0, 5670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7BF6)
    Sleep(50)

    def lambda_7C13():
        OP_95(0xFE, 3710, 0, 4340, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_7C13)

    label("loc_7C28")

    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    ClearChrFlags(0xEF, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C68")

    #C0351
    ChrTalk(
        0x102,
        "#0105Fというと……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CC1")

    label("loc_7C68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C9B")

    #C0352
    ChrTalk(
        0x103,
        "#0205Fと言いますと……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CC1")

    label("loc_7C9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7CC1")

    #C0353
    ChrTalk(
        0x104,
        "#0305Fつーと…？\x02",
    )

    CloseMessageWindow()

    label("loc_7CC1")


    #C0354
    ChrTalk(
        0x8,
        (
            "いえ、ハルトマン議長が\x01",
            "取り巻きの議員がたを連れて\x01",
            "乗り込んで行かれたので……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x8,
        (
            "いつもの事ではありますが\x01",
            "ちょっと心配で……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#0000Fああ、その事ですか。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DBA")

    #C0357
    ChrTalk(
        0x102,
        (
            "#0100Fちょっと心配ですけど……\x01",
            "市長なら大丈夫だと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E4B")

    label("loc_7DBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E06")

    #C0358
    ChrTalk(
        0x103,
        (
            "#0200F少し心配ですが……\x01",
            "市長さんなら大丈夫かと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E4B")

    label("loc_7E06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E4B")

    #C0359
    ChrTalk(
        0x104,
        (
            "#0300Fちょいと心配だが\x01",
            "市長さんなら大丈夫だろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E4B")


    #C0360
    ChrTalk(
        0x8,
        "そうですか……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x8,
        (
            "……こういう時、\x01",
            "市庁舎の職員は無力ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "せめてお忙しい市長を\x01",
            "ねぎらって差し上げられれば\x01",
            "いいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#0006F……そうですね。\x01",
            "俺たちも同じなんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x153,
        (
            "#1105Fおじいちゃんに\x01",
            "なにかしてあげるのー？\x02\x03",

            "#1110Fだったら、おじいちゃんの\x01",
            "好きなものをゴチソウしたら\x01",
            "いーんじゃないかなぁ？\x02",
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
        "#0005Fな、なるほど。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8051")

    #C0366
    ChrTalk(
        0x102,
        (
            "#0100F確かに差し入れというのは\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80DE")

    label("loc_8051")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8097")

    #C0367
    ChrTalk(
        0x103,
        (
            "#0203F確かに差し入れは\x01",
            "効果的ではないかと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80DE")

    label("loc_8097")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80DE")

    #C0368
    ChrTalk(
        0x104,
        (
            "#0304F確かに差し入れってのは\x01",
            "いいかもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80DE")

    TurnDirection(0x101, 0x8, 500)

    #C0369
    ChrTalk(
        0x8,
        "ふふ、そうですね。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        "……あの、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x8,
        (
            "よかったら市長のお気に入りの\x01",
            "飲み物を買ってきて頂けませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x8,
        (
            "近くの噴水広場にある\x01",
            "ジューススタンドに行けば\x01",
            "売っていると思うんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        (
            "#0000F分かりました。\x01",
            "その程度ならお安い御用です。\x02\x03",

            "えっと、市長のお気に入りが\x01",
            "どんな飲み物かご存知ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "詳しくは知らないのですが\x01",
            "普通に売っているものではなく\x01",
            "裏メニューみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "店員の方に聞いたら\x01",
            "教えていただけると思います。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_830C")

    #C0376
    ChrTalk(
        0x102,
        (
            "#0100Fふふ、それじゃあ早速、\x01",
            "噴水広場のジューススタンドに\x01",
            "行ってみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B7")

    label("loc_830C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8366")

    #C0377
    ChrTalk(
        0x103,
        (
            "#0200Fそれでは早速、噴水広場の\x01",
            "ジューススタンドに行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B7")

    label("loc_8366")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83B7")

    #C0378
    ChrTalk(
        0x104,
        (
            "#0300Fそんじゃ早速、噴水広場の\x01",
            "ジューススタンドに行こうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83B7")


    #C0379
    ChrTalk(
        0x153,
        "#1109Fれっつごー！\x02",
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
            "クエスト【市長への差し入れ】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8456")
    SetChrPos(0x0, -2360, 0, 4980, 45)
    Jump("loc_8467")

    label("loc_8456")

    SetChrPos(0x0, 2360, 0, 4980, 315)

    label("loc_8467")

    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x26, 0x4, 0x2)
    EventEnd(0x5)
    Return()

    # Function_18_79CD end

    def Function_19_847F(): pass

    label("Function_19_847F")

    EventBegin(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch06500.itc", 0x1E)
    LoadChrToIndex("chr/ch27800.itc", 0x1F)
    LoadChrToIndex("chr/ch27400.itc", 0x20)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 8119, 4000, 14200, 315)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8588")
    OP_68(-7680, 5500, 15150, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -9250, 4000, 14500, 45)
    SetChrPos(0x153, -10350, 4000, 14450, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_853C")
    SetChrPos(0x102, -9600, 4000, 13150, 45)
    Jump("loc_8583")

    label("loc_853C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8562")
    SetChrPos(0x103, -9600, 4000, 13150, 45)
    Jump("loc_8583")

    label("loc_8562")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8583")
    SetChrPos(0x104, -9600, 4000, 13150, 45)

    label("loc_8583")

    Jump("loc_8645")

    label("loc_8588")

    OP_68(-4800, 5500, 16000, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -1500, 4000, 14500, 270)
    SetChrPos(0x153, -750, 4000, 15250, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85FE")
    SetChrPos(0x102, -500, 4000, 13750, 270)
    Jump("loc_8645")

    label("loc_85FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8624")
    SetChrPos(0x103, -500, 4000, 13750, 270)
    Jump("loc_8645")

    label("loc_8624")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8645")
    SetChrPos(0x104, -500, 4000, 13750, 270)

    label("loc_8645")

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
        "声",
        "#2P──フン、失礼する。\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x1)

    def lambda_871A():
        OP_97(0x15, 0xDAC, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_871A)

    def lambda_8734():
        OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_8734)
    Sleep(50)

    def lambda_8748():
        OP_97(0x16, 0xDAC, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8748)

    def lambda_8762():
        OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_8762)
    Sleep(50)

    def lambda_8776():
        OP_97(0x17, 0xDAC, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8776)

    def lambda_8790():
        OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_8790)
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
            "#11Pまったく！\x01",
            "なんと頑固な老人だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x17,
        (
            "#5P議長閣下の\x01",
            "せっかくの申し出を……！\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x15,
        (
            "#11P#2702Fフン、まあいい。\x01",
            "一応釘は刺せたからな。\x02\x03",

            "#2703F……キャンベルたちには\x01",
            "いつも通り備えるとして……\x02\x03",

            "#2701F問題はルバーチェか。\x01",
            "まったく使えない連中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x16,
        "#11Pそ、そうですね！\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x17,
        (
            "#5P改めて、議長あっての\x01",
            "自分たちであるという事実を\x01",
            "分からせてもいいかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x15,
        (
            "#11P#2703Fうむ、マルコーニには\x01",
            "しばらく会うのは控えるか。\x02\x03",

            "#2702Fそれと、今晩あたりに\x01",
            "久々に会合を開くとしよう。\x02\x03",

            "帝国派全員に声をかけたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x16,
        "#11Pかしこまりました！\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x17,
        "#5P至急、召集をかけます！\x02",
    )

    CloseMessageWindow()
    OP_68(6200, 5500, 17600, 6000)
    BeginChrThread(0x15, 3, 0, 20)
    BeginChrThread(0x16, 3, 0, 21)
    BeginChrThread(0x17, 3, 0, 22)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8A66")
    Sleep(1000)

    def lambda_8A39():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A39)
    Sleep(50)

    def lambda_8A49():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8A49)
    Sleep(50)

    def lambda_8A59():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_8A59)
    Jump("loc_8A96")

    label("loc_8A66")

    Sleep(2500)

    def lambda_8A6E():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A6E)
    Sleep(50)

    def lambda_8A7E():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8A7E)
    Sleep(50)

    def lambda_8A8E():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_8A8E)

    label("loc_8A96")

    WaitChrThread(0x15, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x16, 3)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1900), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8B01")
    Fade(500)
    OP_68(-8100, 5500, 13450, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Jump("loc_8B35")

    label("loc_8B01")

    Fade(500)
    OP_68(-820, 4500, 15700, 0)
    MoveCamera(11, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    label("loc_8B35")


    #C0390
    ChrTalk(
        0x101,
        (
            "#5P#0003Fふう……\x01",
            "用件は終わったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BBB")

    #C0391
    ChrTalk(
        0x102,
        (
            "#12P#0100F今の内におじいさまに\x01",
            "差し入れてしまいましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C4C")

    label("loc_8BBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C05")

    #C0392
    ChrTalk(
        0x103,
        (
            "#12P#0200F今の内に市長さんに\x01",
            "差し入れましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C4C")

    label("loc_8C05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C4C")

    #C0393
    ChrTalk(
        0x104,
        (
            "#12P#0300F今の内に市長さんに\x01",
            "差し入れちまおうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C4C")

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

    # Function_19_847F end

    def Function_20_8CFB(): pass

    label("Function_20_8CFB")


    def lambda_8D00():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D00)
    WaitChrThread(0xFE, 1)

    def lambda_8D1E():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D1E)
    Sleep(1000)

    def lambda_8D2E():
        OP_97(0xFE, 0xFA0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D2E)
    Sleep(2000)

    def lambda_8D4B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8D4B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_8CFB end

    def Function_21_8D5C(): pass

    label("Function_21_8D5C")


    def lambda_8D61():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D61)
    WaitChrThread(0xFE, 1)

    def lambda_8D7F():
        OP_95(0xFE, 6720, 4000, 19320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D7F)
    WaitChrThread(0xFE, 1)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)

    def lambda_8DB2():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8DB2)
    WaitChrThread(0xFE, 1)
    Sleep(2000)

    def lambda_8DC6():
        OP_95(0xFE, 7210, 4000, 18830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8DC6)
    WaitChrThread(0xFE, 1)

    def lambda_8DE4():
        OP_97(0xFE, 0xBB8, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8DE4)
    Sleep(1000)

    def lambda_8E01():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8E01)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_8D5C end

    def Function_22_8E12(): pass

    label("Function_22_8E12")


    def lambda_8E17():
        OP_97(0xFE, 0x2904, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E17)
    WaitChrThread(0xFE, 1)

    def lambda_8E35():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E35)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_8E49():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E49)
    WaitChrThread(0xFE, 1)

    def lambda_8E67():
        OP_97(0xFE, 0xFA0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E67)
    Sleep(2000)

    def lambda_8E84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8E84)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_8E12 end

    def Function_23_8E95(): pass

    label("Function_23_8E95")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    OP_68(-45000, 1500, 11000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -45750, 0, 1500, 0)
    SetChrPos(0x153, -45000, 0, 2750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F1D")
    SetChrPos(0x102, -44250, 0, 2000, 0)
    Jump("loc_8F64")

    label("loc_8F1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F43")
    SetChrPos(0x103, -44250, 0, 2000, 0)
    Jump("loc_8F64")

    label("loc_8F43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F64")
    SetChrPos(0x104, -44250, 0, 2000, 0)

    label("loc_8F64")

    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -45000, 0, 11500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0394
    ChrTalk(
        0x101,
        (
            "#0000Fすみません。\x01",
            "たびたびお邪魔します。\x02",
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
            "#5P#2500Fおお、君たちか。\x01",
            "先ほどは済まなかったね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_900F():
        OP_98(0x153, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_900F)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9056")

    def lambda_903C():
        OP_98(0x102, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_903C)
    Jump("loc_90AF")

    label("loc_9056")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9085")

    def lambda_906B():
        OP_98(0x103, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_906B)
    Jump("loc_90AF")

    label("loc_9085")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90AF")

    def lambda_909A():
        OP_98(0x104, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_909A)

    label("loc_90AF")

    Sleep(50)

    def lambda_90B7():
        OP_98(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_90B7)
    OP_68(-45000, 1100, 10500, 3000)
    OP_6F(0x79)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 1)

    #C0396
    ChrTalk(
        0x101,
        (
            "#12P#0001Fいえ……\x01",
            "大変そうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_915A")

    #C0397
    ChrTalk(
        0x102,
        (
            "#11P#0108Fおじいさま……\x01",
            "その、大丈夫でしたか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F3")

    label("loc_915A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91AC")

    #C0398
    ChrTalk(
        0x103,
        (
            "#11P#0200F色々と不穏な申し出を\x01",
            "されていたようですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F3")

    label("loc_91AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91F3")

    #C0399
    ChrTalk(
        0x104,
        (
            "#11P#0301F大丈夫っスか？\x01",
            "何か不穏そうでしたけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91F3")


    #C0400
    ChrTalk(
        0xB,
        (
            "#5P#2509Fああ、あの程度の\x01",
            "ゴリ押しをいなすくらい\x01",
            "日常茶飯事だからね。\x02\x03",

            "#2500Fところで、どうしたのかな？\x01",
            "何か忘れ物でも？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあ、いえ……\x02\x03",

            "#0002F……ほら、キーア。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x153,
        "#6P#1100Fうんっ。\x02",
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
            "キーアはマクダエル市長に\x01",
            "特製にがトマトシェイクを手渡した。\x07\x00\x02",
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
            "#5P#2505Fこれは……私のお気に入りの。\x02\x03",

            "ひょっとして……\x01",
            "わざわざ買ってきてくれたのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x153,
        (
            "#6P#1110Fみんなからのさしいれだよー。\x02\x03",

            "#1109Fおじいちゃん、いろいろと\x01",
            "がんばってるみたいだからー。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xB,
        "#5P#2509Fおお……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#12P#0003Fその、市庁舎の受付の方に\x01",
            "差し入れを頼まれまして……\x02\x03",

            "#0000Fそれからジューススタンドの\x01",
            "店員さんもサービスしてくれました。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xB,
        (
            "#5P#2503Fそうか……\x01",
            "確かに、みんなからの\x01",
            "差し入れというわけだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95A7")

    #C0409
    ChrTalk(
        0xB,
        (
            "#5P#2500Fありがとう、ロイド君、エリィ。\x01",
            "それにキーア君。\x02\x03",

            "#2509Fおかげで元気百倍、\x01",
            "午後もバリバリ働けそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x102,
        (
            "#11P#0102Fふふ、あまり無茶は\x01",
            "なさらないでくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9734")

    label("loc_95A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_966E")

    #C0411
    ChrTalk(
        0xB,
        (
            "#5P#2500Fありがとう、ロイド君、ティオ君。\x01",
            "それにキーア君。\x02\x03",

            "#2509Fおかげで元気百倍、\x01",
            "午後もバリバリ働けそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        (
            "#11P#0200Fあまり無茶はしない方が\x01",
            "いいとは思いますが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9734")

    label("loc_966E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9734")

    #C0413
    ChrTalk(
        0xB,
        (
            "#5P#2500Fありがとう、ロイド君、ランディ君。\x01",
            "それにキーア君。\x02\x03",

            "#2509Fおかげで元気百倍、\x01",
            "午後もバリバリ働けそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x104,
        (
            "#11P#0300Fははっ、ま、あんまり\x01",
            "無茶はしないでくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9734")


    #C0415
    ChrTalk(
        0xB,
        (
            "#5P#2503Fふむ、しかしそうだな。\x02\x03",

            "このような嬉しい差し入れを\x01",
            "してもらったからには……\x02",
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
            "マクダエル市長は下の棚から\x01",
            "小さな紙の包みを取り出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9830")
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jump("loc_9885")

    label("loc_9830")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_985D")
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jump("loc_9885")

    label("loc_985D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9885")
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_9885")

    OP_97(0xB, 0xFFFFEA84, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0xB, 0xB4, 0x0)

    #C0417
    ChrTalk(
        0xB,
        (
            "#5P#2500F以前、共和国の友人から\x01",
            "もらった貴重な漢方薬でね。\x02\x03",

            "どうか受け取って欲しい。\x02",
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
            "を受け取った。\x02",
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
            "#12P#0005Fそ、そんな……\x01",
            "受け取れませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xB,
        (
            "#5P#2503Fなに、私には必要ないものだ。\x02\x03",

            "君たちのように\x01",
            "危険な目にも遭うことが多い\x01",
            "若者たちにこそ持っていて欲しい。\x02\x03",

            "#2500Fどうか受け取ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        "#12P#0000F……分かりました。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AA5")

    #C0422
    ChrTalk(
        0x102,
        (
            "#11P#0102Fふふ……\x01",
            "ありがたく頂戴します。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B16")

    label("loc_9AA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AE0")

    #C0423
    ChrTalk(
        0x103,
        "#11P#0202Fそれでは、ありがたく。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B16")

    label("loc_9AE0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B16")

    #C0424
    ChrTalk(
        0x104,
        "#11P#0309Fそんじゃ、ありがたく！\x02",
    )

    CloseMessageWindow()

    label("loc_9B16")


    #C0425
    ChrTalk(
        0x153,
        "#6P#1109Fおじーちゃん、ありがとー！\x02",
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
            "クエスト【市長への差し入れ】\x07\x00",
            "を達成した！\x02",
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

    # Function_23_8E95 end

    def Function_24_9C41(): pass

    label("Function_24_9C41")

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
            "#5Pいらっしゃいませ。\x01",
            "クロスベル市庁舎へようこそ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_9D63")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0428
    ChrTalk(
        0x8,
        (
            "#5Pあら……\x01",
            "確か警察の方でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        "#5Pどなたかに面会でも？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E3A")

    label("loc_9D63")


    #C0430
    ChrTalk(
        0x8,
        "#5Pどのようなご用件でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#12P#0000Fはい、自分たちは\x01",
            "クロスベル警察の者なんですが……\x02",
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
            "ロイドは捜査手帳を見せた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0433
    ChrTalk(
        0x8,
        "#5Pああ、そうでしたか。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        "#5Pそれで、どなたかに面会でも？\x02",
    )

    CloseMessageWindow()

    label("loc_9E3A")


    #C0435
    ChrTalk(
        0x102,
        "#0103Fいえ、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0436
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査のため、ジオフロントＢ区画の\x01",
            "鍵が借りられないか聞いてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0437
    ChrTalk(
        0x8,
        (
            "#5PジオフロントＢ区画……\x01",
            "確か、市北西部でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x8,
        "#5P少々お待ちください。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_9F0D():
        OP_95(0xFE, 0, 0, 9400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9F0D)
    OP_0D()
    WaitChrThread(0x8, 1)
    Sleep(500)
    OP_93(0x8, 0x0, 0x0)

    def lambda_9F36():
        OP_95(0xFE, 0, 0, 7400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9F36)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)

    #C0439
    ChrTalk(
        0x8,
        "#5Pこちらになります。\x02",
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
            "を入手した。\x02",
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
        "#12P#0002Fありがたくお借りします。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x103,
        (
            "#12P#0200Fでも、随分あっさりと\x01",
            "貸してもらえるんですね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x8,
        (
            "#5Pええ、クロスベル警察には\x01",
            "便宜を図るよう言われていますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x8,
        (
            "#5Pちなみに遊撃士協会にも\x01",
            "同じ鍵をお貸ししています。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x101,
        "#12P#0012Fそ、そうなんですか……\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x8,
        (
            "#5PジオフロントＢ区画の扉は\x01",
            "住宅街の水路付近にあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x8,
        (
            "#5P以前、鍵を無くされた方もいるので\x01",
            "くれぐれも紛失にご注意ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        "#0100Fええ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x104,
        "#12P#0309Fサンクス、お姉さん。\x02",
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

    # Function_24_9C41 end

    def Function_25_A1BD(): pass

    label("Function_25_A1BD")

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
            "#5P一番安いアパルトメント……\x01",
            "……でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x8,
        (
            "#5Pそれなら一応\x01",
            "こういった資料もありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x12,
        (
            "#12P#1805Fあ、こういう案内があるんですね！\x02\x03",

            "#1809F良かったぁ……\x01",
            "………このパンフレット、\x01",
            "お借りしてもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x8,
        (
            "#5Pええ、ご自由に\x01",
            "持ち帰ってくださって結構ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x8,
        "#5Pでもあの、あまり安い物件は……\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x12,
        (
            "#12P#1806Fふう、早く住む所を決めて\x01",
            "稽古に集中しないと……\x02\x03",

            "#1802F#3S……あ、すみません。\x01",
            "案内どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)
    OP_68(0, 1500, -1030, 3000)

    def lambda_A42D():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A42D)
    Sleep(50)

    def lambda_A44A():
        OP_95(0xFE, 0, 0, 1140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A44A)

    def lambda_A464():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A464)
    Sleep(50)

    def lambda_A481():
        OP_98(0x103, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A481)
    Sleep(50)

    def lambda_A49E():
        OP_98(0x104, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A49E)
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
        "#5P#1805Fあ、すみません！\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        "#12P#0005Fいや、こちらこそ……\x02",
    )

    CloseMessageWindow()

    def lambda_A523():
        OP_98(0x101, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A523)
    Sleep(50)

    def lambda_A540():
        OP_98(0x102, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A540)
    Sleep(25)

    def lambda_A55D():
        OP_98(0x103, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A55D)
    Sleep(25)

    def lambda_A57A():
        OP_98(0x104, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A57A)
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
        "#5P#1804F………………（ペコリ）\x02",
    )

    CloseMessageWindow()

    def lambda_A5E5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFDF94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A5E5)
    Sleep(500)

    def lambda_A602():

        label("loc_A602")

        TurnDirection(0x101, 0x12, 500)
        Yield()
        Jump("loc_A602")

    QueueWorkItem2(0x101, 2, lambda_A602)

    def lambda_A614():

        label("loc_A614")

        TurnDirection(0x102, 0x12, 500)
        Yield()
        Jump("loc_A614")

    QueueWorkItem2(0x102, 2, lambda_A614)

    def lambda_A626():

        label("loc_A626")

        TurnDirection(0x103, 0x12, 500)
        Yield()
        Jump("loc_A626")

    QueueWorkItem2(0x103, 2, lambda_A626)

    def lambda_A638():

        label("loc_A638")

        TurnDirection(0x104, 0x12, 500)
        Yield()
        Jump("loc_A638")

    QueueWorkItem2(0x104, 2, lambda_A638)
    Sleep(1200)

    def lambda_A64D():
        OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_A64D)
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
        "#5P#0000F今の子、確かさっき見かけた……\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        (
            "#5P#0102Fふふ、何だか\x01",
            "よくすれ違う人ね。\x02",
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

    # Function_25_A1BD end

    def Function_26_A6F9(): pass

    label("Function_26_A6F9")

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
            "#5Pこちらはクロスベル\x01",
            "市庁舎の受付となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "#5P公共料金のお支払いや\x01",
            "住所の転居届けは\x01",
            "こちらをご利用ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#12P#0000Fえっとすみません、\x01",
            "クロスベル警察の者です。\x02\x03",

            "市庁からの支援要請を\x01",
            "見てきたんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0464
    ChrTalk(
        0x8,
        "#5Pまあ、警察の方でしたか。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x8,
        (
            "#5Pよかった、意外と早く\x01",
            "来ていただけましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#11P#0100Fはい、早速依頼のお話を\x01",
            "聞かせて頂いてもよろしいですか？\x02\x03",

            "不在住戸の確認、\x01",
            "という事でしたけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x8,
        "#5Pええ、ご説明いたします。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        (
            "#5P……皆さんも『住民登録』に\x01",
            "ついてはご存知ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x8,
        (
            "#5Pクロスベルでは引越しの際に\x01",
            "住民登録を申請していただく事に\x01",
            "なっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x8,
        (
            "#5Pですが……実際には\x01",
            "未申請のまま転入出される方が多くて。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "#5P役所の方でも\x01",
            "把握ができていないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x103,
        "#12P#0200Fはあ……\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x8,
        (
            "#5Pそこで、皆さんに\x01",
            "空家の確認をお願いしたいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x8,
        (
            "#5P特に空家と登録されている住戸のうち\x01",
            "正確でない疑いがある物、ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        (
            "#5P住民課の方でも\x01",
            "手が回っていないらしくて……\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x104,
        (
            "#0300F要するに役所の\x01",
            "手伝いってわけッスね。\x02",
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
            "#12P#0006Fランディ、失礼じゃないか。\x02\x03",

            "#0001Fそれに空家っていうのは\x01",
            "防犯上の観点から見ても望ましくない。\x01",
            "せめて確認くらいはしておかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x104,
        "#0305Fほお、そういうモンなのか。\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x102,
        (
            "#11P#0100Fまあ市内を見て回るのは\x01",
            "悪い事じゃないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x8,
        (
            "#5P……あの、それで\x01",
            "引き受けて頂けますでしょうか。\x02",
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
            "【引き受ける】\x01",      # 0
            "【断る】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_29(0x3, 0x1, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD28")
    Call(0, 28)
    Return()

    label("loc_AD28")


    #C0481
    ChrTalk(
        0x101,
        (
            "#12P#0006Fすみません、\x01",
            "事情は判りましたが\x01",
            "今は他にも仕事が……\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x8,
        (
            "#5Pそうですか……ではまた\x01",
            "都合の良いときにお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x8,
        (
            "#5P本日中なら\x01",
            "いつでも構いませんので。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, 4000, 180)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x1, 0x1F)
    EventEnd(0x5)
    Return()

    # Function_26_A6F9 end

    def Function_27_AE00(): pass

    label("Function_27_AE00")

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
            "#5P皆さんには市内の\x01",
            "空家の確認をお願いしたいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x8,
        (
            "#5P住民課の方でも\x01",
            "手が回っていないらしくて……\x01",
            "引き受けて頂けますでしょうか。\x02",
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
            "【引き受ける】\x01",      # 0
            "【断る】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_29(0x3, 0x1, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF79")
    Call(0, 28)
    Return()

    label("loc_AF79")


    #C0486
    ChrTalk(
        0x101,
        (
            "#12P#0006Fすみません、\x01",
            "事情は判りましたが\x01",
            "今は他にも仕事が……\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x8,
        (
            "#5Pそうですか……ではまた\x01",
            "都合の良いときにお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x8,
        (
            "#5P本日中なら\x01",
            "いつでも構いませんので。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, 4000, 180)
    OP_4C(0x8, 0xFF)
    OP_29(0x3, 0x1, 0x1F)
    EventEnd(0x5)
    Return()

    # Function_27_AE00 end

    def Function_28_B051(): pass

    label("Function_28_B051")

    OP_29(0x3, 0x2, 0x1F)

    #C0489
    ChrTalk(
        0x8,
        (
            "#5Pありがとうございます。\x01",
            "それでは書類をお渡ししますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x8,
        (
            "#5P……こちらがその該当物件の\x01",
            "書類になります。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x101,
        "#12P#0000Fあ、お預かりします。\x02",
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
            "を受け取った。\x02",
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

    def lambda_B178():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B178)
    Sleep(200)

    def lambda_B188():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B188)

    def lambda_B195():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B195)

    def lambda_B1A2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B1A2)
    Sleep(500)

    #C0493
    ChrTalk(
        0x101,
        (
            "#6P#0005Fええっと、全部で３軒か。\x02\x03",

            "#0003F住宅街に１軒。\x01",
            "割と外れにあるみたいだな。\x02\x03",

            "東通りにも１軒……\x01",
            "これは住所からして\x01",
            "遊撃士協会の右隣みたいだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B336")

    #C0494
    ChrTalk(
        0x104,
        (
            "#0300Fギルドの右隣か。\x01",
            "覚えやすくて良さそうだぜ。\x02\x03",

            "#0305F最後の一件は……旧市街みたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x102,
        (
            "#11P#0103F旧市街のアパート\x01",
            "『ロータスハイツ』の３室が空家……\x02\x03",

            "#0105Fちょっと待ってね。\x01",
            "捜査手帳に書き留めておくから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B438")

    label("loc_B336")


    #C0496
    ChrTalk(
        0x104,
        (
            "#0303Fギルドの右隣か。\x01",
            "覚えやすくて良さそうだぜ。\x02\x03",

            "#0305F最後のこの住所は……\x01",
            "どこに当たるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        (
            "#11P#0100F今の旧市街と呼ばれている場所ね。\x02\x03",

            "#0103Fアパート『ロータスハイツ』の\x01",
            "３室が空家……\x02\x03",

            "#0105Fちょっと待ってね。\x01",
            "捜査手帳に書き留めておくから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B438")


    #C0498
    ChrTalk(
        0x102,
        "#11P#0103Fさらさら、さらさら……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    #C0499
    ChrTalk(
        0x102,
        "#11P#0100Fうん、大丈夫よ。\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#6P#0000Fサンキュー、エリィ。\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_B4AC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B4AC)

    def lambda_B4B9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B4B9)

    def lambda_B4C6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B4C6)

    def lambda_B4D3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B4D3)
    Sleep(500)

    #C0501
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれではこれより\x01",
            "空家の確認に向かってきます。\x02\x03",

            "報告はこちらでよろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x8,
        (
            "#5Pええ、３箇所の空家が確認できたら\x01",
            "私の方に知らせてください。\x01",
            "よろしくお願いしますね。\x02",
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
            "クエスト【不在住戸の確認依頼】\x07\x00",
            "を開始した！\x02",
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

    # Function_28_B051 end

    def Function_29_B688(): pass

    label("Function_29_B688")

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
            "#5Pあら皆さん。\x01",
            "空家の確認の方は順調ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええ、一通り\x01",
            "確認が終わったので\x01",
            "報告させていただきます。\x02",
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
            "間違いを修正した書類を手渡した。\x02",
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
            "#5Pあら、部屋番号や\x01",
            "コメントまで書き込んで頂いて……\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x8,
        (
            "#5Pありがとうございました。\x01",
            "住民課の方も喜ばれると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x104,
        (
            "#0306Fはは、できれば\x01",
            "もう少しまともなリストが\x01",
            "欲しかった所だけどな。\x02\x03",

            "あちこち歩き回る羽目に\x01",
            "なっちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x103,
        (
            "#12P#0200F警察のわたし達が\x01",
            "指摘するのもなんですが、\x01",
            "管理が雑すぎるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x8,
        (
            "#5Pす、すみません……\x01",
            "住民課も正確を期すように\x01",
            "努力はしているのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x8,
        (
            "#5P……あそこは議員の方から\x01",
            "圧力が掛かることも多くて……\x01",
            "本当に申し訳ありませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#12P#0005Fい、いえ……そういう事でしたら。\x01",
            "（役所も色々とあるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x102,
        (
            "#11P#0108F（ええ……クロスベルでは\x01",
            "  議員の力が相当強いから……）\x02\x03",

            "#0100Fともかく、お役に立てて良かったです。\x02\x03",

            "市役所の方も大変だと思いますけど……\x01",
            "また何かあれば支援課にご相談下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x103,
        (
            "#12P#0200Fそうですね、これくらいなら\x01",
            "お力になれるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        "#0300Fま、気軽に回してくれや。\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x8,
        (
            "#5Pはい……ありがとうございます。\x01",
            "その際はよろしくお願いしますね。\x02",
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
            "クエスト【不在住戸の確認依頼】\x07\x00",
            "を達成した！\x02",
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

    # Function_29_B688 end

    def Function_30_BCB4(): pass

    label("Function_30_BCB4")

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
            "#5Pはああ、まったく\x01",
            "どうしたものか……\x02",
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
            "#5Pはっ、君たち！\x01",
            "たしか警察の特務支援課、だね！？\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x9, 4870, 4000, 17950, 2000, 0x0)

    #C0521
    ChrTalk(
        0x101,
        (
            "#6P#0000Fはいそうです。\x01",
            "支援要請のことで伺いました。\x02\x03",

            "ええと、何か大変な\x01",
            "事件という事でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x102,
        "#12P#0100F盗難事件でもありましたか？\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x9,
        "#5Pそ、それが……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0x1F4)

    #C0524
    ChrTalk(
        0x9,
        (
            "#5P#4Sそうなんだよ！！\x01",
            "大切な物が盗まれてしまって！！\x02",
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
        "#12P#0205F本当に盗難事件でしたか。\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x104,
        (
            "#12P#0305Fもしかして市庁舎から\x01",
            "盗まれたのか？\x02\x03",

            "#0306F記念祭は事件が多いとは思ってたが、\x01",
            "そんな奴まで出てくるとはなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        "#6P#0001Fそれで、その盗まれた物は……\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x9,
        (
            "#5Pああ……そこに展示されていた\x01",
            "大きな彫像なんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2790, 4200, 19050, 2000)
    MoveCamera(26, 25, 0, 2000)

    def lambda_C07D():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C07D)

    def lambda_C08A():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C08A)

    def lambda_C097():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C097)

    def lambda_C0A4():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C0A4)

    def lambda_C0B1():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C0B1)
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
            "#6P#0003Fそ、そういえば……\x01",
            "何か物足りないとは\x01",
            "思ってたんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x103,
        (
            "#12P#0205F本当に無くなっていますね。\x01",
            "……ちょっと信じられないです。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x9,
        (
            "#5P信じられないのは\x01",
            "私も同じだよ……\x02",
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

    def lambda_C202():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C202)
    Sleep(10)

    def lambda_C212():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C212)

    def lambda_C21F():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C21F)
    Sleep(18)

    def lambda_C22F():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C22F)
    Sleep(300)

    #C0532
    ChrTalk(
        0x9,
        (
            "#5Pあれは『聖者の祈り』といって、\x01",
            "クロスベル自治州が成立した際に\x01",
            "高名な彫刻家が製作した彫像なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x102,
        (
            "#12P#0100Fマグナス・ヘクトール作、\x01",
            "『聖者の祈り』ですね。\x02\x03",

            "#0103Fクロスベルが生んだ稀代の彫刻家が\x01",
            "自治州の創立を讃えて彫った傑作……\x02\x03",

            "#0100Fその歴史的背景もあって、\x01",
            "市庁舎の象徴とされたと聞くわ。\x02\x03",

            "#0108Fその膝元の議会で\x01",
            "帝国や共和国派が幅を利かせているのは\x01",
            "皮肉だと思うけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x9,
        "#5Pはは、まったくですな。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x9,
        (
            "#5Pまあそれはともかく、\x01",
            "あれはクロスベルの誇りとも\x01",
            "言われる大切な物なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x9,
        (
            "#5Pおまけに本日午後には閉会式や\x01",
            "賓客のレセプションがあるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x9,
        (
            "#5Pはあ、祝いの日に\x01",
            "こんなみっともない所は\x01",
            "見せられないよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x101,
        (
            "#6P#0003F確かに、これじゃ\x01",
            "クロスベルは諸国の笑い者ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x104,
        (
            "#12P#0301F少なくともクロスベル警察の\x01",
            "お株は大暴落だろうな。\x02\x03",

            "#0306Fまたクロスベルタイムズ辺りに\x01",
            "デカデカと書き立てられそうだぜ。\x02",
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
            "#12P#0203Fランディさん……\x01",
            "余計な事を言わないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        (
            "#12P#0306F悪ぃ、つい頭に\x01",
            "思い浮かんじまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#6P#0003F本当にありえるだけに\x01",
            "笑えないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x9,
        (
            "#5Pはああ、それだけは\x01",
            "勘弁してくれよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x9,
        (
            "#5P市庁舎はただでさえ\x01",
            "スキャンダルやらなにやらで\x01",
            "書き立てられているんだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x102,
        (
            "#12P#0103F捜査を急いだ方が良さそうね……\x02\x03",

            "#0105Fええと、でもクリップさん、\x01",
            "犯人の手がかりはあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x9,
        (
            "#5Pああ……それが\x01",
            "現場にこのような物が。\x02",
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
            "クリップは１枚のカードを差し出した。\x02",
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
            "警察の特務支援課とやらよ、\x01",
            "我が謎に挑みてその知力を示すがいい。\x02",
        )
    )

    CloseMessageWindow()

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　 始まりの鍵は 　\x01",
            " 時告げぬ街の象徴 \x01",
            "仰いで昏き天を見よ\x01",
            "　　　　──怪盗Ｂ\x02",
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
        "#6P#0005F怪盗Ｂ……だって……！？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#12P#0105F……まさかクロスベルに現れるなんて……\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x104,
        (
            "#12P#0300Fハッ、たかが泥棒風情が、\x01",
            "えらいカッコつけた名前を\x01",
            "名乗ってやがるじゃねえか。\x02\x03",

            "#0303F……ってか待てよ、その名前どっかで\x01",
            "聞いた事があるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x103,
        (
            "#12P#0203Fわたしも耳にしたことが\x01",
            "ある気がします。\x02\x03",

            "#0200F……お二人は\x01",
            "何かご存知のようですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#6P#0003F俺は聞いた事がある程度だけど……\x02\x03",

            "#0001F確か、外国では超がつくほど\x01",
            "有名な犯罪者だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x102,
        (
            "#12P#0103F……帝国を中心に活動する\x01",
            "数々の美術品を盗んできた\x01",
            "神出鬼没の怪人……\x02\x03",

            "#0100Fそれが『怪盗Ｂ』と呼ばれる人物よ。\x02\x03",

            "犯行予告を記したカードを送るという\x01",
            "大胆不敵な方法をとりながら、\x01",
            "一度として捕まったことはない。\x02\x03",

            "数々の摩訶不思議な奇術を操り\x01",
            "鮮やかに獲物を盗み出すその姿は、\x01",
            "一部で英雄視すらされているとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x103,
        (
            "#12P#0203Fそして、その怪盗が今回……\x01",
            "わたしたちに挑戦状を\x01",
            "たたきつけているわけですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x9,
        (
            "#5Pああ、今回遊撃士ではなく\x01",
            "君たちを呼んだ理由もそこにあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x9,
        (
            "#5Pなんせ、はっきり『特務支援課』と\x01",
            "名指ししていたものだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x104,
        "#12P#0304F……へっ、面白えじゃねぇか。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    #C0560
    ChrTalk(
        0x104,
        (
            "#12P#0300Fおいロイド、\x01",
            "怪盗だか何だか知らねえが\x01",
            "とっ捕まえてやろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CD99():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CD99)

    def lambda_CDA6():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CDA6)

    def lambda_CDB3():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CDB3)
    Sleep(300)

    #C0561
    ChrTalk(
        0x101,
        (
            "#6P#0001Fああ、盗まれた彫像も\x01",
            "取り戻す必要がある……\x01",
            "この挑戦、受けて立とう！\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x102,
        "#12P#0100Fそうね、やりましょう。\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x103,
        (
            "#12P#0200F謎掛けの言葉は\x01",
            "『時告げぬ街の象徴』ですね……\x01",
            "どうやら街の中のようですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x104,
        (
            "#12P#0300Fよし、市内の心当たりを\x01",
            "探してみるか！\x02",
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
            "クエスト【市庁舎からの至急要請】\x07\x00",
            "を開始した！\x02",
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

    # Function_30_BCB4 end

    def Function_31_CF5B(): pass

    label("Function_31_CF5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CF99")
    OP_95(0xFE, 3550, 4000, 18550, 1000, 0x0)
    Sleep(200)
    OP_95(0xFE, 5980, 4000, 18550, 1000, 0x0)
    Sleep(200)
    Jump("Function_31_CF5B")

    label("loc_CF99")

    Return()

    # Function_31_CF5B end

    def Function_32_CF9A(): pass

    label("Function_32_CF9A")

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
            "#6Pまさかこれほど早く\x01",
            "戻ってくるとは……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D126():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D126)
    Sleep(20)

    def lambda_D136():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D136)
    Sleep(12)

    def lambda_D146():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D146)

    def lambda_D153():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D153)
    Sleep(15)

    def lambda_D163():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_D163)
    Sleep(400)

    #C0567
    ChrTalk(
        0x9,
        (
            "#6P支援課のみんな、ありがとう。\x01",
            "心より感謝するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        (
            "#11P#0012Fははは……大変でしたが\x01",
            "無事に解決できてよかったです。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x14, 1, 0, 33)

    #C0569
    ChrTalk(
        0x102,
        (
            "#11P#0100Fこれで閉会式やレセプションも\x01",
            "無事に行えますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x9,
        (
            "#6Pええ、本当に。\x01",
            "これで私も一安心だ。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 1)
    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)

    def lambda_D26D():
        OP_95(0xFE, -1570, 4000, 18500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D26D)
    OP_95(0x14, -1570, 4000, 18500, 1000, 0x0)
    OP_95(0x14, -490, 4000, 18500, 1000, 0x0)
    OP_93(0x14, 0xB4, 0x1F4)

    #C0571
    ChrTalk(
        0x13,
        "#5Pうっす、設置完了ですぜ！\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x14,
        "#11Pまいどありがとーございやした！\x02",
    )

    CloseMessageWindow()

    def lambda_D2FF():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D2FF)
    Sleep(20)

    def lambda_D30F():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D30F)
    Sleep(12)

    def lambda_D31F():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D31F)

    def lambda_D32C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D32C)
    Sleep(15)

    def lambda_D33C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_D33C)
    Sleep(300)

    #C0573
    ChrTalk(
        0x9,
        (
            "#6Pおっとそうか、\x01",
            "ご苦労だったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x104,
        "#12P#0300Fサンキュー、助かったぜ。\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x13,
        "#5Pハハ、たいした大荷物だったぜ。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x14,
        (
            "#11Pじゃ、自分らはこれにて\x01",
            "失礼しやーす！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D3F2():

        label("loc_D3F2")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_D3F2")

    QueueWorkItem2(0x0, 1, lambda_D3F2)

    def lambda_D404():

        label("loc_D404")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_D404")

    QueueWorkItem2(0x1, 1, lambda_D404)

    def lambda_D416():

        label("loc_D416")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_D416")

    QueueWorkItem2(0x2, 1, lambda_D416)

    def lambda_D428():

        label("loc_D428")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_D428")

    QueueWorkItem2(0x3, 1, lambda_D428)

    def lambda_D43A():

        label("loc_D43A")

        TurnDirection(0xFE, 0x13, 300)
        Yield()
        Jump("loc_D43A")

    QueueWorkItem2(0x9, 1, lambda_D43A)
    BeginChrThread(0x13, 0, 0, 34)
    BeginChrThread(0x14, 0, 0, 34)
    Sleep(3500)

    #C0577
    ChrTalk(
        0x9,
        (
            "#6Pふう……彼らにも少し\x01",
            "迷惑を掛けてしまったかな。\x01",
            "後でチップを弾んであげないと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_D4D7():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D4D7)

    def lambda_D4E4():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D4E4)

    def lambda_D4F1():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D4F1)

    def lambda_D4FE():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D4FE)

    def lambda_D50B():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_D50B)
    Sleep(300)

    #C0578
    ChrTalk(
        0x9,
        (
            "#6Pそうそう、君たちには\x01",
            "個人的にご褒美を渡しておくよ。\x02",
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
            "クリップ主任から包みを受け取った。\x02",
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
            "#11P#0005Fこれはどうも……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x9,
        (
            "#6Pそれでは、私はこれで。\x01",
            "運送会社のスタッフを\x01",
            "見送らないとね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D63C():

        label("loc_D63C")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_D63C")

    QueueWorkItem2(0x0, 1, lambda_D63C)

    def lambda_D64E():

        label("loc_D64E")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_D64E")

    QueueWorkItem2(0x1, 1, lambda_D64E)

    def lambda_D660():

        label("loc_D660")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_D660")

    QueueWorkItem2(0x2, 1, lambda_D660)

    def lambda_D672():

        label("loc_D672")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_D672")

    QueueWorkItem2(0x3, 1, lambda_D672)
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
        "#12P#0303Fふう、一件落着だな。\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x102,
        (
            "#11P#0100Fあちこち歩き回る羽目に\x01",
            "なっちゃったわね。\x02",
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
            "#12P#0205Fロイドさん、その包みは\x01",
            "何だったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        "#5P#0005Fああ、そうだった。\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_D789():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D789)

    def lambda_D796():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D796)

    def lambda_D7A3():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D7A3)

    def lambda_D7B0():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D7B0)
    Sleep(400)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0586
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "包みの中には『人馬珠』が入っていた。\x02",
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
            "を手に入れた。\x02",
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
            "#12P#0200Fこれは……クオーツですね。\x01",
            "一般には流通していない\x01",
            "タイプのようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x104,
        (
            "#12P#0305F市庁舎のお役人にしちゃあ\x01",
            "意外なモンを持ってるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x101,
        (
            "#5P#0005Fそうだな、\x01",
            "どうしてこんな物を……\x02",
        )
    )

    CloseMessageWindow()
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -15910, 4000, 10130, 39)

    #N0591
    NpcTalk(
        0x9,
        "男性の声",
        "ああっ、君たち……！\x02",
    )

    CloseMessageWindow()
    SetMapObjFlags(0x3, 0x4)

    def lambda_D94D():

        label("loc_D94D")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_D94D")

    QueueWorkItem2(0x0, 1, lambda_D94D)

    def lambda_D95F():

        label("loc_D95F")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_D95F")

    QueueWorkItem2(0x1, 1, lambda_D95F)

    def lambda_D971():

        label("loc_D971")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_D971")

    QueueWorkItem2(0x2, 1, lambda_D971)

    def lambda_D983():

        label("loc_D983")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_D983")

    QueueWorkItem2(0x3, 1, lambda_D983)
    OP_68(-12890, 5500, 12540, 2200)
    Sleep(2200)

    def lambda_D9A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D9A9)
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
            "#6P彫像が戻ったというのは\x01",
            "本当かい！？\x02",
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
            "#6Pおお、本当だ！\x01",
            "君達が見つけて来てくれたのか！\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x9,
        (
            "#6Pもう運び込んでくれたなんて、\x01",
            "いやあ大したものだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(200)

    #C0595
    ChrTalk(
        0x9,
        "#6Pありがとう、特務支援課の諸君！\x02",
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
            "#11P#0005Fあ、あの、クリップさん……\x01",
            "さっき市庁舎を出て行かれたり\x01",
            "しませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x9,
        "#6Pえ、何を言ってるんだい？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x9,
        (
            "#6P私はさっきから向こうのホールで\x01",
            "閉会式の打ち合わせをしていたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x102,
        (
            "#11P#0105Fま、まさか……\x01",
            "……そんな…………\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        (
            "#12P#0203Fこれが怪盗Ｂの手際……\x01",
            "鮮やかすぎです……\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x104,
        (
            "#12P#0301Fさすが国際的な怪盗……\x01",
            "簡単には捕まりそうにねえなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x9,
        "#6Pあの、どうかしたのかい？\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x9,
        (
            "#6Pとにかく、ありがとう！\x01",
            "これで安心して閉会式が開けるよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x101,
        (
            "#11P#0000Fははは、そうですね。\x02\x03",

            "#0003F（怪盗Ｂ、か……\x01",
            "  悪意はないみたいだったけど\x01",
            "  犯罪者には違いない。）\x02\x03",

            "#0001F（いつかきちんと\x01",
            "  ケリを付けたい所だな……）\x02",
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
            "クエスト【市庁舎からの至急要請】\x07\x00",
            "を達成した！\x02",
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

    # Function_32_CF9A end

    def Function_33_DE7D(): pass

    label("Function_33_DE7D")

    OP_95(0x14, -1610, 4000, 18500, 1000, 0x0)
    OP_93(0x14, 0x0, 0x1F4)
    OP_93(0x13, 0xB4, 0x1F4)
    Return()

    # Function_33_DE7D end

    def Function_34_DEA0(): pass

    label("Function_34_DEA0")

    OP_95(0xFE, -4770, 4000, 17860, 2000, 0x0)
    OP_95(0xFE, -8119, 4000, 12220, 2000, 0x0)
    Return()

    # Function_34_DEA0 end

    def Function_35_DEC9(): pass

    label("Function_35_DEC9")

    EventBegin(0x1)

    #C0606
    ChrTalk(
        0x101,
        (
            "#0000F（シンポジウム会場の警備で\x01",
            "  一課とアリオスさんがいる……）\x02\x03",

            "（邪魔するのは止めておこう。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -13650, 4000, 12700, 45)
    EventEnd(0x4)
    Return()

    # Function_35_DEC9 end

    def Function_36_DF46(): pass

    label("Function_36_DF46")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_DFC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 6)), scpexpr(EXPR_END)), "loc_DFBF")
    SetChrName("")

    #A0607
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉の中から、市長と議長たちの\x01",
            "重苦しい話が聞こえてくる……\x02\x03",

            "邪魔しない方が良さそうだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DFBF")

    Jump("loc_E199")

    label("loc_DFC4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0608
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州政府\x01",
            "　　 市長執務室 　　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E16A")

    #C0609
    ChrTalk(
        0x101,
        (
            "#0000Fここは……マクダエル市長の\x01",
            "執務室みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x102,
        (
            "#0100Fそういえば、おじいさまは\x01",
            "いつでも訪ねてきてくれって\x01",
            "仰っていたわね……\x02\x03",

            "お忙しい人だから\x01",
            "部屋にいらっしゃるか\x01",
            "分からないけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        (
            "#0003Fそうだったのか……\x02\x03",

            "#0000Fまあそれなら\x01",
            "一度挨拶くらいはしておいた方が\x01",
            "いいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 6)
    OP_65(0x2, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_E199")

    label("loc_E16A")

    Sound(810, 0, 100, 0)

    #A0612
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E199")

    TalkEnd(0xFF)
    Return()

    # Function_36_DF46 end

    def Function_37_E19D(): pass

    label("Function_37_E19D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0613
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州政府\x01",
            "   市庁舎行政区画\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E232")

    #C0614
    ChrTalk(
        0x101,
        (
            "#0003Fこっちに入る必要は\x01",
            "なさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_E232")

    TalkEnd(0xFF)
    Return()

    # Function_37_E19D end

    SaveToFile()

Try(main)
