from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0110.bin",                # FileName
        "c0110",                    # MapName
        "c0110",                    # Location
        0x0009,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0110",                  # 0
        "赛尔盖科长",             # 1
        "琪雅",                   # 2
        "蔡特",                   # 3
        "塞茜尔",                 # 4
        "柯贝",                   # 5
        "猫食",                   # 6
        "格蕾丝的声音",           # 7
        "餐具",                   # 8
        "餐具",                   # 9
        "餐具",                   # 10
        "餐具",                   # 11
        "餐具",                   # 12
        "餐具",                   # 13
        "餐具",                   # 14
        "餐具",                   # 15
        "餐具",                   # 16
        "餐具",                   # 17
        "餐具",                   # 18
        "餐具",                   # 19
        "餐具",                   # 20
        "餐具",                   # 21
        "餐具",                   # 22
        "餐具",                   # 23
        "餐具",                   # 24
        "餐具",                   # 25
        "餐具",                   # 26
        "椅子",                   # 27
        "椅子",                   # 28
        "椅子",                   # 29
        "椅子",                   # 30
        "椅子",                   # 31
        "椅子",                   # 32
        "椅子",                   # 33
        "椅子",                   # 34
        "幻兽调查报告",           # 35
        "模型",                   # 36
        "人偶",                   # 37
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch08200.itc",                   # 02
        "chr/ch08202.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch02708.itc",                   # 05
        "chr/ch02702.itc",                   # 06
        "chr/ch14300.itc",                   # 07
        "chr/ch39200.itc",                   # 08
        "apl/ch50092.itc",                   # 09
        "chr/ch14302.itc",                   # 0A
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

    DeclNpc(64000,   200,     11399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(2710,    0,       2509,    225,  405,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    438,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 13,  1.0,                   -0.5,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.5,                  0.25,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 14,  -3.299999952316284,    68.0,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.649999976158142,     -34.0,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 64,  7.0,                   10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -3.5,                  -2.0999999046325684,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 65,  11.0,                  13.5,                  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.5,                  -6.75,                 -0.0,                  1.0])
    DeclEvent(0x0000, 0, 66,  19.0,                  4.0,                   0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -9.5,                  -2.0,                  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 15,  1.0,                   71.5,                  0.0,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.5,                  -23.83333396911621,    -0.0,                  1.0])

    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  18, 0x0000)
    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  12, 0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  11, 0x0000)
    DeclActor(64000,   30,      9800,    1500,    64000,   1500,    11400,   0x007E, 0,  4,  0x0000)
    DeclActor(63890,   30,      11070,   1500,    63890,   1000,    11070,   0x007C, 0,  63, 0x0000)

    ChipFrameInfo(2332, 0)                                       # 0

    ScpFunction((
        "Function_0_928",          # 00, 0
        "Function_1_9D8",          # 01, 1
        "Function_2_A03",          # 02, 2
        "Function_3_10AE",         # 03, 3
        "Function_4_139F",         # 04, 4
        "Function_5_13A3",         # 05, 5
        "Function_6_2363",         # 06, 6
        "Function_7_2CDC",         # 07, 7
        "Function_8_373B",         # 08, 8
        "Function_9_384E",         # 09, 9
        "Function_10_3A06",        # 0A, 10
        "Function_11_3D8B",        # 0B, 11
        "Function_12_3DD6",        # 0C, 12
        "Function_13_3E21",        # 0D, 13
        "Function_14_3EC2",        # 0E, 14
        "Function_15_3F63",        # 0F, 15
        "Function_16_3FB2",        # 10, 16
        "Function_17_4271",        # 11, 17
        "Function_18_44EF",        # 12, 18
        "Function_19_4E89",        # 13, 19
        "Function_20_520C",        # 14, 20
        "Function_21_5399",        # 15, 21
        "Function_22_5DB8",        # 16, 22
        "Function_23_6827",        # 17, 23
        "Function_24_70FA",        # 18, 24
        "Function_25_863F",        # 19, 25
        "Function_26_8663",        # 1A, 26
        "Function_27_8EA3",        # 1B, 27
        "Function_28_914E",        # 1C, 28
        "Function_29_A95E",        # 1D, 29
        "Function_30_B374",        # 1E, 30
        "Function_31_BD98",        # 1F, 31
        "Function_32_D478",        # 20, 32
        "Function_33_D8D0",        # 21, 33
        "Function_34_ED92",        # 22, 34
        "Function_35_EE21",        # 23, 35
        "Function_36_F6AE",        # 24, 36
        "Function_37_F6EB",        # 25, 37
        "Function_38_102ED",       # 26, 38
        "Function_39_10987",       # 27, 39
        "Function_40_10DB5",       # 28, 40
        "Function_41_12674",       # 29, 41
        "Function_42_129AF",       # 2A, 42
        "Function_43_1454B",       # 2B, 43
        "Function_44_15405",       # 2C, 44
        "Function_45_159FC",       # 2D, 45
        "Function_46_175DD",       # 2E, 46
        "Function_47_17627",       # 2F, 47
        "Function_48_1767C",       # 30, 48
        "Function_49_176B3",       # 31, 49
        "Function_50_176F7",       # 32, 50
        "Function_51_1773B",       # 33, 51
        "Function_52_17773",       # 34, 52
        "Function_53_177A3",       # 35, 53
        "Function_54_1873B",       # 36, 54
        "Function_55_1878C",       # 37, 55
        "Function_56_191D3",       # 38, 56
        "Function_57_19245",       # 39, 57
        "Function_58_1A10A",       # 3A, 58
        "Function_59_1A18E",       # 3B, 59
        "Function_60_1A1CB",       # 3C, 60
        "Function_61_1A208",       # 3D, 61
        "Function_62_1A26A",       # 3E, 62
        "Function_63_1A398",       # 3F, 63
        "Function_64_1AC27",       # 40, 64
        "Function_65_1AC74",       # 41, 65
        "Function_66_1ACC1",       # 42, 66
        "Function_67_1AD0E",       # 43, 67
    ))


    def Function_0_928(): pass

    label("Function_0_928")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_960"),
        (1, "loc_96C"),
        (2, "loc_978"),
        (3, "loc_984"),
        (4, "loc_990"),
        (5, "loc_99C"),
        (6, "loc_9A8"),
        (SWITCH_DEFAULT, "loc_9B4"),
    )


    label("loc_960")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9C0")

    label("loc_96C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9C0")

    label("loc_978")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9C0")

    label("loc_984")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9C0")

    label("loc_990")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9C0")

    label("loc_99C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9C0")

    label("loc_9A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C0")

    label("loc_9B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C0")

    label("loc_9C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C0")

    label("loc_9D7")

    Return()

    # Function_0_928 end

    def Function_1_9D8(): pass

    label("Function_1_9D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A02")
    OP_94(0xFE, 0x1D8DA, 0x1F18, 0x1E53C, 0x1360, 0x3E8)
    Sleep(300)
    Jump("Function_1_9D8")

    label("loc_A02")

    Return()

    # Function_1_9D8 end

    def Function_2_A03(): pass

    label("Function_2_A03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE1")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3B")
    Jump("loc_ADC")

    label("loc_A3B")

    SetChrPos(0x0, -2190, 0, 68010, 90)
    SetChrPos(0x1, -2190, 0, 68010, 90)
    SetChrPos(0x2, -2190, 0, 68010, 90)
    SetChrPos(0x3, -2190, 0, 68010, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB4")
    SetChrPos(0x4, -2190, 0, 68010, 90)
    SetChrPos(0x5, -2190, 0, 68010, 90)
    Jump("loc_AD3")

    label("loc_AB4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD3")
    SetChrPos(0x4, -2190, 0, 68010, 90)

    label("loc_AD3")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ADC")

    Jump("loc_AE1")

    label("loc_AE1")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AFD")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F48")

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B41")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 122700, 0, 6000, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 121800, 0, 6000, 0)
    Jump("loc_F48")

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B54")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F48")

    label("loc_B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BCF")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x9, 5570, 150, 6230, 180)
    SetChrChipByIndex(0xA, 0x5)
    SetChrPos(0xA, 3470, 30, 6380, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0xA)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 5450, 150, 2100, 0)
    Jump("loc_F48")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BEE")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_F48")

    label("loc_BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_C23")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3470, 30, 6380, 180)
    Jump("loc_F48")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C7F")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x9, 5570, 150, 6230, 180)
    SetChrPos(0xA, 3470, 30, 6380, 180)
    Jump("loc_F48")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CE0")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 117660, 30, 8100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 117430, 30, 4080, 90)
    Jump("loc_F48")

    label("loc_CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D19")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x5)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F48")

    label("loc_D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D4E")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F48")

    label("loc_D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D77")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F48")

    label("loc_D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D8A")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F48")

    label("loc_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_DE6")
    SetChrPos(0x8, 14400, 850, 12500, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x9, 5570, 150, 6230, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F48")

    label("loc_DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_E31")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 117660, 30, 8100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
    Jump("loc_F48")

    label("loc_E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_E7C")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 123270, 0, 4980, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
    Jump("loc_F48")

    label("loc_E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EB1")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F48")

    label("loc_EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EE9")
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE4")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 65890, 0, 1800, 225)

    label("loc_EE4")

    Jump("loc_F48")

    label("loc_EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F3A")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 122060, 0, 5750, 45)
    BeginChrThread(0xC, 0, 0, 1)
    Jump("loc_F48")

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F48")
    SetChrFlags(0x8, 0x80)

    label("loc_F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F5C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)
    Jump("loc_106F")

    label("loc_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F6D")
    ClearScenarioFlags(0x22, 1)
    Jump("loc_106F")

    label("loc_F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_F81")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)
    Jump("loc_106F")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_F92")
    Event(0, 28)
    Jump("loc_106F")

    label("loc_F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_FA6")
    ClearScenarioFlags(0x22, 4)
    Event(0, 31)
    Jump("loc_106F")

    label("loc_FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_FBD")
    ClearScenarioFlags(0x22, 5)
    SetScenarioFlags(0x0, 7)
    Event(0, 35)
    Jump("loc_106F")

    label("loc_FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_FCE")
    Event(0, 37)
    Jump("loc_106F")

    label("loc_FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_FE5")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x0, 7)
    Event(0, 38)
    Jump("loc_106F")

    label("loc_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_FF9")
    ClearScenarioFlags(0x23, 0)
    Event(0, 40)
    Jump("loc_106F")

    label("loc_FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_100D")
    ClearScenarioFlags(0x23, 1)
    Event(0, 42)
    Jump("loc_106F")

    label("loc_100D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_101E")
    ClearScenarioFlags(0x23, 2)
    Jump("loc_106F")

    label("loc_101E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_1032")
    ClearScenarioFlags(0x23, 3)
    Event(0, 43)
    Jump("loc_106F")

    label("loc_1032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_1049")
    ClearScenarioFlags(0x23, 4)
    SetScenarioFlags(0x0, 7)
    Event(0, 45)
    Jump("loc_106F")

    label("loc_1049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_1060")
    ClearScenarioFlags(0x23, 5)
    SetScenarioFlags(0x0, 7)
    Event(0, 53)
    Jump("loc_106F")

    label("loc_1060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_106F")
    ClearScenarioFlags(0x23, 6)
    Event(0, 55)

    label("loc_106F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1097")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_1097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10AD")
    SetMapFlags(0x10000000)
    Event(0, 57)

    label("loc_10AD")

    Return()

    # Function_2_A03 end

    def Function_3_10AE(): pass

    label("Function_3_10AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_10C3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)

    label("loc_10C3")

    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10FC")
    OP_1B(0x0, 0x0, 0x1D)
    OP_1B(0x8, 0x0, 0x1E)

    label("loc_10FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1150")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_119A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BB")
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)

    label("loc_11BB")

    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11DE")
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    Jump("loc_11ED")

    label("loc_11DE")

    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_11ED")

    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_120C")
    SetMapObjFlags(0x3, 0x10)
    OP_65(0x1, 0x1)

    label("loc_120C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_121F")
    SetMapObjFlags(0x6, 0x10)
    OP_65(0x2, 0x1)

    label("loc_121F")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1231")
    Jump("loc_1334")

    label("loc_1231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_123F")
    Jump("loc_1334")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1251")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_1251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_1263")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_1263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1275")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_1275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1287")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_1287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1299")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_1299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12AB")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_12AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_12B9")
    Jump("loc_1334")

    label("loc_12B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_12C7")
    Jump("loc_1334")

    label("loc_12C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_12D5")
    Jump("loc_1334")

    label("loc_12D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_12E7")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_12E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_12F9")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_12F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_130B")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_130B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1319")
    Jump("loc_1334")

    label("loc_1319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_132B")
    OP_66(0x3, 0x1)
    Jump("loc_1334")

    label("loc_132B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1334")

    label("loc_1334")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1361")
    OP_66(0x4, 0x1)

    label("loc_1361")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1383")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1383")

    ModifyEventFlags(0, 5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_139B")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_139B")

    Call(0, 67)
    Return()

    # Function_3_10AE end

    def Function_4_139F(): pass

    label("Function_4_139F")

    Call(0, 5)
    Return()

    # Function_4_139F end

    def Function_5_13A3(): pass

    label("Function_5_13A3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_13B4")
    Jump("loc_235F")

    label("loc_13B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1548")

    #C0001
    ChrTalk(
        0x8,
        (
            "#01000F关于诺艾尔回警备队复职这件事，\x01",
            "就由我来办理必要的手续吧。\x02\x03",

            "由于袭击事件造成的影响，\x01",
            "各地一定提出了不少支援请求，\x01",
            "如果有时间，你们就把那些任务处理一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x109,
        (
            "#10100F好的，今天一整天，\x01",
            "我都会竭尽全力去工作的。\x02\x03",

            "#10103F……赛尔盖科长，\x01",
            "多谢您一直以来对我的照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#01004F呵呵，不用道谢。\x02\x03",

            "#01002F别给自己留下任何遗憾。集中精力，\x01",
            "尽量为工作画上一个完美的句号吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_15C8")

    label("loc_1548")


    #C0004
    ChrTalk(
        0x8,
        (
            "#01000F关于诺艾尔回警备队复职这件事，\x01",
            "就由我来办理必要的手续吧。\x02\x03",

            "#01004F今晚我请客，大家一起去外面吃饭，\x01",
            "记得准时回来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C8")

    Jump("loc_235F")

    label("loc_15CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_171F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1698")

    #C0005
    ChrTalk(
        0x8,
        (
            "#01003F终于掌握兰迪的行踪了吗。\x02\x03",

            "#01002F呵呵，这样一来，\x01",
            "准备工作总算是做好了。\x02\x03",

            "#01001F既然如此，就别磨磨蹭蹭的了。\x01",
            "全员出动，去把那个大笨蛋带回来！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#00001F是……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_171A")

    label("loc_1698")


    #C0007
    ChrTalk(
        0x8,
        (
            "#01003F警备队目前应该在\x01",
            "重组增援部队。\x02\x03",

            "#01001F既然已经掌握到兰迪的行踪，就别磨磨蹭蹭的了。\x01",
            "全员出动，去把那个大笨蛋带回来！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171A")

    Jump("loc_235F")

    label("loc_171F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F9")

    #C0008
    ChrTalk(
        0x8,
        (
            "#01000F受玛因兹遭到占领事件的影响，\x01",
            "目前并没有接到什么支援请求。\x02\x03",

            "#01003F你们就专心寻找\x01",
            "兰迪的下落吧。\x02\x03",

            "#01001F路上注意安全。如果有什么\x01",
            "新消息，我也会联络你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00001F好的……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_187E")

    label("loc_17F9")


    #C0010
    ChrTalk(
        0x8,
        (
            "#01003F反正今天也没接到什么\x01",
            "支援请求，你们就专心\x01",
            "去找兰迪那家伙吧。\x02\x03",

            "#01001F路上注意安全。如果有什么\x01",
            "新消息，我也会联络你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187E")

    Jump("loc_235F")

    label("loc_1883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1969")

    #C0011
    ChrTalk(
        0x8,
        (
            "#01003F二科和警备队正在\x01",
            "加紧调查瓦鲁多·瓦雷斯\x01",
            "与『真知』方面的事件。\x02\x03",

            "#01000F既然铁路已经恢复正常，\x01",
            "现在也就没有什么太让人着急的事了。\x02\x03",

            "关于游击士那件事，\x01",
            "如果有时间，就在工作之余\x01",
            "去协会露个面吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_19ED")

    label("loc_1969")


    #C0012
    ChrTalk(
        0x8,
        (
            "#01000F既然铁路已经恢复正常，\x01",
            "现在也就没有什么太让人着急的事了。\x02\x03",

            "关于游击士那件事，\x01",
            "如果有时间，就在工作之余\x01",
            "去协会露个面吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19ED")

    Jump("loc_235F")

    label("loc_19F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD6")

    #C0013
    ChrTalk(
        0x8,
        (
            "#01000F……你们回来了啊，\x01",
            "芙兰已经联络过你们了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000F是的，我们正准备\x01",
            "前往事故现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#01003F是吗，我知道了。\x02\x03",

            "#01000F人偶工房的调查情况稍后再报告给我，\x01",
            "现在就先尽力处理那边的事吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B66")

    label("loc_1AD6")


    #C0016
    ChrTalk(
        0x8,
        (
            "#01000F二科的人和索妮亚带领\x01",
            "的警备队正在赶往\x01",
            "西克洛斯贝尔街道的事故现场。\x02\x03",

            "人偶工房的调查情况稍后再报告给我，\x01",
            "现在就先尽力处理那边的事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B66")

    Jump("loc_235F")

    label("loc_1B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C71")

    #C0017
    ChrTalk(
        0x8,
        (
            "#01006F调查居民独立意向的投票活动即将举行，\x01",
            "所以我也接到了不少文件。\x02\x03",

            "#01002F其中有几个案件挺让人在意……\x01",
            "算了，还是交给其它科来处理吧。\x02\x03",

            "#01000F暂时要把危机管理摆在第一位。\x01",
            "你们别只顾着调查人偶工房，\x01",
            "也要积极处理其它的支援请求。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1CDD")

    label("loc_1C71")


    #C0018
    ChrTalk(
        0x8,
        (
            "#01004F对了，琪雅刚刚出门\x01",
            "购买晚饭的材料了。\x02\x03",

            "#01002F还说要去一趟图书馆……\x01",
            "如果不放心，就去找找她吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDD")

    Jump("loc_235F")

    label("loc_1CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1DEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D83")

    #C0019
    ChrTalk(
        0x8,
        (
            "#01000F哦，我刚刚才从\x01",
            "医院回来。\x02\x03",

            "#01003F你们就继续调查\x01",
            "『幻兽』吧。\x02\x03",

            "#01002F趁着『风之剑圣』无暇分身之机，\x01",
            "不妨多累积一些成绩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DE7")

    label("loc_1D83")


    #C0020
    ChrTalk(
        0x8,
        (
            "#01003F你们就继续调查\x01",
            "『幻兽』吧。\x02\x03",

            "#01002F趁着『风之剑圣』无暇分身之机，\x01",
            "不妨多累积一些成绩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE7")

    Jump("loc_235F")

    label("loc_1DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DFA")
    Jump("loc_235F")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC9")

    #C0021
    ChrTalk(
        0x8,
        (
            "#01000F我会将有关恐怖分子的情报\x01",
            "传达给市长和警备队。\x02\x03",

            "达德利，这些小家伙\x01",
            "就拜托你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x10A,
        (
            "#00603F嗯，交给我吧。\x02\x03",

            "#00601F……好了，你们几个，赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00000F是！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F2B")

    label("loc_1EC9")


    #C0024
    ChrTalk(
        0x8,
        (
            "#01000F目前还不知道\x01",
            "地下空间发生了什么，\x01",
            "一定要小心些。\x02\x03",

            "达德利，这些小家伙\x01",
            "就拜托你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2B")

    Jump("loc_235F")

    label("loc_1F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_20AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201F")

    #C0025
    ChrTalk(
        0x8,
        (
            "#01000F说起你们偶遇的那个\x01",
            "叫谢莉的小姑娘……\x01",
            "她的出现似乎并没有特别目的。\x02\x03",

            "#01003F虽然『赤色星座』的动向\x01",
            "很令人在意，但也不能只顾着\x01",
            "关注他们。\x02\x03",

            "#01000F总之，接下来的事情就交给你们了。\x01",
            "不要着急，尽力而为吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_20A8")

    label("loc_201F")


    #C0026
    ChrTalk(
        0x8,
        (
            "#01003F虽然『赤色星座』的动向\x01",
            "很令人在意，但也不能只顾着\x01",
            "关注他们。\x02\x03",

            "#01000F总之，接下来的事情就交给你们了。\x01",
            "不要着急，尽力而为吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A8")

    Jump("loc_235F")

    label("loc_20AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2167")

    #C0027
    ChrTalk(
        0x8,
        (
            "#01003F今天我会一直在此留守。\x02\x03",

            "#01000F为了给明天召开的\x01",
            "通商会议做好最后准备，\x01",
            "要与一科保持联络。\x02\x03",

            "如果有什么事，我会联络你们的，\x01",
            "不用担心，尽管出门去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_21C8")

    label("loc_2167")


    #C0028
    ChrTalk(
        0x8,
        (
            "#01003F今天我会一直在此留守。\x02\x03",

            "#01000F如果有什么事，我会联络你们的，\x01",
            "不用担心，尽管出门吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C8")

    Jump("loc_235F")

    label("loc_21CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21DB")
    Jump("loc_235F")

    label("loc_21DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DF")

    #C0029
    ChrTalk(
        0x8,
        (
            "#01002F把市民的安全放在第一位，\x01",
            "并完成各式各样的委托……\x01",
            "这就是特别任务支援科。\x02\x03",

            "#01003F像曹或雷克特这样的人，\x01",
            "用一般的方法根本无法对付，\x01",
            "暂且就交给搜查一科来处理吧。\x02\x03",

            "#01000F不要忘记你们\x01",
            "原本的职责哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00000F嗯，放心吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2351")

    label("loc_22DF")


    #C0031
    ChrTalk(
        0x8,
        (
            "#01000F把市民的安全放在第一位，\x01",
            "并完成各式各样的委托……\x01",
            "这就是特别任务支援科。\x02\x03",

            "不要忘记你们\x01",
            "原本的职责哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2351")

    Jump("loc_235F")

    label("loc_2356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_235F")

    label("loc_235F")

    TalkEnd(0x8)
    Return()

    # Function_5_13A3 end

    def Function_6_2363(): pass

    label("Function_6_2363")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2516")

    #C0032
    ChrTalk(
        0x9,
        (
            "#01108F那、那个……真抱歉。\x02\x03",

            "#01103F我突然做出那种举动……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00000F别在意，琪雅。\x02\x03",

            "#00004F在这种特殊状况下，\x01",
            "你会感到不安也是难免的。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#00202F消除你的不安心情，\x01",
            "正是我们这些监护人的责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#00100F今后如果再遇到什么\x01",
            "问题也不用客气，\x01",
            "随时都可以飞扑到我们的怀里哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，你这么依赖我们，\x01",
            "我们很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#01108F嗯……谢谢。\x02\x03",

            "#01100F要注意安全哦……\x01",
            "琪雅会在这里等着大家的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 6)
    Jump("loc_2561")

    label("loc_2516")


    #C0038
    ChrTalk(
        0x9,
        (
            "#01108F谢谢大家……\x02\x03",

            "#01100F要注意安全哦……\x01",
            "琪雅会在这里等着你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2561")

    Jump("loc_2CD8")

    label("loc_2566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2574")
    Jump("loc_2CD8")

    label("loc_2574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_26D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267D")

    #C0039
    ChrTalk(
        0x9,
        (
            "#01103F真希望……\x01",
            "能平安无事地找到兰迪……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00000F一定会找到他的。\x01",
            "琪雅，你不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        (
            "#10106F兰迪前辈真是太过分了，\x01",
            "竟然害得小琪雅\x01",
            "这么担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#00100F就是的，找到他以后，\x01",
            "一定要好好斥责一顿才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "#01109F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_26CF")

    label("loc_267D")


    #C0044
    ChrTalk(
        0x9,
        (
            "#01109F兰迪回来之后，\x01",
            "琪雅也要训斥他～！\x02\x03",

            "#01100F大家……\x01",
            "千万要注意安全哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26CF")

    Jump("loc_2CD8")

    label("loc_26D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2834")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D6")

    #C0045
    ChrTalk(
        0x9,
        (
            "#01109F嘿嘿，其实我昨天\x01",
            "买了很多食材～\x02\x03",

            "虽然今天下雨了，\x01",
            "但不用再跑出去买东西了～\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，真不愧是琪雅啊。\x02\x03",

            "#00000F我们今天一定会回来吃火锅的，\x01",
            "你要乖乖待在家里看家哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        "#01109F嗯，罗伊德，你们也要注意安全哦～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_282F")

    label("loc_27D6")


    #C0048
    ChrTalk(
        0x9,
        (
            "#01100F琪雅今天会准备好\x01",
            "火锅，等着大家回来的。\x02\x03",

            "#01109F罗伊德，你们要注意安全哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282F")

    Jump("loc_2CD8")

    label("loc_2834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2842")
    Jump("loc_2CD8")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2850")
    Jump("loc_2CD8")

    label("loc_2850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_285E")
    Jump("loc_2CD8")

    label("loc_285E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_286C")
    Jump("loc_2CD8")

    label("loc_286C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_29F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2998")

    #C0049
    ChrTalk(
        0x9,
        (
            "#01100F大家路上小心！\x02\x03",

            "#01109F嘿嘿嘿，达德利也要小心一些哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x10A,
        "#00603F都说过不要直呼别人的名字了……！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        "#01105F嗯～？\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x10A,
        (
            "#00606F……唉唉！算了算了！\x01",
            "你们几个，赶快出发！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00012F（唔……即使是达德利警官，\x01",
            "  也拿琪雅没办法啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_29EE")

    label("loc_2998")


    #C0054
    ChrTalk(
        0x9,
        (
            "#01109F大家路上小心～\x02\x03",

            "嘿嘿嘿，达德利也要小心一些哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x10A,
        "#00603F（真是的……）\x02",
    )

    CloseMessageWindow()

    label("loc_29EE")

    Jump("loc_2CD8")

    label("loc_29F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_2AE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA1")

    #C0056
    ChrTalk(
        0x9,
        (
            "#01105F那只叫基库的小鸟\x01",
            "真是好帅啊～\x02\x03",

            "#01109F而且还很聪明，\x01",
            "真想再见到它～\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00006F（印在字条上的\x01",
            "  白隼图案徽章……\x01",
            "  难、难道是……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2AE2")

    label("loc_2AA1")


    #C0058
    ChrTalk(
        0x9,
        (
            "#01105F那只叫基库的小鸟\x01",
            "真是好帅啊～\x02\x03",

            "#01109F真想再见到它～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE2")

    Jump("loc_2CD8")

    label("loc_2AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_2C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1D")

    #C0059
    ChrTalk(
        0x9,
        (
            "#01102F这些枫糖蛋糕应该可以\x01",
            "放到明天哦～\x02\x03",

            "#01109F如果工作时肚子饿了，\x01",
            "就当作零食吃掉吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢啦，琪雅。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，这蛋糕很美味呢，\x01",
            "真希望肚子赶快饿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        "#01102F嘿嘿，琪雅以后还会做的～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_END)), "loc_2C15")

    #C0063
    ChrTalk(
        0x101,
        (
            "#00002F（哈哈，太好了……\x01",
            "  她总算恢复精神了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C15")

    SetScenarioFlags(0x0, 3)
    Jump("loc_2C84")

    label("loc_2C1D")


    #C0064
    ChrTalk(
        0x9,
        (
            "#01104F啦啦啦～¤\x01",
            "得快点洗好衣服。\x02\x03",

            "#01100F如果工作时肚子饿了，\x01",
            "就把这些枫糖蛋糕\x01",
            "当作午饭吃掉吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C84")

    Jump("loc_2CD8")

    label("loc_2C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C97")
    Jump("loc_2CD8")

    label("loc_2C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CA5")
    Jump("loc_2CD8")

    label("loc_2CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CB3")
    Jump("loc_2CD8")

    label("loc_2CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2CC1")
    Jump("loc_2CD8")

    label("loc_2CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2CCF")
    Jump("loc_2CD8")

    label("loc_2CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CD8")

    label("loc_2CD8")

    TalkEnd(0xFE)
    Return()

    # Function_6_2363 end

    def Function_7_2CDC(): pass

    label("Function_7_2CDC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2DD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB2")

    #C0065
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#00200F蔡特的情绪……\x01",
            "好像有些紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00003F面对现在这种状况，\x01",
            "它也提高警戒了吧。\x02\x03",

            "#00001F蔡特，琪雅和塞茜尔姐姐\x01",
            "就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        "#01200F嗷！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2DCF")

    label("loc_2DB2")


    #C0069
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    label("loc_2DCF")

    Jump("loc_3737")

    label("loc_2DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DE2")
    Jump("loc_3737")

    label("loc_2DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_2F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE0")

    #C0070
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#00200F『那群猎兵很善于野战。\x01",
            "  既然要踏入对方的领地，\x01",
            "  一定要时刻保持警惕。』\x02\x03",

            "……它是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00000F谢谢了，蔡特。\x01",
            "我们会谨记你的忠告的。\x02\x03",

            "一定要多加注意，\x01",
            "避免和那些猎兵正面冲突。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EFD")

    label("loc_2EE0")


    #C0073
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_2EFD")

    Jump("loc_3737")

    label("loc_2F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FAD")

    #C0074
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#00203F……你说的没错，\x01",
            "兰迪前辈真是个大笨蛋。\x02\x03",

            "#00200F我们无论如何\x01",
            "也要把他给带回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#00000F嗯……那当然！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2FC6")

    label("loc_2FAD")


    #C0077
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……\x02",
    )

    CloseMessageWindow()

    label("loc_2FC6")

    Jump("loc_3737")

    label("loc_2FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3006")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE6")
    Call(0, 8)
    Jump("loc_3001")

    label("loc_2FE6")


    #C0078
    ChrTalk(
        0xA,
        "#01203F咕噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    label("loc_3001")

    Jump("loc_3737")

    label("loc_3006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_30C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309B")

    #C0079
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……嗷、嗷。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        (
            "#00200F蔡特好像也感觉到\x01",
            "发生大事了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        "#00001F嗯……我们要保持谨慎地前往现场。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_30BC")

    label("loc_309B")


    #C0082
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……嗷、嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_30BC")

    Jump("loc_3737")

    label("loc_30C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30EC")

    #C0083
    ChrTalk(
        0xA,
        "#01203F……咕噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3737")

    label("loc_30EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CD")

    #C0084
    ChrTalk(
        0xA,
        "#01200F咕噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        (
            "#00200F『一定要保持警惕』。\x01",
            "……它是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00003F如果与幻兽战斗，\x01",
            "恐怕会相当危险吧……\x02\x03",

            "#00000F谢谢了，蔡特。\x01",
            "如果真的遇到危险，\x01",
            "就请你再助我们一臂之力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_31E8")

    label("loc_31CD")


    #C0087
    ChrTalk(
        0xA,
        "#01200F咕噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_31E8")

    Jump("loc_3737")

    label("loc_31ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31FB")
    Jump("loc_3737")

    label("loc_31FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3463")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3441")

    #C0088
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x10A,
        (
            "#00603F哼，这匹狼还是这么盛气凌人啊。\x02\x03",

            "#00600F但既然现在的身份是警犬，\x01",
            "我们便需要借助你的力量。\x01",
            "做好随时出动的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        "#01200F……嗷。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32EE")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_32EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3322")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3322")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3356")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3356")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_338A")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_338A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33BE")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_33BE")

    Sleep(1000)

    #C0091
    ChrTalk(
        0x104,
        (
            "#00306F（盛气凌人这个词\x01",
            "  该用在他自己身上才对吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#00100F（呵呵，这也是达德利警官\x01",
            "  特有的激励方法啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_345E")

    label("loc_3441")


    #C0093
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_345E")

    Jump("loc_3737")

    label("loc_3463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_348E")

    #C0094
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3737")

    label("loc_348E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_358F")

    #C0095
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_358A")

    #C0096
    ChrTalk(
        0x101,
        (
            "#00005F对了，蔡特……\x01",
            "你和琪雅一起观看了\x01",
            "兰花塔的揭幕式吧？\x02\x03",

            "琪雅好像无精打采的，\x01",
            "是不是发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00106F这……缇欧不在的时候，\x01",
            "真是完全听不懂你在说什么啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_358A")

    Jump("loc_3737")

    label("loc_358F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3650")

    #C0099
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#00300F嗨，蔡特。\x02\x03",

            "#00309F哈哈，不久前在旧矿山时，\x01",
            "谢谢你给我带路啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#00000F哈哈，今后也请你多帮忙哦。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        "#01200F咕噜噜……嗷。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_366B")

    label("loc_3650")


    #C0103
    ChrTalk(
        0xA,
        "#01200F咕噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_366B")

    Jump("loc_3737")

    label("loc_3670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_372E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3714")

    #C0104
    ChrTalk(
        0xA,
        "#01203F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00000F在这种雨天，\x01",
            "蔡特也觉得很无聊吧？\x02\x03",

            "不过，今天就拜托你留在这里\x01",
            "好好看家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        "#01200F……嗷。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3729")

    label("loc_3714")


    #C0107
    ChrTalk(
        0xA,
        "#01200F……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_3729")

    Jump("loc_3737")

    label("loc_372E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3737")

    label("loc_3737")

    TalkEnd(0xFE)
    Return()

    # Function_7_2CDC end

    def Function_8_373B(): pass

    label("Function_8_373B")

    OP_4B(0xC, 0xFF)

    #C0108
    ChrTalk(
        0xA,
        "#01200F咕噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        "喵～～\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#00200F看来蔡特和柯贝\x01",
            "也很期待今晚那顿\x01",
            "火锅呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x109,
        (
            "#10105F哎？但猫不是\x01",
            "不能吃热的东西吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x105,
        (
            "#10300F犬科动物好像\x01",
            "也不能吃热的食物吧？\x01",
            "呵呵，这都是常识了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#00203F……我会负责把食物晾凉的。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        "#01200F嗷。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 4)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_8_373B end

    def Function_9_384E(): pass

    label("Function_9_384E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_385F")
    Jump("loc_3A02")

    label("loc_385F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3950")

    #C0115
    ChrTalk(
        0xFE,
        "喵喵呜⊥\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#00100F呵呵，吃了不少呢。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#00200F看来它很怀念猫食\x01",
            "的味道。\x02\x03",

            "我们不在的这段时间，\x01",
            "它都是自己出去\x01",
            "寻找食物的……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        "#00305F嘿，是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，没想到柯贝也有\x01",
            "如此坚强的一面呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_395E")

    label("loc_3950")


    #C0120
    ChrTalk(
        0xFE,
        "喵喵呜⊥\x02",
    )

    CloseMessageWindow()

    label("loc_395E")

    Jump("loc_3A02")

    label("loc_3963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3971")
    Jump("loc_3A02")

    label("loc_3971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_398C")
    Call(0, 8)
    Jump("loc_39D4")

    label("loc_398C")


    #C0121
    ChrTalk(
        0xFE,
        "喵～～\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#00004F（反正有琪雅在，\x01",
            "  我们今天就不必给它喂食了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D4")

    Jump("loc_3A02")

    label("loc_39D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_39E7")
    Jump("loc_3A02")

    label("loc_39E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A02")

    #C0123
    ChrTalk(
        0xFE,
        "喵喵～～嗝。\x02",
    )

    CloseMessageWindow()

    label("loc_3A02")

    TalkEnd(0xFE)
    Return()

    # Function_9_384E end

    def Function_10_3A06(): pass

    label("Function_10_3A06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6A")

    #C0124
    ChrTalk(
        0xB,
        (
            "#05928F没想到亚里欧斯先生强行给\x01",
            "小滴办理出院手续……\x01",
            "竟是因为这等大事。\x02\x03",

            "#05923F考虑到小滴的人身安全，\x01",
            "这也是理所当然的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#00003F嗯，是啊……\x02\x03",

            "#00005F……对了，塞茜尔姐姐，\x01",
            "乌尔斯拉医院现在如何了？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#00100F是啊，我很挂念那些住院的警察，\x01",
            "还有伊莉娅小姐的身体状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "#05920F虽然医院里也有点混乱，\x01",
            "但接待患者们的措施\x01",
            "还是和平常一样的。\x02\x03",

            "#05924F芙兰小姐恢复得非常顺利，\x01",
            "现在已移住到普通病房了……\x02\x03",

            "#05920F多诺邦警督也终于在\x01",
            "不久之前恢复了意识。\x02\x03",

            "#05928F……但伊莉娅\x01",
            "却仍然没有醒过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#00203F是吗……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#00303F真希望她能早日\x01",
            "醒来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        "#05924F嗯……希望如此。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 1)
    Jump("loc_3D87")

    label("loc_3C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D2C")

    #C0131
    ChrTalk(
        0xB,
        (
            "#05920F虽然医院里也有点混乱，\x01",
            "但接待患者们的措施\x01",
            "还是和平常一样的。\x02\x03",

            "#05923F总之……\x01",
            "我会留在这里，和小琪雅\x01",
            "一起看家的。\x02\x03",

            "#05920F现在的局势很特殊……\x01",
            "你们千万要注意安全。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3D87")

    label("loc_3D2C")


    #C0132
    ChrTalk(
        0xB,
        (
            "#05920F我会留在这里，和小琪雅\x01",
            "一起看家的。\x02\x03",

            "现在的局势很特殊……\x01",
            "你们千万要注意安全。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D87")

    TalkEnd(0xFE)
    Return()

    # Function_10_3A06 end

    def Function_11_3D8B(): pass

    label("Function_11_3D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9D")
    Call(0, 16)
    Jump("loc_3DD5")

    label("loc_3D9D")

    TalkBegin(0xFF)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00000F这是缇欧的房间，\x01",
            "还是不要随便进去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_3DD5")

    Return()

    # Function_11_3D8B end

    def Function_12_3DD6(): pass

    label("Function_12_3DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE8")
    Call(0, 17)
    Jump("loc_3E20")

    label("loc_3DE8")

    TalkBegin(0xFF)

    #C0134
    ChrTalk(
        0x101,
        (
            "#00000F这是兰迪的房间，\x01",
            "还是不要随便进去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_3E20")

    Return()

    # Function_12_3DD6 end

    def Function_13_3E21(): pass

    label("Function_13_3E21")

    EventBegin(0x1)

    #C0135
    ChrTalk(
        0x101,
        (
            "#00000F……对了，琪雅今天\x01",
            "好像要去主日学校吧？\x02\x03",

            "科长已经出去了，\x01",
            "我们还是和她一起出门比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        "#00100F说的也是，我们去叫她吧。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_13_3E21 end

    def Function_14_3EC2(): pass

    label("Function_14_3EC2")

    EventBegin(0x1)

    #C0137
    ChrTalk(
        0x101,
        (
            "#00000F……对了，琪雅今天\x01",
            "好像要去主日学校吧？\x02\x03",

            "科长已经出去了，\x01",
            "我们还是和她一起出门比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#00100F说的也是，我们去叫她吧。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_14_3EC2 end

    def Function_15_3F63(): pass

    label("Function_15_3F63")

    EventBegin(0x1)

    #C0139
    ChrTalk(
        0x101,
        (
            "#00000F琪雅要去主日学校上课，\x01",
            "从后门出去比较近。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_15_3F63 end

    def Function_16_3FB2(): pass

    label("Function_16_3FB2")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_404C")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_404C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4099")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x102, 170800, 0, 62310, 315)
    SetChrPos(0x101, 168790, 0, 62190, 45)
    SetChrPos(0x104, 169520, 0, 61730, 0)

    label("loc_4099")

    OP_0D()

    #C0140
    ChrTalk(
        0x102,
        "#6P#00100F这是缇欧的房间呢。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x105,
        (
            "#6P#10300F她现在正在\x01",
            "列曼自治州出差吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#00000F嗯，她和约纳\x01",
            "一起去了爱普斯泰恩\x01",
            "财团的研究所。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#6P#00100F由于自治州法的修正，\x01",
            "导力网络在今后将会进一步普及，\x01",
            "他们好像正在准备那方面的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x109,
        (
            "#11P#10103F听起来真是复杂……\x01",
            "看来他们那边的工作也很辛苦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4217")

    #C0145
    ChrTalk(
        0x1A5,
        "#12P#01100F真希望缇欧早点回来～\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#00000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_423F")

    label("loc_4217")


    #C0147
    ChrTalk(
        0x101,
        (
            "#00000F嗯，真希望她能\x01",
            "早日回来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_423F")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_426B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_426B")

    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_16_3FB2 end

    def Function_17_4271(): pass

    label("Function_17_4271")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_430B")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_430B")

    OP_0D()

    #C0148
    ChrTalk(
        0x101,
        "#12P#00000F这是兰迪的房间。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        (
            "#00100F兰迪现在正带领着\x01",
            "贝尔加德门的部队\x01",
            "进行复健训练吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x105,
        (
            "#10305F哦，据说是因为士兵们\x01",
            "在教团事件中被骗服了那种药物？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x109,
        (
            "#6P#10103F嗯……\x01",
            "虽然还没有严重到\x01",
            "会留下后遗症的程度……\x02\x03",

            "#10108F但想恢复原有的体力与手感，\x01",
            "似乎还需要花费一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#12P#00003F是吗……\x01",
            "希望警备队能尽快重振雄风啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44AF")

    #C0153
    ChrTalk(
        0x1A5,
        "#12P#01100F也希望兰迪早点回来。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#00100F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_44D7")

    label("loc_44AF")


    #C0155
    ChrTalk(
        0x102,
        (
            "#00100F是啊，也希望兰迪\x01",
            "早日回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D7")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_17_4271 end

    def Function_18_44EF(): pass

    label("Function_18_44EF")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4516")
    Call(0, 21)
    Return()

    label("loc_4516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4552")
    TalkBegin(0xFF)
    SetChrName("")

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "终端的导力没有接通。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    label("loc_4552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4654")
    TalkBegin(0xFF)
    SetChrName("")

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "终端的导力没有接通。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4650")

    #C0158
    ChrTalk(
        0x101,
        (
            "#00003F……导力好像没有\x01",
            "传输过来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#00200F嗯，\x01",
            "幸好不是\x01",
            "终端坏掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#00300F也就是说，如果想用终端，\x01",
            "就只能用梅尔卡瓦上的那台了。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#00000F是啊，暂且\x01",
            "不要管这里了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 5)

    label("loc_4650")

    TalkEnd(0xFF)
    Return()

    label("loc_4654")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_466E")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_466E")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4687")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C91")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_46C0"),
        (1, "loc_4862"),
        (2, "loc_4C7C"),
        (3, "loc_4C84"),
        (SWITCH_DEFAULT, "loc_4C8C"),
    )


    label("loc_46C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_46D3")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_485D")

    label("loc_46D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46EE")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_485D")

    label("loc_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4737")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("自动语音")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有支援请求。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_485D")

    label("loc_4737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4752")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_485D")

    label("loc_4752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_478D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_477B")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_4788")

    label("loc_477B")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_4788")

    Jump("loc_485D")

    label("loc_478D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47A6")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_485D")

    label("loc_47A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_47B4")
    Jump("loc_485D")

    label("loc_47B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47D1")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_485D")

    label("loc_47D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_47EE")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_485D")

    label("loc_47EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4807")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_485D")

    label("loc_4807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_483B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_482B")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_4836")

    label("loc_482B")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_4836")

    Jump("loc_485D")

    label("loc_483B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_4852")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_485D")

    label("loc_4852")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_485D")

    Jump("loc_4C8C")

    label("loc_4862")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4919")
    SetChrName("自动语音")

    #A0163
    AnonymousTalk(
        0xFF,
        "这里是克洛斯贝尔警察局。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_48FA")

    #A0164
    AnonymousTalk(
        0xFF,
        "即将受理您的报告。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("自动语音")

    #A0165
    AnonymousTalk(
        0xFF,
        (
            "报告处理完毕，\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4914")

    label("loc_48FA")


    #A0166
    AnonymousTalk(
        0xFF,
        "没有可以报告的委托。\x02",
    )

    CloseMessageWindow()

    label("loc_4914")

    Jump("loc_4C6E")

    label("loc_4919")

    SetChrName("接待小姐芙兰")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_496B")
    Sound(3062, 255, 100, 0)    #voice#Fran

    #A0167
    AnonymousTalk(
        0xFF,
        "#26A您好，这里是克洛斯贝尔警察局～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4983")

    label("loc_496B")

    Sound(3061, 255, 100, 0)    #voice#Fran

    #A0168
    AnonymousTalk(
        0xFF,
        "#29A各位辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_4983")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_4BA6")
    Sound(3067, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0169
    AnonymousTalk(
        0xFF,
        "#27A已经收到大家的报告～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B33")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_49EC"),
        (13, "loc_4A34"),
        (12, "loc_4A78"),
        (SWITCH_DEFAULT, "loc_4ABE"),
    )


    label("loc_49EC")

    Sound(3075, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            "#39A级别１ｓｔ……\x01",
            "罗伊德警官，实在太厉害了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ABE")

    label("loc_4A34")

    Sound(3074, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            "#38A级别２ｎｄ──\x01",
            "罗伊德警官，好厉害呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ABE")

    label("loc_4A78")

    Sound(3073, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            "#33A级别３ｒｄ──\x01",
            "罗伊德警官，做得很好啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ABE")

    label("loc_4ABE")

    Sound(3076, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            "#33A马上就会把奖励物品\x01",
            "给你们送去的～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)    #voice#Fran

    #A0174
    AnonymousTalk(
        0xFF,
        (
            "#33A大家辛苦了～！\x01",
            "以后也请随时来向我报告～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9E")

    label("loc_4B33")

    Sound(3078, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0175
    AnonymousTalk(
        0xFF,
        "#17A报告就是以上这些吧～\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)    #voice#Fran

    #A0176
    AnonymousTalk(
        0xFF,
        (
            "#38A那么，以后如果完成了新的委托，\x01",
            "请再来向我报告吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9E")

    SetScenarioFlags(0x0, 1)
    Jump("loc_4C6E")

    label("loc_4BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C15")
    Sound(3063, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            "#31A哎……\x01",
            "不是刚刚才报告过吗？\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)    #voice#Fran

    #A0178
    AnonymousTalk(
        0xFF,
        "#35A等完成了新的委托之后再来报告吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C6E")

    label("loc_4C15")

    Sound(3065, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0179
    AnonymousTalk(
        0xFF,
        (
            "#38A哎，好像并没有可以\x01",
            "报告的委托啊～\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)    #voice#Fran

    #A0180
    AnonymousTalk(
        0xFF,
        "#20A请下次再来报告吧～\x02",
    )

    CloseMessageWindow()

    label("loc_4C6E")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_4C8C")

    label("loc_4C7C")

    Call(0, 20)
    Jump("loc_4C8C")

    label("loc_4C84")

    Call(0, 19)
    Jump("loc_4C8C")

    label("loc_4C8C")

    Jump("loc_4687")

    label("loc_4C91")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CD2")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 24)
    Return()

    label("loc_4CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D05")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 27)
    Return()

    label("loc_4D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D3F")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 32)
    Return()

    label("loc_4D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D72")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 39)
    Return()

    label("loc_4D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DFF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DC9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DC4")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_4DC4")

    Jump("loc_4DFA")

    label("loc_4DC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DFA")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_4DFA")

    Jump("loc_4E76")

    label("loc_4DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E18")
    SetScenarioFlags(0x168, 2)
    Call(0, 67)
    Jump("loc_4E76")

    label("loc_4E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E52")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 44)
    Return()

    label("loc_4E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_4E64")
    ClearScenarioFlags(0x22, 3)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_4E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_4E76")
    ClearScenarioFlags(0x22, 6)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_4E76")

    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    Call(0, 67)
    TalkEnd(0xFF)
    Return()

    # Function_18_44EF end

    def Function_19_4E89(): pass

    label("Function_19_4E89")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4EB7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x94, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4EB2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EB2")

    Jump("loc_51C7")

    label("loc_4EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4EF7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EF2")

    Jump("loc_51C7")

    label("loc_4EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4F0F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51C7")

    label("loc_4F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4F4F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F4A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F4A")

    Jump("loc_51C7")

    label("loc_4F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4FD9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4FA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F9D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F9D")

    Jump("loc_4FD4")

    label("loc_4FA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FD4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FD4")

    Jump("loc_51C7")

    label("loc_4FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5012")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_500D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_500D")

    Jump("loc_51C7")

    label("loc_5012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_502A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51C7")

    label("loc_502A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5071")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_506C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_506C")

    Jump("loc_51C7")

    label("loc_5071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_50B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50B3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50B3")

    Jump("loc_51C7")

    label("loc_50B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50EC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50EC")

    Jump("loc_51C7")

    label("loc_50F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_516A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_513A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5135")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5135")

    Jump("loc_5165")

    label("loc_513A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5165")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5165")

    Jump("loc_51C7")

    label("loc_516A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_519C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5197")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5197")

    Jump("loc_51C7")

    label("loc_519C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51C7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_520B")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请查阅所有支援请求。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_520B")

    Return()

    # Function_19_4E89 end

    def Function_20_520C(): pass

    label("Function_20_520C")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_522E")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_522E")
    ClearScenarioFlags(0x2A, 0)

    label("loc_522E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_524B")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_524B")
    ClearScenarioFlags(0x2A, 1)

    label("loc_524B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_5268")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5268")
    ClearScenarioFlags(0x2A, 2)

    label("loc_5268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_5285")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5285")
    ClearScenarioFlags(0x2A, 3)

    label("loc_5285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_52A2")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A2")
    ClearScenarioFlags(0x2A, 4)

    label("loc_52A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_52BF")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52BF")
    ClearScenarioFlags(0x2A, 5)

    label("loc_52BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_52CB")
    SetScenarioFlags(0x2A, 6)

    label("loc_52CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_531D")
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_5398")

    label("loc_531D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_536F")
    OP_24(0x80)
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_5398")

    label("loc_536F")

    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_5398")

    Return()

    # Function_20_520C end

    def Function_21_5399(): pass

    label("Function_21_5399")

    EventBegin(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SoundLoad(939)
    OP_68(16740, 1750, 10380, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(24570, 0)
    SetChrPos(0x101, 15000, 850, 10900, 90)
    SetChrPos(0x102, 15970, 850, 9800, 45)
    SetChrPos(0x109, 14390, 850, 9310, 90)
    SetChrPos(0x105, 16500, 850, 8270, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0182
    ChrTalk(
        0x101,
        (
            "#6P#00004F根据罗伯兹主任刚才说的，\x01",
            "我们应该先把这个记录结晶里的\x01",
            "程序安装到终端里吧？\x02\x03",

            "#00000F那么，艾莉……\x01",
            "就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        "#12P#00100F嗯，让我试试吧。\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉在导力终端上\x01",
            "成功安装了『波波碰！』β版。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    Sound(836, 0, 100, 0)
    Sleep(1000)
    Sound(939, 2, 100, 0)
    Sleep(1000)
    OP_24(0x3AB)
    Sound(839, 0, 100, 0)
    Sleep(500)
    Sound(839, 0, 100, 0)

    #C0185
    ChrTalk(
        0x102,
        (
            "#12P#00104F这样就行了……\x02\x03",

            "#00100F已经把罗伯兹主任\x01",
            "给我们的账号输入好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x105,
        "#12P#10302F哦？手法还挺熟练嘛。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x109,
        (
            "#6P#10109F艾莉小姐真是\x01",
            "相当博学呢。\x02\x03",

            "#10100F在政治和法律等方面，\x01",
            "知识也相当丰富。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)
    Sleep(300)

    #C0188
    ChrTalk(
        0x102,
        (
            "#11P#00102F呵呵，\x01",
            "只是因为平时经常\x01",
            "看缇欧操作而已。\x02\x03",

            "#00104F而且还有说明书，\x01",
            "只要认真看一看，\x01",
            "其实并不是很难。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0189
    ChrTalk(
        0x101,
        (
            "#5P#00002F不管怎么说，你真是帮大忙了。\x02\x03",

            "#00006F我就差多了，费了好一番力气，\x01",
            "才刚刚熟悉了键盘的操作。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0190
    ChrTalk(
        0x102,
        (
            "#12P#00109F呵呵，不用谦虚。\x02\x03",

            "#00100F那么……我们现在\x01",
            "可以联系罗伯兹主任了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        "#5P#00000F嗯，马上联系他吧。\x02",
    )

    CloseMessageWindow()

    def lambda_57BF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_57BF)
    Sleep(50)

    def lambda_57CF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57CF)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(823, 0, 100, 0)
    Sleep(2800)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，罗伊德，\x01",
            "你们已经顺利安装好了吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0193
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F是的，已经装好了，\x01",
            "接下来该怎么做呢？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，那就和我\x01",
            "来一场对战吧。\x02\x03",

            "先从终端启动『波波碰！』\x01",
            "这个程序。\x02\x03",

            "列表中会显示\x01",
            "我的用户名，\x01",
            "选择我的名字，就可以开始对战了。\x02\x03",

            "……对了，机会难得，\x01",
            "不如就由你这个支援科的队长\x01",
            "来当代表，和我来一场对战吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0195
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F？？？\x01",
            "好的，我明白了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)

    #C0196
    ChrTalk(
        0x102,
        "#12P#00100F那我们就换个位置吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x14, 0x1F4)

    def lambda_5A58():
        OP_9B(0x1, 0xFE, 0xB4, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A58)
    Sleep(200)

    def lambda_5A70():
        OP_95(0xFE, 15970, 850, 9800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A70)

    def lambda_5A8A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A8A)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x5)
    Sleep(500)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，你能战胜\x01",
            "我这个开发者吗……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S负责照顾缇欧的男人……\x01",
            "就让我好好检验一下你的实力吧！#3S\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0199
    ChrTalk(
        0x109,
        (
            "#6P#10112F……似乎听到他的\x01",
            "真心话了……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#12P#10309F啊哈哈，\x01",
            "真像个担心女儿的笨蛋父亲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#6P#00006F那个……您特地把任务\x01",
            "交给支援科，莫非也是因为……？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊哈哈，不好意思……\x01",
            "难得可以决一胜负，\x01",
            "好像有点激动了。\x02\x03",

            "好啦，那我们就\x01",
            "赶快开始游戏吧！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x27, 2)
    OP_29(0x6C, 0x1, 0x1)
    StopSound(128, 500, 40)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()

    label("loc_5D19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D94")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D51")
    Call(0, 20)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D8F")

    label("loc_5D51")


    #A0203
    AnonymousTalk(
        0x101,
        (
            "#0000F罗伯兹主任还在等着呢，\x01",
            "赶快启动『波波碰！』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5D8F")

    Jump("loc_5D19")

    label("loc_5D94")

    OP_E5(0x6)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    Call(0, 22)
    Return()

    # Function_21_5399 end

    def Function_22_5DB8(): pass

    label("Function_22_5DB8")

    EventBegin(0x0)
    SoundLoad(803)
    SoundLoad(128)
    Sound(128, 2, 50, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E33")
    OP_2C(0x6C, 0x1)

    #C0204
    ChrTalk(
        0x101,
        (
            "#6P#00009F好，总算赢了……！\x02\x03",

            "#00004F（嗯……\x01",
            "  还挺好玩呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x2)
    Jump("loc_5E81")

    label("loc_5E33")


    #C0205
    ChrTalk(
        0x101,
        (
            "#6P#00006F……输了呢。\x02\x03",

            "#00001F（唔……总觉得\x01",
            "  有些不甘心啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x3)

    label("loc_5E81")


    #C0206
    ChrTalk(
        0x102,
        (
            "#12P#00109F呵呵，你玩得\x01",
            "相当入神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x109,
        (
            "#6P#10105F……那个……\x01",
            "这只是我这个旁观者的感觉而已……\x02\x03",

            "#10106F罗伯兹主任好像\x01",
            "并不是很擅长这个游戏吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x105,
        (
            "#12P#10300F是啊，明明是开发者，\x01",
            "玩起来却和你这个初学者\x01",
            "不相上下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0209
    ChrTalk(
        0x101,
        (
            "#5P#00012F哪、哪里……\x01",
            "主任肯定是\x01",
            "手下留情了吧？\x02\x03",

            "#00003F如果不玩得难分难解，\x01",
            "也就起不到测试效果了……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(100)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0210
    ChrTalk(
        0x101,
        "#6P#00000F您好，这里是特别任务支援——\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哎呀！\x01",
            "刚才那场比赛太精彩啦！\x02\x03",

            "简直是一场可以名留青史的大决战！\x01",
            "我真是太兴奋了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0212
    ChrTalk(
        0x101,
        (
            "#6P#00006F（看来他刚才\x01",
            "  很认真啊……）\x02\x03",

            "#00012F那、那么……\x01",
            "测试的结果如何？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，测试非常成功！\x02\x03",

            "在市内对战并没有\x01",
            "明显的延迟现象，\x01",
            "连接状态也很不错。\x02\x03",

            "可以说很完美呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0214
    ChrTalk(
        0x101,
        (
            "#6P#00000F是吗……\x01",
            "那真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不久之后，你刚才安装\x01",
            "的那个β版就会升级为\x01",
            "正式发布版哦。\x02\x03",

            "程序发布以后，\x01",
            "可以对战的人也会随之增加。\x02\x03",

            "希望你们到时候可以和别人交换账号，\x01",
            "尽情享受这个游戏。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6351")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当然了，我以后早晚会\x01",
            "一雪今日战败之耻的！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_63A0")

    label("loc_6351")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当然了，我今后随时都可以\x01",
            "接受你的再次挑战！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_63A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6401")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0218
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当然了，我以后早晚会\x01",
            "一雪今日战败之耻的！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6450")

    label("loc_6401")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当然了，我今后随时都可以\x01",
            "接受你的再次挑战！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6450")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0220
    ChrTalk(
        0x101,
        (
            "#6P#00012F哈、哈哈……\x01",
            "到时候请您手下留情。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，你们能帮我这个忙，\x01",
            "真是太感谢了。\x02\x03",

            "我还有其它工作，\x01",
            "这就要挂断了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0222
    ChrTalk(
        0x101,
        (
            "#6P#00000F不必客气，\x01",
            "如果今后还有什么事情，\x01",
            "随时都可以联系我们。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("罗伯兹的声音")

    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好，我知道了。\x01",
            "那就这样啦！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    #C0224
    ChrTalk(
        0x101,
        (
            "#00004F呼……总算\x01",
            "顺利完成了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#12P#00100F呵呵，辛苦你了。\x02\x03",

            "#00104F该怎么说呢，这件委托\x01",
            "真是很符合主任的行事风格啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#00012F哈哈，是啊。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x105,
        (
            "#12P#10300F话说回来，我们今后也\x01",
            "可以继续玩这个游戏呢。\x02\x03",

            "#10309F既然如此，\x01",
            "不如就将成为克洛斯贝尔最强的\x01",
            "『波波碰大师』定为目标吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#00006F还是算了吧，不管怎么练习，\x01",
            "也不可能赢过缇欧吧……\x02\x03",

            "#00000F不过，在工作之余的\x01",
            "休息时间里稍微练习一下，\x01",
            "也是种不错的娱乐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x109,
        "#6P#10100F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    StopSound(128, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【参加β测试】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_29(0x6C, 0x1, 0x4)
    OP_29(0x6C, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x11)
    SetChrPos(0x0, 14970, 850, 8800, 225)
    OP_24(0x323)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(128, 2, 50, 0)
    EventEnd(0x5)
    Return()

    # Function_22_5DB8 end

    def Function_23_6827(): pass

    label("Function_23_6827")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis011.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis347.itp")
    OP_68(17000, 1650, 10500, 0)
    MoveCamera(19, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 15200, 850, 10900, 90)
    SetChrPos(0x102, 16300, 850, 10200, 45)
    SetChrPos(0x109, 17200, 850, 8000, 315)
    SetChrPos(0x105, 16200, 850, 7700, 0)
    SetCameraDistance(23500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(836, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(72, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #A0231
    AnonymousTalk(
        0x102,
        (
            "#00104F嗯，\x01",
            "果然收到了委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0232
    AnonymousTalk(
        0x109,
        "#10100F这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0233
    AnonymousTalk(
        0x105,
        (
            "#10302F这就是特别任务支援科\x01",
            "负责处理的『支援请求』吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x101, 0x109, 0)
    Sleep(300)

    #A0234
    AnonymousTalk(
        0x101,
        (
            "#00004F没错，基本上是\x01",
            "每天更新一次。\x02\x03",

            "#00000F至于要受理哪些委托，\x01",
            "就由我们来自行斟酌……\x02\x03",

            "不过，标示着『紧急』二字的委托\x01",
            "是必须要处理的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0235
    AnonymousTalk(
        0x105,
        (
            "#10304F原来如此，听起来很合理呢。\x02\x03",

            "#10300F这些时限较长的委托，\x01",
            "意思就是可以第二天再处理吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0236
    AnonymousTalk(
        0x101,
        "#00000F嗯，可以这样理解。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0237
    AnonymousTalk(
        0x102,
        (
            "#00104F时限会随着时间的流逝而变化，\x01",
            "最好每天检查一次。\x02\x03",

            "#00100F此外，在『调查手册』中\x01",
            "也可以确认委托的状况。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0238
    AnonymousTalk(
        0x109,
        "#10105F调查手册是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(24000, 0)
    FadeToBright(0, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    #C0239
    ChrTalk(
        0x109,
        (
            "#12P#10100F就是艾莉小姐经常用来记录事项的\x01",
            "那本黑色手册吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0240
    ChrTalk(
        0x102,
        "#5P#00100F嗯，就是这个。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0241
    AnonymousTalk(
        0x101,
        (
            "#00003F基本来说，只要在调查任务与支援请求中\x01",
            "取得了进展，就要及时记录在手册中。\x02\x03",

            "这样才能有条理地\x01",
            "同时处理多项任务。\x02\x03",

            "#00000F另外，战术导力器\x01",
            "『艾尼格玛』的相关说明\x01",
            "也记录在手册中。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0242
    AnonymousTalk(
        0x105,
        (
            "#10305F哦？还挺方便的嘛。\x02\x03",

            "#10304F不过，这种手册有朝一日\x01",
            "也会被相应的导力设备所取代吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0243
    AnonymousTalk(
        0x102,
        (
            "#00102F是啊……\x01",
            "以前曾听缇欧说过，现在就已经\x01",
            "有了那方面的研究呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0244
    AnonymousTalk(
        0x109,
        (
            "#10112F唔……如果导力设备真的扩张到那种程度，\x01",
            "总觉得反而会让人有点抵触……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0245
    AnonymousTalk(
        0x101,
        (
            "#00002F确实如此，我也觉得\x01",
            "还是纸笔用起来更加顺手。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0246
    ChrTalk(
        0x101,
        (
            "#00004F#5P总之，简单来说，\x01",
            "这就是支援科的基本工作模式了。\x02\x03",

            "#00000F我们先在终端确认一下\x01",
            "今天接到的支援请求吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x109,
        "#12P#10102F明白！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x105,
        "#12P#10309F呵呵，真让人期待呢。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0249
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※按○键调查放置在支援科的终端，\x01",
            "  在列表中选择［确认支援请求］，\x01",
            "  就能看到委托给罗伊德等人的任务一览表。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在支援请求中，会有一些紧急度较高，\x01",
            "　必须要接受的任务。\x01",
            "　这种任务都会附有『紧急』的标示，\x01",
            "　只有将其完成，才能使主线剧情继续进展。\x02",
        )
    )

    CloseMessageWindow()

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※除此之外的支援请求\x01",
            "  并无全部完成的必要，\x01",
            "　但解决这些委托可以获得ＤＰ与米拉。\x01",
            "　另外，一旦超过时限，这些委托就会消失，还请注意。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 15000, 850, 8900, 45)
    SetScenarioFlags(0x126, 0)
    OP_29(0xA1, 0x4, 0x2)
    OP_29(0xA1, 0x1, 0x0)
    Call(0, 67)
    AddItemNumber(0x5, 1)
    AddItemNumber(0x6, 1)
    OP_C9(0x0, 0x1000)
    OP_C9(0x0, 0x200000)
    EventEnd(0x5)
    Return()

    # Function_23_6827 end

    def Function_24_70FA(): pass

    label("Function_24_70FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis231.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis235.itp")
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x2)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrPos(0x105, 11300, 900, 4600, 90)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 19000, 850, 4000, 270)
    OP_4B(0x8, 0xFF)
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0252
    ChrTalk(
        0x109,
        (
            "#6P#10103F两件紧急委托，\x01",
            "还有两件通缉魔兽的任务……\x02\x03",

            "#10101F关于艾尼格玛Ⅱ的那个委托倒是没什么，\x01",
            "但另一个委托却相当特殊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#00106F#11P是啊，没想到那个名叫雷克特的人\x01",
            "竟然再次来到了克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x105,
        (
            "#6P#10303F就是我们在『黑之竞拍会』上\x01",
            "遇到的那位装疯卖傻的老兄吧？\x02\x03",

            "#10300F怎么看都不像是\x01",
            "寻常之辈呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)

    #A0255
    AnonymousTalk(
        0x101,
        (
            "#00003F……我在搜查一科研修的时候，\x01",
            "查阅了关于他的文件。\x02\x03",

            "#00001F他是帝国军情报局的\x01",
            "雷克特·亚兰德尔特务大尉。\x02\x03",

            "另外还有帝国政府\x01",
            "二等书记官这个头衔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0256
    AnonymousTalk(
        0x109,
        "#10108F原来是个间谍工作者吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0257
    ChrTalk(
        0x102,
        (
            "#00103F#11P看来是个连政治工作\x01",
            "都可以处理的情报军官啊。\x02\x03",

            "#00101F那些让人无从捉摸的古怪行为，\x01",
            "或许也是很高明的伪装技术呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x105,
        (
            "#6P#10304F我倒觉得那多半是他的真实性格的体现。\x02\x03",

            "#10302F话说回来，既是帝国政府的书记官，\x01",
            "还同时隶属于帝国军情报局……\x02\x03",

            "难道他是那个大名鼎鼎的\x01",
            "『铁血宰相』的心腹吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#5P#00006F（他为何连这种背景\x01",
            "  都想到了……）\x02\x03",

            "#00001F不错，根据一科的情报，\x01",
            "他正是奥斯本宰相的心腹之一。\x02\x03",

            "已经确认，他去年曾与宰相一同来访\x01",
            "克洛斯贝尔，与哈尔特曼议长进行了\x01",
            "非官方性质的会谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#00108F#11P他本人也曾提起过这件事呢。\x02\x03",

            "#00106F他一副信口开河的语气，\x01",
            "没想到竟然是真的……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x109,
        (
            "#6P#10106F不管怎么看，都是个\x01",
            "相当不好对付的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x105,
        (
            "#6P#10309F呵呵，这不是很有趣嘛。\x02\x03",

            "#10300F也就是说，我们应该优先处理\x01",
            "市内的支援请求吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        (
            "#5P#00000F嗯，其中一项关于通缉魔兽的\x01",
            "委托需要前往市外处理，\x01",
            "那件委托就先放到后面吧。\x02\x03",

            "#00003F……自鲁巴彻消亡，已经过去了好几个月。\x02\x03",

            "#00001F地下世界差不多也该\x01",
            "出现新动向了。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#00108F#11P嗯，比如『黑月』的行动……\x01",
            "以及帝国政府的行动。\x02\x03",

            "#00101F将在月底召开的『通商会议』\x01",
            "或许也会受到很大影响。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x105, 0x0)
    Sleep(300)

    #C0265
    ChrTalk(
        0x109,
        "#6P#10105F『通商会议』就是……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x105,
        (
            "#6P#10300F在新市长的提议下，\x01",
            "汇集了各国首脑人物的国际会议吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    #C0267
    ChrTalk(
        0x102,
        "#00102F#11P是的。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)

    #A0268
    AnonymousTalk(
        0x102,
        (
            "#00104F由新市长迪塔·库罗伊斯主办。\x02\x03",

            "帝国、共和国、利贝尔王国，\x01",
            "以及雷米菲利亚公国的首脑人物\x01",
            "齐聚一堂的国际经济会议。\x02\x03",

            "#00100F会议的正式名称是\x01",
            "『西塞姆里亚通商会议』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0269
    AnonymousTalk(
        0x101,
        (
            "#00004F市长才刚刚就任不久，\x01",
            "竟然就筹划了如此\x01",
            "大规模的国际会议……\x02\x03",

            "#00000F真不愧是兼任ＩＢＣ总裁\x01",
            "一职的人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #C0270
    ChrTalk(
        0x109,
        (
            "#6P#10109F虽然没有直接会过面，\x01",
            "但听说他是一位非常精干的人。\x02\x03",

            "#10102F说起来，瓦吉好像\x01",
            "见过这位新市长吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0271
    ChrTalk(
        0x105,
        (
            "#6P#10304F嗯，拿推荐信的时候见过。\x02\x03",

            "#10302F虽说支援科在警察局中算是个\x01",
            "特立独行的部门，但他竟然会把\x01",
            "不良组织的首领引荐到警察队伍……\x02\x03",

            "#10309F呵呵，这话由我来说可能有些不合适，\x01",
            "但他真是一位非常不拘小节的大叔呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        "#5P#00006F这个……并不好笑啊。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        (
            "#00111F#11P迪塔叔叔也真是的，\x01",
            "竟然还说什么\x01",
            "『哈哈哈，这孩子真有趣』……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    Sleep(300)

    #N0274
    NpcTalk(
        0x8,
        "科长的声音",
        "哦，你们已经在工作了啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(16000, 1850, 4000, 2000)
    MoveCamera(40, 19, 0, 2000)
    SetChrPos(0x8, 20000, 850, 4000, 270)

    def lambda_7D3C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7D3C)

    def lambda_7D4D():
        OP_95(0xFE, 17000, 850, 4000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7D4D)
    SetChrSubChip(0x105, 0x0)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_6F(0x79)

    #C0275
    ChrTalk(
        0x101,
        "#00005F赛尔盖科长……\x02",
    )

    CloseMessageWindow()
    OP_68(12600, 1850, 6600, 4000)
    MoveCamera(35, 17, 0, 4000)
    OP_92(0x8, 0x39D0, 0x20D0, 0x1F4)
    BeginChrThread(0x101, 3, 0, 25)

    def lambda_7DD4():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7DD4)
    WaitChrThread(0x8, 1)

    def lambda_7DF2():
        OP_95(0xFE, 12700, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7DF2)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    Fade(250)
    SetChrPos(0x109, 11100, 850, 5750, 90)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(812, 0, 100, 0)
    OP_0D()
    TurnDirection(0x109, 0x8, 500)

    #C0276
    ChrTalk(
        0x109,
        "#6P#10101F早上好！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x109, 500)
    Sleep(150)

    #C0277
    ChrTalk(
        0x8,
        (
            "#01003F#5P早，坐着就行了。\x02\x03",

            "#01000F我们支援科基本上采取放任主义。\x02\x03",

            "只要没发生什么重大事件，\x01",
            "我是不会出言干预的，\x01",
            "你们可以随意行事。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x109,
        "#6P#10105F是、是吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    Sound(812, 0, 100, 0)
    OP_0D()
    Sleep(200)

    #C0279
    ChrTalk(
        0x105,
        (
            "#6P#10309F啊哈哈，\x01",
            "真是个通情达理的上司啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#11P#00012F……唔……\x01",
            "这么说倒也没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        (
            "#11P#00111F但科长采取这种方针，\x01",
            "很大程度上也是因为怕麻烦吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    #C0282
    ChrTalk(
        0x8,
        (
            "#01004F#5P呵呵，很了解我嘛。\x02\x03",

            "#01002F不过，今天算是个例外，\x01",
            "我有个指示要下达给你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x101,
        "#00011F#11P哦……？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        "#00105F#11P科、科长下指示吗？\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#01003F#5P嗯，你们先把自己手头\x01",
            "的支援请求处理完吧。\x02\x03",

            "#01000F然后去一趟警察学校。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0286
    ChrTalk(
        0x101,
        "#00005F#11P警察学校……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x109,
        (
            "#6P#10100F就是位于西克洛斯贝尔街道中途，\x01",
            "带有演习场的那个地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x8,
        (
            "#01004F#5P罗伊德和诺艾尔\x01",
            "应该对那个地方很熟悉吧？\x02\x03",

            "#01000F我准备好了之后，\x01",
            "就会用艾尼格玛联系你们。\x02\x03",

            "在那之前，你们就先在市内巡视，\x01",
            "同时处理那些支援请求吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        "#00000F#11P这样啊……明白了。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x102,
        "#00100F#11P不过，究竟有什么事呢？\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "#01002F#5P呵呵，谜底要等你们\x01",
            "到了以后才能揭晓。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2328, 0x2648, 0x1F4)
    Sleep(300)

    #C0292
    ChrTalk(
        0x8,
        (
            "#01006F#11P那就先这样吧，\x01",
            "稍后再联系你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(10600, 1850, 6600, 3000)

    def lambda_8328():
        OP_95(0xFE, 9000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8328)
    WaitChrThread(0x8, 1)

    def lambda_8346():
        OP_95(0xFE, 2000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8346)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    OP_0D()

    #C0293
    ChrTalk(
        0x109,
        "#6P#10105F这……\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x102,
        (
            "#00106F#11P诺艾尔小姐……\x01",
            "不好意思，\x01",
            "这就是支援科的行事风格了。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#5P#00006F如果往好的方向去想，\x01",
            "可以把它理解为培养我们的\x01",
            "自主性与判断能力……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    #C0296
    ChrTalk(
        0x109,
        (
            "#6P#10109F原、原来如此！\x01",
            "真不愧是赛尔盖科长！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，一件事情换个说法真是大不相同呢。\x02\x03",

            "#10302F接下来该做什么？\x01",
            "这就要去街上吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0298
    ChrTalk(
        0x101,
        (
            "#5P#00004F嗯，出发吧。\x02\x03",

            "#00005F……对了，琪雅今天\x01",
            "好像要去主日学校吧？\x02\x03",

            "#00000F科长已经出去了，\x01",
            "我们还是和她一起出门比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x102,
        (
            "#00102F#11P说的对，我们先去三层，\x01",
            "叫上琪雅一起走吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_4C(0x8, 0xFF)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetScenarioFlags(0x126, 1)
    OP_29(0xA1, 0x1, 0x1)
    OP_32(0x6, 0x0, 0x32)
    OP_42(0x6, 0x3E9, 0xFF)
    Call(0, 67)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_24_70FA end

    def Function_25_863F(): pass

    label("Function_25_863F")

    Sleep(1500)
    SetChrSubChip(0x109, 0x0)
    Sleep(700)
    SetChrSubChip(0x102, 0x2)
    Sleep(300)
    SetChrSubChip(0x105, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)
    SetChrSubChip(0x109, 0x1)
    Return()

    # Function_25_863F end

    def Function_26_8663(): pass

    label("Function_26_8663")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    OP_68(12600, 2350, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrPos(0x105, 11300, 900, 4600, 90)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 12700, 850, 8400, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    OP_68(12600, 1850, 6600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    #C0300
    ChrTalk(
        0x8,
        (
            "#01006F#5P今天一整天\x01",
            "恐怕都会是小雨天气呢。\x02\x03",

            "#01000F据说到了晚上，雨势还会加大。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00003F是吗……\x02\x03",

            "#00000F难得给我们配了辆导力车，\x01",
            "本来还想开到郊外\x01",
            "四处转转……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x105,
        (
            "#6P#10304F算了，今天也不是\x01",
            "兜风的好日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x109,
        "#6P#10106F呜呜……真遗憾。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        (
            "#00108F#12P对了……关于我们昨天在郊外\x01",
            "遇到的那个人，\x01",
            "还没有查到任何消息吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "#01003F#5P是啊，一科也还\x01",
            "没能确认他的身份。\x02\x03",

            "#01001F曹和雷克特也是一样，\x01",
            "全是些不好对付的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00008F嗯……\x02\x03",

            "#00006F……昨天遇到的那个男人，\x01",
            "恐怕比他们更加危险。\x02\x03",

            "#00001F看上去似乎相当沉稳，但却散发着\x01",
            "一股莫名的残暴气息……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0307
    ChrTalk(
        0x109,
        (
            "#6P#10103F确实如此……\x01",
            "有一股猛虎般的气势。\x02\x03",

            "#10101F甚至让我觉得，只要他愿意，\x01",
            "不消片刻便能把我们吞噬入腹……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x102,
        (
            "#00106F#12P这比喻真是让人后背发冷，\x01",
            "但确实有那种感觉。\x02\x03",

            "#00108F恐怖分子或猎兵……\x01",
            "很可能是这类人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x105,
        (
            "#6P#10308F嗯……\x02\x03",

            "#10304F既然如此，我们可以去\x01",
            "旧城区一带收集一下情报。\x02\x03",

            "#10300F『纳因瓦利』的女老板等人\x01",
            "应该了解不少情报。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(200)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)

    #C0310
    ChrTalk(
        0x101,
        (
            "#00005F#11P交换店的亚修莉女士吗？\x02\x03",

            "#00001F她以前是个武器商人，\x01",
            "对地下世界应该很熟悉……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        (
            "#00101F#11P说的也是，看来\x01",
            "确实值得去咨询一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "#01004F#5P嗯，加油吧。\x02\x03",

            "#01000F但不要忘记，\x01",
            "你们终究是支援科的成员。\x02\x03",

            "如果把全副精力都放在反间谍方面，\x01",
            "将会丢掉自己原本的职责哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    Sleep(200)

    #C0313
    ChrTalk(
        0x101,
        "#00005F我、我明白了。\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0x39D0, 0x20D0, 0x1F4)
    OP_68(14900, 1850, 6600, 3000)

    def lambda_8CBB():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8CBB)
    WaitChrThread(0x8, 1)

    def lambda_8CD9():
        OP_95(0xFE, 18000, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8CD9)
    SetChrSubChip(0x105, 0x0)
    Sleep(500)
    SetChrSubChip(0x109, 0x2)
    Sleep(700)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    ClearMapObjFlags(0x0, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_8D32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8D32)

    def lambda_8D43():
        OP_95(0xFE, 19500, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8D43)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Fade(500)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    SetChrSubChip(0x102, 0x2)
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0314
    ChrTalk(
        0x101,
        (
            "#5P#00006F……总之，先在终端上\x01",
            "确认一下支援请求吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#00100F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetScenarioFlags(0x128, 1)
    OP_29(0xA1, 0x1, 0xC)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_26_8663 end

    def Function_27_8EA3(): pass

    label("Function_27_8EA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14100, 850, 9500, 45)
    SetChrPos(0x105, 15600, 850, 8000, 45)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0316
    ChrTalk(
        0x101,
        (
            "#00000F#6P目前的紧急请求\x01",
            "都在克洛斯贝尔市内呢。\x02\x03",

            "#00004F数量不多，\x01",
            "应该可以全部解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x102,
        (
            "#00104F#12P财团这件委托说不定\x01",
            "和缇欧有什么关系……\x02\x03",

            "#00102F另外还有小桃的委托，\x01",
            "如果可以，我想替她解决呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0318
    ChrTalk(
        0x109,
        (
            "#6P#10100F好，那我们就在处理这些紧急委托的同时，\x01",
            "抽空去旧城区的交换店打探一下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9067():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9067)
    Sleep(100)

    def lambda_9077():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9077)
    Sleep(50)

    def lambda_9087():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9087)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    #C0319
    ChrTalk(
        0x101,
        "#00002F#5P嗯，就这么办。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x105,
        (
            "#12P#10304F不过，现在还下着雨呢，\x01",
            "我们不用太着急，慢慢来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetScenarioFlags(0x128, 2)
    OP_29(0xA1, 0x1, 0xD)
    Call(0, 67)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7150", "ed7562")
    ReplaceBGM("ed7101", "ed7562")
    ReplaceBGM("ed7116", "ed7562")
    ReplaceBGM("ed7117", "ed7562")
    Sleep(500)
    PlayBGM("ed7562", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_27_8EA3 end

    def Function_28_914E(): pass

    label("Function_28_914E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x140, 0)
    OP_29(0xA3, 0x4, 0x2)
    OP_29(0xA3, 0x1, 0x0)
    OP_C9(0x0, 0x1000)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_32(0x6, 0x0, 0x3A)
    OP_42(0x6, 0x3EB, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 65890, 0, 1800, 225)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14000, 850, 9400, 45)
    SetChrPos(0x105, 15500, 850, 7900, 45)
    SetChrPos(0x104, 14000, 850, 7900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 18)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14000, 850, 9400, 45)
    SetChrPos(0x105, 15500, 850, 7900, 45)
    SetChrPos(0x104, 14000, 850, 7900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0321
    ChrTalk(
        0x101,
        (
            "#00003F#5P紧急委托来自警备队\x01",
            "和乌尔斯拉医院这两个地方……\x02\x03",

            "#00002F话说回来，真没想到会接到\x01",
            "道格拉斯教官的委托啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0322
    ChrTalk(
        0x102,
        (
            "#00105F#11P道格拉斯教官？\x01",
            "就是那位新上任的警备队副司令吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_93CA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_93CA)
    Sleep(100)

    def lambda_93DA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_93DA)
    Sleep(50)

    def lambda_93EA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93EA)
    WaitChrThread(0x101, 2)

    #C0323
    ChrTalk(
        0x101,
        (
            "#00004F#5P嗯，他在就任为副司令之前，\x01",
            "担任的职务是警察学校的教官。\x02\x03",

            "#00000F从提高基础体力，\x01",
            "到格斗训练、旋棍压制术等，\x01",
            "我都接受过他的严格教导呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x109,
        (
            "#6P#10102F听说他以前是警备队\x01",
            "倍受期待的人物。\x02\x03",

            "#10106F但因为不讨前警备队司令的喜欢，\x01",
            "便被委派了那种闲职……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        (
            "#6P#00304F在演习的时候，我也受到过他的关照，\x01",
            "是个相当厉害的老兄呢。\x02\x03",

            "#00302F在战斗力方面，\x01",
            "他多半是警备队中的最强者。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_957D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_957D)
    Sleep(50)

    def lambda_958D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_958D)
    WaitChrThread(0x101, 2)

    #C0326
    ChrTalk(
        0x102,
        (
            "#00104F#11P原来如此……\x01",
            "听起来真是个厉害的人物啊。\x02\x03",

            "#00100F考虑到我们与警备队的关系，\x01",
            "还是过去和他见个面为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#00002F#5P嗯，过去打个招呼吧。\x02\x03",

            "#00003F另一个委托来自刚刚来到\x01",
            "乌尔斯拉医院赴任的教授……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#6P#00306F也就是取代约亚西姆，\x01",
            "接管药物学与神经科这两个部门的负责人……\x02\x03",

            "#00301F呼，让人不由自主地心生警觉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x105,
        (
            "#12P#10304F说起来，赛兰德……\x01",
            "似乎有些耳熟呢。\x02\x03",

            "#10300F没记错的话，这个姓氏在\x01",
            "雷米菲利亚好像相当有名吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#00102F#11P雷米菲利亚的一家医疗机械\x01",
            "制造公司就叫赛兰德公司。\x02\x03",

            "赛兰德家族是与大公家族都颇有渊源的名门，\x01",
            "那位教授或许就是赛兰德家族的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#00006F#5P嗯……既然如此，\x01",
            "应该不会是什么可疑人物了……\x02\x03",

            "#00001F先不管这些了。\x01",
            "教授要谈的事情好像还涉及那种药物，\x01",
            "怎么说都得去一趟乌尔斯拉医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x105,
        (
            "#12P#10309F呵呵，而且那里还有\x01",
            "你憧憬的姐姐呢。\x02\x03",

            "#10302F听说她非常适合穿护士服，\x01",
            "是个像圣女一样的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_98FC():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_98FC)
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0333
    ChrTalk(
        0x101,
        (
            "#00005F#5P这……！？\x02\x03",

            "#00012F哪、哪有的事，只是因为我\x01",
            "从小就一直受塞茜尔姐姐的照顾……\x02\x03",

            "#00011F等等，瓦吉！\x01",
            "你明明没见过她，为何会知道这些！？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x104,
        "#6P#00309F抱歉抱歉，是我说出去的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0335
    ChrTalk(
        0x101,
        "#00013F#5P兰、兰迪……你这家伙！\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#00111F#11P（……罗伊德，\x01",
            "  未免也太紧张了吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x109,
        (
            "#6P#10112F（好像完全被说中了心事呢……）\x02\x03",

            "#10102F（但塞茜尔小姐确实是一位非常出色的女性，\x01",
            "  倒也可以理解……）\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#00003F#5P……咳咳。\x01",
            "算了，先不说这些了。\x02\x03",

            "#00000F和那位医生见面之前，\x01",
            "我有些事情想问问塞茜尔姐姐。\x02\x03",

            "#00008F……不知医院的各位有没有从约亚西姆\x01",
            "造成的创伤中重新振作起来，实在是很担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#00106F#11P说的也是呢……\x02\x03",

            "#00100F对了，小滴今天\x01",
            "来市里了吧？\x02\x03",

            "琪雅刚才好像去\x01",
            "协会找她玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#00004F#5P嗯，她说今天要和\x01",
            "小滴好好玩上一整天，\x01",
            "兴高采烈地出门去了。\x02\x03",

            "#00002F她们应该就在协会，\x01",
            "要是有时间，我们就过去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x102,
        "#00109F#11P嗯，好的。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x105,
        (
            "#12P#10305F小滴就是\x01",
            "『风之剑圣』的女儿吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        (
            "#6P#00304F嗯，她的年纪\x01",
            "和阿琪差不多大。\x02\x03",

            "#00302F那孩子非常乖巧，完全不像是\x01",
            "那个顽固大叔的女儿呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9D66")

    #C0344
    ChrTalk(
        0x109,
        (
            "#6P#10109F呵呵……\x01",
            "小滴确实很可爱。\x02\x03",

            "#10102F芙兰也见过她，\x01",
            "之后还一直极力称赞。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DCD")

    label("loc_9D66")


    #C0345
    ChrTalk(
        0x109,
        (
            "#6P#10109F我也听过传闻，\x01",
            "据说是个非常可爱的小女孩呢。\x02\x03",

            "#10102F芙兰见到过她，\x01",
            "之后还一直极力称赞。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DCD")


    #C0346
    ChrTalk(
        0x105,
        (
            "#12P#10300F呵呵，原来如此。\x02\x03",

            "#10304F也就是说，我们今天要去和这几位打个招呼，\x01",
            "顺便巡视一下克洛斯贝尔各地的情况。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)
    Sleep(300)

    #C0347
    ChrTalk(
        0x105,
        (
            "#11P#10302F同时还要调查\x01",
            "『赤色星座』的动向。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_9ED4():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9ED4)
    Sleep(50)

    def lambda_9EE4():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9EE4)
    Sleep(50)

    def lambda_9EF4():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9EF4)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(150)

    #C0348
    ChrTalk(
        0x101,
        "#00013F#5P瓦吉……！\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x109,
        "#6P#10101F你、你真是的……！\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        (
            "#6P#00306F……嗯，没错，\x01",
            "这家伙的提议很正确。\x02\x03",

            "#00303F身为他们的亲人，我也许不该这样说，\x01",
            "但那些家伙实在是很危险。\x02\x03",

            "#00301F在旧矿山埋下炸药的人\x01",
            "多半就是他们。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9FF2():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9FF2)
    Sleep(50)

    def lambda_A002():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A002)
    Sleep(50)

    def lambda_A012():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A012)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(150)

    #C0351
    ChrTalk(
        0x101,
        "#00005F#5P兰迪……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x102,
        (
            "#00108F#11P那个……你也不用\x01",
            "太早下结论……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x104,
        (
            "#6P#00303F我非常了解\x01",
            "叔叔和谢莉。\x02\x03",

            "#00308F虽然现在还无法断言……\x01",
            "但我认为他们是在测试支援科的实力。\x02\x03",

            "#00301F测试这个我舍弃老巢之后所选择的\x01",
            "新队伍究竟有多少能耐。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        "#00101F#11P……！\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x109,
        "#5P#10108F只、只为这个就……？\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#00008F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x105,
        (
            "#11P#10303F也就是说，他们并不是为了加害我们。\x02\x03",

            "#10300F仅仅出于好奇心，\x01",
            "就能做出那样的事情？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x104,
        (
            "#6P#00306F嗯，对他们来说，\x01",
            "那种陷阱就和打个招呼差不多。\x02\x03",

            "#00301F从这个角度来说，虽然我好不容易才归队，\x01",
            "但接下来，最好还是由我一个人去调查他们的动向……\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#00006F#5P从这个角度来说，就更不能让你单独行动了。\x02\x03",

            "#00008F我们的确不能对\x01",
            "『赤色星座』放任不管。\x02\x03",

            "早晚都要查出他们来\x01",
            "克洛斯贝尔的目的，\x01",
            "还有他们与帝国政府之间的关系。\x02\x03",

            "#00001F但是……\x01",
            "这是我们整个特别任务支援科的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x104,
        "#6P#00305F罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        (
            "#00003F#5P我们很需要兰迪，\x01",
            "也不打算让兰迪独自行动。\x02\x03",

            "#00001F而且，就算你真的独自行动，\x01",
            "现阶段恐怕也没有什么头绪吧？\x02\x03",

            "既然如此……\x01",
            "就不要轻易提出单独行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x104,
        "#6P#00308F………………………………\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x105,
        (
            "#11P#10309F呵呵，还是这么\x01",
            "擅长劝说别人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x109,
        (
            "#5P#10101F说、说的没错！\x02\x03",

            "在特殊时期要齐心协力，\x01",
            "这样才能算是特别任务支援科吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x102,
        (
            "#00104F#11P嗯，不错。\x02\x03",

            "#00100F教团事件发生时，\x01",
            "我们也是一起渡过难关的。\x02\x03",

            "兰迪，这次不是也一样吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x104,
        (
            "#6P#00304F……哈哈。\x02\x03",

            "#00302F抱歉，我好像说了些\x01",
            "很没意义的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        (
            "#00006F#5P嗯，你明白就好。\x02\x03",

            "#00000F总之，我们现在已经有车了，\x01",
            "今天就在处理支援请求的同时，\x01",
            "开车去郊外转转吧。\x02\x03",

            "顺便还可以到贝尔加德门\x01",
            "和阿尔摩利卡村看看。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A617():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A617)
    Sleep(50)

    def lambda_A627():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A627)
    Sleep(150)

    #C0368
    ChrTalk(
        0x102,
        (
            "#00104F#11P说的也是，好久没去过这两个地方了……\x02\x03",

            "#00105F说起来，索妮亚司令现在\x01",
            "就在贝尔加德门吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x109,
        (
            "#6P#10102F嗯，应该是的。\x02\x03",

            "不过，为了应对通商会议，\x01",
            "她现在肯定很忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        (
            "#6P#00304F米蕾优大概也在那边，\x01",
            "去和她见个面也不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵……\x01",
            "那我们就赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当队伍成员超过四人时，\x01",
            "多出的成员将成为\x01",
            "『援护成员』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『援护成员』会在战场外待命，\x01",
            "偶尔出现在ＡＴ顺序栏中，当轮到其出场时，\x01",
            "就会发动各种各样的支援行动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0374
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果在场景中被敌人从背后偷袭，\x01",
            "包括『援护成员』在内的整个队列都会被打乱。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0375
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "因此要认真设置『援护成员』\x01",
            "的装备，随时做好战斗准备。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "队伍成员的替换可以在\x01",
            "主菜单的[TACTICS]项目中改动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，在主菜单的[STATUS]项目中，\x01",
            "还可以启用/禁用\x01",
            "各角色的援护战技。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_1B(0x0, 0x0, 0x1D)
    OP_1B(0x8, 0x0, 0x1E)
    EventEnd(0x5)
    Return()

    # Function_28_914E end

    def Function_29_A95E(): pass

    label("Function_29_A95E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(1000, 1100, 1250, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 1000, 10, 3300, 180)
    SetChrPos(0x102, 1500, 10, 1500, 180)
    SetChrPos(0x104, 1500, 0, 2500, 180)
    SetChrPos(0x109, 500, 0, 1000, 180)
    SetChrPos(0x105, 500, 10, 2000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_AA41():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AA41)
    Sleep(200)

    def lambda_AA5E():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AA5E)
    Sleep(200)

    def lambda_AA7B():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AA7B)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_AAB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AAB6)
    Sleep(400)

    def lambda_AACA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AACA)

    def lambda_AADB():
        OP_96(0xFE, 0x3E8, 0xA, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AADB)
    Sleep(400)

    def lambda_AAF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AAF8)

    def lambda_AB09():
        OP_96(0xFE, 0x3E8, 0xA, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB09)
    WaitChrThread(0x101, 1)

    #C0378
    ChrTalk(
        0x101,
        "#00003F#5P那个……兰迪。\x02",
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

    #A0379
    AnonymousTalk(
        0x104,
        "怎么了，罗伊德？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0380
    ChrTalk(
        0x101,
        (
            "#00008F#5P该怎么说呢……\x01",
            "关于你的父亲……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0381
    ChrTalk(
        0x104,
        (
            "#12P#00306F哦，那件事啊……\x02\x03",

            "#00300F其实我并不是很在意啦。\x01",
            "在那个世界里，这并不算什么稀罕事。\x02\x03",

            "而且，在离开猎兵团的时候，\x01",
            "我和父亲之间就已经没什么关系了。\x02\x03",

            "#00304F当然，肯定不会毫无感觉……\x01",
            "但却也觉得好像松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#00006F#5P……是吗。\x02\x03",

            "#00001F等你有心情的时候，\x01",
            "给我讲讲过去的事吧？\x02\x03",

            "说不定我能\x01",
            "以队长的角度\x01",
            "提出一些想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x104,
        "#12P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#00011F#5P啊，抱歉，\x01",
            "我是不是有些自以为是了？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x104,
        (
            "#12P#00304F哈哈，没有没有。\x02\x03",

            "#00302F我只是在想，\x01",
            "你也成长了不少呢。\x02\x03",

            "#00309F嗯～哥哥我感慨颇深啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_B01D")

    #C0386
    ChrTalk(
        0x101,
        "#00006F#5P你可真是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0387
    ChrTalk(
        0x101,
        (
            "#00008F#5P……总之，在这种时候，\x01",
            "我很想为你做点什么。\x02\x03",

            "#00000F也许我现在还不够可靠，\x01",
            "但所谓的『搭档』，就是要互相依赖吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x104,
        "#12P#00305F罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Sleep(300)
    SetCameraDistance(22000, 1000)

    def lambda_AF46():
        OP_96(0xFE, 0x3E8, 0x0, 0x4E2, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF46)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x101, 0x5)
    Sound(811, 0, 30, 0)
    Sleep(300)

    #C0389
    ChrTalk(
        0x104,
        (
            "#12P#00302F……明白了，我以后\x01",
            "或许会和你好好聊聊。\x02\x03",

            "#00309F到时就要麻烦你了哦──搭档。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        "#00002F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0B0")

    label("loc_B01D")


    #C0391
    ChrTalk(
        0x101,
        "#00006F#5P你可真是……\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        (
            "#12P#00304F……好啦，如果我以后有心情，\x01",
            "说不定会和你聊一聊。\x02\x03",

            "#00300F到时就要麻烦你了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#00000F#5P嗯……！\x02",
    )

    CloseMessageWindow()

    label("loc_B0B0")

    SetChrPos(0x102, 1500, -1000, -4000, 180)
    SetChrPos(0x105, 500, -1000, -4000, 180)

    #N0394
    NpcTalk(
        0x105,
        "瓦吉的声音",
        "#1P#2S哎？你们在干什么？\x02",
    )

    CloseMessageWindow()

    #N0395
    NpcTalk(
        0x102,
        "艾莉的声音",
        "#1P#2S你们两个忘带东西了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_B1AD")
    SetCameraDistance(22500, 1000)
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

    def lambda_B194():
        OP_96(0xFE, 0x3E8, 0x0, 0x2EE, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B194)
    WaitChrThread(0x104, 1)

    label("loc_B1AD")


    def lambda_B1B2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B1B2)

    #C0396
    ChrTalk(
        0x101,
        "#00011F#5P抱歉，马上就出发！\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x104,
        (
            "#5P#00304F好，那我们就开始\x01",
            "处理工作吧。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_B214():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B214)
    Sleep(100)

    def lambda_B231():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B231)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_B258():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B258)
    Sleep(400)

    def lambda_B26C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B26C)
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

    #A0398
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从现在开始，可以驾驶导力车，快速驶往\x01",
            "克洛斯贝尔自治州内的各个地区了。\x02\x03",

            "导力车停在位于西街的特别任务支援科后门，\x01",
            "请多加利用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0100", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_29_A95E end

    def Function_30_B374(): pass

    label("Function_30_B374")

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

    def lambda_B457():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B457)
    Sleep(200)

    def lambda_B474():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B474)
    Sleep(200)

    def lambda_B491():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B491)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_B4CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B4CC)
    Sleep(400)

    def lambda_B4E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B4E0)
    Sleep(400)

    def lambda_B4F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B4F4)

    def lambda_B505():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B505)
    Sleep(300)

    def lambda_B522():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B522)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    #C0399
    ChrTalk(
        0x101,
        "#00003F#11P那个……兰迪。\x02",
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

    #A0400
    AnonymousTalk(
        0x104,
        "怎么了，罗伊德？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0401
    ChrTalk(
        0x101,
        (
            "#00008F#11P该怎么说呢……\x01",
            "关于你的父亲……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0402
    ChrTalk(
        0x104,
        (
            "#6P#00306F哦，那件事啊……\x02\x03",

            "#00300F其实我并不是很在意啦。\x01",
            "在那个世界里，这并不算什么稀罕事。\x02\x03",

            "而且，在离开猎兵团的时候，\x01",
            "我和父亲之间就已经没什么关系了。\x02\x03",

            "#00304F当然，肯定不会毫无感觉……\x01",
            "但却也觉得好像松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#00006F#11P……是吗。\x02\x03",

            "#00001F等你有心情的时候，\x01",
            "给我讲讲过去的事吧？\x02\x03",

            "说不定我能\x01",
            "以队长的角度\x01",
            "提出一些想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x104,
        "#6P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x101,
        (
            "#00011F#11P啊，抱歉，\x01",
            "我是不是有些自以为是了？\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x104,
        (
            "#6P#00304F哈哈，没有没有。\x02\x03",

            "#00302F我只是在想，\x01",
            "你也成长了不少呢。\x02\x03",

            "#00309F嗯～哥哥我感慨颇深啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_BA3C")

    #C0407
    ChrTalk(
        0x101,
        "#00006F#11P你可真是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0408
    ChrTalk(
        0x101,
        (
            "#00008F#11P……总之，在这种时候，\x01",
            "我很想为你做点什么。\x02\x03",

            "#00000F也许我现在还不够可靠，\x01",
            "但所谓的『搭档』，就是要互相依赖吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x104,
        "#6P#00305F罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_B965():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B965)
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

    #C0410
    ChrTalk(
        0x104,
        (
            "#6P#00302F……明白了，我以后\x01",
            "或许会和你好好聊聊。\x02\x03",

            "#00309F到时就要麻烦你了哦──搭档。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        "#00002F#11P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_BAD0")

    label("loc_BA3C")


    #C0412
    ChrTalk(
        0x101,
        "#00006F#11P你可真是……\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x104,
        (
            "#6P#00304F……好啦，如果我以后有心情，\x01",
            "说不定会和你聊一聊。\x02\x03",

            "#00300F到时就要麻烦你了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        "#00000F#11P嗯……！\x02",
    )

    CloseMessageWindow()

    label("loc_BAD0")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    #N0415
    NpcTalk(
        0x105,
        "瓦吉的声音",
        "#2P#2S哎？你们在干什么？\x02",
    )

    CloseMessageWindow()

    #N0416
    NpcTalk(
        0x102,
        "艾莉的声音",
        "#2P#2S你们两个忘带东西了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_BBCD")
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

    def lambda_BBB4():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BBB4)
    WaitChrThread(0x104, 1)

    label("loc_BBCD")


    def lambda_BBD2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BBD2)

    #C0417
    ChrTalk(
        0x101,
        "#00011F#11P抱歉，马上就出发！\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x104,
        (
            "#11P#00304F好，不要着急，\x01",
            "慢慢处理工作吧。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_BC38():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BC38)
    Sleep(100)

    def lambda_BC55():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BC55)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_BC7C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BC7C)
    Sleep(400)

    def lambda_BC90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BC90)
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

    #A0419
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从现在开始，可以驾驶导力车，快速驶往\x01",
            "克洛斯贝尔自治州内的各个地区了。\x02\x03",

            "导力车停在位于西街的特别任务支援科后门，\x01",
            "请多加利用。\x07\x00\x02",
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

    # Function_30_B374 end

    def Function_31_BD98(): pass

    label("Function_31_BD98")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch02710.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    SoundLoad(3605)
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x102, 13900, 900, 2550, 270)
    SetChrPos(0x104, 11300, 900, 2550, 90)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrPos(0x105, 11300, 900, 4600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13900, 900, 6650, 270)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1450, 6600, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0xE)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13400, 1300, 6600, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12400, 1450, 6600, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0xE)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12000, 1300, 6600, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1450, 4600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0xE)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13400, 1300, 4600, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12400, 1450, 4600, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0xE)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12000, 1300, 4600, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 12400, 1450, 2600, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0xE)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 12000, 1300, 2600, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1450, 2600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0xE)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 2600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x7)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12700, 1400, 5500, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x7)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12700, 1400, 3500, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 16000, 750, 5500, 0)
    SetChrSubChip(0xF, 0x7)
    SetChrSubChip(0x11, 0x7)
    SetChrSubChip(0x13, 0x7)
    SetChrSubChip(0x15, 0x7)
    SetChrSubChip(0x17, 0x7)
    SetChrSubChip(0x19, 0x7)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0420
    AnonymousTalk(
        0x101,
        (
            "#00003F原来如此，\x01",
            "正式会议将在明天召开啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0421
    ChrTalk(
        0x8,
        (
            "#5P#01003F嗯，今天的主要活动就是\x01",
            "午宴与各种讨论会。\x02\x03",

            "#01002F到了晚上，除了晚宴之外，\x01",
            "还会安排首脑们观赏彩虹剧团的演出。\x02\x03",

            "顺便一提，所有首脑都会在\x01",
            "米修拉姆的迎宾馆就宿。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x102,
        (
            "#00100F所谓的迎宾馆，\x01",
            "就是哈尔特曼前议长当时的住宅吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        (
            "#6P#00305F哦？是那栋大得不像话的房子啊，\x01",
            "原来已经派上这种用场了。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "#5P#01006F嗯，哈尔特曼犯有\x01",
            "渎职与非法交易等罪行，\x01",
            "需要交付一笔数额惊人的罚金。\x02\x03",

            "#01000F所以那栋宅邸便被没收充公，\x01",
            "如今已经成为迎宾馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x109,
        (
            "#6P#10106F嗯……\x01",
            "这也算是自作自受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x105,
        (
            "#6P#10300F既然如此，米修拉姆那边\x01",
            "肯定已经戒严封锁了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x8,
        (
            "#5P#01003F是的，在通商会议召开期间，\x01",
            "酒店和主题公园都临时休业了。\x02\x03",

            "#01002F已经在那边安排了警备队员，\x01",
            "应该不必担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x101,
        (
            "#00004F#11P明白了。\x02\x03",

            "#00000F那我们就和昨天一样，\x01",
            "继续专心处理各类支援请求吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#5P#01004F就这么办吧。\x02\x03",

            "#01000F有些来宾打算在午宴之后\x01",
            "造访克洛斯贝尔各地。\x02\x03",

            "到时说不定会出现什么问题，\x01",
            "你们可以帮些忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x102,
        "#00104F明白了。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x104,
        (
            "#6P#00306F话说回来，那些来宾\x01",
            "果然不同凡响啊。\x02\x03",

            "#00301F尤其是『铁血宰相』……\x01",
            "绝非等闲之辈。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0432
    ChrTalk(
        0x101,
        (
            "#00006F#5P是啊，随行的雷克特大尉\x01",
            "就已经让人很在意了……\x02\x03",

            "#00008F而宰相的气势就更加惊人，\x01",
            "透着一股压倒性的强大迫力。\x02\x03",

            "#00001F至于共和国的洛克史密斯总统，\x01",
            "看起来倒是和蔼可亲的……\x02\x03",

            "#00005F……不过，雾香小姐\x01",
            "紧随在他的身侧呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)

    #C0433
    ChrTalk(
        0x102,
        (
            "#00103F她可是卡尔瓦德的谍报组织\x01",
            "『洛克史密斯机关』的成员……\x02\x03",

            "#00108F总统虽然以庶民派的作风而闻名，\x01",
            "但同样不是易与之辈啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x109,
        (
            "#5P#10102F说起来，利贝尔的科洛蒂娅公主\x01",
            "真是非常有气质呢。\x02\x03",

            "#10109F随行的尤莉亚准校\x01",
            "也相当帅气！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0435
    ChrTalk(
        0x105,
        (
            "#6P#10305F哦，就是利贝尔王国\x01",
            "王室亲卫队的队长吧？\x02\x03",

            "#10302F听说她有很多\x01",
            "狂热的追随者。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x109,
        "#5P#10112F嗯、嗯……是啊。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#00109F啊哈哈……\x01",
            "其实我也算是其中之一呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(250)

    #C0438
    ChrTalk(
        0x101,
        "#5P#00005F哦，是吗？\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x104,
        (
            "#6P#00302F怎么～？\x01",
            "原来大小姐有这种特殊喜好吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(150)

    #C0440
    ChrTalk(
        0x102,
        (
            "#00102F那倒不是……\x02\x03",

            "#00104F不过，我以前去利贝尔的时候，\x01",
            "观看过王室亲卫队的阅兵仪式……\x02\x03",

            "#00100F后来还出了写真集，\x01",
            "我想都没想就买下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x101,
        "#5P#00012F原、原来如此。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x109,
        "#5P#10101F待会请让我看看那本写真集！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0443
    ChrTalk(
        0x102,
        (
            "#00109F啊哈哈……\x01",
            "嗯，好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x104,
        "#6P#00306F哎呀呀，真是可叹啊。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，男装丽人\x01",
            "也是一种浪漫。\x02\x03",

            "#10302F至于我，比较关注帝国的\x01",
            "那位皇子殿下。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0446
    ChrTalk(
        0x101,
        (
            "#00000F#11P奥利维特皇子……\x01",
            "最近经常听到这个名字。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)

    #C0447
    ChrTalk(
        0x102,
        (
            "#00104F由于皇子殿下参与解决了利贝尔异变事件，\x01",
            "因此成为公众热议的名人。\x02\x03",

            "#00100F在那之后，他还出席了各种活动，\x01",
            "获得了相当不错的评价……\x02\x03",

            "不过，我记得他并没有\x01",
            "皇位继承权。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    #C0448
    ChrTalk(
        0x101,
        (
            "#5P#00001F是吗……\x02\x03",

            "#00005F哎，既然参与解决了\x01",
            "利贝尔异变事件……\x02\x03",

            "#00000F那他应该认识\x01",
            "艾丝蒂尔和约修亚吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        "#00105F啊，如此说来……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x104,
        (
            "#6P#00300F那两个人的交际面很广，\x01",
            "说不定还真的认识呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 1000, 0, -2000, 0)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 1000, 0, -2000, 0)
    Sound(103, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #N0451
    NpcTalk(
        0x9,
        "琪雅的声音",
        "#3605V#30W#12A我回来啦～\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1000, 1100, 1500, 2000)
    MoveCamera(40, 23, 0, 2000)
    SetCameraDistance(22000, 2000)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x105, 0x2)
    Sleep(1300)

    def lambda_CE2B():
        OP_96(0xFE, 0x3E8, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CE2B)

    def lambda_CE45():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_CE45)
    Sleep(1000)

    def lambda_CE59():
        OP_96(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CE59)

    def lambda_CE73():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CE73)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)

    def lambda_CE8C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_CE8C)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x1F4)
    SetChrSubChip(0xA, 0x5)
    OP_6F(0x79)

    #C0452
    ChrTalk(
        0x101,
        "#00002F琪雅、蔡特，欢迎回来。\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xA,
        "#6P#01200F嗷。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_CEE8():
        OP_96(0xFE, 0x3E8, 0x352, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CEE8)
    Sleep(1000)
    Fade(1000)
    OP_68(10600, 1850, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_68(12600, 1850, 6600, 3000)
    EndChrThread(0x9, 0x1)
    SetChrPos(0x9, 5000, 850, 8900, 90)

    def lambda_CF5E():
        OP_96(0xFE, 0x2AF8, 0x352, 0x22C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CF5E)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    SetChrSubChip(0x104, 0x1)
    OP_0D()
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x8, 0x2)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0454
    ChrTalk(
        0x102,
        (
            "#00105F哎呀，小滴\x01",
            "没和你们一起回来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x9,
        (
            "#01106F#5P啊……嗯，她和爸爸\x01",
            "一起回医院了。\x02\x03",

            "#01110F不过，我们一起观看了\x01",
            "大楼的揭幕式哦～\x02\x03",

            "#01109F真是好精彩啊～！\x01",
            "罗伊德，你们是在近处观看的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#00012F嗯，老实说，那座大楼实在是太大了，\x01",
            "站在近处，反倒看得不太清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x104,
        (
            "#12P#00300F#N但确实可以深刻体会到，\x01",
            "那是一座相当惊人的大楼。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0458
    ChrTalk(
        0x109,
        (
            "#6P#10109F呵呵，你们也许看得\x01",
            "比我们更加清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x9,
        (
            "#01109F#5P嗯！\x01",
            "真是很帅气～！\x02\x03",

            "#01110F好像是叫……烟花吧？\x01",
            "那个也很漂亮！\x02\x03",

            "#01102F不过……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    #C0460
    ChrTalk(
        0x101,
        "#00005F怎么了？\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x9,
        (
            "#01104F#5P啊……不，没什么。\x02\x03",

            "#01100F罗伊德，你们还要\x01",
            "出去工作吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x101,
        (
            "#00000F是啊，大概要到傍晚时分才能回来。\x02\x03",

            "科长，您呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0463
    ChrTalk(
        0x8,
        (
            "#5P#01003F我今天会一直留守在这里。\x02\x03",

            "#01002F如果有什么事，我会联络你们的。\x01",
            "不必担心，尽管出门吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        "#00004F好的，那我们这就走了。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x102,
        (
            "#00102F先检查一下终端，\x01",
            "然后再出门吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    Sleep(500)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
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
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 3)
    OP_29(0xA3, 0x1, 0x7)
    OP_29(0xA3, 0x1, 0x8)
    Call(0, 67)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D46D")
    Jump("loc_D472")

    label("loc_D46D")

    OP_29(0x73, 0x4, 0x40)

    label("loc_D472")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_BD98 end

    def Function_32_D478(): pass

    label("Function_32_D478")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14000, 850, 9400, 45)
    SetChrPos(0x105, 15500, 850, 7900, 45)
    SetChrPos(0x104, 14000, 850, 7900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)

    #C0466
    ChrTalk(
        0x101,
        (
            "#00001F#5P发来了不少委托……\x01",
            "每一件都很令人在意呢。\x02\x03",

            "#00006F虽然这个寻找演奏家的任务\x01",
            "有点莫名其妙。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#6P#00309F哎呀呀，那两位游击士姐姐\x01",
            "竟然会提出支援请求。\x02\x03",

            "#00302F虽说是训练这种缺少情趣的工作，\x01",
            "但如果有时间，还真想去帮个忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x109,
        (
            "#6P#10104F呵呵，说不定是个好机会呢。\x02\x03",

            "#10100F至于这个找猫任务的委托者，\x01",
            "好像是那家人呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D67C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D67C)

    def lambda_D689():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D689)
    Sleep(50)

    def lambda_D699():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D699)

    def lambda_D6A6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D6A6)
    WaitChrThread(0x101, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D73E")

    #C0469
    ChrTalk(
        0x101,
        (
            "#00002F#5P啊，就是搬到东街的\x01",
            "本德先生一家吧。\x02\x03",

            "#00004F我们和那只猫也挺有缘分的……\x01",
            "如果可以的话，我想助他们一臂之力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7B7")

    label("loc_D73E")


    #C0470
    ChrTalk(
        0x101,
        (
            "#00002F#5P啊，就是搬到东街的\x01",
            "本德先生一家吧。\x02\x03",

            "#00003F他们现在过得应该很辛苦……\x01",
            "如果可以的话，我想助他们一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7B7")


    #C0471
    ChrTalk(
        0x102,
        (
            "#00104F#11P嗯，我也赞成。\x02\x03",

            "#00100F他们很信任我们，\x01",
            "稍后别忘了过去看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，由于兰花塔的揭幕式，\x01",
            "还有那些大人物的来访，\x01",
            "连街上的气氛都变得欢快起来了。\x02\x03",

            "#10302F到处转一转\x01",
            "也挺有意思的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 4)
    OP_29(0xA3, 0x1, 0x9)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    EventEnd(0x5)
    Return()

    # Function_32_D478 end

    def Function_33_D8D0(): pass

    label("Function_33_D8D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("apl/ch51090.itc", 0x23)
    LoadChrToIndex("apl/ch50092.itc", 0x24)
    LoadChrToIndex("apl/ch51210.itc", 0x25)
    SoundLoad(3606)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01102.itp")
    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA01")
    OP_68(1300, 1850, 11800, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    OP_90(0x101, 1700, 4850, 14100, 180)
    OP_90(0x102, 600, 4850, 14400, 180)
    OP_90(0x104, 1700, 4850, 15400, 180)
    OP_90(0x109, 600, 4850, 15700, 180)
    OP_90(0x105, 1700, 4850, 16700, 180)
    Jump("loc_DA84")

    label("loc_DA01")

    OP_68(1000, 1000, 700, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 300, 0, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x104, 300, 0, -2900, 0)
    SetChrPos(0x109, 1400, 0, -3200, 0)
    SetChrPos(0x105, 300, 0, -4200, 0)

    label("loc_DA84")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 11000, 850, 14000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB21")
    OP_68(1300, 1850, 9800, 3500)
    BeginChrThread(0x101, 3, 0, 34)
    Jump("loc_DBC0")

    label("loc_DB21")

    OP_68(1000, 1000, 2700, 3500)

    def lambda_DB37():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DB37)
    Sleep(200)

    def lambda_DB54():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DB54)
    Sleep(200)

    def lambda_DB71():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DB71)
    Sleep(200)

    def lambda_DB8E():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DB8E)
    Sleep(200)

    def lambda_DBAB():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DBAB)

    label("loc_DBC0")

    FadeToBright(1000, 0)

    def lambda_DBCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DBCE)
    Sleep(400)

    def lambda_DBE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DBE2)
    Sleep(600)

    def lambda_DBF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DBF6)
    Sleep(400)

    def lambda_DC0A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DC0A)
    Sleep(600)

    def lambda_DC1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DC1E)
    OP_0D()
    StopBGM(0xFA0)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD1A")

    #C0473
    ChrTalk(
        0x101,
        "#5P#00002F哎……\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x102,
        (
            "#5P#00109F啊……\x01",
            "好香的味道。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x105,
        (
            "#5P#10302F嘿，闻起来好像是\x01",
            "枫糖果酱的香味呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD88")

    label("loc_DD1A")


    #C0476
    ChrTalk(
        0x101,
        "#00002F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x102,
        (
            "#00109F#11P啊……\x01",
            "好香的味道。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x105,
        (
            "#12P#10302F嘿，闻起来好像是\x01",
            "枫糖果酱的香味呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD88")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)
    OP_68(11000, 1750, 10500, 2000)
    SetCameraDistance(26500, 2000)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_DDCC():
        OP_95(0xFE, 10810, 850, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DDCC)

    def lambda_DDE6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_DDE6)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE8F")
    SetChrPos(0x101, 1700, -850, 9100, 180)
    SetChrPos(0x102, 600, -850, 9400, 180)
    SetChrPos(0x104, 1700, -850, 10400, 180)
    SetChrPos(0x109, 600, -850, 10700, 180)
    SetChrPos(0x105, 1700, -850, 11700, 180)

    label("loc_DE8F")


    def lambda_DE94():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_DE94)
    Sleep(150)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0479
    AnonymousTalk(
        0x9,
        (
            "#3606V#30W啊，罗伊德，\x01",
            "你们果然回来啦～\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE16)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0480
    ChrTalk(
        0x101,
        (
            "#00009F嗯，回来休息一下。\x02\x03",

            "#00000F话说……\x01",
            "难道你烤了蛋糕吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFFA")

    #C0481
    ChrTalk(
        0x9,
        (
            "#01104F#11P嘿嘿……因为我总觉得\x01",
            "大家快要回来了啊～\x02\x03",

            "#01110F所以烤了枫糖蛋糕哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E04E")

    label("loc_DFFA")


    #C0482
    ChrTalk(
        0x9,
        (
            "#01104F#5P嘿嘿……因为我总觉得\x01",
            "大家快要回来了啊～\x02\x03",

            "#01110F所以烤了枫糖蛋糕哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E04E")


    #C0483
    ChrTalk(
        0x104,
        (
            "#00305F哦哦……！\x01",
            "阿琪，你真是聪明体贴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x109,
        "#10109F呵呵，真开心。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x102,
        (
            "#00102F机会难得，\x01",
            "不如我来泡一壶红茶吧？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(27000, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(12600, 2650, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 6650, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2550, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13900, 900, 7000, 270)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, 11300, 900, 4600, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16300, 850, 6400, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 6650, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 4600, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 2550, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1400, 7100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x2)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13100, 1350, 6700, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12400, 1400, 6600, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x2)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12300, 1350, 7100, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1400, 5400, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x2)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1350, 5000, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12400, 1400, 4600, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x1)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1350, 5100, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1400, 3800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x2)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1350, 3400, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 2100, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x23)
    SetChrSubChip(0x1A, 0x2)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1350, 1700, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 2600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x2)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1350, 3100, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 16300, 750, 5500, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    Sleep(500)
    OP_68(12600, 2150, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0486
    ChrTalk(
        0x8,
        (
            "#5P#01005F原来如此，\x01",
            "你们在那种地方偶遇了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        (
            "#00006F#11P是的，不过她这次出现，\x01",
            "似乎并无特殊目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x104,
        (
            "#00301F……『赤色星座』\x01",
            "仍然没有任何行动吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x8,
        (
            "#5P#01004F如果他们有什么动向，\x01",
            "一科的人会联络我们的。\x02\x03",

            "#01002F我理解你的心情，\x01",
            "但不要太过焦躁。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        "#00304F哈哈……知道了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0491
    ChrTalk(
        0x101,
        (
            "#00003F#11P另外，需要注意的\x01",
            "并不是只有『赤色星座』。\x02\x03",

            "#00001F总之，我们就在行动过程中\x01",
            "顺便留意一下是否有什么征兆吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(200)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)

    #C0492
    ChrTalk(
        0x102,
        (
            "#6P#00108F嗯……\x01",
            "各国要人全都逗留在此，如果在这种\x01",
            "时候出什么意外，情况可就严重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x109,
        (
            "#6P#10101F如果有时间，我们也可以\x01",
            "开车去郊外转转。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x9,
        "#6P#01105F罗伊德，你们又要出门了吗～？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    #C0495
    ChrTalk(
        0x101,
        (
            "#00004F#11P是啊，要继续工作了。\x02\x03",

            "#00002F蛋糕真是很美味，\x01",
            "谢谢你啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#5P#00109F呵呵，你的烹饪技术\x01",
            "已经超过我们所有人了呢。\x02\x03",

            "#00102F莫非你向奥斯卡先生\x01",
            "学习了制作技巧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(150)

    #C0497
    ChrTalk(
        0x9,
        "#6P#01109F嘿嘿，猜对啦～\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(150)

    #C0498
    ChrTalk(
        0x9,
        (
            "#6P#01110F啊，还剩下一些，\x01",
            "大家拿去吃吧～\x02\x03",

            "我想应该可以\x01",
            "保存到明天～\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0499
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了五个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20F, 5)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0500
    ChrTalk(
        0x105,
        "#10302F嘿，真体贴啊。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        (
            "#00306F呜呜呜……\x01",
            "爸爸感动得都要哭了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0502
    ChrTalk(
        0x101,
        (
            "#00003F#5P……慢着。\x02\x03",

            "#00013F就算是兰迪，也别想从我手里\x01",
            "抢走琪雅的爸爸这个位置哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(150)

    #C0503
    ChrTalk(
        0x104,
        (
            "#00302F哼，有意思，\x01",
            "你想和我对着干吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x9,
        "#6P#01105F哇～\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x102,
        (
            "#6P#00106F唉……\x01",
            "你们在那里较什么劲啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x109,
        "#6P#10112F啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x105,
        "#10309F真是两个笨到极点的父亲啊。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_32(0xFF, 0xFE, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    OP_4C(0x9, 0xFF)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 123270, 0, 4980, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
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
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 6)
    OP_29(0xA3, 0x1, 0x10)
    OP_C9(0x0, 0x1000)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_33_D8D0 end

    def Function_34_ED92(): pass

    label("Function_34_ED92")


    def lambda_ED97():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ED97)
    Sleep(200)

    def lambda_EDB4():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EDB4)
    Sleep(200)

    def lambda_EDD1():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_EDD1)
    Sleep(200)

    def lambda_EDEE():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EDEE)
    Sleep(200)

    def lambda_EE0B():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EE0B)
    Return()

    # Function_34_ED92 end

    def Function_35_EE21(): pass

    label("Function_35_EE21")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14100, 1750, 12300, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22000, 0)
    SoundLoad(848)
    SoundLoad(3607)
    SoundLoad(3608)
    SetChrPos(0x101, 5000, 0, 15000, 0)
    SetChrPos(0x102, 5000, 0, 15000, 0)
    SetChrPos(0x104, 5000, 0, 15000, 0)
    SetChrPos(0x109, 5000, 0, 15000, 0)
    SetChrPos(0x105, 5000, 0, 15000, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 11000, 850, 14000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 13100, 850, 9300, 0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_70(0xA, 0x0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x14, 0x0, 0x20)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(848, 2, 100, 0)
    Sleep(2000)
    PlayBGM("ed7102", 0)
    SetCameraDistance(24000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_EF90():
        OP_95(0xFE, 11000, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EF90)

    def lambda_EFAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_EFAA)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_EFDB():
        OP_95(0xFE, 14100, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EFDB)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x0, 0x1F4)
    OP_79(0x1)
    ClearMapObjFlags(0x1, 0x10)
    Sound(838, 0, 100, 0)
    OP_24(0x350)
    ClearMapObjFlags(0xA, 0x20)
    OP_70(0xA, 0x32)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0508
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01110F#3607V#30W嗯？喂喂？\x02\x03",

            "#01109F#3608V这里是克洛斯贝尔警察局\x01",
            "的特别任务支援科～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE18)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("少女的声音")

    #A0509
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊……是琪雅吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0510
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105F哇，是缇欧～！\x02\x03",

            "#01109F你又打过来啦～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("缇欧的声音")

    #A0511
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，但和昨天不同，\x01",
            "只是普通的导力通讯。\x02\x03",

            "……莫非……\x01",
            "其他人都不在吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0512
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01100F嗯，科长刚刚\x01",
            "也出门了。\x02\x03",

            "蔡特倒是在这里哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 190, -1, -1)

    #A0513
    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01200F嗷。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("缇欧的声音")

    #A0514
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，是吗。\x02\x03",

            "……其实是因为打不通\x01",
            "罗伊德前辈他们的艾尼格玛。\x02\x03",

            "所以我才直接联系\x01",
            "支援科……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0515
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105F哦～原来是这样啊。\x02\x03",

            "#01111F罗伊德他们刚刚被\x01",
            "一只纯白色的隼\x01",
            "叫出去了～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("缇欧的声音")

    #A0516
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "纯白色的隼……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0517
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01110F嗯，它叫基库，\x01",
            "和蔡特一样，会说话哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("缇欧的声音")

    #A0518
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……看来你们那边\x01",
            "发生了不少事呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(801, 0, 50, 0)
    Sleep(1300)
    SetMessageWindowPos(250, 0, -1, -1)
    SetChrName("女性的声音")

    #A0519
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1S#40W……各位乘客，\x01",
            "让你们久等了。\x02",
        )
    )

    CloseMessageWindow()

    #A0520
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1S#40W由列曼飞往……的飞船……\x01",
            "………即将起飞……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0521
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105F？？？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("缇欧的声音")

    #A0522
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "到时间了呢。\x02\x03",

            "琪雅，再见。\x01",
            "替我问候\x01",
            "罗伊德前辈他们和科长。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0523
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01109F嗯，再见～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 190, -1, -1)

    #A0524
    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01200F嗷。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0xA, 0x4)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1000, 0, -1500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sleep(500)

    #N0525
    NpcTalk(
        0x8,
        "赛尔盖的声音",
        "喂～我回来啦。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F553():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x9, 2, lambda_F553)
    OP_68(1960, 1750, 2650, 2500)
    MoveCamera(40, 17, 0, 2500)
    Sleep(2000)

    def lambda_F584():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F584)

    def lambda_F59E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F59E)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x2D, 0x1F4)
    OP_6F(0x79)

    #C0526
    ChrTalk(
        0x9,
        (
            "#01101F#12P啊，科长～\x02\x03",

            "#01106F你要是稍微早点回来，\x01",
            "就能和缇欧说话了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "#01005F#6P哦？她刚才联系我们了吗？\x02\x03",

            "#01002F都说了些什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x9,
        "#01110F#12P嗯～她说……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 36)
    Sleep(1000)
    OP_68(1960, 2250, 2650, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x8, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x350)
    SetScenarioFlags(0x22, 0)
    NewScene("e3210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_EE21 end

    def Function_36_F6AE(): pass

    label("Function_36_F6AE")


    def lambda_F6B3():
        OP_95(0xFE, 1000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F6B3)
    WaitChrThread(0x8, 1)

    def lambda_F6D1():
        OP_95(0xFE, 10000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F6D1)
    WaitChrThread(0x8, 1)
    Return()

    # Function_36_F6AE end

    def Function_37_F6EB(): pass

    label("Function_37_F6EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x141, 5)
    OP_29(0xA3, 0x1, 0x14)
    OP_29(0xA3, 0x1, 0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F717")
    Jump("loc_F71C")

    label("loc_F717")

    OP_29(0x75, 0x4, 0x40)

    label("loc_F71C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F72D")
    Jump("loc_F732")

    label("loc_F72D")

    OP_29(0x76, 0x4, 0x40)

    label("loc_F732")

    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x103, 16300, 850, 10200, 45)
    SetChrPos(0x101, 14600, 850, 9200, 45)
    SetChrPos(0x102, 15000, 850, 8200, 45)
    SetChrPos(0x104, 13400, 850, 9400, 90)
    SetChrPos(0x109, 15700, 850, 7400, 0)
    SetChrPos(0x105, 17000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 14200, 850, 11900, 135)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 18)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x103, 16300, 850, 10200, 45)
    SetChrPos(0x101, 14600, 850, 9200, 45)
    SetChrPos(0x102, 15000, 850, 8200, 45)
    SetChrPos(0x104, 13400, 850, 9400, 90)
    SetChrPos(0x109, 15700, 850, 7400, 0)
    SetChrPos(0x105, 17000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 14200, 850, 11900, 135)
    ClearChrFlags(0x8, 0x80)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0529
    ChrTalk(
        0x101,
        (
            "#6P#00003F……果然发来了好几件\x01",
            "新的支援请求。\x02\x03",

            "#00001F嗯……每一件都很\x01",
            "让人在意呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x102,
        (
            "#12P#00104F如果时间充裕，\x01",
            "就去处理一下吧。\x02\x03",

            "#00100F反正我们上午\x01",
            "可以自由行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x109,
        (
            "#12P#10100F只要开车，\x01",
            "想去郊外地区也没问题。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA0B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FA0B)
    WaitChrThread(0x103, 2)
    Sleep(150)

    #C0532
    ChrTalk(
        0x103,
        (
            "#00204F#5P开车吗……\x01",
            "真有点期待呢。\x02\x03",

            "#00202F听说那是蔡斯中央工房\x01",
            "开发的导力车吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x104,
        (
            "#6P#00302F嗯！那可是连一科的家伙们\x01",
            "都羡慕不已的最新型。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x101,
        (
            "#6P#00005F不过，缇欧，\x01",
            "你昨天才刚回来，这么一大早\x01",
            "就要四处奔波，真的没问题吗？\x02\x03",

            "#00000F其实你今天上午可以\x01",
            "休息一下——\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x103,
        "#00211F#5P（瞪……）\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x101,
        "#6P#00006F抱歉，我不该这样说。\x02",
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x103,
        "#00206F#5P……真是的。\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x104,
        (
            "#6P#00309F哈哈，总算找到\x01",
            "阿缇归队的感觉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x102,
        (
            "#12P#00109F呵呵……是啊。\x02\x03",

            "#00102F还是得让\x01",
            "缇欧站在终端前，\x01",
            "才能让人感到安心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FC0E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FC0E)
    Sleep(50)

    def lambda_FC1E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FC1E)
    WaitChrThread(0x109, 2)

    #C0540
    ChrTalk(
        0x109,
        (
            "#12P#10109F呵呵，各位的感情\x01",
            "果然很好啊。\x02\x03",

            "#10102F总之……\x01",
            "新生特别任务支援科的\x01",
            "全体成员总算聚齐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x105,
        (
            "#10302F#12P呵呵，你作为队长，\x01",
            "是否也感慨万分呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#6P#00004F嗯……是啊。\x02\x03",

            "#00002F缇欧，\x01",
            "今后也请多多关照啦。\x02\x03",

            "还有，多谢你在那种\x01",
            "紧急时刻及时赶回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x103,
        (
            "#00202F#5P嗯，彼此彼此，\x01",
            "今后请多关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x104,
        (
            "#6P#00302F哈哈，总觉得情绪似乎都\x01",
            "高昂起来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    #C0545
    ChrTalk(
        0x8,
        (
            "#01004F#5P呵呵……\x01",
            "有干劲是好事。\x02\x03",

            "#01002F既然你们这么有精神，\x01",
            "应该就不会被通商会议的\x01",
            "特殊气氛所影响了。\x02\x03",

            "就用你们自己的方式来\x01",
            "参与今天的警备工作吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FE3C():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FE3C)
    Sleep(50)

    def lambda_FE4C():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FE4C)
    Sleep(50)

    def lambda_FE5C():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FE5C)
    Sleep(50)

    def lambda_FE6C():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FE6C)
    Sleep(50)

    def lambda_FE7C():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FE7C)
    Sleep(50)

    def lambda_FE8C():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FE8C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_FEB1():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x101, 2, lambda_FEB1)

    def lambda_FEC3():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x102, 2, lambda_FEC3)

    def lambda_FED5():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x103, 2, lambda_FED5)

    def lambda_FEE7():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x104, 2, lambda_FEE7)

    def lambda_FEF9():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x109, 2, lambda_FEF9)

    def lambda_FF0B():
        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x105, 2, lambda_FF0B)

    #C0546
    ChrTalk(
        0x101,
        "#12P#00000F明白了。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x102,
        (
            "#12P#00100F科长，您稍后要去\x01",
            "警察总部待命吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x8,
        (
            "#01006F#5P是啊，他们把与各方面\x01",
            "交涉的工作塞给了我。\x02\x03",

            "#01000F我主要负责后方支援，\x01",
            "应该不会直接参与兰花塔的\x01",
            "警备工作。\x02\x03",

            "不过，如果发生了什么事，\x01",
            "我一定会通知你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x101,
        "#12P#00003F……好的。\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x109,
        "#12P#10101F麻烦您了！\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x8,
        "#01002F#5P好，那我就先走了。\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2DB4, 0x2AF8, 0x1F4)

    def lambda_10076():
        OP_95(0xFE, 11700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10076)
    WaitChrThread(0x8, 1)
    OP_68(12900, 1750, 9800, 3000)

    def lambda_100A5():
        OP_95(0xFE, 5700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_100A5)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x8, 0x80)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    #C0552
    ChrTalk(
        0x101,
        (
            "#5P#00005F对了……\x01",
            "琪雅在图书馆吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1015E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1015E)
    Sleep(100)

    def lambda_1016E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1016E)

    def lambda_1017B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1017B)
    Sleep(50)

    def lambda_1018B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1018B)

    def lambda_10198():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10198)
    WaitChrThread(0x102, 2)

    #C0553
    ChrTalk(
        0x102,
        (
            "#12P#00104F嗯，她一大早就出门\x01",
            "去图书馆了。\x02\x03",

            "#00100F中午应该就会回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#5P#00002F这样啊……\x01",
            "那应该不会有什么问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x104,
        (
            "#6P#00309F好！我们也\x01",
            "赶快出门吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0556
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧加入队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0557
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在主菜单的[TACTICS]选项中\x01",
            "可以将其设置为战斗队员。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_37_F6EB end

    def Function_38_102ED(): pass

    label("Function_38_102ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(12600, 2450, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x102, 13900, 900, 6650, 270)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetChrPos(0x109, 11300, 900, 2550, 90)
    SetChrPos(0x105, 13900, 900, 2550, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x13, 0x2A)
    ClearMapObjFlags(0x13, 0x4)
    OP_49()
    SetChrPos(0x2A, 12700, 1650, 4600, 0)
    OP_D5(0x2A, 0x0, 0x15F90, 0x0, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    UseItem(0x2FC, 0xFF)
    Sleep(500)
    AddItemNumber(0x2FC, 1)
    PlayBGM("ed7111", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(12600, 1950, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0558
    ChrTalk(
        0x101,
        (
            "#11P#00003F乌尔斯拉间道的河滩\x01",
            "和东克洛斯贝尔街道的尽头吗……\x02\x03",

            "#00001F都是我们最近\x01",
            "很少去的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x104,
        (
            "#6P#00306F虽说目标似乎并没有出现在旧矿山\x01",
            "的幻兽那么庞大……\x02\x03",

            "#00301F但我们还是做足\x01",
            "万全的准备为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x109,
        (
            "#12P#10101F另外……\x01",
            "还要查明幻兽出现的原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x102,
        (
            "#00106F#5P嗯……\x02\x03",

            "#00101F据报告所说，\x01",
            "那一带似乎受到了时、空、幻\x01",
            "这三种上级属性的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x103,
        (
            "#6P#00203F如果上级属性真的在活动，\x01",
            "我应该能感知得到。\x02\x03",

            "#00208F不过，要想查明原因……\x01",
            "恐怕就有点困难了。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x105,
        (
            "#10303F『塔』和『僧院』发生异变的原因，\x01",
            "好像也至今都没有查明呢……\x02\x03",

            "#10305F说起来，坐落在古战场的\x01",
            "『太阳堡垒』也是同样的情况吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0564
    ChrTalk(
        0x101,
        (
            "#5P#00006F嗯，我们进入『太阳堡垒』时，\x01",
            "也遇到了类似的状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x102,
        (
            "#00103F#5P不过，当事件顺利解决之后，\x01",
            "就再也没有发生过任何异常了。\x02\x03",

            "#00108F和『僧院』的情况有所不同，\x01",
            "这次的事件并不是由于『大钟』而引起……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x109,
        (
            "#12P#10106F如此一来，真是很难\x01",
            "判断具体原因啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x104,
        (
            "#6P#00304F总之就\x01",
            "尽力而为吧。\x02\x03",

            "#00300F另外，应该还会有\x01",
            "其它的工作。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(150)

    #C0568
    ChrTalk(
        0x101,
        (
            "#11P#00003F是啊……\x02\x03",

            "#00000F好！先确认一下今天的支援请求，\x01",
            "然后再出发吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x2A, 25600, 1650, 9500, 0)
    SetChrFlags(0x2A, 0x80)
    SetMapObjFlags(0x13, 0x4)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 0)
    OP_29(0xA6, 0x4, 0x2)
    OP_29(0xA6, 0x1, 0x0)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_32(0x6, 0x0, 0x43)
    OP_42(0x6, 0x3ED, 0xFF)
    Call(0, 67)
    EventEnd(0x5)
    Return()

    # Function_38_102ED end

    def Function_39_10987(): pass

    label("Function_39_10987")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 13500, 850, 8500, 45)
    SetChrPos(0x104, 13700, 850, 9900, 90)
    SetChrPos(0x109, 14600, 850, 7400, 45)
    SetChrPos(0x105, 16000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x2B, 15000, 850, 8900, 0)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_10A66():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10A66)
    Sleep(100)

    def lambda_10A76():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10A76)
    Sleep(100)

    def lambda_10A86():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10A86)
    Sleep(100)

    def lambda_10A96():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10A96)
    Sleep(100)

    def lambda_10AA6():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10AA6)
    Sleep(100)

    def lambda_10AB6():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10AB6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0569
    ChrTalk(
        0x101,
        (
            "#00003F#5P果然接到了\x01",
            "不少委托呢……\x02\x03",

            "#00008F这大概是因为亚里欧斯先生\x01",
            "现在不能出动吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x102,
        (
            "#00106F#11P……大概吧……\x02\x03",

            "#00108F科长今天去医院\x01",
            "探望小滴了……\x02\x03",

            "#00101F我们最近最好\x01",
            "也过去看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x104,
        (
            "#5P#00306F是啊……\x01",
            "说起来，阿琪昨天去探望过了。\x02\x03",

            "#00308F……回来之后，情绪显得相当低落。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x103,
        (
            "#6P#00206F嗯……\x01",
            "有些让人担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x109,
        (
            "#12P#10103F反正开车去医院也\x01",
            "用不了多少时间……\x02\x03",

            "#10100F要是有空，\x01",
            "我们就去探望她吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x101,
        "#00000F#5P嗯，就这么办吧。\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x105,
        (
            "#12P#10303F话说回来，复明手术……\x02\x03",

            "#10301F凭借目前的医疗技术，\x01",
            "果然还是很勉强啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        "#00006F#5P……是啊。\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x102,
        (
            "#00108F#11P不过，听说这次的\x01",
            "手术也并不算是\x01",
            "彻底失败……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x2B, 22900, 0, 12700, 0)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 1)
    Call(0, 67)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    EventEnd(0x5)
    Return()

    # Function_39_10987 end

    def Function_40_10DB5(): pass

    label("Function_40_10DB5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis255.itp")
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 7000, 90)
    SetChrPos(0x103, 11300, 900, 3800, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2200, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13900, 900, 7000, 270)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 11300, 900, 5400, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16300, 850, 6400, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x12, 0x29)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x29, 11200, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1450, 7100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x18)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13100, 1300, 6700, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12350, 1450, 7100, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x18)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12300, 1300, 6700, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1450, 5400, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x18)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1300, 5000, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12350, 1450, 5400, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x18)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1300, 5000, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1450, 3800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x18)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1300, 3400, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1450, 2100, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x18)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1300, 1700, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12350, 1450, 2100, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x18)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1300, 1700, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 12350, 1450, 3800, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x18)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 12300, 1300, 3400, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x25)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 16300, 750, 5500, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrSubChip(0xF, 0xA)
    SetChrSubChip(0x11, 0xA)
    SetChrSubChip(0x13, 0xA)
    SetChrSubChip(0x15, 0xA)
    SetChrSubChip(0x17, 0xA)
    SetChrSubChip(0x19, 0xA)
    SetChrSubChip(0x1B, 0xA)
    SetChrSubChip(0x1D, 0xA)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0578
    ChrTalk(
        0x8,
        (
            "#5P#01006F原来如此，\x01",
            "蓝花就是那种药的原料啊。\x02\x03",

            "#01001F既然如此，警方也\x01",
            "不能再袖手旁观了。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x101,
        (
            "#00008F#11P嗯，我们打算和协会合作，\x01",
            "继续进行调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x102,
        (
            "#6P#00101F目前还有其它的\x01",
            "重要案件吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0581
    ChrTalk(
        0x8,
        (
            "#11P#01003F有倒是有，\x01",
            "不过，就交给别的科去办吧。\x02\x03",

            "#01000F不管怎么说，由于要举行调查独立意向的\x01",
            "居民投票，一定程度的混乱恐怕是无法避免的。\x02\x03",

            "尽早查明并清除安全隐患，\x01",
            "才是现在最重要的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x109,
        "#6P#10106F……的确如此啊。\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x105,
        "#10302F#12P这就是所谓的危机管理吧。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        (
            "#6P#00203F那么……\x01",
            "我们今天该做如何安排？\x02\x03",

            "#00200F关于幻兽的调查，我们负责的部分\x01",
            "在昨天就已经结束了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)

    #C0585
    ChrTalk(
        0x104,
        (
            "#00302F#11P嗯，我们可以去帮帮\x01",
            "协会的游击士。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x102, 0x2)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x104, 0x2)
    OP_63(0x105, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(1000)

    #C0586
    ChrTalk(
        0x102,
        "#6P#00105F……怎么了？\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x105,
        "#10305F#12P想到什么了吗？\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    #C0588
    ChrTalk(
        0x101,
        (
            "#00003F#11P嗯……我只是突有此念。\x02\x03",

            "#00001F要不要去『罗赞贝尔克工房』\x01",
            "看一看？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0589
    ChrTalk(
        0x102,
        "#6P#00101F啊……\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x109,
        "#6P#10101F就是那个据说与『结社』有关系的工房……\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x104,
        (
            "#00303F#11P对啊，可以去那里看看……\x01",
            "我之前都忘干净了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_11A1D")

    #C0592
    ChrTalk(
        0x101,
        (
            "#00003F#11P当然了，既然没有搜查令，\x01",
            "我们也不能强行入内搜查。\x02\x03",

            "#00001F可是……那位老人\x01",
            "当时曾对我们这样说过。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0593
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "你们现在似乎也没什么\x01",
            "特别的事要说。\x02\x03",

            "以后有什么\x01",
            "事情的时候再来吧。\x02\x03",

            "看在玲的面子上，我会和你们谈谈的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Jump("loc_11B69")

    label("loc_11A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11AEB")

    #C0594
    ChrTalk(
        0x101,
        (
            "#00006F#11P当然了，既然没有搜查令，\x01",
            "我们也不能强行入内搜查。\x02\x03",

            "#00001F不过，根据玲的描述，\x01",
            "那位老人似乎并非不讲道理的人。\x02\x03",

            "而且，由于伊梅尔达夫人当时的那件委托，\x01",
            "我们和他也算是认识了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B69")

    label("loc_11AEB")


    #C0595
    ChrTalk(
        0x101,
        (
            "#00006F#11P当然了，既然没有搜查令，\x01",
            "我们也不能强行入内搜查。\x02\x03",

            "#00001F不过，根据玲的描述，\x01",
            "那位老人似乎并非不讲道理的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B69")


    #C0596
    ChrTalk(
        0x103,
        (
            "#6P#00203F……嗯，看来有\x01",
            "一去的价值呢。\x02\x03",

            "#00201F但也有一定的危险性。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_11C31")

    #C0597
    ChrTalk(
        0x105,
        (
            "#10304F#12P确实如此，但我们最好\x01",
            "能搞清楚那个神秘少年的目的。\x02\x03",

            "#10302F而且，说不定他现在\x01",
            "就在那座工房里呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CA1")

    label("loc_11C31")


    #C0598
    ChrTalk(
        0x105,
        (
            "#10304F#12P确实如此，但我们最好\x01",
            "能搞清楚那个神秘少年的目的。\x02\x03",

            "#10302F而且，说不定他现在\x01",
            "就在那座工房里呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CA1")


    #C0599
    ChrTalk(
        0x109,
        (
            "#6P#10100F我、我也赞成！\x02\x03",

            "#10106F充满威胁的外国势力\x01",
            "已经在蠢蠢欲动了……\x02\x03",

            "#10101F在这种情况下，我们更不能对\x01",
            "其它的可疑势力置之不理！\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x102,
        (
            "#6P#00106F是啊……\x02\x03",

            "#00101F那我们就直接\x01",
            "前往工房如何？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(250)

    #C0601
    ChrTalk(
        0x101,
        (
            "#00000F#11P嗯，先去看看情况吧。\x02\x03",

            "#00003F……根据具体情况，\x01",
            "也许还需要申请搜查令呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x104,
        (
            "#00303F#11P是啊……\x02\x03",

            "#00300F好，那就立刻\x01",
            "出发吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x9,
        (
            "#6P#01105F#6P啊……\x02\x03",

            "大家现在就要出去工作了吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0604
    ChrTalk(
        0x101,
        (
            "#00005F#11P是啊，我们这就要走了。\x02\x03",

            "#00000F琪雅……\x01",
            "你今天要去图书馆吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x9,
        (
            "#6P#01103F嗯，我想帮小滴\x01",
            "找些盲文书。\x02\x03",

            "#01110F回来的时候，我会顺便去买东西，\x01",
            "你们晚饭有什么想吃的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0606
    ChrTalk(
        0x102,
        (
            "#5P#00105F买东西……？\x01",
            "琪雅，你真的可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x103,
        (
            "#6P#00205F虽说你已经给我们\x01",
            "做过好几次饭了……\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x9,
        (
            "#6P#01104F嗯，我一直在小桃爸爸的店，\x01",
            "还有奥斯卡那里买东西。\x02\x03",

            "#01110F和百货店食品区的\x01",
            "阿姨关系也很好哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0609
    ChrTalk(
        0x101,
        "#00012F#11P从、从什么时候就……\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x104,
        "#00309F#11P哈哈，既然是阿琪，倒也不难理解。\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x8,
        (
            "#5P#01004F既然如此……\x01",
            "最近的天气有些转凉了，\x01",
            "正适合吃火锅呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x109,
        (
            "#6P#10102F啊，这主意不错。\x01",
            "大家一起吃火锅，肯定会很热闹。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x105,
        (
            "#10302F#12P火锅好像属于\x01",
            "东方料理吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x102,
        "#5P#00100F琪雅，可以吗？\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x9,
        (
            "#6P#01103F嗯～应该没问题。\x02\x03",

            "#01101F为了让汤底更加美味，\x01",
            "要去东街的露天摊看看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x104,
        "#00305F#11P噢噢，听起来好像很正统啊。\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x103,
        (
            "#6P#00202F真期待回来\x01",
            "以后的火锅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        (
            "#00009F#11P谢谢啦，琪雅。\x02\x03",

            "#00002F我们今天会\x01",
            "尽量早些回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x9,
        "#6P#01109F嘿嘿……嗯！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    OP_4C(0xA, 0xFF)
    OP_49()
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 0)
    OP_29(0xA6, 0x1, 0x9)
    OP_29(0xA6, 0x4, 0x10)
    OP_29(0xA7, 0x4, 0x2)
    OP_29(0xA7, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12626")
    Jump("loc_1262B")

    label("loc_12626")

    OP_29(0x81, 0x4, 0x40)

    label("loc_1262B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1263C")
    Jump("loc_12641")

    label("loc_1263C")

    OP_29(0x82, 0x4, 0x40)

    label("loc_12641")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12652")
    Jump("loc_12657")

    label("loc_12652")

    OP_29(0x84, 0x4, 0x40)

    label("loc_12657")

    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_10DB5 end

    def Function_41_12674(): pass

    label("Function_41_12674")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 13500, 850, 8500, 45)
    SetChrPos(0x104, 13700, 850, 9900, 90)
    SetChrPos(0x109, 14600, 850, 7400, 45)
    SetChrPos(0x105, 16000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x2B, 15000, 850, 8900, 0)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_12753():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12753)
    Sleep(100)

    def lambda_12763():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12763)
    Sleep(100)

    def lambda_12773():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_12773)
    Sleep(100)

    def lambda_12783():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_12783)
    Sleep(100)

    def lambda_12793():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12793)
    Sleep(100)

    def lambda_127A3():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_127A3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0620
    ChrTalk(
        0x105,
        "#11P#10300F接到了几个新委托呢。\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x104,
        (
            "#5P#00300F怎么办？\x01",
            "先去人偶工房看看，\x01",
            "回来再处理也不迟吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0622
    ChrTalk(
        0x101,
        (
            "#00003F#5P不，到了人偶工房之后，\x01",
            "还不知会遇到怎样的情况。\x02\x03",

            "#00001F如果有比较紧急的委托，\x01",
            "还是优先处理为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x109,
        (
            "#12P#10108F说的也是……\x01",
            "到时说不定还需要\x01",
            "强行搜查呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x102,
        (
            "#00100F#11P好，我们准备就绪之后，\x01",
            "就前往山道中的人偶工房吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x103,
        (
            "#6P#00203F（主题公园的兼职\x01",
            "  让我十分在意呢……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x2B, 22900, 0, 12700, 0)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 1)
    Call(0, 67)
    EventEnd(0x5)
    Return()

    # Function_41_12674 end

    def Function_42_129AF(): pass

    label("Function_42_129AF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    SoundLoad(128)
    SoundLoad(848)
    OP_68(12600, 2650, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 7000, 90)
    SetChrPos(0x103, 11300, 900, 3800, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2200, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 13900, 900, 7000, 270)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 11300, 900, 5400, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 16300, 850, 6400, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x12, 0x29)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x29, 11200, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1450, 7100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x14)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13100, 1350, 6800, 0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12200, 1450, 7100, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x11)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12300, 1300, 6800, 0)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1450, 5200, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x14)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1350, 4900, 0)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12200, 1450, 5200, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x11)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1300, 4900, 0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1450, 3800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x14)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1350, 3500, 0)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1450, 2000, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x14)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1350, 1700, 0)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12200, 1450, 2000, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x11)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1300, 1700, 0)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 12200, 1450, 3800, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x11)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 12300, 1300, 3500, 0)
    SetChrChipByIndex(0x1F, 0x25)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 16300, 750, 5500, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrSubChip(0xF, 0x8)
    SetChrSubChip(0x11, 0x8)
    SetChrSubChip(0x13, 0x8)
    SetChrSubChip(0x15, 0x8)
    SetChrSubChip(0x17, 0x8)
    SetChrSubChip(0x19, 0x8)
    SetChrSubChip(0x1B, 0x8)
    SetChrSubChip(0x1D, 0x8)
    Sound(128, 2, 50, 0)
    OP_68(12600, 2150, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0626
    ChrTalk(
        0x101,
        "#00004F#11P呼，我吃饱了。\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x104,
        (
            "#00309F#11P哎呀，身体正冷着，\x01",
            "能吃到热腾腾的杂烩粥，真是让人高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    #C0628
    ChrTalk(
        0x102,
        (
            "#5P#00102F呵呵，是啊，\x01",
            "里面还放了蛋和鸡肉呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(100)

    #C0629
    ChrTalk(
        0x109,
        "#12P#10109F谢谢啦，琪雅。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0630
    ChrTalk(
        0x103,
        "#6P#00202F味道非常棒哦。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    #C0631
    ChrTalk(
        0x9,
        (
            "#6P#01104F嘿嘿，我只是用了昨天\x01",
            "买的火锅材料而已～\x02\x03",

            "#01110F瓦吉，你吃饱了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    #C0632
    ChrTalk(
        0x105,
        (
            "#10304F#11P……嗯，\x01",
            "实在是太美味了。\x02\x03",

            "#10302F谢谢了，琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x9,
        "#6P#01109F嘿嘿，太好了～\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0634
    ChrTalk(
        0x8,
        (
            "#5P#01004F呼……大家应该都缓过来了吧？\x02\x03",

            "#01000F关于瓦鲁多·瓦雷斯那件事，\x01",
            "接下来将会由警备队进行后续调查。\x02\x03",

            "你们就不必太钻牛角尖了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)

    #C0635
    ChrTalk(
        0x105,
        "#10304F#12P……哈哈，说的也是。\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x101,
        (
            "#00013F#11P但瓦鲁多显然\x01",
            "是从某个渠道得到\x01",
            "『真知』的。\x02\x03",

            "我们必须要\x01",
            "将其查明……！\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x8,
        (
            "#5P#01003F关于这个问题，\x01",
            "二科已经开始调查了。\x02\x03",

            "听说一科也在调查这件事情\x01",
            "是否与外国势力有关。\x02\x03",

            "#01000F总之，不要那么着急。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x101,
        "#00006F#11P……好的。\x02",
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x103,
        (
            "#6P#00200F对了，昨天脱轨事故中损坏的铁轨\x01",
            "已经修复完毕了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x8,
        (
            "#5P#01005F嗯，在昨天傍晚，\x01",
            "其中一边的铁路就可以通车了。\x01",
            "之后通宵赶工，现在已经完全恢复。\x02\x03",

            "#01004F幸好没有造成太严重的后果。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x109,
        "#12P#10106F呼……真是万幸。\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x102,
        (
            "#6P#00103F横贯大陆铁道是条大动脉……\x01",
            "要是一直停运的话，\x01",
            "现在肯定已经引起重大混乱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x104,
        (
            "#00306F#11P要是真出了那种事，\x01",
            "也会成为帝国和共和国\x01",
            "强行介入的好借口。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)

    #C0644
    ChrTalk(
        0x101,
        (
            "#00003F#5P嗯……没错。\x02\x03",

            "#00001F……总之，先查看一下\x01",
            "支援请求吧。\x02\x03",

            "今天的委托\x01",
            "应该已经发来了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    #C0645
    ChrTalk(
        0x102,
        "#6P#00100F好，去看看吧。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sound(848, 2, 100, 0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_70(0xA, 0x0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x14, 0x0, 0x20)
    Sleep(800)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    #C0646
    ChrTalk(
        0x9,
        "#6P#01105F通讯器在响哦。\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x101,
        "#00000F#11P嗯，我去接。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 15000, 850, 5700, 270)
    Sound(812, 0, 100, 0)
    OP_0D()
    OP_92(0x101, 0x3714, 0x300C, 0x1F4)
    OP_68(14100, 1850, 12300, 2500)

    def lambda_13653():
        OP_95(0xFE, 14100, 850, 12300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13653)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    OP_6F(0x1)
    OP_24(0x350)
    Sound(838, 0, 100, 0)
    ClearMapObjFlags(0xA, 0x20)
    OP_70(0xA, 0x32)
    FadeToDark(500, 0, 100)
    OP_0D()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0648
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001F您好，这里是克洛斯贝尔警察局，\x01",
            "特别任务支援科……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男人的声音")

    #A0649
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……早上好，\x01",
            "我是协会的接待员米歇尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0650
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F啊，早上好。\x02\x03",

            "#00001F您已经看过我们那份\x01",
            "关于『结社』的报告了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0651
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯……你们真是帮大忙了。\x02\x03",

            "我们已经联系了列曼总部，\x01",
            "正在分析情报……\x02\x03",

            "但那群家伙来历不明，\x01",
            "我们也无法判断他们已经\x01",
            "展开了何种程度的行动。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0652
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006F……这样啊。\x02\x03",

            "#00005F请问，您就是想通知我们这件事？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0653
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，并不是为了\x01",
            "这件事才打给你们。\x02\x03",

            "我是想问问你们，\x01",
            "最近有没有见到我们这里的\x01",
            "林和艾欧莉娅……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_END)), "loc_13960")
    SetMessageWindowPos(90, 130, -1, -1)

    #A0654
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001F这个……我们昨天在医院\x01",
            "见过她们……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_139A4")

    label("loc_13960")

    SetMessageWindowPos(90, 130, -1, -1)

    #A0655
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F这个……我们前天在\x01",
            "兰花塔和她们见过面……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_139A4")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0656
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是吗……这样啊。\x02\x03",

            "……那两个孩子可真是的，\x01",
            "到底在做什么啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0657
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013F请问……\x01",
            "您联系不上她们了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0658
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，从昨晚开始，\x01",
            "就一直打不通她们的艾尼格玛。\x02\x03",

            "算啦，这种情况也不算很少见，\x01",
            "我倒也不是特别担心。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0659
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F是吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0660
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，不用太在意。\x01",
            "你们好像也很忙吧？\x02\x03",

            "听说调查对象是那个混混头目？\x01",
            "看来会很棘手呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0661
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00008F……嗯，是啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0662
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要是看到那两人，\x01",
            "请立刻联系我哦。\x02\x03",

            "就这样，你们努力加油吧⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0663
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004F嗯，您辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0xA, 0x4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0664
    ChrTalk(
        0x8,
        (
            "#01000F好像是协会的人打来的吧？\x01",
            "出什么事了？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0665
    ChrTalk(
        0x101,
        "#00001F#5P嗯，是的……\x02",
    )

    CloseMessageWindow()
    OP_68(12920, 1850, 6140, 2000)
    MoveCamera(35, 17, 0, 2000)

    def lambda_13CB1():
        OP_96(0xFE, 0x319C, 0x352, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CB1)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    SetChrName("")

    #A0666
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将游击士林和艾欧莉娅从昨晚开始\x01",
            "就失去联系的情况转告给了大家。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0667
    ChrTalk(
        0x102,
        "#6P#00101F她们两人……\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x105,
        (
            "#10301F#12P她们两个都是\x01",
            "相当老练的大姐姐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x104,
        (
            "#00303F#11P是啊，特别是艾欧莉娅小姐，\x01",
            "是我最喜欢的类型之一，仅次于塞茜尔小姐呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    #C0670
    ChrTalk(
        0x103,
        "#6P#00211F没人对这种事情感兴趣……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13F1D")

    #C0671
    ChrTalk(
        0x109,
        (
            "#12P#10106F#N嗯，还真有点担心呢。\x02\x03",

            "#10108F毕竟她们一直都把行程\x01",
            "安排得非常细致合理。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0672
    ChrTalk(
        0x101,
        (
            "#5P#00006F是啊……\x01",
            "之前和她们交手的时候，也能看出\x01",
            "她们的行程可谓争分夺秒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FAC")

    label("loc_13F1D")


    #C0673
    ChrTalk(
        0x109,
        (
            "#12P#10106F#N嗯，还真有点担心呢。\x02\x03",

            "#10101F身为游击士，她们肯定会把\x01",
            "行程表安排得很周全。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0674
    ChrTalk(
        0x101,
        (
            "#5P#00003F是啊……\x01",
            "亚里欧斯先生也是如此。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FAC")


    #C0675
    ChrTalk(
        0x8,
        (
            "#01003F#11P要是有时间，你们就在工作之余\x01",
            "去协会露个面吧。\x02\x03",

            "#01002F在这种时候就得互相帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x101,
        "#5P#00000F嗯，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x9,
        (
            "#6P#01105F罗伊德，\x01",
            "你们要出门了吗～？\x02\x03",

            "#01102F今天能回来吃火锅吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14076():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14076)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0678
    ChrTalk(
        0x101,
        (
            "#5P#00002F嗯，我们今天\x01",
            "一定会尽早回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x102,
        (
            "#5P#00106F抱歉哦，琪雅。\x02\x03",

            "#00108F你特意准备了火锅，\x01",
            "我们昨天却没能赶上。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x9,
        (
            "#6P#01121F没关系，这说明大家\x01",
            "工作很努力呀～\x02\x03",

            "#01109F所以琪雅也要努力，\x01",
            "尽量帮上大家的忙。\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x9, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    #C0681
    ChrTalk(
        0x101,
        "#5P#00002F琪雅……\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x105,
        (
            "#10309F#11P哈哈……\x01",
            "这句话相当有杀伤力呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0683
    ChrTalk(
        0x103,
        (
            "#6P#00204F根据天气预报，\x01",
            "下午就会放晴了……\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x104,
        (
            "#00307F#11P尽快处理完手头的工作，\x01",
            "争取早点回来吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x109,
        "#12P#10102F#N嗯……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 117660, 30, 8100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 0)
    OP_29(0xA8, 0x1, 0xB)
    OP_29(0xA8, 0x1, 0xC)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    SubItemNumber(0x330, 1)
    SubItemNumber(0x331, 1)
    SubItemNumber(0x332, 1)
    SubItemNumber(0x33A, 1)
    Call(0, 67)
    ReplaceBGM("ed7150", -1)
    ReplaceBGM("ed7101", "ed7562")
    ReplaceBGM("ed7116", "ed7562")
    OP_24(0x350)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_42_129AF end

    def Function_43_1454B(): pass

    label("Function_43_1454B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x1)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 11300, 900, 3800, 90)
    SetChrPos(0x102, 13900, 900, 7000, 270)
    SetChrPos(0x103, 13900, 900, 2200, 270)
    SetChrPos(0x104, 11300, 900, 7000, 90)
    SetChrPos(0x109, 13900, 900, 5400, 270)
    SetChrPos(0x105, 11300, 900, 2200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 11300, 900, 5400, 90)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 13900, 900, 3800, 270)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 14120, 850, 10500, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x12, 0x29)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x29, 11200, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0686
    AnonymousTalk(
        0x8,
        "#01003F是吗，你要回去了啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0687
    ChrTalk(
        0x109,
        (
            "#10106F#11P是的……原本打算\x01",
            "在这里学习半年左右……\x02\x03",

            "#10101F但经过慎重考虑之后，\x01",
            "我还是决定返回警备队。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x101,
        "#6P#00006F……是吗………\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x102,
        (
            "#5P#00106F……这也可以理解。\x02\x03",

            "#00108F经受了这次的事件，\x01",
            "警备队遭受了相当大的损伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x104,
        (
            "#5P#00306F嗯，他们现在肯定\x01",
            "迫切需要优秀的年轻队员。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x109,
        (
            "#10112F#11P啊哈哈……\x01",
            "是否优秀，倒不敢确定呢。\x02\x03",

            "#10108F……真抱歉。\x01",
            "重建工作好不容易才告一段落，\x01",
            "终于要恢复正常工作了，而我却……\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x101,
        (
            "#6P#00004F不……你不用在意。\x02\x03",

            "#00002F对现在的克洛斯贝尔来说，\x01",
            "警备队的职责十分重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x103,
        (
            "#00206F#11P虽然有点寂寞……\x01",
            "但也只能接受现实了。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x9,
        (
            "#01108F#11P诺艾尔……\x01",
            "要离开这里了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    #C0695
    ChrTalk(
        0x109,
        (
            "#10112F#5P啊哈哈……嗯。\x02\x03",

            "一想到以后就见不到小琪雅了，\x01",
            "真是十分失落呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x9,
        "#01106F#11P……这样啊………\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x109,
        (
            "#10102F#5P但是，我一定会抽时间\x01",
            "过来玩的……！\x02\x03",

            "#10100F#30W而且还会和芙兰一起来……\x02\x01",

            "#10108F#45W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    #C0698
    ChrTalk(
        0x9,
        "#01112F#11P诺艾尔……\x02",
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x103,
        "#00208F#11P诺艾尔小姐……\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x105,
        (
            "#6P#10301F……听说你妹妹\x01",
            "目前还无法出院？\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x109,
        (
            "#10106F#5P嗯……虽然手术很成功，\x01",
            "神智也已恢复，\x01",
            "应该不必再担心了……\x02\x03",

            "#10113F但体力还是\x01",
            "没有恢复过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x102,
        "#5P#00103F……是吗………\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x104,
        "#5P#00308F………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    #C0704
    ChrTalk(
        0x109,
        (
            "#10112F#11P啊哈哈……前辈，\x01",
            "你别摆出这种表情啊。\x02\x03",

            "#10104F那孩子也是一名警察，\x01",
            "早就做好遭遇危险的心理准备了。\x02\x03",

            "#10100F你可千万不要认为……\x01",
            "自己应该担负责任哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x104,
        (
            "#5P#00304F……哈哈，我知道了。\x02\x03",

            "#00302F说起来，今天就是诺艾尔\x01",
            "在支援科工作的最后一天了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x109,
        (
            "#10104F#11P是的，我今天一定会\x01",
            "竭尽全力来完成工作。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0707
    ChrTalk(
        0x109,
        "#10102F#11P请大家多多关照了。\x02",
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x101,
        "#6P#00004F嗯……彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x102,
        (
            "#5P#00102F诺艾尔小姐……\x01",
            "请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x8,
        (
            "#6P#01003F各种手续就\x01",
            "交给我来办吧。\x02\x03",

            "#01002F另外，好久都没去外面吃饭了，\x01",
            "今天晚上，大家就去外面吃一顿吧。\x02\x03",

            "我请客。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x9, 0x0)

    #C0711
    ChrTalk(
        0x109,
        "#10105F#11P赛尔盖科长……\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x101,
        "#6P#00002F哈哈，真是个好提议。\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x103,
        "#00202F#11P科长真大方啊。\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x105,
        (
            "#6P#10309F呵呵，要不要去\x01",
            "我很熟悉的那家男公关俱乐部？\x02\x03",

            "#10302F我可以召集一群美貌的男公关，\x01",
            "举办一场豪华的送别会。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    #C0715
    ChrTalk(
        0x109,
        "#10111F#5P什么！？\x02",
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x104,
        (
            "#5P#00305F噢，听起来蛮不错的嘛。\x02\x03",

            "#00309F不过，我还是更喜欢\x01",
            "有漂亮大姐姐的店。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(100)

    #C0717
    ChrTalk(
        0x102,
        (
            "#11P#00111F喂……\x01",
            "好像越说越远了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x103,
        (
            "#00201F#11P不然还是去奇幻乐园里那家\x01",
            "正在举办咪西展览的餐厅吧……（双眼发光）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)

    #C0719
    ChrTalk(
        0x9,
        "#01105F#5P还有那种店吗？\x02",
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x8,
        (
            "#6P#01006F你们这些家伙……\x01",
            "也得考虑一下我的钱包啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0721
    ChrTalk(
        0x109,
        "#10112F#11P啊哈哈……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0722
    ChrTalk(
        0x101,
        (
            "#6P#00012F总之，我们今天要在天黑之前\x01",
            "把所有工作处理完。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0xA,
        "#01203F#5P#N咕噜噜……嗷。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    OP_49()
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 2)
    Call(0, 67)
    OP_32(0x6, 0x0, 0x49)
    OP_42(0x6, 0x3EF, 0xFF)
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)
    OP_29(0xAB, 0x1, 0x3)
    OP_29(0xAB, 0x4, 0x10)
    OP_29(0xAC, 0x4, 0x2)
    OP_29(0xAC, 0x1, 0x0)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C9(0x0, 0x10000)
    Sleep(1000)
    EventEnd(0x5)
    Return()

    # Function_43_1454B end

    def Function_44_15405(): pass

    label("Function_44_15405")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 13500, 850, 8500, 45)
    SetChrPos(0x104, 13700, 850, 9900, 90)
    SetChrPos(0x109, 14600, 850, 7400, 45)
    SetChrPos(0x105, 16000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x2B, 15000, 850, 8900, 0)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_154E4():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_154E4)
    Sleep(100)

    def lambda_154F4():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_154F4)
    Sleep(100)

    def lambda_15504():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_15504)
    Sleep(100)

    def lambda_15514():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15514)
    Sleep(100)

    def lambda_15524():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15524)
    Sleep(100)

    def lambda_15534():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_15534)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0724
    ChrTalk(
        0x102,
        "#00108F#11P委托真是不少呢……\x02",
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x103,
        (
            "#6P#00200F不过，好像并没有\x01",
            "特别紧急的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x105,
        (
            "#12P#10300F是啊，阿巴斯提交的那件委托好像\x01",
            "也不是很急，可以等到有空时再去处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x104,
        (
            "#6P#00303F嗯，在各地巡视的同时\x01",
            "慢慢处理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x109,
        "#12P#10101F好！\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0729
    ChrTalk(
        0x101,
        (
            "#00003F#5P对了，各位。\x02\x03",

            "#00002F我们在工作间歇\x01",
            "去乌尔斯拉医院看看吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)

    def lambda_15713():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_15713)
    Sleep(50)

    def lambda_15723():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_15723)
    Sleep(50)

    def lambda_15733():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15733)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0730
    ChrTalk(
        0x109,
        "#12P#10105F哎……\x02",
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x102,
        (
            "#00102F#11P嗯……好提议。\x02\x03",

            "#00104F最近这一个星期，我们实在太忙了，\x01",
            "一直都没有去探望她……\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x104,
        (
            "#6P#00304F我赞成。\x02\x03",

            "#00302F既然芙兰已经醒过来了，\x01",
            "我们当然要去看看她啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x109,
        "#12P#10108F但、但是……\x02",
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x105,
        (
            "#12P#10304F不能通过终端\x01",
            "听到她那充满活力的声音，\x01",
            "真是有些寂寞呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x103,
        (
            "#6P#00201F是啊……\x01",
            "至少要去听听她的声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        (
            "#00004F#5P诺艾尔，你就别客气了。\x02\x03",

            "#00000F对我们来说，芙兰也是\x01",
            "非常重要的后援人员啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15900():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_15900)
    Sleep(50)

    def lambda_15910():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_15910)
    Sleep(50)

    def lambda_15920():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15920)
    Sleep(50)

    def lambda_15930():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_15930)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0737
    ChrTalk(
        0x109,
        (
            "#12P#10104F各位……\x01",
            "非常感谢。\x02\x03",

            "#10102F好，等工作告一段落之后，\x01",
            "我们就去乌尔斯拉医院吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 3)
    OP_29(0xAC, 0x1, 0x1)
    Call(0, 67)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7101", "ed7563")
    ReplaceBGM("ed7116", "ed7563")
    ReplaceBGM("ed7123", "ed7515")
    EventEnd(0x5)
    Return()

    # Function_44_15405 end

    def Function_45_159FC(): pass

    label("Function_45_159FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05901.itp")
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50091.itc", 0x22)
    SoundLoad(848)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 4900, 130, 6250, 180)
    SetChrPos(0x102, 6050, 130, 6250, 180)
    SetChrPos(0x103, 4600, 130, 2200, 0)
    SetChrPos(0x104, 6400, 130, 2200, 0)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5500, 130, 2200, 0)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -900, 0, 4100, 135)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 13800, 850, 13000, 0)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x1D)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 4900, 330, 4600, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x1D)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 6000, 330, 3900, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0738
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W　　　　　 两天后……\x02\x03",

            "为了调查大家对克洛斯贝尔独立一事的意向，\x01",
            "正式举行了居民投票活动……\x02\x03",

            "投票结果在当天进行了公开……\x02\x03",

            "一个星期之后……\x01",
            "克洛斯贝尔迎来了『命运之日』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    UseItem(0x2E9, 0xFF)
    AddItemNumber(0x2E9, 1)
    Sleep(1500)
    Sound(18, 0, 100, 0)
    UseItem(0x2EA, 0xFF)
    AddItemNumber(0x2EA, 1)
    OP_68(6020, 3950, 4710, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22800, 0)
    PlayBGM("ed7251", 0)
    Sleep(1500)
    OP_68(6020, 950, 4710, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(22000, 100000)
    MoveCamera(35, 18, 0, 100000)
    Sleep(500)

    #C0739
    ChrTalk(
        0x101,
        "#5P#00013F………………………………\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x104,
        (
            "#00301F……这下可真是\x01",
            "闹大了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x102,
        (
            "#5P#00106F是啊……\x01",
            "老实说，我完全没想到\x01",
            "事情会发展得这么快。\x02\x03",

            "#00108F……本想找迪塔叔叔\x01",
            "确认一下情况，\x01",
            "但从昨天起，就一直联系不上他……\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        (
            "#12P#00206F科长也是，今天一大早就去了总部，\x01",
            "到现在还没回来……\x02\x03",

            "#00201F他好像是去确认\x01",
            "『国防军』这个组织了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x101,
        (
            "#5P#00006F是啊……\x01",
            "说实话，这可真是猝不及防啊。\x02\x03",

            "#00001F而且措手不及的并非只有我们，\x01",
            "警方高层恐怕也是一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x104,
        (
            "#00306F喂喂……\x01",
            "这未免也太奇怪了吧？\x02\x03",

            "#00301F诺艾尔和米蕾优那边\x01",
            "现在是什么情况？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    #C0745
    ChrTalk(
        0x103,
        (
            "#6P#00208F和警备队也\x01",
            "联系不上了。\x02\x03",

            "大概是因为咨询的人太多，\x01",
            "警备队切断了信号吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x102,
        (
            "#5P#00103F……可以理解。\x02\x03",

            "#00101F另外，关于冻结资产一事……\x01",
            "帝国和共和国肯定\x01",
            "不会善罢甘休的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)

    #C0747
    ChrTalk(
        0x101,
        (
            "#5P#00008F共和国甚至已明确表态『不惜动用武力来解决』……\x01",
            "边境那边的情况很让人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x9,
        "#12P#01108F#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(250)

    #C0749
    ChrTalk(
        0x101,
        (
            "#5P#00002F对不起……\x01",
            "让你感到不安了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x9,
        (
            "#12P#01121F……没关系，\x01",
            "琪雅也知道发生了\x01",
            "严重的情况。\x02\x03",

            "#01105F话说回来，从早上开始，\x01",
            "一直没见到瓦吉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x101,
        "#5P#00005F哎，真的呢……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0752
    ChrTalk(
        0x103,
        (
            "#12P#00205F哦，瓦吉先生出去了，\x01",
            "说是要处理一些私事。\x02\x03",

            "#00200F记得是在科长出门之后走的。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x101,
        "#5P#00001F是吗？\x02",
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x102,
        (
            "#5P#00106F真是的，竟然偏偏选在这种时候擅自行动，\x01",
            "这种行为实在是太我行我素了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    #C0755
    ChrTalk(
        0x104,
        "#00308F嗯……？\x02",
    )

    CloseMessageWindow()
    Sound(808, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x101, 0x2)
    Sleep(250)
    MoveCamera(35, 18, 0, 2000)
    OP_68(2300, 950, 2300, 2000)
    SetCameraDistance(24000, 2000)
    OP_6F(0x79)

    #C0756
    ChrTalk(
        0x102,
        "#00105F在这种时候……\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x104,
        "#00301F会是谁呢……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 4900, 30, 5500, 180)
    OP_0D()
    OP_93(0x101, 0x10E, 0x1F4)

    def lambda_163A3():
        OP_95(0xFE, 3500, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_163A3)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xE1, 0x1F4)

    #C0758
    ChrTalk(
        0x101,
        (
            "#00001F来了！\x01",
            "请问是哪位！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, 1000, -1000, -2000, 0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)

    #N0759
    NpcTalk(
        0xB,
        "女性的声音",
        (
            "#1P#2S太好了……\x01",
            "你们都在啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0760
    NpcTalk(
        0xB,
        "女性的声音",
        "#1P#2S是我，塞茜尔。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0761
    ChrTalk(
        0x101,
        "#00011F塞茜尔姐姐！？\x02",
    )

    CloseMessageWindow()

    def lambda_16505():
        OP_95(0xFE, 1000, 0, 2500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16505)
    WaitChrThread(0x101, 1)

    def lambda_16523():
        OP_95(0xFE, 1000, 0, 1000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16523)
    WaitChrThread(0x101, 1)
    Sound(806, 0, 80, 0)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_16550():
        OP_96(0xFE, 0x3E8, 0x0, 0xAF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16550)
    Sleep(500)
    SetChrPos(0xB, 1000, 0, -1500, 0)

    def lambda_1657E():
        OP_96(0xFE, 0x3E8, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1657E)

    def lambda_16598():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_16598)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x101, 1)

    #C0762
    ChrTalk(
        0x9,
        "#12P#01110F啊，是塞茜尔～\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 46)
    Sleep(250)
    OP_68(4500, 1100, 3300, 2000)
    OP_93(0x101, 0x2D, 0x1F4)

    def lambda_165F1():
        OP_95(0xFE, 2000, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_165F1)
    Sleep(500)

    def lambda_1660E():
        OP_95(0xFE, 2000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1660E)
    WaitChrThread(0x101, 1)

    def lambda_1662C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1662C)
    WaitChrThread(0xB, 1)

    def lambda_1663D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1663D)
    OP_6F(0x79)

    #C0763
    ChrTalk(
        0x102,
        (
            "#5P#00105F塞茜尔小姐……\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x104,
        (
            "#00302F你竟然会来这里，\x01",
            "真是稀奇啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0765
    AnonymousTalk(
        0xB,
        (
            "抱歉，\x01",
            "突然跑来打搅。\x02\x03",

            "请问……亚里欧斯先生有没有\x01",
            "来你们这里？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0766
    ChrTalk(
        0x101,
        "#00005F#5P……亚里欧斯先生？\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x103,
        (
            "#12P#00205F他没来过呢……\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0xB,
        (
            "#6P#05926F……其实………\x02\x03",

            "#05928F他昨天深夜来到医院，\x01",
            "把小滴带走了。\x02\x03",

            "而且还当场办理了\x01",
            "出院手续……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0769
    ChrTalk(
        0x101,
        "#00005F#5P什么！？\x02",
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x102,
        "#5P#00101F这……！？\x02",
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x9,
        "#12P#01112F小滴被……\x02",
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0xB,
        (
            "#6P#05926F所以我想搞清楚，\x01",
            "这到底是怎么一回事……\x02\x03",

            "但协会的米歇尔先生\x01",
            "也是一头雾水。\x02\x03",

            "#05921F慎重起见，\x01",
            "我就来你们这里看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x101,
        "#00001F#5P这样啊……\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x104,
        (
            "#00301F那个大叔……\x01",
            "为何要做那种事？\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x103,
        (
            "#12P#00201F大半夜突然跑到医院，\x01",
            "似乎有些反常呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x9,
        "#12P#01108F………………………………\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_70(0xA, 0x0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x14, 0x0, 0x20)
    Sound(848, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(14100, 1750, 12300, 3000)
    MoveCamera(40, 17, 0, 3000)
    SetCameraDistance(22500, 3000)
    SetChrSubChip(0x9, 0x2)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)

    def lambda_16AE0():
        TurnDirection(0x101, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16AE0)
    Sleep(50)

    def lambda_16AF0():
        TurnDirection(0x102, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_16AF0)
    Sleep(50)

    def lambda_16B00():
        TurnDirection(0xB, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_16B00)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xB, 0)
    OP_6F(0x79)

    #C0777
    ChrTalk(
        0x101,
        "#00011F哦……\x02",
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x104,
        (
            "#00301F没有呼叫艾尼格玛，\x01",
            "应该不是科长打来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x102,
        "#00105F难道和亚里欧斯先生有关？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(24000, 5000)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 49)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 50)
    Sleep(500)
    BeginChrThread(0x9, 3, 0, 51)
    Sleep(200)
    BeginChrThread(0xB, 3, 0, 52)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    Sleep(300)
    OP_24(0x350)
    Sound(838, 0, 100, 0)
    ClearMapObjFlags(0xA, 0x20)
    OP_70(0xA, 0x32)
    Sleep(500)

    #C0780
    ChrTalk(
        0x101,
        (
            "#11P#00001F您好，这里是克洛斯贝尔警察局，\x01",
            "特别任务支援科……\x02",
        )
    )

    WaitChrThread(0xB, 3)
    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0781
    NpcTalk(
        0xE,
        "女性的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S#5P太好了！\x01",
            "罗伊德，你在啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x101,
        "#11P#00011F哇……！\x02",
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x103,
        (
            "#6P#00200F通话模式好像\x01",
            "设置成免提了。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x102,
        "#12P#00105F这声音是……格蕾丝小姐？\x02",
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x104,
        "#12P#00300F好像是。\x02",
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x101,
        (
            "#11P#00000F那个……\x01",
            "格蕾丝小姐，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P居然还问有什么事……\x01",
            "出大事了！我想也应该通知你们一声！\x02\x03",

            "刚刚从兰花塔那边\x01",
            "传来一条重大通告！\x02\x03",

            "迪塔市长已经就任为\x01",
            "『克洛斯贝尔独立国』\x01",
            "的首任总统了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0788
    ChrTalk(
        0x101,
        "#11P#00007F什、什么……\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x103,
        "#6P#00205F首任总统……\x02",
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x102,
        (
            "#12P#00107F迪、迪塔叔叔他……\x01",
            "就任为总统！？\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x104,
        (
            "#12P#00305F喂喂……\x01",
            "你真的不是在开玩笑吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P我、我一开始也以为\x01",
            "只是在开玩笑啊！\x02\x03",

            "但是，前来通知我们的人\x01",
            "是穿着白色军服的士兵……\x02\x03",

            "而且他们还自称是刚刚宣布\x01",
            "成立的『国防军』的成员呢！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x101,
        "#11P#00013F真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x104,
        "#12P#00301F既然是士兵，莫非是……\x02",
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P嗯，大概是警备队的\x01",
            "成员吧……\x02\x03",

            "还、还有，你们听了之后可别吃惊哦……\x02\x03",

            "迪塔总统就任之后，\x01",
            "立刻就任命了『国防长官』。\x02\x03",

            "其人选竟然是…#350W…\x01",
            "#20W亚里欧斯先生。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)

    #C0796
    ChrTalk(
        0x101,
        "#11P#00005F……哎？\x02",
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x102,
        "#12P#00105F#30W……这……\x02",
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x104,
        "#12P#00303F#30W嗯……？\x02",
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x103,
        "#6P#00208F#30W亚里欧斯……先生……？\x02",
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0xB,
        "#6P#05925F#30W………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xB)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("罗伊德等人")
    Fade(500)
    SetCameraDistance(24500, 1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)

    #A0801
    AnonymousTalk(
        0xFF,
        "#5S#16A什么！？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(500)

    #C0802
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P现在的时间刚好，\x01",
            "总统的就任演讲马上就要开始了！\x02\x03",

            "据说会在导力网络中同步直播，\x01",
            "你们也看看吧！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0803
    NpcTalk(
        0xE,
        "青年的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#1S……格蕾丝前辈！\x01",
            "总算得到采访许可了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#2S很好！\x01",
            "干得漂亮，雷因兹！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    #C0805
    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#3S不好意思！\x01",
            "我现在要去就任演讲现场采访了！\x02\x03",

            "下次再聊吧～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0xA, 0x4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xB)
    Sleep(500)

    #C0806
    ChrTalk(
        0xB,
        "#6P#05928F刚才说的……都是真的吗？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0807
    ChrTalk(
        0x101,
        (
            "#00006F我、我也不敢确定……\x02\x03",

            "#00013F亚里欧斯先生竟然\x01",
            "出任『国防长官』一职……？\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x102,
        (
            "#12P#00107F所谓的长官，\x01",
            "也就是『国防军』的首领……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x104,
        (
            "#12P#00310F不、不可能吧……\x01",
            "那他游击士这层身份要怎么办！？\x02\x03",

            "#00306F迪塔大叔就任为\x01",
            "总统这件事也非常唐突……\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x103,
        (
            "#6P#00201F……总之，我们先在终端上\x01",
            "观看就任演讲吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x101,
        "#00007F好……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x350)
    SetScenarioFlags(0x22, 4)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_159FC end

    def Function_46_175DD(): pass

    label("Function_46_175DD")

    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 6050, 30, 5500, 180)
    OP_0D()

    def lambda_17606():
        OP_95(0xFE, 4750, 30, 5500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17606)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0xE1, 0x1F4)
    Return()

    # Function_46_175DD end

    def Function_47_17627(): pass

    label("Function_47_17627")

    SetChrPos(0x101, 4100, 850, 10800, 90)

    def lambda_1763D():
        OP_96(0xFE, 0x3138, 0x352, 0x2A30, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1763D)
    WaitChrThread(0x101, 1)

    def lambda_1765B():
        OP_95(0xFE, 14100, 850, 12300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1765B)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_47_17627 end

    def Function_48_1767C(): pass

    label("Function_48_1767C")

    SetChrPos(0x102, 4300, 850, 10200, 90)

    def lambda_17692():
        OP_96(0xFE, 0x37DC, 0x352, 0x27D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17692)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_48_1767C end

    def Function_49_176B3(): pass

    label("Function_49_176B3")

    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 2650, 850, 9600, 90)

    def lambda_176D6():
        OP_96(0xFE, 0x316A, 0x352, 0x2580, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_176D6)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x101, 500)
    Return()

    # Function_49_176B3 end

    def Function_50_176F7(): pass

    label("Function_50_176F7")

    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 2200, 850, 11000, 90)

    def lambda_1771A():
        OP_96(0xFE, 0x2FA8, 0x352, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1771A)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_50_176F7 end

    def Function_51_1773B(): pass

    label("Function_51_1773B")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 800, 850, 10300, 90)

    def lambda_17759():
        OP_96(0xFE, 0x2A30, 0x352, 0x283C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17759)
    WaitChrThread(0x9, 1)
    Return()

    # Function_51_1773B end

    def Function_52_17773(): pass

    label("Function_52_17773")

    SetChrPos(0xB, 800, 850, 11500, 90)

    def lambda_17789():
        OP_96(0xFE, 0x2A30, 0x352, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17789)
    WaitChrThread(0xB, 1)
    Return()

    # Function_52_17773 end

    def Function_53_177A3(): pass

    label("Function_53_177A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("chr/ch08201.itc", 0x1F)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(15900, 2250, 9800, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x103, 16300, 850, 10200, 45)
    SetChrPos(0x101, 15150, 870, 8450, 45)
    SetChrPos(0x102, 16200, 850, 7400, 0)
    SetChrPos(0x104, 17200, 850, 7800, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14500, 850, 10500, 90)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 13900, 850, 9700, 90)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    PlayBGM("ed7561", 0)
    OP_68(15900, 1750, 9800, 3000)
    FadeToBright(2000, 0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xB)
    OP_64(0x9)
    Sleep(500)

    #C0812
    ChrTalk(
        0x101,
        "#6P#00008F………………………………\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1798B():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1798B)
    Sleep(50)

    def lambda_1799B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1799B)
    Sleep(50)

    def lambda_179AB():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_179AB)
    Sleep(50)

    def lambda_179BB():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_179BB)
    Sleep(50)

    def lambda_179CB():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_179CB)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x101, 2)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0813
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F您好，我是罗伊德……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0814
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……哦，是我。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0815
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010F科长！\x01",
            "刚才的就任演讲究竟……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0816
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……嗯，我也看了。\x02\x03",

            "暂且不论是非对错，\x01",
            "总之，警备队已经完全\x01",
            "重组为『国防军』了。\x02\x03",

            "我们警察局也将\x01",
            "被收编到其中。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0817
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006F怎、怎么会这样……\x02\x03",

            "#00013F难道说，\x01",
            "连索妮亚司令也……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0818
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "她也出现在画面中了吧？\x01",
            "那就表示，她应该已经接受了这种决定。\x02\x03",

            "目前还不知道局势会如何发展……\x01",
            "总之，你们最近要注意一些，\x01",
            "不要随意接近兰花塔。\x02\x03",

            "国防军的士兵们正在\x01",
            "严密守卫着那里。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0819
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010F这……我明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0820
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我会再联络你们的，\x01",
            "千万不要太过冲动，擅自行动哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0821
    ChrTalk(
        0x102,
        "#12P#00108F……科长说了什么？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)

    #C0822
    ChrTalk(
        0x101,
        "#5P#00006F嗯，他说国防军……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0823
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将赛尔盖的话转告给了艾莉等人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0824
    ChrTalk(
        0x102,
        "#12P#00106F是吗……\x02",
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x104,
        (
            "#00301F#12P啧，竟然连索妮亚司令\x01",
            "都加入他们那边了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x103,
        (
            "#5P#00206F不过，以她的立场来说，\x01",
            "这也是无可奈何的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0xB,
        (
            "#05923F#5P……亚里欧斯先生\x01",
            "突然带走小滴，\x01",
            "恐怕也是因为这件事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_17F3B():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17F3B)
    Sleep(50)

    def lambda_17F4B():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_17F4B)
    Sleep(50)

    def lambda_17F5B():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_17F5B)
    Sleep(50)

    def lambda_17F6B():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_17F6B)
    Sleep(50)

    def lambda_17F7B():
        TurnDirection(0x9, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_17F7B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x9, 0)

    #C0828
    ChrTalk(
        0x101,
        "#12P#00005F啊……\x02",
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x102,
        (
            "#12P#00108F确实如此……\x01",
            "他的身份突然有了如此巨变，\x01",
            "对小滴也会造成各种影响……\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x104,
        (
            "#00306F#12P甚至有可能会使小滴\x01",
            "被反对派的人盯上……\x02",
        )
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x103,
        (
            "#11P#00208F……在这种状况下，\x01",
            "的确无法否定那种可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x9,
        "#01108F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x101,
        (
            "#12P#00004F琪雅……没事的。\x02\x03",

            "#00000F亚里欧斯先生一定有办法保护小滴，\x01",
            "不会让她遇到危险的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18102():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_18102)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(200)

    #C0834
    ChrTalk(
        0x9,
        (
            "#01121F#5P嗯……是啊。\x02\x03",

            "#01122F……嘿嘿，\x01",
            "但我还是有点担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0xB,
        "#5P#05921F琪雅……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0836
    ChrTalk(
        0x101,
        (
            "#12P#00008F……塞茜尔姐姐，不好意思，\x01",
            "你能帮我们看一会家吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_18235():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_18235)
    Sleep(50)

    def lambda_18245():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_18245)
    Sleep(50)

    def lambda_18255():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_18255)
    Sleep(50)

    def lambda_18265():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_18265)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)

    #C0837
    ChrTalk(
        0x9,
        "#01105F#5P罗伊德……？\x02",
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0xB,
        (
            "#05925F#5P嗯，傍晚之前\x01",
            "应该没问题……\x02\x03",

            "#05921F你们要出门吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x101,
        "#12P#00003F嗯。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0840
    ChrTalk(
        0x101,
        (
            "#5P#00001F各位……\x02\x03",

            "我们就先……\x01",
            "去协会看看吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0841
    ChrTalk(
        0x102,
        "#12P#00101F说、说的也是。\x02",
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x103,
        (
            "#5P#00201F关于亚里欧斯先生这件事，\x01",
            "的确有必要去向他们询问一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0843
    ChrTalk(
        0x104,
        (
            "#00303F#12P是啊……\x01",
            "实在是太突然了。\x02",
        )
    )

    CloseMessageWindow()

    #C0844
    ChrTalk(
        0xB,
        (
            "#05923F#5P……我知道了，\x01",
            "我会和琪雅一起\x01",
            "留在这里看家的。\x02\x03",

            "#05920F现在的局势很特殊……\x01",
            "你们千万要注意安全。\x02\x03",

            "一定不要太乱来哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1849A():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1849A)
    Sleep(50)

    def lambda_184AA():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_184AA)
    Sleep(50)

    def lambda_184BA():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_184BA)
    Sleep(50)

    def lambda_184CA():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_184CA)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)

    #C0845
    ChrTalk(
        0x101,
        "#12P#00002F嗯，我知道。\x02",
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x104,
        "#00309F#12P塞茜尔小姐，多谢啦！\x02",
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x102,
        "#12P#00104F那就拜托您了。\x02",
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0x103,
        (
            "#11P#00202F琪雅，要和塞茜尔小姐\x01",
            "一起乖乖看家哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0849
    ChrTalk(
        0x9,
        "#01112F#5P啊……\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_68(12900, 1750, 9800, 3000)

    def lambda_185AD():
        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0xB, 2, lambda_185AD)

    def lambda_185BF():
        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x9, 2, lambda_185BF)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 54)
    Sleep(350)
    BeginChrThread(0x103, 3, 0, 54)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 54)
    EndChrThread(0xB, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(14150, 1750, 10040, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0xB, 14500, 850, 10700, 270)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0850
    ChrTalk(
        0x9,
        "#11P#01101F……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_18694():
        TurnDirection(0xB, 0x9, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0xB, 2, lambda_18694)

    #C0851
    ChrTalk(
        0xB,
        "#05925F#5P琪雅？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetCameraDistance(24500, 2000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)

    def lambda_186D5():
        OP_95(0xFE, 900, 850, 9700, 5500, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_186D5)
    Sleep(200)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xB, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x238), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x323)
    SetScenarioFlags(0x182, 1)
    SetScenarioFlags(0x23, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_177A3 end

    def Function_54_1873B(): pass

    label("Function_54_1873B")

    OP_95(0xFE, 15150, 850, 8450, 4500, 0x1)
    OP_95(0xFE, 10150, 850, 8950, 4500, 0x1)
    OP_95(0xFE, 5150, 850, 9450, 4500, 0x1)
    OP_95(0xFE, 150, 850, 9450, 4500, 0x1)
    Return()

    # Function_54_1873B end

    def Function_55_1878C(): pass

    label("Function_55_1878C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1000, 1000, 5300, 0)
    MoveCamera(51, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 300, -1000, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x103, 300, 0, -3000, 0)
    SetChrPos(0x104, 1400, 0, -3300, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x2B, 800, 0, 2000, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 2300, 0, 5300, 270)
    SetChrChipByIndex(0xB, 0x7)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetCameraDistance(22500, 5000)
    FadeToBright(2000, 0)

    def lambda_18887():
        OP_95(0xFE, -300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_18887)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x5A, 0x1F4)

    def lambda_188AF():
        OP_95(0xFE, 2300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_188AF)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x10E, 0x1F4)

    def lambda_188D7():
        OP_95(0xFE, 1000, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_188D7)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0852
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#1P塞茜尔姐姐！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(1000, 1000, 4100, 1500)
    SetChrPos(0x101, 300, 0, -1600, 0)
    BeginChrThread(0x101, 3, 0, 56)

    def lambda_18979():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18979)
    Sleep(250)

    def lambda_1898D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1898D)
    Sleep(350)

    def lambda_189A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_189A1)
    Sleep(450)

    def lambda_189B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_189B5)
    OP_93(0xB, 0xB4, 0x1F4)

    #C0853
    ChrTalk(
        0xB,
        "#05921F#5P罗伊德……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    #C0854
    ChrTalk(
        0x101,
        "#12P#00007F琪雅怎么了！？\x02",
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x102,
        (
            "#00101F您刚才说，琪雅被\x01",
            "亚里欧斯先生带走了……\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0xB,
        (
            "#05926F#5P是的，亚里欧斯先生穿着国防军的\x01",
            "白色制服，独自一人前来……\x02\x03",

            "#05921F他说『我来接你了』，\x01",
            "然后琪雅就点了点头……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(850)

    #C0857
    ChrTalk(
        0x101,
        "#12P#00011F什么……？\x02",
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x104,
        (
            "#00305F也就是说，阿琪是\x01",
            "自愿跟着他走的？\x02",
        )
    )

    CloseMessageWindow()

    #C0859
    ChrTalk(
        0xB,
        (
            "#05923F#5P嗯……在我看来，正是如此。\x02\x03",

            "#05921F但是，她居然不通知你们一声，\x01",
            "就直接要动身离开，实在是很反常。\x01",
            "所以我便试图阻止她……\x02\x03",

            "#05926F但琪雅却对我说\x01",
            "『没事的，不用担心』……\x02\x03",

            "听她这样一说，连一直充满警惕\x01",
            "的蔡特都平静下来了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x13B, 0x1F4)
    Sleep(300)

    #C0860
    ChrTalk(
        0x103,
        (
            "#12P#00208F话说回来……\x01",
            "蔡特也不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0xB,
        (
            "#05926F#5P在他们二人离开之后，\x01",
            "蔡特也突然出去了。\x02\x03",

            "#05928F也许是去追\x01",
            "他们了吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_18D38():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18D38)
    Sleep(100)

    def lambda_18D48():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_18D48)
    Sleep(100)

    def lambda_18D58():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_18D58)
    Sleep(100)

    def lambda_18D68():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_18D68)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sleep(150)

    #C0862
    ChrTalk(
        0x101,
        "#5P#00008F……这到底是怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x102,
        (
            "#00108F也许只是和小滴\x01",
            "约好要见面吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0xB,
        (
            "#05923F#5P我原本也是这样想的，\x01",
            "但似乎并非如此……\x02\x03",

            "#05921F从亚里欧斯先生的只言片语来分析，\x01",
            "他们好像是要去米修拉姆。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_18EA3():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18EA3)
    Sleep(50)

    def lambda_18EB3():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_18EB3)
    Sleep(50)

    def lambda_18EC3():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_18EC3)
    Sleep(50)

    def lambda_18ED3():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_18ED3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0865
    ChrTalk(
        0x101,
        "#12P#00005F米修拉姆……？\x02",
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0xB,
        (
            "#05923F#5P嗯，因为他说已经\x01",
            "准备好船了……\x02\x03",

            "#05921F也就是说，他们应该是要\x01",
            "去米修拉姆吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0867
    ChrTalk(
        0x102,
        (
            "#00103F……但在最近这几天，\x01",
            "米修拉姆已经完全停止营业了啊。\x02\x03",

            "#00101F为什么要特意去那种地方……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0868
    ChrTalk(
        0x104,
        (
            "#00310F啧……\x01",
            "果然还是有问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0869
    ChrTalk(
        0x103,
        "#12P#00201F我们去追他们吧，罗伊德前辈。\x02",
    )

    CloseMessageWindow()

    #C0870
    ChrTalk(
        0x101,
        (
            "#11P#00003F好……\x01",
            "先想办法准备船只吧。\x02\x03",

            "#00007F塞茜尔姐姐，不好意思！\x01",
            "我们这就要去追他们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19098():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19098)
    Sleep(50)

    def lambda_190A8():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_190A8)
    Sleep(50)

    def lambda_190B8():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_190B8)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0871
    ChrTalk(
        0xB,
        (
            "#05923F#5P嗯，要小心啊。\x02\x03",

            "#05928F……亚里欧斯先生和小琪雅\x01",
            "都很反常，眼神显得特别严肃。\x02\x03",

            "#05921F我想，一定有什么重大隐情。\x02",
        )
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0x101,
        "#11P#00013F知道了……！\x02",
    )

    CloseMessageWindow()

    #C0873
    ChrTalk(
        0x102,
        (
            "#00107F总之，我们要追上他们，\x01",
            "把这件事的前因后果问清楚……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    SetScenarioFlags(0x22, 2)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_1878C end

    def Function_56_191D3(): pass

    label("Function_56_191D3")


    def lambda_191D8():
        OP_97(0x101, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_191D8)
    Sleep(200)

    def lambda_191F5():
        OP_97(0x102, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_191F5)
    Sleep(200)

    def lambda_19212():
        OP_97(0x103, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19212)
    Sleep(200)

    def lambda_1922F():
        OP_97(0x104, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1922F)
    Return()

    # Function_56_191D3 end

    def Function_57_19245(): pass

    label("Function_57_19245")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51218.itc", 0x1E)
    OP_24(0x101E)
    OP_24(0x101F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis287.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis288.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis289.itp")
    ClearMapFlags(0x10000000)
    OP_68(1000, 1000, 0, 0)
    MoveCamera(55, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x101, 300, 0, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x103, 300, 0, -2900, 0)
    SetChrPos(0x104, 1400, 0, -3200, 0)
    SetChrPos(0xF4, 300, 0, -4200, 0)
    SetChrPos(0xF5, 1400, 0, -4500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    StopBGM(0x1388)
    OP_68(1000, 1000, 2000, 3500)
    BeginChrThread(0x101, 3, 0, 58)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_19403():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19403)
    Sleep(400)

    def lambda_19417():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_19417)
    Sleep(600)

    def lambda_1942B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1942B)
    Sleep(400)

    def lambda_1943F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1943F)
    Sleep(600)

    def lambda_19453():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_19453)
    Sleep(400)

    def lambda_19467():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_19467)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_1947D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1947D)
    WaitChrThread(0x102, 1)

    def lambda_1948E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1948E)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 1)

    def lambda_194A7():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_194A7)
    WaitChrThread(0xF5, 1)

    def lambda_194B8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_194B8)
    OP_6F(0x79)
    OP_68(2640, 1300, 3150, 2000)
    MoveCamera(55, 15, 0, 2000)
    SetCameraDistance(29000, 2000)
    OP_6F(0x79)

    #C0874
    ChrTalk(
        0x101,
        "#6P#00001F#30W……特别任务支援科………\x02",
    )

    CloseMessageWindow()

    #C0875
    ChrTalk(
        0x102,
        "#6P#00108F#30W我们终于回来了……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    VolumeBGM(0x46, 0x64)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(110, 50, -1, -1)

    #A0876
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#4126V#27A#30W啊，大家回来了！\x02\x03",

            "#4127V#4S#30A#30W欢迎回来～\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 62)
    SetMessageWindowPos(170, 25, -1, -1)

    #A0877
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#4S#20A我们出发啦！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    SetMessageWindowPos(180, 20, -1, -1)

    #A0878
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#40A#30W好，\x01",
            "我们开始吃火锅吧。\x02\x03",

            "#70A#30W琪雅为我们准备了\x01",
            "肉、鱼、蔬菜──很丰盛啊。\x02\x03",

            "#50A#30W多吃一些，早点休息……\x01",
            "为明天做好准备吧！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 62)
    SetMessageWindowPos(145, 110, -1, -1)

    #A0879
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#4S#20A我开动了！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    FadeToBright(1000, 16777215)
    VolumeBGM(0x64, 0x7D0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    Sleep(500)

    #C0880
    ChrTalk(
        0x101,
        "#6P#00008F#30W……………………………\x02",
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x104,
        (
            "#5P#00304F#30W……哈哈，\x01",
            "真是太怀念了。\x02",
        )
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x103,
        "#6P#00208F是啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19888")

    #C0883
    ChrTalk(
        0x109,
        (
            "#12P#10106F明明才过了\x01",
            "一个月左右……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19888")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_198C4")

    #C0884
    ChrTalk(
        0x105,
        (
            "#12P#10404F呵呵……\x01",
            "真让人感慨万千啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1993B")

    #C0885
    ChrTalk(
        0x106,
        (
            "#12P#10708F话说回来，这里并没有\x01",
            "想象中那么凌乱呢……\x02\x03",

            "#10710F本以为国防军肯定会\x01",
            "闯进来搜查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1999C")

    label("loc_1993B")


    #C0886
    ChrTalk(
        0x102,
        (
            "#5P#00104F话说回来，这里并没有\x01",
            "想象中那么凌乱呢……\x02\x03",

            "#00100F本以为国防军一定会\x01",
            "闯进来搜查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1999C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19A9B")

    #C0887
    ChrTalk(
        0x10A,
        (
            "#12P#00606F看来是顾及到了\x01",
            "那孩子的心情吧。\x02\x03",

            "#00602F对总统一派来说，\x01",
            "她是最为重要的。\x02\x03",

            "所以他们不想弄乱她在意的地方，\x01",
            "以免惹她生气吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0888
    ChrTalk(
        0x101,
        "#6P#00000F……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0x103,
        (
            "#6P#00204F说得真露骨啊……\x01",
            "但这里能保持原状，我真的很高兴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B88")

    label("loc_19A9B")


    #C0890
    ChrTalk(
        0x101,
        (
            "#6P#00004F他们或许是\x01",
            "考虑到了琪雅的心情。\x02\x03",

            "#00000F对总统一派来说，\x01",
            "那孩子是最为重要的。\x02\x03",

            "所以他们不想弄乱她在意的地方，\x01",
            "以免惹她生气吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0891
    ChrTalk(
        0x104,
        "#5P#00305F……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0892
    ChrTalk(
        0x103,
        (
            "#6P#00204F说得真露骨啊……\x01",
            "但这里能保持原状，我真的很高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B88")

    Sound(953, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    OP_90(0xC, 1500, 3000, 15000, 180)

    def lambda_19BB6():
        OP_96(0xFE, 0x5DC, 0x0, 0x1838, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19BB6)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_19C45():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19C45)
    Sleep(50)

    def lambda_19C55():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19C55)
    Sleep(50)

    def lambda_19C65():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19C65)
    Sleep(50)

    def lambda_19C75():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19C75)
    Sleep(50)

    def lambda_19C85():
        TurnDirection(0xF4, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_19C85)
    Sleep(50)

    def lambda_19C95():
        TurnDirection(0xF5, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_19C95)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Fade(500)
    OP_68(1000, 1750, 9000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    OP_68(1000, 900, 5000, 3000)
    SetCameraDistance(23000, 3000)
    OP_0D()
    WaitChrThread(0xC, 1)
    OP_4B(0xC, 0xFF)
    OP_6F(0x79)

    #C0893
    ChrTalk(
        0x101,
        "#12P#00005F柯贝……！\x02",
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x102,
        (
            "#00102F太好了……\x01",
            "你也平安无事啊。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 61)

    def lambda_19D5B():
        OP_97(0x101, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19D5B)
    Sleep(100)

    def lambda_19D78():
        OP_97(0x102, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19D78)
    Sleep(100)

    def lambda_19D95():
        OP_97(0x104, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19D95)
    Sleep(100)

    def lambda_19DB2():
        OP_97(0xF4, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_19DB2)
    Sleep(100)

    def lambda_19DCF():
        OP_97(0xF5, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_19DCF)
    WaitChrThread(0x104, 0)

    def lambda_19DED():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_19DED)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x103, 3)

    #C0895
    ChrTalk(
        0xC,
        "#11P喵呜。\x02",
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0xC,
        "#11P喵，喵。\x02",
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0x103,
        (
            "#00204F……是吗，真是辛苦你了。\x02\x03",

            "#00202F嗯，嗯……\x01",
            "我们只是暂时离开而已。\x02\x03",

            "#00204F一定……会回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0898
    ChrTalk(
        0x104,
        "#00300F它说了什么？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0x103, 0x101, 500)

    #C0899
    ChrTalk(
        0x103,
        (
            "#00206F#5P自那之后，\x01",
            "柯贝也一直在这里生活……\x02\x03",

            "#00202F它好像还挺挂念我们\x01",
            "这些『同居者』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x101,
        "#12P#00012F哈哈，是吗。\x02",
    )

    CloseMessageWindow()

    #C0901
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，作为一只猫，\x01",
            "还真是很重感情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19FBA")

    #C0902
    ChrTalk(
        0x109,
        (
            "#12P#10102F难得回来，\x01",
            "我们给它准备一些\x01",
            "猫食吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A02F")

    label("loc_19FBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A001")

    #C0903
    ChrTalk(
        0x105,
        (
            "#12P#10402F难得回来，\x01",
            "我们给它准备点食物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A02F")

    label("loc_1A001")


    #C0904
    ChrTalk(
        0x104,
        (
            "#00304F难得回来，\x01",
            "我们给它准备点食物吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A02F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(122400, 700, 6000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0xC, 122700, 0, 6000, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 121800, 0, 6000, 0)
    OP_4C(0xC, 0xFF)
    SetCameraDistance(21000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 10790, 850, 12360, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A5, 4)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    EventEnd(0x5)
    Return()

    # Function_57_19245 end

    def Function_58_1A10A(): pass

    label("Function_58_1A10A")


    def lambda_1A10F():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A10F)
    Sleep(200)

    def lambda_1A12C():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A12C)
    Sleep(200)
    BeginChrThread(0x103, 0, 0, 59)
    Sleep(200)
    BeginChrThread(0x104, 0, 0, 60)
    Sleep(200)

    def lambda_1A15B():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1A15B)
    Sleep(200)

    def lambda_1A178():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1A178)
    Return()

    # Function_58_1A10A end

    def Function_59_1A18E(): pass

    label("Function_59_1A18E")


    def lambda_1A193():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A193)
    WaitChrThread(0x103, 1)

    def lambda_1A1B1():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A1B1)
    WaitChrThread(0x103, 1)
    Return()

    # Function_59_1A18E end

    def Function_60_1A1CB(): pass

    label("Function_60_1A1CB")


    def lambda_1A1D0():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A1D0)
    WaitChrThread(0x104, 1)

    def lambda_1A1EE():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A1EE)
    WaitChrThread(0x104, 1)
    Return()

    # Function_60_1A1CB end

    def Function_61_1A208(): pass

    label("Function_61_1A208")

    Sleep(200)

    def lambda_1A210():
        OP_95(0xFE, -400, 0, 4100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A210)
    WaitChrThread(0x103, 1)

    def lambda_1A22E():
        OP_95(0xFE, 300, 0, 6100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A22E)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0xC, 500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0xC, 0x103, 500)
    Return()

    # Function_61_1A208 end

    def Function_62_1A26A(): pass

    label("Function_62_1A26A")

    OP_CB(0x0, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CC(0x0, 0xFF, 0x0)
    Return()

    # Function_62_1A26A end

    def Function_63_1A398(): pass

    label("Function_63_1A398")

    EventBegin(0x0)
    Fade(500)
    OP_68(64879, 1330, 10230, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24880, 0)
    SetChrPos(0x101, 65030, 30, 11420, 225)
    SetChrPos(0x102, 66810, 30, 10890, 270)
    SetChrPos(0x103, 66810, 30, 9740, 270)
    SetChrPos(0x104, 63390, 0, 8370, 0)
    SetChrPos(0x109, 65019, 0, 8370, 0)
    SetChrPos(0x105, 66270, 0, 8280, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0905
    ChrTalk(
        0x101,
        (
            "#00000F赛尔盖科长以前\x01",
            "的外号好像是\x01",
            "『见缝插针的赛尔盖』。\x02",
        )
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0x102,
        (
            "#11P#00100F也就是说，\x01",
            "科长的椅子就是\x01",
            "『见缝插针的指挥官所坐的椅子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0907
    ChrTalk(
        0x101,
        "#00001F调查一下这附近吧……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0908
    ChrTalk(
        0x101,
        (
            "#00005F……科长的桌子下面\x01",
            "好像有什么东西。\x02\x03",

            "#00000F拖出来看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(63630, 1330, 6190, 0)
    MoveCamera(43, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24880, 0)
    ClearMapObjFlags(0x14, 0x4)
    SetChrPos(0x101, 64060, 30, 5280, 0)
    SetChrPos(0x102, 62990, 30, 5080, 0)
    SetChrPos(0x103, 65190, 30, 5080, 0)
    SetChrPos(0x104, 64060, 30, 4000, 0)
    SetChrPos(0x109, 62990, 30, 4000, 0)
    SetChrPos(0x105, 65190, 30, 4000, 0)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0x2C, 0x1E)
    SetChrSubChip(0x2C, 0xC)
    SetChrPos(0x2C, 64040, 150, 7160, 0)
    OP_52(0x2C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x2)
    SetChrFlags(0x2C, 0x10)
    SetChrFlags(0x2C, 0x20)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0909
    ChrTalk(
        0x104,
        (
            "#12P#00305F这是……\x01",
            "皮箱？\x02",
        )
    )

    CloseMessageWindow()

    #C0910
    ChrTalk(
        0x105,
        (
            "#12P#10300F和我们在『拍卖会』上\x01",
            "发现的那口装着琪雅的箱子\x01",
            "有些相像呢。\x02\x03",

            "#10304F呵呵，他把第一个\x01",
            "隐藏地点选定在这里，\x01",
            "还真是赤裸裸地挑衅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0911
    ChrTalk(
        0x101,
        (
            "#12P#00006F的、的确如此。\x01",
            "而且连科长的外号都知道……\x02\x03",

            "#00000F总之，先打开看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(1024, 0, 100, 0)
    OP_74(0x14, 0x1E)
    OP_71(0x14, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x14)
    Sleep(1000)
    SetChrName("")

    #A0912
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在皮箱的内侧\x01",
            "贴着一张卡片。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0913
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第二个牢笼在市外。\x01",
            "寻找『古道之中，乡间之人\x01",
            "世代传承之地』吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0914
    ChrTalk(
        0x103,
        (
            "#00200F这是罗赞贝尔克出品的\x01",
            "古董人偶……\x01",
            "看来没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0915
    ChrTalk(
        0x102,
        (
            "#12P#00100F嗯，我也见过它。\x02\x03",

            "#00104F贝尔非常喜爱这个人偶，\x01",
            "还给它取名为『卡楠』。\x02",
        )
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x109,
        (
            "#12P#10100F呵呵，竟然还会给人偶起名字，\x01",
            "玛丽亚贝尔小姐也有可爱之处嘛。\x02\x03",

            "#10106F犯人如此小心翼翼地\x01",
            "把盗窃品存放在这种皮箱里……\x01",
            "倒是让人有点意外……\x02",
        )
    )

    CloseMessageWindow()

    #C0917
    ChrTalk(
        0x101,
        (
            "#12P#00003F怪盗Ｂ……\x01",
            "看来他对艺术品\x01",
            "还是相当在意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0x105,
        (
            "#12P#10300F至于这第二张卡片……\x01",
            "地点在『市外』。\x02\x03",

            "#10306F真是的，\x01",
            "搜索范围扩大了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0919
    ChrTalk(
        0x102,
        (
            "#12P#00100F『古道』和『乡间之人世代传承』，\x01",
            "这两处提示应该很重要。\x02\x03",

            "#00103F听起来很有历史沧桑感呢。\x01",
            "在以现代都市而闻名的克洛斯贝尔自治州内，\x01",
            "符合那种描述的地方应该是……\x02",
        )
    )

    CloseMessageWindow()

    #C0920
    ChrTalk(
        0x104,
        (
            "#12P#00300F总之，我们先把这个收好，\x01",
            "然后再去找下一个吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0921
    ChrTalk(
        0x101,
        "#12P#00000F嗯，就这么办。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0922
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16I罗赞贝尔克人偶·Ｃ\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x335, 1)
    SetMapObjFlags(0x14, 0x4)
    SetChrFlags(0x2C, 0x80)
    OP_D7(0x1E)
    SetChrPos(0x0, 64050, 30, 5290, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7A, 0x1, 0x2)
    SetScenarioFlags(0x157, 1)
    OP_65(0x4, 0x1)
    EventEnd(0x5)
    Return()

    # Function_63_1A398 end

    def Function_64_1AC27(): pass

    label("Function_64_1AC27")

    EventBegin(0x1)

    #C0923
    ChrTalk(
        0x101,
        (
            "#00000F先确认一下支援请求吧，\x01",
            "然后再开始行动。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)
    Return()

    # Function_64_1AC27 end

    def Function_65_1AC74(): pass

    label("Function_65_1AC74")

    EventBegin(0x1)

    #C0924
    ChrTalk(
        0x101,
        (
            "#00000F先确认一下支援请求吧，\x01",
            "然后再开始行动。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11000, 850, 11350, 180)
    EventEnd(0x4)
    Return()

    # Function_65_1AC74 end

    def Function_66_1ACC1(): pass

    label("Function_66_1ACC1")

    EventBegin(0x1)

    #C0925
    ChrTalk(
        0x101,
        (
            "#00000F先确认一下支援请求吧，\x01",
            "然后再开始行动。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17000, 850, 4000, 270)
    EventEnd(0x4)
    Return()

    # Function_66_1ACC1 end

    def Function_67_1AD0E(): pass

    label("Function_67_1AD0E")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD3A")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1AD3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD57")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1AD57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD74")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1AD74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD91")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1AD91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ADAE")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1ADAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ADCB")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1ADCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ADE8")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1ADE8")

    Return()

    # Function_67_1AD0E end

    SaveToFile()

Try(main)
