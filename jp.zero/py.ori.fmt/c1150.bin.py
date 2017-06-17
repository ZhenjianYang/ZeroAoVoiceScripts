from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "受付嬢レベッカ",         # 1
        "受付嬢フラン",           # 2
        "ドノバン警部",           # 3
        "レイモンド捜査官",       # 4
        "フランツ巡査",           # 5
        "警官",                   # 6
        "ジョーリッジ課長",       # 7
        "ケイト巡査",             # 8
        "エマ捜査官",             # 9
        "セルゲイ課長",           # 10
        "ピエール副局長",         # 11
        "警官",                   # 12
        "警官",                   # 13
        "警官",                   # 14
        "イス",                   # 15
        "イス",                   # 16
        "イス",                   # 17
        "イス",                   # 18
        "イス",                   # 19
        "イス",                   # 20
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
        "Function_7_164D",         # 07, 7
        "Function_8_3501",         # 08, 8
        "Function_9_3505",         # 09, 9
        "Function_10_62A7",        # 0A, 10
        "Function_11_6785",        # 0B, 11
        "Function_12_6AD6",        # 0C, 12
        "Function_13_7AE1",        # 0D, 13
        "Function_14_886C",        # 0E, 14
        "Function_15_899E",        # 0F, 15
        "Function_16_8BD2",        # 10, 16
        "Function_17_8D34",        # 11, 17
        "Function_18_8F82",        # 12, 18
        "Function_19_98B4",        # 13, 19
        "Function_20_9AFC",        # 14, 20
        "Function_21_A241",        # 15, 21
        "Function_22_A6E6",        # 16, 22
        "Function_23_A816",        # 17, 23
        "Function_24_A96B",        # 18, 24
        "Function_25_AAB1",        # 19, 25
        "Function_26_AC16",        # 1A, 26
        "Function_27_AD4E",        # 1B, 27
        "Function_28_AF55",        # 1C, 28
        "Function_29_B9A9",        # 1D, 29
        "Function_30_C6BC",        # 1E, 30
        "Function_31_C70F",        # 1F, 31
        "Function_32_C79A",        # 20, 32
        "Function_33_D746",        # 21, 33
        "Function_34_D8FB",        # 22, 34
        "Function_35_F600",        # 23, 35
        "Function_36_F610",        # 24, 36
        "Function_37_F64D",        # 25, 37
        "Function_38_F697",        # 26, 38
        "Function_39_F6E2",        # 27, 39
        "Function_40_F798",        # 28, 40
        "Function_41_10D5E",       # 29, 41
        "Function_42_10E34",       # 2A, 42
        "Function_43_10EDF",       # 2B, 43
        "Function_44_11C9D",       # 2C, 44
        "Function_45_12364",       # 2D, 45
        "Function_46_13390",       # 2E, 46
        "Function_47_13432",       # 2F, 47
        "Function_48_134D2",       # 30, 48
        "Function_49_13DB1",       # 31, 49
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_101C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_F05")

    #C0001
    ChrTalk(
        0x8,
        "ふふ、お疲れさまです。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "追加の支援要請は\x01",
            "改めて確認されましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        "#0100Fええ、大丈夫です。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0000F早速、手配魔獣の方に\x01",
            "当たってみるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "そうですか……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "手配魔獣はジオフロントＡ区画、\x01",
            "終点付近にいると思われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "それ以外の魔獣の群れも\x01",
            "再び発生しているので\x01",
            "くれぐれも気をつけてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 1)
    Jump("loc_F90")

    label("loc_F05")


    #C0008
    ChrTalk(
        0x8,
        (
            "これを持ちまして\x01",
            "【支援要請の補足説明】を\x01",
            "“達成済み”とさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "一度、支援課に戻って\x01",
            "端末から報告してみてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F90")


    #C0010
    ChrTalk(
        0x8,
        (
            "それと……支援要請の流れについては\x01",
            "本日中なら説明させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "もし確認したい事があれば\x01",
            "遠慮なく聞いてくださいね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4B, 0)
    Jump("loc_1370")

    label("loc_101C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1370")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1062")

    #C0012
    ChrTalk(
        0x8,
        (
            "手配魔獣の討伐、\x01",
            "お疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1062")


    #C0013
    ChrTalk(
        0x8,
        (
            "そうそう、ご存知ですか？\x01",
            "現在クロスベル警察では\x01",
            "魔獣の情報調査を行っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0005F情報調査……ですか？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "ええ、戦闘手帳には\x01",
            "魔獣についての項目があるのは\x01",
            "ご存知だと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "戦ったことのある魔獣は\x01",
            "戦闘手帳に記述されていくんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "もし情報がある程度溜まったら、\x01",
            "私の方に見せてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "皆さんの集めた情報を元に\x01",
            "署内で安全対策に\x01",
            "役立たせてもらいますから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_123C")

    #C0019
    ChrTalk(
        0x102,
        (
            "#0100Fなるほど……警察も\x01",
            "色々な工夫をしているんですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D9")

    label("loc_123C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1290")

    #C0020
    ChrTalk(
        0x103,
        (
            "#0200Fなるほど……警察も\x01",
            "色々な工夫をしているようですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D9")

    label("loc_1290")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12D9")

    #C0021
    ChrTalk(
        0x104,
        (
            "#0300Fなるほど……警察も\x01",
            "色々な工夫をしてるんスね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D9")


    #C0022
    ChrTalk(
        0x8,
        (
            "ええ、これも市民の安全を\x01",
            "守るためですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "魔獣の情報を見せていただく際には\x01",
            "多少の手当ても支給しますよ。\x01",
            "気軽に立ち寄ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 2)
    SetScenarioFlags(0x2, 0)

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1467")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1384")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1462")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                      # 0
            "支援要請について質問する\x01",      # 1
            "やめる\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_13FA")

    label("loc_13F3")

    OP_60(0x0)
    OP_5A()
    Sleep(150)

    label("loc_13FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Call(0, 44)
    Sleep(150)
    Jump("loc_145D")

    label("loc_142D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1441")
    Jump("loc_145D")

    label("loc_1441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_145D")

    Jump("loc_1384")

    label("loc_1462")

    Jump("loc_1649")

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1593")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_147B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                      # 0
            "支援要請について質問する\x01",      # 1
            "戦闘手帳を見せる\x01",              # 2
            "やめる\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_1502")

    label("loc_14FB")

    OP_60(0x0)
    OP_5A()
    Sleep(150)

    label("loc_1502")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1535")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Call(0, 44)
    Sleep(150)
    Jump("loc_1589")

    label("loc_1535")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1559")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 1)
    Call(0, 45)
    Jump("loc_1589")

    label("loc_1559")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156D")
    Jump("loc_1589")

    label("loc_156D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1589")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_1589")

    Jump("loc_147B")

    label("loc_158E")

    Jump("loc_1649")

    label("loc_1593")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_159D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1649")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "戦闘手帳を見せる\x01",      # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1614")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 1)
    Call(0, 45)
    Jump("loc_1644")

    label("loc_1614")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1628")
    Jump("loc_1644")

    label("loc_1628")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1644")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_1644")

    Jump("loc_159D")

    label("loc_1649")

    TalkEnd(0x8)
    Return()

    # Function_6_D7B end

    def Function_7_164D(): pass

    label("Function_7_164D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1718")

    #C0024
    ChrTalk(
        0x8,
        (
            "魔獣の情報がある程度溜まったら\x01",
            "私の方に見せてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "皆さんの集めた情報を元に\x01",
            "安全対策に役立たせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "多少の手当ても支給しますから\x01",
            "気軽に立ち寄ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3500")

    label("loc_1718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1831")

    #C0027
    ChrTalk(
        0x8,
        (
            "先ほど、ダドリーさんが\x01",
            "本部にお戻りになりましたけど\x01",
            "難しい顔をされていましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "どうやら上層部の動きも含めて\x01",
            "難しい状況になっているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "……皆さんもどうか、\x01",
            "くれぐれも気をつけてください。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182C")

    #C0030
    ChrTalk(
        0x101,
        "#0000Fはい……！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#0300F了解ッス！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_182C")

    Jump("loc_3500")

    label("loc_1831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1A7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A18")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x8,
        (
            "あら……\x01",
            "これは珍しい顔触れですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0000Fええ、まあ……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x10A,
        (
            "#0603F少々事情があってな。\x02\x03",

            "#0600Fそうだ、レベッカ君。\x01",
            "空港封鎖の件については……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "ええ、先ほど\x01",
            "エマさんから伺いました。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "本来ならもう少し早く\x01",
            "事情をを伺いたい所でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "まあ、お急ぎのようなので\x01",
            "嫌味はこのくらいにします。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x10A,
        "#0603F……感謝する。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0000F（ダドリーさんが\x01",
            "  微妙に押されてる……）\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#0100F（珍しい所を\x01",
            "  見てしまったわね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A7A")

    label("loc_1A18")


    #C0041
    ChrTalk(
        0x8,
        (
            "空港封鎖の対応については\x01",
            "こちらの方にお任せを。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "皆さんはどうか\x01",
            "任務に専念してください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7A")

    Jump("loc_3500")

    label("loc_1A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9A")
    Call(0, 11)
    Jump("loc_1B17")

    label("loc_1A9A")


    #C0043
    ChrTalk(
        0x8,
        (
            "しかもどうやら\x01",
            "今回は捜査二課の方にも\x01",
            "声が掛けられたみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "いつも秘密主義の一課が\x01",
            "珍しい事もあるものですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B17")

    Jump("loc_3500")

    label("loc_1B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1BDB")

    #C0045
    ChrTalk(
        0x8,
        (
            "港湾区での銃撃戦について\x01",
            "問い合わせが何件かありました。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "いずれマスコミが報道したら\x01",
            "更に問い合わせが殺到しそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "今のうちに対策を\x01",
            "考える必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3500")

    label("loc_1BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF7")

    #C0048
    ChrTalk(
        0x8,
        "あら、皆さん……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "《黒月》の事務所の襲撃を受けて\x01",
            "捜査一課は本格的に\x01",
            "動いているみたいですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "今朝から全員、\x01",
            "出払ってしまっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#0005Fそ、そうですか。\x01",
            "さすがに行動が早いな……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#0306Fやっぱこの手の捜査は\x01",
            "一課の独壇場なのかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D9C")

    label("loc_1CF7")


    #C0053
    ChrTalk(
        0x8,
        (
            "捜査一課は本格的に\x01",
            "動いているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "早朝に捜査会議があって、\x01",
            "全員出払ってしまったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0001F（さすが一課……\x01",
            "  やることにソツがないな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9C")

    Jump("loc_3500")

    label("loc_1DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_20CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E42")

    #C0056
    ChrTalk(
        0x8,
        (
            "フランが時間通り戻ってきて\x01",
            "ちょっとつまらない思いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "外国人の男の人と\x01",
            "もっと楽しんできてくれれば\x01",
            "面白かったんですけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C7")

    label("loc_1E42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1ED5")

    #C0058
    ChrTalk(
        0x8,
        (
            "ふふ……聞いている限りでは\x01",
            "なんだか楽しそうなお話でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "フランは間違いなく\x01",
            "休憩に行かせますから\x01",
            "ご安心くださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C7")

    label("loc_1ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2053")

    #C0060
    ChrTalk(
        0x8,
        "皆さん、お疲れさまです。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "実は最近、少しずつですが\x01",
            "警察に相談に来る市民の方々が\x01",
            "増えてきているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "ふふ、これも皆さん\x01",
            "特務支援課の活動のお陰かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0000Fはは……だとしたら\x01",
            "俺たちも嬉しいんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        "ええ、きっとそうだと思います。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "ふふっ……\x01",
            "今後の活躍にも期待していますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#0309F（レベッカさん……\x01",
            "  ありがたいお言葉ッス！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20C7")

    label("loc_2053")


    #C0067
    ChrTalk(
        0x8,
        (
            "最近、少しずつですが\x01",
            "警察に相談に来る市民の方々が\x01",
            "増えてきているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        "ふふ、これも皆さんのお陰かしら。\x02",
    )

    CloseMessageWindow()

    label("loc_20C7")

    Jump("loc_3500")

    label("loc_20CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_24DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2318")

    #C0069
    ChrTalk(
        0x8,
        "あら皆さん、お久し振りです。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x153,
        (
            "#1105Fわっ、おねーさんキレー！\x02\x03",

            "#1111Fんーと、何ていうんだっけ。\x01",
            "ビジンさん？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 500)

    #C0071
    ChrTalk(
        0x8,
        "あら……ふふ、お上手ですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0072
    ChrTalk(
        0x8,
        (
            "噂通り、とっても\x01",
            "可愛らしいお嬢さんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#0000Fはは……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "……ルバーチェ商会からは非公式に\x01",
            "“手打ち”の打診が来ています。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "ですが皆さん、念のため\x01",
            "外出の際は気を付けてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#0000Fはい、分かりました。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_22AE")

    #C0077
    ChrTalk(
        0x102,
        "#0101F十分に注意します。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2310")

    label("loc_22AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_22D2")

    #C0078
    ChrTalk(
        0x103,
        "#0200F了解です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2310")

    label("loc_22D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2310")

    #C0079
    ChrTalk(
        0x104,
        (
            "#0300F俺たちが護衛についてるんで\x01",
            "大丈夫ッスよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2310")

    SetScenarioFlags(0xB1, 1)
    Jump("loc_24D5")

    label("loc_2318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2403")

    #C0080
    ChrTalk(
        0x8,
        (
            "そういえば、今日は\x01",
            "ジオフロントのＡ２区画に\x01",
            "手配魔獣が出ているようですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "導力端末がメンテナンス中なので\x01",
            "情報を送れなかったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "危険な魔獣らしいので、\x01",
            "皆さんも気に留めておいてくださいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x25, 0x4, 0x2)
    SetScenarioFlags(0x0, 0)
    Jump("loc_24D5")

    label("loc_2403")


    #C0083
    ChrTalk(
        0x8,
        (
            "今日は導力端末がメンテナンス中なので\x01",
            "フランもお休みを取っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "記念祭からずっと休みなしで\x01",
            "働いてもらっていましたから……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "ふふ、今日一日はゆっくりと\x01",
            "リフレッシュしてもらいたいですね。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)

    label("loc_24D5")

    Jump("loc_3500")

    label("loc_24DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_259A")

    #C0086
    ChrTalk(
        0x8,
        (
            "今日は記念祭関連の対策会議が\x01",
            "３件も入っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "記念祭中の市内巡回や\x01",
            "式場の警備体制……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "特に開会式には\x01",
            "各国のＶＩＰも出席なさるので\x01",
            "とても気を遣うんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3500")

    label("loc_259A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_26DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2663")

    #C0089
    ChrTalk(
        0x8,
        (
            "捜査一課は秘密主義が\x01",
            "徹底しているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "どんな捜査をしているのか\x01",
            "滅多に明かしてくれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "それも……\x01",
            "扱っている事件を考えると\x01",
            "仕方のない事なのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26D9")

    label("loc_2663")


    #C0092
    ChrTalk(
        0x8,
        (
            "捜査一課は秘密主義が\x01",
            "徹底しているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "冷徹に見えるかもしれませんが、\x01",
            "きっと仕方のない事なのでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D9")

    Jump("loc_3500")

    label("loc_26DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_27FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2794")

    #C0094
    ChrTalk(
        0x8,
        (
            "記念祭が近いので\x01",
            "受付の業務も増えているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "露店の出店許可から\x01",
            "それぞれの街区の\x01",
            "飾り付けや催し物の申請……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        "今年も忙しくなりそうですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27F8")

    label("loc_2794")


    #C0097
    ChrTalk(
        0x8,
        (
            "記念祭が近いので\x01",
            "受付の業務も増えているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "毎年この季節だけは\x01",
            "忙しくなるんですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F8")

    Jump("loc_3500")

    label("loc_27FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2996")

    #C0099
    ChrTalk(
        0x8,
        "あら、エリィさんにティオさん。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "先ほどはお手伝い\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#0200Fあんな感じで\x01",
            "良かったでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0100F過去の事件にも目を通せて\x01",
            "とても勉強になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        "ふふ、それは良かったです。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "警察にも導力端末が\x01",
            "置かれるようになって、徐々に\x01",
            "データベース化も進めているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "また手をお借りするかもしれません。\x01",
            "その時はよろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A53")

    label("loc_2996")


    #C0106
    ChrTalk(
        0x8,
        (
            "警察にも導力端末が\x01",
            "置かれるようになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "少しずつ過去の事件も\x01",
            "データベース化も進めているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "また手をお借りするかもしれませんが、\x01",
            "その時はよろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A53")

    Jump("loc_3500")

    label("loc_2A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6C")

    #C0109
    ChrTalk(
        0x8,
        (
            "捜査二課のレイモンドさんって\x01",
            "面白い方ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "毎朝、ここに必ず立ち寄っては\x01",
            "話をされて行かれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "ふふ、今朝は長居をしすぎて\x01",
            "ドノバン警部に連れて行かれて\x01",
            "しまいましたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#0000F（レベッカさんは\x01",
            "  やっぱり人気あるんだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BD8")

    label("loc_2B6C")


    #C0113
    ChrTalk(
        0x8,
        (
            "二課のレイモンドさんって\x01",
            "面白い方ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "毎朝、ここに必ず立ち寄っては\x01",
            "話をされて行かれるんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD8")

    Jump("loc_3500")

    label("loc_2BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2DA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D36")

    #C0115
    ChrTalk(
        0x8,
        (
            "警察本部では、今週を\x01",
            "防犯強化週間と定めています。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "みなさん、戸締りは\x01",
            "十分に確認してくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0003F防犯強化週間……\x01",
            "そんなのがあったんですか。\x02",
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
            "うーん、やっぱり\x01",
            "皆さんも知りませんでしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "上の人たちも、もう少し市民への告知に\x01",
            "予算を割いてくれるといいんですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2DA4")

    label("loc_2D36")


    #C0120
    ChrTalk(
        0x8,
        (
            "警察本部では、今週を\x01",
            "防犯強化週間と定めています。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "市民の皆さんには\x01",
            "戸締りに気を付けて欲しいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA4")

    Jump("loc_3500")

    label("loc_2DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB2")

    #C0122
    ChrTalk(
        0x8,
        (
            "ソーニャ副司令が\x01",
            "いらっしゃっていたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "副司令は警備隊の方ですけど\x01",
            "時々顔を出してくださるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#0005Fそういえば、警察と警備隊って\x01",
            "あまり接点が無いですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "ええ……建前上は同じ\x01",
            "『自治州警察』なんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "警備隊はその性格上、\x01",
            "軍隊と似た運用をされているので\x01",
            "独自の指揮系統があるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "警察本部には局長、警備隊には司令と\x01",
            "同格のトップも別々にいますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#0303Fま、ほとんど別の組織ッスよね。\x02\x03",

            "#0300Fたまに俺みたいに\x01",
            "異動する奴もいるみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3063")

    label("loc_2FB2")


    #C0129
    ChrTalk(
        0x8,
        (
            "警察本部と警備隊は\x01",
            "建前上は一つの組織ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "トップも別々ですし、\x01",
            "ほとんど別組織と言えますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "唯一顔を出してくださるのは\x01",
            "ソーニャ副司令くらいかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3063")

    Jump("loc_3500")

    label("loc_3068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_30CF")

    #C0132
    ChrTalk(
        0x8,
        (
            "どうやら旧市街の方で\x01",
            "騒動が起きているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        "皆さん、どうかお気をつけて。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3500")

    label("loc_30CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3500")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_31FC")

    #C0134
    ChrTalk(
        0x8,
        (
            "どうやらジオフロントの\x01",
            "手配魔獣を退治されたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "今回のような手配魔獣の情報は\x01",
            "遊撃士協会にも回っているので\x01",
            "必ずしも倒す必要はありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        (
            "実際、かなり手強いので\x01",
            "一筋縄では行かないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "ですが余裕があったら是非、\x01",
            "チャレンジしてみてください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3500")

    label("loc_31FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_33FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3361")

    #C0138
    ChrTalk(
        0x8,
        "ふふ、お疲れさまです。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "追加の支援要請は\x01",
            "改めて確認されましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        "#0100Fええ、大丈夫です。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000F早速、手配魔獣の方に\x01",
            "当たってみるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        "そうですか……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "手配魔獣はジオフロントＡ区画、\x01",
            "終点付近にいると思われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "それ以外の魔獣の群れも\x01",
            "再び発生しているので\x01",
            "くれぐれも気をつけてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 1)
    Jump("loc_33F8")

    label("loc_3361")


    #C0145
    ChrTalk(
        0x8,
        (
            "手配魔獣はジオフロントＡ区画、\x01",
            "終点付近にいると思われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "それ以外の魔獣の群れも\x01",
            "再び発生しているようなので\x01",
            "くれぐれも気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F8")

    Jump("loc_3500")

    label("loc_33FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3500")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0147
    ChrTalk(
        0x8,
        (
            "これを持ちまして\x01",
            "【支援要請の補足説明】を\x01",
            "“達成済み”とさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        (
            "一度、支援課に戻って\x01",
            "端末から報告してみてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "#1900Fえへへ、わたしが出て\x01",
            "応対させてもらいますねー。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_3500")

    label("loc_3500")

    Return()

    # Function_7_164D end

    def Function_8_3501(): pass

    label("Function_8_3501")

    Call(0, 9)
    Return()

    # Function_8_3501 end

    def Function_9_3505(): pass

    label("Function_9_3505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3517")
    Call(0, 34)
    Return()

    label("loc_3517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3531")
    Call(0, 43)
    Return()

    label("loc_3531")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_383A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B8")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0150
    ChrTalk(
        0x9,
        (
            "#1905Fあれ……皆さんは\x01",
            "これからお出掛けですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0300Fおお、ちょっと\x01",
            "ウルスラ病院の方までな。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#0200Fフランさんの方は\x01",
            "少しお疲れのようですけど\x01",
            "大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "#1900Fあ、えへへ……\x02\x03",

            "さっきまで空港封鎖についての\x01",
            "問い合わせに追われてまして。\x02\x03",

            "#1903F爆破予告だったみたいですけど\x01",
            "ウソだったみたいで安心しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        "#0002Fそっか……お疲れさま。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "#1909Fふふっ、少し休憩したから\x01",
            "まだまだ頑張りますよ～。\x02\x03",

            "#1900Fもし何かあれば\x01",
            "こちらに連絡をくださいね？\x02\x03",

            "このフラン・シーカー、\x01",
            "皆さんのバックアップなら\x01",
            "バッチリ務めさせて頂きますから～。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        "#0100Fふふ、よろしくお願いするわね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 6)
    Jump("loc_3835")

    label("loc_37B8")


    #C0157
    ChrTalk(
        0x9,
        (
            "#1900Fウルスラ病院なら\x01",
            "導力バスですぐですもんね。\x02\x03",

            "心配ないと思いますけど、\x01",
            "もし何かあれば\x01",
            "こちらに連絡をくださいね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3835")

    Jump("loc_62A3")

    label("loc_383A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_398F")
    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フランが通信器でやり取りをしている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0159
    ChrTalk(
        0x9,
        (
            "#1901Fはい、はい……\x02\x03",

            "#1903F……申しわけありません。\x01",
            "封鎖は一時的なものでして。\x02\x03",

            "#1901Fあと一時間もすれば\x01",
            "解除される見込みかと……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_398A")

    #C0160
    ChrTalk(
        0x101,
        (
            "#0000F（空港封鎖の一件での\x01",
            "  各方面への対応かな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0100F（ええ、忙しそうだし、\x01",
            "  邪魔しない方がいいわね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_398A")

    Jump("loc_62A3")

    label("loc_398F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39AA")
    Call(0, 11)
    Jump("loc_3A1C")

    label("loc_39AA")


    #C0162
    ChrTalk(
        0x9,
        (
            "#1901F一時的とはいえ、\x01",
            "空港を封鎖するなんて……\x02\x03",

            "#1903Fうーん、昨日の襲撃事件もあるし\x01",
            "何だか心配ですねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A1C")

    Jump("loc_62A3")

    label("loc_3A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3B3E")

    #C0163
    ChrTalk(
        0x9,
        (
            "#1900Fあ、皆さん。\x01",
            "お疲れさまです～。\x02\x03",

            "《黒月》襲撃の事件については\x01",
            "あまり続報は入っていませんね。\x02\x03",

            "#1903F何とか大事#4Rおおごと#にならずに\x01",
            "収まって欲しいんですけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B39")

    #C0164
    ChrTalk(
        0x101,
        "#0003Fそうだな……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#0100F今のところ、そちらは一課に\x01",
            "任せるしかなさそうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3B39")

    Jump("loc_62A3")

    label("loc_3B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3C8D")
    TurnDirection(0x9, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C35")

    #C0166
    ChrTalk(
        0x9,
        (
            "#1905Fええ～っ、銃撃戦ですか～？\x02\x03",

            "そんな物騒な……\x01",
            "一体何があったんですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        (
            "#0200F（フランさんは\x01",
            "  今聞いた所みたいですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0003F（やっぱり捜査一課の管轄だと\x01",
            "  情報が流れにくいみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C88")

    label("loc_3C35")


    #C0169
    ChrTalk(
        0x9,
        (
            "#1905Fぶ、物騒な事件ですね……\x02\x03",

            "#1901Fわたし……\x01",
            "なんだか腹が立ってきました！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C88")

    Jump("loc_62A3")

    label("loc_3C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3EB1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D2E")

    #C0170
    ChrTalk(
        0x9,
        (
            "#1900Fアントンさんって、\x01",
            "もう帰っちゃったんでしょうかね？\x02\x03",

            "#1903F楽しく食事をさせてもらった\x01",
            "お礼を言い損ねちゃいました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF4")

    label("loc_3D2E")


    #C0171
    ChrTalk(
        0x9,
        (
            "#1900Fおかげさまでアントンさんと\x01",
            "楽しくお食事できました。\x02\x03",

            "#1909F皆さん、お姉ちゃん。\x01",
            "色々とありがとうございました～。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#0006F（恋する男をフッたのには\x01",
            "  全然気づいてないんだろうな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3DF4")

    Jump("loc_3EAC")

    label("loc_3DF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3E94")

    #C0173
    ChrTalk(
        0x9,
        (
            "#1900Fあと少ししたら、中央広場の\x01",
            "レストラン《ヴァンセット》\x01",
            "に向かいますね。\x02\x03",

            "#1909Fアントンさんにも\x01",
            "よろしく言っておいて下さい～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAC")

    label("loc_3E94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3EA9")
    Call(0, 32)
    Jump("loc_3EAC")

    label("loc_3EA9")

    Call(0, 10)

    label("loc_3EAC")

    Jump("loc_62A3")

    label("loc_3EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3EBF")
    Jump("loc_62A3")

    label("loc_3EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_END)), "loc_4132")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CC")

    #C0174
    ChrTalk(
        0x9,
        (
            "#1900Fあれ、皆さん……\x01",
            "何だかお急ぎみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        "#0000Fああ、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フランに捜査状況を説明し、\x01",
            "《星見の塔》の前で\x01",
            "ノエルと会ったことを話した。\x07\x00\x02",
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
            "#1905Fそ、そんな事が……\x02\x03",

            "それじゃあお姉ちゃんは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        (
            "#0301Fああ、今は塔の前で\x01",
            "俺たちを待ってくれている。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x102,
        (
            "#0100F私たちも準備を済ませたら\x01",
            "戻って合流するつもりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "#1903Fそうですか……\x02\x03",

            "#1901F……皆さん、どうかお気をつけて。\x02\x03",

            "それとお姉ちゃんのこと、\x01",
            "くれぐれも宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 6)
    Jump("loc_412D")

    label("loc_40CC")


    #C0181
    ChrTalk(
        0x9,
        (
            "#1901F皆さん、どうかお気をつけて。\x02\x03",

            "それとお姉ちゃんのこと、\x01",
            "くれぐれも宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_412D")

    Jump("loc_62A3")

    label("loc_4132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_429A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4217")

    #C0182
    ChrTalk(
        0x9,
        (
            "#1900Fアルカンシェルの新作公演は\x01",
            "記念祭の初日に初上演されるんです。\x02\x03",

            "ただでさえ人気なのに、\x01",
            "記念祭に合わせるなんて\x01",
            "凄いことになりそうですよね。\x02\x03",

            "#1906Fはあ、わたしもお姉ちゃんと\x01",
            "見に行きたいな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4295")

    label("loc_4217")


    #C0183
    ChrTalk(
        0x9,
        (
            "#1900Fアルカンシェルの新作公演、\x01",
            "今年は凄いことになりそうですよね。\x02\x03",

            "#1906Fはあ、わたしもお姉ちゃんと\x01",
            "見に行きたいな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4295")

    Jump("loc_62A3")

    label("loc_429A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C2")
    OP_93(0x9, 0x5A, 0x0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    #C0184
    ChrTalk(
        0x9,
        (
            "#1905Fあっ、皆さん……！\x02\x03",

            "#1903Fそのう、残念でしたね……\x01",
            "一課に事件を取られちゃうなんて……\x02\x03",

            "#1900F皆さんをサポートする身として\x01",
            "わたしも何だか悔しいです……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#0012Fいや、フランが\x01",
            "落ち込むことないって。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        (
            "#0100Fフランさん、ありがとう。\x01",
            "私達の方は平気よ。\x02\x03",

            "もう気持ちも\x01",
            "切り替えられたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        (
            "#0200Fまた支援要請があれば\x01",
            "回しておいてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "#1903Fはい……そうですね。\x02\x03",

            "#1900Fえへへ、すみません。\x02\x03",

            "#1901Fオペレーター、フラン。\x01",
            "気持ちを切り替えて\x01",
            "頑張らせていただきます！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 6)
    Jump("loc_458D")

    label("loc_44C2")


    #C0189
    ChrTalk(
        0x9,
        (
            "#1900F一課の人って、受付前を通っても\x01",
            "挨拶もロクにしてくれなくて……\x02\x03",

            "#1903F忙しいのは分かるんですけど\x01",
            "ちょっと寂しいんですよね～。\x02\x03",

            "#1903F同じ警察の仲間なんですから\x01",
            "もっと打ち解けたいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458D")

    Jump("loc_62A3")

    label("loc_4592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4891")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_481E")
    OP_93(0x9, 0x5A, 0x0)

    #C0190
    ChrTalk(
        0x9,
        (
            "#1906Fうーん、導力ネットを通じた\x01",
            "受付の仕事も増えてきたなぁ～。\x02\x03",

            "#1900F記念祭も近いし\x01",
            "わたしも頑張らないと～……\x02",
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
            "#1905Fあ、皆さん～。\x02\x03",

            "#1900Fどうでした、\x01",
            "さっきの依頼者の方は。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_END)), "loc_4762")

    #C0192
    ChrTalk(
        0x101,
        (
            "#0003Fああ、その……色々あって。\x02\x03",

            "#0000Fこれから報告に向かう所なんだ。\x02",
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
            "#1905Fよく分かりませんけど……\x02\x03",

            "#1901F捜査の方、頑張ってくださいね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4816")

    label("loc_4762")


    #C0195
    ChrTalk(
        0x101,
        (
            "#0000Fああ、引き受けることにしたよ。\x02\x03",

            "#0001F難しそうな事件だけど……\x01",
            "さすがに見過ごせないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "#1900Fふふ、よかった～。\x02\x03",

            "#1901Fそれじゃ捜査の方、\x01",
            "頑張ってくださいね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4816")

    SetScenarioFlags(0x0, 1)
    Jump("loc_488C")

    label("loc_481E")


    #C0197
    ChrTalk(
        0x9,
        (
            "#1900F最近、導力ネットを通じた\x01",
            "受付の仕事が増えてるんです。\x02\x03",

            "記念祭も近いですし\x01",
            "わたしも頑張らないと～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_488C")

    Jump("loc_62A3")

    label("loc_4891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_END)), "loc_49F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_497D")

    #C0198
    ChrTalk(
        0x9,
        (
            "#1900Fあ、皆さん。\x01",
            "依頼者からの話は聞けました～？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        (
            "#0304Fああ……\x01",
            "とにかくデカかったぜ。\x02",
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
        "#0006Fランディ……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x103,
        "#0203Fやれやれです。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#0111Fはあ……\x01",
            "もう少し自重して頂戴。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_49F1")

    label("loc_497D")


    #C0204
    ChrTalk(
        0x9,
        (
            "#1903Fよく分かりませんけど\x01",
            "ちょっと深刻そうな感じでした。\x02\x03",

            "#1900F皆さん、どうか\x01",
            "力になってあげてくださいね～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49F1")

    Jump("loc_62A3")

    label("loc_49F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_END)), "loc_4C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA6")

    #C0205
    ChrTalk(
        0x9,
        (
            "#1900Fあ、皆さん！\x02\x03",

            "依頼者の方は\x01",
            "可愛い娘さんでしたよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        "#0301Fよしロイド、全力で帰還だな！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A96")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4A96")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ABC")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4ABC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AE2")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4AE2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B08")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4B08")

    Sleep(1000)

    #C0207
    ChrTalk(
        0x9,
        (
            "#1903Fえっと……\x02\x03",

            "#1901Fちょっと深刻そうな\x01",
            "感じだったので、直接支援課に\x01",
            "向かってもらっています。\x02\x03",

            "#1900Fなるべく早く\x01",
            "行ってあげて下さいね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4C11")

    label("loc_4BA6")


    #C0208
    ChrTalk(
        0x9,
        (
            "#1900F依頼者の方には\x01",
            "直接支援課に向かうように\x01",
            "伝えてあります。\x02\x03",

            "なるべく早く\x01",
            "行ってあげて下さいね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C11")

    Jump("loc_62A3")

    label("loc_4C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E09")

    #C0209
    ChrTalk(
        0x9,
        (
            "#1906Fあ、皆さん！\x01",
            "ちょっと聞いてくださいよ～。\x02\x03",

            "#1901F先日、捜査一課専用の\x01",
            "すごいオペレーションルームが\x01",
            "地下に設置されたんです！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#0000Fへえ、そうなんだ。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x9,
        (
            "#1903Fええ、そりゃもう\x01",
            "すごい部屋でして。\x02\x03",

            "専属のオペレーターが\x01",
            "３人も付いているんです。\x02\x03",

            "#1901Fくうぅ……くやしいなぁ。\x01",
            "わたしだって負けてないのに～！\x02",
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
            "#0303Fそりゃまあ……\x01",
            "うちと捜査一課じゃなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4ECE")

    label("loc_4E09")


    #C0213
    ChrTalk(
        0x9,
        (
            "#1903F先日、捜査一課専用の\x01",
            "すごいオペレーションルームが\x01",
            "地下に設置されたんです。\x02\x03",

            "#1901Fくぅ、わたしも負けていられません。\x01",
            "全力で皆さんをサポートします！\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#0000Fはは、今後ともよろしくな。\x02",
    )

    CloseMessageWindow()

    label("loc_4ECE")

    Jump("loc_62A3")

    label("loc_4ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_523C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C3")

    #C0215
    ChrTalk(
        0x9,
        "#1909Fえへへ……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#0300Fお、フランちゃん。\x01",
            "なんだか嬉しそうだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x9,
        (
            "#1900Fあ、皆さん～。\x01",
            "よくぞ聞いてくれましたっ！\x02\x03",

            "#1909Fさっきお姉ちゃんが来て、\x01",
            "顔を出してくれたんですよ～！\x02\x03",

            "#1900F昨日も来てたらしいんですけど\x01",
            "すれ違っちゃったみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0000Fああ、確かノエル曹長……\x01",
            "だったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#0100F私たちも先ほど改めて\x01",
            "自己紹介をしてもらったわ。\x02\x03",

            "はきはきとして、\x01",
            "とても礼儀正しい方みたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#0200Fフランさんとはあまり\x01",
            "性格は似てなさそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "#1900Fえへへ、そうなんですよ。\x02\x03",

            "#1903Fお姉ちゃんって\x01",
            "凛としてて格好よくって\x01",
            "それでいて可愛くって……\x02\x03",

            "#1900Fわたし小さい頃から\x01",
            "ずっと憧れてるんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#0000Fはは、自慢の\x01",
            "お姉さんみたいだね。\x02\x03",

            "#0008F（……兄弟、か……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 6)
    Jump("loc_5237")

    label("loc_51C3")


    #C0223
    ChrTalk(
        0x9,
        (
            "#1900Fロイドさんたちは今日は\x01",
            "マインツに行くんですよね？\x02\x03",

            "お姉ちゃんも期待してましたし\x01",
            "どうか頑張ってください！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5237")

    Jump("loc_62A3")

    label("loc_523C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_572C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5610")
    OP_4B(0x8, 0xFF)

    #C0224
    ChrTalk(
        0x9,
        (
            "#1900F皆さん、お疲れさまです。\x02\x03",

            "アルモリカ村の調査は\x01",
            "いかがでしたか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#0006Fうーん、今のところは何も。\x01",
            "警備隊の調書以上の事は\x01",
            "分からないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x9,
        "#1903F残念、そうでしたか～……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0227
    ChrTalk(
        0x9,
        (
            "#1900Fそういえば今回の一件って\x01",
            "警備隊も調査したんですよね。\x02\x03",

            "お姉ちゃんも出動したのかなー？\x02",
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
            "ふふ……フランは警備隊に\x01",
            "自慢のお姉さんがいるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "毎日のように\x01",
            "自慢話をしてるんですよ。\x02",
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
            "#1906Fも、もうレベッカさんたら……\x02\x03",

            "それはお姉ちゃんが\x01",
            "あんまり連絡をくれないからで……\x02\x03",

            "#1900Fそれだけですよ～！\x01",
            "寂しいとか、そんなのじゃ\x01",
            "ないんですから～！\x02",
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
            "#0303F（警察本部って、あんま\x01",
            "  いい印象がないんだが……）\x02\x03",

            "#0300F（受付に来ると癒されるなぁ～㈱）\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        (
            "#0102F（２人に受付を任されている理由……\x01",
            "  何となく分かる気がするわ。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x6B, 5)
    Jump("loc_5727")

    label("loc_5610")


    #C0233
    ChrTalk(
        0x9,
        (
            "#1903Fおっほん、先ほどの\x01",
            "話は忘れてください。\x02\x03",

            "#1900Fわたしも警察官ですから\x01",
            "公私混同は慎まなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)

    #C0234
    ChrTalk(
        0x9,
        (
            "#1903F……はあ、お姉ちゃん。\x01",
            "今ごろ何してるんだろうな～……\x02",
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

    label("loc_5727")

    Jump("loc_62A3")

    label("loc_572C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5BEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B5B")
    OP_93(0x9, 0x5A, 0x0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    #C0235
    ChrTalk(
        0x9,
        (
            "#1905Fあ、皆さん、お話は聞きました。\x02\x03",

            "#1900F魔獣被害の調査で\x01",
            "市外に向かわれるんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#0000Fああ、これから\x01",
            "アルモリカ村に\x01",
            "行ってみるつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        (
            "#1901Fフラン・シーカー、\x01",
            "全力でサポートします！\x02\x03",

            "#1903F……と言いたい所ですが……\x02",
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
            "#1900Fえっと、導力通信が届くか\x01",
            "ちょっと心配でして。\x02\x03",

            "う～ん、どうだったかな～。\x01",
            "市内はバッチリなはずなんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        (
            "#0005Fそ、そうか。\x01",
            "もしかしてエニグマって\x01",
            "あまり離れると通信できないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x103,
        (
            "#0203F恐らくオペレーションシステム的には\x01",
            "市内での捜査のみが\x01",
            "想定されているのかと。\x02\x03",

            "#0200Fですが、理論的には\x01",
            "市外およそ２００セルジュ程度なら\x01",
            "導力波が届くはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#0100F２００セルジュ……\x01",
            "自治州内で人の住んでいる場所なら\x01",
            "ぎりぎり届く距離ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        (
            "#1900Fあ、じゃあ通信もできるんですね？\x01",
            "良かったぁ～。\x02\x03",

            "皆さん、もし何かあれば\x01",
            "フラン・シーカーにご連絡下さい！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#0000Fああ、了解。\x01",
            "そんなに心配しないでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x104,
        (
            "#0300Fま、ただ\x01",
            "調査に向かうだけだしな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5BEA")

    label("loc_5B5B")


    #C0245
    ChrTalk(
        0x9,
        (
            "#1900F良かった～、せっかく操作にも\x01",
            "慣れてきたので、\x01",
            "バックアップできないと残念ですし。\x02\x03",

            "皆さん、何かあれば\x01",
            "ぜひ本部に連絡して下さいね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BEA")

    Jump("loc_62A3")

    label("loc_5BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DBE")

    #C0246
    ChrTalk(
        0x9,
        (
            "#1900Fあ、皆さん。\x01",
            "どうもお疲れさまです～。\x02\x03",

            "何でも旧市街の不良さんたちの\x01",
            "ケンカを止めるつもりだとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#0000Fああ、何だか\x01",
            "そういう話になっちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x9,
        (
            "#1900Fそうですか……\x02\x03",

            "わたしの家、東通りにあるので\x01",
            "旧市街の不良さんたちを\x01",
            "たまに見かけるんですけど……\x02\x03",

            "#1903Fやっぱり徒党を組んでる所とか\x01",
            "ケンカ沙汰とかを見てると\x01",
            "ちょっと恐かったりしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0001Fそっか……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x102,
        (
            "#0101Fやっぱり何とかして\x01",
            "止めないといけないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5F34")

    label("loc_5DBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E7E")

    #C0251
    ChrTalk(
        0x9,
        (
            "#1900Fあ、そういえば、\x01",
            "《手配魔獣》の一件ですけど……\x02\x03",

            "お手数ですが、詳細の報告は\x01",
            "支援課の端末からお願いします。\x02\x03",

            "導力ネットワークの導入テストも\x01",
            "兼ねてますので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F34")

    label("loc_5E7E")


    #C0252
    ChrTalk(
        0x9,
        (
            "#1900Fわたしの家、東通りにあるので\x01",
            "旧市街の不良さんたちを\x01",
            "たまに見かけるんですけど……\x02\x03",

            "#1903Fやっぱり徒党を組んでる所とか\x01",
            "ケンカ沙汰とかを見てると\x01",
            "ちょっと恐かったりしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F34")

    Jump("loc_62A3")

    label("loc_5F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_62A3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_61A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_610F")

    #C0253
    ChrTalk(
        0x9,
        (
            "#1909Fえへへ、皆さん、\x01",
            "どうもお疲れさまでした。\x02\x03",

            "#1900Fわたし、ちゃんと\x01",
            "オペレーションできてましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#0000Fああ、全然問題なかったよ。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x102,
        "#0100Fこれからよろしくね、フランさん。\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "#1900Fはい、こちらこそ！\x02\x03",

            "#1903Fただ……\x01",
            "端末でのやり取りは記録されるので\x01",
            "世間話とかはしにくいんですよねぇ。\x02\x03",

            "#1900F皆さん、よかったらまた\x01",
            "こちらにいらしてくださいね～？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x104,
        "#0300Fおお、そりゃ喜んで。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        "#0000Fまた寄らせてもらうよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_619B")

    label("loc_610F")


    #C0259
    ChrTalk(
        0x9,
        (
            "#1903F端末でのやり取りは記録されるので\x01",
            "世間話とかはしにくいんですよねぇ。\x02\x03",

            "#1900F皆さん、よかったらまた\x01",
            "こちらにいらしてくださいね～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_619B")

    Jump("loc_62A3")

    label("loc_61A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_62A3")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0260
    ChrTalk(
        0x8,
        (
            "これを持ちまして\x01",
            "【支援要請の補足説明】を\x01",
            "“達成済み”とさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "一度、支援課に戻って\x01",
            "端末から報告してみてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x9,
        (
            "#1900Fえへへ、わたしが出て\x01",
            "応対させてもらいますねー。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_62A3")

    label("loc_62A3")

    TalkEnd(0x9)
    Return()

    # Function_9_3505 end

    def Function_10_62A7(): pass

    label("Function_10_62A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A6")
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
            "#1905Fあ、お姉ちゃん！\x02\x03",

            "ロイドさんたちに\x01",
            "話してみたんだね～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x109,
        "#0500Fうん、引き受けてくれるって。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x109, 500)

    #C0265
    ChrTalk(
        0x104,
        (
            "#0305Fなんだ、フランちゃんには\x01",
            "話してあったのか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x104, 500)

    #C0266
    ChrTalk(
        0x109,
        (
            "#0500Fあはは……\x01",
            "皆さんに話をする前に\x01",
            "一度フランに相談しまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x9,
        (
            "#1903Fでもユーレイなんて\x01",
            "本当にいるのかな～。\x02\x03",

            "#1900Fわたしはちょっと\x01",
            "信じられないかもー。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_64AE():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64AE)
    Sleep(50)

    def lambda_64BE():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_64BE)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0268
    ChrTalk(
        0x109,
        (
            "#0503Fもう、本当に見たんだってば。\x02\x03",

            "#0500F幽霊かどうかは判らないけど\x01",
            "そういう化物みたいなのを……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x9,
        "#1900Fえー、でもでもぉ～……\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#0006F……あの、２人とも。\x01",
            "エリィが本気で固まってるんだが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_65C4():
        TurnDirection(0x9, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_65C4)

    def lambda_65D1():
        TurnDirection(0x109, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_65D1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x109, 1)

    #C0271
    ChrTalk(
        0x109,
        "#0505Fあ、す、すみません！\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x9,
        (
            "#1900Fえへへ、ごめんなさい……\x01",
            "（エリィさんって、もしかして？）\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        (
            "#0109Fい、いえ、いいのよ。\x01",
            "このくらい大したことは……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 3000, 0, 13500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xCE, 4)
    EventEnd(0x5)
    Jump("loc_6784")

    label("loc_66A6")


    #C0274
    ChrTalk(
        0x9,
        (
            "#1900Fお姉ちゃんから話は聞いてますけど\x01",
            "ユーレイなんて本当にいるのかな～？\x02\x03",

            "#1906Fはあ、受付の仕事が無かったら\x01",
            "わたしもお姉ちゃんと一緒に\x01",
            "見に行きたいんですけどー。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x102,
        (
            "#0106F（フランさんの神経が\x01",
            "  分からないわ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6784")

    Return()

    # Function_10_62A7 end

    def Function_11_6785(): pass

    label("Function_11_6785")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x8, 0x0, 0)

    #C0276
    ChrTalk(
        0x9,
        (
            "#1901Fあ、皆さん……\x01",
            "クロスベル空港の話、聞きました？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        "#0005Fいや……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 6)), scpexpr(EXPR_END)), "loc_6832")

    #C0278
    ChrTalk(
        0x104,
        (
            "#0301Fそういや、空港前に\x01",
            "私服の捜査官がいやがったが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6832")


    #C0279
    ChrTalk(
        0x8,
        (
            "それが、先ほど捜査一課が\x01",
            "警官隊を動員して……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "一時的にクロスベル空港が\x01",
            "封鎖されるそうなんです。\x02",
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
        "#0011Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x102,
        "#0101F……何かあったんですか？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x9,
        (
            "#1906Fそれが……\x01",
            "箝口令#6Rかんこうれい#が敷かれたらしくて\x01",
            "こちらには教えてもらえなくって。\x02\x03",

            "#1901Fその様子だと、ロイドさんたちも\x01",
            "ご存知ないみたいですね～？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x103,
        (
            "#0203Fまあ、こちらには大抵、\x01",
            "重要な情報は回ってきませんし……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#0003Fうーん、気になるけど……\x02\x03",

            "#0008F（あとでダドリー捜査官が\x01",
            "  教えてくれるかもしれない。）\x02\x03",

            "#0001F（今は失踪者の件に\x01",
            "  集中した方が良さそうだな。）\x02",
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

    # Function_11_6785 end

    def Function_12_6AD6(): pass

    label("Function_12_6AD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6AE7")
    Jump("loc_7ADD")

    label("loc_6AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6AF5")
    Jump("loc_7ADD")

    label("loc_6AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6B03")
    Jump("loc_7ADD")

    label("loc_6B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C33")
    OP_93(0xFE, 0x5A, 0x0)

    #C0286
    ChrTalk(
        0xFE,
        "やれやれ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0287
    ChrTalk(
        0xFE,
        "おう、お前らか。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "……今日もいいツラしてやがんな。\x01",
            "たまにお前ら支援課が\x01",
            "羨ましく思えるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#0005Fドノバン警部……\x01",
            "何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "なに大したことじゃねえよ。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "一課にヤマを\x01",
            "取られたってだけの話だ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6CCD")

    label("loc_6C33")


    #C0292
    ChrTalk(
        0xFE,
        (
            "ルバーチェ構成員の絡んだ\x01",
            "傷害事件でな、ただの事件として\x01",
            "捜査すりゃあ……と思ったんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "一課には有無を言わさず\x01",
            "取り上げられたぜ。\x01",
            "やれやれ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CCD")

    Jump("loc_7ADD")

    label("loc_6CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6FBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F29")

    #C0294
    ChrTalk(
        0xFE,
        "よう、特務支援課じゃねえか。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "ヤバい山に手ぇ出した挙句、\x01",
            "ルバーチェに睨まれて\x01",
            "引き篭もるたぁな。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "そのうち何か\x01",
            "やらかすだろとは思ってたが\x01",
            "……さすがにぶったまげたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        (
            "#0001Fすみません……\x01",
            "ご心配とご迷惑をおかけしました。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_6E06")

    #C0298
    ChrTalk(
        0x102,
        "#0103F返す言葉もありません……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E65")

    label("loc_6E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_6E3C")

    #C0299
    ChrTalk(
        0x103,
        "#0203F……返す言葉もありませんね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E65")

    label("loc_6E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6E65")

    #C0300
    ChrTalk(
        0x104,
        "#0303F返す言葉もねえなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_6E65")


    #C0301
    ChrTalk(
        0xFE,
        (
            "へっ、まあ泡食ってんのは\x01",
            "主に上層部だがなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "お前らは１週間\x01",
            "謹慎したようなもんだろ。\x01",
            "あんましょげんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "……俺も、お前らのやったことは\x01",
            "間違いじゃねえと思ってるクチだしな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 2)
    Jump("loc_6FBA")

    label("loc_6F29")


    #C0304
    ChrTalk(
        0xFE,
        (
            "二課の方も\x01",
            "この１週間は警戒してたんだが、\x01",
            "今朝手打ちの話が来てな。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "……特に事件も起こってねえ事だし\x01",
            "そろそろ通常の体制に戻すとすっか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FBA")

    Jump("loc_7ADD")

    label("loc_6FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6FCD")
    Jump("loc_7ADD")

    label("loc_6FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6FDB")
    Jump("loc_7ADD")

    label("loc_6FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6FE9")
    Jump("loc_7ADD")

    label("loc_6FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_71F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7175")

    #C0306
    ChrTalk(
        0xFE,
        "よぉ、お前らか。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "最近事故やら暴力事件なんかが\x01",
            "増えてきててな……\x01",
            "俺たち二課も休む暇がねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 1)), scpexpr(EXPR_END)), "loc_70AD")

    #C0308
    ChrTalk(
        0x101,
        (
            "#0008Fそういえば……\x01",
            "市内でもちらほら噂を聞きました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70E0")

    label("loc_70AD")


    #C0309
    ChrTalk(
        0x101,
        (
            "#0005Fそうなんですか……\x01",
            "少し気になりますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70E0")


    #C0310
    ChrTalk(
        0xFE,
        (
            "ふむ……記念祭が近いだけじゃ\x01",
            "ねえみたいなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "まあお前らも気を付けといてくれや。\x01",
            "市内の見回りなら\x01",
            "お前らの方が気が回んだろ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_71EB")

    label("loc_7175")


    #C0312
    ChrTalk(
        0xFE,
        (
            "近頃、暴力沙汰だの何だのと\x01",
            "物騒な話が増えてやがる。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "昨晩は発砲事件まであってな、\x01",
            "これからその聞き込みだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71EB")

    Jump("loc_7ADD")

    label("loc_71F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_732C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72BC")

    #C0314
    ChrTalk(
        0xFE,
        (
            "よぉお前ら、また\x01",
            "面倒な仕事を回されたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "お偉いさんのゴタゴタには\x01",
            "巻き込まれねえよう気をつけとけよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#0000Fはは、どうも……\x01",
            "（もう手遅れな気もするけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7327")

    label("loc_72BC")


    #C0317
    ChrTalk(
        0xFE,
        "また面倒な仕事を回されたらしいな。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "お偉いさん方にも色々ある。\x01",
            "巻き込まれねえよう気をつけとけよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7327")

    Jump("loc_7ADD")

    label("loc_732C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_74EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7490")

    #C0319
    ChrTalk(
        0xFE,
        (
            "この１ヵ月追っていた事件、\x01",
            "親類に議員がいる事がわかってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "上が及び腰になってるんだ。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "議員がらみと分かると途端にこれだ。\x01",
            "やれやれ、苦労するぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        (
            "#0200F議員の関係者は\x01",
            "逮捕できないのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "いや、そういう訳じゃ\x01",
            "ねえんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "遠回しに圧力が掛かったりするからな。\x01",
            "捜査も慎重に進めねえといけねえのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_74E5")

    label("loc_7490")


    #C0325
    ChrTalk(
        0xFE,
        (
            "親類に議員がいるってだけで\x01",
            "上も及び腰になっちまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "やれやれ、肩が凝るぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_74E5")

    Jump("loc_7ADD")

    label("loc_74EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_76B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7656")

    #C0327
    ChrTalk(
        0xFE,
        "よぉ、お疲れさん。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "今日も支援要請とかいうのを\x01",
            "細々とやってるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#0012Fはは、まあ……\x01",
            "そんなところです。\x02\x03",

            "#0000F二課の方は\x01",
            "最近どうですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "まあぼちぼちだな。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "いくつか事件を手がけてるが\x01",
            "急に捜査が進むわけでもねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "一つ一つ慎重にやるしかねえな。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#0003Fやっぱり……捜査といえば\x01",
            "それしかないですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_76AD")

    label("loc_7656")


    #C0334
    ChrTalk(
        0xFE,
        "二課の方も、まあぼちぼちだぜ。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "捜査なんて一つ一つ\x01",
            "進めていくしかねえからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76AD")

    Jump("loc_7ADD")

    label("loc_76B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_77C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7760")

    #C0336
    ChrTalk(
        0xFE,
        (
            "ふう、やれやれ。\x01",
            "調書取るのも大変だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "クロスベル市は広い上に\x01",
            "人口もハンパじゃねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "一日に何人も\x01",
            "取り調べにゃならねえんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_77BE")

    label("loc_7760")


    #C0339
    ChrTalk(
        0xFE,
        (
            "やれやれ、\x01",
            "ようやくメシに行けるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "いい加減二課#4Rウ　チ#も\x01",
            "万年人手不足で困るぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77BE")

    Jump("loc_7ADD")

    label("loc_77C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79E5")

    #C0341
    ChrTalk(
        0xFE,
        "よぉ、早速頑張ってるようだな。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "……まあお前らは署内でも\x01",
            "あまり良く思われてねえ。\x01",
            "絡まれねえように気をつけとけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        "#0305Fへえ、そんなに酷いんスか？\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "ん～、まあ遊撃士の真似事なんざ、\x01",
            "真面目なヤツからすりゃあ\x01",
            "プライドがた落ちってトコだからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "分室暮らしじゃ分からんだろうが、\x01",
            "署内じゃ目の上のタンコブ扱いだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        "#0003Fうっ……そうですか……\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x103,
        (
            "#0200F分室ビルがあって\x01",
            "ラッキーでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "ま、今はあんま気にしねえで\x01",
            "早く仕事に慣れるこったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "それが連中を見返す\x01",
            "一番の近道だろ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4A, 0)
    SetScenarioFlags(0x0, 2)
    Jump("loc_7ADD")

    label("loc_79E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A6B")

    #C0350
    ChrTalk(
        0xFE,
        "よぉ、早速頑張ってるようだな。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "お前らは署内でも\x01",
            "あまり良く思われてねえ。\x01",
            "絡まれねえように気をつけとけよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7ADD")

    label("loc_7A6B")


    #C0352
    ChrTalk(
        0xFE,
        (
            "お前らは署内でも\x01",
            "あまり良く思われてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "ま、気にしてもしゃあねえが\x01",
            "絡まれねえようには気をつけとけよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ADD")

    TalkEnd(0xFE)
    Return()

    # Function_12_6AD6 end

    def Function_13_7AE1(): pass

    label("Function_13_7AE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7AF2")
    Jump("loc_8868")

    label("loc_7AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7B00")
    Jump("loc_8868")

    label("loc_7B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7B0E")
    Jump("loc_8868")

    label("loc_7B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7BE0")

    #C0354
    ChrTalk(
        0xFE,
        (
            "今朝のルバーチェがらみの傷害事件、\x01",
            "捜査一課に巻き上げられちゃったよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "その上、捜査資料を\x01",
            "全部寄越せだってさ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "くっそ～、ムカツクなぁ。\x01",
            "こういうの続くと\x01",
            "やる気なくしちゃうぞ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8868")

    label("loc_7BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7F52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EDD")

    #C0357
    ChrTalk(
        0xFE,
        (
            "局長と副局長は、今日も\x01",
            "市庁舎に呼ばれてたみたいだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "副局長なんて自分の首を心配してさ～、\x01",
            "最近嫌味を言う余裕も無いみたいだよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_7CAF")

    #C0359
    ChrTalk(
        0x102,
        "#0106Fそれは嬉しいけど……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D06")

    label("loc_7CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_7CDF")

    #C0360
    ChrTalk(
        0x103,
        "#0206Fそれは嬉しいですが……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D06")

    label("loc_7CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_7D06")

    #C0361
    ChrTalk(
        0x104,
        "#0306Fそれは嬉しいが……\x02",
    )

    CloseMessageWindow()

    label("loc_7D06")


    #C0362
    ChrTalk(
        0x101,
        (
            "#0003F今顔をあわせたら\x01",
            "間違いなくどやされるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "うんにゃ、キレて\x01",
            "襲い掛かってくるかもよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "あのキツネ、保身のためには\x01",
            "何だってするらしいからさ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_7E21")

    #C0365
    ChrTalk(
        0x102,
        (
            "#0106Fルバーチェの次は\x01",
            "副局長に気を付けないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EAA")

    label("loc_7E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_7E6A")

    #C0366
    ChrTalk(
        0x103,
        (
            "#0200Fルバーチェの次は\x01",
            "副局長さんに気を付けましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EAA")

    label("loc_7E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_7EAA")

    #C0367
    ChrTalk(
        0x104,
        (
            "#0300Fルバーチェの次は\x01",
            "副局長に気を付けねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EAA")


    #C0368
    ChrTalk(
        0x153,
        (
            "#1111F（キツネ？\x01",
            "  何の話だろ～……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7F4D")

    label("loc_7EDD")


    #C0369
    ChrTalk(
        0xFE,
        (
            "局長と副局長、今日も\x01",
            "市庁舎に呼ばれてたみたいだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "君たちも凄い事するよね～。\x01",
            "僕もビックリだよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F4D")

    Jump("loc_8868")

    label("loc_7F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7F60")
    Jump("loc_8868")

    label("loc_7F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8074")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8007")

    #C0371
    ChrTalk(
        0xFE,
        (
            "一課にはエマって名前の\x01",
            "女捜査官がいるだろ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "あいつ、同期なんだよなー。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "昔からエリートでさー。\x01",
            "ちぇっ、気に食わない女だぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_806F")

    label("loc_8007")


    #C0374
    ChrTalk(
        0xFE,
        (
            "エマの奴は昔から\x01",
            "エリートなんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "同期のくせに見下しやがって。\x01",
            "ちぇっ、気に食わないな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_806F")

    Jump("loc_8868")

    label("loc_8074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8082")
    Jump("loc_8868")

    label("loc_8082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_81BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8176")

    #C0376
    ChrTalk(
        0xFE,
        (
            "ふう、まったく\x01",
            "今週は事件ばっかりだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "昨晩も現場検証で\x01",
            "徹夜フルコースでさー……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "と思ったら、また倉庫街の方で\x01",
            "発砲事件かあったらしいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "まったく……\x01",
            "市民も少しはこの苦労、\x01",
            "分かって欲しいな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_81B8")

    label("loc_8176")


    #C0380
    ChrTalk(
        0xFE,
        "徹夜コースはつらいよ～。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        "警察って結構報われないよね～。\x02",
    )

    CloseMessageWindow()

    label("loc_81B8")

    Jump("loc_8868")

    label("loc_81BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_828F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_81DA")
    Call(0, 14)
    Jump("loc_828A")

    label("loc_81DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_8272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_81F8")
    Call(0, 14)
    Jump("loc_826D")

    label("loc_81F8")


    #C0382
    ChrTalk(
        0xB,
        (
            "ふぅ、とりあえず\x01",
            "本が見つかって助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xB,
        (
            "次からちゃんと内容を確かめてから\x01",
            "借りるようにしないとなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_826D")

    Jump("loc_828A")

    label("loc_8272")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_8287")
    Call(0, 28)
    Jump("loc_828A")

    label("loc_8287")

    Call(0, 14)

    label("loc_828A")

    Jump("loc_8868")

    label("loc_828F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8361")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_82AC")
    Call(0, 15)
    Jump("loc_835C")

    label("loc_82AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_8344")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_82CA")
    Call(0, 15)
    Jump("loc_833F")

    label("loc_82CA")


    #C0384
    ChrTalk(
        0xB,
        (
            "ふぅ、とりあえず\x01",
            "本が見つかって助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xB,
        (
            "次からちゃんと内容を確かめてから\x01",
            "借りるようにしないとなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_833F")

    Jump("loc_835C")

    label("loc_8344")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_8359")
    Call(0, 28)
    Jump("loc_835C")

    label("loc_8359")

    Call(0, 15)

    label("loc_835C")

    Jump("loc_8868")

    label("loc_8361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8433")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_837E")
    Call(0, 16)
    Jump("loc_842E")

    label("loc_837E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_8416")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_839C")
    Call(0, 16)
    Jump("loc_8411")

    label("loc_839C")


    #C0386
    ChrTalk(
        0xB,
        (
            "ふぅ、とりあえず\x01",
            "本が見つかって助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xB,
        (
            "次からちゃんと内容を確かめてから\x01",
            "借りるようにしないとなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_8411")

    Jump("loc_842E")

    label("loc_8416")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_842B")
    Call(0, 28)
    Jump("loc_842E")

    label("loc_842B")

    Call(0, 16)

    label("loc_842E")

    Jump("loc_8868")

    label("loc_8433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_84CC")

    #C0388
    ChrTalk(
        0xFE,
        (
            "ふう、調書を纏めるのも楽じゃないぜ。\x01",
            "カフェイン、カフェインっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "ついでに\x01",
            "レベッカさんのお姿でも拝んで\x01",
            "英気を補充しようっと㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8868")

    label("loc_84CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8725")

    #C0390
    ChrTalk(
        0xFE,
        (
            "フランちゃんから聞いたよ～。\x01",
            "結局例の部署に残ったんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        "いや～、君たちも勇気あるなぁ。\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "ま、残っちゃった以上は後輩なんだし、\x01",
            "分からない事があれば何でも聞いてよ。\x01",
            "適当に答えてあげるからさー。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#0000Fはは……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    #C0394
    ChrTalk(
        0xFE,
        (
            "それはそうと、エリィちゃん。\x01",
            "今ヒマだったりする？\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "これから食事なんてどう！？\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        "#0100Fふふ、それはお断りします。\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "あ、やっぱり？\x01",
            "あはは、ガード固いんだね～。\x02",
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
        "#0000F（随分と軽い人だなぁ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4A, 1)
    SetScenarioFlags(0x0, 3)
    Jump("loc_8868")

    label("loc_8725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87F4")

    #C0399
    ChrTalk(
        0xFE,
        (
            "結局例の部署に残ったんだってね。\x01",
            "いや～、君たちも勇気あるなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "ま、残っちゃった以上は\x01",
            "後輩って事になるし、\x01",
            "分からない事があれば何でも聞いてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        "適当に答えてあげるからさー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8868")

    label("loc_87F4")

    OP_93(0xFE, 0x10E, 0x0)

    #C0402
    ChrTalk(
        0xFE,
        (
            "うーっす、\x01",
            "一応聞き込みましたけど\x01",
            "目撃者はゼロ。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "警部、これ以上捜査しても\x01",
            "らちが明かないっすよー？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8868")

    TalkEnd(0xFE)
    Return()

    # Function_13_7AE1 end

    def Function_14_886C(): pass

    label("Function_14_886C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8948")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xFE, 0xA, 0)

    #C0404
    ChrTalk(
        0xA,
        (
            "まずはホテルの聞き込みからだな。\x01",
            "周辺のミセも回ってみるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        "え～、今日も聞き込み！？\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "面倒だな～。\x01",
            "歓楽街って広いし～。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xA,
        (
            "ったくオメーは……\x01",
            "しゃきっとしやがれってんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0xA, 0xFF)
    Jump("loc_899D")

    label("loc_8948")


    #C0408
    ChrTalk(
        0xFE,
        "やあ、君たちも捜査？\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "お互い忙しいよねー。\x01",
            "女の子とデートする暇も無いよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_899D")

    Return()

    # Function_14_886C end

    def Function_15_899E(): pass

    label("Function_15_899E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B63")
    OP_93(0xFE, 0x0, 0x0)

    #C0410
    ChrTalk(
        0xFE,
        (
            "おっ、この議員の奥様\x01",
            "なかなか美人だな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "うふふ、今度の捜査は\x01",
            "ちょっとやる気出てきちゃったぞ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x101,
        (
            "#0000F（ランディみたいな事を\x01",
            "  言っている……）\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x104,
        (
            "#0305F（ん……？\x01",
            "  そんなの誰でもやってるだろ。）\x02\x03",

            "#0300F（テンションを上げるための\x01",
            "  工夫ってやつだぜ。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AE6")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_8AE6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B0C")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_8B0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B32")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_8B32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B58")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_8B58")

    Sleep(1000)
    SetScenarioFlags(0x0, 3)
    Jump("loc_8BD1")

    label("loc_8B63")


    #C0414
    ChrTalk(
        0xFE,
        (
            "あれ、君たちも捜査資料を\x01",
            "探しに来たのかい～？\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "捜査資料はいいよね～。\x01",
            "たまに美人な奥様に会えるよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD1")

    Return()

    # Function_15_899E end

    def Function_16_8BD2(): pass

    label("Function_16_8BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CCA")

    #C0416
    ChrTalk(
        0xFE,
        (
            "さっき警備隊の\x01",
            "ソーニャ副司令とすれ違ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "警備隊はいいよな～。\x01",
            "オレもあんな人にお仕置きされたい㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x104,
        (
            "#0306Fいや～、実際キツイぜ\x01",
            "あの人の訓練は。\x02\x03",

            "重装備で街道マラソンとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "うげ……\x01",
            "それはちょっと勘弁かな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8D33")

    label("loc_8CCA")


    #C0420
    ChrTalk(
        0xFE,
        (
            "警備隊には\x01",
            "美人な上官がいていいよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        (
            "警察のお偉いさんは\x01",
            "ヤローばっかりで\x01",
            "嫌になっちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D33")

    Return()

    # Function_16_8BD2 end

    def Function_17_8D34(): pass

    label("Function_17_8D34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F01")

    #C0422
    ChrTalk(
        0xFE,
        (
            "やあ、ロイド達か。\x01",
            "朝から仕事みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#0003Fああ、今日はちょっと\x01",
            "忙しくなりそうでさ。\x02\x03",

            "#0000Fフランツの方は\x01",
            "朝から会議みたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "これから広域防犯課全員の\x01",
            "巡回ルートの担当を決めるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "警察に入って１ヶ月……\x01",
            "そろそろ色んな仕事を回すぞって\x01",
            "先輩たちも張り切っててさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        (
            "#0000Fはは、そっか。\x01",
            "そっちも忙しそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        "ま、お互い頑張ろうぜ。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "ロイド達も色々大変だろうけど……\x01",
            "オレたち、まだ新人なんだしさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 4)
    Jump("loc_8F7E")

    label("loc_8F01")


    #C0429
    ChrTalk(
        0xFE,
        (
            "オレたち広域防犯課は\x01",
            "市内の巡回が主な仕事なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "警察に入って１ヶ月……\x01",
            "そろそろ本格的に\x01",
            "任務開始って感じだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F7E")

    TalkEnd(0xFE)
    Return()

    # Function_17_8D34 end

    def Function_18_8F82(): pass

    label("Function_18_8F82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9075")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9021")

    #C0431
    ChrTalk(
        0xFE,
        (
            "いま局長室で\x01",
            "課長クラスが集まって\x01",
            "重要会議をやっているらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "ルバーチェがどうとか\x01",
            "慌ててたけど……何事なんだろ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9070")

    label("loc_9021")


    #C0433
    ChrTalk(
        0xFE,
        "昨日今日と事件続きだよなぁ。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xFE,
        (
            "これ以上どんな事件が\x01",
            "起きるってんだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9070")

    Jump("loc_98B0")

    label("loc_9075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_914B")

    #C0435
    ChrTalk(
        0xFE,
        (
            "今日は朝から合同捜査本部が\x01",
            "設置されているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        (
            "昨日に続き大事件が続くが……\x01",
            "こんな時こそ\x01",
            "我ら警官隊の底力の見せ所だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "卑劣なテロリストに負けてなるものか！\x01",
            "必ず未然に防いでみせるぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98B0")

    label("loc_914B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_926C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91E4")

    #C0438
    ChrTalk(
        0xFE,
        "襲撃事件とは大胆な！\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "……まあ、市民に被害が\x01",
            "出ておらんのは幸いだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "後は早急に犯人を\x01",
            "逮捕できればいいんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9267")

    label("loc_91E4")


    #C0441
    ChrTalk(
        0xFE,
        (
            "犯人がルバーチェ構成員だろうが\x01",
            "証拠をそろえて\x01",
            "必ず検挙してやらんとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "我ら広域防犯課も\x01",
            "すでに聞き込みを開始しているぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9267")

    Jump("loc_98B0")

    label("loc_926C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_931A")

    #C0443
    ChrTalk(
        0xFE,
        (
            "近頃、マフィア関係の事件に\x01",
            "市民が巻き込まれる\x01",
            "トラブルが増えているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "捜査一課もピリピリしててな、\x01",
            "俺たち広域防犯課にも\x01",
            "何かと注文をつけてくるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98B0")

    label("loc_931A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9328")
    Jump("loc_98B0")

    label("loc_9328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_93DD")

    #C0445
    ChrTalk(
        0xFE,
        (
            "聞いたか？\x01",
            "歓楽街の方でまた事件が\x01",
            "あったそうだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "広域防犯課#10Rウ    チ#の巡査が見つけて\x01",
            "捜査二課が動いてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "今ごろあちこち\x01",
            "聞きこんでるはずさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98B0")

    label("loc_93DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9444")

    #C0448
    ChrTalk(
        0xFE,
        "よぉし、今日も市内巡回だ。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "うむ、午前中の巡回は\x01",
            "気持ちが引き締まってよいなぁ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98B0")

    label("loc_9444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_957B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_950A")

    #C0450
    ChrTalk(
        0xFE,
        (
            "自治州の創立記念祭には\x01",
            "各国のＶＩＰも訪れる。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "開会式の警備は\x01",
            "一課や二課に任せるとして、\x01",
            "我らは市内の巡回を強化しないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        "ふう、今年の記念祭は大仕事だぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9576")

    label("loc_950A")


    #C0453
    ChrTalk(
        0xFE,
        (
            "特に創立記念祭の開会式には\x01",
            "各国のＶＩＰが出席なさる……\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "そろそろ市内の\x01",
            "巡回ルートを決めないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9576")

    Jump("loc_98B0")

    label("loc_957B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_966D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9639")

    #C0455
    ChrTalk(
        0xFE,
        (
            "創立記念祭には\x01",
            "行事が盛りだくさんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xFE,
        (
            "警察としても、警備や\x01",
            "市民の誘導の仕事が山ほどある。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "まさに年に一度の大仕事。\x01",
            "我々も気合を入れていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9668")

    label("loc_9639")


    #C0458
    ChrTalk(
        0xFE,
        (
            "来月に向けて\x01",
            "我ら広域防犯課も大忙しだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9668")

    Jump("loc_98B0")

    label("loc_966D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_97A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9734")

    #C0459
    ChrTalk(
        0xFE,
        (
            "今年はウチの課にも\x01",
            "何人か新人が入ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        (
            "みんな頑張ってるかな。\x01",
            "ウチのような平穏な部署にも\x01",
            "色々とあったりするが……\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        (
            "まあめげずに\x01",
            "成長して欲しいものだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_97A2")

    label("loc_9734")


    #C0462
    ChrTalk(
        0xFE,
        (
            "ウチのような平穏な部署でも\x01",
            "辛く苦しい事があるものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        (
            "新人たちにはめげずに\x01",
            "成長して欲しいものだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97A2")

    Jump("loc_98B0")

    label("loc_97A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_97B8")
    Call(0, 19)
    Jump("loc_98B0")

    label("loc_97B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9845")

    #C0464
    ChrTalk(
        0xFE,
        (
            "今日の会議、場所が急に\x01",
            "変更になっちゃってねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "みんな２階の会議室に\x01",
            "向かったんじゃないかな。\x01",
            "ちっとも集まらないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98B0")

    label("loc_9845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_98B0")

    #C0466
    ChrTalk(
        0xFE,
        (
            "ケイト先輩に巡回の段取りを\x01",
            "教えてもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "先輩の指導は\x01",
            "分かりやすくて助かるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98B0")

    TalkEnd(0xFE)
    Return()

    # Function_18_8F82 end

    def Function_19_98B4(): pass

    label("Function_19_98B4")

    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xD, 0xF, 0)
    TurnDirection(0xF, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F0")

    #C0468
    ChrTalk(
        0xD,
        (
            "新人の担当地区も\x01",
            "無事決まったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xD,
        (
            "ケイト巡査、君はどうするんだ？\x01",
            "ベテランの君には\x01",
            "手薄な地区に回って欲しいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xF,
        (
            "先輩、ベテランって\x01",
            "言わないで下さーい。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0xF,
        (
            "まるで私が\x01",
            "お年寄りみたいじゃないですか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0472
    ChrTalk(
        0xD,
        "それはスマンかった……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9AE5")

    label("loc_99F0")


    #C0473
    ChrTalk(
        0xD,
        (
            "それでケイト巡査、\x01",
            "どうかな、この割り振りで。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xF,
        (
            "そうですねー……\x01",
            "最近は導力車が増えてるので、\x01",
            "中央広場には私が行こうかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xF,
        "何と言ってもベテランですので！\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0476
    ChrTalk(
        0xD,
        (
            "そ、そうか。\x01",
            "それではお願いするかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AE5")

    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_93(0xD, 0xB4, 0x0)
    OP_93(0xF, 0x0, 0x0)
    Return()

    # Function_19_98B4 end

    def Function_20_9AFC(): pass

    label("Function_20_9AFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9B0D")
    Jump("loc_A23D")

    label("loc_9B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C06")

    #C0477
    ChrTalk(
        0xFE,
        "あー、君たち。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xFE,
        (
            "この件、混乱が大きいから\x01",
            "市民には知らせない事になったから。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xFE,
        "よく覚えとくようにー。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BC9")

    #C0480
    ChrTalk(
        0x101,
        (
            "#0000Fは、はあ……\x01",
            "（何の話だろ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BFE")

    label("loc_9BC9")


    #C0481
    ChrTalk(
        0x101,
        (
            "#0000Fは、はい……\x01",
            "（やっぱり大事だからな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BFE")

    SetScenarioFlags(0x0, 6)
    Jump("loc_9CAB")

    label("loc_9C06")

    OP_4B(0xD, 0xFF)
    OP_93(0xFE, 0x10E, 0x0)
    TurnDirection(0xD, 0xFE, 0)

    #C0482
    ChrTalk(
        0xFE,
        (
            "あー、それじゃともかく\x01",
            "君らで聞き込みだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        (
            "駅と空港は\x01",
            "一課と二課で持つそうだから。\x01",
            "市内分を頼むぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xD,
        "はっ、了解でありまーす！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_9CAB")

    Jump("loc_A23D")

    label("loc_9CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9CBE")
    Jump("loc_A23D")

    label("loc_9CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9CCC")
    Jump("loc_A23D")

    label("loc_9CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9CDA")
    Jump("loc_A23D")

    label("loc_9CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9CE8")
    Jump("loc_A23D")

    label("loc_9CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9FF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E96")

    #C0485
    ChrTalk(
        0xFE,
        (
            "おー、君らは。\x01",
            "たしかセルゲイ君の所の子だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "うんうん、今になって\x01",
            "新部署を立ち上げて……\x01",
            "セルゲイ君もがんばるもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xFE,
        "私は感心するよ。\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x101,
        (
            "#0000Fセルゲイ課長のこと、\x01",
            "ご存知みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xFE,
        (
            "あー、まあね。\x01",
            "あの男も昔は大層\x01",
            "目立っておったから。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "……まあ、あまりセルゲイ君に\x01",
            "迷惑を掛けんようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xFE,
        (
            "私のような定年間際の\x01",
            "おじさんとは違って、彼はまだまだ\x01",
            "警察にいるべき男だから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 7)
    Jump("loc_9FED")

    label("loc_9E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F96")

    #C0492
    ChrTalk(
        0xFE,
        (
            "ところで……\x01",
            "君らは紅茶党かね？\x01",
            "コーヒー党かね？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xFE,
        "私は大のコーヒー党でなぁ。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "うーむ、デスクにも\x01",
            "豆引きがあればいいんだが……\x02",
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
    Jump("loc_9FED")

    label("loc_9F96")


    #C0495
    ChrTalk(
        0xFE,
        "どれ、缶コーヒーは、と……\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xFE,
        (
            "……またセルゲイ君と\x01",
            "ゆっくり飲みたいもんだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FED")

    Jump("loc_A23D")

    label("loc_9FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A0D8")
    OP_93(0xFE, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0A6")

    #C0497
    ChrTalk(
        0xFE,
        (
            "うーむ、毎年のことながら\x01",
            "割り振りは面倒だなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        "こっちか、それともこっち……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        (
            "あー、誰かが代わりに\x01",
            "決めてくれれば楽なんだがなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_A0D3")

    label("loc_A0A6")


    #C0500
    ChrTalk(
        0xFE,
        (
            "うーむ、やはり\x01",
            "この割り振りで行くかー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0D3")

    Jump("loc_A23D")

    label("loc_A0D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A0E6")
    Jump("loc_A23D")

    label("loc_A0E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A0F4")
    Jump("loc_A23D")

    label("loc_A0F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A102")
    Jump("loc_A23D")

    label("loc_A102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A23D")
    OP_93(0xFE, 0x10E, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A19E")

    #C0501
    ChrTalk(
        0xFE,
        (
            "あー……それでは\x01",
            "そろそろ始めたいと思うー……\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        "ひいふうみい……\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        (
            "うーむ、なんだ。\x01",
            "全然揃っとらんじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_A23D")

    label("loc_A19E")

    TurnDirection(0xFE, 0xF, 0)

    #C0504
    ChrTalk(
        0xFE,
        (
            "ケイト巡査ー。\x01",
            "残りの連中を呼んできてくれんか。\x01",
            "ちっとも始められんぞー。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0xFE, 0)

    #C0505
    ChrTalk(
        0xF,
        (
            "はーい課長、\x01",
            "ちょっとお待ちくださーい！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x10E, 0x0)
    OP_93(0xF, 0x10E, 0x0)
    OP_4C(0xF, 0xFF)

    label("loc_A23D")

    TalkEnd(0xFE)
    Return()

    # Function_20_9AFC end

    def Function_21_A241(): pass

    label("Function_21_A241")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A49F")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0506
    ChrTalk(
        0xFE,
        (
            "あっ……ロイド君？\x01",
            "久しぶりね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#0000Fケイト先輩……\x01",
            "ご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x104,
        "#0300Fなんだ、ロイドの知り合いか？\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        (
            "#0000Fああ、警察学校の授業に\x01",
            "時々来てくれた先輩なんだよ。\x02\x03",

            "座学から射撃まで\x01",
            "色々お世話になったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xFE,
        (
            "ふふっ、ロイド君は\x01",
            "なかなか優秀だったから\x01",
            "教えがいがあったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        (
            "……えっと、何だか難しい部署に\x01",
            "配属になっちゃったみたいだけど\x01",
            "……その、頑張ってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xFE,
        (
            "努力する者は報われる！\x01",
            "希望を捨てちゃダメよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#0006Fは、はい、そうですね。\x01",
            "（気を遣わせてしまった……）\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x102,
        (
            "#0108F（やっぱり支援課は\x01",
            "  日陰者なのよね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 7)
    Jump("loc_A6E2")

    label("loc_A49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A4B0")
    Call(0, 19)
    Jump("loc_A6E2")

    label("loc_A4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A569")

    #C0515
    ChrTalk(
        0xFE,
        "ええと、当番表のプリントは、と……\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xFE,
        (
            "ホントは上の会議室を\x01",
            "使う予定だったんだけど、\x01",
            "捜査一課が占領しちゃってるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xFE,
        (
            "あの人たちったら\x01",
            "いつもこうなんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6E2")

    label("loc_A569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A5EB")

    #C0518
    ChrTalk(
        0xFE,
        (
            "ふう、今年の新人君たちも\x01",
            "無事送り出せてよかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "ちゃらっと報告書をまとめて\x01",
            "課長に報告しなくっちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6E2")

    label("loc_A5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A6E2")

    #C0520
    ChrTalk(
        0xFE,
        (
            "さーて、新人君たちに\x01",
            "みっちり教えてやりますか。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xFE,
        (
            "ちなみに私たちは\x01",
            "『広域防犯課』っていうのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "市内の巡回が主なお仕事ね。\x01",
            "どこかで見かけたら、\x01",
            "またよろしくね！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6E2")

    #C0523
    ChrTalk(
        0x101,
        (
            "#0000Fはい、こちらこそ\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_A6E2")

    TalkEnd(0xFE)
    Return()

    # Function_21_A241 end

    def Function_22_A6E6(): pass

    label("Function_22_A6E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7CD")

    #C0524
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        "まったく……\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        (
            "あれからこちらも会議続きです。\x01",
            "はあ、肩が凝って仕方ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        (
            "#0006F（うっ……捜査一課の人か……）\x02\x03",

            "（まあ嫌味を言われても\x01",
            "  当然の立場だけどな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A812")

    label("loc_A7CD")


    #C0528
    ChrTalk(
        0xFE,
        (
            "あれからこちらも会議続きです。\x01",
            "はあ、肩が凝って仕方ありません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A812")

    TalkEnd(0xFE)
    Return()

    # Function_22_A6E6 end

    def Function_23_A816(): pass

    label("Function_23_A816")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8E3")

    #C0529
    ChrTalk(
        0x101,
        "#0005Fあれ、課長が本部にいる……\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x104,
        (
            "#0300F珍しいっすね。\x01",
            "副局長に呼ばれたんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xFE,
        (
            "#1006F今日は本部会議だっつーの。\x01",
            "嫌なこと言うんじゃねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x104,
        "#0300Fはは、すんません。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A967")

    label("loc_A8E3")


    #C0533
    ChrTalk(
        0xFE,
        (
            "#1006Fそろそろ記念祭も近いからな。\x01",
            "各種会議があるんだよ。\x02\x03",

            "#1000Fお前らは気にせず仕事してろ。\x01",
            "報告なら後でまとめて聞くからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A967")

    TalkEnd(0xFE)
    Return()

    # Function_23_A816 end

    def Function_24_A96B(): pass

    label("Function_24_A96B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A9FF")
    Jump("loc_AA49")

    label("loc_A9FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA1F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AA49")

    label("loc_AA1F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA3F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AA49")

    label("loc_AA3F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA49")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0534
    ChrTalk(
        0xFE,
        (
            "まさか空港を標的にするなんて……\x01",
            "敵はテロリストか！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_A96B end

    def Function_25_AAB1(): pass

    label("Function_25_AAB1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB45")
    Jump("loc_AB8F")

    label("loc_AB45")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AB65")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB8F")

    label("loc_AB65")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB85")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB8F")

    label("loc_AB85")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB8F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0535
    ChrTalk(
        0xFE,
        (
            "非番のところに\x01",
            "呼び出しを食らったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xFE,
        (
            "こ、こんな大事件に\x01",
            "なってるなんてな……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_AAB1 end

    def Function_26_AC16(): pass

    label("Function_26_AC16")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACAA")
    Jump("loc_ACF4")

    label("loc_ACAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ACCA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ACF4")

    label("loc_ACCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACEA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ACF4")

    label("loc_ACEA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ACF4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0537
    ChrTalk(
        0xFE,
        (
            "また事件か……\x01",
            "今年は事件が多いよなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_AC16 end

    def Function_27_AD4E(): pass

    label("Function_27_AD4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE21")

    #C0538
    ChrTalk(
        0xFE,
        "ううむ、一体どこに……\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xFE,
        (
            "まさかあそこか……？\x01",
            "いやいや、そんなはずは……\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#0005F（あれ、副局長……？）\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x102,
        (
            "#0100F（わき目も振らずって感じね。\x01",
            "  どうかしたのかしら。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_AE59")

    label("loc_AE21")


    #C0542
    ChrTalk(
        0xFE,
        "うろうろ、うろうろ……\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xFE,
        "ううむ、一体どこに……\x02",
    )

    CloseMessageWindow()

    label("loc_AE59")

    Jump("loc_AF51")

    label("loc_AE5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_AF4E")

    #C0544
    ChrTalk(
        0x12,
        (
            "探しているのは\x01",
            "紅耀石#6Rカーネリア#をあしらった結婚指輪だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x12,
        (
            "フン、見つけたらすぐに報せたまえ。\x01",
            "──いいね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        (
            "#0003F（ツァイトの鼻を使えば\x01",
            "  探し出せるかもしれない……）\x02\x03",

            "#0000F（ツァイトに相談してみよう。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF51")

    label("loc_AF4E")

    Call(0, 29)

    label("loc_AF51")

    TalkEnd(0xFE)
    Return()

    # Function_27_AD4E end

    def Function_28_AF55(): pass

    label("Function_28_AF55")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_AFEB")
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
    Jump("loc_B0F7")

    label("loc_AFEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B07A")
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
    Jump("loc_B0F7")

    label("loc_B07A")

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

    label("loc_B0F7")

    OP_0D()

    #C0547
    ChrTalk(
        0x101,
        "#11P#0000Fレイモンドさん、こんにちは。\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xB,
        (
            "#5Pやあ、特務支援課の……\x01",
            "今日は本部に用でもあるのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x104,
        (
            "#12P#0304Fフッフッフ……\x01",
            "この期に及んでシラを切るとは\x01",
            "いい度胸じゃねぇか。\x02\x03",

            "#0307F#4S犯人は……アンタだ！！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 500)

    #C0550
    ChrTalk(
        0xB,
        "#5Pえ……ええぇぇぇ！！？？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(500)

    def lambda_B24B():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B24B)

    def lambda_B258():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B258)

    def lambda_B265():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B265)
    Sleep(500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0551
    ChrTalk(
        0x101,
        (
            "#5P#0006Fランディ……\x01",
            "悪ふざけはやめろって。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x103,
        "#11P#0203F……くだらなすぎです。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0553
    ChrTalk(
        0x104,
        (
            "#12P#0306Fちぇっ、警察官なら\x01",
            "一度は言ってみたいセリフだろーが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0554
    ChrTalk(
        0xB,
        (
            "#5Pえ、えっと……\x01",
            "一体なんなんだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B354():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B354)

    def lambda_B361():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B361)

    def lambda_B36E():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B36E)

    def lambda_B37B():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B37B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0555
    ChrTalk(
        0x102,
        (
            "#12P#0103Fコホン……\x01",
            "実は、図書館の方から\x01",
            "支援要請がありまして。\x02\x03",

            "#0100Fレイモンドさん、\x01",
            "図書館の本を借りたままに\x01",
            "していませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0556
    ChrTalk(
        0xB,
        (
            "#5Pあぁ、ハイハイ！\x01",
            "そういえばそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xB,
        "#5P……うん、確かそうだよ。\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xB,
        "#5P借りた借りた……はは。\x02",
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
            "#11P#0006F……あ、あの。\x02\x03",

            "#0012Fもしかして……\x01",
            "本を失くしたりなんてことは……\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xB,
        (
            "#5Pえ、ええっと……\x01",
            "そんなことは、ない、と、思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x103,
        "#11P#0211Fなぜ疑問系……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B5E2")
    TurnDirection(0xA, 0xB, 500)

    #C0564
    ChrTalk(
        0xA,
        (
            "#11P……レイモンド。\x01",
            "さっさと探してこい。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0565
    ChrTalk(
        0xB,
        "#5Pは、はいー！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_B628")

    label("loc_B5E2")


    #C0566
    ChrTalk(
        0xB,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xB,
        "#5P……ちょ、ちょっと探してくるよ！\x02",
    )

    CloseMessageWindow()

    label("loc_B628")

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
            "#5P……あった……あったよ！\x01",
            "はいこれ！\x02",
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
            "を受け取った。\x02",
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
            "#11P#0003Fは、はぁ……\x01",
            "とりあえず、よかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x104,
        "#12P#0306Fヒヤヒヤさせやがるぜ。\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x102,
        (
            "#12P#0105Fしかし、何でまたこの本を……？\x02\x03",

            "確か、大きな功績を残した女性の\x01",
            "エピソードが書かれた本でしたよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xB,
        (
            "#5Pんー、大陸的な美人を集めた\x01",
            "グラビア写真集か何かと思っててさ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xB,
        (
            "#5P思ってたのと違ってて、\x01",
            "そのまま机の奥底にしまって\x01",
            "忘れてたんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x103,
        (
            "#11P#0206F……図書館にそんな本が\x01",
            "あるとは普通、思いませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        (
            "#11P#0012Fま、まぁ……\x01",
            "こうして本を無事回収できたし\x01",
            "結果オーライってことにしようか。\x02\x03",

            "#0000Fレイモンドさん、\x01",
            "ご協力ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xB,
        "#5Pいえいえ、どーいたしまして。\x02",
    )

    CloseMessageWindow()
    OP_29(0x5, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B94F")
    OP_29(0x5, 0x1, 0x1F)

    label("loc_B94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B972")
    SetChrPos(0x0, -12300, 0, 11000, 0)
    OP_4C(0xA, 0xFF)
    Jump("loc_B9A6")

    label("loc_B972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B995")
    SetChrPos(0x0, -125400, 0, 18000, 0)
    OP_4C(0xA, 0xFF)
    Jump("loc_B9A6")

    label("loc_B995")

    SetChrPos(0x0, -11000, 0, 12500, 0)

    label("loc_B9A6")

    EventEnd(0x5)
    Return()

    # Function_28_AF55 end

    def Function_29_B9A9(): pass

    label("Function_29_B9A9")

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
        "#5Pない、ない、ない……！\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x12,
        "#5Pううむ、一体どこに……\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x12, 0xB4, 0x2EE)
    Sleep(750)

    #C0580
    ChrTalk(
        0x12,
        "#5Pム、特務支援課……\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x12,
        (
            "#5Pフン、さっさと行きたまえ。\x01",
            "私は今忙しいんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x101,
        (
            "#11P#0005Fはあ……それはお邪魔しました。\x01",
            "（あれ、この匂い……酒か？）\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x104,
        (
            "#12P#0306Fなんかイラついてる\x01",
            "みてえだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        (
            "#0203F好き好んで叱られる\x01",
            "シュミはありません。\x01",
            "さっさと行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-59280, 1700, 16460, 2000)
    MoveCamera(77, 25, 0, 2000)

    def lambda_BBCA():
        OP_97(0x104, 0xFFFFF736, 0x0, 0xFFFFF736, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BBCA)
    Sleep(50)

    def lambda_BBE7():
        OP_97(0x103, 0xFFFFF830, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BBE7)
    Sleep(50)

    def lambda_BC04():
        OP_97(0x102, 0xFFFFF92A, 0x0, 0xFFFFF92A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BC04)
    Sleep(50)

    def lambda_BC21():
        OP_97(0x101, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC21)
    Sleep(200)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x12, 0xE1, 0x2EE)

    #C0585
    ChrTalk(
        0x12,
        "#5Pま、待ちたまえ。\x02",
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

    def lambda_BCE9():
        TurnDirection(0x101, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCE9)

    def lambda_BCF6():
        TurnDirection(0x102, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BCF6)

    def lambda_BD03():
        TurnDirection(0x103, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BD03)

    def lambda_BD10():
        TurnDirection(0x104, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BD10)
    Sleep(500)

    #C0586
    ChrTalk(
        0x12,
        (
            "#5P君たち、どこかで\x01",
            "『指輪』を見かけなかったかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x12,
        (
            "#5P紅耀石#6Rカーネリア#をあしらった\x01",
            "結婚指輪だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x101,
        (
            "#12P#0005F結婚指輪、ですか？\x01",
            "（何だか意外な話だな……）\x02\x03",

            "#0000F……ええと、エリィはどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x102,
        (
            "#12P#0103Fいえ、私も特に\x01",
            "覚えはないけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x104,
        "#12P#0300F俺もねえな。\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x103,
        (
            "#11P#0200F同じくです。\x01",
            "……結婚指輪を\x01",
            "失くしてしまったのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x12,
        "#5Pうぐっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x12, 1, 0, 30)
    Sleep(500)

    #C0593
    ChrTalk(
        0x12,
        (
            "#5Pあ、あああ……\x01",
            "もしこの事があいつに知られたら……\x02",
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
        "#5Pゾゾッ……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x12, 1, 0, 30)
    Sleep(500)

    #C0595
    ChrTalk(
        0x101,
        (
            "#12P#0003F（副局長……恐妻家みたいだな。）\x02\x03",

            "#0000Fあの、もう少し具体的な話を\x01",
            "してもらえれば、心当たりが\x01",
            "あるかもしれませんが……\x02",
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
        "#5Pうむむ、ほ、本当か？\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x12,
        (
            "#5P……ゴホン。\x01",
            "なんという事はない。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x12,
        (
            "#5P昨晩のうちに、その、\x01",
            "結婚指輪を落としてしまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x12,
        "#5P……どこを探してもない！\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x12,
        (
            "#5Pこうなったらやはり、\x01",
            "歓楽街で落としたとしか……\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        "#12P#0105F……歓楽街………？\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x12,
        (
            "#5Pそんな顔をするんじゃない。\x01",
            "気晴らしに飲みに行っただけだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x12,
        (
            "#5P後はカジノでルーレットに興じて、\x01",
            "そこから帰ったのだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0604
    ChrTalk(
        0x12,
        (
            "#5P……そうだ、あの時は\x01",
            "確かに身に付けていたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x12,
        (
            "#5P#5P少し酔ってはいたが《バルカ》という\x01",
            "カジノハウスを出た所までは覚えている。\x01",
            "間違いない！！\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x103,
        "#11P#0200Fそこから先の記憶は？\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x12,
        "#5Pフン、全くない！\x02",
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
            "#12P#0306F（相当泥酔してたっぽいぜ？\x01",
            "  まだ酒の匂いが抜けきってねえし。）\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        (
            "#12P#0101F（小さな指輪を\x01",
            "  街中で落としたとなると……\x01",
            "  ほとんど無理でしょうね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        (
            "#12P#0006F（ああ、酒に飲まれた\x01",
            "  副局長の責任としか……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0611
    ChrTalk(
        0x101,
        (
            "#12P#0000F副局長、すみませんが……\x01",
            "ハンカチか何かを\x01",
            "お持ちではありませんか？\x02\x03",

            "失くされた結婚指輪のために\x01",
            "しばらくお借りしたいのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x12,
        (
            "#5Pむむ……？\x01",
            "心当たりでもあるのかね？\x02",
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
            "を受け取った。\x02",
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
        "#12P#0000Fありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x103,
        (
            "#11P#0205F（ロイドさん、\x01",
            "  どういうつもりですか？\x01",
            "  そんな物を駆り出して……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0616
    ChrTalk(
        0x101,
        (
            "#5P#0000F（いや……ツァイトの鼻を使えば\x01",
            "  探し出せるかもと思ってさ。）\x02",
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
            "#5P#0000F（困っているみたいだし\x01",
            "  後でツァイトに\x01",
            "  相談してみないか？）\x02",
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
            "クエスト【失くした結婚指輪】\x07\x00",
            "を開始した！\x02",
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

    # Function_29_B9A9 end

    def Function_30_C6BC(): pass

    label("Function_30_C6BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C70E")
    OP_95(0x12, -57800, 0, 19000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0x5A, 0x1F4)
    Sleep(500)
    OP_95(0x12, -56800, 0, 19000, 2000, 0x0)
    Sleep(500)
    OP_93(0x12, 0x10E, 0x1F4)
    Sleep(500)
    Jump("Function_30_C6BC")

    label("loc_C70E")

    Return()

    # Function_30_C6BC end

    def Function_31_C70F(): pass

    label("Function_31_C70F")

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

    # Function_31_C70F end

    def Function_32_C79A(): pass

    label("Function_32_C79A")

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
            "#5P#1905Fあ、みなさん。\x01",
            "それにお姉ちゃん！\x02\x03",

            "#1900Fあの遺跡の調査の件で\x01",
            "何かあったんですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x109,
        (
            "#11P#0500Fえっと……\x01",
            "そういうわけじゃあ\x01",
            "ないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x101,
        "#12P#0000Fフラン、今回は君に用があるんだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0622
    ChrTalk(
        0x9,
        (
            "#5P#1905F私に……？\x01",
            "一体どんな用ですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        (
            "#12P#0003F少し立て込んだ話なんだけど……\x02\x03",

            "#0000Fこの間の記念祭で、\x01",
            "フランらしき人に助けられたっていう\x01",
            "外国人の男性がいてね。\x02\x03",

            "最終日に一緒に\x01",
            "サイフを捜した人のこと……\x01",
            "覚えはあるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x9,
        (
            "#5P#1903Fサイフ……ですか？\x01",
            "ん～………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0625
    ChrTalk(
        0x9,
        (
            "#5P#1900Fあぁ、覚えてます、覚えてます！\x02\x03",

            "たしか、リベールからの\x01",
            "旅行者の人でしたよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x102,
        (
            "#6P#0100Fやっぱりフランさんの事\x01",
            "だったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x9,
        (
            "#5P#1900Fあの日は大変でしたよ～。\x02\x03",

            "#1904Fお仕事の帰りに\x01",
            "泣きそうな顔の男の人がいて、\x01",
            "なんだか放っておけなくて。\x02\x03",

            "#1900Fあの方のサイフを捜す為に\x01",
            "暗くなるまでクロスベル中を\x01",
            "歩いたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x104,
        (
            "#0309Fいやぁ、さすがフランちゃんだなぁ。\x01",
            "見ず知らずの男のために、\x01",
            "なかなかできることじゃないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x9,
        (
            "#5P#1909Fえへへ、これでも\x01",
            "警察官ですからね。\x02\x03",

            "#1903F警察に届けがないか\x01",
            "何度も確認してみたり……\x02\x03",

            "#1900F結局、宿のベッドの下に\x01",
            "落ちていたのが分かって\x01",
            "一安心でしたけど。\x02",
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
        "#12P#0203Fとんだ人騒がせですね……\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x9,
        (
            "#5P#1900Fえっと、それで……\x01",
            "その人がどうしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x109,
        (
            "#11P#0503F……実はその男の人、\x01",
            "アントンさんっていうんだけど……\x02\x03",

            "#0500F記念祭が終わった今も\x01",
            "クロスベルに滞在しているの。\x02\x03",

            "フランにどうしても\x01",
            "お礼を言いたくて、\x01",
            "ずっと捜していたんだって。\x02\x03",

            "だから、ロイドさんたちに\x01",
            "捜して欲しいって言う\x01",
            "依頼が入っていたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x9,
        (
            "#5P#1900Fえ、そうなんですか～？\x01",
            "なんだか照れちゃいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれで……\x01",
            "フランの方はどうだい？\x02\x03",

            "#0003F会いたくなければ\x01",
            "断る事だってできると思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x9,
        (
            "#5P#1900F……えっと、会うのは\x01",
            "全然構いませんよ？\x02",
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
        "#11P#0505F……そうなの？\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x102,
        (
            "#6P#0105F私たちの仕事だからって\x01",
            "無理に手伝ってくれなくても\x01",
            "いいのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x9,
        (
            "#5P#1900Fいえいえ、私も個人的に\x01",
            "お話してみたいんです。\x02\x03",

            "#1909Fふふ、あの時の話で\x01",
            "盛り上がれそうですし～。\x02\x03",

            "#1906F……あ～でも、仕事があるから\x01",
            "ちょっと時間は作れないかも\x01",
            "しれませんね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x101,
        (
            "#12P#0003Fううん、\x01",
            "だったら仕方ないか……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)

    #C0640
    ChrTalk(
        0x8,
        "#6P──あの、皆さん。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_68(1600, 1500, 14500, 1500)

    def lambda_D1E0():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D1E0)

    def lambda_D1ED():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D1ED)

    def lambda_D1FA():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D1FA)

    def lambda_D207():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D207)

    def lambda_D214():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D214)

    def lambda_D221():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D221)
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
        "#11P#1905Fなんですか、レベッカさん？\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x8,
        (
            "#6Pすみません、話に割りこんで\x01",
            "しまいますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x8,
        (
            "#6Pフランはもうちょっとで休憩ですし、\x01",
            "休憩時間中にどこかで会う\x01",
            "約束をしてはどうでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x9,
        "#11P#1905Fえっ、いいんですか？\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x8,
        (
            "#6P勤務中なので多少\x01",
            "イレギュラーですけど、\x01",
            "会う時間くらいはあると思います。\x02\x03",

            "休憩時間だけなら\x01",
            "私だけでも充分ですし。\x02",
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
            "#11P#0506F（レベッカさん……\x01",
            "  なんだか楽しんでるような。）\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x9,
        (
            "#11P#1900Fふふ、せっかくだし\x01",
            "甘えさせてもらいますね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D43C():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D43C)

    def lambda_D449():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D449)

    def lambda_D456():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D456)

    def lambda_D463():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D463)

    def lambda_D470():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D470)

    def lambda_D47D():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D47D)
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
            "#5P#1900Fそれじゃ、待ち合わせですけど……\x01",
            "中央広場のレストラン\x01",
            "《ヴァンセット》でいいですか？\x02\x03",

            "あと少ししたら向かいますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそ、それじゃあ……\x01",
            "本当にいいんだな？\x02\x03",

            "#0000Fアントンさんにも\x01",
            "そういう風に伝えるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x9,
        (
            "#5P#1909Fふふ、楽しみにしてますねって\x01",
            "言っておいてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x109,
        (
            "#11P#0501F（フラン……\x01",
            "  まさかアントンさんに\x01",
            "  気があるのかしら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x104,
        (
            "#12P#0305F……ん、どうしたノエル。\x01",
            "なんだか考え込んでるようだが……\x02",
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
            "#11P#0503Fな、なんでもありません、先輩。\x02\x03",

            "#0500Fロイドさん、それじゃあ……\x01",
            "アントンさんのところに\x01",
            "報告に戻りましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x101,
        "#12P#0000Fああ、そうしようか。\x02",
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

    # Function_32_C79A end

    def Function_33_D746(): pass

    label("Function_33_D746")

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

    def lambda_D7C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D7C6)

    def lambda_D7D7():
        OP_95(0xFE, 0, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D7D7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    #C0655
    ChrTalk(
        0x101,
        (
            "#0000F#4P（クロスベル警察……\x01",
            "  前にも何度か訪ねてるけど……）\x02\x03",

            "#0004F（ここが……\x01",
            "  今日から俺の職場になるんだな。）\x02\x03",

            "#0001F（──さてと。\x01",
            "  まずは受付に挨拶しておこう。）\x02",
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

    # Function_33_D746 end

    def Function_34_D8FB(): pass

    label("Function_34_D8FB")

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
    SetChrName("受付嬢")

    #A0656
    AnonymousTalk(
        0xFF,
        (
            "こんにちはー。\x01",
            "ようこそ、クロスベル警察へ。\x02\x03",

            "どのようなご用件でしょうか？\x02",
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
            "#7P#0005Fあ、いや……\x02\x03",

            "#0003F──今日から\x01",
            "ここで働かせてもらう事になった\x01",
            "ロイド・バニングスといいます。\x02\x03",

            "#0000Fどうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0658
    NpcTalk(
        0x9,
        "受付嬢",
        (
            "#5P#1902Fあ、そうだったんですか。\x02\x03",

            "#1909Fふふっ、嬉しいです。\x01",
            "一緒に働くお仲間が増えて。\x02\x03",

            "#1905Fあれ、でも……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(500)

    #N0659
    NpcTalk(
        0x9,
        "受付嬢",
        (
            "#5P#1903Fうーん、おかしいですね。\x02\x03",

            "今日、新人の方が来るっていう\x01",
            "連絡は受けていないんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(300)

    #N0660
    NpcTalk(
        0x9,
        "受付嬢",
        (
            "#5P#1900Fその、警察本部じゃなくて\x01",
            "警備隊の方ではないですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x101,
        (
            "#7P#0000Fいえ、警察本部で\x01",
            "間違いないと思います。\x02\x03",

            "一応、警察学校の方で\x01",
            "捜査官の資格を貰いましたし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0662
    NpcTalk(
        0x9,
        "受付嬢",
        (
            "#5P#1905Fえ～っ、捜査官試験に\x01",
            "合格されているんですか！？\x02\x03",

            "#1902F凄いですね～！\x01",
            "新人の方では珍しいですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x101,
        (
            "#7P#0012Fい、いや～。\x01",
            "運が良かっただけですよ。\x02\x03",

            "#0002Fそれに今回、試験を受けたのは\x01",
            "自分だけだったみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #N0664
    NpcTalk(
        0x9,
        "受付嬢",
        (
            "#5P#1909Fまたまた～。\x01",
            "謙遜しないでくださいよ。\x02\x03",

            "#1905Fでも、おかしいですね。\x01",
            "だったらこちらにも\x01",
            "連絡が来てるはずですけど……\x02\x03",

            "#1900Fあの、どちらの部署に\x01",
            "配属される予定なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x101,
        (
            "#7P#0006Fはあ、それが……\x02\x03",

            "#0000F『特務支援課』っていう\x01",
            "部署らしいんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #N0666
    NpcTalk(
        0x9,
        "受付嬢",
        "#5P#1905F『特務支援課』……\x02",
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
        "受付嬢",
        (
            "#5P#1901Fえっと……？\x01",
            "そんな部署ありましたっけ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0668
    ChrTalk(
        0x101,
        "#7P#0011F……あの、無いんですか？\x02",
    )

    CloseMessageWindow()

    #N0669
    NpcTalk(
        0x9,
        "受付嬢",
        (
            "#5P#1901Fちょ、ちょっと待ってください。\x02\x03",

            "……どこかでその名前を\x01",
            "聞いた事があるような、無いような。\x02",
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
        "男の声",
        "……おー、来やがったか。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 36)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_E0C6():

        label("loc_E0C6")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_E0C6")

    QueueWorkItem2(0x9, 2, lambda_E0C6)
    Sleep(50)

    def lambda_E0DB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E0DB)
    OP_68(-100, 900, 14000, 4000)
    OP_6F(0x1)

    #N0672
    NpcTalk(
        0x9,
        "受付嬢",
        "#5P#1900Fあ、セルゲイ警部……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 3)
    Sleep(300)

    #N0673
    NpcTalk(
        0x11,
        "無精ヒゲの男",
        (
            "#1000F#6Pフラン。\x01",
            "こいつは俺が引き取ろう。\x02\x03",

            "ウチの新人なんでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x9,
        (
            "#5P#1905Fあ、なるほど……\x02\x03",

            "#1900F警部が立ち上げた\x01",
            "新部署の名前だったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #N0675
    NpcTalk(
        0x11,
        "無精ヒゲの男",
        (
            "#1003F#6Pああ、よろしく頼むわ。\x02\x03",

            "#1002Fま、半年も経たないうちに\x01",
            "無くなってるかもしれんがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x9,
        "#5P#1909Fあ、あはは……\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x101,
        "#11P#0011F……えっと………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("無精ヒゲの男")

    #A0678
    AnonymousTalk(
        0xFF,
        (
            "特務支援課課長、セルゲイ・ロウだ。\x02\x03",

            "ふむ……お前がロイドか。\x02",
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
            "#11P#0001Fは、はい。\x01",
            "ロイド・バニングスです。\x02\x03",

            "クロスベル警察・特務支援課への\x01",
            "着任を報告させて──\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x11,
        "#1003F#6Pああ、それはまだいい。\x02",
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#11P#0005Fえっ……\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x11,
        (
            "#1000F#6P着任報告をするのは\x01",
            "まだ早いと言っている。\x02\x03",

            "付いて来い。\x01",
            "他の連中を紹介しよう。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 37)
    Sleep(1000)

    #C0683
    ChrTalk(
        0x101,
        "#11P#0005Fえ、あ……？\x02",
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
            "#5P#1909Fえ～っと……\x01",
            "その、頑張ってくださいね？\x02\x03",

            "#1901F色々大変だとは思いますけど\x01",
            "ガッツがあれば大丈夫ですよ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    #C0685
    ChrTalk(
        0x101,
        (
            "#7P#0012Fは、はあ……\x01",
            "（激しく不安だ……）\x02",
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

    def lambda_E591():
        OP_95(0xFE, -26000, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E591)
    Sleep(50)

    def lambda_E5AE():
        OP_95(0xFE, -24500, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E5AE)
    PlayBGM("ed7111", 0)
    OP_68(-25500, 1000, 10000, 6000)
    SetCameraDistance(20000, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x11, 1)

    def lambda_E5F4():
        OP_95(0xFE, -26000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E5F4)
    WaitChrThread(0x101, 1)

    def lambda_E612():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E612)
    WaitChrThread(0x11, 1)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_E638():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_E638)

    def lambda_E649():
        OP_95(0xFE, -26000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E649)
    Sleep(500)

    def lambda_E666():
        OP_95(0xFE, -26000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E666)
    WaitChrThread(0x101, 1)

    def lambda_E684():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E684)

    def lambda_E695():
        OP_95(0xFE, -26000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E695)
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

    def lambda_E9BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E9BB)

    def lambda_E9CC():
        OP_95(0xFE, -65000, 0, 13500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E9CC)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)
    SetChrName("娘")

    #N0686
    NpcTalk(
        0x102,
        "娘",
        "#0105Fあら……\x02",
    )

    CloseMessageWindow()
    SetChrName("赤毛の青年")

    #N0687
    NpcTalk(
        0x104,
        "赤毛の青年",
        (
            "#5P#0300Fおっと。\x01",
            "おいでなすったようだな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("黒衣の少女")

    #N0688
    NpcTalk(
        0x103,
        "黒衣の少女",
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
            "#1000F#5P待たせたな。\x01",
            "こいつが最後のメンバーだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    #C0690
    ChrTalk(
        0x11,
        "#1000F#5Pおい、自己紹介。\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x101,
        "#11P#0005Fあ、はい。\x02",
    )

    CloseMessageWindow()

    def lambda_EB46():
        OP_95(0xFE, -58500, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EB46)
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
            "#0001F#11P（あれ……\x01",
            "  先輩にしては顔触れが……）\x02\x03",

            "（同じ新人……？\x01",
            "  いや、それにしたって\x01",
            "  若すぎる子もいるような……）\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x11,
        (
            "#1000F#5Pおい、どうした？\x02\x03",

            "名前と出身だけでいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x101,
        "#0005F#11Pす、すみません。\x02",
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
            "──ロイド・バニングス。\x01",
            "ここクロスベル市の出身です。\x02\x03",

            "しばらくの間、外国で\x01",
            "暮らしていたんですけど……\x02\x03",

            "この度、警察に入るにあたり\x01",
            "戻ってくることになりました。\x02\x03",

            "これから宜しくお願いします。\x02",
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
    SetChrName("赤毛の青年")

    #N0696
    NpcTalk(
        0x104,
        "赤毛の青年",
        "#6P#0302Fおーおー、真面目だねぇ。\x02",
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
    SetChrName("赤毛の青年")

    #A0697
    AnonymousTalk(
        0xFF,
        (
            "俺はランディ。\x01",
            "ランディ・オルランドだ。\x02\x03",

            "趣味はナンパ、ギャンブル、\x01",
            "グラビア雑誌の鑑賞って所だ。\x02\x03",

            "あとでお前さんには\x01",
            "俺の秘蔵コレクションから\x01",
            "取っておきを貸してやるよ。\x02",
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
        "#0011F#11Pええっ……！？\x02",
    )

    CloseMessageWindow()
    SetChrName("娘")

    #N0699
    NpcTalk(
        0x102,
        "娘",
        "#5P#0103F……コホン。\x02",
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
    SetChrName("娘")

    #A0700
    AnonymousTalk(
        0xFF,
        (
            "──初めまして。\x01",
            "エリィ・マクダエルです。\x02\x03",

            "あなたと同じ\x01",
            "クロスベル市の出身です。\x02\x03",

            "よろしくお願いしますね。\x02",
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
        "#0005F#11Pあ、ああ……\x02",
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
    SetChrName("黒衣の少女")

    #A0702
    AnonymousTalk(
        0xFF,
        (
            "ティオ・プラトー。\x01",
            "レマン自治州から来ました。\x02\x03",

            "……よろしく。（ペコリ）\x02",
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
        "#0012F#11Pよ、よろしく……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 500)
    Sleep(300)

    #C0704
    ChrTalk(
        0x101,
        "#12P#0011Fえっと、セルゲイ課長……？\x02",
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x11,
        "#1000F#5Pん、なんだ？\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x101,
        (
            "#12P#0001F『特務支援課』というのは\x01",
            "一体どういう場所なんですか？\x02\x03",

            "その……自分も含めて\x01",
            "ずいぶん若い顔触れのような。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x11,
        (
            "#1004F#5Pま、色々あってな。\x02\x03",

            "ちなみに全員、お前と同じく\x01",
            "期待のルーキーばっかりだ。\x02\x03",

            "#1002Fクク、気楽でいいだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        "#12P#0011Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x102,
        "#5P#0106F……いいのかしら。\x02",
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x104,
        (
            "#6P#0309Fま、口やかましい先輩が\x01",
            "いないってのは有難いねぇ。\x02",
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
            "#12P#0006F（な、なんだこの状況……）\x02\x03",

            "#0001F（何だか無性に\x01",
            "  不安になってきたぞ……）\x02",
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
            "#1005F#5Pこちらセルゲイ……\x02\x03",

            "#1002F……おお、ご苦労さん。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0714
    ChrTalk(
        0x101,
        (
            "#12P#0005F（あれは、携帯用の通信端末？）\x02\x03",

            "（そんなものまで\x01",
            "  実用化されているのか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x11,
        (
            "#1004F#5P……ああ、了解だ。\x02\x03",

            "#1002Fそれじゃあ\x01",
            "後始末の方は任せてくれ。\x02",
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
            "#5P#1003Fよし、喜べルーキーども。\x02\x03",

            "#1002Fこの『特務支援課』が\x01",
            "どんな仕事をするのか……\x02\x03",

            "これから素敵な場所で\x01",
            "じっくりと体験させてやろう。\x02",
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

    # Function_34_D8FB end

    def Function_35_F600(): pass

    label("Function_35_F600")

    #Sound(2080, 255, 100, 0)    #voice#Fran
    Sleep(1000)
    #Sound(2081, 255, 100, 0)    #voice#Fran
    Return()

    # Function_35_F600 end

    def Function_36_F610(): pass

    label("Function_36_F610")


    def lambda_F615():
        OP_95(0xFE, -5000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F615)
    WaitChrThread(0x11, 1)

    def lambda_F633():
        OP_95(0xFE, -2000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F633)
    WaitChrThread(0x11, 1)
    Return()

    # Function_36_F610 end

    def Function_37_F64D(): pass

    label("Function_37_F64D")

    OP_92(0x11, 0xFFFFEC78, 0x2AF8, 0x1F4)

    def lambda_F65F():
        OP_95(0xFE, -5000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F65F)
    WaitChrThread(0x11, 1)

    def lambda_F67D():
        OP_95(0xFE, -13000, 0, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F67D)
    WaitChrThread(0x11, 1)
    Return()

    # Function_37_F64D end

    def Function_38_F697(): pass

    label("Function_38_F697")

    OP_93(0x11, 0x59, 0x1F4)

    def lambda_F6A3():
        OP_95(0xFE, -58000, 0, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F6A3)
    WaitChrThread(0x11, 1)

    def lambda_F6C1():
        OP_95(0xFE, -58000, 0, 20500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F6C1)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0xE1, 0x1F4)
    Return()

    # Function_38_F697 end

    def Function_39_F6E2(): pass

    label("Function_39_F6E2")


    def lambda_F6E7():
        OP_95(0xFE, -58000, 0, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6E7)
    Sleep(1000)
    SetChrFlags(0x104, 0x20)

    def lambda_F709():
        OP_96(0xFE, 0xFFFF0FC4, 0x96, 0x3F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F709)

    def lambda_F723():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F723)

    def lambda_F730():
        OP_D3(0xFE, 0x0, 0x0, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_F730)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    SetChrSubChip(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x101, 1)

    def lambda_F769():
        OP_95(0xFE, -58000, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F769)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_39_F6E2 end

    def Function_40_F798(): pass

    label("Function_40_F798")

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

    def lambda_F94F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F94F)

    def lambda_F960():
        OP_96(0xFE, 0xFFFFCBA8, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F960)
    Sleep(600)

    def lambda_F97D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F97D)

    def lambda_F98E():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F98E)
    Sleep(600)

    def lambda_F9AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F9AB)

    def lambda_F9BC():
        OP_96(0xFE, 0xFFFFCBA8, 0x0, 0x3A34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F9BC)
    Sleep(600)

    def lambda_F9D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F9D9)

    def lambda_F9EA():
        OP_96(0xFE, 0xFFFFD120, 0x0, 0x3A34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F9EA)
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

    def lambda_FA4D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FA4D)
    Sleep(50)

    def lambda_FA5D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FA5D)
    Sleep(50)

    def lambda_FA6D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FA6D)
    WaitChrThread(0x103, 2)

    #C0718
    ChrTalk(
        0x104,
        (
            "#5P#0306Fやれやれ……\x01",
            "何か妙なことになったな。\x02\x03",

            "#0301Fしかし配属を\x01",
            "辞退しろと言ったって……\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x102,
        (
            "#12P#0103Fどうやら警察内部でも\x01",
            "色々とあるみたいね……\x02\x03",

            "#0108F噂程度には聞いていたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x103,
        (
            "#5P#0208F……そうですね。\x01",
            "これでは約束が違います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0721
    ChrTalk(
        0x102,
        "#12P#0105Fあら、約束って……？\x02",
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x103,
        (
            "#5P#0203F……いえ、こちらの事です。\x02\x03",

            "#0200Fそれよりもセルゲイ課長は\x01",
            "どちらにいるんでしょう……？\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x104,
        (
            "#5P#0301Fそういや、そうだぜ。\x02\x03",

            "課題を出すだけ出しておいて\x01",
            "出迎えもナシってのはどういう事だ？\x02\x03",

            "#0306Fかわりに嫌味な副局長ってのに\x01",
            "ネチネチ絡まれちまうし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0724
    ChrTalk(
        0x104,
        (
            "#5P#0305Fなんだよ、ロイド。\x01",
            "元気ないじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FCFF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FCFF)
    Sleep(50)

    def lambda_FD0F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FD0F)
    WaitChrThread(0x103, 2)

    #C0725
    ChrTalk(
        0x102,
        (
            "#11P#0108F配属を辞退しろっていうのが\x01",
            "そんなにショックだったの？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0726
    ChrTalk(
        0x101,
        (
            "#6P#0002Fああ、いや……\x02\x03",

            "#0006F……何だか思ってた場所と\x01",
            "ずいぶん違っていたからさ……\x02",
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
        "#5P#0305Fんー……？\x02",
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
        "男の声",
        (
            "#3Pよお、新人ども。\x01",
            "災難だったみてぇだなぁ。\x02",
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

    def lambda_FEC0():
        OP_95(0xFE, -13300, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FEC0)
    Sleep(150)

    def lambda_FEDD():
        OP_95(0xFE, -12000, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_FEDD)
    Sleep(300)
    OP_68(-12700, 1200, 12400, 3500)
    MoveCamera(35, 19, 0, 3500)
    SetCameraDistance(20500, 3500)

    def lambda_FF1F():

        label("loc_FF1F")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_FF1F")

    QueueWorkItem2(0x101, 2, lambda_FF1F)
    Sleep(50)

    def lambda_FF34():

        label("loc_FF34")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_FF34")

    QueueWorkItem2(0x103, 2, lambda_FF34)
    Sleep(50)

    def lambda_FF49():

        label("loc_FF49")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_FF49")

    QueueWorkItem2(0x102, 2, lambda_FF49)
    Sleep(50)

    def lambda_FF5E():

        label("loc_FF5E")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_FF5E")

    QueueWorkItem2(0x104, 2, lambda_FF5E)
    WaitChrThread(0xA, 1)

    def lambda_FF74():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FF74)
    WaitChrThread(0xB, 1)

    def lambda_FF85():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FF85)
    WaitChrThread(0xB, 2)
    OP_6F(0x79)

    #C0731
    ChrTalk(
        0x101,
        "#0005F#5Pあなた方は……\x02",
    )

    CloseMessageWindow()

    #N0732
    NpcTalk(
        0xA,
        "髭面の男性",
        (
            "#12Pドノバンだ。\x01",
            "捜査二課に所属している。\x02",
        )
    )

    CloseMessageWindow()

    #N0733
    NpcTalk(
        0xB,
        "金髪の青年",
        "#4P同じく二課のレイモンドだよ。\x02",
    )

    CloseMessageWindow()

    #N0734
    NpcTalk(
        0xB,
        "金髪の青年",
        (
            "#4Pへ～、噂には聞いてたけど\x01",
            "こんな小さな子までいるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x103,
        "#5P#0211F（…………むっ……………）\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        (
            "#0000F#5P……初めまして。\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x102,
        "#5P#0100Fエリィ・マクダエルです。\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x104,
        (
            "#5P#0300Fランディ・オルランド。\x01",
            "よろしくッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xA,
        (
            "#12Pおう。\x01",
            "ようこそ、クロスベル警察へ。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xA,
        "#12Pそうか、オメーがあの……\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x101,
        "#0005F#5P……えっ…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0742
    ChrTalk(
        0xB,
        "#11P警部……？\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xA,
        "#12P……いや、何でもねえ。\x02",
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xA,
        (
            "#12Pしかしセルゲイのヤツも\x01",
            "無茶なことを考えやがるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0xA,
        (
            "#12Pこんな新人どもばかり集めて\x01",
            "市民どもの人気取りとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x101,
        "#0011F#5Pえっ……\x02",
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x102,
        (
            "#5P#0105Fそれは……\x01",
            "いったいどういう事ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0xA,
        (
            "#12Pなんだ……\x01",
            "まだ話を聞いてないのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0xA,
        (
            "#12Pうーん。\x01",
            "マズイ事を言っちまったか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)
    Sleep(300)

    #C0750
    ChrTalk(
        0xB,
        (
            "#4Pいや～、しかし君たちも\x01",
            "貧乏クジを引いちゃったよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0xB,
        (
            "#4P大変そうな割には報われなさそうだし\x01",
            "僕だったら辞退してるだろうなぁ。\x02",
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
            "#6Pオメーはもうちょっと\x01",
            "根性入れた方がいいじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0xA,
        (
            "#6P今からでもセルゲイのところに\x01",
            "預けてやってもいいんだぞ？\x02",
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
            "#11Pや、やだなぁ警部。\x01",
            "カンベンしてくださいよ～。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    Sleep(300)

    #C0756
    ChrTalk(
        0xA,
        (
            "#12Pま、大変だとは思うが\x01",
            "セルゲイに付き合うかどうか、\x01",
            "一応考えてみてやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xA,
        (
            "#12Pただ、無理はすんなよ？\x01",
            "何だったらまとめてニ課で\x01",
            "引き取ってもいいからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x101,
        "#0012F#5Pど、どうも……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 500)

    #C0759
    ChrTalk(
        0xB,
        "#4Pそれじゃ、頑張ってね～。\x02",
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0xB,
        (
            "#4Pあ、エリィちゃんだっけ？\x01",
            "今度一緒に食事でもどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0xB,
        "#4P実はいいレストランを見つけて──\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0xB, 500)

    def lambda_10601():
        OP_95(0xFE, -12500, 0, 10400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10601)
    WaitChrThread(0xA, 1)

    def lambda_1061F():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1061F)

    def lambda_10638():
        OP_96(0xFE, 0xFFFFCC0C, 0x0, 0x28A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10638)
    Sound(819, 0, 100, 0)
    WaitChrThread(0xA, 1)

    #C0762
    ChrTalk(
        0xA,
        "#6Pオラ、とっとと行くぞ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0763
    ChrTalk(
        0xB,
        (
            "#11Pあいた！\x01",
            "単なる社交辞令ですってば～。\x02",
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
            "#11P#0306Fはー、何だか知らんが\x01",
            "散々な言われようだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x103,
        (
            "#5P#0206F……貧乏クジはともかく\x01",
            "大変そうなのはイヤかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x102,
        (
            "#12P#0106Fとにかく課長本人から\x01",
            "詳細を聞いてみないと……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0768
    ChrTalk(
        0x102,
        (
            "#11P#0101F受付で聞けば\x01",
            "どこに居るか分かるかしら？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0769
    ChrTalk(
        0x101,
        "#6P#0008Fあ……うん、そうだな──\x02",
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_108BD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_108BD)
    Sleep(50)

    def lambda_108CD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_108CD)
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
            "#0001Fもしもし。\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0771
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おー、キツネの小言と\x01",
            "嫌味は終わったみてーだな。\x02\x03",

            "なかなかウンザリするだろ？\x02",
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
            "#0006Fええ、それはもう……\x02\x03",

            "#0013F──じゃなくて！\x01",
            "一体どこにいるんですか！？\x02\x03",

            "警察本部で待ってるって\x01",
            "言ってたじゃないですか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0773
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、お前らの荷物が届いたから\x01",
            "引越し屋に立ち会ってたんだ。\x02\x03",

            "なかなか親切な上司だろう？\x02",
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
            "#0005F荷物って……\x01",
            "ひょっとして寮ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0775
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、詳しい話は\x01",
            "そこで改めてしてやろう。\x02\x03",

            "待ってるからとっとと来い。\x02",
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
            "#0006Fふう……分かりましたよ。\x02\x03",

            "#0001Fそれで、寮っていうのは\x01",
            "いったい何処にあるんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0777
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、正確には寮じゃないぞ。\x02",
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
            "#0011Fへ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0779
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "正確には、クロスベル警察、\x01",
            "『特務支援課・分室ビル』だ。\x02\x03",

            "そこの２階と３階が、\x01",
            "お前たちの部屋になっている。\x07\x00\x02",
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

    # Function_40_F798 end

    def Function_41_10D5E(): pass

    label("Function_41_10D5E")


    def lambda_10D63():
        OP_95(0xFE, -14600, 0, 11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10D63)
    WaitChrThread(0xA, 1)
    OP_68(-12700, 1000, 14200, 3000)
    MoveCamera(30, 25, 0, 3000)
    SetCameraDistance(22000, 3000)

    def lambda_10DA6():
        OP_95(0xFE, -14600, 0, 17100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10DA6)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_10DCC():
        OP_95(0xFE, -12500, 0, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10DCC)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_10E06():
        OP_95(0xFE, -12500, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10E06)
    Sleep(500)

    def lambda_10E23():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10E23)
    WaitChrThread(0xA, 1)
    Return()

    # Function_41_10D5E end

    def Function_42_10E34(): pass

    label("Function_42_10E34")

    Sleep(600)

    def lambda_10E3C():
        OP_95(0xFE, -14600, 0, 11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10E3C)
    WaitChrThread(0xB, 1)
    Sleep(100)

    def lambda_10E5D():
        OP_95(0xFE, -14600, 0, 17100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10E5D)
    WaitChrThread(0xB, 1)

    def lambda_10E7B():
        OP_95(0xFE, -12500, 0, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10E7B)
    WaitChrThread(0xB, 1)

    def lambda_10E99():
        OP_95(0xFE, -12500, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10E99)
    Sleep(500)

    def lambda_10EB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10EB6)
    WaitChrThread(0xB, 1)
    Sleep(300)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    Return()

    # Function_42_10E34 end

    def Function_43_10EDF(): pass

    label("Function_43_10EDF")

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
        "眼鏡の女性",
        "#5Pあら……\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    #N0781
    NpcTalk(
        0x9,
        "受付嬢",
        "#1905F#5Pあ、ロイドさん！\x02",
    )

    CloseMessageWindow()
    OP_95(0x9, 900, 0, 15400, 2000, 0x0)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0782
    ChrTalk(
        0x101,
        (
            "#0012F#12Pはは……\x01",
            "どうも、こんにちは。\x02\x03",

            "#0000F端末に来ていた連絡を見て\x01",
            "参上したんですが……\x02",
        )
    )

    CloseMessageWindow()

    #N0783
    NpcTalk(
        0x8,
        "眼鏡の女性",
        "#5Pはい、お待ちしていました。\x02",
    )

    CloseMessageWindow()

    #N0784
    NpcTalk(
        0x8,
        "眼鏡の女性",
        (
            "#5P初めまして──\x01",
            "クロスベル警察、受付担当の\x01",
            "レベッカと申します。\x02",
        )
    )

    CloseMessageWindow()

    #N0785
    NpcTalk(
        0x9,
        "受付嬢",
        (
            "#1900F#5P同じく受付担当の\x01",
            "フラン・シーカーです。\x02\x03",

            "#1909Fえへへ、皆さんとは一昨日、\x01",
            "すでに話していますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x101,
        (
            "#0002F#12Pはは、そうだね。\x01",
            "何だかみっともない所を\x01",
            "見せちゃったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x103,
        (
            "#0204F#6P……まあ具体的には\x01",
            "遊撃士に見せ場を奪われた挙句、\x01",
            "副局長のお叱りを受けた訳ですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x101,
        "#0011F#12Pうぐっ……\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x102,
        "#0106F#6Pティ、ティオちゃん……\x02",
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x9,
        (
            "#1909F#5Pあはは……\x01",
            "本当に災難でしたねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x8,
        (
            "#5Pふふ、あまり\x01",
            "気にすることはないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x8,
        (
            "#5P立ち上げたばかりの部署ですから\x01",
            "最初は慣れないこともあるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x8,
        (
            "#5P私たちの方も、皆さんの助けになるよう\x01",
            "可能な限りお手伝いさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x101,
        "#0002F#12Pあ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x104,
        (
            "#0309F#12Pや～、そう言って頂けると\x01",
            "百人力ッスよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x102,
        (
            "#0104F#6Pよろしくお願いします。\x02\x03",

            "#0100Fそれで……支援要請に関する\x01",
            "補足説明をして頂けるそうですが？\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x8,
        (
            "#5Pそうですね。\x01",
            "早速始めさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x8,
        (
            "#5P──まず、皆さんには\x01",
            "専属のオペレーターが\x01",
            "付くことになります。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x8,
        "#5Pこちらのフランですね。\x02",
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x9,
        "#1909F#5Pよろしくお願いしまーす。\x02",
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
        "#0005F#12Pオペレーター……？\x02",
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x102,
        (
            "#0105F#6P例の《エニグマ》を通じて\x01",
            "サポートしていただけるとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x9,
        (
            "#1904F#5Pえっと、現場レベルでの\x01",
            "サポートではなくって……\x02\x03",

            "#1900F主に『支援要請』を達成した時の\x01",
            "報告を処理させていただきます。\x02\x03",

            "《導力ネットワーク》を通じて。\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x104,
        (
            "#0301F#12Pムム、ちょいと話が\x01",
            "難しくなって来やがったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x103,
        (
            "#0203F#6P……要は、わたしたちが\x01",
            "これから片付ける様々な依頼……\x02\x03",

            "#0200Fそれを達成した時の報告を\x01",
            "支援課の端末から導力ネットで\x01",
            "受け付けてくれるという事です。\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x101,
        "#0001F#12Pえっと、それはつまり……\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x102,
        (
            "#0101F#6P警察本部に出頭しなくても\x01",
            "各種報告が出来るわけですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x8,
        (
            "#5Pええ、一連の報告は\x01",
            "その場で査定された上で\x01",
            "特別手当なども支給されます。\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x8,
        (
            "#5Pあと、実績を積まれたら\x01",
            "捜査官としてのランクが上がりますが\x01",
            "それについても連絡できると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x9,
        (
            "#1909F#5Pえへへ……そういった\x01",
            "一連の手続きのオペレーションを\x01",
            "わたしが担当させていただくんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x101,
        "#0004F#12Pなるほど、そういう事か……\x02",
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x104,
        (
            "#0300F#12Pつまり面倒な事務手続きは\x01",
            "あの支援課の端末で\x01",
            "ぜんぶ出来るってことだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x8,
        (
            "#5Pええ、これも導力ネットワークの\x01",
            "試験運用の一環になりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x8,
        (
            "#5Pティオさん。\x01",
            "支援課の端末のセッティングは\x01",
            "もう大丈夫でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x103,
        "#0202F#6Pええ、いつでも報告可能です。\x02",
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x8,
        "#5Pわかりました。\x02",
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x8,
        (
            "#5Pそれでは、最後になりますが\x01",
            "支援要請に関する概要について\x01",
            "改めて説明させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x8,
        (
            "#5P判らないことがあったら\x01",
            "遠慮なく聞いてくださいね？\x02",
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
            "#5Pでは、これを持ちまして\x01",
            "【支援要請の補足説明】を\x01",
            "“達成済み”とさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x9,
        (
            "#1900F#5Pえっと、支援課に戻ったら、\x01",
            "端末から『報告』してみてください。\x02\x03",

            "改めて、新しい支援要請を\x01",
            "そちらの方に送りますから～。\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x101,
        "#0000F#12P分かりました、試してみます。\x02",
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
            "クエスト【支援要請の補足説明】\x07\x00",
            "を達成した！\x02",
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

    # Function_43_10EDF end

    def Function_44_11C9D(): pass

    label("Function_44_11C9D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11CA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12359")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D57")

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【支援要請とは？】\x01",                # 0
            "【どこでチェックするの？】\x01",        # 1
            "【報告はどうすればいいの？】\x01",      # 2
            "【捜査官のランクって？】\x01",          # 3
            "特に聞きたいことはない\x01",            # 4
        )
    )

    MenuEnd(0x1)
    Jump("loc_11DC7")

    label("loc_11D57")


    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【支援要請とは？】\x01",                # 0
            "【どこでチェックするの？】\x01",        # 1
            "【報告はどうすればいいの？】\x01",      # 2
            "【捜査官のランクって？】\x01",          # 3
        )
    )

    MenuEnd(0x1)

    label("loc_11DC7")

    OP_60(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DE6")
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_11DFF")

    label("loc_11DE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DFF")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_11DFF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_11E27"),
        (1, "loc_11F71"),
        (2, "loc_120AD"),
        (3, "loc_121A1"),
        (4, "loc_12326"),
        (SWITCH_DEFAULT, "loc_12335"),
    )


    label("loc_11E27")


    #C0823
    ChrTalk(
        0x8,
        (
            "#5P特務支援課に届けられる\x01",
            "各方面からの様々な“依頼”です。\x02",
        )
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x8,
        (
            "#5P簡単な手伝いから本格的な捜査、\x01",
            "魔獣退治など、様々なタイプの依頼が\x01",
            "来るのではないかと思われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x8,
        (
            "#5P一部の例外を除いて、\x01",
            "実際に引き受けるかどうかは\x01",
            "皆さんにお任せしますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x8,
        (
            "#5P期限内に達成しないと消滅するので\x01",
            "それだけは注意してください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_1233A")

    label("loc_11F71")


    #C0827
    ChrTalk(
        0x8,
        (
            "#5P現在引き受けられる支援要請は、\x01",
            "特務支援課の端末で\x01",
            "チェックすることができます。\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x8,
        (
            "#5P一度チェックすれば、\x01",
            "捜査手帳にも記録されるので\x01",
            "そちらも確認してみてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x8,
        (
            "#5Pなお、支援要請の追加更新は\x01",
            "１日１回を目安にしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x8,
        (
            "#5P日付が変わったら支援課の端末を\x01",
            "確認してみるのをお勧めします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1233A")

    label("loc_120AD")


    #C0831
    ChrTalk(
        0x8,
        (
            "#5P支援要請を“達成”したら\x01",
            "特務支援課の端末から\x01",
            "『報告』を行ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x8,
        (
            "#5P導力ネットワークを通じて\x01",
            "すぐに査定させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x8,
        (
            "#5P内容に応じた特別手当なども\x01",
            "出ますので、こまめに報告されると\x01",
            "よろしいかと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_1233A")

    label("loc_121A1")


    #C0834
    ChrTalk(
        0x8,
        (
            "#5P通常の捜査任務をこなしたり\x01",
            "支援要請を達成していくことで\x01",
            "皆さんの実績は上がっていきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0x8,
        (
            "#5Pこれを『ＤＰ（捜査ポイント）』といい、\x01",
            "各任務や支援要請でどう行動したかで\x01",
            "ボーナスが付くこともあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x8,
        (
            "#5P──ＤＰが規定値に達したところで\x01",
            "『捜査官ランク』が上がります。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x8,
        (
            "#5P現状でランクは１５段階あり、\x01",
            "ランクアップごとに特典もあるので\x01",
            "頑張る価値はあると思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_1233A")

    label("loc_12326")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1233A")

    label("loc_12335")

    Jump("loc_1233A")

    label("loc_1233A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12354")
    FadeToDark(300, 0, 100)
    OP_0D()

    label("loc_12354")

    Jump("loc_11CA7")

    label("loc_12359")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_44_11C9D end

    def Function_45_12364(): pass

    label("Function_45_12364")

    ClearScenarioFlags(0x2, 1)
    ClearScenarioFlags(0x2, 2)
    ClearScenarioFlags(0x2, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12377")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1259A")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_123B6")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_12595")

    label("loc_123B6")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_123EA")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_12595")

    label("loc_123EA")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1241E")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_12595")

    label("loc_1241E")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12452")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_12595")

    label("loc_12452")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12486")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_12595")

    label("loc_12486")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_124BA")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_12595")

    label("loc_124BA")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_124EE")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_12595")

    label("loc_124EE")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12522")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    Jump("loc_12595")

    label("loc_12522")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12559")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    SetScenarioFlags(0x2, 2)
    Jump("loc_12595")

    label("loc_12559")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xEE), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12590")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x2, 1)
    SetScenarioFlags(0x2, 3)
    Jump("loc_12595")

    label("loc_12590")

    Jump("loc_1259A")

    label("loc_12595")

    Jump("loc_12377")

    label("loc_1259A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_1324D")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-900, 1540, 13420, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12624")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0xEF, 300, 40, 13000, 0)
    SetChrPos(0x153, -900, 40, 11800, 0)
    Jump("loc_1274C")

    label("loc_12624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12696")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x109, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_1274C")

    label("loc_12696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12708")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x10A, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_1274C")

    label("loc_12708")

    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)

    label("loc_1274C")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    #C0838
    ChrTalk(
        0x8,
        (
            "あら、皆さん……\x01",
            "戦闘手帳が\x01",
            "大分埋まってきたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x8,
        (
            "魔獣の情報を控えたいので\x01",
            "一度見せてもらっていいでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x101,
        "#0000Fええ、喜んで。\x02",
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
            "ありがとうございました。\x01",
            "手帳を返却しますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x8,
        (
            "こちらは今回の手当てとなります。\x01",
            "どうぞ受け取ってください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12906")

    #A0843
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を1個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_12C7D")

    label("loc_12906")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12969")

    #A0845
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１０００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を2個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_12C7D")

    label("loc_12969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129CC")

    #A0847
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１５００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を3個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_12C7D")

    label("loc_129CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A2F")

    #A0849
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２０００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を4個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_12C7D")

    label("loc_12A2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A92")

    #A0851
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２５００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を5個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_12C7D")

    label("loc_12A92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AF5")

    #A0853
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３０００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を6個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_12C7D")

    label("loc_12AF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B58")

    #A0855
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３５００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を7個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_12C7D")

    label("loc_12B58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BBB")

    #A0857
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４０００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を8個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_12C7D")

    label("loc_12BBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C1E")

    #A0859
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４５００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を9個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_12C7D")

    label("loc_12C1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C7D")

    #A0861
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５０００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "を10個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_12C7D")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CB9")
    Sound(17, 0, 100, 0)

    #A0863
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個、受け取った。\x02",
        )
    )

    AddItemNumber(0x395, 2)
    CloseMessageWindow()
    Jump("loc_12CEA")

    label("loc_12CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12CEA")
    Sound(17, 0, 100, 0)

    #A0864
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x395, 1)
    CloseMessageWindow()

    label("loc_12CEA")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12E17")

    #C0865
    ChrTalk(
        0x8,
        (
            "また魔獣の情報が集まったら\x01",
            "立ち寄ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x101,
        "#0000Fはい、宜しくお願いします。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12DA7")

    #C0867
    ChrTalk(
        0x102,
        "#0100Fまたお邪魔させて頂きますね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E12")

    label("loc_12DA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12DDA")

    #C0868
    ChrTalk(
        0x103,
        "#0200Fまたお邪魔します。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E12")

    label("loc_12DDA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12E12")

    #C0869
    ChrTalk(
        0x104,
        "#0300Fまたお邪魔させてもらうッス。\x02",
    )

    CloseMessageWindow()

    label("loc_12E12")

    Jump("loc_131CA")

    label("loc_12E17")


    #C0870
    ChrTalk(
        0x8,
        (
            "たくさんの情報が集まって……\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0871
    ChrTalk(
        0x8,
        (
            "実は他の捜査官の方にも\x01",
            "お願いしているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0x8,
        (
            "こんなに集めてくださったのは\x01",
            "特務支援課の皆さんだけですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12F20")

    #C0873
    ChrTalk(
        0x104,
        (
            "#0300Fハハ……まあ俺たちは\x01",
            "あちこち出かけてるしなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FC1")

    label("loc_12F20")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12F74")

    #C0874
    ChrTalk(
        0x102,
        (
            "#0100Fあはは……まあ私たちは\x01",
            "あちこち出かけているものね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FC1")

    label("loc_12F74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12FC1")

    #C0875
    ChrTalk(
        0x103,
        (
            "#0200F……まあ、わたし達は\x01",
            "あちこち出かけていますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FC1")


    #C0876
    ChrTalk(
        0x101,
        (
            "#0000F戦闘も頻繁にやっていますし。\x02\x03",

            "……ともかくお役に\x01",
            "立てたみたいで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0877
    ChrTalk(
        0x8,
        "ふふ……やっぱり頼もしいですね。\x02",
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x8,
        (
            "本部に集まった情報も\x01",
            "もう十分だと思いますので、\x01",
            "調査はここまでとさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x8,
        (
            "最後まで付き合っていただいて\x01",
            "ありがとうございました。\x01",
            "今回は特別報酬もお渡ししますね。\x02",
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
            "１００００ミラ\x07\x00",
            "を受け取った。\x02",
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
            "また何かお願いする事が\x01",
            "あるかもしれません。\x01",
            "その時は宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x101,
        (
            "#0000Fええ、こちらこそ。\x01",
            "宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131CA")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131E8")
    Jump("loc_13222")

    label("loc_131E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13205")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_13222")

    label("loc_13205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13222")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_13222")

    label("loc_13222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1322E")
    ClearScenarioFlags(0x2, 0)

    label("loc_1322E")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_1338F")

    label("loc_1324D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13304")

    #C0883
    ChrTalk(
        0x8,
        (
            "本部に集まった情報も\x01",
            "もう十分だと思いますので、\x01",
            "調査はここまでとさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0884
    ChrTalk(
        0x8,
        (
            "また何かお願いする事が\x01",
            "あるかもしれません。\x01",
            "その時は宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1338F")

    label("loc_13304")


    #C0885
    ChrTalk(
        0x8,
        (
            "戦闘手帳の内容も\x01",
            "溜まってきているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x8,
        (
            "もう少し情報が集まったら\x01",
            "私の方に見せてください。\x01",
            "情報を控えさせてもらいますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1338F")

    Return()

    # Function_45_12364 end

    def Function_46_13390(): pass

    label("Function_46_13390")

    EventBegin(0x1)
    Sleep(50)

    #C0887
    ChrTalk(
        0x101,
        (
            "#0005F（おっと……\x01",
            "  外に出てる場合じゃない。）\x02\x03",

            "#0003F（まずは受付で挨拶をして……\x01",
            "  そうだ、配属部署の事も\x01",
            "  聞いてみようかな。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 80, 40, 2480, 0)
    EventEnd(0x4)
    Return()

    # Function_46_13390 end

    def Function_47_13432(): pass

    label("Function_47_13432")

    EventBegin(0x1)
    Sleep(50)

    #C0888
    ChrTalk(
        0x101,
        (
            "#0005F（おっと……\x01",
            "  受付はこっちじゃない。）\x02\x03",

            "#0003F（まずは受付で挨拶をして……\x01",
            "  そうだ、配属部署の事も\x01",
            "  聞いてみようかな。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -6760, 0, 10110, 89)
    EventEnd(0x4)
    Return()

    # Function_47_13432 end

    def Function_48_134D2(): pass

    label("Function_48_134D2")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CA3")
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
        "#0005Fあれ、誰か出てきた。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x12, -12480, 0, 20980, 180)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)

    def lambda_13625():
        OP_95(0xFE, -12480, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_13625)
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
        "#0305F（げげっ……）\x02",
    )

    CloseMessageWindow()

    #C0892
    ChrTalk(
        0x101,
        "#0005F（こ、この人か……）\x02",
    )

    CloseMessageWindow()

    def lambda_136BE():
        OP_95(0xFE, -12480, 0, 18200, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_136BE)
    Sleep(500)

    def lambda_136DB():
        OP_96(0xFE, 0xFFFFCCB6, 0x0, 0x40A6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_136DB)

    def lambda_136F5():
        OP_96(0xFE, 0xFFFFD17A, 0x0, 0x40A6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_136F5)
    Sleep(100)

    def lambda_13712():
        OP_96(0xFE, 0xFFFFCCB6, 0x0, 0x3C14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13712)

    def lambda_1372C():
        OP_96(0xFE, 0xFFFFD17A, 0x0, 0x3C14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1372C)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    #C0893
    ChrTalk(
        0x12,
        (
            "何だね、君達は\x01",
            "こんな所に溜まって……\x02",
        )
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x12,
        (
            "この先は君達のような\x01",
            "日陰者には用のない場所のはずだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0x104,
        "#0306Fそ、そうっすね。\x02",
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0x103,
        "#0200F否定はしませんが……\x02",
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0x12,
        (
            "……そもそも、私の忠告を\x01",
            "聞かなかったのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0898
    ChrTalk(
        0x12,
        (
            "特務支援課など\x01",
            "すぐに辞退しろと言ったろう！\x02",
        )
    )

    CloseMessageWindow()

    #C0899
    ChrTalk(
        0x12,
        (
            "セルゲイの疫病神が\x01",
            "無理矢理作ったにすぎん\x01",
            "くだらん部署など……\x02",
        )
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x12,
        (
            "クズだ。\x01",
            "役立たずだ。\x01",
            "半年で沈むボロ船だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0901
    ChrTalk(
        0x12,
        (
            "まったく、私が善意で\x01",
            "忠告してやったというのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0902
    ChrTalk(
        0x102,
        (
            "#0105Fあ、あのう副局長。\x01",
            "どちらかにお急ぎでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0903
    ChrTalk(
        0x12,
        (
            "フン、そうだった。\x01",
            "お陰で忘れる所だったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-12470, 1500, 15150, 4000)

    def lambda_13982():
        OP_95(0xFE, -12480, 0, 13330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_13982)

    def lambda_1399C():

        label("loc_1399C")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_1399C")

    QueueWorkItem2(0x101, 2, lambda_1399C)

    def lambda_139AE():

        label("loc_139AE")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_139AE")

    QueueWorkItem2(0x102, 2, lambda_139AE)

    def lambda_139C0():

        label("loc_139C0")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_139C0")

    QueueWorkItem2(0x103, 2, lambda_139C0)

    def lambda_139D2():

        label("loc_139D2")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_139D2")

    QueueWorkItem2(0x104, 2, lambda_139D2)

    def lambda_139E4():
        OP_96(0xFE, 0xFFFFCB8A, 0x0, 0x3FAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_139E4)

    def lambda_139FE():
        OP_96(0xFE, 0xFFFFD2A6, 0x0, 0x3FAC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_139FE)
    Sleep(100)

    def lambda_13A1B():
        OP_96(0xFE, 0xFFFFCB8A, 0x0, 0x3B1A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13A1B)

    def lambda_13A35():
        OP_96(0xFE, 0xFFFFD2A6, 0x0, 0x3B1A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13A35)
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
            "いいかね、決して\x01",
            "余計な真似はするなよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0905
    ChrTalk(
        0x12,
        (
            "君たちはただ\x01",
            "市民に見てくれのいい\x01",
            "仕事だけしていればいいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0x12,
        (
            "署内を無断でウロつくな！\x01",
            "自分たちの分室に戻りたまえ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(100)
    OP_95(0x12, -12480, 0, 10350, 2000, 0x0)

    def lambda_13B43():
        OP_95(0xFE, -3890, 0, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_13B43)
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
            "#0006Fえっと……\x01",
            "エレベーターに乗るのは\x01",
            "やめておくか……\x02",
        )
    )

    CloseMessageWindow()

    #C0908
    ChrTalk(
        0x104,
        (
            "#0303Fそうだな、なんつーか……\x01",
            "警察の一員として\x01",
            "認められてないカンジだぜ……\x02",
        )
    )

    CloseMessageWindow()

    #C0909
    ChrTalk(
        0x103,
        (
            "#0200F……特に用事がなければ\x01",
            "上の階にお邪魔するのは\x01",
            "よした方がいいかと。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetScenarioFlags(0x46, 7)
    Jump("loc_13D10")

    label("loc_13CA3")


    #C0910
    ChrTalk(
        0x101,
        (
            "#0003F……上の階に用事はないな……\x02\x03",

            "#0000F副局長に小言を言われたくもないし、\x01",
            "立ち入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_13D9D")

    #C0911
    ChrTalk(
        0x101,
        (
            "#0003F……上の階に用事はないな……\x02\x03",

            "#0000F用もないのに上がっていると\x01",
            "副局長に小言を言われかねない。\x01",
            "立ち入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D9D")

    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_48_134D2 end

    def Function_49_13DB1(): pass

    label("Function_49_13DB1")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14155")

    #C0912
    ChrTalk(
        0x101,
        (
            "#0005Fそういえば……\x01",
            "前から気になってたんだけど。\x02\x03",

            "#0001Fこれって何だ？\x01",
            "何かの装置みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0913
    ChrTalk(
        0x104,
        (
            "#0305Fおお、俺も気になってたぜ。\x02\x03",

            "#0300Fいくつかジュースやらコーヒーやらが\x01",
            "並んでるみたいだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0914
    ChrTalk(
        0x103,
        (
            "#0202Fこれは『導力式自動販売機』です。\x01",
            "お２人は見るのは初めてですか？\x02\x03",

            "#0204Fミラ硬貨を入れると、\x01",
            "その金額に応じた飲料を\x01",
            "買うことが出来ます。\x02\x03",

            "元々エプスタイン財団で開発されたので\x01",
            "あちらの研究施設には\x01",
            "時々置かれているのですが……\x02\x03",

            "#0202Fクロスベルにも実験的に\x01",
            "設置しているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0915
    ChrTalk(
        0x101,
        "#0000Fへー、そうなんだ……\x02",
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x104,
        "#0305Fお嬢は知ってたかよ？\x02",
    )

    CloseMessageWindow()

    #C0917
    ChrTalk(
        0x102,
        (
            "#0104Fううん、私も見るのは初めてね。\x02\x03",

            "#0100Fそれにしても、色々な場所に\x01",
            "エプスタイン財団の装置が\x01",
            "設置されているのね……\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0x103,
        (
            "#0203F何でも、有力なスポンサーが\x01",
            "いると聞いていますが……\x02\x03",

            "#0200F……皆さん、利用するときは\x01",
            "硬貨を使ってください。\x01",
            "紙幣には対応していませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0919
    ChrTalk(
        0x101,
        (
            "#0000Fりょ、了解。\x01",
            "（物珍しいし……\x01",
            "  一度くらい使ってみるか。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143C7")

    label("loc_14155")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0920
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力式の自動販売機がある。\x02",
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
            "#0005Fこれは……確か、硬貨を入れると\x01",
            "飲料が買えるんだったな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14253")

    #C0922
    ChrTalk(
        0x103,
        (
            "#0200Fええ、エプスタイン財団が開発した\x01",
            "自動販売機です。\x02\x03",

            "クロスベルにも実験的に\x01",
            "設置している物ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14390")

    label("loc_14253")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_142F5")

    #C0923
    ChrTalk(
        0x102,
        (
            "#0100Fエプスタイン財団が開発した\x01",
            "自動販売機……だったかしら。\x02\x03",

            "ティオちゃんによれば、\x01",
            "財団が実験的に\x01",
            "クロスベルにも設置しているそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14390")

    label("loc_142F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14390")

    #C0924
    ChrTalk(
        0x104,
        (
            "#0300Fエプスタイン財団が開発した\x01",
            "自動販売機……だったか。\x02\x03",

            "ティオすけによりゃあ、\x01",
            "財団が実験的に\x01",
            "クロスベルにも設置しているそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14390")


    #C0925
    ChrTalk(
        0x101,
        (
            "#0000Fさすがクロスベル……\x01",
            "色んな物があるよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143C7")

    SetScenarioFlags(0x95, 3)
    Jump("loc_143E6")

    label("loc_143CF")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_143E6")

    TalkEnd(0xFF)
    Return()

    # Function_49_13DB1 end

    SaveToFile()

Try(main)
