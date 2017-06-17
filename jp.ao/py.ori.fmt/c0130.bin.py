from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0130.bin",                # FileName
        "c0130",                    # MapName
        "c0130",                    # Location
        0x0009,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0130",                  # 0
        "キーア",                 # 1
        "キーア",                 # 2
        "ツァイト",               # 3
        "SE制御",                 # 4
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08202.itc",                   # 01
        "chr/ch02707.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   1.0,                   -0.5,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.5,                  0.25,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 10,  -3.299999952316284,    68.0,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.649999976158142,     -34.0,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  1.0,                   71.5,                  0.0,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.5,                  -23.83333396911621,    -0.0,                  1.0])

    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  8,  0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  7,  0x0000)
    DeclActor(158830,  0,       125480,  1200,    158830,  2000,    125480,  0x007C, 0,  27, 0x0000)
    DeclActor(155320,  30,      123780,  1200,    155320,  1500,    123780,  0x007C, 0,  28, 0x0000)
    DeclActor(205730,  0,       130250,  1200,    205730,  1500,    130250,  0x007C, 0,  30, 0x0000)
    DeclActor(208820,  0,       123770,  1200,    208820,  2500,    123770,  0x007C, 0,  31, 0x0000)
    DeclActor(259740,  0,       121980,  1200,    259740,  3000,    121980,  0x007C, 0,  32, 0x0000)
    DeclActor(259339,  0,       126100,  1200,    259339,  1500,    126100,  0x007C, 0,  33, 0x0000)
    DeclActor(255780,  30,      65319,   1200,    255780,  1500,    65319,   0x007C, 0,  34, 0x0000)
    DeclActor(257120,  30,      68930,   1200,    257120,  1030,    68930,   0x007C, 0,  35, 0x0000)
    DeclActor(259010,  0,       66930,   1200,    259010,  1000,    66930,   0x007C, 0,  36, 0x0000)
    DeclActor(255680,  30,      73720,   1200,    255680,  1500,    73720,   0x007C, 0,  37, 0x0000)
    DeclActor(258000,  0,       63980,   1200,    258000,  2000,    63980,   0x007C, 0,  38, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  24, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  25, 0x0000)
    DeclActor(258360,  0,       128430,  1200,    258360,  1500,    128430,  0x007C, 0,  26, 0x0000)
    DeclActor(253320,  30,      71340,   1200,    253320,  1500,    71340,   0x007C, 0,  12, 0x0000)

    ChipFrameInfo(1472, 0)                                       # 0

    ScpFunction((
        "Function_0_5C0",          # 00, 0
        "Function_1_670",          # 01, 1
        "Function_2_950",          # 02, 2
        "Function_3_CDC",          # 03, 3
        "Function_4_FBA",          # 04, 4
        "Function_5_108A",         # 05, 5
        "Function_6_14DC",         # 06, 6
        "Function_7_1C21",         # 07, 7
        "Function_8_1C74",         # 08, 8
        "Function_9_1CC9",         # 09, 9
        "Function_10_1D86",        # 0A, 10
        "Function_11_1E43",        # 0B, 11
        "Function_12_1E9A",        # 0C, 12
        "Function_13_2974",        # 0D, 13
        "Function_14_2C30",        # 0E, 14
        "Function_15_2F0C",        # 0F, 15
        "Function_16_311B",        # 10, 16
        "Function_17_333C",        # 11, 17
        "Function_18_354D",        # 12, 18
        "Function_19_375E",        # 13, 19
        "Function_20_3972",        # 14, 20
        "Function_21_3B86",        # 15, 21
        "Function_22_3F82",        # 16, 22
        "Function_23_40A8",        # 17, 23
        "Function_24_4105",        # 18, 24
        "Function_25_41AA",        # 19, 25
        "Function_26_424F",        # 1A, 26
        "Function_27_42F4",        # 1B, 27
        "Function_28_43A7",        # 1C, 28
        "Function_29_4484",        # 1D, 29
        "Function_30_448D",        # 1E, 30
        "Function_31_4544",        # 1F, 31
        "Function_32_45FB",        # 20, 32
        "Function_33_46B4",        # 21, 33
        "Function_34_476B",        # 22, 34
        "Function_35_4822",        # 23, 35
        "Function_36_48D9",        # 24, 36
        "Function_37_498E",        # 25, 37
        "Function_38_4A47",        # 26, 38
        "Function_39_4B02",        # 27, 39
        "Function_40_4B77",        # 28, 40
        "Function_41_4BA6",        # 29, 41
        "Function_42_4BD5",        # 2A, 42
        "Function_43_4C04",        # 2B, 43
        "Function_44_4C33",        # 2C, 44
        "Function_45_5845",        # 2D, 45
        "Function_46_584D",        # 2E, 46
        "Function_47_6A0B",        # 2F, 47
        "Function_48_6A65",        # 30, 48
        "Function_49_6A81",        # 31, 49
        "Function_50_75FE",        # 32, 50
        "Function_51_761A",        # 33, 51
        "Function_52_909F",        # 34, 52
        "Function_53_90EE",        # 35, 53
        "Function_54_9117",        # 36, 54
        "Function_55_91B6",        # 37, 55
        "Function_56_91CD",        # 38, 56
        "Function_57_91E4",        # 39, 57
        "Function_58_91FB",        # 3A, 58
        "Function_59_9212",        # 3B, 59
        "Function_60_922E",        # 3C, 60
        "Function_61_924A",        # 3D, 61
        "Function_62_9266",        # 3E, 62
        "Function_63_92A5",        # 3F, 63
        "Function_64_92EB",        # 40, 64
        "Function_65_9318",        # 41, 65
        "Function_66_9334",        # 42, 66
        "Function_67_9364",        # 43, 67
        "Function_68_9380",        # 44, 68
        "Function_69_9CBC",        # 45, 69
        "Function_70_9D11",        # 46, 70
        "Function_71_9D69",        # 47, 71
        "Function_72_9DC1",        # 48, 72
        "Function_73_9E19",        # 49, 73
        "Function_74_A88D",        # 4A, 74
    ))


    def Function_0_5C0(): pass

    label("Function_0_5C0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5F8"),
        (1, "loc_604"),
        (2, "loc_610"),
        (3, "loc_61C"),
        (4, "loc_628"),
        (5, "loc_634"),
        (6, "loc_640"),
        (SWITCH_DEFAULT, "loc_64C"),
    )


    label("loc_5F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_604")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_610")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_61C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_628")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_634")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_640")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_64C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_658")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_66F")

    Return()

    # Function_0_5C0 end

    def Function_1_670(): pass

    label("Function_1_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34B, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    Event(0, 16)

    label("loc_6A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34A, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CC")
    Event(0, 15)

    label("loc_6CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34D, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F3")
    Event(0, 18)

    label("loc_6F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34C, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71A")
    Event(0, 17)

    label("loc_71A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x351, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_741")
    Event(0, 20)

    label("loc_741")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x350, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_768")
    Event(0, 19)

    label("loc_768")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_783")
    Event(0, 5)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x358, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BB")
    Event(0, 21)

    label("loc_7BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D7")
    Event(0, 21)

    label("loc_7D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F3")
    Event(0, 21)

    label("loc_7F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80F")
    Event(0, 21)

    label("loc_80F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Event(0, 21)

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_839")
    Jump("loc_935")

    label("loc_839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_889")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 257500, 500, 68000, 270)
    SetChrPos(0xA, 258550, 0, 66740, 180)
    Jump("loc_935")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_897")
    Jump("loc_935")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D6")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 257500, 500, 68000, 270)
    ClearChrFlags(0x8, 0x1)

    label("loc_8D6")

    Jump("loc_935")

    label("loc_8DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8E9")
    Jump("loc_935")

    label("loc_8E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8F7")
    Jump("loc_935")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_92C")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 254100, 200, 71300, 270)
    Jump("loc_935")

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_935")

    label("loc_935")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94F")
    Event(0, 68)

    label("loc_94F")

    Return()

    # Function_1_670 end

    def Function_2_950(): pass

    label("Function_2_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_963")
    OP_1B(0x2, 0x0, 0x49)

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AD")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A01")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A86")
    SetMapObjFrame(0xFF, "danbo", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 255600, -1000, 128900, 8000, 5000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 258899, -1000, 126000, 5000, 5000, 90000)
    Jump("loc_AC3")

    label("loc_A86")

    SetMapObjFrame(0xFF, "danbo", 0x0, 0x1)
    SetMapObjFrame(0xFF, "n01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "n03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADD")
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x2)
    OP_65(0x2, 0x1)

    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B08")
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x2)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x14, 0x2)
    Jump("loc_B0E")

    label("loc_B08")

    SetMapObjFlags(0x13, 0x4)

    label("loc_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B28")
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xA, 0x2)
    OP_65(0x4, 0x1)

    label("loc_B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B42")
    SetMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xB, 0x2)
    OP_65(0x5, 0x1)

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B60")
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x2)
    OP_65(0x6, 0x1)

    label("loc_B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B7E")
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xD, 0x2)
    OP_65(0x7, 0x1)

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B98")
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xE, 0x2)
    OP_65(0x8, 0x1)

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB2")
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xF, 0x2)
    OP_65(0x9, 0x1)

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC")
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x10, 0x2)
    OP_65(0xA, 0x1)

    label("loc_BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE6")
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x2)
    OP_65(0xB, 0x1)

    label("loc_BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C00")
    SetMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x12, 0x2)
    OP_65(0xC, 0x1)

    label("loc_C00")

    OP_65(0x10, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6F")
    LoadEffect(0x10, "event\\eva00_00.eff")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 253320, 1200, 71340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x10, 0x1)

    label("loc_C6F")

    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C8E")
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x0, 0x1)

    label("loc_C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CA1")
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x1, 0x1)

    label("loc_CA1")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC3")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_CC3")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDB")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_CDB")

    Return()

    # Function_2_950 end

    def Function_3_CDC(): pass

    label("Function_3_CDC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CED")
    Jump("loc_FB6")

    label("loc_CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D08")
    Call(0, 74)
    Jump("loc_DA5")

    label("loc_D08")


    #C0001
    ChrTalk(
        0x8,
        (
            "#01108Fノエルがいなくなっちゃったら\x01",
            "キーアもサビしいけど……\x01",
            "元気出してね、ノエルー。\x02\x03",

            "#01102F元気になったフランと\x01",
            "２人で遊びにくるのを待ってるからー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA5")

    Jump("loc_FB6")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DB8")
    Jump("loc_FB6")

    label("loc_DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD2")
    TalkEnd(0xFE)
    Call(0, 6)
    Return()

    label("loc_DD2")

    Jump("loc_FB6")

    label("loc_DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4E")

    #C0002
    ChrTalk(
        0x8,
        "#01105Fあ、ロイドたち出かけるのー？\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        "#00000Fああ、キーアは日曜学校の宿題か？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#01100Fうん、今日は外で遊べないから\x01",
            "先にやっちゃおうと思って。\x02\x03",

            "#01106F本当ならあのクルマに\x01",
            "乗りたかったんだけどー。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x109,
        (
            "#10106Fうう、本当に残念だよね。\x02\x03",

            "#10109F今度、晴れた休みの日にでも\x01",
            "みんなでドライブしようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        "#01109Fうん！　楽しみにしてるねー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 1)
    Jump("loc_FB6")

    label("loc_F4E")


    #C0007
    ChrTalk(
        0x8,
        (
            "#01109Fえへへ、今度の\x01",
            "晴れの日が楽しみだねー。\x02\x03",

            "#01110Fよーし、今日はぱぱっと\x01",
            "宿題をやっちゃおー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB6")

    TalkEnd(0xFE)
    Return()

    # Function_3_CDC end

    def Function_4_FBA(): pass

    label("Function_4_FBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1065")

    #C0008
    ChrTalk(
        0xA,
        "#01203Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#00200Fツァイトがノエルさんに\x01",
            "『達者でな』だそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x109,
        (
            "#10109Fあはは……\x01",
            "ありがとう、ツァイト君。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1086")

    label("loc_1065")


    #C0011
    ChrTalk(
        0xA,
        "#01203Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_1086")

    TalkEnd(0xFE)
    Return()

    # Function_4_FBA end

    def Function_5_108A(): pass

    label("Function_5_108A")

    EventBegin(0x0)
    Fade(500)
    OP_68(256649, 800, 124480, 0)
    MoveCamera(26, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x102, 257410, 0, 124690, 45)
    SetChrPos(0x101, 255000, 0, 124690, 315)
    SetChrPos(0x109, 256829, 0, 121730, 0)
    SetChrPos(0x105, 255220, 0, 122530, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1124")
    SetChrPos(0x1A5, 256209, 0, 125400, 0)

    label("loc_1124")

    OP_0D()

    #C0012
    ChrTalk(
        0x109,
        (
            "#12P#10100Fえっと、ここがあたしの部屋です。\x02\x03",

            "#10106Fあんまり面白みがなくて\x01",
            "ちょっと恥ずかしいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、片付いていて\x01",
            "結構じゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#11P#00102Fええ、ノエルさんらしくて\x01",
            "いいと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_131E")
    OP_93(0x1A5, 0x87, 0x1F4)
    Sleep(300)

    #C0015
    ChrTalk(
        0x1A5,
        (
            "#5P#01105Fねーねー、あそこに置いてる\x01",
            "クマさんはなんなのー？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1261():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1261)

    def lambda_126E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_126E)
    Sleep(50)

    def lambda_127E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_127E)
    Sleep(50)

    def lambda_128E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_128E)
    WaitChrThread(0x109, 1)

    #C0016
    ChrTalk(
        0x109,
        (
            "#12P#10109Fあはは……\x01",
            "フランとお揃いで持ってる\x01",
            "ぬいぐるみなの。\x02\x03",

            "#10100F警備隊の詰所に置いてたのを\x01",
            "持ってきちゃったんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140E")

    label("loc_131E")

    OP_93(0x101, 0x87, 0x1F4)

    #C0017
    ChrTalk(
        0x101,
        (
            "#5P#00000Fあれ、あそこに置いてある\x01",
            "ぬいぐるみは……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1363():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1363)
    Sleep(50)

    def lambda_1373():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1373)
    Sleep(50)

    def lambda_1383():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1383)
    WaitChrThread(0x109, 1)

    #C0018
    ChrTalk(
        0x109,
        (
            "#12P#10109Fあはは……\x01",
            "フランとお揃いで持ってる\x01",
            "ぬいぐるみです。\x02\x03",

            "#10100F警備隊の詰所に置いてたのを\x01",
            "持ってきちゃいました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140E")


    #C0019
    ChrTalk(
        0x101,
        (
            "#5P#00000Fはは、なるほど。\x01",
            "アクセントになってよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x109,
        (
            "#12P#10100Fふふ、ありがとうございます。\x02\x03",

            "#10104Fえっと、それじゃあ改めて……\x01",
            "不束者ですがよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 256010, 0, 121130, 0)
    SetScenarioFlags(0x13B, 6)
    EventEnd(0x5)
    Return()

    # Function_5_108A end

    def Function_6_14DC(): pass

    label("Function_6_14DC")

    EventBegin(0x0)
    Fade(500)
    OP_68(256920, 1000, 67670, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 255850, 0, 68670, 135)
    SetChrPos(0x102, 256720, 30, 66620, 45)
    SetChrPos(0x103, 254820, 30, 69190, 135)
    SetChrPos(0x104, 254420, 0, 67580, 90)
    SetChrPos(0x109, 255300, 30, 66540, 56)
    SetChrPos(0x105, 258360, 0, 66040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_1590():

        label("loc_1590")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1590")

    QueueWorkItem2(0x101, 2, lambda_1590)

    def lambda_15A2():

        label("loc_15A2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15A2")

    QueueWorkItem2(0x102, 2, lambda_15A2)

    def lambda_15B4():

        label("loc_15B4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15B4")

    QueueWorkItem2(0x103, 2, lambda_15B4)

    def lambda_15C6():

        label("loc_15C6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15C6")

    QueueWorkItem2(0x104, 2, lambda_15C6)

    def lambda_15D8():

        label("loc_15D8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15D8")

    QueueWorkItem2(0x109, 2, lambda_15D8)

    def lambda_15EA():

        label("loc_15EA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_15EA")

    QueueWorkItem2(0x105, 2, lambda_15EA)
    OP_0D()

    #C0021
    ChrTalk(
        0x8,
        "#11P#01110Fあ、みんなー……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        "#6P#00200Fキーア……大丈夫ですか？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#12P#00108F昨日からずっと\x01",
            "元気がないけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#11P#01102Fえへへ、うん。\x01",
            "キーアは大丈夫だけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0025
    ChrTalk(
        0x8,
        (
            "#11P#01103Fねえロイド……\x02\x03",

            "#01108Fやっぱりシズクの目って、\x01",
            "治すのが難しいの……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 3)), scpexpr(EXPR_END)), "loc_17CF")

    #C0026
    ChrTalk(
        0x101,
        (
            "#6P#00003F……ああ、難しいのは\x01",
            "間違いないと思う。\x02\x03",

            "#00000Fでも、シズクちゃんは\x01",
            "今でも前向きだったよ。\x02\x03",

            "落ち込むどころか、\x01",
            "治療が前進したって\x01",
            "喜んでたくらいさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1849")

    label("loc_17CF")


    #C0027
    ChrTalk(
        0x101,
        (
            "#6P#00003F……ああ、難しいのは\x01",
            "間違いないと思う。\x02\x03",

            "#00008F今回の手術にしたって、\x01",
            "失敗ってわけじゃ\x01",
            "ないそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1849")


    #C0028
    ChrTalk(
        0x8,
        "#11P#01106Fそっか……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#6P#00303Fなあ、キー坊。\x01",
            "落ち込むのは分かるが……\x01",
            "そろそろ元気を出しちゃどうだ？\x02\x03",

            "#00300Fシズクちゃんだって、\x01",
            "キー坊がそんな風に落ち込むのは\x01",
            "望んでないんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#12P#10103Fそ、そうだよ、キーアちゃん。\x02\x03",

            "#10102Fキーアちゃんが\x01",
            "笑顔でいてくれたほうが、\x01",
            "シズクちゃんも嬉しいと思うし！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#11P#01108F……うん、そうだねー。\x02\x03",

            "#01102Fキーアはシズクの親友だから……\x01",
            "今度会ったら元気づけてあげないと。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 256600, 0, 67990, 270)
    SetChrFlags(0x8, 0x40)
    Sound(802, 0, 100, 0)
    OP_0D()

    #C0032
    ChrTalk(
        0x8,
        (
            "#11P#01109Fえへへ、みんなありがとー。\x01",
            "キーアもちょっと元気でてきた。\x02\x03",

            "#01100Fえっと、ヤクソクしてるから\x01",
            "遊びに行ってくるねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#6P#00005Fあ、ああ……気をつけてな。\x02",
    )

    CloseMessageWindow()
    OP_95(0x8, 252320, 0, 65790, 2000, 0x1)

    def lambda_1B04():
        OP_95(0xFE, 251280, 0, 65770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B04)

    def lambda_1B1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B1E)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    EndChrThread(0x0, 0x2)
    EndChrThread(0x1, 0x2)
    EndChrThread(0x2, 0x2)
    EndChrThread(0x3, 0x2)
    EndChrThread(0x4, 0x2)
    EndChrThread(0x5, 0x2)
    Sleep(200)
    Sound(104, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x105,
        "#11P#10308F……大丈夫なのかな？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00003F分からないけど……\x01",
            "キーアならすぐに\x01",
            "元気になってくれるさ。\x02\x03",

            "#00000Fそれじゃあ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 255390, 0, 67800, 225)
    SetScenarioFlags(0x170, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_6_14DC end

    def Function_7_1C21(): pass

    label("Function_7_1C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C33")
    Call(0, 13)
    Jump("loc_1C73")

    label("loc_1C33")

    TalkBegin(0xFF)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00000Fここはティオの部屋だ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1C73")

    Return()

    # Function_7_1C21 end

    def Function_8_1C74(): pass

    label("Function_8_1C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C86")
    Call(0, 14)
    Jump("loc_1CC8")

    label("loc_1C86")

    TalkBegin(0xFF)

    #C0037
    ChrTalk(
        0x101,
        (
            "#00000Fここはランディの部屋だ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1CC8")

    Return()

    # Function_8_1C74 end

    def Function_9_1CC9(): pass

    label("Function_9_1CC9")

    EventBegin(0x1)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、キーアが\x01",
            "日曜学校に行くって言ってたな。\x02\x03",

            "課長も出かけた事だし、\x01",
            "一緒に出た方がいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#00100Fそうね、声を掛けましょう。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_9_1CC9 end

    def Function_10_1D86(): pass

    label("Function_10_1D86")

    EventBegin(0x1)

    #C0040
    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、キーアが\x01",
            "日曜学校に行くって言ってたな。\x02\x03",

            "課長も出かけた事だし、\x01",
            "一緒に出た方がいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00100Fそうね、声を掛けましょう。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_10_1D86 end

    def Function_11_1E43(): pass

    label("Function_11_1E43")

    EventBegin(0x1)

    #C0042
    ChrTalk(
        0x101,
        (
            "#00000Fキーアはこれから日曜学校だ。\x01",
            "裏口の方が近道だな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_11_1E43 end

    def Function_12_1E9A(): pass

    label("Function_12_1E9A")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    StopEffect(0x9, 0x0)
    OP_65(0x10, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis382.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis383.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis384.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis385.itp")
    OP_68(253680, 1430, 71690, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 254540, 30, 72300, 225)
    SetChrPos(0x102, 253960, 30, 69890, 315)
    SetChrPos(0x103, 255030, 30, 71510, 270)
    SetChrPos(0x104, 255370, 30, 70080, 315)
    SetChrPos(0xF4, 256240, 30, 72240, 270)
    SetChrPos(0xF5, 256019, 30, 71220, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x101,
        "#00005Fこれは……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    #C0044
    ChrTalk(
        0x104,
        (
            "#12P#00302Fへえ、白い石か。\x01",
            "なかなか綺麗じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#11P#00205Fこれって確か……\x02\x03",

            "#00200Fミシュラムでロイドさんが\x01",
            "キーアにプレゼントした……？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    #C0046
    ChrTalk(
        0x101,
        (
            "#00006Fああ、ミシュラムのビーチで\x01",
            "キーアにあげた『ホワイトストーン』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#12P#00108Fキーアちゃんが\x01",
            "置き忘れて行ったのかしら……？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはホワイトストーンを手に取った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sound(824, 0, 100, 0)
    Sleep(1000)
    Sound(2955, 255, 50, 0)    #voice#KeA
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2200)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    FadeToBright(500, 0)
    OP_0D()

    #C0049
    ChrTalk(
        0x101,
        "#00011F#30W…………ぇ………………\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    Sound(824, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(2956, 255, 50, 0)    #voice#KeA
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2600)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    Sound(2957, 255, 60, 0)    #voice#KeA
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    Sound(2958, 255, 75, 0)    #voice#KeA
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    Sound(2959, 255, 90, 0)    #voice#KeA
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    Sleep(2000)
    Sound(2960, 255, 100, 0)    #voice#KeA
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(2500)
    FadeToDark(2000, 16777215, -1)
    Sound(829, 0, 100, 0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    OP_0D()
    SetCameraDistance(19000, 0)
    SetCameraDistance(21000, 2000)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)

    #C0050
    ChrTalk(
        0x101,
        "#00005F#40W……………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2420")

    #C0051
    ChrTalk(
        0x106,
        (
            "#11P#10708F#30Wい、今のは……\x01",
            "キーアちゃん……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A6")

    label("loc_2420")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_246B")

    #C0052
    ChrTalk(
        0x109,
        (
            "#11P#10113F#30Wい、今のは……\x01",
            "キーアちゃん……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A6")

    label("loc_246B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24A6")

    #C0053
    ChrTalk(
        0x105,
        "#11P#10408F#30W今のは……キーア……？\x02",
    )

    CloseMessageWindow()

    label("loc_24A6")


    #C0054
    ChrTalk(
        0x104,
        (
            "#12P#00301F#30W間違いねえだろう。\x01",
            "……だが、どこから……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0055
    ChrTalk(
        0x103,
        (
            "#11P#00206F#30Wロイドさんが手にしたそれに、\x01",
            "残留思念のようなものが\x01",
            "込められているのを感じます。\x02\x03",

            "#00208F……哀しさや迷いを\x01",
            "無理やりに押し込めたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#12P#00106F#30Wキーアちゃん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2611")

    #C0057
    ChrTalk(
        0x10A,
        (
            "#11P#00608F#30W……まったく……\x01",
            "あの能天気で無邪気だった子供が……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C2")

    label("loc_2611")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2668")

    #C0058
    ChrTalk(
        0x105,
        (
            "#11P#10408F#30W……やれやれ。\x01",
            "あそこまで無邪気だった子が……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C2")

    label("loc_2668")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26C2")

    #C0059
    ChrTalk(
        0x109,
        (
            "#11P#10106F#30W……ここまでの想いを\x01",
            "キーアちゃんにさせてたなんて……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C2")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0060
    ChrTalk(
        0x101,
        (
            "#00006F#30W……これでもう……\x01",
            "迷いの一片も完全に無くなった。\x02\x03",

            "#00015Fキーアがあんな……\x01",
            "心を押し殺したような気持ちで\x01",
            "ずっといたなんて……\x02\x03",

            "#00010Fそんな状況は、絶対に間違ってる！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#12P#00101Fそうね……そんなのが\x01",
            "正しい事であるわけがないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        (
            "#12P#00307F……こうなったら、\x01",
            "なにがなんでもキー坊の元に\x01",
            "辿り着かなきゃな！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#11P#00201Fええ、キーアの笑顔を\x01",
            "取り戻すためにも……！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#00007Fああ……行こう、みんな。\x02\x03",

            "#00003F（キーア……待っててくれ。\x01",
            "  絶対に迎えに行くからな……！）\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetCameraDistance(21375, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3A1),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x3A1, 1)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(10)
    OP_1F()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 254410, 30, 69820, 225)
    SetScenarioFlags(0x1BC, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2971")
    OP_E0(0x34, 0x0)

    label("loc_2971")

    EventEnd(0x5)
    Return()

    # Function_12_1E9A end

    def Function_13_2974(): pass

    label("Function_13_2974")

    EventBegin(0x0)
    Fade(500)
    OP_68(169990, 1000, 63110, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23860, 0)
    SetChrPos(0x101, 170800, 0, 62310, 315)
    SetChrPos(0x102, 168790, 0, 62190, 45)
    SetChrPos(0x109, 171240, 0, 63400, 270)
    SetChrPos(0x105, 168190, 0, 63200, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A0E")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_2A0E")

    OP_0D()

    #C0066
    ChrTalk(
        0x102,
        "#6P#00100Fここはティオちゃんの部屋ね。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#6P#10300F確か今は、レマン自治州に\x01",
            "出張しているんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#00000Fああ、ヨナと一緒に\x01",
            "エプスタイン財団の\x01",
            "研究所に行っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        (
            "#6P#00100F自治州法の改正で導力ネットも\x01",
            "普及が進められているし、\x01",
            "その関係の手伝いなんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        (
            "#11P#10103F難しいことはわかりませんけど……\x01",
            "そっちもかなり大変そうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BE2")

    #C0071
    ChrTalk(
        0x1A5,
        "#12P#01100Fティオ、早く帰ってこれるといいねー。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#00000Fああ、本当にな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C18")

    label("loc_2BE2")


    #C0073
    ChrTalk(
        0x101,
        (
            "#00000Fああ、早く帰ってこれると\x01",
            "いいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C18")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_13_2974 end

    def Function_14_2C30(): pass

    label("Function_14_2C30")

    EventBegin(0x0)
    Fade(500)
    OP_68(14040, 800, 63300, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23800, 0)
    SetChrPos(0x101, 12730, 0, 61720, 45)
    SetChrPos(0x102, 14330, 0, 61720, 315)
    SetChrPos(0x109, 11530, 0, 62750, 90)
    SetChrPos(0x105, 15130, 0, 62750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CCA")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_2CCA")

    OP_0D()

    #C0074
    ChrTalk(
        0x101,
        "#12P#00000Fこっちはランディの部屋だな。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#00100Fランディは今、\x01",
            "ベルガード門の部隊と\x01",
            "リハビリ訓練の真っ最中なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x105,
        (
            "#10305Fああ、確か教団事件で\x01",
            "例のクスリを盛られてたんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x109,
        (
            "#6P#10103Fうん……\x01",
            "後遺症というほど酷いものが\x01",
            "残ったわけじゃないけど。\x02\x03",

            "#10108F体力とカンを取り戻すのに\x01",
            "しばらく時間がかかるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#12P#00003Fそうか……\x01",
            "警備隊も早く立ち直ってほしいな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EB6")

    #C0079
    ChrTalk(
        0x1A5,
        "#12P#01100Fランディも早く帰ってこないかなー。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        "#00100Fふふ、本当にね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF4")

    label("loc_2EB6")


    #C0081
    ChrTalk(
        0x102,
        (
            "#00100Fそうね、ランディにも\x01",
            "早く帰ってきてもらいたいし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF4")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_14_2C30 end

    def Function_15_2F0C(): pass

    label("Function_15_2F0C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x2)
    OP_68(157620, 1330, 125080, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F66")
    SetChrFlags(0x0, 0x8)

    label("loc_2F66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F79")
    SetChrFlags(0x1, 0x8)

    label("loc_2F79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8C")
    SetChrFlags(0x2, 0x8)

    label("loc_2F8C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F9F")
    SetChrFlags(0x3, 0x8)

    label("loc_2F9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB2")
    SetChrFlags(0x4, 0x8)

    label("loc_2FB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC5")
    SetChrFlags(0x5, 0x8)

    label("loc_2FC5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2FDE")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_2FDE")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 157620, 30, 125080, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0082
    ChrTalk(
        0x102,
        "#0100Fここでいいかしら。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34A, 1)
    SetScenarioFlags(0x13C, 6)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x2, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 44)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308F")
    ClearChrFlags(0x0, 0x8)

    label("loc_308F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30A2")
    ClearChrFlags(0x1, 0x8)

    label("loc_30A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30B5")
    ClearChrFlags(0x2, 0x8)

    label("loc_30B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30C8")
    ClearChrFlags(0x3, 0x8)

    label("loc_30C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30DB")
    ClearChrFlags(0x4, 0x8)

    label("loc_30DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30EE")
    ClearChrFlags(0x5, 0x8)

    label("loc_30EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3107")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_3107")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2F0C end

    def Function_16_311B(): pass

    label("Function_16_311B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x2)
    OP_68(154920, 1330, 122580, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3187")
    SetChrFlags(0x0, 0x8)

    label("loc_3187")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_319A")
    SetChrFlags(0x1, 0x8)

    label("loc_319A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31AD")
    SetChrFlags(0x2, 0x8)

    label("loc_31AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31C0")
    SetChrFlags(0x3, 0x8)

    label("loc_31C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31D3")
    SetChrFlags(0x4, 0x8)

    label("loc_31D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31E6")
    SetChrFlags(0x5, 0x8)

    label("loc_31E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_31FF")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_31FF")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154920, 30, 122580, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0084
    ChrTalk(
        0x102,
        "#0100Fここでいいかしら。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34B, 1)
    SetScenarioFlags(0x13C, 7)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x3, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 44)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B0")
    ClearChrFlags(0x0, 0x8)

    label("loc_32B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32C3")
    ClearChrFlags(0x1, 0x8)

    label("loc_32C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D6")
    ClearChrFlags(0x2, 0x8)

    label("loc_32D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32E9")
    ClearChrFlags(0x3, 0x8)

    label("loc_32E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32FC")
    ClearChrFlags(0x4, 0x8)

    label("loc_32FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_330F")
    ClearChrFlags(0x5, 0x8)

    label("loc_330F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3328")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_3328")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_16_311B end

    def Function_17_333C(): pass

    label("Function_17_333C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x2)
    OP_68(206000, 1300, 129509, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3396")
    SetChrFlags(0x0, 0x8)

    label("loc_3396")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A9")
    SetChrFlags(0x1, 0x8)

    label("loc_33A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33BC")
    SetChrFlags(0x2, 0x8)

    label("loc_33BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33CF")
    SetChrFlags(0x3, 0x8)

    label("loc_33CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33E2")
    SetChrFlags(0x4, 0x8)

    label("loc_33E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F5")
    SetChrFlags(0x5, 0x8)

    label("loc_33F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_340E")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_340E")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 206000, 0, 129509, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0086
    ChrTalk(
        0x103,
        "#0200Fここでいいでしょう。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34C, 1)
    SetScenarioFlags(0x13D, 0)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x4, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 46)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34C1")
    ClearChrFlags(0x0, 0x8)

    label("loc_34C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34D4")
    ClearChrFlags(0x1, 0x8)

    label("loc_34D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E7")
    ClearChrFlags(0x2, 0x8)

    label("loc_34E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34FA")
    ClearChrFlags(0x3, 0x8)

    label("loc_34FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_350D")
    ClearChrFlags(0x4, 0x8)

    label("loc_350D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3520")
    ClearChrFlags(0x5, 0x8)

    label("loc_3520")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3539")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_3539")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_17_333C end

    def Function_18_354D(): pass

    label("Function_18_354D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x2)
    OP_68(208220, 1300, 123970, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A7")
    SetChrFlags(0x0, 0x8)

    label("loc_35A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35BA")
    SetChrFlags(0x1, 0x8)

    label("loc_35BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35CD")
    SetChrFlags(0x2, 0x8)

    label("loc_35CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35E0")
    SetChrFlags(0x3, 0x8)

    label("loc_35E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F3")
    SetChrFlags(0x4, 0x8)

    label("loc_35F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3606")
    SetChrFlags(0x5, 0x8)

    label("loc_3606")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_361F")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_361F")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208220, 0, 123970, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0088
    ChrTalk(
        0x103,
        "#0200Fここでいいでしょう。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34D, 1)
    SetScenarioFlags(0x13D, 1)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x5, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 46)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D2")
    ClearChrFlags(0x0, 0x8)

    label("loc_36D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E5")
    ClearChrFlags(0x1, 0x8)

    label("loc_36E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36F8")
    ClearChrFlags(0x2, 0x8)

    label("loc_36F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_370B")
    ClearChrFlags(0x3, 0x8)

    label("loc_370B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_371E")
    ClearChrFlags(0x4, 0x8)

    label("loc_371E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3731")
    ClearChrFlags(0x5, 0x8)

    label("loc_3731")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_374A")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_374A")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_18_354D end

    def Function_19_375E(): pass

    label("Function_19_375E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    OP_68(258329, 1300, 122180, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37B8")
    SetChrFlags(0x0, 0x8)

    label("loc_37B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37CB")
    SetChrFlags(0x1, 0x8)

    label("loc_37CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37DE")
    SetChrFlags(0x2, 0x8)

    label("loc_37DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37F1")
    SetChrFlags(0x3, 0x8)

    label("loc_37F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3804")
    SetChrFlags(0x4, 0x8)

    label("loc_3804")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3817")
    SetChrFlags(0x5, 0x8)

    label("loc_3817")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3830")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_3830")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258329, 0, 122180, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0090
    ChrTalk(
        0x109,
        "#10100Fここでよさそうですね。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x13D, 2)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x6, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 49)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38E6")
    ClearChrFlags(0x0, 0x8)

    label("loc_38E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F9")
    ClearChrFlags(0x1, 0x8)

    label("loc_38F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_390C")
    ClearChrFlags(0x2, 0x8)

    label("loc_390C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_391F")
    ClearChrFlags(0x3, 0x8)

    label("loc_391F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3932")
    ClearChrFlags(0x4, 0x8)

    label("loc_3932")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3945")
    ClearChrFlags(0x5, 0x8)

    label("loc_3945")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_395E")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_395E")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_19_375E end

    def Function_20_3972(): pass

    label("Function_20_3972")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    OP_68(258149, 1300, 125700, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39CC")
    SetChrFlags(0x0, 0x8)

    label("loc_39CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39DF")
    SetChrFlags(0x1, 0x8)

    label("loc_39DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39F2")
    SetChrFlags(0x2, 0x8)

    label("loc_39F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A05")
    SetChrFlags(0x3, 0x8)

    label("loc_3A05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A18")
    SetChrFlags(0x4, 0x8)

    label("loc_3A18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A2B")
    SetChrFlags(0x5, 0x8)

    label("loc_3A2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3A44")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_3A44")

    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 258149, 0, 125700, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0092
    ChrTalk(
        0x109,
        "#10100Fここでよさそうですね。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x13D, 3)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x7, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 49)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AFA")
    ClearChrFlags(0x0, 0x8)

    label("loc_3AFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B0D")
    ClearChrFlags(0x1, 0x8)

    label("loc_3B0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B20")
    ClearChrFlags(0x2, 0x8)

    label("loc_3B20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B33")
    ClearChrFlags(0x3, 0x8)

    label("loc_3B33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B46")
    ClearChrFlags(0x4, 0x8)

    label("loc_3B46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B59")
    ClearChrFlags(0x5, 0x8)

    label("loc_3B59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3B72")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_3B72")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_20_3972 end

    def Function_21_3B86(): pass

    label("Function_21_3B86")

    EventBegin(0x0)
    SoundLoad(3668)
    SoundLoad(3669)
    SoundLoad(3670)
    SoundLoad(3671)
    FadeToDark(0, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BB2")
    SetChrFlags(0x0, 0x8)

    label("loc_3BB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BC5")
    SetChrFlags(0x1, 0x8)

    label("loc_3BC5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BD8")
    SetChrFlags(0x2, 0x8)

    label("loc_3BD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BEB")
    SetChrFlags(0x3, 0x8)

    label("loc_3BEB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BFE")
    SetChrFlags(0x4, 0x8)

    label("loc_3BFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C11")
    SetChrFlags(0x5, 0x8)

    label("loc_3C11")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0094
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F（そういえば……\x01",
            "  キーアが喜びそうなぬいぐるみを\x01",
            "  手に入れていたな。）\x02\x03",

            "（せっかくだからプレゼントしよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはキーアを捜して\x01",
            "ぬいぐるみをプレゼントした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(280, 150, -1, -1)

    #A0096
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01100F#3668Vわあ、キーアにくれるのー！？\x02\x03",

            "#3669Vえへへ……\x01",
            "ロイド、ありがとーっ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE55)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0097
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000Fはは、どういたしまして。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF4")
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x13D, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x2)
    OP_66(0x9, 0x1)
    SetChrPos(0x9, 255500, 0, 68590, 89)
    OP_68(256000, 1300, 68810, 0)
    Call(0, 22)

    label("loc_3DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E4A")
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x13D, 4)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_66(0x8, 0x1)
    SetChrPos(0x9, 255940, 30, 66720, 180)
    OP_68(256220, 1330, 66750, 0)
    Call(0, 22)

    label("loc_3E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EA0")
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x13D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x2)
    OP_66(0xA, 0x1)
    SetChrPos(0x9, 258089, 0, 67110, 89)
    OP_68(258310, 1300, 67080, 0)
    Call(0, 22)

    label("loc_3EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF6")
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x13D, 7)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x2)
    OP_66(0xB, 0x1)
    SetChrPos(0x9, 255560, 30, 72720, 0)
    OP_68(255320, 1330, 72710, 0)
    Call(0, 22)

    label("loc_3EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x358, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F4C")
    SubItemNumber(0x358, 1)
    SetScenarioFlags(0x13E, 0)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x2)
    OP_66(0xC, 0x1)
    SetChrPos(0x9, 256500, 30, 63940, 89)
    OP_68(256850, 1330, 63910, 0)
    Call(0, 22)

    label("loc_3F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F6D")
    Call(0, 51)

    label("loc_3F6D")

    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x6)
    NewScene("c0130", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3B86 end

    def Function_22_3F82(): pass

    label("Function_22_3F82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F99")
    Sleep(1000)
    Jump("loc_3F9C")

    label("loc_3F99")

    Sleep(500)

    label("loc_3F9C")

    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x9, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400A")

    #C0098
    ChrTalk(
        0x9,
        "#01100F#3670Vうんっ、ここがいいかもー。\x02",
    )

    Jump("loc_4034")

    label("loc_400A")


    #C0099
    ChrTalk(
        0x9,
        "#01100F#3671Vんー、この子はここかな？\x02",
    )


    label("loc_4034")

    CloseMessageWindow()
    OP_24(0xE56)
    OP_24(0xE57)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キーアの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Call(0, 23)
    Call(0, 39)
    FadeToDark(500, 0, -1)
    OP_0D()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_22_3F82 end

    def Function_23_40A8(): pass

    label("Function_23_40A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4104")
    SetChrName("")

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "家具アイテムを入手すると\x01",
            "支援課メンバーの部屋に置く事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_4104")

    Return()

    # Function_23_40A8 end

    def Function_24_4105(): pass

    label("Function_24_4105")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_418C")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_418C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41A8")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_41A8")

    Return()

    # Function_24_4105 end

    def Function_25_41AA(): pass

    label("Function_25_41AA")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4231")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_4231")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_424D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_424D")

    Return()

    # Function_25_41AA end

    def Function_26_424F(): pass

    label("Function_26_424F")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D6")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_42D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42F2")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_42F2")

    Return()

    # Function_26_424F end

    def Function_27_42F4(): pass

    label("Function_27_42F4")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis362.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "瀟洒な姿見がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_27_42F4 end

    def Function_28_43A7(): pass

    label("Function_28_43A7")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis363.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オルゴールがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    BeginChrThread(0xB, 1, 0, 29)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_28_43A7 end

    def Function_29_4484(): pass

    label("Function_29_4484")

    PlayBGM("ed7591", 0)
    Sleep(19000)
    OP_1F()
    Return()

    # Function_29_4484 end

    def Function_30_448D(): pass

    label("Function_30_448D")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis364.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カゲマル貯金箱がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_30_448D end

    def Function_31_4544(): pass

    label("Function_31_4544")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis365.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "みーしぇぐるみがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_31_4544 end

    def Function_32_45FB(): pass

    label("Function_32_45FB")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis370.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レース用フラッグがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_45FB end

    def Function_33_46B4(): pass

    label("Function_33_46B4")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis371.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ミニベロ自転車がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_33_46B4 end

    def Function_34_476B(): pass

    label("Function_34_476B")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis373.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ポムクッションがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_34_476B end

    def Function_35_4822(): pass

    label("Function_35_4822")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis372.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "変なクッションがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_35_4822 end

    def Function_36_48D9(): pass

    label("Function_36_48D9")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis374.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "黒テディベアがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_36_48D9 end

    def Function_37_498E(): pass

    label("Function_37_498E")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis375.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "にがとまとにあんがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_37_498E end

    def Function_38_4A47(): pass

    label("Function_38_4A47")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis376.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＺＷＥＩ２ペンギンがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_38_4A47 end

    def Function_39_4B02(): pass

    label("Function_39_4B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B76")
    OP_E0(0x16, 0x0)

    label("loc_4B76")

    Return()

    # Function_39_4B02 end

    def Function_40_4B77(): pass

    label("Function_40_4B77")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_40_4B77 end

    def Function_41_4BA6(): pass

    label("Function_41_4BA6")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_41_4BA6 end

    def Function_42_4BD5(): pass

    label("Function_42_4BD5")

    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_42_4BD5 end

    def Function_43_4C04(): pass

    label("Function_43_4C04")

    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_43_4C04 end

    def Function_44_4C33(): pass

    label("Function_44_4C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5844")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis362.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis363.itp")
    LoadChrToIndex("chr/ch00102.itc", 0x1E)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 155910, 200, 123440, 290)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4CE5")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_4CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4CFE")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_4CFE")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その日、ロイドたちは\x01",
            "支援業務の合間に支援課に戻り──\x02",
        )
    )

    CloseMessageWindow()

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本部との定時連絡を取りがてら\x01",
            "各自休憩を入れることにした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(154920, 1880, 123500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(154920, 1330, 123500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)

    #C0115
    ChrTalk(
        0x102,
        "#00104F…………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 155790, 0, 118500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    #N0116
    NpcTalk(
        0x101,
        "ロイドの声",
        "#1Pエリィ、いいかな？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x1)
    Sleep(500)

    #C0117
    ChrTalk(
        0x102,
        (
            "#00100Fロイド？\x01",
            "ええ、入ってきて。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x40)
    SetChrPos(0x102, 155440, 30, 122630, 180)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x4)
    OP_68(155280, 1330, 121810, 2000)
    SetCameraDistance(21220, 2000)
    Sleep(500)
    OP_9B(0x0, 0x102, 0x0, 0x1F4, 0x3E8, 0x0)

    def lambda_4F00():

        label("loc_4F00")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4F00")

    QueueWorkItem2(0x102, 2, lambda_4F00)
    OP_0D()
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_4F1C():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F1C)

    def lambda_4F31():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F31)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x102, 500)
    EndChrThread(0x102, 0x2)
    OP_6F(0x79)
    Sleep(200)

    #C0118
    ChrTalk(
        0x102,
        "#00100Fそろそろ出発する？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00004Fああ、本部からの業務連絡も\x01",
            "今日は特に無かったからね。\x02\x03",

            "#00000Fまだみんな集まっていないから\x01",
            "そんなに急がなくてもいいけどさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x14A, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x1E, 0x1F4)
    Sleep(750)

    #C0120
    ChrTalk(
        0x101,
        (
            "#00005Fあ……\x01",
            "何だか色々と増えてるな？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(157760, 1330, 124430, 3000)
    SetCameraDistance(22230, 3000)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_93(0x102, 0x2D, 0x1F4)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 40)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0121
    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00102Fふふ、こうして\x01",
            "暮らしているとつい、ね。\x02\x03",

            "#00104Fたまに実家に戻った時に\x01",
            "必要のない本や小物は\x01",
            "運んでいるのだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0122
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00009Fいや、俺の部屋に比べたら\x01",
            "綺麗に片付けてるじゃないか。\x02\x03",

            "#00000F増えたといっても\x01",
            "部屋に合ったものばかりだし……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 41)
    OP_68(155770, 1330, 122300, 2000)
    SetCameraDistance(23220, 2000)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_51CF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51CF)
    Sleep(200)

    def lambda_51DF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51DF)
    Sleep(500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0123
    ChrTalk(
        0x101,
        (
            "#00005Fそれって……\x01",
            "もしかしてオルゴールか？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        "#00100Fふふ、そうよ。\x02",
    )

    CloseMessageWindow()
    OP_68(155140, 1330, 123720, 2000)
    SetCameraDistance(22230, 2000)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 42)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0125
    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00104Fイメルダさんのお店にあった\x01",
            "リーヴェルト社という所の\x01",
            "アンティーク・オルゴール……\x02\x03",

            "#00100F懐かしい曲だったから\x01",
            "つい買ってしまったの。\x02\x03",

            "#00109F……ちょっと聞いてみる？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0126
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000Fああ、興味あるな。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 43)
    Sleep(750)
    StopBGM(0x1388)
    MoveCamera(45, 22, 0, 4000)
    SetCameraDistance(20000, 4000)
    OP_95(0x102, 155440, 30, 122630, 1000, 0x0)
    Sleep(1000)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 155910, 200, 123440, 290)
    OP_0D()
    Sleep(250)
    OP_95(0x101, 154430, 30, 122450, 2000, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(853, 0, 50, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sleep(1500)
    SetCameraDistance(18000, 19000)
    OP_71(0x9, 0xF, 0x5F, 0x0, 0x20)
    BeginChrThread(0xB, 1, 0, 45)
    WaitChrThread(0xB, 1)
    OP_74(0x9, 0x0)
    Sleep(1000)
    PlayBGM("ed7102", 0)

    #C0127
    ChrTalk(
        0x101,
        (
            "#00009F#1Pはあぁ～……\x01",
            "溜息が出るような音色だな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(200)

    #C0128
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、でしょう？\x02\x03",

            "#00104F帝国のリーヴェルト社といえば\x01",
            "楽器メーカーとして有名なのだけど\x01",
            "オルゴールも人気が高いの。\x02\x03",

            "#00100F私も昔、これと同じ曲で\x01",
            "もっと小さな弁数のものを\x01",
            "持っていたのだけど……\x02\x03",

            "#00106F留学先に持って行った時に\x01",
            "失くしてしまったのよね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0129
    ChrTalk(
        0x101,
        (
            "#00005F#1Pそっか……\x02\x03",

            "#00006F（ひょっとしてご両親との\x01",
            "  想い出の品だったのかな……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        (
            "#00103Fもう廃盤になっていたから\x01",
            "諦めていたのだけど……\x02\x03",

            "#00100Fイメルダさんの所に入荷して\x01",
            "本当に良かったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#00004F#1Pそうだな……\x02\x03",

            "#00002Fハハ、あの人の店も\x01",
            "たまには役に立つもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        "#00109Fふふ、そうね。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x40)
    SetChrPos(0x102, 155640, 30, 122530, 180)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x4)
    OP_68(154430, 1330, 122240, 1500)
    MoveCamera(45, 25, 0, 1500)
    OP_6E(350, 1500)
    SetCameraDistance(19750, 1500)
    OP_0D()

    def lambda_5712():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5712)
    Sleep(200)

    def lambda_5722():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5722)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    Sleep(500)

    #C0133
    ChrTalk(
        0x102,
        (
            "#00100Fさてと。\x01",
            "行きましょうか、ロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#00000F……ああ！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20750, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの家具を全て揃えた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x102, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5805")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_5805")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_581E")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_581E")

    OP_49()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    SetScenarioFlags(0x12C, 6)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 108, 0, 0)
    IdleLoop()

    label("loc_5844")

    Return()

    # Function_44_4C33 end

    def Function_45_5845(): pass

    label("Function_45_5845")

    PlayBGM("ed7591", 1)
    Sleep(19000)
    Return()

    # Function_45_5845 end

    def Function_46_584D(): pass

    label("Function_46_584D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A0A")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis365.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis364.itp")
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    SoundLoad(938)
    SoundLoad(939)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 205890, 80, 126750, 180)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x103, 3, 0, 47)
    ClearMapObjFlags(0x15, 0x4)
    OP_70(0x15, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5925")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_5925")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_593E")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_593E")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その日、ロイドたちは\x01",
            "支援業務の合間に支援課に戻り──\x02",
        )
    )

    CloseMessageWindow()

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本部との定時連絡を取りがてら\x01",
            "各自休憩を入れることにした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(205970, 1830, 125860, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22510, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    Sound(938, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_68(205970, 1330, 125860, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 205780, 0, 119210, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    #N0138
    NpcTalk(
        0x101,
        "ロイドの声",
        "#1Pティオ、ちょっといいか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    StopSound(938, 300, 40)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    #C0139
    ChrTalk(
        0x103,
        (
            "#00200Fええ。\x01",
            "どうぞ、ロイドさん。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(205300, 1330, 124060, 1500)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(205440, 1330, 124910, 2000)

    def lambda_5B03():
        OP_9B(0x0, 0xFE, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B03)

    def lambda_5B18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B18)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x103, 500)
    OP_6F(0x79)
    Sleep(500)

    #C0140
    ChrTalk(
        0x103,
        "#00200Fそろそろ出かけますか？\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#00004Fああ、本部からの業務連絡も\x01",
            "今日は特に無かったからね。\x02\x03",

            "#00000Fまだみんな集まっていないから\x01",
            "そんなに急がなくてもいいけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        "#00204Fいえ、すぐに出れます。\x02",
    )

    CloseMessageWindow()
    Sound(938, 2, 50, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x50, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(750)

    #C0143
    ChrTalk(
        0x101,
        (
            "#00005Fあ……\x01",
            "何だか色々と増えてるな？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(209790, 1330, 124450, 2500)
    MoveCamera(60, 25, 0, 2500)
    OP_6E(350, 2500)
    SetCameraDistance(20000, 2500)
    OP_6F(0x79)
    Sleep(1000)
    OP_68(205740, 1330, 129949, 5000)
    MoveCamera(30, 25, 0, 5000)
    OP_6F(0x79)
    Sleep(2000)
    BeginChrThread(0xB, 1, 0, 48)
    Fade(500)
    OP_68(205720, 1330, 125260, 0)
    OP_6E(350, 0)
    SetCameraDistance(22510, 0)
    MoveCamera(45, 22, 0, 0)
    OP_0D()
    Sleep(1000)
    StopSound(938, 300, 40)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x103, 3)
    Sleep(800)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)
    Sound(71, 0, 60, 0)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x1, 0xA, 0x0, 0x8)
    OP_79(0x15)
    Sleep(500)
    Fade(500)
    SetChrFlags(0x103, 0x40)
    SetChrPos(0x103, 205890, 0, 126850, 180)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x4)
    OP_0D()
    Sleep(1000)

    #C0144
    ChrTalk(
        0x103,
        (
            "#00204F……なかなか良いものが\x01",
            "ゲットできました。\x02\x03",

            "#00202Fキャラクターグッズに関しても\x01",
            "クロスベルは周辺諸国と比較して\x01",
            "かなりのアドバンテージがありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#00009Fはは、何といっても\x01",
            "みっしぃのお膝元だからな。\x02\x03",

            "#00004Fミシュラムのテーマパークのおかげで\x01",
            "周辺国でも広まりつつあるらしいし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(209440, 1330, 124760, 2500)
    MoveCamera(60, 25, 0, 2500)
    OP_6E(350, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_5EDD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EDD)
    Sleep(200)

    def lambda_5EED():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EED)
    OP_6F(0x79)
    Sleep(500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    Call(0, 40)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60E9")
    SetMessageWindowPos(280, 150, -1, -1)

    #A0146
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fそういえば……\x02\x03",

            "#00000Fそっちのピンク色のみっしぃは\x01",
            "《みーしぇ》って言ったっけ。\x02\x03",

            "#00004F確かみっしぃの妹だっていう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    #A0147
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00202Fはい、若干トホホなお兄ちゃんを\x01",
            "仕方ないなぁと言いながら世話を焼く、\x01",
            "非常に高スペックな妹キャラです。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0148
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00012Fそ、そっか……\x01",
            "（高スペックな妹って何だ？）\x02\x03",

            "#00005Fえっと、それじゃあ、\x01",
            "そっちの黒っぽいネコは？\x02\x03",

            "#00000Fクッションにもあしらわれてるけど\x01",
            "みっしぃとは関係ないよな？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_62E8")

    label("loc_60E9")

    SetMessageWindowPos(280, 150, -1, -1)

    #A0149
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fそういえば……\x02\x03",

            "#00000Fそのピンク色のみっしぃは\x01",
            "どういうバージョンなんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x103, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0150
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00206F……ロイドさんは不勉強すぎます。\x02\x03",

            "#00200Fそれはみっしぃではなく、\x01",
            "彼の妹である《みーしぇ》です。\x02\x03",

            "#00211Fクロスベルの捜査官ならば\x01",
            "そのくらい知っていてもらわないと。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0151
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006Fめ、面目ない……\x01",
            "（捜査官は関係ないと思うけど。）\x02\x03",

            "#00005Fえっと、それじゃあ、\x01",
            "そっちの黒っぽいネコは？\x02\x03",

            "#00000Fクッションにもあしらわれてるけど\x01",
            "みっしぃとは関係ないよな？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_62E8")

    Call(0, 41)

    def lambda_62F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62F0)
    Sleep(200)

    def lambda_6300():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6300)
    OP_68(205550, 1330, 128690, 3000)
    MoveCamera(34, 25, 0, 3000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)
    Call(0, 42)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0152
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00202Fそれは《カゲマル》ですね。\x02\x03",

            "#00204F最近、人気の出てきた連載小説の\x01",
            "主人公が飼っているネコで……\x02\x03",

            "#00200Fふてぶてしい可愛らしさと\x01",
            "ブニューという独特な鳴き声で\x01",
            "ブレイクしつつあるキャラです。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0153
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fへえ、そうだったのか。\x02\x03",

            "#00003Fそういえばカジノの景品とかにも\x01",
            "入っているみたいだけど。\x02\x03",

            "#00009Fしかし、みっしぃといいコイツといい\x01",
            "素直に可愛いとは言えないような──\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    #A0154
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00211Fジロッ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0155
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006Fいえ、何でもありません。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    #A0156
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00206F……まあ、言いたい事は判ります。\x02\x03",

            "#00200Fみっしぃは、何とも言えない\x01",
            "ユニークな不安定さが売りの\x01",
            "いわゆる『ゆるキャラ』ですし……\x02\x03",

            "#00203Fカゲマルはその愛想のなさが\x01",
            "逆に絶妙なフックとなっている\x01",
            "定番マスコットキャラですから。\x02\x03",

            "#00200F直球で可愛いとは言いがたいのも\x01",
            "当然といえば当然なわけです。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0157
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fなるほど……\x01",
            "何となく説得力があるような。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 43)
    Sleep(250)
    OP_68(205720, 1330, 125260, 2500)
    OP_6E(350, 2500)
    SetCameraDistance(22510, 2500)
    MoveCamera(45, 22, 0, 2500)
    TurnDirection(0x103, 0x101, 500)
    OP_6F(0x79)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0158
    ChrTalk(
        0x101,
        (
            "#00000Fそういえば、ティオとしては\x01",
            "みっしぃと、カゲマルの\x01",
            "どちらの方が好きなんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0159
    ChrTalk(
        0x103,
        (
            "#00203F……………………………………\x02\x03",

            "#00211F……聞いてしまいましたね？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#00011Fへ……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x103,
        (
            "#00203Fわたしが答えを出したくなくて\x01",
            "目を背けていた問題を……\x02\x03",

            "#00201Fとうとう聞いてしまいましたね？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#00012Fえ、あの、ティオさん……？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#00203Fこの件に関しては、夕食後にでも\x01",
            "じっくり語り合う事にしましょう。\x02\x03",

            "#00204F……ロイドさん。\x01",
            "今夜は熱くなりそうですね……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0164
    ChrTalk(
        0x101,
        (
            "#00006F（……読みたい本があったんだけど\x01",
            "  今日は諦めるしかなさそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23510, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0165
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの家具を全て揃えた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x103, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_69C5")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_69C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_69DE")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_69DE")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetMapObjFlags(0x15, 0x4)
    SetScenarioFlags(0x12C, 7)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_24(0x3AA)
    OP_24(0x3AB)
    EventEnd(0x6)
    NewScene("c0130", 110, 0, 0)
    IdleLoop()

    label("loc_6A0A")

    Return()

    # Function_46_584D end

    def Function_47_6A0B(): pass

    label("Function_47_6A0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A64")
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A36")
    Jump("Function_47_6A0B")

    label("loc_6A36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A4A")
    Jump("loc_6A64")

    label("loc_6A4A")

    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    Jump("Function_47_6A0B")

    label("loc_6A64")

    Return()

    # Function_47_6A0B end

    def Function_48_6A65(): pass

    label("Function_48_6A65")

    Sound(804, 0, 100, 0)
    Sleep(500)
    Sound(939, 2, 70, 0)
    Sleep(1000)
    Sound(73, 0, 100, 0)
    OP_24(0x3AB)
    Return()

    # Function_48_6A65 end

    def Function_49_6A81(): pass

    label("Function_49_6A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75FD")
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x109, 254080, 150, 127100, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6ADB")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_6ADB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6AF4")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_6AF4")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その日、ロイドたちは\x01",
            "支援業務の合間に支援課に戻り──\x02",
        )
    )

    CloseMessageWindow()

    #A0167
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本部との定時連絡を取りがてら\x01",
            "各自休憩を入れることにした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(254580, 1800, 125790, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(254580, 1300, 125790, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)

    #C0168
    ChrTalk(
        0x109,
        (
            "#10100Fえっと……\x01",
            "うん、こんな所かな？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 255880, 0, 119170, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    #N0169
    NpcTalk(
        0x101,
        "ロイドの声",
        "#1Pノエル、ちょっといいかな？\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x109, 0x1)
    Sleep(500)

    #C0170
    ChrTalk(
        0x109,
        (
            "#10100Fロイドさん？\x01",
            "はい、大丈夫です！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x109, 0x40)
    SetChrPos(0x109, 254580, 0, 126410, 180)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x4)
    OP_0D()
    OP_68(255330, 1300, 123600, 2500)
    SetCameraDistance(21000, 2500)
    BeginChrThread(0x109, 1, 0, 50)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_6D09():
        OP_9B(0x0, 0xFE, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D09)

    def lambda_6D1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6D1E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)
    Sleep(200)

    #C0171
    ChrTalk(
        0x109,
        "#10100Fそろそろ出かけますか？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00004Fああ、本部からの業務連絡も\x01",
            "今日は特に無かったからね。\x02\x03",

            "#00000Fまだみんな集まっていないから\x01",
            "そんなに急がなくてもいいけどさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x14A, 0x1F4)
    Sleep(200)
    OP_68(254560, 1300, 125250, 1500)
    SetCameraDistance(20000, 1500)
    OP_93(0x109, 0x14A, 0x1F4)
    OP_6F(0x79)
    Sleep(500)

    #C0173
    ChrTalk(
        0x101,
        "#00005Fあれ、報告書を書いてたのか？\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x109,
        (
            "#10109Fあはは……\x01",
            "一応、出向という形ですから。\x02\x03",

            "#10100Fソーニャ司令への報告書を\x01",
            "週に１回提出しているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        "#00009Fそっか、ご苦労様。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(255830, 1300, 124180, 3000)
    MoveCamera(59, 14, 0, 3000)
    OP_6E(450, 3000)
    SetCameraDistance(16500, 3000)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(200)
    OP_93(0x109, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(750)
    OP_6F(0x79)
    Sleep(500)

    #C0176
    ChrTalk(
        0x101,
        (
            "#00005F#4Pへえ……！\x01",
            "面白いものが増えてるな？\x02\x03",

            "#00000F自転車に……\x01",
            "これはレース用のフラッグか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x101, 500)

    #C0177
    ChrTalk(
        0x109,
        "#10102Fあ……分かりますか！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    #C0178
    ChrTalk(
        0x101,
        (
            "#00000F#4Pああ、俺も２年くらい\x01",
            "共和国で暮らしていたからね。\x02\x03",

            "#00004F向こうじゃこっちより\x01",
            "自転車をよく見かけたし……\x02\x03",

            "#00000F導力車を使ったレースなんかも\x01",
            "たまに開催されていたよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x109,
        (
            "#10109Fそうそう、そうなんです！\x02\x03",

            "#10104F……実は亡くなった父が\x01",
            "そういうのが大好きな人で。\x02\x03",

            "#10100F小さな頃、レースを見に\x01",
            "共和国に鉄道旅行に連れて行って\x01",
            "くれたことがあったんです。\x02\x03",

            "#10102F警備隊の仕事が忙しかったので\x01",
            "本当に１度だけでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00004F#4Pそっか……\x02\x03",

            "#00000Fじゃあ、ノエルの導力車好きは\x01",
            "その時からってわけだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        (
            "#10109Fあはは……ご明察です。\x02\x03",

            "#10100F休暇を貰えたら\x01",
            "ぜひまた導力車レースを\x01",
            "見に行きたいんですけど……\x02\x03",

            "#10106Fなかなかそんな暇ないですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#00009F#4Pはは、お互いにな。\x02\x03",

            "#00004F（ノエルなら見るだけじゃなくて\x01",
            "  レースに参加できそうだけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0183
    ChrTalk(
        0x101,
        (
            "#00003F#4Pレースの方はともかく……\x02\x03",

            "#00002F自転車の方で、\x01",
            "お勧めのモデルとかあったら\x01",
            "今度、教えてくれないかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0184
    ChrTalk(
        0x109,
        "#10105Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#00009F#4Pいや、向こうにいた時、\x01",
            "知り合った友達が乗っていて\x01",
            "ちょっと興味があったんだ。\x02\x03",

            "#00000F休日のサイクリングとかにも\x01",
            "付き合えると思うし、どうかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0186
    ChrTalk(
        0x109,
        (
            "#10100Fい、いいと思います！\x02\x03",

            "#10104F便利ですし、運動になりますし、\x01",
            "何よりも凄く楽しいですから！\x02\x03",

            "#10109F今度、実家に置いてある\x01",
            "カタログを持ってきますよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        "#00009F#4Pはは、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17100, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0188
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルの家具を全て揃えた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x109, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_75C6")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_75C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_75DF")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_75DF")

    OP_49()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 115, 0, 0)
    IdleLoop()

    label("loc_75FD")

    Return()

    # Function_49_6A81 end

    def Function_50_75FE(): pass

    label("Function_50_75FE")

    OP_95(0xFE, 255870, 0, 124760, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_50_75FE end

    def Function_51_761A(): pass

    label("Function_51_761A")

    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis342.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis343.itp")
    LoadChrToIndex("apl/ch51542.itc", 0x1E)
    LoadChrToIndex("apl/ch51216.itc", 0x1F)
    SoundLoad(3672)
    SoundLoad(3673)
    SoundLoad(3031)
    SoundLoad(3318)
    SoundLoad(3319)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 254100, 150, 71270, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_76CE")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_76CE")

    Sleep(1000)
    OP_68(254920, 1830, 70340, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(254920, 1330, 70340, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 251210, 0, 65690, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    #N0189
    NpcTalk(
        0x101,
        "ロイドの声",
        "#2Pキーア、ちょっといいか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x9, 0x1)
    Sleep(500)

    #C0190
    ChrTalk(
        0x9,
        (
            "#01100Fあ、ロイド！\x01",
            "いいよー。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(254320, 1330, 66480, 2000)
    MoveCamera(45, 23, 0, 2000)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_77EC():
        OP_9B(0x0, 0xFE, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77EC)

    def lambda_7801():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7801)
    BeginChrThread(0x9, 1, 0, 52)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x9, 500)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Sleep(500)

    #C0191
    ChrTalk(
        0x101,
        (
            "#00005Fおっと……\x01",
            "さっそく飾ったみたいだな。\x02\x03",

            "#00009Fうーん、こうして見ると\x01",
            "けっこう壮観だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "#01109Fえへへ……\x01",
            "みんなカワイイよね！\x02\x03",

            "#01111Fあ、でも……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_78D7():

        label("loc_78D7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_78D7")

    QueueWorkItem2(0x101, 1, lambda_78D7)
    OP_68(256450, 1300, 64640, 3000)
    MoveCamera(60, 22, 0, 3000)
    SetCameraDistance(20000, 3000)
    OP_93(0x9, 0x5A, 0x1F4)
    OP_95(0x9, 256810, 30, 66480, 2000, 0x1)
    OP_95(0x9, 258100, 0, 65290, 2000, 0x0)
    OP_93(0x9, 0xB4, 0x1F4)
    TurnDirection(0x9, 0x101, 500)
    Sleep(500)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)

    #C0193
    ChrTalk(
        0x9,
        (
            "#01110F#5Pこの子、ホントウは\x01",
            "ぬいぐるみじゃないんだってー。\x02\x03",

            "#01100F“きぐるみ”で、中に入れるって\x01",
            "せつめーしょに書いてたよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_79EC():

        label("loc_79EC")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_79EC")

    QueueWorkItem2(0x9, 1, lambda_79EC)
    BeginChrThread(0x101, 1, 0, 53)
    OP_68(257690, 1300, 64489, 2000)
    MoveCamera(60, 24, 0, 2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7A97")

    #C0194
    ChrTalk(
        0x101,
        (
            "#00005F#2P着ぐるみ……\x01",
            "みっしぃと同じアレか。\x02\x03",

            "#00003Fなるほど、キーアくらいの\x01",
            "子供なら入れそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B02")

    label("loc_7A97")


    #C0195
    ChrTalk(
        0x101,
        (
            "#00005F#2Pきぐるみ……\x01",
            "ああ、“着ぐるみ”か。\x02\x03",

            "#00003Fなるほど、キーアくらいの\x01",
            "子供なら入れそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B02")

    WaitChrThread(0x101, 1)
    EndChrThread(0x9, 0x1)
    OP_6F(0x79)

    #C0196
    ChrTalk(
        0x9,
        (
            "#01105Fあ、それじゃあ……\x02\x03",

            "#01109Fキーア、中に入ってみるから\x01",
            "手伝ってくれるー？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7BE8")

    #C0197
    ChrTalk(
        0x101,
        (
            "#00005F#2Pいいけど……\x01",
            "かなり暑いと思うぞ？\x02\x03",

            "#00012F前にみっしぃの代役をした時は\x01",
            "俺もヘロヘロになったし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C55")

    label("loc_7BE8")


    #C0198
    ChrTalk(
        0x101,
        (
            "#00005F#2Pいいけど……\x01",
            "かなり暑いと思うぞ？\x02\x03",

            "#00003Fこういうのは結構蒸すって\x01",
            "何かで読んだことがあるし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C55")


    #C0199
    ChrTalk(
        0x9,
        (
            "#01100Fんー、たぶんダイジョウブ。\x02\x03",

            "#01109Fそれにロイドに\x01",
            "見て欲しいだけだからー。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#00012F#2Pうっ……分かったよ。\x02\x03",

            "#00004F（うーん、末恐ろしいというか、\x01",
            "  将来大変なことになりそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    SetMapObjFlags(0x12, 0x4)
    Sleep(2000)
    OP_68(254670, 1330, 68760, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 255210, 30, 69560, 0)
    SetChrPos(0x101, 255340, 0, 68850, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(1000, 0, 100, 0)
    Sleep(1000)
    OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)
    Sleep(500)

    #C0201
    ChrTalk(
        0x101,
        (
            "#00004Fよし……これでいいぞ。\x02\x03",

            "#00000Fキーア、苦しくないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "うんっ、ヘイキー。\x02\x03",

            "スースーして\x01",
            "そんなに暑くないよー？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#00005Fへぇ……通気性とか\x01",
            "結構考えられてるのかな？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)
    Sleep(500)
    SetCameraDistance(20000, 500)
    TurnDirection(0x9, 0x101, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    #Sound(3031, 255, 100, 0)    #voice#KeA

    #N0204
    NpcTalk(
        0x9,
        "キーアペンギン",
        "じゃーん！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0205
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#5Sおおおっ！？\x02\x03",

            "#00009F#3Sな、なんていうか……\x01",
            "すさまじくカワイイな……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0xB, 255000, 0, 71000, 315)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)

    #N0206
    NpcTalk(
        0xB,
        "キーアペンギン",
        "#1Pえへへ、そうー？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 1, 0, 54)
    Fade(150)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Fade(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Fade(150)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Fade(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #N0207
    NpcTalk(
        0xB,
        "キーアペンギン",
        (
            "#1P#3672Vこんにちはなのです。\x02\x03",

            "#3673Vよろしくお願いするのです。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE59)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0208
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011Fおおっ……！\x01",
            "（これは凄い破壊力だ……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x103, 250000, 0, 64000, 90)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x103, 0x8)
    SetChrFlags(0x103, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8178")
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_8178")

    SetChrPos(0x102, 250000, 0, 64000, 90)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x102, 0x8)
    SetChrFlags(0x102, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_81B7")
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_81B7")


    #N0209
    NpcTalk(
        0x102,
        "エリィの声",
        "#2Pロイド、そこにいるの？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(253400, 1330, 66290, 1500)
    SetCameraDistance(22500, 1500)
    OP_93(0x101, 0xE1, 0x1F4)
    OP_6F(0x79)

    #N0210
    NpcTalk(
        0x103,
        "ティオの声",
        (
            "#2Pなかなか戻って来ないので\x01",
            "呼びに来たのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#00005Fあ、ああ、待たせてゴメン。\x02\x03",

            "#00004Fその……心の準備をしてから\x01",
            "中に入ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #N0212
    NpcTalk(
        0x102,
        "エリィの声",
        "#2P？？？\x02",
    )

    CloseMessageWindow()

    #N0213
    NpcTalk(
        0x103,
        "ティオの声",
        "#2P心の準備……ですか？\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x102, 251210, 0, 65690, 90)

    def lambda_831C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_831C)
    BeginChrThread(0x102, 1, 0, 55)
    Sleep(500)
    SetChrPos(0x103, 251210, 0, 65690, 90)

    def lambda_8347():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8347)
    BeginChrThread(0x103, 1, 0, 56)

    #C0214
    ChrTalk(
        0x102,
        "#00100F#2P一体どうしたの──\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0215
    ChrTalk(
        0x102,
        "#00105F#2Pへ……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x103,
        "#00205F#3P#N………………………（あんぐり）\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    #N0217
    NpcTalk(
        0x9,
        "キーアペンギン",
        (
            "あー、エリィとティオなのです。\x02\x03",

            "ごきげんいかがなのです。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8460():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8460)
    Sleep(20)

    def lambda_847C():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_847C)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(1000)

    #C0218
    ChrTalk(
        0x102,
        "#00105Fな#500W、#40Wな#500W、#40Wな……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0219
    ChrTalk(
        0x103,
        "#00201F#3P#N#5Sこれは事件です……！\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(254700, 1300, 68970, 1000)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x102, 1, 0, 59)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 60)
    Sleep(260)
    BeginChrThread(0x101, 1, 0, 62)
    OP_82(0x0, 0x64, 0xBB8, 0x64)
    Sound(811, 0, 100, 0)
    #Sound(3318, 255, 100, 0)    #voice#Lloyd

    #C0220
    ChrTalk(
        0x101,
        "#00011F#4P#10Aどわっ！\x02",
    )
    #Auto

    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(500)
    Sound(898, 0, 100, 0)

    def lambda_858C():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_858C)
    Sleep(20)

    def lambda_85A8():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_85A8)
    Sleep(20)

    def lambda_85C4():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_85C4)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)
    OP_6F(0x79)

    #C0221
    ChrTalk(
        0x102,
        (
            "#00114Fか、カワイイっ！\x01",
            "カワイイわキーアちゃん！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x103,
        (
            "#00204Fあ、ありえません……\x02\x03",

            "#00201Fこんなものがこの次元に\x01",
            "存在しえるはずが……！\x02",
        )
    )

    CloseMessageWindow()
    Sound(898, 0, 100, 0)

    def lambda_8689():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8689)
    Sleep(20)

    def lambda_86A5():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_86A5)
    Sleep(20)

    def lambda_86C1():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_86C1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)

    #N0223
    NpcTalk(
        0x9,
        "キーアペンギン",
        (
            "く、くるしいのです……\x02\x03",

            "そんなにだきしめないで\x01",
            "ほしいのです……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x13B, 0x0)
    OP_0D()
    Sleep(250)
    OP_95(0x101, 254940, 0, 68140, 2000, 0x0)
    TurnDirection(0x101, 0x9, 0)
    OP_68(253400, 1330, 66290, 2500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B13")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_87A3")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_87A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_87BC")
    ClearChrFlags(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_87BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_87D5")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_87D5")

    ClearChrFlags(0x109, 0x8)
    SetChrFlags(0x109, 0x40)
    SetChrPos(0x109, 251210, 0, 65690, 90)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8800():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8800)
    BeginChrThread(0x109, 1, 0, 57)
    Sleep(500)
    ClearChrFlags(0x104, 0x8)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x104, 251210, 0, 65690, 90)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8840():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8840)
    BeginChrThread(0x104, 1, 0, 58)
    Sleep(500)
    ClearChrFlags(0x105, 0x8)
    SetChrFlags(0x105, 0x40)
    SetChrPos(0x105, 251210, 0, 65690, 90)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8880():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8880)
    BeginChrThread(0x105, 1, 0, 56)

    #C0224
    ChrTalk(
        0x104,
        "#00305Fなに騒いでんだ──ってなんだぁ！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    OP_6F(0x79)

    #C0225
    ChrTalk(
        0x109,
        (
            "#10105F#12Pキ、キーアちゃん！？\x02\x03",

            "#10109Fうわあああああ～っ！\x01",
            "あたしも抱きしめさせてくださいっ！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 1, 0, 61)
    Sleep(200)
    BeginChrThread(0x101, 1, 0, 63)
    OP_82(0x0, 0x64, 0xBB8, 0x64)
    Sound(811, 0, 100, 0)
    #Sound(3319, 255, 100, 0)    #voice#Lloyd

    #C0226
    ChrTalk(
        0x101,
        "#00011F#4P#10Aあだっ！\x02",
    )
    #Auto

    WaitChrThread(0x109, 1)
    Sleep(500)
    Sound(898, 0, 100, 0)

    def lambda_89A0():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89A0)
    Sleep(20)

    def lambda_89BC():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_89BC)
    Sleep(20)

    def lambda_89D8():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_89D8)
    Sleep(20)

    def lambda_89F4():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_89F4)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_68(255000, 1330, 66890, 2000)
    BeginChrThread(0x104, 1, 0, 66)
    Sleep(200)
    BeginChrThread(0x105, 1, 0, 65)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0227
    ChrTalk(
        0x105,
        (
            "#10304F#6Pフフッ、災難だねぇ。\x02\x03",

            "#10309F確かにあり得ないくらい\x01",
            "凶悪な可愛さだとは思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x104,
        (
            "#00309F#6Pいや～！\x01",
            "マジで戦場に現れたら別の意味で\x01",
            "パニックになるんじゃねぇか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x104, 0x9, 500)
    TurnDirection(0x105, 0x9, 500)
    Jump("loc_8CB2")

    label("loc_8B13")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8B2C")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_8B2C")

    ClearChrFlags(0x104, 0x8)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x104, 251210, 0, 65690, 90)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8B57():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8B57)
    BeginChrThread(0x104, 1, 0, 56)
    Sleep(500)

    #C0229
    ChrTalk(
        0x104,
        "#00305Fなに騒いでんだ──ってなんだぁ！？\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(898, 0, 100, 0)

    def lambda_8BA8():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8BA8)
    Sleep(20)

    def lambda_8BC4():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8BC4)
    Sleep(20)

    def lambda_8BE0():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8BE0)
    OP_68(253160, 1330, 67480, 2000)
    OP_95(0x104, 253400, 0, 68000, 2000, 0x0)
    TurnDirection(0x104, 0x9, 500)
    Sleep(500)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0230
    ChrTalk(
        0x104,
        (
            "#00303F#6Pおいおい、あり得ないくらい\x01",
            "凶悪な可愛さだな……！？\x02\x03",

            "#00309Fマジで戦場に現れたら別の意味で\x01",
            "パニックになるんじゃねぇか！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CE0")
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(750)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    OP_0D()
    TurnDirection(0x101, 0x9, 500)
    Sleep(500)

    label("loc_8CE0")


    #C0231
    ChrTalk(
        0x101,
        (
            "#00012Fは、はは……\x01",
            "（シャレになってないかも……）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(254320, 1330, 68620, 2000)
    Sound(898, 0, 100, 0)

    def lambda_8D34():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D34)
    Sleep(20)

    def lambda_8D50():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D50)
    Sleep(20)

    def lambda_8D6C():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8D6C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DA6")
    Sleep(20)

    def lambda_8D92():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8D92)

    label("loc_8DA6")

    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DC0")
    WaitChrThread(0x109, 1)

    label("loc_8DC0")

    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(200)

    #N0232
    NpcTalk(
        0x9,
        "キーアペンギン",
        (
            "あうう～……\x01",
            "こうさんなのです……\x02\x03",

            "そろそろゆるしてほしいのです……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2500)
    FadeToDark(2000, 0, -1)
    Sound(898, 0, 100, 0)

    def lambda_8E50():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E50)
    Sleep(20)

    def lambda_8E6C():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8E6C)
    Sleep(20)

    def lambda_8E88():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E88)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EC2")
    Sleep(20)

    def lambda_8EAE():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8EAE)

    label("loc_8EC2")

    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EDC")
    WaitChrThread(0x109, 1)

    label("loc_8EDC")

    OP_0D()
    OP_64(0x9)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──その後、女性陣たちは\x01",
            "しばらくしてようやく我に返り……\x02",
        )
    )

    CloseMessageWindow()

    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あまりの危険さゆえに、キーアペンギンは\x01",
            "以後厳禁というルールとなるのだった。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キーアに全てのぬいぐるみを贈った！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8FFB")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_8FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9014")
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_9014")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_902D")
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_902D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9046")
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_9046")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_905F")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_905F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9078")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_9078")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetScenarioFlags(0x12D, 4)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_51_761A end

    def Function_52_909F(): pass

    label("Function_52_909F")

    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    Sound(812, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x1F4, 0xBB8)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0x9, 0x1)
    OP_95(0xFE, 253820, 30, 66880, 2000, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_909F end

    def Function_53_90EE(): pass

    label("Function_53_90EE")

    OP_95(0xFE, 255000, 30, 64379, 2000, 0x1)
    OP_95(0xFE, 256640, 30, 64000, 2000, 0x0)
    Return()

    # Function_53_90EE end

    def Function_54_9117(): pass

    label("Function_54_9117")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91B5")
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)

    label("loc_913E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9155")
    Sleep(150)
    Jump("loc_913E")

    label("loc_9155")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9169")
    Jump("loc_91B5")

    label("loc_9169")

    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)

    label("loc_9185")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_919C")
    Sleep(150)
    Jump("loc_9185")

    label("loc_919C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91B0")
    Jump("loc_91B5")

    label("loc_91B0")

    Jump("Function_54_9117")

    label("loc_91B5")

    Return()

    # Function_54_9117 end

    def Function_55_91B6(): pass

    label("Function_55_91B6")

    OP_9B(0x0, 0xFE, 0x0, 0xA28, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_55_91B6 end

    def Function_56_91CD(): pass

    label("Function_56_91CD")

    OP_9B(0x0, 0xFE, 0x0, 0x640, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_56_91CD end

    def Function_57_91E4(): pass

    label("Function_57_91E4")

    OP_9B(0x0, 0xFE, 0xFFF6, 0xBB8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_57_91E4 end

    def Function_58_91FB(): pass

    label("Function_58_91FB")

    OP_9B(0x0, 0xFE, 0xA, 0xBB8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_58_91FB end

    def Function_59_9212(): pass

    label("Function_59_9212")

    OP_95(0xFE, 255390, 30, 69100, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_59_9212 end

    def Function_60_922E(): pass

    label("Function_60_922E")

    OP_95(0xFE, 254730, 30, 69610, 5000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Return()

    # Function_60_922E end

    def Function_61_924A(): pass

    label("Function_61_924A")

    OP_95(0xFE, 254620, 30, 68940, 5000, 0x0)
    OP_93(0xFE, 0x2D, 0x0)
    Return()

    # Function_61_924A end

    def Function_62_9266(): pass

    label("Function_62_9266")

    SetChrChipByIndex(0xFE, 0xFF)

    def lambda_926F():
        OP_9D(0xFE, 0x3E800, 0x0, 0x1084C, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_926F)
    BeginChrThread(0xFE, 3, 0, 64)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_62_9266 end

    def Function_63_92A5(): pass

    label("Function_63_92A5")

    SetChrChipByIndex(0xFE, 0xFF)

    def lambda_92AE():
        OP_9D(0xFE, 0x3E8C8, 0x0, 0x109DC, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_92AE)
    BeginChrThread(0xFE, 3, 0, 64)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_63_92A5 end

    def Function_64_92EB(): pass

    label("Function_64_92EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9317")
    OP_93(0xFE, 0x10E, 0x3E8)
    OP_93(0xFE, 0x0, 0x3E8)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_93(0xFE, 0xB4, 0x3E8)
    Jump("Function_64_92EB")

    label("loc_9317")

    Return()

    # Function_64_92EB end

    def Function_65_9318(): pass

    label("Function_65_9318")

    OP_95(0xFE, 254750, 30, 67380, 2000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_65_9318 end

    def Function_66_9334(): pass

    label("Function_66_9334")

    OP_95(0xFE, 254770, 30, 66380, 2000, 0x1)
    OP_95(0xFE, 255780, 30, 66850, 2000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_66_9334 end

    def Function_67_9364(): pass

    label("Function_67_9364")

    OP_95(0xFE, 254550, 30, 67480, 2000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_67_9364 end

    def Function_68_9380(): pass

    label("Function_68_9380")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(3657)
    SoundLoad(3039)
    SoundLoad(3660)
    AddParty(0x52, 0xFF, 0xFF)
    LoadChrToIndex("apl/ch51100.itc", 0x1E)
    OP_68(253500, 1100, 71300, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 251000, 0, 66000, 90)
    SetChrPos(0x102, 251000, 0, 66000, 90)
    SetChrPos(0x109, 251000, 0, 66000, 90)
    SetChrPos(0x105, 251000, 0, 66000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x153, 0x4)
    SetChrPos(0x153, 254100, 200, 71300, 270)
    SetChrChipByIndex(0x153, 0x1)
    SetChrSubChip(0x153, 0x0)
    SetCameraDistance(22000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0236
    ChrTalk(
        0x153,
        (
            "#01111F#3657V#11P#40Wえっと、この数式に\x01",
            "この値を代入すれば……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE49)
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x153)
    OP_63(0x153, 0x0, 1700, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0237
    ChrTalk(
        0x153,
        "#01109F#3039V#11P#30W#4S──うん！　できたぁ！\x02",
    )

    CloseMessageWindow()
    OP_24(0xBDF)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    Sound(808, 0, 100, 0)
    Sleep(1000)

    #N0238
    NpcTalk(
        0x101,
        "ロイドの声",
        "キーア？\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x153, 0x1)
    Sound(103, 0, 100, 0)
    OP_68(254000, 1100, 69900, 3000)
    MoveCamera(45, 23, 0, 3000)
    SetCameraDistance(23000, 3000)
    BeginChrThread(0x101, 3, 0, 69)
    BeginChrThread(0x102, 3, 0, 70)
    BeginChrThread(0x109, 3, 0, 71)
    BeginChrThread(0x105, 3, 0, 72)
    OP_C9(0x0, 0x80000000)

    #C0239
    ChrTalk(
        0x153,
        "#01110F#3660V#5P#15A#30Wあ、ロイドー。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)

    #C0240
    ChrTalk(
        0x101,
        (
            "#00005F#11Pキーア、確か今日は\x01",
            "日曜学校があったはずだろう？\x02\x03",

            "#00000F出かけなくてもいいのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x153,
        (
            "#01105F#5Pあ、うん。\x01",
            "もう待ち合わせの時間かも。\x02\x03",

            "#01100Fみんなもお仕事に出るの？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)

    #C0242
    ChrTalk(
        0x102,
        (
            "#12P#00109Fええ、よかったら\x01",
            "一緒に出かけようと思って。\x02\x03",

            "#00105Fあら……\x01",
            "日曜学校の予習をしてたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x153,
        "#01109F#5Pえへへ、そんなとこ。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x109,
        (
            "#10102F#12Pキーアちゃん、偉いなぁ。\x02\x03",

            "#10106F日曜学校の予習なんて\x01",
            "あたしは殆んどしなかったかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、僕はどちらかというと\x01",
            "ほとんど授業に出なかったかな。\x02\x03",

            "#10302F下手な神父に教えられるより\x01",
            "自分で勉強した方が効率いいしね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_984F():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_984F)
    Sleep(150)

    def lambda_985F():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_985F)
    Sleep(150)

    def lambda_986F():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_986F)
    Sleep(150)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    def lambda_988B():

        label("loc_988B")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_988B")

    QueueWorkItem2(0x101, 2, lambda_988B)

    def lambda_989D():

        label("loc_989D")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_989D")

    QueueWorkItem2(0x102, 2, lambda_989D)

    def lambda_98AF():

        label("loc_98AF")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_98AF")

    QueueWorkItem2(0x109, 2, lambda_98AF)

    #C0246
    ChrTalk(
        0x101,
        "#5P#00001Fワジ、あのなぁ……\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        (
            "#00111F#11Pキーアちゃんに悪影響を\x01",
            "与えないで欲しいのだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x153,
        "#01100F#5Pほえ～？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、パパたちがお怒りだ。\x02\x03",

            "#10305F……あれ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_997C():
        OP_95(0xFE, 253000, 30, 69300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_997C)
    WaitChrThread(0x105, 1)
    Sleep(300)

    #C0250
    ChrTalk(
        0x105,
        "#6P#10301F………………………………\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        "#00005F#11Pワジ？\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x153,
        "#01105F#5Pんー、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、さすがクロスベルは\x01",
            "色々進んでいるなと思ってさ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0254
    ChrTalk(
        0x105,
        "#6P#10300Fそれより出かけないのかい？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)

    #C0255
    ChrTalk(
        0x101,
        "#00000F#11Pそうだな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    def lambda_9AA5():

        label("loc_9AA5")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9AA5")

    QueueWorkItem2(0x101, 2, lambda_9AA5)
    Sleep(150)

    #C0256
    ChrTalk(
        0x101,
        "#00000F#11Pキーア、一緒に出るか？\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x153,
        (
            "#01109F#5Pうんっ！\x01",
            "ちょっと待ってて！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_9B0F():

        label("loc_9B0F")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9B0F")

    QueueWorkItem2(0x105, 2, lambda_9B0F)

    def lambda_9B21():

        label("loc_9B21")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9B21")

    QueueWorkItem2(0x102, 2, lambda_9B21)

    def lambda_9B33():

        label("loc_9B33")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_9B33")

    QueueWorkItem2(0x109, 2, lambda_9B33)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    Sound(802, 0, 100, 0)
    OP_68(255000, 1100, 69700, 3000)
    OP_9D(0x153, 0x3E0F8, 0x0, 0x11940, 0x12C, 0xBB8)
    ClearChrFlags(0x153, 0x4)
    OP_93(0x153, 0x2D, 0x1F4)

    def lambda_9B87():
        OP_95(0xFE, 255700, 0, 72800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_9B87)
    WaitChrThread(0x153, 1)
    OP_93(0x153, 0x0, 0x1F4)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x153, 0x1E)
    SetChrSubChip(0x153, 0x0)
    OP_0D()
    OP_93(0x153, 0xB4, 0x1F4)
    SetChrFlags(0x153, 0x1000)

    def lambda_9BC9():
        OP_95(0xFE, 255700, 30, 70400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_9BC9)
    WaitChrThread(0x153, 1)
    ClearChrFlags(0x153, 0x1000)
    OP_93(0x153, 0xE1, 0x1F4)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    OP_6F(0x79)

    #C0258
    ChrTalk(
        0x153,
        "#5P#01110Fうん、お待たせー！\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        "#6P#00002Fよし、それじゃあ行くか。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#12P#00102Fキーアちゃんと一緒なら\x01",
            "裏口から出ましょうか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    OP_D7(0x1E)
    RemoveParty(0x52, 0xFF)
    AddParty(0xA4, 0xFF, 0xFF)
    SetChrPos(0x0, 254700, 30, 69400, 225)
    SetScenarioFlags(0x126, 2)
    EventEnd(0x5)
    Return()

    # Function_68_9380 end

    def Function_69_9CBC(): pass

    label("Function_69_9CBC")


    def lambda_9CC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9CC1)

    def lambda_9CD2():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CD2)
    WaitChrThread(0xFE, 1)

    def lambda_9CF0():
        OP_95(0xFE, 254000, 0, 69300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CF0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_69_9CBC end

    def Function_70_9D11(): pass

    label("Function_70_9D11")

    Sleep(700)

    def lambda_9D19():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9D19)

    def lambda_9D2A():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D2A)
    WaitChrThread(0xFE, 1)

    def lambda_9D48():
        OP_95(0xFE, 254300, 0, 68300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D48)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_70_9D11 end

    def Function_71_9D69(): pass

    label("Function_71_9D69")

    Sleep(1400)

    def lambda_9D71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9D71)

    def lambda_9D82():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D82)
    WaitChrThread(0xFE, 1)

    def lambda_9DA0():
        OP_95(0xFE, 255100, 0, 67900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DA0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_71_9D69 end

    def Function_72_9DC1(): pass

    label("Function_72_9DC1")

    Sleep(2100)

    def lambda_9DC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9DC9)

    def lambda_9DDA():
        OP_95(0xFE, 253000, 0, 66000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DDA)
    WaitChrThread(0xFE, 1)

    def lambda_9DF8():
        OP_95(0xFE, 253100, 0, 67900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DF8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_72_9DC1 end

    def Function_73_9E19(): pass

    label("Function_73_9E19")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(-2250, 1100, 67800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -2000, 10, 69500, 180)
    SetChrPos(0x102, -2000, 10, 68300, 270)
    SetChrPos(0x104, -1000, 0, 68300, 270)
    SetChrPos(0x109, -2500, 10, 67300, 270)
    SetChrPos(0x105, -1500, 10, 67300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_9EFC():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9EFC)
    Sleep(200)

    def lambda_9F19():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9F19)
    Sleep(200)

    def lambda_9F36():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9F36)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_9F71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9F71)
    Sleep(400)

    def lambda_9F85():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9F85)
    Sleep(400)

    def lambda_9F99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9F99)

    def lambda_9FAA():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9FAA)
    Sleep(300)

    def lambda_9FC7():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FC7)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    #C0261
    ChrTalk(
        0x101,
        "#00003F#11P──なあ、ランディ。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0262
    AnonymousTalk(
        0x104,
        "ん？　なんだロイド。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0263
    ChrTalk(
        0x101,
        (
            "#00008F#11Pその……\x01",
            "お父さんのことだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0264
    ChrTalk(
        0x104,
        (
            "#6P#00306Fああ、それか……\x02\x03",

            "#00300F別に気にすることはねぇぜ？\x01",
            "あの世界じゃ珍しくもねぇ話だ。\x02\x03",

            "それに、団を抜けた時に\x01",
            "俺と親父は縁を切っている。\x02\x03",

            "#00304F何も感じないわけじゃねぇが……\x01",
            "ま、サバサバしたもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        (
            "#00006F#11P……そっか。\x02\x03",

            "#00001Fでも、気が向いたら\x01",
            "色々と聞かせてくれよな？\x02\x03",

            "一応、リーダーとして\x01",
            "相談に乗れることがあるかも\x01",
            "しれないしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#6P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#00011F#11Pあ、ゴメン。\x01",
            "ちょっと生意気だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x104,
        (
            "#6P#00304Fハハ、違う違う。\x02\x03",

            "#00302F何だかんだ言って\x01",
            "お前も成長してると思ってな。\x02\x03",

            "#00309Fうーん、お兄さん感慨深いぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_A527")

    #C0269
    ChrTalk(
        0x101,
        "#00006F#11Pあのな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0270
    ChrTalk(
        0x101,
        (
            "#00008F#11P……その、こういう時は\x01",
            "何とか力にならせて欲しいんだ。\x02\x03",

            "#00000F頼りないかもしれないけど\x01",
            "それが“相棒”ってもんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x104,
        "#6P#00305Fロイド……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_A446():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A446)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x101, 0x7)
    Sound(811, 0, 30, 0)
    Sleep(300)

    #C0272
    ChrTalk(
        0x104,
        (
            "#6P#00302F……分かった、いずれ話を\x01",
            "聞いてもらうかもしれねぇ。\x02\x03",

            "#00309Fそん時は頼むぜ──相棒。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        "#00002F#11Pああ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_A5B9")

    label("loc_A527")


    #C0274
    ChrTalk(
        0x101,
        "#00006F#11Pあのな……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x104,
        (
            "#6P#00304F……ま、気が向いたら\x01",
            "相談するかもしれねぇ。\x02\x03",

            "#00300Fそん時はよろしく頼むぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        "#00000F#11Pああ……！\x02",
    )

    CloseMessageWindow()

    label("loc_A5B9")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    #N0277
    NpcTalk(
        0x105,
        "ワジの声",
        "#2P#2Sあれ、何してるの？\x02",
    )

    CloseMessageWindow()

    #N0278
    NpcTalk(
        0x102,
        "エリィの声",
        "#2P#2S２人とも、忘れ物？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_A6B0")
    SetCameraDistance(22500, 700)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_A697():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A697)
    WaitChrThread(0x104, 1)

    label("loc_A6B0")


    def lambda_A6B5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A6B5)

    #C0279
    ChrTalk(
        0x101,
        "#00011F#11Pゴメン、すぐ行く！\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#11P#00304Fそんじゃあボチボチ、\x01",
            "お仕事を始めるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_A729():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A729)
    Sleep(100)

    def lambda_A746():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A746)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_A76D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A76D)
    Sleep(400)

    def lambda_A781():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A781)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0281
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力車で、クロスベル全土に\x01",
            "移動することが可能になりました。\x02\x03",

            "西通りに出る特務支援課の裏口に\x01",
            "停めてあるので活用してみてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0200", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_73_9E19 end

    def Function_74_A88D(): pass

    label("Function_74_A88D")

    EventBegin(0x0)
    Fade(500)
    OP_68(256290, 1300, 67750, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22450, 0)
    SetChrPos(0x101, 255980, 0, 68000, 90)
    SetChrPos(0x102, 255700, 30, 68900, 90)
    SetChrPos(0x103, 255360, 0, 67250, 90)
    SetChrPos(0x104, 254500, 0, 68200, 90)
    SetChrPos(0x109, 253700, 30, 68850, 90)
    SetChrPos(0x105, 253800, 0, 67250, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0282
    ChrTalk(
        0x8,
        "#11P#01100Fいってらっしゃい、みんなー。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x109,
        (
            "#6P#10109Fふふ、行ってくるねキーアちゃん。\x02\x03",

            "#10106F……こうしてキーアちゃんに\x01",
            "『いってらっしゃい』を言われることも\x01",
            "しばらくは無くなるんですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        "#12P#00002Fはは……やっぱり寂しくなるよな。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x102,
        (
            "#00106Fキーアちゃんと離れるなんて、\x01",
            "想像しただけでも耐えられないものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "#11P#01100Fノエルがいなくなっちゃったら\x01",
            "キーアもサビしいけど……\x01",
            "元気出してね、ノエルー。\x02\x03",

            "#01109F元気になったフランと\x01",
            "２人で遊びにくるのを待ってるからー。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x109,
        "#6P#10102Fうん、ありがとうキーアちゃん。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x104,
        (
            "#00302Fハハ、ノエル。\x01",
            "こうなったら警備隊の再編を\x01",
            "とっとと片付けてこねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x103,
        (
            "#12P#00202Fフランさんにも一刻も早く\x01",
            "回復してもらわないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x109,
        (
            "#6P#10109Fふふ、そうだね。\x02\x03",

            "#10100Fキーアちゃんの笑顔に\x01",
            "一日も早く再会するためにも！\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x105,
        "#12P#10302Fやれやれ、燃えてるねえ。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        "#11P#01102Fえへへ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x19D, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 255700, 0, 68570, 90)
    EventEnd(0x5)
    Return()

    # Function_74_A88D end

    SaveToFile()

Try(main)
