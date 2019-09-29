from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1150.bin",                # FileName
        "c1150",                    # MapName
        "c1150",                    # Location
        0x0018,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 5000, 1500, 0, 0, 1, 24, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1150",                  # 0
        "接待小姐瑞贝卡",         # 1
        "接待小姐芙兰",           # 2
        "多诺邦警督",             # 3
        "雷蒙德搜查官",           # 4
        "弗兰茨巡警",             # 5
        "警官",                   # 6
        "乔里基科长",             # 7
        "凯特巡警",               # 8
        "艾玛搜查官",             # 9
        "赛尔盖科长",             # 10
        "皮埃尔副局长",           # 11
        "警官",                   # 12
        "警官",                   # 13
        "警官",                   # 14
        "椅子",                   # 15
        "椅子",                   # 16
        "椅子",                   # 17
        "椅子",                   # 18
        "椅子",                   # 19
        "椅子",                   # 20
    ))

    AddCharChip((
        "chr/ch30400.itc",                   # 00
        "chr/ch06900.itc",                   # 01
        "chr/ch30300.itc",                   # 02
        "chr/ch30200.itc",                   # 03
        "chr/ch30000.itc",                   # 04
        "chr/ch30100.itc",                   # 05
        "chr/ch30100.itc",                   # 06
        "chr/ch02500.itc",                   # 07
        "chr/ch30600.itc",                   # 08
        "chr/ch30500.itc",                   # 09
        "chr/ch30002.itc",                   # 0A
        "chr/ch06400.itc",                   # 0B
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

    DeclNpc(-100,    0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3000,    0,       15930,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-60700,  29,      21360,   135,  389,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   4,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-58049,  0,       15899,   90,   261,  0x0, 0,   6,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-59229,  29,      21360,   270,  389,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-125379, 0,       19520,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-11039,  0,       13810,   90,   389,  0x0, 0,   7,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   11,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(-60659,  180,     20159,   180,  469,  0x0, 0,   10,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-60610,  129,     15789,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(-64050,  129,     15850,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 47,  -9.199999809265137,    10.0,                  -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.599999904632568,     -2.5,                  0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 48,  -12.699999809265137,   19.8700008392334,      -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.233333587646484,     -9.9350004196167,      0.1428571492433548,    1.0])

    DeclActor(-100,    0,       14400,   1100,    -100,    1500,    15400,   0x007E, 0,  5,  0x0000)
    DeclActor(2770,    0,       14280,   1000,    3000,    1500,    15930,   0x007E, 0,  8,  0x0000)
    DeclActor(1970,    0,       14310,   1000,    1970,    1500,    15610,   0x007E, 0,  8,  0x0000)
    DeclActor(1120,    0,       14070,   1000,    900,     1500,    15400,   0x007E, 0,  8,  0x0000)
    DeclActor(-9850,   0,       16000,   1000,    -9850,   1500,    16000,   0x007C, 0,  49, 0x0000)
    DeclActor(-9850,   0,       13750,   1000,    -9850,   1500,    13750,   0x007C, 0,  49, 0x0000)

    ScpFunction((
        "Function_0_59C",          # 00, 0
        "Function_1_654",          # 01, 1
        "Function_2_67F",          # 02, 2
        "Function_3_6D2",          # 03, 3
        "Function_4_C11",          # 04, 4
        "Function_5_D66",          # 05, 5
        "Function_6_D7B",          # 06, 6
        "Function_7_1532",         # 07, 7
        "Function_8_2E63",         # 08, 8
        "Function_9_2E67",         # 09, 9
        "Function_10_54B5",        # 0A, 10
        "Function_11_58E1",        # 0B, 11
        "Function_12_5BC0",        # 0C, 12
        "Function_13_69F7",        # 0D, 13
        "Function_14_7632",        # 0E, 14
        "Function_15_7736",        # 0F, 15
        "Function_16_791A",        # 10, 16
        "Function_17_7A48",        # 11, 17
        "Function_18_7C4C",        # 12, 18
        "Function_19_84AF",        # 13, 19
        "Function_20_868D",        # 14, 20
        "Function_21_8CB8",        # 15, 21
        "Function_22_90BB",        # 16, 22
        "Function_23_91B7",        # 17, 23
        "Function_24_92EA",        # 18, 24
        "Function_25_942C",        # 19, 25
        "Function_26_957F",        # 1A, 26
        "Function_27_96B7",        # 1B, 27
        "Function_28_9874",        # 1C, 28
        "Function_29_A1C4",        # 1D, 29
        "Function_30_AD69",        # 1E, 30
        "Function_31_ADBC",        # 1F, 31
        "Function_32_AE47",        # 20, 32
        "Function_33_BC19",        # 21, 33
        "Function_34_BDC2",        # 22, 34
        "Function_35_D87B",        # 23, 35
        "Function_36_D88B",        # 24, 36
        "Function_37_D8C8",        # 25, 37
        "Function_38_D912",        # 26, 38
        "Function_39_D95D",        # 27, 39
        "Function_40_DA13",        # 28, 40
        "Function_41_EDE7",        # 29, 41
        "Function_42_EEBD",        # 2A, 42
        "Function_43_EF68",        # 2B, 43
        "Function_44_FAA4",        # 2C, 44
        "Function_45_1009B",       # 2D, 45
        "Function_46_10EA5",       # 2E, 46
        "Function_47_10F2D",       # 2F, 47
        "Function_48_10FB5",       # 30, 48
        "Function_49_117DC",       # 31, 49
    ))


    def Function_0_59C(): pass

    label("Function_0_59C")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5DC"),
        (1, "loc_5E8"),
        (2, "loc_5F4"),
        (3, "loc_600"),
        (4, "loc_60C"),
        (5, "loc_618"),
        (6, "loc_624"),
        (SWITCH_DEFAULT, "loc_630"),
    )


    label("loc_5DC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_5E8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_5F4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_600")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_60C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_618")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_624")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_630")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_63C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_653")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_63C")

    label("loc_653")

    Return()

    # Function_0_59C end

    def Function_1_654(): pass

    label("Function_1_654")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67E")
    OP_94(0xFE, 0xFFFF8508, 0x24CC, 0xFFFF93C2, 0x288C, 0x3E8)
    Sleep(300)
    Jump("Function_1_654")

    label("loc_67E")

    Return()

    # Function_1_654 end

    def Function_2_67F(): pass

    label("Function_2_67F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D1")
    OP_95(0x12, -57300, 0, 20000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0xB4, 0x2EE)
    Sleep(500)
    OP_95(0x12, -57300, 0, 16000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0x0, 0x2EE)
    Sleep(500)
    Jump("Function_2_67F")

    label("loc_6D1")

    Return()

    # Function_2_67F end

    def Function_3_6D2(): pass

    label("Function_3_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_700")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, -125380, 0, 19520, 0)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_76B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B")
    OP_93(0x8, 0x5A, 0x0)
    SetChrPos(0x9, 1970, 0, 15610, 270)

    label("loc_72B")

    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xE, -57640, 0, 18750, 270)
    SetChrPos(0xD, -57640, 0, 17260, 270)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_BD9")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7B1")
    OP_93(0x8, 0x5A, 0x0)
    SetChrPos(0x9, 1970, 0, 15610, 270)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, -58050, 0, 15900, 90)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7F7")
    SetChrPos(0xA, -11040, 0, 13810, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    SetChrPos(0xD, -58050, 0, 15900, 90)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_83B")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, -12850, 0, 7690, 90)
    SetChrPos(0xB, -11260, 0, 7690, 270)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_BD9")

    label("loc_83B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_897")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, -123350, 0, 19180, 0)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892")
    SetChrPos(0x12, -57300, 0, 18000, 0)
    BeginChrThread(0x12, 0, 0, 2)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x80)

    label("loc_892")

    Jump("loc_BD9")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_916")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    SetChrPos(0xD, -29870, 0, 9900, 90)
    BeginChrThread(0xD, 0, 0, 1)
    SetChrPos(0xE, -11040, 0, 13810, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_911")
    SetChrPos(0x12, -57300, 0, 18000, 0)
    BeginChrThread(0x12, 0, 0, 2)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)

    label("loc_911")

    Jump("loc_BD9")

    label("loc_916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_94A")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xD, -57630, 0, 17300, 135)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 0)
    Jump("loc_BD9")

    label("loc_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_990")
    SetChrPos(0xA, -125380, 0, 19520, 0)
    SetChrPos(0xB, -123490, 0, 18220, 180)
    SetChrPos(0xD, -58050, 0, 15900, 90)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9D6")
    SetChrPos(0xA, -11040, 0, 13810, 90)
    SetChrPos(0xB, -12290, 0, 12530, 45)
    SetChrPos(0xD, -125380, 0, 19520, 0)
    SetChrFlags(0xE, 0x80)
    Jump("loc_BD9")

    label("loc_9D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A32")
    SetChrPos(0xA, -121660, 0, 18190, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    SetChrPos(0xD, -58050, 0, 15900, 180)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58050, 30, 14700, 0)
    Jump("loc_BD9")

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A9F")
    SetChrPos(0xA, -125380, 0, 19520, 0)
    SetChrPos(0xB, -11040, 0, 13810, 90)
    SetChrPos(0xE, -57420, 0, 18000, 270)
    SetChrPos(0xF, -57270, 0, 16580, 270)
    SetChrPos(0xD, -59320, 30, 21250, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_BD9")

    label("loc_A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_AEF")
    SetChrPos(0xA, -125380, 0, 19520, 0)
    SetChrPos(0xB, -11040, 0, 13810, 90)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -56940, 0, 19650, 90)
    Jump("loc_BD9")

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B91")
    SetChrPos(0xA, -126060, 0, 19340, 90)
    SetChrPos(0xB, -124880, 0, 19200, 270)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xF, -57420, 0, 16239, 90)
    SetChrPos(0xD, -57020, 0, 17260, 135)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B75")
    SetChrPos(0x9, 900, 0, 15400, 180)
    Jump("loc_B8C")

    label("loc_B75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_B8C")

    Jump("loc_BD9")

    label("loc_B91")

    SetChrPos(0x9, -100, 0, 15400, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_BED")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 33)
    Jump("loc_C10")

    label("loc_BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_C01")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 40)
    Jump("loc_C10")

    label("loc_C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_C10")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 31)

    label("loc_C10")

    Return()

    # Function_3_6D2 end

    def Function_4_C11(): pass

    label("Function_4_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_END)), "loc_C23")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C23")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C39")
    Jump("loc_C8A")

    label("loc_C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C54")
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)

    label("loc_C54")

    Jump("loc_C8A")

    label("loc_C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C6F")
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)
    Jump("loc_C8A")

    label("loc_C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C7D")
    Jump("loc_C8A")

    label("loc_C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C8A")
    OP_65(0x1, 0x1)

    label("loc_C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_CB8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB3")
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_CB3")

    Jump("loc_CC0")

    label("loc_CB8")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)

    label("loc_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE1")
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)

    label("loc_CE1")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D21")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_D38")

    label("loc_D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D38")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_D38")

    label("loc_D38")

    OP_1B(0x0, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5A")
    OP_1B(0x0, 0x0, 0x2E)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_D5A")

    ModifyEventFlags(1, 1, 0x80)
    ClearMapObjFlags(0x2, 0x10)
    Return()

    # Function_4_C11 end

    def Function_5_D66(): pass

    label("Function_5_D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D77")
    Call(0, 6)
    Jump("loc_D7A")

    label("loc_D77")

    Call(0, 9)

    label("loc_D7A")

    Return()

    # Function_5_D66 end

    def Function_6_D7B(): pass

    label("Function_6_D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D95")
    Call(0, 43)
    Return()

    label("loc_D95")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FAF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_EC2")

    #C0001
    ChrTalk(
        0x8,
        "呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "追加的支援请求\x01",
            "重新确认过了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        "#0100F嗯，确认过了，没问题。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0000F我们打算立刻前去\x01",
            "解决通缉魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "这样啊……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "通缉魔兽应该在地下空间A区域，\x01",
            "靠近终点的那一带。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "除此之外，也经常有\x01",
            "其它魔兽出没，\x01",
            "因此请多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 1)
    Jump("loc_F2F")

    label("loc_EC2")


    #C0008
    ChrTalk(
        0x8,
        (
            "这样一来，\x01",
            "【支援请求的补充说明】任务\x01",
            "就完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "请各位先回支援科一趟，\x01",
            "试着利用终端提交一下报告。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2F")


    #C0010
    ChrTalk(
        0x8,
        (
            "还有……关于支援请求的流程\x01",
            "今天随时都可以为大家说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "如果各位还有其它想要确认的事，\x01",
            "请不要客气，尽管提出来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4B, 0)
    Jump("loc_1277")

    label("loc_FAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1277")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF5")

    #C0012
    ChrTalk(
        0x8,
        (
            "关于通缉魔兽的讨伐，\x01",
            "辛苦大家了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF5")


    #C0013
    ChrTalk(
        0x8,
        (
            "对了，各位知道吗？\x01",
            "克洛斯贝尔警察正在进行\x01",
            "魔兽的情报调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0005F是……情报调查吗？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "嗯，我想各位应该知道\x01",
            "在战斗手册里记录着\x01",
            "有关魔兽的项目吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "各位曾经遭遇过的魔兽\x01",
            "都会被记录在战斗手册里哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "当情报积攒到一定程度时，\x01",
            "就请拿来给我看一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "因为各位所收集的情报对\x01",
            "警局内制定安全对策\x01",
            "很有帮助。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1177")

    #C0019
    ChrTalk(
        0x102,
        (
            "#0100F原来如此……警察局也\x01",
            "很下功夫啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F6")

    label("loc_1177")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B9")

    #C0020
    ChrTalk(
        0x103,
        (
            "#0200F原来如此……警察局也\x01",
            "很下功夫啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F6")

    label("loc_11B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11F6")

    #C0021
    ChrTalk(
        0x104,
        (
            "#0300F原来如此……警察局也\x01",
            "很下功夫啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F6")


    #C0022
    ChrTalk(
        0x8,
        (
            "嗯，这也是为了保卫\x01",
            "市民的安全。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "各位在向我提交魔兽情报时，\x01",
            "局内会多少支付一些报酬的，\x01",
            "所以请不要客气，随时过来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 2)
    SetScenarioFlags(0x2, 0)

    label("loc_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1364")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_128B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                      # 0
            "询问关于支援请求的事\x01",      # 1
            "放弃\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_12F7")

    label("loc_12F0")

    OP_60(0x0)
    OP_5A()
    Sleep(150)

    label("loc_12F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Call(0, 44)
    Sleep(150)
    Jump("loc_135A")

    label("loc_132A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_133E")
    Jump("loc_135A")

    label("loc_133E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_135A")

    Jump("loc_128B")

    label("loc_135F")

    Jump("loc_152E")

    label("loc_1364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1482")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1378")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                      # 0
            "询问关于支援请求的事\x01",      # 1
            "出示战斗手册\x01",              # 2
            "放弃\x01",                      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13EA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_13F1")

    label("loc_13EA")

    OP_60(0x0)
    OP_5A()
    Sleep(150)

    label("loc_13F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1424")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Call(0, 44)
    Sleep(150)
    Jump("loc_1478")

    label("loc_1424")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1448")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 1)
    Call(0, 45)
    Jump("loc_1478")

    label("loc_1448")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_145C")
    Jump("loc_1478")

    label("loc_145C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1478")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_1478")

    Jump("loc_1378")

    label("loc_147D")

    Jump("loc_152E")

    label("loc_1482")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_148C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "出示战斗手册\x01",      # 1
            "放弃\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 1)
    Call(0, 45)
    Jump("loc_1529")

    label("loc_14F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_150D")
    Jump("loc_1529")

    label("loc_150D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1529")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_1529")

    Jump("loc_148C")

    label("loc_152E")

    TalkEnd(0x8)
    Return()

    # Function_6_D7B end

    def Function_7_1532(): pass

    label("Function_7_1532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_15E5")

    #C0024
    ChrTalk(
        0x8,
        (
            "当情报积攒到一定程度时，\x01",
            "就请拿来给我看一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "因为各位所收集的情报对\x01",
            "制定安全对策很有帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "而且我们多少会支付一些报酬的，\x01",
            "所以请不要客气，随时过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E62")

    label("loc_15E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_16B7")

    #C0027
    ChrTalk(
        0x8,
        (
            "刚才，达德利警官\x01",
            "回到了总部，\x01",
            "但是表情相当严肃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "看起来，包括上级的动向在内，\x01",
            "整体状况变得十分严峻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "……请各位务必\x01",
            "多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B2")

    #C0030
    ChrTalk(
        0x101,
        "#0000F是……！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#0300F明白!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16B2")

    Jump("loc_2E62")

    label("loc_16B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_18C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1874")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x8,
        (
            "哎呀……\x01",
            "真是少见的阵容呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0000F啊，是啊……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x10A,
        (
            "#0603F嗯……稍微有些特殊原因。\x02\x03",

            "#0600F对了，瑞贝卡，\x01",
            "关于封锁空港一事……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "嗯，刚刚已经从\x01",
            "艾玛警官那里听说了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "本打算早一点\x01",
            "询问到事件情况的……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "算了，情况好像非常紧急，\x01",
            "就不再说些令人不快的话了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x10A,
        "#0603F……十分感谢。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0000F（达德利警官的气势\x01",
            "  有点被压倒了呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#0100F（这种情况真是\x01",
            "  难得一见啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18C0")

    label("loc_1874")


    #C0041
    ChrTalk(
        0x8,
        (
            "关于封锁空港的应对工作\x01",
            "就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "请各位专心处理\x01",
            "自己的任务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C0")

    Jump("loc_2E62")

    label("loc_18C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E0")
    Call(0, 11)
    Jump("loc_1943")

    label("loc_18E0")


    #C0043
    ChrTalk(
        0x8,
        (
            "话说回来，好像这次\x01",
            "也跟搜查二科\x01",
            "打过招呼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "这对持保密主义的一科来说，\x01",
            "实在是很罕见啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1943")

    Jump("loc_2E62")

    label("loc_1948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_19E5")

    #C0045
    ChrTalk(
        0x8,
        (
            "刚才已经有好几个人来询问\x01",
            "港湾区枪战的情况了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "要是再被媒体报道出来的话，\x01",
            "肯定会有更多人来询问。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "现在就有必要\x01",
            "好好考虑下对策了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E62")

    label("loc_19E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE7")

    #C0048
    ChrTalk(
        0x8,
        "哎呀，各位……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "有关『黑月』事务所遭受袭击一案，\x01",
            "搜查一科好像已经\x01",
            "正式展开行动了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "从早上开始，\x01",
            "全部人员都出动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#0005F是、是吗……\x01",
            "果然是行动迅速啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#0306F果然，这种案件的调查完全是\x01",
            "一科的独角戏啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B70")

    label("loc_1AE7")


    #C0053
    ChrTalk(
        0x8,
        (
            "搜查一科好像已经\x01",
            "正式展开行动了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "早上召开了调查会议，\x01",
            "之后好像就全员出动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0001F（不愧是一科……\x01",
            "  做事毫无纰漏。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B70")

    Jump("loc_2E62")

    label("loc_1B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1DF6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BF6")

    #C0056
    ChrTalk(
        0x8,
        (
            "芙兰按时回来了，\x01",
            "有点无聊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "她要是和那个外国男人\x01",
            "能够相处得更愉快的话，\x01",
            "肯定会很有意思的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF1")

    label("loc_1BF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1C69")

    #C0058
    ChrTalk(
        0x8,
        (
            "呵呵……听起来\x01",
            "就觉得会有很意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "芙兰休息的时候，\x01",
            "这里的工作就由我负责，\x01",
            "请放心好啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF1")

    label("loc_1C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA1")

    #C0060
    ChrTalk(
        0x8,
        "各位，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "其实，最近来\x01",
            "向警察求助的市民\x01",
            "稍稍增多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "呵呵，这都是多亏了\x01",
            "特别任务支援科的活跃表现啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……如果真是这样的话，\x01",
            "我们也很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        "嗯，我想肯定是这样的。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "呵呵……\x01",
            "我很期待各位今后的表现哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#0309F（瑞贝卡小姐……\x01",
            "  这话太让人感动了！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DF1")

    label("loc_1DA1")


    #C0067
    ChrTalk(
        0x8,
        (
            "其实，最近来\x01",
            "向警察求助的市民\x01",
            "稍稍增多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        "呵呵，这都是多亏了各位呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1DF1")

    Jump("loc_2E62")

    label("loc_1DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2124")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD8")

    #C0069
    ChrTalk(
        0x8,
        "哎呀，各位，好久不见。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x153,
        (
            "#1105F哇，姐姐好漂亮！\x02\x03",

            "#1111F嗯，该怎么说来着。\x01",
            "美人？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 500)

    #C0071
    ChrTalk(
        0x8,
        "哎呀……呵呵，真会说话呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0072
    ChrTalk(
        0x8,
        (
            "如传闻所说，确实\x01",
            "是个很可爱的小姑娘啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……\x01",
            "谢谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "……鲁巴彻商会已经派人来\x01",
            "进行非正式的『和谈』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "但是，慎重起见，\x01",
            "各位外出时还请多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#0000F是，明白。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1F80")

    #C0077
    ChrTalk(
        0x102,
        "#0101F我们会十分注意的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FD0")

    label("loc_1F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1FA0")

    #C0078
    ChrTalk(
        0x103,
        "#0200F了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FD0")

    label("loc_1FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1FD0")

    #C0079
    ChrTalk(
        0x104,
        (
            "#0300F有我们保护她呢，\x01",
            "没问题啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD0")

    SetScenarioFlags(0xB1, 1)
    Jump("loc_211F")

    label("loc_1FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208B")

    #C0080
    ChrTalk(
        0x8,
        (
            "对了，今天\x01",
            "地下空间Ａ２区域\x01",
            "好像出现了通缉魔兽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "由于导力终端正在进行维修，\x01",
            "所以无法发送情报……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "这只魔兽好像非常危险，\x01",
            "请大家一定要留心。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x25, 0x4, 0x2)
    SetScenarioFlags(0x0, 0)
    Jump("loc_211F")

    label("loc_208B")


    #C0083
    ChrTalk(
        0x8,
        (
            "今天导力终端正在进行维修，\x01",
            "所以芙兰也休息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "她从纪念庆典开始就没有休息，\x01",
            "一直在不停工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "呵呵，所以今天想让她\x01",
            "好好放松一天。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)

    label("loc_211F")

    Jump("loc_2E62")

    label("loc_2124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_21D4")

    #C0086
    ChrTalk(
        0x8,
        (
            "今天也要召开三场\x01",
            "有关纪念庆典的对策会议。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "纪念庆典期间的市内巡逻，\x01",
            "还有会场的警备体系……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "特别是开幕仪式，\x01",
            "各国的ＶＩＰ也会出席，\x01",
            "所以要特别注意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E62")

    label("loc_21D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_22F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2283")

    #C0089
    ChrTalk(
        0x8,
        (
            "搜查一科对保密主义\x01",
            "执行得很彻底。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "无论是何种案件的调查，\x01",
            "几乎都不会公开出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "不过……\x01",
            "考虑到他们负责的案件，\x01",
            "这也是没有办法的事呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22EB")

    label("loc_2283")


    #C0092
    ChrTalk(
        0x8,
        (
            "搜查一科对保密主义\x01",
            "执行得很彻底。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "虽然他们的态度可能冷静得近乎冷酷，\x01",
            "但这也是没有办法的事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EB")

    Jump("loc_2E62")

    label("loc_22F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_23F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2398")

    #C0094
    ChrTalk(
        0x8,
        (
            "随着纪念庆典的临近，\x01",
            "接待处的工作量也增多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "从露天店的开店许可\x01",
            "到各个街区\x01",
            "进行装饰和纪念活动的申请……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        "看来今年也会很忙啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23F4")

    label("loc_2398")


    #C0097
    ChrTalk(
        0x8,
        (
            "随着纪念庆典的临近，\x01",
            "接待处的工作量也增多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "只有在每年的这个季节\x01",
            "才会忙碌起来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F4")

    Jump("loc_2E62")

    label("loc_23F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_25B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2536")

    #C0099
    ChrTalk(
        0x8,
        "啊，艾莉和缇欧。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "刚才真是谢谢\x01",
            "你们的帮忙啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#0200F哪里，\x01",
            "帮上忙就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0100F借此机会，我们也了解了不少过去的事件，\x01",
            "学到了很多东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        "呵呵，那真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "警察局里也设置了\x01",
            "导力终端，数据库也会\x01",
            "不断慢慢完善的。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "可能还要借助你们的帮忙。\x01",
            "到时就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25B3")

    label("loc_2536")


    #C0106
    ChrTalk(
        0x8,
        (
            "警察局里也设置了\x01",
            "导力终端。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "也会渐渐把过去的事件\x01",
            "导入成数据库的。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "可能还要借助你们的帮忙，\x01",
            "到时就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B3")

    Jump("loc_2E62")

    label("loc_25B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_26ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2692")

    #C0109
    ChrTalk(
        0x8,
        (
            "搜查二科的雷蒙德警官\x01",
            "是个很有趣的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "每天早上，他都会到这里来\x01",
            "跟我说几句话。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "呵呵，今天早上说太久了，\x01",
            "结果被多诺邦警督\x01",
            "带走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#0000F（瑞贝卡小姐\x01",
            "  果然很受欢迎啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26E8")

    label("loc_2692")


    #C0113
    ChrTalk(
        0x8,
        (
            "二科的雷蒙德警官\x01",
            "是个很有趣的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "每天早上，他都会到这里来\x01",
            "跟我说几句话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26E8")

    Jump("loc_2E62")

    label("loc_26ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27FE")

    #C0115
    ChrTalk(
        0x8,
        (
            "警察局总部决定，将这周定为\x01",
            "预防犯罪强化周。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "各位，请仔细确认\x01",
            "门窗是否已经锁好。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0003F预防犯罪强化周……\x01",
            "有这种东西吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0118
    ChrTalk(
        0x8,
        (
            "嗯，果然\x01",
            "大家还不知道吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "在对市民的宣传上，\x01",
            "上级如果能再拨点预算就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2852")

    label("loc_27FE")


    #C0120
    ChrTalk(
        0x8,
        (
            "警察局总部决定，将这周定为\x01",
            "预防犯罪强化周。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "请各位市民\x01",
            "注意锁好家里门窗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2852")

    Jump("loc_2E62")

    label("loc_2857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A04")

    #C0122
    ChrTalk(
        0x8,
        (
            "索妮亚副司令\x01",
            "好像过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "副司令虽然是警备队的，\x01",
            "但也时常来总部。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#0005F话说回来，警察和警备队\x01",
            "没有什么交集的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "嗯……虽然名义上都\x01",
            "是『自治州警察』。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "但警备队的运作方式\x01",
            "类似军队，\x01",
            "故有其独立的指挥系统。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "警察局总部的局长和警备队的司令虽然级别相同，\x01",
            "但各司其职。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#0303F嗯，基本上这就是两个完全不同的组织。\x02\x03",

            "#0300F虽然偶尔也会有像我这种\x01",
            "从警备队调到警察局的情况存在。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A9B")

    label("loc_2A04")


    #C0129
    ChrTalk(
        0x8,
        (
            "警察局总部和警备队\x01",
            "在名义上属于同一个组织……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "但最高领导人各不相同，\x01",
            "可以说是两个完全无关的组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "经常过来的估计\x01",
            "就只有索妮亚副司令了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9B")

    Jump("loc_2E62")

    label("loc_2AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2AE7")

    #C0132
    ChrTalk(
        0x8,
        (
            "好像旧城区那边\x01",
            "发生了骚乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        "各位，请多加小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E62")

    label("loc_2AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2E62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BE8")

    #C0134
    ChrTalk(
        0x8,
        (
            "看来各位已经消灭\x01",
            "地下空间的通缉魔兽了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "这次的通缉魔兽情报也发给\x01",
            "了游击士协会，\x01",
            "因此各位并没有一定要消灭它的必要。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        (
            "而且，那只魔兽相当厉害，\x01",
            "我想用一般手段是对付不了的。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "但各位如果有信心的话，\x01",
            "请务必前去挑战。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E62")

    label("loc_2BE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_2D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D0E")

    #C0138
    ChrTalk(
        0x8,
        "呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "追加的支援请求\x01",
            "重新确认过了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        "#0100F嗯，确认过了，没问题。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000F我们打算立刻前去\x01",
            "解决通缉魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        "是啊……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "通缉魔兽应该在地下空间A区域，\x01",
            "靠近终点的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "除此之外，那里也再次聚集了\x01",
            "其它各种魔兽，\x01",
            "请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 1)
    Jump("loc_2D82")

    label("loc_2D0E")


    #C0145
    ChrTalk(
        0x8,
        (
            "通缉魔兽应该在地下空间A区域，\x01",
            "靠近终点的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "除此之外，那里也再次聚集了\x01",
            "其它各种魔兽，\x01",
            "请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D82")

    Jump("loc_2E62")

    label("loc_2D87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E62")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0147
    ChrTalk(
        0x8,
        (
            "这样一来，\x01",
            "【支援请求的补充说明】任务\x01",
            "就完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        (
            "请各位先回支援科一趟，\x01",
            "试着利用终端提交一下报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "#1900F呵呵，我会负责\x01",
            "处理各位提交的报告的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_2E62")

    label("loc_2E62")

    Return()

    # Function_7_1532 end

    def Function_8_2E63(): pass

    label("Function_8_2E63")

    Call(0, 9)
    Return()

    # Function_8_2E63 end

    def Function_9_2E67(): pass

    label("Function_9_2E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E79")
    Call(0, 34)
    Return()

    label("loc_2E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E93")
    Call(0, 43)
    Return()

    label("loc_2E93")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_312C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A4")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0150
    ChrTalk(
        0x9,
        (
            "#1905F咦……各位\x01",
            "现在是要出去吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0300F嗯，我们要去下\x01",
            "乌尔斯拉医院那边。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#0200F芙兰小姐，你看起来\x01",
            "好像很疲惫，\x01",
            "没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "#1900F啊，呵呵……\x02\x03",

            "因为今天不断有人来询问\x01",
            "封锁空港的事呢。\x02\x03",

            "#1903F好像是因为一封炸弹恐吓信引起的，\x01",
            "但听说那信息是假的，总算松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        "#0002F是吗……辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "#1909F呵呵，我稍微休息了下，\x01",
            "现在又干劲十足了。\x02\x03",

            "#1900F如果有什么问题，\x01",
            "请跟我联系。\x02\x03",

            "身为各位的联络员，\x01",
            "我会认真负责，\x01",
            "做好自己的工作的。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        "#0100F呵呵，多多指教哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 6)
    Jump("loc_3127")

    label("loc_30A4")


    #C0157
    ChrTalk(
        0x9,
        (
            "#1900F去乌尔斯拉医院的话，\x01",
            "只要乘坐导力巴士，很快就可以到了。\x02\x03",

            "虽然应该没什么可担心的，\x01",
            "但是如果有什么事情的话，\x01",
            "请跟我联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3127")

    Jump("loc_54B1")

    label("loc_312C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_324D")
    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "芙兰正在用通讯器进行通话。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0159
    ChrTalk(
        0x9,
        (
            "#1901F是，是……\x02\x03",

            "#1903F……真是对不起，\x01",
            "封锁只是暂时性的。\x02\x03",

            "#1901F大概再有一个小时\x01",
            "就会解禁了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3248")

    #C0160
    ChrTalk(
        0x101,
        (
            "#0000F（是在应付各个方面\x01",
            "  对封锁空港的询问吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0100F（嗯，她好像很忙，\x01",
            "  我们就不要打扰她了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3248")

    Jump("loc_54B1")

    label("loc_324D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_32D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3268")
    Call(0, 11)
    Jump("loc_32CC")

    label("loc_3268")


    #C0162
    ChrTalk(
        0x9,
        (
            "#1901F虽说是暂时的，\x01",
            "但竟然封锁了空港……\x02\x03",

            "#1903F唔，昨天还发生了袭击事件，\x01",
            "真是让人不安啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32CC")

    Jump("loc_54B1")

    label("loc_32D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_33B1")

    #C0163
    ChrTalk(
        0x9,
        (
            "#1900F啊，各位，\x01",
            "辛苦了~\x02\x03",

            "关于『黑月』袭击事件，\x01",
            "没有什么后续消息呢。\x02\x03",

            "#1903F希望这件事能够\x01",
            "大事化小，小事化了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33AC")

    #C0164
    ChrTalk(
        0x101,
        "#0003F嗯……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#0100F目前来看，这件案子似乎\x01",
            "也只能交给一科来负责了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_33AC")

    Jump("loc_54B1")

    label("loc_33B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34D2")
    TurnDirection(0x9, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348A")

    #C0166
    ChrTalk(
        0x9,
        (
            "#1905F咦咦，是枪战吗？\x02\x03",

            "这么危险啊……\x01",
            "到底发生了什么事啊～？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        (
            "#0200F（芙兰小姐好像\x01",
            "  刚刚才听说这件事啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0003F（在搜查一科的管辖\x01",
            "  之下，相关情报果然很难流出……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34CD")

    label("loc_348A")


    #C0169
    ChrTalk(
        0x9,
        (
            "#1905F真、真是危险的事件啊……\x02\x03",

            "#1901F我……\x01",
            "总觉得满肚子火！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CD")

    Jump("loc_54B1")

    label("loc_34D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_367B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_35EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3541")

    #C0170
    ChrTalk(
        0x9,
        (
            "#1900F安敦先生\x01",
            "已经回去了吧？\x02\x03",

            "#1903F我还没来得及感谢\x01",
            "他邀请我吃饭呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35E6")

    label("loc_3541")


    #C0171
    ChrTalk(
        0x9,
        (
            "#1900F托各位的福，我和安敦先生\x01",
            "一起开心地吃了顿饭。\x02\x03",

            "#1909F各位，姐姐。\x01",
            "真的非常感谢了～\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#0006F（明明把爱慕自己的男人甩了，\x01",
            " 却好像完全没有察觉啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_35E6")

    Jump("loc_3676")

    label("loc_35EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_365E")

    #C0173
    ChrTalk(
        0x9,
        (
            "#1900F再等一会，我就会去\x01",
            "中央广场的\x01",
            "西餐厅『温赛特』。\x02\x03",

            "#1909F请各位替我跟安敦先生\x01",
            "问声好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3676")

    label("loc_365E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3673")
    Call(0, 32)
    Jump("loc_3676")

    label("loc_3673")

    Call(0, 10)

    label("loc_3676")

    Jump("loc_54B1")

    label("loc_367B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3689")
    Jump("loc_54B1")

    label("loc_3689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_END)), "loc_3876")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3832")

    #C0174
    ChrTalk(
        0x9,
        (
            "#1900F那个，各位……\x01",
            "好像有什么急事啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        "#0000F啊，其实……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向芙兰说明了调查情况，\x01",
            "告诉了她在『星见之塔』前\x01",
            "遇见诺艾尔的事。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x9,
        (
            "#1905F有、有那回事啊……\x02\x03",

            "那姐姐呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        (
            "#0301F啊，她现在还在塔前\x01",
            "等着我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x102,
        (
            "#0100F我们打算在准备完后，\x01",
            "就回去跟她汇合。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "#1903F这样啊……\x02\x03",

            "#1901F……各位，请多加小心。\x02\x03",

            "还有，姐姐就\x01",
            "拜托你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 6)
    Jump("loc_3871")

    label("loc_3832")


    #C0181
    ChrTalk(
        0x9,
        (
            "#1901F各位，请多加小心。\x02\x03",

            "以及姐姐就\x01",
            "拜托你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3871")

    Jump("loc_54B1")

    label("loc_3876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_39A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3939")

    #C0182
    ChrTalk(
        0x9,
        (
            "#1900F彩虹的新剧将会\x01",
            "在纪念庆典的第一天首次上演。\x02\x03",

            "本来就已经很受欢迎了，\x01",
            "再加上又赶上了纪念庆典，\x01",
            "看来场面会十分盛大啊。\x02\x03",

            "#1906F呼，我也很想和\x01",
            "姐姐一起去看看啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_399B")

    label("loc_3939")


    #C0183
    ChrTalk(
        0x9,
        (
            "#1900F彩虹的新剧公演，\x01",
            "今年的场面似乎会十分盛大哦。\x02\x03",

            "#1906F呼，我也很想和\x01",
            "姐姐一起去看看啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399B")

    Jump("loc_54B1")

    label("loc_39A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3C18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B60")
    OP_93(0x9, 0x5A, 0x0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    #C0184
    ChrTalk(
        0x9,
        (
            "#1905F啊，各位……！\x02\x03",

            "#1903F那个，真的非常遗憾……\x01",
            "案件居然被交给一科了……\x02\x03",

            "#1900F作为各位的后援者，我\x01",
            "感到非常遗憾……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#0012F不，芙兰\x01",
            "你不用沮丧。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        (
            "#0100F芙兰小姐，谢谢。\x01",
            "我们不要紧的。\x02\x03",

            "因为已经把情绪\x01",
            "调整过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        (
            "#0200F如果还有支援请求的话，\x01",
            "请交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "#1903F是……正如各位所说呢。\x02\x03",

            "#1900F呵呵，对不起啊。\x02\x03",

            "#1901F联络员芙兰，\x01",
            "将会调整情绪，\x01",
            "继续努力的！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 6)
    Jump("loc_3C13")

    label("loc_3B60")


    #C0189
    ChrTalk(
        0x9,
        (
            "#1900F一科的人，即使经过接待处\x01",
            "都几乎不跟我们打招呼的……\x02\x03",

            "#1903F虽然知道他们很忙，\x01",
            "但还是感觉有点寒心啊～\x02\x03",

            "#1903F大家都是警察局里的同事，\x01",
            "如果能相处得更加融洽一点就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C13")

    Jump("loc_54B1")

    label("loc_3C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3EDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E6A")
    OP_93(0x9, 0x5A, 0x0)

    #C0190
    ChrTalk(
        0x9,
        (
            "#1906F嗯，有了导力网络之后，\x01",
            "我们接待处的工作量增加了许多。\x02\x03",

            "#1900F而且纪念庆典也临近了，\x01",
            "我得更加努力才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    #C0191
    ChrTalk(
        0x9,
        (
            "#1905F啊，各位～\x02\x03",

            "#1900F刚才那位委托人\x01",
            "怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_END)), "loc_3DC8")

    #C0192
    ChrTalk(
        0x101,
        (
            "#0003F啊，那个……情况比较复杂。\x02\x03",

            "#0000F我们现在正要去汇报。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        "#0108F…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0194
    ChrTalk(
        0x9,
        (
            "#1905F虽然不是很清楚……\x02\x03",

            "#1901F但希望各位多多加油进行调查哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E62")

    label("loc_3DC8")


    #C0195
    ChrTalk(
        0x101,
        (
            "#0000F嗯，我们已经接受委托了。\x02\x03",

            "#0001F虽然这案件好像很棘手……\x01",
            "但无法坐视不理。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "#1900F呵呵，太好了～\x02\x03",

            "#1901F那么，希望各位\x01",
            "多多加油进行调查哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E62")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3ED8")

    label("loc_3E6A")


    #C0197
    ChrTalk(
        0x9,
        (
            "#1900F最近，有了导力网络之后，\x01",
            "我们接待处的工作量增加了许多。\x02\x03",

            "而且纪念庆典也临近了，\x01",
            "我得更加努力才行～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED8")

    Jump("loc_54B1")

    label("loc_3EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_END)), "loc_401A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FB1")

    #C0198
    ChrTalk(
        0x9,
        (
            "#1900F啊，各位，\x01",
            "你们去找委托人了吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        (
            "#0304F嗯……\x01",
            "总之很大哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        "#1905F？？？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        "#0006F兰迪……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x103,
        "#0203F真是让人无话可说了。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#0111F哈……\x01",
            "你也稍微自重一点吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4015")

    label("loc_3FB1")


    #C0204
    ChrTalk(
        0x9,
        (
            "#1903F虽然不知道怎么回事，\x01",
            "但感觉好像很严重啊。\x02\x03",

            "#1900F各位，请务必\x01",
            "帮助那位女孩解决烦恼哦～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4015")

    Jump("loc_54B1")

    label("loc_401A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_END)), "loc_41E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4194")

    #C0205
    ChrTalk(
        0x9,
        (
            "#1900F啊，各位！\x02\x03",

            "委托人是个\x01",
            "很可爱的女孩子哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        "#0301F罗伊德，我们火速回去吧！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40AC")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_40AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40D2")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_40D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40F8")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_40F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_411E")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_411E")

    Sleep(1000)

    #C0207
    ChrTalk(
        0x9,
        (
            "#1903F那个……\x02\x03",

            "#1901F因为情况似乎很严重，\x01",
            "我就请她直接去支援科\x01",
            "那边了。\x02\x03",

            "#1900F请各位也\x01",
            "尽快过去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41DF")

    label("loc_4194")


    #C0208
    ChrTalk(
        0x9,
        (
            "#1900F我请委托人\x01",
            "直接去支援科\x01",
            "那边了。\x02\x03",

            "方便的话，\x01",
            "还请各位尽快过去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41DF")

    Jump("loc_54B1")

    label("loc_41E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4383")

    #C0209
    ChrTalk(
        0x9,
        (
            "#1906F啊，各位！\x01",
            "请听我说～\x02\x03",

            "#1901F前几天，警察局的地下\x01",
            "设置了一个搜查一科专用的\x01",
            "高级作战室哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#0000F啊，有这样的事啊。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x9,
        (
            "#1903F嗯，那是个\x01",
            "很高级的房间。\x02\x03",

            "里面专门的联络员\x01",
            "就有三个了。\x02\x03",

            "#1901F不……不甘心啊。\x01",
            "我明明不比她们差！\x02",
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

    #C0212
    ChrTalk(
        0x104,
        (
            "#0303F这个……\x01",
            "我们和搜查一科可不能比啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4424")

    label("loc_4383")


    #C0213
    ChrTalk(
        0x9,
        (
            "#1903F前几天，警察局的地下\x01",
            "设置了一个搜查一科专用的\x01",
            "高级作战室哦。\x02\x03",

            "#1901F唔，我也不会输给她们。\x01",
            "一定会竭尽全力支援各位！\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#0000F哈哈，今后请多关照啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4424")

    Jump("loc_54B1")

    label("loc_4429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_46D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4673")

    #C0215
    ChrTalk(
        0x9,
        "#1909F呵呵……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#0300F哦，小芙兰。\x01",
            "你好像很开心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x9,
        (
            "#1900F啊，各位～\x01",
            "听我说哦！\x02\x03",

            "#1909F刚才姐姐\x01",
            "来这里了～\x02\x03",

            "#1900F虽然她昨天好像也来了，\x01",
            "但我们没能遇上。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0000F啊，姐姐是指……\x01",
            "诺艾尔上士吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#0100F上士刚才还正式\x01",
            "向我们做了自我介绍，\x02\x03",

            "似乎是个爽快果断，\x01",
            "而且严守礼仪的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#0200F不过性格上好像\x01",
            "和芙兰小姐相去甚远呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "#1900F呵呵，对哦。\x02\x03",

            "#1903F姐姐\x01",
            "英姿飒爽又帅气，\x01",
            "而且同时也很可爱哦……\x02\x03",

            "#1900F我从小时候开始\x01",
            "就一直很崇拜她呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，你好像\x01",
            "很为姐姐骄傲啊。\x02\x03",

            "#0008F（……兄弟姐妹吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 6)
    Jump("loc_46CB")

    label("loc_4673")


    #C0223
    ChrTalk(
        0x9,
        (
            "#1900F罗伊德警官，你们今天要\x01",
            "去玛因兹吧？\x02\x03",

            "姐姐也对你们抱有很高的期待，\x01",
            "请加油哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46CB")

    Jump("loc_54B1")

    label("loc_46D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A42")
    OP_4B(0x8, 0xFF)

    #C0224
    ChrTalk(
        0x9,
        (
            "#1900F各位，辛苦了。\x02\x03",

            "阿尔摩利卡村的调查\x01",
            "怎么样了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#0006F嗯，现阶段还什么都不清楚。\x01",
            "我们所得到的信息并不比\x01",
            "警备队的调查记录更多。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x9,
        "#1903F这样啊，真可惜～……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0227
    ChrTalk(
        0x9,
        (
            "#1900F话说回来，这次的事件\x01",
            "警备队也有参与调查吧。\x02\x03",

            "姐姐应该出动了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    #C0228
    ChrTalk(
        0x8,
        (
            "呵呵……芙兰的姐姐在警备队，\x01",
            "她很为姐姐骄傲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "每天都在\x01",
            "说关于她姐姐的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)
    TurnDirection(0x9, 0x8, 500)
    TurnDirection(0x8, 0x9, 500)

    #C0230
    ChrTalk(
        0x9,
        (
            "#1906F瑞贝卡小姐，你真是的……\x02\x03",

            "那是因为姐姐都\x01",
            "没怎么跟我联络……\x02\x03",

            "#1900F就只是因为这样～！\x01",
            "并不是因为我觉得\x01",
            "寂寞哦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0231
    ChrTalk(
        0x104,
        (
            "#0303F（虽然对警察局总部都没有\x01",
            "  什么好印象……）\x02\x03",

            "#0300F（但只要来接待处这边就能得到治愈啊～⊥）\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        (
            "#0102F（让这两个人当接待处接待的理由……\x01",
            "  我好像有点明白了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x6B, 5)
    Jump("loc_4B2D")

    label("loc_4A42")


    #C0233
    ChrTalk(
        0x9,
        (
            "#1903F咳咳，请忘掉刚才\x01",
            "我说的话。\x02\x03",

            "#1900F我也是个警察，\x01",
            "所以不能公私不分。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)

    #C0234
    ChrTalk(
        0x9,
        (
            "#1903F……哈，姐姐。\x01",
            "现在正在做什么呢～……\x02",
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

    label("loc_4B2D")

    Jump("loc_54B1")

    label("loc_4B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ECF")
    OP_93(0x9, 0x5A, 0x0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    #C0235
    ChrTalk(
        0x9,
        (
            "#1905F啊，各位，我听到消息了。\x02\x03",

            "#1900F你们是要去市区外\x01",
            "调查魔兽侵害的事件吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#0000F嗯，我们正准备去\x01",
            "阿尔摩利卡村\x01",
            "看一看。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        (
            "#1901F我芙兰·希卡，\x01",
            "将会全力支持各位！\x02\x03",

            "#1903F……虽然我很想这么说……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0238
    ChrTalk(
        0x9,
        (
            "#1900F但是，我担心在那边\x01",
            "会没法使用导力通讯。\x02\x03",

            "嗯，我也不太清楚～\x01",
            "但在市区内应该是没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        (
            "#0005F这、这样啊。\x01",
            "难道当距离较远时，\x01",
            "就无法使用艾尼格玛进行通讯了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x103,
        (
            "#0203F恐怕当初在建立中转系统时，\x01",
            "只考虑到了\x01",
            "市区内的调查。\x02\x03",

            "#0200F但是，理论上\x01",
            "导力波应该可以到达\x01",
            "市外大概２００赛尔矩的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#0100F２００赛尔矩……\x01",
            "这个距离刚好处于自治州内\x01",
            "有人居住区的边缘范围呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        (
            "#1900F啊，那就是可以进行导力通讯了？\x01",
            "太好了～\x02\x03",

            "各位如果有什么事情的话，\x01",
            "就请与我联络！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#0000F好，知道了。\x01",
            "不必太过担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x104,
        (
            "#0300F我们也只是\x01",
            "去进行调查而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4F42")

    label("loc_4ECF")


    #C0245
    ChrTalk(
        0x9,
        (
            "#1900F太好了，我好不容易\x01",
            "习惯了操作，\x01",
            "如果不能派上用场就可惜了。\x02\x03",

            "各位，如果有什么事，\x01",
            "请一定要跟总部联络哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F42")

    Jump("loc_54B1")

    label("loc_4F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_51D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50B4")

    #C0246
    ChrTalk(
        0x9,
        (
            "#1900F啊，各位，\x01",
            "实在是辛苦了～\x02\x03",

            "你们是不是打算去制止旧城区里\x01",
            "不良分子的斗殴？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#0000F嗯，情况不知为何\x01",
            "就变成那样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x9,
        (
            "#1900F这样子啊……\x02\x03",

            "我家住在东街，\x01",
            "所以偶尔也会看到\x01",
            "旧城区的不良分子……\x02\x03",

            "#1903F在看到他们拉帮结伙\x01",
            "或是斗殴的场面时，\x01",
            "总觉得很恐怖。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0001F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x102,
        (
            "#0101F看样子，无论如何\x01",
            "都必须要去制止他们呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_51D0")

    label("loc_50B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5154")

    #C0251
    ChrTalk(
        0x9,
        (
            "#1900F啊，话说回来，\x01",
            "关于『通缉魔兽』的任务……\x02\x03",

            "麻烦各位将详细报告\x01",
            "通过支援科的终端交给我。\x02\x03",

            "这也是为了测试\x01",
            "导力网络的导入情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D0")

    label("loc_5154")


    #C0252
    ChrTalk(
        0x9,
        (
            "#1900F我家住在东街，\x01",
            "所以偶尔也会看到\x01",
            "旧城区的不良分子……\x02\x03",

            "#1903F在看到他们拉帮结伙\x01",
            "或是斗殴的场面时，\x01",
            "总觉得很恐怖。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D0")

    Jump("loc_54B1")

    label("loc_51D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_54B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_53D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535B")

    #C0253
    ChrTalk(
        0x9,
        (
            "#1909F呵呵，各位，\x01",
            "实在是辛苦了。\x02\x03",

            "#1900F各位对我的\x01",
            "联络工作还满意吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#0000F嗯，完全没有问题哦。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x102,
        "#0100F以后请多多关照哦，芙兰小姐。\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "#1900F嗯，彼此彼此！\x02\x03",

            "#1903F只是……\x01",
            "终端上的对话是会被记录下来的，\x01",
            "所以很难有机会闲聊哦。\x02\x03",

            "#1900F各位，以后有空的时候，\x01",
            "请常来这里和我聊聊吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x104,
        "#0300F哦哦，很乐意。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        "#0000F我们还会再来的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_53D1")

    label("loc_535B")


    #C0259
    ChrTalk(
        0x9,
        (
            "#1903F在终端的对话是会被记录下来的，\x01",
            "所以很难有机会闲聊哦。\x02\x03",

            "#1900F各位，以后有空的时候，\x01",
            "请常来这里和我聊聊吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D1")

    Jump("loc_54B1")

    label("loc_53D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_54B1")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0260
    ChrTalk(
        0x8,
        (
            "这样一来，\x01",
            "【支援请求的补充说明】任务\x01",
            "就完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "请各位先回支援科一趟，\x01",
            "试着利用终端提交一下报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x9,
        (
            "#1900F呵呵，我会负责\x01",
            "处理各位提交的报告的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_54B1")

    label("loc_54B1")

    TalkEnd(0x9)
    Return()

    # Function_9_2E67 end

    def Function_10_54B5(): pass

    label("Function_10_54B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5832")
    EventBegin(0x0)
    Fade(500)
    OP_68(3000, 1500, 14000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x109, 3000, 0, 13500, 0)
    SetChrPos(0x104, 3750, 0, 13000, 0)
    SetChrPos(0x102, 2250, 0, 12250, 0)
    SetChrPos(0x103, 4000, 0, 12000, 0)
    SetChrPos(0x101, 2750, 0, 11500, 0)
    TurnDirection(0x9, 0x109, 0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    #C0263
    ChrTalk(
        0x9,
        (
            "#1905F啊，姐姐！\x02\x03",

            "你和罗伊德警官他们\x01",
            "说过了吧～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x109,
        "#0500F嗯，他们接下委托了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x109, 500)

    #C0265
    ChrTalk(
        0x104,
        (
            "#0305F什么啊，原来早就跟小芙兰\x01",
            "说过了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x104, 500)

    #C0266
    ChrTalk(
        0x109,
        (
            "#0500F哈哈……\x01",
            "在跟大家说之前，\x01",
            "我已经和芙兰谈过一次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x9,
        (
            "#1903F但是幽灵什么的\x01",
            "真的存在吗～\x02\x03",

            "#1900F我有些不敢\x01",
            "相信呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_567A():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_567A)
    Sleep(50)

    def lambda_568A():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_568A)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0268
    ChrTalk(
        0x109,
        (
            "#0503F真是的，我亲眼看到了啊。\x02\x03",

            "#0500F虽然不确定是不是幽灵，\x01",
            "但那种跟妖怪一样的……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x9,
        "#1900F哎，但是但是……\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#0006F……那个，两位，\x01",
            "艾莉可快被你们吓死了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5770():
        TurnDirection(0x9, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5770)

    def lambda_577D():
        TurnDirection(0x109, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_577D)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x109, 1)

    #C0271
    ChrTalk(
        0x109,
        "#0505F啊，对、对不起！\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x9,
        (
            "#1900F呵呵，不好意思……\x01",
            "（艾莉小姐她莫非？）\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        (
            "#0109F没、没事啦。\x01",
            "这种程度根本就没什么……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 3000, 0, 13500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xCE, 4)
    EventEnd(0x5)
    Jump("loc_58E0")

    label("loc_5832")


    #C0274
    ChrTalk(
        0x9,
        (
            "#1900F虽然听姐姐说过了，\x01",
            "但幽灵真的存在吗～？\x02\x03",

            "#1906F啊，接待处这边要是没什么事的话，\x01",
            "我也想和姐姐一起\x01",
            "去看看的。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x102,
        (
            "#0106F（芙兰小姐的胆子大得\x01",
            "  让人无法理解啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58E0")

    Return()

    # Function_10_54B5 end

    def Function_11_58E1(): pass

    label("Function_11_58E1")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x8, 0x0, 0)

    #C0276
    ChrTalk(
        0x9,
        (
            "#1901F啊，各位……\x01",
            "你们听说克洛斯贝尔空港的事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        "#0005F空港……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 6)), scpexpr(EXPR_END)), "loc_5990")

    #C0278
    ChrTalk(
        0x104,
        (
            "#0301F这么一说的话，空港那边\x01",
            "好像是有很多穿便服的搜查官……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5990")


    #C0279
    ChrTalk(
        0x8,
        (
            "因为刚刚搜查一科\x01",
            "动员了警队……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "听说好像是要暂时封锁\x01",
            "克洛斯贝尔空港。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x101,
        "#0011F啊！？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x102,
        "#0101F……发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x9,
        (
            "#1906F这个……\x01",
            "好像因为有保密令，\x01",
            "所以他们都不告诉我。\x02\x03",

            "#1901F这样看来，罗伊德警官你们\x01",
            "也都不知道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x103,
        (
            "#0203F嗯，我们这边一向都\x01",
            "得不到什么重要情报……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#0003F嗯，虽然有些在意……\x02\x03",

            "#0008F（但达德利搜查官之后大概\x01",
            "  会告诉我们的。）\x02\x03",

            "#0001F（现在还是集中精神，\x01",
            "  专心调查失踪者的下落为好。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_58E1 end

    def Function_12_5BC0(): pass

    label("Function_12_5BC0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5BD1")
    Jump("loc_69F3")

    label("loc_5BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5BDF")
    Jump("loc_69F3")

    label("loc_5BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5BED")
    Jump("loc_69F3")

    label("loc_5BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CFB")
    OP_93(0xFE, 0x5A, 0x0)

    #C0286
    ChrTalk(
        0xFE,
        "哎呀哎呀……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0287
    ChrTalk(
        0xFE,
        "喂，你们几个。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "……今天的气色也都不错啊。\x01",
            "偶尔也挺羡慕\x01",
            "你们支援科的。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#0005F多诺邦警督……\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "也没有什么大不了的事啦。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "只是案子被一科的人\x01",
            "抢去了而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5D91")

    label("loc_5CFB")


    #C0292
    ChrTalk(
        0xFE,
        (
            "是一起与鲁巴彻成员有关的伤害事件，\x01",
            "本来以为……只要把它当成\x01",
            "一起单纯的事件进行调查就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "但一科不容分说地就将\x01",
            "调查权夺了过去。\x01",
            "哎呀哎呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D91")

    Jump("loc_69F3")

    label("loc_5D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_603F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F9F")

    #C0294
    ChrTalk(
        0xFE,
        "哟，这不是特别任务支援科嘛。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "听说你们插手了一个麻烦的案子，\x01",
            "然后被鲁巴彻给盯上了，\x01",
            "现在都不敢出门了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "我当时就觉得\x01",
            "你们会搞出点什么事了，\x01",
            "……但还是被你们吓了一跳啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        (
            "#0001F不好意思……\x01",
            "给您添麻烦，让您担心了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_5EC0")

    #C0298
    ChrTalk(
        0x102,
        "#0103F我们真是无言以对……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F0B")

    label("loc_5EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5EEA")

    #C0299
    ChrTalk(
        0x103,
        "#0203F……无言以对呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F0B")

    label("loc_5EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_5F0B")

    #C0300
    ChrTalk(
        0x104,
        "#0303F反驳不了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_5F0B")


    #C0301
    ChrTalk(
        0xFE,
        (
            "唔，算了，反正被吓到的\x01",
            "主要是上层人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "你们好像遭到了\x01",
            "反省一周的处罚吧，\x01",
            "别太沮丧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "……我也觉得你们所做的事情\x01",
            "并没有错。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 2)
    Jump("loc_603A")

    label("loc_5F9F")


    #C0304
    ChrTalk(
        0xFE,
        (
            "在最近这一周的时间，\x01",
            "二科的人也一直在警戒，\x01",
            "但今天早上却突然接到了和解的意向呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "……毕竟也没有发生什么大事件，\x01",
            "估计很快就要恢复到正常的体制了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_603A")

    Jump("loc_69F3")

    label("loc_603F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_604D")
    Jump("loc_69F3")

    label("loc_604D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_605B")
    Jump("loc_69F3")

    label("loc_605B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6069")
    Jump("loc_69F3")

    label("loc_6069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_624C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61DD")

    #C0306
    ChrTalk(
        0xFE,
        "哎呀，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "最近这段时间，意外事故和暴力事件\x01",
            "之类的事情增加了不少呢……\x01",
            "我们二科也没什么时间休息。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 1)), scpexpr(EXPR_END)), "loc_6133")

    #C0308
    ChrTalk(
        0x101,
        (
            "#0008F这样说来……\x01",
            "在市区各处确实都能听到些传闻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_615A")

    label("loc_6133")


    #C0309
    ChrTalk(
        0x101,
        (
            "#0005F这样吗……\x01",
            "有点让人在意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_615A")


    #C0310
    ChrTalk(
        0xFE,
        (
            "呼……这好像并不只是因为\x01",
            "纪念庆典的临近吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "你们多加小心就是了。\x01",
            "市内巡逻方面，\x01",
            "既然经常四处跑，你们就多留意吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6247")

    label("loc_61DD")


    #C0312
    ChrTalk(
        0xFE,
        (
            "最近，暴力事件之类的危险事件\x01",
            "增多了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "昨晚又发生了枪击事件，\x01",
            "我们接下来要去进行相关的查访。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6247")

    Jump("loc_69F3")

    label("loc_624C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_635A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F8")

    #C0314
    ChrTalk(
        0xFE,
        (
            "哎呀，你们好像又接到了\x01",
            "棘手的案子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "要注意不要被卷入\x01",
            "那些大人物的纷争之中哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，谢谢……\x01",
            "（虽然觉得说这话为时已晚。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6355")

    label("loc_62F8")


    #C0317
    ChrTalk(
        0xFE,
        "你们好像又接到了棘手的案子啊。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "大人物间有很多冲突矛盾，\x01",
            "你们注意不要被卷入其中哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6355")

    Jump("loc_69F3")

    label("loc_635A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_64FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_649E")

    #C0319
    ChrTalk(
        0xFE,
        (
            "我们追查了一个月的事件，\x01",
            "最后发现犯人是某议员的亲戚。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "结果上面的态度就变得暧昧不清了。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "案子只要一跟议员沾上边就会不了了之啊。\x01",
            "唉，真是难办啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        (
            "#0200F不能逮捕跟\x01",
            "议员有关系的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "不是，\x01",
            "也不能这么说……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "主要是因为那边会间接给我们施加压力。\x01",
            "案件调查也必须慎重进行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_64F5")

    label("loc_649E")


    #C0325
    ChrTalk(
        0xFE,
        (
            "因为那犯人有位亲戚是议员，\x01",
            "结果上面的态度就变得暧昧不清了。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "唉，真是难办啊。\x02",
    )

    CloseMessageWindow()

    label("loc_64F5")

    Jump("loc_69F3")

    label("loc_64FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6664")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_661E")

    #C0327
    ChrTalk(
        0xFE,
        "哎呀，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "你们今天也在处理那些\x01",
            "无足轻重的支援请求吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，算是……\x01",
            "我们正在处理呢。\x02\x03",

            "#0000F二科这边\x01",
            "最近怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "还行吧。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "虽然负责了几个事件，\x01",
            "但不能太急躁，\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "只能慎重地逐个解决。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#0003F果然……调查\x01",
            "只能够这样进行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_665F")

    label("loc_661E")


    #C0334
    ChrTalk(
        0xFE,
        "二科情况也还行。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "像案件调查这种东西，\x01",
            "就只能逐个进行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665F")

    Jump("loc_69F3")

    label("loc_6664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_673F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66F0")

    #C0336
    ChrTalk(
        0xFE,
        (
            "呼，哎呀哎呀。\x01",
            "做笔录也很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市太大了，再加上\x01",
            "人口也多。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "一天里也调查\x01",
            "不了几个人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_673A")

    label("loc_66F0")


    #C0339
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "终于可以去吃饭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "二科也总是人手不足，\x01",
            "真让人头痛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_673A")

    Jump("loc_69F3")

    label("loc_673F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_69F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6919")

    #C0341
    ChrTalk(
        0xFE,
        "哎呀，这么快就在做事啦。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "……你们在局里\x01",
            "可不怎么被看好哦。\x01",
            "注意不要被某些无聊的人缠上。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        "#0305F咦，有这么悲惨吗？\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "嗯，模仿游击士这种行为\x01",
            "会使一些严肃正经的家伙\x01",
            "自尊心受损。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "你们一直都在自己的部门楼，所以应该不知道。\x01",
            "但其实你们在局里一直都被视为眼中钉哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        "#0003F唔……是吗……\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x103,
        (
            "#0200F幸好我们是\x01",
            "住在自己的部门楼里。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "算了，你们现在不用太在意这些。\x01",
            "先尽快熟悉工作就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "这是争口气给他们看看的\x01",
            "最快方法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4A, 0)
    SetScenarioFlags(0x0, 2)
    Jump("loc_69F3")

    label("loc_6919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6989")

    #C0350
    ChrTalk(
        0xFE,
        "哎呀，这么快就在做事啦。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "你们在局里\x01",
            "可不怎么被看好哦。\x01",
            "注意不要被某些无聊的人缠上。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_69F3")

    label("loc_6989")


    #C0352
    ChrTalk(
        0xFE,
        (
            "你们在局里\x01",
            "可不怎么被看好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "不过，这种事就算在意也没用，\x01",
            "你们注意不要被某些无聊的人缠上就行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69F3")

    TalkEnd(0xFE)
    Return()

    # Function_12_5BC0 end

    def Function_13_69F7(): pass

    label("Function_13_69F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6A08")
    Jump("loc_762E")

    label("loc_6A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6A16")
    Jump("loc_762E")

    label("loc_6A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6A24")
    Jump("loc_762E")

    label("loc_6A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6AE4")

    #C0354
    ChrTalk(
        0xFE,
        (
            "今天早上那起与鲁巴彻有关的伤害事件，\x01",
            "调查权已经被搜查一科给抢去了～\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "还让我们把调查资料\x01",
            "全部都交给他们～\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "可恶～真让人火大啊。\x01",
            "这样下去，\x01",
            "我们的干劲会越来越少的啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_762E")

    label("loc_6AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6E18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DBD")

    #C0357
    ChrTalk(
        0xFE,
        (
            "局长和副局长今天好像\x01",
            "也被叫到市政厅去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "副局长好像很担心自己的官位不保，\x01",
            "最近都没有闲情挖苦人了哦～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_6B95")

    #C0359
    ChrTalk(
        0x102,
        "#0106F这虽然很让人高兴……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BF2")

    label("loc_6B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_6BC9")

    #C0360
    ChrTalk(
        0x103,
        "#0206F这虽然令人感到十分高兴……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BF2")

    label("loc_6BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6BF2")

    #C0361
    ChrTalk(
        0x104,
        "#0306F这虽然让人很高兴……\x02",
    )

    CloseMessageWindow()

    label("loc_6BF2")


    #C0362
    ChrTalk(
        0x101,
        (
            "#0003F但如果现在遇上他的话，\x01",
            "肯定还是会被训斥一番的。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "嗯，要是他一不爽，\x01",
            "说不定还会拿你们开刀哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "那只老狐狸，为了保住自己的饭碗，\x01",
            "估计什么都做得出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_6D0D")

    #C0365
    ChrTalk(
        0x102,
        (
            "#0106F除了鲁巴彻之外，\x01",
            "还必须要小心副局长啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8A")

    label("loc_6D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_6D4A")

    #C0366
    ChrTalk(
        0x103,
        (
            "#0200F除了鲁巴彻，\x01",
            "也要注意警惕副局长呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8A")

    label("loc_6D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6D8A")

    #C0367
    ChrTalk(
        0x104,
        (
            "#0300F除了鲁巴彻之外，\x01",
            "还得小心那个副局长才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D8A")


    #C0368
    ChrTalk(
        0x153,
        (
            "#1111F（老狐狸？\x01",
            "  在说什么啊～……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6E13")

    label("loc_6DBD")


    #C0369
    ChrTalk(
        0xFE,
        (
            "局长和副局长今天好像\x01",
            "也被叫到市政厅去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "你们做了件大事哦～\x01",
            "我都吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E13")

    Jump("loc_762E")

    label("loc_6E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6E26")
    Jump("loc_762E")

    label("loc_6E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6F2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EBB")

    #C0371
    ChrTalk(
        0xFE,
        (
            "一科是有个叫艾玛\x01",
            "的女搜查官吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "她是和我同个时期进来的。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "从以前开始就一直很优秀。\x01",
            "嘁，不讨人喜欢的女人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6F25")

    label("loc_6EBB")


    #C0374
    ChrTalk(
        0xFE,
        (
            "艾玛那家伙从以前开始\x01",
            "就很优秀哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "明明是同时期来的，却一直看不起我。\x01",
            "嘁，真是不讨人喜欢的女人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F25")

    Jump("loc_762E")

    label("loc_6F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6F38")
    Jump("loc_762E")

    label("loc_6F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_700A")

    #C0376
    ChrTalk(
        0xFE,
        (
            "呼，真是的，\x01",
            "这个星期怎么有这么多事件啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "昨晚本来以为得通宵\x01",
            "对现场进行勘察……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "但没想到仓库街那边\x01",
            "发生了枪击事件～\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "希望市民也能稍微\x01",
            "理解下我们的辛苦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_704E")

    label("loc_700A")


    #C0380
    ChrTalk(
        0xFE,
        "熬夜真的是很辛苦哦～\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        "警察这份工作总是得不到相应的回报啊～\x02",
    )

    CloseMessageWindow()

    label("loc_704E")

    Jump("loc_762E")

    label("loc_7053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7109")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7070")
    Call(0, 14)
    Jump("loc_7104")

    label("loc_7070")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_70EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_708E")
    Call(0, 14)
    Jump("loc_70E7")

    label("loc_708E")


    #C0382
    ChrTalk(
        0xB,
        (
            "呼，总之，\x01",
            "找到了那本书真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xB,
        (
            "以后在借书前\x01",
            "要注意先好好确认下内容呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_70E7")

    Jump("loc_7104")

    label("loc_70EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_7101")
    Call(0, 28)
    Jump("loc_7104")

    label("loc_7101")

    Call(0, 14)

    label("loc_7104")

    Jump("loc_762E")

    label("loc_7109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_71BF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7126")
    Call(0, 15)
    Jump("loc_71BA")

    label("loc_7126")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_71A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7144")
    Call(0, 15)
    Jump("loc_719D")

    label("loc_7144")


    #C0384
    ChrTalk(
        0xB,
        (
            "呼，总之，\x01",
            "找到了那本书真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xB,
        (
            "以后在借书前\x01",
            "要注意先好好确认下内容呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_719D")

    Jump("loc_71BA")

    label("loc_71A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_71B7")
    Call(0, 28)
    Jump("loc_71BA")

    label("loc_71B7")

    Call(0, 15)

    label("loc_71BA")

    Jump("loc_762E")

    label("loc_71BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7275")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_71DC")
    Call(0, 16)
    Jump("loc_7270")

    label("loc_71DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_7258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_71FA")
    Call(0, 16)
    Jump("loc_7253")

    label("loc_71FA")


    #C0386
    ChrTalk(
        0xB,
        (
            "呼，总之，\x01",
            "找到了那本书真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xB,
        (
            "以后在借书前\x01",
            "要注意先好好确认下内容呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7253")

    Jump("loc_7270")

    label("loc_7258")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_726D")
    Call(0, 28)
    Jump("loc_7270")

    label("loc_726D")

    Call(0, 16)

    label("loc_7270")

    Jump("loc_762E")

    label("loc_7275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_72F2")

    #C0388
    ChrTalk(
        0xFE,
        (
            "呼，总结笔录也是很辛苦的啊，\x01",
            "我需要咖啡因，咖啡因……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "顺便去看看\x01",
            "瑞贝卡小姐那美丽的身姿，\x01",
            "养养眼吧⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_762E")

    label("loc_72F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_762E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74FD")

    #C0390
    ChrTalk(
        0xFE,
        (
            "我听小芙兰说了哦～\x01",
            "结果你们还是留在了那个新部门啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        "哎呀～你们很有勇气呢。\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "不过，既然你们选择留下来，那就是我的后辈了，\x01",
            "如果有什么不明白的事情，都可以问我哦。\x01",
            "我会适当给你们点指导的。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#0000F哈哈……谢谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    #C0394
    ChrTalk(
        0xFE,
        (
            "那么，小艾莉。\x01",
            "你现在有空吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "我们去吃饭怎样！？\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        "#0100F呵呵，容我拒绝。\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "啊，果然会拒绝？\x01",
            "啊哈哈，守卫坚固啊～\x02",
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

    #C0398
    ChrTalk(
        0x101,
        "#0000F（好轻浮的人呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4A, 1)
    SetScenarioFlags(0x0, 3)
    Jump("loc_762E")

    label("loc_74FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75C4")

    #C0399
    ChrTalk(
        0xFE,
        (
            "结果你们还是留在了那个新部门啊。\x01",
            "哎呀～你们很有勇气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "不过，既然你们选择留下来，\x01",
            "那就是我的后辈了，\x01",
            "如果有什么不明白的事情，都可以问我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        "我会适当给你们点指导的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_762E")

    label("loc_75C4")

    OP_93(0xFE, 0x10E, 0x0)

    #C0402
    ChrTalk(
        0xFE,
        (
            "那个，\x01",
            "我大致打听了一下，\x01",
            "但没有发现目击证人。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "警督，再这样调查下去，\x01",
            "也不会有进展的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_762E")

    TalkEnd(0xFE)
    Return()

    # Function_13_69F7 end

    def Function_14_7632(): pass

    label("Function_14_7632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E4")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xFE, 0xA, 0)

    #C0404
    ChrTalk(
        0xA,
        (
            "先去酒店打听一下，\x01",
            "周边的商店也要转一转。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        "哎～今天也要去调查吗！？\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "真麻烦啊～\x01",
            "欢乐街这么大。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xA,
        (
            "我说你……\x01",
            "给我拿出点干劲来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0xA, 0xFF)
    Jump("loc_7735")

    label("loc_76E4")


    #C0408
    ChrTalk(
        0xFE,
        "哦，你们也正在调查吗？\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "大家都很忙啊，\x01",
            "我连和女孩子约会的时间都没有了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7735")

    Return()

    # Function_14_7632 end

    def Function_15_7736(): pass

    label("Function_15_7736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C1")
    OP_93(0xFE, 0x0, 0x0)

    #C0410
    ChrTalk(
        0xFE,
        (
            "哦哦，这个议员的夫人\x01",
            "可真是个美人啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "呵呵，终于对这次的调查\x01",
            "产生干劲了！\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x101,
        (
            "#0000F（这台词跟\x01",
            "  兰迪的真像……）\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x104,
        (
            "#0305F（嗯……？\x01",
            "  这种话谁都会说的吧。）\x02\x03",

            "#0300F（说这种话只是\x01",
            "  为了打起精神哦。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7844")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_7844")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_786A")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_786A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7890")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_7890")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78B6")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_78B6")

    Sleep(1000)
    SetScenarioFlags(0x0, 3)
    Jump("loc_7919")

    label("loc_78C1")


    #C0414
    ChrTalk(
        0xFE,
        (
            "哦，你们也是来\x01",
            "查找调查资料的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "调查资料真好啊～\x01",
            "偶尔还可以遇到美丽的夫人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7919")

    Return()

    # Function_15_7736 end

    def Function_16_791A(): pass

    label("Function_16_791A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79F6")

    #C0416
    ChrTalk(
        0xFE,
        (
            "我刚才与警备队的\x01",
            "索妮亚副司令擦身而过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "警备队真好啊～\x01",
            "我也想被那样的美人教导哦⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x104,
        (
            "#0306F不不～那个人的训练\x01",
            "真是很严苛的。\x02\x03",

            "比如穿着重装备在野外跑马拉松等等。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "这个就算了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7A47")

    label("loc_79F6")


    #C0420
    ChrTalk(
        0xFE,
        (
            "警备队有位\x01",
            "美人长官，真好啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        (
            "警察局里的高层\x01",
            "都是些男人，\x01",
            "看都看烦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A47")

    Return()

    # Function_16_791A end

    def Function_17_7A48(): pass

    label("Function_17_7A48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BDB")

    #C0422
    ChrTalk(
        0xFE,
        (
            "啊，是你们啊，\x01",
            "一大早就开始工作了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#0003F嗯，因为今天\x01",
            "好像会很忙。\x02\x03",

            "#0000F弗兰茨好像\x01",
            "从早上就在开会吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "接下来要决定公共安全科所有成员\x01",
            "的巡逻路线。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "当上警察已经一个月了……\x01",
            "前辈们都认为我该多干点活了，\x01",
            "正跃跃欲试地计划增加我的工作量呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，这样啊。\x01",
            "看来你那边也很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        "嗯，一起加油吧。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "罗伊德，你们也很不容易吧……\x01",
            "因为我们还是新人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 4)
    Jump("loc_7C48")

    label("loc_7BDB")


    #C0429
    ChrTalk(
        0xFE,
        (
            "我们公共安全科\x01",
            "主要负责市区内的巡逻任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "当上警察已经一个月了……\x01",
            "现在才有点\x01",
            "正式开始工作的感觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C48")

    TalkEnd(0xFE)
    Return()

    # Function_17_7A48 end

    def Function_18_7C4C(): pass

    label("Function_18_7C4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7D3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CED")

    #C0431
    ChrTalk(
        0xFE,
        (
            "科长级的人物们现在\x01",
            "都聚集在局长室内，\x01",
            "好像正在开一个很重要的会议。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "说鲁巴彻什么什么的，\x01",
            "很是慌张……到底发生了什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7D36")

    label("loc_7CED")


    #C0433
    ChrTalk(
        0xFE,
        "昨天和今天连续发生了好几起事件。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xFE,
        (
            "接下来还会\x01",
            "发生什么事件呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D36")

    Jump("loc_84AB")

    label("loc_7D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7E07")

    #C0435
    ChrTalk(
        0xFE,
        (
            "今天一大早就设立了\x01",
            "联合搜查部门。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        (
            "继昨天之后，今天又有大事件发生……\x01",
            "正是在这种时候，\x01",
            "才需要我们展现出警察的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "绝对不能输给那些卑劣无耻的恐怖分子！\x01",
            "一定要防止事件的发生！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84AB")

    label("loc_7E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9A")

    #C0438
    ChrTalk(
        0xFE,
        "竟然发动袭击事件，真是够大胆的！\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "……幸运的是，市民中\x01",
            "并没有出现伤亡人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "现在只要尽快\x01",
            "将犯人逮捕就好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7F0B")

    label("loc_7E9A")


    #C0441
    ChrTalk(
        0xFE,
        (
            "犯人大概就是鲁巴彻的成员了，\x01",
            "必须找到足够的证据，\x01",
            "然后将其逮捕。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "我们公共安全科也\x01",
            "已经开始进行查访了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F0B")

    Jump("loc_84AB")

    label("loc_7F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7FA6")

    #C0443
    ChrTalk(
        0xFE,
        (
            "在黑手党最近引起的\x01",
            "骚乱之中，把市民\x01",
            "卷入其中的案例似乎在明显增多。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "搜查一科的人都绷紧着神经，\x01",
            "我们公共安全科\x01",
            "也必须做点什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84AB")

    label("loc_7FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7FB4")
    Jump("loc_84AB")

    label("loc_7FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8056")

    #C0445
    ChrTalk(
        0xFE,
        (
            "你们听说了吗？\x01",
            "欢乐街那边好像\x01",
            "又发生了一起事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "那是公共安全科的巡警发现的，\x01",
            "搜查二科已经出动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "现在他们应该在\x01",
            "市内各处进行查访。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84AB")

    label("loc_8056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_80A5")

    #C0448
    ChrTalk(
        0xFE,
        "好，今天也要认真巡逻。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "嗯，上午的巡逻\x01",
            "果然比较有干劲！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84AB")

    label("loc_80A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_81D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8165")

    #C0450
    ChrTalk(
        0xFE,
        (
            "自治州的创立纪念庆典时，\x01",
            "各个国家的ＶＩＰ都会来访。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "开幕式的警备任务\x01",
            "由一科和二科负责，\x01",
            "我们则必须加强市区内的巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        "呼，今年的纪念庆典工作量很大哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_81CD")

    label("loc_8165")


    #C0453
    ChrTalk(
        0xFE,
        (
            "特别是创立纪念庆典的开幕式时，\x01",
            "各个国家的ＶＩＰ都会出席……\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "必须快点决定好\x01",
            "市区内的巡逻路线。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81CD")

    Jump("loc_84AB")

    label("loc_81D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_82BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8290")

    #C0455
    ChrTalk(
        0xFE,
        (
            "创立纪念庆典\x01",
            "将会举行很多活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xFE,
        (
            "我们警察要执行警备任务，\x01",
            "还要对市民进行引导，工作量非常大。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "这是一年一次的大工作，\x01",
            "我们必须都打起十二分精神来才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_82B7")

    label("loc_8290")


    #C0458
    ChrTalk(
        0xFE,
        (
            "下个月\x01",
            "我们公共安全科将会很忙哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82B7")

    Jump("loc_84AB")

    label("loc_82BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_83E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8375")

    #C0459
    ChrTalk(
        0xFE,
        (
            "今年我们科也来了\x01",
            "几名新人。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        (
            "大家都很努力哦。\x01",
            "像我们这种普通的部门里面\x01",
            "也有各种各样的复杂情况……\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        (
            "希望他们不要被挫折打败，\x01",
            "努力学习，不断进步。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_83DB")

    label("loc_8375")


    #C0462
    ChrTalk(
        0xFE,
        (
            "像我们这种普通的部门里面\x01",
            "也有很多艰辛的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        (
            "希望新人们不要被挫折打败，\x01",
            "努力学习，不断进步。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83DB")

    Jump("loc_84AB")

    label("loc_83E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_83F1")
    Call(0, 19)
    Jump("loc_84AB")

    label("loc_83F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8456")

    #C0464
    ChrTalk(
        0xFE,
        (
            "今天的会议场所\x01",
            "突然改变了。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "大家应该都去\x01",
            "二楼的会议室了吧。\x01",
            "都集合不到一起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84AB")

    label("loc_8456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_84AB")

    #C0466
    ChrTalk(
        0xFE,
        (
            "我向凯特前辈\x01",
            "请教了巡逻的方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "前辈的指导简单易懂，\x01",
            "十分有用哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84AB")

    TalkEnd(0xFE)
    Return()

    # Function_18_7C4C end

    def Function_19_84AF(): pass

    label("Function_19_84AF")

    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xD, 0xF, 0)
    TurnDirection(0xF, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85B3")

    #C0468
    ChrTalk(
        0xD,
        (
            "新人们负责的地区\x01",
            "已经顺利决定好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xD,
        (
            "凯特巡警，你怎么办？\x01",
            "你是老手了，\x01",
            "要不就去人手少的地区帮忙吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xF,
        (
            "前辈，别说\x01",
            "我是老手啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0xF,
        (
            "听起来就好像\x01",
            "我有多老一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0472
    ChrTalk(
        0xD,
        "真是抱歉……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8676")

    label("loc_85B3")


    #C0473
    ChrTalk(
        0xD,
        (
            "那么，凯特巡警，\x01",
            "这样的分配怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xF,
        (
            "嗯……\x01",
            "最近导力车比较多，\x01",
            "所以中央广场那边还是我去比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xF,
        "因为毕竟我的经验丰富点！\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0476
    ChrTalk(
        0xD,
        (
            "这、这样啊。\x01",
            "那就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8676")

    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_93(0xD, 0xB4, 0x0)
    OP_93(0xF, 0x0, 0x0)
    Return()

    # Function_19_84AF end

    def Function_20_868D(): pass

    label("Function_20_868D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_869E")
    Jump("loc_8CB4")

    label("loc_869E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8777")

    #C0477
    ChrTalk(
        0xFE,
        "啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xFE,
        (
            "这个事件很严重，\x01",
            "所以不能让市民知道。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xFE,
        "你们千万要切记。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8742")

    #C0480
    ChrTalk(
        0x101,
        (
            "#0000F好、好的……\x01",
            "（说的是什么事呢？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_876F")

    label("loc_8742")


    #C0481
    ChrTalk(
        0x101,
        (
            "#0000F好、好的……\x01",
            "（果然很重要啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_876F")

    SetScenarioFlags(0x0, 6)
    Jump("loc_8804")

    label("loc_8777")

    OP_4B(0xD, 0xFF)
    OP_93(0xFE, 0x10E, 0x0)
    TurnDirection(0xD, 0xFE, 0)

    #C0482
    ChrTalk(
        0xFE,
        (
            "啊，总而言之，\x01",
            "你们就去进行案情查访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        (
            "车站和空港\x01",
            "有一科和二科来负责，\x01",
            "市区内就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xD,
        "是，了解！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_8804")

    Jump("loc_8CB4")

    label("loc_8809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8817")
    Jump("loc_8CB4")

    label("loc_8817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8825")
    Jump("loc_8CB4")

    label("loc_8825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8833")
    Jump("loc_8CB4")

    label("loc_8833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8841")
    Jump("loc_8CB4")

    label("loc_8841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8AC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8985")

    #C0485
    ChrTalk(
        0xFE,
        (
            "哦，你们\x01",
            "好像是赛尔盖那边的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "嗯，到现在还要\x01",
            "成立新部门……\x01",
            "赛尔盖也很努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xFE,
        "我对他实在非常佩服。\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x101,
        (
            "#0000F您好像认识\x01",
            "赛尔盖科长呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xFE,
        (
            "嗯，算认识吧，\x01",
            "因为他以前做事\x01",
            "非常高调。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "……你们尽量别给赛尔盖\x01",
            "添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xFE,
        (
            "他跟我这种快要退休\x01",
            "的大叔不同，\x01",
            "还是警察局的栋梁呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 7)
    Jump("loc_8AC4")

    label("loc_8985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A71")

    #C0492
    ChrTalk(
        0xFE,
        (
            "对了……\x01",
            "你们是红茶党吗？\x01",
            "还是咖啡党呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xFE,
        "我是十足的咖啡党哦。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "嗯，办公桌上要是\x01",
            "有咖啡豆研磨机就好了……\x02",
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
    SetScenarioFlags(0x0, 6)
    Jump("loc_8AC4")

    label("loc_8A71")


    #C0495
    ChrTalk(
        0xFE,
        "我看看……罐装咖啡，出来了……\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xFE,
        (
            "……还想再和赛尔盖一起\x01",
            "悠闲地喝喝咖啡呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AC4")

    Jump("loc_8CB4")

    label("loc_8AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8B8F")
    OP_93(0xFE, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B67")

    #C0497
    ChrTalk(
        0xFE,
        (
            "嗯，虽然每年都要做，\x01",
            "但分配任务实在是麻烦啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        "这样吗？还是这样好呢……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        (
            "啊啊，要是有人能来\x01",
            "帮我决定就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8B8A")

    label("loc_8B67")


    #C0500
    ChrTalk(
        0xFE,
        (
            "嗯，还是采取\x01",
            "这种分配方案吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B8A")

    Jump("loc_8CB4")

    label("loc_8B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8B9D")
    Jump("loc_8CB4")

    label("loc_8B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8BAB")
    Jump("loc_8CB4")

    label("loc_8BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8BB9")
    Jump("loc_8CB4")

    label("loc_8BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8CB4")
    OP_93(0xFE, 0x10E, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C37")

    #C0501
    ChrTalk(
        0xFE,
        (
            "嗯……那么\x01",
            "就快点开始执行吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        "一、二、三……\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        (
            "嗯，怎么回事。\x01",
            "人都没来齐啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8CB4")

    label("loc_8C37")

    TurnDirection(0xFE, 0xF, 0)

    #C0504
    ChrTalk(
        0xFE,
        (
            "凯特巡警，\x01",
            "帮我把其他人都叫过来吧，\x01",
            "不然没办法开始。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0xFE, 0)

    #C0505
    ChrTalk(
        0xF,
        (
            "好的，科长。\x01",
            "请稍等一下！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x10E, 0x0)
    OP_93(0xF, 0x10E, 0x0)
    OP_4C(0xF, 0xFF)

    label("loc_8CB4")

    TalkEnd(0xFE)
    Return()

    # Function_20_868D end

    def Function_21_8CB8(): pass

    label("Function_21_8CB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8ED8")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0506
    ChrTalk(
        0xFE,
        (
            "啊……是罗伊德吗？\x01",
            "好久不见啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#0000F凯特前辈……\x01",
            "久疏问候了。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x104,
        "#0300F怎么，罗伊德，这是你熟人吗？\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        (
            "#0000F嗯，这位是在警察学校里，\x01",
            "时常会在上课时来给我们进行指导的前辈。\x02\x03",

            "从坐姿到射击，\x01",
            "前辈教了我很多东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xFE,
        (
            "呵呵，罗伊德\x01",
            "很优秀，\x01",
            "所以值得一教呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        (
            "……听说，你好像被分配到了\x01",
            "一个比较艰难的部门啊。\x01",
            "……那个，要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xFE,
        (
            "努力的人一定会有回报！\x01",
            "无论何时都不能放弃希望！\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#0006F嗯，知道了。\x01",
            "（让前辈为我担心了呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x102,
        (
            "#0108F（看来支援科\x01",
            "  确实不被看好啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 7)
    Jump("loc_90B7")

    label("loc_8ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8EE9")
    Call(0, 19)
    Jump("loc_90B7")

    label("loc_8EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8F78")

    #C0515
    ChrTalk(
        0xFE,
        "那个……轮值表的打印版，还有……\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xFE,
        (
            "本来是想使用\x01",
            "楼上的会议室的，\x01",
            "不过那里被搜查一科的人抢占了。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xFE,
        (
            "那群人\x01",
            "总是这样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90B7")

    label("loc_8F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8FE8")

    #C0518
    ChrTalk(
        0xFE,
        (
            "呼，还好顺利把\x01",
            "今年的新人们都派出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "得赶紧把报告书大致总结一下，\x01",
            "然后去跟科长汇报。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90B7")

    label("loc_8FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_90B7")

    #C0520
    ChrTalk(
        0xFE,
        (
            "那么，去给新人们\x01",
            "好好上一课吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xFE,
        (
            "对了，我们部门叫做\x01",
            "『公共安全科』哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "主要负责市区内的巡逻工作。\x01",
            "如果在市内碰见我了，\x01",
            "还请多多指教哦！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90B7")

    #C0523
    ChrTalk(
        0x101,
        (
            "#0000F嗯，\x01",
            "也请前辈多多指教。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_90B7")

    TalkEnd(0xFE)
    Return()

    # Function_21_8CB8 end

    def Function_22_90BB(): pass

    label("Function_22_90BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9186")

    #C0524
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        "真是的……\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        (
            "自那之后就一直在开会。\x01",
            "呼，肩膀又酸又痛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        (
            "#0006F（呜……是搜查一科的人吗……）\x02\x03",

            "（虽然就算被他们抱怨\x01",
            "  也是理所当然的……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_91B3")

    label("loc_9186")


    #C0528
    ChrTalk(
        0xFE,
        (
            "那之后就一直在开会。\x01",
            "呼，真是累死人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91B3")

    TalkEnd(0xFE)
    Return()

    # Function_22_90BB end

    def Function_23_91B7(): pass

    label("Function_23_91B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_926E")

    #C0529
    ChrTalk(
        0x101,
        "#0005F咦，科长居然在总部……\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x104,
        (
            "#0300F很少见啊，\x01",
            "是被副局长叫过来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xFE,
        (
            "#1006F因为今天总部要开会啊，\x01",
            "别说那种惹人厌的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x104,
        "#0300F哈哈，不好意思。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_92E6")

    label("loc_926E")


    #C0533
    ChrTalk(
        0xFE,
        (
            "#1006F纪念庆典也快到了，\x01",
            "所以有很多会议要开。\x02\x03",

            "#1000F你们做好自己的工作就行。\x01",
            "要汇报的话，等忙完这段后我再一起听。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92E6")

    TalkEnd(0xFE)
    Return()

    # Function_23_91B7 end

    def Function_24_92EA(): pass

    label("Function_24_92EA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_937E")
    Jump("loc_93C8")

    label("loc_937E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_939E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93C8")

    label("loc_939E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93BE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93C8")

    label("loc_93BE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93C8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0534
    ChrTalk(
        0xFE,
        (
            "没想到竟然会以空港为目标……\x01",
            "敌人是恐怖分子吗！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_92EA end

    def Function_25_942C(): pass

    label("Function_25_942C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94C0")
    Jump("loc_950A")

    label("loc_94C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_94E0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_950A")

    label("loc_94E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9500")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_950A")

    label("loc_9500")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_950A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0535
    ChrTalk(
        0xFE,
        (
            "我在休息的时候\x01",
            "被叫了过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xFE,
        (
            "竟、竟然发生了\x01",
            "这么严重的事件……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_942C end

    def Function_26_957F(): pass

    label("Function_26_957F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9613")
    Jump("loc_965D")

    label("loc_9613")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9633")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_965D")

    label("loc_9633")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9653")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_965D")

    label("loc_9653")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_965D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0537
    ChrTalk(
        0xFE,
        (
            "又发生事件了吗……\x01",
            "今年的事件可真多啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_957F end

    def Function_27_96B7(): pass

    label("Function_27_96B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_976A")

    #C0538
    ChrTalk(
        0xFE,
        "嗯，到底在哪里呢……\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xFE,
        (
            "难道在那里……？\x01",
            "不会不会，应该不可能……\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#0005F（啊，副局长……？）\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x102,
        (
            "#0100F（聚精会神的，\x01",
            "  在做什么呢？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_97A4")

    label("loc_976A")


    #C0542
    ChrTalk(
        0xFE,
        "（转来转去，转来转去）……\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xFE,
        "唔，到底在哪里呢……\x02",
    )

    CloseMessageWindow()

    label("loc_97A4")

    Jump("loc_9870")

    label("loc_97A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_986D")

    #C0544
    ChrTalk(
        0x12,
        (
            "我在找一枚镶有\x01",
            "红耀石的结婚戒指。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x12,
        (
            "哼，你们找到了就马上跟我说，\x01",
            "──明白了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        (
            "#0003F（利用蔡特发达的嗅觉，\x01",
            "  说不定能找得出来……）\x02\x03",

            "#0000F（跟蔡特商量看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9870")

    label("loc_986D")

    Call(0, 29)

    label("loc_9870")

    TalkEnd(0xFE)
    Return()

    # Function_27_96B7 end

    def Function_28_9874(): pass

    label("Function_28_9874")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_990A")
    OP_4B(0xA, 0xFF)
    OP_68(-13360, 1500, 10430, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21320, 0)
    SetChrPos(0x101, -11800, 0, 11000, 0)
    SetChrPos(0x102, -12800, 0, 10750, 0)
    SetChrPos(0x103, -11800, 0, 9500, 0)
    SetChrPos(0x104, -12800, 0, 9250, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)
    Jump("loc_9A16")

    label("loc_990A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9999")
    OP_4B(0xA, 0xFF)
    OP_68(-125470, 1200, 18490, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24860, 0)
    SetChrPos(0x101, -125400, 0, 18000, 0)
    SetChrPos(0x102, -126400, 0, 17750, 45)
    SetChrPos(0x103, -124000, 0, 18390, 315)
    SetChrPos(0x104, -123620, 0, 19500, 270)
    OP_93(0xB, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)
    Jump("loc_9A16")

    label("loc_9999")

    OP_68(-11160, 1100, 12770, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20160, 0)
    SetChrPos(0x101, -10500, 0, 12500, 0)
    SetChrPos(0x102, -11500, 0, 12250, 0)
    SetChrPos(0x103, -10500, 0, 11000, 0)
    SetChrPos(0x104, -11500, 0, 10750, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)

    label("loc_9A16")

    OP_0D()

    #C0547
    ChrTalk(
        0x101,
        "#11P#0000F雷蒙德警官，您好。\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xB,
        (
            "#5P哦，是特别任务支援科的啊……\x01",
            "今天来总部有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x104,
        (
            "#12P#0304F哼哼哼……\x01",
            "都到这时候了还装傻，\x01",
            "很有胆量嘛。\x02\x03",

            "#0307F#4S犯人就是……你！！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 500)

    #C0550
    ChrTalk(
        0xB,
        "#5P咦……咦咦咦咦！！？？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(500)

    def lambda_9B44():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B44)

    def lambda_9B51():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B51)

    def lambda_9B5E():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9B5E)
    Sleep(500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0551
    ChrTalk(
        0x101,
        (
            "#5P#0006F兰迪……\x01",
            "不要开这种玩笑啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x103,
        "#11P#0203F……你也太无聊了吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0553
    ChrTalk(
        0x104,
        (
            "#12P#0306F嘁，身为警察，\x01",
            "总想试着说一次这种台词嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0554
    ChrTalk(
        0xB,
        (
            "#5P那、那个……\x01",
            "到底怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9C33():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C33)

    def lambda_9C40():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9C40)

    def lambda_9C4D():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C4D)

    def lambda_9C5A():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9C5A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0555
    ChrTalk(
        0x102,
        (
            "#12P#0103F咳咳……\x01",
            "其实我们是接到了\x01",
            "图书馆的支援请求。\x02\x03",

            "#0100F雷蒙德警官，\x01",
            "您是不是在图书馆借了书，\x01",
            "然后就忘记还了呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0556
    ChrTalk(
        0xB,
        (
            "#5P啊，对对！\x01",
            "这么一说好像是呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xB,
        "#5P……嗯，确实借了本书还没还。\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xB,
        "#5P借了借了……哈哈。\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        "#11P#0000F……………………\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xB,
        "#5P……………………\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x101,
        (
            "#11P#0006F……那、那个。\x02\x03",

            "#0012F难道……\x01",
            "您把书丢了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xB,
        (
            "#5P那、那个……\x01",
            "我想应该、没有、吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x103,
        "#11P#0211F为什么是疑问语气……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9E83")
    TurnDirection(0xA, 0xB, 500)

    #C0564
    ChrTalk(
        0xA,
        (
            "#11P……雷蒙德。\x01",
            "快点找找看。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0565
    ChrTalk(
        0xB,
        "#5P好、好的！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EBF")

    label("loc_9E83")


    #C0566
    ChrTalk(
        0xB,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xB,
        "#5P……我、我去找找看哦！\x02",
    )

    CloseMessageWindow()

    label("loc_9EBF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    #C0568
    ChrTalk(
        0xB,
        (
            "#5P……有了……找到了哦！\x01",
            "就是这本！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0569
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D7, 1)

    #C0570
    ChrTalk(
        0x101,
        (
            "#11P#0003F呼……\x01",
            "总之，能找到实在太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x104,
        "#12P#0306F冷汗都快被吓出来了。\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x102,
        (
            "#12P#0105F不过，为什么要借这本书呢……？\x02\x03",

            "这本书描写的，好像是历史上几位\x01",
            "留下显赫功绩的女性的轶事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xB,
        (
            "#5P嗯，我一开始还以为是\x01",
            "全大陆美女们的写真集之类的～\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xB,
        (
            "#5P后来发现不是，\x01",
            "就一直放在抽屉里。\x01",
            "渐渐就把它给忘了。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x103,
        (
            "#11P#0206F……我可不觉得\x01",
            "图书馆里会有那种书。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        (
            "#11P#0012F算、算了……\x01",
            "反正也把书收回来了，\x01",
            "结果还算不错吧。\x02\x03",

            "#0000F雷蒙德警官，\x01",
            "谢谢您的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xB,
        "#5P没事没事，不用客气。\x02",
    )

    CloseMessageWindow()
    OP_29(0x5, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A16A")
    OP_29(0x5, 0x1, 0x1F)

    label("loc_A16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A18D")
    SetChrPos(0x0, -12300, 0, 11000, 0)
    OP_4C(0xA, 0xFF)
    Jump("loc_A1C1")

    label("loc_A18D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A1B0")
    SetChrPos(0x0, -125400, 0, 18000, 0)
    OP_4C(0xA, 0xFF)
    Jump("loc_A1C1")

    label("loc_A1B0")

    SetChrPos(0x0, -11000, 0, 12500, 0)

    label("loc_A1C1")

    EventEnd(0x5)
    Return()

    # Function_28_9874 end

    def Function_29_A1C4(): pass

    label("Function_29_A1C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-57380, 1500, 17520, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -56800, 0, 17500, 0)
    SetChrPos(0x102, -57800, 0, 17250, 0)
    SetChrPos(0x103, -56800, 0, 16000, 0)
    SetChrPos(0x104, -57800, 0, 15750, 0)
    SetChrPos(0x12, -57300, 0, 19000, 0)
    SetChrSubChip(0x12, 0x0)
    OP_0D()

    #C0578
    ChrTalk(
        0x12,
        "#5P没有、没有、没有……！\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x12,
        "#5P唔，到底在哪里啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x12, 0xB4, 0x2EE)
    Sleep(750)

    #C0580
    ChrTalk(
        0x12,
        "#5P唔，是特别任务支援科的人啊……\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x12,
        (
            "#5P哼，快给我出去，\x01",
            "我现在很忙！\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x101,
        (
            "#11P#0005F是……那我们这就告辞了。\x01",
            "（奇怪，这种味道……是酒吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x104,
        (
            "#12P#0306F他看起来好像很\x01",
            "烦躁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        (
            "#0203F我可没兴趣\x01",
            "主动找骂，\x01",
            "我们快点离开吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-59280, 1700, 16460, 2000)
    MoveCamera(77, 25, 0, 2000)

    def lambda_A3B9():
        OP_97(0x104, 0xFFFFF736, 0x0, 0xFFFFF736, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A3B9)
    Sleep(50)

    def lambda_A3D6():
        OP_97(0x103, 0xFFFFF830, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A3D6)
    Sleep(50)

    def lambda_A3F3():
        OP_97(0x102, 0xFFFFF92A, 0x0, 0xFFFFF92A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3F3)
    Sleep(50)

    def lambda_A410():
        OP_97(0x101, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A410)
    Sleep(200)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x12, 0xE1, 0x2EE)

    #C0585
    ChrTalk(
        0x12,
        "#5P给、给我等一下。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    def lambda_A4D8():
        TurnDirection(0x101, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A4D8)

    def lambda_A4E5():
        TurnDirection(0x102, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A4E5)

    def lambda_A4F2():
        TurnDirection(0x103, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A4F2)

    def lambda_A4FF():
        TurnDirection(0x104, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4FF)
    Sleep(500)

    #C0586
    ChrTalk(
        0x12,
        (
            "#5P你们有没有\x01",
            "看到一枚『戒指』？\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x12,
        (
            "#5P是一枚镶有红耀石的\x01",
            "结婚戒指！\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x101,
        (
            "#12P#0005F结婚戒指吗？\x01",
            "（让人有点意外啊……）\x02\x03",

            "#0000F……那个，艾莉你看到过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        (
            "#12P#0103F没有，\x01",
            "我没有什么印象。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x104,
        "#12P#0300F我也没看见过。\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x103,
        (
            "#11P#0200F我也一样。\x01",
            "……您遗失了\x01",
            "结婚戒指是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x12,
        "#5P唔……\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x12, 1, 0, 30)
    Sleep(500)

    #C0593
    ChrTalk(
        0x12,
        (
            "#5P啊、啊啊啊……\x01",
            "如果这件事被老婆发现了的话……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x12, 0x1)
    OP_64(0x12)
    OP_95(0x12, -57300, 0, 19000, 2000, 0x0)
    OP_A6(0x12, 0x0, 0x32, 0x190, 0xBB8)

    #C0594
    ChrTalk(
        0x12,
        "#5P啊啊啊……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x12, 1, 0, 30)
    Sleep(500)

    #C0595
    ChrTalk(
        0x101,
        (
            "#12P#0003F（副局长……好像很怕老婆啊。）\x02\x03",

            "#0000F那个，您能把具体情况\x01",
            "告诉我们吗？\x01",
            "说不定会有些线索……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x12, 0x1)
    OP_64(0x12)
    OP_95(0x12, -57300, 0, 19000, 2000, 0x0)
    OP_93(0x12, 0xE1, 0x2EE)

    #C0596
    ChrTalk(
        0x12,
        "#5P唔唔，真、真的吗？\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x12,
        (
            "#5P……咳咳，\x01",
            "其实也没什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x12,
        (
            "#5P就是我昨晚把\x01",
            "结婚戒指给丢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x12,
        "#5P……而且怎么找都找不到！\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x12,
        (
            "#5P看来，估计是\x01",
            "丢在欢乐街了……\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        "#12P#0105F……欢乐街………？\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x12,
        (
            "#5P别摆出那种表情，\x01",
            "我只是去喝个酒放松一下而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x12,
        (
            "#5P然后到『巴鲁卡』玩了几把，\x01",
            "之后就回家了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0604
    ChrTalk(
        0x12,
        (
            "#5P……对了，我记得戒指在那个时候\x01",
            "都还戴在手上呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x12,
        (
            "#5P#5P虽然当时有点醉了，但在走出那家叫『巴鲁卡』的\x01",
            "店之前的事情我都还记得。\x01",
            "绝对没错！！\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x103,
        "#11P#0200F那之后的呢？\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x12,
        "#5P哼，完全不记得了！\x02",
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

    #C0608
    ChrTalk(
        0x104,
        (
            "#12P#0306F（看来当时醉得很厉害啊，\x01",
            "  到现在都还有酒臭味。）\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        (
            "#12P#0101F（戒指的体积很小，\x01",
            "  要是掉到街上……\x01",
            "  几乎不可能找得回来呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        (
            "#12P#0006F（嗯，只能说是喝得\x01",
            "  烂醉如泥的副局长自己的责任了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0611
    ChrTalk(
        0x101,
        (
            "#12P#0000F副局长，不好意思……\x01",
            "请问您带着\x01",
            "手帕之类的东西吗？\x02\x03",

            "为了找回戒指，\x01",
            "能不能先借我们一用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x12,
        (
            "#5P嗯……？\x01",
            "你有什么主意了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, -57800, 0, 18000, 2000, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0613
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33D, 1)
    OP_98(0x101, 0xFFFFFF06, 0x0, 0xFFFFFC18, 0x7D0, 0x0)

    #C0614
    ChrTalk(
        0x101,
        "#12P#0000F谢谢。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x103,
        (
            "#11P#0205F（罗伊德前辈，\x01",
            "  你打算怎么做呢？\x01",
            "  借来那种东西……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0616
    ChrTalk(
        0x101,
        (
            "#5P#0000F（没什么……就是想靠蔡特的鼻子\x01",
            "  找找看。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0617
    ChrTalk(
        0x101,
        (
            "#5P#0000F（副局长好像也很苦恼，\x01",
            "  等下去找蔡特\x01",
            "  商量看看吧？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0618
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【遗失的结婚戒指】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x15, 0x4, 0x2)
    SetChrPos(0x0, -58800, 30, 15500, 45)
    EventEnd(0x5)
    Return()

    # Function_29_A1C4 end

    def Function_30_AD69(): pass

    label("Function_30_AD69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ADBB")
    OP_95(0x12, -57800, 0, 19000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0x5A, 0x1F4)
    Sleep(500)
    OP_95(0x12, -56800, 0, 19000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0x10E, 0x1F4)
    Sleep(500)
    Jump("Function_30_AD69")

    label("loc_ADBB")

    Return()

    # Function_30_AD69 end

    def Function_31_ADBC(): pass

    label("Function_31_ADBC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-12810, 1500, 17000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -12810, 0, 17000, 180)
    SetChrPos(0x1, -12810, 0, 17000, 180)
    SetChrPos(0x2, -12810, 0, 17000, 180)
    SetChrPos(0x3, -12810, 0, 17000, 180)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_31_ADBC end

    def Function_32_AE47(): pass

    label("Function_32_AE47")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(2330, 1510, 13680, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 3000, 0, 13500, 0)
    SetChrPos(0x109, 3750, 0, 13000, 0)
    SetChrPos(0x102, 2250, 0, 12500, 0)
    SetChrPos(0x103, 3500, 0, 12000, 0)
    SetChrPos(0x104, 2250, 0, 11500, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0619
    ChrTalk(
        0x9,
        (
            "#5P#1905F啊，是各位啊。\x01",
            "姐姐你也来了呢！\x02\x03",

            "#1900F关于那个遗迹的调查，\x01",
            "有什么进展了吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x109,
        (
            "#11P#0500F那个……\x01",
            "我们并不是为那个\x01",
            "而来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x101,
        "#12P#0000F芙兰，我们这次来是找你的。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0622
    ChrTalk(
        0x9,
        (
            "#5P#1905F找我……？\x01",
            "找我做什么呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        (
            "#12P#0003F说来话长……\x02\x03",

            "#0000F有位来自外国的男性说，\x01",
            "在之前的纪念庆典时得到了一位女性的帮助，\x01",
            "而那位女性好像就是芙兰你。\x02\x03",

            "你还记得在纪念庆典的\x01",
            "最后一天，帮助了\x01",
            "一位丢失钱包的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x9,
        (
            "#5P#1903F钱包……吗？\x01",
            "我想想～………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0625
    ChrTalk(
        0x9,
        (
            "#5P#1900F啊，记得记得！\x02\x03",

            "那好像是一位\x01",
            "从利贝尔来的游客吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x102,
        (
            "#6P#0100F果然是\x01",
            "芙兰小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x9,
        (
            "#5P#1900F那一天可真够累人的呢～\x02\x03",

            "#1904F我在下班回家的路上，\x01",
            "看到路边有一位先生急得快要哭出来了，\x01",
            "就不忍心放着他不管呢。\x02\x03",

            "#1900F为了帮那位先生找回钱包，\x01",
            "我跑遍了整个克洛斯贝尔，\x01",
            "找到钱包时天都黑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x104,
        (
            "#0309F真不愧是小芙兰啊。\x01",
            "对一个陌生的男人，\x01",
            "也能这么热心。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x9,
        (
            "#5P#1909F嘻嘻嘻，\x01",
            "因为我也是警察啊。\x02\x03",

            "#1903F当时以为会有路人拾到交给警察，\x01",
            "所以来确认了好几次……\x02\x03",

            "#1900F结果，最后在\x01",
            "他旅馆房间的床底下找到了，\x01",
            "总算松了口气。\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0630
    ChrTalk(
        0x103,
        "#12P#0203F还真是会给人添麻烦啊……\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x9,
        (
            "#5P#1900F话说，那个……\x01",
            "那位先生怎么了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x109,
        (
            "#11P#0503F……其实那位先生\x01",
            "叫做安敦……\x02\x03",

            "#0500F纪念庆典虽然结束了，\x01",
            "但他还留在克洛斯贝尔。\x02\x03",

            "他说无论如何也想\x01",
            "向芙兰你表示谢意，\x01",
            "所以一直在找你。\x02\x03",

            "结果便委托了\x01",
            "罗伊德警官他们\x01",
            "帮忙寻找。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x9,
        (
            "#5P#1900F咦，这样啊？\x01",
            "总觉得有点不好意思呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么……\x01",
            "芙兰你觉得如何？\x02\x03",

            "#0003F要是你不想见他的话，\x01",
            "可以拒绝的……\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x9,
        (
            "#5P#1900F……那个，见个面\x01",
            "当然没问题哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0636
    ChrTalk(
        0x109,
        "#11P#0505F……真的吗？\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x102,
        (
            "#6P#0105F请别因为是我们的工作，\x01",
            "所以就勉强自己\x01",
            "帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x9,
        (
            "#5P#1900F没有没有，我自己也想\x01",
            "跟他聊聊。\x02\x03",

            "#1909F呵呵，因为如果说到那个时候的事，\x01",
            "可能会聊得很投机呢～\x02\x03",

            "#1906F……啊～不过，因为我还有工作，\x01",
            "所以可能抽不出\x01",
            "什么时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x101,
        (
            "#12P#0003F这样啊，\x01",
            "那就没办法了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)

    #C0640
    ChrTalk(
        0x8,
        "#6P──那个，各位。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_68(1600, 1500, 14500, 1500)

    def lambda_B76B():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B76B)

    def lambda_B778():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B778)

    def lambda_B785():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B785)

    def lambda_B792():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B792)

    def lambda_B79F():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B79F)

    def lambda_B7AC():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B7AC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)

    #C0641
    ChrTalk(
        0x9,
        "#11P#1905F怎么了，瑞贝卡小姐？\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x8,
        (
            "#6P不好意思，\x01",
            "打断了你们的对话……\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x8,
        (
            "#6P再过一会就是芙兰的休息时间了，\x01",
            "你们就利用这段休息时间\x01",
            "约他出来见个面如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x9,
        "#11P#1905F咦，可以吗？\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x8,
        (
            "#6P因为还要值班，\x01",
            "所以时间可能会有点不够，\x01",
            "但见个面应该还是可以的。\x02\x03",

            "休息时间里，这边的工作\x01",
            "我一个人就可以应付得来。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0646
    ChrTalk(
        0x109,
        (
            "#11P#0506F（瑞贝卡小姐……\x01",
            "  好像有些乐在其中的感觉啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x9,
        (
            "#11P#1900F呵呵，难得的机会，\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B995():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B995)

    def lambda_B9A2():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B9A2)

    def lambda_B9AF():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B9AF)

    def lambda_B9BC():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B9BC)

    def lambda_B9C9():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B9C9)

    def lambda_B9D6():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B9D6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x9, 1)

    #C0648
    ChrTalk(
        0x9,
        (
            "#5P#1900F那么，见面的地点……\x01",
            "就约在中央广场的西餐厅\x01",
            "『温赛特』怎么样？\x02\x03",

            "再等一会我就过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        (
            "#12P#0003F那、那么……\x01",
            "就这样决定了？\x02\x03",

            "#0000F我们就这样跟\x01",
            "安敦先生传达了哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x9,
        (
            "#5P#1909F嘻嘻，请跟他说一声，\x01",
            "我很期待与他见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x109,
        (
            "#11P#0501F（芙兰……\x01",
            "  难道对安敦先生\x01",
            "  有好感吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x104,
        (
            "#12P#0305F……嗯，怎么了，诺艾尔。\x01",
            "你在沉思什么啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    #C0653
    ChrTalk(
        0x109,
        (
            "#11P#0503F没、没什么，前辈。\x02\x03",

            "#0500F那么，罗伊德警官……\x01",
            "我们就回去跟\x01",
            "安敦先生报告一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x101,
        "#12P#0000F好，走吧。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 3000, 0, 13500, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_29(0x2A, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_32_AE47 end

    def Function_33_BC19(): pass

    label("Function_33_BC19")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 900, 15000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 0, 0, 1000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 900, 7000, 5000)
    SetCameraDistance(24500, 5000)
    FadeToBright(2000, 0)
    OP_6F(0x11)

    def lambda_BC99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BC99)

    def lambda_BCAA():
        OP_95(0xFE, 0, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCAA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    #C0655
    ChrTalk(
        0x101,
        (
            "#0000F#4P（克洛斯贝尔警察局……\x01",
            "  虽然以前来过几次……）\x02\x03",

            "#0004F（但……\x01",
            "  从今天开始，我就要在这里工作了啊。）\x02\x03",

            "#0001F（──那么，\x01",
            "  首先到接待处打个招呼吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0x0, 0x0, 0x3)
    RemoveCraft(0x0, 0xFFFF)
    OP_38(0x0, 0x80, 0x1)
    OP_42(0x0, 0x3E8, 0xFF)
    OP_42(0x0, 0x5DC, 0xFF)
    OP_42(0x0, 0x640, 0xFF)
    AddCraft(0x0, 0x96)
    AddCraft(0x0, 0xFA)
    SetChrChipPat(0x0, 0x6, 0xFA)
    SetChrPos(0x0, 0, 0, 4500, 0)
    SetScenarioFlags(0x40, 1)
    OP_C5(0x1, 0x0)
    OP_C5(0x1, 0x4)
    OP_1B(0x0, 0x0, 0x2E)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_BC19 end

    def Function_34_BDC2(): pass

    label("Function_34_BDC2")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(1000)
    OP_68(-100, 1000, 14000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -100, 0, 13000, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01900.itp")
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    BeginChrThread(0x9, 1, 0, 35)
    Sleep(500)
    SetChrName("接待小姐")

    #A0656
    AnonymousTalk(
        0xFF,
        (
            "您好，\x01",
            "欢迎来到克洛斯贝尔警察局。\x02\x03",

            "请问您有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0657
    ChrTalk(
        0x101,
        (
            "#7P#0005F啊，那个……\x02\x03",

            "#0003F──我叫罗伊德·班宁斯，\x01",
            "从今天开始\x01",
            "将在这里工作。\x02\x03",

            "#0000F还请多多指教。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0658
    NpcTalk(
        0x9,
        "接待小姐",
        (
            "#5P#1902F啊，这样啊。\x02\x03",

            "#1909F呵呵，好开心呢。\x01",
            "又来新同事了。\x02\x03",

            "#1905F啊，不过……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(500)

    #N0659
    NpcTalk(
        0x9,
        "接待小姐",
        (
            "#5P#1903F嗯，好奇怪啊。\x02\x03",

            "我没接到通知说\x01",
            "今天会有新人来啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(300)

    #N0660
    NpcTalk(
        0x9,
        "接待小姐",
        (
            "#5P#1900F那个，您确定是警察局总部，\x01",
            "而不是警备队那边吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x101,
        (
            "#7P#0000F嗯，没错，\x01",
            "是警察局总部。\x02\x03",

            "因为我在警察学校\x01",
            "拿到了搜查官的资格证书。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0662
    NpcTalk(
        0x9,
        "接待小姐",
        (
            "#5P#1905F哎～您通过了\x01",
            "搜查官考试吗！？\x02\x03",

            "#1902F好厉害啊～！\x01",
            "以新人来说，这很少见哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x101,
        (
            "#7P#0012F没、没什么～\x01",
            "只是运气好了点而已。\x02\x03",

            "#0002F而且这次参加考试的好像\x01",
            "就只有我一个人……\x02",
        )
    )

    CloseMessageWindow()

    #N0664
    NpcTalk(
        0x9,
        "接待小姐",
        (
            "#5P#1909F真是的～\x01",
            "不用这么谦虚啦。\x02\x03",

            "#1905F不过好奇怪啊。\x01",
            "如果真有新人加入，我们\x01",
            "应该会接到通知才对啊……\x02\x03",

            "#1900F那个，请问您被分配到了\x01",
            "哪个部门呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x101,
        (
            "#7P#0006F啊，这个啊……\x02\x03",

            "#0000F好像是一个叫做『特别任务支援科』的\x01",
            "部门。\x02",
        )
    )

    CloseMessageWindow()

    #N0666
    NpcTalk(
        0x9,
        "接待小姐",
        "#5P#1905F『特别任务支援科』……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1100)
    Sound(2082, 255, 100, 0)    #voice#Fran
    Sleep(600)

    #N0667
    NpcTalk(
        0x9,
        "接待小姐",
        (
            "#5P#1901F那个……\x01",
            "我们局里有这个部门吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0668
    ChrTalk(
        0x101,
        "#7P#0011F……那个，莫非没有吗？\x02",
    )

    CloseMessageWindow()

    #N0669
    NpcTalk(
        0x9,
        "接待小姐",
        (
            "#5P#1901F请、请稍等一下。\x02\x03",

            "……我好像曾在哪里\x01",
            "听到过这个名字，但又好像没听过。\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x101,
        "#7P#0011F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(-2600, 1000, 14000, 1500)
    OP_6F(0x1)
    SetChrPos(0x11, -13000, 0, 11000, 90)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)

    #N0671
    NpcTalk(
        0x11,
        "男人的声音",
        "……哦，来了啊。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 36)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C499():

        label("loc_C499")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_C499")

    QueueWorkItem2(0x9, 2, lambda_C499)
    Sleep(50)

    def lambda_C4AE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C4AE)
    OP_68(-100, 900, 14000, 4000)
    OP_6F(0x1)

    #N0672
    NpcTalk(
        0x9,
        "接待小姐",
        "#5P#1900F啊，赛尔盖警督……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 3)
    Sleep(300)

    #N0673
    NpcTalk(
        0x11,
        "不修边幅的胡子男",
        (
            "#1000F#6P芙兰，\x01",
            "这家伙就交给我吧。\x02\x03",

            "他是我们部门的新人。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x9,
        (
            "#5P#1905F啊，原来如此……\x02\x03",

            "#1900F特别任务支援科就是警督您\x01",
            "新成立的部门吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0675
    NpcTalk(
        0x11,
        "不修边幅的胡子男",
        (
            "#1003F#6P嗯，还请多指教哦。\x02\x03",

            "#1002F不过，这个部门\x01",
            "说不定连半年都撑不过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x9,
        "#5P#1909F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x101,
        "#11P#0011F……那个………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("不修边幅的胡子男")

    #A0678
    AnonymousTalk(
        0xFF,
        (
            "我是特别任务支援科科长，赛尔盖·罗。\x02\x03",

            "唔……你就是罗伊德吗？\x02",
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

    #C0679
    ChrTalk(
        0x101,
        (
            "#11P#0001F是、是的。\x01",
            "我是罗伊德·班宁斯。\x02\x03",

            "前来克洛斯贝尔警察局·特别任务支援科\x01",
            "报到──\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x11,
        "#1003F#6P啊，这个还不用。\x02",
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#11P#0005F咦……\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x11,
        (
            "#1000F#6P要报到\x01",
            "还早了点。\x02\x03",

            "跟我来吧，\x01",
            "把其他人介绍给你。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 37)
    Sleep(1000)

    #C0683
    ChrTalk(
        0x101,
        "#11P#0005F哎，啊……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 3)
    OP_6F(0x1)
    EndChrThread(0x9, 0x2)
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    #C0684
    ChrTalk(
        0x9,
        (
            "#5P#1909F那个……\x01",
            "请多多加油哦～\x02\x03",

            "#1901F虽然可能会很辛苦，\x01",
            "但只要努力，就一定没问题的！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    #C0685
    ChrTalk(
        0x101,
        (
            "#7P#0012F好、好的……\x01",
            "（超级不安……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_68(-18500, 1000, 10000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x11, -14500, 0, 10000, 270)
    SetChrPos(0x101, -11500, 0, 10000, 270)

    def lambda_C904():
        OP_95(0xFE, -26000, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C904)
    Sleep(50)

    def lambda_C921():
        OP_95(0xFE, -24500, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C921)
    PlayBGM("ed7111", 0)
    OP_68(-25500, 1000, 10000, 6000)
    SetCameraDistance(20000, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x11, 1)

    def lambda_C967():
        OP_95(0xFE, -26000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C967)
    WaitChrThread(0x101, 1)

    def lambda_C985():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C985)
    WaitChrThread(0x11, 1)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_C9AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_C9AB)

    def lambda_C9BC():
        OP_95(0xFE, -26000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C9BC)
    Sleep(500)

    def lambda_C9D9():
        OP_95(0xFE, -26000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C9D9)
    WaitChrThread(0x101, 1)

    def lambda_C9F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C9F7)

    def lambda_CA08():
        OP_95(0xFE, -26000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CA08)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x11, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x101, 0x2)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00102.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("apl/ch50006.itc", 0x21)
    SoundLoad(806)
    OP_68(-62200, 700, 16200, 0)
    MoveCamera(70, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x1)
    SetChrPos(0x11, -62700, 0, 13500, 270)
    SetChrPos(0x101, -65000, 0, 11000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x102, -60500, 150, 19800, 180)
    SetChrPos(0x103, -62500, 150, 19800, 180)
    SetChrPos(0x104, -61800, 150, 16100, 315)
    SetMapObjFrame(0xFF, "isu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu_sd", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    OP_78(0x3, 0x16)
    OP_78(0x4, 0x17)
    OP_78(0x5, 0x18)
    OP_78(0x6, 0x19)
    OP_78(0x7, 0x1A)
    OP_78(0x8, 0x1B)
    OP_49()
    SetChrPos(0x16, -61500, 0, 15900, 0)
    OP_D3(0x16, 0x0, 0xFFFF5038, 0x0, 0x0)
    SetChrPos(0x17, -60500, 0, 20100, 0)
    OP_D3(0x17, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x18, -65000, 0, 15900, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x19, -62500, 0, 20100, 0)
    OP_D3(0x19, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x1A, -67500, 0, 15900, 0)
    OP_D3(0x1A, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1B, -65000, 0, 20100, 0)
    OP_D3(0x1B, 0x0, 0x2BF20, 0x0, 0x0)
    OP_CA(0x1, 0x0, 0x0)
    OP_CA(0x1, 0x1, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00100.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_CD2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CD2E)

    def lambda_CD3F():
        OP_95(0xFE, -65000, 0, 13500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CD3F)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)
    SetChrName("少女")

    #N0686
    NpcTalk(
        0x102,
        "少女",
        "#0105F啊……\x02",
    )

    CloseMessageWindow()
    SetChrName("红发青年")

    #N0687
    NpcTalk(
        0x104,
        "红发青年",
        (
            "#5P#0300F哦，\x01",
            "好像来了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("黑衣少女")

    #N0688
    NpcTalk(
        0x103,
        "黑衣少女",
        "#0200F……………………………\x02",
    )

    CloseMessageWindow()
    OP_68(-59320, 900, 18530, 6000)
    SetCameraDistance(20500, 6000)
    MoveCamera(45, 17, 0, 6000)
    BeginChrThread(0x11, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 39)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    #C0689
    ChrTalk(
        0x11,
        (
            "#1000F#5P久等了，\x01",
            "这家伙就是最后一个成员。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    #C0690
    ChrTalk(
        0x11,
        "#1000F#5P喂，自我介绍。\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x101,
        "#11P#0005F啊，是。\x02",
    )

    CloseMessageWindow()

    def lambda_CE99():
        OP_95(0xFE, -58500, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CE99)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)
    Sleep(300)

    #C0692
    ChrTalk(
        0x101,
        (
            "#0001F#11P（哎……\x01",
            "  就老成员来说，都太年轻了……）\x02\x03",

            "（难道和我一样，都是新人吗……？\x01",
            "  不对，怎么还有个\x01",
            "  年纪这么小的女孩呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x11,
        (
            "#1000F#5P喂，怎么了？\x02\x03",

            "说说名字和出身地就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x101,
        "#0005F#11P抱、抱歉。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0695
    AnonymousTalk(
        0x101,
        (
            "──我叫罗伊德·班宁斯，\x01",
            "是克洛斯贝尔本市人。\x02\x03",

            "不过，之前一段时间\x01",
            "都居住在国外……\x02\x03",

            "如今被警察局录用，\x01",
            "所以又回来了。\x02\x03",

            "今后还请各位多多指教。\x02",
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
    SetChrName("红发青年")

    #N0696
    NpcTalk(
        0x104,
        "红发青年",
        "#6P#0302F哦哦，真是一本正经啊。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1361, 255, 100, 0)    #voice#Randy
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("红发青年")

    #A0697
    AnonymousTalk(
        0xFF,
        (
            "我叫兰迪，\x01",
            "兰迪·奥兰多。\x02\x03",

            "兴趣是搭讪、赌博，\x01",
            "还有欣赏写真集。\x02\x03",

            "到时我可以\x01",
            "把我的珍藏\x01",
            "拿出来借你看哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0698
    ChrTalk(
        0x101,
        "#0011F#11P咦咦……！？\x02",
    )

    CloseMessageWindow()
    SetChrName("少女")

    #N0699
    NpcTalk(
        0x102,
        "少女",
        "#5P#0103F……咳咳。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1171, 255, 100, 0)    #voice#Elie
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("少女")

    #A0700
    AnonymousTalk(
        0xFF,
        (
            "──初次见面，\x01",
            "我叫艾莉·麦克道尔。\x02\x03",

            "和你同样是\x01",
            "克洛斯贝尔本市人。\x02\x03",

            "请多多指教。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0701
    ChrTalk(
        0x101,
        "#0005F#11P啊，好的……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1267, 255, 100, 0)    #voice#Tio
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("黑衣少女")

    #A0702
    AnonymousTalk(
        0xFF,
        (
            "缇欧·普拉托，\x01",
            "来自列曼自治州。\x02\x03",

            "……请多指教。（点头行礼）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    #C0703
    ChrTalk(
        0x101,
        "#0012F#11P请、请多指教……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 500)
    Sleep(300)

    #C0704
    ChrTalk(
        0x101,
        "#12P#0011F那个，赛尔盖科长……？\x02",
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x11,
        "#1000F#5P嗯，怎么？\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x101,
        (
            "#12P#0001F『特别任务支援科』到底\x01",
            "是一个什么样的部门呢？\x02\x03",

            "那个……包括我在内，\x01",
            "成员好像都很年轻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x11,
        (
            "#1004F#5P啊，因为情况有些特殊。\x02\x03",

            "对了，所有成员都跟你一样，\x01",
            "是备受期待的新人。\x02\x03",

            "#1002F呵呵，气氛轻松，很好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        "#12P#0011F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x102,
        "#5P#0106F真的好吗……\x02",
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x104,
        (
            "#6P#0309F总之，没有那些\x01",
            "唠唠叨叨的前辈就已经很值得庆幸了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x103,
        "#5P#0203F………………………………\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x101,
        (
            "#12P#0006F（这、这是什么情况……）\x02\x03",

            "#0001F（不知为何，\x01",
            "  好像越来越不安了……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x11, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0713
    ChrTalk(
        0x11,
        (
            "#1005F#5P我是赛尔盖……\x02\x03",

            "#1002F……哦，辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0714
    ChrTalk(
        0x101,
        (
            "#12P#0005F（那个是……便携式的通讯终端？）\x02\x03",

            "（连那种东西\x01",
            "  都已经投入实际应用了吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x11,
        (
            "#1004F#5P……嗯，了解。\x02\x03",

            "#1002F接下来的\x01",
            "善后工作就交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0x0)
    Sleep(300)
    Sound(807, 0, 100, 0)
    Fade(250)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 0x7)
    SetChrSubChip(0x11, 0x0)
    OP_0D()
    OP_93(0x11, 0xE1, 0x1F4)
    Sleep(300)

    #C0716
    ChrTalk(
        0x11,
        (
            "#5P#1003F好，菜鸟们，你们该高兴了。\x02\x03",

            "#1002F这个『特别任务支援科』\x01",
            "到底是做什么工作的……\x02\x03",

            "接下来我会带你们去\x01",
            "一个很棒的地方慢慢体验一下。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CA(0x1, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_BDC2 end

    def Function_35_D87B(): pass

    label("Function_35_D87B")

    #Sound(2080, 255, 100, 0)    #voice#Fran
    Sleep(1000)
    #Sound(2081, 255, 100, 0)    #voice#Fran
    Return()

    # Function_35_D87B end

    def Function_36_D88B(): pass

    label("Function_36_D88B")


    def lambda_D890():
        OP_95(0xFE, -5000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D890)
    WaitChrThread(0x11, 1)

    def lambda_D8AE():
        OP_95(0xFE, -2000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D8AE)
    WaitChrThread(0x11, 1)
    Return()

    # Function_36_D88B end

    def Function_37_D8C8(): pass

    label("Function_37_D8C8")

    OP_92(0x11, 0xFFFFEC78, 0x2AF8, 0x1F4)

    def lambda_D8DA():
        OP_95(0xFE, -5000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D8DA)
    WaitChrThread(0x11, 1)

    def lambda_D8F8():
        OP_95(0xFE, -13000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D8F8)
    WaitChrThread(0x11, 1)
    Return()

    # Function_37_D8C8 end

    def Function_38_D912(): pass

    label("Function_38_D912")

    OP_93(0x11, 0x59, 0x1F4)

    def lambda_D91E():
        OP_95(0xFE, -58000, 0, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D91E)
    WaitChrThread(0x11, 1)

    def lambda_D93C():
        OP_95(0xFE, -58000, 0, 20500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D93C)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0xE1, 0x1F4)
    Return()

    # Function_38_D912 end

    def Function_39_D95D(): pass

    label("Function_39_D95D")


    def lambda_D962():
        OP_95(0xFE, -58000, 0, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D962)
    Sleep(1000)
    SetChrFlags(0x104, 0x20)

    def lambda_D984():
        OP_96(0xFE, 0xFFFF0FC4, 0x96, 0x3F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D984)

    def lambda_D99E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D99E)

    def lambda_D9AB():
        OP_D3(0xFE, 0x0, 0x0, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_D9AB)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    SetChrSubChip(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x101, 1)

    def lambda_D9E4():
        OP_95(0xFE, -58000, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9E4)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_39_D95D end

    def Function_40_DA13(): pass

    label("Function_40_DA13")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-12300, 1000, 20300, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -12700, 0, 21000, 180)
    SetChrPos(0x102, -12700, 0, 21000, 180)
    SetChrPos(0x103, -12700, 0, 21000, 180)
    SetChrPos(0x104, -12700, 0, 21000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -5000, 0, 10400, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -3700, 0, 10400, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x2, 0x10)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(160, 0, 100, 0)
    Sleep(1000)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    OP_68(-12700, 1000, 14200, 4000)
    MoveCamera(30, 25, 0, 4000)
    SetCameraDistance(22000, 4000)

    def lambda_DBCA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DBCA)

    def lambda_DBDB():
        OP_96(0xFE, 0xFFFFCBA8, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBDB)
    Sleep(600)

    def lambda_DBF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DBF8)

    def lambda_DC09():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DC09)
    Sleep(600)

    def lambda_DC26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DC26)

    def lambda_DC37():
        OP_96(0xFE, 0xFFFFCBA8, 0x0, 0x3A34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DC37)
    Sleep(600)

    def lambda_DC54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DC54)

    def lambda_DC65():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x3A34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DC65)
    Sleep(1000)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)

    #C0717
    ChrTalk(
        0x101,
        "#6P#0008F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_DCC8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DCC8)
    Sleep(50)

    def lambda_DCD8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DCD8)
    Sleep(50)

    def lambda_DCE8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DCE8)
    WaitChrThread(0x103, 2)

    #C0718
    ChrTalk(
        0x104,
        (
            "#5P#0306F哎呀呀……\x01",
            "事情好像变得有点奇怪啊。\x02\x03",

            "#0301F竟然叫我们\x01",
            "自动请辞……\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x102,
        (
            "#12P#0103F看来警察局内部\x01",
            "的情况也很复杂啊……\x02\x03",

            "#0108F虽然早已有所耳闻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x103,
        (
            "#5P#0208F……嗯。\x01",
            "这样一来，就跟约定的不一样了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0721
    ChrTalk(
        0x102,
        "#12P#0105F咦，约定指的是……？\x02",
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x103,
        (
            "#5P#0203F……没什么，自言自语罢了。\x02\x03",

            "#0200F话说，赛尔盖科长\x01",
            "去哪里了呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x104,
        (
            "#5P#0301F是啊。\x02\x03",

            "只给我们出了个课题，\x01",
            "也不来迎接一下，到底在搞什么？\x02\x03",

            "#0306F还害我们被那个讨厌的副局长\x01",
            "唠唠叨叨地斥责了一通……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0724
    ChrTalk(
        0x104,
        (
            "#5P#0305F怎么了，罗伊德。\x01",
            "你看起来很没精神啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DF28():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DF28)
    Sleep(50)

    def lambda_DF38():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DF38)
    WaitChrThread(0x103, 2)

    #C0725
    ChrTalk(
        0x102,
        (
            "#11P#0108F副局长让我们自动请辞，\x01",
            "这对你打击有这么大吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0726
    ChrTalk(
        0x101,
        (
            "#6P#0002F啊，不是……\x02\x03",

            "#0006F……只是觉得\x01",
            "情况跟我想象中差了很多……\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x102,
        "#11P#0105F？？\x02",
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x104,
        "#5P#0305F嗯……？\x02",
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x103,
        "#5P#0200F……………………………\x02",
    )

    CloseMessageWindow()

    #N0730
    NpcTalk(
        0xA,
        "男人的声音",
        (
            "#3P哟，新人们。\x01",
            "你们好像很不幸啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_E0C9():
        OP_95(0xFE, -13300, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E0C9)
    Sleep(150)

    def lambda_E0E6():
        OP_95(0xFE, -12000, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E0E6)
    Sleep(300)
    OP_68(-12700, 1200, 12400, 3500)
    MoveCamera(35, 19, 0, 3500)
    SetCameraDistance(20500, 3500)

    def lambda_E128():

        label("loc_E128")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_E128")

    QueueWorkItem2(0x101, 2, lambda_E128)
    Sleep(50)

    def lambda_E13D():

        label("loc_E13D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_E13D")

    QueueWorkItem2(0x103, 2, lambda_E13D)
    Sleep(50)

    def lambda_E152():

        label("loc_E152")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_E152")

    QueueWorkItem2(0x102, 2, lambda_E152)
    Sleep(50)

    def lambda_E167():

        label("loc_E167")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_E167")

    QueueWorkItem2(0x104, 2, lambda_E167)
    WaitChrThread(0xA, 1)

    def lambda_E17D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E17D)
    WaitChrThread(0xB, 1)

    def lambda_E18E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E18E)
    WaitChrThread(0xB, 2)
    OP_6F(0x79)

    #C0731
    ChrTalk(
        0x101,
        "#0005F#5P您是……\x02",
    )

    CloseMessageWindow()

    #N0732
    NpcTalk(
        0xA,
        "满脸胡子的男性",
        (
            "#12P我叫多诺邦。\x01",
            "隶属于搜查二科。\x02",
        )
    )

    CloseMessageWindow()

    #N0733
    NpcTalk(
        0xB,
        "金发青年",
        "#4P我是同属于搜查二科的雷蒙德。\x02",
    )

    CloseMessageWindow()

    #N0734
    NpcTalk(
        0xB,
        "金发青年",
        (
            "#4P哎～虽然早就有所耳闻，\x01",
            "但没想到还有这么小的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x103,
        "#5P#0211F（…………不爽……………）\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        (
            "#0000F#5P……初次见面，\x01",
            "我叫罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x102,
        "#5P#0100F我叫艾莉·麦克道尔。\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x104,
        (
            "#5P#0300F我是兰迪·奥兰多，\x01",
            "多多指教哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xA,
        (
            "#12P哦，欢迎成为\x01",
            "克洛斯贝尔警察局的一员。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xA,
        "#12P这样啊，原来你就是那个……\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x101,
        "#0005F#5P……咦…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0742
    ChrTalk(
        0xB,
        "#11P警督……？\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xA,
        "#12P……没事，没什么。\x02",
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xA,
        (
            "#12P不过赛尔盖那家伙\x01",
            "也太异想天开了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0xA,
        (
            "#12P凭这几个新人，\x01",
            "就想获得市民的支持吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x101,
        "#0011F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x102,
        (
            "#5P#0105F那个……\x01",
            "两位指的是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0xA,
        (
            "#12P什么啊……\x01",
            "你们还不知道吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0xA,
        (
            "#12P唔，\x01",
            "莫非是我们说漏嘴了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)
    Sleep(300)

    #C0750
    ChrTalk(
        0xB,
        (
            "#4P不过，你们也真是\x01",
            "抽到了下下签啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0xB,
        (
            "#4P这工作不仅辛苦，而且还得不到回报，\x01",
            "要是我的话早就辞职了。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x101,
        "#0005F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0753
    ChrTalk(
        0xA,
        (
            "#6P你这家伙也\x01",
            "有点毅力好不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0xA,
        (
            "#6P现在我还是能把你\x01",
            "踢去赛尔盖那边哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0755
    ChrTalk(
        0xB,
        (
            "#11P不、不要啊，警督。\x01",
            "饶了我吧～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    Sleep(300)

    #C0756
    ChrTalk(
        0xA,
        (
            "#12P虽然会很辛苦，\x01",
            "但我还是希望你们能好好考虑一下，\x01",
            "留下为赛尔盖工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xA,
        (
            "#12P只是，千万不要勉强自己哦。\x01",
            "即使不行，你们也可以全都\x01",
            "来我们二科的。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x101,
        "#0012F#5P谢、谢谢您……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)

    #C0759
    ChrTalk(
        0xB,
        "#4P那你们加油哦～\x02",
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0xB,
        (
            "#4P啊，这不是艾莉吗？\x01",
            "下次要不要一起吃个饭啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0xB,
        "#4P我知道有一家餐厅很不错哦──\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0xB, 500)

    def lambda_E728():
        OP_95(0xFE, -12500, 0, 10400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E728)
    WaitChrThread(0xA, 1)

    def lambda_E746():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E746)

    def lambda_E75F():
        OP_96(0xFE, 0xFFFFCC0C, 0x0, 0x28A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E75F)
    Sound(819, 0, 100, 0)
    WaitChrThread(0xA, 1)

    #C0762
    ChrTalk(
        0xA,
        "#6P喂，赶紧走！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0763
    ChrTalk(
        0xB,
        (
            "#11P好痛！\x01",
            "这只是单纯的客套话啦～\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xA, 0xFFFFC6F8, 0x2E18, 0x1F4)
    BeginChrThread(0xA, 3, 0, 41)
    BeginChrThread(0xB, 3, 0, 42)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0764
    ChrTalk(
        0x101,
        "#6P#0008F………………………………\x02",
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x104,
        (
            "#11P#0306F哈，莫名其妙地\x01",
            "听了一堆乱七八糟的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x103,
        (
            "#5P#0206F……先不说是不是下下签，\x01",
            "但我不喜欢太辛苦的地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x102,
        (
            "#12P#0106F总之，必须向科长本人\x01",
            "询问一下详细情况……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0768
    ChrTalk(
        0x102,
        (
            "#11P#0101F去接待处咨询的话，\x01",
            "应该就能知道他在哪里了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0769
    ChrTalk(
        0x101,
        "#6P#0008F啊……嗯，也对──\x02",
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_E9CA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E9CA)
    Sleep(50)

    def lambda_E9DA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E9DA)
    WaitChrThread(0x103, 2)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    #Sound(1085, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0770
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F您好，\x01",
            "我是罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0771
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，老狐狸的唠叨\x01",
            "和挖苦好像结束了啊。\x02\x03",

            "很烦人吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0772
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F嗯，确实如此……\x02\x03",

            "#0013F──不对！\x01",
            "您到底去哪里了啊！？\x02\x03",

            "您不是说\x01",
            "会在警察局总部等我们的吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0773
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，你们的行李都到了，\x01",
            "所以我去找搬家公司帮你们运行李了。\x02\x03",

            "我这个上司很亲切吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0774
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F您说行李……\x01",
            "难道是运到宿舍里了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0775
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，详细情况\x01",
            "到那里再慢慢讲吧。\x02\x03",

            "我先去那里等，你们快点过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0776
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F呼……知道了。\x02\x03",

            "#0001F不过，宿舍\x01",
            "到底在哪里啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0777
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，正确来说那不算是宿舍哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0778
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F咦……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0779
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那是克洛斯贝尔警察局\x01",
            "『特别任务支援科·部门楼』。\x02\x03",

            "而你们的房间，\x01",
            "就是那里的二楼和三楼。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 0)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_DA13 end

    def Function_41_EDE7(): pass

    label("Function_41_EDE7")


    def lambda_EDEC():
        OP_95(0xFE, -14600, 0, 11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EDEC)
    WaitChrThread(0xA, 1)
    OP_68(-12700, 1000, 14200, 3000)
    MoveCamera(30, 25, 0, 3000)
    SetCameraDistance(22000, 3000)

    def lambda_EE2F():
        OP_95(0xFE, -14600, 0, 17100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EE2F)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_EE55():
        OP_95(0xFE, -12500, 0, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EE55)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_EE8F():
        OP_95(0xFE, -12500, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EE8F)
    Sleep(500)

    def lambda_EEAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EEAC)
    WaitChrThread(0xA, 1)
    Return()

    # Function_41_EDE7 end

    def Function_42_EEBD(): pass

    label("Function_42_EEBD")

    Sleep(600)

    def lambda_EEC5():
        OP_95(0xFE, -14600, 0, 11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EEC5)
    WaitChrThread(0xB, 1)
    Sleep(100)

    def lambda_EEE6():
        OP_95(0xFE, -14600, 0, 17100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EEE6)
    WaitChrThread(0xB, 1)

    def lambda_EF04():
        OP_95(0xFE, -12500, 0, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EF04)
    WaitChrThread(0xB, 1)

    def lambda_EF22():
        OP_95(0xFE, -12500, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EF22)
    Sleep(500)

    def lambda_EF3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EF3F)
    WaitChrThread(0xB, 1)
    Sleep(300)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    Return()

    # Function_42_EEBD end

    def Function_43_EF68(): pass

    label("Function_43_EF68")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-70, 1500, 13120, 0)
    MoveCamera(32, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 680, 0, 12880, 0)
    SetChrPos(0x102, -460, 0, 12880, 0)
    SetChrPos(0x103, -460, 0, 11820, 0)
    SetChrPos(0x104, 680, 0, 11820, 0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #N0780
    NpcTalk(
        0x8,
        "戴眼镜的女性",
        "#5P哎呀……\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    #N0781
    NpcTalk(
        0x9,
        "接待小姐",
        "#1905F#5P啊，罗伊德警官！\x02",
    )

    CloseMessageWindow()
    OP_95(0x9, 900, 0, 15400, 2000, 0x0)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0782
    ChrTalk(
        0x101,
        (
            "#0012F#12P哈哈……\x01",
            "你好。\x02\x03",

            "#0000F我们看到终端上的信息，\x01",
            "所以前来拜访……\x02",
        )
    )

    CloseMessageWindow()

    #N0783
    NpcTalk(
        0x8,
        "戴眼镜的女性",
        "#5P嗯，等你们很久了。\x02",
    )

    CloseMessageWindow()

    #N0784
    NpcTalk(
        0x8,
        "戴眼镜的女性",
        (
            "#5P初次见面──\x01",
            "我是担任克洛斯贝尔警察局\x01",
            "接待处接待工作的瑞贝卡。\x02",
        )
    )

    CloseMessageWindow()

    #N0785
    NpcTalk(
        0x9,
        "接待小姐",
        (
            "#1900F#5P我是芙兰·希卡，\x01",
            "同为担任接待工作的接待员。\x02\x03",

            "#1909F呵呵，前天我已经跟\x01",
            "各位聊过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x101,
        (
            "#0002F#12P哈哈，对哦。\x01",
            "前天让你\x01",
            "见笑了……\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x103,
        (
            "#0204F#6P……具体来说，\x01",
            "就是被游击士抢了风头后，\x01",
            "还被副局长教训了。\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x101,
        "#0011F#12P唔……\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x102,
        "#0106F#6P缇、缇欧……\x02",
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x9,
        (
            "#1909F#5P啊哈哈……\x01",
            "当时各位真的很不幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x8,
        (
            "#5P呵呵，各位请\x01",
            "不用太介意。\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x8,
        (
            "#5P你们的部门刚刚成立，\x01",
            "一开始肯定会有很多不习惯的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x8,
        (
            "#5P我们也会尽可能\x01",
            "为各位提供帮助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x101,
        "#0002F#12P谢、谢谢你们。\x02",
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x104,
        (
            "#0309F#12P哈～有您这句话，\x01",
            "我们就有信心了！\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x102,
        (
            "#0104F#6P那就麻烦你们了。\x02\x03",

            "#0100F那么……可以请您为我们补充说明一下\x01",
            "支援请求的相关事项吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x8,
        (
            "#5P对哦，\x01",
            "那么就马上开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x8,
        (
            "#5P──首先，\x01",
            "局里会给你们配\x01",
            "一名专门的联络员，\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x8,
        "#5P就是芙兰。\x02",
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x9,
        "#1909F#5P请多多指教。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0801
    ChrTalk(
        0x101,
        "#0005F#12P联络员……？\x02",
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x102,
        (
            "#0105F#6P是通过那个『艾尼格玛』\x01",
            "向我们提供帮助吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x9,
        (
            "#1904F#5P那个，其实也并不是\x01",
            "提供现场帮助……\x02\x03",

            "#1900F主要是负责在各位完成『支援请求』时，\x01",
            "处理相关的报告。\x02\x03",

            "这些都是通过『导力网络』来完成的。\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x104,
        (
            "#0301F#12P唔，变得有点\x01",
            "难懂了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x103,
        (
            "#0203F#6P……也就是说，我们今后\x01",
            "将会接受各种各样的委托……\x02\x03",

            "#0200F在完成委托后，\x01",
            "芙兰小姐便会通过支援科的终端\x01",
            "处理我们所提交的报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x101,
        "#0001F#12P那个，也就是说……\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x102,
        (
            "#0101F#6P我们提交报告时，\x01",
            "并不用来警察局总部吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x8,
        (
            "#5P嗯，在即时审查完\x01",
            "各位所提交的报告后，\x01",
            "我们会发放额外报酬的。\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x8,
        (
            "#5P还有，\x01",
            "当成绩点数累积到一定程度后，\x01",
            "搜查官等级还会上升。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x9,
        (
            "#1909F#5P呵呵……\x01",
            "我就是负责帮各位\x01",
            "处理这些事情的。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x101,
        "#0004F#12P原来如此，是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x104,
        (
            "#0300F#12P也就是说\x01",
            "那些麻烦的事务手续，\x01",
            "都可以在支援科的终端上完成？\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x8,
        (
            "#5P嗯，这也是导力网络的\x01",
            "运作试验的内容之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x8,
        (
            "#5P缇欧。\x01",
            "支援科的终端已经\x01",
            "安装好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x103,
        "#0202F#6P嗯，随时都可以使用。\x02",
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x8,
        "#5P我知道了。\x02",
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x8,
        (
            "#5P那么，我最后再\x01",
            "重新说明一下\x01",
            "支援请求的相关事项。\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x8,
        (
            "#5P如果有什么不懂的，\x01",
            "请不要客气，尽管提问哦。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 3)
    ClearScenarioFlags(0x1, 4)
    ClearScenarioFlags(0x1, 5)
    ClearScenarioFlags(0x1, 6)
    FadeToDark(300, 0, 100)
    OP_0D()
    Call(0, 44)

    #C0819
    ChrTalk(
        0x8,
        (
            "#5P那么，这样一来，\x01",
            "【支援请求的补充说明】任务\x01",
            "就完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x9,
        (
            "#1900F#5P那个，各位在回到支援科后，\x01",
            "请通过终端上试着提交一下『报告』。\x02\x03",

            "我会给各位发送\x01",
            "新的支援请求信息～\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x101,
        "#0000F#12P知道了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0822
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【支援请求的补充说明】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_68(-350, 1540, 12250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -350, 0, 12250, 0)
    SetChrPos(0x1, -350, 0, 12250, 0)
    SetChrPos(0x2, -350, 0, 12250, 0)
    SetChrPos(0x3, -350, 0, 12250, 0)
    OP_29(0x1, 0x4, 0x10)
    OP_29(0x1, 0x1, 0x0)
    OP_29(0x1, 0x1, 0x1)
    OP_29(0x3D, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_43_EF68 end

    def Function_44_FAA4(): pass

    label("Function_44_FAA4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FAAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10090")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FB4A")

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【支援请求指的是？】\x01",        # 0
            "【在哪里进行确认？】\x01",        # 1
            "【怎样提交报告？】\x01",          # 2
            "【搜查官等级指的是？】\x01",      # 3
            "没什么特别想要问的\x01",          # 4
        )
    )

    MenuEnd(0x1)
    Jump("loc_FBAA")

    label("loc_FB4A")


    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【支援请求指的是？】\x01",        # 0
            "【在哪里进行确认？】\x01",        # 1
            "【怎样提交报告？】\x01",          # 2
            "【搜查官等级指的是？】\x01",      # 3
        )
    )

    MenuEnd(0x1)

    label("loc_FBAA")

    OP_60(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBC9")
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_FBE2")

    label("loc_FBC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBE2")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_FBE2")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_FC0A"),
        (1, "loc_FD3E"),
        (2, "loc_FE40"),
        (3, "loc_FF14"),
        (4, "loc_1005D"),
        (SWITCH_DEFAULT, "loc_1006C"),
    )


    label("loc_FC0A")


    #C0823
    ChrTalk(
        0x8,
        (
            "#5P支援请求是指各处向特别任务支援科提出的\x01",
            "各式各样的『委托』。\x02",
        )
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x8,
        (
            "#5P从简单的帮助到正式的案件调查，\x01",
            "以及消灭魔兽等，\x01",
            "委托的内容多种多样。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x8,
        (
            "#5P除了少数几种特殊情况外，\x01",
            "要不要接受委托，\x01",
            "各位都可以自行决定……\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x8,
        (
            "#5P但如果不在期限内完成的话，委托便会自动失效，\x01",
            "关于这点，还请各位多加注意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_10071")

    label("loc_FD3E")


    #C0827
    ChrTalk(
        0x8,
        (
            "#5P对于当前能够接受的支援请求，\x01",
            "各位可以通过特别任务支援科的终端\x01",
            "进行确认。\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x8,
        (
            "#5P一经确认，支援请求\x01",
            "便会记录在调查手册上，\x01",
            "这一点也请各位注意查看。\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x8,
        (
            "#5P支援请求的追加更新\x01",
            "每天仅有一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x8,
        (
            "#5P所以建议各位每天都去\x01",
            "支援科的终端进行确认。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_10071")

    label("loc_FE40")


    #C0831
    ChrTalk(
        0x8,
        (
            "#5P当『完成』支援请求后，\x01",
            "请各位通过特别任务支援科的终端\x01",
            "提交『报告』。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x8,
        (
            "#5P通过导力网络，\x01",
            "我们可即时对其进行评定。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x8,
        (
            "#5P根据委托内容，我们有时还会\x01",
            "发放特别奖励，希望各位能\x01",
            "注意经常提交报告。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_10071")

    label("loc_FF14")


    #C0834
    ChrTalk(
        0x8,
        (
            "#5P各位可以通过解决普通的调查任务\x01",
            "以及完成支援请求\x01",
            "以提高成绩。\x02",
        )
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0x8,
        (
            "#5P此成绩会以『ＤＰ（调查点数）』来表示，\x01",
            "根据各任务与支援请求期间各位的表现情况，\x01",
            "有时还会追加奖励点数。\x02",
        )
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x8,
        (
            "#5P──在ＤＰ达到一定数值后，\x01",
            "『搜查官等级』便会上升。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x8,
        (
            "#5P此等级目前分为１５级，\x01",
            "每次提高等级都会得到奖励物品，\x01",
            "所以十分值得争取。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_10071")

    label("loc_1005D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10071")

    label("loc_1006C")

    Jump("loc_10071")

    label("loc_10071")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1008B")
    FadeToDark(300, 0, 100)
    OP_0D()

    label("loc_1008B")

    Jump("loc_FAAE")

    label("loc_10090")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_44_FAA4 end

    def Function_45_1009B(): pass

    label("Function_45_1009B")

    ClearScenarioFlags(0x2, 1)
    ClearScenarioFlags(0x2, 2)
    ClearScenarioFlags(0x2, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_100AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_102D1")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_100ED")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_102CC")

    label("loc_100ED")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10121")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_102CC")

    label("loc_10121")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10155")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_102CC")

    label("loc_10155")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10189")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_102CC")

    label("loc_10189")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_101BD")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_102CC")

    label("loc_101BD")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_101F1")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_102CC")

    label("loc_101F1")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10225")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_102CC")

    label("loc_10225")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10259")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_102CC")

    label("loc_10259")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10290")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    SetScenarioFlags(0x2, 2)
    Jump("loc_102CC")

    label("loc_10290")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xEE), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102C7")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    SetScenarioFlags(0x2, 3)
    Jump("loc_102CC")

    label("loc_102C7")

    Jump("loc_102D1")

    label("loc_102CC")

    Jump("loc_100AE")

    label("loc_102D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_10DBA")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-900, 1540, 13420, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1035B")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0xEF, 300, 40, 13000, 0)
    SetChrPos(0x153, -900, 40, 11800, 0)
    Jump("loc_10483")

    label("loc_1035B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103CD")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x109, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_10483")

    label("loc_103CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1043F")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x10A, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_10483")

    label("loc_1043F")

    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)

    label("loc_10483")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    #C0838
    ChrTalk(
        0x8,
        (
            "啊，各位……\x01",
            "战斗手册的情报好像\x01",
            "有了大量的更新啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x8,
        (
            "我想记录一下魔兽的情报，\x01",
            "所以可以允许我看一下战斗手册吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x101,
        "#0000F嗯，当然可以。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0841
    ChrTalk(
        0x8,
        (
            "十分感谢，\x01",
            "手册还给你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x8,
        (
            "这是本次的奖励，\x01",
            "请收下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105F1")

    #A0843
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0844
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "1个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_108EA")

    label("loc_105F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10646")

    #A0845
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0846
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "2个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_108EA")

    label("loc_10646")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1069B")

    #A0847
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0848
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "3个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_108EA")

    label("loc_1069B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106F0")

    #A0849
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0850
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "4个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_108EA")

    label("loc_106F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10745")

    #A0851
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0852
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "5个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_108EA")

    label("loc_10745")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1079A")

    #A0853
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0854
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "6个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_108EA")

    label("loc_1079A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107EF")

    #A0855
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0856
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "7个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_108EA")

    label("loc_107EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10844")

    #A0857
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0858
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "8个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_108EA")

    label("loc_10844")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10899")

    #A0859
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0860
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "9个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_108EA")

    label("loc_10899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108EA")

    #A0861
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0862
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "10个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_108EA")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1091E")
    Sound(17, 0, 100, 0)

    #A0863
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "2个收下了。\x02",
        )
    )

    AddItemNumber(0x395, 2)
    CloseMessageWindow()
    Jump("loc_10949")

    label("loc_1091E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10949")
    Sound(17, 0, 100, 0)

    #A0864
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber(0x395, 1)
    CloseMessageWindow()

    label("loc_10949")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10A5C")

    #C0865
    ChrTalk(
        0x8,
        (
            "如果以后收集到了新的魔兽情报，\x01",
            "请再次过来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x101,
        "#0000F好的，到时就麻烦你了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_109F8")

    #C0867
    ChrTalk(
        0x102,
        "#0100F那就下次再来打扰了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A57")

    label("loc_109F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10A27")

    #C0868
    ChrTalk(
        0x103,
        "#0200F下次再来打扰。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A57")

    label("loc_10A27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10A57")

    #C0869
    ChrTalk(
        0x104,
        "#0300F那就下次再来打扰啦。\x02",
    )

    CloseMessageWindow()

    label("loc_10A57")

    Jump("loc_10D37")

    label("loc_10A5C")


    #C0870
    ChrTalk(
        0x8,
        (
            "谢谢你们帮忙\x01",
            "收集了这么多情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0871
    ChrTalk(
        0x8,
        (
            "其实我们也拜托过\x01",
            "其他搜查官帮忙收集这些情报……\x02",
        )
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0x8,
        (
            "但只有特别任务支援科的各位\x01",
            "收集得这么全面哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B29")

    #C0873
    ChrTalk(
        0x104,
        (
            "#0300F哈哈……因为我们\x01",
            "总是到处乱晃。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10BA6")

    label("loc_10B29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B6D")

    #C0874
    ChrTalk(
        0x102,
        (
            "#0100F啊哈哈……因为我们\x01",
            "去了很多地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10BA6")

    label("loc_10B6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10BA6")

    #C0875
    ChrTalk(
        0x103,
        (
            "#0200F……因为我们\x01",
            "总是四处奔波呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BA6")


    #C0876
    ChrTalk(
        0x101,
        (
            "#0000F而且我们也经常进行战斗。\x02\x03",

            "……总之，能帮上忙\x01",
            "就再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0877
    ChrTalk(
        0x8,
        "呵呵……各位果然很可靠啊。\x02",
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x8,
        (
            "总部收集的情报\x01",
            "也已经足够了，\x01",
            "所以本项调查就此结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x8,
        (
            "十分感谢各位\x01",
            "能帮忙到最后。\x01",
            "这次会给予各位特别报酬哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0880
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１００００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(10000)

    #C0881
    ChrTalk(
        0x8,
        (
            "以后可能还会有事\x01",
            "需要各位帮忙。\x01",
            "到时就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x101,
        (
            "#0000F嗯，彼此彼此，\x01",
            "到时候就麻烦你了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D37")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D55")
    Jump("loc_10D8F")

    label("loc_10D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D72")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_10D8F")

    label("loc_10D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D8F")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_10D8F")

    label("loc_10D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_10D9B")
    ClearScenarioFlags(0x2, 0)

    label("loc_10D9B")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_10EA4")

    label("loc_10DBA")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E3B")

    #C0883
    ChrTalk(
        0x8,
        (
            "总部收集的情报\x01",
            "也已经足够了，\x01",
            "所以本项调查就此结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0884
    ChrTalk(
        0x8,
        (
            "以后可能还会有事\x01",
            "需要各位帮忙。\x01",
            "到时就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10EA4")

    label("loc_10E3B")


    #C0885
    ChrTalk(
        0x8,
        (
            "战斗手册好像\x01",
            "没有新内容呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x8,
        (
            "等情报得到进一步更新时，\x01",
            "请再拿来给我看。\x01",
            "我们会将情报记录整理的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EA4")

    Return()

    # Function_45_1009B end

    def Function_46_10EA5(): pass

    label("Function_46_10EA5")

    EventBegin(0x1)
    Sleep(50)

    #C0887
    ChrTalk(
        0x101,
        (
            "#0005F（哦……\x01",
            "  现在不需要外出。）\x02\x03",

            "#0003F（先到接待处打声招呼……\x01",
            "  对了，也去问问\x01",
            "  部门分配的事吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 80, 40, 2480, 0)
    EventEnd(0x4)
    Return()

    # Function_46_10EA5 end

    def Function_47_10F2D(): pass

    label("Function_47_10F2D")

    EventBegin(0x1)
    Sleep(50)

    #C0888
    ChrTalk(
        0x101,
        (
            "#0005F（哦……\x01",
            "  这边不是接待处。）\x02\x03",

            "#0003F（先到接待处打声招呼……\x01",
            "  对了，也去问问\x01",
            "  部门分配的事吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -6760, 0, 10110, 89)
    EventEnd(0x4)
    Return()

    # Function_47_10F2D end

    def Function_48_10FB5(): pass

    label("Function_48_10FB5")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11749")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116F2")
    Fade(500)
    OP_68(-12470, 1500, 17150, 0)
    MoveCamera(31, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -13130, 0, 17450, 0)
    SetChrPos(0x102, -11910, 0, 17450, 0)
    SetChrPos(0x103, -13130, 0, 16280, 0)
    SetChrPos(0x104, -11910, 0, 16280, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0889
    ChrTalk(
        0x101,
        "#0005F啊，有人出来了。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x12, -12480, 0, 20980, 180)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)

    def lambda_11104():
        OP_95(0xFE, -12480, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_11104)
    Sleep(200)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
    WaitChrThread(0x12, 1)
    Sleep(600)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)

    #C0890
    ChrTalk(
        0x12,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0891
    ChrTalk(
        0x104,
        "#0305F（咦咦……）\x02",
    )

    CloseMessageWindow()

    #C0892
    ChrTalk(
        0x101,
        "#0005F（这、这个人……）\x02",
    )

    CloseMessageWindow()

    def lambda_11199():
        OP_95(0xFE, -12480, 0, 18200, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_11199)
    Sleep(500)

    def lambda_111B6():
        OP_96(0xFE, 0xFFFFCCB6, 0x0, 0x40A6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_111B6)

    def lambda_111D0():
        OP_96(0xFE, 0xFFFFD17A, 0x0, 0x40A6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_111D0)
    Sleep(100)

    def lambda_111ED():
        OP_96(0xFE, 0xFFFFCCB6, 0x0, 0x3C14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_111ED)

    def lambda_11207():
        OP_96(0xFE, 0xFFFFD17A, 0x0, 0x3C14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11207)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    #C0893
    ChrTalk(
        0x12,
        (
            "你们几个，\x01",
            "为什么会聚在这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x12,
        (
            "这前面可不是你们\x01",
            "这种无名小卒该去的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0x104,
        "#0306F是、是这样呢。\x02",
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0x103,
        "#0200F虽然无法否定……\x02",
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0x12,
        (
            "……话说回来，难道你们\x01",
            "没听从我的忠告吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0898
    ChrTalk(
        0x12,
        (
            "我不是让你们\x01",
            "马上辞去特别任务支援科的工作了吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0899
    ChrTalk(
        0x12,
        (
            "那只是赛尔盖那瘟神\x01",
            "硬要弄出来的\x01",
            "无聊部门……\x02",
        )
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x12,
        (
            "就像垃圾一样，\x01",
            "没半点用处。\x01",
            "这种破船只要半年就会沉掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0901
    ChrTalk(
        0x12,
        (
            "亏我还出于善意\x01",
            "给了你们忠告……\x02",
        )
    )

    CloseMessageWindow()

    #C0902
    ChrTalk(
        0x102,
        (
            "#0105F那、那个，副局长。\x01",
            "您不是急着要去哪里吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0903
    ChrTalk(
        0x12,
        (
            "哼，对了，\x01",
            "都是因为你们，害我完全忘掉了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-12470, 1500, 15150, 4000)

    def lambda_11427():
        OP_95(0xFE, -12480, 0, 13330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_11427)

    def lambda_11441():

        label("loc_11441")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_11441")

    QueueWorkItem2(0x101, 2, lambda_11441)

    def lambda_11453():

        label("loc_11453")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_11453")

    QueueWorkItem2(0x102, 2, lambda_11453)

    def lambda_11465():

        label("loc_11465")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_11465")

    QueueWorkItem2(0x103, 2, lambda_11465)

    def lambda_11477():

        label("loc_11477")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_11477")

    QueueWorkItem2(0x104, 2, lambda_11477)

    def lambda_11489():
        OP_96(0xFE, 0xFFFFCB8A, 0x0, 0x3FAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11489)

    def lambda_114A3():
        OP_96(0xFE, 0xFFFFD2A6, 0x0, 0x3FAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_114A3)
    Sleep(100)

    def lambda_114C0():
        OP_96(0xFE, 0xFFFFCB8A, 0x0, 0x3B1A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_114C0)

    def lambda_114DA():
        OP_96(0xFE, 0xFFFFD2A6, 0x0, 0x3B1A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_114DA)
    OP_6F(0x1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x101, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    Sleep(500)
    OP_93(0x12, 0x0, 0x1F4)
    Sleep(500)

    #C0904
    ChrTalk(
        0x12,
        (
            "给我听好了，\x01",
            "一定不要多管闲事！\x02",
        )
    )

    CloseMessageWindow()

    #C0905
    ChrTalk(
        0x12,
        (
            "你们只要\x01",
            "做些表演给市民看的\x01",
            "工作就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0x12,
        (
            "不要没事就来局里乱晃！\x01",
            "回到你们自己的楼里去！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(100)
    OP_95(0x12, -12480, 0, 10350, 2000, 0x0)

    def lambda_115C2():
        OP_95(0xFE, -3890, 0, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_115C2)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0907
    ChrTalk(
        0x101,
        (
            "#0006F那个……\x01",
            "还是不要\x01",
            "乘导力梯了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0908
    ChrTalk(
        0x104,
        (
            "#0303F嗯，怎么说呢……\x01",
            "感觉我们还并没有\x01",
            "被接受为警察的一员呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0909
    ChrTalk(
        0x103,
        (
            "#0200F……如果没特别的事，\x01",
            "我们还是不要\x01",
            "去楼上了吧。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetScenarioFlags(0x46, 7)
    Jump("loc_11749")

    label("loc_116F2")


    #C0910
    ChrTalk(
        0x101,
        (
            "#0003F……没有事情需要去楼上啊……\x02\x03",

            "#0000F也不想被副局长训斥，\x01",
            "还是不要上去了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_117C8")

    #C0911
    ChrTalk(
        0x101,
        (
            "#0003F……没有事情需要去楼上啊……\x02\x03",

            "#0000F要是没有正事就直接上去，\x01",
            "说不定又会被副局长训斥的。\x01",
            "还是不要上去了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117C8")

    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_48_10FB5 end

    def Function_49_117DC(): pass

    label("Function_49_117DC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AE8")

    #C0912
    ChrTalk(
        0x101,
        (
            "#0005F对了……\x01",
            "我之前就一直很在意。\x02\x03",

            "#0001F这个是什么呢？\x01",
            "好像是某种装置……\x02",
        )
    )

    CloseMessageWindow()

    #C0913
    ChrTalk(
        0x104,
        (
            "#0305F哦哦，我也一直很在意啊。\x02\x03",

            "#0300F里面好像摆放了很多果汁\x01",
            "和咖啡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0914
    ChrTalk(
        0x103,
        (
            "#0202F这是『导力式自动贩卖机』。\x01",
            "两位是第一次见到吗？\x02\x03",

            "#0204F只要投入米拉硬币，\x01",
            "就可以买到相应\x01",
            "价格的饮料哦。\x02\x03",

            "这原本是由爱普斯泰恩财团所开发的，\x01",
            "所以在财团的\x01",
            "研究设施中经常能看到……\x02\x03",

            "#0202F如今似乎也在克洛斯贝尔\x01",
            "投入了实验性使用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0915
    ChrTalk(
        0x101,
        "#0000F哎，原来如此啊……\x02",
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x104,
        "#0305F大小姐，你知道吗？\x02",
    )

    CloseMessageWindow()

    #C0917
    ChrTalk(
        0x102,
        (
            "#0104F不，我也是第一次见到。\x02\x03",

            "#0100F不过，由爱普斯泰恩财团\x01",
            "所研发的装置\x01",
            "还真是遍布各处呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0x103,
        (
            "#0203F听说是因为有\x01",
            "实力雄厚的投资者提供资金……\x02\x03",

            "#0200F……各位如果想要使用，\x01",
            "就请投入硬币吧。\x01",
            "因为这种机器无法识别纸币。\x02",
        )
    )

    CloseMessageWindow()

    #C0919
    ChrTalk(
        0x101,
        (
            "#0000F知、知道了。\x01",
            "（这个装置挺少见的……\x01",
            "  就用一次看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D16")

    label("loc_11AE8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0920
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一台导力式自动贩卖机。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0921
    ChrTalk(
        0x101,
        (
            "#0005F这个……我记得好像投入硬币\x01",
            "就能买到饮料吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11BC6")

    #C0922
    ChrTalk(
        0x103,
        (
            "#0200F嗯，这是由爱普斯泰恩财团开发的\x01",
            "自动贩卖机。\x02\x03",

            "在克洛斯贝尔\x01",
            "也投入了实验性使用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CDD")

    label("loc_11BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C4C")

    #C0923
    ChrTalk(
        0x102,
        (
            "#0100F这个好像是由爱普斯泰恩财团开发的\x01",
            "自动贩卖机……\x02\x03",

            "据缇欧说，\x01",
            "是财团在克洛斯贝尔\x01",
            "将其投入实验性使用的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CDD")

    label("loc_11C4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11CDD")

    #C0924
    ChrTalk(
        0x104,
        (
            "#0300F这个好像是由爱普斯泰恩财团开发的\x01",
            "自动贩卖机……应该没记错吧。\x02\x03",

            "听阿缇说，\x01",
            "这东西是财团在克洛斯贝尔\x01",
            "为了试验而设置的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CDD")


    #C0925
    ChrTalk(
        0x101,
        (
            "#0000F真不愧是克洛斯贝尔……\x01",
            "果然有很多稀奇的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D16")

    SetScenarioFlags(0x95, 3)
    Jump("loc_11D35")

    label("loc_11D1E")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_11D35")

    TalkEnd(0xFF)
    Return()

    # Function_49_117DC end

    SaveToFile()

Try(main)
