from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1150.bin",                # FileName
        "c1150",                    # MapName
        "c1150",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 5000, 1500, 0, 0, 1, 24, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1150",                  # 0
        "受付嬢レベッカ",         # 1
        "受付嬢フラン",           # 2
        "ドノバン警部",           # 3
        "レイモンド捜査官",       # 4
        "ダドリー捜査官",         # 5
        "エマ捜査官",             # 6
        "ケイト巡査",             # 7
        "フランツ巡査",           # 8
        "ピエール副局長",         # 9
        "ユーリ",                 # 10
        "サイクス",               # 11
        "レジー",                 # 12
        "ジョーリッジ課長",       # 13
        "国防軍兵士",             # 14
        "国防軍兵士",             # 15
        "警官",                   # 16
        "警官",                   # 17
        "セルゲイ課長",           # 18
        "イス",                   # 19
        "イス",                   # 20
        "イス",                   # 21
        "イス",                   # 22
        "イス",                   # 23
        "イス",                   # 24
        "イス",                   # 25
        "イス",                   # 26
        "SE制御",                 # 27
    ))

    AddCharChip((
        "chr/ch30400.itc",                   # 00
        "chr/ch06900.itc",                   # 01
        "chr/ch30500.itc",                   # 02
        "chr/ch30600.itc",                   # 03
        "chr/ch30000.itc",                   # 04
        "chr/ch06400.itc",                   # 05
        "chr/ch30100.itc",                   # 06
        "chr/ch44102.itc",                   # 07
        "chr/ch47500.itc",                   # 08
        "chr/ch23600.itc",                   # 09
        "chr/ch30002.itc",                   # 0A
        "chr/ch30300.itc",                   # 0B
        "chr/ch30200.itc",                   # 0C
        "chr/ch41400.itc",                   # 0D
        "chr/ch41500.itc",                   # 0E
        "chr/ch00900.itc",                   # 0F
    ))

    DeclNpc(-100,    0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3000,    0,       15930,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   11,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   15,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-125379, 0,       19520,   0,    453,  0x0, 0,   2,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   36,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 0,   37,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   7,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   8,   0,   255, 255, 0,   34,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   9,   0,   255, 255, 0,   35,  255,  0)
    DeclNpc(-58049,  0,       15899,   90,   389,  0x0, 0,   6,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(2990,    0,       11810,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   43,  255,  0)
    DeclNpc(-12409,  0,       19770,   180,  389,  0x0, 0,   14,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(2990,    0,       11810,   270,  389,  0x0, 0,   4,   0,   0,   0,   0,   41,  255,  0)
    DeclNpc(2990,    0,       11810,   270,  389,  0x0, 0,   4,   0,   0,   0,   0,   42,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 56,  -12.699999809265137,   18.8700008392334,      -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.233333587646484,     -9.4350004196167,      0.1428571492433548,    1.0])
    DeclEvent(0x0000, 0, 50,  -8.260000228881836,    10.029999732971191,    -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.130000114440918,     -2.507499933242798,    0.1428571492433548,    1.0])

    DeclActor(-100,    0,       14400,   1100,    -100,    1500,    15400,   0x007E, 0,  5,  0x0000)
    DeclActor(2770,    0,       14280,   1000,    3000,    1500,    15930,   0x007E, 0,  17, 0x0000)
    DeclActor(-9850,   0,       16000,   1000,    -9850,   1500,    16000,   0x007C, 0,  57, 0x0000)
    DeclActor(-9850,   0,       13750,   1000,    -9850,   1500,    13750,   0x007C, 0,  57, 0x0000)

    ChipFrameInfo(1536, 0)                                       # 0

    ScpFunction((
        "Function_0_600",          # 00, 0
        "Function_1_6B8",          # 01, 1
        "Function_2_6E3",          # 02, 2
        "Function_3_736",          # 03, 3
        "Function_4_E7A",          # 04, 4
        "Function_5_F4D",          # 05, 5
        "Function_6_F51",          # 06, 6
        "Function_7_14C4",         # 07, 7
        "Function_8_29FA",         # 08, 8
        "Function_9_2A09",         # 09, 9
        "Function_10_49EF",        # 0A, 10
        "Function_11_4AF6",        # 0B, 11
        "Function_12_5659",        # 0C, 12
        "Function_13_632C",        # 0D, 13
        "Function_14_6CA0",        # 0E, 14
        "Function_15_6D88",        # 0F, 15
        "Function_16_6E7D",        # 10, 16
        "Function_17_7B89",        # 11, 17
        "Function_18_7CED",        # 12, 18
        "Function_19_9C2A",        # 13, 19
        "Function_20_A4AB",        # 14, 20
        "Function_21_ABB8",        # 15, 21
        "Function_22_B30F",        # 16, 22
        "Function_23_BE00",        # 17, 23
        "Function_24_BE26",        # 18, 24
        "Function_25_C639",        # 19, 25
        "Function_26_CC3F",        # 1A, 26
        "Function_27_CF1C",        # 1B, 27
        "Function_28_D3A3",        # 1C, 28
        "Function_29_DD0A",        # 1D, 29
        "Function_30_E2F9",        # 1E, 30
        "Function_31_F476",        # 1F, 31
        "Function_32_F73B",        # 20, 32
        "Function_33_F83B",        # 21, 33
        "Function_34_F943",        # 22, 34
        "Function_35_FA5F",        # 23, 35
        "Function_36_FB77",        # 24, 36
        "Function_37_FEE9",        # 25, 37
        "Function_38_1019C",       # 26, 38
        "Function_39_103E9",       # 27, 39
        "Function_40_10A0C",       # 28, 40
        "Function_41_10AE1",       # 29, 41
        "Function_42_10C4D",       # 2A, 42
        "Function_43_10DC6",       # 2B, 43
        "Function_44_10EC4",       # 2C, 44
        "Function_45_1132D",       # 2D, 45
        "Function_46_127E0",       # 2E, 46
        "Function_47_12D62",       # 2F, 47
        "Function_48_13DFA",       # 30, 48
        "Function_49_13E0D",       # 31, 49
        "Function_50_14568",       # 32, 50
        "Function_51_151EE",       # 33, 51
        "Function_52_15DCB",       # 34, 52
        "Function_53_168D8",       # 35, 53
        "Function_54_16A26",       # 36, 54
        "Function_55_16B23",       # 37, 55
        "Function_56_16EA1",       # 38, 56
        "Function_57_16FE6",       # 39, 57
    ))


    def Function_0_600(): pass

    label("Function_0_600")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_640"),
        (1, "loc_64C"),
        (2, "loc_658"),
        (3, "loc_664"),
        (4, "loc_670"),
        (5, "loc_67C"),
        (6, "loc_688"),
        (SWITCH_DEFAULT, "loc_694"),
    )


    label("loc_640")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_64C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_658")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_664")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_670")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_67C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_688")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_694")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_6A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_6B7")

    Return()

    # Function_0_600 end

    def Function_1_6B8(): pass

    label("Function_1_6B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E2")
    OP_94(0xFE, 0xFFFF8508, 0x24CC, 0xFFFF93C2, 0x288C, 0x3E8)
    Sleep(300)
    Jump("Function_1_6B8")

    label("loc_6E2")

    Return()

    # Function_1_6B8 end

    def Function_2_6E3(): pass

    label("Function_2_6E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_735")
    OP_95(0x10, -57300, 0, 20000, 2000, 0x0)
    Sleep(500)
    OP_93(0x10, 0xB4, 0x2EE)
    Sleep(500)
    OP_95(0x10, -57300, 0, 16000, 2000, 0x0)
    Sleep(500)
    OP_93(0x10, 0x0, 0x2EE)
    Sleep(500)
    Jump("Function_2_6E3")

    label("loc_735")

    Return()

    # Function_2_6E3 end

    def Function_3_736(): pass

    label("Function_3_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_78B")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x17, -57400, 0, 16210, 0)
    SetChrPos(0x18, -57420, 0, 18000, 180)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    Jump("loc_B69")

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7AD")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B69")

    label("loc_7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_838")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -69670, 30, 19510, 315)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -70670, 0, 20710, 135)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -57400, 0, 16210, 0)
    ClearChrFlags(0xF, 0x40)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -57420, 0, 18000, 180)
    ClearChrFlags(0xE, 0x40)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_B69")

    label("loc_838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_85A")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_B69")

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8F2")
    SetChrPos(0xA, -121660, 0, 18190, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -56800, 0, 16000, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -58000, 30, 15910, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -58210, 0, 18000, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x40)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xF, -56700, 0, 18000, 180)
    Jump("loc_B69")

    label("loc_8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_922")
    SetChrPos(0xA, -12180, 0, 7890, 270)
    SetChrPos(0xB, -13680, 0, 7890, 90)
    Jump("loc_B69")

    label("loc_922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_990")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -57400, 0, 16000, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -56700, 0, 18000, 180)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -58210, 0, 18000, 180)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x18, 0x10)
    Jump("loc_B69")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9EA")
    SetChrPos(0xA, -121550, 0, 18180, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -11040, 0, 13810, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E5")
    SetChrFlags(0xD, 0x10)

    label("loc_9E5")

    Jump("loc_B69")

    label("loc_9EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A24")
    SetChrPos(0xA, -57400, 0, 16210, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -57420, 0, 18000, 180)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B69")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A3C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_B69")

    label("loc_A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A9B")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -57400, 0, 16210, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -57420, 0, 18000, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -10590, 0, 15740, 90)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B69")

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_ACE")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -125380, 0, 19520, 0)
    Jump("loc_B69")

    label("loc_ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B28")
    SetChrPos(0xA, -57400, 0, 16210, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -57420, 0, 18000, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B12")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x14, 0x10)

    label("loc_B12")

    SetChrPos(0xB, -125380, 0, 19520, 0)
    Jump("loc_B69")

    label("loc_B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B69")
    SetChrPos(0xA, -11040, 0, 13810, 225)
    SetChrPos(0xB, -12290, 0, 12530, 45)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -10590, 0, 15740, 90)

    label("loc_B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B84")
    SetMapFlags(0x10000000)
    Event(0, 44)

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB5")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -11040, 0, 13810, 90)

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE5")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -57300, 0, 18750, 270)

    label("loc_BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CEA")
    SetChrChipByIndex(0x11, 0x7)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -122270, 100, 16550, 270)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -121780, 0, 18250, 225)
    BeginChrThread(0x12, 0, 0, 0)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -121570, 0, 14770, 315)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -125880, 0, 12690, 0)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -124800, 0, 18080, 135)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xE, 0x40)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -125000, 100, 16550, 90)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x40)

    label("loc_CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DE3")
    SetChrChipByIndex(0x11, 0x7)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -122270, 100, 16550, 270)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -121780, 0, 18250, 225)
    BeginChrThread(0x12, 0, 0, 0)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -121570, 0, 14770, 315)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -125880, 0, 12690, 0)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -124800, 0, 18080, 135)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xE, 0x40)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -125000, 100, 16550, 90)
    ClearChrFlags(0xF, 0x40)

    label("loc_DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_DF7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 45)
    Jump("loc_E50")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E0B")
    ClearScenarioFlags(0x22, 1)
    Event(0, 49)
    Jump("loc_E50")

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_E1F")
    ClearScenarioFlags(0x22, 2)
    Event(0, 51)
    Jump("loc_E50")

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_E33")
    ClearScenarioFlags(0x22, 3)
    Event(0, 55)
    Jump("loc_E50")

    label("loc_E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_E50")
    ClearScenarioFlags(0x22, 4)
    SetChrPos(0x0, -12810, 0, 14970, 180)

    label("loc_E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E79")
    SetMapFlags(0x10000000)
    Event(0, 46)

    label("loc_E79")

    Return()

    # Function_3_736 end

    def Function_4_E7A(): pass

    label("Function_4_E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBF")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EFA")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_EFA")

    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F1B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F28")
    OP_65(0x1, 0x1)

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3A")
    OP_65(0x0, 0x1)

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4C")
    OP_65(0x0, 0x1)

    label("loc_F4C")

    Return()

    # Function_4_E7A end

    def Function_5_F4D(): pass

    label("Function_5_F4D")

    Call(0, 6)
    Return()

    # Function_5_F4D end

    def Function_6_F51(): pass

    label("Function_6_F51")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_12FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FE")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0001
    ChrTalk(
        0x8,
        (
            "あら、皆さんが\x01",
            "お持ちになっているそれは……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "もしかして、『フラグメント』\x01",
            "ではありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00005Fえっと、これのことですか？\x02\x03",

            "#00000F手に入れたはいいものの、\x01",
            "いまいち使い道が\x01",
            "分からなかったんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはレベッカに\x01",
            "フラグメントを見せた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0005
    ChrTalk(
        0x8,
        "まあ、やっぱり……！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "これは、鑑識課の者が探していた\x01",
            "破損した記憶結晶#8Rメモリークオーツ#の修復に\x01",
            "利用できる結晶の欠片です。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "それがあれば、\x01",
            "教団の端末データの一部分を\x01",
            "解析することができるはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1196")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_1196")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11BF")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_11BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E8")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_11E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_120E")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_120E")

    Sleep(1000)

    #C0008
    ChrTalk(
        0x102,
        (
            "#00105Fそ、それじゃあ……\x01",
            "ヨアヒム・ギュンターによって\x01",
            "隠された文章が読めるように……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "ええ、あくまでも一部では\x01",
            "あるそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "すぐに結果が出ると思いますし、\x01",
            "『フラグメント』を鑑識に回しても\x01",
            "よろしいですか？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 9)
    TalkEnd(0x8)
    Return()

    label("loc_12FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1321")
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_1321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1336")
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_1336")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1340")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B3")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x1, 3)
    Call(0, 8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_13C8")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                        # 0
            "戦闘手帳を見せる\x01",                # 1
            "教団の端末データを確認する\x01",      # 2
            "フラグメントを渡す\x01",              # 3
            "やめる\x01",                          # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_1429")

    label("loc_13C8")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                        # 0
            "戦闘手帳を見せる\x01",                # 1
            "教団の端末データを確認する\x01",      # 2
            "やめる\x01",                          # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1429")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1429")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1457")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)
    Jump("loc_14AE")

    label("loc_1457")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 6)
    Call(0, 16)
    Jump("loc_14AE")

    label("loc_147B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149C")
    Call(0, 10)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_149C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AE")
    Call(0, 9)

    label("loc_14AE")

    Jump("loc_1340")

    label("loc_14B3")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    Return()

    # Function_6_F51 end

    def Function_7_14C4(): pass

    label("Function_7_14C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1873")

    #C0011
    ChrTalk(
        0x8,
        "みなさん……お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00000Fレベッカさん、お疲れ様です。\x01",
            "本部にお戻りになったんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "ええ、ケイトさんや\x01",
            "レイモンドさんたちも\x01",
            "通常業務に戻りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "国防軍の指揮系統からも\x01",
            "外れることになりまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "現在は元通り、各々の配置で\x01",
            "事態の収拾に向けて\x01",
            "各方面への対応をしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        "#00300Fふむ、そいつはよかったッスね。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "ふふ、皆さんのおかげです。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "……そうだ、フランに\x01",
            "伝えておいていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "警察の受付のことは任せて、\x01",
            "皆さんの手伝いに専念するようにと。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1720")

    #C0020
    ChrTalk(
        0x109,
        (
            "#10102Fふふ、分かりました。\x01",
            "ちゃんと伝えておきますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175A")

    label("loc_1720")


    #C0021
    ChrTalk(
        0x103,
        (
            "#00202Fふふ、分かりました。\x01",
            "ちゃんと伝えておきます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17A5")

    #C0022
    ChrTalk(
        0x10A,
        (
            "#00600Fレベッカ君、本部の方は\x01",
            "よろしく頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E3")

    label("loc_17A5")


    #C0023
    ChrTalk(
        0x101,
        (
            "#00000Fレベッカさんも、本部の方は\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E3")


    #C0024
    ChrTalk(
        0x8,
        (
            "はい、市民の皆さんのためにも\x01",
            "力を尽くさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "まだ気の抜けない状況は続きますが……\x01",
            "どうかそちらも頑張って下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 3)
    Jump("loc_19D2")

    label("loc_1873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_194A")

    #C0026
    ChrTalk(
        0x8,
        (
            "警察本部も、事態の収拾に向けて\x01",
            "各方面へ対応をしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "フランには、皆さんの手伝いに\x01",
            "専念するよう伝えて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "まだ気の抜けない状況は続きますが……\x01",
            "どうかそちらも頑張って下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_19D2")

    label("loc_194A")


    #C0029
    ChrTalk(
        0x8,
        (
            "警察本部も、事態の収拾に向けて\x01",
            "全力で動いている最中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "まだ気の抜けない状況は続きますが……\x01",
            "どうかそちらも頑張って下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D2")

    Jump("loc_29F9")

    label("loc_19D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19E5")
    Jump("loc_29F9")

    label("loc_19E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADB")

    #C0031
    ChrTalk(
        0x8,
        (
            "今朝突然、本部の方に\x01",
            "国防軍の方が何人もいらっしゃって\x01",
            "そのまま待機を命じられたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "あまりに突然のことで、\x01",
            "何をどう捉えたらいいか\x01",
            "混乱しますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "とにかく今は、会議が終わるのを\x01",
            "待つしかありませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1B5A")

    label("loc_1ADB")


    #C0034
    ChrTalk(
        0x8,
        (
            "あまりに突然のことで、\x01",
            "何をどう捉えたらいいか\x01",
            "混乱しますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "とにかく今は、会議が終わるのを\x01",
            "待つしかありませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B5A")

    Jump("loc_29F9")

    label("loc_1B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B6D")
    Jump("loc_29F9")

    label("loc_1B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C28")

    #C0036
    ChrTalk(
        0x8,
        (
            "ダドリーさんは今日も随分\x01",
            "険しい表情をしておられましたが……\x01",
            "どうにも状況は芳しくないようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "何としても、戦闘以外の解決策を\x01",
            "見出していただきたいものですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_1C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1D19")

    #C0038
    ChrTalk(
        0x8,
        (
            "警備隊の皆さんのおかげで、\x01",
            "大陸横断鉄道は今朝から運行を\x01",
            "完全再開することが出来ました。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "何とか始発に間に合ったので、\x01",
            "特に運行ダイヤの変更も行わずに\x01",
            "済みましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "これぞまさしく、\x01",
            "警備隊の執念といった所ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_1D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1DD9")

    #C0041
    ChrTalk(
        0x8,
        (
            "列車の事故を受けて、\x01",
            "さっそく各方面から様々な\x01",
            "お問い合わせを頂いております。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "振替#4Rふりかえ#輸送の対応も\x01",
            "既に始まっておりますが……\x01",
            "この状況が続くと流石に厄介ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_1DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E95")

    #C0043
    ChrTalk(
        0x8,
        (
            "『プレロマ草』……\x01",
            "教団のデータベースにもあった\x01",
            "グノーシスの原料、ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "そんなものが突然クロスベルの\x01",
            "各地で見つかるなんて……\x01",
            "一体何が起こっているのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_1E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1FC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F69")

    #C0045
    ChrTalk(
        0x8,
        (
            "皆さんは今度の任務で、\x01",
            "遊撃士協会と共闘されるそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "ふふ、まさかギルドと肩を並べて\x01",
            "依頼をこなす日が来るなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "皆さんには、本当に\x01",
            "いつも良い意味で驚かされます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1FBF")

    label("loc_1F69")


    #C0048
    ChrTalk(
        0x8,
        (
            "フランの言う通り、\x01",
            "幻獣の相手は大変だと思いますが……\x01",
            "どうか頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBF")

    Jump("loc_29F9")

    label("loc_1FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2097")

    #C0049
    ChrTalk(
        0x8,
        (
            "２階の警備対策本部には\x01",
            "既にセルゲイ課長が待機しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "本会議の開始時間も\x01",
            "いよいよ迫って来ましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "まずは首脳たちが、\x01",
            "安全に会場入りすることが\x01",
            "最初の関門ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2110")

    label("loc_2097")


    #C0052
    ChrTalk(
        0x8,
        (
            "本会議の開始時間も\x01",
            "いよいよ迫って来ましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "まずは首脳たちが、\x01",
            "安全に会場入りすることが\x01",
            "最初の関門ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2110")

    Jump("loc_29F9")

    label("loc_2115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21CC")

    #C0054
    ChrTalk(
        0x8,
        (
            "私もフランもそれぞれ休憩時間に\x01",
            "オルキスタワーを見て来たのですが……\x01",
            "その迫力には圧倒されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "まさに、クロスベルの新たな\x01",
            "ランドマークに相応しい建物ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_21CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_256F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B4")

    #C0056
    ChrTalk(
        0x8,
        (
            "今回の警備体制は、\x01",
            "警察と警備隊のかつてない\x01",
            "協力体制の元に築かれています。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "従来の組織では、\x01",
            "ここまでの体制を築くことは\x01",
            "不可能だったと思われますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "その最も大きな要因は、\x01",
            "警察に多大な理解を持っておられる\x01",
            "ソーニャ司令の存在だと言えるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#00303F（う～ん、やっぱ\x01",
            "  レベッカさんは美人だよな。）\x02\x03",

            "#00309F（同じ眼鏡でも、盛りを過ぎた\x01",
            "  ソーニャ司令とは大違いだぜ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        (
            "#10106F（はぁ、ランディ先輩……\x01",
            "  司令に言い付けますよ？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x104)

    #C0061
    ChrTalk(
        0x104,
        (
            "#00305F（い、いや、今のは\x01",
            "  言葉のアヤっつうか……）\x02\x03",

            "#00309F（いや～、レベッカさんも美人だけど\x01",
            "  ソーニャ司令には敵わねえよな～。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 7)
    Jump("loc_256A")

    label("loc_24B4")


    #C0062
    ChrTalk(
        0x8,
        (
            "今回の警備体制は、\x01",
            "警察と警備隊のかつてない\x01",
            "協力体制の元に築かれています。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "その最も大きな要因は、\x01",
            "警察に多大な理解を持っておられる\x01",
            "ソーニャ司令の存在だと言えるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256A")

    Jump("loc_29F9")

    label("loc_256F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_274E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BC")

    #C0064
    ChrTalk(
        0x8,
        (
            "前局長が解任になり、\x01",
            "ディーター市長が就任されてから、\x01",
            "警察の体制も大きく変わりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "新たな困難も多々ありますが、\x01",
            "それでも前進していることを実感します。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "今後、皆さんへの期待も\x01",
            "ますます大きくなると思いますが\x01",
            "ぜひとも頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "私たちも全力で\x01",
            "サポートさせていただきますので。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2749")

    label("loc_26BC")


    #C0068
    ChrTalk(
        0x8,
        (
            "今後、皆さんへの期待も\x01",
            "ますます大きくなると思いますが\x01",
            "ぜひとも頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "私たちも全力で\x01",
            "サポートさせていただきますので。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2749")

    Jump("loc_29F9")

    label("loc_274E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 7)), scpexpr(EXPR_END)), "loc_2965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B8")

    #C0070
    ChrTalk(
        0x8,
        (
            "新型魔獣の報告も\x01",
            "増加の傾向にありますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "それらの実態把握と安全対策のため\x01",
            "少しでも多くの情報が欲しいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "これまでと同様、段階的に\x01",
            "多少の手当ても支給されますので、\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "それと、教団の端末のデータも\x01",
            "こちらで確認していただけます。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "確認する場合は\x01",
            "私にお申し付けくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2960")

    label("loc_28B8")


    #C0075
    ChrTalk(
        0x8,
        (
            "戦闘手帳の報告に関しては\x01",
            "多少の手当ても支給されますので、\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "それと、教団の端末のデータを\x01",
            "確認する場合は\x01",
            "私にお申し付けくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2960")

    Jump("loc_29F9")

    label("loc_2965")


    #C0077
    ChrTalk(
        0x8,
        (
            "ふふ、それにしても\x01",
            "一課からの協力要請なんて\x01",
            "皆さんも出世されましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "特務支援課の活躍を\x01",
            "拝見してきた者の一人として\x01",
            "何だか感慨深いです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F9")

    Return()

    # Function_7_14C4 end

    def Function_8_29FA(): pass

    label("Function_8_29FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_2A08")
    SetScenarioFlags(0x1, 3)

    label("loc_2A08")

    Return()

    # Function_8_29FA end

    def Function_9_2A09(): pass

    label("Function_9_2A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_2AA7")

    #C0079
    ChrTalk(
        0x8,
        (
            "あら、『フラグメント』を\x01",
            "持ってきてくださったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "教団の端末データを解析するため、\x01",
            "『フラグメント』を鑑識に回しても\x01",
            "よろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA7")


    #C0081
    ChrTalk(
        0x101,
        "#00000Fええ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "それでは、少々お待ち下さい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_2B00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48D1")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_48CC")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber(0x334, 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B88")
    Sound(9, 0, 100, 0)

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情報端末データ\x01",
            "『教団について』のページ１を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2B88")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE4")
    Sound(9, 0, 100, 0)

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情報端末データ\x01",
            "『教団について』のページ３を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2BE4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C46")
    Sound(9, 0, 100, 0)

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』のページ１を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2C46")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA8")
    Sound(9, 0, 100, 0)

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』のページ２を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2CA8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_356C")
    Sound(9, 0, 100, 0)

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情報端末データ\x01",
            "『教団について』のページ４を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情報端末データ\x01",
            "『教団について』の解析を完了した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    FadeToBright(1000, 0)
    OP_0D()

    #C0089
    ChrTalk(
        0x8,
        (
            "#5P第０１情報端末の全データの\x01",
            "解析が完了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "#5Pさっそく確認してみますか？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#12P#00001Fええ、お願いします。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 11)

    #C0092
    ChrTalk(
        0x8,
        (
            "#5P……このデータには、\x01",
            "教団についての概要が\x01",
            "記載されていたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "#5P女神の否定という教義……\x01",
            "本当に信じられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#12P#00003Fええ……ですが\x01",
            "ヨアヒム・ギュンターの\x01",
            "証言とも一致します。\x02\x03",

            "#00001Fそして、この《Ｄ》という言葉……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30A3")

    #C0095
    ChrTalk(
        0x103,
        (
            "#12P#00203F彼らが女神の代わりに信奉した\x01",
            "《真なる神》を指す言葉なんでしょう。\x02\x03",

            "#00201FＤ∴Ｇ教団の名前にある『Ｇ』が\x01",
            "《真なる叡智#10Rグ ノ ー シ ス#》を指すということは\x01",
            "既に突き止められていますし……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_304E")

    #C0096
    ChrTalk(
        0x105,
        (
            "#12P#10403Fふむ、これで『Ｄ∴Ｇ』の意味も\x01",
            "ようやく判明したと言えそうだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_309E")

    label("loc_304E")


    #C0097
    ChrTalk(
        0x105,
        (
            "#12P#10303Fふむ、これで『Ｄ∴Ｇ』の意味も\x01",
            "ようやく判明したと言えそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_309E")

    Jump("loc_31AC")

    label("loc_30A3")


    #C0098
    ChrTalk(
        0x103,
        (
            "#12P#00200F彼らが女神の代わりに信奉した\x01",
            "《真なる神》を指す言葉なんでしょう。\x02\x03",

            "#00201FＤ∴Ｇ教団の名前にある『Ｇ』が\x01",
            "《真なる叡智#10Rグ ノ ー シ ス#》を指すということは\x01",
            "既に突き止められていますし……\x02\x03",

            "これで『Ｄ∴Ｇ』の意味も\x01",
            "ようやく判明したと言えるはずです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AC")


    #C0099
    ChrTalk(
        0x102,
        (
            "#12P#00108Fでも……確かヨアヒム先生は、\x01",
            "キーアちゃんの事を\x01",
            "『神となる御方』と言ってたのよね。\x02\x03",

            "そうなると、《Ｄ》とは\x01",
            "キーアちゃんを指す言葉にも\x01",
            "なってしまうけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D4")

    #C0100
    ChrTalk(
        0x109,
        (
            "#12P#10101Fヨアヒム・ギュンターが\x01",
            "どこまでの事を知ってたのか……\x02\x03",

            "……これだけじゃまだ判りませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BA")

    label("loc_32D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_335C")

    #C0101
    ChrTalk(
        0x104,
        (
            "#12P#00301Fヨアヒムの野郎が\x01",
            "どこまでの事を知ってたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x109,
        "#12P#10101F……これだけじゃまだ判りませんね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_33BA")

    label("loc_335C")


    #C0103
    ChrTalk(
        0x104,
        (
            "#12P#00301Fヨアヒムの野郎が\x01",
            "どこまでの事を知ってたのか……\x02\x03",

            "これだけじゃまだ判らねえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BA")


    #C0104
    ChrTalk(
        0x101,
        (
            "#12P#00001Fアーネストさんも、ヨアヒムから\x01",
            "すべてを聞いていたわけじゃ\x01",
            "ないみたいだし……\x02\x03",

            "#00003F彼を逮捕できていれば……\x01",
            "つくづくそう思ってしまうな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34C6")

    #C0105
    ChrTalk(
        0x8,
        (
            "#5P……ともかく、この調子で\x01",
            "データを解析していけば、\x01",
            "色々な事が見えてくると思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356C")

    label("loc_34C6")


    #C0106
    ChrTalk(
        0x8,
        (
            "#5P……ともかく、この調子で\x01",
            "データを解析していけば、\x01",
            "色々な事が見えてくると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "#5P残りの『フラグメント』も\x01",
            "解析に回してみるとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_356C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35CE")
    Sound(9, 0, 100, 0)

    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』のページ３を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_35CE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362A")
    Sound(9, 0, 100, 0)

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情報端末データ\x01",
            "『御子について』のページ１を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_362A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F50")
    Sound(9, 0, 100, 0)

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』のページ４を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』の解析を完了した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    FadeToBright(1000, 0)
    OP_0D()

    #C0112
    ChrTalk(
        0x8,
        (
            "#5P第０２情報端末の全データの\x01",
            "解析が完了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        "#5Pさっそく確認してみますか？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#12P#00001Fええ、お願いします。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 12)

    #C0115
    ChrTalk(
        0x8,
        (
            "#5P……このデータには、\x01",
            "あの《グノーシス》に関する\x01",
            "詳細が記されているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "#5P身体能力と感応力を高め、\x01",
            "さらには潜在能力すら\x01",
            "引き出す効能を持つ薬物……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#5P“魔人化”といった現象といい、\x01",
            "かなり謎の多い薬物ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#12P#00001F原料として使われた\x01",
            "《プレロマ草》という植物が\x01",
            "湿地帯に群生していた事から……\x02\x03",

            "ヨアヒムが湿地帯に材料を\x01",
            "採取しに行っていたらしい事も\x01",
            "状況的に間違いなさそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A20")

    #C0119
    ChrTalk(
        0x102,
        (
            "#12P#00101Fそれと、データにはグノーシスが\x01",
            "彼らの言う所の真なる神……\x02\x03",

            "つまり、《Ｄ》を復活させる為の\x01",
            "薬物だという一節もあるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x109,
        (
            "#12P#10108F正直言って、荒唐無稽な話に\x01",
            "聞こえますけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_3A20")


    #C0121
    ChrTalk(
        0x102,
        (
            "#12P#00101Fそれと、データにはグノーシスが\x01",
            "彼らの言う所の真なる神……\x02\x03",

            "つまり、《Ｄ》を復活させる為の\x01",
            "薬物だという一節もあるわね。\x02\x03",

            "#00108F正直言って、荒唐無稽な話に\x01",
            "聞こえるけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADB")


    #C0122
    ChrTalk(
        0x103,
        (
            "#12P#00201Fそれでも、教団は５００年もの間\x01",
            "“儀式”という形で\x01",
            "グノーシスの研究を続けてきた……\x02\x03",

            "#00203F……わたしは運良くガイさんに\x01",
            "助け出されましたが、今までに\x01",
            "相当な数の犠牲者も出たそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#12P#00301Fそれを“多少の犠牲”だなんて\x01",
            "言い方をしてるんだからな……\x02\x03",

            "本当に救いようのねえ連中だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C79")

    #C0124
    ChrTalk(
        0x105,
        (
            "#12P#10403F……それと、最近はヴァルドも\x01",
            "グノーシスを服用していたんだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CC9")

    label("loc_3C79")


    #C0125
    ChrTalk(
        0x105,
        (
            "#12P#10303F……それと、最近はヴァルドも\x01",
            "グノーシスを服用していたんだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC9")


    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#00001Fああ……教団がなくなったとはいえ、\x01",
            "まだ注意は必要なのかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DAE")

    label("loc_3D22")


    #C0127
    ChrTalk(
        0x101,
        (
            "#12P#00003F……それと、最近はヴァルドも\x01",
            "グノーシスを服用していた。\x02\x03",

            "#00001F教団がなくなったとはいえ、\x01",
            "まだ注意は必要なのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DAE")


    #C0128
    ChrTalk(
        0x102,
        (
            "#12P#00101Fええ……本当にそうね。\x02\x03",

            "グノーシスに限らず、\x01",
            "こんな薬物は、私たち警察が\x01",
            "きちんと取り締まらなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3EA0")

    #C0129
    ChrTalk(
        0x8,
        "#5Pええ、本当にそう思います。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "#5P……ひとまずグノーシスに関しては\x01",
            "こんなところでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F50")

    label("loc_3EA0")


    #C0131
    ChrTalk(
        0x8,
        "#5Pええ、本当にそう思います。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "#5P……ひとまずグノーシスに関しては\x01",
            "こんなところでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "#5P残りの『フラグメント』も\x01",
            "解析に回してみるとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_3F50")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FAC")
    Sound(9, 0, 100, 0)

    #A0134
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情報端末データ\x01",
            "『御子について』のページ２を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3FAC")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48CC")
    Sound(9, 0, 100, 0)

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情報端末データ\x01",
            "『御子について』のページ３を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情報端末データ\x01",
            "『御子について』の解析を完了した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    SetScenarioFlags(0x12A, 6)
    FadeToBright(1000, 0)
    OP_0D()

    #C0137
    ChrTalk(
        0x8,
        (
            "#5P第０３情報端末の全データの\x01",
            "解析が完了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        "#5Pさっそく確認してみますか？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#12P#00001Fええ、お願いします。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 13)

    #C0140
    ChrTalk(
        0x8,
        (
            "#5Pこの内容は、\x01",
            "支援課で保護されていた\x01",
            "キーアさんの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#12P#00003F５００年前、クロイス家によって\x01",
            "キーアが生み出され……\x01",
            "信仰対象として教団に与えられた。\x02\x03",

            "《揺籃#4Rゆりかご#》に眠り続ける、\x01",
            "神の依り代たる『御子』として……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#12P#00101F……教団の人間も、何一つ真実を\x01",
            "知らされていなかったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#12P#00203Fクロイス家の真の目的のために\x01",
            "影で誘導されているとも知らずに、\x01",
            "《真なる神》という幻想を求め続けた……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_431C")

    #C0144
    ChrTalk(
        0x106,
        "#12P#10708F……ある意味、哀れな人たちですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4393")

    label("loc_431C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4364")

    #C0145
    ChrTalk(
        0x109,
        "#12P#10108F……ある意味、哀れな人たちですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4393")

    label("loc_4364")


    #C0146
    ChrTalk(
        0x105,
        "#12P#10408F……ある意味、哀れな連中だね。\x02",
    )

    CloseMessageWindow()

    label("loc_4393")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43EA")

    #C0147
    ChrTalk(
        0x10A,
        (
            "#12P#00603F奴らのやってきた事を考えると\x01",
            "同情すら沸かんがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4493")

    label("loc_43EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4447")

    #C0148
    ChrTalk(
        0x105,
        (
            "#12P#10403F彼らのやってきた事を考えると\x01",
            "同情する余地はないけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4493")

    label("loc_4447")


    #C0149
    ChrTalk(
        0x109,
        (
            "#12P#10103F彼らのやってきた事を考えると\x01",
            "同情する余地はありませんが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4493")


    #C0150
    ChrTalk(
        0x101,
        (
            "#12P#00001F教団はともかく……\x01",
            "キーアには何の罪もなかったはずだ。\x02\x03",

            "#00003F例えクロイス家の目的のために\x01",
            "造られた存在だったとしても……\x02\x03",

            "例え不可思議な能力を\x01",
            "持っていたとしても……\x01",
            "そんなことは関係がない。\x02\x03",

            "俺たちの目の前で目覚めたあの子は\x01",
            "正真正銘、普通の女の子だったはずだ。\x02\x03",

            "#00001Fそれなのに、何百年もあんな所に\x01",
            "一人ぼっちで閉じ込められて……\x02\x03",

            "今また、マリアベルさんと\x01",
            "イアン先生によって\x01",
            "利用されようとしている。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#12P#00301F……どんな事情があろうと、\x01",
            "絶対に許すわけにはいかねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "#5P……ひとまず、教団のデータは\x01",
            "これで全て解析が完了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#5P私は皆さんほど今回の事件の\x01",
            "細かい事情に通じてはいませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "#5P皆さんにとってキーアさんが\x01",
            "とても大切な存在だという事は\x01",
            "痛いほど分かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#5Pどうか……頑張ってください。\x01",
            "私も陰ながら応援させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#12P#00000Fありがとうございます、レベッカさん。\x02\x03",

            "#00003F俺たちの手で絶対に、\x01",
            "キーアを取り戻してみせます。\x02\x03",

            "#00001F俺たちの大切なキーアが……\x01",
            "あの子自身が笑顔で過ごせる\x01",
            "未来を作るためにも……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_48A4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_48A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_48BD")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_48BD")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)
    TalkEnd(0x8)

    label("loc_48CC")

    Jump("loc_2B00")

    label("loc_48D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49EE")
    FadeToBright(1000, 0)
    OP_0D()

    #C0157
    ChrTalk(
        0x8,
        (
            "#5Pまた『フラグメント』を手に入れたら\x01",
            "私の方にお持ちくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "#5P解析されたデータを確認する場合も\x01",
            "改めてお申し付けください。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49CF")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_49CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49E8")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_49E8")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_49EE")

    Return()

    # Function_9_2A09 end

    def Function_10_49EF(): pass

    label("Function_10_49EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AF5")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【教団について】\x01",            # 0
            "【グノーシスについて】\x01",      # 1
            "【御子について】\x01",            # 2
            "【やめる】\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4AA8"),
        (1, "loc_4AB6"),
        (2, "loc_4AC4"),
        (3, "loc_4AD2"),
        (SWITCH_DEFAULT, "loc_4AE1"),
    )


    label("loc_4AA8")

    Sound(72, 0, 100, 0)
    Call(0, 11)
    Jump("loc_4AF0")

    label("loc_4AB6")

    Sound(72, 0, 100, 0)
    Call(0, 12)
    Jump("loc_4AF0")

    label("loc_4AC4")

    Sound(72, 0, 100, 0)
    Call(0, 13)
    Jump("loc_4AF0")

    label("loc_4AD2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AF0")

    label("loc_4AE1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AF0")

    label("loc_4AF0")

    Jump("loc_49F9")

    label("loc_4AF5")

    Return()

    # Function_10_49EF end

    def Function_11_4AF6(): pass

    label("Function_11_4AF6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CBD")
    SetChrName("")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『教団について』\x01\x01",
            "──私の名はヨアヒム・ギュンター。\x01",
            "《Ｄ∴Ｇ教団》に属する幹部司祭である。\x01",
            "６年前、遊撃士を含む多くの勢力の手で\x01",
            "我が教団は壊滅状態に陥ってしまった。\x01",
            "しかし、私だけは故あって難を逃れ、\x01",
            "この■■の地へと落ち延びる事ができた。\x01",
            "大いなる《■》の導きによって\x01",
            "教団の大望を成すべく私は永らえたのだ。\x01",
            "いずれ来るその時──\x01",
            "新たな聖典を記すための資料として\x01",
            "各端末にデータを記録しておく事とする。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4E5E")

    label("loc_4CBD")

    SetChrName("")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『教団について』\x01\x01",
            "──私の名はヨアヒム・ギュンター。\x01",
            "《Ｄ∴Ｇ教団》に属する幹部司祭である。\x01",
            "６年前、遊撃士を含む多くの勢力の手で\x01",
            "我が教団は壊滅状態に陥ってしまった。\x01",
            "しかし、私だけは故あって難を逃れ、\x01",
            "この起源の地へと落ち延びる事ができた。\x01",
            "大いなる《Ｄ》の導きによって\x01",
            "教団の大望を成すべく私は永らえたのだ。\x01",
            "いずれ来るその時──\x01",
            "新たな聖典を記すための資料として\x01",
            "各端末にデータを記録しておく事とする。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4E5E")

    SetChrName("")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sまず、我が教団の成り立ちについて語ろう。\x01",
            "そのためには、このゼムリア大陸が辿った\x01",
            "忌々しい歴史を振り返る必要がある。\x01\x01",
            "──約１２００年前の《大崩壊》によって\x01",
            "大陸は高度な文明と秩序を失い、\x01",
            "戦と貧困の支配する《暗黒時代》が訪れた。\x01",
            "そして、疲れ果てた人々は\x01",
            "大いなる間違いを犯してしまった。\x01\x01",
            "突如現れた愚か者どもの甘言に惑わされ、\x01",
            "彼らの作りだした身勝手な秩序を\x01",
            "受け入れてしまったのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51A5")
    SetChrName("")

    #A0163
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sすなわち──愚かなる■■■■と\x01",
            "信仰の象徴たる《■の■■》である。\x01",
            "彼らの秩序によって《暗黒時代》は終焉し、\x01",
            "その信仰はたちまち大陸中に広まったが……\x01\x01",
            "よく考えてみてほしい。\x01",
            "もし真に《■■》が存在するというのならば\x01",
            "誰もが等しく救いを受けるべきではないか？\x01",
            "しかし、未だに格差の概念は無くならず、\x01",
            "災厄や不幸で命を落とす者も後を絶たない。\x01\x01",
            "《■■》は救う人間を選ぶというのか？\x01",
            "あまりに馬鹿馬鹿しい話ではないか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_534C")

    label("loc_51A5")

    SetChrName("")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sすなわち──愚かなる七耀教会と\x01",
            "信仰の象徴たる《空の女神》である。\x01",
            "彼らの秩序によって《暗黒時代》は終焉し、\x01",
            "その信仰はたちまち大陸中に広まったが……\x01\x01",
            "よく考えてみてほしい。\x01",
            "もし真に《女神》が存在するというのならば\x01",
            "誰もが等しく救いを受けるべきではないか？\x01",
            "しかし、未だに格差の概念は無くならず、\x01",
            "災厄や不幸で命を落とす者も後を絶たない。\x01\x01",
            "《女神》は救う人間を選ぶというのか？\x01",
            "あまりに馬鹿馬鹿しい話ではないか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_534C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54D2")
    SetChrName("")

    #A0165
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S所詮は■■■■が権威を得るため\x01",
            "作りだした虚像に過ぎないのである。\x01",
            "《■■》など、存在するわけがないのだ。\x01\x01",
            "真理に辿りついた我々の先人たちは、\x01",
            "《■■■■》に邂逅すべく長き旅路に出た。\x01\x01",
            "そして時代が中世に移り変わる頃、\x01",
            "ついに彼らは見出したのである。\x01",
            "この地の奥深くで■■■■■■■■■■\x01",
            "■■■■■■■■■■■■■■■……\x01\x01",
            "《■》──それはそう呼ばれていた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5645")

    label("loc_54D2")

    SetChrName("")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S所詮は七耀教会が権威を得るため\x01",
            "作りだした虚像に過ぎないのである。\x01",
            "《女神》など、存在するわけがないのだ。\x01\x01",
            "真理に辿りついた我々の先人たちは、\x01",
            "《真なる神》に邂逅すべく長き旅路に出た。\x01\x01",
            "そして時代が中世に移り変わる頃、\x01",
            "ついに彼らは見出したのである。\x01",
            "この地の奥深くで永い眠りにつきながら\x01",
            "大いなる力をその身に宿した存在……\x01\x01",
            "《Ｄ》──それはそう呼ばれていた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5645")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_4AF6 end

    def Function_12_5659(): pass

    label("Function_12_5659")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_580E")
    SetChrName("")

    #A0167
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『グノーシスについて』\x01\x01",
            "《グノーシス》……それは、\x01",
            "■■■■■■■■という■■■■■、\x01",
            "《プレロマ草》を原料とした秘薬である。\x01\x01",
            "その調合方法は■■■■■■■■■、\x01",
            "服用することで身体能力と感応力を高め、\x01",
            "さらには潜在能力すら引き出す効能を持つ。\x01",
            "■■■■■■■■■■■■■■■■■。\x01",
            "■■■■■■■■■■■■■■■。\x01",
            "《グノーシス》は、■■■の■■を\x01",
            "《■》の■■に■■■■■■■薬なのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_599D")

    label("loc_580E")

    SetChrName("")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『グノーシスについて』\x01\x01",
            "《グノーシス》……それは、\x01",
            "七耀脈の上に咲くという伝説の植物、\x01",
            "《プレロマ草》を原料とした秘薬である。\x01\x01",
            "その調合方法は《Ｄ》と共に伝わり、\x01",
            "服用することで身体能力と感応力を高め、\x01",
            "さらには潜在能力すら引き出す効能を持つ。\x01",
            "だが、それらは単なる布石にすぎない。\x01",
            "この薬の真の力は別にあったのだ。\x01",
            "《グノーシス》は、服用者の精神を\x01",
            "《Ｄ》の御心に接続するための薬なのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_599D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B3B")
    SetChrName("")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S《■》は■■■の■■を■■することで\x01",
            "■■を蓄え、■■する性質を持つ。\x01",
            "いずれその■■が《■■》に至ったとき、\x01",
            "《■》は■■するのである。\x01\x01",
            "さらに、《グノーシス》には\x01",
            "改良の余地が残されていた。\x01",
            "■■■■■■■■■■■■■■■■■、\x01",
            "■■■■■■■を《■》に■■■■■のだ。\x01\x01",
            "それから■■■■■■■、我が教団は\x01",
            "より効果の高い《グノーシス》の研究……\x01",
            "いわゆる“儀式”を繰り返してきた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CC6")

    label("loc_5B3B")

    SetChrName("")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S《Ｄ》は服用者の精神を統合することで\x01",
            "知識を蓄え、成長する性質を持つ。\x01",
            "いずれその知識が《叡智》に至ったとき、\x01",
            "《Ｄ》は復活するのである。\x01\x01",
            "さらに、《グノーシス》には\x01",
            "改良の余地が残されていた。\x01",
            "服用者の能力を限界まで引き出せれば、\x01",
            "より多くの知識を《Ｄ》に供給できるのだ。\x01\x01",
            "それから５００年もの間、我が教団は\x01",
            "より効果の高い《グノーシス》の研究……\x01",
            "いわゆる“儀式”を繰り返してきた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5CC6")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E58")
    SetChrName("")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sそうして、■■■■■の■■■とは\x01",
            "■■■■■■■■■■■■\x01",
            "《グノーシス》は完成へと近づいたが、\x01",
            "今一歩のところで誤算が生じてしまう。\x01\x01",
            "実験の規模を大きくしたことで\x01",
            "遊撃士やその他の勢力に存在を感づかれ、\x01",
            "各ロッジ、及び教団そのものの壊滅に\x01",
            "繋がってしまったのである。\x01\x01",
            "誠に愚かな事であると言わざるを得ない。\x01",
            "《■■■■》の■■のためには\x01",
            "多少の犠牲は付き物だというのに……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5FD7")

    label("loc_5E58")

    SetChrName("")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sそうして、５００年前の発足時とは\x01",
            "比較できないほどの速度で\x01",
            "《グノーシス》は完成へと近づいたが、\x01",
            "今一歩のところで誤算が生じてしまう。\x01\x01",
            "実験の規模を大きくしたことで\x01",
            "遊撃士やその他の勢力に存在を感づかれ、\x01",
            "各ロッジ、及び教団そのものの壊滅に\x01",
            "繋がってしまったのである。\x01\x01",
            "誠に愚かな事であると言わざるを得ない。\x01",
            "《真なる神》の復活のためには\x01",
            "多少の犠牲は付き物だというのに……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5FD7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6181")
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S私は、壊滅したロッジから\x01",
            "実験のデータを秘密裏に回収し、\x01",
            "この■■の地クロスベルへと至った。\x01\x01",
            "《グノーシス》の材料である\x01",
            "《プレロマ草》は■■■■■■■の\x01",
            "■■■に■■しているため、\x01",
            "■■■■■に困ることはなかった。\x01",
            "また、この《太陽の砦》の深層は\x01",
            "■■の■■■■の■■■研究施設であり、\x01",
            "数々の高度な設備を備えている。\x01",
            "こうして私は恵まれた研究環境を手に入れ\x01",
            "遂にこの秘薬を完成させたのである──。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6318")

    label("loc_6181")

    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S私は、壊滅したロッジから\x01",
            "実験のデータを秘密裏に回収し、\x01",
            "この起源の地クロスベルへと至った。\x01\x01",
            "《グノーシス》の材料である\x01",
            "《プレロマ草》はクロスベル南部の\x01",
            "湿地帯に群生しているため、\x01",
            "材料の調達に困ることはなかった。\x01",
            "また、この《太陽の砦》の深層は\x01",
            "中世の錬金術師の築いた研究施設であり、\x01",
            "数々の高度な設備を備えている。\x01",
            "こうして私は恵まれた研究環境を手に入れ\x01",
            "遂にこの秘薬を完成させたのである──。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6318")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_12_5659 end

    def Function_13_632C(): pass

    label("Function_13_632C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64EF")
    SetChrName("")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『御子について』\x01\x01",
            "このクロスベルは我々《Ｄ∴Ｇ教団》の\x01",
            "■■■であるとともに、■■■■とされる。\x01",
            "その■■は、《御子》たるものが\x01",
            "■■■■■■■■■■■■■だからである。\x01\x01",
            "《御子》とは、《■■■■》■■■■■■■\x01",
            "■■《Ｄ∴Ｇ教団》■■■■■■■■■■。\x01",
            "《太陽の砦》■■■■■■■■■■■■、\x01",
            "■■■■■■■■■■■■■■■■■、\x01",
            "■■■■■■■《太陽の砦》■■■■\x01",
            "■■■■■■■■■■■■■■のだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_668C")

    label("loc_64EF")

    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『御子について』\x01\x01",
            "このクロスベルは我々《Ｄ∴Ｇ教団》の\x01",
            "本拠地であるとともに、起源の地とされる。\x01",
            "その理由は、《御子》たるものが\x01",
            "始祖より継承されてきた場所だからである。\x01\x01",
            "《御子》とは、《真なる神》の依り代にして\x01",
            "我が《Ｄ∴Ｇ教団》の象徴たる存在である。\x01",
            "《太陽の砦》の地下で眠り続けるそれは、\x01",
            "一見すれば人間の少女の姿をしており、\x01",
            "５００年もの間《太陽の砦》の祭壇で\x01",
            "目覚めの時を待っているというのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_668C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_681C")
    SetChrName("")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S■■がそれほどの■■を■■■など、\x01",
            "俗世の者には信じ難い話であろう。\x01\x01",
            "だが、私は確かにこの目で見たのだ。\x01",
            "『■■■■■』と呼ばれる■■の■で\x01",
            "■■■■■■■■■■■■■■──\x01",
            "その神々しき■■を。\x01\x01",
            "『■■■■■』は、《古代遺物》を\x01",
            "■■していた■■■■■■の■■を元に\x01",
            "■■■■■■■■■■■■■■■である。\x01",
            "ならば、この■■■■■■■■■■にも\x01",
            "何ら不思議はないだろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_69A5")

    label("loc_681C")

    SetChrName("")

    #A0178
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S人間がそれほどの時間を生きるなど、\x01",
            "俗世の者には信じ難い話であろう。\x01\x01",
            "だが、私は確かにこの目で見たのだ。\x01",
            "『聖なる揺籃#4Rゆりかご#』と呼ばれる球体の中で\x01",
            "まどろむように眠り続ける少女──\x01",
            "その神々しき御姿を。\x01\x01",
            "『聖なる揺籃』は、《古代遺物》を\x01",
            "研究していた錬金術師たちの技術を元に\x01",
            "教団の先人たちが造り上げたものである。\x01",
            "ならば、この奇蹟ともいうべき現象にも\x01",
            "何ら不思議はないだろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_69A5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B22")
    SetChrName("")

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S《御子》は■■■■■■から\x01",
            "《グノーシス》を■■■、■■■■■■■\x01",
            "■■■■■■■■■■■■■。\x01\x01",
            "──《■■》■■■■■《御子》は■■■、\x01",
            "■■■■《■》■■■であろう。\x01",
            "そして、■■の■■の■■と■■は\x01",
            "《■》のもとに■■され、\x01",
            "人々を《■■》の呪縛から解き放つのだ。\x01\x01",
            "それが我が《Ｄ∴Ｇ教団》の先人が残した\x01",
            "預言であり、成すべき大望なのである──。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6C8C")

    label("loc_6B22")

    SetChrName("")

    #A0180
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S《御子》は生まれし時代から\x01",
            "《グノーシス》を介して、無限ともいえる\x01",
            "知識を御身に宿したとされる。\x01\x01",
            "──《叡智》に至りし時《御子》は目覚め、\x01",
            "真なる神《Ｄ》と成るであろう。\x01",
            "そして、全ての人々の意思と魂魄は\x01",
            "《Ｄ》のもとに集約され、\x01",
            "人々を《女神》の呪縛から解き放つのだ。\x01\x01",
            "それが我が《Ｄ∴Ｇ教団》の先人が残した\x01",
            "預言であり、成すべき大望なのである──。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6C8C")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_13_632C end

    def Function_14_6CA0(): pass

    label("Function_14_6CA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC5")
    SetChrPos(0xFE, 40, 40, 12610, 0)
    Jump("loc_6D79")

    label("loc_6CC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CEA")
    SetChrPos(0xFE, -1000, 40, 12400, 0)
    Jump("loc_6D79")

    label("loc_6CEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D0F")
    SetChrPos(0xFE, 1140, 40, 12400, 0)
    Jump("loc_6D79")

    label("loc_6D0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D34")
    SetChrPos(0xFE, 110, 0, 11010, 0)
    Jump("loc_6D79")

    label("loc_6D34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D59")
    SetChrPos(0xFE, -950, 0, 10770, 0)
    Jump("loc_6D79")

    label("loc_6D59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D79")
    SetChrPos(0xFE, 1080, 0, 10720, 0)

    label("loc_6D79")

    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_6CA0 end

    def Function_15_6D88(): pass

    label("Function_15_6D88")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DA8")
    BeginChrThread(0x101, 1, 0, 14)

    label("loc_6DA8")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DBF")
    BeginChrThread(0x102, 1, 0, 14)

    label("loc_6DBF")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DD6")
    BeginChrThread(0x103, 1, 0, 14)

    label("loc_6DD6")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DED")
    BeginChrThread(0x104, 1, 0, 14)

    label("loc_6DED")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E04")
    BeginChrThread(0x109, 1, 0, 14)

    label("loc_6E04")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E1B")
    BeginChrThread(0x105, 1, 0, 14)

    label("loc_6E1B")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E32")
    BeginChrThread(0x106, 1, 0, 14)

    label("loc_6E32")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E49")
    BeginChrThread(0x10A, 1, 0, 14)

    label("loc_6E49")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6E63")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_6E63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6E7C")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_6E7C")

    Return()

    # Function_15_6D88 end

    def Function_16_6E7D(): pass

    label("Function_16_6E7D")

    ClearScenarioFlags(0x1, 6)
    ClearScenarioFlags(0x1, 7)
    ClearScenarioFlags(0x2, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70B3")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ECF")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6ECF")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F03")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6F03")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F37")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6F37")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F6B")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6F6B")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F9F")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6F9F")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FD3")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6FD3")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7007")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_7007")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_703B")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_703B")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7072")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Jump("loc_70AE")

    label("loc_7072")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A9")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x2, 0)
    Jump("loc_70AE")

    label("loc_70A9")

    Jump("loc_70B3")

    label("loc_70AE")

    Jump("loc_6E90")

    label("loc_70B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_7A46")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    FadeToBright(500, 0)
    OP_0D()

    #C0181
    ChrTalk(
        0x8,
        (
            "あら、皆さん……\x01",
            "戦闘手帳が\x01",
            "大分埋まってきたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "魔獣の情報を控えたいので\x01",
            "一度見せてもらっていいでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#0000F#12Pええ、喜んで。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0184
    ChrTalk(
        0x8,
        (
            "ありがとうございました。\x01",
            "手帳を返却しますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B6")

    #A0186
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

    #A0187
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を1個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_762D")

    label("loc_72B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7319")

    #A0188
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

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_762D")

    label("loc_7319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_737C")

    #A0190
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

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を3個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_762D")

    label("loc_737C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73DF")

    #A0192
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

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を4個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_762D")

    label("loc_73DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7442")

    #A0194
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

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を5個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_762D")

    label("loc_7442")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A5")

    #A0196
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

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を6個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_762D")

    label("loc_74A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7508")

    #A0198
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

    #A0199
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を7個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_762D")

    label("loc_7508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_756B")

    #A0200
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

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を8個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_762D")

    label("loc_756B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75CE")

    #A0202
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

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を9個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_762D")

    label("loc_75CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_762D")

    #A0204
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

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を10個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_762D")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7669")
    Sound(17, 0, 100, 0)

    #A0206
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
    Jump("loc_769A")

    label("loc_7669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_769A")
    Sound(17, 0, 100, 0)

    #A0207
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

    label("loc_769A")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77D7")

    #C0208
    ChrTalk(
        0x8,
        (
            "また魔獣の情報が集まったら\x01",
            "お立ち寄りくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        "#12P#0000Fはい、宜しくお願いします。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_775F")

    #C0210
    ChrTalk(
        0x102,
        "#12P#0100Fまたお邪魔させて頂きますね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_77D2")

    label("loc_775F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7796")

    #C0211
    ChrTalk(
        0x103,
        "#12P#0200Fまたお邪魔します。\x02",
    )

    CloseMessageWindow()
    Jump("loc_77D2")

    label("loc_7796")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77D2")

    #C0212
    ChrTalk(
        0x104,
        "#12P#0300Fまたお邪魔させてもらうッス。\x02",
    )

    CloseMessageWindow()

    label("loc_77D2")

    Jump("loc_79DE")

    label("loc_77D7")


    #C0213
    ChrTalk(
        0x8,
        (
            "新型魔獣の情報も\x01",
            "十分に集まったようですね。\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "これで今後の安全対策も\x01",
            "より万全なものに出来ると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#12P#0000Fはは……お役に立てて光栄です。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "ふふ、皆さんには本当に\x01",
            "お世話になりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "それでは、今回は\x01",
            "特別報酬もお渡しさせていただきます。\x01",
            "是非お受け取りください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0218
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

    #C0219
    ChrTalk(
        0x8,
        (
            "今後とも皆様のご活躍を\x01",
            "お祈りさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "また何かありましたら\x01",
            "いつでもお越しくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79DE")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_79F5")
    ClearScenarioFlags(0x1, 5)

    label("loc_79F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7A0E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_7A0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7A27")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_7A27")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_7B88")

    label("loc_7A46")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AFD")

    #C0221
    ChrTalk(
        0x8,
        (
            "本部に集まった情報も\x01",
            "もう十分だと思いますので、\x01",
            "調査はここまでとさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "また何かお願いする事が\x01",
            "あるかもしれません。\x01",
            "その時は宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B88")

    label("loc_7AFD")


    #C0223
    ChrTalk(
        0x8,
        (
            "戦闘手帳の内容も\x01",
            "溜まってきているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "もう少し情報が集まったら\x01",
            "私の方に見せてください。\x01",
            "情報を控えさせてもらいますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B88")

    Return()

    # Function_16_6E7D end

    def Function_17_7B89(): pass

    label("Function_17_7B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BB2")
    Call(0, 18)
    Jump("loc_7CE4")

    label("loc_7BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BCD")
    Call(0, 18)
    Jump("loc_7CE4")

    label("loc_7BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BE3")
    Call(0, 18)
    Jump("loc_7CE4")

    label("loc_7BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BF9")
    Call(0, 18)
    Jump("loc_7CE4")

    label("loc_7BF9")

    TalkBegin(0x9)

    #C0225
    ChrTalk(
        0x9,
        (
            "#01900F皆さんは、『ポムっと！』っていう\x01",
            "導力ゲームをご存知ですか～？\x02\x03",

            "#01909Fふふ、実はわたしも始めてみたんです。\x01",
            "よかったらアカウントを交換して下さい～。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)

    #A0226
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『フランのアカウント』\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    TalkEnd(0x9)

    label("loc_7CE4")

    Jump("loc_7CEC")

    label("loc_7CE9")

    Call(0, 18)

    label("loc_7CEC")

    Return()

    # Function_17_7B89 end

    def Function_18_7CED(): pass

    label("Function_18_7CED")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7CFE")
    Jump("loc_9C26")

    label("loc_7CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D0C")
    Jump("loc_9C26")

    label("loc_7D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7F6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EB9")
    SoundLoad(803)

    #C0227
    ChrTalk(
        0x9,
        (
            "#01901Fみ、皆さん、\x01",
            "大変なことになりましたね。\x02\x03",

            "警察本部の方も、\x01",
            "今朝からずっと慌しくって……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0228
    ChrTalk(
        0x9,
        "#01905Fあっ、すみません――\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    OP_24(0x323)
    Sound(804, 0, 100, 0)

    #C0229
    ChrTalk(
        0x9,
        (
            "#01903Fはい、こちらクロスベル警察――\x02\x03",

            "#01901Fはい、はい……\x02\x03",

            "そうです、昨夜から\x01",
            "警備隊が事態の収束に――\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#00001F（流石に忙しそうだな……）\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x102,
        (
            "#00101F（ええ、私たちも\x01",
            "  やるべきことをやりましょう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 7)
    OP_24(0x323)
    Jump("loc_7F65")

    label("loc_7EB9")

    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    #A0232
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

    #C0233
    ChrTalk(
        0x9,
        (
            "#01901Fはい、はい……\x02\x03",

            "#01908F……申し訳ありません。\x01",
            "武装集団の正体につきましても\x01",
            "まだはっきりしたことは……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F65")

    Jump("loc_9C26")

    label("loc_7F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_8063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F85")
    Call(0, 21)
    Jump("loc_805E")

    label("loc_7F85")


    #C0234
    ChrTalk(
        0x9,
        (
            "#01900F先ほどお伝えしたとおり、\x01",
            "導力ボートは港湾区の波止場に\x01",
            "手配しておきました～。\x02\x03",

            "#01904F近くに整備員さんが\x01",
            "いらっしゃるはずなので、\x01",
            "そちらに訪ねてみてください～！\x02\x03",

            "#01900F気をつけて行ってくださいね、皆さん！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_805E")

    Jump("loc_9C26")

    label("loc_8063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_83A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82EC")

    #C0235
    ChrTalk(
        0x9,
        (
            "#01900F皆さん、昨日は\x01",
            "本当にお疲れ様でした～。\x02\x03",

            "《結社》という組織についても\x01",
            "列車事故の原因にしても、\x01",
            "お手柄だったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#00006Fいや、まあ実際に大したことが\x01",
            "出来たわけじゃないんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        (
            "#00100Fええ、事故の対応にしても\x01",
            "夜通しで作業してくれた人たちの方が\x01",
            "よっぽど大変だったでしょうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x9,
        (
            "#01904Fそれでも、昨日は皆さんも\x01",
            "かなり夜遅くまで捜索活動を\x01",
            "続けていらっしゃったんですよね。\x02\x03",

            "#01902Fくれぐれも、\x01",
            "体調管理には気を付けてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x103,
        "#00202Fお気遣い、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x104,
        (
            "#00302Fま、忙しいのはそっちも同じだろうし、\x01",
            "フランちゃんも無理しないようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x9,
        "#01909Fはい、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 0)
    Jump("loc_839E")

    label("loc_82EC")


    #C0242
    ChrTalk(
        0x9,
        (
            "#01900F今日も新しい支援要請が\x01",
            "いくつか来ているようですが……\x02\x03",

            "くれぐれも、無理のない\x01",
            "範囲で頑張ってくださいね。\x02\x03",

            "私もしっかり自己管理をして、\x01",
            "無理しないよう心がけますので。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_839E")

    Jump("loc_9C26")

    label("loc_83A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_85CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8502")
    SetChrName("")

    #A0243
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

    #C0244
    ChrTalk(
        0x9,
        (
            "#01903Fはい、はい……\x02\x03",

            "#01901F……申し訳ありません。\x01",
            "事故の原因については\x01",
            "只今調査中でして……\x02\x03",

            "復旧の時期についても\x01",
            "今の時点では何とも……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#00001F（どうやら列車事故の\x01",
            "  対応をしているみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        (
            "#00101F（ええ、忙しそうだし、\x01",
            "  邪魔しない方がいいわね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_85C6")

    label("loc_8502")

    SetChrName("")

    #A0247
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

    #C0248
    ChrTalk(
        0x9,
        (
            "#01903Fはい、はい……\x02\x03",

            "#01901F……申し訳ありません。\x01",
            "事故の原因については\x01",
            "只今調査中でして……\x02\x03",

            "復旧の時期についても\x01",
            "今の時点では何とも……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85C6")

    Jump("loc_9C26")

    label("loc_85CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_87BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86E3")

    #C0249
    ChrTalk(
        0x9,
        (
            "#01903F蒼い花、それに幻獣……\x02\x03",

            "#01901F何だか不吉な印象を受けますが\x01",
            "とにかく、私たちは出来ることを\x01",
            "尽くすしかありませんよね。\x02\x03",

            "あの、皆さんどうか\x01",
            "これからも気を付けて下さいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        "#00000Fああ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x109,
        "#10100Fフランもサポートよろしくね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_87B7")

    label("loc_86E3")


    #C0252
    ChrTalk(
        0x9,
        (
            "#01903F独立提唱による緊張状態といい、\x01",
            "今回の異常事態といい、\x01",
            "何だか不吉な印象を受けますね。\x02\x03",

            "#01901Fあまり考えすぎても\x01",
            "仕方ないと思いますが……\x02\x03",

            "とにかく私も、目の前の仕事を\x01",
            "確実にこなして行こうと思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B7")

    Jump("loc_9C26")

    label("loc_87BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A5D")

    #C0253
    ChrTalk(
        0x9,
        (
            "#01901F皆さん……何でも《幻獣》の\x01",
            "対応をされているそうですね？\x02\x03",

            "旧鉱山にいたのと同じで、\x01",
            "奇妙なモンスターらしいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00000Fああ、まだまだ分からない\x01",
            "ことばかりだけどね。\x01",
            "とりあえず調査を進めてみるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        "#10105F？　何か不安でもあるの？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "#01906Fああうん、幻獣はかなり\x01",
            "手強いって話を聞いているから……\x01",
            "怪我して欲しくないなって。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x109,
        (
            "#10103Fうん、そうね。\x02\x03",

            "#10100Fでも無理はしないから、\x01",
            "そんなに心配しなくて大丈夫よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x9,
        (
            "#01904Fうん……そうだよね。\x02\x03",

            "それに皆さんは何たって\x01",
            "百戦錬磨の特務支援課ですし。\x02\x03",

            "#01909Fフラン・シーカー、\x01",
            "皆さんの健闘を信じて\x01",
            "報告を待ちたいと思います！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        (
            "#00302Fはは、ありがとな、\x01",
            "フランちゃん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 1)
    Jump("loc_8AE3")

    label("loc_8A5D")


    #C0260
    ChrTalk(
        0x9,
        (
            "#01902F皆さん、幻獣の調査、\x01",
            "気を付けて行って来て下さいね。\x02\x03",

            "フラン・シーカー、\x01",
            "皆さんの健闘を信じて\x01",
            "報告を待たせて頂きますので！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AE3")

    Jump("loc_9C26")

    label("loc_8AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B03")
    Call(0, 20)
    Jump("loc_8D4E")

    label("loc_8B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C98")

    #C0261
    ChrTalk(
        0x9,
        (
            "#01900Fユリア准佐は凛としてて\x01",
            "とってもかっこよくて……\x01",
            "本当に憧れちゃいますよ～。\x02\x03",

            "#01909Fまあ、お姉ちゃんの方が\x01",
            "かっこいいと思いますけど㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x109,
        (
            "#10106Fはあ、この子ったら……\x02\x03",

            "#10101F他のユリア准佐ファンが聞いたら\x01",
            "絶対怒ると思うよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、どうかな。\x01",
            "君ならユリア准佐みたいに\x01",
            "結構ファンがつきそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        "#01909Fね～、そうですよね～！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x109,
        "#10106Fか、勘弁してよ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8D4E")

    label("loc_8C98")


    #C0266
    ChrTalk(
        0x9,
        (
            "#01900F今日のオルキスタワーの警備、\x01",
            "折角だからわたしも\x01",
            "配属されたいくらいですよ～。\x02\x03",

            "#01906F凛としてとってもかっこいい\x01",
            "ユリア准佐とお姉ちゃんが、\x01",
            "警備する姿を見たかったです～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D4E")

    Jump("loc_9C26")

    label("loc_8D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F70")
    TurnDirection(0x9, 0x109, 0)

    #C0267
    ChrTalk(
        0x9,
        (
            "#01902Fあ、お姉ちゃん。\x02\x03",

            "除幕式の警備に参加したんだよね。\x01",
            "――どうだった、すごかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x109,
        (
            "#10109Fうん、それはもう。\x02\x03",

            "特にリベール王国の\x01",
            "クローディア姫と\x01",
            "ユリア准佐が素敵で――\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0269
    ChrTalk(
        0x9,
        (
            "#01905Fそ、そんなに近くで拝見したの！？\x02\x03",

            "#01906Fうぅ、いいなぁ。\x01",
            "お姉ちゃんだけずるいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x109,
        (
            "#10100Fあはは、ごめんねフラン。\x01",
            "今度何かで埋め合わせするから。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        (
            "#00002F（はは、フランも当然\x01",
            "  ユリア准佐のファンってわけか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x104,
        (
            "#00306F（う～む、なんつうか\x01",
            "  世の男の立つ瀬がねえなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 6)
    Jump("loc_8FD3")

    label("loc_8F70")


    #C0273
    ChrTalk(
        0x9,
        (
            "#01902Fクローディア姫に――\x01",
            "それにユリア准佐……！\x02\x03",

            "いいなぁ、私も\x01",
            "近くで拝見したかったです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FD3")

    Jump("loc_9C26")

    label("loc_8FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91EA")

    #C0274
    ChrTalk(
        0x9,
        (
            "#01902Fふふ、とうとう明日から\x01",
            "通商会議が始まりますね～。\x02\x03",

            "各国から首脳たちが集まって、\x01",
            "オルキスタワーの除幕式があって……\x01",
            "何だかワクワクしますー。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x109,
        (
            "#10106Fもう、子供じゃないんだから\x01",
            "のんきな事ばかり言ってないで\x01",
            "仕事に集中しなさいよ？\x02\x03",

            "#10106Fフランだって会議の期間中は\x01",
            "いつもより忙しいんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x9,
        (
            "#01900Fそうだけど、だからこそ\x01",
            "楽しみを見つけなくっちゃ。\x02\x03",

            "お姉ちゃんの方こそ、\x01",
            "いつも真面目すぎだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x105,
        "#10304Fフフ、確かに言えてるね。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x109,
        "#10101Fワ、ワジ君……！\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        "#00012Fあはは……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 7)
    Jump("loc_9270")

    label("loc_91EA")


    #C0280
    ChrTalk(
        0x9,
        (
            "#01902F確かに仕事は忙しいですけど、\x01",
            "こういう大きな行事って\x01",
            "何だかワクワクしますよね～。\x02\x03",

            "#01909Fふふ、明日の式典が楽しみですー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9270")

    Jump("loc_9C26")

    label("loc_9275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_9338")

    #C0281
    ChrTalk(
        0x9,
        (
            "#01901Fビクセン町長のお話では、\x01",
            "どうも旧鉱山の内部がおかしな事に\x01",
            "なっちゃっているそうなんです。\x02\x03",

            "何がどうおかしいのかは\x01",
            "よく分かりませんけど……\x01",
            "どうかよろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C26")

    label("loc_9338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9353")
    Call(0, 19)
    Jump("loc_958C")

    label("loc_9353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94D9")

    #C0282
    ChrTalk(
        0x9,
        (
            "#01906Fは～、お姉ちゃんって\x01",
            "呼べるようになって\x01",
            "本当によかったです～。\x02\x03",

            "#01902Fこれで心置きなく\x01",
            "オペレーションに\x01",
            "集中できそうですよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x109,
        (
            "#10106Fし、仕事に支障がでるほど\x01",
            "イヤだったの……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x109, 500)

    #C0284
    ChrTalk(
        0x9,
        (
            "#01901Fだって、わたしにとっては\x01",
            "死活問題なんだよ～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x109,
        "#10106F（ああもう、職場での礼節が……）\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        "#00012F（ど、どんまいノエル。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_958C")

    label("loc_94D9")


    #C0287
    ChrTalk(
        0x9,
        (
            "#01902Fふふ、これで心置きなく\x01",
            "オペレーションに\x01",
            "集中できそうですよ～。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x109, 500)

    #C0288
    ChrTalk(
        0x9,
        (
            "#01909F今日もお仕事がんばってね、\x01",
            "お姉ちゃん㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x109,
        "#10106F（もう何も言わないでおこう……）\x02",
    )

    CloseMessageWindow()

    label("loc_958C")

    Jump("loc_9C26")

    label("loc_9591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9C26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A97")

    #C0290
    ChrTalk(
        0x9,
        (
            "#01900Fふふ、それにしても\x01",
            "特務支援課の活動がようやく\x01",
            "再開されたんですね～。\x02\x03",

            "#01909Fオペレーターとして\x01",
            "関わってきたわたしとしては\x01",
            "感動もひとしおですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#00002Fはは、俺たちも\x01",
            "支援課に戻ってきたことを\x01",
            "改めて実感するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x102,
        (
            "#00100Fふふっ、そうね。\x01",
            "またフランさんと一緒に\x01",
            "仕事が出来るし。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x9,
        (
            "#01909Fええ、オペレーションにも\x01",
            "熱が入るってものですよ～！\x02\x03",

            "#01906F皆さんがお休みの間、\x01",
            "市民からの依頼もひっきりなしで\x01",
            "対応にも一苦労でしたから……\x02\x03",

            "#01902F今回の支援課の活動再開は、\x01",
            "本当に心待ちにしていたんですよ～。\x02\x03",

            "#01909F……それに、ようやくお姉ちゃんと\x01",
            "一緒に働けるわけですし～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0294
    ChrTalk(
        0x101,
        "#00009Fはは……なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x109,
        (
            "#10106Fもう、フラン……\x01",
            "お姉ちゃんは駄目だって\x01",
            "何度言わせるつもりなの？\x02\x03",

            "#10101Fいい？　いくら姉妹でも\x01",
            "職場が同じになったからには\x01",
            "最低限の礼節は弁えないと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0296
    ChrTalk(
        0x9,
        (
            "#01906Fあう～……ごめんなさ～い。\x02\x03",

            "#01908Fで、でも、慣れないんだもん……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x109,
        "#10103Fだもんじゃありません。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x105,
        "#10302Fはは、厳しいお姉さんだねえ。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x9,
        (
            "#01906Fと、とにかく～……\x02\x03",

            "#01900Fあとはティオちゃんと\x01",
            "ランディさんが加われば\x01",
            "もはや敵ナシですよ。\x02\x03",

            "#01902Fふふ、皆さんが揃うのが\x01",
            "心から待ち遠しいです～。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#00004Fああ、俺も同じ気持ちだよ。\x02\x03",

            "#00002Fそれじゃ……\x01",
            "改めてよろしくな、フラン。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x9,
        "#01909Fはいっ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 1)
    Jump("loc_9C26")

    label("loc_9A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B7F")

    #C0302
    ChrTalk(
        0x9,
        (
            "#01902Fふふっ、また皆さんと仕事ができて\x01",
            "オペレーションにも熱が入りますね～。\x02\x03",

            "#01909Fお姉ちゃ……コホン。\x01",
            "ノエルさん、とも働けますし！\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x109,
        "#10106F（もう、この子ったら……）\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#00012F（はは、まあまあ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9C26")

    label("loc_9B7F")


    #C0305
    ChrTalk(
        0x9,
        (
            "#01900F支援課の活動再開にあたって、\x01",
            "これからたくさんの依頼が\x01",
            "入ってくると思います。\x02\x03",

            "#01909F以前のように、オペレーターとして\x01",
            "しっかりサポートさせて頂きますね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C26")

    TalkEnd(0x9)
    Return()

    # Function_18_7CED end

    def Function_19_9C2A(): pass

    label("Function_19_9C2A")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1300, 13270, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29370, 0)
    SetChrPos(0x101, 2550, 0, 12860, 0)
    SetChrPos(0x102, 3690, 0, 12840, 0)
    SetChrPos(0x109, 1950, 0, 11360, 0)
    SetChrPos(0x105, 3360, 0, 11340, 0)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0306
    ChrTalk(
        0x9,
        (
            "#01900Fあっ、丁度いいところに～！\x02\x03",

            "#01901F実はお姉ちゃ……ノエルさんに、\x01",
            "大事な話があるんだけど～……\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x109,
        (
            "#12P#10105Fど、どうしたのフラン？\x01",
            "そんな深刻な顔して……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x9,
        (
            "#01908Fあのね…………………………………\x02\x03",

            "#01906F……どうしても、職場で\x01",
            "『お姉ちゃん』って呼んじゃダメ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0309
    ChrTalk(
        0x101,
        "#00006F#12Pガクッ……\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x109,
        (
            "#12P#10106Fな、何事かと思ったら……\x02\x03",

            "#10101F……コホン。\x01",
            "支援課への出向が決まった時に\x01",
            "何度も説明したでしょう？\x02\x03",

            "#10103F職場が同じになったからには\x01",
            "最低限の礼節は弁えないとって。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x9,
        (
            "#01905Fだ、だってお姉ちゃ……\x01",
            "じゃなくって、ノエルさ……\x02\x03",

            "#01906Fああっ、やっぱりダメ～！\x01",
            "どうやっても慣れないよ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_9FDB():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FDB)
    Sleep(50)

    def lambda_9FEB():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FEB)
    Sleep(300)

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#00012Fま、まあ……ノエル。\x01",
            "そこまで厳しくすることは\x01",
            "ないんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        (
            "#00104Fふふ、そうね。\x01",
            "フランさんが『ノエルさん』って言うと\x01",
            "よそよそしすぎる気もするし……\x02\x03",

            "#00100F緊急を要する連絡の時に慣れない呼び方だと、\x01",
            "かえって非効率的にならないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x109,
        "#12P#10106Fそ、それはそうかもしれないですけど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0315
    ChrTalk(
        0x9,
        (
            "#01902Fほ、ほら～っ！\x01",
            "皆さんもこう言ってくださってるし！\x02\x03",

            "#01909F『お姉ちゃん』でいいでしょ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#12P#10304Fま、少しくらいユルい方が\x01",
            "支援課のスタンスには\x01",
            "合ってそうじゃない？\x02\x03",

            "#10302Fだってほら、課長からして\x01",
            "あんな感じなワケだし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0317
    ChrTalk(
        0x101,
        "#5P#00006F（その点は言い返せないな……）\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        (
            "#12P#10106F……はあ、まあ仕方ないですね。\x01",
            "皆さんがそうおっしゃるなら……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x9,
        (
            "#01909Fやった～！　じゃあ決まりだね！\x02\x03",

            "#01900Fえへへ、皆さんも\x01",
            "ありがとうございます～！\x02\x03",

            "#01904Fコホン、それじゃあ……\x02\x01",

            "#01909Fお姉ちゃん、改めてよろしくね㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0320
    ChrTalk(
        0x109,
        (
            "#12P#10101Fだ、だけどね、フラン。\x01",
            "くれぐれも公私混同だけは……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x9,
        "#01909F分かってるって、お姉ちゃん㈱\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x109,
        "#12P#10106F（ぜ、絶対分かってない……）\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#00012F（はは、ノエルもフランには形無しだな。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x13F, 0)
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3010, 0, 12380, 0)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_9C2A end

    def Function_20_A4AB(): pass

    label("Function_20_A4AB")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1300, 13270, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29370, 0)
    SetChrPos(0x101, 2400, 0, 12670, 0)
    SetChrPos(0x102, 3550, 0, 12670, 0)
    SetChrPos(0x103, 1360, 0, 12490, 0)
    SetChrPos(0x104, 1860, 0, 11200, 0)
    SetChrPos(0x109, 3040, 0, 11190, 0)
    SetChrPos(0x105, 4090, 0, 11380, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0324
    ChrTalk(
        0x9,
        (
            "#01900Fあ、ティオちゃん～！\x01",
            "ようやく帰ってきたみたいだね！\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x103,
        (
            "#12P#00202Fええ、おかげさまで。\x02\x03",

            "#00204Fフランさん、また改めて\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x9,
        (
            "#01909Fふふ、こちらこそ～。\x02\x03",

            "#01900Fともかく、これで\x01",
            "特務支援課の皆さんも\x01",
            "フルメンバーになりましたね～！\x02\x03",

            "より一層の活躍を期待してますよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#12P#00002Fはは、ありがとうフラン。\x01",
            "精一杯頑張らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0328
    ChrTalk(
        0x9,
        (
            "#01905Fあっそうだ……\x01",
            "改めてお礼を言わなくっちゃ！\x02\x03",

            "#01900Fお姉ちゃん、ユリア准佐のサインを\x01",
            "わたしの分ももらってくれたんでしょ～！\x02\x03",

            "#01909F本当にどうもありがとう～！\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x109,
        (
            "#12P#10102Fあはは、気にしないでいいから。\x02\x03",

            "#10106Fあたしだけ面と向かってお話しちゃって\x01",
            "フランに申し訳ないくらいだし……\x02\x03",

            "#10100Fまた今度、落ち着いた時に渡すね。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x9,
        "#01909Fうん、楽しみにしてるね～！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、そういえば昨日アルセイユで\x01",
            "エリィとノエルがもらってたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x102,
        (
            "#00100Fええ、姫殿下もユリア准佐も\x01",
            "本当に心の広い方だったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        (
            "#12P#00302Fハハ、やっぱりフランちゃんも\x01",
            "ユリア准佐のファンなのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x9,
        (
            "#01904Fもっちろんです！\x02\x03",

            "#01900Fユリア准佐は凛としてて\x01",
            "とってもかっこよくて……\x01",
            "本当に憧れちゃいますよ～。\x02\x03",

            "#01909Fまあ、それでもお姉ちゃんの方が\x01",
            "ダントツにかっこいいと思いますけど㈱\x02",
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
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0335
    ChrTalk(
        0x109,
        (
            "#12P#10111Fちょっ……ちょっと……！\x02\x03",

            "#10106Fな、なんて恐れ多いことを\x01",
            "言ってるの、フランってば……！\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、フランさんにとっては\x01",
            "何があろうとも\x01",
            "ノエルさんが一番みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        "#12P#00012Fう～ん、さすがだなあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x148, 5)
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3010, 0, 12380, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    EventEnd(0x5)
    Return()

    # Function_20_A4AB end

    def Function_21_ABB8(): pass

    label("Function_21_ABB8")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1300, 13270, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29370, 0)
    SetChrPos(0x101, 2400, 0, 12670, 0)
    SetChrPos(0x102, 3550, 0, 12670, 0)
    SetChrPos(0x103, 1360, 0, 12490, 0)
    SetChrPos(0x104, 1860, 0, 11200, 0)
    SetChrPos(0x109, 3040, 0, 11190, 0)
    SetChrPos(0x105, 4090, 0, 11380, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0338
    ChrTalk(
        0x9,
        (
            "#01905Fあ、皆さん……\x02\x03",

            "#01900F先ほどお伝えしたとおり、\x01",
            "導力ボートは港湾区の波止場に\x01",
            "手配しておきました～。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        "#12P#00000Fああ、ありがとうフラン。\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        "#12P#00100Fさっそく使わせてもらうわね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0341
    ChrTalk(
        0x9,
        (
            "#01903F遊撃士の方々を捜索するため\x01",
            "湿地帯に向かわれるそうですけど……\x02\x03",

            "#01908Fその、大丈夫なんでしょうか～……？\x01",
            "Ａ級にも届くほどの遊撃士が、\x01",
            "２人も行方不明になる場所なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#12P#00200Fフランさん……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        "#12P#00303Fすまねえな、心配かけちまうが……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x9,
        (
            "#01906Fはあ、こんな時わたしにも\x01",
            "何かできればいいんですけど……\x02\x03",

            "#01900Fあの、よかったらお守りに\x01",
            "バンバンを持っていきますか？\x02",
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
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0345
    ChrTalk(
        0x101,
        "#12P#00005Fバンバンってたしか……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x109,
        (
            "#12P#10106Fえっと……\x01",
            "クマのぬいぐるみですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x9,
        (
            "#01909F抱いてるとすごく落ち着くんだよ～！\x02\x03",

            "#01900Fお姉ちゃんも誰も見てない時に\x01",
            "たまにやってるでしょ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    #C0348
    ChrTalk(
        0x109,
        (
            "#12P#10111Fちょっ！？\x01",
            "あ、あたしはそんなこと……！\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x9,
        (
            "#01901Fバンバンを危ないかもしれない場所に\x01",
            "送り込むのは断腸の想いですけど、\x01",
            "皆さんのためならっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        (
            "#12P#00012Fい、いやいいから……\x01",
            "とりあえず君が落ち着いてくれ。\x02\x03",

            "#00002Fはは、でも気持ちはありがたいよ。\x01",
            "少し不安な気持ちはあったけど、\x01",
            "おかげで何だかリラックスできた気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、これぞフランの真骨頂だよね。\x02\x03",

            "#10309Fノエルのプライベートも垣間見れたし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0352
    ChrTalk(
        0x109,
        (
            "#12P#10106F（うう、フランったら\x01",
            "  後で覚えてなさいよ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x9,
        (
            "#01909Fあはは、だったらよかったです～。\x02\x03",

            "#01900F気をつけて行ってくださいね、皆さん！\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        "#00000Fああ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x17B, 7)
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3010, 0, 12380, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    EventEnd(0x5)
    Return()

    # Function_21_ABB8 end

    def Function_22_B30F(): pass

    label("Function_22_B30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B32D")
    Call(0, 47)
    Return()

    label("loc_B32D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B33E")
    Jump("loc_BDFC")

    label("loc_B33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B34C")
    Jump("loc_BDFC")

    label("loc_B34C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B3DF")

    #C0355
    ChrTalk(
        0xFE,
        (
            "赤い星座は、\x01",
            "クロスベルの総力をもって\x01",
            "何としても排除してみせます。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "あなたたちも、自分たちに\x01",
            "出来ることを尽くしてください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDFC")

    label("loc_B3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B3ED")
    Jump("loc_BDFC")

    label("loc_B3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B3FB")
    Jump("loc_BDFC")

    label("loc_B3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7DC")

    #C0357
    ChrTalk(
        0xFE,
        "ふう、染みますね……\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#00005F（エマさんの持っているビン、\x01",
            "  あれは栄養剤か何かか……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x103,
        (
            "#00200F（みたいですね……\x01",
            "  よほど疲れているんでしょうか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x105,
        (
            "#10302Fふふ、『スポリタンＸ』――\x02\x03",

            "なかなかパンチの効いたものを\x01",
            "飲んでいるみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0361
    ChrTalk(
        0x109,
        "#10105Fワ、ワジ君――\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    #C0362
    ChrTalk(
        0xFE,
        (
            "て、徹夜明けなのだから\x01",
            "仕方ないでしょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "それとも何ですか？\x01",
            "私が栄養ドリンクを飲むのが\x01",
            "そんなにおかしいと言うのですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "答えなさい――\x01",
            "ロイド・バニングス捜査官！\x02",
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

    #C0365
    ChrTalk(
        0x101,
        "#00006Fいや、俺は別に何も……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "ふ、ふん……\x01",
            "なら問題ないという事ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "とにかく、\x01",
            "あなたたちもこんな所で\x01",
            "油を売っていていいのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "その……支援要請とやらを\x01",
            "１つでも多くこなすべきでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#00006Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x105,
        "#10302F（フフ、何だか災難だったね。）\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        "#00001F（……お前が言うな。）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x171, 6)
    Jump("loc_B844")

    label("loc_B7DC")


    #C0372
    ChrTalk(
        0xFE,
        (
            "何はともあれ、こんな所で\x01",
            "油を売っていないで支援要請を\x01",
            "こなすべきでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        "――話は以上です。\x02",
    )

    CloseMessageWindow()

    label("loc_B844")

    Jump("loc_BDFC")

    label("loc_B849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B857")
    Jump("loc_BDFC")

    label("loc_B857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B865")
    Jump("loc_BDFC")

    label("loc_B865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BA96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B88D")
    Call(0, 30)
    Jump("loc_B933")

    label("loc_B88D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B89F")
    Call(0, 31)
    Jump("loc_B933")

    label("loc_B89F")


    #C0374
    ChrTalk(
        0xFE,
        (
            "ダドリーさんが\x01",
            "支援課に期待しているのは\x01",
            "遊軍としての活躍です。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "その意味をよく考えれば\x01",
            "やるべきことは見えるはず……\x01",
            "よろしく頼みましたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B933")

    Jump("loc_BA91")

    label("loc_B938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA04")

    #C0376
    ChrTalk(
        0xFE,
        (
            "レクター・アランドール、\x01",
            "キリカ・ロウランについては\x01",
            "捜査一課でマークを続けましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "２大国が何を企んでいるか……\x01",
            "現時点では計りようもないですが、\x01",
            "根気強く調査をしてみないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_BA91")

    label("loc_BA04")


    #C0378
    ChrTalk(
        0xFE,
        (
            "レクター・アランドール、\x01",
            "キリカ・ロウランについては\x01",
            "捜査一課に任せて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "あなた達は、一度あなた達の\x01",
            "業務に戻るといいでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA91")

    Jump("loc_BDFC")

    label("loc_BA96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BDE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD4B")

    #C0380
    ChrTalk(
        0xFE,
        (
            "バニングス捜査官……\x01",
            "支援要請の仕事は順調ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#00000Fええまあ……とりあえず\x01",
            "いつものペースでこなしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        "……そうですか。\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "ちなみにダドリーさんは\x01",
            "オルキスタワーで本会議における\x01",
            "警備体制の最終確認を行っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "セルゲイ課長も本日一杯は\x01",
            "２階の対策本部にて各方面と調整予定。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "……あなたたちも、\x01",
            "気を引き締めて仕事に臨む事ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "それこそ、\x01",
            "いつものペースと言わず#22R㈲  ㈲  ㈲  ㈲  ㈲  ㈲  ㈲  ㈲  ㈲  ㈲  ㈲#にね。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        "#00001Fは、はい、了解です。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x105,
        (
            "#10302F（フフ、相変わらず\x01",
            "  手厳しいお姉さんだね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x104,
        (
            "#00303F（う～ん、黙ってりゃ\x01",
            "  けっこう美人なんだがなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x109,
        (
            "#10106F（ランディ先輩、\x01",
            "  そういう問題じゃ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 0)
    Jump("loc_BDE0")

    label("loc_BD4B")


    #C0391
    ChrTalk(
        0xFE,
        (
            "ダドリーさんもセルゲイ課長も\x01",
            "自分の持てる力を最大限に発揮して\x01",
            "任務に当たっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "……あなたたちも、\x01",
            "気を引き締めて仕事に臨む事ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDE0")

    Jump("loc_BDFC")

    label("loc_BDE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BDF3")
    Jump("loc_BDFC")

    label("loc_BDF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_BDFC")

    label("loc_BDFC")

    TalkEnd(0xFE)
    Return()

    # Function_22_B30F end

    def Function_23_BE00(): pass

    label("Function_23_BE00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE1F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE1F")
    Call(0, 52)
    Return()

    label("loc_BE1F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_23_BE00 end

    def Function_24_BE26(): pass

    label("Function_24_BE26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BE37")
    Jump("loc_C635")

    label("loc_BE37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE45")
    Jump("loc_C635")

    label("loc_BE45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C00A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF4B")

    #C0393
    ChrTalk(
        0xFE,
        (
            "ったく、恐ろしく\x01",
            "厄介な事になりやがったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "とりあえず二課では現状、\x01",
            "他の全ての案件に目を瞑って\x01",
            "一課のサポートに努めている所でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "クロスベル入りしている諜報員……\x01",
            "特に帝国の諜報員の情報を片っ端から\x01",
            "洗っている最中だぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C005")

    label("loc_BF4B")


    #C0396
    ChrTalk(
        0xFE,
        (
            "とりあえず二課では現状、\x01",
            "他の全ての案件に目を瞑って\x01",
            "一課のサポートに努めている所でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "クロスベル入りしている諜報員……\x01",
            "特に帝国の諜報員の情報を片っ端から\x01",
            "洗っている最中だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C005")

    Jump("loc_C635")

    label("loc_C00A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C1BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C142")

    #C0398
    ChrTalk(
        0xFE,
        "グノーシスか……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "まずは定石通り、\x01",
            "ルバーチェ方面のルートから\x01",
            "改めて当たっていく予定だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "どうにも、そっち方面から\x01",
            "流れた可能性は低い気がすんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "ま、とにかく今の段階で\x01",
            "あれこれ考えても仕方ねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "とりあえずは、１つずつ\x01",
            "確実に潰して行くしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C1B8")

    label("loc_C142")


    #C0403
    ChrTalk(
        0xFE,
        (
            "ま、とにかく今の段階で\x01",
            "あれこれ考えても仕方ねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "とりあえずは、１つずつ\x01",
            "確実に潰して行くしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1B8")

    Jump("loc_C635")

    label("loc_C1BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C1CB")
    Jump("loc_C635")

    label("loc_C1CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C368")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C2A1")

    #C0405
    ChrTalk(
        0xFE,
        (
            "支援課の協力があったとはいえ、\x01",
            "レイモンドのヤツも昨日は\x01",
            "なかなかよく頑張ったみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "だが偽ブランド商を追いかけて\x01",
            "テロリストの残党に遭遇するたあ、\x01",
            "つくづくあり得ねえ話だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C363")

    label("loc_C2A1")


    #C0407
    ChrTalk(
        0xFE,
        (
            "黒月が裏で動いていたとはいえ、\x01",
            "レイモンドのヤツも昨日は１人で\x01",
            "なかなかよく頑張ったみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "だが偽ブランド商を追いかけて\x01",
            "テロリストの残党に遭遇するたあ、\x01",
            "つくづくあり得ねえ話だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C363")

    Jump("loc_C635")

    label("loc_C368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C40B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C383")
    Call(0, 25)
    Jump("loc_C406")

    label("loc_C383")


    #C0409
    ChrTalk(
        0xFE,
        (
            "本来は一課の領分の仕事も\x01",
            "いくつかは二課の方で\x01",
            "引き受けることになってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "何せこの状況だ。\x01",
            "まさに総動員の体制ってこった。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C406")

    Jump("loc_C635")

    label("loc_C40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C419")
    Jump("loc_C635")

    label("loc_C419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C427")
    Jump("loc_C635")

    label("loc_C427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C435")
    Jump("loc_C635")

    label("loc_C435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C49D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C450")
    Call(0, 26)
    Jump("loc_C498")

    label("loc_C450")


    #C0411
    ChrTalk(
        0xA,
        (
            "無軌道な若者か……\x01",
            "ったく、人様に迷惑かけて\x01",
            "何が楽しいんだかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C498")

    Jump("loc_C635")

    label("loc_C49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4B8")
    Call(0, 27)
    Jump("loc_C635")

    label("loc_C4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5C7")

    #C0412
    ChrTalk(
        0xFE,
        (
            "まあ、とにかくだ。\x01",
            "今後とも何かあった時は\x01",
            "よろしく頼むぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "お前たちには、俺たち捜査二課も\x01",
            "期待してるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        (
            "#00002Fは、はい。\x02\x03",

            "（なんか、こういう言葉って\x01",
            "  純粋に嬉しいな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x102,
        (
            "#00102F（ええ、私たちも随分\x01",
            "  認められた気がするわね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C635")

    label("loc_C5C7")


    #C0416
    ChrTalk(
        0xFE,
        (
            "ま、今後とも何かあった時は\x01",
            "どうかよろしく頼むぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "お前たちには、俺たち捜査二課も\x01",
            "期待してるからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C635")

    TalkEnd(0xFE)
    Return()

    # Function_24_BE26 end

    def Function_25_C639(): pass

    label("Function_25_C639")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    #C0418
    ChrTalk(
        0xA,
        "よう、特務支援課じゃねえか。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    #C0419
    ChrTalk(
        0xC,
        (
            "#00603F誰かと思ったらお前たちか。\x02\x03",

            "#00600F何でも《幻獣》の\x01",
            "調査を引き受けたらしいな？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        "#00000Fええ、そうですが……\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x105,
        "#10300Fフフ、流石に耳が早いね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x105, 500)

    #C0422
    ChrTalk(
        0xC,
        (
            "#00603Fフン、警備隊の正式な依頼だからな。\x01",
            "当然情報は流れて来るわけだが……\x02\x03",

            "#00600F話を聞く限り、どうやら常識では\x01",
            "計り切れない相手のようだからな。\x02\x03",

            "交戦する場合は、\x01",
            "せいぜい気合いを入れて行けよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        "#00100Fご忠告ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x101,
        (
            "#00005Fそれにしても……\x01",
            "そちらは防諜の仕事が\x01",
            "かなり忙しいみたいですね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0425
    ChrTalk(
        0xA,
        (
            "まあ、独立の提唱なんてモンが\x01",
            "声高になされちまったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xA,
        (
            "クロスベルの動向を探ろうと、\x01",
            "大陸各国から諜報員が次々と\x01",
            "送られて来ている状況なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xA,
        (
            "それこそ、単純に\x01",
            "把握しようとするだけで\x01",
            "手一杯なほどの数の諜報員がな。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x109,
        "#10105Fそ、そんなにですか……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    #C0429
    ChrTalk(
        0xC,
        (
            "#00601F……加えて《赤い星座》や\x01",
            "《黒月》の動向のこともある。\x02\x03",

            "さらに当然、\x01",
            "それら以外の犯罪の対応にも\x01",
            "手を抜くわけにはいかんからな。\x02\x03",

            "#00603F対処すべき案件は、\x01",
            "まさに幾らでも存在する状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xA,
        (
            "ま、そんな事情もあって\x01",
            "一課の領分の仕事のいくつかを\x01",
            "二課で引き受けることになってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xA,
        (
            "そのことで、ちょいと\x01",
            "打ち合わせをしてたってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x103,
        (
            "#00200Fなるほど……\x01",
            "そういう話をしていたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x104,
        (
            "#00300Fなんつうか、\x01",
            "色々と厳しい状況みてえだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x104, 500)

    #C0434
    ChrTalk(
        0xC,
        (
            "#00603Fフン、例えいかに\x01",
            "手札が限られていようと\x01",
            "やるべきことをやるだけだがな。\x02\x03",

            "#00601Fとにかく、お前たちも\x01",
            "与えられた役目を果たすことだ。\x02\x03",

            "《幻獣》の件にしても、およそ\x01",
            "放っておける問題ではないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#00001Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    SetScenarioFlags(0x16A, 2)
    Return()

    # Function_25_C639 end

    def Function_26_CC3F(): pass

    label("Function_26_CC3F")

    OP_4B(0xA, 0xFF)
    OP_4B(0x14, 0xFF)

    #C0436
    ChrTalk(
        0xA,
        (
            "そういえば、\x01",
            "例の暴走車の若者ですが……\x01",
            "昨日、検挙したんですってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x14,
        "まー、流石に放置できなくてなー。\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x14,
        (
            "罰金刑だけだから本人たちは\x01",
            "堪えていないみたいだったがー。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x14,
        (
            "とりあえず今日、市内で\x01",
            "見かけないことを考えると少しは\x01",
            "効果があったんじゃないかなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xA,
        "ふぅ、だといいんですがね。\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xA,
        (
            "ったく、外国人じゃなきゃ\x01",
            "拘留してこってり絞ることも\x01",
            "出来たんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xA,
        (
            "ま、その辺は今後の法整備に\x01",
            "期待ってところですかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x14,
        (
            "そうだねー、まあ\x01",
            "ウチらは地道にやれることを\x01",
            "やるだけだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_CEC8")

    #C0444
    ChrTalk(
        0x101,
        (
            "#00001F（どうやら、\x01",
            "  あの３人組の話のようだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x102,
        (
            "#00103F（みたいね、危険な運転は\x01",
            "  二度として欲しくない所だけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF06")

    label("loc_CEC8")


    #C0446
    ChrTalk(
        0x101,
        (
            "#00001F（昨日、か……\x01",
            "  市内で何か事件があったのかな？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF06")

    SetScenarioFlags(0x13E, 7)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_26_CC3F end

    def Function_27_CF1C(): pass

    label("Function_27_CF1C")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 500)

    #C0447
    ChrTalk(
        0xA,
        (
            "お、何か新鮮な顔ぶれが\x01",
            "混じっているようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xA,
        (
            "もしかして、そいつらが噂の\x01",
            "特務支援課の新メンバーか？\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        "#00000Fええ、その通りです。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x109, 500)

    #C0450
    ChrTalk(
        0xB,
        (
            "ということは、\x01",
            "君が警備隊のノエルちゃん？\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xB,
        (
            "むふふ、よかったら\x01",
            "今度一緒にお茶でもどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x109,
        "#10106Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x105,
        "#10302Fフフ、おあいにく様だってさ。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xB,
        "へっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 500)

    #C0455
    ChrTalk(
        0xB,
        (
            "って、そういうお前は\x01",
            "テスタメンツのワジ・ヘミスフィア。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xB,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xB,
        (
            "……何ていうか、近くで見ると\x01",
            "けっこう綺麗な顔してんだな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x105,
        (
            "#10302Fふふ、そうかい？\x02\x03",

            "#10304Fけど残念ながら、僕は君のことが\x01",
            "タイプじゃないみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xB,
        "そ、そうなんだ……\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xB,
        (
            "――って、なんで男同士で\x01",
            "へこまないといけないんだよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)
    TurnDirection(0xA, 0xB, 500)

    #C0461
    ChrTalk(
        0xA,
        (
            "……ったく、黙って聞いてりゃ\x01",
            "くだらねえ事ばっか言いやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xA,
        (
            "オメーも、ちっとは支援課の\x01",
            "連中を見習って成長してみやがれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xA,
        (
            "何ならまた、警察学校から\x01",
            "出直せるように手配してやろうか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0464
    ChrTalk(
        0xB,
        (
            "警部～、それだけは\x01",
            "カンベンしてくださいよ～。\x02",
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
    OP_93(0xA, 0xE1, 0x0)
    OP_93(0xB, 0x2D, 0x0)
    SetScenarioFlags(0x13F, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_27_CF1C end

    def Function_28_D3A3(): pass

    label("Function_28_D3A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D58D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D522")

    #C0465
    ChrTalk(
        0xFE,
        (
            "やあ、聞いてくれよ～。\x01",
            "もうすぐドノバン警部が\x01",
            "警察に復帰するんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xFE,
        (
            "警部の穴を埋めるために\x01",
            "色々苦労も多かったけど、\x01",
            "これてやっと解放されそうだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        "#00002Fはは、よかったですね。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x103,
        (
            "#00200F警部にそんな事を聞かれたら\x01",
            "どやされそうですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0469
    ChrTalk(
        0xFE,
        (
            "お、おっと、それもそうだね。\x01",
            "……ナイショにしといてくれよ～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_D588")

    label("loc_D522")


    #C0470
    ChrTalk(
        0xFE,
        (
            "警部が帰ってくるなら\x01",
            "捜査二課も安心だよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0xFE,
        (
            "よ～し、それまで僕らも\x01",
            "がんばってかないとね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D588")

    Jump("loc_DD06")

    label("loc_D58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D59B")
    Jump("loc_DD06")

    label("loc_D59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D647")

    #C0472
    ChrTalk(
        0xFE,
        (
            "事前連絡もなしに\x01",
            "いきなりやって来て\x01",
            "国防軍に組み込むだなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xFE,
        (
            "大声じゃ言えないけど、\x01",
            "ほんと横暴もいい所だよな～。\x01",
            "……はぁ、一体どうなってんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD06")

    label("loc_D647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D655")
    Jump("loc_DD06")

    label("loc_D655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D72C")

    #C0474
    ChrTalk(
        0xFE,
        (
            "帝国は既に、犯行への関与を\x01",
            "否定しているみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xFE,
        (
            "それでも何とか水面下で\x01",
            "交渉できないか模索している所なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        (
            "こんなことをしでかすワケだから、\x01",
            "何か狙いがあるのは間違いないからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD06")

    label("loc_D72C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D7C0")

    #C0477
    ChrTalk(
        0xFE,
        (
            "ヴァルド・ヴァレスが\x01",
            "どこでグノーシスを手に入れたか……\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xFE,
        (
            "仮にルバーチェ経由じゃないとしたら、\x01",
            "一体どこのルートなんだろうね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD06")

    label("loc_D7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D7CE")
    Jump("loc_DD06")

    label("loc_D7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DA76")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D9CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D989")

    #C0479
    ChrTalk(
        0xFE,
        (
            "ああ、君たち～。\x01",
            "昨日は本当に助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xFE,
        (
            "そうそう、そういえば昨日の夜は\x01",
            "夢にあの婆さんが出て来てさ～。\x01",
            "なぜか逆に追いかけられるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        (
            "ふう、おかげで\x01",
            "あんまり眠れなかったんだよね。\x02",
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

    #C0482
    ChrTalk(
        0x101,
        (
            "#00006F（何かそう言われると、\x01",
            "  こっちまで夢に見そうだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x102,
        "#00106F（……頑張って忘れましょ。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_D9C9")

    label("loc_D989")


    #C0484
    ChrTalk(
        0xFE,
        (
            "とにかく、\x01",
            "昨日はほんとにありがとう。\x01",
            "おかげで助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9C9")

    Jump("loc_DA71")

    label("loc_D9CE")


    #C0485
    ChrTalk(
        0xFE,
        (
            "ふう、昨日はすごく\x01",
            "イヤな夢を見ちゃってね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "昨日連行されてった婆さんに\x01",
            "追いかけられる夢なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xFE,
        (
            "ぞわわ、思い返すと\x01",
            "イヤな汗が出て来るよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA71")

    Jump("loc_DD06")

    label("loc_DA76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DA84")
    Jump("loc_DD06")

    label("loc_DA84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DA92")
    Jump("loc_DD06")

    label("loc_DA92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DAA0")
    Jump("loc_DD06")

    label("loc_DAA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DAAE")
    Jump("loc_DD06")

    label("loc_DAAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DC62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBBA")

    #C0488
    ChrTalk(
        0xFE,
        (
            "ふう、このところ本部内の\x01",
            "空気もピリピリしっ放しでね。\x01",
            "ほんと参っちゃうよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xFE,
        (
            "議員や上層部からの圧力も\x01",
            "一応は減ってはいるとはいえ、\x01",
            "自治州の抱える問題は山積み……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "はあ、一体いつになったら少しは\x01",
            "楽できるようになるんだろうね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_DC5D")

    label("loc_DBBA")


    #C0491
    ChrTalk(
        0xFE,
        (
            "まあでも、とりあえずは\x01",
            "ディーター市長の政治改革を\x01",
            "心の支えにして頑張るしかないよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        (
            "あとは議会の方で給与の底上げを\x01",
            "してくれると嬉しいな～、なんてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC5D")

    Jump("loc_DD06")

    label("loc_DC62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DD06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC7D")
    Call(0, 27)
    Jump("loc_DD06")

    label("loc_DC7D")


    #C0493
    ChrTalk(
        0xFE,
        (
            "はぁ、警部にはまた\x01",
            "痛いところを突かれちゃったよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "オレももう少し\x01",
            "しっかりしたいとは思うんだけど……\x01",
            "性格は直せないからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD06")

    TalkEnd(0xFE)
    Return()

    # Function_28_D3A3 end

    def Function_29_DD0A(): pass

    label("Function_29_DD0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DD1B")
    Jump("loc_E2F5")

    label("loc_DD1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DD29")
    Jump("loc_E2F5")

    label("loc_DD29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DF8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEDC")

    #C0495
    ChrTalk(
        0xC,
        (
            "#00600Fお前たちか。\x02\x03",

            "#00603F……オルランドの話は聞いた。\x01",
            "どうやら面倒な事に\x01",
            "なっているらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x101,
        "#00001Fええ、ですが必ず連れ戻します。\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xC,
        (
            "#00603Fフン、そうか。\x01",
            "ならば何も言うことはない。\x02\x03",

            "#00600Fとにかく今はこんな状況だ。\x01",
            "お前たちに押し付けたい仕事も\x01",
            "当然山のようにある。\x02\x03",

            "そのためにも、\x01",
            "仲間の問題なんてものは\x01",
            "さっさと解決してこい。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x102,
        "#00100Fダドリーさん……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        "#00001Fはい、もちろんです！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 3)
    Jump("loc_DF89")

    label("loc_DEDC")


    #C0500
    ChrTalk(
        0xC,
        (
            "#00603F私は打ち合わせを済ませたら、\x01",
            "市長の所に出向いて次の対策について\x01",
            "話し合いをしてくる予定だ。\x02\x03",

            "#00600Fお前たちもとにかく、やるべき事を\x01",
            "さっさと片付けて来るがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF89")

    Jump("loc_E2F5")

    label("loc_DF8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DF9C")
    Jump("loc_E2F5")

    label("loc_DF9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DFAA")
    Jump("loc_E2F5")

    label("loc_DFAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DFB8")
    Jump("loc_E2F5")

    label("loc_DFB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E05F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFD3")
    Call(0, 25)
    Jump("loc_E05A")

    label("loc_DFD3")


    #C0501
    ChrTalk(
        0xC,
        (
            "#00600F案件は山積している状況だが、\x01",
            "とにかく防諜はこちらに任せておけ。\x02\x03",

            "お前たちは、お前たちの役目を\x01",
            "果たすことだけ考えることだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E05A")

    Jump("loc_E2F5")

    label("loc_E05F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E06D")
    Jump("loc_E2F5")

    label("loc_E06D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E2D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E095")
    Call(0, 30)
    Jump("loc_E123")

    label("loc_E095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0A7")
    Call(0, 31)
    Jump("loc_E123")

    label("loc_E0A7")


    #C0502
    ChrTalk(
        0xC,
        (
            "#00603F私の方は、ここでしばらく\x01",
            "各方面の情報に目を配る予定だ。\x02\x03",

            "#00600F何かあれば直接でもいい。\x01",
            "いつでも連絡してこい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E123")

    Jump("loc_E2CB")

    label("loc_E128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E256")

    #C0503
    ChrTalk(
        0xFE,
        (
            "#00603F帝国軍情報局と、\x01",
            "共和国のロックスミス機関……\x01",
            "どちらも侮れない相手だ。\x02\x03",

            "その２つが接触していたとなると……\x01",
            "水面下で何らかの動きがあるのは\x01",
            "間違いなさそうだな。\x02\x03",

            "#00600Fとにかく、今は警察として\x01",
            "出来ることをしていくしかあるまい。\x02\x03",

            "また何かあったら\x01",
            "こちらにも連絡するがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E2CB")

    label("loc_E256")


    #C0504
    ChrTalk(
        0xFE,
        (
            "#00600Fとにかく、今は警察として\x01",
            "出来ることをしていくしかあるまい。\x02\x03",

            "また何かあったら\x01",
            "こちらにも連絡するがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2CB")

    Jump("loc_E2F5")

    label("loc_E2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E2DE")
    Jump("loc_E2F5")

    label("loc_E2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E2EC")
    Jump("loc_E2F5")

    label("loc_E2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E2F5")

    label("loc_E2F5")

    TalkEnd(0xFE)
    Return()

    # Function_29_DD0A end

    def Function_30_E2F9(): pass

    label("Function_30_E2F9")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xC, 0x0)
    OP_4B(0xD, 0x0)
    OP_68(-59230, 1730, 14590, 0)
    MoveCamera(47, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23690, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -59000, 30, 14800, 45)
    SetChrPos(0x102, -58970, 30, 16280, 90)
    SetChrPos(0x104, -57950, 0, 14250, 0)
    SetChrPos(0x109, -59810, 30, 14920, 45)
    SetChrPos(0x105, -59060, 0, 13870, 45)
    OP_93(0xC, 0xE1, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_0D()
    Sleep(500)

    #C0505
    ChrTalk(
        0xC,
        "#00600F#2Pお前たちか。\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xD,
        "#5P……何か御用ですか？\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#00001F#6Pええ……どうしても捜査一課に\x01",
            "報告したい事がありまして。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0508
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キリカとレクターが\x01",
            "市内に現れたことを報告した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0509
    ChrTalk(
        0xC,
        (
            "#00603F#2P……なるほどな。\x02\x03",

            "帝国軍情報局とロックスミス機関、\x01",
            "両機関の重要人物が市内に……か。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xD,
        "#5Pダドリーさん、これは……\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x101,
        (
            "#00001F#6P……今回の件、どう見ますか？\x02\x03",

            "本会議を明日に控えたタイミングで\x01",
            "２大国の諜報員が現れたわけですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x102,
        "#00108F#6P偶然にしては出来すぎよね……\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x105,
        (
            "#10302F#12Pフフ、本人たちはお使いとか\x01",
            "気晴らしだとか言ってたけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x109,
        "#10106F#6Pさ、流石に怪しすぎるでしょ。\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xC,
        (
            "#00603F#2P無論、何らかの思惑はあるのだろう。\x02\x03",

            "#00600Fだが、それはどちらかといえば\x01",
            "直接彼らと話したお前たちだからこそ\x01",
            "感じとれるものがあるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        "#00303F#12P……確かにそうかもしれねえな。\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xC,
        (
            "#00600F#2P……逆に聞こう、バニングス。\x01",
            "彼らは一体何のために、\x01",
            "市内に姿を現したと思う？\x02\x03",

            "#00603F彼らとの会話や、移動ルート……\x01",
            "どこかにヒントがあったはずだ。\x02\x03",

            "#00600F推測で構わん、言ってみるがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        "#00001F#6Pそ、そうですね……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0519
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "キリカとレクターが\x01",
            "市内に姿を現した理由は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "首脳の警備のため\x01",          # 0
            "息抜きと買い物のため\x01",      # 1
            "密談をするため\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E89A"),
        (1, "loc_E9FA"),
        (2, "loc_EB8B"),
        (SWITCH_DEFAULT, "loc_EBDC"),
    )


    label("loc_E89A")


    #C0520
    ChrTalk(
        0x101,
        (
            "#00001F#6P首脳の警備のため、でしょうか？\x02\x03",

            "#00003Fいざという時のために\x01",
            "クロスベル市内の地形の\x01",
            "把握をしていたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xC,
        (
            "#00603F#2P……その可能性は低いだろう。\x02\x03",

            "#00600F警備は諜報員の管轄外だろうし、\x01",
            "もとより彼らは数ヶ月前から\x01",
            "クロスベルを訪れていたのだ。\x02\x03",

            "今更、街の地形を確認する\x01",
            "必要性などあるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        "#00006F#6Pた、確かにそうですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_EBDC")

    label("loc_E9FA")


    #C0523
    ChrTalk(
        0x101,
        (
            "#00001F#6P……やはり、彼らが言っていた通り、\x01",
            "息抜きと買い物のためでしょうか？\x02\x03",

            "#00003F通商会議に臨むに当たって、\x01",
            "必要じゃないとは言い切れませんし……\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xC,
        (
            "#00603F#2P……その可能性は無いだろう。\x02\x03",

            "#00600Fはぐらかされたことも考えると、\x01",
            "それらは単なる擬装にすぎないはずだ。\x02\x03",

            "#00606Fふう、やれやれ……\x01",
            "もう少し出来ると思っていたんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#00001F#6Pま、待ってください。\x01",
            "えっと、それじゃあ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBDC")

    label("loc_EB8B")

    OP_2C(0xA3, 0x1)

    #C0526
    ChrTalk(
        0x101,
        (
            "#00001F#6P……２人が密談の場を設けていた\x01",
            "可能性はあると思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBDC")

    label("loc_EBDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC5C")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0527
    ChrTalk(
        0x101,
        (
            "#00001F#6Pそうだ、もしかしたら……\x01",
            "２人が密談の場を設けていた\x01",
            "可能性はあると思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC5C")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_ECD6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ECD6)
    Sleep(50)

    def lambda_ECE6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_ECE6)
    Sleep(50)

    def lambda_ECF6():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_ECF6)
    Sleep(50)

    def lambda_ED06():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ED06)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    #C0528
    ChrTalk(
        0xD,
        "#5P密談……ですか？\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xC,
        "#00600F#2Pフム……なぜそう思う？\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x101,
        (
            "#00003F#6P彼らの最初の目撃情報は、\x01",
            "どちらも港湾区で得られました。\x02\x03",

            "#00001F俺たちが追跡を開始する前に、\x01",
            "２人が同じ区画にいた……\x01",
            "これは偶然とは思えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x102,
        (
            "#00105F#5Pあ……確かにそうだったわね。\x02\x03",

            "#00100F港湾区にあるＩＢＣでは\x01",
            "前日から大統領による視察が\x01",
            "予定されていたし……\x02\x03",

            "密談という目的で待ち合わせるには\x01",
            "好都合な場所だったかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x109,
        (
            "#10100F#6P丁度開催されていた\x01",
            "みっしぃのイベントも\x01",
            "カムフラージュになりそうですしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xD,
        (
            "#5Pそれぞれ、束の間の息抜き、\x01",
            "大統領の買い物という偽装をしつつ\x01",
            "密かに会っていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xD,
        "#5P……辻褄は合いそうですですね。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x104,
        (
            "#00301F#12Pしかし、密談って言っても\x01",
            "何を話してたってんだ？\x02\x03",

            "そもそも、帝国と共和国は\x01",
            "対立関係にあったはずじゃ\x01",
            "なかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x102,
        (
            "#00108F#5P……考えられないことじゃないわ。\x02\x03",

            "#00103F先の教団事件によって、\x01",
            "自治州議会から帝国派と共和国派の\x01",
            "議員の多くが失脚し……\x02\x03",

            "新市長と新議長の協力体制が\x01",
            "築かれたことで、クロスベルは\x01",
            "徐々に発言力を持ち始めている。\x02\x03",

            "#00101Fこんな状況……帝国と共和国が\x01",
            "そのままにしておくわけがないもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x101,
        "#00005F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x105,
        (
            "#10300F#12Pなるほど、その点で２大国は\x01",
            "利害が一致しているわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xC,
        (
            "#00608F#2P断言することは出来んが……\x01",
            "水面下で何らかの動きがあるのは\x01",
            "間違いなさそうだな。\x02\x03",

            "#00603F……現時点で言えるのはこんな所か。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F22D():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F22D)
    Sleep(50)

    def lambda_F23D():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F23D)
    Sleep(50)

    def lambda_F24D():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F24D)
    Sleep(50)

    def lambda_F25D():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F25D)
    Sleep(50)

    def lambda_F26D():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F26D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    #C0540
    ChrTalk(
        0xD,
        (
            "#5Pレクター・アランドール、\x01",
            "キリカ・ロウランについては\x01",
            "捜査一課でマークを続けましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xD,
        "#5P報告、ご苦労様でした。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        "#00000F#6Pいえ、お力になれたなら幸いです。\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x102,
        (
            "#00108F#6P明日の本会議……\x01",
            "つつがなく終わればいいんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xC,
        (
            "#00603F#2Pそのためにも、今は警察として\x01",
            "出来ることをしていくしかあるまい。\x02\x03",

            "#00601Fまた何かあったら\x01",
            "こちらにも連絡するがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        "#00000F#6Pはい、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_2C(0xA3, 0x1)
    OP_29(0xA3, 0x1, 0xD)
    OP_93(0xC, 0x0, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, -59320, 30, 14570, 45)
    SetScenarioFlags(0x1C7, 4)
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_30_E2F9 end

    def Function_31_F476(): pass

    label("Function_31_F476")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xD, 0x101, 0)

    #C0546
    ChrTalk(
        0xD,
        "バニングス捜査官。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    #C0547
    ChrTalk(
        0xC,
        (
            "#00600Fお前たちか。\x01",
            "何かあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        "#00000Fいえ、今の所は特に。\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xC,
        (
            "#00603Fそうか……だが\x01",
            "くれぐれも気は抜くなよ。\x02\x03",

            "お前たちも感じたと思うが、\x01",
            "ＶＩＰの来訪に街全体が\x01",
            "少々浮き立っている状態だ。\x02\x03",

            "#00600Fどんな異常にせよ、\x01",
            "こういった雰囲気の中では\x01",
            "紛れやすいものだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x109,
        "#10101F確かにそうですね……\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、よく目を\x01",
            "凝らしていかないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#00100Fちなみにダドリーさんは、\x01",
            "しばらくこちらの方に\x01",
            "いらっしゃるんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    #C0553
    ChrTalk(
        0xC,
        (
            "#00603Fまあな、とりあえず首脳たちの\x01",
            "アルカンシェル観劇が始まるまでは\x01",
            "本部に詰めている予定だ。\x02\x03",

            "#00600F何かあれば直接でもいい。\x01",
            "いつでも連絡してこい。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        "#00000Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_31_F476 end

    def Function_32_F73B(): pass

    label("Function_32_F73B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F74C")
    Jump("loc_F837")

    label("loc_F74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F780")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F77B")

    #C0555
    ChrTalk(
        0x11,
        "…………チッ…………\x02",
    )

    CloseMessageWindow()

    label("loc_F77B")

    Jump("loc_F837")

    label("loc_F780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F78E")
    Jump("loc_F837")

    label("loc_F78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F837")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7B5")
    Call(0, 33)
    Jump("loc_F837")

    label("loc_F7B5")

    ClearChrFlags(0x11, 0x10)

    #C0556
    ChrTalk(
        0x11,
        (
            "俺たちを捕まえても\x01",
            "罰金しか与えられないってのに、\x01",
            "必死すぎるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x11,
        (
            "フフ、警察はそんなに\x01",
            "小遣い稼ぎがしたいのか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F837")

    TalkEnd(0xFE)
    Return()

    # Function_32_F73B end

    def Function_33_F83B(): pass

    label("Function_33_F83B")


    #C0558
    ChrTalk(
        0xF,
        (
            "それじゃあ……\x01",
            "君たちが今住んでいる家は\x01",
            "どこにあるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x11,
        "フン、答えてやる義理はないな。\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x11,
        (
            "まあ、お前のような庶民には\x01",
            "到底住めないような場所……\x01",
            "とだけは言っておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xF,
        "（く、くそお……！）\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x101,
        "#00001F（が、がんばれフランツ……）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_33_F83B end

    def Function_34_F943(): pass

    label("Function_34_F943")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F954")
    Jump("loc_FA5B")

    label("loc_F954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F9B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F9AE")

    #C0563
    ChrTalk(
        0x12,
        "免停……免停かあ。\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x12,
        (
            "しかも１ヶ月って……\x01",
            "はあああああああ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9AE")

    Jump("loc_FA5B")

    label("loc_F9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F9C1")
    Jump("loc_FA5B")

    label("loc_F9C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FA5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FA5B")

    #C0565
    ChrTalk(
        0x12,
        (
            "お前ら……\x01",
            "バリケードを組んでいた奴らだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x12,
        (
            "フン、浅知恵を働かせやがって。\x01",
            "あんまり調子に乗ってると\x01",
            "ロクな目に合わないぜ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA5B")

    TalkEnd(0xFE)
    Return()

    # Function_34_F943 end

    def Function_35_FA5F(): pass

    label("Function_35_FA5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FA70")
    Jump("loc_FB73")

    label("loc_FA70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FB17")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FB12")

    #C0567
    ChrTalk(
        0x13,
        (
            "はあ、今回ばっかりは\x01",
            "さすがにやりすぎだったよな……。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x13,
        (
            "車もオシャカになっちゃったし、\x01",
            "しばらくはおとなしく\x01",
            "しといた方がよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB12")

    Jump("loc_FB73")

    label("loc_FB17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FB25")
    Jump("loc_FB73")

    label("loc_FB25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FB73")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FB73")

    #C0569
    ChrTalk(
        0x13,
        (
            "あー、早く帰りてーなー。\x01",
            "取調べなんてかったりーよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB73")

    TalkEnd(0xFE)
    Return()

    # Function_35_FA5F end

    def Function_36_FB77(): pass

    label("Function_36_FB77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FBE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB95")
    Call(0, 38)
    Jump("loc_FBE2")

    label("loc_FB95")


    #C0570
    ChrTalk(
        0xFE,
        (
            "正直まだ夢でも見ている気分だけど……\x01",
            "ほんとこれからどうなるのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBE2")

    Jump("loc_FEE5")

    label("loc_FBE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_FBF5")
    Jump("loc_FEE5")

    label("loc_FBF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FC03")
    Jump("loc_FEE5")

    label("loc_FC03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FD23")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FD1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCB9")

    #C0571
    ChrTalk(
        0xE,
        (
            "暴走車の取締り、\x01",
            "本当にご苦労だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xE,
        (
            "この子達のことは、\x01",
            "こちらに任せてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xE,
        (
            "また何かあったら\x01",
            "よろしくお願いするわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD19")

    label("loc_FCB9")


    #C0574
    ChrTalk(
        0xE,
        (
            "この子達のことは、\x01",
            "こちらに任せてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xE,
        (
            "また何かあったら\x01",
            "よろしくお願いするわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD19")

    Jump("loc_FD1E")

    label("loc_FD1E")

    Jump("loc_FEE5")

    label("loc_FD23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_FD31")
    Jump("loc_FEE5")

    label("loc_FD31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_FD3F")
    Jump("loc_FEE5")

    label("loc_FD3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FD4D")
    Jump("loc_FEE5")

    label("loc_FD4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_FD5B")
    Jump("loc_FEE5")

    label("loc_FD5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FD69")
    Jump("loc_FEE5")

    label("loc_FD69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FD77")
    Jump("loc_FEE5")

    label("loc_FD77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FD85")
    Jump("loc_FEE5")

    label("loc_FD85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FEE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FEE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE8D")
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0576
    ChrTalk(
        0xE,
        (
            "あなたたちがやったことは\x01",
            "立派な犯罪なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xE,
        "少しは反省したらどうなの！？\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x11,
        "フン、そうカッカするなよ。\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x13,
        (
            "ハンセイハンセイ～。\x01",
            "ほら、反省したぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x12,
        (
            "つーかそろそろ\x01",
            "帰らせてほしいんだけどなあ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_FEE0")

    label("loc_FE8D")


    #C0581
    ChrTalk(
        0xE,
        (
            "あなたたちがやったことは\x01",
            "立派な犯罪なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xE,
        "少しは反省したらどうなの！？\x02",
    )

    CloseMessageWindow()

    label("loc_FEE0")

    Jump("loc_FEE5")

    label("loc_FEE5")

    TalkEnd(0xFE)
    Return()

    # Function_36_FB77 end

    def Function_37_FEE9(): pass

    label("Function_37_FEE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FF90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF07")
    Call(0, 38)
    Jump("loc_FF8B")

    label("loc_FF07")


    #C0583
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "あの大統領演説は\x01",
            "まるで宣戦布告だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "いくら国防軍って言っても\x01",
            "２大国に対抗できるなんて\x01",
            "思えないが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF8B")

    Jump("loc_10198")

    label("loc_FF90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_FF9E")
    Jump("loc_10198")

    label("loc_FF9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10039")

    #C0585
    ChrTalk(
        0xFE,
        (
            "ついに一晩経ったが……\x01",
            "どうにも状況は悪化するばかりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xFE,
        (
            "とにかく、\x01",
            "広域防犯課の方でもこれから\x01",
            "さらに出来ることを尽くす予定だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10198")

    label("loc_10039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_100D9")

    #C0587
    ChrTalk(
        0xF,
        (
            "外国人を厳しく\x01",
            "取り締まれるようになった、\x01",
            "とはまだ言い難いけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xF,
        (
            "今回の件も大事な一歩だ。\x01",
            "俺たち警察もめげずに\x01",
            "頑張っていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10198")

    label("loc_100D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_100E7")
    Jump("loc_10198")

    label("loc_100E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_100F5")
    Jump("loc_10198")

    label("loc_100F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10103")
    Jump("loc_10198")

    label("loc_10103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10111")
    Jump("loc_10198")

    label("loc_10111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1011F")
    Jump("loc_10198")

    label("loc_1011F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1012D")
    Jump("loc_10198")

    label("loc_1012D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1013B")
    Jump("loc_10198")

    label("loc_1013B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_10198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10156")
    Call(0, 33)
    Jump("loc_10198")

    label("loc_10156")

    ClearChrFlags(0xF, 0x10)

    #C0589
    ChrTalk(
        0xF,
        (
            "（こいつらの性格の悪さは\x01",
            "  どこから来てるんだ……！？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10198")

    TalkEnd(0xFE)
    Return()

    # Function_37_FEE9 end

    def Function_38_1019C(): pass

    label("Function_38_1019C")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xE, 0x101, 0)

    #C0590
    ChrTalk(
        0xE,
        (
            "あ、ロイド君。\x01",
            "大変なことになったわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    #C0591
    ChrTalk(
        0xF,
        (
            "支援課の方では\x01",
            "何か聞いていたりしたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#00003Fああいや何も……\x02\x03",

            "#00001F今もまだ詳しい事は課長の\x01",
            "連絡を待っている状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xF,
        (
            "なるほど、\x01",
            "俺たち広域防犯課と同じか。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0xE,
        (
            "会議が終わり次第、具体的な\x01",
            "通達が行われるそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xE,
        (
            "ほんと、何がどうなるか\x01",
            "まったく予想が付かないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xF,
        (
            "とにかく今は成り行きに\x01",
            "従うしかなさそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xF,
        (
            "ロイドたちは何か独自に\x01",
            "動いているみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xF,
        (
            "何ていうか、\x01",
            "国防軍に目を付けられないように\x01",
            "気を付けろよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x101,
        "#00000Fああ、ありがとう。\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x18F, 6)
    Return()

    # Function_38_1019C end

    def Function_39_103E9(): pass

    label("Function_39_103E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_103FA")
    Jump("loc_10A08")

    label("loc_103FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_10408")
    Jump("loc_10A08")

    label("loc_10408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1053C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104C3")

    #C0600
    ChrTalk(
        0xFE,
        (
            "警官隊は半分に分けて、\x01",
            "一方は警備隊の\x01",
            "サポート要員として待機。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "もう一方は\x01",
            "街の巡回強化に動く予定だぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0xFE,
        (
            "苦しい時こそ、\x01",
            "互いに支え合わんとなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_10537")

    label("loc_104C3")


    #C0603
    ChrTalk(
        0xFE,
        (
            "警備隊ばかりに血を\x01",
            "流させるわけにもいかんからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xFE,
        (
            "苦しい時に助けてやれなくて\x01",
            "何が警察だという話だぞー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10537")

    Jump("loc_10A08")

    label("loc_1053C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_105D3")

    #C0605
    ChrTalk(
        0xFE,
        (
            "厄介そうな子達だが、\x01",
            "今日は比較的素直に\x01",
            "受け答えしてくれているなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xFE,
        (
            "ケイト君が一喝したらしいが、\x01",
            "それがよほど効いたんだろー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A08")

    label("loc_105D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_105E4")
    Call(0, 40)
    Jump("loc_10A08")

    label("loc_105E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_105F2")
    Jump("loc_10A08")

    label("loc_105F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10600")
    Jump("loc_10A08")

    label("loc_10600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1060E")
    Jump("loc_10A08")

    label("loc_1060E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1067E")

    #C0607
    ChrTalk(
        0xFE,
        (
            "さて、除幕式も終わって\x01",
            "ようやく一息付けるぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xFE,
        (
            "ふう、やはり\x01",
            "一服はコーヒーに限るなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A08")

    label("loc_1067E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1068C")
    Jump("loc_10A08")

    label("loc_1068C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1071C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106A7")
    Call(0, 26)
    Jump("loc_10717")

    label("loc_106A7")


    #C0609
    ChrTalk(
        0xFE,
        (
            "うーん、あれもいわゆる\x01",
            "自己主張ってヤツなんだろうねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xFE,
        (
            "迷惑をこうむる側は\x01",
            "堪ったものじゃないがなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10717")

    Jump("loc_10A08")

    label("loc_1071C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_10A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10917")

    #C0611
    ChrTalk(
        0xFE,
        (
            "おー、君らはー。\x01",
            "新顔もいるが特務支援課だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xFE,
        (
            "いよいよ改めて\x01",
            "活動再開というわけかー。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x101,
        "#00000Fはい、おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x105,
        (
            "#10302Fふむ、そういうあなたは\x01",
            "広域防犯課の課長殿だね？\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x109,
        "#10101Fあの、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0xFE,
        "あー、わざわざすまんね。\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "ふーむ、しかしなかなか\x01",
            "面白い人材を集めたようだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xFE,
        (
            "まあ、何はともあれ、\x01",
            "君らには期待しとるからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "これからも課の垣根を越えて、\x01",
            "じゃんじゃん活躍してくれよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x102,
        "#00102Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 3)
    Jump("loc_10A08")

    label("loc_10917")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10994")

    #C0621
    ChrTalk(
        0x14,
        (
            "ふーむ、それにしても\x01",
            "厄介な子達が来たものだなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x14,
        (
            "まあ、ケイト君たちに\x01",
            "任せておけば大丈夫だろー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A08")

    label("loc_10994")


    #C0623
    ChrTalk(
        0xFE,
        (
            "ふう、こいつを飲んだら\x01",
            "また会議に戻らんとなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        (
            "やれやれ、この所は会議続きで\x01",
            "定年間際の身体に堪えるぞー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A08")

    TalkEnd(0xFE)
    Return()

    # Function_39_103E9 end

    def Function_40_10A0C(): pass

    label("Function_40_10A0C")

    OP_4B(0x14, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)

    #C0625
    ChrTalk(
        0x14,
        (
            "共和国方面からの列車が来たら、\x01",
            "また振替輸送の対応があるからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x14,
        (
            "君らはこれから、\x01",
            "駅と空港方面の応援に向かってくれー。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x17,
        "はっ、了解であります。\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x18,
        "直ちに現場に向かいます。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    Return()

    # Function_40_10A0C end

    def Function_41_10AE1(): pass

    label("Function_41_10AE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10B7F")

    #C0629
    ChrTalk(
        0xFE,
        (
            "広域防犯課でも、\x01",
            "市内の巡回を再開しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xFE,
        (
            "大きな混乱が治安の悪化に\x01",
            "影響する可能性もあります。\x01",
            "注意して見回らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C49")

    label("loc_10B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_10B8D")
    Jump("loc_10C49")

    label("loc_10B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10C3D")

    #C0631
    ChrTalk(
        0xFE,
        (
            "本部の復旧もようやく\x01",
            "一区切りと思った矢先に\x01",
            "国防軍への組み込み、ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        (
            "自分はこれから\x01",
            "軍人だなんて……流石に素直に\x01",
            "受け入れられそうにありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C49")

    label("loc_10C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10C49")
    Call(0, 40)

    label("loc_10C49")

    TalkEnd(0xFE)
    Return()

    # Function_41_10AE1 end

    def Function_42_10C4D(): pass

    label("Function_42_10C4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10CCE")

    #C0633
    ChrTalk(
        0xFE,
        (
            "ジョーリッジ課長は\x01",
            "国防軍が去った警察学校の\x01",
            "事後処理に向かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xFE,
        "課長の留守は俺たちで守らないとな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10DC2")

    label("loc_10CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_10CDC")
    Jump("loc_10DC2")

    label("loc_10CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10D8C")

    #C0635
    ChrTalk(
        0xFE,
        (
            "本部の復旧もようやく\x01",
            "終わったと思った矢先に\x01",
            "国防軍への組み込み、ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        (
            "自分はこれから\x01",
            "軍人だなんて……流石に素直に\x01",
            "受け入れられそうにありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC2")

    label("loc_10D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_10D9A")
    Jump("loc_10DC2")

    label("loc_10D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10DA8")
    Jump("loc_10DC2")

    label("loc_10DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10DB6")
    Jump("loc_10DC2")

    label("loc_10DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10DC2")
    Call(0, 40)

    label("loc_10DC2")

    TalkEnd(0xFE)
    Return()

    # Function_42_10C4D end

    def Function_43_10DC6(): pass

    label("Function_43_10DC6")

    TalkBegin(0xFE)

    #C0637
    ChrTalk(
        0xFE,
        (
            "既に聞いていると思いますが、\x01",
            "警察は国防軍の一組織として\x01",
            "再編されることが決まりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xFE,
        (
            "現在、今後の体制について\x01",
            "２階の会議室で各方面の責任者に\x01",
            "説明を行っている状況です。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0xFE,
        (
            "皆さんは上からの指示が出るまで、\x01",
            "分室ビルの方でお待ち下さい。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_10DC6 end

    def Function_44_10EC4(): pass

    label("Function_44_10EC4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-950, 1500, 7780, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21800, 0)
    SetChrPos(0x101, -900, 40, 1900, 0)
    SetChrPos(0x102, 300, 40, 1900, 0)
    SetChrPos(0x103, -900, 40, 700, 0)
    SetChrPos(0x104, 300, 40, 700, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x15, 0xFF)

    def lambda_10F4F():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10F4F)
    Sleep(50)

    def lambda_10F6C():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10F6C)
    Sleep(50)

    def lambda_10F89():
        OP_98(0x103, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10F89)
    Sleep(50)

    def lambda_10FA6():
        OP_98(0x104, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10FA6)
    Sleep(50)
    SetCameraDistance(25000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0640
    ChrTalk(
        0x8,
        "あ、皆さん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 500)

    #C0641
    ChrTalk(
        0x15,
        "おや……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-350, 1540, 12250, 0)
    SetCameraDistance(19950, 0)
    SetChrPos(0x15, 1000, 0, 13400, 180)
    SetChrPos(0x101, 0, 40, 11800, 0)
    SetChrPos(0x102, 2000, 40, 11800, 0)
    SetChrPos(0x103, -200, 40, 10300, 0)
    SetChrPos(0x104, 2200, 40, 10300, 0)
    OP_0D()

    #C0642
    ChrTalk(
        0x15,
        (
            "あなた方は\x01",
            "特務支援課の皆さんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x15,
        (
            "既に聞いていると思いますが、\x01",
            "警察は国防軍の一組織として\x01",
            "再編されることが決まりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x15,
        (
            "現在、今後の体制について\x01",
            "２階の会議室で各方面の責任者に\x01",
            "説明を行っている状況です。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x15,
        (
            "皆さんは上からの指示が出るまで、\x01",
            "分室ビルの方でお待ち下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x101,
        "#12P#00001Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x15,
        (
            "なお１階内の移動は自由ですが、\x01",
            "余計な行動は慎んで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x15,
        (
            "不審と判断した場合は、\x01",
            "身柄を拘束させて頂く可能性も\x01",
            "ありますので、ご了承下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        "#12P#00006Fりょ、了解です。\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x102,
        "#12P#00108F（何だか、すごく威圧的ね……）\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x104,
        (
            "#12P#00303F（ああ、だが\x01",
            "  下手に逆らえそうにねえな。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrPos(0x15, 2990, 0, 11810, 270)
    SetScenarioFlags(0x18F, 7)
    ClearMapFlags(0x10000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_44_10EC4 end

    def Function_45_1132D(): pass

    label("Function_45_1132D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch02502.itc", 0x24)
    LoadChrToIndex("chr/ch30102.itc", 0x25)
    LoadChrToIndex("chr/ch30302.itc", 0x26)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis312.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis404.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -62750, 150, 16149, 0)
    SetChrPos(0x102, -65000, 150, 16149, 0)
    SetChrPos(0x104, -65000, 150, 19900, 180)
    SetChrPos(0x109, -67250, 150, 19900, 180)
    SetChrPos(0x105, -67250, 150, 16149, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0xF)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, -57600, 0, 18000, 270)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x2)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x4)
    SetChrPos(0x19, -60500, 150, 16149, 0)
    OP_4B(0x14, 0xFF)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, -62750, 150, 19900, 180)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, -60500, 150, 19900, 180)
    SetMapObjFrame(0xFF, "isu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu_sd", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_78(0x3, 0x1A)
    OP_78(0x4, 0x1B)
    OP_78(0x5, 0x1C)
    OP_78(0x6, 0x1D)
    OP_78(0x7, 0x1E)
    OP_78(0x8, 0x1F)
    OP_78(0x9, 0x20)
    OP_78(0xA, 0x21)
    OP_49()
    SetChrPos(0x1A, -60500, 0, 15900, 0)
    OP_D5(0x1A, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1B, -60500, 0, 20100, 0)
    OP_D5(0x1B, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x1C, -62750, 0, 15900, 0)
    OP_D5(0x1C, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1D, -62750, 0, 20100, 0)
    OP_D5(0x1D, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x1E, -65000, 0, 15900, 0)
    OP_D5(0x1E, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1F, -65000, 0, 20100, 0)
    OP_D5(0x1F, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x20, -67250, 0, 15900, 0)
    OP_D5(0x20, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x21, -67250, 0, 20100, 0)
    OP_D5(0x21, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(-62500, 2200, 18000, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0652
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "そして──\x01",
            "各国首脳がクロスベル入りをし、\x01",
            "オルキスタワーが公開される前日。\x02\x03",

            "警察本部の対策会議の場に\x01",
            "支援課のメンバーが呼ばれていた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_68(-62500, 1200, 18000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0653
    AnonymousTalk(
        0xC,
        (
            "──以上が明日から３日間の\x01",
            "通商会議の警備体制となります。\x02\x03",

            "ベルガード、タングラム門及び\x01",
            "国境付近にはすでに警備隊による\x01",
            "検問体制が敷かれています。\x02\x03",

            "市内に関しては──\x01",
            "ジョーリッジ課長、ドノバン警部。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetChrSubChip(0x14, 0x0)
    Sleep(250)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x19, 0x0)

    #C0654
    ChrTalk(
        0x14,
        (
            "#5Pあー、広域防犯課では総員を\x01",
            "市内巡回に当たらせている状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x14,
        "#5P会議終了まではフル稼働だな。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0656
    ChrTalk(
        0xA,
        (
            "#5P二課は駅・空港・商業区画を\x01",
            "特に重点的に警戒しているぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xA,
        (
            "#5Pこちらも会議終了までは\x01",
            "総員で当たることになりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0xC,
        (
            "#11P#00603Fなお、警備対策本部は\x01",
            "捜査一課で運営している状況です。\x02\x03",

            "#00600F考えられる限りの非常事態に\x01",
            "対応できると自負していますが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x2)
    Sleep(200)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)

    #C0659
    ChrTalk(
        0x19,
        (
            "#12P#01003F……どんなに厳重な警備体制も\x01",
            "決して完璧ではありえない。\x02\x03",

            "#01000Fそこで支援課#6Rウ　チ#の出番ってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xC,
        (
            "#11P#00604Fええ、お伝えしているように\x01",
            "セルゲイ課長には渉外担当として\x01",
            "対策本部に詰めていただきます。\x02\x03",

            "#00602F警備隊方面との連絡も\x01",
            "受け持っていただけると。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x19,
        "#12P#01006Fやれやれ、人使いが荒いこった。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0xA,
        (
            "#5Pハハ、とにかく色んな所に\x01",
            "顔を突っ込んでるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0xA,
        (
            "#5Pそれで死角を突いたやり方で\x01",
            "有利な捜査体制を確立する……\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x14,
        (
            "#5Pうむうむ。\x01",
            "『搦#2Rから#め手のセルゲイ』の\x01",
            "面目躍如ということだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x0)
    Sleep(300)

    #C0665
    ChrTalk(
        0x19,
        "#12P#01005Fよして下さいよ、ンな昔の話。\x02",
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x101,
        "#12P#00002F『搦#2Rから#め手のセルゲイ』ですか……\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x102,
        (
            "#6P#00109Fふふっ……\x01",
            "成程という呼ばれ方ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x1)
    Sleep(300)

    #C0668
    ChrTalk(
        0x19,
        "#11P#01006F昔の話だ、昔の。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x19, 0x2)
    Sleep(200)

    #C0669
    ChrTalk(
        0x19,
        (
            "#12P#01000Fそれで……\x01",
            "コイツらに関してはいいんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0xC,
        (
            "#11P#00603Fええ、構いません。\x02\x03",

            "#00600F彼らにはしばらく遊軍として\x01",
            "動いてもらおうと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0671
    ChrTalk(
        0x109,
        "#10105F遊軍ということは……\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x101,
        (
            "#12P#00001F通常の支援活動を行いながら\x01",
            "何かあればバックアップに\x01",
            "回れるようにするんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0xC,
        (
            "#11P#00606Fああ、その通りだ。\x02\x03",

            "遊撃士協会と同じスタンスだが\x01",
            "彼らに頼り切るわけにもいかん。\x02\x03",

            "#00601Fそれに……\x01",
            "あんな連中#10R㈲　㈲　㈲　㈲　㈲#が入り込んできた以上、\x01",
            "予想外の事態への保険は欲しい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(50)
    SetChrSubChip(0x14, 0x1)

    #C0674
    ChrTalk(
        0x102,
        "#6P#00108Fあんな連中……\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x104,
        "#00303F──《赤い星座》だな。\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xC,
        "#11P#00601Fああ……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0677
    AnonymousTalk(
        0xC,
        (
            "#00603F猟兵団《赤い星座》……\x02\x03",

            "ゼムリア大陸西部において\x01",
            "最強と言われる猟兵団の一つだ。\x02\x03",

            "#00601F現在、多数の所属メンバーが\x01",
            "クロスベル入りしていることが\x01",
            "確認されている。\x02\x03",

            "ちなみに１年ほど前、\x01",
            "あの『黒月#4Rヘイユエ#』と共和国方面で\x01",
            "大規模な抗争を起こしたらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0678
    ChrTalk(
        0x14,
        "#5Pふーむ、物騒な連中だなァ。\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xA,
        (
            "#5Pってことは、この街で黒月と\x01",
            "抗争の続きをするつもりなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0xC,
        (
            "#11P#00603Fいえ、基本的に猟兵団は\x01",
            "ミラによって動く連中です。\x02\x03",

            "以前争っていたとはいえ、\x01",
            "再び争う理由にはなりません。\x02\x03",

            "#00600Fそうだな、オルランド？\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x104,
        (
            "#00306F──まあな。\x02\x03",

            "#00303F縄張りを重視するマフィアと違って\x01",
            "猟兵団にはミラと戦場が全てだ。\x02\x03",

            "昨日の敵は今日の味方……\x01",
            "その逆も日常茶飯事にありえる。\x02\x03",

            "#00300Fその意味で、以前の抗争を\x01",
            "引っ張るというのはねぇだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x105,
        (
            "#6P#N#10304Fフフ、そうなると\x01",
            "一つの謎が浮上してくるわけだ？\x02\x03",

            "#10302Fどうして《赤い星座》が\x01",
            "クロスベル入りしたのかっていう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0683
    ChrTalk(
        0xC,
        (
            "#11P#00606F一課でも探ってはいるが\x01",
            "その目的は未だ判明していない。\x02\x03",

            "#00601Fただ、帝国政府の後押しを\x01",
            "受けているのは確実なようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x102,
        (
            "#6P#00108F通商会議に関係することで\x01",
            "何かを行おうとしている……\x02\x03",

            "#00101Fもしくは共和国系の『黒月』の\x01",
            "台頭を抑えるのが狙いでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x19,
        (
            "#12P#01006Fま、どちらもあり得るだろう。\x02\x03",

            "#01000Fいずれにせよ、通商会議において\x01",
            "無視できる要素じゃないってのは\x01",
            "間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0xC,
        (
            "#11P#00603Fええ、無論です。\x02\x03",

            "#00600F──ちなみに《赤い星座》だが、\x01",
            "クロスベル市の周辺にも\x01",
            "何度か足を延ばしているらしい。\x02\x03",

            "もし、各地を回ることがあれば\x01",
            "そのあたりの動向も探って欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x101,
        (
            "#12P#00003F──了解しました。\x02\x03",

            "#00001Fそれでは、支援要請に対応しつつ、\x01",
            "《赤い星座》の情報収集を行います。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(50)
    SetChrSubChip(0x14, 0x0)
    Sleep(100)

    #C0688
    ChrTalk(
        0x102,
        (
            "#6P#00100F何かありましたら\x01",
            "各方面に応援に行きますので\x01",
            "いつでも連絡してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0xA,
        "#5Pおう、頼りにしてるぜ。\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x14,
        "#5P遠慮なく頼らせてもらうぞ～。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_E5(0xA)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 3)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_1132D end

    def Function_46_127E0(): pass

    label("Function_46_127E0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-690, 1400, 7180, 0)
    MoveCamera(34, 9, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21430, 0)
    SetChrPos(0x101, -900, 40, 1900, 0)
    SetChrPos(0x102, 300, 40, 1900, 0)
    SetChrPos(0x109, -900, 40, 700, 0)
    SetChrPos(0x105, 300, 40, 700, 0)

    def lambda_12863():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12863)
    Sleep(50)

    def lambda_12880():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12880)
    Sleep(50)

    def lambda_1289D():
        OP_98(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1289D)
    Sleep(50)

    def lambda_128BA():
        OP_98(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_128BA)
    Sleep(50)
    SetCameraDistance(20430, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0691
    ChrTalk(
        0x8,
        "まあ、皆さん。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(500)

    #C0692
    ChrTalk(
        0x9,
        "#5P#01902Fあ、皆さん、お姉ちゃん！\x02",
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x109,
        (
            "#12P#10106Fもう、職場でお姉ちゃんは\x01",
            "駄目だって言ったでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-900, 1540, 13080, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, -900, 40, 12200, 0)
    SetChrPos(0x102, 300, 40, 11800, 0)
    SetChrPos(0x109, -1200, 40, 10800, 0)
    SetChrPos(0x105, 500, 40, 10600, 0)

    def lambda_12A24():
        OP_98(0x101, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A24)
    Sleep(50)

    def lambda_12A41():
        OP_98(0x102, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12A41)
    Sleep(50)

    def lambda_12A5E():
        OP_98(0x109, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12A5E)
    Sleep(50)

    def lambda_12A7B():
        OP_98(0x105, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12A7B)
    Sleep(50)
    TurnDirection(0x9, 0x101, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    #C0694
    ChrTalk(
        0x101,
        (
            "#12P#00002Fはは、レベッカさん。\x01",
            "お疲れさまです。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x102,
        "#12P#00102Fご無沙汰していました。\x02",
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x8,
        (
            "うふふ。\x01",
            "特務支援課、再始動ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x8,
        (
            "さっそく支援要請を\x01",
            "始めていらっしゃるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x101,
        (
            "#12P#00000Fええ、新メンバーもいますし、\x01",
            "市内を回りながら。\x02\x03",

            "一課の要請を受けたんですけど\x01",
            "エマさんはどちらに？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x8,
        "そこの会議室でお待ちですよ。\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x8,
        (
            "一課からの協力要請なんて\x01",
            "皆さんも出世されましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        "ふふ、何だか感慨深いです。\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        "#12P#00012Fいや、そんな……\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、無理難題を\x01",
            "押し付けられなければいいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x102,
        "#12P#00106Fもう、ワジ君……\x02",
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#12P#00001Fと、とにかくエマさんから\x01",
            "話を聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x9,
        "#11P#01909F頑張ってくださいね～。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x130, 0)
    OP_29(0x66, 0x1, 0x0)
    SetChrPos(0x0, -350, 0, 12250, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_46_127E0 end

    def Function_47_12D62(): pass

    label("Function_47_12D62")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-57410, 1500, 17030, 0)
    MoveCamera(47, 35, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23750, 0)
    SetChrPos(0x101, -56800, 0, 17250, 0)
    SetChrPos(0x102, -57800, 0, 17000, 0)
    SetChrPos(0x109, -56800, 0, 16000, 0)
    SetChrPos(0x105, -57800, 0, 15750, 0)
    OP_4B(0xD, 0xFF)
    OP_93(0xD, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0707
    ChrTalk(
        0xD,
        (
            "来ましたか……\x01",
            "バニングス捜査官。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        (
            "#12P#00012Fど、どうもエマさん。\x01",
            "その節はお世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0xD,
        (
            "一課での研修の事であれば\x01",
            "世話したつもりはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0xD,
        (
            "あくまで、ダドリーさんの\x01",
            "指示に従っただけのことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0xD,
        (
            "スジは悪くありませんが……\x01",
            "一課への誘いを蹴って支援課に\x01",
            "戻ったのは理解に苦しみますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x101,
        "#12P#00006Fす、すみません。\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x102,
        "#12P#00105F（色々あったみたいね……）\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x109,
        (
            "#12P#10100F（確かにロイドさんだったら\x01",
            "  他の部署も欲しがりそうですよね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0xD,
        (
            "まあいいでしょう。\x01",
            "早速、本題に入ります。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0xD,
        (
            "ここに来たという事は\x01",
            "手伝ってもらえると\x01",
            "考えてもいいのですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x101,
        (
            "#12P#00003Fええ、もちろんです。\x02\x03",

            "#00001F……何でも、\x01",
            "あのレクター・アランドールが\x01",
            "クロスベル入りしているとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0xD,
        "一課ではそう掴んでいます。\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0xD,
        (
            "……ですが、残念ながら\x01",
            "いまだ確定できていません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0720
    ChrTalk(
        0x101,
        "#12P#00005Fそれはどういう……？\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x102,
        (
            "#12P#00105F所在が確認できないという\x01",
            "ことでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0xD,
        (
            "そもそもクロスベル入りしたと\x01",
            "いうのが不確かな情報なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0xD,
        (
            "それらしき目撃情報はある……\x01",
            "だが、足取りを追おうとすると\x01",
            "陽炎のようにぼやけてしまう……\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xD,
        (
            "恐らく、こちらの動きを察知して\x01",
            "捕捉を逃れているのだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x101,
        "#12P#00013F……なるほど……\x02",
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x109,
        "#12P#10106Fと、とんでもない人ですね。\x02",
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x105,
        (
            "#12P#10302Fま、あのお兄さんなら\x01",
            "そのくらいはやりそうかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xD,
        (
            "そこで貴方たちに\x01",
            "レクター・アランドールの\x01",
            "滞在事実を確認して欲しいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0xD,
        (
            "本当にクロスベル入りしているのか、\x01",
            "それとも何らかの偽装情報なのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0xD,
        (
            "可能ならば、帝国軍将校、\x01",
            "ないし帝国政府の書記官としての\x01",
            "身元確認も頼みたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x101,
        "#12P#00000F……分かりました。\x02",
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x102,
        "#12P#00100Fですが、どうして私たちに？\x02",
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0xD,
        (
            "以前、あなた方は\x01",
            "“彼”と何度か接触しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0xD,
        "それに賭けてみる事にしました。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0735
    ChrTalk(
        0x101,
        "#12P#00012Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、エリートの割には\x01",
            "意外と柔軟な対応なんだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0xD,
        "ぐっ……仕方ないでしょう。\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xD,
        (
            "人手を割けば捕捉は可能ですが\x01",
            "下手をすれば外交問題になりますし、\x01",
            "それ以外の案件も抱えています。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xD,
        (
            "……ダドリーさんがいらしたら\x01",
            "貴方たちには頼まなかったのに。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0740
    ChrTalk(
        0x101,
        (
            "#12P#00005Fそういえば……\x01",
            "ダドリーさんはどちらに？\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0xD,
        (
            "昨日の夕方、\x01",
            "通商会議の警備の打ち合わせで\x01",
            "リベール方面に向かいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0xD,
        "戻るのは明日になると思います。\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x101,
        "#12P#00001Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x102,
        "#12P#00100Fお忙しそうですね……\x02",
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0xD,
        (
            "ですから、彼が帰って来る前に\x01",
            "何とか片付けておきたいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0xD,
        (
            "どれだけ出張で疲れていても\x01",
            "引き受けてしまう人ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x102,
        "#12P#00103Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x109,
        (
            "#12P#10106F確かにダドリーさんなら\x01",
            "そのくらいはしそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#12P#00003F分かりました。\x01",
            "引き受けさせてもらいます。\x02\x03",

            "#00000Fとりあえず……\x01",
            "どのあたりでレクター大尉が\x01",
            "目撃されたか分かりますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0xD,
        (
            "そうですね……\x01",
            "真偽は定かではありませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0xD,
        (
            "“裏通り”のあたりで\x01",
            "見かけたという情報があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x102,
        (
            "#12P#00105F裏通り……\x01",
            "旧ルバーチェの近くですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x105,
        "#12P#10302Fフフ、それっぽいじゃない。\x02",
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x101,
        (
            "#12P#00000F分かりました。\x01",
            "早速、調査に入ります。\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0xD,
        "よろしく頼みます。\x02",
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0xD,
        (
            "私は一課で待機しているので\x01",
            "報告の時は受付で呼んでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xD,
        "それでは失礼します。\x02",
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_13AC2():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13AC2)

    def lambda_13ACF():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13ACF)

    def lambda_13ADC():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13ADC)

    def lambda_13AE9():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13AE9)
    OP_68(-57500, 1500, 16430, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_13B3B():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13B3B)

    def lambda_13B48():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13B48)

    def lambda_13B55():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13B55)

    def lambda_13B62():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13B62)
    OP_0D()
    OP_6F(0x1)

    #C0758
    ChrTalk(
        0x101,
        "#11P#00006Fふう……\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x102,
        (
            "#6P#00100F随分、一課の研修で\x01",
            "お世話になったみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x101,
        (
            "#11P#00000Fああ、態度は厳しいけど\x01",
            "懇切丁寧に教えてくれたよ。\x02\x03",

            "#00004F何ていうか……\x01",
            "生真面目な人なんだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x109,
        "#10102Fふふっ、そんな感じですよね。\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x105,
        (
            "#12P#10304Fま、そういうお姉さんほど\x01",
            "癒しを求めているものだけどね。\x02\x03",

            "#10302Fフフ、今晩あたりに\x01",
            "飲みでも誘ってみようかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x101,
        (
            "#11P#00006Fあのな……\x02\x03",

            "#00000Fとにかく当たりを付けて\x01",
            "レクターさんを捜してみよう。\x02\x03",

            "まずは裏通りからだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x102,
        "#6P#00100Fええ、行きましょう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0765
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【帝国書記官の身元確認】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x130, 1)
    OP_29(0x66, 0x1, 0x1)
    SetChrPos(0x0, -56800, 0, 17500, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_47_12D62 end

    def Function_48_13DFA(): pass

    label("Function_48_13DFA")

    Sleep(2500)
    Sound(103, 0, 100, 0)
    Sleep(400)
    Sound(104, 0, 100, 0)
    Return()

    # Function_48_13DFA end

    def Function_49_13E0D(): pass

    label("Function_49_13E0D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x4)
    SetChrPos(0xD, -57300, 0, 18750, 180)
    OP_4B(0xD, 0xFF)
    OP_68(-57300, 1500, 17520, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -56800, 0, 17250, 0)
    SetChrPos(0x102, -57800, 0, 17000, 0)
    SetChrPos(0x109, -56800, 0, 16000, 0)
    SetChrPos(0x105, -57800, 0, 15750, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0766
    ChrTalk(
        0xD,
        (
            "──ご苦労でした。\x01",
            "色々と掴めたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x101,
        (
            "#12P#00001Fええ、まさかあっさりと\x01",
            "情報局の人間であることまで\x01",
            "認めるとは思いませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0xD,
        (
            "……こちらに知られた所で、\x01",
            "諜報活動を制限されないという\x01",
            "自信があるのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0xD,
        (
            "しかしこれで、滞在期間も\x01",
            "大まかに把握できましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0xD,
        (
            "予想以上の成果を\x01",
            "上げてくれたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x101,
        (
            "#12P#00002Fはは……\x01",
            "そう言っていただけると。\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、誰かさんが身体を張った\x01",
            "甲斐があるってもんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x102,
        "#6P#00113Fは、張ってません！\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0xD,
        (
            "しかしその、同行していた\x01",
            "少女というのも気になりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xD,
        (
            "レクター大尉の諜報関係の\x01",
            "部下といった感じでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x101,
        (
            "#12P#00003F……いえ、違うと思います。\x02\x03",

            "#00008F諜報関係者にしては若すぎるし、\x01",
            "あまりにも無邪気すぎる。\x02\x03",

            "#00001Fもっとも、普通の民間人にも\x01",
            "見えませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x109,
        (
            "#12P#10101F……そうですね。\x01",
            "身のこなしも素早かったですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0xD,
        (
            "──分かりました。\x01",
            "その娘については一課の方でも\x01",
            "動向を把握しておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0xD,
        (
            "では、私はこれで。\x01",
            "今回はお世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x101,
        (
            "#12P#00002Fいえ、また何かあったら\x01",
            "遠慮なく連絡してください。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_142ED():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_142ED)

    def lambda_142FA():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_142FA)

    def lambda_14307():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14307)

    def lambda_14314():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14314)
    OP_68(-57300, 1500, 16880, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_14366():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14366)

    def lambda_14373():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14373)

    def lambda_14380():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14380)

    def lambda_1438D():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1438D)
    OP_0D()
    OP_6F(0x1)

    #C0781
    ChrTalk(
        0x101,
        (
            "#00006Fふう……\x01",
            "何とか期待に応えられたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x102,
        (
            "#6P#00106F……はあ、そうね……\x02\x03",

            "#00108Fそれにしてもあの子……\x01",
            "本当に何者なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x109,
        (
            "#10101Fそうですね……\x01",
            "ノリで誤魔化されましたけど\x01",
            "普通の旅行者とは思えませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x105,
        (
            "#12P#10302F大国の情報将校に同行する\x01",
            "無邪気で奔放な少女か……\x02\x03",

            "#10304Fフフ、なかなか興味深いね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0785
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【帝国書記官の身元確認】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x66, 0x1, 0x5)
    OP_29(0x66, 0x1, 0x6)
    OP_29(0x66, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x3)
    SetChrPos(0x0, -56800, 0, 17500, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_49_13E0D end

    def Function_50_14568(): pass

    label("Function_50_14568")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(-4980, 1900, 10000, 0)
    MoveCamera(27, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20960, 0)
    SetChrPos(0x101, -5180, 0, 11860, 90)
    SetChrPos(0x102, -5660, 0, 10860, 90)
    SetChrPos(0x109, -6640, 0, 11950, 90)
    SetChrPos(0x105, -7250, 0, 10910, 90)
    OP_68(-1640, 1900, 10930, 3000)

    def lambda_145FB():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_145FB)
    Sleep(50)

    def lambda_14618():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14618)
    Sleep(50)

    def lambda_14635():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14635)
    Sleep(50)

    def lambda_14652():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14652)
    Sleep(300)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    #C0786
    ChrTalk(
        0x8,
        (
            "あ……支援課の皆さん、\x01",
            "お仕事は終わったみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-710, 1500, 13250, 1500)
    MoveCamera(43, 24, 0, 1500)

    def lambda_14721():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14721)
    Sleep(50)

    def lambda_1473E():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1473E)
    Sleep(50)

    def lambda_1475B():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1475B)
    Sleep(50)

    def lambda_14778():
        OP_97(0xFE, 0x3E8, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14778)
    WaitChrThread(0x101, 1)

    def lambda_14796():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14796)
    WaitChrThread(0x109, 1)

    def lambda_147A7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_147A7)
    WaitChrThread(0x102, 1)

    def lambda_147B8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_147B8)
    WaitChrThread(0x105, 1)

    def lambda_147C9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_147C9)
    Sleep(300)
    OP_6F(0x79)

    #C0787
    ChrTalk(
        0x101,
        (
            "#12P#00002Fええ、ついさっき\x01",
            "報告を終えました。\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、ひとまずは\x01",
            "一件落着って所だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x8,
        "ふふ、お疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x8,
        (
            "今後も再始動した支援課には\x01",
            "沢山の依頼が舞い込むかと思いますが、\x01",
            "どうか頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x102,
        (
            "#12P#00102Fありがとうございます、\x01",
            "レベッカさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x109,
        (
            "#12P#10100F新メンバーとしては\x01",
            "まだまだ未熟ですけど……\x01",
            "なんとか頑張りたいです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0793
    ChrTalk(
        0x8,
        (
            "そういえば、みなさん。\x01",
            "新しい戦闘手帳は活用していますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x8,
        (
            "ロイドさんが一課の研修の際に、\x01",
            "受け取っているはずですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x101,
        (
            "#12P#00000Fあ、そういえば……\x01",
            "ええ、活用させていただいてます。\x02\x03",

            "#00004F手帳の情報が増えたときは、\x01",
            "レベッカさんに報告すれば\x01",
            "いいんでしたよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x8,
        "ええ、そうして頂けると助かります。\x02",
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x8,
        (
            "特に最近は、新型魔獣の報告も\x01",
            "増加の傾向にありますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x8,
        (
            "それらの実態把握と安全対策のため\x01",
            "少しでも多くの情報が欲しいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x8,
        (
            "これまでと同様、段階的に\x01",
            "多少の手当ても支給されますので、\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x101,
        "#12P#00000Fええ、了解しました。\x02",
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x109,
        (
            "#12P#10100Fある程度、定期的に\x01",
            "立ち寄った方がよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x8,
        "ふふ、お待ちしております。\x02",
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x8,
        (
            "それと……もうひとつ\x01",
            "みなさんにお知らせしなければ\x01",
            "ならないことがあるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x8,
        (
            "皆さんが教団事件の時に発見した\x01",
            "端末のデータの事なのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x8,
        (
            "先日、ようやく解析できる\x01",
            "可能性が見えてきたそうでして。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0806
    ChrTalk(
        0x102,
        "#12P#00105Fほ、本当ですか！？\x02",
    )

    CloseMessageWindow()

    def lambda_14D30():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14D30)
    Sleep(50)

    def lambda_14D40():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14D40)
    Sleep(300)

    #C0807
    ChrTalk(
        0x105,
        "#6P#10305Fふむ、何の話だい？\x02",
    )

    CloseMessageWindow()

    def lambda_14D72():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14D72)
    Sleep(50)

    def lambda_14D82():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14D82)
    Sleep(300)

    #C0808
    ChrTalk(
        0x101,
        (
            "#11P#00003F……あの教団事件の時に、\x01",
            "《太陽の砦》にあった端末から\x01",
            "あるデータが手に入ったんだ。\x02\x03",

            "《Ｄ∴Ｇ教団》について、\x01",
            "ヨアヒム・ギュンター自身が\x01",
            "記したとみられるデータがね。\x02\x03",

            "#00008F文章の一部が意図的に消されて\x01",
            "解読が不可能だったから、\x01",
            "鑑識に回してたんだけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0809
    ChrTalk(
        0x101,
        (
            "#12P#00001Fもしかして、消された文章を\x01",
            "復旧できたんですか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14EEA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14EEA)
    Sleep(50)

    def lambda_14EFA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14EFA)
    Sleep(50)

    def lambda_14F0A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14F0A)
    Sleep(300)

    #C0810
    ChrTalk(
        0x8,
        (
            "いえ、鑑識課によりますと\x01",
            "まだ見込みが立ったという\x01",
            "段階みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x8,
        (
            "記憶結晶#8Rメモリークオーツ#の内部に\x01",
            "破損したデータの破片が\x01",
            "存在していたとのことですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x8,
        (
            "完全に解析するには\x01",
            "かなりの時間を要してしまうとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x109,
        (
            "#12P#10106Fそうですか……\x02\x03",

            "#10108Fあの事件の不明瞭だった部分が\x01",
            "ようやく分かるようになるかと\x01",
            "思ったんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x101,
        (
            "#12P#00003F……今の所は地道に待つしか\x01",
            "ないのかもしれないな。\x02\x03",

            "#00000Fレベッカさん、教えていただいて\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x8,
        "ふふ、どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x8,
        (
            "一応、言っていただければ\x01",
            "いつでも端末のデータを\x01",
            "確認していただけます。\x02",
        )
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x8,
        (
            "解析に進展がありましたら\x01",
            "またお知らせいたしますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x102,
        "#12P#00100Fええ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    SetScenarioFlags(0x130, 7)
    ModifyEventFlags(0, 1, 0x80)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_50_14568 end

    def Function_51_151EE(): pass

    label("Function_51_151EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-124920, 1500, 15840, 0)
    MoveCamera(53, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    LoadChrToIndex("chr/ch44102.itc", 0x1E)
    LoadChrToIndex("chr/ch47500.itc", 0x1F)
    LoadChrToIndex("chr/ch23600.itc", 0x20)
    LoadChrToIndex("chr/ch30100.itc", 0x21)
    LoadChrToIndex("chr/ch30002.itc", 0x22)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xE, -34500, 0, 18310, 180)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -122270, 100, 16550, 270)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -121780, 0, 18250, 225)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -121570, 0, 14770, 315)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -125880, 0, 12690, 0)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xF, -125000, 100, 16550, 90)
    SetChrPos(0x101, -35350, 0, 16000, 0)
    SetChrPos(0x102, -34150, 0, 16000, 0)
    SetChrPos(0x109, -35350, 0, 14800, 0)
    SetChrPos(0x105, -34150, 0, 14800, 0)
    OP_4B(0x14, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0819
    ChrTalk(
        0xF,
        (
            "それじゃ、改めて調書をとるから\x01",
            "質問に答えてくれるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0xF,
        "えーと、君達の名前は？\x02",
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x13,
        "ナナシノゴンベ。（ホジホジ）\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x12,
        "ジョン・スミス。（ボリボリ）\x02",
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x11,
        (
            "フン、お前みたいなヤツに\x01",
            "答えてやる義理があるのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0824
    ChrTalk(
        0xF,
        (
            "お、お前らなあっ！！\x01",
            "ふざけるのもいい加減に……！\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x14,
        (
            "まーまー、フランツ君。\x01",
            "落ち着いてやりたまえー。\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x12,
        "プッ、注意されてやんの。\x02",
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0x13,
        "ダッセー。\x02",
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x11,
        "やれやれ、これだから庶民は……\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-35670, 1800, 15820, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20190, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0829
    ChrTalk(
        0x109,
        (
            "#10101F……彼らに与えられるのは、\x01",
            "罰金刑のみなんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0xE,
        "……残念だけどね。\x02",
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0xE,
        (
            "確かに自治州法では、\x01",
            "交通に関する決まりごとも\x01",
            "最低限は整備されているけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0xE,
        (
            "彼らが共和国人である以上、\x01",
            "どうしても厳しく取り締まれないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0xE,
        (
            "今日は厳重注意をするけど、\x01",
            "すぐに釈放されてしまうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x101,
        "#00003F……やっぱりですか。\x02",
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0x105,
        (
            "#10300Fふむ、なんだかある程度\x01",
            "予想はしていたみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1570A():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1570A)
    Sleep(50)

    def lambda_1571A():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1571A)
    Sleep(100)

    #C0836
    ChrTalk(
        0x102,
        (
            "#00108F……以前にも、\x01",
            "似たような事があったのよね。\x02\x03",

            "偽ブランド商の事件の時は、\x01",
            "厳重注意と１ヶ月間の\x01",
            "自治州退去命令だけだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x109,
        (
            "#10106Fそういえば……\x01",
            "そんな事もありましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x102,
        (
            "#00103F……おじさまが新市長になって、\x01",
            "自治州法も見直す動きが\x01",
            "高まってきているけど……\x02\x03",

            "それでもまだ手の届かない部分が\x01",
            "多いのが現状なのよね。\x02\x03",

            "#00101F外国人に対して強く出れない事も、\x01",
            "長年クロスベルが抱えてきた\x01",
            "“歪み”の一つと言えるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x105,
        (
            "#10306Fフウ、やれやれ……\x02\x03",

            "それじゃ、今回の件は\x01",
            "骨折り損だったってコトに\x01",
            "なっちゃうのかな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(100)

    #C0840
    ChrTalk(
        0x101,
        (
            "#00004F……いや、そんなことはないさ。\x02\x03",

            "#00000F今まで何度か\x01",
            "同じような事はあったけど、\x01",
            "どれも決して無駄じゃなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0xE,
        (
            "今回のだってもちろん、\x01",
            "無駄なんかじゃないと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_159F9():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_159F9)
    Sleep(50)

    def lambda_15A09():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15A09)
    Sleep(100)

    #C0842
    ChrTalk(
        0xE,
        (
            "少なくとも、今日はこれ以上\x01",
            "暴走車が走ることはないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0843
    ChrTalk(
        0x101,
        (
            "#00003F……これからも、何度でも\x01",
            "こういう壁に直面すると思う。\x02\x03",

            "#00000Fだからこそ、\x01",
            "諦めずに立ち向かうって\x01",
            "ことが大事なんだと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0844
    ChrTalk(
        0x109,
        (
            "#10101Fそうですね……\x01",
            "あたしもがんばらないと！\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x105,
        (
            "#10304Fそれじゃ、せいぜい僕は\x01",
            "クールに立ち回らせて\x01",
            "もらうとしようかな。\x02\x03",

            "#10302F君たちが熱くなりすぎて\x01",
            "暴走しちゃわないようにね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0846
    ChrTalk(
        0x102,
        (
            "#00106Fワジ君ったら……\x01",
            "折角まとまりかけてるのに\x01",
            "水を差さないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x101,
        (
            "#00012F……ま、まあいいさ。\x02\x03",

            "#00000Fそれじゃ、ケイト先輩……\x01",
            "あとはお任せしていいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0xE,
        "ええ、もちろん。\x02",
    )

    CloseMessageWindow()

    #C0849
    ChrTalk(
        0xE,
        (
            "今日は本当に助かったわ。\x01",
            "また何かあったら\x01",
            "よろしくお願いするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x101,
        "#00002Fはい、お待ちしてます。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0851
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【暴走車の取り締まり】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x69, 0x1, 0x0)
    OP_29(0x69, 0x1, 0x1)
    OP_29(0x69, 0x4, 0x10)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0x14, 0x40)
    OP_4C(0x14, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -34750, 0, 15400, 180)
    EventEnd(0x5)
    Return()

    # Function_51_151EE end

    def Function_52_15DCB(): pass

    label("Function_52_15DCB")

    EventBegin(0x0)
    Fade(500)
    OP_68(-13030, 1500, 12910, 0)
    MoveCamera(27, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -12540, 0, 13210, 90)
    SetChrPos(0x102, -12540, 0, 14610, 135)
    SetChrPos(0x103, -13740, 0, 13610, 90)
    SetChrPos(0x104, -14000, 0, 14810, 135)
    SetChrPos(0x109, -15000, 0, 13400, 90)
    SetChrPos(0x105, -14100, 0, 12000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1681C")
    OP_0D()

    #C0852
    ChrTalk(
        0x10,
        (
            "ああ、マーガレット……\x01",
            "どうしてこんなことに……\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x10,
        (
            "あんな男に引っかかるなんて\x01",
            "オマエらしくもない……！\x02",
        )
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x10,
        (
            "と、とにかく、\x01",
            "取り返しがつかなくなる前に\x01",
            "なんとかしなければ……\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x101,
        (
            "#00005F（ピエール局長……\x01",
            "  珍しいな、こんなところで。）\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x102,
        "#00105F（何か悩んでいるみたいだけど……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x10, 0x10E, 0x3E8)
    Sleep(50)

    #C0857
    ChrTalk(
        0x10,
        (
            "き、君たちは……\x01",
            "いつからそこにいたのだねっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x10,
        (
            "ま、まさか今の独り言を\x01",
            "聞いていたんじゃないだろうね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0859
    ChrTalk(
        0x104,
        (
            "#00302Fい、いや……\x01",
            "詳しくは聞いてないッスけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0860
    ChrTalk(
        0x103,
        (
            "#00203Fマーガレットがどうとか、\x01",
            "あんな男に引っかかるとか、\x01",
            "部分的には聞こえてきましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x10,
        "ギクッ……\x02",
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、副局長御用達の\x01",
            "ホステスさんの名前かい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0863
    ChrTalk(
        0x10,
        (
            "ひ、人聞きの悪い事は\x01",
            "言わないでもらおうかっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0x10,
        (
            "マーガレットは……\x01",
            "私のワイフの名前だ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0865
    ChrTalk(
        0x109,
        "#10105Fワ、ワイフって……\x02",
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x101,
        "#00005F奥さんの事ですか？\x02",
    )

    CloseMessageWindow()

    #C0867
    ChrTalk(
        0x10,
        "そうだ！\x02",
    )

    CloseMessageWindow()

    #C0868
    ChrTalk(
        0x10,
        (
            "……まあ、前に指輪を失くしたり、\x01",
            "次期局長の座を逃してからは\x01",
            "更に邪険に扱われるようになったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0869
    ChrTalk(
        0x10,
        (
            "……って、なんで私がこんな事まで\x01",
            "赤裸々に話さなきゃならないんだね！？\x02",
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
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16478")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0870
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆前編の「指輪探しクエスト」を？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",          # 0
            "【クリアしている】\x01",      # 1
            "【それ以外】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1645F"),
        (1, "loc_16464"),
        (2, "loc_1646E"),
        (SWITCH_DEFAULT, "loc_16478"),
    )


    label("loc_1645F")

    Jump("loc_16478")

    label("loc_16464")

    OP_29(0x15, 0x4, 0x10)
    Jump("loc_16478")

    label("loc_1646E")

    OP_29(0x15, 0x3, 0x10)
    Jump("loc_16478")

    label("loc_16478")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16509")

    #C0871
    ChrTalk(
        0x101,
        (
            "#00003F（そういえば副局長……\x01",
            "  恐妻家で有名だったな。）\x02\x03",

            "#00008F（ってことは、今副局長が\x01",
            "  悩んでいるのもそれ関係か……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1657B")

    label("loc_16509")


    #C0872
    ChrTalk(
        0x101,
        (
            "#00003F（副局長……\x01",
            "  恐妻家みたいだな。）\x02\x03",

            "#00008F（ってことは、今副局長が\x01",
            "  悩んでいるのもそれ関係か……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1657B")


    #C0873
    ChrTalk(
        0x10,
        (
            "……ええい、仕方ない。\x01",
            "この際、背に腹は変えられん。\x02",
        )
    )

    CloseMessageWindow()

    #C0874
    ChrTalk(
        0x10,
        (
            "特務支援課の諸君！\x01",
            "君たちに極秘任務を与える！！\x02",
        )
    )

    CloseMessageWindow()

    #C0875
    ChrTalk(
        0x102,
        (
            "#00105F極秘任務……ですか？\x01",
            "それってどういう……\x02",
        )
    )

    CloseMessageWindow()

    #C0876
    ChrTalk(
        0x10,
        (
            "う、うむ、ありていに言えば……\x01",
            "私のワイフの身辺調査を頼みたいのだ。\x02",
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
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0877
    ChrTalk(
        0x104,
        "#00305Fし、身辺調査って……\x02",
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x103,
        (
            "#00206F部署の私的な運用は\x01",
            "警察の職務規定に反しますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x10,
        (
            "この際、細かい事はどうでもいい！\x01",
            "私も切羽詰まっているのだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0880
    ChrTalk(
        0x10,
        (
            "何なら、君たちへの\x01",
            "依頼という形で処理しても構わん！\x01",
            "それならどうだね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x101,
        (
            "#00006Fう、うーん……\x01",
            "（どうしようか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_168B9")

    label("loc_1681C")

    OP_93(0x10, 0x10E, 0x0)
    OP_0D()

    #C0882
    ChrTalk(
        0x10,
        (
            "特務支援課の諸君！\x01",
            "君たちに極秘の任務を与えたい！！\x02",
        )
    )

    CloseMessageWindow()

    #C0883
    ChrTalk(
        0x10,
        (
            "何なら、君たちへの\x01",
            "依頼という形で処理しても構わん！\x01",
            "どうか引き受けてもらえないかね！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_168B9")

    Call(0, 53)
    OP_4C(0x10, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -12540, 0, 14410, 0)
    EventEnd(0x5)
    Return()

    # Function_52_15DCB end

    def Function_53_168D8(): pass

    label("Function_53_168D8")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16936")
    Call(0, 54)
    Jump("loc_16A25")

    label("loc_16936")


    #C0884
    ChrTalk(
        0x101,
        (
            "#00006Fすみません……\x01",
            "俺たちも仕事がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0885
    ChrTalk(
        0x10,
        "そ、そうか……仕方ない。\x02",
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x10,
        (
            "ならば、即刻片付けて\x01",
            "ここに戻ってくるように！\x01",
            "……いいね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0887
    ChrTalk(
        0x101,
        "#00005Fぜ、善処します。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x174, 7)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x10, 0x5A, 0x0)
    SetChrPos(0x0, -12540, 0, 1096611267, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_16A25")

    Return()

    # Function_53_168D8 end

    def Function_54_16A26(): pass

    label("Function_54_16A26")


    #C0888
    ChrTalk(
        0x101,
        (
            "#00001Fわ、分かりました。\x01",
            "どうやらお困りのようですし……\x01",
            "話くらいは聞かせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0x10,
        "おおっ……本当かね！？\x02",
    )

    CloseMessageWindow()

    #C0890
    ChrTalk(
        0x10,
        (
            "よし、そうときまれば\x01",
            "ここで話をするのもなんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0891
    ChrTalk(
        0x10,
        (
            "副局長室についてきたまえ。\x01",
            "そこで詳しく話そう！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_54_16A26 end

    def Function_55_16B23(): pass

    label("Function_55_16B23")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x10, 0xFF)
    OP_68(-12660, 1500, 14950, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24690, 0)
    SetChrPos(0x101, -11960, 0, 15570, 225)
    SetChrPos(0x102, -11390, 0, 13820, 315)
    SetChrPos(0x103, -13360, 0, 16370, 135)
    SetChrPos(0x104, -14520, 0, 15460, 90)
    SetChrPos(0x109, -14300, 0, 13610, 90)
    SetChrPos(0x105, -12900, 0, 12810, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0892
    ChrTalk(
        0x104,
        (
            "#00306Fやれやれ、\x01",
            "結局引き受けることに\x01",
            "なっちまったなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0893
    ChrTalk(
        0x102,
        (
            "#00102Fまあ、副局長も奥様が\x01",
            "心配なのでしょうし……\x02\x03",

            "真相が分かるまでは\x01",
            "付き合ってみても\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x103,
        "#00206Fふう、仕方ありませんね。\x02",
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0x109,
        (
            "#10100Fそれじゃ、最初は\x01",
            "どこを調べるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0x101,
        (
            "#00000Fまずは中央広場の\x01",
            "レストランに行ってみよう。\x02\x03",

            "ホストらしき人物と副局長夫人が\x01",
            "最近よく会っているらしいし、\x01",
            "直接話が聞けるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、それで\x01",
            "いいんじゃないかな。\x02\x03",

            "#10309Fそれじゃ、さっそく\x01",
            "行ってみるとしようか㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0898
    ChrTalk(
        0x101,
        "#00006F（なんだか楽しんでるな……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0899
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【副局長の依頼】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x84, 0x4, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x84, 0x4, 0x2)
    OP_29(0x84, 0x1, 0x0)
    SetScenarioFlags(0x175, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_55_16B23 end

    def Function_56_16EA1(): pass

    label("Function_56_16EA1")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_16EF6")

    #C0900
    ChrTalk(
        0x101,
        (
            "#00000F……上の階に用事はないな。\x01",
            "立ち入るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FD2")

    label("loc_16EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16F90")
    OP_4B(0x16, 0xFF)
    TurnDirection(0x16, 0x0, 500)

    #C0901
    ChrTalk(
        0x16,
        (
            "只今、エレベーターは\x01",
            "使用禁止とさせて頂いております。\x02",
        )
    )

    CloseMessageWindow()

    #C0902
    ChrTalk(
        0x16,
        (
            "皆さんは、１階会議室で\x01",
            "指示が出るのをお待ちください。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xB4, 0x0)
    OP_4C(0x16, 0xFF)
    Jump("loc_16FD2")

    label("loc_16F90")


    #C0903
    ChrTalk(
        0x101,
        (
            "#00000F……上の階に用事はないな。\x01",
            "立ち入るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FD2")

    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_56_16EA1 end

    def Function_57_16FE6(): pass

    label("Function_57_16FE6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_57_16FE6 end

    SaveToFile()

Try(main)
