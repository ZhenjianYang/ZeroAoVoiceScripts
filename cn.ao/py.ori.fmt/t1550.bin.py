from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1550.bin",                # FileName
        "t1550",                    # MapName
        "t1550",                    # Location
        0x0052,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 82, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1550",                  # 0
        "芙兰",                   # 1
        "多诺邦警督",             # 2
        "雷蒙德搜查官",           # 3
        "伊莉娅",                 # 4
        "修利",                   # 5
        "滴",                     # 6
        "米海尔",                 # 7
        "亚里欧斯",               # 8
        "勤杂工戴森",             # 9
        "塞茜尔",                 # 10
        "希伦护士",               # 11
        "梅菲尔护士",             # 12
        "诊断医生贝尔达因",       # 13
        "阿尔伯特大公",           # 14
        "法拉夫人",               # 15
        "赛兰德教授",             # 16
        "丸椅子",                 # 17
        "赛尔盖",                 # 18
        "SE控制",                 # 19
    ))

    AddCharChip((
        "apl/ch51518.itc",                   # 00
        "apl/ch51519.itc",                   # 01
        "chr/ch30202.itc",                   # 02
        "apl/ch51520.itc",                   # 03
        "chr/ch10002.itc",                   # 04
        "apl/ch50105.itc",                   # 05
        "chr/ch34000.itc",                   # 06
        "apl/ch50145.itc",                   # 07
        "chr/ch02400.itc",                   # 08
        "chr/ch20200.itc",                   # 09
        "chr/ch05300.itc",                   # 0A
        "chr/ch29900.itc",                   # 0B
        "chr/ch29800.itc",                   # 0C
        "chr/ch29300.itc",                   # 0D
        "chr/ch11800.itc",                   # 0E
        "chr/ch21900.itc",                   # 0F
        "chr/ch21902.itc",                   # 10
        "chr/ch44800.itc",                   # 11
        "apl/ch51703.itc",                   # 12
        "chr/ch30300.itc",                   # 13
        "chr/ch08500.itc",                   # 14
        "chr/ch06900.itc",                   # 15
        "apl/ch51702.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(6199,    0,       -47500,  270,  389,  0x0, 0,   0,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(-55000,  0,       -47500,  270,  389,  0x0, 0,   1,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(-55700,  100,     -49799,  0,    389,  0x0, 0,   2,   0,   255, 255, 0,   22,  255,  0)
    DeclNpc(-98000,  0,       -5199,   180,  389,  0x0, 0,   3,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-99500,  100,     -5699,   90,   389,  0x0, 0,   4,   0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-97739,  699,     56169,   180,  325,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(6050,    699,     -47549,  270,  389,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-99220,  0,       56180,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-8310,   0,       25229,   90,   389,  0x0, 0,   9,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-99220,  0,       56180,   90,   389,  0x0, 0,   10,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-8600,   0,       10350,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-7599,   0,       9350,    315,  389,  0x0, 0,   12,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(4809,    0,       -48900,  45,   389,  0x0, 0,   13,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(-99220,  0,       55110,   45,   389,  0x0, 0,   14,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-55700,  100,     -49799,  0,    389,  0x0, 0,   15,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(-99220,  0,       56180,   90,   389,  0x0, 0,   17,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 87,  -15.210000038146973,   8.899999618530273,     -1.0,                  64.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   7.605000019073486,     -1.1124999523162842,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 88,  -9.210000038146973,    15.65999984741211,     -1.0,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.1512500047683716,    -7.829999923706055,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 91,  -21.149999618530273,   29.889999389648438,    -1.0,                  64.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   10.574999809265137,    -3.7362499237060547,   0.20000000298023224,   1.0])

    DeclActor(-98310,  0,       54690,   1200,    -97740,  1500,    56170,   0x007E, 0,  12, 0x0000)

    ChipFrameInfo(1504, 0)                                       # 0

    ScpFunction((
        "Function_0_5E0",          # 00, 0
        "Function_1_698",          # 01, 1
        "Function_2_D6C",          # 02, 2
        "Function_3_12A4",         # 03, 3
        "Function_4_12B3",         # 04, 4
        "Function_5_12FA",         # 05, 5
        "Function_6_1301",         # 06, 6
        "Function_7_130E",         # 07, 7
        "Function_8_1321",         # 08, 8
        "Function_9_1328",         # 09, 9
        "Function_10_1335",        # 0A, 10
        "Function_11_133C",        # 0B, 11
        "Function_12_1367",        # 0C, 12
        "Function_13_1994",        # 0D, 13
        "Function_14_1AD2",        # 0E, 14
        "Function_15_1B70",        # 0F, 15
        "Function_16_1C7C",        # 10, 16
        "Function_17_1D00",        # 11, 17
        "Function_18_1DF0",        # 12, 18
        "Function_19_258B",        # 13, 19
        "Function_20_2887",        # 14, 20
        "Function_21_2DB7",        # 15, 21
        "Function_22_33E3",        # 16, 22
        "Function_23_350A",        # 17, 23
        "Function_24_433B",        # 18, 24
        "Function_25_4487",        # 19, 25
        "Function_26_46E4",        # 1A, 26
        "Function_27_522A",        # 1B, 27
        "Function_28_55D8",        # 1C, 28
        "Function_29_5AF7",        # 1D, 29
        "Function_30_5D99",        # 1E, 30
        "Function_31_5E7A",        # 1F, 31
        "Function_32_5F38",        # 20, 32
        "Function_33_62CD",        # 21, 33
        "Function_34_6396",        # 22, 34
        "Function_35_64D0",        # 23, 35
        "Function_36_6938",        # 24, 36
        "Function_37_6F5E",        # 25, 37
        "Function_38_6F65",        # 26, 38
        "Function_39_7195",        # 27, 39
        "Function_40_71FD",        # 28, 40
        "Function_41_83DC",        # 29, 41
        "Function_42_8411",        # 2A, 42
        "Function_43_8437",        # 2B, 43
        "Function_44_8463",        # 2C, 44
        "Function_45_8489",        # 2D, 45
        "Function_46_84BE",        # 2E, 46
        "Function_47_84E4",        # 2F, 47
        "Function_48_8D83",        # 30, 48
        "Function_49_8D8D",        # 31, 49
        "Function_50_A560",        # 32, 50
        "Function_51_A57F",        # 33, 51
        "Function_52_A58F",        # 34, 52
        "Function_53_A5A4",        # 35, 53
        "Function_54_A5C0",        # 36, 54
        "Function_55_A5DC",        # 37, 55
        "Function_56_A5F8",        # 38, 56
        "Function_57_A614",        # 39, 57
        "Function_58_A630",        # 3A, 58
        "Function_59_A64C",        # 3B, 59
        "Function_60_A698",        # 3C, 60
        "Function_61_B3F6",        # 3D, 61
        "Function_62_B778",        # 3E, 62
        "Function_63_C46C",        # 3F, 63
        "Function_64_CB16",        # 40, 64
        "Function_65_CB3F",        # 41, 65
        "Function_66_CB68",        # 42, 66
        "Function_67_CB7B",        # 43, 67
        "Function_68_D71D",        # 44, 68
        "Function_69_D776",        # 45, 69
        "Function_70_D7CF",        # 46, 70
        "Function_71_D828",        # 47, 71
        "Function_72_D881",        # 48, 72
        "Function_73_D8DA",        # 49, 73
        "Function_74_D933",        # 4A, 74
        "Function_75_D946",        # 4B, 75
        "Function_76_E0BB",        # 4C, 76
        "Function_77_E2DC",        # 4D, 77
        "Function_78_EE6A",        # 4E, 78
        "Function_79_EEA7",        # 4F, 79
        "Function_80_EF79",        # 50, 80
        "Function_81_EFA9",        # 51, 81
        "Function_82_EFD9",        # 52, 82
        "Function_83_F009",        # 53, 83
        "Function_84_F025",        # 54, 84
        "Function_85_F041",        # 55, 85
        "Function_86_F051",        # 56, 86
        "Function_87_F653",        # 57, 87
        "Function_88_F66C",        # 58, 88
        "Function_89_F697",        # 59, 89
        "Function_90_F6C2",        # 5A, 90
        "Function_91_F6ED",        # 5B, 91
        "Function_92_F706",        # 5C, 92
        "Function_93_F744",        # 5D, 93
        "Function_94_F7B1",        # 5E, 94
    ))


    def Function_0_5E0(): pass

    label("Function_0_5E0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_620"),
        (1, "loc_62C"),
        (2, "loc_638"),
        (3, "loc_644"),
        (4, "loc_650"),
        (5, "loc_65C"),
        (6, "loc_668"),
        (SWITCH_DEFAULT, "loc_674"),
    )


    label("loc_620")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_62C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_638")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_644")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_650")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_65C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_668")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_674")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_680")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_697")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_697")

    Return()

    # Function_0_5E0 end

    def Function_1_698(): pass

    label("Function_1_698")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B0")
    ClearScenarioFlags(0x25, 1)
    Call(0, 37)

    label("loc_6B0")

    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_731")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55260, 0, -49740, 270)
    SetChrChipByIndex(0x9, 0x13)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -56460, 0, -49740, 90)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jump("loc_C40")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7AD")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55300, 700, -47750, 270)
    SetChrChipByIndex(0x9, 0x12)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x10)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_C40")

    label("loc_7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_844")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55300, 700, -47750, 270)
    SetChrChipByIndex(0x9, 0x12)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x10)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -99490, 0, -5640, 90)
    Jump("loc_C40")

    label("loc_844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_902")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x15)
    SetChrPos(0x8, -55180, 0, -49470, 0)
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55300, 700, -47750, 270)
    SetChrChipByIndex(0x9, 0x12)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrSubChip(0x9, 0x1)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -56380, 0, -49470, 90)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FD")
    SetChrFlags(0x17, 0x10)

    label("loc_8FD")

    Jump("loc_C40")

    label("loc_902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9B2")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x14)
    SetChrPos(0x8, 7850, 0, -50750, 90)
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -55300, 700, -47750, 270)
    SetChrChipByIndex(0x9, 0x12)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x10)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -98000, 700, -5200, 180)
    SetChrChipByIndex(0xB, 0x16)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AD")
    SetChrFlags(0x17, 0x10)

    label("loc_9AD")

    Jump("loc_C40")

    label("loc_9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A6C")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrPos(0x8, 6100, 400, -47500, 270)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x1000)
    SetChrPos(0x9, -55500, 400, -47700, 270)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x1000)
    SetChrPos(0xB, -97700, 420, -5500, 180)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x80)
    Jump("loc_C40")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AA2")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9D")
    SetChrFlags(0x13, 0x10)

    label("loc_A9D")

    Jump("loc_C40")

    label("loc_AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_ABA")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    Jump("loc_C40")

    label("loc_ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AE3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 4810, 0, -48900, 45)
    Jump("loc_C40")

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B49")
    SetChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xE, -99220, 0, 56180, 90)
    SetChrChipByIndex(0xE, 0x6)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -100590, 0, 57320, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3F")
    SetChrFlags(0x11, 0x10)

    label("loc_B3F")

    ClearChrFlags(0x10, 0x80)
    Jump("loc_C40")

    label("loc_B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BDC")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 4810, 0, -48900, 45)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD7")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -100500, 0, 54700, 45)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -100500, 0, 55990, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC8")
    SetChrFlags(0xF, 0x10)

    label("loc_BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD7")
    SetChrFlags(0x15, 0x10)

    label("loc_BD7")

    Jump("loc_C40")

    label("loc_BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C40")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C00")
    SetChrFlags(0x11, 0x80)

    label("loc_C00")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -55020, 0, -49520, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C40")
    SetChrFlags(0x14, 0x10)

    label("loc_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C4F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 75)

    label("loc_C4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6E")
    Event(0, 40)
    Jump("loc_D23")

    label("loc_C6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C8D")
    Event(0, 47)
    Jump("loc_D23")

    label("loc_C8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CAC")
    Event(0, 49)
    Jump("loc_D23")

    label("loc_CAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCB")
    Event(0, 60)
    Jump("loc_D23")

    label("loc_CCB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEA")
    Event(0, 61)
    Jump("loc_D23")

    label("loc_CEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D09")
    Event(0, 62)
    Jump("loc_D23")

    label("loc_D09")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D23")
    Event(0, 63)

    label("loc_D23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4C")
    Event(0, 76)
    Jump("loc_D6B")

    label("loc_D4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6B")
    Event(0, 67)

    label("loc_D6B")

    Return()

    # Function_1_698 end

    def Function_2_D6C(): pass

    label("Function_2_D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_D7E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA5")
    Sound(1016, 1, 60, 0)
    Jump("loc_DA8")

    label("loc_DA5")

    OP_24(0x3F8)

    label("loc_DA8")

    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mec_T15_02n", 0x0, 0x1)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E83")
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Call(0, 11)
    Jump("loc_1091")

    label("loc_E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_ED4")
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Call(0, 10)
    Call(0, 11)
    Jump("loc_1091")

    label("loc_ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_F25")
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Call(0, 10)
    Call(0, 11)
    Jump("loc_1091")

    label("loc_F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_F83")
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F78")
    Call(0, 9)

    label("loc_F78")

    Call(0, 10)
    Call(0, 11)
    Jump("loc_1091")

    label("loc_F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1005")
    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED03", 0x1, 0x1)
    Call(0, 8)
    Call(0, 5)
    Call(0, 6)
    Call(0, 7)
    SetMapObjFrame(0xFF, "mec_T15_02e", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    Jump("loc_1091")

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1013")
    Jump("loc_1091")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1021")
    Jump("loc_1091")

    label("loc_1021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_102F")
    Jump("loc_1091")

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_103D")
    Jump("loc_1091")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1063")
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    Jump("loc_1091")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1091")
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)

    label("loc_1091")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10AC")
    OP_66(0x0, 0x1)
    Jump("loc_10C5")

    label("loc_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C5")
    OP_66(0x0, 0x1)

    label("loc_10C5")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EC")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1109")
    ModifyEventFlags(1, 1, 0x80)
    OP_1B(0x0, 0x0, 0x59)
    OP_1B(0x1, 0x0, 0x5A)

    label("loc_1109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1126")
    OP_1B(0x0, 0x0, 0x59)
    OP_1B(0x1, 0x0, 0x5A)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_114D")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_114D")
    OP_1B(0x8, 0x0, 0x26)
    OP_1B(0x9, 0x0, 0x27)

    label("loc_114D")

    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_116F")
    Jump("loc_11CE")

    label("loc_116F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11A1")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    Jump("loc_11CE")

    label("loc_11A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CE")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -99500, 0, -5700, 0)

    label("loc_11CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11E2")
    SetMapObjFlags(0x6, 0x4)
    Jump("loc_1267")

    label("loc_11E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_120B")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    Jump("loc_1267")

    label("loc_120B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1234")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    Jump("loc_1267")

    label("loc_1234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1267")
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_1267")
    SetMapObjFlags(0x6, 0x4)

    label("loc_1267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A3")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_12A3")

    Return()

    # Function_2_D6C end

    def Function_3_12A4(): pass

    label("Function_3_12A4")

    SetMapObjFrame(0xFF, "obj_07", 0x1, 0x1)
    Return()

    # Function_3_12A4 end

    def Function_4_12B3(): pass

    label("Function_4_12B3")

    SetMapObjFrame(0xFF, "obj_08", 0x1, 0x1)
    SetMapObjFrame(0xFF, "obj_10", 0x1, 0x1)
    SetMapObjFrame(0xFF, "obj_09", 0x1, 0x1)
    SetMapObjFrame(0xFF, "obj_11", 0x1, 0x1)
    SetMapObjFrame(0xFF, "obj_12", 0x1, 0x1)
    Return()

    # Function_4_12B3 end

    def Function_5_12FA(): pass

    label("Function_5_12FA")

    ClearMapObjFlags(0x7, 0x4)
    Return()

    # Function_5_12FA end

    def Function_6_1301(): pass

    label("Function_6_1301")

    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Return()

    # Function_6_1301 end

    def Function_7_130E(): pass

    label("Function_7_130E")

    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    Return()

    # Function_7_130E end

    def Function_8_1321(): pass

    label("Function_8_1321")

    ClearMapObjFlags(0x11, 0x4)
    Return()

    # Function_8_1321 end

    def Function_9_1328(): pass

    label("Function_9_1328")

    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    Return()

    # Function_9_1328 end

    def Function_10_1335(): pass

    label("Function_10_1335")

    ClearMapObjFlags(0xD, 0x4)
    Return()

    # Function_10_1335 end

    def Function_11_133C(): pass

    label("Function_11_133C")

    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    Return()

    # Function_11_133C end

    def Function_12_1367(): pass

    label("Function_12_1367")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1378")
    Jump("loc_1990")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1389")
    Call(0, 27)
    Jump("loc_1990")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_139A")
    Call(0, 27)
    Jump("loc_1990")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C8")

    #C0001
    ChrTalk(
        0xD,
        (
            "#11205F……啊，对了……\x02\x03",

            "#11203F琪雅昨天来\x01",
            "医院探望过我……\x02\x03",

            "#11210F她知道了我的手术结果之后，\x01",
            "情绪好像非常沮丧。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00003F……嗯，确实，她从今天\x01",
            "早上开始就一直闷闷不乐的。\x02\x03",

            "#00000F但不要紧的，\x01",
            "既然你这么乐观，\x01",
            "琪雅应该很快就能恢复精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xD,
        "#11200F嗯……希望如此。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_14F9")

    label("loc_14C8")


    #C0004
    ChrTalk(
        0xD,
        (
            "#11200F琪雅……\x01",
            "要是能早日恢复精神\x01",
            "就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F9")

    Jump("loc_1990")

    label("loc_14FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_150F")
    Call(0, 13)
    Jump("loc_1990")

    label("loc_150F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1987")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1909")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1534")
    Call(0, 18)
    Jump("loc_1904")

    label("loc_1534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1904")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1550")
    Call(0, 17)
    Jump("loc_1904")

    label("loc_1550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188B")

    #C0005
    ChrTalk(
        0xD,
        (
            "#01505F……啊，对了……\x02\x03",

            "#01500F琪雅今天是不是\x01",
            "有点奇怪？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165F")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆在支援科和发呆的琪雅？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【未变更】\x01",      # 0
            "【已对话】\x01",      # 1
            "【未对话】\x01",      # 2
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
        (0, "loc_164A"),
        (1, "loc_164F"),
        (2, "loc_1657"),
        (SWITCH_DEFAULT, "loc_165F"),
    )


    label("loc_164A")

    Jump("loc_165F")

    label("loc_164F")

    SetScenarioFlags(0x151, 6)
    Jump("loc_165F")

    label("loc_1657")

    ClearScenarioFlags(0x151, 6)
    Jump("loc_165F")

    label("loc_165F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 6)), scpexpr(EXPR_END)), "loc_16DF")

    #C0007
    ChrTalk(
        0x109,
        "#10105F啊……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00008F……听你这么一说，我也觉得\x01",
            "她刚才好像有些发呆呢。\x02\x03",

            "#00001F揭幕式时发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1734")

    label("loc_16DF")


    #C0009
    ChrTalk(
        0x109,
        (
            "#10105F哎……？\x01",
            "我觉得和平时没什么不同啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00001F揭幕式时发生了什么事吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1734")


    #C0011
    ChrTalk(
        0xD,
        (
            "#01500F不，并没有发生\x01",
            "什么特别的事……\x02\x03",

            "#01508F但我总觉得琪雅在看\x01",
            "揭幕式的时候有些失神。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x105,
        (
            "#10300F嗯……也许是被兰花塔的\x01",
            "壮观景象震撼到了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xD,
        (
            "#01505F啊……\x01",
            "是这样吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00003F唔……搞不懂原因，\x01",
            "总之我们会多留意一下的。\x02\x03",

            "#00000F谢谢你这么\x01",
            "关心琪雅啊，小滴。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xD,
        (
            "#01500F不，没什么……\x01",
            "真不好意思，我说了\x01",
            "一些奇怪的话。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 2)
    Jump("loc_1904")

    label("loc_188B")


    #C0016
    ChrTalk(
        0xD,
        (
            "#01502F多亏琪雅，\x01",
            "我在今天的揭幕式上\x01",
            "玩得非常开心呢。\x02\x03",

            "如果我的眼睛以后能看见东西了，\x01",
            "好想和琪雅一起\x01",
            "再看看兰花塔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1904")

    Jump("loc_1982")

    label("loc_1909")


    #C0017
    ChrTalk(
        0xD,
        (
            "#01502F多亏琪雅，\x01",
            "我在今天的揭幕式上\x01",
            "玩得非常开心呢。\x02\x03",

            "如果我的眼睛以后能看见东西了，\x01",
            "好想和琪雅一起\x01",
            "再看看兰花塔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1982")

    Jump("loc_1990")

    label("loc_1987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1990")

    label("loc_1990")

    TalkEnd(0xD)
    Return()

    # Function_12_1367 end

    def Function_13_1994(): pass

    label("Function_13_1994")

    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A57")

    #C0018
    ChrTalk(
        0xD,
        (
            "#01502F米海尔，听说你\x01",
            "马上就可以出院了。\x02\x03",

            "呵呵，恭喜你，\x01",
            "以后要多保重哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xE,
        (
            "嗯……小滴，\x01",
            "多谢你这段时间对我的照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xE,
        (
            "我一定会写信给你的。\x01",
            "小滴，你也要多保重呀！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_1ACD")

    label("loc_1A57")


    #C0021
    ChrTalk(
        0xD,
        (
            "#01502F米海尔能出院，\x01",
            "我也觉得很高兴呢。\x02\x03",

            "以后要是有机会，我会和爸爸\x01",
            "一起去列曼找你玩的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        (
            "嗯……！\x01",
            "我等你！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACD")

    OP_4C(0xE, 0xFF)
    Return()

    # Function_13_1994 end

    def Function_14_1AD2(): pass

    label("Function_14_1AD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1AE3")
    Jump("loc_1B6C")

    label("loc_1AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1AF4")
    Call(0, 13)
    Jump("loc_1B6C")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B05")
    Call(0, 29)
    Jump("loc_1B6C")

    label("loc_1B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B20")
    Call(0, 34)
    Jump("loc_1B6C")

    label("loc_1B20")


    #C0023
    ChrTalk(
        0xE,
        (
            "出院……\x01",
            "这一天竟然真的到来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xE,
        (
            "得、得赶快联系\x01",
            "身在列曼的妈妈！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6C")

    TalkEnd(0xFE)
    Return()

    # Function_14_1AD2 end

    def Function_15_1B70(): pass

    label("Function_15_1B70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C00")

    #C0025
    ChrTalk(
        0xF,
        (
            "#01400F『幻兽』的调查工作就拜托你们了。\x02\x03",

            "我明天就会返回协会，\x01",
            "并参与调查工作，在我回去之前，\x01",
            "就拜托你们协助斯克特他们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C78")

    label("loc_1C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1C")
    Call(0, 18)
    Jump("loc_1C78")

    label("loc_1C1C")


    #C0026
    ChrTalk(
        0xF,
        (
            "#01400F阁下说他想\x01",
            "见见小滴。\x02\x03",

            "#01403F……百忙之中还记挂着一个小女孩，\x01",
            "真是让人感动啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C78")

    TalkEnd(0xFE)
    Return()

    # Function_15_1B70 end

    def Function_16_1C7C(): pass

    label("Function_16_1C7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9B")
    Call(0, 18)
    Jump("loc_1CFC")

    label("loc_1C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAD")
    Call(0, 17)
    Jump("loc_1CFC")

    label("loc_1CAD")


    #C0027
    ChrTalk(
        0x15,
        (
            "啊，对了，\x01",
            "待会我得去\x01",
            "见见赛兰德。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x15,
        (
            "好久没见到她了，\x01",
            "但愿她一切都好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFC")

    TalkEnd(0xFE)
    Return()

    # Function_16_1C7C end

    def Function_17_1D00(): pass

    label("Function_17_1D00")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x15, 0xFF)

    #C0029
    ChrTalk(
        0x15,
        (
            "说起来，我听说小滴的\x01",
            "眼睛失明了。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x15,
        (
            "……你一定很不安吧，\x01",
            "但这家医院的医生们\x01",
            "医术高超，很值得信赖。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x15,
        (
            "虽然也许会花上不少时间，\x01",
            "但你一定要努力忍耐，\x01",
            "并相信自己的眼睛可以复明哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xD,
        (
            "#01505F啊……\x01",
            "谢谢您。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x15, 0xFF)
    Return()

    # Function_17_1D00 end

    def Function_18_1DF0(): pass

    label("Function_18_1DF0")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xD, 0x2)
    OP_4B(0xF, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    OP_68(-99630, 1000, 53940, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19710, 0)
    SetChrPos(0x101, -100420, 0, 52850, 0)
    SetChrPos(0x102, -98870, 0, 52710, 315)
    SetChrPos(0x104, -98240, 0, 51510, 315)
    SetChrPos(0x109, -99630, 50, 50760, 0)
    SetChrPos(0x105, -100770, 50, 51180, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0033
    ChrTalk(
        0xD,
        "#01505F啊……是支援科的各位吗？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x15,
        "哦，你们是……\x02",
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x101,
        (
            "#00005F您、您是雷米菲利亚公国的\x01",
            "阿尔伯特大公阁下……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x109,
        "#10105F而且亚里欧斯先生也在……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xF,
        (
            "#01403F嗯，真是巧遇啊。\x02\x03",

            "#01400F阁下，他们就是我曾经和您\x01",
            "提到过的『特别任务支援科』成员。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x15,
        "哦哦，原来就是他们啊。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x15,
        "……初次见面，支援科的各位。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x15,
        (
            "我的名字是阿尔伯特·冯·巴尔特罗梅斯，\x01",
            "雷米菲利亚的国家元首。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x15,
        (
            "为了克洛斯贝尔，希望各位\x01",
            "今后也继续努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#00002F是、是的，请多指教。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x15,
        (
            "呵呵，我听亚里欧斯\x01",
            "说起过你们，\x01",
            "一直都想见上一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x15,
        "还有艾莉，我们也好久没见了啊。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，久疏问候。\x01",
            "看来大公阁下的身体十分安康……\x02\x03",

            "#00103F不过，真没想到\x01",
            "能在医院\x01",
            "与您偶遇呢。\x02\x03",

            "#00105F您今天是来\x01",
            "视察的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x15,
        (
            "嗯，毕竟雷米菲利亚公国是\x01",
            "这所医院的资助方之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x15,
        (
            "而且我还想来慰问一下\x01",
            "亚里欧斯的女儿。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xD,
        "#01502F非、非常感谢您的关心，大公阁下。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xF,
        (
            "#01400F关于这一点，\x01",
            "我个人认为您还是应该\x01",
            "多带些护卫人员。\x02\x03",

            "#01403F此次出行，只有我和司机陪同，\x01",
            "未免有些草率了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0xF, 500)
    Sleep(300)

    #C0050
    ChrTalk(
        0x15,
        (
            "呵呵，亚里欧斯，\x01",
            "这是因为我很信任\x01",
            "你的能力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x15,
        (
            "而且只不过是一次视察而已，\x01",
            "如果带上过多护卫人员，\x01",
            "难免会影响到医院的正常工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00000F（阿尔伯特大公……\x01",
            "  不仅认识亚里欧斯先生，\x01",
            "  连艾莉也认识啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        (
            "#10100F（嗯，他和艾莉小姐、\x01",
            "  亚里欧斯先生……\x01",
            "  还有赛兰德教授好像都是旧识。）\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x105,
        (
            "#10300F（呵呵，比我想象中\x01",
            "  还要爽朗亲和呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(300)

    #C0055
    ChrTalk(
        0x15,
        (
            "总之，我也会为\x01",
            "你们加油的。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x15,
        "今后请继续努力吧。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00000F是，非常感谢您。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#00100F大公阁下，今天回去时，\x01",
            "请一定要多加注意。\x02\x03",

            "在明天的通商会议上，\x01",
            "我们会给您加油的。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x15,
        "呵呵，我一定努力。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xD, 0x0)
    OP_4C(0xF, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0xF, 0x5A, 0x0)
    OP_93(0x15, 0x2D, 0x0)
    SetScenarioFlags(0x1C6, 5)
    ClearChrFlags(0xF, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -99930, 0, 52260, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_18_1DF0 end

    def Function_19_258B(): pass

    label("Function_19_258B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_25F5")

    #C0060
    ChrTalk(
        0x8,
        (
            "#01900F警督，非常感谢\x01",
            "您在危机时刻\x01",
            "救了我～\x02\x03",

            "#01909F我以后一定会多抽空\x01",
            "来探望您的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2883")

    label("loc_25F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_277B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26FA")

    #C0061
    ChrTalk(
        0x8,
        (
            "#06400F笔记本、艾尼格玛……\x01",
            "还有牙刷牙膏……\x02\x03",

            "#06405F啊，对了，还要去跟\x01",
            "其他的患者和护士们\x01",
            "打声招呼！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00000F（看来芙兰还得花上一段时间\x01",
            "  才能做好准备……）\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#10404F（既然如此，\x01",
            "  我们就利用这段时间\x01",
            "  去探望其他人吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2776")

    label("loc_26FA")


    #C0064
    ChrTalk(
        0x8,
        (
            "#06405F啊啊，对了，还得\x01",
            "换上制服才行……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0065
    ChrTalk(
        0x8,
        "#06401F……你们不准偷看哦～\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00012F才、才不会偷看呢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_2776")

    Jump("loc_2883")

    label("loc_277B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_END)), "loc_2883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286A")

    #C0067
    ChrTalk(
        0x8,
        "#11703F呼……呼……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2834")

    #C0068
    ChrTalk(
        0x105,
        "#10300F呵呵，睡得很香呢。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x136,
        (
            "#01302F没事的，诺艾尔小姐。\x01",
            "看她这样子，一定很快就能恢复健康。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        "#10102F嗯……谢谢你。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2862")

    label("loc_2834")


    #C0071
    ChrTalk(
        0x109,
        (
            "#10103F（芙兰……\x01",
            "  你要快点好起来啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2862")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2883")

    label("loc_286A")


    #C0072
    ChrTalk(
        0x8,
        "#11703F呼……呼……\x02",
    )

    CloseMessageWindow()

    label("loc_2883")

    TalkEnd(0xFE)
    Return()

    # Function_19_258B end

    def Function_20_2887(): pass

    label("Function_20_2887")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2927")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A5")
    Call(0, 21)
    Jump("loc_2922")

    label("loc_28A5")


    #C0073
    ChrTalk(
        0x9,
        (
            "我马上就要和同事们会合了……\x01",
            "总之，我会在力所能及的\x01",
            "范围内尽量帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "你们肯定也有很多事要忙吧，\x01",
            "记得要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2922")

    Jump("loc_2DB3")

    label("loc_2927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29EE")

    #C0075
    ChrTalk(
        0x9,
        (
            "独立无效宣言吗……\x01",
            "没想到你们竟能\x01",
            "做到这种地步。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "身处市内的赛尔盖等人\x01",
            "一定也会趁此机会\x01",
            "开始行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "看来我暂时无法\x01",
            "和大家会合了。\x01",
            "……之后的事就交给你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A68")

    label("loc_29EE")


    #C0078
    ChrTalk(
        0x9,
        (
            "我估计，身处市内的\x01",
            "赛尔盖等人也会趁此机会\x01",
            "开始行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "看来我暂时无法\x01",
            "和大家会合了。\x01",
            "……之后的事就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A68")

    Jump("loc_2DB3")

    label("loc_2A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2AEE")

    #C0080
    ChrTalk(
        0x9,
        (
            "看来我暂时无法\x01",
            "和大家会合了。\x01",
            "既然如此，那就专心休养一阵子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "现在只能靠雷蒙德和赛尔盖他们\x01",
            "多加努力了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB3")

    label("loc_2AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_2B63")

    #C0082
    ChrTalk(
        0x9,
        (
            "哈哈，你看，我这不是没事吗，\x01",
            "完全没必要那么在意啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "你自己也是\x01",
            "重伤初愈，\x01",
            "一定要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB3")

    label("loc_2B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2BD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7E")
    Call(0, 21)
    Jump("loc_2BD0")

    label("loc_2B7E")


    #C0084
    ChrTalk(
        0x9,
        (
            "总之不管怎样……\x01",
            "请大家小心点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "如果能在近期和赛尔盖他们\x01",
            "会合就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD0")

    Jump("loc_2DB3")

    label("loc_2BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_2DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D93")

    #C0086
    ChrTalk(
        0x9,
        "#90W……………………………\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x109,
        (
            "#10108F……等警督醒过来以后，\x01",
            "我一定要郑重向他道谢，\x01",
            "感谢他保护了芙兰。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D5B")

    #C0088
    ChrTalk(
        0x136,
        (
            "#01303F他的呼吸系统\x01",
            "受到了相当严重的损伤，\x01",
            "恐怕需要很长时间才能恢复……\x02\x03",

            "#01300F不过已经渡过危险期了，\x01",
            "近期内一定能\x01",
            "醒过来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#00103F但愿如此……\x02\x03",

            "#00100F……警督这里有雷蒙德警官\x01",
            "照料就可以了。\x01",
            "我们走吧，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#00000F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D8B")

    label("loc_2D5B")


    #C0091
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x01",
            "如果能快点恢复健康就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D8B")

    SetScenarioFlags(0x0, 1)
    Jump("loc_2DB3")

    label("loc_2D93")


    #C0092
    ChrTalk(
        0x9,
        "#90W……………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2DB3")

    TalkEnd(0xFE)
    Return()

    # Function_20_2887 end

    def Function_21_2DB7(): pass

    label("Function_21_2DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3062")
    OP_4B(0x9, 0xFF)
    OP_4B(0x16, 0xFF)

    def lambda_2DCD():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2DCD)
    Sleep(0)

    def lambda_2DDD():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_2DDD)
    Sleep(0)

    def lambda_2DED():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_2DED)
    Sleep(0)

    def lambda_2DFD():
        TurnDirection(0x3, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_2DFD)
    Sleep(0)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x16, 0x0, 0)

    #C0093
    ChrTalk(
        0x9,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x16,
        "呵呵呵，你们好啊。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00000F多诺邦警督……！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        "#00200F您已经可以走动了吗？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "嗯，刚才已经办好\x01",
            "出院手续了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "听说克洛斯贝尔市解放作战\x01",
            "大获成功，\x01",
            "我也准备去和同事们会合。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x16,
        (
            "其实还要再过几天才到\x01",
            "预定的出院日期。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x16,
        (
            "我原本并不想让他逞强，\x01",
            "可他执意如此，\x01",
            "我也只好让步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，雷蒙德那家伙\x01",
            "一定会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#00100F警督归队之后，\x01",
            "搜查二科肯定能发挥\x01",
            "更强的作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "总之，我会在力所能及的\x01",
            "范围内尽量帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "你们肯定也有很多事要忙吧，\x01",
            "记得多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#00000F好的，非常感谢您！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 7)
    TurnDirection(0x9, 0x16, 0)
    TurnDirection(0x16, 0x9, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_33E2")

    label("loc_3062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_33E2")

    def lambda_3070():
        TurnDirection(0x0, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3070)
    Sleep(0)

    def lambda_3080():
        TurnDirection(0x1, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3080)
    Sleep(0)

    def lambda_3090():
        TurnDirection(0x2, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_3090)
    Sleep(0)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3138")
    Jump("loc_3182")

    label("loc_3138")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3158")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3182")

    label("loc_3158")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3178")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3182")

    label("loc_3178")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3182")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x16, 0x10)
    TurnDirection(0x16, 0x0, 0)
    OP_52(0x16, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3238")
    Jump("loc_3282")

    label("loc_3238")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3258")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3282")

    label("loc_3258")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3278")
    OP_52(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3282")

    label("loc_3278")

    OP_52(0x16, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3282")

    OP_52(0x16, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x16, 0x10)

    #C0106
    ChrTalk(
        0x9,
        (
            "哎呀呀，让你们\x01",
            "见笑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "我和法拉结婚以来，\x01",
            "一直被她牵着鼻子走……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00000F哈哈，我觉得她是个好太太呢。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x105,
        "#10402F呵呵，而且也十分可爱。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x16,
        "哎呀……¤\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x16,
        (
            "呵呵，人家说我很可爱哦，\x01",
            "你听到了吗，老公⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "（……就是因为你在这些家伙还有雷蒙德\x01",
            "  面前也这副样子，我才为难啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x16, 0x10)

    label("loc_33E2")

    Return()

    # Function_21_2DB7 end

    def Function_22_33E3(): pass

    label("Function_22_33E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_END)), "loc_3506")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3494")

    #C0113
    ChrTalk(
        0xA,
        (
            "多诺邦警督拼了命才\x01",
            "救下我。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "虽然我一直都很没用……\x01",
            "但以后一定要\x01",
            "有所长进。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "总有一天要成为\x01",
            "一名出色的搜查官、\x01",
            "不辱警督之名的好部下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3506")

    label("loc_3494")


    #C0116
    ChrTalk(
        0xA,
        (
            "虽然我一直都很没用……\x01",
            "但以后一定要\x01",
            "有所长进。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "总有一天要成为\x01",
            "一名出色的搜查官、\x01",
            "不辱警督之名的好部下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3506")

    TalkEnd(0xFE)
    Return()

    # Function_22_33E3 end

    def Function_23_350A(): pass

    label("Function_23_350A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374F")

    #C0118
    ChrTalk(
        0xB,
        (
            "#11601F警察弟弟……\x01",
            "好像发生了\x01",
            "很严重的情况吧。\x02\x03",

            "#11606F听说突然出现了\x01",
            "一棵来历不明的\x01",
            "『大树』？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00001F是啊……说实话，\x01",
            "我们也不知道接下来会发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        (
            "#00103F医院也不能\x01",
            "说是完全安全的。\x02\x03",

            "#00101F伊莉娅小姐，您一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xB,
        (
            "#11609F哈哈哈，谢谢。\x01",
            "虽然并不了解\x01",
            "事情的具体状况……\x02\x03",

            "#11600F但我相信，只要你们不放弃，\x01",
            "最后就一定能成功\x01",
            "把握住重要之物。\x02\x03",

            "#11604F我也绝对不会放弃的，\x01",
            "直到重新回到舞台……\x02\x03",

            "#11609F所以，你们也一定\x01",
            "要努力到最后哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x103,
        "#00200F是……！\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#00309F伊莉娅小姐的声援\x01",
            "胜过百人之力！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_3747")
    Call(0, 77)
    Return()

    label("loc_3747")

    SetScenarioFlags(0x0, 3)
    Jump("loc_37E1")

    label("loc_374F")


    #C0124
    ChrTalk(
        0xB,
        (
            "#11604F只要你们不放弃，\x01",
            "最后就一定能成功\x01",
            "把握住重要之物。\x02\x03",

            "#11609F我也绝对不会放弃的，\x01",
            "直到重新回到舞台……\x01",
            "所以，你们也一定要努力到最后哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37E1")

    Jump("loc_3A38")

    label("loc_37E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6C), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3801")
    Call(0, 86)
    Jump("loc_3A38")

    label("loc_3801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_38E1")

    #C0125
    ChrTalk(
        0xB,
        (
            "#11600F只要你们不放弃，\x01",
            "最后就一定能成功\x01",
            "把握住重要之物。\x02\x03",

            "#11604F我也绝对不会放弃的，\x01",
            "直到重新回到舞台……\x01",
            "所以，你们也一定要努力到最后哦。\x02\x03",

            "#11609F呵呵，站在门外的那孩子\x01",
            "也拜托你们多加照顾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399E")

    label("loc_38E1")


    #C0126
    ChrTalk(
        0xB,
        (
            "#11600F只要你们不放弃，\x01",
            "最后就一定能成功\x01",
            "把握住重要之物。\x02\x03",

            "#11604F我也绝对不会放弃的，\x01",
            "直到重新回到舞台……\x01",
            "所以，你们也一定要努力到最后哦。\x02\x03",

            "#11609F呵呵，那孩子也拜托你们多加照顾了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399E")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3A38")

    label("loc_39A6")


    #C0127
    ChrTalk(
        0xB,
        (
            "#11604F只要你们不放弃，\x01",
            "最后就一定能成功\x01",
            "把握住重要之物。\x02\x03",

            "#11609F我也绝对不会放弃的，\x01",
            "直到重新回到舞台……\x01",
            "所以，你们也一定要努力到最后哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A38")

    Jump("loc_4337")

    label("loc_3A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CCD")

    #C0128
    ChrTalk(
        0xB,
        (
            "#11603F警察弟弟，有传闻说市内\x01",
            "出大事了啊……\x02\x03",

            "#11601F据说几个月前那起袭击事件的\x01",
            "真相已经被公开了？\x02\x03",

            "不过具体情报被限制了，\x01",
            "没有传到这里来……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#00001F伊莉娅小姐……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        (
            "#00108F（对伊莉娅小姐而言，\x01",
            "  那就是害得她受到重伤的\x01",
            "  根本原因啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)

    #C0131
    ChrTalk(
        0xB,
        (
            "#11603F……事到如今，我对那起事件的\x01",
            "真相根本毫无兴趣。\x02\x03",

            "#11600F对我来说，更重要的是下一次\x01",
            "复健运动要在何时开始。\x02\x03",

            "#11609F为了尽早回到舞台，\x01",
            "我好想尽快活动一下身体，\x01",
            "都要按耐不住了¤\x02",
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

    #C0132
    ChrTalk(
        0x101,
        "#00012F哈哈，该怎么说呢……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#00202F真不愧是伊莉娅小姐啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 2)
    Jump("loc_3D6A")

    label("loc_3CCD")


    #C0134
    ChrTalk(
        0xB,
        (
            "#11602F我一定要努力进行复健运动，\x01",
            "重新回到舞台上去，\x01",
            "所以对其它的事完全没兴趣。\x02\x03",

            "#11609F啊啊，还没到下次复健运动的时间吗？\x01",
            "我想要快点活动一下身体啊～¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D6A")

    Jump("loc_4337")

    label("loc_3D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC2")

    #C0135
    ChrTalk(
        0xB,
        (
            "#11600F据赛兰德医生所说，\x01",
            "现阶段还不知道\x01",
            "以后能不能走路……\x02\x03",

            "#11604F但既然并非毫无希望，\x01",
            "我就没有理由放弃。\x02\x03",

            "#11602F人这种生物，为了自己重要的东西，\x01",
            "可是会不惜一切努力的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2B")

    #C0136
    ChrTalk(
        0x103,
        (
            "#00200F看着伊莉娅小姐，\x01",
            "我也忍不住这样想了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "#11604F呵呵，警察弟弟。\x01",
            "你们要是见到了莉夏，就替我转告她一句话。\x02\x03",

            "#11600F『面对那重要之物，\x01",
            "你能不为之努力吗？』\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00000F好的，我知道了。\x01",
            "要是能遇到她，\x01",
            "我一定会转告她的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FBA")

    label("loc_3F2B")


    #C0139
    ChrTalk(
        0x101,
        (
            "#00008F（虽然已经帮伊莉娅小姐\x01",
            "  转告了那句话给莉夏……\x01",
            "  但她们现在恐怕还没法见面。）\x02\x03",

            "#00003F（关于莉夏的事，\x01",
            "  暂时还是先向她保密吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBA")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4041")

    label("loc_3FC2")


    #C0140
    ChrTalk(
        0xB,
        (
            "#11604F人为了自己重要的东西\x01",
            "可是会不惜一切努力的。\x02\x03",

            "#11600F毕竟不是毫无希望，\x01",
            "说不定能恢复到自由走动呢，\x01",
            "我没有理由放弃。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4041")

    Jump("loc_4337")

    label("loc_4046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_421E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B7")

    #C0141
    ChrTalk(
        0xB,
        (
            "#11600F我有点担心市内\x01",
            "彩虹剧团的各位。\x02\x03",

            "#11609F但以他们的性格来说，就算处在\x01",
            "这种状况下，应该也会继续坚持练习的。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#00000F哈哈，您是在担心这个啊。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#00202F彩虹剧团的各位肯定\x01",
            "都在专心练习。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#10400F呵呵，因为大家都是\x01",
            "专业演员嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "#11604F另外，修利正处在飞速进步期……\x02\x03",

            "#11609F就算是为了迎接我回归，\x01",
            "也希望他们能好好练习。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4219")

    label("loc_41B7")


    #C0146
    ChrTalk(
        0xB,
        (
            "#11600F我有点担心市内\x01",
            "彩虹剧团的各位。\x02\x03",

            "#11609F就算是为了迎接我回归，\x01",
            "也希望他们能好好练习。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4219")

    Jump("loc_4337")

    label("loc_421E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_END)), "loc_4337")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4310")

    #C0147
    ChrTalk(
        0xB,
        "#11603F#90W……………………………\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        (
            "#00306F……话说回来，真没想到会看到\x01",
            "这副模样的伊莉娅小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        (
            "#00208F是啊……\x01",
            "我至今依然不敢相信呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00003F伊莉娅小姐一定能回到舞台……\x01",
            "我们如今就坚信这一点吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4337")

    label("loc_4310")


    #C0151
    ChrTalk(
        0xB,
        "#11603F#90W……………………………\x02",
    )

    CloseMessageWindow()

    label("loc_4337")

    TalkEnd(0xFE)
    Return()

    # Function_23_350A end

    def Function_24_433B(): pass

    label("Function_24_433B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43FE")

    #C0152
    ChrTalk(
        0xC,
        (
            "#04200F莉夏姐……\x01",
            "就拜托\x01",
            "你们了。\x02\x03",

            "#04203F我总觉得只要莉夏姐能回来，\x01",
            "伊莉娅小姐一定就会\x01",
            "恢复精神……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#00000F……好，你就等着吧。\x01",
            "我们一定会把她\x01",
            "找出来的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4483")

    label("loc_43FE")


    #C0154
    ChrTalk(
        0xC,
        (
            "#04203F我总觉得只要莉夏姐能回来，\x01",
            "伊莉娅小姐一定就会\x01",
            "恢复精神……\x02\x03",

            "#04200F在那之前，我们彩虹剧团一定要全力\x01",
            "支持伊莉娅小姐才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4483")

    TalkEnd(0xFE)
    Return()

    # Function_24_433B end

    def Function_25_4487(): pass

    label("Function_25_4487")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4498")
    Jump("loc_46E0")

    label("loc_4498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_459E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4545")

    #C0155
    ChrTalk(
        0x10,
        (
            "我们的物资不够了，\x01",
            "得去申请供给才行……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x10,
        (
            "但由于独立无效宣言，\x01",
            "国防军的士兵们都回\x01",
            "部队里去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x10,
        (
            "唔……真头疼啊。\x01",
            "今后该如何交涉呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4599")

    label("loc_4545")


    #C0158
    ChrTalk(
        0x10,
        (
            "唔……真头疼啊。\x01",
            "国防军都回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x10,
        (
            "今后我该如何和他们交涉\x01",
            "物资的供给呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4599")

    Jump("loc_46E0")

    label("loc_459E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_45AC")
    Jump("loc_46E0")

    label("loc_45AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_45BA")
    Jump("loc_46E0")

    label("loc_45BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_46E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4677")

    #C0160
    ChrTalk(
        0x10,
        (
            "以前医院遭到袭击的时候，\x01",
            "据说有人躲进了这个\x01",
            "储藏室。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x10,
        (
            "在那起事件中，\x01",
            "我的腹部\x01",
            "中了一枪……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x10,
        (
            "现在回头一想，\x01",
            "我当时也该赶紧躲起来。\x01",
            "唉……真是失策啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_46E0")

    label("loc_4677")


    #C0163
    ChrTalk(
        0x10,
        (
            "以前医院遭到袭击的时候，\x01",
            "我中了一枪。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x10,
        (
            "现在回头一想，\x01",
            "我当时也该赶紧躲起来。\x01",
            "唉……真是失策啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E0")

    TalkEnd(0xFE)
    Return()

    # Function_25_4487 end

    def Function_26_46E4(): pass

    label("Function_26_46E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_46F5")
    Jump("loc_5226")

    label("loc_46F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4703")
    Jump("loc_5226")

    label("loc_4703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4711")
    Jump("loc_5226")

    label("loc_4711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4BAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A53")
    TurnDirection(0x11, 0x0, 0)

    #C0165
    ChrTalk(
        0x11,
        (
            "#01309F话说回来……\x01",
            "真希望小滴现在也还好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x103,
        (
            "#00203F……是啊，的确如此。\x02\x03",

            "#00200F琪雅之前也\x01",
            "非常担心她呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00008F按正常思路来想，\x01",
            "小滴现在应该是在\x01",
            "兰花塔吧。\x02\x03",

            "#00003F要是我们能见到\x01",
            "她就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x11,
        (
            "#01302F嗯，另外……\x01",
            "真希望支援科的各位\x01",
            "也能早日聚齐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x105,
        (
            "#10406F说实话，这恐怕\x01",
            "是相当艰辛的。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#00003F……但要想夺回琪雅，\x01",
            "大家的力量都是不可或缺的。\x02\x03",

            "#00000F所以，无论遇到怎样的艰难险阻，\x01",
            "我们也绝不能放弃前进。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x11,
        (
            "#01309F呵呵，罗伊德，你们一定能做到的。\x02\x03",

            "#01304F我会在这里向女神祈祷……\x01",
            "你们一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00000F谢谢你，塞茜尔姐姐，\x01",
            "你的声援胜过百人之力。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A44")

    #C0173
    ChrTalk(
        0x107,
        (
            "#01200F#13C……………………………………\x02\x03",

            "（不愧是你的后代啊……\x01",
            "  乌尔斯拉。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x107, 500)

    #C0174
    ChrTalk(
        0x103,
        (
            "#00205F蔡特……\x01",
            "你怎么了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x103, 500)

    #C0175
    ChrTalk(
        0x107,
        (
            "#01203F#13C……呵呵，别介意。\x01",
            "我有时候也会\x01",
            "陷入沉思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A44")

    OP_93(0x11, 0x5A, 0x0)
    SetScenarioFlags(0x1AC, 2)
    Jump("loc_4BAA")

    label("loc_4A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B29")
    SetChrSubChip(0xB, 0x2)

    #C0176
    ChrTalk(
        0x11,
        (
            "#01300F伊莉娅，差不多该去\x01",
            "接受复健训练了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "#11604F嗯，知道了。\x02\x03",

            "#11609F今天也拜托你了啊，\x01",
            "塞茜尔护士主任⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x11,
        (
            "#01309F呵呵，这是为了伊莉娅和大家嘛。\x01",
            "我当然会努力帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_4BAA")

    label("loc_4B29")


    #C0179
    ChrTalk(
        0x11,
        (
            "#01302F罗伊德，你们一定能把\x01",
            "支援科的各位救出来的，\x01",
            "也一定能和琪雅再会。\x02\x03",

            "#01304F我会在这里向女神祈祷……\x01",
            "你们一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BAA")

    Jump("loc_5226")

    label("loc_4BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4BBD")
    Jump("loc_5226")

    label("loc_4BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4BCB")
    Jump("loc_5226")

    label("loc_4BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4BDC")
    Call(0, 27)
    Jump("loc_5226")

    label("loc_4BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4BED")
    Call(0, 27)
    Jump("loc_5226")

    label("loc_4BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4BFB")
    Jump("loc_5226")

    label("loc_4BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB9")
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x103, 500)

    #C0180
    ChrTalk(
        0x11,
        (
            "#01302F哎呀，这不是小缇欧吗，\x01",
            "你已经回到支援科了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        "#00202F是的，我昨天才刚回来。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x11,
        (
            "#01309F呵呵，能再次见到你真是太好了。\x02\x03",

            "#01304F我听说你这段时间\x01",
            "一直非常忙……\x01",
            "嗯，不过你今天气色不错呢。\x02\x03",

            "#01300F可别再像之前\x01",
            "那样晕倒了哦，\x01",
            "一定要多注意自己的身体。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#00204F呵呵，那时候\x01",
            "真是承蒙照顾了。\x02\x03",

            "#00200F不过，要是能再次\x01",
            "睡在塞茜尔小姐你那柔软的床上的话，\x01",
            "晕倒也并不是什么坏事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x104,
        "#00309F唔，我完全同意这点。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        "#00006F兰迪，我说你啊……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#00106F拜托你自重些啊。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x11,
        (
            "#01302F呵呵……\x01",
            "你们完全回到以前\x01",
            "的气氛了呢。\x02\x03",

            "#01304F小缇欧一回来，\x01",
            "支援科也终于\x01",
            "完全启动机能了吗。\x02\x03",

            "#01309F我会一直支持你们的，\x01",
            "今后你们也要多努力啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x151, 5)
    ClearChrFlags(0x11, 0x10)
    Jump("loc_4F0E")

    label("loc_4EB9")


    #C0188
    ChrTalk(
        0x11,
        (
            "#01300F米海尔马上就要出院了。\x02\x03",

            "#01304F虽然有点觉得寂寞……\x01",
            "呵呵，但真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F0E")

    Jump("loc_5226")

    label("loc_4F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F24")
    Call(0, 29)
    Jump("loc_5226")

    label("loc_4F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C5")

    #C0189
    ChrTalk(
        0x101,
        (
            "#00000F啊……\x01",
            "塞茜尔姐姐，原来你在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#00100F我记得这里是\x01",
            "小滴的病房吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x11,
        (
            "#01300F是啊，趁她不在，\x01",
            "我来打扫一下。\x02\x03",

            "#01304F小滴今天去\x01",
            "市里玩了。\x02\x03",

            "#01309F她从前段时间起，\x01",
            "就一直很高兴地和我说\x01",
            "『能和琪雅见面了』。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，她们已经成为\x01",
            "很好的朋友了。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#00000F嗯，毕竟对方是琪雅，\x01",
            "这也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，的确呢。\x01",
            "我觉得琪雅好像有一种天生的才能，\x01",
            "能和他人建立起友好的关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x109,
        "#10102F呵呵……好像真是这样呢。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x11,
        (
            "#01300F多亏了她，\x01",
            "小滴变得比以前开朗多了……\x01",
            "真是十分感谢琪雅呢。\x02\x03",

            "#01302F下次轮休的时候，\x01",
            "我去找琪雅一起玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#00000F好，琪雅一定会很高兴的。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x11,
        "#01309F呵呵，到时候就要麻烦大家了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 1)
    Jump("loc_5226")

    label("loc_51C5")


    #C0199
    ChrTalk(
        0x11,
        (
            "#01300F小滴\x01",
            "现在应该正和\x01",
            "琪雅一起玩吧。\x02\x03",

            "#01309F呵呵，难得能外出，\x01",
            "真希望她能玩得开心点呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5226")

    TalkEnd(0xFE)
    Return()

    # Function_26_46E4 end

    def Function_27_522A(): pass

    label("Function_27_522A")

    SetChrSubChip(0xD, 0x2)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539B")

    #C0200
    ChrTalk(
        0xD,
        (
            "#11200F塞茜尔小姐……\x01",
            "昨天似乎有很多急救车\x01",
            "出动了啊。\x02\x03",

            "#11210F我听说是发生了\x01",
            "什么重大事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x11,
        (
            "#01303F听说是因为西克洛斯贝尔街道\x01",
            "发生了列车脱轨事故。\x02\x03",

            "#01302F不过，放心吧。\x01",
            "多亏各位医生的努力，\x01",
            "没有任何人丧生哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xD,
        (
            "#11202F这样啊……太好了。\x02\x03",

            "#11208F我还在担心，生怕和我当年\x01",
            "遇到的那起事故一样严重……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x11,
        "#01308F小滴……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_5433")

    label("loc_539B")


    #C0204
    ChrTalk(
        0x11,
        (
            "#01300F多亏各位医生的努力，\x01",
            "列车事故的伤者们\x01",
            "都已经得救了。\x02\x03",

            "所以，你不用担心\x01",
            "事故的事情哦。\x01",
            "现在就专心于康复治疗吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xD,
        "#11202F好的……谢谢您。\x02",
    )

    CloseMessageWindow()

    label("loc_5433")

    Jump("loc_55CF")

    label("loc_5438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_55CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5453")
    Call(0, 28)
    Jump("loc_55CF")

    label("loc_5453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5558")

    #C0206
    ChrTalk(
        0x11,
        (
            "#01304F呵呵，那我就读给你听了哦。\x01",
            "……咳咳。\x02\x03",

            "#01300F『小滴，你这段时间还好吗？\x01",
            "  我过得很好。』\x02\x03",

            "『我每晚都会向女神祈祷，\x01",
            "  祈祷小滴的眼睛能够\x01",
            "  恢复光明。』\x02\x03",

            "#01309F呵呵，很符合那孩子的性格呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xD,
        (
            "#11202F米海尔……\x01",
            "……我真的好高兴。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_55CF")

    label("loc_5558")


    #C0208
    ChrTalk(
        0x11,
        (
            "#01304F对了，他还随信\x01",
            "寄来了照片。\x02\x03",

            "#01302F呵呵，他站在父母之间，\x01",
            "看起来十分开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xD,
        "#11209F呵呵，真好啊……\x02",
    )

    CloseMessageWindow()

    label("loc_55CF")

    SetChrSubChip(0xD, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_27_522A end

    def Function_28_55D8(): pass

    label("Function_28_55D8")

    EventBegin(0x0)
    Fade(500)
    OP_68(-98690, 1000, 54300, 0)
    MoveCamera(36, 13, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18760, 0)
    SetChrPos(0x101, -99000, 50, 53000, 0)
    SetChrPos(0x102, -100940, 50, 53000, 45)
    SetChrPos(0x103, -100740, 0, 51800, 45)
    SetChrPos(0x104, -98340, 0, 52200, 0)
    SetChrPos(0x109, -100740, 0, 50600, 0)
    SetChrPos(0x105, -99240, 0, 50800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    OP_93(0x11, 0xB4, 0x0)
    SetChrSubChip(0xD, 0x2)
    OP_0D()

    #C0210
    ChrTalk(
        0x101,
        "#12P#00000F嗨，塞茜尔姐姐，小滴。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xD,
        "#11P#11202F啊……大家好。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x11,
        (
            "#5P#01300F啊，罗伊德，是你们啊。\x02\x03",

            "#01309F呵呵，是来看望\x01",
            "小滴的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        "#6P#00202F嗯，是的……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x109,
        (
            "#N#12P#10105F那个……是不是\x01",
            "打扰到你们了？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x11, 0xB4, 0x1F4)

    #C0215
    ChrTalk(
        0x11,
        (
            "#5P#01302F呵呵，没有的事。\x02\x03",

            "#01304F今天收到了米海尔\x01",
            "从列曼自治州寄来的信。\x02\x03",

            "#01300F我正准备读给小滴\x01",
            "听呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        "#6P#00105F米海尔……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x105,
        (
            "#12P#10302F就是由赛兰德医生主刀\x01",
            "做了手术的那个男孩吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xD,
        (
            "#11P#11204F嗯，我们两个是\x01",
            "很好的朋友……\x02\x03",

            "#11200F在他出院的时候，\x01",
            "我们约定要保持通信。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x104,
        "#12P#00302F哈哈，那可真不错。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x11,
        (
            "#5P#01300F乌尔斯拉医院时而\x01",
            "能收到这种已出院患者\x01",
            "寄来的信。\x02\x03",

            "#01304F因为工作忙碌，\x01",
            "总是没时间回信给他们……\x02\x03",

            "#01300F但对于我而言，能了解到患者们出院后的生活，\x01",
            "也是一大工作动力。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#12P#00002F哈哈，虽然你这么说，\x01",
            "但肯定认真的\x01",
            "给他们回信了。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x103,
        (
            "#6P#00204F……早知如此，我当时也应该\x01",
            "给玛萨护士长写信呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xE1, 0x1F4)

    #C0223
    ChrTalk(
        0x11,
        (
            "#5P#01302F呵呵，护士长之前和你重逢的时候，\x01",
            "真是非常高兴。\x02\x03",

            "#01309F现在也不算晚，\x01",
            "以后要是有机会就给她写信吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x103,
        (
            "#6P#00202F呵呵，等工作告一段落之后，\x01",
            "我会想想该怎么写的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x16B, 7)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -99740, 0, 53570, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xD, 0x0)
    OP_93(0x11, 0x5A, 0x0)
    OP_4C(0x11, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_55D8 end

    def Function_29_5AF7(): pass

    label("Function_29_5AF7")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D27")

    #C0225
    ChrTalk(
        0x11,
        "#01300F米海尔，你感觉如何？\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xE,
        (
            "嗯，最近完全没有发病了，\x01",
            "以前的痛苦好像都是假的一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x11,
        (
            "#01304F呵呵，太好了。\x02\x03",

            "#01300F你的出院日期也快到了……\x01",
            "马上就又能和家人一起\x01",
            "生活了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xE,
        (
            "……我现在的心情，高兴\x01",
            "和寂寞各占一半呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xE,
        (
            "回到列曼自治州以后，\x01",
            "就要和塞茜尔姐姐和小滴\x01",
            "分开了……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x11,
        (
            "#01300F……长久以来，咱们都\x01",
            "一直在一起与病魔抗争，\x01",
            "突然要分开了，确实让人感到寂寞……\x02\x03",

            "#01304F但就算相隔再远，\x01",
            "这份羁绊也一定不会断开。\x01",
            "……我是这么认为的。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xE,
        "……嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xE,
        (
            "塞茜尔姐姐，感谢你至今对我的照顾。\x01",
            "我绝对不会忘记你的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x150, 3)
    Jump("loc_5D90")

    label("loc_5D27")


    #C0233
    ChrTalk(
        0x11,
        (
            "#01309F呵呵，你一定\x01",
            "要以笑容迎接出院那一天哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xE,
        "嗯，我会的。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xE,
        (
            "……还得好好向\x01",
            "小滴道别才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D90")

    SetChrSubChip(0xE, 0x0)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_29_5AF7 end

    def Function_30_5D99(): pass

    label("Function_30_5D99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5DAA")
    Jump("loc_5E76")

    label("loc_5DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5E35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DC5")
    Call(0, 31)
    Jump("loc_5E30")

    label("loc_5DC5")

    OP_4B(0x13, 0xFF)

    #C0236
    ChrTalk(
        0x12,
        (
            "嗯～昨天的天空\x01",
            "明明不像要下雨的啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x13,
        (
            "要是你的\x01",
            "直觉比天气预报还准，\x01",
            "那还要天气预报干什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)

    label("loc_5E30")

    Jump("loc_5E76")

    label("loc_5E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5E43")
    Jump("loc_5E76")

    label("loc_5E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5E51")
    Jump("loc_5E76")

    label("loc_5E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E5F")
    Jump("loc_5E76")

    label("loc_5E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5E6D")
    Jump("loc_5E76")

    label("loc_5E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E76")

    label("loc_5E76")

    TalkEnd(0xFE)
    Return()

    # Function_30_5D99 end

    def Function_31_5E7A(): pass

    label("Function_31_5E7A")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0238
    ChrTalk(
        0x13,
        (
            "希伦……\x01",
            "你在屋顶上晒床单了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x13,
        (
            "事务长不是说过了吗，\x01",
            "天气预报说今天有雨啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x12,
        (
            "说不定不会下雨呢～\x01",
            "嘿嘿嘿，所以就赌了一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x13,
        "你干嘛要赌这种事啊！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 7)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_31_5E7A end

    def Function_32_5F38(): pass

    label("Function_32_5F38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5F49")
    Jump("loc_62C9")

    label("loc_5F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5FCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F64")
    Call(0, 31)
    Jump("loc_5FCA")

    label("loc_5F64")


    #C0242
    ChrTalk(
        0x13,
        (
            "真是的，好不容易才洗好的床单，\x01",
            "又得再洗一次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x13,
        (
            "啊啊，没空说这些了，\x01",
            "得赶快把床单收进来啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FCA")

    Jump("loc_62C9")

    label("loc_5FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5FDD")
    Jump("loc_62C9")

    label("loc_5FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_618C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6111")

    #C0244
    ChrTalk(
        0x13,
        (
            "米海尔出院那天，\x01",
            "看着那孩子精神饱满地挥着手，\x01",
            "我感动得流下了泪水呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x13,
        (
            "然后，希伦就默默地\x01",
            "递给了我一条手帕。\x01",
            "我正想着，她偶尔也有聪明的时候嘛……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x13,
        (
            "结果仔细一看，那并不是手帕，\x01",
            "而是我以前丢失不见的那条\x01",
            "我很喜欢的方巾。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x13,
        (
            "……实在是让人无话可说，\x01",
            "我的感动全被她毁了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6187")

    label("loc_6111")


    #C0248
    ChrTalk(
        0x13,
        (
            "算了，先不说这些了……\x01",
            "米海尔能够出院，\x01",
            "真是太好了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x13,
        (
            "他现在应该在列曼自治州，\x01",
            "快乐地和家人\x01",
            "生活在一起……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6187")

    Jump("loc_62C9")

    label("loc_618C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_619A")
    Jump("loc_62C9")

    label("loc_619A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_61A8")
    Jump("loc_62C9")

    label("loc_61A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_62C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6252")

    #C0250
    ChrTalk(
        0x13,
        (
            "曾在这里住院的那个叫盖巴尔的人，\x01",
            "已经出院好一段时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x13,
        (
            "那个人当时老是肆意妄为，\x01",
            "真是让人吃了不少苦头……\x01",
            "不知道他现在在做些什么呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_62C9")

    label("loc_6252")


    #C0252
    ChrTalk(
        0x13,
        (
            "啊，对了，今天好像是\x01",
            "由希伦去负责输液的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x13,
        (
            "那孩子总是闹出大问题来，\x01",
            "真是让人担心啊。\x01",
            "……待会去看看状况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62C9")

    TalkEnd(0xFE)
    Return()

    # Function_32_5F38 end

    def Function_33_62CD(): pass

    label("Function_33_62CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_62DE")
    Jump("loc_6392")

    label("loc_62DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_62EC")
    Jump("loc_6392")

    label("loc_62EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_62FA")
    Jump("loc_6392")

    label("loc_62FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6308")
    Jump("loc_6392")

    label("loc_6308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6316")
    Jump("loc_6392")

    label("loc_6316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6324")
    Jump("loc_6392")

    label("loc_6324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_633F")
    Call(0, 34)
    Jump("loc_6392")

    label("loc_633F")


    #C0254
    ChrTalk(
        0x14,
        (
            "话说回来，\x01",
            "赛兰德教授的医术\x01",
            "真是了不起。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x14,
        (
            "我有很多地方都应该\x01",
            "向她学习呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6392")

    TalkEnd(0xFE)
    Return()

    # Function_33_62CD end

    def Function_34_6396(): pass

    label("Function_34_6396")

    SetChrSubChip(0xE, 0x1)
    OP_4B(0x14, 0xFF)

    #C0256
    ChrTalk(
        0x14,
        (
            "唔……\x01",
            "手术后恢复得很好，\x01",
            "近期内应该就可以出院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x14,
        (
            "待会去联系一下你\x01",
            "身在列曼自治州的父母吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x14,
        "嗯，当然是真的。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x14,
        (
            "赛兰德教授的医术固然高超，\x01",
            "但你那决心接受手术的勇气\x01",
            "才是战胜病魔的最大关键。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x14,
        "……你做的很好。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xE,
        (
            "……呜呜……\x01",
            "谢谢你，医生……！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1, 6)
    SetChrSubChip(0xE, 0x0)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_34_6396 end

    def Function_35_64D0(): pass

    label("Function_35_64D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64EE")
    Call(0, 21)
    Jump("loc_6572")

    label("loc_64EE")


    #C0263
    ChrTalk(
        0x16,
        (
            "其实还要再过几天才到\x01",
            "预定的出院日期……\x01",
            "但是他一直恳求我。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x16,
        (
            "呵呵呵，不过，其实我很高兴。\x01",
            "因为，我最喜欢他工作时的\x01",
            "模样了⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6572")

    Jump("loc_6934")

    label("loc_6577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_669C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6644")

    #C0265
    ChrTalk(
        0x16,
        (
            "我来探病时带来的书\x01",
            "已经读完了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x16,
        (
            "读过一次的书再读就没意思了……\x01",
            "嗯，不如就当作礼物\x01",
            "送给你们吧¤\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0267
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2FA, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 4)
    Jump("loc_6697")

    label("loc_6644")


    #C0268
    ChrTalk(
        0x16,
        (
            "之前守在医院的那些国防军士兵\x01",
            "已经全部离开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x16,
        "……是不是发生什么事了啊？\x02",
    )

    CloseMessageWindow()

    label("loc_6697")

    Jump("loc_6934")

    label("loc_669C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6819")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6780")

    #C0270
    ChrTalk(
        0x16,
        (
            "独立宣言发表的时候，\x01",
            "我刚好来医院探望他，\x01",
            "结果就一直待在这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x16,
        (
            "因为现在出入市内\x01",
            "必须要办理非常麻烦的手续。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x16,
        (
            "而且能和他悠闲共处的时候可不多，\x01",
            "既然有这种好机会，\x01",
            "不好好享受一下可就亏了¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6814")

    label("loc_6780")


    #C0273
    ChrTalk(
        0x16,
        (
            "独立宣言发表的时候，\x01",
            "我刚好来医院探望他，\x01",
            "结果就一直待在这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x16,
        (
            "能和他悠闲共处的时候\x01",
            "可不多，既然有这种好机会，\x01",
            "不好好享受一下可就亏了¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6814")

    Jump("loc_6934")

    label("loc_6819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_68C5")

    #C0275
    ChrTalk(
        0x16,
        (
            "呵呵，你可真是的，早就不是年轻的\x01",
            "小伙子了，却还是这么冲动……\x01",
            "都让芙兰小姐为你担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x16,
        (
            "不过，能保护芙兰小姐这么\x01",
            "可爱的女孩子，\x01",
            "也算是最棒的演出了¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6934")

    label("loc_68C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6934")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68E0")
    Call(0, 21)
    Jump("loc_6934")

    label("loc_68E0")


    #C0277
    ChrTalk(
        0x16,
        (
            "我也知道目前的形势\x01",
            "很严峻……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x16,
        (
            "但我不希望他再次逞强，\x01",
            "所以必须看好他才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6934")

    TalkEnd(0xFE)
    Return()

    # Function_35_64D0 end

    def Function_36_6938(): pass

    label("Function_36_6938")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6949")
    Jump("loc_6F5A")

    label("loc_6949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6957")
    Jump("loc_6F5A")

    label("loc_6957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AB3")

    #C0279
    ChrTalk(
        0x17,
        (
            "成为独立国，并且与外界断绝之后，\x01",
            "最大的麻烦就是今后无法\x01",
            "与雷米菲利亚合作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x17,
        (
            "虽然总统那边似乎\x01",
            "储备了大量的\x01",
            "基本医疗物资……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x17,
        (
            "但药品这种东西，\x01",
            "必须要结合患者的症状和体质，\x01",
            "并经过严密的选择才能开处方。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x17,
        (
            "光凭总统准备的那些药品，\x01",
            "恐怕很难顾及到\x01",
            "全部的患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x17,
        (
            "今后究竟该怎么办才好呢……\x01",
            "得想个办法才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_6B1E")

    label("loc_6AB3")


    #C0284
    ChrTalk(
        0x17,
        (
            "光凭总统准备的那些药品，\x01",
            "恐怕很难顾及到\x01",
            "全部的患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x17,
        (
            "今后究竟该怎么办才好呢……\x01",
            "得想个办法才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B1E")

    Jump("loc_6F5A")

    label("loc_6B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6F5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DF2")

    #C0286
    ChrTalk(
        0x17,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#00005F赛兰德医生……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x17, 0x0, 500)

    #C0288
    ChrTalk(
        0x17,
        "……是你们啊，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x103,
        (
            "#00200F这里是小滴当时的病房吧，\x01",
            "您在这里做什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x17,
        (
            "那个孩子当时是由我负责主治的患者。\x01",
            "来到这里，一时有些触景生情。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x17,
        (
            "……不知她被亚里欧斯·马克莱因\x01",
            "带出医院之后怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x105,
        (
            "#10401F说起来，自那之后\x01",
            "就一直没见过她了。\x02\x03",

            "#10403F现在多半已经被安置在\x01",
            "兰花塔的某处了。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x17,
        (
            "……虽说亚里欧斯是滴的父亲，\x01",
            "但对我而言，自己的患者被抢走，\x01",
            "仍然是莫大的耻辱。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x17,
        (
            "他那时已经赴任为国防长官，\x01",
            "我也明白接走滴是\x01",
            "无可奈何的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x17,
        (
            "虽然明白……\x01",
            "但还是无法接受。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        "#00001F医生……\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x17,
        (
            "……抱歉，\x01",
            "我说了些没用的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x17,
        (
            "你们是来看望患者的吧？\x01",
            "……抱歉，能让我独处一会吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 6)
    ClearChrFlags(0x17, 0x10)
    Jump("loc_6F5A")

    label("loc_6DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6ED1")

    #C0299
    ChrTalk(
        0x17,
        (
            "滴·马克莱因……\x01",
            "为那女孩严密规划的治疗方针\x01",
            "已经排到了一年后。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x17,
        (
            "……虽说那是她的父亲，\x01",
            "但对我而言，自己的患者被抢走，\x01",
            "仍然是莫大的耻辱。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x17,
        (
            "可是，一直纠结于已出院的患者，\x01",
            "也只是在浪费时间而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_6F5A")

    label("loc_6ED1")


    #C0302
    ChrTalk(
        0x17,
        (
            "……虽说那是她的父亲，\x01",
            "但对我而言，自己的患者被抢走，\x01",
            "仍然是莫大的耻辱。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x17,
        (
            "可是，一直纠结于已出院的患者，\x01",
            "也只是在浪费时间而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F5A")

    TalkEnd(0xFE)
    Return()

    # Function_36_6938 end

    def Function_37_6F5E(): pass

    label("Function_37_6F5E")

    Sound(160, 0, 100, 0)
    Return()

    # Function_37_6F5E end

    def Function_38_6F65(): pass

    label("Function_38_6F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7130")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13500, 600, 30340, 0)
    MoveCamera(43, 29, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20580, 0)
    SetChrPos(0x106, -12930, 0, 29900, 270)
    SetChrPos(0x101, -15140, 0, 29900, 90)
    SetChrPos(0x102, -15140, 0, 31030, 90)
    SetChrPos(0x103, -15140, 0, 28800, 90)
    SetChrPos(0x104, -16360, 0, 30550, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_701A")
    SetChrPos(0x109, -16360, 0, 29320, 90)

    label("loc_701A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_703B")
    SetChrPos(0x105, -16360, 0, 29320, 90)

    label("loc_703B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_705C")
    SetChrPos(0x10A, -16360, 0, 29320, 90)

    label("loc_705C")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0304
    ChrTalk(
        0x106,
        (
            "#10703F（……各位，如果你们\x01",
            "  要进去，那我就待在这里了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        "#00000F（……我明白了。）\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        "#00300F（好吧，就表现得像平时一样。）\x02",
    )

    CloseMessageWindow()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -16360, 0, 29440, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    SetScenarioFlags(0x1CE, 3)
    Jump("loc_7194")

    label("loc_7130")

    TalkBegin(0xFF)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-100110, 1050, -1300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x5, 0xFF)
    SetScenarioFlags(0x2, 3)
    SetChrPos(0x0, -100110, 50, -1300, 180)
    FadeToBright(500, 0)
    TalkEnd(0xFF)

    label("loc_7194")

    Return()

    # Function_38_6F65 end

    def Function_39_7195(): pass

    label("Function_39_7195")

    TalkBegin(0xFF)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-16500, 1000, 27500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    AddParty(0x5, 0xFF, 0xFF)
    SetChrChipPat(0x5, 0x1, 0x20)
    ClearScenarioFlags(0x2, 3)
    SetChrPos(0x0, -16500, 0, 27500, 0)
    FadeToBright(500, 0)
    TalkEnd(0xFF)
    Return()

    # Function_39_7195 end

    def Function_40_71FD(): pass

    label("Function_40_71FD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(2723)
    AddParty(0x35, 0xFF, 0xFF)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11700.itp")
    SetChrPos(0x101, -1400, 0, -50500, 90)
    SetChrPos(0x102, -1400, 0, -49500, 90)
    SetChrPos(0x103, -2500, 0, -50500, 90)
    SetChrPos(0x104, -2500, 0, -49500, 90)
    SetChrPos(0x109, -3600, 0, -50500, 90)
    SetChrPos(0x105, -3600, 0, -49500, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 6300, 600, -47500, 270)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x136, 6000, 0, -49000, 0)
    OP_68(6080, 2500, -47450, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    OP_68(6080, 1000, -47450, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(808, 0, 80, 0)
    Sleep(300)

    #C0307
    ChrTalk(
        0x101,
        "#2P#2S打扰了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_68(5670, 1000, -47970, 2500)

    def lambda_73CD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73CD)
    Sleep(200)

    def lambda_73E5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_73E5)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    def lambda_7401():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7401)

    def lambda_7416():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_7416)
    Sleep(50)

    def lambda_7426():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7426)
    Sleep(50)

    def lambda_743E():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_743E)
    Sleep(50)

    def lambda_7456():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7456)

    def lambda_746B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_746B)
    Sleep(200)

    def lambda_747F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_747F)
    Sleep(500)

    def lambda_7493():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7493)

    def lambda_74A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_74A4)
    Sleep(500)

    def lambda_74B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_74B8)

    def lambda_74C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_74C9)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_C9(0x0, 0x80000000)

    #C0308
    ChrTalk(
        0x8,
        (
            "#11705F#2723V#5P#40W啊……\x01",
            "姐姐，还有各位……！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAA3)
    OP_C9(0x1, 0x80000000)

    #C0309
    ChrTalk(
        0x136,
        "#01302F#11P哎呀，大家好。\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        "#00000F#6P塞茜尔姐姐，你也在这里啊。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x109,
        (
            "#10113F#6P#N打扰了，\x01",
            "请问现在可以探视吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0312
    ChrTalk(
        0x136,
        (
            "#01309F#11P呵呵，没问题，\x01",
            "我只是在换点滴瓶而已。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(5920, 1000, -48010, 2000)

    def lambda_75EF():
        OP_9B(0x1, 0xFE, 0xE1, 0x6D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_75EF)
    Sleep(350)
    BeginChrThread(0x101, 1, 0, 41)
    Sleep(100)
    BeginChrThread(0x102, 1, 0, 42)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 44)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 43)
    Sleep(150)
    BeginChrThread(0x105, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 46)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x238), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0313
    AnonymousTalk(
        0x8,
        (
            "#30W嘿嘿……\x01",
            "谢谢大家～\x02\x03",

            "你们是特地来\x01",
            "看望我的吗～？\x02",
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

    #C0314
    ChrTalk(
        0x101,
        (
            "#00002F#12P是啊，听诺艾尔说，\x01",
            "你已经醒过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#00109F#12P呵呵，看来比我想象中\x01",
            "还要有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#10302F#6P是啊，\x01",
            "脸色也很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x8,
        (
            "#11704F#5P#30W嘿嘿，我现在精力十足，\x01",
            "已经没问题了～\x02\x03",

            "#11700F两三天之内，\x01",
            "应该就会移住到普通病房了……\x02\x03",

            "#11709F然后过不了多久\x01",
            "就能出院了～\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        (
            "#10106F#12P那可不行哦，芙兰。\x02\x03",

            "#10101F毕竟你元气大伤，\x01",
            "暂时还得静养一段时间才行……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "#11704F#5P#30W嘿嘿……\x01",
            "我的伤势根本不算什么～\x02\x03",

            "#11708F舍身保护我的\x01",
            "多诺邦警督才……\x02\x03",

            "#11706F#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        "#00208F#6P芙兰小姐……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#00306F#6P……小芙兰，\x01",
            "你并不需要想太多。\x02\x03",

            "#00301F发生了这种事情……\x01",
            "责任全都在『赤色星座』的那帮猎兵。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        (
            "#11712F#5P#30W嘿嘿……我知道了。\x02\x03",

            "#11711F但我毕竟还要为大家\x01",
            "提供后援工作……\x02\x03",

            "#11706F所以必须要努力调养，尽早康复……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00004F#12P没事的，你就放心吧。\x02\x03",

            "#00000F虽然听不到芙兰的声音有些寂寞，\x01",
            "但处理报告那方面的工作没什么问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        (
            "#00104F#12P你现在就安心修养，\x01",
            "争取早日恢复精神吧。\x02\x03",

            "#00102F等到那时，我们就可以\x01",
            "毫不客气地继续依靠你的支援了。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "#11704F#5P#30W……好的，\x01",
            "谢谢大家～\x02\x03",

            "#11705F对了……\x01",
            "姐姐，听说你要回\x01",
            "警备队了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x109,
        (
            "#10100F#12P是妈妈告诉你的吧？\x01",
            "……嗯，其实我也考虑了很久。\x02\x03",

            "#10112F一想到今后无法再得到\x01",
            "芙兰的后方支援，\x01",
            "我也觉得稍有寂寞呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "#11701F#5P#40W哼……居然只是稍有寂寞，\x01",
            "实在太薄情了……\x02\x03",

            "#11706F#50W……姐姐你……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7C2D():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7C2D)
    WaitChrThread(0x8, 2)
    Sleep(500)
    SetChrSubChip(0x8, 0x2)
    Fade(250)
    OP_0D()
    Sleep(300)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0328
    ChrTalk(
        0x109,
        "#10111F#12P芙兰……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x136, 0x13B, 0x1F4)
    Sleep(150)

    #C0329
    ChrTalk(
        0x136,
        (
            "#01304F#11P没事的，只是点滴的药力\x01",
            "开始发挥作用了。\x02\x03",

            "#01302F聊天就到此结束，\x01",
            "你好好睡一觉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "#11706F#11P#40W我没事的……\x01",
            "难得罗伊德警官\x01",
            "和大家都来看我……\x02\x03",

            "#11701F而且……我要在姐姐回警备队之前，\x01",
            "教给她必胜之法……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x109,
        (
            "#10106F#12P唉，胡说些什么呢。\x02\x03",

            "#10108F……各位，不好意思，\x01",
            "可以让她睡一会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        (
            "#00002F#12P当然。\x01",
            "……芙兰，我们还会再来看你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        (
            "#00204F#6P先安心休息一下吧。\x02\x03",

            "#00202F等你恢复精神之后，\x01",
            "我们会带蛋糕来看你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "#11712F#11P#40W哈哈……\x01",
            "嗯，我很期待……\x02\x03",

            "#11704F#50W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(800)
    OP_68(6270, 1000, -47800, 800)
    SetCameraDistance(21380, 800)
    Sound(898, 0, 100, 0)
    SetChrPos(0x8, 6100, 400, -47500, 270)
    SetChrSubChip(0x8, 0x3)
    OP_0D()
    Sleep(300)
    OP_6F(0x79)
    OP_63(0x8, 0x12C, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    #C0335
    ChrTalk(
        0x105,
        (
            "#10308F#6P……体力果然还是\x01",
            "很差啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x136,
        (
            "#01303F#11P是啊，毕竟在手术时\x01",
            "输了大量的血……\x02\x03",

            "#01300F但接下来就会渐渐恢复了。\x02\x03",

            "#01309F不用担心，她很快就能重振精神的。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x109,
        "#10106F#12P嗯……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        "#00003F#11P……那我们出去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x8)
    OP_68(4990, 1000, 7500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23300, 0)
    SetChrPos(0x101, 3250, 0, 7700, 90)
    SetChrPos(0x102, 3250, 0, 6300, 90)
    SetChrPos(0x104, 3750, 0, 8800, 135)
    SetChrPos(0x103, 3750, 0, 5500, 45)
    SetChrPos(0x109, 2100, 0, 7900, 90)
    SetChrPos(0x105, 2100, 0, 6100, 90)
    SetChrPos(0x136, 7200, 0, 7500, 270)
    OP_A7(0x136, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    SetCameraDistance(22800, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(700)
    Sound(107, 0, 100, 0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    Sleep(1300)

    def lambda_8169():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_8169)
    Sleep(50)

    def lambda_8181():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_8181)
    WaitChrThread(0x136, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x1, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)

    #C0339
    ChrTalk(
        0x101,
        (
            "#00005F#6P对了……\x02\x03",

            "#00001F多诺邦警督和伊莉娅小姐\x01",
            "还是谢绝探望吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x136,
        (
            "#01306F#11P……原则上是的。\x02\x03",

            "#01308F但你们毕竟也算是\x01",
            "他们的关系人……\x02\x03",

            "#01300F如果由我陪同，\x01",
            "倒也可以去看看他们的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x102,
        "#00105F#6P可、可以吗？\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#00203F#12P真是太感谢了。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        "#00301F#5P塞茜尔小姐，麻烦你了。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x136,
        (
            "#01304F#11P呵呵……\x01",
            "那我们这就走吧。\x02\x03",

            "#01300F旁边的３０２号房就是\x01",
            "多诺邦警督的病房。\x02\x03",

            "伊莉娅则在３０３号病房……\x01",
            "也就是小滴房间的对面。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        "#00001F#6P明白了，我们走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_74(0x1, 0x1E)
    SetChrPos(0x0, 4500, 0, 7500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x180, 7)
    OP_29(0xAC, 0x1, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    OP_1B(0x0, 0x0, 0x59)
    OP_1B(0x1, 0x0, 0x5A)
    ModifyEventFlags(1, 2, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_40_71FD end

    def Function_41_83DC(): pass

    label("Function_41_83DC")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_41_83DC end

    def Function_42_8411(): pass

    label("Function_42_8411")

    OP_9B(0x0, 0xFE, 0x0, 0x6D6, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xFA, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_42_8411 end

    def Function_43_8437(): pass

    label("Function_43_8437")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_43_8437 end

    def Function_44_8463(): pass

    label("Function_44_8463")

    OP_9B(0x0, 0xFE, 0x14A, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x79E, 0x7D0, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_44_8463 end

    def Function_45_8489(): pass

    label("Function_45_8489")

    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_45_8489 end

    def Function_46_84BE(): pass

    label("Function_46_84BE")

    OP_9B(0x0, 0xFE, 0x4, 0x2EE, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_46_84BE end

    def Function_47_84E4(): pass

    label("Function_47_84E4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-50500, 1000, -50000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_68(-54200, 1000, -46530, 0)
    MoveCamera(39, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetCameraDistance(23500, 2000)
    SetChrPos(0x136, -50000, 50, -50000, 270)
    SetChrPos(0x101, -48900, 50, -49660, 270)
    SetChrPos(0x102, -48900, 50, -50640, 270)
    SetChrPos(0x103, -47900, 50, -50640, 270)
    SetChrPos(0x104, -47900, 50, -49660, 270)
    SetChrPos(0x109, -46900, 50, -49660, 270)
    SetChrPos(0x105, -46900, 50, -50640, 270)
    OP_A7(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(808, 0, 80, 0)
    Sleep(300)

    #N0346
    NpcTalk(
        0x136,
        "塞茜尔的声音",
        (
            "#2S#5P雷蒙德警官，您在吗？\x01",
            "我们进去了哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    SetChrSubChip(0xA, 0x2)
    Sleep(200)
    Sound(107, 0, 100, 0)
    OP_74(0x4, 0xF)
    OP_71(0x4, 0x0, 0x14, 0x0, 0x0)
    Sleep(700)
    OP_68(-53710, 1000, -47510, 3000)
    SetCameraDistance(24000, 3000)

    def lambda_86D4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_86D4)

    def lambda_86E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_86E9)
    Sleep(100)
    Sleep(100)

    def lambda_8700():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8700)

    def lambda_8711():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8711)
    Sleep(100)

    def lambda_8729():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8729)
    Sleep(100)

    def lambda_8741():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8741)

    def lambda_8752():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8752)
    Sleep(100)

    def lambda_876A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_876A)

    def lambda_877B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_877B)
    Sleep(100)

    def lambda_8793():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8793)

    def lambda_87A4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_87A4)
    Sleep(100)

    def lambda_87BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_87BC)

    def lambda_87CD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_87CD)
    Sleep(100)

    def lambda_87E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_87E5)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x4, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)

    #C0347
    ChrTalk(
        0xA,
        (
            "#6P塞茜尔小姐……\x01",
            "还有支援科的诸位……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#00003F#11P雷蒙德警官……\x01",
            "真是辛苦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#00108F#11P您在这里看护警督吗？\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xA,
        (
            "#6P哈哈……只是刚好接替\x01",
            "警督的妻子一会而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xA,
        (
            "#6P如果警督醒过来了，\x01",
            "肯定会大骂我一顿\x01",
            "『你又在偷懒了！』之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x104,
        "#00308F#11P是吗……\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x103,
        (
            "#00203F#11P……他确实有可能\x01",
            "那样说呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x105,
        (
            "#10301F#11P那个设备……\x01",
            "难道是人工呼吸器？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0355
    ChrTalk(
        0xA,
        (
            "#11P是的……因为他的呼吸系统\x01",
            "受到了严重的损伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xA,
        (
            "#11P如果能想办法让他醒过来，\x01",
            "应该就可以恢复得快一点了……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xA,
        "#11P#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    Sleep(300)

    #C0358
    ChrTalk(
        0xA,
        (
            "#11P警督他……\x01",
            "在爆炸的时候，舍身保护了\x01",
            "我和芙兰。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xA,
        (
            "#11P保护了我这个在关键时刻\x01",
            "被吓得手足无措，\x01",
            "什么忙都帮不上的废物……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xA,
        (
            "#11P而且，芙兰受了重伤，\x01",
            "需要接受手术，\x01",
            "我却只有一点擦伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xA,
        (
            "#11P……真为自己的好运气和\x01",
            "厚颜无耻感到羞愧啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        "#00008F#11P雷蒙德警官……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x104,
        "#00306F#11P……那并不是你的错啊。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x136,
        (
            "#01303F#11P……雷蒙德警官，\x01",
            "要不要休息一下呢？\x02\x03",

            "#01301F他现在的情况很稳定，\x01",
            "我们也会随时巡视的。\x02\x03",

            "你如果不休息一下，可能会撑不住哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    #C0365
    ChrTalk(
        0xA,
        "#6P哈哈……谢谢关心。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xA,
        (
            "#6P不过，再过一会，\x01",
            "警督的妻子就会回来了，\x01",
            "在那之前，就由我……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x136,
        "#01306F#11P嗯……我明白了。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x102,
        "#00103F#11P……请保重身体啊。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x103,
        "#00202F#11P我们会再来看望的。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xA,
        (
            "#6P嗯……\x01",
            "警督一定也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrSubChip(0xA, 0x0)
    Sleep(500)
    SetCameraDistance(24250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_74(0x4, 0x1E)
    SetChrPos(0x0, -53500, 0, -50000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 0)
    OP_29(0xAC, 0x1, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x0, 0x0, 0x59)
    OP_1B(0x1, 0x0, 0x5A)
    ModifyEventFlags(1, 2, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_47_84E4 end

    def Function_48_8D83(): pass

    label("Function_48_8D83")

    Sleep(600)
    Sound(107, 0, 100, 0)
    Return()

    # Function_48_8D83 end

    def Function_49_8D8D(): pass

    label("Function_49_8D8D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-96210, 1600, -4360, 0)
    MoveCamera(55, 15, 0, 0)
    MoveCamera(55, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22330, 0)
    LoadChrToIndex("apl/ch51521.itc", 0x1E)
    SetChrPos(0x136, -100000, 50, -150, 180)
    SetChrPos(0x102, -100660, 50, 1100, 180)
    SetChrPos(0x101, -99640, 50, 1100, 180)
    SetChrPos(0x103, -100660, 50, 2200, 180)
    SetChrPos(0x104, -99640, 50, 2200, 180)
    SetChrPos(0x109, -100660, 50, 3300, 180)
    SetChrPos(0x105, -99640, 50, 3300, 180)
    OP_A7(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-96210, 800, -4360, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(808, 0, 80, 0)
    Sleep(300)

    #N0371
    NpcTalk(
        0x136,
        "塞茜尔的声音",
        (
            "#2S#11P修利小姐，\x01",
            "现在方便吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xC,
        "#04208F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x0, 0x14, 0x0, 0x0)
    Sleep(700)
    OP_68(-97700, 1000, -3750, 3000)

    def lambda_8F66():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_8F66)
    Sleep(50)

    def lambda_8F7E():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F7E)

    def lambda_8F93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x136, 2, lambda_8F93)
    Sleep(50)

    def lambda_8FA7():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8FA7)
    Sleep(50)

    def lambda_8FBF():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8FBF)
    Sleep(50)

    def lambda_8FD7():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8FD7)
    Sleep(50)

    def lambda_8FEF():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8FEF)
    Sleep(50)

    def lambda_9007():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9007)
    Sleep(50)
    Sleep(100)

    def lambda_9022():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9022)

    def lambda_9033():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9033)
    Sleep(400)

    def lambda_9047():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9047)

    def lambda_9058():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9058)
    Sleep(400)

    def lambda_906C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_906C)

    def lambda_907D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_907D)
    WaitChrThread(0x136, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x5, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_6F(0x79)

    #C0373
    ChrTalk(
        0x101,
        "#00008F#5P修利……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_9108")

    #C0374
    ChrTalk(
        0x102,
        "#00108F#5P……………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_9126")

    label("loc_9108")


    #C0375
    ChrTalk(
        0x102,
        "#00106F#5P你也来了啊……\x02",
    )

    CloseMessageWindow()

    label("loc_9126")

    OP_68(-97460, 1000, -5050, 2500)
    MoveCamera(50, 20, 0, 2500)
    OP_6E(400, 2500)
    SetCameraDistance(20500, 2500)
    OP_93(0x136, 0x87, 0x1F4)
    BeginChrThread(0x136, 1, 0, 52)
    Sleep(200)
    BeginChrThread(0x101, 1, 0, 53)
    Sleep(100)
    BeginChrThread(0x102, 1, 0, 54)
    Sleep(100)
    BeginChrThread(0x103, 1, 0, 55)
    Sleep(100)
    BeginChrThread(0x104, 1, 0, 56)
    Sleep(100)
    BeginChrThread(0x105, 1, 0, 57)
    Sleep(100)
    BeginChrThread(0x109, 1, 0, 58)
    OP_6F(0x79)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)

    #C0376
    ChrTalk(
        0xB,
        "#11P#5P#60W……………………………\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        "#00208F#6P#N伊莉娅小姐……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0378
    ChrTalk(
        0x104,
        "#00301F#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xC)
    Sleep(500)

    #C0379
    ChrTalk(
        0xC,
        (
            "#04206F#6P#30W这张睡脸……是不是既安静又漂亮？\x02\x03",

            "#04208F平时总是睡得死死的，\x01",
            "睡相也差得要命，\x01",
            "在这种时候却偏偏……\x02\x03",

            "#04202F哈哈……\x01",
            "这真是太不像\x01",
            "伊莉娅·普拉提耶的风格了……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x109,
        "#10108F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x105,
        "#10301F#5P……她的身体状况如何？\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x136,
        (
            "#01303F#5P……全身骨折，\x01",
            "外加内脏受损。\x02\x03",

            "#01308F手术虽然成功了，\x01",
            "但还是昏迷不醒……\x02\x03",

            "#01301F目前仍然不得不\x01",
            "依靠生命维持装置……\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#00006F#5P……居然这么严重………\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x104,
        "#00306F#5P……可恶……！\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x102,
        "#00108F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0386
    ChrTalk(
        0xC,
        (
            "#04202F#6P#30W据说……哪怕能苏醒过来，\x01",
            "也不可能再度复出了……\x02\x03",

            "你们能相信吗？\x01",
            "伊莉娅小姐竟然再也\x01",
            "无法站上舞台了……？\x02\x03",

            "#04208F而且这仅仅是为了……\x01",
            "为了保护我这样的人……\x02\x03",

            "#04206F#40W……怎么会……\x01",
            "怎么会有这种事……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9509():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_9509)
    Sleep(800)
    TurnDirection(0x101, 0xC, 500)
    Sleep(150)

    #C0387
    ChrTalk(
        0x101,
        "#00001F#5P……修利………\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x136,
        "#01303F#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x136, 0xB4, 0x190)
    Sleep(300)
    SetCameraDistance(19500, 1500)
    BeginChrThread(0x136, 1, 0, 50)
    WaitChrThread(0x136, 1)
    SetChrFlags(0x136, 0x2)
    SetChrChipByIndex(0x136, 0x1E)
    SetChrSubChip(0x136, 0x0)
    Sound(898, 0, 100, 0)
    OP_6F(0x79)

    #C0389
    ChrTalk(
        0xC,
        "#04205F#6P#40W………哎……………\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x136,
        (
            "#01304F#5P放心吧……一定会没事的。\x02\x03",

            "我最了解\x01",
            "伊莉娅这个人了。\x02\x03",

            "#01308F无论处于怎样的逆境之中，她也绝\x01",
            "不会放弃，只会不断追求更高的目标……\x02\x03",

            "#01302F这就是伊莉娅·普拉提耶。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xC,
        "#04212F#6P#40W……可、可是……\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        (
            "#00004F#5P我也这样想。\x02\x03",

            "#00002F如果不是那样的人，\x01",
            "根本就不可能创作出\x01",
            "那种超乎想象的舞剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x102,
        (
            "#00104F#6P#N是啊……\x02\x03",

            "#00102F正是因为伊莉娅小姐有着强烈的执念，\x01",
            "才能完成那种前所未有的表演。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0394
    ChrTalk(
        0x103,
        (
            "#00204F#6P#N只要舞台还在……\x01",
            "伊莉娅小姐就一定会回来。\x02\x03",

            "#00202F虽然很不可思议，但就是让人有这种想法。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0395
    ChrTalk(
        0xC,
        "#04205F#6P#30W………啊……………\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x104,
        (
            "#00304F#5P是啊……\x02\x03",

            "#00300F现在一定要相信女神和伊莉娅小姐，\x01",
            "然后尽最大努力做好自己能做的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x105,
        (
            "#10304F#5P今天就算了，但以后可不要\x01",
            "再缺席表演练习哦。\x02\x03",

            "#10302F如果你努力训练，\x01",
            "说不定能把她给唤醒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x109,
        (
            "#10112F#6P嗯……没错！\x02\x03",

            "#10102F感应到精彩的舞台表演之后，\x01",
            "伊莉娅小姐一定会醒过来的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xC,
        "#04212F#6P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(19750, 800)
    ClearChrFlags(0x136, 0x2)
    SetChrChipByIndex(0x136, 0xA)
    SetChrSubChip(0x136, 0x0)
    Sound(812, 0, 100, 0)
    BeginChrThread(0x136, 1, 0, 51)
    WaitChrThread(0x136, 1)
    OP_6F(0x79)
    Sleep(300)

    #C0400
    ChrTalk(
        0xC,
        (
            "#04204F#6P………谢谢，\x01",
            "我稍微打起一点精神了。\x02\x03",

            "#04208F说的没错……\x01",
            "我们必须要鼓起干劲才行……\x02\x03",

            "何况……莉夏姐也不知\x01",
            "跑到哪里去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#00108F#6P#N啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0402
    ChrTalk(
        0x101,
        "#00008F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x1)
    Sleep(300)

    #C0403
    ChrTalk(
        0xC,
        (
            "#04206F#6P那个……\x02\x03",

            "如果可以，你们能帮我找找\x01",
            "莉夏姐吗……？\x02\x03",

            "#04208F不管有什么样的隐情，\x01",
            "莉夏姐也永远是莉夏姐……\x02\x03",

            "#04201F而且我总觉得，只要莉夏姐能回来，\x01",
            "伊莉娅小姐就一定会恢复精神的。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#00003F#5P我知道了。\x02\x03",

            "#00000F赌上特别任务支援科的名誉，\x01",
            "我们一定会把她找出来的。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(1016, 1000, 100)
    SetCameraDistance(20250, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    OP_68(-16329, 3200, 29420, 0)
    MoveCamera(43, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17760, 0)
    SetChrPos(0x101, -17100, 0, 29000, 180)
    SetChrPos(0x102, -15900, 0, 29000, 180)
    SetChrPos(0x103, -17600, 0, 29700, 180)
    SetChrPos(0x104, -15400, 0, 30300, 180)
    SetChrPos(0x109, -17200, 0, 31200, 180)
    SetChrPos(0x105, -15800, 0, 31200, 180)
    SetChrPos(0x136, -16500, 0, 27500, 0)
    OP_68(-16329, 1200, 29420, 3000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0405
    ChrTalk(
        0x136,
        (
            "#01302F#12P……真是谢谢大家了。\x02\x03",

            "这样一来，修利应该就能\x01",
            "重新打起精神了吧。\x02\x03",

            "#01304F连我也……\x01",
            "产生了一些勇气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x101,
        "#00008F#5P塞茜尔姐姐……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x102,
        (
            "#00106F#5P伊莉娅小姐的身体状况\x01",
            "还是十分严峻吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x136,
        (
            "#01306F#12P是的……\x01",
            "说实话，现在还不能安心。\x02\x03",

            "#01308F……但尽管如此，\x01",
            "我还是坚信伊莉娅会没事的。\x02\x03",

            "#01302F而且我觉得，相信她的人越多，\x01",
            "她就越会报以强烈的回应。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x104,
        "#00302F#5P说的没错……\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x103,
        (
            "#00204F#5P确实，那正是\x01",
            "伊莉娅小姐的作风。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x105,
        (
            "#10303F#5P这样一来……\x01",
            "关键问题就是莉夏了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E38():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9E38)
    WaitChrThread(0x105, 2)
    Sleep(150)

    #C0412
    ChrTalk(
        0x105,
        "#10300F#5P罗伊德，你能找到她吗？\x02",
    )

    CloseMessageWindow()

    def lambda_9E72():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E72)
    Sleep(150)

    def lambda_9E82():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E82)
    Sleep(50)

    def lambda_9E92():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9E92)
    Sleep(50)

    def lambda_9EA2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9EA2)
    Sleep(50)

    def lambda_9EB2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9EB2)
    Sleep(50)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)

    #C0413
    ChrTalk(
        0x101,
        (
            "#00003F#6P……老实说，我也不知道。\x02\x03",

            "#00008F如果她真想隐藏起来，\x01",
            "我们恐怕很难找到她。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x109,
        (
            "#10106F#5P是啊……\x02\x03",

            "#10108F目前行踪不明的『黑月』也是一样，\x01",
            "连他们是否还留在\x01",
            "自治州内都无法判断……\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        (
            "#00303F#11P说不定他们已经回到\x01",
            "卡尔瓦德共和国了……\x02\x03",

            "#00300F但阿修都那样拜托我们了，\x01",
            "我们总不能就此\x01",
            "放弃吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        "#00000F#6P嗯，当然不能。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x102,
        (
            "#00100F#11P连同『黑月』的行踪，\x01",
            "我们用心留意一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x103,
        (
            "#00202F#6P我也会时常在导力网络上\x01",
            "调查的。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x136,
        (
            "#01304F#12P呵呵，真是谢谢你们了。\x02\x03",

            "#01300F我这就要回护士中心了，\x01",
            "罗伊德，你们有什么打算？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A0F0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A0F0)
    Sleep(150)

    def lambda_A100():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A100)
    Sleep(50)

    def lambda_A110():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A110)
    Sleep(50)

    def lambda_A120():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A120)
    Sleep(50)

    def lambda_A130():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A130)
    Sleep(50)

    def lambda_A140():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A140)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    #C0420
    ChrTalk(
        0x101,
        (
            "#00002F#5P哦，我们也还有其它工作，\x01",
            "差不多就该告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        (
            "#00104F#5P谢谢你给我们\x01",
            "带路。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x136,
        (
            "#01309F#12P呵呵，我才要谢谢你们呢。\x02\x03",

            "#01302F虽然现在的状况很艰难……\x01",
            "但我们都好好加油吧。\x02\x03",

            "不过，不要太勉强自己哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        "#00309F#5P明白啦。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x103,
        "#00204F#5P您辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_68(-14130, 1200, 29280, 3000)
    BeginChrThread(0x136, 1, 0, 59)
    Sleep(400)

    def lambda_A288():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A288)
    Sleep(350)

    def lambda_A298():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A298)
    Sleep(150)

    def lambda_A2A8():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A2A8)
    Sleep(250)

    def lambda_A2B8():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A2B8)
    Sleep(150)

    def lambda_A2C8():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A2C8)
    Sleep(150)

    def lambda_A2D8():
        TurnDirection(0xFE, 0x136, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A2D8)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_68(-16329, 1200, 29420, 1300)
    MoveCamera(43, 22, 0, 1300)
    OP_6E(440, 1300)
    SetCameraDistance(17760, 1300)

    def lambda_A397():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A397)
    Sleep(150)

    def lambda_A3A7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A3A7)
    Sleep(50)

    def lambda_A3B7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A3B7)
    Sleep(50)

    def lambda_A3C7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A3C7)
    Sleep(50)

    def lambda_A3D7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A3D7)
    Sleep(50)

    def lambda_A3E7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A3E7)
    Sleep(50)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0425
    ChrTalk(
        0x101,
        (
            "#00006F#6P现在……\x01",
            "确实是必须要努力的时刻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x102,
        (
            "#00103F#11P嗯……是啊。\x02\x03",

            "#00108F这也是为了让那些身心都\x01",
            "受到伤害的人们能够重拾笑容。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x109,
        (
            "#10108F#5P…………………………\x01",
            "（必须要努力的时刻吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18260, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RemoveParty(0x35, 0xFF)
    OP_74(0x5, 0x1E)
    SetChrPos(0x0, -16500, 0, 29250, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 1)
    OP_29(0xAC, 0x1, 0x6)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_49_8D8D end

    def Function_50_A560(): pass

    label("Function_50_A560")

    OP_9B(0x0, 0xFE, 0x5, 0xFA, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x5, 0xC8, 0x1F4, 0x0)
    Return()

    # Function_50_A560 end

    def Function_51_A57F(): pass

    label("Function_51_A57F")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x1F4, 0x0)
    Return()

    # Function_51_A57F end

    def Function_52_A58F(): pass

    label("Function_52_A58F")

    OP_96(0x136, 0xFFFE7C08, 0x0, 0xFFFFED7C, 0x4B0, 0x0)
    Return()

    # Function_52_A58F end

    def Function_53_A5A4(): pass

    label("Function_53_A5A4")

    OP_95(0xFE, -97730, 0, -3800, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_53_A5A4 end

    def Function_54_A5C0(): pass

    label("Function_54_A5C0")

    OP_95(0xFE, -100440, 0, -7000, 1500, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_54_A5C0 end

    def Function_55_A5DC(): pass

    label("Function_55_A5DC")

    OP_95(0xFE, -101020, 0, -6010, 1500, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_A5DC end

    def Function_56_A5F8(): pass

    label("Function_56_A5F8")

    OP_95(0xFE, -98500, 0, -3400, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_56_A5F8 end

    def Function_57_A614(): pass

    label("Function_57_A614")

    OP_95(0xFE, -99600, 0, -3350, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_57_A614 end

    def Function_58_A630(): pass

    label("Function_58_A630")

    OP_95(0xFE, -100570, 0, -4650, 1500, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_58_A630 end

    def Function_59_A64C(): pass

    label("Function_59_A64C")

    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xBB8, 0x7D0, 0x1)
    Return()

    # Function_59_A64C end

    def Function_60_A698(): pass

    label("Function_60_A698")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11600.itp")
    OP_68(-100000, 1000, -3500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -100660, 50, 1100, 180)
    SetChrPos(0x103, -99640, 50, 1100, 180)
    SetChrPos(0x105, -100160, 50, 2200, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(808, 0, 80, 0)
    Sleep(300)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x2)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0428
    AnonymousTalk(
        0xB,
        (
            "#11P嗯……？\x02\x03",

            "是哪位？\x01",
            "请进来吧。\x02",
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
    Sound(107, 0, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x0, 0x14, 0x0, 0x0)
    Sleep(700)

    #C0429
    ChrTalk(
        0x103,
        "#00204F#6P……打扰了。\x02",
    )

    CloseMessageWindow()
    OP_68(-97660, 1000, -3500, 3000)
    MoveCamera(45, 19, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(22000, 3000)

    def lambda_A886():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A886)

    def lambda_A89B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A89B)
    Sleep(100)

    def lambda_A8AF():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8AF)

    def lambda_A8C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A8C4)
    Sleep(100)

    def lambda_A8D8():
        OP_9B(0x0, 0xFE, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A8D8)

    def lambda_A8ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A8ED)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x5, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_6F(0x79)

    #C0430
    ChrTalk(
        0xB,
        "#11602F#11P哎呀，小缇欧和……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0431
    ChrTalk(
        0xB,
        (
            "#11605F#11P咦咦咦，这不是警察弟弟嘛！？\x02\x03",

            "#11602F旁边那个孩子是叫……\x01",
            "瓦吉吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x105,
        "#10404F#5P是的，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        (
            "#00002F#5P伊莉娅小姐……\x01",
            "真是好久不见了。\x02\x03",

            "#00006F抱歉，我们跑来看望您，\x01",
            "却两手空空的……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xB,
        (
            "#11609F#11P哎呀，真是的！\x01",
            "这种小事有什么好在意的！\x02\x03",

            "#11602F快来快来，你们三个\x01",
            "都到我这边来。\x02\x03",

            "#11605F啊，对了，支持者们给我送来了不少零食，\x01",
            "你们可以随便吃哦。\x02\x03",

            "#11609F曲奇之类的东西\x01",
            "应该还没过期呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#00012F#5P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x103,
        "#00204F#5P那我们就打扰了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_78(0x6, 0x18)
    ClearMapObjFlags(0x6, 0x4)
    SetChrPos(0x18, -99500, 0, -5700, 0)
    SetChrPos(0x101, -99300, 200, -5700, 90)
    SetChrPos(0x103, -99500, 0, -6800, 45)
    SetChrPos(0x105, -100100, 0, -5100, 90)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    OP_68(-97700, 400, -3750, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    Sleep(500)
    SetCameraDistance(21000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0437
    ChrTalk(
        0xB,
        (
            "#11603F#11P是吗……\x01",
            "看来你们也经历了不少事情啊。\x02\x03",

            "#11601F其实我也听过不少传言，\x01",
            "据说整个克洛斯贝尔的\x01",
            "状况都相当糟糕。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        "#00003F#6P是的……\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x105,
        (
            "#10406F#6P如今的事态，确实也只能用\x01",
            "糟糕来形容了。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xB,
        (
            "#11606F#11P唔……双腿无法行动，\x01",
            "真是让人着急啊……\x02\x03",

            "#11608F我很想亲眼看看\x01",
            "彩虹剧团的现状。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W伊莉娅小姐，请问……\x02\x03",

            "#00008F您的身体状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xB,
        (
            "#11605F#11P哦。\x02\x03",

            "#11603F赛兰德医生说，\x01",
            "现阶段还无法确定我以后\x01",
            "能不能再次下地走动。\x02\x03",

            "#11600F不过，她也没有断言说\x01",
            "百分之百不可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x101,
        "#00006F#6P#40W……是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x105,
        "#10408F#6P#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xB,
        (
            "#11606F#11P哎呀，真是的，露出那么阴沉的表情，\x01",
            "害得我都要跟着沮丧了。\x02\x03",

            "#11601F记住哦，如果总是自己对自己说不行、没希望，\x01",
            "最后可就真的连一点希望都没有了。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        "#00005F#6P#30W哎……\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xB,
        (
            "#11604F#11P舞台表演也是一样……\x01",
            "我们所寻求的『答案』一定就隐藏在某个地方。\x02\x03",

            "#11600F无论多么艰辛，多么绝望，\x01",
            "也一定存在着一线光明。\x02\x03",

            "#11609F只要不放弃，就一定能抓住它。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x101,
        "#00005F#6P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x103,
        "#00204F#12P呵呵……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x105,
        "#10402F#6P……您真了不起。\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xB,
        (
            "#11606F#11P唔，倒也谈不上\x01",
            "了不起吧。\x02\x03",

            "#11601F而且据我所知，\x01",
            "你们现在也十分辛苦吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0452
    ChrTalk(
        0x101,
        "#00011F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x103,
        (
            "#00206F#12P……以常理来推测，\x01",
            "我们所走的确实是一条万分艰险的道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xB,
        (
            "#11604F#11P所以说，我们都是一样的。\x02\x03",

            "#11600F人这种生物，为了自己重要的东西，\x01",
            "可是会不惜一切努力的。\x02\x03",

            "只是程度有高有低罢了……\x01",
            "我认为这就是人类的强大之处。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x101,
        "#00002F#6P人类的强大之处……\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x105,
        "#10404F#6P……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xB,
        (
            "#11602F#11P我在所有人之中，\x01",
            "应该算是欲望很强的那类。\x02\x03",

            "但如果究其本质，\x01",
            "其实所有人都是相同的。\x02\x03",

            "#11604F剧团里的各位全都一样……\x02\x01",

            "#11600F莉夏当然也是一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0458
    ChrTalk(
        0x101,
        "#00001F#6P伊莉娅小姐……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xB,
        (
            "#11602F#11P呵呵，如果你们能见到那孩子，\x01",
            "可以帮我转达几句话吗？\x02\x03",

            "#11604F『对你来说，\x01",
            "  什么才是最重要的？』\x02\x03",

            "『面对那重要之物，\x01",
            "  你能不为之努力吗？』\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        (
            "#00004F#6P……我明白了。\x02\x03",

            "#00000F只要见到莉夏，\x01",
            "我们一定会转达您这番话的。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xB,
        "#11609F#11P嗯，那就拜托你们啦！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21225, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -100000, 0, -5000, 90)
    OP_69(0xFF, 0x0)
    SetMapObjFlags(0x6, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrSubChip(0xB, 0x0)
    OP_74(0x5, 0x1E)
    SetScenarioFlags(0x1A0, 6)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_60_A698 end

    def Function_61_B3F6(): pass

    label("Function_61_B3F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-16500, 1000, 30000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -17100, 0, 26000, 0)
    SetChrPos(0x103, -15900, 0, 26000, 0)
    SetChrPos(0x105, -16500, 0, 25000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)

    def lambda_B492():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B492)

    def lambda_B4A7():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B4A7)
    Sleep(50)

    def lambda_B4BF():
        OP_9B(0x0, 0xFE, 0x0, 0x109A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B4BF)
    Sleep(50)
    Sleep(50)
    Sleep(100)

    def lambda_B4DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B4DD)

    def lambda_B4EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B4EE)
    Sleep(400)

    def lambda_B502():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B502)
    Sleep(800)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x105, 1)
    OP_0D()

    def lambda_B529():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B529)
    Sleep(50)

    def lambda_B539():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B539)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    #C0462
    ChrTalk(
        0x105,
        (
            "#10404F#12P哈哈……\x01",
            "真是太了不起了。\x02\x03",

            "#10402F不愧是\x01",
            "『炎之舞姬』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        (
            "#00204F#5P……简直就是舞台上的\x01",
            "『太阳舞姬』本人。\x02\x03",

            "#00208F我被带到这里之后，\x01",
            "和她聊过好几次天……\x02\x03",

            "#00202F她和塞茜尔小姐\x01",
            "让我获得了很多勇气。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#00004F#6P是吗……\x02\x03",

            "#00008F……真希望能想办法\x01",
            "找到莉夏。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x105,
        (
            "#10406F#12P这就只能\x01",
            "看女神的安排了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 1)), scpexpr(EXPR_END)), "loc_B70A")

    #C0466
    ChrTalk(
        0x103,
        (
            "#00202F#5P叫上芙兰小姐，\x01",
            "我们差不多也该回去了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        "#00000F#6P嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_B777")

    label("loc_B70A")


    #C0468
    ChrTalk(
        0x103,
        (
            "#00202F#5P要不要也去看望一下\x01",
            "多诺邦警督呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        "#00000F#6P嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -16500, 0, 30000, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_B777")

    Return()

    # Function_61_B3F6 end

    def Function_62_B778(): pass

    label("Function_62_B778")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-52720, 1000, -50000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -49020, 0, -49670, 270)
    SetChrPos(0x103, -49020, 0, -49670, 270)
    SetChrPos(0x105, -49020, 0, -49670, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(808, 0, 80, 0)
    Sleep(300)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x16, 0x2)
    SetChrSubChip(0x9, 0x1)

    #C0470
    ChrTalk(
        0x16,
        "#6P哎呀，到检查体温的时间了吗？\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x9,
        "请进吧。\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        "#6P……打扰了。\x02",
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    OP_74(0x4, 0xF)
    OP_71(0x4, 0x0, 0x14, 0x0, 0x0)
    Sleep(700)
    OP_68(-54130, 1000, -49290, 3000)
    MoveCamera(45, 22, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(20740, 3000)

    def lambda_B8DF():
        OP_95(0x101, -53180, 0, -49830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B8DF)

    def lambda_B8F9():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B8F9)
    Sleep(500)

    def lambda_B90D():
        OP_95(0x105, -53100, 0, -50830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B90D)

    def lambda_B927():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B927)
    Sleep(600)

    def lambda_B93B():
        OP_95(0x103, -51840, 50, -50110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B93B)

    def lambda_B955():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B955)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x10E, 0x1F4)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x10E, 0x1F4)
    BeginChrThread(0x1A, 1, 0, 48)
    OP_71(0x4, 0x14, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0473
    ChrTalk(
        0x9,
        (
            "哦哦，你们……\x01",
            "这不是支援科的人吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        (
            "#00000F#11P哈哈，好久不见了，\x01",
            "多诺邦警督。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x105,
        (
            "#10405F#12P哎呀，那位美人是谁呢？\x02\x03",

            "#10409F呵呵，我们是不是打扰\x01",
            "二位的幽会了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0476
    ChrTalk(
        0x9,
        (
            "才刚刚重逢，\x01",
            "你怎么就开始胡说八道……\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        "#00006F#11P瓦吉，我说你啊……\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x103,
        (
            "#00202F#2P这位是警督的妻子，\x01",
            "法拉女士。\x02\x03",

            "不久前来这里探望警督，\x01",
            "然后就待在这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x16,
        (
            "#6P呵呵呵，初次见面。\x01",
            "我丈夫承蒙各位照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x16,
        (
            "#6P我经常听我丈夫和缇欧小姐\x01",
            "谈起有关各位的传闻，\x01",
            "感觉你们都是很有趣的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x105,
        "#10402F#12P呵呵，感谢您的夸奖。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x101,
        (
            "#00006F#11P（那好像并不是\x01",
            "  夸奖吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x9,
        (
            "我想你们肯定有不少话想说……但在那之前，\x01",
            "可以给我讲讲事情的整个经过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        "#00000F#11P好的，我明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x18, -56080, 0, -50980, 0)
    SetChrPos(0x16, -57180, 0, -49690, 90)
    SetChrPos(0x101, -56170, 0, -50280, 0)
    SetChrPos(0x105, -54970, 0, -50480, 0)
    SetChrPos(0x103, -54150, 0, -49250, 315)
    OP_68(-55150, 1000, -48820, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20280, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    #C0485
    ChrTalk(
        0x9,
        (
            "#1P唔……事态比我想象的\x01",
            "还要严重啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x9,
        (
            "#1P另外，从你们所说的情况来看，\x01",
            "我还是不要向总部报告自己\x01",
            "曾在这里遇到过你们为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#00000F#12P是的，您能保密，那自然再好不过。\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x105,
        (
            "#10406F#12P我倒是无所谓，\x01",
            "但罗伊德正在被通缉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x16,
        "#6P嗯……\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        (
            "#00001F#12P先、先不说这些了。\x01",
            "……警督，克洛斯贝尔市内的\x01",
            "状况如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x9,
        (
            "#1P这个嘛，我也是听前来\x01",
            "探视的雷蒙德说的……\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x9,
        (
            "#1P听说克洛斯贝尔警察局\x01",
            "已经完全成为国防军的\x01",
            "下层组织了。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x9,
        (
            "#1P工作内容虽然没有改变，\x01",
            "但现在尽是被派去\x01",
            "处理市内的各种杂事。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x103,
        "#00203F果然如此……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x105,
        (
            "#10406F#12P考虑到现状，\x01",
            "这也是无可奈何的。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x101,
        (
            "#00001F#12P但是……那种体制\x01",
            "应该会引起大家的反抗吧？\x02\x03",

            "#00003F皮埃尔副局长也许会忍下来，\x01",
            "但赛尔盖科长和达德利搜查官\x01",
            "应该不会默默服从……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x9,
        "#1P嗯，这些话只能在这里说……\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x9,
        (
            "#1P据说赛尔盖、达德利，\x01",
            "还有包括雷蒙德在内的警官们\x01",
            "已经开始暗中行动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0499
    ChrTalk(
        0x103,
        "#00205F科长他们吗……？\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x9,
        "#1P当然，也只是在暗中隐秘行动而已。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x9,
        (
            "#1P他们目前正在寻找机会，\x01",
            "试图找出打破现状的\x01",
            "方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x105,
        (
            "#10402F#12P看来大家都没有\x01",
            "就此放弃呢。\x02\x03",

            "#10404F呵呵，好像看到点希望了。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x101,
        (
            "#00000F#12P是啊，虽说现在很难\x01",
            "与他们接触上……\x01",
            "但市内的事情交给他们就可以了。\x02\x03",

            "#00003F我们就以自己的方式，\x01",
            "继续去寻找打破现状的\x01",
            "方法吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x9,
        "#1P这才是特别任务支援科啊。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x9,
        (
            "#1P接下来的路恐怕会相当艰难，\x01",
            "但你们一定要多加努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x9,
        (
            "#1P等我复职之后，马上就会\x01",
            "和赛尔盖他们会合……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x16,
        (
            "#6P哎呀，你可真是的……\x01",
            "先把事情交给这几个孩子和雷蒙德他们就好了，\x01",
            "你得先把身体休养好才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x16,
        (
            "#6P在你完全康复之前，\x01",
            "我绝对不会让你跑出去勉强自己的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0509
    ChrTalk(
        0x9,
        "#1P唔、唔……我知道了。\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        (
            "#00000F#12P（哈哈……\x01",
            "  想说的话被她抢先说了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x103,
        (
            "#00200F（警督在妻子面前\x01",
            "  也是一点办法都没有呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x105,
        (
            "#10404F#12P（呵呵，有位这么好的妻子，\x01",
            "  警督还真是幸福。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x18, -55700, 0, -49800, 0)
    SetChrPos(0x16, -55700, 100, -49800, 0)
    SetChrChipByIndex(0x16, 0x10)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrSubChip(0x9, 0x0)
    OP_74(0x4, 0x1E)
    SetChrPos(0x0, -53970, 0, -49930, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A1, 0)
    EventEnd(0x5)
    Return()

    # Function_62_B778 end

    def Function_63_C46C(): pass

    label("Function_63_C46C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-16120, 1000, 8160, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21280, 0)
    SetChrPos(0x101, -19090, 0, 8790, 90)
    SetChrPos(0x103, -19090, 0, 8790, 90)
    SetChrPos(0x105, -19090, 0, 8790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x15)
    SetChrPos(0x8, -840, 0, 9000, 270)
    OP_4B(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_68(-14770, 1000, 8790, 5000)
    MoveCamera(45, 28, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(19350, 5000)

    def lambda_C559():
        OP_95(0x101, -15360, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C559)

    def lambda_C573():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C573)
    Sleep(600)

    def lambda_C587():
        OP_95(0x103, -14800, 0, 7940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C587)

    def lambda_C5A1():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C5A1)
    Sleep(600)

    def lambda_C5B5():
        OP_95(0x105, -14980, 0, 10240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C5B5)

    def lambda_C5CF():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C5CF)
    Sleep(1200)
    Sound(107, 0, 100, 0)

    #C0513
    ChrTalk(
        0x8,
        "啊，各位～\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_C63F():

        label("loc_C63F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C63F")

    QueueWorkItem2(0x101, 2, lambda_C63F)

    def lambda_C651():

        label("loc_C651")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C651")

    QueueWorkItem2(0x105, 2, lambda_C651)

    def lambda_C663():

        label("loc_C663")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C663")

    QueueWorkItem2(0x103, 2, lambda_C663)
    OP_95(0x8, -13480, 0, 9000, 3000, 0x0)
    SetChrSubChip(0x8, 0x0)

    #C0514
    ChrTalk(
        0x101,
        (
            "#00000F#6P芙兰……\x01",
            "你已经整理好行李了吗？\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0515
    AnonymousTalk(
        0x8,
        "嗯嗯，已经整理好了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x8, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    OP_93(0x8, 0x1E, 0x1F4)
    OP_93(0x8, 0x96, 0x1F4)
    OP_93(0x8, 0x10E, 0x1F4)
    OP_64(0x8)
    Sleep(500)

    #C0516
    ChrTalk(
        0x103,
        (
            "#00202F#6P好久没见过芙兰小姐\x01",
            "穿上制服的样子了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x8,
        (
            "#01909F#11P呵呵，我自己也是一样啊～\x02\x03",

            "#01900F各位已经探望过\x01",
            "多诺邦警督了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        (
            "#00004F#6P嗯，刚刚聊完。\x02\x03",

            "#00000F芙兰也是来看警督的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x8,
        (
            "#01904F#11P是的，我打算在\x01",
            "出院之前，和大家\x01",
            "都打声招呼。\x02\x03",

            "#01902F尤其是警督，他在那么危险的\x01",
            "时刻救了我，\x01",
            "我必须要再次向他郑重道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        (
            "#00002F#6P哈哈，是吗，\x01",
            "那就等下再见吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        "#01909F#11P好的，稍后见～！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    OP_68(-14920, 1000, 8940, 3000)
    BeginChrThread(0x105, 1, 0, 64)
    BeginChrThread(0x101, 1, 0, 65)
    Sleep(500)
    BeginChrThread(0x1A, 1, 0, 66)
    OP_95(0x8, -18060, 0, 8900, 2500, 0x1)

    def lambda_C985():
        OP_95(0xFE, -19090, 0, 8900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C985)

    def lambda_C99F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C99F)
    WaitChrThread(0x8, 2)
    Sleep(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_C9CB():
        OP_95(0xFE, -16200, 0, 8800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C9CB)
    Sleep(50)

    def lambda_C9E8():
        OP_95(0xFE, -14800, 0, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C9E8)
    Sleep(50)

    def lambda_CA05():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CA05)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    SetScenarioFlags(0x1A1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 7)), scpexpr(EXPR_END)), "loc_CA93")

    #C0522
    ChrTalk(
        0x105,
        (
            "#10402F#5P等她跟大家打完招呼，\x01",
            "我们就回梅尔卡瓦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x101,
        "#00000F#6P嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_CB15")

    label("loc_CA93")


    #C0524
    ChrTalk(
        0x105,
        (
            "#10402F#5P接下来，我们就去\x01",
            "探望一下\x01",
            "伊莉娅小姐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        "#00000F#6P嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x1000)
    SetChrPos(0x0, -15000, 0, 9000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_CB15")

    Return()

    # Function_63_C46C end

    def Function_64_CB16(): pass

    label("Function_64_CB16")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xE1, 0x320, 0x3E8, 0x0)

    def lambda_CB31():

        label("loc_CB31")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_CB31")

    QueueWorkItem2(0xFE, 2, lambda_CB31)
    Return()

    # Function_64_CB16 end

    def Function_65_CB3F(): pass

    label("Function_65_CB3F")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x1, 0xFE, 0xA0, 0x5DC, 0x3E8, 0x0)

    def lambda_CB5A():

        label("loc_CB5A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_CB5A")

    QueueWorkItem2(0xFE, 2, lambda_CB5A)
    Return()

    # Function_65_CB3F end

    def Function_66_CB68(): pass

    label("Function_66_CB68")

    Sleep(1850)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    Return()

    # Function_66_CB68 end

    def Function_67_CB7B(): pass

    label("Function_67_CB7B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -99220, 0, 55110, 315)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -99820, 0, 55990, 135)
    SetChrFlags(0xD, 0x8000)
    SetChrSubChip(0xD, 0x2)
    OP_68(-99000, 1000, 56020, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    SetChrPos(0x101, -100000, 50, 48000, 0)
    SetChrPos(0x102, -100000, 50, 48000, 0)
    SetChrPos(0x103, -100000, 50, 48000, 0)
    SetChrPos(0x104, -100000, 50, 48000, 0)
    SetChrPos(0x109, -100000, 50, 48000, 0)
    SetChrPos(0x105, -100000, 50, 48000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xF, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0526
    ChrTalk(
        0xF,
        (
            "#01400F……赛尔盖先生，听说您接下了\x01",
            "调查『幻兽』的任务。\x02\x03",

            "#01403F我身为一名游击士，\x01",
            "本应去调查并消灭它们……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x19,
        (
            "#12P#01000F你不必那么介意。\x02\x03",

            "#01003F关于幻兽的事情，我们和协会\x01",
            "分工合作，完全可以应付。\x02\x03",

            "#01000F总之，今天就交给\x01",
            "那些小家伙去负责吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xF,
        "#01408F可是……\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x19,
        (
            "#12P#01002F那些小家伙已经成长了不少，\x01",
            "你不必太过担心。\x02\x03",

            "#01004F而且你平时也没什么\x01",
            "时间来探望小滴吧？\x02\x03",

            "#01002F在这种时候\x01",
            "陪在女儿的身边，\x01",
            "可是老爸的职责哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xF,
        "#01403F……感激不尽。\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xD,
        (
            "#11P#11209F呵呵……\x01",
            "真是太谢谢您了，科长先生。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 160, -1, -1)
    SetChrName("罗伊德的声音")

    #A0532
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……打扰了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_CF36():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_CF36)
    Sleep(50)
    OP_93(0x19, 0xB4, 0x1F4)
    OP_68(-98690, 1100, 54300, 4000)
    MoveCamera(40, 15, 0, 4000)
    OP_6E(440, 4000)
    SetCameraDistance(20840, 4000)
    Sound(107, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 68)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 69)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 70)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 71)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 72)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 73)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)
    Sound(107, 0, 100, 0)

    #C0533
    ChrTalk(
        0xF,
        "#01405F是你们……\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x19,
        (
            "#01005F怎么，你们也来了啊。\x02\x03",

            "#01006F真是的，我不是说了吗，\x01",
            "现在这么忙碌，我一个人\x01",
            "来探病就行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#12P#00012F对、对不起，科长。\x02\x03",

            "#00000F但我们实在是\x01",
            "很在意小滴现在的\x01",
            "状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xD,
        (
            "#5P#11202F呵呵……\x01",
            "谢谢大家特地来探望我。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0537
    ChrTalk(
        0x102,
        "#6P#00105F小滴睁着眼睛……\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x109,
        (
            "#12P#10105F难道你已经……\x01",
            "能看见了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xD,
        "#5P#11208F……不，很遗憾，还是看不见。\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xF,
        (
            "#01403F……在这次的手术中，\x01",
            "执刀医生赛兰德医师\x01",
            "已经尽其所能，做到最好了。\x02\x03",

            "#01400F虽然手术并非完全没有成效……\x01",
            "但还是没能使小滴复明。\x02\x03",

            "#01408F她现在的视力仅仅恢复到了\x01",
            "可以感知四周光芒的地步。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x104,
        "#12P#00303F是吗……\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x103,
        "#12P#00208F该说什么才好呢……\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xD,
        (
            "#5P#11200F呵呵，请不用担心，\x01",
            "我没事的。\x02\x03",

            "#11202F对了，爸爸……\x01",
            "我想跟大家一起到屋顶去。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)

    #C0544
    ChrTalk(
        0x19,
        (
            "#6P#01002F啊，好提议。\x02\x03",

            "#01004F一个病房里挤进这么多人\x01",
            "也不大好，而且我也想\x01",
            "呼吸一下新鲜空气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        (
            "#12P#00005F可、可是，\x01",
            "你刚做完手术不久，\x01",
            "最好别太勉强自己活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xF,
        (
            "#01403F……不，据医生说，\x01",
            "只要不长时间处于强光之下，\x01",
            "就不会产生什么负面影响。\x02\x03",

            "#01400F像今天这种天气，\x01",
            "出去一会应该没什么问题。\x02\x03",

            "#01403F……我去向医生申请一下。\x01",
            "不好意思，麻烦你们帮小滴\x01",
            "准备一下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D4A9():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_D4A9)

    def lambda_D4C3():

        label("loc_D4C3")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_D4C3")

    QueueWorkItem2(0x19, 2, lambda_D4C3)

    def lambda_D4D5():

        label("loc_D4D5")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_D4D5")

    QueueWorkItem2(0x101, 2, lambda_D4D5)

    def lambda_D4E7():

        label("loc_D4E7")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_D4E7")

    QueueWorkItem2(0x102, 2, lambda_D4E7)

    def lambda_D4F9():

        label("loc_D4F9")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_D4F9")

    QueueWorkItem2(0x103, 2, lambda_D4F9)

    def lambda_D50B():

        label("loc_D50B")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_D50B")

    QueueWorkItem2(0x104, 2, lambda_D50B)

    def lambda_D51D():

        label("loc_D51D")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_D51D")

    QueueWorkItem2(0x109, 2, lambda_D51D)

    def lambda_D52F():

        label("loc_D52F")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_D52F")

    QueueWorkItem2(0x105, 2, lambda_D52F)
    BeginChrThread(0x1A, 1, 0, 74)
    WaitChrThread(0xF, 1)

    def lambda_D54B():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_D54B)

    def lambda_D565():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_D565)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xF, 2)
    SetChrFlags(0xF, 0x80)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)

    #C0547
    ChrTalk(
        0x102,
        "#00105F啊……\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x105,
        (
            "#12P#10304F哎呀呀，大名鼎鼎的『风之剑圣』\x01",
            "还真是宠爱女儿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xD,
        (
            "#5P#11209F爸爸平时一直都\x01",
            "非常温柔。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D61D():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D61D)
    Sleep(50)

    def lambda_D62D():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D62D)
    Sleep(50)

    def lambda_D63D():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D63D)
    Sleep(50)

    def lambda_D64D():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D64D)
    Sleep(50)

    def lambda_D65D():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D65D)
    Sleep(50)

    def lambda_D66D():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D66D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    TurnDirection(0x19, 0x101, 500)

    #C0550
    ChrTalk(
        0x19,
        (
            "#01004F唔，既然如此，\x01",
            "我们就陪陪他们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        "#12P#00000F嗯……说的也是。\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xD,
        "#5P#11202F呵呵，麻烦大家了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t1600", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_67_CB7B end

    def Function_68_D71D(): pass

    label("Function_68_D71D")


    def lambda_D722():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D722)

    def lambda_D73C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D73C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_D755():
        OP_95(0xFE, -99000, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D755)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_68_D71D end

    def Function_69_D776(): pass

    label("Function_69_D776")


    def lambda_D77B():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D77B)

    def lambda_D795():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D795)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_D7AE():
        OP_95(0xFE, -100940, 50, 53000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7AE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_69_D776 end

    def Function_70_D7CF(): pass

    label("Function_70_D7CF")


    def lambda_D7D4():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7D4)

    def lambda_D7EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D7EE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_D807():
        OP_95(0xFE, -98340, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D807)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_70_D7CF end

    def Function_71_D828(): pass

    label("Function_71_D828")


    def lambda_D82D():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D82D)

    def lambda_D847():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D847)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_D860():
        OP_95(0xFE, -100740, 0, 51800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D860)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_71_D828 end

    def Function_72_D881(): pass

    label("Function_72_D881")


    def lambda_D886():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D886)

    def lambda_D8A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D8A0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_D8B9():
        OP_95(0xFE, -99240, 0, 50800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D8B9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_72_D881 end

    def Function_73_D8DA(): pass

    label("Function_73_D8DA")


    def lambda_D8DF():
        OP_95(0xFE, -100000, 50, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D8DF)

    def lambda_D8F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D8F9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_D912():
        OP_95(0xFE, -100740, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D912)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_73_D8DA end

    def Function_74_D933(): pass

    label("Function_74_D933")

    Sleep(2600)
    Sound(107, 0, 100, 0)
    Sleep(1100)
    Sound(107, 0, 100, 0)
    Return()

    # Function_74_D933 end

    def Function_75_D946(): pass

    label("Function_75_D946")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -99220, 0, 55110, 315)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -99820, 0, 55990, 135)
    SetChrFlags(0xD, 0x8000)
    OP_68(-98690, 1100, 54300, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20840, 0)
    SetChrPos(0x101, -99000, 50, 53000, 0)
    SetChrPos(0x102, -100940, 50, 53000, 45)
    SetChrPos(0x103, -100740, 0, 51800, 45)
    SetChrPos(0x104, -98340, 0, 52200, 0)
    SetChrPos(0x109, -100740, 0, 50600, 0)
    SetChrPos(0x105, -99240, 0, 50800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xF, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0553
    ChrTalk(
        0x19,
        (
            "#12P#01002F……那我\x01",
            "就先回\x01",
            "支援科了。\x02\x03",

            "#01004F亚里欧斯，你今天就\x01",
            "好好待在小滴身边吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xF,
        "#01403F……嗯，好的。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x101,
        "#12P#00000F您辛苦了，科长。\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)

    #C0556
    ChrTalk(
        0x19,
        (
            "#01005F嗯，你们就继续调查\x01",
            "『幻兽』吧。\x02\x03",

            "#01002F趁着『风之剑圣』无暇分身之机，\x01",
            "不妨多累积一些成绩。\x02",
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

    #C0557
    ChrTalk(
        0x102,
        "#6P#00106F科、科长……\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x19,
        "#01004F呵呵，我先走了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)

    #C0559
    ChrTalk(
        0xD,
        (
            "#5P#11202F啊……\x01",
            "谢谢您来看我。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xD, 500)
    Sleep(500)
    OP_93(0x19, 0xB4, 0x1F4)

    def lambda_DC62():
        OP_95(0xFE, -99820, 0, 54000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_DC62)
    WaitChrThread(0x19, 1)

    def lambda_DC80():
        OP_95(0xFE, -100000, 50, 49000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_DC80)

    def lambda_DC9A():

        label("loc_DC9A")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_DC9A")

    QueueWorkItem2(0xF, 2, lambda_DC9A)

    def lambda_DCAC():

        label("loc_DCAC")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_DCAC")

    QueueWorkItem2(0x101, 2, lambda_DCAC)

    def lambda_DCBE():

        label("loc_DCBE")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_DCBE")

    QueueWorkItem2(0x102, 2, lambda_DCBE)

    def lambda_DCD0():

        label("loc_DCD0")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_DCD0")

    QueueWorkItem2(0x103, 2, lambda_DCD0)

    def lambda_DCE2():

        label("loc_DCE2")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_DCE2")

    QueueWorkItem2(0x104, 2, lambda_DCE2)

    def lambda_DCF4():

        label("loc_DCF4")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_DCF4")

    QueueWorkItem2(0x109, 2, lambda_DCF4)

    def lambda_DD06():

        label("loc_DD06")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_DD06")

    QueueWorkItem2(0x105, 2, lambda_DD06)
    Sleep(1500)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x19, 1)

    def lambda_DD25():
        OP_95(0xFE, -100000, 50, 47000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_DD25)

    def lambda_DD3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_DD3F)
    Sleep(100)
    Sound(107, 0, 100, 0)
    WaitChrThread(0x19, 1)
    WaitChrThread(0x19, 2)
    SetChrFlags(0x19, 0x80)
    EndChrThread(0xF, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)

    #C0560
    ChrTalk(
        0x104,
        (
            "#5P#00306F哎呀呀，竟然当着\x01",
            "『风之剑圣』的面说出那种话。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x105,
        "#11P#10300F呵呵，科长一贯如此呢。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xF,
        (
            "#01402F呵呵，从我还在\x01",
            "当警察的时候，\x01",
            "他就是一名优秀的上司。\x02\x03",

            "#01403F……『幻兽』的调查工作，\x01",
            "就拜托你们了。\x02\x03",

            "#01400F我明天就会返回协会，\x01",
            "并参与调查工作，在我回去之前，\x01",
            "就拜托你们协助斯克特他们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DEB0():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DEB0)
    Sleep(50)

    def lambda_DEC0():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DEC0)
    Sleep(50)

    def lambda_DED0():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DED0)
    Sleep(50)

    def lambda_DEE0():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DEE0)
    Sleep(50)

    def lambda_DEF0():
        TurnDirection(0x105, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DEF0)
    Sleep(50)

    def lambda_DF00():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DF00)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0563
    ChrTalk(
        0x103,
        "#12P#00200F好的，我们一定会尽力而为。\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xD,
        (
            "#5P#11202F非常感谢\x01",
            "大家来看我。\x02\x03",

            "#11209F能和各位聊这么久，我很开心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DF9A():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DF9A)
    Sleep(50)

    def lambda_DFAA():
        TurnDirection(0x102, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DFAA)
    Sleep(50)

    def lambda_DFBA():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DFBA)
    Sleep(50)

    def lambda_DFCA():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DFCA)
    Sleep(50)

    def lambda_DFDA():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DFDA)
    Sleep(50)

    def lambda_DFEA():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DFEA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0565
    ChrTalk(
        0x109,
        "#12P#10100F不要客气，我们也很开心哦。\x02",
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x101,
        "#12P#00000F我们还会再来的，你就安心休养吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x170, 3)
    SetChrPos(0xF, -99220, 0, 56180, 90)
    OP_4C(0xF, 0xFF)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -100000, 50, 53000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_75_D946 end

    def Function_76_E0BB(): pass

    label("Function_76_E0BB")

    EventBegin(0x0)
    Fade(500)
    OP_68(-99000, 900, 55030, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -100000, 50, 48000, 0)
    SetChrPos(0x102, -100000, 50, 48000, 0)
    SetChrPos(0x103, -100000, 50, 48000, 0)
    SetChrPos(0x104, -100000, 50, 48000, 0)
    SetChrPos(0x109, -100000, 50, 48000, 0)
    SetChrPos(0x105, -100000, 50, 48000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sound(107, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 68)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 69)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 70)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 71)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 72)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 73)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)

    #C0567
    ChrTalk(
        0x101,
        (
            "#00005F咦，这里应该是小滴的\x01",
            "病房啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x102,
        "#6P#00100F说不定她到外面去了。\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x103,
        (
            "#6P#00200F但我们并没有在这栋楼里\x01",
            "看见她啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x104,
        "#12P#00300F如果很在意，就去找找看吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x18E, 7)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -100000, 50, 52410, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_76_E0BB end

    def Function_77_E2DC(): pass

    label("Function_77_E2DC")

    StopBGM(0xBB8)

    #C0571
    ChrTalk(
        0xB,
        "#11603F对了——\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    Sleep(500)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    #C0572
    ChrTalk(
        0xB,
        (
            "#11602F……站在外面的某人\x01",
            "好像还是没有进来的意思啊？\x02",
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
    Sleep(50)
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Fade(500)
    EventBegin(0x0)
    OP_68(-98780, 1000, -4030, 0)
    MoveCamera(71, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18860, 0)
    SetChrPos(0x101, -99960, 0, -5580, 90)
    SetChrPos(0x102, -99960, 0, -6900, 90)
    SetChrPos(0x103, -100870, 0, -5000, 90)
    SetChrPos(0x104, -100870, 0, -6300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E478")
    SetChrPos(0x109, -100670, 0, -7660, 90)
    Jump("loc_E4BF")

    label("loc_E478")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E49E")
    SetChrPos(0x105, -100670, 0, -7660, 90)
    Jump("loc_E4BF")

    label("loc_E49E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E4BF")
    SetChrPos(0x10A, -100670, 0, -7660, 90)

    label("loc_E4BF")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0573
    ChrTalk(
        0x101,
        "#6P#00005F伊、伊莉娅小姐……？\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x102,
        "#12P#00105F您在说什么呢……\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xB,
        (
            "#11P#11604F呵呵，虽然不知道是谁，\x01",
            "但似乎是个相当害羞的孩子呢。\x02\x03",

            "#11609F我猜，应该是个性格内敛，\x01",
            "但却有着任性的一面，而且还拥有\x01",
            "一副好身材的人吧⊥\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0576
    ChrTalk(
        0x104,
        "#12P#00306F（这……）\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x103,
        "#6P#00206F（完全察觉到了啊。）\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("莉夏")

    #A0578
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10708F#3C#40W#2S…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0579
    ChrTalk(
        0xB,
        (
            "#11P#11603F……虽然不知道你是谁，\x01",
            "但我已经开始做复健运动了。\x02\x03",

            "#11601F如果老是偷懒不去练习，\x01",
            "很快就会被我追上并远远抛下哦。\x02\x03",

            "#11604F如果不想被我甩在后面，\x01",
            "就赶快把麻烦事都解决掉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("莉夏")

    #A0580
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10717F#3C#40W#2S……………唔…………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0581
    ChrTalk(
        0xB,
        (
            "#11P#11604F还有，记得多加小心。\x02\x03",

            "#11600F不管你有多强，\x01",
            "也要记住自己是个女人。\x02\x03",

            "#11603F有一种强大，只有女性才能展示出来，\x01",
            "就像我们的舞剧一样……\x02\x03",

            "#11600F那份强大一定会保护你的。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 0, -1, -1)
    SetChrName("莉夏")

    #A0582
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10715F#3C#40W#2S…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0583
    ChrTalk(
        0x102,
        "#12P#00102F伊莉娅小姐……\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x101,
        "#6P#00002F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xB,
        (
            "#5P#11604F呵呵，耽搁了你们一些时间呢。\x02\x03",

            "#11600F警察弟弟，你们也要多加注意，\x01",
            "千万别让塞茜尔悲伤哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x101,
        "#6P#00000F……是！\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x104,
        "#12P#00300F明白了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_68(-14240, 1000, 29970, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20470, 0)
    AddParty(0x5, 0xFF, 0xFF)
    SetChrChipPat(0x5, 0x1, 0x20)
    ClearScenarioFlags(0x2, 3)
    OP_49()
    SetChrPos(0x106, -12930, 0, 29900, 90)
    BeginChrThread(0x106, 1, 0, 78)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 1, 0, 79)
    WaitChrThread(0x101, 1)
    Sleep(600)
    BeginChrThread(0x102, 1, 0, 79)
    WaitChrThread(0x102, 1)
    Sleep(600)
    BeginChrThread(0x103, 1, 0, 79)
    WaitChrThread(0x103, 1)
    Sleep(600)
    BeginChrThread(0x104, 1, 0, 79)
    WaitChrThread(0x104, 1)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAAD")
    BeginChrThread(0x109, 1, 0, 79)
    WaitChrThread(0x109, 1)
    Jump("loc_EAE6")

    label("loc_EAAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EACC")
    BeginChrThread(0x105, 1, 0, 79)
    WaitChrThread(0x105, 1)
    Jump("loc_EAE6")

    label("loc_EACC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAE6")
    BeginChrThread(0x10A, 1, 0, 79)
    WaitChrThread(0x10A, 1)

    label("loc_EAE6")

    Sleep(2500)
    EndChrThread(0x106, 0x1)
    Sound(107, 0, 100, 0)

    #C0588
    ChrTalk(
        0x106,
        "#10715F#40W………………………………\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x101,
        (
            "#6P#00006F那个……对不起。\x02\x03",

            "#00008F完全没想到\x01",
            "会被她发现……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x104,
        (
            "#6P#00302F莉夏当时明明已经把\x01",
            "气息隐藏起来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x106,
        (
            "#10710F#30W呵呵……\x01",
            "因为伊莉娅小姐是个天才啊……\x02\x03",

            "#10704F#30W只是听见一点轻微的呼吸声和脚步声，\x01",
            "她就立刻察觉到了……\x02\x03",

            "在舞台上互相配合的时候，\x01",
            "她也经常凭脚步声辨人……\x02\x03",

            "#10716F#30W但是……在舞台之外的地方，\x01",
            "她明明是个粗枝大叶又怕麻烦的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        "#6P#00002F是吗……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x103,
        (
            "#6P#00204F不愧是\x01",
            "伊莉娅小姐……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED09")

    #C0594
    ChrTalk(
        0x109,
        (
            "#6P#10109F呵呵……\x01",
            "不过……真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED86")

    label("loc_ED09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED4D")

    #C0595
    ChrTalk(
        0x105,
        (
            "#6P#10409F呵呵……\x01",
            "她总能让人大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED86")

    label("loc_ED4D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED86")

    #C0596
    ChrTalk(
        0x10A,
        (
            "#6P#00602F呼……\x01",
            "真不愧是伊莉娅啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED86")

    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)
    OP_93(0x106, 0x10E, 0x1F4)

    #C0597
    ChrTalk(
        0x106,
        (
            "#10704F这样一来，\x01",
            "我的决心就更加坚定了。\x02\x03",

            "#10702F我们出发吧，各位……！\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        "#6P#00000F好……！\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x102,
        "#6P#00100F嗯……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1AD, 0)
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    BeginChrThread(0x1A, 1, 0, 85)
    SetChrPos(0x0, -16360, 0, 29440, 0)
    EventEnd(0x5)
    TalkEnd(0xFE)
    Return()

    # Function_77_E2DC end

    def Function_78_EE6A(): pass

    label("Function_78_EE6A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEA6")
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(500)
    OP_A6(0x106, 0x0, 0x1E, 0x190, 0x7D0)
    Sleep(800)
    Jump("Function_78_EE6A")

    label("loc_EEA6")

    Return()

    # Function_78_EE6A end

    def Function_79_EEA7(): pass

    label("Function_79_EEA7")

    SetChrPos(0xFE, -16470, 0, 25770, 0)

    def lambda_EEBD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_EEBD)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEED")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 80)
    Jump("loc_EF78")

    label("loc_EEED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF11")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 81)
    Jump("loc_EF78")

    label("loc_EF11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF35")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 82)
    Jump("loc_EF78")

    label("loc_EF35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF59")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 83)
    Jump("loc_EF78")

    label("loc_EF59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF78")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 84)

    label("loc_EF78")

    Return()

    # Function_79_EEA7 end

    def Function_80_EF79(): pass

    label("Function_80_EF79")

    OP_95(0xFE, -16340, 0, 28470, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 29900, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_80_EF79 end

    def Function_81_EFA9(): pass

    label("Function_81_EFA9")

    OP_95(0xFE, -16360, 0, 29870, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 31030, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_81_EFA9 end

    def Function_82_EFD9(): pass

    label("Function_82_EFD9")

    OP_95(0xFE, -16400, 0, 27970, 2000, 0x0)
    OP_95(0xFE, -15140, 0, 28800, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_82_EFD9 end

    def Function_83_F009(): pass

    label("Function_83_F009")

    OP_95(0xFE, -16360, 0, 30550, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_83_F009 end

    def Function_84_F025(): pass

    label("Function_84_F025")

    OP_95(0xFE, -16360, 0, 29320, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_84_F025 end

    def Function_85_F041(): pass

    label("Function_85_F041")

    StopBGM(0x7D0)
    Sleep(2000)
    Sleep(10)
    PlayBGM("ed7563", 0)
    Return()

    # Function_85_F041 end

    def Function_86_F051(): pass

    label("Function_86_F051")

    EventBegin(0x0)
    Fade(500)
    SetChrSubChip(0xB, 0x2)
    OP_68(-98530, 900, -5100, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_F153")
    SetChrPos(0x101, -99960, 0, -5280, 90)
    SetChrPos(0x102, -99960, 0, -6600, 90)
    SetChrPos(0x103, -100870, 0, -4700, 90)
    SetChrPos(0x104, -100870, 0, -6000, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F0FD")
    SetChrPos(0x109, -100670, 0, -7360, 90)
    Jump("loc_F144")

    label("loc_F0FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F123")
    SetChrPos(0x105, -100670, 0, -7360, 90)
    Jump("loc_F144")

    label("loc_F123")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F144")
    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_F144")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_F2D0")

    label("loc_F153")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -99960, 0, -6000, 90)
    SetChrPos(0x102, -99960, 0, -4700, 90)
    SetChrPos(0x103, -99960, 0, -7360, 90)
    SetChrPos(0x104, -100870, 0, -4700, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F1CC")
    SetChrPos(0x109, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F1CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F21C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F20B")
    SetChrPos(0x105, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F21C")

    label("loc_F20B")

    SetChrPos(0x105, -100670, 0, -7360, 90)

    label("loc_F21C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F26C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F25B")
    SetChrPos(0x106, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F26C")

    label("loc_F25B")

    SetChrPos(0x106, -100670, 0, -7360, 90)

    label("loc_F26C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2BC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2AB")
    SetChrPos(0x10A, -100870, 0, -6000, 90)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F2BC")

    label("loc_F2AB")

    SetChrPos(0x10A, -100670, 0, -7360, 90)

    label("loc_F2BC")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_F2D0")

    OP_0D()

    #C0600
    ChrTalk(
        0xB,
        (
            "#11P#11600F对了，警察弟弟……\x01",
            "你可以收下这个吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0601
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39F, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0602
    ChrTalk(
        0x101,
        "#6P#00000F这是……？\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xB,
        (
            "#11P#11600F这是我第一次\x01",
            "以主角的身份站上舞台时\x01",
            "所佩戴的发饰。\x02\x03",

            "#11604F为了让自己不要忘记最初的目标，\x01",
            "我一直随身携带着它。\x02\x03",

            "#11609F呵呵，这可是狂热支持者们\x01",
            "梦寐以求的珍贵物品哦。\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4B9")
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_F4B9")

    Sleep(1000)

    #C0604
    ChrTalk(
        0x104,
        (
            "#6P#00303F（确实，有些人肯定会想要\x01",
            "  不惜重金的把它弄到手呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x101,
        (
            "#6P#00005F可、可是……\x01",
            "我们真的可以收下\x01",
            "这么贵重的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xB,
        (
            "#11P#11604F呵呵，当然，不用客气。\x01",
            "这件礼物就用来答谢你们至今为止所做的一切。\x02\x03",

            "#11600F如果愿意，就把它带走，\x01",
            "当作护身符吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x101,
        (
            "#6P#00002F……谢谢您，\x01",
            "我们一定会珍惜它的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_F60C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_F620")

    label("loc_F60C")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_F620")

    SetChrPos(0x0, -100140, 0, -6120, 90)
    SetScenarioFlags(0x1AD, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F650")
    OP_E0(0x34, 0x0)

    label("loc_F650")

    EventEnd(0x5)
    Return()

    # Function_86_F051 end

    def Function_87_F653(): pass

    label("Function_87_F653")

    EventBegin(0x1)
    Call(0, 92)
    SetChrPos(0x0, -13440, 0, 8760, 89)
    EventEnd(0x4)
    Return()

    # Function_87_F653 end

    def Function_88_F66C(): pass

    label("Function_88_F66C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F680")
    Call(0, 92)
    Jump("loc_F683")

    label("loc_F680")

    Call(0, 94)

    label("loc_F683")

    SetChrPos(0x0, -9210, 0, 13390, 180)
    EventEnd(0x4)
    Return()

    # Function_88_F66C end

    def Function_89_F697(): pass

    label("Function_89_F697")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6AB")
    Call(0, 94)
    Jump("loc_F6AE")

    label("loc_F6AB")

    Call(0, 93)

    label("loc_F6AE")

    SetChrPos(0x0, 1350, 0, 80, 89)
    EventEnd(0x4)
    Return()

    # Function_89_F697 end

    def Function_90_F6C2(): pass

    label("Function_90_F6C2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6D6")
    Call(0, 94)
    Jump("loc_F6D9")

    label("loc_F6D6")

    Call(0, 93)

    label("loc_F6D9")

    SetChrPos(0x0, -5500, 0, 12500, 225)
    EventEnd(0x4)
    Return()

    # Function_90_F6C2 end

    def Function_91_F6ED(): pass

    label("Function_91_F6ED")

    EventBegin(0x1)
    Call(0, 93)
    SetChrPos(0x0, -19350, 0, 29820, 89)
    EventEnd(0x4)
    Return()

    # Function_91_F6ED end

    def Function_92_F706(): pass

    label("Function_92_F706")


    #C0608
    ChrTalk(
        0x101,
        (
            "#00000F芙兰的病房是３０１号，\x01",
            "赶快过去看看她的状况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_92_F706 end

    def Function_93_F744(): pass

    label("Function_93_F744")


    #C0609
    ChrTalk(
        0x136,
        (
            "#01300F伊莉娅的病房是３０３号房。\x02\x03",

            "我不能陪你们太久，\x01",
            "还是赶快过去比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x101,
        "#00001F嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_93_F744 end

    def Function_94_F7B1(): pass

    label("Function_94_F7B1")


    #C0611
    ChrTalk(
        0x136,
        (
            "#01300F多诺邦警督的病房是３０２号房。\x02\x03",

            "我不能陪你们太久，\x01",
            "还是赶快过去比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x101,
        "#00000F嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Return()

    # Function_94_F7B1 end

    SaveToFile()

Try(main)
